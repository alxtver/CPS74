# Generated by Django 2.2.2 on 2019-07-01 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department74', '0010_auto_20190701_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computeritems',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='computeritems',
            name='item',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='department74.TypeComponents'),
        ),
    ]
