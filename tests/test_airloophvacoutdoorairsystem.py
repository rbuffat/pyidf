import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.air_distribution import AirLoopHvacOutdoorAirSystem

log = logging.getLogger(__name__)

class TestAirLoopHvacOutdoorAirSystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacoutdoorairsystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacOutdoorAirSystem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_controller_list_name = "object-list|Controller List Name"
        obj.controller_list_name = var_controller_list_name
        # object-list
        var_outdoor_air_equipment_list_name = "object-list|Outdoor Air Equipment List Name"
        obj.outdoor_air_equipment_list_name = var_outdoor_air_equipment_list_name
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacoutdoorairsystems[0].name, var_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystems[0].controller_list_name, var_controller_list_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystems[0].outdoor_air_equipment_list_name, var_outdoor_air_equipment_list_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystems[0].availability_manager_list_name, var_availability_manager_list_name)