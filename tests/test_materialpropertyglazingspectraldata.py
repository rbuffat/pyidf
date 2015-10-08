import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import MaterialPropertyGlazingSpectralData

log = logging.getLogger(__name__)

class TestMaterialPropertyGlazingSpectralData(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_materialpropertyglazingspectraldata(self):

        pyidf.validation_level = ValidationLevel.error

        obj = MaterialPropertyGlazingSpectralData()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_wavelength = 2.2
        paras.append(var_wavelength)
        var_transmittance = 3.3
        paras.append(var_transmittance)
        var_front_reflectance = 4.4
        paras.append(var_front_reflectance)
        var_back_reflectance = 5.5
        paras.append(var_back_reflectance)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.materialpropertyglazingspectraldatas[0].name, var_name)
        index = obj.extensible_field_index("Wavelength")
        self.assertAlmostEqual(idf2.materialpropertyglazingspectraldatas[0].extensibles[0][index], var_wavelength)
        index = obj.extensible_field_index("Transmittance")
        self.assertAlmostEqual(idf2.materialpropertyglazingspectraldatas[0].extensibles[0][index], var_transmittance)
        index = obj.extensible_field_index("Front Reflectance")
        self.assertAlmostEqual(idf2.materialpropertyglazingspectraldatas[0].extensibles[0][index], var_front_reflectance)
        index = obj.extensible_field_index("Back Reflectance")
        self.assertAlmostEqual(idf2.materialpropertyglazingspectraldatas[0].extensibles[0][index], var_back_reflectance)