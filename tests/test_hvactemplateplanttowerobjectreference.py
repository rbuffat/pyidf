import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplatePlantTowerObjectReference

log = logging.getLogger(__name__)

class TestHvactemplatePlantTowerObjectReference(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplateplanttowerobjectreference(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplatePlantTowerObjectReference()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_cooling_tower_object_type = "CoolingTower:SingleSpeed"
        obj.cooling_tower_object_type = var_cooling_tower_object_type
        # object-list
        var_cooling_tower_name = "object-list|Cooling Tower Name"
        obj.cooling_tower_name = var_cooling_tower_name
        # real
        var_priority = 4.4
        obj.priority = var_priority
        # alpha
        var_template_plant_loop_type = "ChilledWater"
        obj.template_plant_loop_type = var_template_plant_loop_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplateplanttowerobjectreferences[0].name, var_name)
        self.assertEqual(idf2.hvactemplateplanttowerobjectreferences[0].cooling_tower_object_type, var_cooling_tower_object_type)
        self.assertEqual(idf2.hvactemplateplanttowerobjectreferences[0].cooling_tower_name, var_cooling_tower_name)
        self.assertAlmostEqual(idf2.hvactemplateplanttowerobjectreferences[0].priority, var_priority)
        self.assertEqual(idf2.hvactemplateplanttowerobjectreferences[0].template_plant_loop_type, var_template_plant_loop_type)