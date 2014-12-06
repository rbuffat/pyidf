import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementSurfaceProps

log = logging.getLogger(__name__)

class TestGroundHeatTransferBasementSurfaceProps(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementsurfaceprops(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementSurfaceProps()
        # real
        var_albedo_surface_albedo_for_no_snow_conditions = 0.5
        obj.albedo_surface_albedo_for_no_snow_conditions = var_albedo_surface_albedo_for_no_snow_conditions
        # real
        var_albedo_surface_albedo_for_snow_conditions = 0.5
        obj.albedo_surface_albedo_for_snow_conditions = var_albedo_surface_albedo_for_snow_conditions
        # real
        var_epsln_surface_emissivity_no_snow = 0.5
        obj.epsln_surface_emissivity_no_snow = var_epsln_surface_emissivity_no_snow
        # real
        var_epsln_surface_emissivity_with_snow = 0.5
        obj.epsln_surface_emissivity_with_snow = var_epsln_surface_emissivity_with_snow
        # real
        var_veght_surface_roughness_no_snow_conditions = 0.0
        obj.veght_surface_roughness_no_snow_conditions = var_veght_surface_roughness_no_snow_conditions
        # real
        var_veght_surface_roughness_snow_conditions = 0.0
        obj.veght_surface_roughness_snow_conditions = var_veght_surface_roughness_snow_conditions
        # alpha
        var_pet_flag_potential_evapotranspiration_on = "TRUE"
        obj.pet_flag_potential_evapotranspiration_on = var_pet_flag_potential_evapotranspiration_on

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferbasementsurfacepropss[0].albedo_surface_albedo_for_no_snow_conditions, var_albedo_surface_albedo_for_no_snow_conditions)
        self.assertAlmostEqual(idf2.groundheattransferbasementsurfacepropss[0].albedo_surface_albedo_for_snow_conditions, var_albedo_surface_albedo_for_snow_conditions)
        self.assertAlmostEqual(idf2.groundheattransferbasementsurfacepropss[0].epsln_surface_emissivity_no_snow, var_epsln_surface_emissivity_no_snow)
        self.assertAlmostEqual(idf2.groundheattransferbasementsurfacepropss[0].epsln_surface_emissivity_with_snow, var_epsln_surface_emissivity_with_snow)
        self.assertAlmostEqual(idf2.groundheattransferbasementsurfacepropss[0].veght_surface_roughness_no_snow_conditions, var_veght_surface_roughness_no_snow_conditions)
        self.assertAlmostEqual(idf2.groundheattransferbasementsurfacepropss[0].veght_surface_roughness_snow_conditions, var_veght_surface_roughness_snow_conditions)
        self.assertEqual(idf2.groundheattransferbasementsurfacepropss[0].pet_flag_potential_evapotranspiration_on, var_pet_flag_potential_evapotranspiration_on)