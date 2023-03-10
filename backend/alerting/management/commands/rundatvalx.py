# -*- coding: utf-8 -*-


import os
import logging

from django.core.management.base import BaseCommand
from alerting.models import ActiveSignalCheck, ParamSet

from alerting.datvalx import routine


LOG_FILE = os.environ.get("logger_file")

logging.basicConfig(filename=LOG_FILE,
                    filemode="a",
                    format="%(asctime)s %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d",
                    level=logging.DEBUG)


class Command(BaseCommand):
    help = "Run the daily datValX routine."

    def handle(self, *args, **options):

        # list of source and parameter combinations which are no longer tested. not useful
        # according to hierarchical test arrangement. e.g. if no data, then no battery check.
        # the list is not saved after a run.
        blacklist = []

        for id, source_name, variable_name, check_name, param_set in list(
            ActiveSignalCheck.objects.all().values_list()
        ):
            try:
                params = ParamSet.objects.get(pk=param_set).paramset_value
                routine.run(id, source_name, variable_name, check_name, params, blacklist)
            except:
                logging.ERROR(f"Check {check_name} failed for {source_name} and {variable_name}.")
                self.stdout.write(
                    self.style.ERROR(
                        f"Check {check_name} failed for {source_name} and {variable_name}."
                    )
                )

        self.stdout.write(self.style.SUCCESS("Successfully run datValX routine."))
