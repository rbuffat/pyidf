import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.node import OutdoorAirNode

log = logging.getLogger(__name__)

class TestOutdoorAirNode(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outdoorairnode(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutdoorAirNode()
        # node
        var_name = "node|Name"
        obj.name = var_name
        # real
        var_height_above_ground = 2.2
        obj.height_above_ground = var_height_above_ground

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outdoorairnodes[0].name, var_name)
        self.assertAlmostEqual(idf2.outdoorairnodes[0].height_above_ground, var_height_above_ground)