import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import WindowThermalModelParams
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowThermalModelParams(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowthermalmodelparams(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowThermalModelParams()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_standard = "ISO15099"
        obj.standard = var_standard
        # alpha
        var_thermal_model = "ISO15099"
        obj.thermal_model = var_thermal_model
        # real
        var_sdscalar = 0.5
        obj.sdscalar = var_sdscalar
        # alpha
        var_deflection_model = "NoDeflection"
        obj.deflection_model = var_deflection_model
        # real
        var_vacuum_pressure_limit = 6.6
        obj.vacuum_pressure_limit = var_vacuum_pressure_limit
        # real
        var_initial_temperature = 7.7
        obj.initial_temperature = var_initial_temperature
        # real
        var_initial_pressure = 8.8
        obj.initial_pressure = var_initial_pressure

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowthermalmodelparamss[0].name, var_name)
        self.assertEqual(idf2.windowthermalmodelparamss[0].standard, var_standard)
        self.assertEqual(idf2.windowthermalmodelparamss[0].thermal_model, var_thermal_model)
        self.assertAlmostEqual(idf2.windowthermalmodelparamss[0].sdscalar, var_sdscalar)
        self.assertEqual(idf2.windowthermalmodelparamss[0].deflection_model, var_deflection_model)
        self.assertAlmostEqual(idf2.windowthermalmodelparamss[0].vacuum_pressure_limit, var_vacuum_pressure_limit)
        self.assertAlmostEqual(idf2.windowthermalmodelparamss[0].initial_temperature, var_initial_temperature)
        self.assertAlmostEqual(idf2.windowthermalmodelparamss[0].initial_pressure, var_initial_pressure)