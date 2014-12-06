import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.evaporative_coolers import EvaporativeCoolerDirectResearchSpecial

log = logging.getLogger(__name__)

class TestEvaporativeCoolerDirectResearchSpecial(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_evaporativecoolerdirectresearchspecial(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EvaporativeCoolerDirectResearchSpecial()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_cooler_effectiveness = 0.5
        obj.cooler_effectiveness = var_cooler_effectiveness
        # real
        var_recirculating_water_pump_power_consumption = 0.0
        obj.recirculating_water_pump_power_consumption = var_recirculating_water_pump_power_consumption
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # node
        var_sensor_node_name = "node|Sensor Node Name"
        obj.sensor_node_name = var_sensor_node_name
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
        self.assertEqual(idf2.evaporativecoolerdirectresearchspecials[0].name, var_name)
        self.assertEqual(idf2.evaporativecoolerdirectresearchspecials[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.evaporativecoolerdirectresearchspecials[0].cooler_effectiveness, var_cooler_effectiveness)
        self.assertAlmostEqual(idf2.evaporativecoolerdirectresearchspecials[0].recirculating_water_pump_power_consumption, var_recirculating_water_pump_power_consumption)
        self.assertEqual(idf2.evaporativecoolerdirectresearchspecials[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.evaporativecoolerdirectresearchspecials[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.evaporativecoolerdirectresearchspecials[0].sensor_node_name, var_sensor_node_name)
        self.assertEqual(idf2.evaporativecoolerdirectresearchspecials[0].water_supply_storage_tank_name, var_water_supply_storage_tank_name)
        self.assertAlmostEqual(idf2.evaporativecoolerdirectresearchspecials[0].drift_loss_fraction, var_drift_loss_fraction)
        self.assertAlmostEqual(idf2.evaporativecoolerdirectresearchspecials[0].blowdown_concentration_ratio, var_blowdown_concentration_ratio)