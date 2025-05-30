# Generated by Django 4.2.21 on 2025-05-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_astanahubparticipant_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Статус задачи'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание задачи'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название задачи'),
        ),
    ]
