# Generated by Django 2.2.2 on 2019-07-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department74', '0012_auto_20190701_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='type_components',
            field=models.ManyToManyField(to='department74.TypeComponents'),
        ),
    ]
