# -*- coding: utf-8 -*-


from django.core.management.base import BaseCommand
from alerting.models import ActiveSignalCheck, ParamSet


ALL_ACTIVE_SIGNALS = [
    ("bl_ceb5f_58sbw_undermulistr", "water_level"),
    ("bl_dl256_rubbasin_ara", "water_level"),
    ("bl_dl258_rubbasin_ara", "water_level"),
    ("bl_dl309_sk102_wermatswilstr", "water_level"),
    ("bl_dl310_sk_ara", "water_level"),
    ("bl_dl311_rubmorg_inflow", "water_level"),
    # ("bl_dl312_40d_imberg", "water_level"),
    # ("bl_dl313_124a_chueferi", "water_level"),
    # ("bl_dl317_124a_chueferi", "water_level"),
    # ("bl_dl314_50sbw_acherm", "water_level"),
    ("bl_dl316_40g_csovoland", "water_level"),
    ("bl_dl318_597sbw_ara", "water_level"),
    ("bl_dl319_wildbach_rumlikonstr", "water_level"),
    # ("bl_dl321_48sbw_notuberlauf", "water_level"),
    ("bl_dl322_rub128inflow_usterstr", "water_level"),
    # ("bl_dl323_156a_geerenstr", "water_level"),
    ("bl_dl324_137_schutzengasse", "water_level"),
    ("bl_dl9449_15a_russikerstr", "water_level"),
    ("bl_plsZUH1201_inflow_ara", "water_level"),
    ("bl_plsRKPI1201_rubpw80sbw_industry", "water_level"),
    ("bl_plsRKBU1201_rub128basin_usterstr", "water_level"),
    ("bl_plsRKBM1203_rub_morg", "water_level"),
    ("bl_plsRKBM1201_rubmorg_inflow", "water_level"),
    ("bl_plsRKBA1201_rubbasin_ara", "water_level"),
    ("bl_plsRFBA1201_sk_ara", "water_level"),
    ("bl_lm064_rubpw80sbwbasin_industry", "water_level"),
    ("bl_lm065_7_kempttalstr", "water_level"),
    ("bl_lm069_ra40a_sbwvoland", "water_level"),
    # ("bl_lm078_581a_wildbach", "water_level"),
    ("bl_dl893_585sbw_amwildbach", "water_level"),
    # ("bl_ce463_vs22_kempttalstr", "water_level"),
    # ("bp_dl326_wildbach_kempttalstr", "pressure"),
    ("bp_dl327_luppmen_usterstr", "pressure"),
    ("bq_lpicm4_594_undermulistr", "inductive_conductivity"),
    # ("bq_lpicm5_rub128_schieber", "conductivity"),
    ("bm_dl328_sk_ara", "dielectric_permittivity"),
    ("bm_dl329_rub128basin_usterstr", "dielectric_permittivity"),
    ("bm_dl330_rub128inflow_usterstr", "dielectric_permittivity"),
    ("bm_dl332_rub_morg", "dielectric_permittivity"),
    # ("bm_dl333_vs22_kempttalstr", "dielectric_permittivity"),
    # ("bm_dl892_58sbw_undermulistr", "dielectric_permittivity"),
    # ("bm_lm067_ra40a_sbwvoland", "dielectric_permittivity"),
    ("bm_lm085_rubpw80sbwbasin_industry", "dielectric_permittivity"),
    ("bm_dl290_rubbasin_ara", "dielectric_permittivity"),
    # ("bm_dl291_rubbasin_ara", "dielectric_permittivity"),
    ("bt_dl906_pumpwgeeren_geerenstr", "ambient_air_temperature"),
    ("bt_dl907_rub_morg", "ambient_air_temperature"),
    ("bt_dl4185_voland_unterdorf", "headspace_temperature"),
    ("bt_dl916_inflow_ara", "water_temperature"),
    ("bt_dl917_162_luppmenweg", "water_temperature"),
    ("bt_dl923_166_luppmenweg", "water_temperature"),
    # ("bt_dl958_166_luppmenweg", "headspace_temperature"),
    ("bt_dl926_rubmorg_inflow", "water_temperature"),
    ("bt_dl927_164_luppmenweg", "headspace_temperature"),
    ("bt_dl928_164_luppmenweg", "headspace_temperature"),
    # ("bt_dl929_164_luppmenweg", "water_temperature"),
    # ("bt_dl930_40d_imberg", "water_temperature"),
    # ("bt_dl931_vs22_kempttalstr", "water_temperature"),
    ("bt_dl934_47a_zurcherstr", "water_temperature"),
    ("bt_dl935_15a_russikerstr", "water_temperature"),
    # ("bt_dl936_7_kempttalstr", "water_temperature"),
    # ("bt_dl937_58sbw_undermulistr", "water_temperature"),
    ("bt_dl938_124a_chueferi", "water_temperature"),
    ("bt_dl939_11h_veloweg", "water_temperature"),
    ("bt_dl941_585sbw_wildbach", "water_temperature"),
    ("bt_dl944_597sbw_ara", "water_temperature"),
    ("bt_dl945_156a_geerenstr", "water_temperature"),
    ("bt_dl946_555_mesikerstr", "water_temperature"),
    ("bt_dl948_rub128inflow_usterstr", "water_temperature"),
    # ("bt_dl954_rw137_schutzengasse", "water_temperature"),
    ("bt_dl955_594_undermulistr", "water_temperature"),
    ("bt_uit01_t1_rumpisweg", "soil_temperature"),
    ("bt_uit01_t2_rumpisweg", "soil_temperature"),
    ("bt_uit01_t3_rumpisweg", "soil_temperature"),
    ("bt_uit01_t4_rumpisweg", "soil_temperature"),
    ("bt_uit01_t5_rumpisweg", "soil_temperature"),
    ("bt_uit01_t6_rumpisweg", "soil_temperature"),
    # ("bf_f02_555_mesikerstr", "flow_rate"),
    # ("bf_f03_11e_russikerstr", "flow_rate"),
    ("bf_f07_23_bahnhofstr", "flow_rate"),
    ("bf_f08_166_luppmenweg", "flow_rate"),
    ("bf_f12_47a_zurcherstr", "flow_rate"),
    ("bf_plsRKBU1101_rub128basin_usterstr", "flow_rate"),
    ("bf_plsZUL1101_inflow_ara", "flow_rate"),
    ("bf_plsZUL1102_inflow_ara", "flow_rate"),
    # ("bf_plsZUL1100_inflow_ara", "flow_rate"),
    ("bf_plsRKPI1102_rubpw80sbw_overflow", "flow_rate"),
    ("bf_plsRKBU1102_rub128basin_overflow", "flow_rate"),
    ("bf_plsRKBA1101_rubbasin_ara_overflow", "flow_rate"),
    # ("bf_plsRKBM1101_rubmorg_outflow", "flow_rate"),
    ("bf_plsRKBM1101_3r_rub_morg_overflow", "flow_rate"),
    ("bn_r03_rub_morg", "rainfall_intensity"),
    ("bn_r04_airport_speck", "rainfall_intensity"),
    ("bn_r05_schutzenhaus_burgweg", "rainfall_intensity"),
    ("bn_plsALG1801E_ara_flatroof", "rainfall_intensity"),
    ("bn_dl797_rub_morg", "rainfall_intensity"),
    ("bn_dl798_electrosuisse_luppmenstr", "rainfall_intensity"),
    ("bn_dl799_ara_flatroof", "rainfall_intensity"),
    ("bn_dl800_pumpwau_rumlikerstr", "rainfall_intensity"),
    ("bn_dl801_pumpwgeeren_geerenstr", "rainfall_intensity"),
    ("bn_dl802_gerber_zurcherstr", "rainfall_intensity"),
    ("bn_dl803_coop_grundstr", "rainfall_intensity"),
    ("bn_dl259_rub_morg", "rainfall_intensity"),
]

ACTIVE_SIGNALS_BATTERY_LEVEL_DECENTLAB = [
    "bl_dl256_rubbasin_ara",
    "bl_dl309_sk102_wermatswilstr",
    "bl_dl310_sk_ara",
    "bl_dl316_40g_csovoland",
    "bl_dl319_wildbach_rumlikonstr",
    "bl_dl322_rub128inflow_usterstr",
    "bl_dl324_137_schutzengasse",
    "bm_dl290_rubbasin_ara",
    "bm_dl328_sk_ara",
    "bm_dl329_rub128basin_usterstr",
    "bm_dl330_rub128inflow_usterstr",
    "bm_dl332_rub_morg",
    "bm_lm085_rubpw80sbwbasin_industry",
    "bn_dl259_rub_morg",
    "bn_dl797_rub_morg",
    "bn_dl798_electrosuisse_luppmenstr",
    "bn_dl799_ara_flatroof",
    "bn_dl800_pumpwau_rumlikerstr",
    "bn_dl801_pumpwgeeren_geerenstr",
    "bn_dl802_gerber_zurcherstr",
    "bn_dl803_coop_grundstr",
    "bn_dl259_rub_morg",
]


ACTIVE_SIGNALS_BATTERY_LEVEL_RAIN_AND_FLOW = [
    "bn_r03_rub_morg",
    "bn_r04_airport_speck",
    "bn_r05_schutzenhaus_burgweg",
]


ACTIVE_SIGNALS_BATTERY_LEVEL_NIVUS = [
    "bf_f07_23_bahnhofstr",
    "bf_f08_166_luppmenweg",
    "bf_f12_47a_zurcherstr",
]


class Command(BaseCommand):
    help = "Add active signalchecks to database."

    def handle(self, *args, **options):
        
        # lastdataset = ParamSet(
        #     paramset_name="last_data_default",
        #     paramset_value={
        #         "days": 7,
        #     },
        # )
        # lastdataset.save()

        # for signal, variable in ALL_ACTIVE_SIGNALS:
        #     tmp = ActiveSignalCheck(
        #         source_name=signal,
        #         variable_name=variable,
        #         check_name="last_data",
        #         param_set=lastdataset,
        #     )
        #     tmp.save()

        # batterylevelset = ParamSet(
        #     paramset_name="battery_level_decentlab_nodes",
        #     paramset_value={
        #         "threshold": 2.1,
        #     },
        # )
        # batterylevelset.save()

        # for signal in ACTIVE_SIGNALS_BATTERY_LEVEL_DECENTLAB:
        #     asc = ActiveSignalCheck(
        #         source_name=signal,
        #         variable_name="battery_voltage",
        #         check_name="battery_level",
        #         param_set=batterylevelset,
        #     )
        #     asc.save()

        # batterylevelset2 = ParamSet(
        #     paramset_name="battery_level_rain_and_flow",
        #     paramset_value={
        #         "threshold": 12,
        #     },
        # )
        # batterylevelset2.save()

        # for signal in ACTIVE_SIGNALS_BATTERY_LEVEL_RAIN_AND_FLOW:
        #     asc = ActiveSignalCheck(
        #         source_name=signal,
        #         variable_name="battery_voltage",
        #         check_name="battery_level",
        #         param_set=batterylevelset2,
        #     )
        #     asc.save()

        # batterylevelset3 = ParamSet(
        #     paramset_name="battery_level_nivus",
        #     paramset_value={
        #         "threshold": 7,
        #     },
        # )
        # batterylevelset3.save()

        # for signal in ACTIVE_SIGNALS_BATTERY_LEVEL_NIVUS:
        #     asc = ActiveSignalCheck(
        #         source_name=signal,
        #         variable_name="battery_voltage",
        #         check_name="battery_level",
        #         param_set=batterylevelset3,
        #     )
        #     asc.save()

        # prsqos = ParamSet(
        #     paramset_name="prs_qos_default",
        #     paramset_value={
        #         "days": 100,
        #         "time_until_next_package_in_min": 5,
        #         "threshold": 70,
        #     },
        # )
        # prsqos.save()

        # for signal, variable in ALL_ACTIVE_SIGNALS:
        #     tmp = ActiveSignalCheck(
        #         source_name=signal,
        #         variable_name=variable,
        #         check_name="prs_qos",
        #         param_set=prsqos,
        #     )
        #     tmp.save()

        # rainsum = ParamSet(
        #     paramset_name="rain_sum_default",
        #     paramset_value={"max_difference": 5, "reference_sensors": ["bn_r03_rub_morg", "bn_r04_airport_speck", "bn_r05_schutzenhaus_burgweg"], "checked_sensors": ["bn_dl259_rub_morg", "bn_dl797_rub_morg", "bn_dl798_electrosuisse_luppmenstr", "bn_dl799_ara_flatroof", "bn_dl800_pumpwau_rumlikerstr", "bn_dl801_pumpwgeeren_geerenstr", "bn_dl802_gerber_zurcherstr", "bn_dl803_coop_grundstr", "bn_dl259_rub_morg"], "considered_time_window": 24, "max_reference_variance": 0.25},
        # )
        # rainsum.save()

        # tmp = ActiveSignalCheck(
        #     source_name="rain",
        #     variable_name="rainfall_intensity",
        #     check_name="rain_sum",
        #     param_set=rainsum,
        # )
        # tmp.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully created active signalchecks in db.")
        )
