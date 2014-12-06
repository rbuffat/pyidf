import os
import tempfile
import unittest
import pyidf
from pyidf.economics import LifeCycleCostParameters
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestLifeCycleCostParameters(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_lifecyclecostparameters(self):

        pyidf.validation_level = ValidationLevel.error

        obj = LifeCycleCostParameters()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_discounting_convention = "EndOfYear"
        obj.discounting_convention = var_discounting_convention
        # alpha
        var_inflation_approach = "ConstantDollar"
        obj.inflation_approach = var_inflation_approach
        # real
        var_real_discount_rate = 4.4
        obj.real_discount_rate = var_real_discount_rate
        # real
        var_nominal_discount_rate = 5.5
        obj.nominal_discount_rate = var_nominal_discount_rate
        # real
        var_inflation = 6.6
        obj.inflation = var_inflation
        # alpha
        var_base_date_month = "January"
        obj.base_date_month = var_base_date_month
        # integer
        var_base_date_year = 2000
        obj.base_date_year = var_base_date_year
        # alpha
        var_service_date_month = "January"
        obj.service_date_month = var_service_date_month
        # integer
        var_service_date_year = 2000
        obj.service_date_year = var_service_date_year
        # integer
        var_length_of_study_period_in_years = 50
        obj.length_of_study_period_in_years = var_length_of_study_period_in_years
        # real
        var_tax_rate = 0.0
        obj.tax_rate = var_tax_rate
        # alpha
        var_depreciation_method = "ModifiedAcceleratedCostRecoverySystem-3year"
        obj.depreciation_method = var_depreciation_method

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.lifecyclecostparameterss[0].name, var_name)
        self.assertEqual(idf2.lifecyclecostparameterss[0].discounting_convention, var_discounting_convention)
        self.assertEqual(idf2.lifecyclecostparameterss[0].inflation_approach, var_inflation_approach)
        self.assertAlmostEqual(idf2.lifecyclecostparameterss[0].real_discount_rate, var_real_discount_rate)
        self.assertAlmostEqual(idf2.lifecyclecostparameterss[0].nominal_discount_rate, var_nominal_discount_rate)
        self.assertAlmostEqual(idf2.lifecyclecostparameterss[0].inflation, var_inflation)
        self.assertEqual(idf2.lifecyclecostparameterss[0].base_date_month, var_base_date_month)
        self.assertEqual(idf2.lifecyclecostparameterss[0].base_date_year, var_base_date_year)
        self.assertEqual(idf2.lifecyclecostparameterss[0].service_date_month, var_service_date_month)
        self.assertEqual(idf2.lifecyclecostparameterss[0].service_date_year, var_service_date_year)
        self.assertEqual(idf2.lifecyclecostparameterss[0].length_of_study_period_in_years, var_length_of_study_period_in_years)
        self.assertAlmostEqual(idf2.lifecyclecostparameterss[0].tax_rate, var_tax_rate)
        self.assertEqual(idf2.lifecyclecostparameterss[0].depreciation_method, var_depreciation_method)