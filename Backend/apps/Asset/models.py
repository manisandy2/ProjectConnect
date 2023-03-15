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

class ClassManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return " ID :{}, Name : {},  Status : {} ".format(self.id, self.name, self.status)

    class Meta:
        db_table = "Class Management"
        verbose_name_plural = "Class Management"

########################################################################################################################


class BrandManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return " ID :{}, Name : {},  Status : {} ".format(self.id, self.name, self.status)

    class Meta:
        db_table = "Brand Management"
        verbose_name_plural = "Brand Management"

########################################################################################################################


class BrandLocation(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Id : {} ,Name : {},  Status : {} ".format(self.id, self.name, self.status)

    class Meta:
        db_table = "Brand Location"
        verbose_name_plural = "Brand Location"


########################################################################################################################


class StatusManagement(models.Model):
    Visibility = [
        ("Assets", "Assets"),
        ("Vendor", "Vendor")
    ]
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)
    VisibilityList = models.BooleanField(choices=Visibility, max_length=120)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "Status Management"
        verbose_name_plural = "Status Management"

########################################################################################################################


class LightManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "ID:{} ,Name : {},  Status : {} ".format(self.id, self.name, self.status)

    class Meta:
        db_table = "Light Management"
        verbose_name_plural = "Light Management"

########################################################################################################################


class MaterialManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "S No : {}, Name : {},  Status : {} ".format(self.id, self.name, self.status)

    class Meta:
        db_table = "Material Management"
        verbose_name_plural = "Material Management"

########################################################################################################################




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




########################################################################################################################




########################################################################################################################


class Grade(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Grade"
        verbose_name_plural = "Grade"
########################################################################################################################


class ImageManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.ForeignKey(to=Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Degree Image Management"
        verbose_name_plural = "360 Degree Image Management"
########################################################################################################################


class FloorDiagramManagement(models.Model):
    ShowroomLocation = models.ForeignKey(to=ShowroomDetail, null=True, blank=True, on_delete=models.SET_NULL)
    FloorDiagram = models.ImageField()


########################################################################################################################

class AssetManagement(models.Model):
    Location = models.ForeignKey(to=ShowroomDetail, null=True, blank=True, on_delete=models.SET_NULL)
    ClassManagement = models.ForeignKey(to=ClassManagement, null=True, blank=True, on_delete=models.SET_NULL)
    Brand = models.ForeignKey(to=BrandManagement, null=True, blank=True, on_delete=models.SET_NULL)
    BrandingType = models.ForeignKey(to=BrandTypeManagement, null=True, blank=True, on_delete=models.SET_NULL)
    BrandLocation = models.ForeignKey(to=BrandLocation, null=True, blank=True, on_delete=models.SET_NULL)
    ModelName = models.CharField(max_length=120, null=True, blank=True)
    Height = models.CharField(max_length=120, null=True, blank=True)
    Width = models.CharField(max_length=120, null=True, blank=True)
    Material = models.ForeignKey(to=MaterialManagement, null=True, blank=True, on_delete=models.SET_NULL)
    LightType = models.ForeignKey(to=LightManagement, null=True, blank=True, on_delete=models.SET_NULL)
    ExpiryDate = models.DateField(null=True, blank=True)
    Vendor = models.ForeignKey(to=VendorManagement, null=True, blank=True, on_delete=models.SET_NULL)
    Status = models.ForeignKey(to=StatusManagement, null=True, blank=True, on_delete=models.SET_NULL)
    CreateDate = models.DateTimeField(null=True, blank=True)
    UpdatedDate = models.DateTimeField(null=True, blank=True)
    Comments = models.CharField(max_length=240, null=True, blank=True)
    AssetImage = models.URLField(null=True, blank=True)
    ADImage = models.URLField(null=True, blank=True)

    def __str__(self):
        return "Location : {},  Class : {},  Brand : {},  BrandingType : {},  " \
               "Model : {},  Height : {},  Width : {} ,Material : {},  LightType : {}," \
               "ExpiryDate : {},  Vendor : {},  Status : {},  CreateDate : {},  UpdatedDate : {}" \
               "Comments : {},  AssetImage : {},  ADImage : {},ASM :{} " \
            .format(self.Location, self.ClassManagement, self.Brand, self.BrandingType,
                    self.BrandLocation, self.ModelName, self.Height, self.Width,
                    self.Material, self.LightType, self.ExpiryDate, self.Vendor,
                    self.Status, self.CreateDate, self.UpdatedDate, self.Comments,
                    self.AssetImage, self.ADImage)

    class Meta:
        db_table = "Asset Management"
        verbose_name_plural = "Asset Management"
