import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.economics import UtilityCostTariff

log = logging.getLogger(__name__)

class TestUtilityCostTariff(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_utilitycosttariff(self):

        pyidf.validation_level = ValidationLevel.error

        obj = UtilityCostTariff()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # external-list
        var_output_meter_name = "external-list|Output Meter Name"
        obj.output_meter_name = var_output_meter_name
        # alpha
        var_conversion_factor_choice = "UserDefined"
        obj.conversion_factor_choice = var_conversion_factor_choice
        # real
        var_energy_conversion_factor = 4.4
        obj.energy_conversion_factor = var_energy_conversion_factor
        # real
        var_demand_conversion_factor = 5.5
        obj.demand_conversion_factor = var_demand_conversion_factor
        # object-list
        var_time_of_use_period_schedule_name = "object-list|Time of Use Period Schedule Name"
        obj.time_of_use_period_schedule_name = var_time_of_use_period_schedule_name
        # object-list
        var_season_schedule_name = "object-list|Season Schedule Name"
        obj.season_schedule_name = var_season_schedule_name
        # object-list
        var_month_schedule_name = "object-list|Month Schedule Name"
        obj.month_schedule_name = var_month_schedule_name
        # alpha
        var_demand_window_length = "QuarterHour"
        obj.demand_window_length = var_demand_window_length
        # alpha
        var_monthly_charge_or_variable_name = "Monthly Charge or Variable Name"
        obj.monthly_charge_or_variable_name = var_monthly_charge_or_variable_name
        # alpha
        var_minimum_monthly_charge_or_variable_name = "Minimum Monthly Charge or Variable Name"
        obj.minimum_monthly_charge_or_variable_name = var_minimum_monthly_charge_or_variable_name
        # object-list
        var_real_time_pricing_charge_schedule_name = "object-list|Real Time Pricing Charge Schedule Name"
        obj.real_time_pricing_charge_schedule_name = var_real_time_pricing_charge_schedule_name
        # object-list
        var_customer_baseline_load_schedule_name = "object-list|Customer Baseline Load Schedule Name"
        obj.customer_baseline_load_schedule_name = var_customer_baseline_load_schedule_name
        # alpha
        var_group_name = "Group Name"
        obj.group_name = var_group_name
        # alpha
        var_buy_or_sell = "BuyFromUtility"
        obj.buy_or_sell = var_buy_or_sell

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.utilitycosttariffs[0].name, var_name)
        self.assertEqual(idf2.utilitycosttariffs[0].output_meter_name, var_output_meter_name)
        self.assertEqual(idf2.utilitycosttariffs[0].conversion_factor_choice, var_conversion_factor_choice)
        self.assertAlmostEqual(idf2.utilitycosttariffs[0].energy_conversion_factor, var_energy_conversion_factor)
        self.assertAlmostEqual(idf2.utilitycosttariffs[0].demand_conversion_factor, var_demand_conversion_factor)
        self.assertEqual(idf2.utilitycosttariffs[0].time_of_use_period_schedule_name, var_time_of_use_period_schedule_name)
        self.assertEqual(idf2.utilitycosttariffs[0].season_schedule_name, var_season_schedule_name)
        self.assertEqual(idf2.utilitycosttariffs[0].month_schedule_name, var_month_schedule_name)
        self.assertEqual(idf2.utilitycosttariffs[0].demand_window_length, var_demand_window_length)
        self.assertEqual(idf2.utilitycosttariffs[0].monthly_charge_or_variable_name, var_monthly_charge_or_variable_name)
        self.assertEqual(idf2.utilitycosttariffs[0].minimum_monthly_charge_or_variable_name, var_minimum_monthly_charge_or_variable_name)
        self.assertEqual(idf2.utilitycosttariffs[0].real_time_pricing_charge_schedule_name, var_real_time_pricing_charge_schedule_name)
        self.assertEqual(idf2.utilitycosttariffs[0].customer_baseline_load_schedule_name, var_customer_baseline_load_schedule_name)
        self.assertEqual(idf2.utilitycosttariffs[0].group_name, var_group_name)
        self.assertEqual(idf2.utilitycosttariffs[0].buy_or_sell, var_buy_or_sell)