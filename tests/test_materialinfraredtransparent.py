import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import MaterialInfraredTransparent
from pyidf import ValidationLevel
from pyidf.idf import IDF


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
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialinfraredtransparents[0].name, var_name)