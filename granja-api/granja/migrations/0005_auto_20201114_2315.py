# Generated by Django 3.1.3 on 2020-11-14 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granja', '0004_auto_20201114_2305'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='localizacao',
            unique_together={('granja', 'nome')},
        ),
    ]