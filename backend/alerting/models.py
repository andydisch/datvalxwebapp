# -*- coding: utf-8 -*-


from django.db import models


class AlarmStatus(models.TextChoices):
    ACTIVE = "active"
    ACKNOWLEDGED = "acknowledged"
    CLEARED = "cleared"


class VariableName(models.TextChoices):
    WATER_LEVEL = "water_level"
    BATTERY_VOLTAGE = "battery_voltage"
    PRESSURE = "pressure"
    INDUCTIVE_CONDUCTIVITY = "inductive_conductivity"
    DIELECTRIC_PERMITTIVITY = "dielectric_permittivity"
    AMBIENT_AIR_TEMPERATURE = "ambient_air_temperature"
    HEADSPACE_TEMPERATURE = "headspace_temperature"
    WATER_TEMPERATURE = "water_temperature"
    SOIL_TEMPERATURE = "soil_temperature"
    FLOW_RATE = "flow_rate"
    RAINFALL_INTENSITY = "rainfall_intensity"


class CheckName(models.TextChoices):
    LAST_DATAPOINT = "last_data"
    BATTERY_LEVEL = "battery_level"
    PRS_QOS = "prs_qos"
    RAIN_SUM = "rain_sum"


class Alert(models.Model):
    source = models.TextField()
    variable = models.CharField(max_length=23, choices=VariableName.choices)
    time_of_occurrence = models.DateTimeField()
    alarming_fact = models.TextField()
    alarm_preview = models.ImageField(blank=True, null=True)
    type = models.TextField()
    severity = models.TextField()
    status = models.CharField(max_length=12, choices=AlarmStatus.choices)
    originator = models.TextField()
    created_time = models.DateTimeField()
    acknowledged_time = models.DateTimeField(blank=True, null=True)
    cleared_time = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.source} {self.variable} {self.type}"


class ParamSet(models.Model):
    paramset_name = models.TextField()
    paramset_value = models.JSONField(null=True)

    def __str__(self) -> str:
        return f"{self.paramset_name}"


class ActiveSignalCheck(models.Model):
    source_name = models.TextField()
    variable_name = models.CharField(max_length=23, choices=VariableName.choices)
    check_name = models.CharField(max_length=14, choices=CheckName.choices)
    param_set = models.ForeignKey(ParamSet, on_delete=models.CASCADE, null=True)
