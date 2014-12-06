import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilHeatingDesuperheater

log = logging.getLogger(__name__)

class TestCoilHeatingDesuperheater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatingdesuperheater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingDesuperheater()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_heat_reclaim_recovery_efficiency = 0.0
        obj.heat_reclaim_recovery_efficiency = var_heat_reclaim_recovery_efficiency
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_heating_source_object_type = "Coil:Cooling:DX:SingleSpeed"
        obj.heating_source_object_type = var_heating_source_object_type
        # object-list
        var_heating_source_name = "object-list|Heating Source Name"
        obj.heating_source_name = var_heating_source_name
        # node
        var_temperature_setpoint_node_name = "node|Temperature Setpoint Node Name"
        obj.temperature_setpoint_node_name = var_temperature_setpoint_node_name
        # real
        var_parasitic_electric_load = 0.0
        obj.parasitic_electric_load = var_parasitic_electric_load

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatingdesuperheaters[0].name, var_name)
        self.assertEqual(idf2.coilheatingdesuperheaters[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.coilheatingdesuperheaters[0].heat_reclaim_recovery_efficiency, var_heat_reclaim_recovery_efficiency)
        self.assertEqual(idf2.coilheatingdesuperheaters[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilheatingdesuperheaters[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilheatingdesuperheaters[0].heating_source_object_type, var_heating_source_object_type)
        self.assertEqual(idf2.coilheatingdesuperheaters[0].heating_source_name, var_heating_source_name)
        self.assertEqual(idf2.coilheatingdesuperheaters[0].temperature_setpoint_node_name, var_temperature_setpoint_node_name)
        self.assertAlmostEqual(idf2.coilheatingdesuperheaters[0].parasitic_electric_load, var_parasitic_electric_load)