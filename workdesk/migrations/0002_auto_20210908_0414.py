# Generated by Django 3.2.6 on 2021-09-08 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workdesk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='workdesk.list'),
        ),
        migrations.AlterField(
            model_name='list',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='workdesk.project'),
        ),
        migrations.AlterField(
            model_name='member',
            name='users',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('body', models.CharField(max_length=250)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_card', to='workdesk.card')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='workdesk.member')),
            ],
        ),
    ]
