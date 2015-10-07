import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.operational_faults import FaultModelFoulingAirFilter

log = logging.getLogger(__name__)

class TestFaultModelFoulingAirFilter(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_faultmodelfoulingairfilter(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FaultModelFoulingAirFilter()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_fan_object_type = "Fan:OnOff"
        obj.fan_object_type = var_fan_object_type
        # object-list
        var_fan_name = "object-list|Fan Name"
        obj.fan_name = var_fan_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_pressure_fraction_schedule_name = "object-list|Pressure Fraction Schedule Name"
        obj.pressure_fraction_schedule_name = var_pressure_fraction_schedule_name
        # object-list
        var_fan_curve_name = "object-list|Fan Curve Name"
        obj.fan_curve_name = var_fan_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.faultmodelfoulingairfilters[0].name, var_name)
        self.assertEqual(idf2.faultmodelfoulingairfilters[0].fan_object_type, var_fan_object_type)
        self.assertEqual(idf2.faultmodelfoulingairfilters[0].fan_name, var_fan_name)
        self.assertEqual(idf2.faultmodelfoulingairfilters[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.faultmodelfoulingairfilters[0].pressure_fraction_schedule_name, var_pressure_fraction_schedule_name)
        self.assertEqual(idf2.faultmodelfoulingairfilters[0].fan_curve_name, var_fan_curve_name)