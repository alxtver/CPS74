# Generated by Django 2.2.3 on 2019-07-15 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department74', '0028_auto_20190704_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comp',
            name='items',
            field=models.ManyToManyField(related_name='all_items', through='department74.CompItems', to='department74.TypeComponents'),
        ),
        migrations.AlterField(
            model_name='compitems',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
