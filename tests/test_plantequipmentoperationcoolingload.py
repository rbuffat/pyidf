import os
import tempfile
import unittest
import pyidf
from pyidf.plant import PlantEquipmentOperationCoolingLoad
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPlantEquipmentOperationCoolingLoad(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_plantequipmentoperationcoolingload(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PlantEquipmentOperationCoolingLoad()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_load_range_1_lower_limit = 0.0
        obj.load_range_1_lower_limit = var_load_range_1_lower_limit
        # real
        var_load_range_1_upper_limit = 0.0
        obj.load_range_1_upper_limit = var_load_range_1_upper_limit
        # object-list
        var_range_1_equipment_list_name = "object-list|Range 1 Equipment List Name"
        obj.range_1_equipment_list_name = var_range_1_equipment_list_name
        # real
        var_load_range_2_lower_limit = 0.0
        obj.load_range_2_lower_limit = var_load_range_2_lower_limit
        # real
        var_load_range_2_upper_limit = 6.6
        obj.load_range_2_upper_limit = var_load_range_2_upper_limit
        # object-list
        var_range_2_equipment_list_name = "object-list|Range 2 Equipment List Name"
        obj.range_2_equipment_list_name = var_range_2_equipment_list_name
        # real
        var_load_range_3_lower_limit = 0.0
        obj.load_range_3_lower_limit = var_load_range_3_lower_limit
        # real
        var_load_range_3_upper_limit = 0.0
        obj.load_range_3_upper_limit = var_load_range_3_upper_limit
        # object-list
        var_range_3_equipment_list_name = "object-list|Range 3 Equipment List Name"
        obj.range_3_equipment_list_name = var_range_3_equipment_list_name
        # real
        var_load_range_4_lower_limit = 0.0
        obj.load_range_4_lower_limit = var_load_range_4_lower_limit
        # real
        var_load_range_4_upper_limit = 0.0
        obj.load_range_4_upper_limit = var_load_range_4_upper_limit
        # object-list
        var_range_4_equipment_list_name = "object-list|Range 4 Equipment List Name"
        obj.range_4_equipment_list_name = var_range_4_equipment_list_name
        # real
        var_load_range_5_lower_limit = 0.0
        obj.load_range_5_lower_limit = var_load_range_5_lower_limit
        # real
        var_load_range_5_upper_limit = 0.0
        obj.load_range_5_upper_limit = var_load_range_5_upper_limit
        # object-list
        var_range_5_equipment_list_name = "object-list|Range 5 Equipment List Name"
        obj.range_5_equipment_list_name = var_range_5_equipment_list_name
        # real
        var_load_range_6_lower_limit = 0.0
        obj.load_range_6_lower_limit = var_load_range_6_lower_limit
        # real
        var_load_range_6_upper_limit = 0.0
        obj.load_range_6_upper_limit = var_load_range_6_upper_limit
        # object-list
        var_range_6_equipment_list_name = "object-list|Range 6 Equipment List Name"
        obj.range_6_equipment_list_name = var_range_6_equipment_list_name
        # real
        var_load_range_7_lower_limit = 0.0
        obj.load_range_7_lower_limit = var_load_range_7_lower_limit
        # real
        var_load_range_7_upper_limit = 0.0
        obj.load_range_7_upper_limit = var_load_range_7_upper_limit
        # object-list
        var_range_7_equipment_list_name = "object-list|Range 7 Equipment List Name"
        obj.range_7_equipment_list_name = var_range_7_equipment_list_name
        # real
        var_load_range_8_lower_limit = 0.0
        obj.load_range_8_lower_limit = var_load_range_8_lower_limit
        # real
        var_load_range_8_upper_limit = 0.0
        obj.load_range_8_upper_limit = var_load_range_8_upper_limit
        # object-list
        var_range_8_equipment_list_name = "object-list|Range 8 Equipment List Name"
        obj.range_8_equipment_list_name = var_range_8_equipment_list_name
        # real
        var_load_range_9_lower_limit = 0.0
        obj.load_range_9_lower_limit = var_load_range_9_lower_limit
        # real
        var_load_range_9_upper_limit = 0.0
        obj.load_range_9_upper_limit = var_load_range_9_upper_limit
        # object-list
        var_range_9_equipment_list_name = "object-list|Range 9 Equipment List Name"
        obj.range_9_equipment_list_name = var_range_9_equipment_list_name
        # real
        var_load_range_10_lower_limit = 0.0
        obj.load_range_10_lower_limit = var_load_range_10_lower_limit
        # real
        var_load_range_10_upper_limit = 0.0
        obj.load_range_10_upper_limit = var_load_range_10_upper_limit
        # object-list
        var_range_10_equipment_list_name = "object-list|Range 10 Equipment List Name"
        obj.range_10_equipment_list_name = var_range_10_equipment_list_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].name, var_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_1_lower_limit, var_load_range_1_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_1_upper_limit, var_load_range_1_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].range_1_equipment_list_name, var_range_1_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_2_lower_limit, var_load_range_2_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_2_upper_limit, var_load_range_2_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].range_2_equipment_list_name, var_range_2_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_3_lower_limit, var_load_range_3_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_3_upper_limit, var_load_range_3_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].range_3_equipment_list_name, var_range_3_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_4_lower_limit, var_load_range_4_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_4_upper_limit, var_load_range_4_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].range_4_equipment_list_name, var_range_4_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_5_lower_limit, var_load_range_5_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_5_upper_limit, var_load_range_5_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].range_5_equipment_list_name, var_range_5_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_6_lower_limit, var_load_range_6_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_6_upper_limit, var_load_range_6_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].range_6_equipment_list_name, var_range_6_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_7_lower_limit, var_load_range_7_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_7_upper_limit, var_load_range_7_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].range_7_equipment_list_name, var_range_7_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_8_lower_limit, var_load_range_8_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_8_upper_limit, var_load_range_8_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].range_8_equipment_list_name, var_range_8_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_9_lower_limit, var_load_range_9_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_9_upper_limit, var_load_range_9_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].range_9_equipment_list_name, var_range_9_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_10_lower_limit, var_load_range_10_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationcoolingloads[0].load_range_10_upper_limit, var_load_range_10_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationcoolingloads[0].range_10_equipment_list_name, var_range_10_equipment_list_name)