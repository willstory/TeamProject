# Generated by Django 5.1.3 on 2024-12-27 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0008_alter_academy_academy_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academy.category'),
        ),
    ]
