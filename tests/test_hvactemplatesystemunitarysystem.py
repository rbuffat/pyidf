import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplateSystemUnitarySystem
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplateSystemUnitarySystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatesystemunitarysystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateSystemUnitarySystem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_system_availability_schedule_name = "object-list|System Availability Schedule Name"
        obj.system_availability_schedule_name = var_system_availability_schedule_name
        # alpha
        var_control_type = "Load"
        obj.control_type = var_control_type
        # object-list
        var_control_zone_or_thermostat_location_name = "object-list|Control Zone or Thermostat Location Name"
        obj.control_zone_or_thermostat_location_name = var_control_zone_or_thermostat_location_name
        # real
        var_cooling_supply_air_flow_rate = 0.0001
        obj.cooling_supply_air_flow_rate = var_cooling_supply_air_flow_rate
        # real
        var_heating_supply_air_flow_rate = 0.0001
        obj.heating_supply_air_flow_rate = var_heating_supply_air_flow_rate
        # real
        var_no_load_supply_air_flow_rate = 0.0
        obj.no_load_supply_air_flow_rate = var_no_load_supply_air_flow_rate
        # object-list
        var_supply_fan_operating_mode_schedule_name = "object-list|Supply Fan Operating Mode Schedule Name"
        obj.supply_fan_operating_mode_schedule_name = var_supply_fan_operating_mode_schedule_name
        # alpha
        var_supply_fan_placement = "BlowThrough"
        obj.supply_fan_placement = var_supply_fan_placement
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
        var_cooling_coil_type = "SingleSpeedDX"
        obj.cooling_coil_type = var_cooling_coil_type
        # integer
        var_number_of_speeds_for_cooling = 2
        obj.number_of_speeds_for_cooling = var_number_of_speeds_for_cooling
        # object-list
        var_cooling_coil_availability_schedule_name = "object-list|Cooling Coil Availability Schedule Name"
        obj.cooling_coil_availability_schedule_name = var_cooling_coil_availability_schedule_name
        # real
        var_cooling_design_supply_air_temperature = 17.17
        obj.cooling_design_supply_air_temperature = var_cooling_design_supply_air_temperature
        # real
        var_dx_cooling_coil_gross_rated_total_capacity = 18.18
        obj.dx_cooling_coil_gross_rated_total_capacity = var_dx_cooling_coil_gross_rated_total_capacity
        # real
        var_dx_cooling_coil_gross_rated_sensible_heat_ratio = 0.75
        obj.dx_cooling_coil_gross_rated_sensible_heat_ratio = var_dx_cooling_coil_gross_rated_sensible_heat_ratio
        # real
        var_dx_cooling_coil_gross_rated_cop = 0.0001
        obj.dx_cooling_coil_gross_rated_cop = var_dx_cooling_coil_gross_rated_cop
        # alpha
        var_heating_coil_type = "Electric"
        obj.heating_coil_type = var_heating_coil_type
        # integer
        var_number_of_speeds_or_stages_for_heating = 2
        obj.number_of_speeds_or_stages_for_heating = var_number_of_speeds_or_stages_for_heating
        # object-list
        var_heating_coil_availability_schedule_name = "object-list|Heating Coil Availability Schedule Name"
        obj.heating_coil_availability_schedule_name = var_heating_coil_availability_schedule_name
        # real
        var_heating_design_supply_air_temperature = 24.24
        obj.heating_design_supply_air_temperature = var_heating_design_supply_air_temperature
        # real
        var_heating_coil_gross_rated_capacity = 0.0001
        obj.heating_coil_gross_rated_capacity = var_heating_coil_gross_rated_capacity
        # real
        var_gas_heating_coil_efficiency = 0.5
        obj.gas_heating_coil_efficiency = var_gas_heating_coil_efficiency
        # real
        var_gas_heating_coil_parasitic_electric_load = 0.0
        obj.gas_heating_coil_parasitic_electric_load = var_gas_heating_coil_parasitic_electric_load
        # real
        var_heat_pump_heating_coil_gross_rated_cop = 0.0001
        obj.heat_pump_heating_coil_gross_rated_cop = var_heat_pump_heating_coil_gross_rated_cop
        # real
        var_heat_pump_heating_minimum_outdoor_drybulb_temperature = -20.0
        obj.heat_pump_heating_minimum_outdoor_drybulb_temperature = var_heat_pump_heating_minimum_outdoor_drybulb_temperature
        # real
        var_heat_pump_defrost_maximum_outdoor_drybulb_temperature = 3.61
        obj.heat_pump_defrost_maximum_outdoor_drybulb_temperature = var_heat_pump_defrost_maximum_outdoor_drybulb_temperature
        # alpha
        var_heat_pump_defrost_strategy = "ReverseCycle"
        obj.heat_pump_defrost_strategy = var_heat_pump_defrost_strategy
        # alpha
        var_heat_pump_defrost_control = "Timed"
        obj.heat_pump_defrost_control = var_heat_pump_defrost_control
        # real
        var_heat_pump_defrost_time_period_fraction = 0.0
        obj.heat_pump_defrost_time_period_fraction = var_heat_pump_defrost_time_period_fraction
        # alpha
        var_supplemental_heating_or_reheat_coil_type = "Electric"
        obj.supplemental_heating_or_reheat_coil_type = var_supplemental_heating_or_reheat_coil_type
        # object-list
        var_supplemental_heating_or_reheat_coil_availability_schedule_name = "object-list|Supplemental Heating or Reheat Coil Availability Schedule Name"
        obj.supplemental_heating_or_reheat_coil_availability_schedule_name = var_supplemental_heating_or_reheat_coil_availability_schedule_name
        # real
        var_supplemental_heating_or_reheat_coil_capacity = 36.36
        obj.supplemental_heating_or_reheat_coil_capacity = var_supplemental_heating_or_reheat_coil_capacity
        # real
        var_supplemental_heating_or_reheat_coil_maximum_outdoor_drybulb_temperature = 21.0
        obj.supplemental_heating_or_reheat_coil_maximum_outdoor_drybulb_temperature = var_supplemental_heating_or_reheat_coil_maximum_outdoor_drybulb_temperature
        # real
        var_supplemental_gas_heating_or_reheat_coil_efficiency = 0.5
        obj.supplemental_gas_heating_or_reheat_coil_efficiency = var_supplemental_gas_heating_or_reheat_coil_efficiency
        # real
        var_supplemental_gas_heating_or_reheat_coil_parasitic_electric_load = 0.0
        obj.supplemental_gas_heating_or_reheat_coil_parasitic_electric_load = var_supplemental_gas_heating_or_reheat_coil_parasitic_electric_load
        # real
        var_maximum_outdoor_air_flow_rate = 0.0
        obj.maximum_outdoor_air_flow_rate = var_maximum_outdoor_air_flow_rate
        # real
        var_minimum_outdoor_air_flow_rate = 0.0
        obj.minimum_outdoor_air_flow_rate = var_minimum_outdoor_air_flow_rate
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
        var_economizer_maximum_limit_drybulb_temperature = 45.45
        obj.economizer_maximum_limit_drybulb_temperature = var_economizer_maximum_limit_drybulb_temperature
        # real
        var_economizer_maximum_limit_enthalpy = 46.46
        obj.economizer_maximum_limit_enthalpy = var_economizer_maximum_limit_enthalpy
        # real
        var_economizer_maximum_limit_dewpoint_temperature = 47.47
        obj.economizer_maximum_limit_dewpoint_temperature = var_economizer_maximum_limit_dewpoint_temperature
        # real
        var_economizer_minimum_limit_drybulb_temperature = 48.48
        obj.economizer_minimum_limit_drybulb_temperature = var_economizer_minimum_limit_drybulb_temperature
        # object-list
        var_supply_plenum_name = "object-list|Supply Plenum Name"
        obj.supply_plenum_name = var_supply_plenum_name
        # object-list
        var_return_plenum_name = "object-list|Return Plenum Name"
        obj.return_plenum_name = var_return_plenum_name
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

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].name, var_name)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].control_type, var_control_type)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].control_zone_or_thermostat_location_name, var_control_zone_or_thermostat_location_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].cooling_supply_air_flow_rate, var_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].heating_supply_air_flow_rate, var_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].no_load_supply_air_flow_rate, var_no_load_supply_air_flow_rate)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].supply_fan_operating_mode_schedule_name, var_supply_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].supply_fan_placement, var_supply_fan_placement)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].supply_fan_total_efficiency, var_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].supply_fan_delta_pressure, var_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].supply_fan_motor_efficiency, var_supply_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].supply_fan_motor_in_air_stream_fraction, var_supply_fan_motor_in_air_stream_fraction)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].cooling_coil_type, var_cooling_coil_type)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].number_of_speeds_for_cooling, var_number_of_speeds_for_cooling)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].cooling_coil_availability_schedule_name, var_cooling_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].cooling_design_supply_air_temperature, var_cooling_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].dx_cooling_coil_gross_rated_total_capacity, var_dx_cooling_coil_gross_rated_total_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].dx_cooling_coil_gross_rated_sensible_heat_ratio, var_dx_cooling_coil_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].dx_cooling_coil_gross_rated_cop, var_dx_cooling_coil_gross_rated_cop)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].heating_coil_type, var_heating_coil_type)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].number_of_speeds_or_stages_for_heating, var_number_of_speeds_or_stages_for_heating)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].heating_coil_availability_schedule_name, var_heating_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].heating_design_supply_air_temperature, var_heating_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].heating_coil_gross_rated_capacity, var_heating_coil_gross_rated_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].gas_heating_coil_efficiency, var_gas_heating_coil_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].gas_heating_coil_parasitic_electric_load, var_gas_heating_coil_parasitic_electric_load)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].heat_pump_heating_coil_gross_rated_cop, var_heat_pump_heating_coil_gross_rated_cop)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].heat_pump_heating_minimum_outdoor_drybulb_temperature, var_heat_pump_heating_minimum_outdoor_drybulb_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].heat_pump_defrost_maximum_outdoor_drybulb_temperature, var_heat_pump_defrost_maximum_outdoor_drybulb_temperature)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].heat_pump_defrost_strategy, var_heat_pump_defrost_strategy)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].heat_pump_defrost_control, var_heat_pump_defrost_control)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].heat_pump_defrost_time_period_fraction, var_heat_pump_defrost_time_period_fraction)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].supplemental_heating_or_reheat_coil_type, var_supplemental_heating_or_reheat_coil_type)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].supplemental_heating_or_reheat_coil_availability_schedule_name, var_supplemental_heating_or_reheat_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].supplemental_heating_or_reheat_coil_capacity, var_supplemental_heating_or_reheat_coil_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].supplemental_heating_or_reheat_coil_maximum_outdoor_drybulb_temperature, var_supplemental_heating_or_reheat_coil_maximum_outdoor_drybulb_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].supplemental_gas_heating_or_reheat_coil_efficiency, var_supplemental_gas_heating_or_reheat_coil_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].supplemental_gas_heating_or_reheat_coil_parasitic_electric_load, var_supplemental_gas_heating_or_reheat_coil_parasitic_electric_load)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].maximum_outdoor_air_flow_rate, var_maximum_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].minimum_outdoor_air_flow_rate, var_minimum_outdoor_air_flow_rate)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].minimum_outdoor_air_schedule_name, var_minimum_outdoor_air_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].economizer_type, var_economizer_type)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].economizer_lockout, var_economizer_lockout)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].economizer_maximum_limit_drybulb_temperature, var_economizer_maximum_limit_drybulb_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].economizer_maximum_limit_enthalpy, var_economizer_maximum_limit_enthalpy)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].economizer_maximum_limit_dewpoint_temperature, var_economizer_maximum_limit_dewpoint_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].economizer_minimum_limit_drybulb_temperature, var_economizer_minimum_limit_drybulb_temperature)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].supply_plenum_name, var_supply_plenum_name)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].return_plenum_name, var_return_plenum_name)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].heat_recovery_type, var_heat_recovery_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].sensible_heat_recovery_effectiveness, var_sensible_heat_recovery_effectiveness)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].latent_heat_recovery_effectiveness, var_latent_heat_recovery_effectiveness)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].heat_recovery_heat_exchanger_type, var_heat_recovery_heat_exchanger_type)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].heat_recovery_frost_control_type, var_heat_recovery_frost_control_type)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].dehumidification_control_zone_name, var_dehumidification_control_zone_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].dehumidification_relative_humidity_setpoint, var_dehumidification_relative_humidity_setpoint)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].dehumidification_relative_humidity_setpoint_schedule_name, var_dehumidification_relative_humidity_setpoint_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].humidifier_type, var_humidifier_type)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].humidifier_availability_schedule_name, var_humidifier_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].humidifier_rated_capacity, var_humidifier_rated_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].humidifier_rated_electric_power, var_humidifier_rated_electric_power)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].humidifier_control_zone_name, var_humidifier_control_zone_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].humidifier_relative_humidity_setpoint, var_humidifier_relative_humidity_setpoint)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].humidifier_relative_humidity_setpoint_schedule_name, var_humidifier_relative_humidity_setpoint_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].sizing_option, var_sizing_option)
        self.assertEqual(idf2.hvactemplatesystemunitarysystems[0].return_fan, var_return_fan)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].return_fan_total_efficiency, var_return_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].return_fan_delta_pressure, var_return_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].return_fan_motor_efficiency, var_return_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitarysystems[0].return_fan_motor_in_air_stream_fraction, var_return_fan_motor_in_air_stream_fraction)