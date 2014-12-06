import os
import tempfile
import unittest
import pyidf
from pyidf.refrigeration import MatrixTwoDimension
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestMatrixTwoDimension(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_matrixtwodimension(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MatrixTwoDimension()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # integer
        var_number_of_rows = 2
        obj.number_of_rows = var_number_of_rows
        # integer
        var_number_of_columns = 3
        obj.number_of_columns = var_number_of_columns
        paras = []
        var_value = 4.4
        paras.append(var_value)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.matrixtwodimensions[0].name, var_name)
        self.assertEqual(idf2.matrixtwodimensions[0].number_of_rows, var_number_of_rows)
        self.assertEqual(idf2.matrixtwodimensions[0].number_of_columns, var_number_of_columns)
        index = obj.extensible_field_index("Value")
        self.assertAlmostEqual(idf2.matrixtwodimensions[0].extensibles[0][index], var_value)