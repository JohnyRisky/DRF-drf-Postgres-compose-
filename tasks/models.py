from django.db import models
from django.urls import reverse


class AstanaHubParticipant(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="Организация", unique=True)
    registration_data = models.DateField(blank=True, verbose_name="Дата регистрации")
    valid_to = models.DateField(blank=True, verbose_name="Дата окончания регистрации")
    company_bin = models.CharField(max_length=12, blank=True, verbose_name="БИН организации", unique=True)
    status = models.CharField(max_length=10, verbose_name="Статус")
   
    class Meta:
        verbose_name_plural = "Участники Астана ХАБ"
        ordering = ["id"]

    def __str__(self):
        return f"{self.company_name}, БИН: {self.company_bin}"


class Tasks(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(blank=True, verbose_name="Описание задачи")
    completed = models.BooleanField(default=False, verbose_name="Статус задачи")
    
    class Meta:
        verbose_name_plural = "Ваши задачи"
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse("task_pk", kwargs={"pk": self.id})
    
    def __str__(self):
        return f"{self.title[:30]}... (Completed: {'Yes' if self.completed else 'No'})"