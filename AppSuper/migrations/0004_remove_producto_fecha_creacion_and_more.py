# Generated by Django 4.0.4 on 2022-11-28 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppSuper', '0003_producto_fecha_creacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='producto',
            name='date_generated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
