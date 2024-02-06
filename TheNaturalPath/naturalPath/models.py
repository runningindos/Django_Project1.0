from django.db import models

# Create your models here.
class Providers(models.Model):
    prid = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)

class Practice(models.Model):
    pracid = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    prac_phone = models.CharField(max_length=200)
    prac_email = models.CharField(max_length=200)
    prac_name = models.CharField(max_length=200)
    prac_address = models.CharField(max_length=200)
    prac_city = models.CharField(max_length=50)
    prac_region = models.CharField(max_length=100)
    prac_country = models.CharField(max_length=100)