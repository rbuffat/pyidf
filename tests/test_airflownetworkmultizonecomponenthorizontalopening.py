import os
import tempfile
import unittest
import pyidf
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneComponentHorizontalOpening
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirflowNetworkMultiZoneComponentHorizontalOpening(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonecomponenthorizontalopening(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneComponentHorizontalOpening()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_air_mass_flow_coefficient_when_opening_is_closed = 0.0001
        obj.air_mass_flow_coefficient_when_opening_is_closed = var_air_mass_flow_coefficient_when_opening_is_closed
        # real
        var_air_mass_flow_exponent_when_opening_is_closed = 0.75
        obj.air_mass_flow_exponent_when_opening_is_closed = var_air_mass_flow_exponent_when_opening_is_closed
        # real
        var_sloping_plane_angle = 45.00005
        obj.sloping_plane_angle = var_sloping_plane_angle
        # real
        var_discharge_coefficient = 0.0001
        obj.discharge_coefficient = var_discharge_coefficient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonecomponenthorizontalopenings[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponenthorizontalopenings[0].air_mass_flow_coefficient_when_opening_is_closed, var_air_mass_flow_coefficient_when_opening_is_closed)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponenthorizontalopenings[0].air_mass_flow_exponent_when_opening_is_closed, var_air_mass_flow_exponent_when_opening_is_closed)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponenthorizontalopenings[0].sloping_plane_angle, var_sloping_plane_angle)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponenthorizontalopenings[0].discharge_coefficient, var_discharge_coefficient)