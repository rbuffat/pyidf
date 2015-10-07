import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SiteGroundTemperatureUndisturbedKusudaAchenbach

log = logging.getLogger(__name__)

class TestSiteGroundTemperatureUndisturbedKusudaAchenbach(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitegroundtemperatureundisturbedkusudaachenbach(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteGroundTemperatureUndisturbedKusudaAchenbach()
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
        var_average_soil_surface_temperature = 5.5
        obj.average_soil_surface_temperature = var_average_soil_surface_temperature
        # real
        var_average_amplitude_of_surface_temperature = 0.0
        obj.average_amplitude_of_surface_temperature = var_average_amplitude_of_surface_temperature
        # real
        var_phase_shift_of_minimum_surface_temperature = 182.49995
        obj.phase_shift_of_minimum_surface_temperature = var_phase_shift_of_minimum_surface_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sitegroundtemperatureundisturbedkusudaachenbachs[0].name, var_name)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedkusudaachenbachs[0].soil_thermal_conductivity, var_soil_thermal_conductivity)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedkusudaachenbachs[0].soil_density, var_soil_density)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedkusudaachenbachs[0].soil_specific_heat, var_soil_specific_heat)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedkusudaachenbachs[0].average_soil_surface_temperature, var_average_soil_surface_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedkusudaachenbachs[0].average_amplitude_of_surface_temperature, var_average_amplitude_of_surface_temperature)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedkusudaachenbachs[0].phase_shift_of_minimum_surface_temperature, var_phase_shift_of_minimum_surface_temperature)