# Generated by Django 4.0.6 on 2022-08-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_admin_enquires_receiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquires',
            name='time_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
