# -*- coding: utf-8 -*-

from django.test import TestCase

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()

import pendulum

from alerting.datvalx import datapoolclient
from alerting.datvalx.core import last_data, battery_level


class TestDataPoolClient(TestCase):

    # This source 'bf_f03_11e_russikerstr' is deinstalled and datapoints
    # should not change in value.
    def test_query_datapool(self):

        nd = pendulum.today("Europe/Zurich")
        strt = nd.subtract(days=365)

        df = datapoolclient.query_datapool(
            signal="bf_f03_11e_russikerstr",
            variable="flow_rate",
            start=strt,
            end=nd,
            )

        assert df["value"].iloc[0] == 7.1623976020608
        assert str(df.index[0]) == "2022-03-07 00:00:00"

    # This source 'bf_f03_11e_russikerstr' is deinstalled and therefore 
    # the last datapoint should not change in value.
    def test_get_last_datapoint(self):

        latest = pendulum.today("Europe/Zurich").subtract(days=365)

        df = datapoolclient.get_last_datapoint(
            signal="bf_f03_11e_russikerstr",
            variable="flow_rate",
            latest=latest,
            )

        assert df["value"].iloc[0] == 10.9039050676794
        assert str(df.index[0]) == "2022-09-14 08:15:00"
