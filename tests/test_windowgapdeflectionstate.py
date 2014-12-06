import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import WindowGapDeflectionState
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowGapDeflectionState(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowgapdeflectionstate(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowGapDeflectionState()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_deflected_thickness = 0.0
        obj.deflected_thickness = var_deflected_thickness
        # real
        var_initial_temperature = 0.0
        obj.initial_temperature = var_initial_temperature
        # real
        var_initial_pressure = 0.0
        obj.initial_pressure = var_initial_pressure

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowgapdeflectionstates[0].name, var_name)
        self.assertAlmostEqual(idf2.windowgapdeflectionstates[0].deflected_thickness, var_deflected_thickness)
        self.assertAlmostEqual(idf2.windowgapdeflectionstates[0].initial_temperature, var_initial_temperature)
        self.assertAlmostEqual(idf2.windowgapdeflectionstates[0].initial_pressure, var_initial_pressure)