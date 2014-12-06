import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.controllers import ControllerMechanicalVentilation

log = logging.getLogger(__name__)

class TestControllerMechanicalVentilation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_controllermechanicalventilation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ControllerMechanicalVentilation()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_demand_controlled_ventilation = "Yes"
        obj.demand_controlled_ventilation = var_demand_controlled_ventilation
        # alpha
        var_system_outdoor_air_method = "ZoneSum"
        obj.system_outdoor_air_method = var_system_outdoor_air_method
        # real
        var_zone_maximum_outdoor_air_fraction = 0.0001
        obj.zone_maximum_outdoor_air_fraction = var_zone_maximum_outdoor_air_fraction
        paras = []
        var_zone_1_name = "object-list|Zone 1 Name"
        paras.append(var_zone_1_name)
        var_design_specification_outdoor_air_object_name_1 = "object-list|Design Specification Outdoor Air Object Name 1"
        paras.append(var_design_specification_outdoor_air_object_name_1)
        var_design_specification_zone_air_distribution_object_name_1 = "object-list|Design Specification Zone Air Distribution Object Name 1"
        paras.append(var_design_specification_zone_air_distribution_object_name_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.controllermechanicalventilations[0].name, var_name)
        self.assertEqual(idf2.controllermechanicalventilations[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.controllermechanicalventilations[0].demand_controlled_ventilation, var_demand_controlled_ventilation)
        self.assertEqual(idf2.controllermechanicalventilations[0].system_outdoor_air_method, var_system_outdoor_air_method)
        self.assertAlmostEqual(idf2.controllermechanicalventilations[0].zone_maximum_outdoor_air_fraction, var_zone_maximum_outdoor_air_fraction)
        index = obj.extensible_field_index("Zone 1 Name")
        self.assertEqual(idf2.controllermechanicalventilations[0].extensibles[0][index], var_zone_1_name)
        index = obj.extensible_field_index("Design Specification Outdoor Air Object Name 1")
        self.assertEqual(idf2.controllermechanicalventilations[0].extensibles[0][index], var_design_specification_outdoor_air_object_name_1)
        index = obj.extensible_field_index("Design Specification Zone Air Distribution Object Name 1")
        self.assertEqual(idf2.controllermechanicalventilations[0].extensibles[0][index], var_design_specification_zone_air_distribution_object_name_1)