import os
import tempfile
import unittest
import pyidf
from pyidf.internal_gains import SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacecontaminantsourceandsinkgenericboundarylayerdiffusion(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # real
        var_mass_transfer_coefficient = 0.0
        obj.mass_transfer_coefficient = var_mass_transfer_coefficient
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # real
        var_henry_adsorption_constant_or_partition_coefficient = 0.0001
        obj.henry_adsorption_constant_or_partition_coefficient = var_henry_adsorption_constant_or_partition_coefficient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacecontaminantsourceandsinkgenericboundarylayerdiffusions[0].name, var_name)
        self.assertEqual(idf2.surfacecontaminantsourceandsinkgenericboundarylayerdiffusions[0].surface_name, var_surface_name)
        self.assertAlmostEqual(idf2.surfacecontaminantsourceandsinkgenericboundarylayerdiffusions[0].mass_transfer_coefficient, var_mass_transfer_coefficient)
        self.assertEqual(idf2.surfacecontaminantsourceandsinkgenericboundarylayerdiffusions[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.surfacecontaminantsourceandsinkgenericboundarylayerdiffusions[0].henry_adsorption_constant_or_partition_coefficient, var_henry_adsorption_constant_or_partition_coefficient)