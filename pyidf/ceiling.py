from collections import OrderedDict

class CeilingAdiabatic(object):
    """ Corresponds to IDD object `Ceiling:Adiabatic`
        Allows for simplified entry of interior ceilings.
    """
    internal_name = "Ceiling:Adiabatic"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Ceiling:Adiabatic`
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
        self._data["Width"] = None

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
            self.width = None
        else:
            self.width = vals[i]
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
        Facing direction of outside of Ceiling

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
    def tilt_angle(self, value=0.0 ):
        """  Corresponds to IDD Field `tilt_angle`
        Ceilings are usually tilted 0 degrees

        Args:
            value (float): value for IDD Field `tilt_angle`
                Unit: deg
                Default value: 0.0
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
        If not Flat, Starting coordinate is the Lower Left Corner of the Ceiling

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
        Along X Axis

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
    def width(self):
        """Get width

        Returns:
            float: the value of `width` or None if not set
        """
        return self._data["Width"]

    @width.setter
    def width(self, value=None):
        """  Corresponds to IDD Field `width`
        Along Y Axis

        Args:
            value (float): value for IDD Field `width`
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
                                 'for field `width`'.format(value))

        self._data["Width"] = value

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
        out.append(self._to_str(self.width))
        return ",".join(out)

class CeilingInterzone(object):
    """ Corresponds to IDD object `Ceiling:Interzone`
        Allows for simplified entry of ceilings using adjacent zone
        (interzone) heat transfer - adjacent surface should be a floor
    """
    internal_name = "Ceiling:Interzone"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Ceiling:Interzone`
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
        self._data["Width"] = None

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
            self.width = None
        else:
            self.width = vals[i]
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
        Specify a surface name in an adjacent zone for known interior floors
        Specify a zone name of an adjacent zone to automatically generate
        the interior floor in the adjacent zone.

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
    def tilt_angle(self, value=0.0 ):
        """  Corresponds to IDD Field `tilt_angle`
        Ceilings are usually tilted 0 degrees

        Args:
            value (float): value for IDD Field `tilt_angle`
                Unit: deg
                Default value: 0.0
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
        If not Flat, should be Lower Left Corner (from outside)

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
        Along X Axis

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
    def width(self):
        """Get width

        Returns:
            float: the value of `width` or None if not set
        """
        return self._data["Width"]

    @width.setter
    def width(self, value=None):
        """  Corresponds to IDD Field `width`
        Along Y Axis

        Args:
            value (float): value for IDD Field `width`
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
                                 'for field `width`'.format(value))

        self._data["Width"] = value

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
        out.append(self._to_str(self.width))
        return ",".join(out)