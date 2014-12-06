import os
import tempfile
import unittest
import pyidf
from pyidf.internal_gains import ZoneContaminantSourceAndSinkGenericCutoffModel
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneContaminantSourceAndSinkGenericCutoffModel(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecontaminantsourceandsinkgenericcutoffmodel(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneContaminantSourceAndSinkGenericCutoffModel()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_design_generation_rate_coefficient = 0.0
        obj.design_generation_rate_coefficient = var_design_generation_rate_coefficient
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # real
        var_cutoff_generic_contaminant_at_which_emission_ceases = 0.0001
        obj.cutoff_generic_contaminant_at_which_emission_ceases = var_cutoff_generic_contaminant_at_which_emission_ceases

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericcutoffmodels[0].name, var_name)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericcutoffmodels[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.zonecontaminantsourceandsinkgenericcutoffmodels[0].design_generation_rate_coefficient, var_design_generation_rate_coefficient)
        self.assertEqual(idf2.zonecontaminantsourceandsinkgenericcutoffmodels[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.zonecontaminantsourceandsinkgenericcutoffmodels[0].cutoff_generic_contaminant_at_which_emission_ceases, var_cutoff_generic_contaminant_at_which_emission_ceases)