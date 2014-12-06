import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.advanced_construction import SurfacePropertyOtherSideConditionsModel

log = logging.getLogger(__name__)

class TestSurfacePropertyOtherSideConditionsModel(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacepropertyothersideconditionsmodel(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfacePropertyOtherSideConditionsModel()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_type_of_modeling = "GapConvectionRadiation"
        obj.type_of_modeling = var_type_of_modeling

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacepropertyothersideconditionsmodels[0].name, var_name)
        self.assertEqual(idf2.surfacepropertyothersideconditionsmodels[0].type_of_modeling, var_type_of_modeling)