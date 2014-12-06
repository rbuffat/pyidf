import os
import tempfile
import unittest
import pyidf
from pyidf.refrigeration import RefrigerationSubcooler
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRefrigerationSubcooler(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationsubcooler(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationSubcooler()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_subcooler_type = "Mechanical"
        obj.subcooler_type = var_subcooler_type
        # real
        var_liquid_suction_design_subcooling_temperature_difference = 3.3
        obj.liquid_suction_design_subcooling_temperature_difference = var_liquid_suction_design_subcooling_temperature_difference
        # real
        var_design_liquid_inlet_temperature = 4.4
        obj.design_liquid_inlet_temperature = var_design_liquid_inlet_temperature
        # real
        var_design_vapor_inlet_temperature = 5.5
        obj.design_vapor_inlet_temperature = var_design_vapor_inlet_temperature
        # object-list
        var_capacityproviding_system = "object-list|Capacity-Providing System"
        obj.capacityproviding_system = var_capacityproviding_system
        # real
        var_outlet_control_temperature = 7.7
        obj.outlet_control_temperature = var_outlet_control_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationsubcoolers[0].name, var_name)
        self.assertEqual(idf2.refrigerationsubcoolers[0].subcooler_type, var_subcooler_type)
        self.assertAlmostEqual(idf2.refrigerationsubcoolers[0].liquid_suction_design_subcooling_temperature_difference, var_liquid_suction_design_subcooling_temperature_difference)
        self.assertAlmostEqual(idf2.refrigerationsubcoolers[0].design_liquid_inlet_temperature, var_design_liquid_inlet_temperature)
        self.assertAlmostEqual(idf2.refrigerationsubcoolers[0].design_vapor_inlet_temperature, var_design_vapor_inlet_temperature)
        self.assertEqual(idf2.refrigerationsubcoolers[0].capacityproviding_system, var_capacityproviding_system)
        self.assertAlmostEqual(idf2.refrigerationsubcoolers[0].outlet_control_temperature, var_outlet_control_temperature)