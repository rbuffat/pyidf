import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputControlReportingTolerances
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputControlReportingTolerances(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputcontrolreportingtolerances(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputControlReportingTolerances()
        # real
        var_tolerance_for_time_heating_setpoint_not_met = 5.0
        obj.tolerance_for_time_heating_setpoint_not_met = var_tolerance_for_time_heating_setpoint_not_met
        # real
        var_tolerance_for_time_cooling_setpoint_not_met = 5.0
        obj.tolerance_for_time_cooling_setpoint_not_met = var_tolerance_for_time_cooling_setpoint_not_met

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.outputcontrolreportingtolerancess[0].tolerance_for_time_heating_setpoint_not_met, var_tolerance_for_time_heating_setpoint_not_met)
        self.assertAlmostEqual(idf2.outputcontrolreportingtolerancess[0].tolerance_for_time_cooling_setpoint_not_met, var_tolerance_for_time_cooling_setpoint_not_met)