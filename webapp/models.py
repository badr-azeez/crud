from django.db import models

# Create your models here.
class Record(models.Model):
    creation_data = models.DateTimeField(auto_now_add=True  )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email     = models.EmailField()
    phone     = models.CharField(max_length=20)
    address   = models.CharField(max_length=255)
    city      = models.CharField(max_length=255)
    province  = models.CharField(max_length=255)
    country   = models.CharField(max_length=125)

    def __str__(self):
        return self.first_name + " " + self.last_name

