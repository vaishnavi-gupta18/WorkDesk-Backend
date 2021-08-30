# Generated by Django 3.2.6 on 2021-08-29 22:23

import ckeditor.fields
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', ckeditor.fields.RichTextField()),
                ('start_date', models.DateTimeField()),
                ('creator', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('projects', models.ManyToManyField(to='workdesk.project')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workdesk.project')),
            ],
        ),
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', ckeditor.fields.RichTextField()),
                ('start_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('creator', models.PositiveIntegerField()),
                ('assignees', models.ManyToManyField(to='workdesk.member')),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workdesk.list')),
            ],
        ),
    ]