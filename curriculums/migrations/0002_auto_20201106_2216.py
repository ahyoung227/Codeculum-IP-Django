# Generated by Django 2.2.5 on 2020-11-07 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curriculums', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curriculums', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='related_skill',
            field=models.ManyToManyField(blank=True, related_name='skill', to='curriculums.Skill'),
        ),
    ]
