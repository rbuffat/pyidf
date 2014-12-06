import os
import tempfile
import unittest
import pyidf
from pyidf.economics import UtilityCostVariable
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestUtilityCostVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_utilitycostvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = UtilityCostVariable()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_tariff_name = "Tariff Name"
        obj.tariff_name = var_tariff_name
        # alpha
        var_variable_type = "Energy"
        obj.variable_type = var_variable_type
        # real
        var_january_value = 4.4
        obj.january_value = var_january_value
        # real
        var_february_value = 5.5
        obj.february_value = var_february_value
        # real
        var_march_value = 6.6
        obj.march_value = var_march_value
        # real
        var_april_value = 7.7
        obj.april_value = var_april_value
        # real
        var_may_value = 8.8
        obj.may_value = var_may_value
        # real
        var_june_value = 9.9
        obj.june_value = var_june_value
        # real
        var_july_value = 10.1
        obj.july_value = var_july_value
        # real
        var_august_value = 11.11
        obj.august_value = var_august_value
        # real
        var_september_value = 12.12
        obj.september_value = var_september_value
        # real
        var_october_value = 13.13
        obj.october_value = var_october_value
        # real
        var_november_value = 14.14
        obj.november_value = var_november_value
        # real
        var_december_value = 15.15
        obj.december_value = var_december_value

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.utilitycostvariables[0].name, var_name)
        self.assertEqual(idf2.utilitycostvariables[0].tariff_name, var_tariff_name)
        self.assertEqual(idf2.utilitycostvariables[0].variable_type, var_variable_type)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].january_value, var_january_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].february_value, var_february_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].march_value, var_march_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].april_value, var_april_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].may_value, var_may_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].june_value, var_june_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].july_value, var_july_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].august_value, var_august_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].september_value, var_september_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].october_value, var_october_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].november_value, var_november_value)
        self.assertAlmostEqual(idf2.utilitycostvariables[0].december_value, var_december_value)