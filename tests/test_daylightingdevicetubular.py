import os
import tempfile
import unittest
import pyidf
from pyidf.daylighting import DaylightingDeviceTubular
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestDaylightingDeviceTubular(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_daylightingdevicetubular(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DaylightingDeviceTubular()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_dome_name = "object-list|Dome Name"
        obj.dome_name = var_dome_name
        # object-list
        var_diffuser_name = "object-list|Diffuser Name"
        obj.diffuser_name = var_diffuser_name
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # real
        var_diameter = 0.0001
        obj.diameter = var_diameter
        # real
        var_total_length = 0.0001
        obj.total_length = var_total_length
        # real
        var_effective_thermal_resistance = 0.0001
        obj.effective_thermal_resistance = var_effective_thermal_resistance
        paras = []
        var_transition_zone_1_name = "object-list|Transition Zone 1 Name"
        paras.append(var_transition_zone_1_name)
        var_transition_zone_1_length = 0.0
        paras.append(var_transition_zone_1_length)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.daylightingdevicetubulars[0].name, var_name)
        self.assertEqual(idf2.daylightingdevicetubulars[0].dome_name, var_dome_name)
        self.assertEqual(idf2.daylightingdevicetubulars[0].diffuser_name, var_diffuser_name)
        self.assertEqual(idf2.daylightingdevicetubulars[0].construction_name, var_construction_name)
        self.assertAlmostEqual(idf2.daylightingdevicetubulars[0].diameter, var_diameter)
        self.assertAlmostEqual(idf2.daylightingdevicetubulars[0].total_length, var_total_length)
        self.assertAlmostEqual(idf2.daylightingdevicetubulars[0].effective_thermal_resistance, var_effective_thermal_resistance)
        index = obj.extensible_field_index("Transition Zone 1 Name")
        self.assertEqual(idf2.daylightingdevicetubulars[0].extensibles[0][index], var_transition_zone_1_name)
        index = obj.extensible_field_index("Transition Zone 1 Length")
        self.assertAlmostEqual(idf2.daylightingdevicetubulars[0].extensibles[0][index], var_transition_zone_1_length)