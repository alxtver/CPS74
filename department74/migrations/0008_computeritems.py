# Generated by Django 2.2.2 on 2019-07-01 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department74', '0007_auto_20190627_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_components_quantity', models.IntegerField(default=1)),
                ('computer_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='department74.Computer')),
                ('type_components', models.ManyToManyField(blank=True, to='department74.TypeComponents')),
            ],
        ),
    ]