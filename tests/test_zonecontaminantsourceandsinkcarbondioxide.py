import os
import tempfile
import unittest
import pyidf
from pyidf.internal_gains import ZoneContaminantSourceAndSinkCarbonDioxide
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneContaminantSourceAndSinkCarbonDioxide(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontaminantsourceandsinkcarbondioxide(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneContaminantSourceAndSinkCarbonDioxide()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_design_generation_rate = 3.3
        obj.design_generation_rate = var_design_generation_rate
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontaminantsourceandsinkcarbondioxides[0].name, var_name)
        self.assertEqual(idf2.zonecontaminantsourceandsinkcarbondioxides[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.zonecontaminantsourceandsinkcarbondioxides[0].design_generation_rate, var_design_generation_rate)
        self.assertEqual(idf2.zonecontaminantsourceandsinkcarbondioxides[0].schedule_name, var_schedule_name)