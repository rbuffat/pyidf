import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.heat_recovery import HeatExchangerAirToAirFlatPlate

log = logging.getLogger(__name__)

class TestHeatExchangerAirToAirFlatPlate(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_heatexchangerairtoairflatplate(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HeatExchangerAirToAirFlatPlate()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_flow_arrangement_type = "CounterFlow"
        obj.flow_arrangement_type = var_flow_arrangement_type
        # alpha
        var_economizer_lockout = "Yes"
        obj.economizer_lockout = var_economizer_lockout
        # real
        var_ratio_of_supply_to_secondary_ha_values = 0.0
        obj.ratio_of_supply_to_secondary_ha_values = var_ratio_of_supply_to_secondary_ha_values
        # real
        var_nominal_supply_air_flow_rate = 0.0001
        obj.nominal_supply_air_flow_rate = var_nominal_supply_air_flow_rate
        # real
        var_nominal_supply_air_inlet_temperature = 7.7
        obj.nominal_supply_air_inlet_temperature = var_nominal_supply_air_inlet_temperature
        # real
        var_nominal_supply_air_outlet_temperature = 8.8
        obj.nominal_supply_air_outlet_temperature = var_nominal_supply_air_outlet_temperature
        # real
        var_nominal_secondary_air_flow_rate = 0.0001
        obj.nominal_secondary_air_flow_rate = var_nominal_secondary_air_flow_rate
        # real
        var_nominal_secondary_air_inlet_temperature = 10.1
        obj.nominal_secondary_air_inlet_temperature = var_nominal_secondary_air_inlet_temperature
        # real
        var_nominal_electric_power = 11.11
        obj.nominal_electric_power = var_nominal_electric_power
        # node
        var_supply_air_inlet_node_name = "node|Supply Air Inlet Node Name"
        obj.supply_air_inlet_node_name = var_supply_air_inlet_node_name
        # node
        var_supply_air_outlet_node_name = "node|Supply Air Outlet Node Name"
        obj.supply_air_outlet_node_name = var_supply_air_outlet_node_name
        # node
        var_secondary_air_inlet_node_name = "node|Secondary Air Inlet Node Name"
        obj.secondary_air_inlet_node_name = var_secondary_air_inlet_node_name
        # node
        var_secondary_air_outlet_node_name = "node|Secondary Air Outlet Node Name"
        obj.secondary_air_outlet_node_name = var_secondary_air_outlet_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.heatexchangerairtoairflatplates[0].name, var_name)
        self.assertEqual(idf2.heatexchangerairtoairflatplates[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.heatexchangerairtoairflatplates[0].flow_arrangement_type, var_flow_arrangement_type)
        self.assertEqual(idf2.heatexchangerairtoairflatplates[0].economizer_lockout, var_economizer_lockout)
        self.assertAlmostEqual(idf2.heatexchangerairtoairflatplates[0].ratio_of_supply_to_secondary_ha_values, var_ratio_of_supply_to_secondary_ha_values)
        self.assertAlmostEqual(idf2.heatexchangerairtoairflatplates[0].nominal_supply_air_flow_rate, var_nominal_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.heatexchangerairtoairflatplates[0].nominal_supply_air_inlet_temperature, var_nominal_supply_air_inlet_temperature)
        self.assertAlmostEqual(idf2.heatexchangerairtoairflatplates[0].nominal_supply_air_outlet_temperature, var_nominal_supply_air_outlet_temperature)
        self.assertAlmostEqual(idf2.heatexchangerairtoairflatplates[0].nominal_secondary_air_flow_rate, var_nominal_secondary_air_flow_rate)
        self.assertAlmostEqual(idf2.heatexchangerairtoairflatplates[0].nominal_secondary_air_inlet_temperature, var_nominal_secondary_air_inlet_temperature)
        self.assertAlmostEqual(idf2.heatexchangerairtoairflatplates[0].nominal_electric_power, var_nominal_electric_power)
        self.assertEqual(idf2.heatexchangerairtoairflatplates[0].supply_air_inlet_node_name, var_supply_air_inlet_node_name)
        self.assertEqual(idf2.heatexchangerairtoairflatplates[0].supply_air_outlet_node_name, var_supply_air_outlet_node_name)
        self.assertEqual(idf2.heatexchangerairtoairflatplates[0].secondary_air_inlet_node_name, var_secondary_air_inlet_node_name)
        self.assertEqual(idf2.heatexchangerairtoairflatplates[0].secondary_air_outlet_node_name, var_secondary_air_outlet_node_name)