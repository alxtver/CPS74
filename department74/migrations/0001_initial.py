# Generated by Django 2.2.2 on 2019-06-24 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=255)),
                ('date_of_arrival', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('part_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeComponents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=100)),
                ('components', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='department74.Components')),
                ('part_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='department74.Part')),
            ],
        ),
        migrations.AddField(
            model_name='components',
            name='country',
            field=models.ForeignKey(help_text='Страна производства', null=True, on_delete=django.db.models.deletion.SET_NULL, to='department74.Country'),
        ),
        migrations.AddField(
            model_name='components',
            name='name_type',
            field=models.ForeignKey(help_text='Тип комплектующих', null=True, on_delete=django.db.models.deletion.SET_NULL, to='department74.TypeComponents'),
        ),
    ]
