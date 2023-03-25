from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.urls.authtoken')),
    path("admin/", admin.site.urls),

    path("api/", include("apps.users.urls")),
    path("api/", include("apps.Asset.urls")),
    path("api/", include("apps.showroom.urls")),
    # path('api/auth/', include('djoser.urls')),

]

