import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.advanced_construction import SurfacePropertiesVaporCoefficients

log = logging.getLogger(__name__)

class TestSurfacePropertiesVaporCoefficients(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacepropertiesvaporcoefficients(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfacePropertiesVaporCoefficients()
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # alpha
        var_constant_external_vapor_transfer_coefficient = "Yes"
        obj.constant_external_vapor_transfer_coefficient = var_constant_external_vapor_transfer_coefficient
        # real
        var_external_vapor_coefficient_value = 0.0
        obj.external_vapor_coefficient_value = var_external_vapor_coefficient_value
        # alpha
        var_constant_internal_vapor_transfer_coefficient = "Yes"
        obj.constant_internal_vapor_transfer_coefficient = var_constant_internal_vapor_transfer_coefficient
        # real
        var_internal_vapor_coefficient_value = 0.0
        obj.internal_vapor_coefficient_value = var_internal_vapor_coefficient_value

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacepropertiesvaporcoefficientss[0].surface_name, var_surface_name)
        self.assertEqual(idf2.surfacepropertiesvaporcoefficientss[0].constant_external_vapor_transfer_coefficient, var_constant_external_vapor_transfer_coefficient)
        self.assertAlmostEqual(idf2.surfacepropertiesvaporcoefficientss[0].external_vapor_coefficient_value, var_external_vapor_coefficient_value)
        self.assertEqual(idf2.surfacepropertiesvaporcoefficientss[0].constant_internal_vapor_transfer_coefficient, var_constant_internal_vapor_transfer_coefficient)
        self.assertAlmostEqual(idf2.surfacepropertiesvaporcoefficientss[0].internal_vapor_coefficient_value, var_internal_vapor_coefficient_value)