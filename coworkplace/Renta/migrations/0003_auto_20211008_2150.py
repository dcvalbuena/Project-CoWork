# Generated by Django 3.2.7 on 2021-10-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renta', '0002_auto_20211008_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]