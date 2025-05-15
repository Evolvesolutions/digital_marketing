from django.db import models
 


# Create your models here.

class contactform (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.TextField()
    phone=models.CharField(max_length=15)
    message=models.TextField()




    def __str__(self):
        return self.name