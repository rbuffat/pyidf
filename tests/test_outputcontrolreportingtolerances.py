import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import OutputControlReportingTolerances

log = logging.getLogger(__name__)

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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.outputcontrolreportingtolerancess[0].tolerance_for_time_heating_setpoint_not_met, var_tolerance_for_time_heating_setpoint_not_met)
        self.assertAlmostEqual(idf2.outputcontrolreportingtolerancess[0].tolerance_for_time_cooling_setpoint_not_met, var_tolerance_for_time_cooling_setpoint_not_met)