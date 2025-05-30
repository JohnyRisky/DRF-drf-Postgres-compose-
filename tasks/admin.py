from django.contrib import admin
from .models import Tasks, AstanaHubParticipant


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "completed"]
    list_display_links = ["id", "description"]
    ordering = ["id", "title", "completed"]
    list_editable = ["title", "completed"]
    list_per_page = 8
    search_fields = ["title", "completed__startswith"]
    list_filter = ["completed"]

@admin.register(AstanaHubParticipant)
class HubAdmin(admin.ModelAdmin):
    list_display = ["id", "company_name", "company_bin", "status"]
    list_display_links = ["id", "company_name"]
    ordering = ["id", "company_name", "status"]
    list_editable = ["status"]
    list_per_page = 8
    search_fields = ["company_name", "status__startswith"]
    list_filter = ["status"]