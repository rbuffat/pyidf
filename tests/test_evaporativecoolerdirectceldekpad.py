import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.evaporative_coolers import EvaporativeCoolerDirectCelDekPad

log = logging.getLogger(__name__)

class TestEvaporativeCoolerDirectCelDekPad(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_evaporativecoolerdirectceldekpad(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EvaporativeCoolerDirectCelDekPad()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_direct_pad_area = 0.0
        obj.direct_pad_area = var_direct_pad_area
        # real
        var_direct_pad_depth = 0.0
        obj.direct_pad_depth = var_direct_pad_depth
        # real
        var_recirculating_water_pump_power_consumption = 5.5
        obj.recirculating_water_pump_power_consumption = var_recirculating_water_pump_power_consumption
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_control_type = "Control Type"
        obj.control_type = var_control_type
        # object-list
        var_water_supply_storage_tank_name = "object-list|Water Supply Storage Tank Name"
        obj.water_supply_storage_tank_name = var_water_supply_storage_tank_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.evaporativecoolerdirectceldekpads[0].name, var_name)
        self.assertEqual(idf2.evaporativecoolerdirectceldekpads[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.evaporativecoolerdirectceldekpads[0].direct_pad_area, var_direct_pad_area)
        self.assertAlmostEqual(idf2.evaporativecoolerdirectceldekpads[0].direct_pad_depth, var_direct_pad_depth)
        self.assertAlmostEqual(idf2.evaporativecoolerdirectceldekpads[0].recirculating_water_pump_power_consumption, var_recirculating_water_pump_power_consumption)
        self.assertEqual(idf2.evaporativecoolerdirectceldekpads[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.evaporativecoolerdirectceldekpads[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.evaporativecoolerdirectceldekpads[0].control_type, var_control_type)
        self.assertEqual(idf2.evaporativecoolerdirectceldekpads[0].water_supply_storage_tank_name, var_water_supply_storage_tank_name)