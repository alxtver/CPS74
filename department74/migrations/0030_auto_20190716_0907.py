# Generated by Django 2.2.3 on 2019-07-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department74', '0029_auto_20190715_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Quantity',
        ),
    ]
