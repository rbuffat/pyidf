import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import OutputVariable

log = logging.getLogger(__name__)

class TestOutputVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputVariable()
        # alpha
        var_key_value = "Key Value"
        obj.key_value = var_key_value
        # external-list
        var_variable_name = "external-list|Variable Name"
        obj.variable_name = var_variable_name
        # alpha
        var_reporting_frequency = "Detailed"
        obj.reporting_frequency = var_reporting_frequency
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputvariables[0].key_value, var_key_value)
        self.assertEqual(idf2.outputvariables[0].variable_name, var_variable_name)
        self.assertEqual(idf2.outputvariables[0].reporting_frequency, var_reporting_frequency)
        self.assertEqual(idf2.outputvariables[0].schedule_name, var_schedule_name)