import os
import tempfile
import unittest
import pyidf
from pyidf.advanced_construction import SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSurfaceConvectionAlgorithmOutsideAdaptiveModelSelections(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfaceconvectionalgorithmoutsideadaptivemodelselections(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_wind_convection_windward_vertical_wall_equation_source = "SimpleCombined"
        obj.wind_convection_windward_vertical_wall_equation_source = var_wind_convection_windward_vertical_wall_equation_source
        # object-list
        var_wind_convection_windward_equation_vertical_wall_user_curve_name = "object-list|Wind Convection Windward Equation Vertical Wall User Curve Name"
        obj.wind_convection_windward_equation_vertical_wall_user_curve_name = var_wind_convection_windward_equation_vertical_wall_user_curve_name
        # alpha
        var_wind_convection_leeward_vertical_wall_equation_source = "SimpleCombined"
        obj.wind_convection_leeward_vertical_wall_equation_source = var_wind_convection_leeward_vertical_wall_equation_source
        # object-list
        var_wind_convection_leeward_vertical_wall_equation_user_curve_name = "object-list|Wind Convection Leeward Vertical Wall Equation User Curve Name"
        obj.wind_convection_leeward_vertical_wall_equation_user_curve_name = var_wind_convection_leeward_vertical_wall_equation_user_curve_name
        # alpha
        var_wind_convection_horizontal_roof_equation_source = "SimpleCombined"
        obj.wind_convection_horizontal_roof_equation_source = var_wind_convection_horizontal_roof_equation_source
        # object-list
        var_wind_convection_horizontal_roof_user_curve_name = "object-list|Wind Convection Horizontal Roof User Curve Name"
        obj.wind_convection_horizontal_roof_user_curve_name = var_wind_convection_horizontal_roof_user_curve_name
        # alpha
        var_natural_convection_vertical_wall_equation_source = "ASHRAEVerticalWall"
        obj.natural_convection_vertical_wall_equation_source = var_natural_convection_vertical_wall_equation_source
        # object-list
        var_natural_convection_vertical_wall_equation_user_curve_name = "object-list|Natural Convection Vertical Wall Equation User Curve Name"
        obj.natural_convection_vertical_wall_equation_user_curve_name = var_natural_convection_vertical_wall_equation_user_curve_name
        # alpha
        var_natural_convection_stable_horizontal_equation_source = "WaltonStableHorizontalOrTilt"
        obj.natural_convection_stable_horizontal_equation_source = var_natural_convection_stable_horizontal_equation_source
        # object-list
        var_natural_convection_stable_horizontal_equation_user_curve_name = "object-list|Natural Convection Stable Horizontal Equation User Curve Name"
        obj.natural_convection_stable_horizontal_equation_user_curve_name = var_natural_convection_stable_horizontal_equation_user_curve_name
        # alpha
        var_natural_convection_unstable_horizontal_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.natural_convection_unstable_horizontal_equation_source = var_natural_convection_unstable_horizontal_equation_source
        # object-list
        var_natural_convection_unstable_horizontal_equation_user_curve_name = "object-list|Natural Convection Unstable Horizontal Equation User Curve Name"
        obj.natural_convection_unstable_horizontal_equation_user_curve_name = var_natural_convection_unstable_horizontal_equation_user_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].name, var_name)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].wind_convection_windward_vertical_wall_equation_source, var_wind_convection_windward_vertical_wall_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].wind_convection_windward_equation_vertical_wall_user_curve_name, var_wind_convection_windward_equation_vertical_wall_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].wind_convection_leeward_vertical_wall_equation_source, var_wind_convection_leeward_vertical_wall_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].wind_convection_leeward_vertical_wall_equation_user_curve_name, var_wind_convection_leeward_vertical_wall_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].wind_convection_horizontal_roof_equation_source, var_wind_convection_horizontal_roof_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].wind_convection_horizontal_roof_user_curve_name, var_wind_convection_horizontal_roof_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].natural_convection_vertical_wall_equation_source, var_natural_convection_vertical_wall_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].natural_convection_vertical_wall_equation_user_curve_name, var_natural_convection_vertical_wall_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].natural_convection_stable_horizontal_equation_source, var_natural_convection_stable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].natural_convection_stable_horizontal_equation_user_curve_name, var_natural_convection_stable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].natural_convection_unstable_horizontal_equation_source, var_natural_convection_unstable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithmoutsideadaptivemodelselectionss[0].natural_convection_unstable_horizontal_equation_user_curve_name, var_natural_convection_unstable_horizontal_equation_user_curve_name)