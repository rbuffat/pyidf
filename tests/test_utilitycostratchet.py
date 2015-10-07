import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.economics import UtilityCostRatchet

log = logging.getLogger(__name__)

class TestUtilityCostRatchet(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_utilitycostratchet(self):

        pyidf.validation_level = ValidationLevel.error

        obj = UtilityCostRatchet()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_tariff_name = "object-list|Tariff Name"
        obj.tariff_name = var_tariff_name
        # alpha
        var_baseline_source_variable = "Baseline Source Variable"
        obj.baseline_source_variable = var_baseline_source_variable
        # alpha
        var_adjustment_source_variable = "Adjustment Source Variable"
        obj.adjustment_source_variable = var_adjustment_source_variable
        # alpha
        var_season_from = "Annual"
        obj.season_from = var_season_from
        # alpha
        var_season_to = "Annual"
        obj.season_to = var_season_to
        # alpha
        var_multiplier_value_or_variable_name = "Multiplier Value or Variable Name"
        obj.multiplier_value_or_variable_name = var_multiplier_value_or_variable_name
        # alpha
        var_offset_value_or_variable_name = "Offset Value or Variable Name"
        obj.offset_value_or_variable_name = var_offset_value_or_variable_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.utilitycostratchets[0].name, var_name)
        self.assertEqual(idf2.utilitycostratchets[0].tariff_name, var_tariff_name)
        self.assertEqual(idf2.utilitycostratchets[0].baseline_source_variable, var_baseline_source_variable)
        self.assertEqual(idf2.utilitycostratchets[0].adjustment_source_variable, var_adjustment_source_variable)
        self.assertEqual(idf2.utilitycostratchets[0].season_from, var_season_from)
        self.assertEqual(idf2.utilitycostratchets[0].season_to, var_season_to)
        self.assertEqual(idf2.utilitycostratchets[0].multiplier_value_or_variable_name, var_multiplier_value_or_variable_name)
        self.assertEqual(idf2.utilitycostratchets[0].offset_value_or_variable_name, var_offset_value_or_variable_name)