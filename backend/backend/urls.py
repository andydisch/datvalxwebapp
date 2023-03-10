# -*- coding: utf-8 -*-


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from alerting import views


router = routers.DefaultRouter()
router.register(r"alarms", views.AlertView, basename="alarm")
router.register(r"signalchecks", views.ActiveSignalCheckView, basename="signalcheck")
router.register(r"paramsets", views.ParamSetView, basename="paramset")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
