# Generated by Django 5.0.4 on 2024-07-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipodocumento', '0005_ciudad_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.BigIntegerField(),
        ),
    ]
