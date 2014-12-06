import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneComponentSimpleOpening

log = logging.getLogger(__name__)

class TestAirflowNetworkMultiZoneComponentSimpleOpening(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonecomponentsimpleopening(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneComponentSimpleOpening()
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
        var_minimum_density_difference_for_twoway_flow = 0.0001
        obj.minimum_density_difference_for_twoway_flow = var_minimum_density_difference_for_twoway_flow
        # real
        var_discharge_coefficient = 0.0001
        obj.discharge_coefficient = var_discharge_coefficient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonecomponentsimpleopenings[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentsimpleopenings[0].air_mass_flow_coefficient_when_opening_is_closed, var_air_mass_flow_coefficient_when_opening_is_closed)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentsimpleopenings[0].air_mass_flow_exponent_when_opening_is_closed, var_air_mass_flow_exponent_when_opening_is_closed)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentsimpleopenings[0].minimum_density_difference_for_twoway_flow, var_minimum_density_difference_for_twoway_flow)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentsimpleopenings[0].discharge_coefficient, var_discharge_coefficient)