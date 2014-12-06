import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirSettingsThreeNodeDisplacementVentilation

log = logging.getLogger(__name__)

class TestRoomAirSettingsThreeNodeDisplacementVentilation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairsettingsthreenodedisplacementventilation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirSettingsThreeNodeDisplacementVentilation()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_gain_distribution_schedule_name = "object-list|Gain Distribution Schedule Name"
        obj.gain_distribution_schedule_name = var_gain_distribution_schedule_name
        # real
        var_number_of_plumes_per_occupant = 0.0001
        obj.number_of_plumes_per_occupant = var_number_of_plumes_per_occupant
        # real
        var_thermostat_height = 0.0001
        obj.thermostat_height = var_thermostat_height
        # real
        var_comfort_height = 0.0001
        obj.comfort_height = var_comfort_height
        # real
        var_temperature_difference_threshold_for_reporting = 0.0
        obj.temperature_difference_threshold_for_reporting = var_temperature_difference_threshold_for_reporting

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairsettingsthreenodedisplacementventilations[0].zone_name, var_zone_name)
        self.assertEqual(idf2.roomairsettingsthreenodedisplacementventilations[0].gain_distribution_schedule_name, var_gain_distribution_schedule_name)
        self.assertAlmostEqual(idf2.roomairsettingsthreenodedisplacementventilations[0].number_of_plumes_per_occupant, var_number_of_plumes_per_occupant)
        self.assertAlmostEqual(idf2.roomairsettingsthreenodedisplacementventilations[0].thermostat_height, var_thermostat_height)
        self.assertAlmostEqual(idf2.roomairsettingsthreenodedisplacementventilations[0].comfort_height, var_comfort_height)
        self.assertAlmostEqual(idf2.roomairsettingsthreenodedisplacementventilations[0].temperature_difference_threshold_for_reporting, var_temperature_difference_threshold_for_reporting)