import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import Timestep
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestTimestep(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_timestep(self):

        pyidf.validation_level = ValidationLevel.error

        obj = Timestep()
        # integer
        var_number_of_timesteps_per_hour = 30
        obj.number_of_timesteps_per_hour = var_number_of_timesteps_per_hour

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.timesteps[0].number_of_timesteps_per_hour, var_number_of_timesteps_per_hour)