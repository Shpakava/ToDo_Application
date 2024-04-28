# Generated by Django 5.0.3 on 2024-04-07 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categories_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('done', models.BooleanField(default=False)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='Tasks.categories')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
