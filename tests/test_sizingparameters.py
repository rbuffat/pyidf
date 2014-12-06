import os
import tempfile
import unittest
import pyidf
from pyidf.hvac_design_objects import SizingParameters
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSizingParameters(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sizingparameters(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SizingParameters()
        # real
        var_heating_sizing_factor = 0.0001
        obj.heating_sizing_factor = var_heating_sizing_factor
        # real
        var_cooling_sizing_factor = 0.0001
        obj.cooling_sizing_factor = var_cooling_sizing_factor
        # integer
        var_timesteps_in_averaging_window = 1
        obj.timesteps_in_averaging_window = var_timesteps_in_averaging_window

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.sizingparameterss[0].heating_sizing_factor, var_heating_sizing_factor)
        self.assertAlmostEqual(idf2.sizingparameterss[0].cooling_sizing_factor, var_cooling_sizing_factor)
        self.assertEqual(idf2.sizingparameterss[0].timesteps_in_averaging_window, var_timesteps_in_averaging_window)