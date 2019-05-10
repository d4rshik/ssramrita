from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here

class Posts(models.Model):
    ssrid = models.CharField(primary_key=True, max_length=9, blank=False, unique=True)
    title = models.CharField(max_length=75, blank=False)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="static/main/",default="static/project/main.jpg")
    mission = models.CharField(max_length=1000,blank=False,default=None)
    content = models.TextField(default="None")
    video = models.URLField(max_length=200,default="https://www.youtube.com/embed/8O3df8lXOME")
    cat = "Awareness, Self Defence, Medical Camp, Skill Building, Yoga, Career Guidance, Cleanup Drive, Organic Farming, Waste Management and Composting, Go Green, Safety and Security, Health and Hygiene, Flood Relief, Orphanage, Social awareness, Rennovation, Construction"
    category = models.CharField(max_length=200,default=cat.lower())
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.ssrid


class Comments(models.Model):
    ssrid = models.CharField(max_length=9, blank=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    val = models.BooleanField(default=False)

    def __str__(self):
        return self.message
