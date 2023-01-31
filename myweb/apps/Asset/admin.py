from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class StatusAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Status, StatusAdmin)

class StatusManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(StatusManagement, StatusManagementAdmin)

########################################################################################################################


class MaterialManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(MaterialManagement, MaterialManagementAdmin)
########################################################################################################################


class LightManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(LightManagement, LightManagementAdmin)
########################################################################################################################


class BrandLocationAdmin(ImportExportModelAdmin):
    pass


admin.site.register(BrandLocation, BrandLocationAdmin)

########################################################################################################################

class VendorManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(VendorManagement, VendorManagementAdmin)

########################################################################################################################
class BrandTypeManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(BrandTypeManagement, BrandTypeManagementAdmin)
########################################################################################################################

class BrandManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(BrandManagement, BrandManagementAdmin)

########################################################################################################################
class ClassManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(ClassManagement, ClassManagementAdmin)
########################################################################################################################

class GradeAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Grade, GradeAdmin)

########################################################################################################################


class ImageManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(ImageManagement, ImageManagementAdmin)
########################################################################################################################


class FloorDiagramManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(FloorDiagramManagement, FloorDiagramManagementAdmin)
########################################################################################################################
class AssetManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(AssetManagement, AssetManagementAdmin)
########################################################################################################################