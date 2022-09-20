# Generated by Django 4.0.6 on 2022-08-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginners', models.ImageField(upload_to='images/')),
                ('intermediate', models.ImageField(upload_to='images/')),
                ('advanced', models.ImageField(upload_to='images/')),
                ('t_video', models.FileField(upload_to='files/')),
            ],
        ),
    ]