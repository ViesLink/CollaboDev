# Generated by Django 2.0 on 2018-02-25 23:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks_completed', models.IntegerField(default=0)),
                ('associated_image', models.CharField(default='/accounts/images/default_avatar.png', max_length=1000)),
                ('gravatar_url', models.CharField(default='', max_length=1000)),
                ('gravatar_enabled', models.BooleanField(default=False)),
                ('quest', models.CharField(default='null', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=70)),
                ('task_description', models.CharField(max_length=400)),
                ('task_owner', models.CharField(max_length=15)),
                ('task_priority', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('task_open', models.BooleanField(default=True)),
                ('task_size', models.IntegerField(validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(1)])),
                ('created_by', models.CharField(max_length=20)),
                ('publish_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('deadline_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='current_task',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
