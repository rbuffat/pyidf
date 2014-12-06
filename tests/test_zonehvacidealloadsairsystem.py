import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_forced_air_units import ZoneHvacIdealLoadsAirSystem

log = logging.getLogger(__name__)

class TestZoneHvacIdealLoadsAirSystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacidealloadsairsystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacIdealLoadsAirSystem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_zone_supply_air_node_name = "node|Zone Supply Air Node Name"
        obj.zone_supply_air_node_name = var_zone_supply_air_node_name
        # node
        var_zone_exhaust_air_node_name = "node|Zone Exhaust Air Node Name"
        obj.zone_exhaust_air_node_name = var_zone_exhaust_air_node_name
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
        # alpha
        var_humidification_control_type = "None"
        obj.humidification_control_type = var_humidification_control_type
        # object-list
        var_design_specification_outdoor_air_object_name = "object-list|Design Specification Outdoor Air Object Name"
        obj.design_specification_outdoor_air_object_name = var_design_specification_outdoor_air_object_name
        # node
        var_outdoor_air_inlet_node_name = "node|Outdoor Air Inlet Node Name"
        obj.outdoor_air_inlet_node_name = var_outdoor_air_inlet_node_name
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
        # object-list
        var_design_specification_zonehvac_sizing_object_name = "object-list|Design Specification ZoneHVAC Sizing Object Name"
        obj.design_specification_zonehvac_sizing_object_name = var_design_specification_zonehvac_sizing_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].name, var_name)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].zone_supply_air_node_name, var_zone_supply_air_node_name)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].zone_exhaust_air_node_name, var_zone_exhaust_air_node_name)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].maximum_heating_supply_air_temperature, var_maximum_heating_supply_air_temperature)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].minimum_cooling_supply_air_temperature, var_minimum_cooling_supply_air_temperature)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].maximum_heating_supply_air_humidity_ratio, var_maximum_heating_supply_air_humidity_ratio)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].minimum_cooling_supply_air_humidity_ratio, var_minimum_cooling_supply_air_humidity_ratio)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].heating_limit, var_heating_limit)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].maximum_heating_air_flow_rate, var_maximum_heating_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].maximum_sensible_heating_capacity, var_maximum_sensible_heating_capacity)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].cooling_limit, var_cooling_limit)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].maximum_cooling_air_flow_rate, var_maximum_cooling_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].maximum_total_cooling_capacity, var_maximum_total_cooling_capacity)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].heating_availability_schedule_name, var_heating_availability_schedule_name)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].cooling_availability_schedule_name, var_cooling_availability_schedule_name)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].cooling_sensible_heat_ratio, var_cooling_sensible_heat_ratio)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].humidification_control_type, var_humidification_control_type)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].outdoor_air_inlet_node_name, var_outdoor_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].demand_controlled_ventilation_type, var_demand_controlled_ventilation_type)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].outdoor_air_economizer_type, var_outdoor_air_economizer_type)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].heat_recovery_type, var_heat_recovery_type)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].sensible_heat_recovery_effectiveness, var_sensible_heat_recovery_effectiveness)
        self.assertAlmostEqual(idf2.zonehvacidealloadsairsystems[0].latent_heat_recovery_effectiveness, var_latent_heat_recovery_effectiveness)
        self.assertEqual(idf2.zonehvacidealloadsairsystems[0].design_specification_zonehvac_sizing_object_name, var_design_specification_zonehvac_sizing_object_name)