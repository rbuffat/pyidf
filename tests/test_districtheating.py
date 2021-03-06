import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant_heating_and_cooling_equipment import DistrictHeating

log = logging.getLogger(__name__)

class TestDistrictHeating(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_districtheating(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DistrictHeating()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_hot_water_inlet_node_name = "node|Hot Water Inlet Node Name"
        obj.hot_water_inlet_node_name = var_hot_water_inlet_node_name
        # node
        var_hot_water_outlet_node_name = "node|Hot Water Outlet Node Name"
        obj.hot_water_outlet_node_name = var_hot_water_outlet_node_name
        # real
        var_nominal_capacity = 0.0
        obj.nominal_capacity = var_nominal_capacity
        # object-list
        var_capacity_fraction_schedule_name = "object-list|Capacity Fraction Schedule Name"
        obj.capacity_fraction_schedule_name = var_capacity_fraction_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.districtheatings[0].name, var_name)
        self.assertEqual(idf2.districtheatings[0].hot_water_inlet_node_name, var_hot_water_inlet_node_name)
        self.assertEqual(idf2.districtheatings[0].hot_water_outlet_node_name, var_hot_water_outlet_node_name)
        self.assertAlmostEqual(idf2.districtheatings[0].nominal_capacity, var_nominal_capacity)
        self.assertEqual(idf2.districtheatings[0].capacity_fraction_schedule_name, var_capacity_fraction_schedule_name)