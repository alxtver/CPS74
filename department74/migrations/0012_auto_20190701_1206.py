# Generated by Django 2.2.2 on 2019-07-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department74', '0011_auto_20190701_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='serial_number',
        ),
        migrations.AlterField(
            model_name='computer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
