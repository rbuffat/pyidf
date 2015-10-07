import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_heaters_and_thermal_storage import ThermalStorageIceDetailed

log = logging.getLogger(__name__)

class TestThermalStorageIceDetailed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_thermalstorageicedetailed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ThermalStorageIceDetailed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_capacity = 3.3
        obj.capacity = var_capacity
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # alpha
        var_discharging_curve_object_type = "Curve:QuadraticLinear"
        obj.discharging_curve_object_type = var_discharging_curve_object_type
        # object-list
        var_discharging_curve_name = "object-list|Discharging Curve Name"
        obj.discharging_curve_name = var_discharging_curve_name
        # alpha
        var_charging_curve_object_type = "Curve:QuadraticLinear"
        obj.charging_curve_object_type = var_charging_curve_object_type
        # object-list
        var_charging_curve_name = "object-list|Charging Curve Name"
        obj.charging_curve_name = var_charging_curve_name
        # real
        var_timestep_of_the_curve_data = 10.1
        obj.timestep_of_the_curve_data = var_timestep_of_the_curve_data
        # real
        var_parasitic_electric_load_during_discharging = 11.11
        obj.parasitic_electric_load_during_discharging = var_parasitic_electric_load_during_discharging
        # real
        var_parasitic_electric_load_during_charging = 12.12
        obj.parasitic_electric_load_during_charging = var_parasitic_electric_load_during_charging
        # real
        var_tank_loss_coefficient = 13.13
        obj.tank_loss_coefficient = var_tank_loss_coefficient
        # real
        var_freezing_temperature_of_storage_medium = 14.14
        obj.freezing_temperature_of_storage_medium = var_freezing_temperature_of_storage_medium
        # alpha
        var_thaw_process_indicator = "InsideMelt"
        obj.thaw_process_indicator = var_thaw_process_indicator

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.thermalstorageicedetaileds[0].name, var_name)
        self.assertEqual(idf2.thermalstorageicedetaileds[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.thermalstorageicedetaileds[0].capacity, var_capacity)
        self.assertEqual(idf2.thermalstorageicedetaileds[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.thermalstorageicedetaileds[0].outlet_node_name, var_outlet_node_name)
        self.assertEqual(idf2.thermalstorageicedetaileds[0].discharging_curve_object_type, var_discharging_curve_object_type)
        self.assertEqual(idf2.thermalstorageicedetaileds[0].discharging_curve_name, var_discharging_curve_name)
        self.assertEqual(idf2.thermalstorageicedetaileds[0].charging_curve_object_type, var_charging_curve_object_type)
        self.assertEqual(idf2.thermalstorageicedetaileds[0].charging_curve_name, var_charging_curve_name)
        self.assertAlmostEqual(idf2.thermalstorageicedetaileds[0].timestep_of_the_curve_data, var_timestep_of_the_curve_data)
        self.assertAlmostEqual(idf2.thermalstorageicedetaileds[0].parasitic_electric_load_during_discharging, var_parasitic_electric_load_during_discharging)
        self.assertAlmostEqual(idf2.thermalstorageicedetaileds[0].parasitic_electric_load_during_charging, var_parasitic_electric_load_during_charging)
        self.assertAlmostEqual(idf2.thermalstorageicedetaileds[0].tank_loss_coefficient, var_tank_loss_coefficient)
        self.assertAlmostEqual(idf2.thermalstorageicedetaileds[0].freezing_temperature_of_storage_medium, var_freezing_temperature_of_storage_medium)
        self.assertEqual(idf2.thermalstorageicedetaileds[0].thaw_process_indicator, var_thaw_process_indicator)