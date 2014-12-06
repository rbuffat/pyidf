import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import OutputTableTimeBins

log = logging.getLogger(__name__)

class TestOutputTableTimeBins(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputtabletimebins(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputTableTimeBins()
        # alpha
        var_key_value = "Key Value"
        obj.key_value = var_key_value
        # external-list
        var_variable_name = "external-list|Variable Name"
        obj.variable_name = var_variable_name
        # real
        var_interval_start = 3.3
        obj.interval_start = var_interval_start
        # real
        var_interval_size = 4.4
        obj.interval_size = var_interval_size
        # integer
        var_interval_count = 10
        obj.interval_count = var_interval_count
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # alpha
        var_variable_type = "Energy"
        obj.variable_type = var_variable_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputtabletimebinss[0].key_value, var_key_value)
        self.assertEqual(idf2.outputtabletimebinss[0].variable_name, var_variable_name)
        self.assertAlmostEqual(idf2.outputtabletimebinss[0].interval_start, var_interval_start)
        self.assertAlmostEqual(idf2.outputtabletimebinss[0].interval_size, var_interval_size)
        self.assertEqual(idf2.outputtabletimebinss[0].interval_count, var_interval_count)
        self.assertEqual(idf2.outputtabletimebinss[0].schedule_name, var_schedule_name)
        self.assertEqual(idf2.outputtabletimebinss[0].variable_type, var_variable_type)