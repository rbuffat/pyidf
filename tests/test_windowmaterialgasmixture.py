import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowMaterialGasMixture

log = logging.getLogger(__name__)

class TestWindowMaterialGasMixture(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialgasmixture(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialGasMixture()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_thickness = 0.0001
        obj.thickness = var_thickness
        # integer
        var_number_of_gases_in_mixture = 2
        obj.number_of_gases_in_mixture = var_number_of_gases_in_mixture
        # alpha
        var_gas_1_type = "Air"
        obj.gas_1_type = var_gas_1_type
        # real
        var_gas_1_fraction = 0.50005
        obj.gas_1_fraction = var_gas_1_fraction
        # alpha
        var_gas_2_type = "Air"
        obj.gas_2_type = var_gas_2_type
        # real
        var_gas_2_fraction = 0.50005
        obj.gas_2_fraction = var_gas_2_fraction
        # alpha
        var_gas_3_type = "Air"
        obj.gas_3_type = var_gas_3_type
        # real
        var_gas_3_fraction = 0.50005
        obj.gas_3_fraction = var_gas_3_fraction
        # alpha
        var_gas_4_type = "Air"
        obj.gas_4_type = var_gas_4_type
        # real
        var_gas_4_fraction = 0.50005
        obj.gas_4_fraction = var_gas_4_fraction

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialgasmixtures[0].name, var_name)
        self.assertAlmostEqual(idf2.windowmaterialgasmixtures[0].thickness, var_thickness)
        self.assertEqual(idf2.windowmaterialgasmixtures[0].number_of_gases_in_mixture, var_number_of_gases_in_mixture)
        self.assertEqual(idf2.windowmaterialgasmixtures[0].gas_1_type, var_gas_1_type)
        self.assertAlmostEqual(idf2.windowmaterialgasmixtures[0].gas_1_fraction, var_gas_1_fraction)
        self.assertEqual(idf2.windowmaterialgasmixtures[0].gas_2_type, var_gas_2_type)
        self.assertAlmostEqual(idf2.windowmaterialgasmixtures[0].gas_2_fraction, var_gas_2_fraction)
        self.assertEqual(idf2.windowmaterialgasmixtures[0].gas_3_type, var_gas_3_type)
        self.assertAlmostEqual(idf2.windowmaterialgasmixtures[0].gas_3_fraction, var_gas_3_fraction)
        self.assertEqual(idf2.windowmaterialgasmixtures[0].gas_4_type, var_gas_4_type)
        self.assertAlmostEqual(idf2.windowmaterialgasmixtures[0].gas_4_fraction, var_gas_4_fraction)