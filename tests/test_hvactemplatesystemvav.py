import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplateSystemVav

log = logging.getLogger(__name__)

class TestHvactemplateSystemVav(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatesystemvav(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateSystemVav()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_system_availability_schedule_name = "object-list|System Availability Schedule Name"
        obj.system_availability_schedule_name = var_system_availability_schedule_name
        # real
        var_supply_fan_maximum_flow_rate = 0.0001
        obj.supply_fan_maximum_flow_rate = var_supply_fan_maximum_flow_rate
        # real
        var_supply_fan_minimum_flow_rate = 0.0
        obj.supply_fan_minimum_flow_rate = var_supply_fan_minimum_flow_rate
        # real
        var_supply_fan_total_efficiency = 0.50005
        obj.supply_fan_total_efficiency = var_supply_fan_total_efficiency
        # real
        var_supply_fan_delta_pressure = 0.0
        obj.supply_fan_delta_pressure = var_supply_fan_delta_pressure
        # real
        var_supply_fan_motor_efficiency = 0.50005
        obj.supply_fan_motor_efficiency = var_supply_fan_motor_efficiency
        # real
        var_supply_fan_motor_in_air_stream_fraction = 0.5
        obj.supply_fan_motor_in_air_stream_fraction = var_supply_fan_motor_in_air_stream_fraction
        # alpha
        var_cooling_coil_type = "ChilledWater"
        obj.cooling_coil_type = var_cooling_coil_type
        # object-list
        var_cooling_coil_availability_schedule_name = "object-list|Cooling Coil Availability Schedule Name"
        obj.cooling_coil_availability_schedule_name = var_cooling_coil_availability_schedule_name
        # object-list
        var_cooling_coil_setpoint_schedule_name = "object-list|Cooling Coil Setpoint Schedule Name"
        obj.cooling_coil_setpoint_schedule_name = var_cooling_coil_setpoint_schedule_name
        # real
        var_cooling_coil_design_setpoint = 12.12
        obj.cooling_coil_design_setpoint = var_cooling_coil_design_setpoint
        # alpha
        var_heating_coil_type = "HotWater"
        obj.heating_coil_type = var_heating_coil_type
        # object-list
        var_heating_coil_availability_schedule_name = "object-list|Heating Coil Availability Schedule Name"
        obj.heating_coil_availability_schedule_name = var_heating_coil_availability_schedule_name
        # object-list
        var_heating_coil_setpoint_schedule_name = "object-list|Heating Coil Setpoint Schedule Name"
        obj.heating_coil_setpoint_schedule_name = var_heating_coil_setpoint_schedule_name
        # real
        var_heating_coil_design_setpoint = 16.16
        obj.heating_coil_design_setpoint = var_heating_coil_design_setpoint
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
        # object-list
        var_preheat_coil_setpoint_schedule_name = "object-list|Preheat Coil Setpoint Schedule Name"
        obj.preheat_coil_setpoint_schedule_name = var_preheat_coil_setpoint_schedule_name
        # real
        var_preheat_coil_design_setpoint = 22.22
        obj.preheat_coil_design_setpoint = var_preheat_coil_design_setpoint
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
        var_economizer_upper_temperature_limit = 31.31
        obj.economizer_upper_temperature_limit = var_economizer_upper_temperature_limit
        # real
        var_economizer_lower_temperature_limit = 32.32
        obj.economizer_lower_temperature_limit = var_economizer_lower_temperature_limit
        # real
        var_economizer_upper_enthalpy_limit = 33.33
        obj.economizer_upper_enthalpy_limit = var_economizer_upper_enthalpy_limit
        # real
        var_economizer_maximum_limit_dewpoint_temperature = 34.34
        obj.economizer_maximum_limit_dewpoint_temperature = var_economizer_maximum_limit_dewpoint_temperature
        # object-list
        var_supply_plenum_name = "object-list|Supply Plenum Name"
        obj.supply_plenum_name = var_supply_plenum_name
        # object-list
        var_return_plenum_name = "object-list|Return Plenum Name"
        obj.return_plenum_name = var_return_plenum_name
        # alpha
        var_supply_fan_placement = "DrawThrough"
        obj.supply_fan_placement = var_supply_fan_placement
        # alpha
        var_supply_fan_partload_power_coefficients = "InletVaneDampers"
        obj.supply_fan_partload_power_coefficients = var_supply_fan_partload_power_coefficients
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
        var_cooling_coil_setpoint_reset_type = "None"
        obj.cooling_coil_setpoint_reset_type = var_cooling_coil_setpoint_reset_type
        # alpha
        var_heating_coil_setpoint_reset_type = "None"
        obj.heating_coil_setpoint_reset_type = var_heating_coil_setpoint_reset_type
        # alpha
        var_dehumidification_control_type = "None"
        obj.dehumidification_control_type = var_dehumidification_control_type
        # object-list
        var_dehumidification_control_zone_name = "object-list|Dehumidification Control Zone Name"
        obj.dehumidification_control_zone_name = var_dehumidification_control_zone_name
        # real
        var_dehumidification_setpoint = 50.0
        obj.dehumidification_setpoint = var_dehumidification_setpoint
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
        var_humidifier_setpoint = 50.0
        obj.humidifier_setpoint = var_humidifier_setpoint
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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].name, var_name)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].supply_fan_maximum_flow_rate, var_supply_fan_maximum_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].supply_fan_minimum_flow_rate, var_supply_fan_minimum_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].supply_fan_total_efficiency, var_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].supply_fan_delta_pressure, var_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].supply_fan_motor_efficiency, var_supply_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].supply_fan_motor_in_air_stream_fraction, var_supply_fan_motor_in_air_stream_fraction)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].cooling_coil_type, var_cooling_coil_type)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].cooling_coil_availability_schedule_name, var_cooling_coil_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].cooling_coil_setpoint_schedule_name, var_cooling_coil_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].cooling_coil_design_setpoint, var_cooling_coil_design_setpoint)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].heating_coil_type, var_heating_coil_type)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].heating_coil_availability_schedule_name, var_heating_coil_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].heating_coil_setpoint_schedule_name, var_heating_coil_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].heating_coil_design_setpoint, var_heating_coil_design_setpoint)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].gas_heating_coil_efficiency, var_gas_heating_coil_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].gas_heating_coil_parasitic_electric_load, var_gas_heating_coil_parasitic_electric_load)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].preheat_coil_type, var_preheat_coil_type)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].preheat_coil_availability_schedule_name, var_preheat_coil_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].preheat_coil_setpoint_schedule_name, var_preheat_coil_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].preheat_coil_design_setpoint, var_preheat_coil_design_setpoint)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].gas_preheat_coil_efficiency, var_gas_preheat_coil_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].gas_preheat_coil_parasitic_electric_load, var_gas_preheat_coil_parasitic_electric_load)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].maximum_outdoor_air_flow_rate, var_maximum_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].minimum_outdoor_air_flow_rate, var_minimum_outdoor_air_flow_rate)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].minimum_outdoor_air_control_type, var_minimum_outdoor_air_control_type)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].minimum_outdoor_air_schedule_name, var_minimum_outdoor_air_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].economizer_type, var_economizer_type)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].economizer_lockout, var_economizer_lockout)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].economizer_upper_temperature_limit, var_economizer_upper_temperature_limit)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].economizer_lower_temperature_limit, var_economizer_lower_temperature_limit)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].economizer_upper_enthalpy_limit, var_economizer_upper_enthalpy_limit)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].economizer_maximum_limit_dewpoint_temperature, var_economizer_maximum_limit_dewpoint_temperature)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].supply_plenum_name, var_supply_plenum_name)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].return_plenum_name, var_return_plenum_name)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].supply_fan_placement, var_supply_fan_placement)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].supply_fan_partload_power_coefficients, var_supply_fan_partload_power_coefficients)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].night_cycle_control, var_night_cycle_control)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].night_cycle_control_zone_name, var_night_cycle_control_zone_name)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].heat_recovery_type, var_heat_recovery_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].sensible_heat_recovery_effectiveness, var_sensible_heat_recovery_effectiveness)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].latent_heat_recovery_effectiveness, var_latent_heat_recovery_effectiveness)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].cooling_coil_setpoint_reset_type, var_cooling_coil_setpoint_reset_type)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].heating_coil_setpoint_reset_type, var_heating_coil_setpoint_reset_type)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].dehumidification_control_zone_name, var_dehumidification_control_zone_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].dehumidification_setpoint, var_dehumidification_setpoint)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].humidifier_type, var_humidifier_type)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].humidifier_availability_schedule_name, var_humidifier_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].humidifier_rated_capacity, var_humidifier_rated_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].humidifier_rated_electric_power, var_humidifier_rated_electric_power)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].humidifier_control_zone_name, var_humidifier_control_zone_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].humidifier_setpoint, var_humidifier_setpoint)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].sizing_option, var_sizing_option)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].return_fan, var_return_fan)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].return_fan_total_efficiency, var_return_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].return_fan_delta_pressure, var_return_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].return_fan_motor_efficiency, var_return_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemvavs[0].return_fan_motor_in_air_stream_fraction, var_return_fan_motor_in_air_stream_fraction)
        self.assertEqual(idf2.hvactemplatesystemvavs[0].return_fan_partload_power_coefficients, var_return_fan_partload_power_coefficients)