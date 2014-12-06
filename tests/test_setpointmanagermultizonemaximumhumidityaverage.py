import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.setpoint_managers import SetpointManagerMultiZoneMaximumHumidityAverage

log = logging.getLogger(__name__)

class TestSetpointManagerMultiZoneMaximumHumidityAverage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagermultizonemaximumhumidityaverage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerMultiZoneMaximumHumidityAverage()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_hvac_air_loop_name = "object-list|HVAC Air Loop Name"
        obj.hvac_air_loop_name = var_hvac_air_loop_name
        # real
        var_minimum_setpoint_humidity_ratio = 0.0001
        obj.minimum_setpoint_humidity_ratio = var_minimum_setpoint_humidity_ratio
        # real
        var_maximum_setpoint_humidity_ratio = 0.0001
        obj.maximum_setpoint_humidity_ratio = var_maximum_setpoint_humidity_ratio
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
        self.assertEqual(idf2.setpointmanagermultizonemaximumhumidityaverages[0].name, var_name)
        self.assertEqual(idf2.setpointmanagermultizonemaximumhumidityaverages[0].hvac_air_loop_name, var_hvac_air_loop_name)
        self.assertAlmostEqual(idf2.setpointmanagermultizonemaximumhumidityaverages[0].minimum_setpoint_humidity_ratio, var_minimum_setpoint_humidity_ratio)
        self.assertAlmostEqual(idf2.setpointmanagermultizonemaximumhumidityaverages[0].maximum_setpoint_humidity_ratio, var_maximum_setpoint_humidity_ratio)
        self.assertEqual(idf2.setpointmanagermultizonemaximumhumidityaverages[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)