import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputSurfacesList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputSurfacesList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputsurfaceslist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputSurfacesList()
        # alpha
        var_report_type = "Details"
        obj.report_type = var_report_type
        # alpha
        var_report_specifications = "IDF"
        obj.report_specifications = var_report_specifications

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputsurfaceslists[0].report_type, var_report_type)
        self.assertEqual(idf2.outputsurfaceslists[0].report_specifications, var_report_specifications)