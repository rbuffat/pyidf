import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_forced_air_units import ZoneHvacEnergyRecoveryVentilatorController

log = logging.getLogger(__name__)

class TestZoneHvacEnergyRecoveryVentilatorController(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacenergyrecoveryventilatorcontroller(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacEnergyRecoveryVentilatorController()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_temperature_high_limit = 2.2
        obj.temperature_high_limit = var_temperature_high_limit
        # real
        var_temperature_low_limit = 3.3
        obj.temperature_low_limit = var_temperature_low_limit
        # real
        var_enthalpy_high_limit = 4.4
        obj.enthalpy_high_limit = var_enthalpy_high_limit
        # real
        var_dewpoint_temperature_limit = 5.5
        obj.dewpoint_temperature_limit = var_dewpoint_temperature_limit
        # object-list
        var_electronic_enthalpy_limit_curve_name = "object-list|Electronic Enthalpy Limit Curve Name"
        obj.electronic_enthalpy_limit_curve_name = var_electronic_enthalpy_limit_curve_name
        # alpha
        var_exhaust_air_temperature_limit = "ExhaustAirTemperatureLimit"
        obj.exhaust_air_temperature_limit = var_exhaust_air_temperature_limit
        # alpha
        var_exhaust_air_enthalpy_limit = "ExhaustAirEnthalpyLimit"
        obj.exhaust_air_enthalpy_limit = var_exhaust_air_enthalpy_limit
        # object-list
        var_time_of_day_economizer_flow_control_schedule_name = "object-list|Time of Day Economizer Flow Control Schedule Name"
        obj.time_of_day_economizer_flow_control_schedule_name = var_time_of_day_economizer_flow_control_schedule_name
        # alpha
        var_high_humidity_control_flag = "Yes"
        obj.high_humidity_control_flag = var_high_humidity_control_flag
        # object-list
        var_humidistat_control_zone_name = "object-list|Humidistat Control Zone Name"
        obj.humidistat_control_zone_name = var_humidistat_control_zone_name
        # real
        var_high_humidity_outdoor_air_flow_ratio = 0.0001
        obj.high_humidity_outdoor_air_flow_ratio = var_high_humidity_outdoor_air_flow_ratio
        # alpha
        var_control_high_indoor_humidity_based_on_outdoor_humidity_ratio = "Yes"
        obj.control_high_indoor_humidity_based_on_outdoor_humidity_ratio = var_control_high_indoor_humidity_based_on_outdoor_humidity_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].name, var_name)
        self.assertAlmostEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].temperature_high_limit, var_temperature_high_limit)
        self.assertAlmostEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].temperature_low_limit, var_temperature_low_limit)
        self.assertAlmostEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].enthalpy_high_limit, var_enthalpy_high_limit)
        self.assertAlmostEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].dewpoint_temperature_limit, var_dewpoint_temperature_limit)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].electronic_enthalpy_limit_curve_name, var_electronic_enthalpy_limit_curve_name)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].exhaust_air_temperature_limit, var_exhaust_air_temperature_limit)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].exhaust_air_enthalpy_limit, var_exhaust_air_enthalpy_limit)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].time_of_day_economizer_flow_control_schedule_name, var_time_of_day_economizer_flow_control_schedule_name)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].high_humidity_control_flag, var_high_humidity_control_flag)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].humidistat_control_zone_name, var_humidistat_control_zone_name)
        self.assertAlmostEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].high_humidity_outdoor_air_flow_ratio, var_high_humidity_outdoor_air_flow_ratio)
        self.assertEqual(idf2.zonehvacenergyrecoveryventilatorcontrollers[0].control_high_indoor_humidity_based_on_outdoor_humidity_ratio, var_control_high_indoor_humidity_based_on_outdoor_humidity_ratio)