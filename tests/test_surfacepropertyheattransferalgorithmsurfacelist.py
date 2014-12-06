import os
import tempfile
import unittest
import pyidf
from pyidf.advanced_construction import SurfacePropertyHeatTransferAlgorithmSurfaceList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSurfacePropertyHeatTransferAlgorithmSurfaceList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacepropertyheattransferalgorithmsurfacelist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfacePropertyHeatTransferAlgorithmSurfaceList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_algorithm = "ConductionTransferFunction"
        obj.algorithm = var_algorithm
        paras = []
        var_surface_name_1 = "object-list|Surface Name 1"
        paras.append(var_surface_name_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacepropertyheattransferalgorithmsurfacelists[0].name, var_name)
        self.assertEqual(idf2.surfacepropertyheattransferalgorithmsurfacelists[0].algorithm, var_algorithm)
        index = obj.extensible_field_index("Surface Name 1")
        self.assertEqual(idf2.surfacepropertyheattransferalgorithmsurfacelists[0].extensibles[0][index], var_surface_name_1)