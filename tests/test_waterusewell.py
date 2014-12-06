import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_systems import WaterUseWell

log = logging.getLogger(__name__)

class TestWaterUseWell(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_waterusewell(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WaterUseWell()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_storage_tank_name = "object-list|Storage Tank Name"
        obj.storage_tank_name = var_storage_tank_name
        # real
        var_pump_depth = 3.3
        obj.pump_depth = var_pump_depth
        # real
        var_pump_rated_flow_rate = 4.4
        obj.pump_rated_flow_rate = var_pump_rated_flow_rate
        # real
        var_pump_rated_head = 5.5
        obj.pump_rated_head = var_pump_rated_head
        # real
        var_pump_rated_power_consumption = 6.6
        obj.pump_rated_power_consumption = var_pump_rated_power_consumption
        # real
        var_pump_efficiency = 7.7
        obj.pump_efficiency = var_pump_efficiency
        # real
        var_well_recovery_rate = 8.8
        obj.well_recovery_rate = var_well_recovery_rate
        # real
        var_nominal_well_storage_volume = 9.9
        obj.nominal_well_storage_volume = var_nominal_well_storage_volume
        # alpha
        var_water_table_depth_mode = "Constant"
        obj.water_table_depth_mode = var_water_table_depth_mode
        # real
        var_water_table_depth = 11.11
        obj.water_table_depth = var_water_table_depth
        # object-list
        var_water_table_depth_schedule_name = "object-list|Water Table Depth Schedule Name"
        obj.water_table_depth_schedule_name = var_water_table_depth_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.waterusewells[0].name, var_name)
        self.assertEqual(idf2.waterusewells[0].storage_tank_name, var_storage_tank_name)
        self.assertAlmostEqual(idf2.waterusewells[0].pump_depth, var_pump_depth)
        self.assertAlmostEqual(idf2.waterusewells[0].pump_rated_flow_rate, var_pump_rated_flow_rate)
        self.assertAlmostEqual(idf2.waterusewells[0].pump_rated_head, var_pump_rated_head)
        self.assertAlmostEqual(idf2.waterusewells[0].pump_rated_power_consumption, var_pump_rated_power_consumption)
        self.assertAlmostEqual(idf2.waterusewells[0].pump_efficiency, var_pump_efficiency)
        self.assertAlmostEqual(idf2.waterusewells[0].well_recovery_rate, var_well_recovery_rate)
        self.assertAlmostEqual(idf2.waterusewells[0].nominal_well_storage_volume, var_nominal_well_storage_volume)
        self.assertEqual(idf2.waterusewells[0].water_table_depth_mode, var_water_table_depth_mode)
        self.assertAlmostEqual(idf2.waterusewells[0].water_table_depth, var_water_table_depth)
        self.assertEqual(idf2.waterusewells[0].water_table_depth_schedule_name, var_water_table_depth_schedule_name)