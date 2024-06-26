from django.urls import path
from stat_compare.stats import views


urlpatterns = [
    path("", views.ObjGetView.as_view(), name="ObjGetView"),
    path("<uuid:mon_id>/", views.ObjGetPutDelete.as_view(), name="ObjGetPutDelete"),
]
