import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirNodeAirflowNetworkAdjacentSurfaceList

log = logging.getLogger(__name__)

class TestRoomAirNodeAirflowNetworkAdjacentSurfaceList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairnodeairflownetworkadjacentsurfacelist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirNodeAirflowNetworkAdjacentSurfaceList()
        # Alpha
        var_name = "Alpha|Name"
        obj.name = var_name
        paras = []
        var_surface_1_name = "object-list|Surface 1 Name"
        paras.append(var_surface_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairnodeairflownetworkadjacentsurfacelists[0].name, var_name)
        index = obj.extensible_field_index("Surface 1 Name")
        self.assertEqual(idf2.roomairnodeairflownetworkadjacentsurfacelists[0].extensibles[0][index], var_surface_1_name)