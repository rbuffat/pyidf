import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirNodeAirflowNetworkInternalGains

log = logging.getLogger(__name__)

class TestRoomAirNodeAirflowNetworkInternalGains(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairnodeairflownetworkinternalgains(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirNodeAirflowNetworkInternalGains()
        # Alpha
        var_name = "Alpha|Name"
        obj.name = var_name
        paras = []
        var_internal_gain_object_1_type = "People"
        paras.append(var_internal_gain_object_1_type)
        var_internal_gain_object_1_name = "Internal Gain Object 1 Name"
        paras.append(var_internal_gain_object_1_name)
        var_fraction_of_gains_to_node_1 = 0.5
        paras.append(var_fraction_of_gains_to_node_1)
        var_internal_gain_object_2_type = "People"
        paras.append(var_internal_gain_object_2_type)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairnodeairflownetworkinternalgainss[0].name, var_name)
        index = obj.extensible_field_index("Internal Gain Object 1 Type")
        self.assertEqual(idf2.roomairnodeairflownetworkinternalgainss[0].extensibles[0][index], var_internal_gain_object_1_type)
        index = obj.extensible_field_index("Internal Gain Object 1 Name")
        self.assertEqual(idf2.roomairnodeairflownetworkinternalgainss[0].extensibles[0][index], var_internal_gain_object_1_name)
        index = obj.extensible_field_index("Fraction of Gains to Node 1")
        self.assertAlmostEqual(idf2.roomairnodeairflownetworkinternalgainss[0].extensibles[0][index], var_fraction_of_gains_to_node_1)
        index = obj.extensible_field_index("Internal Gain Object 2 Type")
        self.assertEqual(idf2.roomairnodeairflownetworkinternalgainss[0].extensibles[0][index], var_internal_gain_object_2_type)