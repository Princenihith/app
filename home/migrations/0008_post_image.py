# Generated by Django 2.0.4 on 2018-07-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180702_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='profile_image'),
            preserve_default=False,
        ),
    ]
