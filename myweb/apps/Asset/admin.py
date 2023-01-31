from django.contrib import admin
from .models import *
from import_export.admin import  ImportExportModelAdmin

# Register your models here.
# admin.site.register(StatusManagement)
# admin.site.register(LightTypeList)
# admin.site.register(MaterialManagement)
# admin.site.register(BrandLocation)
# admin.site.register(Grade)
# admin.site.register(ImageManagement)
# admin.site.register(FloorManagement)
admin.site.register(LightTypeList)
admin.site.register(MaterialManagement)
admin.site.register(BrandLocation)
admin.site.register(Grade)
admin.site.register(ImageManagement)
admin.site.register(FloorManagement)


class StatusManagementAdmin(ImportExportModelAdmin):
    pass


admin.site.register(StatusManagement,StatusManagementAdmin)
