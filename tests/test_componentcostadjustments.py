import os
import tempfile
import unittest
import pyidf
from pyidf.economics import ComponentCostAdjustments
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestComponentCostAdjustments(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_componentcostadjustments(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ComponentCostAdjustments()
        # real
        var_miscellaneous_cost_per_conditioned_area = 1.1
        obj.miscellaneous_cost_per_conditioned_area = var_miscellaneous_cost_per_conditioned_area
        # real
        var_design_and_engineering_fees = 2.2
        obj.design_and_engineering_fees = var_design_and_engineering_fees
        # real
        var_contractor_fee = 3.3
        obj.contractor_fee = var_contractor_fee
        # real
        var_contingency = 4.4
        obj.contingency = var_contingency
        # real
        var_permits_bonding_and_insurance = 5.5
        obj.permits_bonding_and_insurance = var_permits_bonding_and_insurance
        # real
        var_commissioning_fee = 6.6
        obj.commissioning_fee = var_commissioning_fee
        # real
        var_regional_adjustment_factor = 7.7
        obj.regional_adjustment_factor = var_regional_adjustment_factor

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.componentcostadjustmentss[0].miscellaneous_cost_per_conditioned_area, var_miscellaneous_cost_per_conditioned_area)
        self.assertAlmostEqual(idf2.componentcostadjustmentss[0].design_and_engineering_fees, var_design_and_engineering_fees)
        self.assertAlmostEqual(idf2.componentcostadjustmentss[0].contractor_fee, var_contractor_fee)
        self.assertAlmostEqual(idf2.componentcostadjustmentss[0].contingency, var_contingency)
        self.assertAlmostEqual(idf2.componentcostadjustmentss[0].permits_bonding_and_insurance, var_permits_bonding_and_insurance)
        self.assertAlmostEqual(idf2.componentcostadjustmentss[0].commissioning_fee, var_commissioning_fee)
        self.assertAlmostEqual(idf2.componentcostadjustmentss[0].regional_adjustment_factor, var_regional_adjustment_factor)