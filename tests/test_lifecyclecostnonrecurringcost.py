import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.economics import LifeCycleCostNonrecurringCost

log = logging.getLogger(__name__)

class TestLifeCycleCostNonrecurringCost(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_lifecyclecostnonrecurringcost(self):

        pyidf.validation_level = ValidationLevel.error

        obj = LifeCycleCostNonrecurringCost()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_category = "Construction"
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

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.lifecyclecostnonrecurringcosts[0].name, var_name)
        self.assertEqual(idf2.lifecyclecostnonrecurringcosts[0].category, var_category)
        self.assertAlmostEqual(idf2.lifecyclecostnonrecurringcosts[0].cost, var_cost)
        self.assertEqual(idf2.lifecyclecostnonrecurringcosts[0].start_of_costs, var_start_of_costs)
        self.assertEqual(idf2.lifecyclecostnonrecurringcosts[0].years_from_start, var_years_from_start)
        self.assertEqual(idf2.lifecyclecostnonrecurringcosts[0].months_from_start, var_months_from_start)