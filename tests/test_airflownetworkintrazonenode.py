import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkIntraZoneNode

log = logging.getLogger(__name__)

class TestAirflowNetworkIntraZoneNode(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkintrazonenode(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkIntraZoneNode()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_roomairnodeairflownetwork_name = "RoomAir:Node:AirflowNetwork Name"
        obj.roomairnodeairflownetwork_name = var_roomairnodeairflownetwork_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_node_height = 4.4
        obj.node_height = var_node_height

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkintrazonenodes[0].name, var_name)
        self.assertEqual(idf2.airflownetworkintrazonenodes[0].roomairnodeairflownetwork_name, var_roomairnodeairflownetwork_name)
        self.assertEqual(idf2.airflownetworkintrazonenodes[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.airflownetworkintrazonenodes[0].node_height, var_node_height)