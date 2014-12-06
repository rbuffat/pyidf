import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import SimulationControl
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSimulationControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_simulationcontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SimulationControl()
        # alpha
        var_do_zone_sizing_calculation = "Yes"
        obj.do_zone_sizing_calculation = var_do_zone_sizing_calculation
        # alpha
        var_do_system_sizing_calculation = "Yes"
        obj.do_system_sizing_calculation = var_do_system_sizing_calculation
        # alpha
        var_do_plant_sizing_calculation = "Yes"
        obj.do_plant_sizing_calculation = var_do_plant_sizing_calculation
        # alpha
        var_run_simulation_for_sizing_periods = "Yes"
        obj.run_simulation_for_sizing_periods = var_run_simulation_for_sizing_periods
        # alpha
        var_run_simulation_for_weather_file_run_periods = "Yes"
        obj.run_simulation_for_weather_file_run_periods = var_run_simulation_for_weather_file_run_periods

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.simulationcontrols[0].do_zone_sizing_calculation, var_do_zone_sizing_calculation)
        self.assertEqual(idf2.simulationcontrols[0].do_system_sizing_calculation, var_do_system_sizing_calculation)
        self.assertEqual(idf2.simulationcontrols[0].do_plant_sizing_calculation, var_do_plant_sizing_calculation)
        self.assertEqual(idf2.simulationcontrols[0].run_simulation_for_sizing_periods, var_run_simulation_for_sizing_periods)
        self.assertEqual(idf2.simulationcontrols[0].run_simulation_for_weather_file_run_periods, var_run_simulation_for_weather_file_run_periods)