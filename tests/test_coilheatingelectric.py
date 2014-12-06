import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilHeatingElectric

log = logging.getLogger(__name__)

class TestCoilHeatingElectric(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatingelectric(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingElectric()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_efficiency = 0.50005
        obj.efficiency = var_efficiency
        # real
        var_nominal_capacity = 4.4
        obj.nominal_capacity = var_nominal_capacity
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # node
        var_temperature_setpoint_node_name = "node|Temperature Setpoint Node Name"
        obj.temperature_setpoint_node_name = var_temperature_setpoint_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatingelectrics[0].name, var_name)
        self.assertEqual(idf2.coilheatingelectrics[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.coilheatingelectrics[0].efficiency, var_efficiency)
        self.assertAlmostEqual(idf2.coilheatingelectrics[0].nominal_capacity, var_nominal_capacity)
        self.assertEqual(idf2.coilheatingelectrics[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilheatingelectrics[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilheatingelectrics[0].temperature_setpoint_node_name, var_temperature_setpoint_node_name)