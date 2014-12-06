import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.advanced_construction import SurfaceControlMovableInsulation

log = logging.getLogger(__name__)

class TestSurfaceControlMovableInsulation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacecontrolmovableinsulation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfaceControlMovableInsulation()
        # alpha
        var_insulation_type = "Outside"
        obj.insulation_type = var_insulation_type
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # alpha
        var_material_name = "Material Name"
        obj.material_name = var_material_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacecontrolmovableinsulations[0].insulation_type, var_insulation_type)
        self.assertEqual(idf2.surfacecontrolmovableinsulations[0].surface_name, var_surface_name)
        self.assertEqual(idf2.surfacecontrolmovableinsulations[0].material_name, var_material_name)
        self.assertEqual(idf2.surfacecontrolmovableinsulations[0].schedule_name, var_schedule_name)