import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplatePlantMixedWaterLoop
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplatePlantMixedWaterLoop(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplateplantmixedwaterloop(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplatePlantMixedWaterLoop()
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
        var_operation_scheme_type = "Default"
        obj.operation_scheme_type = var_operation_scheme_type
        # object-list
        var_equipment_operation_schemes_name = "object-list|Equipment Operation Schemes Name"
        obj.equipment_operation_schemes_name = var_equipment_operation_schemes_name
        # object-list
        var_high_temperature_setpoint_schedule_name = "object-list|High Temperature Setpoint Schedule Name"
        obj.high_temperature_setpoint_schedule_name = var_high_temperature_setpoint_schedule_name
        # real
        var_high_temperature_design_setpoint = 7.7
        obj.high_temperature_design_setpoint = var_high_temperature_design_setpoint
        # object-list
        var_low_temperature_setpoint_schedule_name = "object-list|Low Temperature Setpoint Schedule Name"
        obj.low_temperature_setpoint_schedule_name = var_low_temperature_setpoint_schedule_name
        # real
        var_low_temperature_design_setpoint = 9.9
        obj.low_temperature_design_setpoint = var_low_temperature_design_setpoint
        # alpha
        var_water_pump_configuration = "VariableFlow"
        obj.water_pump_configuration = var_water_pump_configuration
        # real
        var_water_pump_rated_head = 0.0
        obj.water_pump_rated_head = var_water_pump_rated_head
        # alpha
        var_water_pump_type = "SinglePump"
        obj.water_pump_type = var_water_pump_type
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
        var_loop_design_delta_temperature = 16.16
        obj.loop_design_delta_temperature = var_loop_design_delta_temperature
        # alpha
        var_load_distribution_scheme = "Optimal"
        obj.load_distribution_scheme = var_load_distribution_scheme

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].name, var_name)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].pump_schedule_name, var_pump_schedule_name)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].pump_control_type, var_pump_control_type)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].operation_scheme_type, var_operation_scheme_type)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].equipment_operation_schemes_name, var_equipment_operation_schemes_name)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].high_temperature_setpoint_schedule_name, var_high_temperature_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplateplantmixedwaterloops[0].high_temperature_design_setpoint, var_high_temperature_design_setpoint)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].low_temperature_setpoint_schedule_name, var_low_temperature_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplateplantmixedwaterloops[0].low_temperature_design_setpoint, var_low_temperature_design_setpoint)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].water_pump_configuration, var_water_pump_configuration)
        self.assertAlmostEqual(idf2.hvactemplateplantmixedwaterloops[0].water_pump_rated_head, var_water_pump_rated_head)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].water_pump_type, var_water_pump_type)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].supply_side_bypass_pipe, var_supply_side_bypass_pipe)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].demand_side_bypass_pipe, var_demand_side_bypass_pipe)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].fluid_type, var_fluid_type)
        self.assertAlmostEqual(idf2.hvactemplateplantmixedwaterloops[0].loop_design_delta_temperature, var_loop_design_delta_temperature)
        self.assertEqual(idf2.hvactemplateplantmixedwaterloops[0].load_distribution_scheme, var_load_distribution_scheme)