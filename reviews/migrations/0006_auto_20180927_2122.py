# Generated by Django 2.0.4 on 2018-09-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20180927_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
    ]
