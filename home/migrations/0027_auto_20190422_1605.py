# Generated by Django 2.1.5 on 2019-04-22 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_delete_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='proj', to='home.Posts'),
        ),
    ]