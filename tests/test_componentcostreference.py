import os
import tempfile
import unittest
import pyidf
from pyidf.economics import ComponentCostReference
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestComponentCostReference(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_componentcostreference(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ComponentCostReference()
        # real
        var_reference_building_line_item_costs = 1.1
        obj.reference_building_line_item_costs = var_reference_building_line_item_costs
        # real
        var_reference_building_miscellaneous_cost_per_conditioned_area = 2.2
        obj.reference_building_miscellaneous_cost_per_conditioned_area = var_reference_building_miscellaneous_cost_per_conditioned_area
        # real
        var_reference_building_design_and_engineering_fees = 3.3
        obj.reference_building_design_and_engineering_fees = var_reference_building_design_and_engineering_fees
        # real
        var_reference_building_contractor_fee = 4.4
        obj.reference_building_contractor_fee = var_reference_building_contractor_fee
        # real
        var_reference_building_contingency = 5.5
        obj.reference_building_contingency = var_reference_building_contingency
        # real
        var_reference_building_permits_bonding_and_insurance = 6.6
        obj.reference_building_permits_bonding_and_insurance = var_reference_building_permits_bonding_and_insurance
        # real
        var_reference_building_commissioning_fee = 7.7
        obj.reference_building_commissioning_fee = var_reference_building_commissioning_fee
        # real
        var_reference_building_regional_adjustment_factor = 8.8
        obj.reference_building_regional_adjustment_factor = var_reference_building_regional_adjustment_factor

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.componentcostreferences[0].reference_building_line_item_costs, var_reference_building_line_item_costs)
        self.assertAlmostEqual(idf2.componentcostreferences[0].reference_building_miscellaneous_cost_per_conditioned_area, var_reference_building_miscellaneous_cost_per_conditioned_area)
        self.assertAlmostEqual(idf2.componentcostreferences[0].reference_building_design_and_engineering_fees, var_reference_building_design_and_engineering_fees)
        self.assertAlmostEqual(idf2.componentcostreferences[0].reference_building_contractor_fee, var_reference_building_contractor_fee)
        self.assertAlmostEqual(idf2.componentcostreferences[0].reference_building_contingency, var_reference_building_contingency)
        self.assertAlmostEqual(idf2.componentcostreferences[0].reference_building_permits_bonding_and_insurance, var_reference_building_permits_bonding_and_insurance)
        self.assertAlmostEqual(idf2.componentcostreferences[0].reference_building_commissioning_fee, var_reference_building_commissioning_fee)
        self.assertAlmostEqual(idf2.componentcostreferences[0].reference_building_regional_adjustment_factor, var_reference_building_regional_adjustment_factor)