import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import SiteSolarAndVisibleSpectrum
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSiteSolarAndVisibleSpectrum(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitesolarandvisiblespectrum(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteSolarAndVisibleSpectrum()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_spectrum_data_method = "Default"
        obj.spectrum_data_method = var_spectrum_data_method
        # alpha
        var_solar_spectrum_data_object_name = "Solar Spectrum Data Object Name"
        obj.solar_spectrum_data_object_name = var_solar_spectrum_data_object_name
        # alpha
        var_visible_spectrum_data_object_name = "Visible Spectrum Data Object Name"
        obj.visible_spectrum_data_object_name = var_visible_spectrum_data_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sitesolarandvisiblespectrums[0].name, var_name)
        self.assertEqual(idf2.sitesolarandvisiblespectrums[0].spectrum_data_method, var_spectrum_data_method)
        self.assertEqual(idf2.sitesolarandvisiblespectrums[0].solar_spectrum_data_object_name, var_solar_spectrum_data_object_name)
        self.assertEqual(idf2.sitesolarandvisiblespectrums[0].visible_spectrum_data_object_name, var_visible_spectrum_data_object_name)