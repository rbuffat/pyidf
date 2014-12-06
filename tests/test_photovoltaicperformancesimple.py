import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import PhotovoltaicPerformanceSimple
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPhotovoltaicPerformanceSimple(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_photovoltaicperformancesimple(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PhotovoltaicPerformanceSimple()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_fraction_of_surface_area_with_active_solar_cells = 0.5
        obj.fraction_of_surface_area_with_active_solar_cells = var_fraction_of_surface_area_with_active_solar_cells
        # alpha
        var_conversion_efficiency_input_mode = "Fixed"
        obj.conversion_efficiency_input_mode = var_conversion_efficiency_input_mode
        # real
        var_value_for_cell_efficiency_if_fixed = 0.5
        obj.value_for_cell_efficiency_if_fixed = var_value_for_cell_efficiency_if_fixed
        # object-list
        var_efficiency_schedule_name = "object-list|Efficiency Schedule Name"
        obj.efficiency_schedule_name = var_efficiency_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.photovoltaicperformancesimples[0].name, var_name)
        self.assertAlmostEqual(idf2.photovoltaicperformancesimples[0].fraction_of_surface_area_with_active_solar_cells, var_fraction_of_surface_area_with_active_solar_cells)
        self.assertEqual(idf2.photovoltaicperformancesimples[0].conversion_efficiency_input_mode, var_conversion_efficiency_input_mode)
        self.assertAlmostEqual(idf2.photovoltaicperformancesimples[0].value_for_cell_efficiency_if_fixed, var_value_for_cell_efficiency_if_fixed)
        self.assertEqual(idf2.photovoltaicperformancesimples[0].efficiency_schedule_name, var_efficiency_schedule_name)