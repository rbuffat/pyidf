import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.system_availability_managers import AvailabilityManagerLowTemperatureTurnOff

log = logging.getLogger(__name__)

class TestAvailabilityManagerLowTemperatureTurnOff(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_availabilitymanagerlowtemperatureturnoff(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AvailabilityManagerLowTemperatureTurnOff()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_sensor_node_name = "node|Sensor Node Name"
        obj.sensor_node_name = var_sensor_node_name
        # real
        var_temperature = 3.3
        obj.temperature = var_temperature
        # object-list
        var_applicability_schedule_name = "object-list|Applicability Schedule Name"
        obj.applicability_schedule_name = var_applicability_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.availabilitymanagerlowtemperatureturnoffs[0].name, var_name)
        self.assertEqual(idf2.availabilitymanagerlowtemperatureturnoffs[0].sensor_node_name, var_sensor_node_name)
        self.assertAlmostEqual(idf2.availabilitymanagerlowtemperatureturnoffs[0].temperature, var_temperature)
        self.assertEqual(idf2.availabilitymanagerlowtemperatureturnoffs[0].applicability_schedule_name, var_applicability_schedule_name)