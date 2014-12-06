import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.internal_gains import ZoneContaminantSourceAndSinkGenericDepositionRateSink

log = logging.getLogger(__name__)

class TestZoneContaminantSourceAndSinkGenericDepositionRateSink(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontaminantsourceandsinkgenericdepositionratesink(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneContaminantSourceAndSinkGenericDepositionRateSink()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_deposition_rate = 0.0
        obj.deposition_rate = var_deposition_rate
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericdepositionratesinks[0].name, var_name)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericdepositionratesinks[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.zonecontaminantsourceandsinkgenericdepositionratesinks[0].deposition_rate, var_deposition_rate)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericdepositionratesinks[0].schedule_name, var_schedule_name)