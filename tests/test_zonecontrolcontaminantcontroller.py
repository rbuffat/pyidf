import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_controls_and_thermostats import ZoneControlContaminantController

log = logging.getLogger(__name__)

class TestZoneControlContaminantController(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontrolcontaminantcontroller(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneControlContaminantController()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_controlled_zone_name = "object-list|Controlled Zone Name"
        obj.controlled_zone_name = var_controlled_zone_name
        # object-list
        var_carbon_dioxide_control_availability_schedule_name = "object-list|Carbon Dioxide Control Availability Schedule Name"
        obj.carbon_dioxide_control_availability_schedule_name = var_carbon_dioxide_control_availability_schedule_name
        # object-list
        var_carbon_dioxide_setpoint_schedule_name = "object-list|Carbon Dioxide Setpoint Schedule Name"
        obj.carbon_dioxide_setpoint_schedule_name = var_carbon_dioxide_setpoint_schedule_name
        # object-list
        var_minimum_carbon_dioxide_concentration_schedule_name = "object-list|Minimum Carbon Dioxide Concentration Schedule Name"
        obj.minimum_carbon_dioxide_concentration_schedule_name = var_minimum_carbon_dioxide_concentration_schedule_name
        # object-list
        var_generic_contaminant_control_availability_schedule_name = "object-list|Generic Contaminant Control Availability Schedule Name"
        obj.generic_contaminant_control_availability_schedule_name = var_generic_contaminant_control_availability_schedule_name
        # object-list
        var_generic_contaminant_setpoint_schedule_name = "object-list|Generic Contaminant Setpoint Schedule Name"
        obj.generic_contaminant_setpoint_schedule_name = var_generic_contaminant_setpoint_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontrolcontaminantcontrollers[0].name, var_name)
        self.assertEqual(idf2.zonecontrolcontaminantcontrollers[0].controlled_zone_name, var_controlled_zone_name)
        self.assertEqual(idf2.zonecontrolcontaminantcontrollers[0].carbon_dioxide_control_availability_schedule_name, var_carbon_dioxide_control_availability_schedule_name)
        self.assertEqual(idf2.zonecontrolcontaminantcontrollers[0].carbon_dioxide_setpoint_schedule_name, var_carbon_dioxide_setpoint_schedule_name)
        self.assertEqual(idf2.zonecontrolcontaminantcontrollers[0].minimum_carbon_dioxide_concentration_schedule_name, var_minimum_carbon_dioxide_concentration_schedule_name)
        self.assertEqual(idf2.zonecontrolcontaminantcontrollers[0].generic_contaminant_control_availability_schedule_name, var_generic_contaminant_control_availability_schedule_name)
        self.assertEqual(idf2.zonecontrolcontaminantcontrollers[0].generic_contaminant_setpoint_schedule_name, var_generic_contaminant_setpoint_schedule_name)