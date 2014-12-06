import os
import tempfile
import unittest
import pyidf
from pyidf.location_and_climate import RoofIrrigation
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRoofIrrigation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_roofirrigation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RoofIrrigation()
        # alpha
        var_irrigation_model_type = "Schedule"
        obj.irrigation_model_type = var_irrigation_model_type
        # object-list
        var_irrigation_rate_schedule_name = "object-list|Irrigation Rate Schedule Name"
        obj.irrigation_rate_schedule_name = var_irrigation_rate_schedule_name
        # real
        var_irrigation_maximum_saturation_threshold = 50.0
        obj.irrigation_maximum_saturation_threshold = var_irrigation_maximum_saturation_threshold

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.roofirrigations[0].irrigation_model_type, var_irrigation_model_type)
        self.assertEqual(idf2.roofirrigations[0].irrigation_rate_schedule_name, var_irrigation_rate_schedule_name)
        self.assertAlmostEqual(idf2.roofirrigations[0].irrigation_maximum_saturation_threshold, var_irrigation_maximum_saturation_threshold)