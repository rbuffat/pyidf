import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorFuelCellInverter
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorFuelCellInverter(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorfuelcellinverter(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorFuelCellInverter()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_inverter_efficiency_calculation_mode = "Quadratic"
        obj.inverter_efficiency_calculation_mode = var_inverter_efficiency_calculation_mode
        # real
        var_inverter_efficiency = 0.5
        obj.inverter_efficiency = var_inverter_efficiency
        # object-list
        var_efficiency_function_of_dc_power_curve_name = "object-list|Efficiency Function of DC Power Curve Name"
        obj.efficiency_function_of_dc_power_curve_name = var_efficiency_function_of_dc_power_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorfuelcellinverters[0].name, var_name)
        self.assertEqual(idf2.generatorfuelcellinverters[0].inverter_efficiency_calculation_mode, var_inverter_efficiency_calculation_mode)
        self.assertAlmostEqual(idf2.generatorfuelcellinverters[0].inverter_efficiency, var_inverter_efficiency)
        self.assertEqual(idf2.generatorfuelcellinverters[0].efficiency_function_of_dc_power_curve_name, var_efficiency_function_of_dc_power_curve_name)