from collections import OrderedDict

class PipingSystemUndergroundDomain(object):
    """ Corresponds to IDD object `PipingSystem:Underground:Domain`
        The ground domain object for underground piping system simulation.
    """
    internal_name = "PipingSystem:Underground:Domain"
    field_count = 37

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PipingSystem:Underground:Domain`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Xmax"] = None
        self._data["Ymax"] = None
        self._data["Zmax"] = None
        self._data["X-Direction Mesh Density Parameter"] = None
        self._data["X-Direction Mesh Type"] = None
        self._data["X-Direction Geometric Coefficient"] = None
        self._data["Y-Direction Mesh Density Parameter"] = None
        self._data["Y-Direction Mesh Type"] = None
        self._data["Y-Direction Geometric Coefficient"] = None
        self._data["Z-Direction Mesh Density Parameter"] = None
        self._data["Z-Direction Mesh Type"] = None
        self._data["Z-Direction Geometric Coefficient"] = None
        self._data["Soil Thermal Conductivity"] = None
        self._data["Soil Density"] = None
        self._data["Soil Specific Heat"] = None
        self._data["Soil Moisture Content Volume Fraction"] = None
        self._data["Soil Moisture Content Volume Fraction at Saturation"] = None
        self._data["Kusuda-Achenbach Average Surface Temperature"] = None
        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = None
        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = None
        self._data["This Domain Includes Basement Surface Interaction"] = None
        self._data["Width of Basement Floor in Ground Domain"] = None
        self._data["Depth of Basement Wall In Ground Domain"] = None
        self._data["Shift Pipe X Coordinates By Basement Width"] = None
        self._data["Name of Basement Wall Boundary Condition Model"] = None
        self._data["Name of Basement Floor Boundary Condition Model"] = None
        self._data["Convergence Criterion for the Outer Cartesian Domain Iteration Loop"] = None
        self._data["Maximum Iterations in the Outer Cartesian Domain Iteration Loop"] = None
        self._data["Evapotranspiration Ground Cover Parameter"] = None
        self._data["Number of Pipe Circuits Entered for this Domain"] = None
        self._data["Pipe Circuit 1"] = None
        self._data["Pipe Circuit 2"] = None
        self._data["Pipe Circuit 3"] = None
        self._data["Pipe Circuit 4"] = None
        self._data["Pipe Circuit 5"] = None
        self._data["Pipe Circuit 6"] = None

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
            self.xmax = None
        else:
            self.xmax = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ymax = None
        else:
            self.ymax = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zmax = None
        else:
            self.zmax = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.xdirection_mesh_density_parameter = None
        else:
            self.xdirection_mesh_density_parameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.xdirection_mesh_type = None
        else:
            self.xdirection_mesh_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.xdirection_geometric_coefficient = None
        else:
            self.xdirection_geometric_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ydirection_mesh_density_parameter = None
        else:
            self.ydirection_mesh_density_parameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ydirection_mesh_type = None
        else:
            self.ydirection_mesh_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ydirection_geometric_coefficient = None
        else:
            self.ydirection_geometric_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zdirection_mesh_density_parameter = None
        else:
            self.zdirection_mesh_density_parameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zdirection_mesh_type = None
        else:
            self.zdirection_mesh_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zdirection_geometric_coefficient = None
        else:
            self.zdirection_geometric_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_thermal_conductivity = None
        else:
            self.soil_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_density = None
        else:
            self.soil_density = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_specific_heat = None
        else:
            self.soil_specific_heat = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_moisture_content_volume_fraction = None
        else:
            self.soil_moisture_content_volume_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_moisture_content_volume_fraction_at_saturation = None
        else:
            self.soil_moisture_content_volume_fraction_at_saturation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_surface_temperature = None
        else:
            self.kusudaachenbach_average_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = None
        else:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = None
        else:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.this_domain_includes_basement_surface_interaction = None
        else:
            self.this_domain_includes_basement_surface_interaction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.width_of_basement_floor_in_ground_domain = None
        else:
            self.width_of_basement_floor_in_ground_domain = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depth_of_basement_wall_in_ground_domain = None
        else:
            self.depth_of_basement_wall_in_ground_domain = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shift_pipe_x_coordinates_by_basement_width = None
        else:
            self.shift_pipe_x_coordinates_by_basement_width = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.name_of_basement_wall_boundary_condition_model = None
        else:
            self.name_of_basement_wall_boundary_condition_model = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.name_of_basement_floor_boundary_condition_model = None
        else:
            self.name_of_basement_floor_boundary_condition_model = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop = None
        else:
            self.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop = None
        else:
            self.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.evapotranspiration_ground_cover_parameter = None
        else:
            self.evapotranspiration_ground_cover_parameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_pipe_circuits_entered_for_this_domain = None
        else:
            self.number_of_pipe_circuits_entered_for_this_domain = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_circuit_1 = None
        else:
            self.pipe_circuit_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_circuit_2 = None
        else:
            self.pipe_circuit_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_circuit_3 = None
        else:
            self.pipe_circuit_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_circuit_4 = None
        else:
            self.pipe_circuit_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_circuit_5 = None
        else:
            self.pipe_circuit_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_circuit_6 = None
        else:
            self.pipe_circuit_6 = vals[i]
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
    def xmax(self):
        """Get xmax

        Returns:
            float: the value of `xmax` or None if not set
        """
        return self._data["Xmax"]

    @xmax.setter
    def xmax(self, value=None):
        """  Corresponds to IDD Field `xmax`
        Domain extent in the local 'X' direction

        Args:
            value (float): value for IDD Field `xmax`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `xmax`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `xmax`')

        self._data["Xmax"] = value

    @property
    def ymax(self):
        """Get ymax

        Returns:
            float: the value of `ymax` or None if not set
        """
        return self._data["Ymax"]

    @ymax.setter
    def ymax(self, value=None):
        """  Corresponds to IDD Field `ymax`
        Domain extent in the local 'Y' direction

        Args:
            value (float): value for IDD Field `ymax`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ymax`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ymax`')

        self._data["Ymax"] = value

    @property
    def zmax(self):
        """Get zmax

        Returns:
            float: the value of `zmax` or None if not set
        """
        return self._data["Zmax"]

    @zmax.setter
    def zmax(self, value=None):
        """  Corresponds to IDD Field `zmax`
        Domain extent in the local 'Y' direction

        Args:
            value (float): value for IDD Field `zmax`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `zmax`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `zmax`')

        self._data["Zmax"] = value

    @property
    def xdirection_mesh_density_parameter(self):
        """Get xdirection_mesh_density_parameter

        Returns:
            int: the value of `xdirection_mesh_density_parameter` or None if not set
        """
        return self._data["X-Direction Mesh Density Parameter"]

    @xdirection_mesh_density_parameter.setter
    def xdirection_mesh_density_parameter(self, value=4 ):
        """  Corresponds to IDD Field `xdirection_mesh_density_parameter`
        If mesh type is symmetric geometric, this should be an even number.

        Args:
            value (int): value for IDD Field `xdirection_mesh_density_parameter`
                Default value: 4
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `xdirection_mesh_density_parameter`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `xdirection_mesh_density_parameter`')

        self._data["X-Direction Mesh Density Parameter"] = value

    @property
    def xdirection_mesh_type(self):
        """Get xdirection_mesh_type

        Returns:
            str: the value of `xdirection_mesh_type` or None if not set
        """
        return self._data["X-Direction Mesh Type"]

    @xdirection_mesh_type.setter
    def xdirection_mesh_type(self, value=None):
        """  Corresponds to IDD Field `xdirection_mesh_type`

        Args:
            value (str): value for IDD Field `xdirection_mesh_type`
                Accepted values are:
                      - Uniform
                      - SymmetricGeometric
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
                                 'for field `xdirection_mesh_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `xdirection_mesh_type`')
            vals = set()
            vals.add("Uniform")
            vals.add("SymmetricGeometric")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `xdirection_mesh_type`'.format(value))

        self._data["X-Direction Mesh Type"] = value

    @property
    def xdirection_geometric_coefficient(self):
        """Get xdirection_geometric_coefficient

        Returns:
            float: the value of `xdirection_geometric_coefficient` or None if not set
        """
        return self._data["X-Direction Geometric Coefficient"]

    @xdirection_geometric_coefficient.setter
    def xdirection_geometric_coefficient(self, value=1.3 ):
        """  Corresponds to IDD Field `xdirection_geometric_coefficient`
        optional
        Only used if mesh type is symmetric geometric

        Args:
            value (float): value for IDD Field `xdirection_geometric_coefficient`
                Default value: 1.3
                value >= 1.0
                value <= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `xdirection_geometric_coefficient`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `xdirection_geometric_coefficient`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `xdirection_geometric_coefficient`')

        self._data["X-Direction Geometric Coefficient"] = value

    @property
    def ydirection_mesh_density_parameter(self):
        """Get ydirection_mesh_density_parameter

        Returns:
            int: the value of `ydirection_mesh_density_parameter` or None if not set
        """
        return self._data["Y-Direction Mesh Density Parameter"]

    @ydirection_mesh_density_parameter.setter
    def ydirection_mesh_density_parameter(self, value=4 ):
        """  Corresponds to IDD Field `ydirection_mesh_density_parameter`
        If mesh type is symmetric geometric, this should be an even number.

        Args:
            value (int): value for IDD Field `ydirection_mesh_density_parameter`
                Default value: 4
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `ydirection_mesh_density_parameter`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `ydirection_mesh_density_parameter`')

        self._data["Y-Direction Mesh Density Parameter"] = value

    @property
    def ydirection_mesh_type(self):
        """Get ydirection_mesh_type

        Returns:
            str: the value of `ydirection_mesh_type` or None if not set
        """
        return self._data["Y-Direction Mesh Type"]

    @ydirection_mesh_type.setter
    def ydirection_mesh_type(self, value=None):
        """  Corresponds to IDD Field `ydirection_mesh_type`

        Args:
            value (str): value for IDD Field `ydirection_mesh_type`
                Accepted values are:
                      - Uniform
                      - SymmetricGeometric
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
                                 'for field `ydirection_mesh_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ydirection_mesh_type`')
            vals = set()
            vals.add("Uniform")
            vals.add("SymmetricGeometric")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `ydirection_mesh_type`'.format(value))

        self._data["Y-Direction Mesh Type"] = value

    @property
    def ydirection_geometric_coefficient(self):
        """Get ydirection_geometric_coefficient

        Returns:
            float: the value of `ydirection_geometric_coefficient` or None if not set
        """
        return self._data["Y-Direction Geometric Coefficient"]

    @ydirection_geometric_coefficient.setter
    def ydirection_geometric_coefficient(self, value=1.3 ):
        """  Corresponds to IDD Field `ydirection_geometric_coefficient`
        optional
        Only used if mesh type is symmetric geometric

        Args:
            value (float): value for IDD Field `ydirection_geometric_coefficient`
                Default value: 1.3
                value >= 1.0
                value <= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ydirection_geometric_coefficient`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `ydirection_geometric_coefficient`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `ydirection_geometric_coefficient`')

        self._data["Y-Direction Geometric Coefficient"] = value

    @property
    def zdirection_mesh_density_parameter(self):
        """Get zdirection_mesh_density_parameter

        Returns:
            int: the value of `zdirection_mesh_density_parameter` or None if not set
        """
        return self._data["Z-Direction Mesh Density Parameter"]

    @zdirection_mesh_density_parameter.setter
    def zdirection_mesh_density_parameter(self, value=4 ):
        """  Corresponds to IDD Field `zdirection_mesh_density_parameter`
        If mesh type is symmetric geometric, this should be an even number.

        Args:
            value (int): value for IDD Field `zdirection_mesh_density_parameter`
                Default value: 4
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `zdirection_mesh_density_parameter`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `zdirection_mesh_density_parameter`')

        self._data["Z-Direction Mesh Density Parameter"] = value

    @property
    def zdirection_mesh_type(self):
        """Get zdirection_mesh_type

        Returns:
            str: the value of `zdirection_mesh_type` or None if not set
        """
        return self._data["Z-Direction Mesh Type"]

    @zdirection_mesh_type.setter
    def zdirection_mesh_type(self, value=None):
        """  Corresponds to IDD Field `zdirection_mesh_type`

        Args:
            value (str): value for IDD Field `zdirection_mesh_type`
                Accepted values are:
                      - Uniform
                      - SymmetricGeometric
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
                                 'for field `zdirection_mesh_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zdirection_mesh_type`')
            vals = set()
            vals.add("Uniform")
            vals.add("SymmetricGeometric")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `zdirection_mesh_type`'.format(value))

        self._data["Z-Direction Mesh Type"] = value

    @property
    def zdirection_geometric_coefficient(self):
        """Get zdirection_geometric_coefficient

        Returns:
            float: the value of `zdirection_geometric_coefficient` or None if not set
        """
        return self._data["Z-Direction Geometric Coefficient"]

    @zdirection_geometric_coefficient.setter
    def zdirection_geometric_coefficient(self, value=1.3 ):
        """  Corresponds to IDD Field `zdirection_geometric_coefficient`
        optional
        Only used if mesh type is symmetric geometric

        Args:
            value (float): value for IDD Field `zdirection_geometric_coefficient`
                Default value: 1.3
                value >= 1.0
                value <= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `zdirection_geometric_coefficient`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `zdirection_geometric_coefficient`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `zdirection_geometric_coefficient`')

        self._data["Z-Direction Geometric Coefficient"] = value

    @property
    def soil_thermal_conductivity(self):
        """Get soil_thermal_conductivity

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set
        """
        return self._data["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `soil_thermal_conductivity`

        Args:
            value (float): value for IDD Field `soil_thermal_conductivity`
                Unit: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_thermal_conductivity`')

        self._data["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """Get soil_density

        Returns:
            float: the value of `soil_density` or None if not set
        """
        return self._data["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=None):
        """  Corresponds to IDD Field `soil_density`

        Args:
            value (float): value for IDD Field `soil_density`
                Unit: kg/m3
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_density`')

        self._data["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """Get soil_specific_heat

        Returns:
            float: the value of `soil_specific_heat` or None if not set
        """
        return self._data["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=None):
        """  Corresponds to IDD Field `soil_specific_heat`
        This is a dry soil property, which is adjusted for freezing effects
        by the simulation algorithm.

        Args:
            value (float): value for IDD Field `soil_specific_heat`
                Unit: J/kg-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_specific_heat`')

        self._data["Soil Specific Heat"] = value

    @property
    def soil_moisture_content_volume_fraction(self):
        """Get soil_moisture_content_volume_fraction

        Returns:
            float: the value of `soil_moisture_content_volume_fraction` or None if not set
        """
        return self._data["Soil Moisture Content Volume Fraction"]

    @soil_moisture_content_volume_fraction.setter
    def soil_moisture_content_volume_fraction(self, value=30.0 ):
        """  Corresponds to IDD Field `soil_moisture_content_volume_fraction`

        Args:
            value (float): value for IDD Field `soil_moisture_content_volume_fraction`
                Unit: percent
                Default value: 30.0
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_moisture_content_volume_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `soil_moisture_content_volume_fraction`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `soil_moisture_content_volume_fraction`')

        self._data["Soil Moisture Content Volume Fraction"] = value

    @property
    def soil_moisture_content_volume_fraction_at_saturation(self):
        """Get soil_moisture_content_volume_fraction_at_saturation

        Returns:
            float: the value of `soil_moisture_content_volume_fraction_at_saturation` or None if not set
        """
        return self._data["Soil Moisture Content Volume Fraction at Saturation"]

    @soil_moisture_content_volume_fraction_at_saturation.setter
    def soil_moisture_content_volume_fraction_at_saturation(self, value=50.0 ):
        """  Corresponds to IDD Field `soil_moisture_content_volume_fraction_at_saturation`

        Args:
            value (float): value for IDD Field `soil_moisture_content_volume_fraction_at_saturation`
                Unit: percent
                Default value: 50.0
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_moisture_content_volume_fraction_at_saturation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `soil_moisture_content_volume_fraction_at_saturation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `soil_moisture_content_volume_fraction_at_saturation`')

        self._data["Soil Moisture Content Volume Fraction at Saturation"] = value

    @property
    def kusudaachenbach_average_surface_temperature(self):
        """Get kusudaachenbach_average_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Surface Temperature"]

    @kusudaachenbach_average_surface_temperature.setter
    def kusudaachenbach_average_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_average_surface_temperature`

        Args:
            value (float): value for IDD Field `kusudaachenbach_average_surface_temperature`
                Unit: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_average_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Average Surface Temperature"] = value

    @property
    def kusudaachenbach_average_amplitude_of_surface_temperature(self):
        """Get kusudaachenbach_average_amplitude_of_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_amplitude_of_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"]

    @kusudaachenbach_average_amplitude_of_surface_temperature.setter
    def kusudaachenbach_average_amplitude_of_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_average_amplitude_of_surface_temperature`

        Args:
            value (float): value for IDD Field `kusudaachenbach_average_amplitude_of_surface_temperature`
                Unit: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_average_amplitude_of_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = value

    @property
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self):
        """Get kusudaachenbach_phase_shift_of_minimum_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_phase_shift_of_minimum_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"]

    @kusudaachenbach_phase_shift_of_minimum_surface_temperature.setter
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`

        Args:
            value (float): value for IDD Field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`
                Unit: days
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = value

    @property
    def this_domain_includes_basement_surface_interaction(self):
        """Get this_domain_includes_basement_surface_interaction

        Returns:
            str: the value of `this_domain_includes_basement_surface_interaction` or None if not set
        """
        return self._data["This Domain Includes Basement Surface Interaction"]

    @this_domain_includes_basement_surface_interaction.setter
    def this_domain_includes_basement_surface_interaction(self, value="No"):
        """  Corresponds to IDD Field `this_domain_includes_basement_surface_interaction`
        if Yes, then the following basement inputs are used
        if No, then the following basement inputs are *ignored*

        Args:
            value (str): value for IDD Field `this_domain_includes_basement_surface_interaction`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 'for field `this_domain_includes_basement_surface_interaction`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `this_domain_includes_basement_surface_interaction`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `this_domain_includes_basement_surface_interaction`'.format(value))

        self._data["This Domain Includes Basement Surface Interaction"] = value

    @property
    def width_of_basement_floor_in_ground_domain(self):
        """Get width_of_basement_floor_in_ground_domain

        Returns:
            float: the value of `width_of_basement_floor_in_ground_domain` or None if not set
        """
        return self._data["Width of Basement Floor in Ground Domain"]

    @width_of_basement_floor_in_ground_domain.setter
    def width_of_basement_floor_in_ground_domain(self, value=None):
        """  Corresponds to IDD Field `width_of_basement_floor_in_ground_domain`
        Required only if Domain Has Basement Interaction

        Args:
            value (float): value for IDD Field `width_of_basement_floor_in_ground_domain`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `width_of_basement_floor_in_ground_domain`'.format(value))

        self._data["Width of Basement Floor in Ground Domain"] = value

    @property
    def depth_of_basement_wall_in_ground_domain(self):
        """Get depth_of_basement_wall_in_ground_domain

        Returns:
            float: the value of `depth_of_basement_wall_in_ground_domain` or None if not set
        """
        return self._data["Depth of Basement Wall In Ground Domain"]

    @depth_of_basement_wall_in_ground_domain.setter
    def depth_of_basement_wall_in_ground_domain(self, value=None):
        """  Corresponds to IDD Field `depth_of_basement_wall_in_ground_domain`
        Required only if Domain Has Basement Interaction

        Args:
            value (float): value for IDD Field `depth_of_basement_wall_in_ground_domain`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `depth_of_basement_wall_in_ground_domain`'.format(value))

        self._data["Depth of Basement Wall In Ground Domain"] = value

    @property
    def shift_pipe_x_coordinates_by_basement_width(self):
        """Get shift_pipe_x_coordinates_by_basement_width

        Returns:
            str: the value of `shift_pipe_x_coordinates_by_basement_width` or None if not set
        """
        return self._data["Shift Pipe X Coordinates By Basement Width"]

    @shift_pipe_x_coordinates_by_basement_width.setter
    def shift_pipe_x_coordinates_by_basement_width(self, value=None):
        """  Corresponds to IDD Field `shift_pipe_x_coordinates_by_basement_width`
        Required only if Domain Has Basement Interaction

        Args:
            value (str): value for IDD Field `shift_pipe_x_coordinates_by_basement_width`
                Accepted values are:
                      - Yes
                      - No
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
                                 'for field `shift_pipe_x_coordinates_by_basement_width`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `shift_pipe_x_coordinates_by_basement_width`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `shift_pipe_x_coordinates_by_basement_width`'.format(value))

        self._data["Shift Pipe X Coordinates By Basement Width"] = value

    @property
    def name_of_basement_wall_boundary_condition_model(self):
        """Get name_of_basement_wall_boundary_condition_model

        Returns:
            str: the value of `name_of_basement_wall_boundary_condition_model` or None if not set
        """
        return self._data["Name of Basement Wall Boundary Condition Model"]

    @name_of_basement_wall_boundary_condition_model.setter
    def name_of_basement_wall_boundary_condition_model(self, value=None):
        """  Corresponds to IDD Field `name_of_basement_wall_boundary_condition_model`
        Required only if Domain Has Basement Interaction

        Args:
            value (str): value for IDD Field `name_of_basement_wall_boundary_condition_model`
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
                                 'for field `name_of_basement_wall_boundary_condition_model`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name_of_basement_wall_boundary_condition_model`')

        self._data["Name of Basement Wall Boundary Condition Model"] = value

    @property
    def name_of_basement_floor_boundary_condition_model(self):
        """Get name_of_basement_floor_boundary_condition_model

        Returns:
            str: the value of `name_of_basement_floor_boundary_condition_model` or None if not set
        """
        return self._data["Name of Basement Floor Boundary Condition Model"]

    @name_of_basement_floor_boundary_condition_model.setter
    def name_of_basement_floor_boundary_condition_model(self, value=None):
        """  Corresponds to IDD Field `name_of_basement_floor_boundary_condition_model`
        Required only if Domain Has Basement Interaction

        Args:
            value (str): value for IDD Field `name_of_basement_floor_boundary_condition_model`
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
                                 'for field `name_of_basement_floor_boundary_condition_model`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name_of_basement_floor_boundary_condition_model`')

        self._data["Name of Basement Floor Boundary Condition Model"] = value

    @property
    def convergence_criterion_for_the_outer_cartesian_domain_iteration_loop(self):
        """Get convergence_criterion_for_the_outer_cartesian_domain_iteration_loop

        Returns:
            float: the value of `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop` or None if not set
        """
        return self._data["Convergence Criterion for the Outer Cartesian Domain Iteration Loop"]

    @convergence_criterion_for_the_outer_cartesian_domain_iteration_loop.setter
    def convergence_criterion_for_the_outer_cartesian_domain_iteration_loop(self, value=0.001 ):
        """  Corresponds to IDD Field `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`

        Args:
            value (float): value for IDD Field `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`
                Unit: deltaC
                Default value: 0.001
                value >= 1e-06
                value <= 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`'.format(value))
            if value < 1e-06:
                raise ValueError('value need to be greater or equal 1e-06 '
                                 'for field `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`')

        self._data["Convergence Criterion for the Outer Cartesian Domain Iteration Loop"] = value

    @property
    def maximum_iterations_in_the_outer_cartesian_domain_iteration_loop(self):
        """Get maximum_iterations_in_the_outer_cartesian_domain_iteration_loop

        Returns:
            int: the value of `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop` or None if not set
        """
        return self._data["Maximum Iterations in the Outer Cartesian Domain Iteration Loop"]

    @maximum_iterations_in_the_outer_cartesian_domain_iteration_loop.setter
    def maximum_iterations_in_the_outer_cartesian_domain_iteration_loop(self, value=500 ):
        """  Corresponds to IDD Field `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`

        Args:
            value (int): value for IDD Field `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`
                Default value: 500
                value >= 3
                value <= 10000
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`'.format(value))
            if value < 3:
                raise ValueError('value need to be greater or equal 3 '
                                 'for field `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`')
            if value > 10000:
                raise ValueError('value need to be smaller 10000 '
                                 'for field `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`')

        self._data["Maximum Iterations in the Outer Cartesian Domain Iteration Loop"] = value

    @property
    def evapotranspiration_ground_cover_parameter(self):
        """Get evapotranspiration_ground_cover_parameter

        Returns:
            float: the value of `evapotranspiration_ground_cover_parameter` or None if not set
        """
        return self._data["Evapotranspiration Ground Cover Parameter"]

    @evapotranspiration_ground_cover_parameter.setter
    def evapotranspiration_ground_cover_parameter(self, value=0.4 ):
        """  Corresponds to IDD Field `evapotranspiration_ground_cover_parameter`
        This specifies the ground cover effects during evapotranspiration
        calculations.  The value roughly represents the following cases:
        = 0   : concrete or other solid, non-permeable ground surface material
        = 0.5 : short grass, much like a manicured lawn
        = 1   : standard reference state (12 cm grass)
        = 1.5 : wild growth

        Args:
            value (float): value for IDD Field `evapotranspiration_ground_cover_parameter`
                Default value: 0.4
                value >= 0.0
                value <= 1.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `evapotranspiration_ground_cover_parameter`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evapotranspiration_ground_cover_parameter`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `evapotranspiration_ground_cover_parameter`')

        self._data["Evapotranspiration Ground Cover Parameter"] = value

    @property
    def number_of_pipe_circuits_entered_for_this_domain(self):
        """Get number_of_pipe_circuits_entered_for_this_domain

        Returns:
            int: the value of `number_of_pipe_circuits_entered_for_this_domain` or None if not set
        """
        return self._data["Number of Pipe Circuits Entered for this Domain"]

    @number_of_pipe_circuits_entered_for_this_domain.setter
    def number_of_pipe_circuits_entered_for_this_domain(self, value=None):
        """  Corresponds to IDD Field `number_of_pipe_circuits_entered_for_this_domain`

        Args:
            value (int): value for IDD Field `number_of_pipe_circuits_entered_for_this_domain`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_pipe_circuits_entered_for_this_domain`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_pipe_circuits_entered_for_this_domain`')

        self._data["Number of Pipe Circuits Entered for this Domain"] = value

    @property
    def pipe_circuit_1(self):
        """Get pipe_circuit_1

        Returns:
            str: the value of `pipe_circuit_1` or None if not set
        """
        return self._data["Pipe Circuit 1"]

    @pipe_circuit_1.setter
    def pipe_circuit_1(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_1`
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_1`
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
                                 'for field `pipe_circuit_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_1`')

        self._data["Pipe Circuit 1"] = value

    @property
    def pipe_circuit_2(self):
        """Get pipe_circuit_2

        Returns:
            str: the value of `pipe_circuit_2` or None if not set
        """
        return self._data["Pipe Circuit 2"]

    @pipe_circuit_2.setter
    def pipe_circuit_2(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_2`
        optional
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_2`
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
                                 'for field `pipe_circuit_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_2`')

        self._data["Pipe Circuit 2"] = value

    @property
    def pipe_circuit_3(self):
        """Get pipe_circuit_3

        Returns:
            str: the value of `pipe_circuit_3` or None if not set
        """
        return self._data["Pipe Circuit 3"]

    @pipe_circuit_3.setter
    def pipe_circuit_3(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_3`
        optional
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_3`
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
                                 'for field `pipe_circuit_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_3`')

        self._data["Pipe Circuit 3"] = value

    @property
    def pipe_circuit_4(self):
        """Get pipe_circuit_4

        Returns:
            str: the value of `pipe_circuit_4` or None if not set
        """
        return self._data["Pipe Circuit 4"]

    @pipe_circuit_4.setter
    def pipe_circuit_4(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_4`
        optional
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_4`
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
                                 'for field `pipe_circuit_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_4`')

        self._data["Pipe Circuit 4"] = value

    @property
    def pipe_circuit_5(self):
        """Get pipe_circuit_5

        Returns:
            str: the value of `pipe_circuit_5` or None if not set
        """
        return self._data["Pipe Circuit 5"]

    @pipe_circuit_5.setter
    def pipe_circuit_5(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_5`
        optional
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_5`
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
                                 'for field `pipe_circuit_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_5`')

        self._data["Pipe Circuit 5"] = value

    @property
    def pipe_circuit_6(self):
        """Get pipe_circuit_6

        Returns:
            str: the value of `pipe_circuit_6` or None if not set
        """
        return self._data["Pipe Circuit 6"]

    @pipe_circuit_6.setter
    def pipe_circuit_6(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_6`
        optional
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_6`
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
                                 'for field `pipe_circuit_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_6`')

        self._data["Pipe Circuit 6"] = value

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
        out.append(self._to_str(self.xmax))
        out.append(self._to_str(self.ymax))
        out.append(self._to_str(self.zmax))
        out.append(self._to_str(self.xdirection_mesh_density_parameter))
        out.append(self._to_str(self.xdirection_mesh_type))
        out.append(self._to_str(self.xdirection_geometric_coefficient))
        out.append(self._to_str(self.ydirection_mesh_density_parameter))
        out.append(self._to_str(self.ydirection_mesh_type))
        out.append(self._to_str(self.ydirection_geometric_coefficient))
        out.append(self._to_str(self.zdirection_mesh_density_parameter))
        out.append(self._to_str(self.zdirection_mesh_type))
        out.append(self._to_str(self.zdirection_geometric_coefficient))
        out.append(self._to_str(self.soil_thermal_conductivity))
        out.append(self._to_str(self.soil_density))
        out.append(self._to_str(self.soil_specific_heat))
        out.append(self._to_str(self.soil_moisture_content_volume_fraction))
        out.append(self._to_str(self.soil_moisture_content_volume_fraction_at_saturation))
        out.append(self._to_str(self.kusudaachenbach_average_surface_temperature))
        out.append(self._to_str(self.kusudaachenbach_average_amplitude_of_surface_temperature))
        out.append(self._to_str(self.kusudaachenbach_phase_shift_of_minimum_surface_temperature))
        out.append(self._to_str(self.this_domain_includes_basement_surface_interaction))
        out.append(self._to_str(self.width_of_basement_floor_in_ground_domain))
        out.append(self._to_str(self.depth_of_basement_wall_in_ground_domain))
        out.append(self._to_str(self.shift_pipe_x_coordinates_by_basement_width))
        out.append(self._to_str(self.name_of_basement_wall_boundary_condition_model))
        out.append(self._to_str(self.name_of_basement_floor_boundary_condition_model))
        out.append(self._to_str(self.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop))
        out.append(self._to_str(self.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop))
        out.append(self._to_str(self.evapotranspiration_ground_cover_parameter))
        out.append(self._to_str(self.number_of_pipe_circuits_entered_for_this_domain))
        out.append(self._to_str(self.pipe_circuit_1))
        out.append(self._to_str(self.pipe_circuit_2))
        out.append(self._to_str(self.pipe_circuit_3))
        out.append(self._to_str(self.pipe_circuit_4))
        out.append(self._to_str(self.pipe_circuit_5))
        out.append(self._to_str(self.pipe_circuit_6))
        return ",".join(out)

class PipingSystemUndergroundPipeCircuit(object):
    """ Corresponds to IDD object `PipingSystem:Underground:PipeCircuit`
        The pipe circuit object in an underground piping system.
        This object is simulated within an underground piping domain object
        and connected on a branch on a plant loop.
    """
    internal_name = "PipingSystem:Underground:PipeCircuit"
    field_count = 20

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PipingSystem:Underground:PipeCircuit`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Pipe Thermal Conductivity"] = None
        self._data["Pipe Density"] = None
        self._data["Pipe Specific Heat"] = None
        self._data["Pipe Inner Diameter"] = None
        self._data["Pipe Outer Diameter"] = None
        self._data["Design Flow Rate"] = None
        self._data["Circuit Inlet Node"] = None
        self._data["Circuit Outlet Node"] = None
        self._data["Convergence Criterion for the Inner Radial Iteration Loop"] = None
        self._data["Maximum Iterations in the Inner Radial Iteration Loop"] = None
        self._data["Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region"] = None
        self._data["Radial Thickness of Inner Radial Near Pipe Mesh Region"] = None
        self._data["Number of Pipe Segments Entered for this Pipe Circuit"] = None
        self._data["Pipe Segment 1"] = None
        self._data["Pipe Segment 2"] = None
        self._data["Pipe Segment 3"] = None
        self._data["Pipe Segment 4"] = None
        self._data["Pipe Segment 5"] = None
        self._data["Pipe Segment 6"] = None

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
            self.pipe_thermal_conductivity = None
        else:
            self.pipe_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_density = None
        else:
            self.pipe_density = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_specific_heat = None
        else:
            self.pipe_specific_heat = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_inner_diameter = None
        else:
            self.pipe_inner_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_outer_diameter = None
        else:
            self.pipe_outer_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.circuit_inlet_node = None
        else:
            self.circuit_inlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.circuit_outlet_node = None
        else:
            self.circuit_outlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convergence_criterion_for_the_inner_radial_iteration_loop = None
        else:
            self.convergence_criterion_for_the_inner_radial_iteration_loop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_iterations_in_the_inner_radial_iteration_loop = None
        else:
            self.maximum_iterations_in_the_inner_radial_iteration_loop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region = None
        else:
            self.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.radial_thickness_of_inner_radial_near_pipe_mesh_region = None
        else:
            self.radial_thickness_of_inner_radial_near_pipe_mesh_region = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_pipe_segments_entered_for_this_pipe_circuit = None
        else:
            self.number_of_pipe_segments_entered_for_this_pipe_circuit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_segment_1 = None
        else:
            self.pipe_segment_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_segment_2 = None
        else:
            self.pipe_segment_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_segment_3 = None
        else:
            self.pipe_segment_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_segment_4 = None
        else:
            self.pipe_segment_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_segment_5 = None
        else:
            self.pipe_segment_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_segment_6 = None
        else:
            self.pipe_segment_6 = vals[i]
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
    def pipe_thermal_conductivity(self):
        """Get pipe_thermal_conductivity

        Returns:
            float: the value of `pipe_thermal_conductivity` or None if not set
        """
        return self._data["Pipe Thermal Conductivity"]

    @pipe_thermal_conductivity.setter
    def pipe_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `pipe_thermal_conductivity`

        Args:
            value (float): value for IDD Field `pipe_thermal_conductivity`
                Unit: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_thermal_conductivity`')

        self._data["Pipe Thermal Conductivity"] = value

    @property
    def pipe_density(self):
        """Get pipe_density

        Returns:
            float: the value of `pipe_density` or None if not set
        """
        return self._data["Pipe Density"]

    @pipe_density.setter
    def pipe_density(self, value=None):
        """  Corresponds to IDD Field `pipe_density`

        Args:
            value (float): value for IDD Field `pipe_density`
                Unit: kg/m3
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_density`')

        self._data["Pipe Density"] = value

    @property
    def pipe_specific_heat(self):
        """Get pipe_specific_heat

        Returns:
            float: the value of `pipe_specific_heat` or None if not set
        """
        return self._data["Pipe Specific Heat"]

    @pipe_specific_heat.setter
    def pipe_specific_heat(self, value=None):
        """  Corresponds to IDD Field `pipe_specific_heat`

        Args:
            value (float): value for IDD Field `pipe_specific_heat`
                Unit: J/kg-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_specific_heat`')

        self._data["Pipe Specific Heat"] = value

    @property
    def pipe_inner_diameter(self):
        """Get pipe_inner_diameter

        Returns:
            float: the value of `pipe_inner_diameter` or None if not set
        """
        return self._data["Pipe Inner Diameter"]

    @pipe_inner_diameter.setter
    def pipe_inner_diameter(self, value=None):
        """  Corresponds to IDD Field `pipe_inner_diameter`

        Args:
            value (float): value for IDD Field `pipe_inner_diameter`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_inner_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_inner_diameter`')

        self._data["Pipe Inner Diameter"] = value

    @property
    def pipe_outer_diameter(self):
        """Get pipe_outer_diameter

        Returns:
            float: the value of `pipe_outer_diameter` or None if not set
        """
        return self._data["Pipe Outer Diameter"]

    @pipe_outer_diameter.setter
    def pipe_outer_diameter(self, value=None):
        """  Corresponds to IDD Field `pipe_outer_diameter`

        Args:
            value (float): value for IDD Field `pipe_outer_diameter`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_outer_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_outer_diameter`')

        self._data["Pipe Outer Diameter"] = value

    @property
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_flow_rate`

        Args:
            value (float): value for IDD Field `design_flow_rate`
                Unit: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_flow_rate`')

        self._data["Design Flow Rate"] = value

    @property
    def circuit_inlet_node(self):
        """Get circuit_inlet_node

        Returns:
            str: the value of `circuit_inlet_node` or None if not set
        """
        return self._data["Circuit Inlet Node"]

    @circuit_inlet_node.setter
    def circuit_inlet_node(self, value=None):
        """  Corresponds to IDD Field `circuit_inlet_node`

        Args:
            value (str): value for IDD Field `circuit_inlet_node`
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
                                 'for field `circuit_inlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `circuit_inlet_node`')

        self._data["Circuit Inlet Node"] = value

    @property
    def circuit_outlet_node(self):
        """Get circuit_outlet_node

        Returns:
            str: the value of `circuit_outlet_node` or None if not set
        """
        return self._data["Circuit Outlet Node"]

    @circuit_outlet_node.setter
    def circuit_outlet_node(self, value=None):
        """  Corresponds to IDD Field `circuit_outlet_node`

        Args:
            value (str): value for IDD Field `circuit_outlet_node`
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
                                 'for field `circuit_outlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `circuit_outlet_node`')

        self._data["Circuit Outlet Node"] = value

    @property
    def convergence_criterion_for_the_inner_radial_iteration_loop(self):
        """Get convergence_criterion_for_the_inner_radial_iteration_loop

        Returns:
            float: the value of `convergence_criterion_for_the_inner_radial_iteration_loop` or None if not set
        """
        return self._data["Convergence Criterion for the Inner Radial Iteration Loop"]

    @convergence_criterion_for_the_inner_radial_iteration_loop.setter
    def convergence_criterion_for_the_inner_radial_iteration_loop(self, value=0.001 ):
        """  Corresponds to IDD Field `convergence_criterion_for_the_inner_radial_iteration_loop`

        Args:
            value (float): value for IDD Field `convergence_criterion_for_the_inner_radial_iteration_loop`
                Unit: deltaC
                Default value: 0.001
                value >= 1e-06
                value <= 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `convergence_criterion_for_the_inner_radial_iteration_loop`'.format(value))
            if value < 1e-06:
                raise ValueError('value need to be greater or equal 1e-06 '
                                 'for field `convergence_criterion_for_the_inner_radial_iteration_loop`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `convergence_criterion_for_the_inner_radial_iteration_loop`')

        self._data["Convergence Criterion for the Inner Radial Iteration Loop"] = value

    @property
    def maximum_iterations_in_the_inner_radial_iteration_loop(self):
        """Get maximum_iterations_in_the_inner_radial_iteration_loop

        Returns:
            int: the value of `maximum_iterations_in_the_inner_radial_iteration_loop` or None if not set
        """
        return self._data["Maximum Iterations in the Inner Radial Iteration Loop"]

    @maximum_iterations_in_the_inner_radial_iteration_loop.setter
    def maximum_iterations_in_the_inner_radial_iteration_loop(self, value=500 ):
        """  Corresponds to IDD Field `maximum_iterations_in_the_inner_radial_iteration_loop`

        Args:
            value (int): value for IDD Field `maximum_iterations_in_the_inner_radial_iteration_loop`
                Default value: 500
                value >= 3
                value <= 10000
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `maximum_iterations_in_the_inner_radial_iteration_loop`'.format(value))
            if value < 3:
                raise ValueError('value need to be greater or equal 3 '
                                 'for field `maximum_iterations_in_the_inner_radial_iteration_loop`')
            if value > 10000:
                raise ValueError('value need to be smaller 10000 '
                                 'for field `maximum_iterations_in_the_inner_radial_iteration_loop`')

        self._data["Maximum Iterations in the Inner Radial Iteration Loop"] = value

    @property
    def number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region(self):
        """Get number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region

        Returns:
            int: the value of `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region` or None if not set
        """
        return self._data["Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region"]

    @number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region.setter
    def number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region(self, value=3 ):
        """  Corresponds to IDD Field `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`

        Args:
            value (int): value for IDD Field `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`
                Default value: 3
                value >= 1
                value <= 15
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`')
            if value > 15:
                raise ValueError('value need to be smaller 15 '
                                 'for field `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`')

        self._data["Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region"] = value

    @property
    def radial_thickness_of_inner_radial_near_pipe_mesh_region(self):
        """Get radial_thickness_of_inner_radial_near_pipe_mesh_region

        Returns:
            float: the value of `radial_thickness_of_inner_radial_near_pipe_mesh_region` or None if not set
        """
        return self._data["Radial Thickness of Inner Radial Near Pipe Mesh Region"]

    @radial_thickness_of_inner_radial_near_pipe_mesh_region.setter
    def radial_thickness_of_inner_radial_near_pipe_mesh_region(self, value=None):
        """  Corresponds to IDD Field `radial_thickness_of_inner_radial_near_pipe_mesh_region`
        Required because it must be selected by user instead of being
        inferred from circuit/domain object inputs.

        Args:
            value (float): value for IDD Field `radial_thickness_of_inner_radial_near_pipe_mesh_region`
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `radial_thickness_of_inner_radial_near_pipe_mesh_region`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `radial_thickness_of_inner_radial_near_pipe_mesh_region`')

        self._data["Radial Thickness of Inner Radial Near Pipe Mesh Region"] = value

    @property
    def number_of_pipe_segments_entered_for_this_pipe_circuit(self):
        """Get number_of_pipe_segments_entered_for_this_pipe_circuit

        Returns:
            int: the value of `number_of_pipe_segments_entered_for_this_pipe_circuit` or None if not set
        """
        return self._data["Number of Pipe Segments Entered for this Pipe Circuit"]

    @number_of_pipe_segments_entered_for_this_pipe_circuit.setter
    def number_of_pipe_segments_entered_for_this_pipe_circuit(self, value=None):
        """  Corresponds to IDD Field `number_of_pipe_segments_entered_for_this_pipe_circuit`

        Args:
            value (int): value for IDD Field `number_of_pipe_segments_entered_for_this_pipe_circuit`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_pipe_segments_entered_for_this_pipe_circuit`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_pipe_segments_entered_for_this_pipe_circuit`')

        self._data["Number of Pipe Segments Entered for this Pipe Circuit"] = value

    @property
    def pipe_segment_1(self):
        """Get pipe_segment_1

        Returns:
            str: the value of `pipe_segment_1` or None if not set
        """
        return self._data["Pipe Segment 1"]

    @pipe_segment_1.setter
    def pipe_segment_1(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_1`
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_1`
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
                                 'for field `pipe_segment_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_1`')

        self._data["Pipe Segment 1"] = value

    @property
    def pipe_segment_2(self):
        """Get pipe_segment_2

        Returns:
            str: the value of `pipe_segment_2` or None if not set
        """
        return self._data["Pipe Segment 2"]

    @pipe_segment_2.setter
    def pipe_segment_2(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_2`
        optional
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_2`
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
                                 'for field `pipe_segment_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_2`')

        self._data["Pipe Segment 2"] = value

    @property
    def pipe_segment_3(self):
        """Get pipe_segment_3

        Returns:
            str: the value of `pipe_segment_3` or None if not set
        """
        return self._data["Pipe Segment 3"]

    @pipe_segment_3.setter
    def pipe_segment_3(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_3`
        optional
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_3`
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
                                 'for field `pipe_segment_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_3`')

        self._data["Pipe Segment 3"] = value

    @property
    def pipe_segment_4(self):
        """Get pipe_segment_4

        Returns:
            str: the value of `pipe_segment_4` or None if not set
        """
        return self._data["Pipe Segment 4"]

    @pipe_segment_4.setter
    def pipe_segment_4(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_4`
        optional
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_4`
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
                                 'for field `pipe_segment_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_4`')

        self._data["Pipe Segment 4"] = value

    @property
    def pipe_segment_5(self):
        """Get pipe_segment_5

        Returns:
            str: the value of `pipe_segment_5` or None if not set
        """
        return self._data["Pipe Segment 5"]

    @pipe_segment_5.setter
    def pipe_segment_5(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_5`
        optional
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_5`
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
                                 'for field `pipe_segment_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_5`')

        self._data["Pipe Segment 5"] = value

    @property
    def pipe_segment_6(self):
        """Get pipe_segment_6

        Returns:
            str: the value of `pipe_segment_6` or None if not set
        """
        return self._data["Pipe Segment 6"]

    @pipe_segment_6.setter
    def pipe_segment_6(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_6`
        optional
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_6`
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
                                 'for field `pipe_segment_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_6`')

        self._data["Pipe Segment 6"] = value

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
        out.append(self._to_str(self.pipe_thermal_conductivity))
        out.append(self._to_str(self.pipe_density))
        out.append(self._to_str(self.pipe_specific_heat))
        out.append(self._to_str(self.pipe_inner_diameter))
        out.append(self._to_str(self.pipe_outer_diameter))
        out.append(self._to_str(self.design_flow_rate))
        out.append(self._to_str(self.circuit_inlet_node))
        out.append(self._to_str(self.circuit_outlet_node))
        out.append(self._to_str(self.convergence_criterion_for_the_inner_radial_iteration_loop))
        out.append(self._to_str(self.maximum_iterations_in_the_inner_radial_iteration_loop))
        out.append(self._to_str(self.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region))
        out.append(self._to_str(self.radial_thickness_of_inner_radial_near_pipe_mesh_region))
        out.append(self._to_str(self.number_of_pipe_segments_entered_for_this_pipe_circuit))
        out.append(self._to_str(self.pipe_segment_1))
        out.append(self._to_str(self.pipe_segment_2))
        out.append(self._to_str(self.pipe_segment_3))
        out.append(self._to_str(self.pipe_segment_4))
        out.append(self._to_str(self.pipe_segment_5))
        out.append(self._to_str(self.pipe_segment_6))
        return ",".join(out)

class PipingSystemUndergroundPipeSegment(object):
    """ Corresponds to IDD object `PipingSystem:Underground:PipeSegment`
        The pipe segment to be used in an underground piping system
        This object represents a single pipe leg positioned axially
        in the local z-direction, at a given x, y location in the domain
    """
    internal_name = "PipingSystem:Underground:PipeSegment"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PipingSystem:Underground:PipeSegment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["X Position"] = None
        self._data["Y Position"] = None
        self._data["Flow Direction"] = None

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
            self.x_position = None
        else:
            self.x_position = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.y_position = None
        else:
            self.y_position = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.flow_direction = None
        else:
            self.flow_direction = vals[i]
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
    def x_position(self):
        """Get x_position

        Returns:
            float: the value of `x_position` or None if not set
        """
        return self._data["X Position"]

    @x_position.setter
    def x_position(self, value=None):
        """  Corresponds to IDD Field `x_position`
        This segment will be centered at this distance from the x=0
        domain surface or the basement wall surface, based on whether
        a basement exists in this domain and the selection of the
        shift input field found in the domain object.

        Args:
            value (float): value for IDD Field `x_position`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `x_position`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `x_position`')

        self._data["X Position"] = value

    @property
    def y_position(self):
        """Get y_position

        Returns:
            float: the value of `y_position` or None if not set
        """
        return self._data["Y Position"]

    @y_position.setter
    def y_position(self, value=None):
        """  Corresponds to IDD Field `y_position`
        This segment will be centered at this distance away from the
        ground surface; thus this value represents the burial depth
        of this pipe segment.

        Args:
            value (float): value for IDD Field `y_position`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `y_position`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `y_position`')

        self._data["Y Position"] = value

    @property
    def flow_direction(self):
        """Get flow_direction

        Returns:
            str: the value of `flow_direction` or None if not set
        """
        return self._data["Flow Direction"]

    @flow_direction.setter
    def flow_direction(self, value=None):
        """  Corresponds to IDD Field `flow_direction`
        This segment will be simulated such that the flow is in the
        selected direction.  This can allow for detailed analysis
        of circuiting effects in a single domain.

        Args:
            value (str): value for IDD Field `flow_direction`
                Accepted values are:
                      - IncreasingZ
                      - DecreasingZ
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
                                 'for field `flow_direction`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `flow_direction`')
            vals = set()
            vals.add("IncreasingZ")
            vals.add("DecreasingZ")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `flow_direction`'.format(value))

        self._data["Flow Direction"] = value

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
        out.append(self._to_str(self.x_position))
        out.append(self._to_str(self.y_position))
        out.append(self._to_str(self.flow_direction))
        return ",".join(out)