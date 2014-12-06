import os
import tempfile
import unittest
import pyidf
from pyidf.operational_faults import FaultModelFoulingCoil
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestFaultModelFoulingCoil(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_faultmodelfoulingcoil(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FaultModelFoulingCoil()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_coil_name = "object-list|Coil Name"
        obj.coil_name = var_coil_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_severity_schedule_name = "object-list|Severity Schedule Name"
        obj.severity_schedule_name = var_severity_schedule_name
        # alpha
        var_fouling_input_method = "FouledUARated"
        obj.fouling_input_method = var_fouling_input_method
        # real
        var_uafouled = 0.0001
        obj.uafouled = var_uafouled
        # real
        var_water_side_fouling_factor = 0.0
        obj.water_side_fouling_factor = var_water_side_fouling_factor
        # real
        var_air_side_fouling_factor = 0.0
        obj.air_side_fouling_factor = var_air_side_fouling_factor
        # real
        var_outside_coil_surface_area = 0.0001
        obj.outside_coil_surface_area = var_outside_coil_surface_area
        # real
        var_inside_to_outside_coil_surface_area_ratio = 0.0001
        obj.inside_to_outside_coil_surface_area_ratio = var_inside_to_outside_coil_surface_area_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.faultmodelfoulingcoils[0].name, var_name)
        self.assertEqual(idf2.faultmodelfoulingcoils[0].coil_name, var_coil_name)
        self.assertEqual(idf2.faultmodelfoulingcoils[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.faultmodelfoulingcoils[0].severity_schedule_name, var_severity_schedule_name)
        self.assertEqual(idf2.faultmodelfoulingcoils[0].fouling_input_method, var_fouling_input_method)
        self.assertAlmostEqual(idf2.faultmodelfoulingcoils[0].uafouled, var_uafouled)
        self.assertAlmostEqual(idf2.faultmodelfoulingcoils[0].water_side_fouling_factor, var_water_side_fouling_factor)
        self.assertAlmostEqual(idf2.faultmodelfoulingcoils[0].air_side_fouling_factor, var_air_side_fouling_factor)
        self.assertAlmostEqual(idf2.faultmodelfoulingcoils[0].outside_coil_surface_area, var_outside_coil_surface_area)
        self.assertAlmostEqual(idf2.faultmodelfoulingcoils[0].inside_to_outside_coil_surface_area_ratio, var_inside_to_outside_coil_surface_area_ratio)