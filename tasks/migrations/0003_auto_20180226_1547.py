# Generated by Django 2.0 on 2018-02-26 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20180226_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_owner',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
