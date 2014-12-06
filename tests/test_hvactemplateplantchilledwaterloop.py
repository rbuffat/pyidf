import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplatePlantChilledWaterLoop

log = logging.getLogger(__name__)

class TestHvactemplatePlantChilledWaterLoop(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplateplantchilledwaterloop(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplatePlantChilledWaterLoop()
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
        var_chiller_plant_operation_scheme_type = "Default"
        obj.chiller_plant_operation_scheme_type = var_chiller_plant_operation_scheme_type
        # object-list
        var_chiller_plant_equipment_operation_schemes_name = "object-list|Chiller Plant Equipment Operation Schemes Name"
        obj.chiller_plant_equipment_operation_schemes_name = var_chiller_plant_equipment_operation_schemes_name
        # object-list
        var_chilled_water_setpoint_schedule_name = "object-list|Chilled Water Setpoint Schedule Name"
        obj.chilled_water_setpoint_schedule_name = var_chilled_water_setpoint_schedule_name
        # real
        var_chilled_water_design_setpoint = 7.7
        obj.chilled_water_design_setpoint = var_chilled_water_design_setpoint
        # alpha
        var_chilled_water_pump_configuration = "ConstantPrimaryNoSecondary"
        obj.chilled_water_pump_configuration = var_chilled_water_pump_configuration
        # real
        var_primary_chilled_water_pump_rated_head = 0.0
        obj.primary_chilled_water_pump_rated_head = var_primary_chilled_water_pump_rated_head
        # real
        var_secondary_chilled_water_pump_rated_head = 0.0
        obj.secondary_chilled_water_pump_rated_head = var_secondary_chilled_water_pump_rated_head
        # alpha
        var_condenser_plant_operation_scheme_type = "Default"
        obj.condenser_plant_operation_scheme_type = var_condenser_plant_operation_scheme_type
        # object-list
        var_condenser_equipment_operation_schemes_name = "object-list|Condenser Equipment Operation Schemes Name"
        obj.condenser_equipment_operation_schemes_name = var_condenser_equipment_operation_schemes_name
        # alpha
        var_condenser_water_temperature_control_type = "OutdoorWetBulbTemperature"
        obj.condenser_water_temperature_control_type = var_condenser_water_temperature_control_type
        # object-list
        var_condenser_water_setpoint_schedule_name = "object-list|Condenser Water Setpoint Schedule Name"
        obj.condenser_water_setpoint_schedule_name = var_condenser_water_setpoint_schedule_name
        # real
        var_condenser_water_design_setpoint = 15.15
        obj.condenser_water_design_setpoint = var_condenser_water_design_setpoint
        # real
        var_condenser_water_pump_rated_head = 0.0
        obj.condenser_water_pump_rated_head = var_condenser_water_pump_rated_head
        # alpha
        var_chilled_water_setpoint_reset_type = "None"
        obj.chilled_water_setpoint_reset_type = var_chilled_water_setpoint_reset_type
        # real
        var_chilled_water_setpoint_at_outdoor_drybulb_low = 18.18
        obj.chilled_water_setpoint_at_outdoor_drybulb_low = var_chilled_water_setpoint_at_outdoor_drybulb_low
        # real
        var_chilled_water_reset_outdoor_drybulb_low = 19.19
        obj.chilled_water_reset_outdoor_drybulb_low = var_chilled_water_reset_outdoor_drybulb_low
        # real
        var_chilled_water_setpoint_at_outdoor_drybulb_high = 20.2
        obj.chilled_water_setpoint_at_outdoor_drybulb_high = var_chilled_water_setpoint_at_outdoor_drybulb_high
        # real
        var_chilled_water_reset_outdoor_drybulb_high = 21.21
        obj.chilled_water_reset_outdoor_drybulb_high = var_chilled_water_reset_outdoor_drybulb_high
        # alpha
        var_chilled_water_primary_pump_type = "SinglePump"
        obj.chilled_water_primary_pump_type = var_chilled_water_primary_pump_type
        # alpha
        var_chilled_water_secondary_pump_type = "SinglePump"
        obj.chilled_water_secondary_pump_type = var_chilled_water_secondary_pump_type
        # alpha
        var_condenser_water_pump_type = "SinglePump"
        obj.condenser_water_pump_type = var_condenser_water_pump_type
        # alpha
        var_chilled_water_supply_side_bypass_pipe = "Yes"
        obj.chilled_water_supply_side_bypass_pipe = var_chilled_water_supply_side_bypass_pipe
        # alpha
        var_chilled_water_demand_side_bypass_pipe = "Yes"
        obj.chilled_water_demand_side_bypass_pipe = var_chilled_water_demand_side_bypass_pipe
        # alpha
        var_condenser_water_supply_side_bypass_pipe = "Yes"
        obj.condenser_water_supply_side_bypass_pipe = var_condenser_water_supply_side_bypass_pipe
        # alpha
        var_condenser_water_demand_side_bypass_pipe = "Yes"
        obj.condenser_water_demand_side_bypass_pipe = var_condenser_water_demand_side_bypass_pipe
        # alpha
        var_fluid_type = "Water"
        obj.fluid_type = var_fluid_type
        # real
        var_loop_design_delta_temperature = 30.3
        obj.loop_design_delta_temperature = var_loop_design_delta_temperature
        # real
        var_minimum_outdoor_dry_bulb_temperature = 31.31
        obj.minimum_outdoor_dry_bulb_temperature = var_minimum_outdoor_dry_bulb_temperature
        # alpha
        var_chilled_water_load_distribution_scheme = "Optimal"
        obj.chilled_water_load_distribution_scheme = var_chilled_water_load_distribution_scheme
        # alpha
        var_condenser_water_load_distribution_scheme = "Optimal"
        obj.condenser_water_load_distribution_scheme = var_condenser_water_load_distribution_scheme

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].name, var_name)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].pump_schedule_name, var_pump_schedule_name)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].pump_control_type, var_pump_control_type)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].chiller_plant_operation_scheme_type, var_chiller_plant_operation_scheme_type)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].chiller_plant_equipment_operation_schemes_name, var_chiller_plant_equipment_operation_schemes_name)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_setpoint_schedule_name, var_chilled_water_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_design_setpoint, var_chilled_water_design_setpoint)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_pump_configuration, var_chilled_water_pump_configuration)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].primary_chilled_water_pump_rated_head, var_primary_chilled_water_pump_rated_head)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].secondary_chilled_water_pump_rated_head, var_secondary_chilled_water_pump_rated_head)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].condenser_plant_operation_scheme_type, var_condenser_plant_operation_scheme_type)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].condenser_equipment_operation_schemes_name, var_condenser_equipment_operation_schemes_name)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].condenser_water_temperature_control_type, var_condenser_water_temperature_control_type)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].condenser_water_setpoint_schedule_name, var_condenser_water_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].condenser_water_design_setpoint, var_condenser_water_design_setpoint)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].condenser_water_pump_rated_head, var_condenser_water_pump_rated_head)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_setpoint_reset_type, var_chilled_water_setpoint_reset_type)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_setpoint_at_outdoor_drybulb_low, var_chilled_water_setpoint_at_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_reset_outdoor_drybulb_low, var_chilled_water_reset_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_setpoint_at_outdoor_drybulb_high, var_chilled_water_setpoint_at_outdoor_drybulb_high)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_reset_outdoor_drybulb_high, var_chilled_water_reset_outdoor_drybulb_high)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_primary_pump_type, var_chilled_water_primary_pump_type)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_secondary_pump_type, var_chilled_water_secondary_pump_type)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].condenser_water_pump_type, var_condenser_water_pump_type)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_supply_side_bypass_pipe, var_chilled_water_supply_side_bypass_pipe)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_demand_side_bypass_pipe, var_chilled_water_demand_side_bypass_pipe)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].condenser_water_supply_side_bypass_pipe, var_condenser_water_supply_side_bypass_pipe)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].condenser_water_demand_side_bypass_pipe, var_condenser_water_demand_side_bypass_pipe)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].fluid_type, var_fluid_type)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].loop_design_delta_temperature, var_loop_design_delta_temperature)
        self.assertAlmostEqual(idf2.hvactemplateplantchilledwaterloops[0].minimum_outdoor_dry_bulb_temperature, var_minimum_outdoor_dry_bulb_temperature)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].chilled_water_load_distribution_scheme, var_chilled_water_load_distribution_scheme)
        self.assertEqual(idf2.hvactemplateplantchilledwaterloops[0].condenser_water_load_distribution_scheme, var_condenser_water_load_distribution_scheme)