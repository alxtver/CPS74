# Generated by Django 2.2.2 on 2019-06-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department74', '0004_auto_20190626_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='type_components',
            field=models.ManyToManyField(null=True, to='department74.TypeComponents'),
        ),
    ]
