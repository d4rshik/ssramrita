# Generated by Django 2.1.5 on 2019-04-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='ssrid',
        ),
        migrations.AddField(
            model_name='comments',
            name='ssrid',
            field=models.ManyToManyField(to='home.Posts'),
        ),
    ]