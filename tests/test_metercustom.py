import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import MeterCustom

log = logging.getLogger(__name__)

class TestMeterCustom(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_metercustom(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MeterCustom()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_fuel_type = "Electricity"
        obj.fuel_type = var_fuel_type
        paras = []
        var_key_name_1 = "Key Name 1"
        paras.append(var_key_name_1)
        var_output_variable_or_meter_name_1 = "Output Variable or Meter Name 1"
        paras.append(var_output_variable_or_meter_name_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.metercustoms[0].name, var_name)
        self.assertEqual(idf2.metercustoms[0].fuel_type, var_fuel_type)
        index = obj.extensible_field_index("Key Name 1")
        self.assertEqual(idf2.metercustoms[0].extensibles[0][index], var_key_name_1)
        index = obj.extensible_field_index("Output Variable or Meter Name 1")
        self.assertEqual(idf2.metercustoms[0].extensibles[0][index], var_output_variable_or_meter_name_1)