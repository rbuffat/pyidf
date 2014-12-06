import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementMatlProps

log = logging.getLogger(__name__)

class TestGroundHeatTransferBasementMatlProps(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementmatlprops(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementMatlProps()
        # real
        var_nmat_number_of_materials_in_this_domain = 6.0
        obj.nmat_number_of_materials_in_this_domain = var_nmat_number_of_materials_in_this_domain
        # real
        var_density_for_foundation_wall = 0.0001
        obj.density_for_foundation_wall = var_density_for_foundation_wall
        # real
        var_density_for_floor_slab = 0.0001
        obj.density_for_floor_slab = var_density_for_floor_slab
        # real
        var_density_for_ceiling = 0.0001
        obj.density_for_ceiling = var_density_for_ceiling
        # real
        var_density_for_soil = 0.0001
        obj.density_for_soil = var_density_for_soil
        # real
        var_density_for_gravel = 0.0001
        obj.density_for_gravel = var_density_for_gravel
        # real
        var_density_for_wood = 0.0001
        obj.density_for_wood = var_density_for_wood
        # real
        var_specific_heat_for_foundation_wall = 0.0001
        obj.specific_heat_for_foundation_wall = var_specific_heat_for_foundation_wall
        # real
        var_specific_heat_for_floor_slab = 0.0001
        obj.specific_heat_for_floor_slab = var_specific_heat_for_floor_slab
        # real
        var_specific_heat_for_ceiling = 0.0001
        obj.specific_heat_for_ceiling = var_specific_heat_for_ceiling
        # real
        var_specific_heat_for_soil = 0.0001
        obj.specific_heat_for_soil = var_specific_heat_for_soil
        # real
        var_specific_heat_for_gravel = 0.0001
        obj.specific_heat_for_gravel = var_specific_heat_for_gravel
        # real
        var_specific_heat_for_wood = 0.0001
        obj.specific_heat_for_wood = var_specific_heat_for_wood
        # real
        var_thermal_conductivity_for_foundation_wall = 0.0001
        obj.thermal_conductivity_for_foundation_wall = var_thermal_conductivity_for_foundation_wall
        # real
        var_thermal_conductivity_for_floor_slab = 0.0001
        obj.thermal_conductivity_for_floor_slab = var_thermal_conductivity_for_floor_slab
        # real
        var_thermal_conductivity_for_ceiling = 0.0001
        obj.thermal_conductivity_for_ceiling = var_thermal_conductivity_for_ceiling
        # real
        var_thermal_conductivity_for_soil = 0.0001
        obj.thermal_conductivity_for_soil = var_thermal_conductivity_for_soil
        # real
        var_thermal_conductivity_for_gravel = 0.0001
        obj.thermal_conductivity_for_gravel = var_thermal_conductivity_for_gravel
        # real
        var_thermal_conductivity_for_wood = 0.0001
        obj.thermal_conductivity_for_wood = var_thermal_conductivity_for_wood

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].nmat_number_of_materials_in_this_domain, var_nmat_number_of_materials_in_this_domain)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].density_for_foundation_wall, var_density_for_foundation_wall)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].density_for_floor_slab, var_density_for_floor_slab)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].density_for_ceiling, var_density_for_ceiling)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].density_for_soil, var_density_for_soil)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].density_for_gravel, var_density_for_gravel)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].density_for_wood, var_density_for_wood)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].specific_heat_for_foundation_wall, var_specific_heat_for_foundation_wall)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].specific_heat_for_floor_slab, var_specific_heat_for_floor_slab)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].specific_heat_for_ceiling, var_specific_heat_for_ceiling)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].specific_heat_for_soil, var_specific_heat_for_soil)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].specific_heat_for_gravel, var_specific_heat_for_gravel)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].specific_heat_for_wood, var_specific_heat_for_wood)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].thermal_conductivity_for_foundation_wall, var_thermal_conductivity_for_foundation_wall)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].thermal_conductivity_for_floor_slab, var_thermal_conductivity_for_floor_slab)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].thermal_conductivity_for_ceiling, var_thermal_conductivity_for_ceiling)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].thermal_conductivity_for_soil, var_thermal_conductivity_for_soil)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].thermal_conductivity_for_gravel, var_thermal_conductivity_for_gravel)
        self.assertAlmostEqual(idf2.groundheattransferbasementmatlpropss[0].thermal_conductivity_for_wood, var_thermal_conductivity_for_wood)