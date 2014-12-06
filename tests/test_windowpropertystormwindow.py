import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import WindowPropertyStormWindow
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowPropertyStormWindow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowpropertystormwindow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowPropertyStormWindow()
        # alpha
        var_window_name = "Window Name"
        obj.window_name = var_window_name
        # object-list
        var_storm_glass_layer_name = "object-list|Storm Glass Layer Name"
        obj.storm_glass_layer_name = var_storm_glass_layer_name
        # real
        var_distance_between_storm_glass_layer_and_adjacent_glass = 0.25005
        obj.distance_between_storm_glass_layer_and_adjacent_glass = var_distance_between_storm_glass_layer_and_adjacent_glass
        # integer
        var_month_that_storm_glass_layer_is_put_on = 6
        obj.month_that_storm_glass_layer_is_put_on = var_month_that_storm_glass_layer_is_put_on
        # integer
        var_day_of_month_that_storm_glass_layer_is_put_on = 16
        obj.day_of_month_that_storm_glass_layer_is_put_on = var_day_of_month_that_storm_glass_layer_is_put_on
        # integer
        var_month_that_storm_glass_layer_is_taken_off = 6
        obj.month_that_storm_glass_layer_is_taken_off = var_month_that_storm_glass_layer_is_taken_off
        # integer
        var_day_of_month_that_storm_glass_layer_is_taken_off = 16
        obj.day_of_month_that_storm_glass_layer_is_taken_off = var_day_of_month_that_storm_glass_layer_is_taken_off

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowpropertystormwindows[0].window_name, var_window_name)
        self.assertEqual(idf2.windowpropertystormwindows[0].storm_glass_layer_name, var_storm_glass_layer_name)
        self.assertAlmostEqual(idf2.windowpropertystormwindows[0].distance_between_storm_glass_layer_and_adjacent_glass, var_distance_between_storm_glass_layer_and_adjacent_glass)
        self.assertEqual(idf2.windowpropertystormwindows[0].month_that_storm_glass_layer_is_put_on, var_month_that_storm_glass_layer_is_put_on)
        self.assertEqual(idf2.windowpropertystormwindows[0].day_of_month_that_storm_glass_layer_is_put_on, var_day_of_month_that_storm_glass_layer_is_put_on)
        self.assertEqual(idf2.windowpropertystormwindows[0].month_that_storm_glass_layer_is_taken_off, var_month_that_storm_glass_layer_is_taken_off)
        self.assertEqual(idf2.windowpropertystormwindows[0].day_of_month_that_storm_glass_layer_is_taken_off, var_day_of_month_that_storm_glass_layer_is_taken_off)