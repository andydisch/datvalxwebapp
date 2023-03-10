from django.apps import AppConfig


class AlertingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "alerting"


class ActiveSignalCheckConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "signalchecks"


class ParamSetConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "paramset"
