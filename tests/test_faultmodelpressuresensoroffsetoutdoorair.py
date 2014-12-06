import os
import tempfile
import unittest
import pyidf
from pyidf.operational_faults import FaultModelPressureSensorOffsetOutdoorAir
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestFaultModelPressureSensorOffsetOutdoorAir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_faultmodelpressuresensoroffsetoutdoorair(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FaultModelPressureSensorOffsetOutdoorAir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_severity_schedule_name = "object-list|Severity Schedule Name"
        obj.severity_schedule_name = var_severity_schedule_name
        # alpha
        var_controller_object_type = "Controller:OutdoorAir"
        obj.controller_object_type = var_controller_object_type
        # object-list
        var_controller_object_name = "object-list|Controller Object Name"
        obj.controller_object_name = var_controller_object_name
        # real
        var_pressure_sensor_offset = 0.0
        obj.pressure_sensor_offset = var_pressure_sensor_offset

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.faultmodelpressuresensoroffsetoutdoorairs[0].name, var_name)
        self.assertEqual(idf2.faultmodelpressuresensoroffsetoutdoorairs[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.faultmodelpressuresensoroffsetoutdoorairs[0].severity_schedule_name, var_severity_schedule_name)
        self.assertEqual(idf2.faultmodelpressuresensoroffsetoutdoorairs[0].controller_object_type, var_controller_object_type)
        self.assertEqual(idf2.faultmodelpressuresensoroffsetoutdoorairs[0].controller_object_name, var_controller_object_name)
        self.assertAlmostEqual(idf2.faultmodelpressuresensoroffsetoutdoorairs[0].pressure_sensor_offset, var_pressure_sensor_offset)