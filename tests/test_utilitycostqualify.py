import os
import tempfile
import unittest
import pyidf
from pyidf.economics import UtilityCostQualify
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestUtilityCostQualify(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_utilitycostqualify(self):

        pyidf.validation_level = ValidationLevel.error

        obj = UtilityCostQualify()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_tariff_name = "Tariff Name"
        obj.tariff_name = var_tariff_name
        # alpha
        var_variable_name = "Variable Name"
        obj.variable_name = var_variable_name
        # alpha
        var_qualify_type = "Minimum"
        obj.qualify_type = var_qualify_type
        # alpha
        var_threshold_value_or_variable_name = "Threshold Value or Variable Name"
        obj.threshold_value_or_variable_name = var_threshold_value_or_variable_name
        # alpha
        var_season = "Annual"
        obj.season = var_season
        # alpha
        var_threshold_test = "Count"
        obj.threshold_test = var_threshold_test
        # real
        var_number_of_months = 6.5
        obj.number_of_months = var_number_of_months

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.utilitycostqualifys[0].name, var_name)
        self.assertEqual(idf2.utilitycostqualifys[0].tariff_name, var_tariff_name)
        self.assertEqual(idf2.utilitycostqualifys[0].variable_name, var_variable_name)
        self.assertEqual(idf2.utilitycostqualifys[0].qualify_type, var_qualify_type)
        self.assertEqual(idf2.utilitycostqualifys[0].threshold_value_or_variable_name, var_threshold_value_or_variable_name)
        self.assertEqual(idf2.utilitycostqualifys[0].season, var_season)
        self.assertEqual(idf2.utilitycostqualifys[0].threshold_test, var_threshold_test)
        self.assertAlmostEqual(idf2.utilitycostqualifys[0].number_of_months, var_number_of_months)