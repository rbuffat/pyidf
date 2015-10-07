import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.room_air_models import RoomAirNodeAirflowNetworkHvacequipment

log = logging.getLogger(__name__)

class TestRoomAirNodeAirflowNetworkHvacequipment(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roomairnodeairflownetworkhvacequipment(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoomAirNodeAirflowNetworkHvacequipment()
        # Alpha
        var_name = "Alpha|Name"
        obj.name = var_name
        paras = []
        var_zonehvac_or_air_terminal_equipment_object_type_1 = "ZoneHVAC:TerminalUnit:VariableRefrigerantFlow"
        paras.append(var_zonehvac_or_air_terminal_equipment_object_type_1)
        var_zonehvac_or_air_terminal_equipment_object_name_1 = "ZoneHVAC or Air Terminal Equipment Object Name 1"
        paras.append(var_zonehvac_or_air_terminal_equipment_object_name_1)
        var_fraction_of_output_or_supply_air_from_hvac_equipment_1 = 0.5
        paras.append(var_fraction_of_output_or_supply_air_from_hvac_equipment_1)
        var_fraction_of_input_or_return_air_to_hvac_equipment_1 = 0.5
        paras.append(var_fraction_of_input_or_return_air_to_hvac_equipment_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roomairnodeairflownetworkhvacequipments[0].name, var_name)
        index = obj.extensible_field_index("ZoneHVAC or Air Terminal Equipment Object Type 1")
        self.assertEqual(idf2.roomairnodeairflownetworkhvacequipments[0].extensibles[0][index], var_zonehvac_or_air_terminal_equipment_object_type_1)
        index = obj.extensible_field_index("ZoneHVAC or Air Terminal Equipment Object Name 1")
        self.assertEqual(idf2.roomairnodeairflownetworkhvacequipments[0].extensibles[0][index], var_zonehvac_or_air_terminal_equipment_object_name_1)
        index = obj.extensible_field_index("Fraction of Output or Supply Air from HVAC Equipment 1")
        self.assertAlmostEqual(idf2.roomairnodeairflownetworkhvacequipments[0].extensibles[0][index], var_fraction_of_output_or_supply_air_from_hvac_equipment_1)
        index = obj.extensible_field_index("Fraction of Input or Return Air to HVAC Equipment 1")
        self.assertAlmostEqual(idf2.roomairnodeairflownetworkhvacequipments[0].extensibles[0][index], var_fraction_of_input_or_return_air_to_hvac_equipment_1)