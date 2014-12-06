import os
import tempfile
import unittest
import pyidf
from pyidf.room_air_models import GroundHeatTransferBasementYface
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferBasementYface(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementyface(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementYface()

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)