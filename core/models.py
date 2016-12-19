from django.db import models

# Create your models here.


class Client(models.Model):
    full_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    tel_number = models.CharField(max_length=20,)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    update = models.DateField(auto_now_add=False, auto_now=True)
    note = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.email


class Gallery(models.Model):
 pass