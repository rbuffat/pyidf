from collections import OrderedDict

class SurfaceConvectionAlgorithmInside(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside`
        Default indoor surface heat transfer convection algorithm to be used for all zones
    """
    internal_name = "SurfaceConvectionAlgorithm:Inside"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceConvectionAlgorithm:Inside`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="TARP"):
        """  Corresponds to IDD Field `algorithm`
        Simple = constant value natural convection (ASHRAE)
        TARP = variable natural convection based on temperature difference (ASHRAE, Walton)
        CeilingDiffuser = ACH-based forced and mixed convection correlations
        for ceiling diffuser configuration with simple natural convection limit
        AdaptiveConvectionAlgorithm = dynamic selection of convection models based on conditions

        Args:
            value (str): value for IDD Field `algorithm`
                Accepted values are:
                      - Simple
                      - TARP
                      - CeilingDiffuser
                      - AdaptiveConvectionAlgorithm
                Default value: TARP
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("Simple")
            vals.add("TARP")
            vals.add("CeilingDiffuser")
            vals.add("AdaptiveConvectionAlgorithm")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.algorithm))
        return ",".join(out)

class SurfaceConvectionAlgorithmOutside(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside`
        Default outside surface heat transfer convection algorithm to be used for all zones
    """
    internal_name = "SurfaceConvectionAlgorithm:Outside"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceConvectionAlgorithm:Outside`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="DOE-2"):
        """  Corresponds to IDD Field `algorithm`
        SimpleCombined = Combined radiation and convection coefficient using simple ASHRAE model
        TARP = correlation from models developed by ASHRAE, Walton, and Sparrow et. al.
        MoWiTT = correlation from measurements by Klems and Yazdanian for smooth surfaces
        DOE-2 = correlation from measurements by Klems and Yazdanian for rough surfaces
        AdaptiveConvectionAlgorithm = dynamic selection of correlations based on conditions

        Args:
            value (str): value for IDD Field `algorithm`
                Accepted values are:
                      - SimpleCombined
                      - TARP
                      - MoWiTT
                      - DOE-2
                      - AdaptiveConvectionAlgorithm
                Default value: DOE-2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("SimpleCombined")
            vals.add("TARP")
            vals.add("MoWiTT")
            vals.add("DOE-2")
            vals.add("AdaptiveConvectionAlgorithm")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.algorithm))
        return ",".join(out)

class SurfaceConvectionAlgorithmInsideAdaptiveModelSelections(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections`
        Options to change the individual convection model equations for dynamic selection when using AdaptiveConvectiongAlgorithm
        This object is only needed to make changes to the default model selections for any or all of the surface categories.
        This object is for the inside face, the side of the surface facing a thermal zone.
    """
    internal_name = "SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections"
    field_count = 91

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Simple Bouyancy Vertical Wall Equation Source"] = None
        self._data["Simple Bouyancy Vertical Wall User Curve Name"] = None
        self._data["Simple Bouyancy Stable Horizontal Equation Source"] = None
        self._data["Simple Bouyancy Stable Horizontal Equation User Curve Name"] = None
        self._data["Simple Bouyancy Unstable Horizontal Equation Source"] = None
        self._data["Simple Bouyancy Unstable Horizontal Equation User Curve Name"] = None
        self._data["Simple Bouyancy Stable Tilted Equation Source"] = None
        self._data["Simple Bouyancy Stable Tilted Equation User Curve Name"] = None
        self._data["Simple Bouyancy Unstable Tilted Equation Source"] = None
        self._data["Simple Bouyancy Unstable Tilted Equation User Curve Name"] = None
        self._data["Simple Bouyancy Windows Equation Source"] = None
        self._data["Simple Bouyancy Windows Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Vertical Wall Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Stable Horizontal Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Heated Floor Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Heated Floor Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Stable Tilted Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Unstable Tilted Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Window Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Window Equation User Curve Name"] = None
        self._data["Wall Panel Heating Vertical Wall Equation Source"] = None
        self._data["Wall Panel Heating Vertical Wall Equation User Curve Name"] = None
        self._data["Wall Panel Heating Heated Wall Equation Source"] = None
        self._data["Wall Panel Heating Heated Wall Equation User Curve Name"] = None
        self._data["Wall Panel Heating Stable Horizontal Equation Source"] = None
        self._data["Wall Panel Heating Stable Horizontal Equation User Curve Name"] = None
        self._data["Wall Panel Heating Unstable Horizontal Equation Source"] = None
        self._data["Wall Panel Heating Unstable Horizontal Equation User Curve Name"] = None
        self._data["Wall Panel Heating Stable Tilted Equation Source"] = None
        self._data["Wall Panel Heating Stable Tilted Equation User Curve Name"] = None
        self._data["Wall Panel Heating Unstable Tilted Equation Source"] = None
        self._data["Wall Panel Heating Unstable Tilted Equation User Curve Name"] = None
        self._data["Wall Panel Heating Window Equation Source"] = None
        self._data["Wall Panel Heating Window Equation User Curve Name"] = None
        self._data["Convective Zone Heater Vertical Wall Equation Source"] = None
        self._data["Convective Zone Heater Vertical Wall Equation User Curve Name"] = None
        self._data["Convective Zone Heater Vertical Walls Near Heater Equation Source"] = None
        self._data["Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name"] = None
        self._data["Convective Zone Heater Stable Horizontal Equation Source"] = None
        self._data["Convective Zone Heater Stable Horizontal Equation User Curve Name"] = None
        self._data["Convective Zone Heater Unstable Horizontal Equation Source"] = None
        self._data["Convective Zone Heater Unstable Horizontal Equation User Curve Name"] = None
        self._data["Convective Zone Heater Stable Tilted Equation Source"] = None
        self._data["Convective Zone Heater Stable Tilted Equation User Curve Name"] = None
        self._data["Convective Zone Heater Unstable Tilted Equation Source"] = None
        self._data["Convective Zone Heater Unstable Tilted Equation User Curve Name"] = None
        self._data["Convective Zone Heater Windows Equation Source"] = None
        self._data["Convective Zone Heater Windows Equation User Curve Name"] = None
        self._data["Central Air Diffuser Wall Equation Source"] = None
        self._data["Central Air Diffuser Wall Equation User Curve Name"] = None
        self._data["Central Air Diffuser Ceiling Equation Source"] = None
        self._data["Central Air Diffuser Ceiling Equation User Curve Name"] = None
        self._data["Central Air Diffuser Floor Equation Source"] = None
        self._data["Central Air Diffuser Floor Equation User Curve Name"] = None
        self._data["Central Air Diffuser Window Equation Source"] = None
        self._data["Central Air Diffuser Window Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Vertical Wall Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Stable Tilted Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Window Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Window Equation User Curve Name"] = None
        self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation Source"] = None
        self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation User Curve Name"] = None
        self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation Source"] = None
        self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation User Curve Name"] = None
        self._data["Mixed Regime Stable Floor Equation Source"] = None
        self._data["Mixed Regime Stable Floor Equation User Curve Name"] = None
        self._data["Mixed Regime Unstable Floor Equation Source"] = None
        self._data["Mixed Regime Unstable Floor Equation User Curve Name"] = None
        self._data["Mixed Regime Stable Ceiling Equation Source"] = None
        self._data["Mixed Regime Stable Ceiling Equation User Curve Name"] = None
        self._data["Mixed Regime Unstable Ceiling Equation Source"] = None
        self._data["Mixed Regime Unstable Ceiling Equation User Curve Name"] = None
        self._data["Mixed Regime Window Equation Source"] = None
        self._data["Mixed Regime Window Equation User Curve Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_vertical_wall_equation_source = None
        else:
            self.simple_bouyancy_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_vertical_wall_user_curve_name = None
        else:
            self.simple_bouyancy_vertical_wall_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_horizontal_equation_source = None
        else:
            self.simple_bouyancy_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_horizontal_equation_user_curve_name = None
        else:
            self.simple_bouyancy_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_horizontal_equation_source = None
        else:
            self.simple_bouyancy_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_horizontal_equation_user_curve_name = None
        else:
            self.simple_bouyancy_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_tilted_equation_source = None
        else:
            self.simple_bouyancy_stable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_tilted_equation_user_curve_name = None
        else:
            self.simple_bouyancy_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_tilted_equation_source = None
        else:
            self.simple_bouyancy_unstable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_tilted_equation_user_curve_name = None
        else:
            self.simple_bouyancy_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_windows_equation_source = None
        else:
            self.simple_bouyancy_windows_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_windows_equation_user_curve_name = None
        else:
            self.simple_bouyancy_windows_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_vertical_wall_equation_source = None
        else:
            self.floor_heat_ceiling_cool_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_source = None
        else:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_source = None
        else:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_heated_floor_equation_source = None
        else:
            self.floor_heat_ceiling_cool_heated_floor_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_source = None
        else:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_tilted_equation_source = None
        else:
            self.floor_heat_ceiling_cool_stable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_source = None
        else:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_window_equation_source = None
        else:
            self.floor_heat_ceiling_cool_window_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_window_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_window_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_vertical_wall_equation_source = None
        else:
            self.wall_panel_heating_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_vertical_wall_equation_user_curve_name = None
        else:
            self.wall_panel_heating_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_heated_wall_equation_source = None
        else:
            self.wall_panel_heating_heated_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_heated_wall_equation_user_curve_name = None
        else:
            self.wall_panel_heating_heated_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_horizontal_equation_source = None
        else:
            self.wall_panel_heating_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_horizontal_equation_user_curve_name = None
        else:
            self.wall_panel_heating_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_horizontal_equation_source = None
        else:
            self.wall_panel_heating_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_horizontal_equation_user_curve_name = None
        else:
            self.wall_panel_heating_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_tilted_equation_source = None
        else:
            self.wall_panel_heating_stable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_tilted_equation_user_curve_name = None
        else:
            self.wall_panel_heating_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_tilted_equation_source = None
        else:
            self.wall_panel_heating_unstable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_tilted_equation_user_curve_name = None
        else:
            self.wall_panel_heating_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_window_equation_source = None
        else:
            self.wall_panel_heating_window_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_window_equation_user_curve_name = None
        else:
            self.wall_panel_heating_window_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_wall_equation_source = None
        else:
            self.convective_zone_heater_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_wall_equation_user_curve_name = None
        else:
            self.convective_zone_heater_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_walls_near_heater_equation_source = None
        else:
            self.convective_zone_heater_vertical_walls_near_heater_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name = None
        else:
            self.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_horizontal_equation_source = None
        else:
            self.convective_zone_heater_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_horizontal_equation_user_curve_name = None
        else:
            self.convective_zone_heater_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_horizontal_equation_source = None
        else:
            self.convective_zone_heater_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_horizontal_equation_user_curve_name = None
        else:
            self.convective_zone_heater_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_tilted_equation_source = None
        else:
            self.convective_zone_heater_stable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_tilted_equation_user_curve_name = None
        else:
            self.convective_zone_heater_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_tilted_equation_source = None
        else:
            self.convective_zone_heater_unstable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_tilted_equation_user_curve_name = None
        else:
            self.convective_zone_heater_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_windows_equation_source = None
        else:
            self.convective_zone_heater_windows_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_windows_equation_user_curve_name = None
        else:
            self.convective_zone_heater_windows_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_wall_equation_source = None
        else:
            self.central_air_diffuser_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_wall_equation_user_curve_name = None
        else:
            self.central_air_diffuser_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_ceiling_equation_source = None
        else:
            self.central_air_diffuser_ceiling_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_ceiling_equation_user_curve_name = None
        else:
            self.central_air_diffuser_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_floor_equation_source = None
        else:
            self.central_air_diffuser_floor_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_floor_equation_user_curve_name = None
        else:
            self.central_air_diffuser_floor_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_window_equation_source = None
        else:
            self.central_air_diffuser_window_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_window_equation_user_curve_name = None
        else:
            self.central_air_diffuser_window_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_window_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_window_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_window_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_window_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source = None
        else:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name = None
        else:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source = None
        else:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name = None
        else:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_stable_floor_equation_source = None
        else:
            self.mixed_regime_stable_floor_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_stable_floor_equation_user_curve_name = None
        else:
            self.mixed_regime_stable_floor_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_floor_equation_source = None
        else:
            self.mixed_regime_unstable_floor_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_floor_equation_user_curve_name = None
        else:
            self.mixed_regime_unstable_floor_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_stable_ceiling_equation_source = None
        else:
            self.mixed_regime_stable_ceiling_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_stable_ceiling_equation_user_curve_name = None
        else:
            self.mixed_regime_stable_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_ceiling_equation_source = None
        else:
            self.mixed_regime_unstable_ceiling_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_ceiling_equation_user_curve_name = None
        else:
            self.mixed_regime_unstable_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_window_equation_source = None
        else:
            self.mixed_regime_window_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_window_equation_user_curve_name = None
        else:
            self.mixed_regime_window_equation_user_curve_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def simple_bouyancy_vertical_wall_equation_source(self):
        """Get simple_bouyancy_vertical_wall_equation_source

        Returns:
            str: the value of `simple_bouyancy_vertical_wall_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Vertical Wall Equation Source"]

    @simple_bouyancy_vertical_wall_equation_source.setter
    def simple_bouyancy_vertical_wall_equation_source(self, value="FohannoPolidoriVerticalWall"):
        """  Corresponds to IDD Field `simple_bouyancy_vertical_wall_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for vertical walls

        Args:
            value (str): value for IDD Field `simple_bouyancy_vertical_wall_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - KhalifaEq6NonHeatedWalls
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: FohannoPolidoriVerticalWall
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_vertical_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("KhalifaEq6NonHeatedWalls")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_vertical_wall_equation_source`'.format(value))

        self._data["Simple Bouyancy Vertical Wall Equation Source"] = value

    @property
    def simple_bouyancy_vertical_wall_user_curve_name(self):
        """Get simple_bouyancy_vertical_wall_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_vertical_wall_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Vertical Wall User Curve Name"]

    @simple_bouyancy_vertical_wall_user_curve_name.setter
    def simple_bouyancy_vertical_wall_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `simple_bouyancy_vertical_wall_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_vertical_wall_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_vertical_wall_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_vertical_wall_user_curve_name`')

        self._data["Simple Bouyancy Vertical Wall User Curve Name"] = value

    @property
    def simple_bouyancy_stable_horizontal_equation_source(self):
        """Get simple_bouyancy_stable_horizontal_equation_source

        Returns:
            str: the value of `simple_bouyancy_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Stable Horizontal Equation Source"]

    @simple_bouyancy_stable_horizontal_equation_source.setter
    def simple_bouyancy_stable_horizontal_equation_source(self, value="AlamdariHammondStableHorizontal"):
        """  Corresponds to IDD Field `simple_bouyancy_stable_horizontal_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `simple_bouyancy_stable_horizontal_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: AlamdariHammondStableHorizontal
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_stable_horizontal_equation_source`'.format(value))

        self._data["Simple Bouyancy Stable Horizontal Equation Source"] = value

    @property
    def simple_bouyancy_stable_horizontal_equation_user_curve_name(self):
        """Get simple_bouyancy_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Stable Horizontal Equation User Curve Name"]

    @simple_bouyancy_stable_horizontal_equation_user_curve_name.setter
    def simple_bouyancy_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `simple_bouyancy_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_stable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_stable_horizontal_equation_user_curve_name`')

        self._data["Simple Bouyancy Stable Horizontal Equation User Curve Name"] = value

    @property
    def simple_bouyancy_unstable_horizontal_equation_source(self):
        """Get simple_bouyancy_unstable_horizontal_equation_source

        Returns:
            str: the value of `simple_bouyancy_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Unstable Horizontal Equation Source"]

    @simple_bouyancy_unstable_horizontal_equation_source.setter
    def simple_bouyancy_unstable_horizontal_equation_source(self, value="AlamdariHammondUnstableHorizontal"):
        """  Corresponds to IDD Field `simple_bouyancy_unstable_horizontal_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for passive horizontal surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `simple_bouyancy_unstable_horizontal_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: AlamdariHammondUnstableHorizontal
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_unstable_horizontal_equation_source`'.format(value))

        self._data["Simple Bouyancy Unstable Horizontal Equation Source"] = value

    @property
    def simple_bouyancy_unstable_horizontal_equation_user_curve_name(self):
        """Get simple_bouyancy_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Unstable Horizontal Equation User Curve Name"]

    @simple_bouyancy_unstable_horizontal_equation_user_curve_name.setter
    def simple_bouyancy_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `simple_bouyancy_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_unstable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_unstable_horizontal_equation_user_curve_name`')

        self._data["Simple Bouyancy Unstable Horizontal Equation User Curve Name"] = value

    @property
    def simple_bouyancy_stable_tilted_equation_source(self):
        """Get simple_bouyancy_stable_tilted_equation_source

        Returns:
            str: the value of `simple_bouyancy_stable_tilted_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Stable Tilted Equation Source"]

    @simple_bouyancy_stable_tilted_equation_source.setter
    def simple_bouyancy_stable_tilted_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `simple_bouyancy_stable_tilted_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `simple_bouyancy_stable_tilted_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: WaltonStableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_stable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_stable_tilted_equation_source`'.format(value))

        self._data["Simple Bouyancy Stable Tilted Equation Source"] = value

    @property
    def simple_bouyancy_stable_tilted_equation_user_curve_name(self):
        """Get simple_bouyancy_stable_tilted_equation_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_stable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Stable Tilted Equation User Curve Name"]

    @simple_bouyancy_stable_tilted_equation_user_curve_name.setter
    def simple_bouyancy_stable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `simple_bouyancy_stable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_stable_tilted_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_stable_tilted_equation_user_curve_name`')

        self._data["Simple Bouyancy Stable Tilted Equation User Curve Name"] = value

    @property
    def simple_bouyancy_unstable_tilted_equation_source(self):
        """Get simple_bouyancy_unstable_tilted_equation_source

        Returns:
            str: the value of `simple_bouyancy_unstable_tilted_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Unstable Tilted Equation Source"]

    @simple_bouyancy_unstable_tilted_equation_source.setter
    def simple_bouyancy_unstable_tilted_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `simple_bouyancy_unstable_tilted_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `simple_bouyancy_unstable_tilted_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: WaltonUnstableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_unstable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_unstable_tilted_equation_source`'.format(value))

        self._data["Simple Bouyancy Unstable Tilted Equation Source"] = value

    @property
    def simple_bouyancy_unstable_tilted_equation_user_curve_name(self):
        """Get simple_bouyancy_unstable_tilted_equation_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_unstable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Unstable Tilted Equation User Curve Name"]

    @simple_bouyancy_unstable_tilted_equation_user_curve_name.setter
    def simple_bouyancy_unstable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `simple_bouyancy_unstable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_unstable_tilted_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_unstable_tilted_equation_user_curve_name`')

        self._data["Simple Bouyancy Unstable Tilted Equation User Curve Name"] = value

    @property
    def simple_bouyancy_windows_equation_source(self):
        """Get simple_bouyancy_windows_equation_source

        Returns:
            str: the value of `simple_bouyancy_windows_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Windows Equation Source"]

    @simple_bouyancy_windows_equation_source.setter
    def simple_bouyancy_windows_equation_source(self, value="ISO15099Windows"):
        """  Corresponds to IDD Field `simple_bouyancy_windows_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `simple_bouyancy_windows_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - KaradagChilledCeiling
                      - ISO15099Windows
                      - UserCurve
                Default value: ISO15099Windows
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_windows_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_windows_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("KaradagChilledCeiling")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_windows_equation_source`'.format(value))

        self._data["Simple Bouyancy Windows Equation Source"] = value

    @property
    def simple_bouyancy_windows_equation_user_curve_name(self):
        """Get simple_bouyancy_windows_equation_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_windows_equation_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Windows Equation User Curve Name"]

    @simple_bouyancy_windows_equation_user_curve_name.setter
    def simple_bouyancy_windows_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `simple_bouyancy_windows_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_windows_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_windows_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_windows_equation_user_curve_name`')

        self._data["Simple Bouyancy Windows Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_vertical_wall_equation_source(self):
        """Get floor_heat_ceiling_cool_vertical_wall_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_vertical_wall_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Vertical Wall Equation Source"]

    @floor_heat_ceiling_cool_vertical_wall_equation_source.setter
    def floor_heat_ceiling_cool_vertical_wall_equation_source(self, value="KhalifaEq3WallAwayFromHeat"):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_vertical_wall_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for vertical walls

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_vertical_wall_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: KhalifaEq3WallAwayFromHeat
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_vertical_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_vertical_wall_equation_source`'.format(value))

        self._data["Floor Heat Ceiling Cool Vertical Wall Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name"]

    @floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`')

        self._data["Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_stable_horizontal_equation_source(self):
        """Get floor_heat_ceiling_cool_stable_horizontal_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Stable Horizontal Equation Source"]

    @floor_heat_ceiling_cool_stable_horizontal_equation_source.setter
    def floor_heat_ceiling_cool_stable_horizontal_equation_source(self, value="AlamdariHammondStableHorizontal"):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_stable_horizontal_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for passive horizontal surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_stable_horizontal_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: AlamdariHammondStableHorizontal
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_stable_horizontal_equation_source`'.format(value))

        self._data["Floor Heat Ceiling Cool Stable Horizontal Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name"]

    @floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`')

        self._data["Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_unstable_horizontal_equation_source(self):
        """Get floor_heat_ceiling_cool_unstable_horizontal_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation Source"]

    @floor_heat_ceiling_cool_unstable_horizontal_equation_source.setter
    def floor_heat_ceiling_cool_unstable_horizontal_equation_source(self, value="KhalifaEq4CeilingAwayFromHeat"):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_unstable_horizontal_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for passive horizontal surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_unstable_horizontal_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - KhalifaEq4CeilingAwayFromHeat
                      - UserCurve
                Default value: KhalifaEq4CeilingAwayFromHeat
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("KhalifaEq4CeilingAwayFromHeat")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_unstable_horizontal_equation_source`'.format(value))

        self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name"]

    @floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`')

        self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_heated_floor_equation_source(self):
        """Get floor_heat_ceiling_cool_heated_floor_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_heated_floor_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Heated Floor Equation Source"]

    @floor_heat_ceiling_cool_heated_floor_equation_source.setter
    def floor_heat_ceiling_cool_heated_floor_equation_source(self, value="AwbiHattonHeatedFloor"):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_heated_floor_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for a floor with active heating elements

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_heated_floor_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - AwbiHattonHeatedFloor
                      - UserCurve
                Default value: AwbiHattonHeatedFloor
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_heated_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_heated_floor_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("AwbiHattonHeatedFloor")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_heated_floor_equation_source`'.format(value))

        self._data["Floor Heat Ceiling Cool Heated Floor Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_heated_floor_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_heated_floor_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Heated Floor Equation User Curve Name"]

    @floor_heat_ceiling_cool_heated_floor_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_heated_floor_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`')

        self._data["Floor Heat Ceiling Cool Heated Floor Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_chilled_ceiling_equation_source(self):
        """Get floor_heat_ceiling_cool_chilled_ceiling_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_chilled_ceiling_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation Source"]

    @floor_heat_ceiling_cool_chilled_ceiling_equation_source.setter
    def floor_heat_ceiling_cool_chilled_ceiling_equation_source(self, value="KaradagChilledCeiling"):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_chilled_ceiling_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for a ceiling with active cooling elements

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_chilled_ceiling_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - KaradagChilledCeiling
                      - UserCurve
                Default value: KaradagChilledCeiling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_chilled_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_chilled_ceiling_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("KaradagChilledCeiling")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_chilled_ceiling_equation_source`'.format(value))

        self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name"]

    @floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`')

        self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_stable_tilted_equation_source(self):
        """Get floor_heat_ceiling_cool_stable_tilted_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_tilted_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Stable Tilted Equation Source"]

    @floor_heat_ceiling_cool_stable_tilted_equation_source.setter
    def floor_heat_ceiling_cool_stable_tilted_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_stable_tilted_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_stable_tilted_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - ISO15099Windows
                      - UserCurve
                Default value: WaltonStableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_stable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_stable_tilted_equation_source`'.format(value))

        self._data["Floor Heat Ceiling Cool Stable Tilted Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name"]

    @floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`')

        self._data["Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_unstable_tilted_equation_source(self):
        """Get floor_heat_ceiling_cool_unstable_tilted_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_tilted_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Unstable Tilted Equation Source"]

    @floor_heat_ceiling_cool_unstable_tilted_equation_source.setter
    def floor_heat_ceiling_cool_unstable_tilted_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_unstable_tilted_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_unstable_tilted_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - ISO15099Windows
                      - UserCurve
                Default value: WaltonUnstableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_unstable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_unstable_tilted_equation_source`'.format(value))

        self._data["Floor Heat Ceiling Cool Unstable Tilted Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name"]

    @floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`')

        self._data["Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_window_equation_source(self):
        """Get floor_heat_ceiling_cool_window_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_window_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Window Equation Source"]

    @floor_heat_ceiling_cool_window_equation_source.setter
    def floor_heat_ceiling_cool_window_equation_source(self, value="ISO15099Windows"):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_window_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_window_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: ISO15099Windows
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_window_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_window_equation_source`'.format(value))

        self._data["Floor Heat Ceiling Cool Window Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_window_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_window_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_window_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Window Equation User Curve Name"]

    @floor_heat_ceiling_cool_window_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_window_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_window_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_window_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_window_equation_user_curve_name`')

        self._data["Floor Heat Ceiling Cool Window Equation User Curve Name"] = value

    @property
    def wall_panel_heating_vertical_wall_equation_source(self):
        """Get wall_panel_heating_vertical_wall_equation_source

        Returns:
            str: the value of `wall_panel_heating_vertical_wall_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Vertical Wall Equation Source"]

    @wall_panel_heating_vertical_wall_equation_source.setter
    def wall_panel_heating_vertical_wall_equation_source(self, value="KhalifaEq6NonHeatedWalls"):
        """  Corresponds to IDD Field `wall_panel_heating_vertical_wall_equation_source`
        Applies to zone with in-wall panel heating
        This is for vertical walls that are not actively heated

        Args:
            value (str): value for IDD Field `wall_panel_heating_vertical_wall_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq6NonHeatedWalls
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: KhalifaEq6NonHeatedWalls
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_vertical_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq6NonHeatedWalls")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_vertical_wall_equation_source`'.format(value))

        self._data["Wall Panel Heating Vertical Wall Equation Source"] = value

    @property
    def wall_panel_heating_vertical_wall_equation_user_curve_name(self):
        """Get wall_panel_heating_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Vertical Wall Equation User Curve Name"]

    @wall_panel_heating_vertical_wall_equation_user_curve_name.setter
    def wall_panel_heating_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `wall_panel_heating_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_vertical_wall_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_vertical_wall_equation_user_curve_name`')

        self._data["Wall Panel Heating Vertical Wall Equation User Curve Name"] = value

    @property
    def wall_panel_heating_heated_wall_equation_source(self):
        """Get wall_panel_heating_heated_wall_equation_source

        Returns:
            str: the value of `wall_panel_heating_heated_wall_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Heated Wall Equation Source"]

    @wall_panel_heating_heated_wall_equation_source.setter
    def wall_panel_heating_heated_wall_equation_source(self, value="AwbiHattonHeatedWall"):
        """  Corresponds to IDD Field `wall_panel_heating_heated_wall_equation_source`
        Applies to zone with in-wall panel heating
        This is for vertical walls that are being actively heated

        Args:
            value (str): value for IDD Field `wall_panel_heating_heated_wall_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq5WallNearHeat
                      - AwbiHattonHeatedWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: AwbiHattonHeatedWall
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_heated_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_heated_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq5WallNearHeat")
            vals.add("AwbiHattonHeatedWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_heated_wall_equation_source`'.format(value))

        self._data["Wall Panel Heating Heated Wall Equation Source"] = value

    @property
    def wall_panel_heating_heated_wall_equation_user_curve_name(self):
        """Get wall_panel_heating_heated_wall_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_heated_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Heated Wall Equation User Curve Name"]

    @wall_panel_heating_heated_wall_equation_user_curve_name.setter
    def wall_panel_heating_heated_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `wall_panel_heating_heated_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_heated_wall_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_heated_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_heated_wall_equation_user_curve_name`')

        self._data["Wall Panel Heating Heated Wall Equation User Curve Name"] = value

    @property
    def wall_panel_heating_stable_horizontal_equation_source(self):
        """Get wall_panel_heating_stable_horizontal_equation_source

        Returns:
            str: the value of `wall_panel_heating_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Stable Horizontal Equation Source"]

    @wall_panel_heating_stable_horizontal_equation_source.setter
    def wall_panel_heating_stable_horizontal_equation_source(self, value="AlamdariHammondStableHorizontal"):
        """  Corresponds to IDD Field `wall_panel_heating_stable_horizontal_equation_source`
        Applies to zone with in-wall panel heating
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `wall_panel_heating_stable_horizontal_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: AlamdariHammondStableHorizontal
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_stable_horizontal_equation_source`'.format(value))

        self._data["Wall Panel Heating Stable Horizontal Equation Source"] = value

    @property
    def wall_panel_heating_stable_horizontal_equation_user_curve_name(self):
        """Get wall_panel_heating_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Stable Horizontal Equation User Curve Name"]

    @wall_panel_heating_stable_horizontal_equation_user_curve_name.setter
    def wall_panel_heating_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `wall_panel_heating_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_stable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_stable_horizontal_equation_user_curve_name`')

        self._data["Wall Panel Heating Stable Horizontal Equation User Curve Name"] = value

    @property
    def wall_panel_heating_unstable_horizontal_equation_source(self):
        """Get wall_panel_heating_unstable_horizontal_equation_source

        Returns:
            str: the value of `wall_panel_heating_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Unstable Horizontal Equation Source"]

    @wall_panel_heating_unstable_horizontal_equation_source.setter
    def wall_panel_heating_unstable_horizontal_equation_source(self, value="KhalifaEq7Ceiling"):
        """  Corresponds to IDD Field `wall_panel_heating_unstable_horizontal_equation_source`
        Applies to zone with in-wall panel heating
        This is for horizontal surfaces with heat flow directed for unstable thermal stratification

        Args:
            value (str): value for IDD Field `wall_panel_heating_unstable_horizontal_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - KhalifaEq7Ceiling
                      - KaradagChilledCeiling
                      - UserCurve
                Default value: KhalifaEq7Ceiling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("KhalifaEq7Ceiling")
            vals.add("KaradagChilledCeiling")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_unstable_horizontal_equation_source`'.format(value))

        self._data["Wall Panel Heating Unstable Horizontal Equation Source"] = value

    @property
    def wall_panel_heating_unstable_horizontal_equation_user_curve_name(self):
        """Get wall_panel_heating_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Unstable Horizontal Equation User Curve Name"]

    @wall_panel_heating_unstable_horizontal_equation_user_curve_name.setter
    def wall_panel_heating_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `wall_panel_heating_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_unstable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_unstable_horizontal_equation_user_curve_name`')

        self._data["Wall Panel Heating Unstable Horizontal Equation User Curve Name"] = value

    @property
    def wall_panel_heating_stable_tilted_equation_source(self):
        """Get wall_panel_heating_stable_tilted_equation_source

        Returns:
            str: the value of `wall_panel_heating_stable_tilted_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Stable Tilted Equation Source"]

    @wall_panel_heating_stable_tilted_equation_source.setter
    def wall_panel_heating_stable_tilted_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `wall_panel_heating_stable_tilted_equation_source`
        Applies to zone with in-wall panel heating
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `wall_panel_heating_stable_tilted_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - ISO15099Windows
                      - UserCurve
                Default value: WaltonStableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_stable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_stable_tilted_equation_source`'.format(value))

        self._data["Wall Panel Heating Stable Tilted Equation Source"] = value

    @property
    def wall_panel_heating_stable_tilted_equation_user_curve_name(self):
        """Get wall_panel_heating_stable_tilted_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_stable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Stable Tilted Equation User Curve Name"]

    @wall_panel_heating_stable_tilted_equation_user_curve_name.setter
    def wall_panel_heating_stable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `wall_panel_heating_stable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_stable_tilted_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_stable_tilted_equation_user_curve_name`')

        self._data["Wall Panel Heating Stable Tilted Equation User Curve Name"] = value

    @property
    def wall_panel_heating_unstable_tilted_equation_source(self):
        """Get wall_panel_heating_unstable_tilted_equation_source

        Returns:
            str: the value of `wall_panel_heating_unstable_tilted_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Unstable Tilted Equation Source"]

    @wall_panel_heating_unstable_tilted_equation_source.setter
    def wall_panel_heating_unstable_tilted_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `wall_panel_heating_unstable_tilted_equation_source`
        Applies to zone with in-wall panel heating
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `wall_panel_heating_unstable_tilted_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - ISO15099Windows
                      - UserCurve
                Default value: WaltonUnstableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_unstable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_unstable_tilted_equation_source`'.format(value))

        self._data["Wall Panel Heating Unstable Tilted Equation Source"] = value

    @property
    def wall_panel_heating_unstable_tilted_equation_user_curve_name(self):
        """Get wall_panel_heating_unstable_tilted_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_unstable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Unstable Tilted Equation User Curve Name"]

    @wall_panel_heating_unstable_tilted_equation_user_curve_name.setter
    def wall_panel_heating_unstable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `wall_panel_heating_unstable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_unstable_tilted_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_unstable_tilted_equation_user_curve_name`')

        self._data["Wall Panel Heating Unstable Tilted Equation User Curve Name"] = value

    @property
    def wall_panel_heating_window_equation_source(self):
        """Get wall_panel_heating_window_equation_source

        Returns:
            str: the value of `wall_panel_heating_window_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Window Equation Source"]

    @wall_panel_heating_window_equation_source.setter
    def wall_panel_heating_window_equation_source(self, value="ISO15099Windows"):
        """  Corresponds to IDD Field `wall_panel_heating_window_equation_source`
        Applies to zone with in-wall panel heating
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `wall_panel_heating_window_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: ISO15099Windows
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_window_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_window_equation_source`'.format(value))

        self._data["Wall Panel Heating Window Equation Source"] = value

    @property
    def wall_panel_heating_window_equation_user_curve_name(self):
        """Get wall_panel_heating_window_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_window_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Window Equation User Curve Name"]

    @wall_panel_heating_window_equation_user_curve_name.setter
    def wall_panel_heating_window_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `wall_panel_heating_window_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_window_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_window_equation_user_curve_name`')

        self._data["Wall Panel Heating Window Equation User Curve Name"] = value

    @property
    def convective_zone_heater_vertical_wall_equation_source(self):
        """Get convective_zone_heater_vertical_wall_equation_source

        Returns:
            str: the value of `convective_zone_heater_vertical_wall_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Vertical Wall Equation Source"]

    @convective_zone_heater_vertical_wall_equation_source.setter
    def convective_zone_heater_vertical_wall_equation_source(self, value="FohannoPolidoriVerticalWall"):
        """  Corresponds to IDD Field `convective_zone_heater_vertical_wall_equation_source`
        Applies to zone with convective heater
        This is for vertical walls not directly affected by heater

        Args:
            value (str): value for IDD Field `convective_zone_heater_vertical_wall_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - KhalifaEq6NonHeatedWalls
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: FohannoPolidoriVerticalWall
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_vertical_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("KhalifaEq6NonHeatedWalls")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_vertical_wall_equation_source`'.format(value))

        self._data["Convective Zone Heater Vertical Wall Equation Source"] = value

    @property
    def convective_zone_heater_vertical_wall_equation_user_curve_name(self):
        """Get convective_zone_heater_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Vertical Wall Equation User Curve Name"]

    @convective_zone_heater_vertical_wall_equation_user_curve_name.setter
    def convective_zone_heater_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `convective_zone_heater_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_vertical_wall_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_vertical_wall_equation_user_curve_name`')

        self._data["Convective Zone Heater Vertical Wall Equation User Curve Name"] = value

    @property
    def convective_zone_heater_vertical_walls_near_heater_equation_source(self):
        """Get convective_zone_heater_vertical_walls_near_heater_equation_source

        Returns:
            str: the value of `convective_zone_heater_vertical_walls_near_heater_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Vertical Walls Near Heater Equation Source"]

    @convective_zone_heater_vertical_walls_near_heater_equation_source.setter
    def convective_zone_heater_vertical_walls_near_heater_equation_source(self, value="KhalifaEq5WallNearHeat"):
        """  Corresponds to IDD Field `convective_zone_heater_vertical_walls_near_heater_equation_source`
        Applies to zone with convective heater
        This is for vertical walls that are directly affected by heater
        Walls are considered "near" when listed in field set for Fraction of Radiant Energy to Surface

        Args:
            value (str): value for IDD Field `convective_zone_heater_vertical_walls_near_heater_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq5WallNearHeat
                      - AwbiHattonHeatedWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: KhalifaEq5WallNearHeat
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_vertical_walls_near_heater_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_vertical_walls_near_heater_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq5WallNearHeat")
            vals.add("AwbiHattonHeatedWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_vertical_walls_near_heater_equation_source`'.format(value))

        self._data["Convective Zone Heater Vertical Walls Near Heater Equation Source"] = value

    @property
    def convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name(self):
        """Get convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name"]

    @convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name.setter
    def convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`')

        self._data["Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name"] = value

    @property
    def convective_zone_heater_stable_horizontal_equation_source(self):
        """Get convective_zone_heater_stable_horizontal_equation_source

        Returns:
            str: the value of `convective_zone_heater_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Stable Horizontal Equation Source"]

    @convective_zone_heater_stable_horizontal_equation_source.setter
    def convective_zone_heater_stable_horizontal_equation_source(self, value="AlamdariHammondStableHorizontal"):
        """  Corresponds to IDD Field `convective_zone_heater_stable_horizontal_equation_source`
        Applies to zone with convective heater
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `convective_zone_heater_stable_horizontal_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: AlamdariHammondStableHorizontal
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_stable_horizontal_equation_source`'.format(value))

        self._data["Convective Zone Heater Stable Horizontal Equation Source"] = value

    @property
    def convective_zone_heater_stable_horizontal_equation_user_curve_name(self):
        """Get convective_zone_heater_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Stable Horizontal Equation User Curve Name"]

    @convective_zone_heater_stable_horizontal_equation_user_curve_name.setter
    def convective_zone_heater_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `convective_zone_heater_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_stable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_stable_horizontal_equation_user_curve_name`')

        self._data["Convective Zone Heater Stable Horizontal Equation User Curve Name"] = value

    @property
    def convective_zone_heater_unstable_horizontal_equation_source(self):
        """Get convective_zone_heater_unstable_horizontal_equation_source

        Returns:
            str: the value of `convective_zone_heater_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Unstable Horizontal Equation Source"]

    @convective_zone_heater_unstable_horizontal_equation_source.setter
    def convective_zone_heater_unstable_horizontal_equation_source(self, value="KhalifaEq7Ceiling"):
        """  Corresponds to IDD Field `convective_zone_heater_unstable_horizontal_equation_source`
        Applies to zone with convective heater
        This is for horizontal surfaces with heat flow directed for unstable thermal stratification

        Args:
            value (str): value for IDD Field `convective_zone_heater_unstable_horizontal_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - KhalifaEq4CeilingAwayFromHeat
                      - KhalifaEq7Ceiling
                      - UserCurve
                Default value: KhalifaEq7Ceiling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("KhalifaEq4CeilingAwayFromHeat")
            vals.add("KhalifaEq7Ceiling")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_unstable_horizontal_equation_source`'.format(value))

        self._data["Convective Zone Heater Unstable Horizontal Equation Source"] = value

    @property
    def convective_zone_heater_unstable_horizontal_equation_user_curve_name(self):
        """Get convective_zone_heater_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Unstable Horizontal Equation User Curve Name"]

    @convective_zone_heater_unstable_horizontal_equation_user_curve_name.setter
    def convective_zone_heater_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `convective_zone_heater_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_unstable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_unstable_horizontal_equation_user_curve_name`')

        self._data["Convective Zone Heater Unstable Horizontal Equation User Curve Name"] = value

    @property
    def convective_zone_heater_stable_tilted_equation_source(self):
        """Get convective_zone_heater_stable_tilted_equation_source

        Returns:
            str: the value of `convective_zone_heater_stable_tilted_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Stable Tilted Equation Source"]

    @convective_zone_heater_stable_tilted_equation_source.setter
    def convective_zone_heater_stable_tilted_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `convective_zone_heater_stable_tilted_equation_source`
        Applies to zone with convective heater
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `convective_zone_heater_stable_tilted_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: WaltonStableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_stable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_stable_tilted_equation_source`'.format(value))

        self._data["Convective Zone Heater Stable Tilted Equation Source"] = value

    @property
    def convective_zone_heater_stable_tilted_equation_user_curve_name(self):
        """Get convective_zone_heater_stable_tilted_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_stable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Stable Tilted Equation User Curve Name"]

    @convective_zone_heater_stable_tilted_equation_user_curve_name.setter
    def convective_zone_heater_stable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `convective_zone_heater_stable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_stable_tilted_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_stable_tilted_equation_user_curve_name`')

        self._data["Convective Zone Heater Stable Tilted Equation User Curve Name"] = value

    @property
    def convective_zone_heater_unstable_tilted_equation_source(self):
        """Get convective_zone_heater_unstable_tilted_equation_source

        Returns:
            str: the value of `convective_zone_heater_unstable_tilted_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Unstable Tilted Equation Source"]

    @convective_zone_heater_unstable_tilted_equation_source.setter
    def convective_zone_heater_unstable_tilted_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `convective_zone_heater_unstable_tilted_equation_source`
        Applies to zone with convective heater
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `convective_zone_heater_unstable_tilted_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: WaltonUnstableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_unstable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_unstable_tilted_equation_source`'.format(value))

        self._data["Convective Zone Heater Unstable Tilted Equation Source"] = value

    @property
    def convective_zone_heater_unstable_tilted_equation_user_curve_name(self):
        """Get convective_zone_heater_unstable_tilted_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_unstable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Unstable Tilted Equation User Curve Name"]

    @convective_zone_heater_unstable_tilted_equation_user_curve_name.setter
    def convective_zone_heater_unstable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `convective_zone_heater_unstable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_unstable_tilted_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_unstable_tilted_equation_user_curve_name`')

        self._data["Convective Zone Heater Unstable Tilted Equation User Curve Name"] = value

    @property
    def convective_zone_heater_windows_equation_source(self):
        """Get convective_zone_heater_windows_equation_source

        Returns:
            str: the value of `convective_zone_heater_windows_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Windows Equation Source"]

    @convective_zone_heater_windows_equation_source.setter
    def convective_zone_heater_windows_equation_source(self, value="ISO15099Windows"):
        """  Corresponds to IDD Field `convective_zone_heater_windows_equation_source`
        Applies to zone with convective heater
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `convective_zone_heater_windows_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: ISO15099Windows
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_windows_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_windows_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_windows_equation_source`'.format(value))

        self._data["Convective Zone Heater Windows Equation Source"] = value

    @property
    def convective_zone_heater_windows_equation_user_curve_name(self):
        """Get convective_zone_heater_windows_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_windows_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Windows Equation User Curve Name"]

    @convective_zone_heater_windows_equation_user_curve_name.setter
    def convective_zone_heater_windows_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `convective_zone_heater_windows_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_windows_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_windows_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_windows_equation_user_curve_name`')

        self._data["Convective Zone Heater Windows Equation User Curve Name"] = value

    @property
    def central_air_diffuser_wall_equation_source(self):
        """Get central_air_diffuser_wall_equation_source

        Returns:
            str: the value of `central_air_diffuser_wall_equation_source` or None if not set
        """
        return self._data["Central Air Diffuser Wall Equation Source"]

    @central_air_diffuser_wall_equation_source.setter
    def central_air_diffuser_wall_equation_source(self, value="GoldsteinNovoselacCeilingDiffuserWalls"):
        """  Corresponds to IDD Field `central_air_diffuser_wall_equation_source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all wall surfaces

        Args:
            value (str): value for IDD Field `central_air_diffuser_wall_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - FisherPedersenCeilingDiffuserWalls
                      - AlamdariHammondVerticalWall
                      - BeausoleilMorrisonMixedAssistedWall
                      - BeausoleilMorrisonMixedOpposingWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - UserCurve
                Default value: GoldsteinNovoselacCeilingDiffuserWalls
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `central_air_diffuser_wall_equation_source`'.format(value))

        self._data["Central Air Diffuser Wall Equation Source"] = value

    @property
    def central_air_diffuser_wall_equation_user_curve_name(self):
        """Get central_air_diffuser_wall_equation_user_curve_name

        Returns:
            str: the value of `central_air_diffuser_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Central Air Diffuser Wall Equation User Curve Name"]

    @central_air_diffuser_wall_equation_user_curve_name.setter
    def central_air_diffuser_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `central_air_diffuser_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `central_air_diffuser_wall_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_wall_equation_user_curve_name`')

        self._data["Central Air Diffuser Wall Equation User Curve Name"] = value

    @property
    def central_air_diffuser_ceiling_equation_source(self):
        """Get central_air_diffuser_ceiling_equation_source

        Returns:
            str: the value of `central_air_diffuser_ceiling_equation_source` or None if not set
        """
        return self._data["Central Air Diffuser Ceiling Equation Source"]

    @central_air_diffuser_ceiling_equation_source.setter
    def central_air_diffuser_ceiling_equation_source(self, value="FisherPedersenCeilingDiffuserCeiling"):
        """  Corresponds to IDD Field `central_air_diffuser_ceiling_equation_source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all ceiling surfaces

        Args:
            value (str): value for IDD Field `central_air_diffuser_ceiling_equation_source`
                Accepted values are:
                      - FisherPedersenCeilingDiffuserCeiling
                      - BeausoleilMorrisonMixedStableCeiling
                      - BeausoleilMorrisonMixedUnstableCeiling
                      - UserCurve
                Default value: FisherPedersenCeilingDiffuserCeiling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_ceiling_equation_source`')
            vals = set()
            vals.add("FisherPedersenCeilingDiffuserCeiling")
            vals.add("BeausoleilMorrisonMixedStableCeiling")
            vals.add("BeausoleilMorrisonMixedUnstableCeiling")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `central_air_diffuser_ceiling_equation_source`'.format(value))

        self._data["Central Air Diffuser Ceiling Equation Source"] = value

    @property
    def central_air_diffuser_ceiling_equation_user_curve_name(self):
        """Get central_air_diffuser_ceiling_equation_user_curve_name

        Returns:
            str: the value of `central_air_diffuser_ceiling_equation_user_curve_name` or None if not set
        """
        return self._data["Central Air Diffuser Ceiling Equation User Curve Name"]

    @central_air_diffuser_ceiling_equation_user_curve_name.setter
    def central_air_diffuser_ceiling_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `central_air_diffuser_ceiling_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `central_air_diffuser_ceiling_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_ceiling_equation_user_curve_name`')

        self._data["Central Air Diffuser Ceiling Equation User Curve Name"] = value

    @property
    def central_air_diffuser_floor_equation_source(self):
        """Get central_air_diffuser_floor_equation_source

        Returns:
            str: the value of `central_air_diffuser_floor_equation_source` or None if not set
        """
        return self._data["Central Air Diffuser Floor Equation Source"]

    @central_air_diffuser_floor_equation_source.setter
    def central_air_diffuser_floor_equation_source(self, value="GoldsteinNovoselacCeilingDiffuserFloor"):
        """  Corresponds to IDD Field `central_air_diffuser_floor_equation_source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all floor surfaces

        Args:
            value (str): value for IDD Field `central_air_diffuser_floor_equation_source`
                Accepted values are:
                      - FisherPedersenCeilingDiffuserFloor
                      - BeausoleilMorrisonMixedStableFloor
                      - BeausoleilMorrisonMixedUnstableFloor
                      - GoldsteinNovoselacCeilingDiffuserFloor
                      - UserCurve
                Default value: GoldsteinNovoselacCeilingDiffuserFloor
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_floor_equation_source`')
            vals = set()
            vals.add("FisherPedersenCeilingDiffuserFloor")
            vals.add("BeausoleilMorrisonMixedStableFloor")
            vals.add("BeausoleilMorrisonMixedUnstableFloor")
            vals.add("GoldsteinNovoselacCeilingDiffuserFloor")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `central_air_diffuser_floor_equation_source`'.format(value))

        self._data["Central Air Diffuser Floor Equation Source"] = value

    @property
    def central_air_diffuser_floor_equation_user_curve_name(self):
        """Get central_air_diffuser_floor_equation_user_curve_name

        Returns:
            str: the value of `central_air_diffuser_floor_equation_user_curve_name` or None if not set
        """
        return self._data["Central Air Diffuser Floor Equation User Curve Name"]

    @central_air_diffuser_floor_equation_user_curve_name.setter
    def central_air_diffuser_floor_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `central_air_diffuser_floor_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `central_air_diffuser_floor_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_floor_equation_user_curve_name`')

        self._data["Central Air Diffuser Floor Equation User Curve Name"] = value

    @property
    def central_air_diffuser_window_equation_source(self):
        """Get central_air_diffuser_window_equation_source

        Returns:
            str: the value of `central_air_diffuser_window_equation_source` or None if not set
        """
        return self._data["Central Air Diffuser Window Equation Source"]

    @central_air_diffuser_window_equation_source.setter
    def central_air_diffuser_window_equation_source(self, value="GoldsteinNovoselacCeilingDiffuserWindow"):
        """  Corresponds to IDD Field `central_air_diffuser_window_equation_source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `central_air_diffuser_window_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - FisherPedersenCeilingDiffuserWalls
                      - BeausoleilMorrisonMixedAssistedWall
                      - BeausoleilMorrisonMixedOpposingWall
                      - FohannoPolidoriVerticalWall
                      - AlamdariHammondVerticalWall
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWindow
                      - UserCurve
                Default value: GoldsteinNovoselacCeilingDiffuserWindow
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_window_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWindow")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `central_air_diffuser_window_equation_source`'.format(value))

        self._data["Central Air Diffuser Window Equation Source"] = value

    @property
    def central_air_diffuser_window_equation_user_curve_name(self):
        """Get central_air_diffuser_window_equation_user_curve_name

        Returns:
            str: the value of `central_air_diffuser_window_equation_user_curve_name` or None if not set
        """
        return self._data["Central Air Diffuser Window Equation User Curve Name"]

    @central_air_diffuser_window_equation_user_curve_name.setter
    def central_air_diffuser_window_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `central_air_diffuser_window_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `central_air_diffuser_window_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_window_equation_user_curve_name`')

        self._data["Central Air Diffuser Window Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_vertical_wall_equation_source(self):
        """Get mechanical_zone_fan_circulation_vertical_wall_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_vertical_wall_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Vertical Wall Equation Source"]

    @mechanical_zone_fan_circulation_vertical_wall_equation_source.setter
    def mechanical_zone_fan_circulation_vertical_wall_equation_source(self, value="KhalifaEq3WallAwayFromHeat"):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_vertical_wall_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_vertical_wall_equation_source`
                Accepted values are:
                      - KhalifaEq3WallAwayFromHeat
                      - ASHRAEVerticalWall
                      - FisherPedersenCeilingDiffuserWalls
                      - AlamdariHammondVerticalWall
                      - BeausoleilMorrisonMixedAssistedWall
                      - BeausoleilMorrisonMixedOpposingWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - UserCurve
                Default value: KhalifaEq3WallAwayFromHeat
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_vertical_wall_equation_source`')
            vals = set()
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("ASHRAEVerticalWall")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_vertical_wall_equation_source`'.format(value))

        self._data["Mechanical Zone Fan Circulation Vertical Wall Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name"]

    @mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`')

        self._data["Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_stable_horizontal_equation_source(self):
        """Get mechanical_zone_fan_circulation_stable_horizontal_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation Source"]

    @mechanical_zone_fan_circulation_stable_horizontal_equation_source.setter
    def mechanical_zone_fan_circulation_stable_horizontal_equation_source(self, value="AlamdariHammondStableHorizontal"):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_stable_horizontal_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_stable_horizontal_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: AlamdariHammondStableHorizontal
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_stable_horizontal_equation_source`'.format(value))

        self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name"]

    @mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`')

        self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_source(self):
        """Get mechanical_zone_fan_circulation_unstable_horizontal_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation Source"]

    @mechanical_zone_fan_circulation_unstable_horizontal_equation_source.setter
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_source(self, value="KhalifaEq4CeilingAwayFromHeat"):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_unstable_horizontal_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_unstable_horizontal_equation_source`
                Accepted values are:
                      - KhalifaEq4CeilingAwayFromHeat
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: KhalifaEq4CeilingAwayFromHeat
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("KhalifaEq4CeilingAwayFromHeat")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_unstable_horizontal_equation_source`'.format(value))

        self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name"]

    @mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`')

        self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_stable_tilted_equation_source(self):
        """Get mechanical_zone_fan_circulation_stable_tilted_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_tilted_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Stable Tilted Equation Source"]

    @mechanical_zone_fan_circulation_stable_tilted_equation_source.setter
    def mechanical_zone_fan_circulation_stable_tilted_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_stable_tilted_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_stable_tilted_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - UserCurve
                Default value: WaltonStableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_stable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_stable_tilted_equation_source`'.format(value))

        self._data["Mechanical Zone Fan Circulation Stable Tilted Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name"]

    @mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`')

        self._data["Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_tilted_equation_source(self):
        """Get mechanical_zone_fan_circulation_unstable_tilted_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_tilted_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation Source"]

    @mechanical_zone_fan_circulation_unstable_tilted_equation_source.setter
    def mechanical_zone_fan_circulation_unstable_tilted_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_unstable_tilted_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_unstable_tilted_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: WaltonUnstableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_unstable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_unstable_tilted_equation_source`'.format(value))

        self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name"]

    @mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`')

        self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_window_equation_source(self):
        """Get mechanical_zone_fan_circulation_window_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_window_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Window Equation Source"]

    @mechanical_zone_fan_circulation_window_equation_source.setter
    def mechanical_zone_fan_circulation_window_equation_source(self, value="ISO15099Windows"):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_window_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_window_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWindow
                      - UserCurve
                Default value: ISO15099Windows
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_window_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWindow")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_window_equation_source`'.format(value))

        self._data["Mechanical Zone Fan Circulation Window Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_window_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_window_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_window_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Window Equation User Curve Name"]

    @mechanical_zone_fan_circulation_window_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_window_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_window_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_window_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_window_equation_user_curve_name`')

        self._data["Mechanical Zone Fan Circulation Window Equation User Curve Name"] = value

    @property
    def mixed_regime_bouyancy_assisting_flow_on_walls_equation_source(self):
        """Get mixed_regime_bouyancy_assisting_flow_on_walls_equation_source

        Returns:
            str: the value of `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source` or None if not set
        """
        return self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation Source"]

    @mixed_regime_bouyancy_assisting_flow_on_walls_equation_source.setter
    def mixed_regime_bouyancy_assisting_flow_on_walls_equation_source(self, value="BeausoleilMorrisonMixedAssistedWall"):
        """  Corresponds to IDD Field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`
                Accepted values are:
                      - BeausoleilMorrisonMixedAssistedWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - ASHRAEVerticalWall
                      - FisherPedersenCeilingDiffuserWalls
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - UserCurve
                Default value: BeausoleilMorrisonMixedAssistedWall
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ASHRAEVerticalWall")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`'.format(value))

        self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation Source"] = value

    @property
    def mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name(self):
        """Get mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation User Curve Name"]

    @mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name.setter
    def mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`')

        self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation User Curve Name"] = value

    @property
    def mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source(self):
        """Get mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source

        Returns:
            str: the value of `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source` or None if not set
        """
        return self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation Source"]

    @mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source.setter
    def mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source(self, value="BeausoleilMorrisonMixedOpposingWall"):
        """  Corresponds to IDD Field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`
                Accepted values are:
                      - BeausoleilMorrisonMixedOpposingWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - ASHRAEVerticalWall
                      - FisherPedersenCeilingDiffuserWalls
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - UserCurve
                Default value: BeausoleilMorrisonMixedOpposingWall
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ASHRAEVerticalWall")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`'.format(value))

        self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation Source"] = value

    @property
    def mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name(self):
        """Get mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation User Curve Name"]

    @mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name.setter
    def mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`')

        self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation User Curve Name"] = value

    @property
    def mixed_regime_stable_floor_equation_source(self):
        """Get mixed_regime_stable_floor_equation_source

        Returns:
            str: the value of `mixed_regime_stable_floor_equation_source` or None if not set
        """
        return self._data["Mixed Regime Stable Floor Equation Source"]

    @mixed_regime_stable_floor_equation_source.setter
    def mixed_regime_stable_floor_equation_source(self, value="BeausoleilMorrisonMixedStableFloor"):
        """  Corresponds to IDD Field `mixed_regime_stable_floor_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_stable_floor_equation_source`
                Accepted values are:
                      - BeausoleilMorrisonMixedStableFloor
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: BeausoleilMorrisonMixedStableFloor
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_stable_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_stable_floor_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedStableFloor")
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_stable_floor_equation_source`'.format(value))

        self._data["Mixed Regime Stable Floor Equation Source"] = value

    @property
    def mixed_regime_stable_floor_equation_user_curve_name(self):
        """Get mixed_regime_stable_floor_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_stable_floor_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Stable Floor Equation User Curve Name"]

    @mixed_regime_stable_floor_equation_user_curve_name.setter
    def mixed_regime_stable_floor_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mixed_regime_stable_floor_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_stable_floor_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_stable_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_stable_floor_equation_user_curve_name`')

        self._data["Mixed Regime Stable Floor Equation User Curve Name"] = value

    @property
    def mixed_regime_unstable_floor_equation_source(self):
        """Get mixed_regime_unstable_floor_equation_source

        Returns:
            str: the value of `mixed_regime_unstable_floor_equation_source` or None if not set
        """
        return self._data["Mixed Regime Unstable Floor Equation Source"]

    @mixed_regime_unstable_floor_equation_source.setter
    def mixed_regime_unstable_floor_equation_source(self, value="BeausoleilMorrisonMixedUnstableFloor"):
        """  Corresponds to IDD Field `mixed_regime_unstable_floor_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_unstable_floor_equation_source`
                Accepted values are:
                      - BeausoleilMorrisonMixedUnstableFloor
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: BeausoleilMorrisonMixedUnstableFloor
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_unstable_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_unstable_floor_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedUnstableFloor")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_unstable_floor_equation_source`'.format(value))

        self._data["Mixed Regime Unstable Floor Equation Source"] = value

    @property
    def mixed_regime_unstable_floor_equation_user_curve_name(self):
        """Get mixed_regime_unstable_floor_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_unstable_floor_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Unstable Floor Equation User Curve Name"]

    @mixed_regime_unstable_floor_equation_user_curve_name.setter
    def mixed_regime_unstable_floor_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mixed_regime_unstable_floor_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_unstable_floor_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_unstable_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_unstable_floor_equation_user_curve_name`')

        self._data["Mixed Regime Unstable Floor Equation User Curve Name"] = value

    @property
    def mixed_regime_stable_ceiling_equation_source(self):
        """Get mixed_regime_stable_ceiling_equation_source

        Returns:
            str: the value of `mixed_regime_stable_ceiling_equation_source` or None if not set
        """
        return self._data["Mixed Regime Stable Ceiling Equation Source"]

    @mixed_regime_stable_ceiling_equation_source.setter
    def mixed_regime_stable_ceiling_equation_source(self, value="BeausoleilMorrisonMixedStableCeiling"):
        """  Corresponds to IDD Field `mixed_regime_stable_ceiling_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_stable_ceiling_equation_source`
                Accepted values are:
                      - BeausoleilMorrisonMixedStableCeiling
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: BeausoleilMorrisonMixedStableCeiling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_stable_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_stable_ceiling_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedStableCeiling")
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_stable_ceiling_equation_source`'.format(value))

        self._data["Mixed Regime Stable Ceiling Equation Source"] = value

    @property
    def mixed_regime_stable_ceiling_equation_user_curve_name(self):
        """Get mixed_regime_stable_ceiling_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_stable_ceiling_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Stable Ceiling Equation User Curve Name"]

    @mixed_regime_stable_ceiling_equation_user_curve_name.setter
    def mixed_regime_stable_ceiling_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mixed_regime_stable_ceiling_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_stable_ceiling_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_stable_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_stable_ceiling_equation_user_curve_name`')

        self._data["Mixed Regime Stable Ceiling Equation User Curve Name"] = value

    @property
    def mixed_regime_unstable_ceiling_equation_source(self):
        """Get mixed_regime_unstable_ceiling_equation_source

        Returns:
            str: the value of `mixed_regime_unstable_ceiling_equation_source` or None if not set
        """
        return self._data["Mixed Regime Unstable Ceiling Equation Source"]

    @mixed_regime_unstable_ceiling_equation_source.setter
    def mixed_regime_unstable_ceiling_equation_source(self, value="BeausoleilMorrisonMixedUnstableCeiling"):
        """  Corresponds to IDD Field `mixed_regime_unstable_ceiling_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_unstable_ceiling_equation_source`
                Accepted values are:
                      - BeausoleilMorrisonMixedUnstableCeiling
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: BeausoleilMorrisonMixedUnstableCeiling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_unstable_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_unstable_ceiling_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedUnstableCeiling")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_unstable_ceiling_equation_source`'.format(value))

        self._data["Mixed Regime Unstable Ceiling Equation Source"] = value

    @property
    def mixed_regime_unstable_ceiling_equation_user_curve_name(self):
        """Get mixed_regime_unstable_ceiling_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_unstable_ceiling_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Unstable Ceiling Equation User Curve Name"]

    @mixed_regime_unstable_ceiling_equation_user_curve_name.setter
    def mixed_regime_unstable_ceiling_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mixed_regime_unstable_ceiling_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_unstable_ceiling_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_unstable_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_unstable_ceiling_equation_user_curve_name`')

        self._data["Mixed Regime Unstable Ceiling Equation User Curve Name"] = value

    @property
    def mixed_regime_window_equation_source(self):
        """Get mixed_regime_window_equation_source

        Returns:
            str: the value of `mixed_regime_window_equation_source` or None if not set
        """
        return self._data["Mixed Regime Window Equation Source"]

    @mixed_regime_window_equation_source.setter
    def mixed_regime_window_equation_source(self, value="GoldsteinNovoselacCeilingDiffuserWindow"):
        """  Corresponds to IDD Field `mixed_regime_window_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_window_equation_source`
                Accepted values are:
                      - GoldsteinNovoselacCeilingDiffuserWindow
                      - ISO15099Windows
                      - UserCurve
                Default value: GoldsteinNovoselacCeilingDiffuserWindow
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_window_equation_source`')
            vals = set()
            vals.add("GoldsteinNovoselacCeilingDiffuserWindow")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_window_equation_source`'.format(value))

        self._data["Mixed Regime Window Equation Source"] = value

    @property
    def mixed_regime_window_equation_user_curve_name(self):
        """Get mixed_regime_window_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_window_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Window Equation User Curve Name"]

    @mixed_regime_window_equation_user_curve_name.setter
    def mixed_regime_window_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `mixed_regime_window_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_window_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_window_equation_user_curve_name`')

        self._data["Mixed Regime Window Equation User Curve Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.simple_bouyancy_vertical_wall_equation_source))
        out.append(self._to_str(self.simple_bouyancy_vertical_wall_user_curve_name))
        out.append(self._to_str(self.simple_bouyancy_stable_horizontal_equation_source))
        out.append(self._to_str(self.simple_bouyancy_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.simple_bouyancy_unstable_horizontal_equation_source))
        out.append(self._to_str(self.simple_bouyancy_unstable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.simple_bouyancy_stable_tilted_equation_source))
        out.append(self._to_str(self.simple_bouyancy_stable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.simple_bouyancy_unstable_tilted_equation_source))
        out.append(self._to_str(self.simple_bouyancy_unstable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.simple_bouyancy_windows_equation_source))
        out.append(self._to_str(self.simple_bouyancy_windows_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_vertical_wall_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_stable_horizontal_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_unstable_horizontal_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_heated_floor_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_chilled_ceiling_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_stable_tilted_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_unstable_tilted_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_window_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_window_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_vertical_wall_equation_source))
        out.append(self._to_str(self.wall_panel_heating_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_heated_wall_equation_source))
        out.append(self._to_str(self.wall_panel_heating_heated_wall_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_stable_horizontal_equation_source))
        out.append(self._to_str(self.wall_panel_heating_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_unstable_horizontal_equation_source))
        out.append(self._to_str(self.wall_panel_heating_unstable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_stable_tilted_equation_source))
        out.append(self._to_str(self.wall_panel_heating_stable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_unstable_tilted_equation_source))
        out.append(self._to_str(self.wall_panel_heating_unstable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_window_equation_source))
        out.append(self._to_str(self.wall_panel_heating_window_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_vertical_wall_equation_source))
        out.append(self._to_str(self.convective_zone_heater_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_vertical_walls_near_heater_equation_source))
        out.append(self._to_str(self.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_stable_horizontal_equation_source))
        out.append(self._to_str(self.convective_zone_heater_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_unstable_horizontal_equation_source))
        out.append(self._to_str(self.convective_zone_heater_unstable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_stable_tilted_equation_source))
        out.append(self._to_str(self.convective_zone_heater_stable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_unstable_tilted_equation_source))
        out.append(self._to_str(self.convective_zone_heater_unstable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_windows_equation_source))
        out.append(self._to_str(self.convective_zone_heater_windows_equation_user_curve_name))
        out.append(self._to_str(self.central_air_diffuser_wall_equation_source))
        out.append(self._to_str(self.central_air_diffuser_wall_equation_user_curve_name))
        out.append(self._to_str(self.central_air_diffuser_ceiling_equation_source))
        out.append(self._to_str(self.central_air_diffuser_ceiling_equation_user_curve_name))
        out.append(self._to_str(self.central_air_diffuser_floor_equation_source))
        out.append(self._to_str(self.central_air_diffuser_floor_equation_user_curve_name))
        out.append(self._to_str(self.central_air_diffuser_window_equation_source))
        out.append(self._to_str(self.central_air_diffuser_window_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_vertical_wall_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_stable_horizontal_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_unstable_horizontal_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_stable_tilted_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_unstable_tilted_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_window_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_window_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source))
        out.append(self._to_str(self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source))
        out.append(self._to_str(self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_stable_floor_equation_source))
        out.append(self._to_str(self.mixed_regime_stable_floor_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_unstable_floor_equation_source))
        out.append(self._to_str(self.mixed_regime_unstable_floor_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_stable_ceiling_equation_source))
        out.append(self._to_str(self.mixed_regime_stable_ceiling_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_unstable_ceiling_equation_source))
        out.append(self._to_str(self.mixed_regime_unstable_ceiling_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_window_equation_source))
        out.append(self._to_str(self.mixed_regime_window_equation_user_curve_name))
        return ",".join(out)

class SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections`
        Options to change the individual convection model equations for dynamic selection when using AdaptiveConvectiongAlgorithm
        This object is only needed to make changes to the default model selections for any or all of the surface categories.
        This object is for the outside face, the side of the surface facing away from the thermal zone.
    """
    internal_name = "SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Wind Convection Windward Vertical Wall Equation Source"] = None
        self._data["Wind Convection Windward Equation Vertical Wall User Curve Name"] = None
        self._data["Wind Convection Leeward Vertical Wall Equation Source"] = None
        self._data["Wind Convection Leeward Vertical Wall Equation User Curve Name"] = None
        self._data["Wind Convection Horizontal Roof Equation Source"] = None
        self._data["Wind Convection Horizontal Roof User Curve Name"] = None
        self._data["Natural Convection Vertical Wall Equation Source"] = None
        self._data["Natural Convection Vertical Wall Equation User Curve Name"] = None
        self._data["Natural Convection Stable Horizontal Equation Source"] = None
        self._data["Natural Convection Stable Horizontal Equation User Curve Name"] = None
        self._data["Natural Convection Unstable Horizontal Equation Source"] = None
        self._data["Natural Convection Unstable Horizontal Equation User Curve Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_windward_vertical_wall_equation_source = None
        else:
            self.wind_convection_windward_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_windward_equation_vertical_wall_user_curve_name = None
        else:
            self.wind_convection_windward_equation_vertical_wall_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_leeward_vertical_wall_equation_source = None
        else:
            self.wind_convection_leeward_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_leeward_vertical_wall_equation_user_curve_name = None
        else:
            self.wind_convection_leeward_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_horizontal_roof_equation_source = None
        else:
            self.wind_convection_horizontal_roof_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_horizontal_roof_user_curve_name = None
        else:
            self.wind_convection_horizontal_roof_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_vertical_wall_equation_source = None
        else:
            self.natural_convection_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_vertical_wall_equation_user_curve_name = None
        else:
            self.natural_convection_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_stable_horizontal_equation_source = None
        else:
            self.natural_convection_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_stable_horizontal_equation_user_curve_name = None
        else:
            self.natural_convection_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_unstable_horizontal_equation_source = None
        else:
            self.natural_convection_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_unstable_horizontal_equation_user_curve_name = None
        else:
            self.natural_convection_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def wind_convection_windward_vertical_wall_equation_source(self):
        """Get wind_convection_windward_vertical_wall_equation_source

        Returns:
            str: the value of `wind_convection_windward_vertical_wall_equation_source` or None if not set
        """
        return self._data["Wind Convection Windward Vertical Wall Equation Source"]

    @wind_convection_windward_vertical_wall_equation_source.setter
    def wind_convection_windward_vertical_wall_equation_source(self, value="TARPWindward"):
        """  Corresponds to IDD Field `wind_convection_windward_vertical_wall_equation_source`

        Args:
            value (str): value for IDD Field `wind_convection_windward_vertical_wall_equation_source`
                Accepted values are:
                      - SimpleCombined
                      - TARPWindward
                      - MoWiTTWindward
                      - DOE2Windward
                      - NusseltJurges
                      - McAdams
                      - Mitchell
                      - BlockenWindward
                      - EmmelVertical
                      - UserCurve
                Default value: TARPWindward
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_convection_windward_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_windward_vertical_wall_equation_source`')
            vals = set()
            vals.add("SimpleCombined")
            vals.add("TARPWindward")
            vals.add("MoWiTTWindward")
            vals.add("DOE2Windward")
            vals.add("NusseltJurges")
            vals.add("McAdams")
            vals.add("Mitchell")
            vals.add("BlockenWindward")
            vals.add("EmmelVertical")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_convection_windward_vertical_wall_equation_source`'.format(value))

        self._data["Wind Convection Windward Vertical Wall Equation Source"] = value

    @property
    def wind_convection_windward_equation_vertical_wall_user_curve_name(self):
        """Get wind_convection_windward_equation_vertical_wall_user_curve_name

        Returns:
            str: the value of `wind_convection_windward_equation_vertical_wall_user_curve_name` or None if not set
        """
        return self._data["Wind Convection Windward Equation Vertical Wall User Curve Name"]

    @wind_convection_windward_equation_vertical_wall_user_curve_name.setter
    def wind_convection_windward_equation_vertical_wall_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `wind_convection_windward_equation_vertical_wall_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wind_convection_windward_equation_vertical_wall_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_convection_windward_equation_vertical_wall_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_windward_equation_vertical_wall_user_curve_name`')

        self._data["Wind Convection Windward Equation Vertical Wall User Curve Name"] = value

    @property
    def wind_convection_leeward_vertical_wall_equation_source(self):
        """Get wind_convection_leeward_vertical_wall_equation_source

        Returns:
            str: the value of `wind_convection_leeward_vertical_wall_equation_source` or None if not set
        """
        return self._data["Wind Convection Leeward Vertical Wall Equation Source"]

    @wind_convection_leeward_vertical_wall_equation_source.setter
    def wind_convection_leeward_vertical_wall_equation_source(self, value="TARPLeeward"):
        """  Corresponds to IDD Field `wind_convection_leeward_vertical_wall_equation_source`

        Args:
            value (str): value for IDD Field `wind_convection_leeward_vertical_wall_equation_source`
                Accepted values are:
                      - SimpleCombined
                      - TARPLeeward
                      - MoWiTTLeeward
                      - DOE2Leeward
                      - EmmelVertical
                      - NusseltJurges
                      - McAdams
                      - Mitchell
                      - UserCurve
                Default value: TARPLeeward
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_convection_leeward_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_leeward_vertical_wall_equation_source`')
            vals = set()
            vals.add("SimpleCombined")
            vals.add("TARPLeeward")
            vals.add("MoWiTTLeeward")
            vals.add("DOE2Leeward")
            vals.add("EmmelVertical")
            vals.add("NusseltJurges")
            vals.add("McAdams")
            vals.add("Mitchell")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_convection_leeward_vertical_wall_equation_source`'.format(value))

        self._data["Wind Convection Leeward Vertical Wall Equation Source"] = value

    @property
    def wind_convection_leeward_vertical_wall_equation_user_curve_name(self):
        """Get wind_convection_leeward_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `wind_convection_leeward_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Wind Convection Leeward Vertical Wall Equation User Curve Name"]

    @wind_convection_leeward_vertical_wall_equation_user_curve_name.setter
    def wind_convection_leeward_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `wind_convection_leeward_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wind_convection_leeward_vertical_wall_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_convection_leeward_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_leeward_vertical_wall_equation_user_curve_name`')

        self._data["Wind Convection Leeward Vertical Wall Equation User Curve Name"] = value

    @property
    def wind_convection_horizontal_roof_equation_source(self):
        """Get wind_convection_horizontal_roof_equation_source

        Returns:
            str: the value of `wind_convection_horizontal_roof_equation_source` or None if not set
        """
        return self._data["Wind Convection Horizontal Roof Equation Source"]

    @wind_convection_horizontal_roof_equation_source.setter
    def wind_convection_horizontal_roof_equation_source(self, value="ClearRoof"):
        """  Corresponds to IDD Field `wind_convection_horizontal_roof_equation_source`

        Args:
            value (str): value for IDD Field `wind_convection_horizontal_roof_equation_source`
                Accepted values are:
                      - SimpleCombined
                      - TARPWindward
                      - MoWiTTWindward
                      - DOE2Windward
                      - NusseltJurges
                      - McAdams
                      - Mitchell
                      - BlockenWindward
                      - EmmelRoof
                      - ClearRoof
                      - UserCurve
                Default value: ClearRoof
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_convection_horizontal_roof_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_horizontal_roof_equation_source`')
            vals = set()
            vals.add("SimpleCombined")
            vals.add("TARPWindward")
            vals.add("MoWiTTWindward")
            vals.add("DOE2Windward")
            vals.add("NusseltJurges")
            vals.add("McAdams")
            vals.add("Mitchell")
            vals.add("BlockenWindward")
            vals.add("EmmelRoof")
            vals.add("ClearRoof")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_convection_horizontal_roof_equation_source`'.format(value))

        self._data["Wind Convection Horizontal Roof Equation Source"] = value

    @property
    def wind_convection_horizontal_roof_user_curve_name(self):
        """Get wind_convection_horizontal_roof_user_curve_name

        Returns:
            str: the value of `wind_convection_horizontal_roof_user_curve_name` or None if not set
        """
        return self._data["Wind Convection Horizontal Roof User Curve Name"]

    @wind_convection_horizontal_roof_user_curve_name.setter
    def wind_convection_horizontal_roof_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `wind_convection_horizontal_roof_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wind_convection_horizontal_roof_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_convection_horizontal_roof_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_horizontal_roof_user_curve_name`')

        self._data["Wind Convection Horizontal Roof User Curve Name"] = value

    @property
    def natural_convection_vertical_wall_equation_source(self):
        """Get natural_convection_vertical_wall_equation_source

        Returns:
            str: the value of `natural_convection_vertical_wall_equation_source` or None if not set
        """
        return self._data["Natural Convection Vertical Wall Equation Source"]

    @natural_convection_vertical_wall_equation_source.setter
    def natural_convection_vertical_wall_equation_source(self, value="ASHRAEVerticalWall"):
        """  Corresponds to IDD Field `natural_convection_vertical_wall_equation_source`
        This is for vertical walls

        Args:
            value (str): value for IDD Field `natural_convection_vertical_wall_equation_source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                      - None
                Default value: ASHRAEVerticalWall
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `natural_convection_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_vertical_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `natural_convection_vertical_wall_equation_source`'.format(value))

        self._data["Natural Convection Vertical Wall Equation Source"] = value

    @property
    def natural_convection_vertical_wall_equation_user_curve_name(self):
        """Get natural_convection_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `natural_convection_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Natural Convection Vertical Wall Equation User Curve Name"]

    @natural_convection_vertical_wall_equation_user_curve_name.setter
    def natural_convection_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `natural_convection_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `natural_convection_vertical_wall_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `natural_convection_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_vertical_wall_equation_user_curve_name`')

        self._data["Natural Convection Vertical Wall Equation User Curve Name"] = value

    @property
    def natural_convection_stable_horizontal_equation_source(self):
        """Get natural_convection_stable_horizontal_equation_source

        Returns:
            str: the value of `natural_convection_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Natural Convection Stable Horizontal Equation Source"]

    @natural_convection_stable_horizontal_equation_source.setter
    def natural_convection_stable_horizontal_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `natural_convection_stable_horizontal_equation_source`
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `natural_convection_stable_horizontal_equation_source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                      - None
                Default value: WaltonStableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `natural_convection_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `natural_convection_stable_horizontal_equation_source`'.format(value))

        self._data["Natural Convection Stable Horizontal Equation Source"] = value

    @property
    def natural_convection_stable_horizontal_equation_user_curve_name(self):
        """Get natural_convection_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `natural_convection_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Natural Convection Stable Horizontal Equation User Curve Name"]

    @natural_convection_stable_horizontal_equation_user_curve_name.setter
    def natural_convection_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `natural_convection_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `natural_convection_stable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `natural_convection_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_stable_horizontal_equation_user_curve_name`')

        self._data["Natural Convection Stable Horizontal Equation User Curve Name"] = value

    @property
    def natural_convection_unstable_horizontal_equation_source(self):
        """Get natural_convection_unstable_horizontal_equation_source

        Returns:
            str: the value of `natural_convection_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Natural Convection Unstable Horizontal Equation Source"]

    @natural_convection_unstable_horizontal_equation_source.setter
    def natural_convection_unstable_horizontal_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `natural_convection_unstable_horizontal_equation_source`

        Args:
            value (str): value for IDD Field `natural_convection_unstable_horizontal_equation_source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                      - None
                Default value: WaltonUnstableHorizontalOrTilt
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `natural_convection_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `natural_convection_unstable_horizontal_equation_source`'.format(value))

        self._data["Natural Convection Unstable Horizontal Equation Source"] = value

    @property
    def natural_convection_unstable_horizontal_equation_user_curve_name(self):
        """Get natural_convection_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `natural_convection_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Natural Convection Unstable Horizontal Equation User Curve Name"]

    @natural_convection_unstable_horizontal_equation_user_curve_name.setter
    def natural_convection_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `natural_convection_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `natural_convection_unstable_horizontal_equation_user_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `natural_convection_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_unstable_horizontal_equation_user_curve_name`')

        self._data["Natural Convection Unstable Horizontal Equation User Curve Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.wind_convection_windward_vertical_wall_equation_source))
        out.append(self._to_str(self.wind_convection_windward_equation_vertical_wall_user_curve_name))
        out.append(self._to_str(self.wind_convection_leeward_vertical_wall_equation_source))
        out.append(self._to_str(self.wind_convection_leeward_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.wind_convection_horizontal_roof_equation_source))
        out.append(self._to_str(self.wind_convection_horizontal_roof_user_curve_name))
        out.append(self._to_str(self.natural_convection_vertical_wall_equation_source))
        out.append(self._to_str(self.natural_convection_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.natural_convection_stable_horizontal_equation_source))
        out.append(self._to_str(self.natural_convection_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.natural_convection_unstable_horizontal_equation_source))
        out.append(self._to_str(self.natural_convection_unstable_horizontal_equation_user_curve_name))
        return ",".join(out)

class SurfaceConvectionAlgorithmInsideUserCurve(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside:UserCurve`
        Used to describe a custom model equation for surface convection heat transfer coefficient
        If more than one curve is referenced they are all used and added together.
    """
    internal_name = "SurfaceConvectionAlgorithm:Inside:UserCurve"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceConvectionAlgorithm:Inside:UserCurve`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Temperature for Convection Heat Transfer"] = None
        self._data["Hc Function of Temperature Difference Curve Name"] = None
        self._data["Hc Function of Temperature Difference Divided by Height Curve Name"] = None
        self._data["Hc Function of Air Change Rate Curve Name"] = None
        self._data["Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_temperature_for_convection_heat_transfer = None
        else:
            self.reference_temperature_for_convection_heat_transfer = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hc_function_of_temperature_difference_curve_name = None
        else:
            self.hc_function_of_temperature_difference_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hc_function_of_temperature_difference_divided_by_height_curve_name = None
        else:
            self.hc_function_of_temperature_difference_divided_by_height_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hc_function_of_air_change_rate_curve_name = None
        else:
            self.hc_function_of_air_change_rate_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name = None
        else:
            self.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def reference_temperature_for_convection_heat_transfer(self):
        """Get reference_temperature_for_convection_heat_transfer

        Returns:
            str: the value of `reference_temperature_for_convection_heat_transfer` or None if not set
        """
        return self._data["Reference Temperature for Convection Heat Transfer"]

    @reference_temperature_for_convection_heat_transfer.setter
    def reference_temperature_for_convection_heat_transfer(self, value=None):
        """  Corresponds to IDD Field `reference_temperature_for_convection_heat_transfer`
        Controls which temperature is differenced from surface temperature when using the Hc value

        Args:
            value (str): value for IDD Field `reference_temperature_for_convection_heat_transfer`
                Accepted values are:
                      - MeanAirTemperature
                      - AdjacentAirTemperature
                      - SupplyAirTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reference_temperature_for_convection_heat_transfer`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_temperature_for_convection_heat_transfer`')
            vals = set()
            vals.add("MeanAirTemperature")
            vals.add("AdjacentAirTemperature")
            vals.add("SupplyAirTemperature")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `reference_temperature_for_convection_heat_transfer`'.format(value))

        self._data["Reference Temperature for Convection Heat Transfer"] = value

    @property
    def hc_function_of_temperature_difference_curve_name(self):
        """Get hc_function_of_temperature_difference_curve_name

        Returns:
            str: the value of `hc_function_of_temperature_difference_curve_name` or None if not set
        """
        return self._data["Hc Function of Temperature Difference Curve Name"]

    @hc_function_of_temperature_difference_curve_name.setter
    def hc_function_of_temperature_difference_curve_name(self, value=None):
        """  Corresponds to IDD Field `hc_function_of_temperature_difference_curve_name`
        Curve's "x" is absolute value of delta-T (Surface temperature minus reference temperature, (C))
        Table:OneIndependentVariable objects can also be used

        Args:
            value (str): value for IDD Field `hc_function_of_temperature_difference_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hc_function_of_temperature_difference_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hc_function_of_temperature_difference_curve_name`')

        self._data["Hc Function of Temperature Difference Curve Name"] = value

    @property
    def hc_function_of_temperature_difference_divided_by_height_curve_name(self):
        """Get hc_function_of_temperature_difference_divided_by_height_curve_name

        Returns:
            str: the value of `hc_function_of_temperature_difference_divided_by_height_curve_name` or None if not set
        """
        return self._data["Hc Function of Temperature Difference Divided by Height Curve Name"]

    @hc_function_of_temperature_difference_divided_by_height_curve_name.setter
    def hc_function_of_temperature_difference_divided_by_height_curve_name(self, value=None):
        """  Corresponds to IDD Field `hc_function_of_temperature_difference_divided_by_height_curve_name`
        Curve's "x" is absolute value of delta-T/Height (Surface temp minus Air temp)/(vertical length scale), (C/m)
        when used for an inside face the vertical length scale is the zone's interior height
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `hc_function_of_temperature_difference_divided_by_height_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hc_function_of_temperature_difference_divided_by_height_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hc_function_of_temperature_difference_divided_by_height_curve_name`')

        self._data["Hc Function of Temperature Difference Divided by Height Curve Name"] = value

    @property
    def hc_function_of_air_change_rate_curve_name(self):
        """Get hc_function_of_air_change_rate_curve_name

        Returns:
            str: the value of `hc_function_of_air_change_rate_curve_name` or None if not set
        """
        return self._data["Hc Function of Air Change Rate Curve Name"]

    @hc_function_of_air_change_rate_curve_name.setter
    def hc_function_of_air_change_rate_curve_name(self, value=None):
        """  Corresponds to IDD Field `hc_function_of_air_change_rate_curve_name`
        Curve's "x" is mechanical ACH (Air Changes per hour from mechanical air system), (1/hr)
        Table:OneIndependentVariable objects can also be used

        Args:
            value (str): value for IDD Field `hc_function_of_air_change_rate_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hc_function_of_air_change_rate_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hc_function_of_air_change_rate_curve_name`')

        self._data["Hc Function of Air Change Rate Curve Name"] = value

    @property
    def hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name(self):
        """Get hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name

        Returns:
            str: the value of `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name` or None if not set
        """
        return self._data["Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name"]

    @hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name.setter
    def hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name(self, value=None):
        """  Corresponds to IDD Field `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`
        Curve's "x" is mechanical system air flow rate (m3/s) divided by zone's length along
        exterior walls (m).
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`')

        self._data["Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.reference_temperature_for_convection_heat_transfer))
        out.append(self._to_str(self.hc_function_of_temperature_difference_curve_name))
        out.append(self._to_str(self.hc_function_of_temperature_difference_divided_by_height_curve_name))
        out.append(self._to_str(self.hc_function_of_air_change_rate_curve_name))
        out.append(self._to_str(self.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name))
        return ",".join(out)

class SurfaceConvectionAlgorithmOutsideUserCurve(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside:UserCurve`
        Used to describe a custom model equation for surface convection heat transfer coefficient
        If more than one curve is referenced they are all used and added together.
    """
    internal_name = "SurfaceConvectionAlgorithm:Outside:UserCurve"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceConvectionAlgorithm:Outside:UserCurve`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Wind Speed Type for Curve"] = None
        self._data["Hf Function of Wind Speed Curve Name"] = None
        self._data["Hn Function of Temperature Difference Curve Name"] = None
        self._data["Hn Function of Temperature Difference Divided by Height Curve Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_speed_type_for_curve = None
        else:
            self.wind_speed_type_for_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hf_function_of_wind_speed_curve_name = None
        else:
            self.hf_function_of_wind_speed_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hn_function_of_temperature_difference_curve_name = None
        else:
            self.hn_function_of_temperature_difference_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hn_function_of_temperature_difference_divided_by_height_curve_name = None
        else:
            self.hn_function_of_temperature_difference_divided_by_height_curve_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def wind_speed_type_for_curve(self):
        """Get wind_speed_type_for_curve

        Returns:
            str: the value of `wind_speed_type_for_curve` or None if not set
        """
        return self._data["Wind Speed Type for Curve"]

    @wind_speed_type_for_curve.setter
    def wind_speed_type_for_curve(self, value="HeightAdjust"):
        """  Corresponds to IDD Field `wind_speed_type_for_curve`

        Args:
            value (str): value for IDD Field `wind_speed_type_for_curve`
                Accepted values are:
                      - WeatherFile
                      - HeightAdjust
                      - ParallelComponent
                      - ParallelComponentHeightAdjust
                Default value: HeightAdjust
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_speed_type_for_curve`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_speed_type_for_curve`')
            vals = set()
            vals.add("WeatherFile")
            vals.add("HeightAdjust")
            vals.add("ParallelComponent")
            vals.add("ParallelComponentHeightAdjust")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_speed_type_for_curve`'.format(value))

        self._data["Wind Speed Type for Curve"] = value

    @property
    def hf_function_of_wind_speed_curve_name(self):
        """Get hf_function_of_wind_speed_curve_name

        Returns:
            str: the value of `hf_function_of_wind_speed_curve_name` or None if not set
        """
        return self._data["Hf Function of Wind Speed Curve Name"]

    @hf_function_of_wind_speed_curve_name.setter
    def hf_function_of_wind_speed_curve_name(self, value=None):
        """  Corresponds to IDD Field `hf_function_of_wind_speed_curve_name`
        Curve's "x" is wind speed of the type determined in the previous field (m/s)
        Table:OneIndependentVariable objects can also be used

        Args:
            value (str): value for IDD Field `hf_function_of_wind_speed_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hf_function_of_wind_speed_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hf_function_of_wind_speed_curve_name`')

        self._data["Hf Function of Wind Speed Curve Name"] = value

    @property
    def hn_function_of_temperature_difference_curve_name(self):
        """Get hn_function_of_temperature_difference_curve_name

        Returns:
            str: the value of `hn_function_of_temperature_difference_curve_name` or None if not set
        """
        return self._data["Hn Function of Temperature Difference Curve Name"]

    @hn_function_of_temperature_difference_curve_name.setter
    def hn_function_of_temperature_difference_curve_name(self, value=None):
        """  Corresponds to IDD Field `hn_function_of_temperature_difference_curve_name`
        Curve's "x" is absolute value of delta-T (Surface temperature minus air temperature, (C))
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `hn_function_of_temperature_difference_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hn_function_of_temperature_difference_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hn_function_of_temperature_difference_curve_name`')

        self._data["Hn Function of Temperature Difference Curve Name"] = value

    @property
    def hn_function_of_temperature_difference_divided_by_height_curve_name(self):
        """Get hn_function_of_temperature_difference_divided_by_height_curve_name

        Returns:
            str: the value of `hn_function_of_temperature_difference_divided_by_height_curve_name` or None if not set
        """
        return self._data["Hn Function of Temperature Difference Divided by Height Curve Name"]

    @hn_function_of_temperature_difference_divided_by_height_curve_name.setter
    def hn_function_of_temperature_difference_divided_by_height_curve_name(self, value=None):
        """  Corresponds to IDD Field `hn_function_of_temperature_difference_divided_by_height_curve_name`
        Curve's "x" is absolute value of delta-T/Height (Surface temp minus Air temp)/(vertical length scale), (C/m)
        when used for an outside face the vertical length scale is the exterior facade's overall height
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `hn_function_of_temperature_difference_divided_by_height_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hn_function_of_temperature_difference_divided_by_height_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hn_function_of_temperature_difference_divided_by_height_curve_name`')

        self._data["Hn Function of Temperature Difference Divided by Height Curve Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.wind_speed_type_for_curve))
        out.append(self._to_str(self.hf_function_of_wind_speed_curve_name))
        out.append(self._to_str(self.hn_function_of_temperature_difference_curve_name))
        out.append(self._to_str(self.hn_function_of_temperature_difference_divided_by_height_curve_name))
        return ",".join(out)