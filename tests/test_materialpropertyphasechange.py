import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import MaterialPropertyPhaseChange
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestMaterialPropertyPhaseChange(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialpropertyphasechange(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialPropertyPhaseChange()
        # object-list
        var_name = "object-list|Name"
        obj.name = var_name
        # real
        var_temperature_coefficient_for_thermal_conductivity = 2.2
        obj.temperature_coefficient_for_thermal_conductivity = var_temperature_coefficient_for_thermal_conductivity
        # real
        var_temperature_1 = 3.3
        obj.temperature_1 = var_temperature_1
        # real
        var_enthalpy_1 = 4.4
        obj.enthalpy_1 = var_enthalpy_1
        # real
        var_temperature_2 = 5.5
        obj.temperature_2 = var_temperature_2
        # real
        var_enthalpy_2 = 6.6
        obj.enthalpy_2 = var_enthalpy_2
        # real
        var_temperature_3 = 7.7
        obj.temperature_3 = var_temperature_3
        # real
        var_enthalpy_3 = 8.8
        obj.enthalpy_3 = var_enthalpy_3
        # real
        var_temperature_4 = 9.9
        obj.temperature_4 = var_temperature_4
        # real
        var_enthalpy_4 = 10.1
        obj.enthalpy_4 = var_enthalpy_4
        # real
        var_temperature_5 = 11.11
        obj.temperature_5 = var_temperature_5
        # real
        var_enthalpy_5 = 12.12
        obj.enthalpy_5 = var_enthalpy_5
        # real
        var_temperature_6 = 13.13
        obj.temperature_6 = var_temperature_6
        # real
        var_enthalpy_6 = 14.14
        obj.enthalpy_6 = var_enthalpy_6
        # real
        var_temperature_7 = 15.15
        obj.temperature_7 = var_temperature_7
        # real
        var_enthalpy_7 = 16.16
        obj.enthalpy_7 = var_enthalpy_7
        # real
        var_temperature_8 = 17.17
        obj.temperature_8 = var_temperature_8
        # real
        var_enthalpy_8 = 18.18
        obj.enthalpy_8 = var_enthalpy_8
        # real
        var_temperature_9 = 19.19
        obj.temperature_9 = var_temperature_9
        # real
        var_enthalpy_9 = 20.2
        obj.enthalpy_9 = var_enthalpy_9
        # real
        var_temperature_10 = 21.21
        obj.temperature_10 = var_temperature_10
        # real
        var_enthalpy_10 = 22.22
        obj.enthalpy_10 = var_enthalpy_10
        # real
        var_temperature_11 = 23.23
        obj.temperature_11 = var_temperature_11
        # real
        var_enthalpy_11 = 24.24
        obj.enthalpy_11 = var_enthalpy_11
        # real
        var_temperature_12 = 25.25
        obj.temperature_12 = var_temperature_12
        # real
        var_enthalpy_12 = 26.26
        obj.enthalpy_12 = var_enthalpy_12
        # real
        var_temperature_13 = 27.27
        obj.temperature_13 = var_temperature_13
        # real
        var_enthalpy_13 = 28.28
        obj.enthalpy_13 = var_enthalpy_13
        # real
        var_temperature_14 = 29.29
        obj.temperature_14 = var_temperature_14
        # real
        var_enthalpy_14 = 30.3
        obj.enthalpy_14 = var_enthalpy_14
        # real
        var_temperature_15 = 31.31
        obj.temperature_15 = var_temperature_15
        # real
        var_enthalpy_15 = 32.32
        obj.enthalpy_15 = var_enthalpy_15
        # real
        var_temperature_16 = 33.33
        obj.temperature_16 = var_temperature_16
        # real
        var_enthalpy_16 = 34.34
        obj.enthalpy_16 = var_enthalpy_16

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialpropertyphasechanges[0].name, var_name)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_coefficient_for_thermal_conductivity, var_temperature_coefficient_for_thermal_conductivity)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_1, var_temperature_1)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_1, var_enthalpy_1)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_2, var_temperature_2)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_2, var_enthalpy_2)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_3, var_temperature_3)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_3, var_enthalpy_3)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_4, var_temperature_4)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_4, var_enthalpy_4)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_5, var_temperature_5)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_5, var_enthalpy_5)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_6, var_temperature_6)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_6, var_enthalpy_6)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_7, var_temperature_7)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_7, var_enthalpy_7)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_8, var_temperature_8)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_8, var_enthalpy_8)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_9, var_temperature_9)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_9, var_enthalpy_9)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_10, var_temperature_10)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_10, var_enthalpy_10)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_11, var_temperature_11)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_11, var_enthalpy_11)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_12, var_temperature_12)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_12, var_enthalpy_12)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_13, var_temperature_13)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_13, var_enthalpy_13)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_14, var_temperature_14)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_14, var_enthalpy_14)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_15, var_temperature_15)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_15, var_enthalpy_15)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].temperature_16, var_temperature_16)
        self.assertAlmostEqual(idf2.materialpropertyphasechanges[0].enthalpy_16, var_enthalpy_16)