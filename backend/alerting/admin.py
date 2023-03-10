# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import Alert, ActiveSignalCheck, ParamSet


class AlertAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "source",
        "variable",
        "time_of_occurrence",
        "type",
        "severity",
        "status",
        "alarming_fact",
    )


class ActiveSignalCheckAdmin(admin.ModelAdmin):
    list_display = ("id", "source_name", "variable_name", "check_name", "param_set")


class ParamSetAdmin(admin.ModelAdmin):
    list_display = ("id", "paramset_name", "paramset_value")


admin.site.register(Alert, AlertAdmin)
admin.site.register(ActiveSignalCheck, ActiveSignalCheckAdmin)
admin.site.register(ParamSet, ParamSetAdmin)
