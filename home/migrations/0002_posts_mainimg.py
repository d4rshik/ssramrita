# Generated by Django 2.1.5 on 2019-04-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='mainimg',
            field=models.ImageField(default='projects/1.jpg', upload_to='projects/'),
        ),
    ]
