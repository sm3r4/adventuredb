from django.db import models

# Create your models here.
class Rides(models.Model):
    adv_id = models.AutoField(primary_key=True)
    ride_title=models.CharField(max_length=120)
    location=models.CharField(max_length=70)
    date=models.CharField(max_length=120)
    adv_img = models.URLField()
    adv_desc = models.TextField()
    b1_color= models.CharField(max_length=9)
    b2_color = models.CharField(max_length=9)
    def __str__(self):
        return self.ride_title 


class Advreg(models.Model):
    NAME=models.CharField(max_length=120)
    AGE=models.IntegerField()
    WEIGHT=models.IntegerField()
    PHNO=models.IntegerField()
    advent=models.ForeignKey('Rides',on_delete=models.CASCADE)
    def __str__(self):
        return self.NAME 
    
    


    
    
    