# Generated by Django 2.1.5 on 2019-04-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20190418_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='mission',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
