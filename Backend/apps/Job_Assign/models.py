from django.db import models
from apps.showroom.models import ShowroomDetail
from django.contrib.auth.models import User


class JobFor(models.Model):
    name = models.CharField(max_length=120)


class JobType(models.Model):
    name = models.CharField(max_length=120)


class DesignType(models.Model):
    name = models.CharField(max_length=120)


class Priority(models.Model):
    name = models.CharField(max_length=120)


class Status(models.Model):
    name = models.CharField(max_length=120)


class JobForm(models.Model):
    jobFor = models.ForeignKey(to=JobFor, null=True, blank=True, on_delete=models.SET_NULL)
    jobType = models.ForeignKey(to=JobType, null=True, blank=True, on_delete=models.SET_NULL)
    designType = models.ForeignKey(to=DesignType, null=True, blank=True, on_delete=models.SET_NULL)
    showroom = models.ForeignKey(to=ShowroomDetail,null=True, blank=True, on_delete=models.SET_NULL)
    priority = models.ForeignKey(to=Priority, null=True, blank=True, on_delete=models.SET_NULL)
    assign_to = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.SET_NULL)
    startDate = models.DateTimeField()
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)
    endData = models.DateTimeField()
    comment = models.CharField(max_length=1200)

    def __str__(self):
        return " Id :{}, jobFor : {}, jobType :{},designType :{}," \
               " showroom :{} ,priority :{} ,assign_to :{}," \
               " startDate:{} ,status :{}, endDate :{},Comment :{} ".format(self.id,
                self.jobFor, self.jobType, self.designType, self.showroom, self.priority,
                self.assign_to, self.startDate, self.status, self.endData,  self.comment)

    class Meta:
        db_table = "JobForm"
        verbose_name_plural = "JobForm"


