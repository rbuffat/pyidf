import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirTemperaturePatternTwoGradient

log = logging.getLogger(__name__)

class TestRoomAirTemperaturePatternTwoGradient(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairtemperaturepatterntwogradient(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirTemperaturePatternTwoGradient()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # integer
        var_control_integer_for_pattern_control_schedule_name = 2
        obj.control_integer_for_pattern_control_schedule_name = var_control_integer_for_pattern_control_schedule_name
        # real
        var_thermostat_height = 3.3
        obj.thermostat_height = var_thermostat_height
        # real
        var_return_air_height = 4.4
        obj.return_air_height = var_return_air_height
        # real
        var_exhaust_air_height = 5.5
        obj.exhaust_air_height = var_exhaust_air_height
        # real
        var_temperature_gradient_lower_bound = 6.6
        obj.temperature_gradient_lower_bound = var_temperature_gradient_lower_bound
        # real
        var_temperature_gradient_upper_bound = 7.7
        obj.temperature_gradient_upper_bound = var_temperature_gradient_upper_bound
        # alpha
        var_gradient_interpolation_mode = "OutdoorDryBulbTemperature"
        obj.gradient_interpolation_mode = var_gradient_interpolation_mode
        # real
        var_upper_temperature_bound = 9.9
        obj.upper_temperature_bound = var_upper_temperature_bound
        # real
        var_lower_temperature_bound = 10.1
        obj.lower_temperature_bound = var_lower_temperature_bound
        # real
        var_upper_heat_rate_bound = 11.11
        obj.upper_heat_rate_bound = var_upper_heat_rate_bound
        # real
        var_lower_heat_rate_bound = 12.12
        obj.lower_heat_rate_bound = var_lower_heat_rate_bound

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairtemperaturepatterntwogradients[0].name, var_name)
        self.assertEqual(idf2.roomairtemperaturepatterntwogradients[0].control_integer_for_pattern_control_schedule_name, var_control_integer_for_pattern_control_schedule_name)
        self.assertAlmostEqual(idf2.roomairtemperaturepatterntwogradients[0].thermostat_height, var_thermostat_height)
        self.assertAlmostEqual(idf2.roomairtemperaturepatterntwogradients[0].return_air_height, var_return_air_height)
        self.assertAlmostEqual(idf2.roomairtemperaturepatterntwogradients[0].exhaust_air_height, var_exhaust_air_height)
        self.assertAlmostEqual(idf2.roomairtemperaturepatterntwogradients[0].temperature_gradient_lower_bound, var_temperature_gradient_lower_bound)
        self.assertAlmostEqual(idf2.roomairtemperaturepatterntwogradients[0].temperature_gradient_upper_bound, var_temperature_gradient_upper_bound)
        self.assertEqual(idf2.roomairtemperaturepatterntwogradients[0].gradient_interpolation_mode, var_gradient_interpolation_mode)
        self.assertAlmostEqual(idf2.roomairtemperaturepatterntwogradients[0].upper_temperature_bound, var_upper_temperature_bound)
        self.assertAlmostEqual(idf2.roomairtemperaturepatterntwogradients[0].lower_temperature_bound, var_lower_temperature_bound)
        self.assertAlmostEqual(idf2.roomairtemperaturepatterntwogradients[0].upper_heat_rate_bound, var_upper_heat_rate_bound)
        self.assertAlmostEqual(idf2.roomairtemperaturepatterntwogradients[0].lower_heat_rate_bound, var_lower_heat_rate_bound)