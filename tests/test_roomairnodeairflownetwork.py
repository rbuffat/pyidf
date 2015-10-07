import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirNodeAirflowNetwork

log = logging.getLogger(__name__)

class TestRoomAirNodeAirflowNetwork(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairnodeairflownetwork(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirNodeAirflowNetwork()
        # Alpha
        var_name = "Alpha|Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_fraction_of_zone_air_volume = 0.5
        obj.fraction_of_zone_air_volume = var_fraction_of_zone_air_volume
        # object-list
        var_roomairnodeairflownetworkadjacentsurfacelist_name = "object-list|RoomAir:Node:AirflowNetwork:AdjacentSurfaceList Name"
        obj.roomairnodeairflownetworkadjacentsurfacelist_name = var_roomairnodeairflownetworkadjacentsurfacelist_name
        # object-list
        var_roomairnodeairflownetworkinternalgains_name = "object-list|RoomAir:Node:AirflowNetwork:InternalGains Name"
        obj.roomairnodeairflownetworkinternalgains_name = var_roomairnodeairflownetworkinternalgains_name
        # object-list
        var_roomairnodeairflownetworkhvacequipment_name = "object-list|RoomAir:Node:AirflowNetwork:HVACEquipment Name"
        obj.roomairnodeairflownetworkhvacequipment_name = var_roomairnodeairflownetworkhvacequipment_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairnodeairflownetworks[0].name, var_name)
        self.assertEqual(idf2.roomairnodeairflownetworks[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.roomairnodeairflownetworks[0].fraction_of_zone_air_volume, var_fraction_of_zone_air_volume)
        self.assertEqual(idf2.roomairnodeairflownetworks[0].roomairnodeairflownetworkadjacentsurfacelist_name, var_roomairnodeairflownetworkadjacentsurfacelist_name)
        self.assertEqual(idf2.roomairnodeairflownetworks[0].roomairnodeairflownetworkinternalgains_name, var_roomairnodeairflownetworkinternalgains_name)
        self.assertEqual(idf2.roomairnodeairflownetworks[0].roomairnodeairflownetworkhvacequipment_name, var_roomairnodeairflownetworkhvacequipment_name)