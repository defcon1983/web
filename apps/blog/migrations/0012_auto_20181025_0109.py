# Generated by Django 2.0.6 on 2018-10-25 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181022_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='estado',
            field=models.BooleanField(default=False, verbose_name='Publicado/No Publicado'),
        ),
    ]
