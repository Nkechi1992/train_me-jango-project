from django.db import models

# Create your models here.
class web_responders(models.Model):
    R_name= models.CharField(max_length=100)
    R_age= models.IntegerField()
    R_city= models.CharField(max_length=100)
    R_gender= models.CharField(max_length=50)
    R_academy= models.CharField(max_length=100)
    R_phone= models.CharField(max_length=100)
    R_email= models.CharField(max_length=100)
    R_program= models.CharField(max_length=150)
    R_image = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.R_name} {self.R_program}"