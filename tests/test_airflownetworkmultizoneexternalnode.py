import os
import tempfile
import unittest
import pyidf
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneExternalNode
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirflowNetworkMultiZoneExternalNode(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizoneexternalnode(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneExternalNode()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_external_node_height = 2.2
        obj.external_node_height = var_external_node_height
        # object-list
        var_wind_pressure_coefficient_values_object_name = "object-list|Wind Pressure Coefficient Values Object Name"
        obj.wind_pressure_coefficient_values_object_name = var_wind_pressure_coefficient_values_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizoneexternalnodes[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizoneexternalnodes[0].external_node_height, var_external_node_height)
        self.assertEqual(idf2.airflownetworkmultizoneexternalnodes[0].wind_pressure_coefficient_values_object_name, var_wind_pressure_coefficient_values_object_name)