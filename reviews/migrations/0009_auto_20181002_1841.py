# Generated by Django 2.0.4 on 2018-10-02 13:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20181002_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_name',
            field=models.ForeignKey(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='wine',
            field=models.ForeignKey(on_delete='models.CASCADE', to='reviews.Wine'),
        ),
    ]
