from django.db import models
from apps.showroom.models import ShowroomDetail


class StatusManagement(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "Status"
        verbose_name_plural = "Status"

########################################################################################################################


class LightTypeList(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=StatusManagement, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return "Name : {},  Status : {} ".format(self.name,self.status)

    class Meta:
        db_table = "Light Type List"
        verbose_name_plural = "Light Type List"

########################################################################################################################


class MaterialManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=StatusManagement, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return "Name : {},  Status : {} ".format(self.name,self.status)

    class Meta:
        db_table = "Material Type List"
        verbose_name_plural = "Material Type List"

########################################################################################################################


class BrandLocation(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=StatusManagement, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Name : {},  Status : {} ".format(self.name, self.status)

    class Meta:
        db_table = "Brand Type List"
        verbose_name_plural = "Brand Type List"

########################################################################################################################


class BrandManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=StatusManagement, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Name : {},  Status : {} ".format(self.name, self.status)

    class Meta:
        db_table = "Brand"
        verbose_name_plural = "Brand"

########################################################################################################################


class ClassManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=StatusManagement, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Class Management"
        verbose_name_plural = "Class Management"

########################################################################################################################


class Grade(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=StatusManagement, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Grade"
        verbose_name_plural = "Grade"
########################################################################################################################


class ImageManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=StatusManagement, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Degree Image Management"
        verbose_name_plural = "360 Degree Image Management"
########################################################################################################################


class FloorManagement(models.Model):
    ShowroomLocation = models.ForeignKey(to=ShowroomDetail, null=True,blank=True,on_delete=models.SET_NULL)
    FloorDiagram = models.ImageField()


########################################################################################################################
