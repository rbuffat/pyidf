import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.simulation_parameters import Building

log = logging.getLogger(__name__)

class TestBuilding(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_building(self):

        pyidf.validation_level = ValidationLevel.error

        obj = Building()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_north_axis = 2.2
        obj.north_axis = var_north_axis
        # alpha
        var_terrain = "Country"
        obj.terrain = var_terrain
        # real
        var_loads_convergence_tolerance_value = 0.25005
        obj.loads_convergence_tolerance_value = var_loads_convergence_tolerance_value
        # real
        var_temperature_convergence_tolerance_value = 0.25005
        obj.temperature_convergence_tolerance_value = var_temperature_convergence_tolerance_value
        # alpha
        var_solar_distribution = "MinimalShadowing"
        obj.solar_distribution = var_solar_distribution
        # integer
        var_maximum_number_of_warmup_days = 1
        obj.maximum_number_of_warmup_days = var_maximum_number_of_warmup_days
        # integer
        var_minimum_number_of_warmup_days = 1
        obj.minimum_number_of_warmup_days = var_minimum_number_of_warmup_days

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.buildings[0].name, var_name)
        self.assertAlmostEqual(idf2.buildings[0].north_axis, var_north_axis)
        self.assertEqual(idf2.buildings[0].terrain, var_terrain)
        self.assertAlmostEqual(idf2.buildings[0].loads_convergence_tolerance_value, var_loads_convergence_tolerance_value)
        self.assertAlmostEqual(idf2.buildings[0].temperature_convergence_tolerance_value, var_temperature_convergence_tolerance_value)
        self.assertEqual(idf2.buildings[0].solar_distribution, var_solar_distribution)
        self.assertEqual(idf2.buildings[0].maximum_number_of_warmup_days, var_maximum_number_of_warmup_days)
        self.assertEqual(idf2.buildings[0].minimum_number_of_warmup_days, var_minimum_number_of_warmup_days)