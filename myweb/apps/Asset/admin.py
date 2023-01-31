from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class StatusManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(StatusManagement, StatusManagementAdmin)

########################################################################################################################


class MaterialManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(MaterialManagement, MaterialManagementAdmin)
########################################################################################################################


class LightTypeListAdmin(ImportExportModelAdmin):
    pass


admin.site.register(LightTypeList, LightTypeListAdmin)
########################################################################################################################


class BrandLocationAdmin(ImportExportModelAdmin):
    pass


admin.site.register(BrandLocation, BrandLocationAdmin)

########################################################################################################################


class BrandManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(BrandManagement, BrandManagementAdmin)

########################################################################################################################


class GradeAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Grade, GradeAdmin)

########################################################################################################################


class ImageManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(ImageManagement, ImageManagementAdmin)
########################################################################################################################


class FloorManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(FloorManagement, FloorManagementAdmin)
########################################################################################################################
