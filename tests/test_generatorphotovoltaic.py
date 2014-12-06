import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import GeneratorPhotovoltaic
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGeneratorPhotovoltaic(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorphotovoltaic(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorPhotovoltaic()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # alpha
        var_photovoltaic_performance_object_type = "PhotovoltaicPerformance:Simple"
        obj.photovoltaic_performance_object_type = var_photovoltaic_performance_object_type
        # object-list
        var_module_performance_name = "object-list|Module Performance Name"
        obj.module_performance_name = var_module_performance_name
        # alpha
        var_heat_transfer_integration_mode = "Decoupled"
        obj.heat_transfer_integration_mode = var_heat_transfer_integration_mode
        # real
        var_number_of_series_strings_in_parallel = 1.0
        obj.number_of_series_strings_in_parallel = var_number_of_series_strings_in_parallel
        # real
        var_number_of_modules_in_series = 1.0
        obj.number_of_modules_in_series = var_number_of_modules_in_series

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorphotovoltaics[0].name, var_name)
        self.assertEqual(idf2.generatorphotovoltaics[0].surface_name, var_surface_name)
        self.assertEqual(idf2.generatorphotovoltaics[0].photovoltaic_performance_object_type, var_photovoltaic_performance_object_type)
        self.assertEqual(idf2.generatorphotovoltaics[0].module_performance_name, var_module_performance_name)
        self.assertEqual(idf2.generatorphotovoltaics[0].heat_transfer_integration_mode, var_heat_transfer_integration_mode)
        self.assertAlmostEqual(idf2.generatorphotovoltaics[0].number_of_series_strings_in_parallel, var_number_of_series_strings_in_parallel)
        self.assertAlmostEqual(idf2.generatorphotovoltaics[0].number_of_modules_in_series, var_number_of_modules_in_series)