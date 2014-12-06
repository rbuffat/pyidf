import os
import tempfile
import unittest
import pyidf
from pyidf.variable_refrigerant_flow_equipment import ZoneTerminalUnitList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneTerminalUnitList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneterminalunitlist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneTerminalUnitList()
        # alpha
        var_zone_terminal_unit_list_name = "Zone Terminal Unit List Name"
        obj.zone_terminal_unit_list_name = var_zone_terminal_unit_list_name
        paras = []
        var_zone_terminal_unit_name_1 = "object-list|Zone Terminal Unit Name 1"
        paras.append(var_zone_terminal_unit_name_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneterminalunitlists[0].zone_terminal_unit_list_name, var_zone_terminal_unit_list_name)
        index = obj.extensible_field_index("Zone Terminal Unit Name 1")
        self.assertEqual(idf2.zoneterminalunitlists[0].extensibles[0][index], var_zone_terminal_unit_name_1)