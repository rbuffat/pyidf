import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferSlabMatlProps

log = logging.getLogger(__name__)

class TestGroundHeatTransferSlabMatlProps(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferslabmatlprops(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferSlabMatlProps()
        # real
        var_rho_slab_material_density = 0.0001
        obj.rho_slab_material_density = var_rho_slab_material_density
        # real
        var_rho_soil_density = 0.0001
        obj.rho_soil_density = var_rho_soil_density
        # real
        var_cp_slab_cp = 0.0001
        obj.cp_slab_cp = var_cp_slab_cp
        # real
        var_cp_soil_cp = 0.0001
        obj.cp_soil_cp = var_cp_soil_cp
        # real
        var_tcon_slab_k = 0.0001
        obj.tcon_slab_k = var_tcon_slab_k
        # real
        var_tcon_soil_k = 0.0001
        obj.tcon_soil_k = var_tcon_soil_k

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferslabmatlpropss[0].rho_slab_material_density, var_rho_slab_material_density)
        self.assertAlmostEqual(idf2.groundheattransferslabmatlpropss[0].rho_soil_density, var_rho_soil_density)
        self.assertAlmostEqual(idf2.groundheattransferslabmatlpropss[0].cp_slab_cp, var_cp_slab_cp)
        self.assertAlmostEqual(idf2.groundheattransferslabmatlpropss[0].cp_soil_cp, var_cp_soil_cp)
        self.assertAlmostEqual(idf2.groundheattransferslabmatlpropss[0].tcon_slab_k, var_tcon_slab_k)
        self.assertAlmostEqual(idf2.groundheattransferslabmatlpropss[0].tcon_soil_k, var_tcon_soil_k)