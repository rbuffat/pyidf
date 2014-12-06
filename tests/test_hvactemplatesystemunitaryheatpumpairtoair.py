import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplateSystemUnitaryHeatPumpAirToAir

log = logging.getLogger(__name__)

class TestHvactemplateSystemUnitaryHeatPumpAirToAir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatesystemunitaryheatpumpairtoair(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateSystemUnitaryHeatPumpAirToAir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_system_availability_schedule_name = "object-list|System Availability Schedule Name"
        obj.system_availability_schedule_name = var_system_availability_schedule_name
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
        # object-list
        var_cooling_coil_availability_schedule_name = "object-list|Cooling Coil Availability Schedule Name"
        obj.cooling_coil_availability_schedule_name = var_cooling_coil_availability_schedule_name
        # real
        var_cooling_design_supply_air_temperature = 15.15
        obj.cooling_design_supply_air_temperature = var_cooling_design_supply_air_temperature
        # real
        var_cooling_coil_gross_rated_total_capacity = 16.16
        obj.cooling_coil_gross_rated_total_capacity = var_cooling_coil_gross_rated_total_capacity
        # real
        var_cooling_coil_gross_rated_sensible_heat_ratio = 0.75
        obj.cooling_coil_gross_rated_sensible_heat_ratio = var_cooling_coil_gross_rated_sensible_heat_ratio
        # real
        var_cooling_coil_gross_rated_cop = 0.0001
        obj.cooling_coil_gross_rated_cop = var_cooling_coil_gross_rated_cop
        # alpha
        var_heat_pump_heating_coil_type = "SingleSpeedDXHeatPump"
        obj.heat_pump_heating_coil_type = var_heat_pump_heating_coil_type
        # object-list
        var_heat_pump_heating_coil_availability_schedule_name = "object-list|Heat Pump Heating Coil Availability Schedule Name"
        obj.heat_pump_heating_coil_availability_schedule_name = var_heat_pump_heating_coil_availability_schedule_name
        # real
        var_heating_design_supply_air_temperature = 21.21
        obj.heating_design_supply_air_temperature = var_heating_design_supply_air_temperature
        # real
        var_heat_pump_heating_coil_gross_rated_capacity = 0.0001
        obj.heat_pump_heating_coil_gross_rated_capacity = var_heat_pump_heating_coil_gross_rated_capacity
        # real
        var_heat_pump_heating_coil_rated_cop = 0.0001
        obj.heat_pump_heating_coil_rated_cop = var_heat_pump_heating_coil_rated_cop
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
        var_supplemental_heating_coil_type = "Electric"
        obj.supplemental_heating_coil_type = var_supplemental_heating_coil_type
        # object-list
        var_supplemental_heating_coil_availability_schedule_name = "object-list|Supplemental Heating Coil Availability Schedule Name"
        obj.supplemental_heating_coil_availability_schedule_name = var_supplemental_heating_coil_availability_schedule_name
        # real
        var_supplemental_heating_coil_capacity = 31.31
        obj.supplemental_heating_coil_capacity = var_supplemental_heating_coil_capacity
        # real
        var_supplemental_heating_coil_maximum_outdoor_drybulb_temperature = 21.0
        obj.supplemental_heating_coil_maximum_outdoor_drybulb_temperature = var_supplemental_heating_coil_maximum_outdoor_drybulb_temperature
        # real
        var_supplemental_gas_heating_coil_efficiency = 0.5
        obj.supplemental_gas_heating_coil_efficiency = var_supplemental_gas_heating_coil_efficiency
        # real
        var_supplemental_gas_heating_coil_parasitic_electric_load = 0.0
        obj.supplemental_gas_heating_coil_parasitic_electric_load = var_supplemental_gas_heating_coil_parasitic_electric_load
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
        var_economizer_maximum_limit_drybulb_temperature = 40.4
        obj.economizer_maximum_limit_drybulb_temperature = var_economizer_maximum_limit_drybulb_temperature
        # real
        var_economizer_maximum_limit_enthalpy = 41.41
        obj.economizer_maximum_limit_enthalpy = var_economizer_maximum_limit_enthalpy
        # real
        var_economizer_maximum_limit_dewpoint_temperature = 42.42
        obj.economizer_maximum_limit_dewpoint_temperature = var_economizer_maximum_limit_dewpoint_temperature
        # real
        var_economizer_minimum_limit_drybulb_temperature = 43.43
        obj.economizer_minimum_limit_drybulb_temperature = var_economizer_minimum_limit_drybulb_temperature
        # object-list
        var_supply_plenum_name = "object-list|Supply Plenum Name"
        obj.supply_plenum_name = var_supply_plenum_name
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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].name, var_name)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].control_zone_or_thermostat_location_name, var_control_zone_or_thermostat_location_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].cooling_supply_air_flow_rate, var_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heating_supply_air_flow_rate, var_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].no_load_supply_air_flow_rate, var_no_load_supply_air_flow_rate)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supply_fan_operating_mode_schedule_name, var_supply_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supply_fan_placement, var_supply_fan_placement)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supply_fan_total_efficiency, var_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supply_fan_delta_pressure, var_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supply_fan_motor_efficiency, var_supply_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supply_fan_motor_in_air_stream_fraction, var_supply_fan_motor_in_air_stream_fraction)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].cooling_coil_type, var_cooling_coil_type)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].cooling_coil_availability_schedule_name, var_cooling_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].cooling_design_supply_air_temperature, var_cooling_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].cooling_coil_gross_rated_total_capacity, var_cooling_coil_gross_rated_total_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].cooling_coil_gross_rated_sensible_heat_ratio, var_cooling_coil_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].cooling_coil_gross_rated_cop, var_cooling_coil_gross_rated_cop)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heat_pump_heating_coil_type, var_heat_pump_heating_coil_type)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heat_pump_heating_coil_availability_schedule_name, var_heat_pump_heating_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heating_design_supply_air_temperature, var_heating_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heat_pump_heating_coil_gross_rated_capacity, var_heat_pump_heating_coil_gross_rated_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heat_pump_heating_coil_rated_cop, var_heat_pump_heating_coil_rated_cop)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heat_pump_heating_minimum_outdoor_drybulb_temperature, var_heat_pump_heating_minimum_outdoor_drybulb_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heat_pump_defrost_maximum_outdoor_drybulb_temperature, var_heat_pump_defrost_maximum_outdoor_drybulb_temperature)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heat_pump_defrost_strategy, var_heat_pump_defrost_strategy)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heat_pump_defrost_control, var_heat_pump_defrost_control)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heat_pump_defrost_time_period_fraction, var_heat_pump_defrost_time_period_fraction)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supplemental_heating_coil_type, var_supplemental_heating_coil_type)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supplemental_heating_coil_availability_schedule_name, var_supplemental_heating_coil_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supplemental_heating_coil_capacity, var_supplemental_heating_coil_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supplemental_heating_coil_maximum_outdoor_drybulb_temperature, var_supplemental_heating_coil_maximum_outdoor_drybulb_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supplemental_gas_heating_coil_efficiency, var_supplemental_gas_heating_coil_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supplemental_gas_heating_coil_parasitic_electric_load, var_supplemental_gas_heating_coil_parasitic_electric_load)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].maximum_outdoor_air_flow_rate, var_maximum_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].minimum_outdoor_air_flow_rate, var_minimum_outdoor_air_flow_rate)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].minimum_outdoor_air_schedule_name, var_minimum_outdoor_air_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].economizer_type, var_economizer_type)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].economizer_lockout, var_economizer_lockout)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].economizer_maximum_limit_drybulb_temperature, var_economizer_maximum_limit_drybulb_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].economizer_maximum_limit_enthalpy, var_economizer_maximum_limit_enthalpy)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].economizer_maximum_limit_dewpoint_temperature, var_economizer_maximum_limit_dewpoint_temperature)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].economizer_minimum_limit_drybulb_temperature, var_economizer_minimum_limit_drybulb_temperature)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].supply_plenum_name, var_supply_plenum_name)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].return_plenum_name, var_return_plenum_name)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].night_cycle_control, var_night_cycle_control)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].night_cycle_control_zone_name, var_night_cycle_control_zone_name)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].heat_recovery_type, var_heat_recovery_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].sensible_heat_recovery_effectiveness, var_sensible_heat_recovery_effectiveness)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].latent_heat_recovery_effectiveness, var_latent_heat_recovery_effectiveness)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].humidifier_type, var_humidifier_type)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].humidifier_availability_schedule_name, var_humidifier_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].humidifier_rated_capacity, var_humidifier_rated_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].humidifier_rated_electric_power, var_humidifier_rated_electric_power)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].humidifier_control_zone_name, var_humidifier_control_zone_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].humidifier_setpoint, var_humidifier_setpoint)
        self.assertEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].return_fan, var_return_fan)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].return_fan_total_efficiency, var_return_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].return_fan_delta_pressure, var_return_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].return_fan_motor_efficiency, var_return_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemunitaryheatpumpairtoairs[0].return_fan_motor_in_air_stream_fraction, var_return_fan_motor_in_air_stream_fraction)