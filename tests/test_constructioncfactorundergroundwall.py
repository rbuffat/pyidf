import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import ConstructionCfactorUndergroundWall

log = logging.getLogger(__name__)

class TestConstructionCfactorUndergroundWall(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_constructioncfactorundergroundwall(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ConstructionCfactorUndergroundWall()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_cfactor = 0.0001
        obj.cfactor = var_cfactor
        # real
        var_height = 0.0001
        obj.height = var_height

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.constructioncfactorundergroundwalls[0].name, var_name)
        self.assertAlmostEqual(idf2.constructioncfactorundergroundwalls[0].cfactor, var_cfactor)
        self.assertAlmostEqual(idf2.constructioncfactorundergroundwalls[0].height, var_height)