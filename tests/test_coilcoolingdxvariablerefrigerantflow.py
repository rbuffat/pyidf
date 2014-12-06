import os
import tempfile
import unittest
import pyidf
from pyidf.coils import CoilCoolingDxVariableRefrigerantFlow
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCoilCoolingDxVariableRefrigerantFlow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingdxvariablerefrigerantflow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingDxVariableRefrigerantFlow()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_gross_rated_total_cooling_capacity = 0.0001
        obj.gross_rated_total_cooling_capacity = var_gross_rated_total_cooling_capacity
        # real
        var_gross_rated_sensible_heat_ratio = 0.0001
        obj.gross_rated_sensible_heat_ratio = var_gross_rated_sensible_heat_ratio
        # real
        var_rated_air_flow_rate = 0.0001
        obj.rated_air_flow_rate = var_rated_air_flow_rate
        # object-list
        var_cooling_capacity_ratio_modifier_function_of_temperature_curve_name = "object-list|Cooling Capacity Ratio Modifier Function of Temperature Curve Name"
        obj.cooling_capacity_ratio_modifier_function_of_temperature_curve_name = var_cooling_capacity_ratio_modifier_function_of_temperature_curve_name
        # object-list
        var_cooling_capacity_modifier_curve_function_of_flow_fraction_name = "object-list|Cooling Capacity Modifier Curve Function of Flow Fraction Name"
        obj.cooling_capacity_modifier_curve_function_of_flow_fraction_name = var_cooling_capacity_modifier_curve_function_of_flow_fraction_name
        # node
        var_coil_air_inlet_node = "node|Coil Air Inlet Node"
        obj.coil_air_inlet_node = var_coil_air_inlet_node
        # node
        var_coil_air_outlet_node = "node|Coil Air Outlet Node"
        obj.coil_air_outlet_node = var_coil_air_outlet_node
        # object-list
        var_name_of_water_storage_tank_for_condensate_collection = "object-list|Name of Water Storage Tank for Condensate Collection"
        obj.name_of_water_storage_tank_for_condensate_collection = var_name_of_water_storage_tank_for_condensate_collection

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflows[0].name, var_name)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflows[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablerefrigerantflows[0].gross_rated_total_cooling_capacity, var_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablerefrigerantflows[0].gross_rated_sensible_heat_ratio, var_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablerefrigerantflows[0].rated_air_flow_rate, var_rated_air_flow_rate)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflows[0].cooling_capacity_ratio_modifier_function_of_temperature_curve_name, var_cooling_capacity_ratio_modifier_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflows[0].cooling_capacity_modifier_curve_function_of_flow_fraction_name, var_cooling_capacity_modifier_curve_function_of_flow_fraction_name)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflows[0].coil_air_inlet_node, var_coil_air_inlet_node)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflows[0].coil_air_outlet_node, var_coil_air_outlet_node)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflows[0].name_of_water_storage_tank_for_condensate_collection, var_name_of_water_storage_tank_for_condensate_collection)