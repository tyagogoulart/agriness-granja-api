# Generated by Django 3.1.3 on 2020-11-14 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('granja', '0005_auto_20201114_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localizacao',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome da Localização'),
        ),
    ]
