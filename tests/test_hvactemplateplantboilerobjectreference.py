import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplatePlantBoilerObjectReference
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplatePlantBoilerObjectReference(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplateplantboilerobjectreference(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplatePlantBoilerObjectReference()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_boiler_object_type = "Boiler:HotWater"
        obj.boiler_object_type = var_boiler_object_type
        # object-list
        var_boiler_name = "object-list|Boiler Name"
        obj.boiler_name = var_boiler_name
        # real
        var_priority = 4.4
        obj.priority = var_priority
        # alpha
        var_template_plant_loop_type = "HotWater"
        obj.template_plant_loop_type = var_template_plant_loop_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplateplantboilerobjectreferences[0].name, var_name)
        self.assertEqual(idf2.hvactemplateplantboilerobjectreferences[0].boiler_object_type, var_boiler_object_type)
        self.assertEqual(idf2.hvactemplateplantboilerobjectreferences[0].boiler_name, var_boiler_name)
        self.assertAlmostEqual(idf2.hvactemplateplantboilerobjectreferences[0].priority, var_priority)
        self.assertEqual(idf2.hvactemplateplantboilerobjectreferences[0].template_plant_loop_type, var_template_plant_loop_type)