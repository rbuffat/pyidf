import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import GroundHeatTransferBasementZface

log = logging.getLogger(__name__)

class TestGroundHeatTransferBasementZface(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementzface(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementZface()

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)