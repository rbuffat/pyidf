import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.fluid_properties import FluidPropertiesName

log = logging.getLogger(__name__)

class TestFluidPropertiesName(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fluidpropertiesname(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FluidPropertiesName()
        # alpha
        var_fluid_name = "Fluid Name"
        obj.fluid_name = var_fluid_name
        # alpha
        var_fluid_type = "Refrigerant"
        obj.fluid_type = var_fluid_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fluidpropertiesnames[0].fluid_name, var_fluid_name)
        self.assertEqual(idf2.fluidpropertiesnames[0].fluid_type, var_fluid_type)