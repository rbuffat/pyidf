import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.setpoint_managers import SetpointManagerCondenserEnteringReset

log = logging.getLogger(__name__)

class TestSetpointManagerCondenserEnteringReset(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagercondenserenteringreset(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerCondenserEnteringReset()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # object-list
        var_default_condenser_entering_water_temperature_schedule_name = "object-list|Default Condenser Entering Water Temperature Schedule Name"
        obj.default_condenser_entering_water_temperature_schedule_name = var_default_condenser_entering_water_temperature_schedule_name
        # object-list
        var_minimum_design_wetbulb_temperature_curve_name = "object-list|Minimum Design Wetbulb Temperature Curve Name"
        obj.minimum_design_wetbulb_temperature_curve_name = var_minimum_design_wetbulb_temperature_curve_name
        # object-list
        var_minimum_outside_air_wetbulb_temperature_curve_name = "object-list|Minimum Outside Air Wetbulb Temperature Curve Name"
        obj.minimum_outside_air_wetbulb_temperature_curve_name = var_minimum_outside_air_wetbulb_temperature_curve_name
        # object-list
        var_optimized_cond_entering_water_temperature_curve_name = "object-list|Optimized Cond Entering Water Temperature Curve Name"
        obj.optimized_cond_entering_water_temperature_curve_name = var_optimized_cond_entering_water_temperature_curve_name
        # real
        var_minimum_lift = 7.7
        obj.minimum_lift = var_minimum_lift
        # real
        var_maximum_condenser_entering_water_temperature = 8.8
        obj.maximum_condenser_entering_water_temperature = var_maximum_condenser_entering_water_temperature
        # real
        var_cooling_tower_design_inlet_air_wetbulb_temperature = 9.9
        obj.cooling_tower_design_inlet_air_wetbulb_temperature = var_cooling_tower_design_inlet_air_wetbulb_temperature
        # node
        var_setpoint_node_or_nodelist_name = "node|Setpoint Node or NodeList Name"
        obj.setpoint_node_or_nodelist_name = var_setpoint_node_or_nodelist_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagercondenserenteringresets[0].name, var_name)
        self.assertEqual(idf2.setpointmanagercondenserenteringresets[0].control_variable, var_control_variable)
        self.assertEqual(idf2.setpointmanagercondenserenteringresets[0].default_condenser_entering_water_temperature_schedule_name, var_default_condenser_entering_water_temperature_schedule_name)
        self.assertEqual(idf2.setpointmanagercondenserenteringresets[0].minimum_design_wetbulb_temperature_curve_name, var_minimum_design_wetbulb_temperature_curve_name)
        self.assertEqual(idf2.setpointmanagercondenserenteringresets[0].minimum_outside_air_wetbulb_temperature_curve_name, var_minimum_outside_air_wetbulb_temperature_curve_name)
        self.assertEqual(idf2.setpointmanagercondenserenteringresets[0].optimized_cond_entering_water_temperature_curve_name, var_optimized_cond_entering_water_temperature_curve_name)
        self.assertAlmostEqual(idf2.setpointmanagercondenserenteringresets[0].minimum_lift, var_minimum_lift)
        self.assertAlmostEqual(idf2.setpointmanagercondenserenteringresets[0].maximum_condenser_entering_water_temperature, var_maximum_condenser_entering_water_temperature)
        self.assertAlmostEqual(idf2.setpointmanagercondenserenteringresets[0].cooling_tower_design_inlet_air_wetbulb_temperature, var_cooling_tower_design_inlet_air_wetbulb_temperature)
        self.assertEqual(idf2.setpointmanagercondenserenteringresets[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)