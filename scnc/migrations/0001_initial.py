# Generated by Django 5.1.7 on 2025-03-30 17:57

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cnc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, max_length=252, null=True, upload_to='cnc\\pics')),
                ('decs', tinymce.models.HTMLField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='cnc\\pics')),
                ('editor', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
