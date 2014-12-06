import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_equipment_connections import ZoneHvacEquipmentList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacEquipmentList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacequipmentlist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacEquipmentList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_zone_equipment_1_object_type = "ZoneHVAC:TerminalUnit:VariableRefrigerantFlow"
        paras.append(var_zone_equipment_1_object_type)
        var_zone_equipment_1_name = "Zone Equipment 1 Name"
        paras.append(var_zone_equipment_1_name)
        var_zone_equipment_1_cooling_sequence = 1
        paras.append(var_zone_equipment_1_cooling_sequence)
        var_zone_equipment_1_heating_or_noload_sequence = 1
        paras.append(var_zone_equipment_1_heating_or_noload_sequence)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacequipmentlists[0].name, var_name)
        index = obj.extensible_field_index("Zone Equipment 1 Object Type")
        self.assertEqual(idf2.zonehvacequipmentlists[0].extensibles[0][index], var_zone_equipment_1_object_type)
        index = obj.extensible_field_index("Zone Equipment 1 Name")
        self.assertEqual(idf2.zonehvacequipmentlists[0].extensibles[0][index], var_zone_equipment_1_name)
        index = obj.extensible_field_index("Zone Equipment 1 Cooling Sequence")
        self.assertEqual(idf2.zonehvacequipmentlists[0].extensibles[0][index], var_zone_equipment_1_cooling_sequence)
        index = obj.extensible_field_index("Zone Equipment 1 Heating or No-Load Sequence")
        self.assertEqual(idf2.zonehvacequipmentlists[0].extensibles[0][index], var_zone_equipment_1_heating_or_noload_sequence)