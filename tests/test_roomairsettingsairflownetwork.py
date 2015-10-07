import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirSettingsAirflowNetwork

log = logging.getLogger(__name__)

class TestRoomAirSettingsAirflowNetwork(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairsettingsairflownetwork(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirSettingsAirflowNetwork()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_control_point_roomairflownetworknode_name = "object-list|Control Point RoomAirflowNetwork:Node Name"
        obj.control_point_roomairflownetworknode_name = var_control_point_roomairflownetworknode_name
        paras = []
        var_roomairflownetworknode_name_1 = "object-list|RoomAirflowNetwork:Node Name 1"
        paras.append(var_roomairflownetworknode_name_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairsettingsairflownetworks[0].name, var_name)
        self.assertEqual(idf2.roomairsettingsairflownetworks[0].zone_name, var_zone_name)
        self.assertEqual(idf2.roomairsettingsairflownetworks[0].control_point_roomairflownetworknode_name, var_control_point_roomairflownetworknode_name)
        index = obj.extensible_field_index("RoomAirflowNetwork:Node Name 1")
        self.assertEqual(idf2.roomairsettingsairflownetworks[0].extensibles[0][index], var_roomairflownetworknode_name_1)