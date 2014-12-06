import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import OutputSurfacesDrawing

log = logging.getLogger(__name__)

class TestOutputSurfacesDrawing(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputsurfacesdrawing(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputSurfacesDrawing()
        # alpha
        var_report_type = "DXF"
        obj.report_type = var_report_type
        # alpha
        var_report_specifications_1 = "Triangulate3DFace"
        obj.report_specifications_1 = var_report_specifications_1
        # object-list
        var_report_specifications_2 = "object-list|Report Specifications 2"
        obj.report_specifications_2 = var_report_specifications_2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputsurfacesdrawings[0].report_type, var_report_type)
        self.assertEqual(idf2.outputsurfacesdrawings[0].report_specifications_1, var_report_specifications_1)
        self.assertEqual(idf2.outputsurfacesdrawings[0].report_specifications_2, var_report_specifications_2)