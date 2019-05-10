# Generated by Django 2.1.5 on 2019-04-21 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_posts_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Posts')),
            ],
        ),
    ]