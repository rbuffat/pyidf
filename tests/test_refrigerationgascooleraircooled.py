import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.refrigeration import RefrigerationGasCoolerAirCooled

log = logging.getLogger(__name__)

class TestRefrigerationGasCoolerAirCooled(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationgascooleraircooled(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationGasCoolerAirCooled()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_rated_total_heat_rejection_rate_curve_name = "object-list|Rated Total Heat Rejection Rate Curve Name"
        obj.rated_total_heat_rejection_rate_curve_name = var_rated_total_heat_rejection_rate_curve_name
        # alpha
        var_gas_cooler_fan_speed_control_type = "Fixed"
        obj.gas_cooler_fan_speed_control_type = var_gas_cooler_fan_speed_control_type
        # real
        var_rated_fan_power = 0.0
        obj.rated_fan_power = var_rated_fan_power
        # real
        var_minimum_fan_air_flow_ratio = 0.0
        obj.minimum_fan_air_flow_ratio = var_minimum_fan_air_flow_ratio
        # real
        var_transition_temperature = 6.6
        obj.transition_temperature = var_transition_temperature
        # real
        var_transcritical_approach_temperature = 7.7
        obj.transcritical_approach_temperature = var_transcritical_approach_temperature
        # real
        var_subcritical_temperature_difference = 8.8
        obj.subcritical_temperature_difference = var_subcritical_temperature_difference
        # real
        var_minimum_condensing_temperature = 9.9
        obj.minimum_condensing_temperature = var_minimum_condensing_temperature
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # real
        var_gas_cooler_refrigerant_operating_charge_inventory = 12.12
        obj.gas_cooler_refrigerant_operating_charge_inventory = var_gas_cooler_refrigerant_operating_charge_inventory
        # real
        var_gas_cooler_receiver_refrigerant_inventory = 13.13
        obj.gas_cooler_receiver_refrigerant_inventory = var_gas_cooler_receiver_refrigerant_inventory
        # real
        var_gas_cooler_outlet_piping_refrigerant_inventory = 14.14
        obj.gas_cooler_outlet_piping_refrigerant_inventory = var_gas_cooler_outlet_piping_refrigerant_inventory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationgascooleraircooleds[0].name, var_name)
        self.assertEqual(idf2.refrigerationgascooleraircooleds[0].rated_total_heat_rejection_rate_curve_name, var_rated_total_heat_rejection_rate_curve_name)
        self.assertEqual(idf2.refrigerationgascooleraircooleds[0].gas_cooler_fan_speed_control_type, var_gas_cooler_fan_speed_control_type)
        self.assertAlmostEqual(idf2.refrigerationgascooleraircooleds[0].rated_fan_power, var_rated_fan_power)
        self.assertAlmostEqual(idf2.refrigerationgascooleraircooleds[0].minimum_fan_air_flow_ratio, var_minimum_fan_air_flow_ratio)
        self.assertAlmostEqual(idf2.refrigerationgascooleraircooleds[0].transition_temperature, var_transition_temperature)
        self.assertAlmostEqual(idf2.refrigerationgascooleraircooleds[0].transcritical_approach_temperature, var_transcritical_approach_temperature)
        self.assertAlmostEqual(idf2.refrigerationgascooleraircooleds[0].subcritical_temperature_difference, var_subcritical_temperature_difference)
        self.assertAlmostEqual(idf2.refrigerationgascooleraircooleds[0].minimum_condensing_temperature, var_minimum_condensing_temperature)
        self.assertEqual(idf2.refrigerationgascooleraircooleds[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.refrigerationgascooleraircooleds[0].enduse_subcategory, var_enduse_subcategory)
        self.assertAlmostEqual(idf2.refrigerationgascooleraircooleds[0].gas_cooler_refrigerant_operating_charge_inventory, var_gas_cooler_refrigerant_operating_charge_inventory)
        self.assertAlmostEqual(idf2.refrigerationgascooleraircooleds[0].gas_cooler_receiver_refrigerant_inventory, var_gas_cooler_receiver_refrigerant_inventory)
        self.assertAlmostEqual(idf2.refrigerationgascooleraircooleds[0].gas_cooler_outlet_piping_refrigerant_inventory, var_gas_cooler_outlet_piping_refrigerant_inventory)