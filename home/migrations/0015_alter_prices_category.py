# Generated by Django 4.0.6 on 2022-08-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='category',
            field=models.CharField(choices=[('Pencil Drawings', 'Pencil Drawings'), ('Picture Framing', 'Picture Framing'), ('Gift Boxes', 'Gift Boxes'), ('Greeting Cards', 'Greeting Cards'), ('Training', 'Training')], max_length=30),
        ),
    ]
