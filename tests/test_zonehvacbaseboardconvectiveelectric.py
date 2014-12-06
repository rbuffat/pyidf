import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_radiative import ZoneHvacBaseboardConvectiveElectric

log = logging.getLogger(__name__)

class TestZoneHvacBaseboardConvectiveElectric(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacbaseboardconvectiveelectric(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacBaseboardConvectiveElectric()
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
        var_efficiency = 0.5
        obj.efficiency = var_efficiency

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacbaseboardconvectiveelectrics[0].name, var_name)
        self.assertEqual(idf2.zonehvacbaseboardconvectiveelectrics[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacbaseboardconvectiveelectrics[0].heating_design_capacity_method, var_heating_design_capacity_method)
        self.assertAlmostEqual(idf2.zonehvacbaseboardconvectiveelectrics[0].heating_design_capacity, var_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvacbaseboardconvectiveelectrics[0].heating_design_capacity_per_floor_area, var_heating_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.zonehvacbaseboardconvectiveelectrics[0].fraction_of_autosized_heating_design_capacity, var_fraction_of_autosized_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvacbaseboardconvectiveelectrics[0].efficiency, var_efficiency)