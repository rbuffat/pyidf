import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_design_objects import OutputControlSizingStyle

log = logging.getLogger(__name__)

class TestOutputControlSizingStyle(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputcontrolsizingstyle(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputControlSizingStyle()
        # alpha
        var_column_separator = "Comma"
        obj.column_separator = var_column_separator

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputcontrolsizingstyles[0].column_separator, var_column_separator)