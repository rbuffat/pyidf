import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import OutputControlSurfaceColorScheme

log = logging.getLogger(__name__)

class TestOutputControlSurfaceColorScheme(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputcontrolsurfacecolorscheme(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputControlSurfaceColorScheme()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_drawing_element_1_type = "Text"
        obj.drawing_element_1_type = var_drawing_element_1_type
        # integer
        var_color_for_drawing_element_1 = 127
        obj.color_for_drawing_element_1 = var_color_for_drawing_element_1
        # alpha
        var_drawing_element_2_type = "Text"
        obj.drawing_element_2_type = var_drawing_element_2_type
        # integer
        var_color_for_drawing_element_2 = 127
        obj.color_for_drawing_element_2 = var_color_for_drawing_element_2
        # alpha
        var_drawing_element_3_type = "Text"
        obj.drawing_element_3_type = var_drawing_element_3_type
        # integer
        var_color_for_drawing_element_3 = 127
        obj.color_for_drawing_element_3 = var_color_for_drawing_element_3
        # alpha
        var_drawing_element_4_type = "Text"
        obj.drawing_element_4_type = var_drawing_element_4_type
        # integer
        var_color_for_drawing_element_4 = 127
        obj.color_for_drawing_element_4 = var_color_for_drawing_element_4
        # alpha
        var_drawing_element_5_type = "Text"
        obj.drawing_element_5_type = var_drawing_element_5_type
        # integer
        var_color_for_drawing_element_5 = 127
        obj.color_for_drawing_element_5 = var_color_for_drawing_element_5
        # alpha
        var_drawing_element_6_type = "Text"
        obj.drawing_element_6_type = var_drawing_element_6_type
        # integer
        var_color_for_drawing_element_6 = 127
        obj.color_for_drawing_element_6 = var_color_for_drawing_element_6
        # alpha
        var_drawing_element_7_type = "Text"
        obj.drawing_element_7_type = var_drawing_element_7_type
        # integer
        var_color_for_drawing_element_7 = 127
        obj.color_for_drawing_element_7 = var_color_for_drawing_element_7
        # alpha
        var_drawing_element_8_type = "Text"
        obj.drawing_element_8_type = var_drawing_element_8_type
        # integer
        var_color_for_drawing_element_8 = 127
        obj.color_for_drawing_element_8 = var_color_for_drawing_element_8
        # alpha
        var_drawing_element_9_type = "Text"
        obj.drawing_element_9_type = var_drawing_element_9_type
        # integer
        var_color_for_drawing_element_9 = 127
        obj.color_for_drawing_element_9 = var_color_for_drawing_element_9
        # alpha
        var_drawing_element_10_type = "Text"
        obj.drawing_element_10_type = var_drawing_element_10_type
        # integer
        var_color_for_drawing_element_10 = 127
        obj.color_for_drawing_element_10 = var_color_for_drawing_element_10
        # alpha
        var_drawing_element_11_type = "Text"
        obj.drawing_element_11_type = var_drawing_element_11_type
        # integer
        var_color_for_drawing_element_11 = 127
        obj.color_for_drawing_element_11 = var_color_for_drawing_element_11
        # alpha
        var_drawing_element_12_type = "Text"
        obj.drawing_element_12_type = var_drawing_element_12_type
        # integer
        var_color_for_drawing_element_12 = 127
        obj.color_for_drawing_element_12 = var_color_for_drawing_element_12
        # alpha
        var_drawing_element_13_type = "Text"
        obj.drawing_element_13_type = var_drawing_element_13_type
        # integer
        var_color_for_drawing_element_13 = 127
        obj.color_for_drawing_element_13 = var_color_for_drawing_element_13
        # alpha
        var_drawing_element_14_type = "Text"
        obj.drawing_element_14_type = var_drawing_element_14_type
        # integer
        var_color_for_drawing_element_14 = 127
        obj.color_for_drawing_element_14 = var_color_for_drawing_element_14
        # alpha
        var_drawing_element_15_type = "Text"
        obj.drawing_element_15_type = var_drawing_element_15_type
        # integer
        var_color_for_drawing_element_15 = 127
        obj.color_for_drawing_element_15 = var_color_for_drawing_element_15

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].name, var_name)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_1_type, var_drawing_element_1_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_1, var_color_for_drawing_element_1)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_2_type, var_drawing_element_2_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_2, var_color_for_drawing_element_2)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_3_type, var_drawing_element_3_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_3, var_color_for_drawing_element_3)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_4_type, var_drawing_element_4_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_4, var_color_for_drawing_element_4)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_5_type, var_drawing_element_5_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_5, var_color_for_drawing_element_5)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_6_type, var_drawing_element_6_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_6, var_color_for_drawing_element_6)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_7_type, var_drawing_element_7_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_7, var_color_for_drawing_element_7)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_8_type, var_drawing_element_8_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_8, var_color_for_drawing_element_8)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_9_type, var_drawing_element_9_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_9, var_color_for_drawing_element_9)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_10_type, var_drawing_element_10_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_10, var_color_for_drawing_element_10)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_11_type, var_drawing_element_11_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_11, var_color_for_drawing_element_11)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_12_type, var_drawing_element_12_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_12, var_color_for_drawing_element_12)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_13_type, var_drawing_element_13_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_13, var_color_for_drawing_element_13)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_14_type, var_drawing_element_14_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_14, var_color_for_drawing_element_14)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].drawing_element_15_type, var_drawing_element_15_type)
        self.assertEqual(idf2.outputcontrolsurfacecolorschemes[0].color_for_drawing_element_15, var_color_for_drawing_element_15)