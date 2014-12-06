import os
import tempfile
import unittest
import pyidf
from pyidf.room_air_models import GroundHeatTransferSlabXface
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferSlabXface(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferslabxface(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferSlabXface()

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)