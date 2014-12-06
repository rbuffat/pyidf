import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import MaterialPropertyMoisturePenetrationDepthSettings

log = logging.getLogger(__name__)

class TestMaterialPropertyMoisturePenetrationDepthSettings(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialpropertymoisturepenetrationdepthsettings(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialPropertyMoisturePenetrationDepthSettings()
        # object-list
        var_name = "object-list|Name"
        obj.name = var_name
        # real
        var_moisture_penetration_depth = 0.0
        obj.moisture_penetration_depth = var_moisture_penetration_depth
        # real
        var_moisture_equation_coefficient_a = 3.3
        obj.moisture_equation_coefficient_a = var_moisture_equation_coefficient_a
        # real
        var_moisture_equation_coefficient_b = 4.4
        obj.moisture_equation_coefficient_b = var_moisture_equation_coefficient_b
        # real
        var_moisture_equation_coefficient_c = 5.5
        obj.moisture_equation_coefficient_c = var_moisture_equation_coefficient_c
        # real
        var_moisture_equation_coefficient_d = 6.6
        obj.moisture_equation_coefficient_d = var_moisture_equation_coefficient_d

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialpropertymoisturepenetrationdepthsettingss[0].name, var_name)
        self.assertAlmostEqual(idf2.materialpropertymoisturepenetrationdepthsettingss[0].moisture_penetration_depth, var_moisture_penetration_depth)
        self.assertAlmostEqual(idf2.materialpropertymoisturepenetrationdepthsettingss[0].moisture_equation_coefficient_a, var_moisture_equation_coefficient_a)
        self.assertAlmostEqual(idf2.materialpropertymoisturepenetrationdepthsettingss[0].moisture_equation_coefficient_b, var_moisture_equation_coefficient_b)
        self.assertAlmostEqual(idf2.materialpropertymoisturepenetrationdepthsettingss[0].moisture_equation_coefficient_c, var_moisture_equation_coefficient_c)
        self.assertAlmostEqual(idf2.materialpropertymoisturepenetrationdepthsettingss[0].moisture_equation_coefficient_d, var_moisture_equation_coefficient_d)