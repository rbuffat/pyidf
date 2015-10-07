import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.unitary_equipment import AirLoopHvacUnitaryHeatCoolVavchangeoverBypass

log = logging.getLogger(__name__)

class TestAirLoopHvacUnitaryHeatCoolVavchangeoverBypass(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacunitaryheatcoolvavchangeoverbypass(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacUnitaryHeatCoolVavchangeoverBypass()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_cooling_supply_air_flow_rate = 0.0001
        obj.cooling_supply_air_flow_rate = var_cooling_supply_air_flow_rate
        # real
        var_heating_supply_air_flow_rate = 0.0001
        obj.heating_supply_air_flow_rate = var_heating_supply_air_flow_rate
        # real
        var_no_load_supply_air_flow_rate = 0.0
        obj.no_load_supply_air_flow_rate = var_no_load_supply_air_flow_rate
        # real
        var_cooling_outdoor_air_flow_rate = 0.0
        obj.cooling_outdoor_air_flow_rate = var_cooling_outdoor_air_flow_rate
        # real
        var_heating_outdoor_air_flow_rate = 0.0
        obj.heating_outdoor_air_flow_rate = var_heating_outdoor_air_flow_rate
        # real
        var_no_load_outdoor_air_flow_rate = 0.0
        obj.no_load_outdoor_air_flow_rate = var_no_load_outdoor_air_flow_rate
        # object-list
        var_outdoor_air_flow_rate_multiplier_schedule_name = "object-list|Outdoor Air Flow Rate Multiplier Schedule Name"
        obj.outdoor_air_flow_rate_multiplier_schedule_name = var_outdoor_air_flow_rate_multiplier_schedule_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_bypass_duct_mixer_node_name = "node|Bypass Duct Mixer Node Name"
        obj.bypass_duct_mixer_node_name = var_bypass_duct_mixer_node_name
        # node
        var_bypass_duct_splitter_node_name = "node|Bypass Duct Splitter Node Name"
        obj.bypass_duct_splitter_node_name = var_bypass_duct_splitter_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_outdoor_air_mixer_object_type = "OutdoorAir:Mixer"
        obj.outdoor_air_mixer_object_type = var_outdoor_air_mixer_object_type
        # object-list
        var_outdoor_air_mixer_name = "object-list|Outdoor Air Mixer Name"
        obj.outdoor_air_mixer_name = var_outdoor_air_mixer_name
        # alpha
        var_supply_air_fan_object_type = "Fan:OnOff"
        obj.supply_air_fan_object_type = var_supply_air_fan_object_type
        # object-list
        var_supply_air_fan_name = "object-list|Supply Air Fan Name"
        obj.supply_air_fan_name = var_supply_air_fan_name
        # alpha
        var_supply_air_fan_placement = "BlowThrough"
        obj.supply_air_fan_placement = var_supply_air_fan_placement
        # object-list
        var_supply_air_fan_operating_mode_schedule_name = "object-list|Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:DX:SingleSpeed"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # alpha
        var_heating_coil_object_type = "Coil:Heating:DX:SingleSpeed"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # alpha
        var_priority_control_mode = "CoolingPriority"
        obj.priority_control_mode = var_priority_control_mode
        # real
        var_minimum_outlet_air_temperature_during_cooling_operation = 0.0001
        obj.minimum_outlet_air_temperature_during_cooling_operation = var_minimum_outlet_air_temperature_during_cooling_operation
        # real
        var_maximum_outlet_air_temperature_during_heating_operation = 0.0001
        obj.maximum_outlet_air_temperature_during_heating_operation = var_maximum_outlet_air_temperature_during_heating_operation
        # alpha
        var_dehumidification_control_type = "None"
        obj.dehumidification_control_type = var_dehumidification_control_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].name, var_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].cooling_supply_air_flow_rate, var_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].heating_supply_air_flow_rate, var_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].no_load_supply_air_flow_rate, var_no_load_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].cooling_outdoor_air_flow_rate, var_cooling_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].heating_outdoor_air_flow_rate, var_heating_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].no_load_outdoor_air_flow_rate, var_no_load_outdoor_air_flow_rate)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].outdoor_air_flow_rate_multiplier_schedule_name, var_outdoor_air_flow_rate_multiplier_schedule_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].bypass_duct_mixer_node_name, var_bypass_duct_mixer_node_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].bypass_duct_splitter_node_name, var_bypass_duct_splitter_node_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].outdoor_air_mixer_object_type, var_outdoor_air_mixer_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].outdoor_air_mixer_name, var_outdoor_air_mixer_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].supply_air_fan_placement, var_supply_air_fan_placement)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].cooling_coil_name, var_cooling_coil_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].heating_coil_name, var_heating_coil_name)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].priority_control_mode, var_priority_control_mode)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].minimum_outlet_air_temperature_during_cooling_operation, var_minimum_outlet_air_temperature_during_cooling_operation)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].maximum_outlet_air_temperature_during_heating_operation, var_maximum_outlet_air_temperature_during_heating_operation)
        self.assertEqual(idf2.airloophvacunitaryheatcoolvavchangeoverbypasss[0].dehumidification_control_type, var_dehumidification_control_type)