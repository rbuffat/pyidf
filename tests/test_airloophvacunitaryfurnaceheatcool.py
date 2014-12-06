import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.unitary_equipment import AirLoopHvacUnitaryFurnaceHeatCool

log = logging.getLogger(__name__)

class TestAirLoopHvacUnitaryFurnaceHeatCool(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacunitaryfurnaceheatcool(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacUnitaryFurnaceHeatCool()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_furnace_air_inlet_node_name = "node|Furnace Air Inlet Node Name"
        obj.furnace_air_inlet_node_name = var_furnace_air_inlet_node_name
        # node
        var_furnace_air_outlet_node_name = "node|Furnace Air Outlet Node Name"
        obj.furnace_air_outlet_node_name = var_furnace_air_outlet_node_name
        # object-list
        var_supply_air_fan_operating_mode_schedule_name = "object-list|Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
        # real
        var_maximum_supply_air_temperature = 6.6
        obj.maximum_supply_air_temperature = var_maximum_supply_air_temperature
        # real
        var_supply_air_flow_rate_during_cooling_operation = 0.0001
        obj.supply_air_flow_rate_during_cooling_operation = var_supply_air_flow_rate_during_cooling_operation
        # real
        var_supply_air_flow_rate_during_heating_operation = 0.0001
        obj.supply_air_flow_rate_during_heating_operation = var_supply_air_flow_rate_during_heating_operation
        # real
        var_supply_air_flow_rate_when_no_cooling_or_heating_is_needed = 0.0
        obj.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = var_supply_air_flow_rate_when_no_cooling_or_heating_is_needed
        # object-list
        var_controlling_zone_or_thermostat_location = "object-list|Controlling Zone or Thermostat Location"
        obj.controlling_zone_or_thermostat_location = var_controlling_zone_or_thermostat_location
        # alpha
        var_supply_fan_object_type = "Fan:OnOff"
        obj.supply_fan_object_type = var_supply_fan_object_type
        # object-list
        var_supply_fan_name = "object-list|Supply Fan Name"
        obj.supply_fan_name = var_supply_fan_name
        # alpha
        var_fan_placement = "BlowThrough"
        obj.fan_placement = var_fan_placement
        # alpha
        var_heating_coil_object_type = "Coil:Heating:Gas"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:DX:SingleSpeed"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # alpha
        var_dehumidification_control_type = "None"
        obj.dehumidification_control_type = var_dehumidification_control_type
        # alpha
        var_reheat_coil_object_type = "Coil:Heating:Gas"
        obj.reheat_coil_object_type = var_reheat_coil_object_type
        # object-list
        var_reheat_coil_name = "object-list|Reheat Coil Name"
        obj.reheat_coil_name = var_reheat_coil_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].name, var_name)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].furnace_air_inlet_node_name, var_furnace_air_inlet_node_name)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].furnace_air_outlet_node_name, var_furnace_air_outlet_node_name)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertAlmostEqual(idf2.airloophvacunitaryfurnaceheatcools[0].maximum_supply_air_temperature, var_maximum_supply_air_temperature)
        self.assertAlmostEqual(idf2.airloophvacunitaryfurnaceheatcools[0].supply_air_flow_rate_during_cooling_operation, var_supply_air_flow_rate_during_cooling_operation)
        self.assertAlmostEqual(idf2.airloophvacunitaryfurnaceheatcools[0].supply_air_flow_rate_during_heating_operation, var_supply_air_flow_rate_during_heating_operation)
        self.assertAlmostEqual(idf2.airloophvacunitaryfurnaceheatcools[0].supply_air_flow_rate_when_no_cooling_or_heating_is_needed, var_supply_air_flow_rate_when_no_cooling_or_heating_is_needed)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].controlling_zone_or_thermostat_location, var_controlling_zone_or_thermostat_location)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].supply_fan_object_type, var_supply_fan_object_type)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].supply_fan_name, var_supply_fan_name)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].fan_placement, var_fan_placement)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].heating_coil_name, var_heating_coil_name)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].cooling_coil_name, var_cooling_coil_name)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].reheat_coil_object_type, var_reheat_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryfurnaceheatcools[0].reheat_coil_name, var_reheat_coil_name)