import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirTemperaturePatternUserDefined

log = logging.getLogger(__name__)

class TestRoomAirTemperaturePatternUserDefined(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairtemperaturepatternuserdefined(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirTemperaturePatternUserDefined()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_pattern_control_schedule_name = "object-list|Pattern Control Schedule Name"
        obj.pattern_control_schedule_name = var_pattern_control_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairtemperaturepatternuserdefineds[0].name, var_name)
        self.assertEqual(idf2.roomairtemperaturepatternuserdefineds[0].zone_name, var_zone_name)
        self.assertEqual(idf2.roomairtemperaturepatternuserdefineds[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.roomairtemperaturepatternuserdefineds[0].pattern_control_schedule_name, var_pattern_control_schedule_name)