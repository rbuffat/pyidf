import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.economics import ComponentCostLineItem

log = logging.getLogger(__name__)

class TestComponentCostLineItem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_componentcostlineitem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ComponentCostLineItem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_type = "Type"
        obj.type = var_type
        # alpha
        var_line_item_type = "General"
        obj.line_item_type = var_line_item_type
        # alpha
        var_item_name = "Item Name"
        obj.item_name = var_item_name
        # alpha
        var_object_enduse_key = "Object End-Use Key"
        obj.object_enduse_key = var_object_enduse_key
        # real
        var_cost_per_each = 6.6
        obj.cost_per_each = var_cost_per_each
        # real
        var_cost_per_area = 7.7
        obj.cost_per_area = var_cost_per_area
        # real
        var_cost_per_unit_of_output_capacity = 8.8
        obj.cost_per_unit_of_output_capacity = var_cost_per_unit_of_output_capacity
        # real
        var_cost_per_unit_of_output_capacity_per_cop = 9.9
        obj.cost_per_unit_of_output_capacity_per_cop = var_cost_per_unit_of_output_capacity_per_cop
        # real
        var_cost_per_volume = 10.1
        obj.cost_per_volume = var_cost_per_volume
        # real
        var_cost_per_volume_rate = 11.11
        obj.cost_per_volume_rate = var_cost_per_volume_rate
        # real
        var_cost_per_energy_per_temperature_difference = 12.12
        obj.cost_per_energy_per_temperature_difference = var_cost_per_energy_per_temperature_difference
        # real
        var_quantity = 13.13
        obj.quantity = var_quantity

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.componentcostlineitems[0].name, var_name)
        self.assertEqual(idf2.componentcostlineitems[0].type, var_type)
        self.assertEqual(idf2.componentcostlineitems[0].line_item_type, var_line_item_type)
        self.assertEqual(idf2.componentcostlineitems[0].item_name, var_item_name)
        self.assertEqual(idf2.componentcostlineitems[0].object_enduse_key, var_object_enduse_key)
        self.assertAlmostEqual(idf2.componentcostlineitems[0].cost_per_each, var_cost_per_each)
        self.assertAlmostEqual(idf2.componentcostlineitems[0].cost_per_area, var_cost_per_area)
        self.assertAlmostEqual(idf2.componentcostlineitems[0].cost_per_unit_of_output_capacity, var_cost_per_unit_of_output_capacity)
        self.assertAlmostEqual(idf2.componentcostlineitems[0].cost_per_unit_of_output_capacity_per_cop, var_cost_per_unit_of_output_capacity_per_cop)
        self.assertAlmostEqual(idf2.componentcostlineitems[0].cost_per_volume, var_cost_per_volume)
        self.assertAlmostEqual(idf2.componentcostlineitems[0].cost_per_volume_rate, var_cost_per_volume_rate)
        self.assertAlmostEqual(idf2.componentcostlineitems[0].cost_per_energy_per_temperature_difference, var_cost_per_energy_per_temperature_difference)
        self.assertAlmostEqual(idf2.componentcostlineitems[0].quantity, var_quantity)