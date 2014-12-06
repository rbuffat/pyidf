import os
import tempfile
import unittest
import pyidf
from pyidf.unitary_equipment import AirLoopHvacUnitarySystem
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirLoopHvacUnitarySystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacunitarysystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacUnitarySystem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_type = "Load"
        obj.control_type = var_control_type
        # object-list
        var_controlling_zone_or_thermostat_location = "object-list|Controlling Zone or Thermostat Location"
        obj.controlling_zone_or_thermostat_location = var_controlling_zone_or_thermostat_location
        # alpha
        var_dehumidification_control_type = "None"
        obj.dehumidification_control_type = var_dehumidification_control_type
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_supply_fan_object_type = "Fan:OnOff"
        obj.supply_fan_object_type = var_supply_fan_object_type
        # object-list
        var_supply_fan_name = "object-list|Supply Fan Name"
        obj.supply_fan_name = var_supply_fan_name
        # alpha
        var_fan_placement = "BlowThrough"
        obj.fan_placement = var_fan_placement
        # object-list
        var_supply_air_fan_operating_mode_schedule_name = "object-list|Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
        # alpha
        var_heating_coil_object_type = "Coil:Heating:DX:SingleSpeed"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # real
        var_dx_heating_coil_sizing_ratio = 0.0001
        obj.dx_heating_coil_sizing_ratio = var_dx_heating_coil_sizing_ratio
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:DX:SingleSpeed"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # alpha
        var_use_doas_dx_cooling_coil = "Yes"
        obj.use_doas_dx_cooling_coil = var_use_doas_dx_cooling_coil
        # real
        var_doas_dx_cooling_coil_leaving_minimum_air_temperature = 3.6
        obj.doas_dx_cooling_coil_leaving_minimum_air_temperature = var_doas_dx_cooling_coil_leaving_minimum_air_temperature
        # alpha
        var_latent_load_control = "SensibleOnlyLoadControl"
        obj.latent_load_control = var_latent_load_control
        # alpha
        var_supplemental_heating_coil_object_type = "Coil:Heating:Gas"
        obj.supplemental_heating_coil_object_type = var_supplemental_heating_coil_object_type
        # object-list
        var_supplemental_heating_coil_name = "object-list|Supplemental Heating Coil Name"
        obj.supplemental_heating_coil_name = var_supplemental_heating_coil_name
        # alpha
        var_supply_air_flow_rate_method_during_cooling_operation = "None"
        obj.supply_air_flow_rate_method_during_cooling_operation = var_supply_air_flow_rate_method_during_cooling_operation
        # real
        var_supply_air_flow_rate_during_cooling_operation = 0.0
        obj.supply_air_flow_rate_during_cooling_operation = var_supply_air_flow_rate_during_cooling_operation
        # real
        var_supply_air_flow_rate_per_floor_area_during_cooling_operation = 0.0
        obj.supply_air_flow_rate_per_floor_area_during_cooling_operation = var_supply_air_flow_rate_per_floor_area_during_cooling_operation
        # real
        var_fraction_of_autosized_design_cooling_supply_air_flow_rate = 0.0
        obj.fraction_of_autosized_design_cooling_supply_air_flow_rate = var_fraction_of_autosized_design_cooling_supply_air_flow_rate
        # real
        var_design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation = 0.0
        obj.design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation = var_design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation
        # alpha
        var_supply_air_flow_rate_method_during_heating_operation = "None"
        obj.supply_air_flow_rate_method_during_heating_operation = var_supply_air_flow_rate_method_during_heating_operation
        # real
        var_supply_air_flow_rate_during_heating_operation = 0.0
        obj.supply_air_flow_rate_during_heating_operation = var_supply_air_flow_rate_during_heating_operation
        # real
        var_supply_air_flow_rate_per_floor_area_during_heating_operation = 0.0
        obj.supply_air_flow_rate_per_floor_area_during_heating_operation = var_supply_air_flow_rate_per_floor_area_during_heating_operation
        # real
        var_fraction_of_autosized_design_heating_supply_air_flow_rate = 0.0
        obj.fraction_of_autosized_design_heating_supply_air_flow_rate = var_fraction_of_autosized_design_heating_supply_air_flow_rate
        # real
        var_design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation = 0.0
        obj.design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation = var_design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation
        # alpha
        var_supply_air_flow_rate_method_when_no_cooling_or_heating_is_required = "None"
        obj.supply_air_flow_rate_method_when_no_cooling_or_heating_is_required = var_supply_air_flow_rate_method_when_no_cooling_or_heating_is_required
        # real
        var_supply_air_flow_rate_when_no_cooling_or_heating_is_required = 0.0
        obj.supply_air_flow_rate_when_no_cooling_or_heating_is_required = var_supply_air_flow_rate_when_no_cooling_or_heating_is_required
        # real
        var_supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required = 0.0
        obj.supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required = var_supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required
        # real
        var_fraction_of_autosized_design_cooling_supply_air_flow_rate_v3 = 0.0
        obj.fraction_of_autosized_design_cooling_supply_air_flow_rate_v3 = var_fraction_of_autosized_design_cooling_supply_air_flow_rate_v3
        # real
        var_fraction_of_autosized_design_heating_supply_air_flow_rate_v3 = 0.0
        obj.fraction_of_autosized_design_heating_supply_air_flow_rate_v3 = var_fraction_of_autosized_design_heating_supply_air_flow_rate_v3
        # real
        var_design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v3 = 0.0
        obj.design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v3 = var_design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v3
        # real
        var_design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v3 = 0.0
        obj.design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v3 = var_design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v3
        # real
        var_maximum_supply_air_temperature = 39.39
        obj.maximum_supply_air_temperature = var_maximum_supply_air_temperature
        # real
        var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = 40.4
        obj.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation
        # node
        var_outdoor_drybulb_temperature_sensor_node_name = "node|Outdoor Dry-Bulb Temperature Sensor Node Name"
        obj.outdoor_drybulb_temperature_sensor_node_name = var_outdoor_drybulb_temperature_sensor_node_name
        # real
        var_maximum_cycling_rate = 2.5
        obj.maximum_cycling_rate = var_maximum_cycling_rate
        # real
        var_heat_pump_time_constant = 250.0
        obj.heat_pump_time_constant = var_heat_pump_time_constant
        # real
        var_fraction_of_oncycle_power_use = 0.025
        obj.fraction_of_oncycle_power_use = var_fraction_of_oncycle_power_use
        # real
        var_heat_pump_fan_delay_time = 0.0
        obj.heat_pump_fan_delay_time = var_heat_pump_fan_delay_time
        # real
        var_ancilliary_oncycle_electric_power = 0.0
        obj.ancilliary_oncycle_electric_power = var_ancilliary_oncycle_electric_power
        # real
        var_ancilliary_offcycle_electric_power = 0.0
        obj.ancilliary_offcycle_electric_power = var_ancilliary_offcycle_electric_power
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
        # alpha
        var_design_specification_multispeed_heat_pump_object_type = "UnitarySystemPerformance:HeatPump:Multispeed"
        obj.design_specification_multispeed_heat_pump_object_type = var_design_specification_multispeed_heat_pump_object_type
        # object-list
        var_design_specification_multispeed_heat_pump_object_name = "object-list|Design Specification Multispeed Heat Pump Object Name"
        obj.design_specification_multispeed_heat_pump_object_name = var_design_specification_multispeed_heat_pump_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacunitarysystems[0].name, var_name)
        self.assertEqual(idf2.airloophvacunitarysystems[0].control_type, var_control_type)
        self.assertEqual(idf2.airloophvacunitarysystems[0].controlling_zone_or_thermostat_location, var_controlling_zone_or_thermostat_location)
        self.assertEqual(idf2.airloophvacunitarysystems[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertEqual(idf2.airloophvacunitarysystems[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airloophvacunitarysystems[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.airloophvacunitarysystems[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.airloophvacunitarysystems[0].supply_fan_object_type, var_supply_fan_object_type)
        self.assertEqual(idf2.airloophvacunitarysystems[0].supply_fan_name, var_supply_fan_name)
        self.assertEqual(idf2.airloophvacunitarysystems[0].fan_placement, var_fan_placement)
        self.assertEqual(idf2.airloophvacunitarysystems[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.airloophvacunitarysystems[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.airloophvacunitarysystems[0].heating_coil_name, var_heating_coil_name)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].dx_heating_coil_sizing_ratio, var_dx_heating_coil_sizing_ratio)
        self.assertEqual(idf2.airloophvacunitarysystems[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.airloophvacunitarysystems[0].cooling_coil_name, var_cooling_coil_name)
        self.assertEqual(idf2.airloophvacunitarysystems[0].use_doas_dx_cooling_coil, var_use_doas_dx_cooling_coil)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].doas_dx_cooling_coil_leaving_minimum_air_temperature, var_doas_dx_cooling_coil_leaving_minimum_air_temperature)
        self.assertEqual(idf2.airloophvacunitarysystems[0].latent_load_control, var_latent_load_control)
        self.assertEqual(idf2.airloophvacunitarysystems[0].supplemental_heating_coil_object_type, var_supplemental_heating_coil_object_type)
        self.assertEqual(idf2.airloophvacunitarysystems[0].supplemental_heating_coil_name, var_supplemental_heating_coil_name)
        self.assertEqual(idf2.airloophvacunitarysystems[0].supply_air_flow_rate_method_during_cooling_operation, var_supply_air_flow_rate_method_during_cooling_operation)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].supply_air_flow_rate_during_cooling_operation, var_supply_air_flow_rate_during_cooling_operation)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].supply_air_flow_rate_per_floor_area_during_cooling_operation, var_supply_air_flow_rate_per_floor_area_during_cooling_operation)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].fraction_of_autosized_design_cooling_supply_air_flow_rate, var_fraction_of_autosized_design_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation, var_design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation)
        self.assertEqual(idf2.airloophvacunitarysystems[0].supply_air_flow_rate_method_during_heating_operation, var_supply_air_flow_rate_method_during_heating_operation)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].supply_air_flow_rate_during_heating_operation, var_supply_air_flow_rate_during_heating_operation)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].supply_air_flow_rate_per_floor_area_during_heating_operation, var_supply_air_flow_rate_per_floor_area_during_heating_operation)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].fraction_of_autosized_design_heating_supply_air_flow_rate, var_fraction_of_autosized_design_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation, var_design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation)
        self.assertEqual(idf2.airloophvacunitarysystems[0].supply_air_flow_rate_method_when_no_cooling_or_heating_is_required, var_supply_air_flow_rate_method_when_no_cooling_or_heating_is_required)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].supply_air_flow_rate_when_no_cooling_or_heating_is_required, var_supply_air_flow_rate_when_no_cooling_or_heating_is_required)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required, var_supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].fraction_of_autosized_design_cooling_supply_air_flow_rate_v3, var_fraction_of_autosized_design_cooling_supply_air_flow_rate_v3)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].fraction_of_autosized_design_heating_supply_air_flow_rate_v3, var_fraction_of_autosized_design_heating_supply_air_flow_rate_v3)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v3, var_design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v3)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v3, var_design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v3)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].maximum_supply_air_temperature, var_maximum_supply_air_temperature)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation, var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation)
        self.assertEqual(idf2.airloophvacunitarysystems[0].outdoor_drybulb_temperature_sensor_node_name, var_outdoor_drybulb_temperature_sensor_node_name)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].maximum_cycling_rate, var_maximum_cycling_rate)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].heat_pump_time_constant, var_heat_pump_time_constant)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].fraction_of_oncycle_power_use, var_fraction_of_oncycle_power_use)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].heat_pump_fan_delay_time, var_heat_pump_fan_delay_time)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].ancilliary_oncycle_electric_power, var_ancilliary_oncycle_electric_power)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].ancilliary_offcycle_electric_power, var_ancilliary_offcycle_electric_power)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].design_heat_recovery_water_flow_rate, var_design_heat_recovery_water_flow_rate)
        self.assertAlmostEqual(idf2.airloophvacunitarysystems[0].maximum_temperature_for_heat_recovery, var_maximum_temperature_for_heat_recovery)
        self.assertEqual(idf2.airloophvacunitarysystems[0].heat_recovery_water_inlet_node_name, var_heat_recovery_water_inlet_node_name)
        self.assertEqual(idf2.airloophvacunitarysystems[0].heat_recovery_water_outlet_node_name, var_heat_recovery_water_outlet_node_name)
        self.assertEqual(idf2.airloophvacunitarysystems[0].design_specification_multispeed_heat_pump_object_type, var_design_specification_multispeed_heat_pump_object_type)
        self.assertEqual(idf2.airloophvacunitarysystems[0].design_specification_multispeed_heat_pump_object_name, var_design_specification_multispeed_heat_pump_object_name)