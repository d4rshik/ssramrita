# Generated by Django 2.1.5 on 2019-04-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190418_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]