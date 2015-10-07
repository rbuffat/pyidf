import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilHeatingDxVariableRefrigerantFlowFluidTemperatureControl

log = logging.getLogger(__name__)

class TestCoilHeatingDxVariableRefrigerantFlowFluidTemperatureControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatingdxvariablerefrigerantflowfluidtemperaturecontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingDxVariableRefrigerantFlowFluidTemperatureControl()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule = "object-list|Availability Schedule"
        obj.availability_schedule = var_availability_schedule
        # node
        var_coil_air_inlet_node = "node|Coil Air Inlet Node"
        obj.coil_air_inlet_node = var_coil_air_inlet_node
        # node
        var_coil_air_outlet_node = "node|Coil Air Outlet Node"
        obj.coil_air_outlet_node = var_coil_air_outlet_node
        # real
        var_rated_total_heating_capacity = 0.0001
        obj.rated_total_heating_capacity = var_rated_total_heating_capacity
        # real
        var_indoor_unit_reference_subcooling = 0.0
        obj.indoor_unit_reference_subcooling = var_indoor_unit_reference_subcooling
        # object-list
        var_indoor_unit_condensing_temperature_function_of_subcooling_curve_name = "object-list|Indoor Unit Condensing Temperature Function of Subcooling Curve Name"
        obj.indoor_unit_condensing_temperature_function_of_subcooling_curve_name = var_indoor_unit_condensing_temperature_function_of_subcooling_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflowfluidtemperaturecontrols[0].name, var_name)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflowfluidtemperaturecontrols[0].availability_schedule, var_availability_schedule)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflowfluidtemperaturecontrols[0].coil_air_inlet_node, var_coil_air_inlet_node)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflowfluidtemperaturecontrols[0].coil_air_outlet_node, var_coil_air_outlet_node)
        self.assertAlmostEqual(idf2.coilheatingdxvariablerefrigerantflowfluidtemperaturecontrols[0].rated_total_heating_capacity, var_rated_total_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingdxvariablerefrigerantflowfluidtemperaturecontrols[0].indoor_unit_reference_subcooling, var_indoor_unit_reference_subcooling)
        self.assertEqual(idf2.coilheatingdxvariablerefrigerantflowfluidtemperaturecontrols[0].indoor_unit_condensing_temperature_function_of_subcooling_curve_name, var_indoor_unit_condensing_temperature_function_of_subcooling_curve_name)