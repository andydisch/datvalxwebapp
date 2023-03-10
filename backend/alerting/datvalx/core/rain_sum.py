# -*- coding: utf-8 -*-


import logging
import pendulum

import numpy as np

from alerting.datvalx import datapoolclient
from alerting.models import Alert


def rain_sum(_, source_name, variable_name, param_set, blacklist):
	
    reference_sensors = param_set.get("reference_sensors")
    considered_time_window = param_set.get("considered_time_window")

    end = pendulum.today("Europe/Zurich")
    start = end.subtract(hours=considered_time_window)

    reference_rain = []
    for s in reference_sensors:
        df = datapoolclient.query_datapool(s, "rainfall_intensity", start, end)
        reference_rain.append(df["value"].sum())

    max_reference_variance = param_set.get("max_reference_variance")
    if not np.std(reference_rain) <= max_reference_variance:
        logging.info("Rain sum test cannot be calculated. The reference measurements differ significantly.")
    reference_rain = np.mean(reference_rain)
    
    checked_sensors = param_set.get("checked_sensors")
    max_difference = param_set.get("max_difference")
    for s in checked_sensors:

        if f"{s} + rainfall_intensity" in blacklist:
            logging.info(f"Rain sum check skipped - {s} and rainfall_intensity blacklisted.")
            continue

        df = datapoolclient.query_datapool(s, "rainfall_intensity", start, end)
        rain_sum = df["value"].sum()

        if rain_sum > reference_rain + max_difference or rain_sum < reference_rain - max_difference:

            alarming_fact = f"Rain total {rain_sum}mm deviates more than {max_difference}mm from reference sum {reference_rain}mm."

            try:
                existing_alert = Alert.objects.get(
                    source=s,
                    variable="rainfall_intensity",
                    type="rain_sum",
                    )
                if existing_alert.status == "acknowledged":
                    logging.info(f"Alert {s} rainfall_intensity for rain sum check staged, nothing changed.")
                else:
                    existing_alert.created_time = pendulum.now("Europe/Zurich")
                    existing_alert.status = "active"
                    existing_alert.save()
                    logging.info(f"Alert {s} rainfall_intensity for rain sum check updated. {alarming_fact}")
            except Alert.DoesNotExist:
                alert = Alert(
                    source=s,
                    variable="rainfall_intensity",
                    type="rain_sum",
                    alarming_fact=alarming_fact,
                    time_of_occurrence=start,
                    severity="high",
                    status="active",
                    originator="datValX",
                    created_time=pendulum.now("Europe/Zurich"),
                )
                alert.save()
                logging.info(f"Alert {s} rainfall_intensity for rain sum check written. {alarming_fact}")
