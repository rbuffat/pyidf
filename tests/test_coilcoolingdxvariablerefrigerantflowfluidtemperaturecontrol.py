import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilCoolingDxVariableRefrigerantFlowFluidTemperatureControl

log = logging.getLogger(__name__)

class TestCoilCoolingDxVariableRefrigerantFlowFluidTemperatureControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingdxvariablerefrigerantflowfluidtemperaturecontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingDxVariableRefrigerantFlowFluidTemperatureControl()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_coil_air_inlet_node = "node|Coil Air Inlet Node"
        obj.coil_air_inlet_node = var_coil_air_inlet_node
        # node
        var_coil_air_outlet_node = "node|Coil Air Outlet Node"
        obj.coil_air_outlet_node = var_coil_air_outlet_node
        # real
        var_rated_total_cooling_capacity = 0.0001
        obj.rated_total_cooling_capacity = var_rated_total_cooling_capacity
        # real
        var_rated_sensible_heat_ratio = 0.0001
        obj.rated_sensible_heat_ratio = var_rated_sensible_heat_ratio
        # real
        var_indoor_unit_reference_superheating = 0.0
        obj.indoor_unit_reference_superheating = var_indoor_unit_reference_superheating
        # object-list
        var_indoor_unit_evaporating_temperature_function_of_superheating_curve_name = "object-list|Indoor Unit Evaporating Temperature Function of Superheating Curve Name"
        obj.indoor_unit_evaporating_temperature_function_of_superheating_curve_name = var_indoor_unit_evaporating_temperature_function_of_superheating_curve_name
        # object-list
        var_name_of_water_storage_tank_for_condensate_collection = "object-list|Name of Water Storage Tank for Condensate Collection"
        obj.name_of_water_storage_tank_for_condensate_collection = var_name_of_water_storage_tank_for_condensate_collection

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflowfluidtemperaturecontrols[0].name, var_name)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflowfluidtemperaturecontrols[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflowfluidtemperaturecontrols[0].coil_air_inlet_node, var_coil_air_inlet_node)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflowfluidtemperaturecontrols[0].coil_air_outlet_node, var_coil_air_outlet_node)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablerefrigerantflowfluidtemperaturecontrols[0].rated_total_cooling_capacity, var_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablerefrigerantflowfluidtemperaturecontrols[0].rated_sensible_heat_ratio, var_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxvariablerefrigerantflowfluidtemperaturecontrols[0].indoor_unit_reference_superheating, var_indoor_unit_reference_superheating)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflowfluidtemperaturecontrols[0].indoor_unit_evaporating_temperature_function_of_superheating_curve_name, var_indoor_unit_evaporating_temperature_function_of_superheating_curve_name)
        self.assertEqual(idf2.coilcoolingdxvariablerefrigerantflowfluidtemperaturecontrols[0].name_of_water_storage_tank_for_condensate_collection, var_name_of_water_storage_tank_for_condensate_collection)