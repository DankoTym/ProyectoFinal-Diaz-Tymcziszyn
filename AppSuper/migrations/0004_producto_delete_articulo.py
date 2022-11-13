# Generated by Django 4.0.4 on 2022-11-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSuper', '0003_rename_mensaje_mensaje_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Articulo',
        ),
    ]