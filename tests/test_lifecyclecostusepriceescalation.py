import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.economics import LifeCycleCostUsePriceEscalation

log = logging.getLogger(__name__)

class TestLifeCycleCostUsePriceEscalation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_lifecyclecostusepriceescalation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = LifeCycleCostUsePriceEscalation()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_resource = "Electricity"
        obj.resource = var_resource
        # integer
        var_escalation_start_year = 2000
        obj.escalation_start_year = var_escalation_start_year
        # alpha
        var_escalation_start_month = "January"
        obj.escalation_start_month = var_escalation_start_month
        paras = []
        var_year_1_escalation = 5.5
        paras.append(var_year_1_escalation)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.lifecyclecostusepriceescalations[0].name, var_name)
        self.assertEqual(idf2.lifecyclecostusepriceescalations[0].resource, var_resource)
        self.assertEqual(idf2.lifecyclecostusepriceescalations[0].escalation_start_year, var_escalation_start_year)
        self.assertEqual(idf2.lifecyclecostusepriceescalations[0].escalation_start_month, var_escalation_start_month)
        index = obj.extensible_field_index("Year 1 Escalation")
        self.assertAlmostEqual(idf2.lifecyclecostusepriceescalations[0].extensibles[0][index], var_year_1_escalation)