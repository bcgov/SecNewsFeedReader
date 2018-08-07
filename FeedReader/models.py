from django.db import models

class Categories(models.Model):
    top_heading = models.CharField(max_length=100)
    sub_headings = []

class Feeds(models.Model):
    filter=models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    description = models.CharField(max_length=500)