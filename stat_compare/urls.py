from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/compare/", include("stat_compare.stats.urls"))
]
