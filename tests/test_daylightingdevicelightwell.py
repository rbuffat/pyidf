import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.daylighting import DaylightingDeviceLightWell

log = logging.getLogger(__name__)

class TestDaylightingDeviceLightWell(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_daylightingdevicelightwell(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DaylightingDeviceLightWell()
        # alpha
        var_exterior_window_name = "Exterior Window Name"
        obj.exterior_window_name = var_exterior_window_name
        # real
        var_height_of_well = 0.0
        obj.height_of_well = var_height_of_well
        # real
        var_perimeter_of_bottom_of_well = 0.0001
        obj.perimeter_of_bottom_of_well = var_perimeter_of_bottom_of_well
        # real
        var_area_of_bottom_of_well = 0.0001
        obj.area_of_bottom_of_well = var_area_of_bottom_of_well
        # real
        var_visible_reflectance_of_well_walls = 0.5
        obj.visible_reflectance_of_well_walls = var_visible_reflectance_of_well_walls

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.daylightingdevicelightwells[0].exterior_window_name, var_exterior_window_name)
        self.assertAlmostEqual(idf2.daylightingdevicelightwells[0].height_of_well, var_height_of_well)
        self.assertAlmostEqual(idf2.daylightingdevicelightwells[0].perimeter_of_bottom_of_well, var_perimeter_of_bottom_of_well)
        self.assertAlmostEqual(idf2.daylightingdevicelightwells[0].area_of_bottom_of_well, var_area_of_bottom_of_well)
        self.assertAlmostEqual(idf2.daylightingdevicelightwells[0].visible_reflectance_of_well_walls, var_visible_reflectance_of_well_walls)