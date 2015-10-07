import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.unitary_equipment import AirLoopHvacUnitaryHeatPumpAirToAirMultiSpeed

log = logging.getLogger(__name__)

class TestAirLoopHvacUnitaryHeatPumpAirToAirMultiSpeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacunitaryheatpumpairtoairmultispeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacUnitaryHeatPumpAirToAirMultiSpeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # object-list
        var_controlling_zone_or_thermostat_location = "object-list|Controlling Zone or Thermostat Location"
        obj.controlling_zone_or_thermostat_location = var_controlling_zone_or_thermostat_location
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
        var_heating_coil_object_type = "Coil:Heating:DX:MultiSpeed"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # real
        var_minimum_outdoor_drybulb_temperature_for_compressor_operation = 12.12
        obj.minimum_outdoor_drybulb_temperature_for_compressor_operation = var_minimum_outdoor_drybulb_temperature_for_compressor_operation
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:DX:MultiSpeed"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # alpha
        var_supplemental_heating_coil_object_type = "Coil:Heating:Gas"
        obj.supplemental_heating_coil_object_type = var_supplemental_heating_coil_object_type
        # object-list
        var_supplemental_heating_coil_name = "object-list|Supplemental Heating Coil Name"
        obj.supplemental_heating_coil_name = var_supplemental_heating_coil_name
        # real
        var_maximum_supply_air_temperature_from_supplemental_heater = 17.17
        obj.maximum_supply_air_temperature_from_supplemental_heater = var_maximum_supply_air_temperature_from_supplemental_heater
        # real
        var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = 21.0
        obj.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation
        # real
        var_auxiliary_oncycle_electric_power = 0.0
        obj.auxiliary_oncycle_electric_power = var_auxiliary_oncycle_electric_power
        # real
        var_auxiliary_offcycle_electric_power = 0.0
        obj.auxiliary_offcycle_electric_power = var_auxiliary_offcycle_electric_power
        # real
        var_design_heat_recovery_water_flow_rate = 0.0
        obj.design_heat_recovery_water_flow_rate = var_design_heat_recovery_water_flow_rate
        # real
        var_maximum_temperature_for_heat_recovery = 50.0
        obj.maximum_temperature_for_heat_recovery = var_maximum_temperature_for_heat_recovery
        # node
        var_heat_recovery_water_inlet_node_name = "node|Heat Recovery Water Inlet Node Name"
        obj.heat_recovery_water_inlet_node_name = var_heat_recovery_water_inlet_node_name
        # node
        var_heat_recovery_water_outlet_node_name = "node|Heat Recovery Water Outlet Node Name"
        obj.heat_recovery_water_outlet_node_name = var_heat_recovery_water_outlet_node_name
        # real
        var_no_load_supply_air_flow_rate = 0.0
        obj.no_load_supply_air_flow_rate = var_no_load_supply_air_flow_rate
        # integer
        var_number_of_speeds_for_heating = 2
        obj.number_of_speeds_for_heating = var_number_of_speeds_for_heating
        # integer
        var_number_of_speeds_for_cooling = 3
        obj.number_of_speeds_for_cooling = var_number_of_speeds_for_cooling
        # real
        var_heating_speed_1_supply_air_flow_rate = 0.0001
        obj.heating_speed_1_supply_air_flow_rate = var_heating_speed_1_supply_air_flow_rate
        # real
        var_heating_speed_2_supply_air_flow_rate = 0.0001
        obj.heating_speed_2_supply_air_flow_rate = var_heating_speed_2_supply_air_flow_rate
        # real
        var_heating_speed_3_supply_air_flow_rate = 0.0001
        obj.heating_speed_3_supply_air_flow_rate = var_heating_speed_3_supply_air_flow_rate
        # real
        var_heating_speed_4_supply_air_flow_rate = 0.0001
        obj.heating_speed_4_supply_air_flow_rate = var_heating_speed_4_supply_air_flow_rate
        # real
        var_cooling_speed_1_supply_air_flow_rate = 0.0001
        obj.cooling_speed_1_supply_air_flow_rate = var_cooling_speed_1_supply_air_flow_rate
        # real
        var_cooling_speed_2_supply_air_flow_rate = 0.0001
        obj.cooling_speed_2_supply_air_flow_rate = var_cooling_speed_2_supply_air_flow_rate
        # real
        var_cooling_speed_3_supply_air_flow_rate = 0.0001
        obj.cooling_speed_3_supply_air_flow_rate = var_cooling_speed_3_supply_air_flow_rate
        # real
        var_cooling_speed_4_supply_air_flow_rate = 0.0001
        obj.cooling_speed_4_supply_air_flow_rate = var_cooling_speed_4_supply_air_flow_rate

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].name, var_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].controlling_zone_or_thermostat_location, var_controlling_zone_or_thermostat_location)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].supply_air_fan_placement, var_supply_air_fan_placement)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].heating_coil_name, var_heating_coil_name)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].minimum_outdoor_drybulb_temperature_for_compressor_operation, var_minimum_outdoor_drybulb_temperature_for_compressor_operation)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].cooling_coil_name, var_cooling_coil_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].supplemental_heating_coil_object_type, var_supplemental_heating_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].supplemental_heating_coil_name, var_supplemental_heating_coil_name)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].maximum_supply_air_temperature_from_supplemental_heater, var_maximum_supply_air_temperature_from_supplemental_heater)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation, var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].auxiliary_oncycle_electric_power, var_auxiliary_oncycle_electric_power)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].auxiliary_offcycle_electric_power, var_auxiliary_offcycle_electric_power)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].design_heat_recovery_water_flow_rate, var_design_heat_recovery_water_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].maximum_temperature_for_heat_recovery, var_maximum_temperature_for_heat_recovery)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].heat_recovery_water_inlet_node_name, var_heat_recovery_water_inlet_node_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].heat_recovery_water_outlet_node_name, var_heat_recovery_water_outlet_node_name)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].no_load_supply_air_flow_rate, var_no_load_supply_air_flow_rate)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].number_of_speeds_for_heating, var_number_of_speeds_for_heating)
        self.assertEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].number_of_speeds_for_cooling, var_number_of_speeds_for_cooling)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].heating_speed_1_supply_air_flow_rate, var_heating_speed_1_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].heating_speed_2_supply_air_flow_rate, var_heating_speed_2_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].heating_speed_3_supply_air_flow_rate, var_heating_speed_3_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].heating_speed_4_supply_air_flow_rate, var_heating_speed_4_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].cooling_speed_1_supply_air_flow_rate, var_cooling_speed_1_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].cooling_speed_2_supply_air_flow_rate, var_cooling_speed_2_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].cooling_speed_3_supply_air_flow_rate, var_cooling_speed_3_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpairtoairmultispeeds[0].cooling_speed_4_supply_air_flow_rate, var_cooling_speed_4_supply_air_flow_rate)