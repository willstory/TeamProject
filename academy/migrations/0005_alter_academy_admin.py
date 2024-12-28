# Generated by Django 5.1.3 on 2024-12-27 10:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0004_alter_academy_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy',
            name='admin',
            field=models.OneToOneField(default='academy_admin', limit_choices_to={'member_type': 'academy_admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='academy', to=settings.AUTH_USER_MODEL),
        ),
    ]