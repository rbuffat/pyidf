import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import ConvergenceLimits
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestConvergenceLimits(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_convergencelimits(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ConvergenceLimits()
        # integer
        var_minimum_system_timestep = 30
        obj.minimum_system_timestep = var_minimum_system_timestep
        # integer
        var_maximum_hvac_iterations = 1
        obj.maximum_hvac_iterations = var_maximum_hvac_iterations
        # integer
        var_minimum_plant_iterations = 1
        obj.minimum_plant_iterations = var_minimum_plant_iterations
        # integer
        var_maximum_plant_iterations = 2
        obj.maximum_plant_iterations = var_maximum_plant_iterations

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.convergencelimitss[0].minimum_system_timestep, var_minimum_system_timestep)
        self.assertEqual(idf2.convergencelimitss[0].maximum_hvac_iterations, var_maximum_hvac_iterations)
        self.assertEqual(idf2.convergencelimitss[0].minimum_plant_iterations, var_minimum_plant_iterations)
        self.assertEqual(idf2.convergencelimitss[0].maximum_plant_iterations, var_maximum_plant_iterations)