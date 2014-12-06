import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.refrigeration import RefrigerationCondenserWaterCooled

log = logging.getLogger(__name__)

class TestRefrigerationCondenserWaterCooled(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationcondenserwatercooled(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationCondenserWaterCooled()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_rated_effective_total_heat_rejection_rate = 0.0001
        obj.rated_effective_total_heat_rejection_rate = var_rated_effective_total_heat_rejection_rate
        # real
        var_rated_condensing_temperature = 0.0001
        obj.rated_condensing_temperature = var_rated_condensing_temperature
        # real
        var_rated_subcooling_temperature_difference = 0.0
        obj.rated_subcooling_temperature_difference = var_rated_subcooling_temperature_difference
        # real
        var_rated_water_inlet_temperature = 0.0001
        obj.rated_water_inlet_temperature = var_rated_water_inlet_temperature
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
        # alpha
        var_watercooled_loop_flow_type = "VariableFlow"
        obj.watercooled_loop_flow_type = var_watercooled_loop_flow_type
        # object-list
        var_water_outlet_temperature_schedule_name = "object-list|Water Outlet Temperature Schedule Name"
        obj.water_outlet_temperature_schedule_name = var_water_outlet_temperature_schedule_name
        # real
        var_water_design_flow_rate = 0.0001
        obj.water_design_flow_rate = var_water_design_flow_rate
        # real
        var_water_maximum_flow_rate = 0.0001
        obj.water_maximum_flow_rate = var_water_maximum_flow_rate
        # real
        var_water_maximum_water_outlet_temperature = 35.0
        obj.water_maximum_water_outlet_temperature = var_water_maximum_water_outlet_temperature
        # real
        var_water_minimum_water_inlet_temperature = 20.0
        obj.water_minimum_water_inlet_temperature = var_water_minimum_water_inlet_temperature
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # real
        var_condenser_refrigerant_operating_charge_inventory = 15.15
        obj.condenser_refrigerant_operating_charge_inventory = var_condenser_refrigerant_operating_charge_inventory
        # real
        var_condensate_receiver_refrigerant_inventory = 16.16
        obj.condensate_receiver_refrigerant_inventory = var_condensate_receiver_refrigerant_inventory
        # real
        var_condensate_piping_refrigerant_inventory = 17.17
        obj.condensate_piping_refrigerant_inventory = var_condensate_piping_refrigerant_inventory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationcondenserwatercooleds[0].name, var_name)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].rated_effective_total_heat_rejection_rate, var_rated_effective_total_heat_rejection_rate)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].rated_condensing_temperature, var_rated_condensing_temperature)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].rated_subcooling_temperature_difference, var_rated_subcooling_temperature_difference)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].rated_water_inlet_temperature, var_rated_water_inlet_temperature)
        self.assertEqual(idf2.refrigerationcondenserwatercooleds[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.refrigerationcondenserwatercooleds[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.refrigerationcondenserwatercooleds[0].watercooled_loop_flow_type, var_watercooled_loop_flow_type)
        self.assertEqual(idf2.refrigerationcondenserwatercooleds[0].water_outlet_temperature_schedule_name, var_water_outlet_temperature_schedule_name)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].water_design_flow_rate, var_water_design_flow_rate)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].water_maximum_flow_rate, var_water_maximum_flow_rate)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].water_maximum_water_outlet_temperature, var_water_maximum_water_outlet_temperature)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].water_minimum_water_inlet_temperature, var_water_minimum_water_inlet_temperature)
        self.assertEqual(idf2.refrigerationcondenserwatercooleds[0].enduse_subcategory, var_enduse_subcategory)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].condenser_refrigerant_operating_charge_inventory, var_condenser_refrigerant_operating_charge_inventory)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].condensate_receiver_refrigerant_inventory, var_condensate_receiver_refrigerant_inventory)
        self.assertAlmostEqual(idf2.refrigerationcondenserwatercooleds[0].condensate_piping_refrigerant_inventory, var_condensate_piping_refrigerant_inventory)