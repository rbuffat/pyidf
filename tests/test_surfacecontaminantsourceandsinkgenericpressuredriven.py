import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.internal_gains import SurfaceContaminantSourceAndSinkGenericPressureDriven

log = logging.getLogger(__name__)

class TestSurfaceContaminantSourceAndSinkGenericPressureDriven(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacecontaminantsourceandsinkgenericpressuredriven(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfaceContaminantSourceAndSinkGenericPressureDriven()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # real
        var_design_generation_rate_coefficient = 0.0
        obj.design_generation_rate_coefficient = var_design_generation_rate_coefficient
        # object-list
        var_generation_schedule_name = "object-list|Generation Schedule Name"
        obj.generation_schedule_name = var_generation_schedule_name
        # real
        var_generation_exponent = 0.50005
        obj.generation_exponent = var_generation_exponent

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacecontaminantsourceandsinkgenericpressuredrivens[0].name, var_name)
        self.assertEqual(idf2.surfacecontaminantsourceandsinkgenericpressuredrivens[0].surface_name, var_surface_name)
        self.assertAlmostEqual(idf2.surfacecontaminantsourceandsinkgenericpressuredrivens[0].design_generation_rate_coefficient, var_design_generation_rate_coefficient)
        self.assertEqual(idf2.surfacecontaminantsourceandsinkgenericpressuredrivens[0].generation_schedule_name, var_generation_schedule_name)
        self.assertAlmostEqual(idf2.surfacecontaminantsourceandsinkgenericpressuredrivens[0].generation_exponent, var_generation_exponent)