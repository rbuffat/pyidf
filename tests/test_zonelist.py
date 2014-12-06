import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import ZoneList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonelist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_zone_1_name = "object-list|Zone 1 Name"
        paras.append(var_zone_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonelists[0].name, var_name)
        index = obj.extensible_field_index("Zone 1 Name")
        self.assertEqual(idf2.zonelists[0].extensibles[0][index], var_zone_1_name)