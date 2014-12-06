import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilHeatingDxVariableRefrigerantFlow

log = logging.getLogger(__name__)

class TestCoilHeatingDxVariableRefrigerantFlow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatingdxvariablerefrigerantflow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingDxVariableRefrigerantFlow()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule = "object-list|Availability Schedule"
        obj.availability_schedule = var_availability_schedule
        # real
        var_gross_rated_heating_capacity = 0.0001
        obj.gross_rated_heating_capacity = var_gross_rated_heating_capacity
        # real
        var_rated_air_flow_rate = 0.0001
        obj.rated_air_flow_rate = var_rated_air_flow_rate
        # node
        var_coil_air_inlet_node = "node|Coil Air Inlet Node"
        obj.coil_air_inlet_node = var_coil_air_inlet_node
        # node
        var_coil_air_outlet_node = "node|Coil Air Outlet Node"
        obj.coil_air_outlet_node = var_coil_air_outlet_node
        # object-list
        var_heating_capacity_ratio_modifier_function_of_temperature_curve_name = "object-list|Heating Capacity Ratio Modifier Function of Temperature Curve Name"
        obj.heating_capacity_ratio_modifier_function_of_temperature_curve_name = var_heating_capacity_ratio_modifier_function_of_temperature_curve_name
        # object-list
        var_heating_capacity_modifier_function_of_flow_fraction_curve_name = "object-list|Heating Capacity Modifier Function of Flow Fraction Curve Name"
        obj.heating_capacity_modifier_function_of_flow_fraction_curve_name = var_heating_capacity_modifier_function_of_flow_fraction_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflows[0].name, var_name)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflows[0].availability_schedule, var_availability_schedule)
        self.assertAlmostEqual(idf2.coilheatingdxvariablerefrigerantflows[0].gross_rated_heating_capacity, var_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablerefrigerantflows[0].rated_air_flow_rate, var_rated_air_flow_rate)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflows[0].coil_air_inlet_node, var_coil_air_inlet_node)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflows[0].coil_air_outlet_node, var_coil_air_outlet_node)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflows[0].heating_capacity_ratio_modifier_function_of_temperature_curve_name, var_heating_capacity_ratio_modifier_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflows[0].heating_capacity_modifier_function_of_flow_fraction_curve_name, var_heating_capacity_modifier_function_of_flow_fraction_curve_name)