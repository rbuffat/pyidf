import os
import tempfile
import unittest
import pyidf
from pyidf.coils import CoilSystemCoolingDx
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCoilSystemCoolingDx(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilsystemcoolingdx(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilSystemCoolingDx()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_dx_cooling_coil_system_inlet_node_name = "node|DX Cooling Coil System Inlet Node Name"
        obj.dx_cooling_coil_system_inlet_node_name = var_dx_cooling_coil_system_inlet_node_name
        # node
        var_dx_cooling_coil_system_outlet_node_name = "node|DX Cooling Coil System Outlet Node Name"
        obj.dx_cooling_coil_system_outlet_node_name = var_dx_cooling_coil_system_outlet_node_name
        # node
        var_dx_cooling_coil_system_sensor_node_name = "node|DX Cooling Coil System Sensor Node Name"
        obj.dx_cooling_coil_system_sensor_node_name = var_dx_cooling_coil_system_sensor_node_name
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:DX:SingleSpeed"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # alpha
        var_dehumidification_control_type = "None"
        obj.dehumidification_control_type = var_dehumidification_control_type
        # alpha
        var_run_on_sensible_load = "Yes"
        obj.run_on_sensible_load = var_run_on_sensible_load
        # alpha
        var_run_on_latent_load = "Yes"
        obj.run_on_latent_load = var_run_on_latent_load
        # alpha
        var_use_outdoor_air_dx_cooling_coil = "Yes"
        obj.use_outdoor_air_dx_cooling_coil = var_use_outdoor_air_dx_cooling_coil
        # real
        var_outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature = 3.6
        obj.outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature = var_outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].name, var_name)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].dx_cooling_coil_system_inlet_node_name, var_dx_cooling_coil_system_inlet_node_name)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].dx_cooling_coil_system_outlet_node_name, var_dx_cooling_coil_system_outlet_node_name)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].dx_cooling_coil_system_sensor_node_name, var_dx_cooling_coil_system_sensor_node_name)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].cooling_coil_name, var_cooling_coil_name)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].run_on_sensible_load, var_run_on_sensible_load)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].run_on_latent_load, var_run_on_latent_load)
        self.assertEqual(idf2.coilsystemcoolingdxs[0].use_outdoor_air_dx_cooling_coil, var_use_outdoor_air_dx_cooling_coil)
        self.assertAlmostEqual(idf2.coilsystemcoolingdxs[0].outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature, var_outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature)