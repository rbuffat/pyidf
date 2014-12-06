import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.setpoint_managers import SetpointManagerOutdoorAirPretreat

log = logging.getLogger(__name__)

class TestSetpointManagerOutdoorAirPretreat(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanageroutdoorairpretreat(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerOutdoorAirPretreat()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # real
        var_minimum_setpoint_temperature = 3.3
        obj.minimum_setpoint_temperature = var_minimum_setpoint_temperature
        # real
        var_maximum_setpoint_temperature = 4.4
        obj.maximum_setpoint_temperature = var_maximum_setpoint_temperature
        # real
        var_minimum_setpoint_humidity_ratio = 1.0
        obj.minimum_setpoint_humidity_ratio = var_minimum_setpoint_humidity_ratio
        # real
        var_maximum_setpoint_humidity_ratio = 1.0
        obj.maximum_setpoint_humidity_ratio = var_maximum_setpoint_humidity_ratio
        # node
        var_reference_setpoint_node_name = "node|Reference Setpoint Node Name"
        obj.reference_setpoint_node_name = var_reference_setpoint_node_name
        # node
        var_mixed_air_stream_node_name = "node|Mixed Air Stream Node Name"
        obj.mixed_air_stream_node_name = var_mixed_air_stream_node_name
        # node
        var_outdoor_air_stream_node_name = "node|Outdoor Air Stream Node Name"
        obj.outdoor_air_stream_node_name = var_outdoor_air_stream_node_name
        # node
        var_return_air_stream_node_name = "node|Return Air Stream Node Name"
        obj.return_air_stream_node_name = var_return_air_stream_node_name
        # node
        var_setpoint_node_or_nodelist_name = "node|Setpoint Node or NodeList Name"
        obj.setpoint_node_or_nodelist_name = var_setpoint_node_or_nodelist_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanageroutdoorairpretreats[0].name, var_name)
        self.assertEqual(idf2.setpointmanageroutdoorairpretreats[0].control_variable, var_control_variable)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairpretreats[0].minimum_setpoint_temperature, var_minimum_setpoint_temperature)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairpretreats[0].maximum_setpoint_temperature, var_maximum_setpoint_temperature)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairpretreats[0].minimum_setpoint_humidity_ratio, var_minimum_setpoint_humidity_ratio)
        self.assertAlmostEqual(idf2.setpointmanageroutdoorairpretreats[0].maximum_setpoint_humidity_ratio, var_maximum_setpoint_humidity_ratio)
        self.assertEqual(idf2.setpointmanageroutdoorairpretreats[0].reference_setpoint_node_name, var_reference_setpoint_node_name)
        self.assertEqual(idf2.setpointmanageroutdoorairpretreats[0].mixed_air_stream_node_name, var_mixed_air_stream_node_name)
        self.assertEqual(idf2.setpointmanageroutdoorairpretreats[0].outdoor_air_stream_node_name, var_outdoor_air_stream_node_name)
        self.assertEqual(idf2.setpointmanageroutdoorairpretreats[0].return_air_stream_node_name, var_return_air_stream_node_name)
        self.assertEqual(idf2.setpointmanageroutdoorairpretreats[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)