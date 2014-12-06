import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_airflow import ZoneInfiltrationFlowCoefficient

log = logging.getLogger(__name__)

class TestZoneInfiltrationFlowCoefficient(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneinfiltrationflowcoefficient(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneInfiltrationFlowCoefficient()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # real
        var_flow_coefficient = 0.0001
        obj.flow_coefficient = var_flow_coefficient
        # real
        var_stack_coefficient = 0.0001
        obj.stack_coefficient = var_stack_coefficient
        # real
        var_pressure_exponent = 0.0001
        obj.pressure_exponent = var_pressure_exponent
        # real
        var_wind_coefficient = 0.0001
        obj.wind_coefficient = var_wind_coefficient
        # real
        var_shelter_factor = 0.0001
        obj.shelter_factor = var_shelter_factor

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneinfiltrationflowcoefficients[0].name, var_name)
        self.assertEqual(idf2.zoneinfiltrationflowcoefficients[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zoneinfiltrationflowcoefficients[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.zoneinfiltrationflowcoefficients[0].flow_coefficient, var_flow_coefficient)
        self.assertAlmostEqual(idf2.zoneinfiltrationflowcoefficients[0].stack_coefficient, var_stack_coefficient)
        self.assertAlmostEqual(idf2.zoneinfiltrationflowcoefficients[0].pressure_exponent, var_pressure_exponent)
        self.assertAlmostEqual(idf2.zoneinfiltrationflowcoefficients[0].wind_coefficient, var_wind_coefficient)
        self.assertAlmostEqual(idf2.zoneinfiltrationflowcoefficients[0].shelter_factor, var_shelter_factor)