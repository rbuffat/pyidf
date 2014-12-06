import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_radiative import ZoneHvacBaseboardRadiantConvectiveElectric
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacBaseboardRadiantConvectiveElectric(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacbaseboardradiantconvectiveelectric(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacBaseboardRadiantConvectiveElectric()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
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
        var_efficiency = 0.50005
        obj.efficiency = var_efficiency
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
        self.assertEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].name, var_name)
        self.assertEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].heating_design_capacity_method, var_heating_design_capacity_method)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].heating_design_capacity, var_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].heating_design_capacity_per_floor_area, var_heating_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].fraction_of_autosized_heating_design_capacity, var_fraction_of_autosized_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].efficiency, var_efficiency)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].fraction_radiant, var_fraction_radiant)
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].fraction_of_radiant_energy_incident_on_people, var_fraction_of_radiant_energy_incident_on_people)
        index = obj.extensible_field_index("Surface 1 Name")
        self.assertEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].extensibles[0][index], var_surface_1_name)
        index = obj.extensible_field_index("Fraction of Radiant Energy to Surface 1")
        self.assertAlmostEqual(idf2.zonehvacbaseboardradiantconvectiveelectrics[0].extensibles[0][index], var_fraction_of_radiant_energy_to_surface_1)