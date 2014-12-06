import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_controls_and_thermostats import ZoneControlThermostatTemperatureAndHumidity

log = logging.getLogger(__name__)

class TestZoneControlThermostatTemperatureAndHumidity(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontrolthermostattemperatureandhumidity(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneControlThermostatTemperatureAndHumidity()
        # object-list
        var_thermostat_name = "object-list|Thermostat Name"
        obj.thermostat_name = var_thermostat_name
        # object-list
        var_dehumidifying_relative_humidity_setpoint_schedule_name = "object-list|Dehumidifying Relative Humidity Setpoint Schedule Name"
        obj.dehumidifying_relative_humidity_setpoint_schedule_name = var_dehumidifying_relative_humidity_setpoint_schedule_name
        # alpha
        var_dehumidification_control_type = "Overcool"
        obj.dehumidification_control_type = var_dehumidification_control_type
        # alpha
        var_overcool_range_input_method = "Constant"
        obj.overcool_range_input_method = var_overcool_range_input_method
        # real
        var_overcool_constant_range = 1.5
        obj.overcool_constant_range = var_overcool_constant_range
        # object-list
        var_overcool_range_schedule_name = "object-list|Overcool Range Schedule Name"
        obj.overcool_range_schedule_name = var_overcool_range_schedule_name
        # real
        var_overcool_control_ratio = 0.0
        obj.overcool_control_ratio = var_overcool_control_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontrolthermostattemperatureandhumiditys[0].thermostat_name, var_thermostat_name)
        self.assertEqual(idf2.zonecontrolthermostattemperatureandhumiditys[0].dehumidifying_relative_humidity_setpoint_schedule_name, var_dehumidifying_relative_humidity_setpoint_schedule_name)
        self.assertEqual(idf2.zonecontrolthermostattemperatureandhumiditys[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertEqual(idf2.zonecontrolthermostattemperatureandhumiditys[0].overcool_range_input_method, var_overcool_range_input_method)
        self.assertAlmostEqual(idf2.zonecontrolthermostattemperatureandhumiditys[0].overcool_constant_range, var_overcool_constant_range)
        self.assertEqual(idf2.zonecontrolthermostattemperatureandhumiditys[0].overcool_range_schedule_name, var_overcool_range_schedule_name)
        self.assertAlmostEqual(idf2.zonecontrolthermostattemperatureandhumiditys[0].overcool_control_ratio, var_overcool_control_ratio)