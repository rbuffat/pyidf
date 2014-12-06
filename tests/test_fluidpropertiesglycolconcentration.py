import os
import tempfile
import unittest
import pyidf
from pyidf.fluid_properties import FluidPropertiesGlycolConcentration
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestFluidPropertiesGlycolConcentration(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fluidpropertiesglycolconcentration(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FluidPropertiesGlycolConcentration()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_glycol_type = "EthyleneGlycol"
        obj.glycol_type = var_glycol_type
        # object-list
        var_user_defined_glycol_name = "object-list|User Defined Glycol Name"
        obj.user_defined_glycol_name = var_user_defined_glycol_name
        # real
        var_glycol_concentration = 0.5
        obj.glycol_concentration = var_glycol_concentration

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fluidpropertiesglycolconcentrations[0].name, var_name)
        self.assertEqual(idf2.fluidpropertiesglycolconcentrations[0].glycol_type, var_glycol_type)
        self.assertEqual(idf2.fluidpropertiesglycolconcentrations[0].user_defined_glycol_name, var_user_defined_glycol_name)
        self.assertAlmostEqual(idf2.fluidpropertiesglycolconcentrations[0].glycol_concentration, var_glycol_concentration)