import os
import tempfile
import unittest
import pyidf
from pyidf.internal_gains import SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSurfaceContaminantSourceAndSinkGenericDepositionVelocitySink(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacecontaminantsourceandsinkgenericdepositionvelocitysink(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # real
        var_deposition_velocity = 0.0
        obj.deposition_velocity = var_deposition_velocity
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacecontaminantsourceandsinkgenericdepositionvelocitysinks[0].name, var_name)
        self.assertEqual(idf2.surfacecontaminantsourceandsinkgenericdepositionvelocitysinks[0].surface_name, var_surface_name)
        self.assertAlmostEqual(idf2.surfacecontaminantsourceandsinkgenericdepositionvelocitysinks[0].deposition_velocity, var_deposition_velocity)
        self.assertEqual(idf2.surfacecontaminantsourceandsinkgenericdepositionvelocitysinks[0].schedule_name, var_schedule_name)