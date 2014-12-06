import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalSingleDuctSupplySideMixer
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirTerminalSingleDuctSupplySideMixer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminalsingleductsupplysidemixer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalSingleDuctSupplySideMixer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_zonehvac_terminal_unit_object_type = "ZoneHVAC Terminal Unit Object Type"
        obj.zonehvac_terminal_unit_object_type = var_zonehvac_terminal_unit_object_type
        # alpha
        var_zonehvac_terminal_unit_name = "ZoneHVAC Terminal Unit Name"
        obj.zonehvac_terminal_unit_name = var_zonehvac_terminal_unit_name
        # alpha
        var_terminal_unit_outlet_node_name = "Terminal Unit Outlet Node Name"
        obj.terminal_unit_outlet_node_name = var_terminal_unit_outlet_node_name
        # alpha
        var_terminal_unit_primary_air_inlet_node_name = "Terminal Unit Primary Air Inlet Node Name"
        obj.terminal_unit_primary_air_inlet_node_name = var_terminal_unit_primary_air_inlet_node_name
        # alpha
        var_terminal_unit_secondary_air_inlet_node_name = "Terminal Unit Secondary Air Inlet Node Name"
        obj.terminal_unit_secondary_air_inlet_node_name = var_terminal_unit_secondary_air_inlet_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airterminalsingleductsupplysidemixers[0].name, var_name)
        self.assertEqual(idf2.airterminalsingleductsupplysidemixers[0].zonehvac_terminal_unit_object_type, var_zonehvac_terminal_unit_object_type)
        self.assertEqual(idf2.airterminalsingleductsupplysidemixers[0].zonehvac_terminal_unit_name, var_zonehvac_terminal_unit_name)
        self.assertEqual(idf2.airterminalsingleductsupplysidemixers[0].terminal_unit_outlet_node_name, var_terminal_unit_outlet_node_name)
        self.assertEqual(idf2.airterminalsingleductsupplysidemixers[0].terminal_unit_primary_air_inlet_node_name, var_terminal_unit_primary_air_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductsupplysidemixers[0].terminal_unit_secondary_air_inlet_node_name, var_terminal_unit_secondary_air_inlet_node_name)