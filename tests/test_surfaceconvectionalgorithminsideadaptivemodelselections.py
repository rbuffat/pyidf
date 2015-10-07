import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.advanced_construction import SurfaceConvectionAlgorithmInsideAdaptiveModelSelections

log = logging.getLogger(__name__)

class TestSurfaceConvectionAlgorithmInsideAdaptiveModelSelections(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfaceconvectionalgorithminsideadaptivemodelselections(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfaceConvectionAlgorithmInsideAdaptiveModelSelections()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_simple_buoyancy_vertical_wall_equation_source = "ASHRAEVerticalWall"
        obj.simple_buoyancy_vertical_wall_equation_source = var_simple_buoyancy_vertical_wall_equation_source
        # object-list
        var_simple_buoyancy_vertical_wall_user_curve_name = "object-list|Simple Buoyancy Vertical Wall User Curve Name"
        obj.simple_buoyancy_vertical_wall_user_curve_name = var_simple_buoyancy_vertical_wall_user_curve_name
        # alpha
        var_simple_buoyancy_stable_horizontal_equation_source = "WaltonStableHorizontalOrTilt"
        obj.simple_buoyancy_stable_horizontal_equation_source = var_simple_buoyancy_stable_horizontal_equation_source
        # object-list
        var_simple_buoyancy_stable_horizontal_equation_user_curve_name = "object-list|Simple Buoyancy Stable Horizontal Equation User Curve Name"
        obj.simple_buoyancy_stable_horizontal_equation_user_curve_name = var_simple_buoyancy_stable_horizontal_equation_user_curve_name
        # alpha
        var_simple_buoyancy_unstable_horizontal_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.simple_buoyancy_unstable_horizontal_equation_source = var_simple_buoyancy_unstable_horizontal_equation_source
        # object-list
        var_simple_buoyancy_unstable_horizontal_equation_user_curve_name = "object-list|Simple Buoyancy Unstable Horizontal Equation User Curve Name"
        obj.simple_buoyancy_unstable_horizontal_equation_user_curve_name = var_simple_buoyancy_unstable_horizontal_equation_user_curve_name
        # alpha
        var_simple_buoyancy_stable_tilted_equation_source = "WaltonStableHorizontalOrTilt"
        obj.simple_buoyancy_stable_tilted_equation_source = var_simple_buoyancy_stable_tilted_equation_source
        # object-list
        var_simple_buoyancy_stable_tilted_equation_user_curve_name = "object-list|Simple Buoyancy Stable Tilted Equation User Curve Name"
        obj.simple_buoyancy_stable_tilted_equation_user_curve_name = var_simple_buoyancy_stable_tilted_equation_user_curve_name
        # alpha
        var_simple_buoyancy_unstable_tilted_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.simple_buoyancy_unstable_tilted_equation_source = var_simple_buoyancy_unstable_tilted_equation_source
        # object-list
        var_simple_buoyancy_unstable_tilted_equation_user_curve_name = "object-list|Simple Buoyancy Unstable Tilted Equation User Curve Name"
        obj.simple_buoyancy_unstable_tilted_equation_user_curve_name = var_simple_buoyancy_unstable_tilted_equation_user_curve_name
        # alpha
        var_simple_buoyancy_windows_equation_source = "ASHRAEVerticalWall"
        obj.simple_buoyancy_windows_equation_source = var_simple_buoyancy_windows_equation_source
        # object-list
        var_simple_buoyancy_windows_equation_user_curve_name = "object-list|Simple Buoyancy Windows Equation User Curve Name"
        obj.simple_buoyancy_windows_equation_user_curve_name = var_simple_buoyancy_windows_equation_user_curve_name
        # alpha
        var_floor_heat_ceiling_cool_vertical_wall_equation_source = "ASHRAEVerticalWall"
        obj.floor_heat_ceiling_cool_vertical_wall_equation_source = var_floor_heat_ceiling_cool_vertical_wall_equation_source
        # object-list
        var_floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name = "object-list|Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name"
        obj.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name = var_floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name
        # alpha
        var_floor_heat_ceiling_cool_stable_horizontal_equation_source = "WaltonStableHorizontalOrTilt"
        obj.floor_heat_ceiling_cool_stable_horizontal_equation_source = var_floor_heat_ceiling_cool_stable_horizontal_equation_source
        # object-list
        var_floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name = "object-list|Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name"
        obj.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name = var_floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name
        # alpha
        var_floor_heat_ceiling_cool_unstable_horizontal_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.floor_heat_ceiling_cool_unstable_horizontal_equation_source = var_floor_heat_ceiling_cool_unstable_horizontal_equation_source
        # object-list
        var_floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name = "object-list|Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name"
        obj.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name = var_floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name
        # alpha
        var_floor_heat_ceiling_cool_heated_floor_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.floor_heat_ceiling_cool_heated_floor_equation_source = var_floor_heat_ceiling_cool_heated_floor_equation_source
        # object-list
        var_floor_heat_ceiling_cool_heated_floor_equation_user_curve_name = "object-list|Floor Heat Ceiling Cool Heated Floor Equation User Curve Name"
        obj.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name = var_floor_heat_ceiling_cool_heated_floor_equation_user_curve_name
        # alpha
        var_floor_heat_ceiling_cool_chilled_ceiling_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.floor_heat_ceiling_cool_chilled_ceiling_equation_source = var_floor_heat_ceiling_cool_chilled_ceiling_equation_source
        # object-list
        var_floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name = "object-list|Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name"
        obj.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name = var_floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name
        # alpha
        var_floor_heat_ceiling_cool_stable_tilted_equation_source = "WaltonStableHorizontalOrTilt"
        obj.floor_heat_ceiling_cool_stable_tilted_equation_source = var_floor_heat_ceiling_cool_stable_tilted_equation_source
        # object-list
        var_floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name = "object-list|Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name"
        obj.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name = var_floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name
        # alpha
        var_floor_heat_ceiling_cool_unstable_tilted_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.floor_heat_ceiling_cool_unstable_tilted_equation_source = var_floor_heat_ceiling_cool_unstable_tilted_equation_source
        # object-list
        var_floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name = "object-list|Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name"
        obj.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name = var_floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name
        # alpha
        var_floor_heat_ceiling_cool_window_equation_source = "ASHRAEVerticalWall"
        obj.floor_heat_ceiling_cool_window_equation_source = var_floor_heat_ceiling_cool_window_equation_source
        # object-list
        var_floor_heat_ceiling_cool_window_equation_user_curve_name = "object-list|Floor Heat Ceiling Cool Window Equation User Curve Name"
        obj.floor_heat_ceiling_cool_window_equation_user_curve_name = var_floor_heat_ceiling_cool_window_equation_user_curve_name
        # alpha
        var_wall_panel_heating_vertical_wall_equation_source = "ASHRAEVerticalWall"
        obj.wall_panel_heating_vertical_wall_equation_source = var_wall_panel_heating_vertical_wall_equation_source
        # object-list
        var_wall_panel_heating_vertical_wall_equation_user_curve_name = "object-list|Wall Panel Heating Vertical Wall Equation User Curve Name"
        obj.wall_panel_heating_vertical_wall_equation_user_curve_name = var_wall_panel_heating_vertical_wall_equation_user_curve_name
        # alpha
        var_wall_panel_heating_heated_wall_equation_source = "ASHRAEVerticalWall"
        obj.wall_panel_heating_heated_wall_equation_source = var_wall_panel_heating_heated_wall_equation_source
        # object-list
        var_wall_panel_heating_heated_wall_equation_user_curve_name = "object-list|Wall Panel Heating Heated Wall Equation User Curve Name"
        obj.wall_panel_heating_heated_wall_equation_user_curve_name = var_wall_panel_heating_heated_wall_equation_user_curve_name
        # alpha
        var_wall_panel_heating_stable_horizontal_equation_source = "WaltonStableHorizontalOrTilt"
        obj.wall_panel_heating_stable_horizontal_equation_source = var_wall_panel_heating_stable_horizontal_equation_source
        # object-list
        var_wall_panel_heating_stable_horizontal_equation_user_curve_name = "object-list|Wall Panel Heating Stable Horizontal Equation User Curve Name"
        obj.wall_panel_heating_stable_horizontal_equation_user_curve_name = var_wall_panel_heating_stable_horizontal_equation_user_curve_name
        # alpha
        var_wall_panel_heating_unstable_horizontal_equation_source = "ASHRAEVerticalWall"
        obj.wall_panel_heating_unstable_horizontal_equation_source = var_wall_panel_heating_unstable_horizontal_equation_source
        # object-list
        var_wall_panel_heating_unstable_horizontal_equation_user_curve_name = "object-list|Wall Panel Heating Unstable Horizontal Equation User Curve Name"
        obj.wall_panel_heating_unstable_horizontal_equation_user_curve_name = var_wall_panel_heating_unstable_horizontal_equation_user_curve_name
        # alpha
        var_wall_panel_heating_stable_tilted_equation_source = "WaltonStableHorizontalOrTilt"
        obj.wall_panel_heating_stable_tilted_equation_source = var_wall_panel_heating_stable_tilted_equation_source
        # object-list
        var_wall_panel_heating_stable_tilted_equation_user_curve_name = "object-list|Wall Panel Heating Stable Tilted Equation User Curve Name"
        obj.wall_panel_heating_stable_tilted_equation_user_curve_name = var_wall_panel_heating_stable_tilted_equation_user_curve_name
        # alpha
        var_wall_panel_heating_unstable_tilted_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.wall_panel_heating_unstable_tilted_equation_source = var_wall_panel_heating_unstable_tilted_equation_source
        # object-list
        var_wall_panel_heating_unstable_tilted_equation_user_curve_name = "object-list|Wall Panel Heating Unstable Tilted Equation User Curve Name"
        obj.wall_panel_heating_unstable_tilted_equation_user_curve_name = var_wall_panel_heating_unstable_tilted_equation_user_curve_name
        # alpha
        var_wall_panel_heating_window_equation_source = "ASHRAEVerticalWall"
        obj.wall_panel_heating_window_equation_source = var_wall_panel_heating_window_equation_source
        # object-list
        var_wall_panel_heating_window_equation_user_curve_name = "object-list|Wall Panel Heating Window Equation User Curve Name"
        obj.wall_panel_heating_window_equation_user_curve_name = var_wall_panel_heating_window_equation_user_curve_name
        # alpha
        var_convective_zone_heater_vertical_wall_equation_source = "ASHRAEVerticalWall"
        obj.convective_zone_heater_vertical_wall_equation_source = var_convective_zone_heater_vertical_wall_equation_source
        # object-list
        var_convective_zone_heater_vertical_wall_equation_user_curve_name = "object-list|Convective Zone Heater Vertical Wall Equation User Curve Name"
        obj.convective_zone_heater_vertical_wall_equation_user_curve_name = var_convective_zone_heater_vertical_wall_equation_user_curve_name
        # alpha
        var_convective_zone_heater_vertical_walls_near_heater_equation_source = "ASHRAEVerticalWall"
        obj.convective_zone_heater_vertical_walls_near_heater_equation_source = var_convective_zone_heater_vertical_walls_near_heater_equation_source
        # object-list
        var_convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name = "object-list|Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name"
        obj.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name = var_convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name
        # alpha
        var_convective_zone_heater_stable_horizontal_equation_source = "WaltonStableHorizontalOrTilt"
        obj.convective_zone_heater_stable_horizontal_equation_source = var_convective_zone_heater_stable_horizontal_equation_source
        # object-list
        var_convective_zone_heater_stable_horizontal_equation_user_curve_name = "object-list|Convective Zone Heater Stable Horizontal Equation User Curve Name"
        obj.convective_zone_heater_stable_horizontal_equation_user_curve_name = var_convective_zone_heater_stable_horizontal_equation_user_curve_name
        # alpha
        var_convective_zone_heater_unstable_horizontal_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.convective_zone_heater_unstable_horizontal_equation_source = var_convective_zone_heater_unstable_horizontal_equation_source
        # object-list
        var_convective_zone_heater_unstable_horizontal_equation_user_curve_name = "object-list|Convective Zone Heater Unstable Horizontal Equation User Curve Name"
        obj.convective_zone_heater_unstable_horizontal_equation_user_curve_name = var_convective_zone_heater_unstable_horizontal_equation_user_curve_name
        # alpha
        var_convective_zone_heater_stable_tilted_equation_source = "WaltonStableHorizontalOrTilt"
        obj.convective_zone_heater_stable_tilted_equation_source = var_convective_zone_heater_stable_tilted_equation_source
        # object-list
        var_convective_zone_heater_stable_tilted_equation_user_curve_name = "object-list|Convective Zone Heater Stable Tilted Equation User Curve Name"
        obj.convective_zone_heater_stable_tilted_equation_user_curve_name = var_convective_zone_heater_stable_tilted_equation_user_curve_name
        # alpha
        var_convective_zone_heater_unstable_tilted_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.convective_zone_heater_unstable_tilted_equation_source = var_convective_zone_heater_unstable_tilted_equation_source
        # object-list
        var_convective_zone_heater_unstable_tilted_equation_user_curve_name = "object-list|Convective Zone Heater Unstable Tilted Equation User Curve Name"
        obj.convective_zone_heater_unstable_tilted_equation_user_curve_name = var_convective_zone_heater_unstable_tilted_equation_user_curve_name
        # alpha
        var_convective_zone_heater_windows_equation_source = "ASHRAEVerticalWall"
        obj.convective_zone_heater_windows_equation_source = var_convective_zone_heater_windows_equation_source
        # object-list
        var_convective_zone_heater_windows_equation_user_curve_name = "object-list|Convective Zone Heater Windows Equation User Curve Name"
        obj.convective_zone_heater_windows_equation_user_curve_name = var_convective_zone_heater_windows_equation_user_curve_name
        # alpha
        var_central_air_diffuser_wall_equation_source = "ASHRAEVerticalWall"
        obj.central_air_diffuser_wall_equation_source = var_central_air_diffuser_wall_equation_source
        # object-list
        var_central_air_diffuser_wall_equation_user_curve_name = "object-list|Central Air Diffuser Wall Equation User Curve Name"
        obj.central_air_diffuser_wall_equation_user_curve_name = var_central_air_diffuser_wall_equation_user_curve_name
        # alpha
        var_central_air_diffuser_ceiling_equation_source = "FisherPedersenCeilingDiffuserCeiling"
        obj.central_air_diffuser_ceiling_equation_source = var_central_air_diffuser_ceiling_equation_source
        # object-list
        var_central_air_diffuser_ceiling_equation_user_curve_name = "object-list|Central Air Diffuser Ceiling Equation User Curve Name"
        obj.central_air_diffuser_ceiling_equation_user_curve_name = var_central_air_diffuser_ceiling_equation_user_curve_name
        # alpha
        var_central_air_diffuser_floor_equation_source = "FisherPedersenCeilingDiffuserFloor"
        obj.central_air_diffuser_floor_equation_source = var_central_air_diffuser_floor_equation_source
        # object-list
        var_central_air_diffuser_floor_equation_user_curve_name = "object-list|Central Air Diffuser Floor Equation User Curve Name"
        obj.central_air_diffuser_floor_equation_user_curve_name = var_central_air_diffuser_floor_equation_user_curve_name
        # alpha
        var_central_air_diffuser_window_equation_source = "ASHRAEVerticalWall"
        obj.central_air_diffuser_window_equation_source = var_central_air_diffuser_window_equation_source
        # object-list
        var_central_air_diffuser_window_equation_user_curve_name = "object-list|Central Air Diffuser Window Equation User Curve Name"
        obj.central_air_diffuser_window_equation_user_curve_name = var_central_air_diffuser_window_equation_user_curve_name
        # alpha
        var_mechanical_zone_fan_circulation_vertical_wall_equation_source = "KhalifaEq3WallAwayFromHeat"
        obj.mechanical_zone_fan_circulation_vertical_wall_equation_source = var_mechanical_zone_fan_circulation_vertical_wall_equation_source
        # object-list
        var_mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name = "object-list|Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name"
        obj.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name = var_mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name
        # alpha
        var_mechanical_zone_fan_circulation_stable_horizontal_equation_source = "WaltonStableHorizontalOrTilt"
        obj.mechanical_zone_fan_circulation_stable_horizontal_equation_source = var_mechanical_zone_fan_circulation_stable_horizontal_equation_source
        # object-list
        var_mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name = "object-list|Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name"
        obj.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name = var_mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name
        # alpha
        var_mechanical_zone_fan_circulation_unstable_horizontal_equation_source = "KhalifaEq4CeilingAwayFromHeat"
        obj.mechanical_zone_fan_circulation_unstable_horizontal_equation_source = var_mechanical_zone_fan_circulation_unstable_horizontal_equation_source
        # object-list
        var_mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name = "object-list|Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name"
        obj.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name = var_mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name
        # alpha
        var_mechanical_zone_fan_circulation_stable_tilted_equation_source = "WaltonStableHorizontalOrTilt"
        obj.mechanical_zone_fan_circulation_stable_tilted_equation_source = var_mechanical_zone_fan_circulation_stable_tilted_equation_source
        # object-list
        var_mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name = "object-list|Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name"
        obj.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name = var_mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name
        # alpha
        var_mechanical_zone_fan_circulation_unstable_tilted_equation_source = "WaltonUnstableHorizontalOrTilt"
        obj.mechanical_zone_fan_circulation_unstable_tilted_equation_source = var_mechanical_zone_fan_circulation_unstable_tilted_equation_source
        # object-list
        var_mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name = "object-list|Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name"
        obj.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name = var_mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name
        # alpha
        var_mechanical_zone_fan_circulation_window_equation_source = "ASHRAEVerticalWall"
        obj.mechanical_zone_fan_circulation_window_equation_source = var_mechanical_zone_fan_circulation_window_equation_source
        # object-list
        var_mechanical_zone_fan_circulation_window_equation_user_curve_name = "object-list|Mechanical Zone Fan Circulation Window Equation User Curve Name"
        obj.mechanical_zone_fan_circulation_window_equation_user_curve_name = var_mechanical_zone_fan_circulation_window_equation_user_curve_name
        # alpha
        var_mixed_regime_buoyancy_assisting_flow_on_walls_equation_source = "BeausoleilMorrisonMixedAssistedWall"
        obj.mixed_regime_buoyancy_assisting_flow_on_walls_equation_source = var_mixed_regime_buoyancy_assisting_flow_on_walls_equation_source
        # object-list
        var_mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name = "object-list|Mixed Regime Buoyancy Assisting Flow on Walls Equation User Curve Name"
        obj.mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name = var_mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name
        # alpha
        var_mixed_regime_buoyancy_opposing_flow_on_walls_equation_source = "BeausoleilMorrisonMixedOpposingWall"
        obj.mixed_regime_buoyancy_opposing_flow_on_walls_equation_source = var_mixed_regime_buoyancy_opposing_flow_on_walls_equation_source
        # object-list
        var_mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name = "object-list|Mixed Regime Buoyancy Opposing Flow on Walls Equation User Curve Name"
        obj.mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name = var_mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name
        # alpha
        var_mixed_regime_stable_floor_equation_source = "BeausoleilMorrisonMixedStableFloor"
        obj.mixed_regime_stable_floor_equation_source = var_mixed_regime_stable_floor_equation_source
        # object-list
        var_mixed_regime_stable_floor_equation_user_curve_name = "object-list|Mixed Regime Stable Floor Equation User Curve Name"
        obj.mixed_regime_stable_floor_equation_user_curve_name = var_mixed_regime_stable_floor_equation_user_curve_name
        # alpha
        var_mixed_regime_unstable_floor_equation_source = "BeausoleilMorrisonMixedUnstableFloor"
        obj.mixed_regime_unstable_floor_equation_source = var_mixed_regime_unstable_floor_equation_source
        # object-list
        var_mixed_regime_unstable_floor_equation_user_curve_name = "object-list|Mixed Regime Unstable Floor Equation User Curve Name"
        obj.mixed_regime_unstable_floor_equation_user_curve_name = var_mixed_regime_unstable_floor_equation_user_curve_name
        # alpha
        var_mixed_regime_stable_ceiling_equation_source = "BeausoleilMorrisonMixedStableCeiling"
        obj.mixed_regime_stable_ceiling_equation_source = var_mixed_regime_stable_ceiling_equation_source
        # object-list
        var_mixed_regime_stable_ceiling_equation_user_curve_name = "object-list|Mixed Regime Stable Ceiling Equation User Curve Name"
        obj.mixed_regime_stable_ceiling_equation_user_curve_name = var_mixed_regime_stable_ceiling_equation_user_curve_name
        # alpha
        var_mixed_regime_unstable_ceiling_equation_source = "BeausoleilMorrisonMixedUnstableCeiling"
        obj.mixed_regime_unstable_ceiling_equation_source = var_mixed_regime_unstable_ceiling_equation_source
        # object-list
        var_mixed_regime_unstable_ceiling_equation_user_curve_name = "object-list|Mixed Regime Unstable Ceiling Equation User Curve Name"
        obj.mixed_regime_unstable_ceiling_equation_user_curve_name = var_mixed_regime_unstable_ceiling_equation_user_curve_name
        # alpha
        var_mixed_regime_window_equation_source = "GoldsteinNovoselacCeilingDiffuserWindow"
        obj.mixed_regime_window_equation_source = var_mixed_regime_window_equation_source
        # object-list
        var_mixed_regime_window_equation_user_curve_name = "object-list|Mixed Regime Window Equation User Curve Name"
        obj.mixed_regime_window_equation_user_curve_name = var_mixed_regime_window_equation_user_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].name, var_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_vertical_wall_equation_source, var_simple_buoyancy_vertical_wall_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_vertical_wall_user_curve_name, var_simple_buoyancy_vertical_wall_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_stable_horizontal_equation_source, var_simple_buoyancy_stable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_stable_horizontal_equation_user_curve_name, var_simple_buoyancy_stable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_unstable_horizontal_equation_source, var_simple_buoyancy_unstable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_unstable_horizontal_equation_user_curve_name, var_simple_buoyancy_unstable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_stable_tilted_equation_source, var_simple_buoyancy_stable_tilted_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_stable_tilted_equation_user_curve_name, var_simple_buoyancy_stable_tilted_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_unstable_tilted_equation_source, var_simple_buoyancy_unstable_tilted_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_unstable_tilted_equation_user_curve_name, var_simple_buoyancy_unstable_tilted_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_windows_equation_source, var_simple_buoyancy_windows_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].simple_buoyancy_windows_equation_user_curve_name, var_simple_buoyancy_windows_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_vertical_wall_equation_source, var_floor_heat_ceiling_cool_vertical_wall_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name, var_floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_stable_horizontal_equation_source, var_floor_heat_ceiling_cool_stable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name, var_floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_unstable_horizontal_equation_source, var_floor_heat_ceiling_cool_unstable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name, var_floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_heated_floor_equation_source, var_floor_heat_ceiling_cool_heated_floor_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_heated_floor_equation_user_curve_name, var_floor_heat_ceiling_cool_heated_floor_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_chilled_ceiling_equation_source, var_floor_heat_ceiling_cool_chilled_ceiling_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name, var_floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_stable_tilted_equation_source, var_floor_heat_ceiling_cool_stable_tilted_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name, var_floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_unstable_tilted_equation_source, var_floor_heat_ceiling_cool_unstable_tilted_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name, var_floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_window_equation_source, var_floor_heat_ceiling_cool_window_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].floor_heat_ceiling_cool_window_equation_user_curve_name, var_floor_heat_ceiling_cool_window_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_vertical_wall_equation_source, var_wall_panel_heating_vertical_wall_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_vertical_wall_equation_user_curve_name, var_wall_panel_heating_vertical_wall_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_heated_wall_equation_source, var_wall_panel_heating_heated_wall_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_heated_wall_equation_user_curve_name, var_wall_panel_heating_heated_wall_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_stable_horizontal_equation_source, var_wall_panel_heating_stable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_stable_horizontal_equation_user_curve_name, var_wall_panel_heating_stable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_unstable_horizontal_equation_source, var_wall_panel_heating_unstable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_unstable_horizontal_equation_user_curve_name, var_wall_panel_heating_unstable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_stable_tilted_equation_source, var_wall_panel_heating_stable_tilted_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_stable_tilted_equation_user_curve_name, var_wall_panel_heating_stable_tilted_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_unstable_tilted_equation_source, var_wall_panel_heating_unstable_tilted_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_unstable_tilted_equation_user_curve_name, var_wall_panel_heating_unstable_tilted_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_window_equation_source, var_wall_panel_heating_window_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].wall_panel_heating_window_equation_user_curve_name, var_wall_panel_heating_window_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_vertical_wall_equation_source, var_convective_zone_heater_vertical_wall_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_vertical_wall_equation_user_curve_name, var_convective_zone_heater_vertical_wall_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_vertical_walls_near_heater_equation_source, var_convective_zone_heater_vertical_walls_near_heater_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name, var_convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_stable_horizontal_equation_source, var_convective_zone_heater_stable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_stable_horizontal_equation_user_curve_name, var_convective_zone_heater_stable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_unstable_horizontal_equation_source, var_convective_zone_heater_unstable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_unstable_horizontal_equation_user_curve_name, var_convective_zone_heater_unstable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_stable_tilted_equation_source, var_convective_zone_heater_stable_tilted_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_stable_tilted_equation_user_curve_name, var_convective_zone_heater_stable_tilted_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_unstable_tilted_equation_source, var_convective_zone_heater_unstable_tilted_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_unstable_tilted_equation_user_curve_name, var_convective_zone_heater_unstable_tilted_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_windows_equation_source, var_convective_zone_heater_windows_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].convective_zone_heater_windows_equation_user_curve_name, var_convective_zone_heater_windows_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].central_air_diffuser_wall_equation_source, var_central_air_diffuser_wall_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].central_air_diffuser_wall_equation_user_curve_name, var_central_air_diffuser_wall_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].central_air_diffuser_ceiling_equation_source, var_central_air_diffuser_ceiling_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].central_air_diffuser_ceiling_equation_user_curve_name, var_central_air_diffuser_ceiling_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].central_air_diffuser_floor_equation_source, var_central_air_diffuser_floor_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].central_air_diffuser_floor_equation_user_curve_name, var_central_air_diffuser_floor_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].central_air_diffuser_window_equation_source, var_central_air_diffuser_window_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].central_air_diffuser_window_equation_user_curve_name, var_central_air_diffuser_window_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_vertical_wall_equation_source, var_mechanical_zone_fan_circulation_vertical_wall_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name, var_mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_stable_horizontal_equation_source, var_mechanical_zone_fan_circulation_stable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name, var_mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_unstable_horizontal_equation_source, var_mechanical_zone_fan_circulation_unstable_horizontal_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name, var_mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_stable_tilted_equation_source, var_mechanical_zone_fan_circulation_stable_tilted_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name, var_mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_unstable_tilted_equation_source, var_mechanical_zone_fan_circulation_unstable_tilted_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name, var_mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_window_equation_source, var_mechanical_zone_fan_circulation_window_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mechanical_zone_fan_circulation_window_equation_user_curve_name, var_mechanical_zone_fan_circulation_window_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_buoyancy_assisting_flow_on_walls_equation_source, var_mixed_regime_buoyancy_assisting_flow_on_walls_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name, var_mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_buoyancy_opposing_flow_on_walls_equation_source, var_mixed_regime_buoyancy_opposing_flow_on_walls_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name, var_mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_stable_floor_equation_source, var_mixed_regime_stable_floor_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_stable_floor_equation_user_curve_name, var_mixed_regime_stable_floor_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_unstable_floor_equation_source, var_mixed_regime_unstable_floor_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_unstable_floor_equation_user_curve_name, var_mixed_regime_unstable_floor_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_stable_ceiling_equation_source, var_mixed_regime_stable_ceiling_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_stable_ceiling_equation_user_curve_name, var_mixed_regime_stable_ceiling_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_unstable_ceiling_equation_source, var_mixed_regime_unstable_ceiling_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_unstable_ceiling_equation_user_curve_name, var_mixed_regime_unstable_ceiling_equation_user_curve_name)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_window_equation_source, var_mixed_regime_window_equation_source)
        self.assertEqual(idf2.surfaceconvectionalgorithminsideadaptivemodelselectionss[0].mixed_regime_window_equation_user_curve_name, var_mixed_regime_window_equation_user_curve_name)