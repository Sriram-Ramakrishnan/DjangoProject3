# Generated by Django 4.1.3 on 2022-12-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskplanner', '0007_alter_task_completed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]