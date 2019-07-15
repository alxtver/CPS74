# Generated by Django 2.2.2 on 2019-07-04 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department74', '0025_auto_20190703_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comp',
            name='items',
        ),
        migrations.AddField(
            model_name='comp',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='department74.TypeComponents'),
        ),
        migrations.AlterField(
            model_name='compitems',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
