import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirNode

log = logging.getLogger(__name__)

class TestRoomAirNode(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairnode(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirNode()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_node_type = "Inlet"
        obj.node_type = var_node_type
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_height_of_nodal_control_volume_center = 4.4
        obj.height_of_nodal_control_volume_center = var_height_of_nodal_control_volume_center
        # object-list
        var_surface_1_name = "object-list|Surface 1 Name"
        obj.surface_1_name = var_surface_1_name
        # object-list
        var_surface_2_name = "object-list|Surface 2 Name"
        obj.surface_2_name = var_surface_2_name
        # object-list
        var_surface_3_name = "object-list|Surface 3 Name"
        obj.surface_3_name = var_surface_3_name
        # object-list
        var_surface_4_name = "object-list|Surface 4 Name"
        obj.surface_4_name = var_surface_4_name
        # object-list
        var_surface_5_name = "object-list|Surface 5 Name"
        obj.surface_5_name = var_surface_5_name
        # object-list
        var_surface_6_name = "object-list|Surface 6 Name"
        obj.surface_6_name = var_surface_6_name
        # object-list
        var_surface_7_name = "object-list|Surface 7 Name"
        obj.surface_7_name = var_surface_7_name
        # object-list
        var_surface_8_name = "object-list|Surface 8 Name"
        obj.surface_8_name = var_surface_8_name
        # object-list
        var_surface_9_name = "object-list|Surface 9 Name"
        obj.surface_9_name = var_surface_9_name
        # object-list
        var_surface_10_name = "object-list|Surface 10 Name"
        obj.surface_10_name = var_surface_10_name
        # object-list
        var_surface_11_name = "object-list|Surface 11 Name"
        obj.surface_11_name = var_surface_11_name
        # object-list
        var_surface_12_name = "object-list|Surface 12 Name"
        obj.surface_12_name = var_surface_12_name
        # object-list
        var_surface_13_name = "object-list|Surface 13 Name"
        obj.surface_13_name = var_surface_13_name
        # object-list
        var_surface_14_name = "object-list|Surface 14 Name"
        obj.surface_14_name = var_surface_14_name
        # object-list
        var_surface_15_name = "object-list|Surface 15 Name"
        obj.surface_15_name = var_surface_15_name
        # object-list
        var_surface_16_name = "object-list|Surface 16 Name"
        obj.surface_16_name = var_surface_16_name
        # object-list
        var_surface_17_name = "object-list|Surface 17 Name"
        obj.surface_17_name = var_surface_17_name
        # object-list
        var_surface_18_name = "object-list|Surface 18 Name"
        obj.surface_18_name = var_surface_18_name
        # object-list
        var_surface_19_name = "object-list|Surface 19 Name"
        obj.surface_19_name = var_surface_19_name
        # object-list
        var_surface_20_name = "object-list|Surface 20 Name"
        obj.surface_20_name = var_surface_20_name
        # object-list
        var_surface_21_name = "object-list|Surface 21 Name"
        obj.surface_21_name = var_surface_21_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairnodes[0].name, var_name)
        self.assertEqual(idf2.roomairnodes[0].node_type, var_node_type)
        self.assertEqual(idf2.roomairnodes[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.roomairnodes[0].height_of_nodal_control_volume_center, var_height_of_nodal_control_volume_center)
        self.assertEqual(idf2.roomairnodes[0].surface_1_name, var_surface_1_name)
        self.assertEqual(idf2.roomairnodes[0].surface_2_name, var_surface_2_name)
        self.assertEqual(idf2.roomairnodes[0].surface_3_name, var_surface_3_name)
        self.assertEqual(idf2.roomairnodes[0].surface_4_name, var_surface_4_name)
        self.assertEqual(idf2.roomairnodes[0].surface_5_name, var_surface_5_name)
        self.assertEqual(idf2.roomairnodes[0].surface_6_name, var_surface_6_name)
        self.assertEqual(idf2.roomairnodes[0].surface_7_name, var_surface_7_name)
        self.assertEqual(idf2.roomairnodes[0].surface_8_name, var_surface_8_name)
        self.assertEqual(idf2.roomairnodes[0].surface_9_name, var_surface_9_name)
        self.assertEqual(idf2.roomairnodes[0].surface_10_name, var_surface_10_name)
        self.assertEqual(idf2.roomairnodes[0].surface_11_name, var_surface_11_name)
        self.assertEqual(idf2.roomairnodes[0].surface_12_name, var_surface_12_name)
        self.assertEqual(idf2.roomairnodes[0].surface_13_name, var_surface_13_name)
        self.assertEqual(idf2.roomairnodes[0].surface_14_name, var_surface_14_name)
        self.assertEqual(idf2.roomairnodes[0].surface_15_name, var_surface_15_name)
        self.assertEqual(idf2.roomairnodes[0].surface_16_name, var_surface_16_name)
        self.assertEqual(idf2.roomairnodes[0].surface_17_name, var_surface_17_name)
        self.assertEqual(idf2.roomairnodes[0].surface_18_name, var_surface_18_name)
        self.assertEqual(idf2.roomairnodes[0].surface_19_name, var_surface_19_name)
        self.assertEqual(idf2.roomairnodes[0].surface_20_name, var_surface_20_name)
        self.assertEqual(idf2.roomairnodes[0].surface_21_name, var_surface_21_name)