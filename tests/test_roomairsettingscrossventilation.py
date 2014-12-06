import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirSettingsCrossVentilation

log = logging.getLogger(__name__)

class TestRoomAirSettingsCrossVentilation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairsettingscrossventilation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirSettingsCrossVentilation()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_gain_distribution_schedule_name = "object-list|Gain Distribution Schedule Name"
        obj.gain_distribution_schedule_name = var_gain_distribution_schedule_name
        # alpha
        var_airflow_region_used_for_thermal_comfort_evaluation = "Jet"
        obj.airflow_region_used_for_thermal_comfort_evaluation = var_airflow_region_used_for_thermal_comfort_evaluation

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairsettingscrossventilations[0].zone_name, var_zone_name)
        self.assertEqual(idf2.roomairsettingscrossventilations[0].gain_distribution_schedule_name, var_gain_distribution_schedule_name)
        self.assertEqual(idf2.roomairsettingscrossventilations[0].airflow_region_used_for_thermal_comfort_evaluation, var_airflow_region_used_for_thermal_comfort_evaluation)