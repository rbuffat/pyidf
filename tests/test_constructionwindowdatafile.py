import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import ConstructionWindowDataFile
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestConstructionWindowDataFile(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_constructionwindowdatafile(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ConstructionWindowDataFile()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_file_name = "File Name"
        obj.file_name = var_file_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.constructionwindowdatafiles[0].name, var_name)
        self.assertEqual(idf2.constructionwindowdatafiles[0].file_name, var_file_name)