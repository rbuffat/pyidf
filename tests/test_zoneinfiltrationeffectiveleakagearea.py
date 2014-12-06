import os
import tempfile
import unittest
import pyidf
from pyidf.zone_airflow import ZoneInfiltrationEffectiveLeakageArea
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneInfiltrationEffectiveLeakageArea(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneinfiltrationeffectiveleakagearea(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneInfiltrationEffectiveLeakageArea()
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
        var_effective_air_leakage_area = 0.0001
        obj.effective_air_leakage_area = var_effective_air_leakage_area
        # real
        var_stack_coefficient = 0.0001
        obj.stack_coefficient = var_stack_coefficient
        # real
        var_wind_coefficient = 0.0001
        obj.wind_coefficient = var_wind_coefficient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneinfiltrationeffectiveleakageareas[0].name, var_name)
        self.assertEqual(idf2.zoneinfiltrationeffectiveleakageareas[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zoneinfiltrationeffectiveleakageareas[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.zoneinfiltrationeffectiveleakageareas[0].effective_air_leakage_area, var_effective_air_leakage_area)
        self.assertAlmostEqual(idf2.zoneinfiltrationeffectiveleakageareas[0].stack_coefficient, var_stack_coefficient)
        self.assertAlmostEqual(idf2.zoneinfiltrationeffectiveleakageareas[0].wind_coefficient, var_wind_coefficient)