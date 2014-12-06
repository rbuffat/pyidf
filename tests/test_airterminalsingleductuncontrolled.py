import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalSingleDuctUncontrolled
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirTerminalSingleDuctUncontrolled(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminalsingleductuncontrolled(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalSingleDuctUncontrolled()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_zone_supply_air_node_name = "node|Zone Supply Air Node Name"
        obj.zone_supply_air_node_name = var_zone_supply_air_node_name
        # real
        var_maximum_air_flow_rate = 0.0
        obj.maximum_air_flow_rate = var_maximum_air_flow_rate

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airterminalsingleductuncontrolleds[0].name, var_name)
        self.assertEqual(idf2.airterminalsingleductuncontrolleds[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airterminalsingleductuncontrolleds[0].zone_supply_air_node_name, var_zone_supply_air_node_name)
        self.assertAlmostEqual(idf2.airterminalsingleductuncontrolleds[0].maximum_air_flow_rate, var_maximum_air_flow_rate)