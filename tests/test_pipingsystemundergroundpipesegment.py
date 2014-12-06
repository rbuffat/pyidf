import os
import tempfile
import unittest
import pyidf
from pyidf.node import PipingSystemUndergroundPipeSegment
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPipingSystemUndergroundPipeSegment(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_pipingsystemundergroundpipesegment(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PipingSystemUndergroundPipeSegment()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_x_position = 0.0001
        obj.x_position = var_x_position
        # real
        var_y_position = 0.0001
        obj.y_position = var_y_position
        # alpha
        var_flow_direction = "IncreasingZ"
        obj.flow_direction = var_flow_direction

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.pipingsystemundergroundpipesegments[0].name, var_name)
        self.assertAlmostEqual(idf2.pipingsystemundergroundpipesegments[0].x_position, var_x_position)
        self.assertAlmostEqual(idf2.pipingsystemundergroundpipesegments[0].y_position, var_y_position)
        self.assertEqual(idf2.pipingsystemundergroundpipesegments[0].flow_direction, var_flow_direction)