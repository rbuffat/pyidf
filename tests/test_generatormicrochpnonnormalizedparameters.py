import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import GeneratorMicroChpNonNormalizedParameters

log = logging.getLogger(__name__)

class TestGeneratorMicroChpNonNormalizedParameters(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatormicrochpnonnormalizedparameters(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorMicroChpNonNormalizedParameters()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_maximum_electric_power = 2.2
        obj.maximum_electric_power = var_maximum_electric_power
        # real
        var_minimum_electric_power = 3.3
        obj.minimum_electric_power = var_minimum_electric_power
        # real
        var_minimum_cooling_water_flow_rate = 4.4
        obj.minimum_cooling_water_flow_rate = var_minimum_cooling_water_flow_rate
        # real
        var_maximum_cooling_water_temperature = 5.5
        obj.maximum_cooling_water_temperature = var_maximum_cooling_water_temperature
        # object-list
        var_electrical_efficiency_curve_name = "object-list|Electrical Efficiency Curve Name"
        obj.electrical_efficiency_curve_name = var_electrical_efficiency_curve_name
        # object-list
        var_thermal_efficiency_curve_name = "object-list|Thermal Efficiency Curve Name"
        obj.thermal_efficiency_curve_name = var_thermal_efficiency_curve_name
        # alpha
        var_cooling_water_flow_rate_mode = "PlantControl"
        obj.cooling_water_flow_rate_mode = var_cooling_water_flow_rate_mode
        # object-list
        var_cooling_water_flow_rate_curve_name = "object-list|Cooling Water Flow Rate Curve Name"
        obj.cooling_water_flow_rate_curve_name = var_cooling_water_flow_rate_curve_name
        # object-list
        var_air_flow_rate_curve_name = "object-list|Air Flow Rate Curve Name"
        obj.air_flow_rate_curve_name = var_air_flow_rate_curve_name
        # real
        var_maximum_net_electrical_power_rate_of_change = 11.11
        obj.maximum_net_electrical_power_rate_of_change = var_maximum_net_electrical_power_rate_of_change
        # real
        var_maximum_fuel_flow_rate_of_change = 12.12
        obj.maximum_fuel_flow_rate_of_change = var_maximum_fuel_flow_rate_of_change
        # real
        var_heat_exchanger_ufactor_times_area_value = 13.13
        obj.heat_exchanger_ufactor_times_area_value = var_heat_exchanger_ufactor_times_area_value
        # real
        var_skin_loss_ufactor_times_area_value = 14.14
        obj.skin_loss_ufactor_times_area_value = var_skin_loss_ufactor_times_area_value
        # real
        var_skin_loss_radiative_fraction = 15.15
        obj.skin_loss_radiative_fraction = var_skin_loss_radiative_fraction
        # real
        var_aggregated_thermal_mass_of_energy_conversion_portion_of_generator = 0.0001
        obj.aggregated_thermal_mass_of_energy_conversion_portion_of_generator = var_aggregated_thermal_mass_of_energy_conversion_portion_of_generator
        # real
        var_aggregated_thermal_mass_of_heat_recovery_portion_of_generator = 0.0001
        obj.aggregated_thermal_mass_of_heat_recovery_portion_of_generator = var_aggregated_thermal_mass_of_heat_recovery_portion_of_generator
        # real
        var_standby_power = 18.18
        obj.standby_power = var_standby_power
        # alpha
        var_warm_up_mode = "NominalEngineTemperature"
        obj.warm_up_mode = var_warm_up_mode
        # real
        var_warm_up_fuel_flow_rate_coefficient = 20.2
        obj.warm_up_fuel_flow_rate_coefficient = var_warm_up_fuel_flow_rate_coefficient
        # real
        var_nominal_engine_operating_temperature = 21.21
        obj.nominal_engine_operating_temperature = var_nominal_engine_operating_temperature
        # real
        var_warm_up_power_coefficient = 22.22
        obj.warm_up_power_coefficient = var_warm_up_power_coefficient
        # real
        var_warm_up_fuel_flow_rate_limit_ratio = 23.23
        obj.warm_up_fuel_flow_rate_limit_ratio = var_warm_up_fuel_flow_rate_limit_ratio
        # real
        var_warm_up_delay_time = 24.24
        obj.warm_up_delay_time = var_warm_up_delay_time
        # real
        var_cool_down_power = 25.25
        obj.cool_down_power = var_cool_down_power
        # real
        var_cool_down_delay_time = 26.26
        obj.cool_down_delay_time = var_cool_down_delay_time
        # alpha
        var_restart_mode = "MandatoryCoolDown"
        obj.restart_mode = var_restart_mode

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatormicrochpnonnormalizedparameterss[0].name, var_name)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].maximum_electric_power, var_maximum_electric_power)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].minimum_electric_power, var_minimum_electric_power)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].minimum_cooling_water_flow_rate, var_minimum_cooling_water_flow_rate)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].maximum_cooling_water_temperature, var_maximum_cooling_water_temperature)
        self.assertEqual(idf2.generatormicrochpnonnormalizedparameterss[0].electrical_efficiency_curve_name, var_electrical_efficiency_curve_name)
        self.assertEqual(idf2.generatormicrochpnonnormalizedparameterss[0].thermal_efficiency_curve_name, var_thermal_efficiency_curve_name)
        self.assertEqual(idf2.generatormicrochpnonnormalizedparameterss[0].cooling_water_flow_rate_mode, var_cooling_water_flow_rate_mode)
        self.assertEqual(idf2.generatormicrochpnonnormalizedparameterss[0].cooling_water_flow_rate_curve_name, var_cooling_water_flow_rate_curve_name)
        self.assertEqual(idf2.generatormicrochpnonnormalizedparameterss[0].air_flow_rate_curve_name, var_air_flow_rate_curve_name)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].maximum_net_electrical_power_rate_of_change, var_maximum_net_electrical_power_rate_of_change)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].maximum_fuel_flow_rate_of_change, var_maximum_fuel_flow_rate_of_change)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].heat_exchanger_ufactor_times_area_value, var_heat_exchanger_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].skin_loss_ufactor_times_area_value, var_skin_loss_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].skin_loss_radiative_fraction, var_skin_loss_radiative_fraction)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].aggregated_thermal_mass_of_energy_conversion_portion_of_generator, var_aggregated_thermal_mass_of_energy_conversion_portion_of_generator)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].aggregated_thermal_mass_of_heat_recovery_portion_of_generator, var_aggregated_thermal_mass_of_heat_recovery_portion_of_generator)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].standby_power, var_standby_power)
        self.assertEqual(idf2.generatormicrochpnonnormalizedparameterss[0].warm_up_mode, var_warm_up_mode)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].warm_up_fuel_flow_rate_coefficient, var_warm_up_fuel_flow_rate_coefficient)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].nominal_engine_operating_temperature, var_nominal_engine_operating_temperature)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].warm_up_power_coefficient, var_warm_up_power_coefficient)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].warm_up_fuel_flow_rate_limit_ratio, var_warm_up_fuel_flow_rate_limit_ratio)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].warm_up_delay_time, var_warm_up_delay_time)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].cool_down_power, var_cool_down_power)
        self.assertAlmostEqual(idf2.generatormicrochpnonnormalizedparameterss[0].cool_down_delay_time, var_cool_down_delay_time)
        self.assertEqual(idf2.generatormicrochpnonnormalizedparameterss[0].restart_mode, var_restart_mode)