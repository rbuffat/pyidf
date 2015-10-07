import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.economics import UtilityCostChargeBlock

log = logging.getLogger(__name__)

class TestUtilityCostChargeBlock(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_utilitycostchargeblock(self):

        pyidf.validation_level = ValidationLevel.error

        obj = UtilityCostChargeBlock()
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
        var_remaining_into_variable = "Remaining Into Variable"
        obj.remaining_into_variable = var_remaining_into_variable
        # alpha
        var_block_size_multiplier_value_or_variable_name = "Block Size Multiplier Value or Variable Name"
        obj.block_size_multiplier_value_or_variable_name = var_block_size_multiplier_value_or_variable_name
        # alpha
        var_block_size_1_value_or_variable_name = "Block Size 1 Value or Variable Name"
        obj.block_size_1_value_or_variable_name = var_block_size_1_value_or_variable_name
        # alpha
        var_block_1_cost_per_unit_value_or_variable_name = "Block 1 Cost per Unit Value or Variable Name"
        obj.block_1_cost_per_unit_value_or_variable_name = var_block_1_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_2_value_or_variable_name = "Block Size 2 Value or Variable Name"
        obj.block_size_2_value_or_variable_name = var_block_size_2_value_or_variable_name
        # alpha
        var_block_2_cost_per_unit_value_or_variable_name = "Block 2 Cost per Unit Value or Variable Name"
        obj.block_2_cost_per_unit_value_or_variable_name = var_block_2_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_3_value_or_variable_name = "Block Size 3 Value or Variable Name"
        obj.block_size_3_value_or_variable_name = var_block_size_3_value_or_variable_name
        # alpha
        var_block_3_cost_per_unit_value_or_variable_name = "Block 3 Cost per Unit Value or Variable Name"
        obj.block_3_cost_per_unit_value_or_variable_name = var_block_3_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_4_value_or_variable_name = "Block Size 4 Value or Variable Name"
        obj.block_size_4_value_or_variable_name = var_block_size_4_value_or_variable_name
        # alpha
        var_block_4_cost_per_unit_value_or_variable_name = "Block 4 Cost per Unit Value or Variable Name"
        obj.block_4_cost_per_unit_value_or_variable_name = var_block_4_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_5_value_or_variable_name = "Block Size 5 Value or Variable Name"
        obj.block_size_5_value_or_variable_name = var_block_size_5_value_or_variable_name
        # alpha
        var_block_5_cost_per_unit_value_or_variable_name = "Block 5 Cost per Unit Value or Variable Name"
        obj.block_5_cost_per_unit_value_or_variable_name = var_block_5_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_6_value_or_variable_name = "Block Size 6 Value or Variable Name"
        obj.block_size_6_value_or_variable_name = var_block_size_6_value_or_variable_name
        # alpha
        var_block_6_cost_per_unit_value_or_variable_name = "Block 6 Cost per Unit Value or Variable Name"
        obj.block_6_cost_per_unit_value_or_variable_name = var_block_6_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_7_value_or_variable_name = "Block Size 7 Value or Variable Name"
        obj.block_size_7_value_or_variable_name = var_block_size_7_value_or_variable_name
        # alpha
        var_block_7_cost_per_unit_value_or_variable_name = "Block 7 Cost per Unit Value or Variable Name"
        obj.block_7_cost_per_unit_value_or_variable_name = var_block_7_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_8_value_or_variable_name = "Block Size 8 Value or Variable Name"
        obj.block_size_8_value_or_variable_name = var_block_size_8_value_or_variable_name
        # alpha
        var_block_8_cost_per_unit_value_or_variable_name = "Block 8 Cost per Unit Value or Variable Name"
        obj.block_8_cost_per_unit_value_or_variable_name = var_block_8_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_9_value_or_variable_name = "Block Size 9 Value or Variable Name"
        obj.block_size_9_value_or_variable_name = var_block_size_9_value_or_variable_name
        # alpha
        var_block_9_cost_per_unit_value_or_variable_name = "Block 9 Cost per Unit Value or Variable Name"
        obj.block_9_cost_per_unit_value_or_variable_name = var_block_9_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_10_value_or_variable_name = "Block Size 10 Value or Variable Name"
        obj.block_size_10_value_or_variable_name = var_block_size_10_value_or_variable_name
        # alpha
        var_block_10_cost_per_unit_value_or_variable_name = "Block 10 Cost per Unit Value or Variable Name"
        obj.block_10_cost_per_unit_value_or_variable_name = var_block_10_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_11_value_or_variable_name = "Block Size 11 Value or Variable Name"
        obj.block_size_11_value_or_variable_name = var_block_size_11_value_or_variable_name
        # alpha
        var_block_11_cost_per_unit_value_or_variable_name = "Block 11 Cost per Unit Value or Variable Name"
        obj.block_11_cost_per_unit_value_or_variable_name = var_block_11_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_12_value_or_variable_name = "Block Size 12 Value or Variable Name"
        obj.block_size_12_value_or_variable_name = var_block_size_12_value_or_variable_name
        # alpha
        var_block_12_cost_per_unit_value_or_variable_name = "Block 12 Cost per Unit Value or Variable Name"
        obj.block_12_cost_per_unit_value_or_variable_name = var_block_12_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_13_value_or_variable_name = "Block Size 13 Value or Variable Name"
        obj.block_size_13_value_or_variable_name = var_block_size_13_value_or_variable_name
        # alpha
        var_block_13_cost_per_unit_value_or_variable_name = "Block 13 Cost per Unit Value or Variable Name"
        obj.block_13_cost_per_unit_value_or_variable_name = var_block_13_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_14_value_or_variable_name = "Block Size 14 Value or Variable Name"
        obj.block_size_14_value_or_variable_name = var_block_size_14_value_or_variable_name
        # alpha
        var_block_14_cost_per_unit_value_or_variable_name = "Block 14 Cost per Unit Value or Variable Name"
        obj.block_14_cost_per_unit_value_or_variable_name = var_block_14_cost_per_unit_value_or_variable_name
        # alpha
        var_block_size_15_value_or_variable_name = "Block Size 15 Value or Variable Name"
        obj.block_size_15_value_or_variable_name = var_block_size_15_value_or_variable_name
        # alpha
        var_block_15_cost_per_unit_value_or_variable_name = "Block 15 Cost per Unit Value or Variable Name"
        obj.block_15_cost_per_unit_value_or_variable_name = var_block_15_cost_per_unit_value_or_variable_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.utilitycostchargeblocks[0].name, var_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].tariff_name, var_tariff_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].source_variable, var_source_variable)
        self.assertEqual(idf2.utilitycostchargeblocks[0].season, var_season)
        self.assertEqual(idf2.utilitycostchargeblocks[0].category_variable_name, var_category_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].remaining_into_variable, var_remaining_into_variable)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_multiplier_value_or_variable_name, var_block_size_multiplier_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_1_value_or_variable_name, var_block_size_1_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_1_cost_per_unit_value_or_variable_name, var_block_1_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_2_value_or_variable_name, var_block_size_2_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_2_cost_per_unit_value_or_variable_name, var_block_2_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_3_value_or_variable_name, var_block_size_3_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_3_cost_per_unit_value_or_variable_name, var_block_3_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_4_value_or_variable_name, var_block_size_4_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_4_cost_per_unit_value_or_variable_name, var_block_4_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_5_value_or_variable_name, var_block_size_5_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_5_cost_per_unit_value_or_variable_name, var_block_5_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_6_value_or_variable_name, var_block_size_6_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_6_cost_per_unit_value_or_variable_name, var_block_6_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_7_value_or_variable_name, var_block_size_7_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_7_cost_per_unit_value_or_variable_name, var_block_7_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_8_value_or_variable_name, var_block_size_8_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_8_cost_per_unit_value_or_variable_name, var_block_8_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_9_value_or_variable_name, var_block_size_9_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_9_cost_per_unit_value_or_variable_name, var_block_9_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_10_value_or_variable_name, var_block_size_10_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_10_cost_per_unit_value_or_variable_name, var_block_10_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_11_value_or_variable_name, var_block_size_11_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_11_cost_per_unit_value_or_variable_name, var_block_11_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_12_value_or_variable_name, var_block_size_12_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_12_cost_per_unit_value_or_variable_name, var_block_12_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_13_value_or_variable_name, var_block_size_13_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_13_cost_per_unit_value_or_variable_name, var_block_13_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_14_value_or_variable_name, var_block_size_14_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_14_cost_per_unit_value_or_variable_name, var_block_14_cost_per_unit_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_size_15_value_or_variable_name, var_block_size_15_value_or_variable_name)
        self.assertEqual(idf2.utilitycostchargeblocks[0].block_15_cost_per_unit_value_or_variable_name, var_block_15_cost_per_unit_value_or_variable_name)