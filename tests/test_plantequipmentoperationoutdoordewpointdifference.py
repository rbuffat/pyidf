import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant import PlantEquipmentOperationOutdoorDewpointDifference

log = logging.getLogger(__name__)

class TestPlantEquipmentOperationOutdoorDewpointDifference(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_plantequipmentoperationoutdoordewpointdifference(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PlantEquipmentOperationOutdoorDewpointDifference()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_reference_temperature_node_name = "node|Reference Temperature Node Name"
        obj.reference_temperature_node_name = var_reference_temperature_node_name
        # real
        var_dewpoint_temperature_difference_range_1_lower_limit = 25.0
        obj.dewpoint_temperature_difference_range_1_lower_limit = var_dewpoint_temperature_difference_range_1_lower_limit
        # real
        var_dewpoint_temperature_difference_range_1_upper_limit = 25.0
        obj.dewpoint_temperature_difference_range_1_upper_limit = var_dewpoint_temperature_difference_range_1_upper_limit
        # object-list
        var_range_1_equipment_list_name = "object-list|Range 1 Equipment List Name"
        obj.range_1_equipment_list_name = var_range_1_equipment_list_name
        # real
        var_dewpoint_temperature_difference_range_2_lower_limit = 25.0
        obj.dewpoint_temperature_difference_range_2_lower_limit = var_dewpoint_temperature_difference_range_2_lower_limit
        # real
        var_dewpoint_temperature_difference_range_2_upper_limit = 25.0
        obj.dewpoint_temperature_difference_range_2_upper_limit = var_dewpoint_temperature_difference_range_2_upper_limit
        # object-list
        var_range_2_equipment_list_name = "object-list|Range 2 Equipment List Name"
        obj.range_2_equipment_list_name = var_range_2_equipment_list_name
        # real
        var_dewpoint_temperature_difference_range_3_lower_limit = 25.0
        obj.dewpoint_temperature_difference_range_3_lower_limit = var_dewpoint_temperature_difference_range_3_lower_limit
        # real
        var_dewpoint_temperature_difference_range_3_upper_limit = 25.0
        obj.dewpoint_temperature_difference_range_3_upper_limit = var_dewpoint_temperature_difference_range_3_upper_limit
        # object-list
        var_range_3_equipment_list_name = "object-list|Range 3 Equipment List Name"
        obj.range_3_equipment_list_name = var_range_3_equipment_list_name
        # real
        var_dewpoint_temperature_difference_range_4_lower_limit = 25.0
        obj.dewpoint_temperature_difference_range_4_lower_limit = var_dewpoint_temperature_difference_range_4_lower_limit
        # real
        var_dewpoint_temperature_difference_range_4_upper_limit = 25.0
        obj.dewpoint_temperature_difference_range_4_upper_limit = var_dewpoint_temperature_difference_range_4_upper_limit
        # object-list
        var_range_4_equipment_list_name = "object-list|Range 4 Equipment List Name"
        obj.range_4_equipment_list_name = var_range_4_equipment_list_name
        # real
        var_dewpoint_temperature_difference_range_5_lower_limit = 25.0
        obj.dewpoint_temperature_difference_range_5_lower_limit = var_dewpoint_temperature_difference_range_5_lower_limit
        # real
        var_dewpoint_temperature_difference_range_5_upper_limit = 25.0
        obj.dewpoint_temperature_difference_range_5_upper_limit = var_dewpoint_temperature_difference_range_5_upper_limit
        # object-list
        var_range_5_equipment_list_name = "object-list|Range 5 Equipment List Name"
        obj.range_5_equipment_list_name = var_range_5_equipment_list_name
        # real
        var_dewpoint_temperature_difference_range_6_lower_limit = 25.0
        obj.dewpoint_temperature_difference_range_6_lower_limit = var_dewpoint_temperature_difference_range_6_lower_limit
        # real
        var_dewpoint_temperature_difference_range_6_upper_limit = 25.0
        obj.dewpoint_temperature_difference_range_6_upper_limit = var_dewpoint_temperature_difference_range_6_upper_limit
        # object-list
        var_range_6_equipment_list_name = "object-list|Range 6 Equipment List Name"
        obj.range_6_equipment_list_name = var_range_6_equipment_list_name
        # real
        var_dewpoint_temperature_difference_range_7_lower_limit = 25.0
        obj.dewpoint_temperature_difference_range_7_lower_limit = var_dewpoint_temperature_difference_range_7_lower_limit
        # real
        var_dewpoint_temperature_difference_range_7_upper_limit = 25.0
        obj.dewpoint_temperature_difference_range_7_upper_limit = var_dewpoint_temperature_difference_range_7_upper_limit
        # object-list
        var_range_7_equipment_list_name = "object-list|Range 7 Equipment List Name"
        obj.range_7_equipment_list_name = var_range_7_equipment_list_name
        # real
        var_dewpoint_temperature_difference_range_8_lower_limit = 25.0
        obj.dewpoint_temperature_difference_range_8_lower_limit = var_dewpoint_temperature_difference_range_8_lower_limit
        # real
        var_dewpoint_temperature_difference_range_8_upper_limit = 25.0
        obj.dewpoint_temperature_difference_range_8_upper_limit = var_dewpoint_temperature_difference_range_8_upper_limit
        # object-list
        var_range_8_equipment_list_name = "object-list|Range 8 Equipment List Name"
        obj.range_8_equipment_list_name = var_range_8_equipment_list_name
        # real
        var_dewpoint_temperature_difference_range_9_lower_limit = 25.0
        obj.dewpoint_temperature_difference_range_9_lower_limit = var_dewpoint_temperature_difference_range_9_lower_limit
        # real
        var_dewpoint_temperature_difference_range_9_upper_limit = 25.0
        obj.dewpoint_temperature_difference_range_9_upper_limit = var_dewpoint_temperature_difference_range_9_upper_limit
        # object-list
        var_range_9_equipment_list_name = "object-list|Range 9 Equipment List Name"
        obj.range_9_equipment_list_name = var_range_9_equipment_list_name
        # real
        var_dewpoint_temperature_difference_range_10_lower_limit = 25.0
        obj.dewpoint_temperature_difference_range_10_lower_limit = var_dewpoint_temperature_difference_range_10_lower_limit
        # real
        var_dewpoint_temperature_difference_range_10_upper_limit = 25.0
        obj.dewpoint_temperature_difference_range_10_upper_limit = var_dewpoint_temperature_difference_range_10_upper_limit
        # object-list
        var_range_10_equipment_list_name = "object-list|Range 10 Equipment List Name"
        obj.range_10_equipment_list_name = var_range_10_equipment_list_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].name, var_name)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].reference_temperature_node_name, var_reference_temperature_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_1_lower_limit, var_dewpoint_temperature_difference_range_1_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_1_upper_limit, var_dewpoint_temperature_difference_range_1_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].range_1_equipment_list_name, var_range_1_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_2_lower_limit, var_dewpoint_temperature_difference_range_2_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_2_upper_limit, var_dewpoint_temperature_difference_range_2_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].range_2_equipment_list_name, var_range_2_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_3_lower_limit, var_dewpoint_temperature_difference_range_3_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_3_upper_limit, var_dewpoint_temperature_difference_range_3_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].range_3_equipment_list_name, var_range_3_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_4_lower_limit, var_dewpoint_temperature_difference_range_4_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_4_upper_limit, var_dewpoint_temperature_difference_range_4_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].range_4_equipment_list_name, var_range_4_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_5_lower_limit, var_dewpoint_temperature_difference_range_5_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_5_upper_limit, var_dewpoint_temperature_difference_range_5_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].range_5_equipment_list_name, var_range_5_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_6_lower_limit, var_dewpoint_temperature_difference_range_6_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_6_upper_limit, var_dewpoint_temperature_difference_range_6_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].range_6_equipment_list_name, var_range_6_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_7_lower_limit, var_dewpoint_temperature_difference_range_7_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_7_upper_limit, var_dewpoint_temperature_difference_range_7_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].range_7_equipment_list_name, var_range_7_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_8_lower_limit, var_dewpoint_temperature_difference_range_8_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_8_upper_limit, var_dewpoint_temperature_difference_range_8_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].range_8_equipment_list_name, var_range_8_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_9_lower_limit, var_dewpoint_temperature_difference_range_9_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_9_upper_limit, var_dewpoint_temperature_difference_range_9_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].range_9_equipment_list_name, var_range_9_equipment_list_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_10_lower_limit, var_dewpoint_temperature_difference_range_10_lower_limit)
        self.assertAlmostEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].dewpoint_temperature_difference_range_10_upper_limit, var_dewpoint_temperature_difference_range_10_upper_limit)
        self.assertEqual(idf2.plantequipmentoperationoutdoordewpointdifferences[0].range_10_equipment_list_name, var_range_10_equipment_list_name)