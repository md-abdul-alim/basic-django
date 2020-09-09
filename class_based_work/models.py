from django.db import models
from django.urls import reverse

from django.shortcuts import render, get_object_or_404, redirect
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=120)
    content= models.CharField(max_length=120)
    active= models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
        #Note:(articles:article-detail) here articles is connected with urls.py app_name='articles'
        #return reverse("articles:article-list")
    