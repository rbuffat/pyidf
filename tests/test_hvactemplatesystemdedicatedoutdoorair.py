import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplateSystemDedicatedOutdoorAir

log = logging.getLogger(__name__)

class TestHvactemplateSystemDedicatedOutdoorAir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatesystemdedicatedoutdoorair(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateSystemDedicatedOutdoorAir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_system_availability_schedule_name = "object-list|System Availability Schedule Name"
        obj.system_availability_schedule_name = var_system_availability_schedule_name
        # alpha
        var_air_outlet_type = "DirectIntoZone"
        obj.air_outlet_type = var_air_outlet_type
        # real
        var_supply_fan_flow_rate = 0.0001
        obj.supply_fan_flow_rate = var_supply_fan_flow_rate
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
        var_supply_fan_placement = "DrawThrough"
        obj.supply_fan_placement = var_supply_fan_placement
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
        var_cooling_coil_design_setpoint = 13.13
        obj.cooling_coil_design_setpoint = var_cooling_coil_design_setpoint
        # object-list
        var_cooling_coil_setpoint_schedule_name = "object-list|Cooling Coil Setpoint Schedule Name"
        obj.cooling_coil_setpoint_schedule_name = var_cooling_coil_setpoint_schedule_name
        # real
        var_cooling_coil_setpoint_at_outdoor_drybulb_low = 15.15
        obj.cooling_coil_setpoint_at_outdoor_drybulb_low = var_cooling_coil_setpoint_at_outdoor_drybulb_low
        # real
        var_cooling_coil_reset_outdoor_drybulb_low = 16.16
        obj.cooling_coil_reset_outdoor_drybulb_low = var_cooling_coil_reset_outdoor_drybulb_low
        # real
        var_cooling_coil_setpoint_at_outdoor_drybulb_high = 17.17
        obj.cooling_coil_setpoint_at_outdoor_drybulb_high = var_cooling_coil_setpoint_at_outdoor_drybulb_high
        # real
        var_cooling_coil_reset_outdoor_drybulb_high = 18.18
        obj.cooling_coil_reset_outdoor_drybulb_high = var_cooling_coil_reset_outdoor_drybulb_high
        # real
        var_dx_cooling_coil_gross_rated_total_capacity = 19.19
        obj.dx_cooling_coil_gross_rated_total_capacity = var_dx_cooling_coil_gross_rated_total_capacity
        # real
        var_dx_cooling_coil_gross_rated_sensible_heat_ratio = 0.75
        obj.dx_cooling_coil_gross_rated_sensible_heat_ratio = var_dx_cooling_coil_gross_rated_sensible_heat_ratio
        # real
        var_dx_cooling_coil_gross_rated_cop = 0.0001
        obj.dx_cooling_coil_gross_rated_cop = var_dx_cooling_coil_gross_rated_cop
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
        var_heating_coil_design_setpoint = 25.25
        obj.heating_coil_design_setpoint = var_heating_coil_design_setpoint
        # object-list
        var_heating_coil_setpoint_schedule_name = "object-list|Heating Coil Setpoint Schedule Name"
        obj.heating_coil_setpoint_schedule_name = var_heating_coil_setpoint_schedule_name
        # real
        var_heating_coil_setpoint_at_outdoor_drybulb_low = 27.27
        obj.heating_coil_setpoint_at_outdoor_drybulb_low = var_heating_coil_setpoint_at_outdoor_drybulb_low
        # real
        var_heating_coil_reset_outdoor_drybulb_low = 28.28
        obj.heating_coil_reset_outdoor_drybulb_low = var_heating_coil_reset_outdoor_drybulb_low
        # real
        var_heating_coil_setpoint_at_outdoor_drybulb_high = 29.29
        obj.heating_coil_setpoint_at_outdoor_drybulb_high = var_heating_coil_setpoint_at_outdoor_drybulb_high
        # real
        var_heating_coil_reset_outdoor_drybulb_high = 30.3
        obj.heating_coil_reset_outdoor_drybulb_high = var_heating_coil_reset_outdoor_drybulb_high
        # real
        var_gas_heating_coil_efficiency = 0.5
        obj.gas_heating_coil_efficiency = var_gas_heating_coil_efficiency
        # real
        var_gas_heating_coil_parasitic_electric_load = 0.0
        obj.gas_heating_coil_parasitic_electric_load = var_gas_heating_coil_parasitic_electric_load
        # alpha
        var_heat_recovery_type = "None"
        obj.heat_recovery_type = var_heat_recovery_type
        # real
        var_heat_recovery_sensible_effectiveness = 0.5
        obj.heat_recovery_sensible_effectiveness = var_heat_recovery_sensible_effectiveness
        # real
        var_heat_recovery_latent_effectiveness = 0.5
        obj.heat_recovery_latent_effectiveness = var_heat_recovery_latent_effectiveness
        # alpha
        var_heat_recovery_heat_exchanger_type = "Plate"
        obj.heat_recovery_heat_exchanger_type = var_heat_recovery_heat_exchanger_type
        # alpha
        var_heat_recovery_frost_control_type = "None"
        obj.heat_recovery_frost_control_type = var_heat_recovery_frost_control_type
        # alpha
        var_dehumidification_control_type = "None"
        obj.dehumidification_control_type = var_dehumidification_control_type
        # real
        var_dehumidification_setpoint = 0.5
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
        # real
        var_humidifier_constant_setpoint = 0.5
        obj.humidifier_constant_setpoint = var_humidifier_constant_setpoint
        # object-list
        var_dehumidification_setpoint_schedule_name = "object-list|Dehumidification Setpoint Schedule Name"
        obj.dehumidification_setpoint_schedule_name = var_dehumidification_setpoint_schedule_name
        # object-list
        var_humidifier_setpoint_schedule_name = "object-list|Humidifier Setpoint Schedule Name"
        obj.humidifier_setpoint_schedule_name = var_humidifier_setpoint_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].name, var_name)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].air_outlet_type, var_air_outlet_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].supply_fan_flow_rate, var_supply_fan_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].supply_fan_total_efficiency, var_supply_fan_total_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].supply_fan_delta_pressure, var_supply_fan_delta_pressure)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].supply_fan_motor_efficiency, var_supply_fan_motor_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].supply_fan_motor_in_air_stream_fraction, var_supply_fan_motor_in_air_stream_fraction)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].supply_fan_placement, var_supply_fan_placement)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].cooling_coil_type, var_cooling_coil_type)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].cooling_coil_availability_schedule_name, var_cooling_coil_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].cooling_coil_setpoint_control_type, var_cooling_coil_setpoint_control_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].cooling_coil_design_setpoint, var_cooling_coil_design_setpoint)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].cooling_coil_setpoint_schedule_name, var_cooling_coil_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].cooling_coil_setpoint_at_outdoor_drybulb_low, var_cooling_coil_setpoint_at_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].cooling_coil_reset_outdoor_drybulb_low, var_cooling_coil_reset_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].cooling_coil_setpoint_at_outdoor_drybulb_high, var_cooling_coil_setpoint_at_outdoor_drybulb_high)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].cooling_coil_reset_outdoor_drybulb_high, var_cooling_coil_reset_outdoor_drybulb_high)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].dx_cooling_coil_gross_rated_total_capacity, var_dx_cooling_coil_gross_rated_total_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].dx_cooling_coil_gross_rated_sensible_heat_ratio, var_dx_cooling_coil_gross_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].dx_cooling_coil_gross_rated_cop, var_dx_cooling_coil_gross_rated_cop)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heating_coil_type, var_heating_coil_type)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heating_coil_availability_schedule_name, var_heating_coil_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heating_coil_setpoint_control_type, var_heating_coil_setpoint_control_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heating_coil_design_setpoint, var_heating_coil_design_setpoint)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heating_coil_setpoint_schedule_name, var_heating_coil_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heating_coil_setpoint_at_outdoor_drybulb_low, var_heating_coil_setpoint_at_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heating_coil_reset_outdoor_drybulb_low, var_heating_coil_reset_outdoor_drybulb_low)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heating_coil_setpoint_at_outdoor_drybulb_high, var_heating_coil_setpoint_at_outdoor_drybulb_high)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heating_coil_reset_outdoor_drybulb_high, var_heating_coil_reset_outdoor_drybulb_high)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].gas_heating_coil_efficiency, var_gas_heating_coil_efficiency)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].gas_heating_coil_parasitic_electric_load, var_gas_heating_coil_parasitic_electric_load)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heat_recovery_type, var_heat_recovery_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heat_recovery_sensible_effectiveness, var_heat_recovery_sensible_effectiveness)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heat_recovery_latent_effectiveness, var_heat_recovery_latent_effectiveness)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heat_recovery_heat_exchanger_type, var_heat_recovery_heat_exchanger_type)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].heat_recovery_frost_control_type, var_heat_recovery_frost_control_type)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].dehumidification_setpoint, var_dehumidification_setpoint)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].humidifier_type, var_humidifier_type)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].humidifier_availability_schedule_name, var_humidifier_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].humidifier_rated_capacity, var_humidifier_rated_capacity)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].humidifier_rated_electric_power, var_humidifier_rated_electric_power)
        self.assertAlmostEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].humidifier_constant_setpoint, var_humidifier_constant_setpoint)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].dehumidification_setpoint_schedule_name, var_dehumidification_setpoint_schedule_name)
        self.assertEqual(idf2.hvactemplatesystemdedicatedoutdoorairs[0].humidifier_setpoint_schedule_name, var_humidifier_setpoint_schedule_name)