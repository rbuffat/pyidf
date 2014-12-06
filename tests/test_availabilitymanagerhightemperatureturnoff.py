import os
import tempfile
import unittest
import pyidf
from pyidf.system_availability_managers import AvailabilityManagerHighTemperatureTurnOff
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAvailabilityManagerHighTemperatureTurnOff(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_availabilitymanagerhightemperatureturnoff(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AvailabilityManagerHighTemperatureTurnOff()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_sensor_node_name = "node|Sensor Node Name"
        obj.sensor_node_name = var_sensor_node_name
        # real
        var_temperature = 3.3
        obj.temperature = var_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.availabilitymanagerhightemperatureturnoffs[0].name, var_name)
        self.assertEqual(idf2.availabilitymanagerhightemperatureturnoffs[0].sensor_node_name, var_sensor_node_name)
        self.assertAlmostEqual(idf2.availabilitymanagerhightemperatureturnoffs[0].temperature, var_temperature)