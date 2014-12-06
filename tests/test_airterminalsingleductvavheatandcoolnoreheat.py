import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalSingleDuctVavHeatAndCoolNoReheat

log = logging.getLogger(__name__)

class TestAirTerminalSingleDuctVavHeatAndCoolNoReheat(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminalsingleductvavheatandcoolnoreheat(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalSingleDuctVavHeatAndCoolNoReheat()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # real
        var_maximum_air_flow_rate = 0.0001
        obj.maximum_air_flow_rate = var_maximum_air_flow_rate
        # real
        var_zone_minimum_air_flow_fraction = 0.5
        obj.zone_minimum_air_flow_fraction = var_zone_minimum_air_flow_fraction

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airterminalsingleductvavheatandcoolnoreheats[0].name, var_name)
        self.assertEqual(idf2.airterminalsingleductvavheatandcoolnoreheats[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airterminalsingleductvavheatandcoolnoreheats[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.airterminalsingleductvavheatandcoolnoreheats[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertAlmostEqual(idf2.airterminalsingleductvavheatandcoolnoreheats[0].maximum_air_flow_rate, var_maximum_air_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductvavheatandcoolnoreheats[0].zone_minimum_air_flow_fraction, var_zone_minimum_air_flow_fraction)