import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirTemperaturePatternConstantGradient

log = logging.getLogger(__name__)

class TestRoomAirTemperaturePatternConstantGradient(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairtemperaturepatternconstantgradient(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirTemperaturePatternConstantGradient()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # integer
        var_control_integer_for_pattern_control_schedule_name = 2
        obj.control_integer_for_pattern_control_schedule_name = var_control_integer_for_pattern_control_schedule_name
        # real
        var_thermostat_offset = 3.3
        obj.thermostat_offset = var_thermostat_offset
        # real
        var_return_air_offset = 4.4
        obj.return_air_offset = var_return_air_offset
        # real
        var_exhaust_air_offset = 5.5
        obj.exhaust_air_offset = var_exhaust_air_offset
        # real
        var_temperature_gradient = 6.6
        obj.temperature_gradient = var_temperature_gradient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairtemperaturepatternconstantgradients[0].name, var_name)
        self.assertEqual(idf2.roomairtemperaturepatternconstantgradients[0].control_integer_for_pattern_control_schedule_name, var_control_integer_for_pattern_control_schedule_name)
        self.assertAlmostEqual(idf2.roomairtemperaturepatternconstantgradients[0].thermostat_offset, var_thermostat_offset)
        self.assertAlmostEqual(idf2.roomairtemperaturepatternconstantgradients[0].return_air_offset, var_return_air_offset)
        self.assertAlmostEqual(idf2.roomairtemperaturepatternconstantgradients[0].exhaust_air_offset, var_exhaust_air_offset)
        self.assertAlmostEqual(idf2.roomairtemperaturepatternconstantgradients[0].temperature_gradient, var_temperature_gradient)