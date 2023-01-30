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


########################################################################################################################

class StatusManagement(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Status"
        verbose_name_plural = "Status"

########################################################################################################################


class LightTypeList(models.Model):
    name = models.CharField(max_length=120)
    status = models.OneToOneField(to=StatusManagement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Light Type List"
        verbose_name_plural = "Light Type List"

########################################################################################################################


class MaterialManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.OneToOneField(to=StatusManagement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Material Type List"
        verbose_name_plural = "Material Type List"


class BrandLocation(models.Model):
    name = models.CharField(max_length=120)
    status = models.OneToOneField(to=StatusManagement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Brand Type List"
        verbose_name_plural = "Brand Type List"


class ClassManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.OneToOneField(to=StatusManagement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Class Management"
        verbose_name_plural = "Class Management"


class Grade(models.Model):
    name = models.CharField(max_length=120)
    status = models.OneToOneField(to=StatusManagement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Grade"
        verbose_name_plural = "Grade"


class ImageManagement(models.Model):
    name = models.CharField(max_length=120)
    status = models.OneToOneField(to=StatusManagement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Degree Image Management"
        verbose_name_plural = "360 Degree Image Management"


class FloorManagement(models.Model):
    ShowroomLocation = models.OneToOneField(to=ShowroomDetail,on_delete=models.CASCADE)
    FloorDiagram = models.ImageField()