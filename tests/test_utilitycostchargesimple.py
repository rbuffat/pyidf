import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.economics import UtilityCostChargeSimple

log = logging.getLogger(__name__)

class TestUtilityCostChargeSimple(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_utilitycostchargesimple(self):

        pyidf.validation_level = ValidationLevel.error

        obj = UtilityCostChargeSimple()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_tariff_name = "object-list|Tariff Name"
        obj.tariff_name = var_tariff_name
        # alpha
        var_source_variable = "Source Variable"
        obj.source_variable = var_source_variable
        # alpha
        var_season = "Annual"
        obj.season = var_season
        # alpha
        var_category_variable_name = "EnergyCharges"
        obj.category_variable_name = var_category_variable_name
        # alpha
        var_cost_per_unit_value_or_variable_name = "Cost per Unit Value or Variable Name"
        obj.cost_per_unit_value_or_variable_name = var_cost_per_unit_value_or_variable_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.utilitycostchargesimples[0].name, var_name)
        self.assertEqual(idf2.utilitycostchargesimples[0].tariff_name, var_tariff_name)
        self.assertEqual(idf2.utilitycostchargesimples[0].source_variable, var_source_variable)
        self.assertEqual(idf2.utilitycostchargesimples[0].season, var_season)
        self.assertEqual(idf2.utilitycostchargesimples[0].category_variable_name, var_category_variable_name)
        self.assertEqual(idf2.utilitycostchargesimples[0].cost_per_unit_value_or_variable_name, var_cost_per_unit_value_or_variable_name)