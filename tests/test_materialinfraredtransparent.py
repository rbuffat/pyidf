import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import MaterialInfraredTransparent

log = logging.getLogger(__name__)

class TestMaterialInfraredTransparent(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialinfraredtransparent(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialInfraredTransparent()
        # alpha
        var_name = "Name"
        obj.name = var_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialinfraredtransparents[0].name, var_name)