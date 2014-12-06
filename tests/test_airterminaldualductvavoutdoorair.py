import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalDualDuctVavOutdoorAir

log = logging.getLogger(__name__)

class TestAirTerminalDualDuctVavOutdoorAir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminaldualductvavoutdoorair(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalDualDuctVavOutdoorAir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_air_outlet_node_name = "Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # node
        var_outdoor_air_inlet_node_name = "node|Outdoor Air Inlet Node Name"
        obj.outdoor_air_inlet_node_name = var_outdoor_air_inlet_node_name
        # node
        var_recirculated_air_inlet_node_name = "node|Recirculated Air Inlet Node Name"
        obj.recirculated_air_inlet_node_name = var_recirculated_air_inlet_node_name
        # real
        var_maximum_terminal_air_flow_rate = 0.0
        obj.maximum_terminal_air_flow_rate = var_maximum_terminal_air_flow_rate
        # object-list
        var_design_specification_outdoor_air_object_name = "object-list|Design Specification Outdoor Air Object Name"
        obj.design_specification_outdoor_air_object_name = var_design_specification_outdoor_air_object_name
        # alpha
        var_per_person_ventilation_rate_mode = "CurrentOccupancy"
        obj.per_person_ventilation_rate_mode = var_per_person_ventilation_rate_mode

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airterminaldualductvavoutdoorairs[0].name, var_name)
        self.assertEqual(idf2.airterminaldualductvavoutdoorairs[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airterminaldualductvavoutdoorairs[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.airterminaldualductvavoutdoorairs[0].outdoor_air_inlet_node_name, var_outdoor_air_inlet_node_name)
        self.assertEqual(idf2.airterminaldualductvavoutdoorairs[0].recirculated_air_inlet_node_name, var_recirculated_air_inlet_node_name)
        self.assertAlmostEqual(idf2.airterminaldualductvavoutdoorairs[0].maximum_terminal_air_flow_rate, var_maximum_terminal_air_flow_rate)
        self.assertEqual(idf2.airterminaldualductvavoutdoorairs[0].design_specification_outdoor_air_object_name, var_design_specification_outdoor_air_object_name)
        self.assertEqual(idf2.airterminaldualductvavoutdoorairs[0].per_person_ventilation_rate_mode, var_per_person_ventilation_rate_mode)