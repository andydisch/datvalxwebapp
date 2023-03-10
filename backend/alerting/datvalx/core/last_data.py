# -*- coding: utf-8 -*-


import logging
import pendulum

from alerting.datvalx import datapoolclient
from alerting.models import Alert


def last_data(_, source_name, variable_name, param_set, blacklist):
    
    criteria = param_set.get("days")

    end = pendulum.today("Europe/Zurich")
    start = end.subtract(days=criteria)

    df = datapoolclient.query_datapool(source_name, variable_name, start, end)

    if df.empty:

        df = datapoolclient.get_last_datapoint(source_name, variable_name)
        if df.empty:
            alarming_fact = f"Last datapoint before {start.subtract(days=100).to_string()}."
        else:    
            alarming_fact = f"Last datapoint on {df.index[0].strftime('%Y-%m-%d')}."
        blacklist.append(f"{source_name} + {variable_name}")
        logging.info(f"{source_name} + {variable_name} blacklisted by last data check.")

        try:
            existing_alert = Alert.objects.get(
                source=source_name,
                variable=variable_name,
                type="last_data",
                )
            if existing_alert.status == "acknowledged":
                logging.info(f"Alert {source_name} {variable_name} for last data check staged, nothing changed.")
            else:
                existing_alert.created_time=pendulum.now("Europe/Zurich")
                existing_alert.status = "active"
                existing_alert.save()
                logging.info(f"Alert {source_name} {variable_name} for last data check updated. {alarming_fact}")
        except Alert.DoesNotExist:
            alert = Alert(
                    source=source_name,
                    variable=variable_name,
                    type="last_data",
                    alarming_fact=alarming_fact,
                    time_of_occurrence=pendulum.now("Europe/Zurich"),
                    severity="high",
                    status="active",
                    originator="datValX",
                    created_time=pendulum.now("Europe/Zurich"),
                )
            alert.save()
            logging.info(f"Alert {source_name} {variable_name} for last data check written. {alarming_fact}")
