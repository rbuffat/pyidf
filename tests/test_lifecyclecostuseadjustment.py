import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.economics import LifeCycleCostUseAdjustment

log = logging.getLogger(__name__)

class TestLifeCycleCostUseAdjustment(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_lifecyclecostuseadjustment(self):

        pyidf.validation_level = ValidationLevel.error

        obj = LifeCycleCostUseAdjustment()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_resource = "Electricity"
        obj.resource = var_resource
        paras = []
        var_year_1_multiplier = 3.3
        paras.append(var_year_1_multiplier)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.lifecyclecostuseadjustments[0].name, var_name)
        self.assertEqual(idf2.lifecyclecostuseadjustments[0].resource, var_resource)
        index = obj.extensible_field_index("Year 1 Multiplier")
        self.assertAlmostEqual(idf2.lifecyclecostuseadjustments[0].extensibles[0][index], var_year_1_multiplier)