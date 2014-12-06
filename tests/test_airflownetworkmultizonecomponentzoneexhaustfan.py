import os
import tempfile
import unittest
import pyidf
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneComponentZoneExhaustFan
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirflowNetworkMultiZoneComponentZoneExhaustFan(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonecomponentzoneexhaustfan(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneComponentZoneExhaustFan()
        # object-list
        var_name = "object-list|Name"
        obj.name = var_name
        # real
        var_air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions = 0.0001
        obj.air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions = var_air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions
        # real
        var_air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off = 0.75
        obj.air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off = var_air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off
        # object-list
        var_reference_crack_conditions = "object-list|Reference Crack Conditions"
        obj.reference_crack_conditions = var_reference_crack_conditions

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonecomponentzoneexhaustfans[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentzoneexhaustfans[0].air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions, var_air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentzoneexhaustfans[0].air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off, var_air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off)
        self.assertEqual(idf2.airflownetworkmultizonecomponentzoneexhaustfans[0].reference_crack_conditions, var_reference_crack_conditions)