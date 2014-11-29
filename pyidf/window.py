from collections import OrderedDict

class Window(object):
    """ Corresponds to IDD object `Window`
        Allows for simplified entry of Windows.
    """
    internal_name = "Window"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Window`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Building Surface Name"] = None
        self._data["Shading Control Name"] = None
        self._data["Frame and Divider Name"] = None
        self._data["Multiplier"] = None
        self._data["Starting X Coordinate"] = None
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
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
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
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
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
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `building_surface_name`
        Name of Surface (Wall, usually) the Window is on (i.e., Base Surface)
        Window assumes the azimuth and tilt angles of the surface it is on.

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
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_x_coordinate`
        Window starting coordinate is specified relative to the Base Surface origin.

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
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_z_coordinate`
        How far up the wall the Window starts. (in 2-d, this would be a Y Coordinate)

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
        out.append(self._to_str(self.building_surface_name))
        out.append(self._to_str(self.shading_control_name))
        out.append(self._to_str(self.frame_and_divider_name))
        out.append(self._to_str(self.multiplier))
        out.append(self._to_str(self.starting_x_coordinate))
        out.append(self._to_str(self.starting_z_coordinate))
        out.append(self._to_str(self.length))
        out.append(self._to_str(self.height))
        return ",".join(out)

class WindowInterzone(object):
    """ Corresponds to IDD object `Window:Interzone`
        Allows for simplified entry of interzone windows (adjacent to
        other zones).
    """
    internal_name = "Window:Interzone"
    field_count = 9

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Window:Interzone`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Building Surface Name"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Multiplier"] = None
        self._data["Starting X Coordinate"] = None
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
            self.multiplier = None
        else:
            self.multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
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
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `building_surface_name`
        Name of Surface (Wall, usually) the Window is on (i.e., Base Surface)
        Window assumes the azimuth and tilt angles of the surface it is on.

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
        Specify a surface name in an adjacent zone for known interior windows.
        Specify a zone name of an adjacent zone to automatically generate
        the interior window in the adjacent zone.
        a blank field will set up a Window in an adjacent zone
        (same zone as adjacent to base surface)

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
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_x_coordinate`
        Window starting coordinate is specified relative to the Base Surface origin.

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
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `starting_z_coordinate`
        How far up the wall the Window starts. (in 2-d, this would be a Y Coordinate)

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
        out.append(self._to_str(self.building_surface_name))
        out.append(self._to_str(self.outside_boundary_condition_object))
        out.append(self._to_str(self.multiplier))
        out.append(self._to_str(self.starting_x_coordinate))
        out.append(self._to_str(self.starting_z_coordinate))
        out.append(self._to_str(self.length))
        out.append(self._to_str(self.height))
        return ",".join(out)