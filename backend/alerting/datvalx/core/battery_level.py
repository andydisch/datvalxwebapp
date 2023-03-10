# -*- coding: utf-8 -*-


import logging
import pendulum

from alerting.datvalx import datapoolclient
from alerting.models import Alert


def battery_level(_, source_name, variable_name, param_set, blacklist):

    if f"{source_name} + {variable_name}" in blacklist:
        logging.info(f"Battery level check skipped - {source_name} and {variable_name} blacklisted.")
        return

    start = pendulum.yesterday("Europe/Zurich")
    end = pendulum.today("Europe/Zurich")

    criteria = param_set.get("threshold")

    df = datapoolclient.query_datapool(source_name, variable_name, start, end)

    if df.empty:
        # Difference between last_data 7 days threshold and 1 last day data for this check.
        logging.info(f"No data for battery level check - {source_name}.")
        return

    df = df.resample("24H").mean()
    df["result_column"] = False
    df.loc[df["value"] < criteria, "result_column"] = True

    for index, row in df.iterrows():
        
        alarming_fact = f"Battery level below {criteria} V."

        if row["result_column"]:
            try:
                existing_alert = Alert.objects.get(
                    source=source_name,
                    variable=variable_name,
                    type="battery_level",
                    time_of_occurrence=index.tz_localize("Europe/Zurich"),
                    )
                if existing_alert.status == "acknowledged":
                    logging.info(f"Alert {source_name} {variable_name} for battery level check staged, nothing changed.")
                else:
                    existing_alert.created_time=pendulum.now("Europe/Zurich")
                    existing_alert.status = "active"
                    existing_alert.save()
                    logging.info(f"Alert {source_name} {variable_name} for battery level updated. {alarming_fact}")
            except Alert.DoesNotExist:
                alert = Alert(
                    source=source_name,
                    variable=variable_name,
                    type="battery_level",
                    alarming_fact=alarming_fact,
                    time_of_occurrence=index.tz_localize("Europe/Zurich"),
                    severity="high",
                    status="active",
                    originator="datValX",
                    created_time=pendulum.now("Europe/Zurich"),
                )
                alert.save()
                logging.info(f"Alert {source_name} {variable_name} for battery level written. {alarming_fact}")
