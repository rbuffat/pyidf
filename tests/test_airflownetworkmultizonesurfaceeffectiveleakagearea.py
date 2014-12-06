import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea

log = logging.getLogger(__name__)

class TestAirflowNetworkMultiZoneSurfaceEffectiveLeakageArea(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonesurfaceeffectiveleakagearea(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_effective_leakage_area = 0.0001
        obj.effective_leakage_area = var_effective_leakage_area
        # real
        var_discharge_coefficient = 0.0001
        obj.discharge_coefficient = var_discharge_coefficient
        # real
        var_reference_pressure_difference = 0.0001
        obj.reference_pressure_difference = var_reference_pressure_difference
        # real
        var_air_mass_flow_exponent = 0.75
        obj.air_mass_flow_exponent = var_air_mass_flow_exponent

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonesurfaceeffectiveleakageareas[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfaceeffectiveleakageareas[0].effective_leakage_area, var_effective_leakage_area)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfaceeffectiveleakageareas[0].discharge_coefficient, var_discharge_coefficient)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfaceeffectiveleakageareas[0].reference_pressure_difference, var_reference_pressure_difference)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfaceeffectiveleakageareas[0].air_mass_flow_exponent, var_air_mass_flow_exponent)