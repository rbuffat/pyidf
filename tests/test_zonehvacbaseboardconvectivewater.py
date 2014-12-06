import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_radiative import ZoneHvacBaseboardConvectiveWater
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacBaseboardConvectiveWater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacbaseboardconvectivewater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacBaseboardConvectiveWater()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # alpha
        var_heating_design_capacity_method = "HeatingDesignCapacity"
        obj.heating_design_capacity_method = var_heating_design_capacity_method
        # real
        var_heating_design_capacity = 0.0
        obj.heating_design_capacity = var_heating_design_capacity
        # real
        var_heating_design_capacity_per_floor_area = 0.0
        obj.heating_design_capacity_per_floor_area = var_heating_design_capacity_per_floor_area
        # real
        var_fraction_of_autosized_heating_design_capacity = 0.0
        obj.fraction_of_autosized_heating_design_capacity = var_fraction_of_autosized_heating_design_capacity
        # real
        var_ufactor_times_area_value = 9.9
        obj.ufactor_times_area_value = var_ufactor_times_area_value
        # real
        var_maximum_water_flow_rate = 10.1
        obj.maximum_water_flow_rate = var_maximum_water_flow_rate
        # real
        var_convergence_tolerance = 0.0001
        obj.convergence_tolerance = var_convergence_tolerance

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacbaseboardconvectivewaters[0].name, var_name)
        self.assertEqual(idf2.zonehvacbaseboardconvectivewaters[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacbaseboardconvectivewaters[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.zonehvacbaseboardconvectivewaters[0].outlet_node_name, var_outlet_node_name)
        self.assertEqual(idf2.zonehvacbaseboardconvectivewaters[0].heating_design_capacity_method, var_heating_design_capacity_method)
        self.assertAlmostEqual(idf2.zonehvacbaseboardconvectivewaters[0].heating_design_capacity, var_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvacbaseboardconvectivewaters[0].heating_design_capacity_per_floor_area, var_heating_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.zonehvacbaseboardconvectivewaters[0].fraction_of_autosized_heating_design_capacity, var_fraction_of_autosized_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvacbaseboardconvectivewaters[0].ufactor_times_area_value, var_ufactor_times_area_value)
        self.assertAlmostEqual(idf2.zonehvacbaseboardconvectivewaters[0].maximum_water_flow_rate, var_maximum_water_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacbaseboardconvectivewaters[0].convergence_tolerance, var_convergence_tolerance)