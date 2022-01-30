from django.db import models

# Create your models here.

class Service_provider(models.Model):
    name=models.CharField(max_length=70)
    def __str__(self):
        return self.name

class Plan(models.Model):
    service_provider = models.ForeignKey(Service_provider,on_delete=models.CASCADE)
    price =models.FloatField(max_length=70)
    talktime=models.CharField(max_length=70,null=True,blank=True)
    data=models.CharField(max_length=70,null=True,blank=True)
    validity=models.CharField(max_length=70)
    sms=models.CharField(max_length=70,null=True,blank=True)
    other_details=models.CharField(max_length=500,null=True,blank=True)