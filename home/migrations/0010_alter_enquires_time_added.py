# Generated by Django 4.0.6 on 2022-08-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_enquires_time_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquires',
            name='time_added',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
