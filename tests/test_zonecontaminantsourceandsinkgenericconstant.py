import os
import tempfile
import unittest
import pyidf
from pyidf.internal_gains import ZoneContaminantSourceAndSinkGenericConstant
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneContaminantSourceAndSinkGenericConstant(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontaminantsourceandsinkgenericconstant(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneContaminantSourceAndSinkGenericConstant()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_design_generation_rate = 0.0
        obj.design_generation_rate = var_design_generation_rate
        # object-list
        var_generation_schedule_name = "object-list|Generation Schedule Name"
        obj.generation_schedule_name = var_generation_schedule_name
        # real
        var_design_removal_coefficient = 0.0
        obj.design_removal_coefficient = var_design_removal_coefficient
        # object-list
        var_removal_schedule_name = "object-list|Removal Schedule Name"
        obj.removal_schedule_name = var_removal_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericconstants[0].name, var_name)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericconstants[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.zonecontaminantsourceandsinkgenericconstants[0].design_generation_rate, var_design_generation_rate)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericconstants[0].generation_schedule_name, var_generation_schedule_name)
        self.assertAlmostEqual(idf2.zonecontaminantsourceandsinkgenericconstants[0].design_removal_coefficient, var_design_removal_coefficient)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericconstants[0].removal_schedule_name, var_removal_schedule_name)