# Generated by Django 2.1.7 on 2019-03-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutoms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='name',
            field=models.TextField(max_length='150'),
        ),
        migrations.AlterField(
            model_name='database',
            name='phone_no',
            field=models.TextField(max_length='150'),
        ),
    ]
