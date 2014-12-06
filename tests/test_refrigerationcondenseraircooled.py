import os
import tempfile
import unittest
import pyidf
from pyidf.refrigeration import RefrigerationCondenserAirCooled
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRefrigerationCondenserAirCooled(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationcondenseraircooled(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationCondenserAirCooled()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_rated_effective_total_heat_rejection_rate_curve_name = "object-list|Rated Effective Total Heat Rejection Rate Curve Name"
        obj.rated_effective_total_heat_rejection_rate_curve_name = var_rated_effective_total_heat_rejection_rate_curve_name
        # real
        var_rated_subcooling_temperature_difference = 0.0
        obj.rated_subcooling_temperature_difference = var_rated_subcooling_temperature_difference
        # alpha
        var_condenser_fan_speed_control_type = "Fixed"
        obj.condenser_fan_speed_control_type = var_condenser_fan_speed_control_type
        # real
        var_rated_fan_power = 0.0
        obj.rated_fan_power = var_rated_fan_power
        # real
        var_minimum_fan_air_flow_ratio = 0.0
        obj.minimum_fan_air_flow_ratio = var_minimum_fan_air_flow_ratio
        # node
        var_air_inlet_node_name_or_zone_name = "node|Air Inlet Node Name or Zone Name"
        obj.air_inlet_node_name_or_zone_name = var_air_inlet_node_name_or_zone_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # real
        var_condenser_refrigerant_operating_charge_inventory = 9.9
        obj.condenser_refrigerant_operating_charge_inventory = var_condenser_refrigerant_operating_charge_inventory
        # real
        var_condensate_receiver_refrigerant_inventory = 10.1
        obj.condensate_receiver_refrigerant_inventory = var_condensate_receiver_refrigerant_inventory
        # real
        var_condensate_piping_refrigerant_inventory = 11.11
        obj.condensate_piping_refrigerant_inventory = var_condensate_piping_refrigerant_inventory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationcondenseraircooleds[0].name, var_name)
        self.assertEqual(idf2.refrigerationcondenseraircooleds[0].rated_effective_total_heat_rejection_rate_curve_name, var_rated_effective_total_heat_rejection_rate_curve_name)
        self.assertAlmostEqual(idf2.refrigerationcondenseraircooleds[0].rated_subcooling_temperature_difference, var_rated_subcooling_temperature_difference)
        self.assertEqual(idf2.refrigerationcondenseraircooleds[0].condenser_fan_speed_control_type, var_condenser_fan_speed_control_type)
        self.assertAlmostEqual(idf2.refrigerationcondenseraircooleds[0].rated_fan_power, var_rated_fan_power)
        self.assertAlmostEqual(idf2.refrigerationcondenseraircooleds[0].minimum_fan_air_flow_ratio, var_minimum_fan_air_flow_ratio)
        self.assertEqual(idf2.refrigerationcondenseraircooleds[0].air_inlet_node_name_or_zone_name, var_air_inlet_node_name_or_zone_name)
        self.assertEqual(idf2.refrigerationcondenseraircooleds[0].enduse_subcategory, var_enduse_subcategory)
        self.assertAlmostEqual(idf2.refrigerationcondenseraircooleds[0].condenser_refrigerant_operating_charge_inventory, var_condenser_refrigerant_operating_charge_inventory)
        self.assertAlmostEqual(idf2.refrigerationcondenseraircooleds[0].condensate_receiver_refrigerant_inventory, var_condensate_receiver_refrigerant_inventory)
        self.assertAlmostEqual(idf2.refrigerationcondenseraircooleds[0].condensate_piping_refrigerant_inventory, var_condensate_piping_refrigerant_inventory)