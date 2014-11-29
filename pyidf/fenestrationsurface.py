from collections import OrderedDict

class FenestrationSurfaceDetailed(object):
    """ Corresponds to IDD object `FenestrationSurface:Detailed`
        Allows for detailed entry of subsurfaces
        (windows, doors, glass doors, tubular daylighting devices).
    """
    internal_name = "FenestrationSurface:Detailed"
    field_count = 22

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `FenestrationSurface:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Type"] = None
        self._data["Construction Name"] = None
        self._data["Building Surface Name"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["View Factor to Ground"] = None
        self._data["Shading Control Name"] = None
        self._data["Frame and Divider Name"] = None
        self._data["Multiplier"] = None
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
            self.surface_type = None
        else:
            self.surface_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_to_ground = None
        else:
            self.view_factor_to_ground = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shading_control_name = None
        else:
            self.shading_control_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.frame_and_divider_name = None
        else:
            self.frame_and_divider_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.multiplier = None
        else:
            self.multiplier = vals[i]
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
    def surface_type(self):
        """Get surface_type

        Returns:
            str: the value of `surface_type` or None if not set
        """
        return self._data["Surface Type"]

    @surface_type.setter
    def surface_type(self, value=None):
        """  Corresponds to IDD Field `surface_type`

        Args:
            value (str): value for IDD Field `surface_type`
                Accepted values are:
                      - Window
                      - Door
                      - GlassDoor
                      - TubularDaylightDome
                      - TubularDaylightDiffuser
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
                                 'for field `surface_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_type`')
            vals = set()
            vals.add("Window")
            vals.add("Door")
            vals.add("GlassDoor")
            vals.add("TubularDaylightDome")
            vals.add("TubularDaylightDiffuser")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `surface_type`'.format(value))

        self._data["Surface Type"] = value

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
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `building_surface_name`

        Args:
            value (str): value for IDD Field `building_surface_name`
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
                                 'for field `building_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `building_surface_name`')

        self._data["Building Surface Name"] = value

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
        Non-blank only if base surface field Outside Boundary Condition is
        Surface or OtherSideCoefficients
        If Base Surface's Surface, specify name of corresponding subsurface in adjacent zone or
        specify current subsurface name for internal partition separating like zones
        If OtherSideCoefficients, specify name of SurfaceProperty:OtherSideCoefficients
        or leave blank to inherit Base Surface's OtherSide Coefficients

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
    def shading_control_name(self):
        """Get shading_control_name

        Returns:
            str: the value of `shading_control_name` or None if not set
        """
        return self._data["Shading Control Name"]

    @shading_control_name.setter
    def shading_control_name(self, value=None):
        """  Corresponds to IDD Field `shading_control_name`
        enter the name of a WindowProperty:ShadingControl object
        used for windows and glass doors only
        If not specified, window or glass door has no shading (blind, roller shade, etc.)

        Args:
            value (str): value for IDD Field `shading_control_name`
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
                                 'for field `shading_control_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `shading_control_name`')

        self._data["Shading Control Name"] = value

    @property
    def frame_and_divider_name(self):
        """Get frame_and_divider_name

        Returns:
            str: the value of `frame_and_divider_name` or None if not set
        """
        return self._data["Frame and Divider Name"]

    @frame_and_divider_name.setter
    def frame_and_divider_name(self, value=None):
        """  Corresponds to IDD Field `frame_and_divider_name`
        Enter the name of a WindowProperty:FrameAndDivider object
        Used only for exterior windows (rectangular) and glass doors.
        Unused for triangular windows.
        If not specified (blank), window or glass door has no frame or divider
        and no beam solar reflection from reveal surfaces.

        Args:
            value (str): value for IDD Field `frame_and_divider_name`
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
                                 'for field `frame_and_divider_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `frame_and_divider_name`')

        self._data["Frame and Divider Name"] = value

    @property
    def multiplier(self):
        """Get multiplier

        Returns:
            float: the value of `multiplier` or None if not set
        """
        return self._data["Multiplier"]

    @multiplier.setter
    def multiplier(self, value=1.0 ):
        """  Corresponds to IDD Field `multiplier`
        Used only for Surface Type = WINDOW, GLASSDOOR or DOOR
        Non-integer values will be truncated to integer

        Args:
            value (float): value for IDD Field `multiplier`
                Default value: 1.0
                value >= 1.0
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
                                 'for field `multiplier`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `multiplier`')

        self._data["Multiplier"] = value

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
        vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates
        are "relative" to the Zone Origin.  If world, then building and zone origins are used
        for some internal calculations, but all coordinates are given in an "absolute" system.

        Args:
            value (float): value for IDD Field `number_of_vertices`
                value >= 3.0
                value <= 4.0
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
            if value > 4.0:
                raise ValueError('value need to be smaller 4.0 '
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
        Not used for triangles

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
        Not used for triangles

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
        Not used for triangles

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
        out.append(self._to_str(self.surface_type))
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.building_surface_name))
        out.append(self._to_str(self.outside_boundary_condition_object))
        out.append(self._to_str(self.view_factor_to_ground))
        out.append(self._to_str(self.shading_control_name))
        out.append(self._to_str(self.frame_and_divider_name))
        out.append(self._to_str(self.multiplier))
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
        return ",".join(out)