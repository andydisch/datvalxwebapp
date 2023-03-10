# -*- coding: utf-8 -*-


from rest_framework import serializers
from .models import Alert, ActiveSignalCheck, ParamSet


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = (
            "id",
            "source",
            "variable",
            "alarming_fact",
            "time_of_occurrence",
            "alarm_preview",
            "type",
            "severity",
            "status",
            "originator",
            "created_time",
            "acknowledged_time",
            "cleared_time",
        )


class ActiveSignalCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveSignalCheck
        fields = (
            "id",
            "source_name",
            "variable_name",
            "check_name",
            "param_set",
        )


class ParamSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParamSet
        fields = (
            "id",
            "paramset_name",
            "paramsert_value",
        )
