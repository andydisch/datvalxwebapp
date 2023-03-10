# -*- coding: utf-8 -*-


from rest_framework import viewsets
from .serializers import (
    AlertSerializer,
    ActiveSignalCheckSerializer,
    ParamSetSerializer,
)
from .models import Alert, ActiveSignalCheck, ParamSet


class AlertView(viewsets.ModelViewSet):
    serializer_class = AlertSerializer

    def get_queryset(self):
        queryset = Alert.objects.all()
        query_param = self.request.query_params.get("status")
        oldest_first = self.request.query_params.get("oldest_first")
        if query_param is not None:
            queryset = queryset.filter(status=query_param).order_by("-created_time")
        if oldest_first is not None:
            queryset = queryset.order_by("created_time")

        return queryset


class ActiveSignalCheckView(viewsets.ModelViewSet):
    serializer_class = ActiveSignalCheckSerializer

    def get_queryset(self):
        queryset = ActiveSignalCheck.objects.all()
        return queryset


class ParamSetView(viewsets.ModelViewSet):
    serializer_class = ParamSetSerializer

    def get_queryset(self):
        queryset = ParamSet.objects.all()
        return queryset
