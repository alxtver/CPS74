# Generated by Django 2.2.2 on 2019-06-27 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department74', '0006_auto_20190626_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='components',
            name='country',
            field=models.ForeignKey(blank=True, help_text='Страна производства', null=True, on_delete=django.db.models.deletion.SET_NULL, to='department74.Country'),
        ),
        migrations.AlterField(
            model_name='components',
            name='name_type',
            field=models.ForeignKey(help_text='Тип комплектующих', on_delete=django.db.models.deletion.CASCADE, to='department74.TypeComponents'),
        ),
        migrations.AlterField(
            model_name='components',
            name='serial_number',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='serial_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
