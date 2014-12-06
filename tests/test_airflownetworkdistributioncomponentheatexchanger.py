import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkDistributionComponentHeatExchanger

log = logging.getLogger(__name__)

class TestAirflowNetworkDistributionComponentHeatExchanger(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkdistributioncomponentheatexchanger(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkDistributionComponentHeatExchanger()
        # object-list
        var_heatexchanger_name = "object-list|HeatExchanger Name"
        obj.heatexchanger_name = var_heatexchanger_name
        # alpha
        var_heatexchanger_object_type = "HeatExchanger:AirToAir:FlatPlate"
        obj.heatexchanger_object_type = var_heatexchanger_object_type
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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkdistributioncomponentheatexchangers[0].heatexchanger_name, var_heatexchanger_name)
        self.assertEqual(idf2.airflownetworkdistributioncomponentheatexchangers[0].heatexchanger_object_type, var_heatexchanger_object_type)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentheatexchangers[0].air_path_length, var_air_path_length)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentheatexchangers[0].air_path_hydraulic_diameter, var_air_path_hydraulic_diameter)