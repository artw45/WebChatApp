# Generated by Django 3.2.8 on 2021-10-29 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='connectionid',
            field=models.CharField(default='', max_length=30),
        ),
    ]
