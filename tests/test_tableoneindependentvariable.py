import os
import tempfile
import unittest
import pyidf
from pyidf.performance_tables import TableOneIndependentVariable
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestTableOneIndependentVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_tableoneindependentvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = TableOneIndependentVariable()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_curve_type = "Linear"
        obj.curve_type = var_curve_type
        # alpha
        var_interpolation_method = "LinearInterpolationOfTable"
        obj.interpolation_method = var_interpolation_method
        # real
        var_minimum_value_of_x = 4.4
        obj.minimum_value_of_x = var_minimum_value_of_x
        # real
        var_maximum_value_of_x = 5.5
        obj.maximum_value_of_x = var_maximum_value_of_x
        # real
        var_minimum_table_output = 6.6
        obj.minimum_table_output = var_minimum_table_output
        # real
        var_maximum_table_output = 7.7
        obj.maximum_table_output = var_maximum_table_output
        # alpha
        var_input_unit_type_for_x = "Dimensionless"
        obj.input_unit_type_for_x = var_input_unit_type_for_x
        # alpha
        var_output_unit_type = "Dimensionless"
        obj.output_unit_type = var_output_unit_type
        # real
        var_normalization_reference = 10.1
        obj.normalization_reference = var_normalization_reference
        paras = []
        var_x_value = 11.11
        paras.append(var_x_value)
        var_output_value = 12.12
        paras.append(var_output_value)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.tableoneindependentvariables[0].name, var_name)
        self.assertEqual(idf2.tableoneindependentvariables[0].curve_type, var_curve_type)
        self.assertEqual(idf2.tableoneindependentvariables[0].interpolation_method, var_interpolation_method)
        self.assertAlmostEqual(idf2.tableoneindependentvariables[0].minimum_value_of_x, var_minimum_value_of_x)
        self.assertAlmostEqual(idf2.tableoneindependentvariables[0].maximum_value_of_x, var_maximum_value_of_x)
        self.assertAlmostEqual(idf2.tableoneindependentvariables[0].minimum_table_output, var_minimum_table_output)
        self.assertAlmostEqual(idf2.tableoneindependentvariables[0].maximum_table_output, var_maximum_table_output)
        self.assertEqual(idf2.tableoneindependentvariables[0].input_unit_type_for_x, var_input_unit_type_for_x)
        self.assertEqual(idf2.tableoneindependentvariables[0].output_unit_type, var_output_unit_type)
        self.assertAlmostEqual(idf2.tableoneindependentvariables[0].normalization_reference, var_normalization_reference)
        index = obj.extensible_field_index("X Value")
        self.assertAlmostEqual(idf2.tableoneindependentvariables[0].extensibles[0][index], var_x_value)
        index = obj.extensible_field_index("Output Value")
        self.assertAlmostEqual(idf2.tableoneindependentvariables[0].extensibles[0][index], var_output_value)