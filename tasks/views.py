from datetime import datetime
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseNotFound
from django.views.generic import ListView, DetailView
from .techpark_parser import hub_parser
from .models import Tasks, AstanaHubParticipant
from .forms import TaskFilterForm, TaskPostForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class TasksListView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    allow_empty = True
    paginate_by = 3
    login_url = '/auth/login/'
    

    def get_queryset(self):
        queryset = Tasks.objects.all()

        title = self.request.GET.get('title')
        completed = self.request.GET.get('completed')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if completed in ['true', 'false']:
            is_completed = completed == 'true'
            queryset = queryset.filter(completed=is_completed)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_title'] = 'Список задач'
        context['form'] = TaskFilterForm(self.request.GET)
        context['post_form'] = TaskPostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = self.get_context_data()
        context['post_form'] = form
        return self.render_to_response(context)
    

class TaskAddUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


@login_required
def parse_hub(request):
    participants = hub_parser()

    existing_participants = {
        p.company_bin: p
        for p in AstanaHubParticipant.objects.all()
    }

    new_objects = []

    for participant in participants:
        company_bin = participant['company_bin']
        existing = existing_participants.get(company_bin)

        if existing:
            if (
                existing.company_name != participant['company_name'] or
                existing.status != participant['status']
            ):
                existing.company_name = participant['company_name']
                existing.status = participant['status']
                existing.save()
        else:
            new_objects.append(AstanaHubParticipant(
                company_name=participant['company_name'],
                registration_data=datetime.strptime(participant['registration_date'], "%Y-%m-%d").date(),
                valid_to=datetime.strptime(participant['valid_until'], "%Y-%m-%d").date(),
                company_bin=participant['company_bin'],
                status=participant['status']
            ))

    AstanaHubParticipant.objects.bulk_create(new_objects)

    return render(request, "tasks/parser.html", {"participants": participants})


def page404(request, exception):
    return render(request, 'errors/404.html', status=404)




