import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SiteGroundTemperatureUndisturbedXing

log = logging.getLogger(__name__)

class TestSiteGroundTemperatureUndisturbedXing(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitegroundtemperatureundisturbedxing(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteGroundTemperatureUndisturbedXing()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_soil_thermal_conductivity = 0.0001
        obj.soil_thermal_conductivity = var_soil_thermal_conductivity
        # real
        var_soil_density = 0.0001
        obj.soil_density = var_soil_density
        # real
        var_soil_specific_heat = 0.0001
        obj.soil_specific_heat = var_soil_specific_heat
        # real
        var_average_soil_surface_tempeature = 5.5
        obj.average_soil_surface_tempeature = var_average_soil_surface_tempeature
        # real
        var_soil_surface_temperature_amplitude_1 = 6.6
        obj.soil_surface_temperature_amplitude_1 = var_soil_surface_temperature_amplitude_1
        # real
        var_soil_surface_temperature_amplitude_2 = 7.7
        obj.soil_surface_temperature_amplitude_2 = var_soil_surface_temperature_amplitude_2
        # real
        var_phase_shift_of_temperature_amplitude_1 = 364.9999
        obj.phase_shift_of_temperature_amplitude_1 = var_phase_shift_of_temperature_amplitude_1
        # real
        var_phase_shift_of_temperature_amplitude_2 = 364.9999
        obj.phase_shift_of_temperature_amplitude_2 = var_phase_shift_of_temperature_amplitude_2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sitegroundtemperatureundisturbedxings[0].name, var_name)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedxings[0].soil_thermal_conductivity, var_soil_thermal_conductivity)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedxings[0].soil_density, var_soil_density)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedxings[0].soil_specific_heat, var_soil_specific_heat)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedxings[0].average_soil_surface_tempeature, var_average_soil_surface_tempeature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedxings[0].soil_surface_temperature_amplitude_1, var_soil_surface_temperature_amplitude_1)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedxings[0].soil_surface_temperature_amplitude_2, var_soil_surface_temperature_amplitude_2)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedxings[0].phase_shift_of_temperature_amplitude_1, var_phase_shift_of_temperature_amplitude_1)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedxings[0].phase_shift_of_temperature_amplitude_2, var_phase_shift_of_temperature_amplitude_2)