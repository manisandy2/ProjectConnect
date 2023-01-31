from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(ShowroomDetail)
# admin.site.register(RSM)
admin.site.register(ASM)
admin.site.register(Manager)
admin.site.register(Region)


class StoreAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Store, StoreAdmin)


class StateAdmin(ImportExportModelAdmin):
    pass


admin.site.register(State, StateAdmin)


class RSMAdmin(ImportExportModelAdmin):
    pass


admin.site.register(RSM, RSMAdmin)
