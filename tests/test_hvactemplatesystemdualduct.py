import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplateSystemDualDuct
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplateSystemDualDuct(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatesystemdualduct(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateSystemDualDuct()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_system_availability_schedule_name = "object-list|System Availability Schedule Name"
        obj.system_availability_schedule_name = var_system_availability_schedule_name
        # alpha
        var_system_configuration_type = "SingleFanConstantVolume"
        obj.system_configuration_type = var_system_configuration_type
        # real
        var_main_supply_fan_maximum_flow_rate = 0.0001
        obj.main_supply_fan_maximum_flow_rate = var_main_supply_fan_maximum_flow_rate
        # real
        var_main_supply_fan_minimum_flow_fraction = 0.5
        obj.main_supply_fan_minimum_flow_fraction = var_main_supply_fan_minimum_flow_fraction
        # real
        var_main_supply_fan_total_efficiency = 0.50005
        obj.main_supply_fan_total_efficiency = var_main_supply_fan_total_efficiency
        # real
        var_main_supply_fan_delta_pressure = 0.0
        obj.main_supply_fan_delta_pressure = var_main_supply_fan_delta_pressure
        # real
        var_main_supply_fan_motor_efficiency = 0.50005
        obj.main_supply_fan_motor_efficiency = var_main_supply_fan_motor_efficiency
        # real
        var_main_supply_fan_motor_in_air_stream_fraction = 0.5
        obj.main_supply_fan_motor_in_air_stream_fraction = var_main_supply_fan_motor_in_air_stream_fraction
        # alpha
        var_main_supply_fan_partload_power_coefficients = "InletVaneDampers"
        obj.main_supply_fan_partload_power_coefficients = var_main_supply_fan_partload_power_coefficients
        # real
        var_cold_duct_supply_fan_maximum_flow_rate = 0.0001
        obj.cold_duct_supply_fan_maximum_flow_rate = var_cold_duct_supply_fan_maximum_flow_rate
        # real
        var_cold_duct_supply_fan_minimum_flow_fraction = 0.5
        obj.cold_duct_supply_fan_minimum_flow_fraction = var_cold_duct_supply_fan_minimum_flow_fraction
        # real
        var_cold_duct_supply_fan_total_efficiency = 0.50005
        obj.cold_duct_supply_fan_total_efficiency = var_cold_duct_supply_fan_total_efficiency
        # real
        var_cold_duct_supply_fan_delta_pressure = 0.0
        obj.cold_duct_supply_fan_delta_pressure = var_cold_duct_supply_fan_delta_pressure
        # real
        var_cold_duct_supply_fan_motor_efficiency = 0.50005
        obj.cold_duct_supply_fan_motor_efficiency = var_cold_duct_supply_fan_motor_efficiency
        # real
        var_cold_duct_supply_fan_motor_in_air_stream_fraction = 0.5
        obj.cold_duct_supply_fan_motor_in_air_stream_fraction = var_cold_duct_supply_fan_motor_in_air_stream_fraction
        # alpha
        var_cold_duct_supply_fan_partload_power_coefficients = "InletVaneDampers"
        obj.cold_duct_supply_fan_partload_power_coefficients = var_cold_duct_supply_fan_partload_power_coefficients
        # alpha
        var_cold_duct_supply_fan_placement = "BlowThrough"
        obj.cold_duct_supply_fan_placement = var_cold_duct_supply_fan_placement
        # real
        var_hot_duct_supply_fan_maximum_flow_rate = 0.0001
        obj.hot_duct_supply_fan_maximum_flow_rate = var_hot_duct_supply_fan_maximum_flow_rate
        # real
        var_hot_duct_supply_fan_minimum_flow_fraction = 0.5
        obj.hot_duct_supply_fan_minimum_flow_fraction = var_hot_duct_supply_fan_minimum_flow_fraction
        # real
        var_hot_duct_supply_fan_total_efficiency = 0.50005
        obj.hot_duct_supply_fan_total_efficiency = var_hot_duct_supply_fan_total_efficiency
        # real
        var_hot_duct_supply_fan_delta_pressure = 0.0
        obj.hot_duct_supply_fan_delta_pressure = var_hot_duct_supply_fan_delta_pressure
        # real
        var_hot_duct_supply_fan_motor_efficiency = 0.50005
        obj.hot_duct_supply_fan_motor_efficiency = var_hot_duct_supply_fan_motor_efficiency
        # real
        var_hot_duct_supply_fan_motor_in_air_stream_fraction = 0.5
        obj.hot_duct_supply_fan_motor_in_air_stream_fraction = var_hot_duct_supply_fan_motor_in_air_stream_fraction
        # alpha
        var_hot_duct_supply_fan_partload_power_coefficients = "InletVaneDampers"
        obj.hot_duct_supply_fan_partload_power_coefficients = var_hot_duct_supply_fan_partload_power_coefficients
        # alpha
        var_hot_duct_supply_fan_placement = "BlowThrough"
        obj.hot_duct_supply_fan_placement = var_hot_duct_supply_fan_placement
        # alpha
        var_cooling_coil_type = "ChilledWater"
        obj.cooling_coil_type = var_cooling_coil_type
        # object-list
        var_cooling_coil_availability_schedule_name = "object-list|Cooling Coil Availability Schedule Name"
        obj.cooling_coil_availability_schedule_name = var_cooling_coil_availability_schedule_name
        # alpha
        var_cooling_coil_setpoint_control_type = "FixedSetpoint"
        obj.cooling_coil_setpoint_control_type = var_cooling_coil_setpoint_control_type
        # real
        var_cooling_coil_design_setpoint_temperature = 30.3
        obj.cooling_coil_design_setpoint_temperature = var_cooling_coil_design_setpoint_temperature
        # object-list
        var_cooling_coil_setpoint_schedule_name = "object-list|Cooling Coil Setpoint Schedule Name"
        obj.cooling_coil_setpoint_schedule_name = var_cooling_coil_setpoint_schedule_name
        # real
        var_cooling_coil_setpoint_at_outdoor_drybulb_low = 32.32
        obj.cooling_coil_setpoint_at_outdoor_drybulb_low = var_cooling_coil_setpoint_at_outdoor_drybulb_low
        # real
        var_cooling_coil_reset_outdoor_drybulb_low = 33.33
        obj.cooling_coil_reset_outdoor_drybulb_low = var_cooling_coil_reset_outdoor_drybulb_low
        # real
        var_cooling_coil_setpoint_at_outdoor_drybulb_high = 34.34
        obj.cooling_coil_setpoint_at_outdoor_drybulb_high = var_cooling_coil_setpoint_at_outdoor_drybulb_high
        # real
        var_cooling_coil_reset_outdoor_drybulb_high = 35.35
        obj.cooling_coil_reset_outdoor_drybulb_high = var_cooling_coil_reset_outdoor_drybulb_high
        # alpha
        var_heating_coil_type = "HotWater"
        obj.heating_coil_type = var_heating_coil_type
        # object-list
        var_heating_coil_availability_schedule_name = "object-list|Heating Coil Availability Schedule Name"
        obj.heating_coil_availability_schedule_name = var_heating_coil_availability_schedule_name
        # alpha
        var_heating_coil_setpoint_control_type = "FixedSetpoint"
        obj.heating_coil_setpoint_control_type = var_heating_coil_setpoint_control_type
        # real
        var_heating_coil_design_setpoint = 39.39
        obj.heating_coil_design_setpoint = var_heating_coil_design_setpoint
        # object-list
        var_heating_coil_setpoint_schedule_name = "object-list|Heating Coil Setpoint Schedule Name"
        obj.heating_coil_setpoint_schedule_name = var_heating_coil_setpoint_schedule_name
        # real
        var_heating_coil_setpoint_at_outdoor_drybulb_low = 41.41
        obj.heating_coil_setpoint_at_outdoor_drybulb_low = var_heating_coil_setpoint_at_outdoor_drybulb_low
        # real
        var_heating_coil_reset_outdoor_drybulb_low = 42.42
        obj.heating_coil_reset_outdoor_drybulb_low = var_heating_coil_reset_outdoor_drybulb_low
        # real
        var_heating_coil_setpoint_at_outdoor_drybulb_high = 43.43
        obj.heating_coil_setpoint_at_outdoor_drybulb_high = var_heating_coil_setpoint_at_outdoor_drybulb_high
        # real
        var_heating_coil_reset_outdoor_drybulb_high = 44.44
        obj.heating_coil_reset_outdoor_drybulb_high = var_heating_coil_reset_outdoor_drybulb_high
        # real
        var_heating_coil_capacity = 45.45
        obj.heating_coil_capacity = var_heating_coil_capacity
        # real
        var_gas_heating_coil_efficiency = 0.5
        obj.gas_heating_coil_efficiency = var_gas_heating_coil_efficiency
        # real
        var_gas_heating_coil_parasitic_electric_load = 0.0
        obj.gas_heating_coil_parasitic_electric_load = var_gas_heating_coil_parasitic_electric_load
        # alpha
        var_preheat_coil_type = "Electric"
        obj.preheat_coil_type = var_preheat_coil_type
        # object-list
        var_preheat_coil_availability_schedule_name = "object-list|Preheat Coil Availability Schedule Name"
        obj.preheat_coil_availability_schedule_name = var_preheat_coil_availability_schedule_name
        # real
        var_preheat_coil_design_setpoint = 50.5
        obj.preheat_coil_design_setpoint = var_preheat_coil_design_setpoint
        # object-list
        var_preheat_coil_setpoint_schedule_name = "object-list|Preheat Coil Setpoint Schedule Name"
        obj.preheat_coil_setpoint_schedule_name = var_preheat_coil_setpoint_schedule_name
        # real
        var_gas_preheat_coil_efficiency = 0.5
        obj.gas_preheat_coil_efficiency = var_gas_preheat_coil_efficiency
        # real
        var_gas_preheat_coil_parasitic_electric_load = 0.0
        obj.gas_preheat_coil_parasitic_electric_load = var_gas_preheat_coil_parasitic_electric_load
        # real
        var_maximum_outdoor_air_flow_rate = 0.0
        obj.maximum_outdoor_air_flow_rate = var_maximum_outdoor_air_flow_rate
        # real
        var_minimum_outdoor_air_flow_rate = 0.0
        obj.minimum_outdoor_air_flow_rate = var_minimum_outdoor_air_flow_rate
        # alpha
        var_minimum_outdoor_air_control_type = "FixedMinimum"
        obj.minimum_outdoor_air_control_type = var_minimum_outdoor_air_control_type
        # object-list
        var_minimum_outdoor_air_schedule_name = "object-list|Minimum Outdoor Air Schedule Name"
        obj.minimum_outdoor_air_schedule_name = var_minimum_outdoor_air_schedule_name
        # alpha
        var_economizer_type = "FixedDryBulb"
        obj.economizer_type = var_economizer_type
        # alpha
        var_economizer_lockout = "NoLockout"
        obj.economizer_lockout = var_economizer_lockout
        # real
        var_economizer_upper_temperature_limit = 60.6
        obj.economizer_upper_temperature_limit = var_economizer_upper_temperature_limit
        # real
        var_economizer_lower_temperature_limit = 61.61
        obj.economizer_lower_temperature_limit = var_economizer_lower_temperature_limit
        # real
        var_economizer_upper_enthalpy_limit = 62.62
        obj.economizer_upper_enthalpy_limit = var_economizer_upper_enthalpy_limit
        # real
        var_economizer_maximum_limit_dewpoint_temperature = 63.63
        obj.economizer_maximum_limit_dewpoint_temperature = var_economizer_maximum_limit_dewpoint_temperature
        # object-list
        var_cold_supply_plenum_name = "object-list|Cold Supply Plenum Name"
        obj.cold_supply_plenum_name = var_cold_supply_plenum_name
        # object-list
        var_hot_supply_plenum_name = "object-list|Hot Supply Plenum Name"
        obj.hot_supply_plenum_name = var_hot_supply_plenum_name
        # object-list
        var_return_plenum_name = "object-list|Return Plenum Name"
        obj.return_plenum_name = var_return_plenum_name
        # alpha
        var_night_cycle_control = "StayOff"
        obj.night_cycle_control = var_night_cycle_control
        # object-list
        var_night_cycle_control_zone_name = "object-list|Night Cycle Control Zone Name"
        obj.night_cycle_control_zone_name = var_night_cycle_control_zone_name
        # alpha
        var_heat_recovery_type = "None"
        obj.heat_recovery_type = var_heat_recovery_type
        # real
        var_sensible_heat_recovery_effectiveness = 0.5
        obj.sensible_heat_recovery_effectiveness = var_sensible_heat_recovery_effectiveness
        # real
        var_latent_heat_recovery_effectiveness = 0.5
        obj.latent_heat_recovery_effectiveness = var_latent_heat_recovery_effectiveness
        # alpha
        var_heat_recovery_heat_exchanger_type = "Plate"
        obj.heat_recovery_heat_exchanger_type = var_heat_recovery_heat_exchanger_type
        # alpha
        var_heat_recovery_frost_control_type = "None"
        obj.heat_recovery_frost_control_type = var_heat_recovery_frost_control_type
        # alpha
        var_dehumidification_control_type = "None"
        obj.dehumidification_control_type = var_dehumidification_control_type
        # object-list
        var_dehumidification_control_zone_name = "object-list|Dehumidification Control Zone Name"
        obj.dehumidification_control_zone_name = var_dehumidification_control_zone_name
        # real
        var_dehumidification_relative_humidity_setpoint = 50.0
        obj.dehumidification_relative_humidity_setpoint = var_dehumidification_relative_humidity_setpoint
        # object-list
        var_dehumidification_relative_humidity_setpoint_schedule_name = "object-list|Dehumidification Relative Humidity Setpoint Schedule Name"
        obj.dehumidification_relative_humidity_setpoint_schedule_name = var_dehumidification_relative_humidity_setpoint_schedule_name
        # alpha
        var_humidifier_type = "None"
        obj.humidifier_type = var_humidifier_type
        # object-list
        var_humidifier_availability_schedule_name = "object-list|Humidifier Availability Schedule Name"
        obj.humidifier_availability_schedule_name = var_humidifier_availability_schedule_name
        # real
        var_humidifier_rated_capacity = 0.0
        obj.humidifier_rated_capacity = var_humidifier_rated_capacity
        # real
        var_humidifier_rated_electric_power = 0.0
        obj.humidifier_rated_electric_power = var_humidifier_rated_electric_power
        # object-list
        var_humidifier_control_zone_name = "object-list|Humidifier Control Zone Name"
        obj.humidifier_control_zone_name = var_humidifier_control_zone_name
        # real
        var_humidifier_relative_humidity_setpoint = 50.0
        obj.humidifier_relative_humidity_setpoint = var_humidifier_relative_humidity_setpoint
        # object-list
        var_humidifier_relative_humidity_setpoint_schedule_name = "object-list|Humidifier Relative Humidity Setpoint Schedule Name"
        obj.humidifier_relative_humidity_setpoint_schedule_name = var_humidifier_relative_humidity_setpoint_schedule_name
        # alpha
        var_sizing_option = "Coincident"
        obj.sizing_option = var_sizing_option
        # alpha
        var_return_fan = "Yes"
        obj.return_fan = var_return_fan
        # real
        var_return_fan_total_efficiency = 0.50005
        obj.return_fan_total_efficiency = var_return_fan_total_efficiency
        # real
        var_return_fan_delta_pressure = 0.0
        obj.return_fan_delta_pressure = var_return_fan_delta_pressure
        # real
        var_return_fan_motor_efficiency = 0.50005
        obj.return_fan_motor_efficiency = var_return_fan_motor_efficiency
        # real
        var_return_fan_motor_in_air_stream_fraction = 0.5
        obj.return_fan_motor_in_air_stream_fraction = var_return_fan_motor_in_air_stream_fraction
        # alpha
        var_return_fan_partload_power_coefficients = "InletVaneDampers"
        obj.return_fan_partload_power_coefficients = var_return_fan_partload_power_coefficients

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].name, var_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].system_configuration_type, var_system_configuration_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].main_supply_fan_maximum_flow_rate, var_main_supply_fan_maximum_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].main_supply_fan_minimum_flow_fraction, var_main_supply_fan_minimum_flow_fraction)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].main_supply_fan_total_efficiency, var_main_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].main_supply_fan_delta_pressure, var_main_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].main_supply_fan_motor_efficiency, var_main_supply_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].main_supply_fan_motor_in_air_stream_fraction, var_main_supply_fan_motor_in_air_stream_fraction)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].main_supply_fan_partload_power_coefficients, var_main_supply_fan_partload_power_coefficients)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cold_duct_supply_fan_maximum_flow_rate, var_cold_duct_supply_fan_maximum_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cold_duct_supply_fan_minimum_flow_fraction, var_cold_duct_supply_fan_minimum_flow_fraction)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cold_duct_supply_fan_total_efficiency, var_cold_duct_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cold_duct_supply_fan_delta_pressure, var_cold_duct_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cold_duct_supply_fan_motor_efficiency, var_cold_duct_supply_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cold_duct_supply_fan_motor_in_air_stream_fraction, var_cold_duct_supply_fan_motor_in_air_stream_fraction)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].cold_duct_supply_fan_partload_power_coefficients, var_cold_duct_supply_fan_partload_power_coefficients)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].cold_duct_supply_fan_placement, var_cold_duct_supply_fan_placement)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].hot_duct_supply_fan_maximum_flow_rate, var_hot_duct_supply_fan_maximum_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].hot_duct_supply_fan_minimum_flow_fraction, var_hot_duct_supply_fan_minimum_flow_fraction)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].hot_duct_supply_fan_total_efficiency, var_hot_duct_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].hot_duct_supply_fan_delta_pressure, var_hot_duct_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].hot_duct_supply_fan_motor_efficiency, var_hot_duct_supply_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].hot_duct_supply_fan_motor_in_air_stream_fraction, var_hot_duct_supply_fan_motor_in_air_stream_fraction)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].hot_duct_supply_fan_partload_power_coefficients, var_hot_duct_supply_fan_partload_power_coefficients)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].hot_duct_supply_fan_placement, var_hot_duct_supply_fan_placement)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].cooling_coil_type, var_cooling_coil_type)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].cooling_coil_availability_schedule_name, var_cooling_coil_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].cooling_coil_setpoint_control_type, var_cooling_coil_setpoint_control_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cooling_coil_design_setpoint_temperature, var_cooling_coil_design_setpoint_temperature)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].cooling_coil_setpoint_schedule_name, var_cooling_coil_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cooling_coil_setpoint_at_outdoor_drybulb_low, var_cooling_coil_setpoint_at_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cooling_coil_reset_outdoor_drybulb_low, var_cooling_coil_reset_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cooling_coil_setpoint_at_outdoor_drybulb_high, var_cooling_coil_setpoint_at_outdoor_drybulb_high)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].cooling_coil_reset_outdoor_drybulb_high, var_cooling_coil_reset_outdoor_drybulb_high)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].heating_coil_type, var_heating_coil_type)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].heating_coil_availability_schedule_name, var_heating_coil_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].heating_coil_setpoint_control_type, var_heating_coil_setpoint_control_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].heating_coil_design_setpoint, var_heating_coil_design_setpoint)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].heating_coil_setpoint_schedule_name, var_heating_coil_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].heating_coil_setpoint_at_outdoor_drybulb_low, var_heating_coil_setpoint_at_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].heating_coil_reset_outdoor_drybulb_low, var_heating_coil_reset_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].heating_coil_setpoint_at_outdoor_drybulb_high, var_heating_coil_setpoint_at_outdoor_drybulb_high)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].heating_coil_reset_outdoor_drybulb_high, var_heating_coil_reset_outdoor_drybulb_high)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].heating_coil_capacity, var_heating_coil_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].gas_heating_coil_efficiency, var_gas_heating_coil_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].gas_heating_coil_parasitic_electric_load, var_gas_heating_coil_parasitic_electric_load)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].preheat_coil_type, var_preheat_coil_type)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].preheat_coil_availability_schedule_name, var_preheat_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].preheat_coil_design_setpoint, var_preheat_coil_design_setpoint)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].preheat_coil_setpoint_schedule_name, var_preheat_coil_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].gas_preheat_coil_efficiency, var_gas_preheat_coil_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].gas_preheat_coil_parasitic_electric_load, var_gas_preheat_coil_parasitic_electric_load)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].maximum_outdoor_air_flow_rate, var_maximum_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].minimum_outdoor_air_flow_rate, var_minimum_outdoor_air_flow_rate)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].minimum_outdoor_air_control_type, var_minimum_outdoor_air_control_type)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].minimum_outdoor_air_schedule_name, var_minimum_outdoor_air_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].economizer_type, var_economizer_type)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].economizer_lockout, var_economizer_lockout)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].economizer_upper_temperature_limit, var_economizer_upper_temperature_limit)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].economizer_lower_temperature_limit, var_economizer_lower_temperature_limit)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].economizer_upper_enthalpy_limit, var_economizer_upper_enthalpy_limit)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].economizer_maximum_limit_dewpoint_temperature, var_economizer_maximum_limit_dewpoint_temperature)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].cold_supply_plenum_name, var_cold_supply_plenum_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].hot_supply_plenum_name, var_hot_supply_plenum_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].return_plenum_name, var_return_plenum_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].night_cycle_control, var_night_cycle_control)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].night_cycle_control_zone_name, var_night_cycle_control_zone_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].heat_recovery_type, var_heat_recovery_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].sensible_heat_recovery_effectiveness, var_sensible_heat_recovery_effectiveness)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].latent_heat_recovery_effectiveness, var_latent_heat_recovery_effectiveness)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].heat_recovery_heat_exchanger_type, var_heat_recovery_heat_exchanger_type)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].heat_recovery_frost_control_type, var_heat_recovery_frost_control_type)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].dehumidification_control_zone_name, var_dehumidification_control_zone_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].dehumidification_relative_humidity_setpoint, var_dehumidification_relative_humidity_setpoint)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].dehumidification_relative_humidity_setpoint_schedule_name, var_dehumidification_relative_humidity_setpoint_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].humidifier_type, var_humidifier_type)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].humidifier_availability_schedule_name, var_humidifier_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].humidifier_rated_capacity, var_humidifier_rated_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].humidifier_rated_electric_power, var_humidifier_rated_electric_power)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].humidifier_control_zone_name, var_humidifier_control_zone_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].humidifier_relative_humidity_setpoint, var_humidifier_relative_humidity_setpoint)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].humidifier_relative_humidity_setpoint_schedule_name, var_humidifier_relative_humidity_setpoint_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].sizing_option, var_sizing_option)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].return_fan, var_return_fan)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].return_fan_total_efficiency, var_return_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].return_fan_delta_pressure, var_return_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].return_fan_motor_efficiency, var_return_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdualducts[0].return_fan_motor_in_air_stream_fraction, var_return_fan_motor_in_air_stream_fraction)
        self.assertEqual(idf2.hvactemplatesystemdualducts[0].return_fan_partload_power_coefficients, var_return_fan_partload_power_coefficients)