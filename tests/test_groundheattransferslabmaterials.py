import os
import tempfile
import unittest
import pyidf
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferSlabMaterials
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferSlabMaterials(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferslabmaterials(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferSlabMaterials()
        # real
        var_nmat_number_of_materials = 0.0001
        obj.nmat_number_of_materials = var_nmat_number_of_materials
        # real
        var_albedo_surface_albedo_no_snow = 0.5
        obj.albedo_surface_albedo_no_snow = var_albedo_surface_albedo_no_snow
        # real
        var_albedo_surface_albedo_snow = 0.5
        obj.albedo_surface_albedo_snow = var_albedo_surface_albedo_snow
        # real
        var_epslw_surface_emissivity_no_snow = 0.0001
        obj.epslw_surface_emissivity_no_snow = var_epslw_surface_emissivity_no_snow
        # real
        var_epslw_surface_emissivity_snow = 0.0001
        obj.epslw_surface_emissivity_snow = var_epslw_surface_emissivity_snow
        # real
        var_z0_surface_roughness_no_snow = 0.0001
        obj.z0_surface_roughness_no_snow = var_z0_surface_roughness_no_snow
        # real
        var_z0_surface_roughness_snow = 0.0001
        obj.z0_surface_roughness_snow = var_z0_surface_roughness_snow
        # real
        var_hin_indoor_hconv_downward_flow = 0.0001
        obj.hin_indoor_hconv_downward_flow = var_hin_indoor_hconv_downward_flow
        # real
        var_hin_indoor_hconv_upward = 0.0001
        obj.hin_indoor_hconv_upward = var_hin_indoor_hconv_upward

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferslabmaterialss[0].nmat_number_of_materials, var_nmat_number_of_materials)
        self.assertAlmostEqual(idf2.groundheattransferslabmaterialss[0].albedo_surface_albedo_no_snow, var_albedo_surface_albedo_no_snow)
        self.assertAlmostEqual(idf2.groundheattransferslabmaterialss[0].albedo_surface_albedo_snow, var_albedo_surface_albedo_snow)
        self.assertAlmostEqual(idf2.groundheattransferslabmaterialss[0].epslw_surface_emissivity_no_snow, var_epslw_surface_emissivity_no_snow)
        self.assertAlmostEqual(idf2.groundheattransferslabmaterialss[0].epslw_surface_emissivity_snow, var_epslw_surface_emissivity_snow)
        self.assertAlmostEqual(idf2.groundheattransferslabmaterialss[0].z0_surface_roughness_no_snow, var_z0_surface_roughness_no_snow)
        self.assertAlmostEqual(idf2.groundheattransferslabmaterialss[0].z0_surface_roughness_snow, var_z0_surface_roughness_snow)
        self.assertAlmostEqual(idf2.groundheattransferslabmaterialss[0].hin_indoor_hconv_downward_flow, var_hin_indoor_hconv_downward_flow)
        self.assertAlmostEqual(idf2.groundheattransferslabmaterialss[0].hin_indoor_hconv_upward, var_hin_indoor_hconv_upward)