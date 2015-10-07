import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SiteGroundTemperatureUndisturbedFiniteDifference

log = logging.getLogger(__name__)

class TestSiteGroundTemperatureUndisturbedFiniteDifference(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitegroundtemperatureundisturbedfinitedifference(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteGroundTemperatureUndisturbedFiniteDifference()
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
        var_soil_moisture_content_volume_fraction = 50.0
        obj.soil_moisture_content_volume_fraction = var_soil_moisture_content_volume_fraction
        # real
        var_soil_moisture_content_volume_fraction_at_saturation = 50.0
        obj.soil_moisture_content_volume_fraction_at_saturation = var_soil_moisture_content_volume_fraction_at_saturation
        # real
        var_evapotranspiration_ground_cover_parameter = 0.75
        obj.evapotranspiration_ground_cover_parameter = var_evapotranspiration_ground_cover_parameter

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sitegroundtemperatureundisturbedfinitedifferences[0].name, var_name)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedfinitedifferences[0].soil_thermal_conductivity, var_soil_thermal_conductivity)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedfinitedifferences[0].soil_density, var_soil_density)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedfinitedifferences[0].soil_specific_heat, var_soil_specific_heat)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedfinitedifferences[0].soil_moisture_content_volume_fraction, var_soil_moisture_content_volume_fraction)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedfinitedifferences[0].soil_moisture_content_volume_fraction_at_saturation, var_soil_moisture_content_volume_fraction_at_saturation)
        self.assertAlmostEqual(idf2.sitegroundtemperatureundisturbedfinitedifferences[0].evapotranspiration_ground_cover_parameter, var_evapotranspiration_ground_cover_parameter)