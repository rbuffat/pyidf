import os
import tempfile
import unittest
import pyidf
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkDistributionComponentTerminalUnit
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirflowNetworkDistributionComponentTerminalUnit(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkdistributioncomponentterminalunit(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkDistributionComponentTerminalUnit()
        # object-list
        var_terminal_unit_name = "object-list|Terminal Unit Name"
        obj.terminal_unit_name = var_terminal_unit_name
        # alpha
        var_terminal_unit_object_type = "AirTerminal:SingleDuct:ConstantVolume:Reheat"
        obj.terminal_unit_object_type = var_terminal_unit_object_type
        # real
        var_air_path_length = 0.0001
        obj.air_path_length = var_air_path_length
        # real
        var_air_path_hydraulic_diameter = 0.0001
        obj.air_path_hydraulic_diameter = var_air_path_hydraulic_diameter

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkdistributioncomponentterminalunits[0].terminal_unit_name, var_terminal_unit_name)
        self.assertEqual(idf2.airflownetworkdistributioncomponentterminalunits[0].terminal_unit_object_type, var_terminal_unit_object_type)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentterminalunits[0].air_path_length, var_air_path_length)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentterminalunits[0].air_path_hydraulic_diameter, var_air_path_hydraulic_diameter)