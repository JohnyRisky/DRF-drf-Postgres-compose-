from django import forms
from .models import Tasks


class TaskFilterForm(forms.Form):

    title = forms.CharField(max_length=100, label="Название", required=False)
    completed = forms.ChoiceField(
            required=False,  
            label="Статус", 
            choices=[
                ('', 'Все'),
                ('true', 'Завершённые'),
                ('false', 'Незавершённые')
            ]
    )


class TaskPostForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__"