import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputTableMonthly
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputTableMonthly(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputtablemonthly(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputTableMonthly()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # integer
        var_digits_after_decimal = 5
        obj.digits_after_decimal = var_digits_after_decimal
        paras = []
        var_variable_or_meter_1_name = "external-list|Variable or Meter 1 Name"
        paras.append(var_variable_or_meter_1_name)
        var_aggregation_type_for_variable_or_meter_1 = "SumOrAverage"
        paras.append(var_aggregation_type_for_variable_or_meter_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputtablemonthlys[0].name, var_name)
        self.assertEqual(idf2.outputtablemonthlys[0].digits_after_decimal, var_digits_after_decimal)
        index = obj.extensible_field_index("Variable or Meter 1 Name")
        self.assertEqual(idf2.outputtablemonthlys[0].extensibles[0][index], var_variable_or_meter_1_name)
        index = obj.extensible_field_index("Aggregation Type for Variable or Meter 1")
        self.assertEqual(idf2.outputtablemonthlys[0].extensibles[0][index], var_aggregation_type_for_variable_or_meter_1)