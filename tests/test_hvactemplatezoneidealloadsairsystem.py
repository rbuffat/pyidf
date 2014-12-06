import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_templates import HvactemplateZoneIdealLoadsAirSystem
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHvactemplateZoneIdealLoadsAirSystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatezoneidealloadsairsystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateZoneIdealLoadsAirSystem()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_template_thermostat_name = "object-list|Template Thermostat Name"
        obj.template_thermostat_name = var_template_thermostat_name
        # object-list
        var_system_availability_schedule_name = "object-list|System Availability Schedule Name"
        obj.system_availability_schedule_name = var_system_availability_schedule_name
        # real
        var_maximum_heating_supply_air_temperature = 50.0
        obj.maximum_heating_supply_air_temperature = var_maximum_heating_supply_air_temperature
        # real
        var_minimum_cooling_supply_air_temperature = -25.0
        obj.minimum_cooling_supply_air_temperature = var_minimum_cooling_supply_air_temperature
        # real
        var_maximum_heating_supply_air_humidity_ratio = 0.0001
        obj.maximum_heating_supply_air_humidity_ratio = var_maximum_heating_supply_air_humidity_ratio
        # real
        var_minimum_cooling_supply_air_humidity_ratio = 0.0001
        obj.minimum_cooling_supply_air_humidity_ratio = var_minimum_cooling_supply_air_humidity_ratio
        # alpha
        var_heating_limit = "NoLimit"
        obj.heating_limit = var_heating_limit
        # real
        var_maximum_heating_air_flow_rate = 0.0
        obj.maximum_heating_air_flow_rate = var_maximum_heating_air_flow_rate
        # real
        var_maximum_sensible_heating_capacity = 0.0
        obj.maximum_sensible_heating_capacity = var_maximum_sensible_heating_capacity
        # alpha
        var_cooling_limit = "NoLimit"
        obj.cooling_limit = var_cooling_limit
        # real
        var_maximum_cooling_air_flow_rate = 0.0
        obj.maximum_cooling_air_flow_rate = var_maximum_cooling_air_flow_rate
        # real
        var_maximum_total_cooling_capacity = 0.0
        obj.maximum_total_cooling_capacity = var_maximum_total_cooling_capacity
        # object-list
        var_heating_availability_schedule_name = "object-list|Heating Availability Schedule Name"
        obj.heating_availability_schedule_name = var_heating_availability_schedule_name
        # object-list
        var_cooling_availability_schedule_name = "object-list|Cooling Availability Schedule Name"
        obj.cooling_availability_schedule_name = var_cooling_availability_schedule_name
        # alpha
        var_dehumidification_control_type = "ConstantSensibleHeatRatio"
        obj.dehumidification_control_type = var_dehumidification_control_type
        # real
        var_cooling_sensible_heat_ratio = 0.50005
        obj.cooling_sensible_heat_ratio = var_cooling_sensible_heat_ratio
        # real
        var_dehumidification_setpoint = 50.0
        obj.dehumidification_setpoint = var_dehumidification_setpoint
        # alpha
        var_humidification_control_type = "None"
        obj.humidification_control_type = var_humidification_control_type
        # real
        var_humidification_setpoint = 50.0
        obj.humidification_setpoint = var_humidification_setpoint
        # alpha
        var_outdoor_air_method = "None"
        obj.outdoor_air_method = var_outdoor_air_method
        # real
        var_outdoor_air_flow_rate_per_person = 22.22
        obj.outdoor_air_flow_rate_per_person = var_outdoor_air_flow_rate_per_person
        # real
        var_outdoor_air_flow_rate_per_zone_floor_area = 23.23
        obj.outdoor_air_flow_rate_per_zone_floor_area = var_outdoor_air_flow_rate_per_zone_floor_area
        # real
        var_outdoor_air_flow_rate_per_zone = 24.24
        obj.outdoor_air_flow_rate_per_zone = var_outdoor_air_flow_rate_per_zone
        # object-list
        var_design_specification_outdoor_air_object_name = "object-list|Design Specification Outdoor Air Object Name"
        obj.design_specification_outdoor_air_object_name = var_design_specification_outdoor_air_object_name
        # alpha
        var_demand_controlled_ventilation_type = "None"
        obj.demand_controlled_ventilation_type = var_demand_controlled_ventilation_type
        # alpha
        var_outdoor_air_economizer_type = "NoEconomizer"
        obj.outdoor_air_economizer_type = var_outdoor_air_economizer_type
        # alpha
        var_heat_recovery_type = "None"
        obj.heat_recovery_type = var_heat_recovery_type
        # real
        var_sensible_heat_recovery_effectiveness = 0.5
        obj.sensible_heat_recovery_effectiveness = var_sensible_heat_recovery_effectiveness
        # real
        var_latent_heat_recovery_effectiveness = 0.5
        obj.latent_heat_recovery_effectiveness = var_latent_heat_recovery_effectiveness

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].zone_name, var_zone_name)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].template_thermostat_name, var_template_thermostat_name)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].system_availability_schedule_name, var_system_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].maximum_heating_supply_air_temperature, var_maximum_heating_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].minimum_cooling_supply_air_temperature, var_minimum_cooling_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].maximum_heating_supply_air_humidity_ratio, var_maximum_heating_supply_air_humidity_ratio)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].minimum_cooling_supply_air_humidity_ratio, var_minimum_cooling_supply_air_humidity_ratio)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].heating_limit, var_heating_limit)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].maximum_heating_air_flow_rate, var_maximum_heating_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].maximum_sensible_heating_capacity, var_maximum_sensible_heating_capacity)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].cooling_limit, var_cooling_limit)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].maximum_cooling_air_flow_rate, var_maximum_cooling_air_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].maximum_total_cooling_capacity, var_maximum_total_cooling_capacity)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].heating_availability_schedule_name, var_heating_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].cooling_availability_schedule_name, var_cooling_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].cooling_sensible_heat_ratio, var_cooling_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].dehumidification_setpoint, var_dehumidification_setpoint)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].humidification_control_type, var_humidification_control_type)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].humidification_setpoint, var_humidification_setpoint)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].outdoor_air_method, var_outdoor_air_method)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].outdoor_air_flow_rate_per_person, var_outdoor_air_flow_rate_per_person)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].outdoor_air_flow_rate_per_zone_floor_area, var_outdoor_air_flow_rate_per_zone_floor_area)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].outdoor_air_flow_rate_per_zone, var_outdoor_air_flow_rate_per_zone)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].demand_controlled_ventilation_type, var_demand_controlled_ventilation_type)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].outdoor_air_economizer_type, var_outdoor_air_economizer_type)
        self.assertEqual(idf2.hvactemplatezoneidealloadsairsystems[0].heat_recovery_type, var_heat_recovery_type)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].sensible_heat_recovery_effectiveness, var_sensible_heat_recovery_effectiveness)
        self.assertAlmostEqual(idf2.hvactemplatezoneidealloadsairsystems[0].latent_heat_recovery_effectiveness, var_latent_heat_recovery_effectiveness)