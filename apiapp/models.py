from django.db import models

# Create your models here.
class PersonalDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Age = models.IntegerField()
    gender = models.CharField(max_length=30)
    speciality = models.CharField(max_length=50)
    campus = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.first_name
