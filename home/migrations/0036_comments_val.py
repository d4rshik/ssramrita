# Generated by Django 2.1.5 on 2019-05-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20190425_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='val',
            field=models.BooleanField(default=False),
        ),
    ]
