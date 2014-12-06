import os
import tempfile
import unittest
import pyidf
from pyidf.economics import LifeCycleCostRecurringCosts
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestLifeCycleCostRecurringCosts(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_lifecyclecostrecurringcosts(self):

        pyidf.validation_level = ValidationLevel.error

        obj = LifeCycleCostRecurringCosts()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_category = "Maintenance"
        obj.category = var_category
        # real
        var_cost = 3.3
        obj.cost = var_cost
        # alpha
        var_start_of_costs = "ServicePeriod"
        obj.start_of_costs = var_start_of_costs
        # integer
        var_years_from_start = 50
        obj.years_from_start = var_years_from_start
        # integer
        var_months_from_start = 600
        obj.months_from_start = var_months_from_start
        # integer
        var_repeat_period_years = 50
        obj.repeat_period_years = var_repeat_period_years
        # integer
        var_repeat_period_months = 600
        obj.repeat_period_months = var_repeat_period_months
        # real
        var_annual_escalation_rate = 0.0
        obj.annual_escalation_rate = var_annual_escalation_rate

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.lifecyclecostrecurringcostss[0].name, var_name)
        self.assertEqual(idf2.lifecyclecostrecurringcostss[0].category, var_category)
        self.assertAlmostEqual(idf2.lifecyclecostrecurringcostss[0].cost, var_cost)
        self.assertEqual(idf2.lifecyclecostrecurringcostss[0].start_of_costs, var_start_of_costs)
        self.assertEqual(idf2.lifecyclecostrecurringcostss[0].years_from_start, var_years_from_start)
        self.assertEqual(idf2.lifecyclecostrecurringcostss[0].months_from_start, var_months_from_start)
        self.assertEqual(idf2.lifecyclecostrecurringcostss[0].repeat_period_years, var_repeat_period_years)
        self.assertEqual(idf2.lifecyclecostrecurringcostss[0].repeat_period_months, var_repeat_period_months)
        self.assertAlmostEqual(idf2.lifecyclecostrecurringcostss[0].annual_escalation_rate, var_annual_escalation_rate)