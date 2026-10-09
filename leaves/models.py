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


class LeaveRequest(models.Model):
    class Status(models.TextChoices):
        PENDING='PENDING','Pending',
        APPROVED='APPROVED','Approved',
        REJECTED='REJECTED','Rejected',
        CANCELLED='CANCELED','Cancelled'

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='leave_request')
    leave_type=models.ForeignKey(LeaveType,on_delete=models.PROTECT)
    start_date=models.DateField()
    end_date=models.DateField()
    is_half_day=models.BooleanField(default=False)
    reason=models.TextField()
    Status=models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING)
    reviewed_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET_NULL,related_name='reviewed_leaves')
    manager_commit=models.TextField(blank=True)
    ai_summery=models.TextField()
    create_at=models.DateTimeField(auto_created=True)

    class Meta:
        ordering=['-create_at']


        @property
        def days(self):
            if self.is_half_day:
                return 0.5
            return (self.end_date-self.start_date).days+1


    class Holiday(models.Model):
        date=models.DateField(unique=True)
        name=models.TextField(max_length=100)

        def __str__(self):
            return f"{self.name}-{self.name}"