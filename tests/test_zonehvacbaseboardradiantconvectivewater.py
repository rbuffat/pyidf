import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_radiative import ZoneHvacBaseboardRadiantConvectiveWater
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacBaseboardRadiantConvectiveWater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacbaseboardradiantconvectivewater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacBaseboardRadiantConvectiveWater()
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
        # real
        var_rated_average_water_temperature = 85.0
        obj.rated_average_water_temperature = var_rated_average_water_temperature
        # real
        var_rated_water_mass_flow_rate = 5.00005
        obj.rated_water_mass_flow_rate = var_rated_water_mass_flow_rate
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
        var_maximum_water_flow_rate = 11.11
        obj.maximum_water_flow_rate = var_maximum_water_flow_rate
        # real
        var_convergence_tolerance = 0.0001
        obj.convergence_tolerance = var_convergence_tolerance
        # real
        var_fraction_radiant = 0.5
        obj.fraction_radiant = var_fraction_radiant
        # real
        var_fraction_of_radiant_energy_incident_on_people = 0.5
        obj.fraction_of_radiant_energy_incident_on_people = var_fraction_of_radiant_energy_incident_on_people
        paras = []
        var_surface_1_name = "object-list|Surface 1 Name"
        paras.append(var_surface_1_name)
        var_fraction_of_radiant_energy_to_surface_1 = 0.5
        paras.append(var_fraction_of_radiant_energy_to_surface_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].name, var_name)
        self.assertEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].outlet_node_name, var_outlet_node_name)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].rated_average_water_temperature, var_rated_average_water_temperature)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].rated_water_mass_flow_rate, var_rated_water_mass_flow_rate)
        self.assertEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].heating_design_capacity_method, var_heating_design_capacity_method)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].heating_design_capacity, var_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].heating_design_capacity_per_floor_area, var_heating_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].fraction_of_autosized_heating_design_capacity, var_fraction_of_autosized_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].maximum_water_flow_rate, var_maximum_water_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].convergence_tolerance, var_convergence_tolerance)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].fraction_radiant, var_fraction_radiant)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].fraction_of_radiant_energy_incident_on_people, var_fraction_of_radiant_energy_incident_on_people)
        index = obj.extensible_field_index("Surface 1 Name")
        self.assertEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].extensibles[0][index], var_surface_1_name)
        index = obj.extensible_field_index("Fraction of Radiant Energy to Surface 1")
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectivewaters[0].extensibles[0][index], var_fraction_of_radiant_energy_to_surface_1)