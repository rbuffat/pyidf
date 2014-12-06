import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkDistributionComponentFan

log = logging.getLogger(__name__)

class TestAirflowNetworkDistributionComponentFan(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkdistributioncomponentfan(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkDistributionComponentFan()
        # object-list
        var_fan_name = "object-list|Fan Name"
        obj.fan_name = var_fan_name
        # alpha
        var_supply_fan_object_type = "Fan:OnOff"
        obj.supply_fan_object_type = var_supply_fan_object_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkdistributioncomponentfans[0].fan_name, var_fan_name)
        self.assertEqual(idf2.airflownetworkdistributioncomponentfans[0].supply_fan_object_type, var_supply_fan_object_type)