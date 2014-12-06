import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.system_availability_managers import AvailabilityManagerDifferentialThermostat

log = logging.getLogger(__name__)

class TestAvailabilityManagerDifferentialThermostat(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_availabilitymanagerdifferentialthermostat(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AvailabilityManagerDifferentialThermostat()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_hot_node_name = "node|Hot Node Name"
        obj.hot_node_name = var_hot_node_name
        # node
        var_cold_node_name = "node|Cold Node Name"
        obj.cold_node_name = var_cold_node_name
        # real
        var_temperature_difference_on_limit = 4.4
        obj.temperature_difference_on_limit = var_temperature_difference_on_limit
        # real
        var_temperature_difference_off_limit = 5.5
        obj.temperature_difference_off_limit = var_temperature_difference_off_limit

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.availabilitymanagerdifferentialthermostats[0].name, var_name)
        self.assertEqual(idf2.availabilitymanagerdifferentialthermostats[0].hot_node_name, var_hot_node_name)
        self.assertEqual(idf2.availabilitymanagerdifferentialthermostats[0].cold_node_name, var_cold_node_name)
        self.assertAlmostEqual(idf2.availabilitymanagerdifferentialthermostats[0].temperature_difference_on_limit, var_temperature_difference_on_limit)
        self.assertAlmostEqual(idf2.availabilitymanagerdifferentialthermostats[0].temperature_difference_off_limit, var_temperature_difference_off_limit)