from django.db import models
from django.urls import reverse
# Create your models here.

# https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types


class Product(models.Model):
    title = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    summary = models.TextField(blank=True, null=True)
    #featured = models.BooleanField(null=True, default=True)
    #featured = models.BooleanField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return f"/product_delete_view/{self.id}/"
        return reverse("products:product_delete_view",kwargs={
            'id':self.id
        })

# class Testtable(models.Model):
#     test= models.CharField(max_length=120)


