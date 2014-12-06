import os
import tempfile
import unittest
import pyidf
from pyidf.room_air_models import RoomAirModelType
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRoomAirModelType(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairmodeltype(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirModelType()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # alpha
        var_roomair_modeling_type = "Mixing"
        obj.roomair_modeling_type = var_roomair_modeling_type
        # alpha
        var_air_temperature_coupling_strategy = "Direct"
        obj.air_temperature_coupling_strategy = var_air_temperature_coupling_strategy

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairmodeltypes[0].name, var_name)
        self.assertEqual(idf2.roomairmodeltypes[0].zone_name, var_zone_name)
        self.assertEqual(idf2.roomairmodeltypes[0].roomair_modeling_type, var_roomair_modeling_type)
        self.assertEqual(idf2.roomairmodeltypes[0].air_temperature_coupling_strategy, var_air_temperature_coupling_strategy)