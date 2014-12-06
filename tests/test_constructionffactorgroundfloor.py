import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import ConstructionFfactorGroundFloor

log = logging.getLogger(__name__)

class TestConstructionFfactorGroundFloor(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_constructionffactorgroundfloor(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ConstructionFfactorGroundFloor()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_ffactor = 0.0001
        obj.ffactor = var_ffactor
        # real
        var_area = 0.0001
        obj.area = var_area
        # real
        var_perimeterexposed = 0.0
        obj.perimeterexposed = var_perimeterexposed

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.constructionffactorgroundfloors[0].name, var_name)
        self.assertAlmostEqual(idf2.constructionffactorgroundfloors[0].ffactor, var_ffactor)
        self.assertAlmostEqual(idf2.constructionffactorgroundfloors[0].area, var_area)
        self.assertAlmostEqual(idf2.constructionffactorgroundfloors[0].perimeterexposed, var_perimeterexposed)