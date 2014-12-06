import os
import tempfile
import unittest
import pyidf
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneReferenceCrackConditions
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirflowNetworkMultiZoneReferenceCrackConditions(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonereferencecrackconditions(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneReferenceCrackConditions()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_reference_temperature = 2.2
        obj.reference_temperature = var_reference_temperature
        # real
        var_reference_barometric_pressure = 75500.0
        obj.reference_barometric_pressure = var_reference_barometric_pressure
        # real
        var_reference_humidity_ratio = 4.4
        obj.reference_humidity_ratio = var_reference_humidity_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonereferencecrackconditionss[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonereferencecrackconditionss[0].reference_temperature, var_reference_temperature)
        self.assertAlmostEqual(idf2.airflownetworkmultizonereferencecrackconditionss[0].reference_barometric_pressure, var_reference_barometric_pressure)
        self.assertAlmostEqual(idf2.airflownetworkmultizonereferencecrackconditionss[0].reference_humidity_ratio, var_reference_humidity_ratio)