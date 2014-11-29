from collections import OrderedDict

class WallDetailed(object):
    """ Corresponds to IDD object `Wall:Detailed`
        Allows for detailed entry of wall heat transfer surfaces.
    """
    internal_name = "Wall:Detailed"
    field_count = 39

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Wall:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Outside Boundary Condition"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Sun Exposure"] = None
        self._data["Wind Exposure"] = None
        self._data["View Factor to Ground"] = None
        self._data["Number of Vertices"] = None
        self._data["Vertex 1 X-coordinate"] = None
        self._data["Vertex 1 Y-coordinate"] = None
        self._data["Vertex 1 Z-coordinate"] = None
        self._data["Vertex 2 X-coordinate"] = None
        self._data["Vertex 2 Y-coordinate"] = None
        self._data["Vertex 2 Z-coordinate"] = None
        self._data["Vertex 3 X-coordinate"] = None
        self._data["Vertex 3 Y-coordinate"] = None
        self._data["Vertex 3 Z-coordinate"] = None
        self._data["Vertex 4 X-coordinate"] = None
        self._data["Vertex 4 Y-coordinate"] = None
        self._data["Vertex 4 Z-coordinate"] = None
        self._data["Vertex 5 X-coordinate"] = None
        self._data["Vertex 5 Y-coordinate"] = None
        self._data["Vertex 5 Z-coordinate"] = None
        self._data["Vertex 6 X-coordinate"] = None
        self._data["Vertex 6 Y-coordinate"] = None
        self._data["Vertex 6 Z-coordinate"] = None
        self._data["Vertex 7 X-coordinate"] = None
        self._data["Vertex 7 Y-coordinate"] = None
        self._data["Vertex 7 Z-coordinate"] = None
        self._data["Vertex 8 X-coordinate"] = None
        self._data["Vertex 8 Y-coordinate"] = None
        self._data["Vertex 8 Z-coordinate"] = None
        self._data["Vertex 9 X-coordinate"] = None
        self._data["Vertex 9 Y-coordinate"] = None
        self._data["Vertex 9 Z-coordinate"] = None
        self._data["Vertex 10 X-coordinate"] = None
        self._data["Vertex 10 Y-coordinate"] = None
        self._data["Vertex 10 Z-coordinate"] = None

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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_boundary_condition = None
        else:
            self.outside_boundary_condition = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sun_exposure = None
        else:
            self.sun_exposure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_exposure = None
        else:
            self.wind_exposure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_to_ground = None
        else:
            self.view_factor_to_ground = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_vertices = None
        else:
            self.number_of_vertices = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_1_xcoordinate = None
        else:
            self.vertex_1_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_1_ycoordinate = None
        else:
            self.vertex_1_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_1_zcoordinate = None
        else:
            self.vertex_1_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_2_xcoordinate = None
        else:
            self.vertex_2_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_2_ycoordinate = None
        else:
            self.vertex_2_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_2_zcoordinate = None
        else:
            self.vertex_2_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_3_xcoordinate = None
        else:
            self.vertex_3_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_3_ycoordinate = None
        else:
            self.vertex_3_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_3_zcoordinate = None
        else:
            self.vertex_3_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_4_xcoordinate = None
        else:
            self.vertex_4_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_4_ycoordinate = None
        else:
            self.vertex_4_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_4_zcoordinate = None
        else:
            self.vertex_4_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_5_xcoordinate = None
        else:
            self.vertex_5_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_5_ycoordinate = None
        else:
            self.vertex_5_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_5_zcoordinate = None
        else:
            self.vertex_5_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_6_xcoordinate = None
        else:
            self.vertex_6_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_6_ycoordinate = None
        else:
            self.vertex_6_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_6_zcoordinate = None
        else:
            self.vertex_6_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_7_xcoordinate = None
        else:
            self.vertex_7_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_7_ycoordinate = None
        else:
            self.vertex_7_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_7_zcoordinate = None
        else:
            self.vertex_7_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_8_xcoordinate = None
        else:
            self.vertex_8_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_8_ycoordinate = None
        else:
            self.vertex_8_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_8_zcoordinate = None
        else:
            self.vertex_8_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_9_xcoordinate = None
        else:
            self.vertex_9_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_9_ycoordinate = None
        else:
            self.vertex_9_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_9_zcoordinate = None
        else:
            self.vertex_9_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_10_xcoordinate = None
        else:
            self.vertex_10_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_10_ycoordinate = None
        else:
            self.vertex_10_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_10_zcoordinate = None
        else:
            self.vertex_10_zcoordinate = vals[i]
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
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `construction_name`
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
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `zone_name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def outside_boundary_condition(self):
        """Get outside_boundary_condition

        Returns:
            str: the value of `outside_boundary_condition` or None if not set
        """
        return self._data["Outside Boundary Condition"]

    @outside_boundary_condition.setter
    def outside_boundary_condition(self, value=None):
        """  Corresponds to IDD Field `outside_boundary_condition`

        Args:
            value (str): value for IDD Field `outside_boundary_condition`
                Accepted values are:
                      - Adiabatic
                      - Surface
                      - Zone
                      - Outdoors
                      - Ground
                      - GroundFCfactorMethod
                      - OtherSideCoefficients
                      - OtherSideConditionsModel
                      - GroundSlabPreprocessorAverage
                      - GroundSlabPreprocessorCore
                      - GroundSlabPreprocessorPerimeter
                      - GroundBasementPreprocessorAverageWall
                      - GroundBasementPreprocessorAverageFloor
                      - GroundBasementPreprocessorUpperWall
                      - GroundBasementPreprocessorLowerWall
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
                                 'for field `outside_boundary_condition`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_boundary_condition`')
            vals = set()
            vals.add("Adiabatic")
            vals.add("Surface")
            vals.add("Zone")
            vals.add("Outdoors")
            vals.add("Ground")
            vals.add("GroundFCfactorMethod")
            vals.add("OtherSideCoefficients")
            vals.add("OtherSideConditionsModel")
            vals.add("GroundSlabPreprocessorAverage")
            vals.add("GroundSlabPreprocessorCore")
            vals.add("GroundSlabPreprocessorPerimeter")
            vals.add("GroundBasementPreprocessorAverageWall")
            vals.add("GroundBasementPreprocessorAverageFloor")
            vals.add("GroundBasementPreprocessorUpperWall")
            vals.add("GroundBasementPreprocessorLowerWall")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outside_boundary_condition`'.format(value))

        self._data["Outside Boundary Condition"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `outside_boundary_condition_object`
        Non-blank only if the field Outside Boundary Condition is Surface,
        Zone, OtherSideCoefficients or OtherSideConditionsModel
        If Surface, specify name of corresponding surface in adjacent zone or
        specify current surface name for internal partition separating like zones
        If Zone, specify the name of the corresponding zone and
        the program will generate the corresponding interzone surface
        If OtherSideCoefficients, specify name of SurfaceProperty:OtherSideCoefficients
        If OtherSideConditionsModel, specify name of SurfaceProperty:OtherSideConditionsModel

        Args:
            value (str): value for IDD Field `outside_boundary_condition_object`
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
                                 'for field `outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_boundary_condition_object`')

        self._data["Outside Boundary Condition Object"] = value

    @property
    def sun_exposure(self):
        """Get sun_exposure

        Returns:
            str: the value of `sun_exposure` or None if not set
        """
        return self._data["Sun Exposure"]

    @sun_exposure.setter
    def sun_exposure(self, value="SunExposed"):
        """  Corresponds to IDD Field `sun_exposure`

        Args:
            value (str): value for IDD Field `sun_exposure`
                Accepted values are:
                      - SunExposed
                      - NoSun
                Default value: SunExposed
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
                                 'for field `sun_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sun_exposure`')
            vals = set()
            vals.add("SunExposed")
            vals.add("NoSun")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `sun_exposure`'.format(value))

        self._data["Sun Exposure"] = value

    @property
    def wind_exposure(self):
        """Get wind_exposure

        Returns:
            str: the value of `wind_exposure` or None if not set
        """
        return self._data["Wind Exposure"]

    @wind_exposure.setter
    def wind_exposure(self, value="WindExposed"):
        """  Corresponds to IDD Field `wind_exposure`

        Args:
            value (str): value for IDD Field `wind_exposure`
                Accepted values are:
                      - WindExposed
                      - NoWind
                Default value: WindExposed
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
                                 'for field `wind_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_exposure`')
            vals = set()
            vals.add("WindExposed")
            vals.add("NoWind")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_exposure`'.format(value))

        self._data["Wind Exposure"] = value

    @property
    def view_factor_to_ground(self):
        """Get view_factor_to_ground

        Returns:
            float: the value of `view_factor_to_ground` or None if not set
        """
        return self._data["View Factor to Ground"]

    @view_factor_to_ground.setter
    def view_factor_to_ground(self, value=None):
        """  Corresponds to IDD Field `view_factor_to_ground`
        From the exterior of the surface
        Unused if one uses the "reflections" options in Solar Distribution in Building input
        unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been specified.
        autocalculate will automatically calculate this value from the tilt of the surface

        Args:
            value (float): value for IDD Field `view_factor_to_ground`
                value >= 0.0
                value <= 1.0
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
                                 'for field `view_factor_to_ground`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `view_factor_to_ground`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_to_ground`')

        self._data["View Factor to Ground"] = value

    @property
    def number_of_vertices(self):
        """Get number_of_vertices

        Returns:
            float: the value of `number_of_vertices` or None if not set
        """
        return self._data["Number of Vertices"]

    @number_of_vertices.setter
    def number_of_vertices(self, value=None):
        """  Corresponds to IDD Field `number_of_vertices`
        shown with 10 vertex coordinates -- extensible object
        "extensible" -- duplicate last set of x,y,z coordinates, renumbering please
        (and changing z terminator to a comma "," for all but last one which needs a semi-colon ";")
        vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates
        are "relative" to the Zone Origin.  If world, then building and zone origins are used
        for some internal calculations, but all coordinates are given in an "absolute" system.

        Args:
            value (float): value for IDD Field `number_of_vertices`
                value >= 3.0
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
                                 'for field `number_of_vertices`'.format(value))
            if value < 3.0:
                raise ValueError('value need to be greater or equal 3.0 '
                                 'for field `number_of_vertices`')

        self._data["Number of Vertices"] = value

    @property
    def vertex_1_xcoordinate(self):
        """Get vertex_1_xcoordinate

        Returns:
            float: the value of `vertex_1_xcoordinate` or None if not set
        """
        return self._data["Vertex 1 X-coordinate"]

    @vertex_1_xcoordinate.setter
    def vertex_1_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_1_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_1_xcoordinate`
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
                                 'for field `vertex_1_xcoordinate`'.format(value))

        self._data["Vertex 1 X-coordinate"] = value

    @property
    def vertex_1_ycoordinate(self):
        """Get vertex_1_ycoordinate

        Returns:
            float: the value of `vertex_1_ycoordinate` or None if not set
        """
        return self._data["Vertex 1 Y-coordinate"]

    @vertex_1_ycoordinate.setter
    def vertex_1_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_1_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_1_ycoordinate`
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
                                 'for field `vertex_1_ycoordinate`'.format(value))

        self._data["Vertex 1 Y-coordinate"] = value

    @property
    def vertex_1_zcoordinate(self):
        """Get vertex_1_zcoordinate

        Returns:
            float: the value of `vertex_1_zcoordinate` or None if not set
        """
        return self._data["Vertex 1 Z-coordinate"]

    @vertex_1_zcoordinate.setter
    def vertex_1_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_1_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_1_zcoordinate`
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
                                 'for field `vertex_1_zcoordinate`'.format(value))

        self._data["Vertex 1 Z-coordinate"] = value

    @property
    def vertex_2_xcoordinate(self):
        """Get vertex_2_xcoordinate

        Returns:
            float: the value of `vertex_2_xcoordinate` or None if not set
        """
        return self._data["Vertex 2 X-coordinate"]

    @vertex_2_xcoordinate.setter
    def vertex_2_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_2_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_2_xcoordinate`
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
                                 'for field `vertex_2_xcoordinate`'.format(value))

        self._data["Vertex 2 X-coordinate"] = value

    @property
    def vertex_2_ycoordinate(self):
        """Get vertex_2_ycoordinate

        Returns:
            float: the value of `vertex_2_ycoordinate` or None if not set
        """
        return self._data["Vertex 2 Y-coordinate"]

    @vertex_2_ycoordinate.setter
    def vertex_2_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_2_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_2_ycoordinate`
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
                                 'for field `vertex_2_ycoordinate`'.format(value))

        self._data["Vertex 2 Y-coordinate"] = value

    @property
    def vertex_2_zcoordinate(self):
        """Get vertex_2_zcoordinate

        Returns:
            float: the value of `vertex_2_zcoordinate` or None if not set
        """
        return self._data["Vertex 2 Z-coordinate"]

    @vertex_2_zcoordinate.setter
    def vertex_2_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_2_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_2_zcoordinate`
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
                                 'for field `vertex_2_zcoordinate`'.format(value))

        self._data["Vertex 2 Z-coordinate"] = value

    @property
    def vertex_3_xcoordinate(self):
        """Get vertex_3_xcoordinate

        Returns:
            float: the value of `vertex_3_xcoordinate` or None if not set
        """
        return self._data["Vertex 3 X-coordinate"]

    @vertex_3_xcoordinate.setter
    def vertex_3_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_3_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_3_xcoordinate`
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
                                 'for field `vertex_3_xcoordinate`'.format(value))

        self._data["Vertex 3 X-coordinate"] = value

    @property
    def vertex_3_ycoordinate(self):
        """Get vertex_3_ycoordinate

        Returns:
            float: the value of `vertex_3_ycoordinate` or None if not set
        """
        return self._data["Vertex 3 Y-coordinate"]

    @vertex_3_ycoordinate.setter
    def vertex_3_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_3_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_3_ycoordinate`
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
                                 'for field `vertex_3_ycoordinate`'.format(value))

        self._data["Vertex 3 Y-coordinate"] = value

    @property
    def vertex_3_zcoordinate(self):
        """Get vertex_3_zcoordinate

        Returns:
            float: the value of `vertex_3_zcoordinate` or None if not set
        """
        return self._data["Vertex 3 Z-coordinate"]

    @vertex_3_zcoordinate.setter
    def vertex_3_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_3_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_3_zcoordinate`
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
                                 'for field `vertex_3_zcoordinate`'.format(value))

        self._data["Vertex 3 Z-coordinate"] = value

    @property
    def vertex_4_xcoordinate(self):
        """Get vertex_4_xcoordinate

        Returns:
            float: the value of `vertex_4_xcoordinate` or None if not set
        """
        return self._data["Vertex 4 X-coordinate"]

    @vertex_4_xcoordinate.setter
    def vertex_4_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_4_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_4_xcoordinate`
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
                                 'for field `vertex_4_xcoordinate`'.format(value))

        self._data["Vertex 4 X-coordinate"] = value

    @property
    def vertex_4_ycoordinate(self):
        """Get vertex_4_ycoordinate

        Returns:
            float: the value of `vertex_4_ycoordinate` or None if not set
        """
        return self._data["Vertex 4 Y-coordinate"]

    @vertex_4_ycoordinate.setter
    def vertex_4_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_4_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_4_ycoordinate`
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
                                 'for field `vertex_4_ycoordinate`'.format(value))

        self._data["Vertex 4 Y-coordinate"] = value

    @property
    def vertex_4_zcoordinate(self):
        """Get vertex_4_zcoordinate

        Returns:
            float: the value of `vertex_4_zcoordinate` or None if not set
        """
        return self._data["Vertex 4 Z-coordinate"]

    @vertex_4_zcoordinate.setter
    def vertex_4_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_4_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_4_zcoordinate`
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
                                 'for field `vertex_4_zcoordinate`'.format(value))

        self._data["Vertex 4 Z-coordinate"] = value

    @property
    def vertex_5_xcoordinate(self):
        """Get vertex_5_xcoordinate

        Returns:
            float: the value of `vertex_5_xcoordinate` or None if not set
        """
        return self._data["Vertex 5 X-coordinate"]

    @vertex_5_xcoordinate.setter
    def vertex_5_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_5_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_5_xcoordinate`
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
                                 'for field `vertex_5_xcoordinate`'.format(value))

        self._data["Vertex 5 X-coordinate"] = value

    @property
    def vertex_5_ycoordinate(self):
        """Get vertex_5_ycoordinate

        Returns:
            float: the value of `vertex_5_ycoordinate` or None if not set
        """
        return self._data["Vertex 5 Y-coordinate"]

    @vertex_5_ycoordinate.setter
    def vertex_5_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_5_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_5_ycoordinate`
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
                                 'for field `vertex_5_ycoordinate`'.format(value))

        self._data["Vertex 5 Y-coordinate"] = value

    @property
    def vertex_5_zcoordinate(self):
        """Get vertex_5_zcoordinate

        Returns:
            float: the value of `vertex_5_zcoordinate` or None if not set
        """
        return self._data["Vertex 5 Z-coordinate"]

    @vertex_5_zcoordinate.setter
    def vertex_5_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_5_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_5_zcoordinate`
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
                                 'for field `vertex_5_zcoordinate`'.format(value))

        self._data["Vertex 5 Z-coordinate"] = value

    @property
    def vertex_6_xcoordinate(self):
        """Get vertex_6_xcoordinate

        Returns:
            float: the value of `vertex_6_xcoordinate` or None if not set
        """
        return self._data["Vertex 6 X-coordinate"]

    @vertex_6_xcoordinate.setter
    def vertex_6_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_6_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_6_xcoordinate`
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
                                 'for field `vertex_6_xcoordinate`'.format(value))

        self._data["Vertex 6 X-coordinate"] = value

    @property
    def vertex_6_ycoordinate(self):
        """Get vertex_6_ycoordinate

        Returns:
            float: the value of `vertex_6_ycoordinate` or None if not set
        """
        return self._data["Vertex 6 Y-coordinate"]

    @vertex_6_ycoordinate.setter
    def vertex_6_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_6_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_6_ycoordinate`
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
                                 'for field `vertex_6_ycoordinate`'.format(value))

        self._data["Vertex 6 Y-coordinate"] = value

    @property
    def vertex_6_zcoordinate(self):
        """Get vertex_6_zcoordinate

        Returns:
            float: the value of `vertex_6_zcoordinate` or None if not set
        """
        return self._data["Vertex 6 Z-coordinate"]

    @vertex_6_zcoordinate.setter
    def vertex_6_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_6_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_6_zcoordinate`
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
                                 'for field `vertex_6_zcoordinate`'.format(value))

        self._data["Vertex 6 Z-coordinate"] = value

    @property
    def vertex_7_xcoordinate(self):
        """Get vertex_7_xcoordinate

        Returns:
            float: the value of `vertex_7_xcoordinate` or None if not set
        """
        return self._data["Vertex 7 X-coordinate"]

    @vertex_7_xcoordinate.setter
    def vertex_7_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_7_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_7_xcoordinate`
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
                                 'for field `vertex_7_xcoordinate`'.format(value))

        self._data["Vertex 7 X-coordinate"] = value

    @property
    def vertex_7_ycoordinate(self):
        """Get vertex_7_ycoordinate

        Returns:
            float: the value of `vertex_7_ycoordinate` or None if not set
        """
        return self._data["Vertex 7 Y-coordinate"]

    @vertex_7_ycoordinate.setter
    def vertex_7_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_7_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_7_ycoordinate`
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
                                 'for field `vertex_7_ycoordinate`'.format(value))

        self._data["Vertex 7 Y-coordinate"] = value

    @property
    def vertex_7_zcoordinate(self):
        """Get vertex_7_zcoordinate

        Returns:
            float: the value of `vertex_7_zcoordinate` or None if not set
        """
        return self._data["Vertex 7 Z-coordinate"]

    @vertex_7_zcoordinate.setter
    def vertex_7_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_7_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_7_zcoordinate`
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
                                 'for field `vertex_7_zcoordinate`'.format(value))

        self._data["Vertex 7 Z-coordinate"] = value

    @property
    def vertex_8_xcoordinate(self):
        """Get vertex_8_xcoordinate

        Returns:
            float: the value of `vertex_8_xcoordinate` or None if not set
        """
        return self._data["Vertex 8 X-coordinate"]

    @vertex_8_xcoordinate.setter
    def vertex_8_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_8_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_8_xcoordinate`
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
                                 'for field `vertex_8_xcoordinate`'.format(value))

        self._data["Vertex 8 X-coordinate"] = value

    @property
    def vertex_8_ycoordinate(self):
        """Get vertex_8_ycoordinate

        Returns:
            float: the value of `vertex_8_ycoordinate` or None if not set
        """
        return self._data["Vertex 8 Y-coordinate"]

    @vertex_8_ycoordinate.setter
    def vertex_8_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_8_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_8_ycoordinate`
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
                                 'for field `vertex_8_ycoordinate`'.format(value))

        self._data["Vertex 8 Y-coordinate"] = value

    @property
    def vertex_8_zcoordinate(self):
        """Get vertex_8_zcoordinate

        Returns:
            float: the value of `vertex_8_zcoordinate` or None if not set
        """
        return self._data["Vertex 8 Z-coordinate"]

    @vertex_8_zcoordinate.setter
    def vertex_8_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_8_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_8_zcoordinate`
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
                                 'for field `vertex_8_zcoordinate`'.format(value))

        self._data["Vertex 8 Z-coordinate"] = value

    @property
    def vertex_9_xcoordinate(self):
        """Get vertex_9_xcoordinate

        Returns:
            float: the value of `vertex_9_xcoordinate` or None if not set
        """
        return self._data["Vertex 9 X-coordinate"]

    @vertex_9_xcoordinate.setter
    def vertex_9_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_9_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_9_xcoordinate`
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
                                 'for field `vertex_9_xcoordinate`'.format(value))

        self._data["Vertex 9 X-coordinate"] = value

    @property
    def vertex_9_ycoordinate(self):
        """Get vertex_9_ycoordinate

        Returns:
            float: the value of `vertex_9_ycoordinate` or None if not set
        """
        return self._data["Vertex 9 Y-coordinate"]

    @vertex_9_ycoordinate.setter
    def vertex_9_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_9_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_9_ycoordinate`
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
                                 'for field `vertex_9_ycoordinate`'.format(value))

        self._data["Vertex 9 Y-coordinate"] = value

    @property
    def vertex_9_zcoordinate(self):
        """Get vertex_9_zcoordinate

        Returns:
            float: the value of `vertex_9_zcoordinate` or None if not set
        """
        return self._data["Vertex 9 Z-coordinate"]

    @vertex_9_zcoordinate.setter
    def vertex_9_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_9_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_9_zcoordinate`
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
                                 'for field `vertex_9_zcoordinate`'.format(value))

        self._data["Vertex 9 Z-coordinate"] = value

    @property
    def vertex_10_xcoordinate(self):
        """Get vertex_10_xcoordinate

        Returns:
            float: the value of `vertex_10_xcoordinate` or None if not set
        """
        return self._data["Vertex 10 X-coordinate"]

    @vertex_10_xcoordinate.setter
    def vertex_10_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_10_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_10_xcoordinate`
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
                                 'for field `vertex_10_xcoordinate`'.format(value))

        self._data["Vertex 10 X-coordinate"] = value

    @property
    def vertex_10_ycoordinate(self):
        """Get vertex_10_ycoordinate

        Returns:
            float: the value of `vertex_10_ycoordinate` or None if not set
        """
        return self._data["Vertex 10 Y-coordinate"]

    @vertex_10_ycoordinate.setter
    def vertex_10_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_10_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_10_ycoordinate`
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
                                 'for field `vertex_10_ycoordinate`'.format(value))

        self._data["Vertex 10 Y-coordinate"] = value

    @property
    def vertex_10_zcoordinate(self):
        """Get vertex_10_zcoordinate

        Returns:
            float: the value of `vertex_10_zcoordinate` or None if not set
        """
        return self._data["Vertex 10 Z-coordinate"]

    @vertex_10_zcoordinate.setter
    def vertex_10_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_10_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_10_zcoordinate`
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
                                 'for field `vertex_10_zcoordinate`'.format(value))

        self._data["Vertex 10 Z-coordinate"] = value

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
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.outside_boundary_condition))
        out.append(self._to_str(self.outside_boundary_condition_object))
        out.append(self._to_str(self.sun_exposure))
        out.append(self._to_str(self.wind_exposure))
        out.append(self._to_str(self.view_factor_to_ground))
        out.append(self._to_str(self.number_of_vertices))
        out.append(self._to_str(self.vertex_1_xcoordinate))
        out.append(self._to_str(self.vertex_1_ycoordinate))
        out.append(self._to_str(self.vertex_1_zcoordinate))
        out.append(self._to_str(self.vertex_2_xcoordinate))
        out.append(self._to_str(self.vertex_2_ycoordinate))
        out.append(self._to_str(self.vertex_2_zcoordinate))
        out.append(self._to_str(self.vertex_3_xcoordinate))
        out.append(self._to_str(self.vertex_3_ycoordinate))
        out.append(self._to_str(self.vertex_3_zcoordinate))
        out.append(self._to_str(self.vertex_4_xcoordinate))
        out.append(self._to_str(self.vertex_4_ycoordinate))
        out.append(self._to_str(self.vertex_4_zcoordinate))
        out.append(self._to_str(self.vertex_5_xcoordinate))
        out.append(self._to_str(self.vertex_5_ycoordinate))
        out.append(self._to_str(self.vertex_5_zcoordinate))
        out.append(self._to_str(self.vertex_6_xcoordinate))
        out.append(self._to_str(self.vertex_6_ycoordinate))
        out.append(self._to_str(self.vertex_6_zcoordinate))
        out.append(self._to_str(self.vertex_7_xcoordinate))
        out.append(self._to_str(self.vertex_7_ycoordinate))
        out.append(self._to_str(self.vertex_7_zcoordinate))
        out.append(self._to_str(self.vertex_8_xcoordinate))
        out.append(self._to_str(self.vertex_8_ycoordinate))
        out.append(self._to_str(self.vertex_8_zcoordinate))
        out.append(self._to_str(self.vertex_9_xcoordinate))
        out.append(self._to_str(self.vertex_9_ycoordinate))
        out.append(self._to_str(self.vertex_9_zcoordinate))
        out.append(self._to_str(self.vertex_10_xcoordinate))
        out.append(self._to_str(self.vertex_10_ycoordinate))
        out.append(self._to_str(self.vertex_10_zcoordinate))
        return ",".join(out)

class WallExterior(object):
    """ Corresponds to IDD object `Wall:Exterior`
        Allows for simplified entry of exterior walls.
        View Factor to Ground is automatically calculated.
    """
    internal_name = "Wall:Exterior"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Wall:Exterior`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None

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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `construction_name`
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
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `zone_name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `azimuth_angle`
        Facing direction of outside of wall (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `azimuth_angle`
                Unit: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `azimuth_angle`')

        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=90.0 ):
        """  Corresponds to IDD Field `tilt_angle`
        Walls are usually tilted 90 degrees

        Args:
            value (float): value for IDD Field `tilt_angle`
                Unit: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 'for field `tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `tilt_angle`')

        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_x_coordinate`
        Starting (x,y,z) coordinate is the Lower Left Corner of the Wall

        Args:
            value (float): value for IDD Field `starting_x_coordinate`
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
                                 'for field `starting_x_coordinate`'.format(value))

        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_y_coordinate`

        Args:
            value (float): value for IDD Field `starting_y_coordinate`
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
                                 'for field `starting_y_coordinate`'.format(value))

        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_z_coordinate`

        Args:
            value (float): value for IDD Field `starting_z_coordinate`
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
                                 'for field `starting_z_coordinate`'.format(value))

        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `length`

        Args:
            value (float): value for IDD Field `length`
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
                                 'for field `length`'.format(value))

        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `height`

        Args:
            value (float): value for IDD Field `height`
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
                                 'for field `height`'.format(value))

        self._data["Height"] = value

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
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.azimuth_angle))
        out.append(self._to_str(self.tilt_angle))
        out.append(self._to_str(self.starting_x_coordinate))
        out.append(self._to_str(self.starting_y_coordinate))
        out.append(self._to_str(self.starting_z_coordinate))
        out.append(self._to_str(self.length))
        out.append(self._to_str(self.height))
        return ",".join(out)

class WallAdiabatic(object):
    """ Corresponds to IDD object `Wall:Adiabatic`
        Allows for simplified entry of interior walls.
    """
    internal_name = "Wall:Adiabatic"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Wall:Adiabatic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None

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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `construction_name`
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
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `zone_name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `azimuth_angle`
        Facing direction of outside of wall (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `azimuth_angle`
                Unit: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `azimuth_angle`')

        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=90.0 ):
        """  Corresponds to IDD Field `tilt_angle`
        Walls are usually tilted 90 degrees

        Args:
            value (float): value for IDD Field `tilt_angle`
                Unit: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 'for field `tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `tilt_angle`')

        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_x_coordinate`
        Starting (x,y,z) coordinate is the Lower Left Corner of the Wall

        Args:
            value (float): value for IDD Field `starting_x_coordinate`
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
                                 'for field `starting_x_coordinate`'.format(value))

        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_y_coordinate`

        Args:
            value (float): value for IDD Field `starting_y_coordinate`
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
                                 'for field `starting_y_coordinate`'.format(value))

        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_z_coordinate`

        Args:
            value (float): value for IDD Field `starting_z_coordinate`
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
                                 'for field `starting_z_coordinate`'.format(value))

        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `length`

        Args:
            value (float): value for IDD Field `length`
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
                                 'for field `length`'.format(value))

        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `height`

        Args:
            value (float): value for IDD Field `height`
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
                                 'for field `height`'.format(value))

        self._data["Height"] = value

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
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.azimuth_angle))
        out.append(self._to_str(self.tilt_angle))
        out.append(self._to_str(self.starting_x_coordinate))
        out.append(self._to_str(self.starting_y_coordinate))
        out.append(self._to_str(self.starting_z_coordinate))
        out.append(self._to_str(self.length))
        out.append(self._to_str(self.height))
        return ",".join(out)

class WallUnderground(object):
    """ Corresponds to IDD object `Wall:Underground`
        Allows for simplified entry of underground walls.
    """
    internal_name = "Wall:Underground"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Wall:Underground`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None

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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`
        To be matched with a construction in this input file.
        If the construction is type "Construction:CfactorUndergroundWall",
        then the GroundFCfactorMethod will be used.

        Args:
            value (str): value for IDD Field `construction_name`
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
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `zone_name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `azimuth_angle`
        Facing direction of outside of wall (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `azimuth_angle`
                Unit: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `azimuth_angle`')

        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=90.0 ):
        """  Corresponds to IDD Field `tilt_angle`
        Walls are usually tilted 90 degrees

        Args:
            value (float): value for IDD Field `tilt_angle`
                Unit: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 'for field `tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `tilt_angle`')

        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_x_coordinate`
        Starting (x,y,z) coordinate is the Lower Left Corner of the Wall

        Args:
            value (float): value for IDD Field `starting_x_coordinate`
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
                                 'for field `starting_x_coordinate`'.format(value))

        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_y_coordinate`

        Args:
            value (float): value for IDD Field `starting_y_coordinate`
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
                                 'for field `starting_y_coordinate`'.format(value))

        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_z_coordinate`

        Args:
            value (float): value for IDD Field `starting_z_coordinate`
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
                                 'for field `starting_z_coordinate`'.format(value))

        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `length`

        Args:
            value (float): value for IDD Field `length`
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
                                 'for field `length`'.format(value))

        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `height`

        Args:
            value (float): value for IDD Field `height`
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
                                 'for field `height`'.format(value))

        self._data["Height"] = value

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
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.azimuth_angle))
        out.append(self._to_str(self.tilt_angle))
        out.append(self._to_str(self.starting_x_coordinate))
        out.append(self._to_str(self.starting_y_coordinate))
        out.append(self._to_str(self.starting_z_coordinate))
        out.append(self._to_str(self.length))
        out.append(self._to_str(self.height))
        return ",".join(out)

class WallInterzone(object):
    """ Corresponds to IDD object `Wall:Interzone`
        Allows for simplified entry of interzone walls (walls between zones).
    """
    internal_name = "Wall:Interzone"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Wall:Interzone`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None

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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `construction_name`
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
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Zone for the inside of the surface

        Args:
            value (str): value for IDD Field `zone_name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `outside_boundary_condition_object`
        Specify a surface name in an adjacent zone for known interior walls.
        Specify a zone name of an adjacent zone to automatically generate
        the interior wall in the adjacent zone.

        Args:
            value (str): value for IDD Field `outside_boundary_condition_object`
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
                                 'for field `outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_boundary_condition_object`')

        self._data["Outside Boundary Condition Object"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `azimuth_angle`
        Facing direction of outside of wall (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `azimuth_angle`
                Unit: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `azimuth_angle`')

        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=90.0 ):
        """  Corresponds to IDD Field `tilt_angle`
        Walls are usually tilted 90 degrees

        Args:
            value (float): value for IDD Field `tilt_angle`
                Unit: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 'for field `tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `tilt_angle`')

        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_x_coordinate`
        Starting (x,y,z) coordinate is the Lower Left Corner of the Wall

        Args:
            value (float): value for IDD Field `starting_x_coordinate`
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
                                 'for field `starting_x_coordinate`'.format(value))

        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_y_coordinate`

        Args:
            value (float): value for IDD Field `starting_y_coordinate`
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
                                 'for field `starting_y_coordinate`'.format(value))

        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_z_coordinate`

        Args:
            value (float): value for IDD Field `starting_z_coordinate`
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
                                 'for field `starting_z_coordinate`'.format(value))

        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `length`

        Args:
            value (float): value for IDD Field `length`
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
                                 'for field `length`'.format(value))

        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `height`

        Args:
            value (float): value for IDD Field `height`
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
                                 'for field `height`'.format(value))

        self._data["Height"] = value

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
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.outside_boundary_condition_object))
        out.append(self._to_str(self.azimuth_angle))
        out.append(self._to_str(self.tilt_angle))
        out.append(self._to_str(self.starting_x_coordinate))
        out.append(self._to_str(self.starting_y_coordinate))
        out.append(self._to_str(self.starting_z_coordinate))
        out.append(self._to_str(self.length))
        out.append(self._to_str(self.height))
        return ",".join(out)