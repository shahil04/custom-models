# Generated by Django 2.1.7 on 2019-03-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutoms', '0002_auto_20190320_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='phone_no',
            field=models.PositiveIntegerField(default=0),
        ),
    ]