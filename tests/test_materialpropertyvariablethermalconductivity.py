import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import MaterialPropertyVariableThermalConductivity

log = logging.getLogger(__name__)

class TestMaterialPropertyVariableThermalConductivity(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialpropertyvariablethermalconductivity(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialPropertyVariableThermalConductivity()
        # object-list
        var_name = "object-list|Name"
        obj.name = var_name
        # real
        var_temperature_1 = 2.2
        obj.temperature_1 = var_temperature_1
        # real
        var_thermal_conductivity_1 = 3.3
        obj.thermal_conductivity_1 = var_thermal_conductivity_1
        # real
        var_temperature_2 = 4.4
        obj.temperature_2 = var_temperature_2
        # real
        var_thermal_conductivity_2 = 5.5
        obj.thermal_conductivity_2 = var_thermal_conductivity_2
        # real
        var_temperature_3 = 6.6
        obj.temperature_3 = var_temperature_3
        # real
        var_thermal_conductivity_3 = 7.7
        obj.thermal_conductivity_3 = var_thermal_conductivity_3
        # real
        var_temperature_4 = 8.8
        obj.temperature_4 = var_temperature_4
        # real
        var_thermal_conductivity_4 = 9.9
        obj.thermal_conductivity_4 = var_thermal_conductivity_4
        # real
        var_temperature_5 = 10.1
        obj.temperature_5 = var_temperature_5
        # real
        var_thermal_conductivity_5 = 11.11
        obj.thermal_conductivity_5 = var_thermal_conductivity_5
        # real
        var_temperature_6 = 12.12
        obj.temperature_6 = var_temperature_6
        # real
        var_thermal_conductivity_6 = 13.13
        obj.thermal_conductivity_6 = var_thermal_conductivity_6
        # real
        var_temperature_7 = 14.14
        obj.temperature_7 = var_temperature_7
        # real
        var_thermal_conductivity_7 = 15.15
        obj.thermal_conductivity_7 = var_thermal_conductivity_7
        # real
        var_temperature_8 = 16.16
        obj.temperature_8 = var_temperature_8
        # real
        var_thermal_conductivity_8 = 17.17
        obj.thermal_conductivity_8 = var_thermal_conductivity_8
        # real
        var_temperature_9 = 18.18
        obj.temperature_9 = var_temperature_9
        # real
        var_thermal_conductivity_9 = 19.19
        obj.thermal_conductivity_9 = var_thermal_conductivity_9
        # real
        var_temperature_10 = 20.2
        obj.temperature_10 = var_temperature_10
        # real
        var_thermal_conductivity_10 = 21.21
        obj.thermal_conductivity_10 = var_thermal_conductivity_10

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialpropertyvariablethermalconductivitys[0].name, var_name)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].temperature_1, var_temperature_1)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].thermal_conductivity_1, var_thermal_conductivity_1)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].temperature_2, var_temperature_2)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].thermal_conductivity_2, var_thermal_conductivity_2)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].temperature_3, var_temperature_3)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].thermal_conductivity_3, var_thermal_conductivity_3)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].temperature_4, var_temperature_4)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].thermal_conductivity_4, var_thermal_conductivity_4)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].temperature_5, var_temperature_5)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].thermal_conductivity_5, var_thermal_conductivity_5)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].temperature_6, var_temperature_6)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].thermal_conductivity_6, var_thermal_conductivity_6)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].temperature_7, var_temperature_7)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].thermal_conductivity_7, var_thermal_conductivity_7)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].temperature_8, var_temperature_8)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].thermal_conductivity_8, var_thermal_conductivity_8)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].temperature_9, var_temperature_9)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].thermal_conductivity_9, var_thermal_conductivity_9)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].temperature_10, var_temperature_10)
        self.assertAlmostEqual(idf2.materialpropertyvariablethermalconductivitys[0].thermal_conductivity_10, var_thermal_conductivity_10)