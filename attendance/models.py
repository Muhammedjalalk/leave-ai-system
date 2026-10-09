from django.db import models

# Create your models here.
from django.conf import settings

class Attendance(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODELS,on_delete=models.CASCADE,related_name='attendance')
    date=models.CharField()
    Check_in=models.TimeField(null=True,blank=True)
    Check_out=models.TimeField(null=True,blank=True)



    class Meta:
        unique_together=('user','date')
        ordering=['-date']

        
