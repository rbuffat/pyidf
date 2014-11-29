from collections import OrderedDict

class Zone(object):
    """ Corresponds to IDD object `Zone`
        Defines a thermal zone of the building.
    """
    internal_name = "Zone"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Zone`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Direction of Relative North"] = None
        self._data["X Origin"] = None
        self._data["Y Origin"] = None
        self._data["Z Origin"] = None
        self._data["Type"] = None
        self._data["Multiplier"] = None
        self._data["Ceiling Height"] = None
        self._data["Volume"] = None
        self._data["Floor Area"] = None
        self._data["Zone Inside Convection Algorithm"] = None
        self._data["Zone Outside Convection Algorithm"] = None
        self._data["Part of Total Floor Area"] = None

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
            self.direction_of_relative_north = None
        else:
            self.direction_of_relative_north = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_origin = None
        else:
            self.x_origin = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.y_origin = None
        else:
            self.y_origin = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.z_origin = None
        else:
            self.z_origin = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.type = None
        else:
            self.type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.multiplier = None
        else:
            self.multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ceiling_height = None
        else:
            self.ceiling_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.volume = None
        else:
            self.volume = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_area = None
        else:
            self.floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_inside_convection_algorithm = None
        else:
            self.zone_inside_convection_algorithm = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_outside_convection_algorithm = None
        else:
            self.zone_outside_convection_algorithm = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.part_of_total_floor_area = None
        else:
            self.part_of_total_floor_area = vals[i]
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
    def direction_of_relative_north(self):
        """Get direction_of_relative_north

        Returns:
            float: the value of `direction_of_relative_north` or None if not set
        """
        return self._data["Direction of Relative North"]

    @direction_of_relative_north.setter
    def direction_of_relative_north(self, value=0.0 ):
        """  Corresponds to IDD Field `direction_of_relative_north`

        Args:
            value (float): value for IDD Field `direction_of_relative_north`
                Unit: deg
                Default value: 0.0
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
                                 'for field `direction_of_relative_north`'.format(value))

        self._data["Direction of Relative North"] = value

    @property
    def x_origin(self):
        """Get x_origin

        Returns:
            float: the value of `x_origin` or None if not set
        """
        return self._data["X Origin"]

    @x_origin.setter
    def x_origin(self, value=0.0 ):
        """  Corresponds to IDD Field `x_origin`

        Args:
            value (float): value for IDD Field `x_origin`
                Unit: m
                Default value: 0.0
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
                                 'for field `x_origin`'.format(value))

        self._data["X Origin"] = value

    @property
    def y_origin(self):
        """Get y_origin

        Returns:
            float: the value of `y_origin` or None if not set
        """
        return self._data["Y Origin"]

    @y_origin.setter
    def y_origin(self, value=0.0 ):
        """  Corresponds to IDD Field `y_origin`

        Args:
            value (float): value for IDD Field `y_origin`
                Unit: m
                Default value: 0.0
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
                                 'for field `y_origin`'.format(value))

        self._data["Y Origin"] = value

    @property
    def z_origin(self):
        """Get z_origin

        Returns:
            float: the value of `z_origin` or None if not set
        """
        return self._data["Z Origin"]

    @z_origin.setter
    def z_origin(self, value=0.0 ):
        """  Corresponds to IDD Field `z_origin`

        Args:
            value (float): value for IDD Field `z_origin`
                Unit: m
                Default value: 0.0
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
                                 'for field `z_origin`'.format(value))

        self._data["Z Origin"] = value

    @property
    def type(self):
        """Get type

        Returns:
            int: the value of `type` or None if not set
        """
        return self._data["Type"]

    @type.setter
    def type(self, value=1 ):
        """  Corresponds to IDD Field `type`

        Args:
            value (int): value for IDD Field `type`
                Default value: 1
                value >= 1
                value <= 1
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
                                 'for field `type`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `type`')
            if value > 1:
                raise ValueError('value need to be smaller 1 '
                                 'for field `type`')

        self._data["Type"] = value

    @property
    def multiplier(self):
        """Get multiplier

        Returns:
            int: the value of `multiplier` or None if not set
        """
        return self._data["Multiplier"]

    @multiplier.setter
    def multiplier(self, value=1 ):
        """  Corresponds to IDD Field `multiplier`

        Args:
            value (int): value for IDD Field `multiplier`
                Default value: 1
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
                                 'for field `multiplier`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `multiplier`')

        self._data["Multiplier"] = value

    @property
    def ceiling_height(self):
        """Get ceiling_height

        Returns:
            float: the value of `ceiling_height` or None if not set
        """
        return self._data["Ceiling Height"]

    @ceiling_height.setter
    def ceiling_height(self, value=None):
        """  Corresponds to IDD Field `ceiling_height`
        If this field is 0.0, negative or autocalculate, then the average height
        of the zone is automatically calculated and used in subsequent calculations.
        If this field is positive, then the number entered here will be used.
        Note that the Zone Ceiling Height is the distance from the Floor to
        the Ceiling in the Zone, not an absolute height from the ground.

        Args:
            value (float): value for IDD Field `ceiling_height`
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
                                 'for field `ceiling_height`'.format(value))

        self._data["Ceiling Height"] = value

    @property
    def volume(self):
        """Get volume

        Returns:
            float: the value of `volume` or None if not set
        """
        return self._data["Volume"]

    @volume.setter
    def volume(self, value=None):
        """  Corresponds to IDD Field `volume`
        If this field is 0.0, negative or autocalculate, then the volume of the zone
        is automatically calculated and used in subsequent calculations.
        If this field is positive, then the number entered here will be used.

        Args:
            value (float): value for IDD Field `volume`
                Unit: m3
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
                                 'for field `volume`'.format(value))

        self._data["Volume"] = value

    @property
    def floor_area(self):
        """Get floor_area

        Returns:
            float: the value of `floor_area` or None if not set
        """
        return self._data["Floor Area"]

    @floor_area.setter
    def floor_area(self, value=None):
        """  Corresponds to IDD Field `floor_area`
        If this field is 0.0, negative or autocalculate, then the floor area of the zone
        is automatically calculated and used in subsequent calculations.
        If this field is positive, then the number entered here will be used.

        Args:
            value (float): value for IDD Field `floor_area`
                Unit: m2
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
                                 'for field `floor_area`'.format(value))

        self._data["Floor Area"] = value

    @property
    def zone_inside_convection_algorithm(self):
        """Get zone_inside_convection_algorithm

        Returns:
            str: the value of `zone_inside_convection_algorithm` or None if not set
        """
        return self._data["Zone Inside Convection Algorithm"]

    @zone_inside_convection_algorithm.setter
    def zone_inside_convection_algorithm(self, value=None):
        """  Corresponds to IDD Field `zone_inside_convection_algorithm`
        Will default to same value as SurfaceConvectionAlgorithm:Inside object
        setting this field overrides the default SurfaceConvectionAlgorithm:Inside for this zone
        Simple = constant natural convection (ASHRAE)
        TARP = variable natural convection based on temperature difference (ASHRAE)
        CeilingDiffuser = ACH based forced and mixed convection correlations
        for ceiling diffuser configuration with simple natural convection limit
        AdaptiveConvectionAlgorithm = dynamic selection of convection models based on conditions
        TrombeWall = variable natural convection in an enclosed rectangular cavity

        Args:
            value (str): value for IDD Field `zone_inside_convection_algorithm`
                Accepted values are:
                      - Simple
                      - TARP
                      - CeilingDiffuser
                      - AdaptiveConvectionAlgorithm
                      - TrombeWall
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
                                 'for field `zone_inside_convection_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_inside_convection_algorithm`')
            vals = set()
            vals.add("Simple")
            vals.add("TARP")
            vals.add("CeilingDiffuser")
            vals.add("AdaptiveConvectionAlgorithm")
            vals.add("TrombeWall")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `zone_inside_convection_algorithm`'.format(value))

        self._data["Zone Inside Convection Algorithm"] = value

    @property
    def zone_outside_convection_algorithm(self):
        """Get zone_outside_convection_algorithm

        Returns:
            str: the value of `zone_outside_convection_algorithm` or None if not set
        """
        return self._data["Zone Outside Convection Algorithm"]

    @zone_outside_convection_algorithm.setter
    def zone_outside_convection_algorithm(self, value=None):
        """  Corresponds to IDD Field `zone_outside_convection_algorithm`
        Will default to same value as SurfaceConvectionAlgorithm:Outside object
        setting this field overrides the default SurfaceConvectionAlgorithm:Outside for this zone
        SimpleCombined = Combined radiation and convection coefficient using simple ASHRAE model
        TARP = correlation from models developed by ASHRAE, Walton, and Sparrow et. al.
        MoWiTT = correlation from measurements by Klems and Yazdanian for smooth surfaces
        DOE-2 = correlation from measurements by Klems and Yazdanian for rough surfaces
        AdaptiveConvectionAlgorithm = dynamic selection of correlations based on conditions

        Args:
            value (str): value for IDD Field `zone_outside_convection_algorithm`
                Accepted values are:
                      - SimpleCombined
                      - TARP
                      - DOE-2
                      - MoWiTT
                      - AdaptiveConvectionAlgorithm
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
                                 'for field `zone_outside_convection_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_outside_convection_algorithm`')
            vals = set()
            vals.add("SimpleCombined")
            vals.add("TARP")
            vals.add("DOE-2")
            vals.add("MoWiTT")
            vals.add("AdaptiveConvectionAlgorithm")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `zone_outside_convection_algorithm`'.format(value))

        self._data["Zone Outside Convection Algorithm"] = value

    @property
    def part_of_total_floor_area(self):
        """Get part_of_total_floor_area

        Returns:
            str: the value of `part_of_total_floor_area` or None if not set
        """
        return self._data["Part of Total Floor Area"]

    @part_of_total_floor_area.setter
    def part_of_total_floor_area(self, value="Yes"):
        """  Corresponds to IDD Field `part_of_total_floor_area`

        Args:
            value (str): value for IDD Field `part_of_total_floor_area`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
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
                                 'for field `part_of_total_floor_area`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `part_of_total_floor_area`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `part_of_total_floor_area`'.format(value))

        self._data["Part of Total Floor Area"] = value

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
        out.append(self._to_str(self.direction_of_relative_north))
        out.append(self._to_str(self.x_origin))
        out.append(self._to_str(self.y_origin))
        out.append(self._to_str(self.z_origin))
        out.append(self._to_str(self.type))
        out.append(self._to_str(self.multiplier))
        out.append(self._to_str(self.ceiling_height))
        out.append(self._to_str(self.volume))
        out.append(self._to_str(self.floor_area))
        out.append(self._to_str(self.zone_inside_convection_algorithm))
        out.append(self._to_str(self.zone_outside_convection_algorithm))
        out.append(self._to_str(self.part_of_total_floor_area))
        return ",".join(out)