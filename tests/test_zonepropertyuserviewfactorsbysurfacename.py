import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.advanced_construction import ZonePropertyUserViewFactorsBySurfaceName

log = logging.getLogger(__name__)

class TestZonePropertyUserViewFactorsBySurfaceName(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonepropertyuserviewfactorsbysurfacename(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZonePropertyUserViewFactorsBySurfaceName()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        paras = []
        var_from_surface_1 = "object-list|From Surface 1"
        paras.append(var_from_surface_1)
        var_to_surface_1 = "object-list|To Surface 1"
        paras.append(var_to_surface_1)
        var_view_factor_1 = 1.0
        paras.append(var_view_factor_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonepropertyuserviewfactorsbysurfacenames[0].zone_name, var_zone_name)
        index = obj.extensible_field_index("From Surface 1")
        self.assertEqual(idf2.zonepropertyuserviewfactorsbysurfacenames[0].extensibles[0][index], var_from_surface_1)
        index = obj.extensible_field_index("To Surface 1")
        self.assertEqual(idf2.zonepropertyuserviewfactorsbysurfacenames[0].extensibles[0][index], var_to_surface_1)
        index = obj.extensible_field_index("View Factor 1")
        self.assertAlmostEqual(idf2.zonepropertyuserviewfactorsbysurfacenames[0].extensibles[0][index], var_view_factor_1)