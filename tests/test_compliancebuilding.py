import os
import tempfile
import unittest
import pyidf
from pyidf.compliance_objects import ComplianceBuilding
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestComplianceBuilding(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_compliancebuilding(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ComplianceBuilding()
        # real
        var_building_rotation_for_appendix_g = 1.1
        obj.building_rotation_for_appendix_g = var_building_rotation_for_appendix_g

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.compliancebuildings[0].building_rotation_for_appendix_g, var_building_rotation_for_appendix_g)