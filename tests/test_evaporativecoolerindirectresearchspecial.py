import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.evaporative_coolers import EvaporativeCoolerIndirectResearchSpecial

log = logging.getLogger(__name__)

class TestEvaporativeCoolerIndirectResearchSpecial(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_evaporativecoolerindirectresearchspecial(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EvaporativeCoolerIndirectResearchSpecial()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_cooler_maximum_effectiveness = 1.0
        obj.cooler_maximum_effectiveness = var_cooler_maximum_effectiveness
        # real
        var_cooler_flow_ratio = 4.4
        obj.cooler_flow_ratio = var_cooler_flow_ratio
        # real
        var_recirculating_water_pump_power_consumption = 5.5
        obj.recirculating_water_pump_power_consumption = var_recirculating_water_pump_power_consumption
        # real
        var_secondary_fan_flow_rate = 0.0
        obj.secondary_fan_flow_rate = var_secondary_fan_flow_rate
        # real
        var_secondary_fan_total_efficiency = 0.50005
        obj.secondary_fan_total_efficiency = var_secondary_fan_total_efficiency
        # real
        var_secondary_fan_delta_pressure = 0.0
        obj.secondary_fan_delta_pressure = var_secondary_fan_delta_pressure
        # node
        var_primary_air_inlet_node_name = "node|Primary Air Inlet Node Name"
        obj.primary_air_inlet_node_name = var_primary_air_inlet_node_name
        # node
        var_primary_air_outlet_node_name = "node|Primary Air Outlet Node Name"
        obj.primary_air_outlet_node_name = var_primary_air_outlet_node_name
        # alpha
        var_control_type = "Control Type"
        obj.control_type = var_control_type
        # real
        var_dewpoint_effectiveness_factor = 12.12
        obj.dewpoint_effectiveness_factor = var_dewpoint_effectiveness_factor
        # node
        var_secondary_air_inlet_node_name = "node|Secondary Air Inlet Node Name"
        obj.secondary_air_inlet_node_name = var_secondary_air_inlet_node_name
        # node
        var_sensor_node_name = "node|Sensor Node Name"
        obj.sensor_node_name = var_sensor_node_name
        # node
        var_relief_air_inlet_node_name = "node|Relief Air Inlet Node Name"
        obj.relief_air_inlet_node_name = var_relief_air_inlet_node_name
        # object-list
        var_water_supply_storage_tank_name = "object-list|Water Supply Storage Tank Name"
        obj.water_supply_storage_tank_name = var_water_supply_storage_tank_name
        # real
        var_drift_loss_fraction = 0.0
        obj.drift_loss_fraction = var_drift_loss_fraction
        # real
        var_blowdown_concentration_ratio = 2.0
        obj.blowdown_concentration_ratio = var_blowdown_concentration_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].name, var_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].cooler_maximum_effectiveness, var_cooler_maximum_effectiveness)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].cooler_flow_ratio, var_cooler_flow_ratio)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].recirculating_water_pump_power_consumption, var_recirculating_water_pump_power_consumption)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_fan_flow_rate, var_secondary_fan_flow_rate)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_fan_total_efficiency, var_secondary_fan_total_efficiency)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_fan_delta_pressure, var_secondary_fan_delta_pressure)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].primary_air_inlet_node_name, var_primary_air_inlet_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].primary_air_outlet_node_name, var_primary_air_outlet_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].control_type, var_control_type)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].dewpoint_effectiveness_factor, var_dewpoint_effectiveness_factor)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].secondary_air_inlet_node_name, var_secondary_air_inlet_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].sensor_node_name, var_sensor_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].relief_air_inlet_node_name, var_relief_air_inlet_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectresearchspecials[0].water_supply_storage_tank_name, var_water_supply_storage_tank_name)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].drift_loss_fraction, var_drift_loss_fraction)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectresearchspecials[0].blowdown_concentration_ratio, var_blowdown_concentration_ratio)