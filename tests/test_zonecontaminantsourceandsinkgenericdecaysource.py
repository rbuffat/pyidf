import os
import tempfile
import unittest
import pyidf
from pyidf.internal_gains import ZoneContaminantSourceAndSinkGenericDecaySource
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneContaminantSourceAndSinkGenericDecaySource(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontaminantsourceandsinkgenericdecaysource(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneContaminantSourceAndSinkGenericDecaySource()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_initial_emission_rate = 0.0
        obj.initial_emission_rate = var_initial_emission_rate
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # real
        var_delay_time_constant = 0.0001
        obj.delay_time_constant = var_delay_time_constant

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericdecaysources[0].name, var_name)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericdecaysources[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.zonecontaminantsourceandsinkgenericdecaysources[0].initial_emission_rate, var_initial_emission_rate)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericdecaysources[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.zonecontaminantsourceandsinkgenericdecaysources[0].delay_time_constant, var_delay_time_constant)