# Generated by Django 5.2 on 2025-04-12 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attribute_1', models.CharField(max_length=50)),
                ('Attribute_2', models.CharField(max_length=50)),
                ('Attribute_3', models.CharField(max_length=50)),
                ('Attribute_4', models.CharField(max_length=50)),
                ('Attribute_5', models.CharField(max_length=50)),
                ('Attribute_6', models.CharField(max_length=50)),
                ('Attribute_7', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Inspection',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attribute_1', models.CharField(max_length=50)),
                ('Attribute_2', models.CharField(max_length=50)),
                ('Attribute_3', models.CharField(max_length=50)),
                ('Attribute_4', models.CharField(max_length=50)),
                ('Attribute_5', models.CharField(max_length=50)),
                ('Attribute_6', models.CharField(max_length=50)),
                ('Attribute_7', models.CharField(max_length=50)),
                ('Inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.inspection')),
            ],
            options={
                'db_table': 'Condition',
            },
        ),
    ]
