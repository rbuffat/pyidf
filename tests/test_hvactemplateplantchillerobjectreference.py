import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplatePlantChillerObjectReference
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplatePlantChillerObjectReference(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplateplantchillerobjectreference(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplatePlantChillerObjectReference()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_chiller_object_type = "Chiller:Electric:EIR"
        obj.chiller_object_type = var_chiller_object_type
        # object-list
        var_chiller_name = "object-list|Chiller Name"
        obj.chiller_name = var_chiller_name
        # real
        var_priority = 4.4
        obj.priority = var_priority

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplateplantchillerobjectreferences[0].name, var_name)
        self.assertEqual(idf2.hvactemplateplantchillerobjectreferences[0].chiller_object_type, var_chiller_object_type)
        self.assertEqual(idf2.hvactemplateplantchillerobjectreferences[0].chiller_name, var_chiller_name)
        self.assertAlmostEqual(idf2.hvactemplateplantchillerobjectreferences[0].priority, var_priority)