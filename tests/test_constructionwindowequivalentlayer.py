import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import ConstructionWindowEquivalentLayer
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestConstructionWindowEquivalentLayer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_constructionwindowequivalentlayer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ConstructionWindowEquivalentLayer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_outside_layer = "object-list|Outside Layer"
        obj.outside_layer = var_outside_layer
        # object-list
        var_layer_2 = "object-list|Layer 2"
        obj.layer_2 = var_layer_2
        # object-list
        var_layer_3 = "object-list|Layer 3"
        obj.layer_3 = var_layer_3
        # object-list
        var_layer_4 = "object-list|Layer 4"
        obj.layer_4 = var_layer_4
        # object-list
        var_layer_5 = "object-list|Layer 5"
        obj.layer_5 = var_layer_5
        # object-list
        var_layer_6 = "object-list|Layer 6"
        obj.layer_6 = var_layer_6
        # object-list
        var_layer_7 = "object-list|Layer 7"
        obj.layer_7 = var_layer_7
        # object-list
        var_layer_8 = "object-list|Layer 8"
        obj.layer_8 = var_layer_8
        # object-list
        var_layer_9 = "object-list|Layer 9"
        obj.layer_9 = var_layer_9
        # object-list
        var_layer_10 = "object-list|Layer 10"
        obj.layer_10 = var_layer_10
        # object-list
        var_layer_11 = "object-list|Layer 11"
        obj.layer_11 = var_layer_11

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].name, var_name)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].outside_layer, var_outside_layer)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].layer_2, var_layer_2)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].layer_3, var_layer_3)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].layer_4, var_layer_4)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].layer_5, var_layer_5)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].layer_6, var_layer_6)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].layer_7, var_layer_7)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].layer_8, var_layer_8)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].layer_9, var_layer_9)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].layer_10, var_layer_10)
        self.assertEqual(idf2.constructionwindowequivalentlayers[0].layer_11, var_layer_11)