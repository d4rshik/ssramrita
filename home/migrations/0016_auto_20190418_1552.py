# Generated by Django 2.1.5 on 2019-04-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20190418_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Awareness', 'Awareness'), ('Self Defence', 'Self Defence'), ('Medical Camp', 'Medical Camp'), ('Skill Building', 'Skill Building'), ('Yoga', 'Yoga'), ('Career Guidance', 'Career Guidance'), ('Cleanup Drive', 'Cleanup Drive'), ('Organic Farming', 'Organic Farming'), ('Waste Management & Composting', 'Waste Management & Composting'), ('Go Green', 'Go Green'), ('Safety & Security', 'Safety & Security'), ('Health & Hygiene', 'Health & Hygiene'), ('Flood Relief', 'Flood Relief'), ('Orphanage', 'Orphanage'), ('Social awareness', 'Social awareness'), ('Rennovation', 'Rennovation'), ('Construction', 'Construction')], max_length=50),
        ),
    ]
