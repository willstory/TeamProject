# Generated by Django 5.1.3 on 2024-12-27 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_remove_category_description_academy_academy_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy',
            name='category',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='academies', to='academy.category'),
        ),
    ]