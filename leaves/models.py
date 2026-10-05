from django.db import models
from django.conf import settings


class LeaveType(models.Model):
    name=models.CharField(max_length=50,unique=True)
    annual_quota=models.PositiveBigIntegerField(default=12)


    def __str__(self):
        return self.name



class LeaveBalance(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,   related_name='leave_requests')
    leave_type=models.ForeignKey(LeaveType,on_delete=models.CASCADE)
    year=models.PositiveBigIntegerField()
    used=models.DecimalField(max_length=5,decimal_places=1,default=0)

    class Meta:
        unique_together=('user','leave_type','year')

    @property
    def remaining(self):
        return self.leave_type.annual_quota-self.used