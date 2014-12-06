import os
import tempfile
import unittest
import pyidf
from pyidf.room_air_models import RoomAirTemperaturePatternSurfaceMapping
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRoomAirTemperaturePatternSurfaceMapping(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairtemperaturepatternsurfacemapping(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirTemperaturePatternSurfaceMapping()
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
        paras = []
        var_surface_name_pair_1 = "object-list|Surface Name Pair 1"
        paras.append(var_surface_name_pair_1)
        var_delta_adjacent_air_temperature_pair_1 = 7.7
        paras.append(var_delta_adjacent_air_temperature_pair_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairtemperaturepatternsurfacemappings[0].name, var_name)
        self.assertEqual(idf2.roomairtemperaturepatternsurfacemappings[0].control_integer_for_pattern_control_schedule_name, var_control_integer_for_pattern_control_schedule_name)
        self.assertAlmostEqual(idf2.roomairtemperaturepatternsurfacemappings[0].thermostat_offset, var_thermostat_offset)
        self.assertAlmostEqual(idf2.roomairtemperaturepatternsurfacemappings[0].return_air_offset, var_return_air_offset)
        self.assertAlmostEqual(idf2.roomairtemperaturepatternsurfacemappings[0].exhaust_air_offset, var_exhaust_air_offset)
        index = obj.extensible_field_index("Surface Name Pair 1")
        self.assertEqual(idf2.roomairtemperaturepatternsurfacemappings[0].extensibles[0][index], var_surface_name_pair_1)
        index = obj.extensible_field_index("Delta Adjacent Air Temperature Pair 1")
        self.assertAlmostEqual(idf2.roomairtemperaturepatternsurfacemappings[0].extensibles[0][index], var_delta_adjacent_air_temperature_pair_1)