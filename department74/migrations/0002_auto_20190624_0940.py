# Generated by Django 2.2.2 on 2019-06-24 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department74', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='components',
        ),
        migrations.AddField(
            model_name='computer',
            name='components',
            field=models.ManyToManyField(null=True, to='department74.Components'),
        ),
    ]
