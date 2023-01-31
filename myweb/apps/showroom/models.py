from django.db import models
from django.utils.translation import gettext_lazy as _

########################################################################################################################


class RSM(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "RSM"
        verbose_name_plural = "RSM"

########################################################################################################################


class ASM(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ASM"
        verbose_name_plural = "ASM"
########################################################################################################################


class Manager(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Manager"
        verbose_name_plural = "Manager"
########################################################################################################################


class Region(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Region"
        verbose_name_plural = "Region"
########################################################################################################################


class State(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "State"
        verbose_name_plural = "State"
########################################################################################################################


class ShowroomDetail(models.Model):
    name = models.CharField(max_length=120)
    RSM = models.OneToOneField(to=RSM,on_delete=models.CASCADE)
    ASM = models.OneToOneField(to=ASM,on_delete=models.CASCADE)
    Manager = models.OneToOneField(to=Manager,on_delete=models.CASCADE)
    CUG_NO = models.CharField(max_length=120)
    Landline = models.CharField(max_length=120)
    E_Mail = models.CharField(max_length=120)
    Region = models.OneToOneField(to=Region,on_delete=models.CASCADE)
    State = models.OneToOneField(to=State,on_delete=models.CASCADE)
    Address = models.CharField(max_length=120)

    def __str__(self):
        return self.name

