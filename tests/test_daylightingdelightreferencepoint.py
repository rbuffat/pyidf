import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.daylighting import DaylightingDelightReferencePoint

log = logging.getLogger(__name__)

class TestDaylightingDelightReferencePoint(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_daylightingdelightreferencepoint(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DaylightingDelightReferencePoint()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_delight_name = "object-list|DElight Name"
        obj.delight_name = var_delight_name
        # real
        var_xcoordinate_of_reference_point = 3.3
        obj.xcoordinate_of_reference_point = var_xcoordinate_of_reference_point
        # real
        var_ycoordinate_of_reference_point = 4.4
        obj.ycoordinate_of_reference_point = var_ycoordinate_of_reference_point
        # real
        var_zcoordinate_of_reference_point = 5.5
        obj.zcoordinate_of_reference_point = var_zcoordinate_of_reference_point
        # real
        var_fraction_of_zone_controlled_by_reference_point = 0.5
        obj.fraction_of_zone_controlled_by_reference_point = var_fraction_of_zone_controlled_by_reference_point
        # real
        var_illuminance_setpoint_at_reference_point = 0.0
        obj.illuminance_setpoint_at_reference_point = var_illuminance_setpoint_at_reference_point

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.daylightingdelightreferencepoints[0].name, var_name)
        self.assertEqual(idf2.daylightingdelightreferencepoints[0].delight_name, var_delight_name)
        self.assertAlmostEqual(idf2.daylightingdelightreferencepoints[0].xcoordinate_of_reference_point, var_xcoordinate_of_reference_point)
        self.assertAlmostEqual(idf2.daylightingdelightreferencepoints[0].ycoordinate_of_reference_point, var_ycoordinate_of_reference_point)
        self.assertAlmostEqual(idf2.daylightingdelightreferencepoints[0].zcoordinate_of_reference_point, var_zcoordinate_of_reference_point)
        self.assertAlmostEqual(idf2.daylightingdelightreferencepoints[0].fraction_of_zone_controlled_by_reference_point, var_fraction_of_zone_controlled_by_reference_point)
        self.assertAlmostEqual(idf2.daylightingdelightreferencepoints[0].illuminance_setpoint_at_reference_point, var_illuminance_setpoint_at_reference_point)