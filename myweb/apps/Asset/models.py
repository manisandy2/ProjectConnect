from django.db import models
from apps.showroom.models import ShowroomDetail

class Status(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "Status"
        verbose_name_plural = "Status"

########################################################################################################################


class StatusManagement(models.Model):
    Visibility = [
        ("Assets","Assets"),
        ("Vendor","Vendor")
    ]
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True,blank=True,on_delete=models.SET_NULL)
    VisibilityList = models.CharField(choices=Visibility,max_length=120)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "Status Management"
        verbose_name_plural = "Status Management"

########################################################################################################################


class LightManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return "Name : {},  Status : {} ".format(self.name,self.status)

    class Meta:
        db_table = "Light Management"
        verbose_name_plural = "Light Management"

########################################################################################################################


class MaterialManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return "Name : {},  Status : {} ".format(self.name,self.status)

    class Meta:
        db_table = "Material Management"
        verbose_name_plural = "Material Management"

########################################################################################################################


class BrandLocation(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Name : {},  Status : {} ".format(self.name, self.status)

    class Meta:
        db_table = "Brand Location"
        verbose_name_plural = "Brand Location"

########################################################################################################################
class VendorManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Name : {},  Status : {} ".format(self.name, self.status)

    class Meta:
        db_table = "Vendor Management"
        verbose_name_plural = "Vendor Management"

########################################################################################################################
class BrandTypeManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Name : {},  Status : {} ".format(self.name, self.status)

    class Meta:
        db_table = "Brand Type Management"
        verbose_name_plural = "Brand Type Management"
########################################################################################################################


class BrandManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Name : {},  Status : {} ".format(self.name, self.status)

    class Meta:
        db_table = "Brand Management"
        verbose_name_plural = "Brand Management"

########################################################################################################################


class ClassManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Class Management"
        verbose_name_plural = "Class Management"

########################################################################################################################


class Grade(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Grade"
        verbose_name_plural = "Grade"
########################################################################################################################


class ImageManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Degree Image Management"
        verbose_name_plural = "360 Degree Image Management"
########################################################################################################################


class FloorDiagramManagement(models.Model):
    ShowroomLocation = models.ForeignKey(to=ShowroomDetail, null=True,blank=True,on_delete=models.SET_NULL)
    FloorDiagram = models.ImageField()


########################################################################################################################

class AssetManagement(models.Model):
    ShowroomLocation = models.CharField(max_length=120)
    BrandingType = models.CharField(max_length=120)
    BrandLocation = models.CharField(max_length=120)
    Brand = models.CharField(max_length=120)
    ModelName = models.CharField(max_length=120)
    Width = models.CharField(max_length=120)
    Height = models.CharField(max_length=120)
    Material =  models.CharField(max_length=120)
    Region = models.CharField(max_length=120)
    ADImage = models.CharField(max_length=120)
    JobStatus = models.CharField(max_length=120)