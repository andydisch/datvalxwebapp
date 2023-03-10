# -*- coding: utf-8 -*-


import logging
import pendulum

from alerting.datvalx import datapoolclient
from alerting.models import Alert


def prs_qos(_, source_name, variable_name, param_set, blacklist):

    if f"{source_name} + {variable_name}" in blacklist:
        logging.info(f"PRS check skipped - {source_name} and {variable_name} blacklisted.")
        return

    criteria = param_set.get("days")
    time_until_next_package_in_min = param_set.get("time_until_next_package_in_min")
    threshold = param_set.get("threshold")

    end = pendulum.today("Europe/Zurich")
    start = end.subtract(days=criteria)

    df = datapoolclient.query_datapool(source_name, variable_name, start, end)

    df = df.groupby(df.index.date).count()
    df["psr"] = df["value"] / (24 * 60 / time_until_next_package_in_min)
    
    mean_psr = df["psr"].mean()
        
        
    if mean_psr * 100 < threshold:

        alarming_fact = f"PSR to low with {round(mean_psr * 100, 2)} %."

        try:
            existing_alert = Alert.objects.get(
                source=source_name,
                variable=variable_name,
                type="prs_qos",
                )
            if existing_alert.status == "acknowledged":
                logging.info(f"Alert {source_name} {variable_name} for psr check staged, nothing changed.")
            else:
                existing_alert.created_time = pendulum.now("Europe/Zurich")
                existing_alert.status = "active"
                existing_alert.save()
                logging.info(f"Alert {source_name} {variable_name} for psr check updated. {alarming_fact}")
        except Alert.DoesNotExist:
            alert = Alert(
                source=source_name,
                variable=variable_name,
                type="prs_qos",
                alarming_fact=alarming_fact,
                time_of_occurrence=pendulum.now("Europe/Zurich"),
                severity="high",
                status="active",
                originator="datValX",
                created_time=pendulum.now("Europe/Zurich"),
            )
            alert.save()
            logging.info(f"Alert {source_name} {variable_name} for psr check written. {alarming_fact}")
