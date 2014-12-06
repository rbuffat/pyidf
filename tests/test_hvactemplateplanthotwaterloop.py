import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplatePlantHotWaterLoop

log = logging.getLogger(__name__)

class TestHvactemplatePlantHotWaterLoop(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplateplanthotwaterloop(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplatePlantHotWaterLoop()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_pump_schedule_name = "object-list|Pump Schedule Name"
        obj.pump_schedule_name = var_pump_schedule_name
        # alpha
        var_pump_control_type = "Intermittent"
        obj.pump_control_type = var_pump_control_type
        # alpha
        var_hot_water_plant_operation_scheme_type = "Default"
        obj.hot_water_plant_operation_scheme_type = var_hot_water_plant_operation_scheme_type
        # object-list
        var_hot_water_plant_equipment_operation_schemes_name = "object-list|Hot Water Plant Equipment Operation Schemes Name"
        obj.hot_water_plant_equipment_operation_schemes_name = var_hot_water_plant_equipment_operation_schemes_name
        # object-list
        var_hot_water_setpoint_schedule_name = "object-list|Hot Water Setpoint Schedule Name"
        obj.hot_water_setpoint_schedule_name = var_hot_water_setpoint_schedule_name
        # real
        var_hot_water_design_setpoint = 7.7
        obj.hot_water_design_setpoint = var_hot_water_design_setpoint
        # alpha
        var_hot_water_pump_configuration = "VariableFlow"
        obj.hot_water_pump_configuration = var_hot_water_pump_configuration
        # real
        var_hot_water_pump_rated_head = 0.0
        obj.hot_water_pump_rated_head = var_hot_water_pump_rated_head
        # alpha
        var_hot_water_setpoint_reset_type = "None"
        obj.hot_water_setpoint_reset_type = var_hot_water_setpoint_reset_type
        # real
        var_hot_water_setpoint_at_outdoor_drybulb_low = 11.11
        obj.hot_water_setpoint_at_outdoor_drybulb_low = var_hot_water_setpoint_at_outdoor_drybulb_low
        # real
        var_hot_water_reset_outdoor_drybulb_low = 12.12
        obj.hot_water_reset_outdoor_drybulb_low = var_hot_water_reset_outdoor_drybulb_low
        # real
        var_hot_water_setpoint_at_outdoor_drybulb_high = 13.13
        obj.hot_water_setpoint_at_outdoor_drybulb_high = var_hot_water_setpoint_at_outdoor_drybulb_high
        # real
        var_hot_water_reset_outdoor_drybulb_high = 14.14
        obj.hot_water_reset_outdoor_drybulb_high = var_hot_water_reset_outdoor_drybulb_high
        # alpha
        var_hot_water_pump_type = "SinglePump"
        obj.hot_water_pump_type = var_hot_water_pump_type
        # alpha
        var_supply_side_bypass_pipe = "Yes"
        obj.supply_side_bypass_pipe = var_supply_side_bypass_pipe
        # alpha
        var_demand_side_bypass_pipe = "Yes"
        obj.demand_side_bypass_pipe = var_demand_side_bypass_pipe
        # alpha
        var_fluid_type = "Water"
        obj.fluid_type = var_fluid_type
        # real
        var_loop_design_delta_temperature = 19.19
        obj.loop_design_delta_temperature = var_loop_design_delta_temperature
        # real
        var_maximum_outdoor_dry_bulb_temperature = 20.2
        obj.maximum_outdoor_dry_bulb_temperature = var_maximum_outdoor_dry_bulb_temperature
        # alpha
        var_load_distribution_scheme = "Optimal"
        obj.load_distribution_scheme = var_load_distribution_scheme

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].name, var_name)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].pump_schedule_name, var_pump_schedule_name)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].pump_control_type, var_pump_control_type)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_plant_operation_scheme_type, var_hot_water_plant_operation_scheme_type)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_plant_equipment_operation_schemes_name, var_hot_water_plant_equipment_operation_schemes_name)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_setpoint_schedule_name, var_hot_water_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_design_setpoint, var_hot_water_design_setpoint)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_pump_configuration, var_hot_water_pump_configuration)
        self.assertAlmostEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_pump_rated_head, var_hot_water_pump_rated_head)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_setpoint_reset_type, var_hot_water_setpoint_reset_type)
        self.assertAlmostEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_setpoint_at_outdoor_drybulb_low, var_hot_water_setpoint_at_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_reset_outdoor_drybulb_low, var_hot_water_reset_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_setpoint_at_outdoor_drybulb_high, var_hot_water_setpoint_at_outdoor_drybulb_high)
        self.assertAlmostEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_reset_outdoor_drybulb_high, var_hot_water_reset_outdoor_drybulb_high)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].hot_water_pump_type, var_hot_water_pump_type)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].supply_side_bypass_pipe, var_supply_side_bypass_pipe)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].demand_side_bypass_pipe, var_demand_side_bypass_pipe)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].fluid_type, var_fluid_type)
        self.assertAlmostEqual(idf2.hvactemplateplanthotwaterloops[0].loop_design_delta_temperature, var_loop_design_delta_temperature)
        self.assertAlmostEqual(idf2.hvactemplateplanthotwaterloops[0].maximum_outdoor_dry_bulb_temperature, var_maximum_outdoor_dry_bulb_temperature)
        self.assertEqual(idf2.hvactemplateplanthotwaterloops[0].load_distribution_scheme, var_load_distribution_scheme)