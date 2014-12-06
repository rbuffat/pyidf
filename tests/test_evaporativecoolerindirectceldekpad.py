import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.evaporative_coolers import EvaporativeCoolerIndirectCelDekPad

log = logging.getLogger(__name__)

class TestEvaporativeCoolerIndirectCelDekPad(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_evaporativecoolerindirectceldekpad(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EvaporativeCoolerIndirectCelDekPad()
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
        # real
        var_secondary_fan_flow_rate = 0.0
        obj.secondary_fan_flow_rate = var_secondary_fan_flow_rate
        # real
        var_secondary_fan_total_efficiency = 0.50005
        obj.secondary_fan_total_efficiency = var_secondary_fan_total_efficiency
        # real
        var_secondary_fan_delta_pressure = 0.0
        obj.secondary_fan_delta_pressure = var_secondary_fan_delta_pressure
        # real
        var_indirect_heat_exchanger_effectiveness = 0.0
        obj.indirect_heat_exchanger_effectiveness = var_indirect_heat_exchanger_effectiveness
        # node
        var_primary_air_inlet_node_name = "node|Primary Air Inlet Node Name"
        obj.primary_air_inlet_node_name = var_primary_air_inlet_node_name
        # node
        var_primary_air_outlet_node_name = "node|Primary Air Outlet Node Name"
        obj.primary_air_outlet_node_name = var_primary_air_outlet_node_name
        # alpha
        var_control_type = "Control Type"
        obj.control_type = var_control_type
        # object-list
        var_water_supply_storage_tank_name = "object-list|Water Supply Storage Tank Name"
        obj.water_supply_storage_tank_name = var_water_supply_storage_tank_name
        # node
        var_secondary_air_inlet_node_name = "node|Secondary Air Inlet Node Name"
        obj.secondary_air_inlet_node_name = var_secondary_air_inlet_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.evaporativecoolerindirectceldekpads[0].name, var_name)
        self.assertEqual(idf2.evaporativecoolerindirectceldekpads[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectceldekpads[0].direct_pad_area, var_direct_pad_area)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectceldekpads[0].direct_pad_depth, var_direct_pad_depth)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectceldekpads[0].recirculating_water_pump_power_consumption, var_recirculating_water_pump_power_consumption)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectceldekpads[0].secondary_fan_flow_rate, var_secondary_fan_flow_rate)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectceldekpads[0].secondary_fan_total_efficiency, var_secondary_fan_total_efficiency)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectceldekpads[0].secondary_fan_delta_pressure, var_secondary_fan_delta_pressure)
        self.assertAlmostEqual(idf2.evaporativecoolerindirectceldekpads[0].indirect_heat_exchanger_effectiveness, var_indirect_heat_exchanger_effectiveness)
        self.assertEqual(idf2.evaporativecoolerindirectceldekpads[0].primary_air_inlet_node_name, var_primary_air_inlet_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectceldekpads[0].primary_air_outlet_node_name, var_primary_air_outlet_node_name)
        self.assertEqual(idf2.evaporativecoolerindirectceldekpads[0].control_type, var_control_type)
        self.assertEqual(idf2.evaporativecoolerindirectceldekpads[0].water_supply_storage_tank_name, var_water_supply_storage_tank_name)
        self.assertEqual(idf2.evaporativecoolerindirectceldekpads[0].secondary_air_inlet_node_name, var_secondary_air_inlet_node_name)