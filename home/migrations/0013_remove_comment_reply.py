# Generated by Django 2.0.4 on 2018-07-10 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_comment_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
    ]
