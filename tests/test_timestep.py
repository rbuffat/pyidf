import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.simulation_parameters import Timestep

log = logging.getLogger(__name__)

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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.timesteps[0].number_of_timesteps_per_hour, var_number_of_timesteps_per_hour)