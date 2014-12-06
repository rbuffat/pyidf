import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneSurfaceCrack

log = logging.getLogger(__name__)

class TestAirflowNetworkMultiZoneSurfaceCrack(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonesurfacecrack(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneSurfaceCrack()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_air_mass_flow_coefficient_at_reference_conditions = 0.0001
        obj.air_mass_flow_coefficient_at_reference_conditions = var_air_mass_flow_coefficient_at_reference_conditions
        # real
        var_air_mass_flow_exponent = 0.75
        obj.air_mass_flow_exponent = var_air_mass_flow_exponent
        # object-list
        var_reference_crack_conditions = "object-list|Reference Crack Conditions"
        obj.reference_crack_conditions = var_reference_crack_conditions

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonesurfacecracks[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfacecracks[0].air_mass_flow_coefficient_at_reference_conditions, var_air_mass_flow_coefficient_at_reference_conditions)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfacecracks[0].air_mass_flow_exponent, var_air_mass_flow_exponent)
        self.assertEqual(idf2.airflownetworkmultizonesurfacecracks[0].reference_crack_conditions, var_reference_crack_conditions)