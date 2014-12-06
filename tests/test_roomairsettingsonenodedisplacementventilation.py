import os
import tempfile
import unittest
import pyidf
from pyidf.room_air_models import RoomAirSettingsOneNodeDisplacementVentilation
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRoomAirSettingsOneNodeDisplacementVentilation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairsettingsonenodedisplacementventilation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirSettingsOneNodeDisplacementVentilation()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_fraction_of_convective_internal_loads_added_to_floor_air = 0.5
        obj.fraction_of_convective_internal_loads_added_to_floor_air = var_fraction_of_convective_internal_loads_added_to_floor_air
        # real
        var_fraction_of_infiltration_internal_loads_added_to_floor_air = 0.5
        obj.fraction_of_infiltration_internal_loads_added_to_floor_air = var_fraction_of_infiltration_internal_loads_added_to_floor_air

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairsettingsonenodedisplacementventilations[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.roomairsettingsonenodedisplacementventilations[0].fraction_of_convective_internal_loads_added_to_floor_air, var_fraction_of_convective_internal_loads_added_to_floor_air)
        self.assertAlmostEqual(idf2.roomairsettingsonenodedisplacementventilations[0].fraction_of_infiltration_internal_loads_added_to_floor_air, var_fraction_of_infiltration_internal_loads_added_to_floor_air)