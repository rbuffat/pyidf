import os
import tempfile
import unittest
import pyidf
from pyidf.air_distribution import AirLoopHvacOutdoorAirSystemEquipmentList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirLoopHvacOutdoorAirSystemEquipmentList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacoutdoorairsystemequipmentlist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacOutdoorAirSystemEquipmentList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_component_1_object_type = "Component 1 Object Type"
        obj.component_1_object_type = var_component_1_object_type
        # alpha
        var_component_1_name = "Component 1 Name"
        obj.component_1_name = var_component_1_name
        # alpha
        var_component_2_object_type = "Component 2 Object Type"
        obj.component_2_object_type = var_component_2_object_type
        # alpha
        var_component_2_name = "Component 2 Name"
        obj.component_2_name = var_component_2_name
        # alpha
        var_component_3_object_type = "Component 3 Object Type"
        obj.component_3_object_type = var_component_3_object_type
        # alpha
        var_component_3_name = "Component 3 Name"
        obj.component_3_name = var_component_3_name
        # alpha
        var_component_4_object_type = "Component 4 Object Type"
        obj.component_4_object_type = var_component_4_object_type
        # alpha
        var_component_4_name = "Component 4 Name"
        obj.component_4_name = var_component_4_name
        # alpha
        var_component_5_object_type = "Component 5 Object Type"
        obj.component_5_object_type = var_component_5_object_type
        # alpha
        var_component_5_name = "Component 5 Name"
        obj.component_5_name = var_component_5_name
        # alpha
        var_component_6_object_type = "Component 6 Object Type"
        obj.component_6_object_type = var_component_6_object_type
        # alpha
        var_component_6_name = "Component 6 Name"
        obj.component_6_name = var_component_6_name
        # alpha
        var_component_7_object_type = "Component 7 Object Type"
        obj.component_7_object_type = var_component_7_object_type
        # alpha
        var_component_7_name = "Component 7 Name"
        obj.component_7_name = var_component_7_name
        # alpha
        var_component_8_object_type = "Component 8 Object Type"
        obj.component_8_object_type = var_component_8_object_type
        # alpha
        var_component_8_name = "Component 8 Name"
        obj.component_8_name = var_component_8_name
        # alpha
        var_component_9_object_type = "Component 9 Object Type"
        obj.component_9_object_type = var_component_9_object_type
        # alpha
        var_component_9_name = "Component 9 Name"
        obj.component_9_name = var_component_9_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].name, var_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_1_object_type, var_component_1_object_type)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_1_name, var_component_1_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_2_object_type, var_component_2_object_type)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_2_name, var_component_2_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_3_object_type, var_component_3_object_type)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_3_name, var_component_3_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_4_object_type, var_component_4_object_type)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_4_name, var_component_4_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_5_object_type, var_component_5_object_type)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_5_name, var_component_5_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_6_object_type, var_component_6_object_type)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_6_name, var_component_6_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_7_object_type, var_component_7_object_type)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_7_name, var_component_7_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_8_object_type, var_component_8_object_type)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_8_name, var_component_8_name)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_9_object_type, var_component_9_object_type)
        self.assertEqual(idf2.airloophvacoutdoorairsystemequipmentlists[0].component_9_name, var_component_9_name)