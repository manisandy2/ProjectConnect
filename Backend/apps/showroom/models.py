from django.db import models
from django.utils.translation import gettext_lazy as _

########################################################################################################################


class RSM(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "RSM"
        verbose_name_plural = "RSM"

########################################################################################################################


class ASM(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "ASM"
        verbose_name_plural = "ASM"
########################################################################################################################


class Manager(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "Manager"
        verbose_name_plural = "Manager"
########################################################################################################################


class Region(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "Region"
        verbose_name_plural = "Region"
########################################################################################################################


class State(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "State"
        verbose_name_plural = "State"
########################################################################################################################


class ShowroomDetail(models.Model):
    name = models.CharField(max_length=120)
    RSM = models.ForeignKey(to=RSM, null=True, blank=True, on_delete=models.SET_NULL)
    ASM = models.ForeignKey(to=ASM, null=True, blank=True,on_delete=models.SET_NULL)
    Manager = models.ForeignKey(to=Manager, null=True,blank=True, on_delete=models.SET_NULL)
    CUG_NO = models.CharField(max_length=120, null=True, blank=True)
    Landline = models.CharField(max_length=120, null=True, blank=True)
    E_Mail = models.CharField(max_length=120, null=True, blank=True)
    Region = models.ForeignKey(to=Region, null=True, blank=True, on_delete=models.SET_NULL)
    State = models.ForeignKey(to=State, null=True, blank=True, on_delete=models.SET_NULL)
    Address = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return "id :{} ,Name : {},  RSM : {}, ASM : {}," \
               "Manager : {},CUG NO : {},Landline : {},E_Mail : {},Region : {},State : {},Address : {} ".\
            format(self.id, self.name, self.RSM, self.ASM, self.Manager, self.CUG_NO, self.Landline, self.E_Mail,
                   self.Region,self.State,self.Address)

    class Meta:
        db_table = "Show Room Detail"
        verbose_name_plural = "Show Room Detail"

########################################################################################################################


class Store(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "Store"
        verbose_name_plural = "Store"

########################################################################################################################