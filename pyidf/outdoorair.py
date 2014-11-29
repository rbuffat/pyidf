from collections import OrderedDict

class OutdoorAirMixer(object):
    """ Corresponds to IDD object `OutdoorAir:Mixer`
        Outdoor air mixer. Node names cannot be duplicated within a single OutdoorAir:Mixer
        object or across all outdoor air mixers.
    """
    internal_name = "OutdoorAir:Mixer"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `OutdoorAir:Mixer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Mixed Air Node Name"] = None
        self._data["Outdoor Air Stream Node Name"] = None
        self._data["Relief Air Stream Node Name"] = None
        self._data["Return Air Stream Node Name"] = None

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
            self.mixed_air_node_name = None
        else:
            self.mixed_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_stream_node_name = None
        else:
            self.outdoor_air_stream_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relief_air_stream_node_name = None
        else:
            self.relief_air_stream_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.return_air_stream_node_name = None
        else:
            self.return_air_stream_node_name = vals[i]
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
    def mixed_air_node_name(self):
        """Get mixed_air_node_name

        Returns:
            str: the value of `mixed_air_node_name` or None if not set
        """
        return self._data["Mixed Air Node Name"]

    @mixed_air_node_name.setter
    def mixed_air_node_name(self, value=None):
        """  Corresponds to IDD Field `mixed_air_node_name`
        Name of Mixed Air Node

        Args:
            value (str): value for IDD Field `mixed_air_node_name`
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
                                 'for field `mixed_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_air_node_name`')

        self._data["Mixed Air Node Name"] = value

    @property
    def outdoor_air_stream_node_name(self):
        """Get outdoor_air_stream_node_name

        Returns:
            str: the value of `outdoor_air_stream_node_name` or None if not set
        """
        return self._data["Outdoor Air Stream Node Name"]

    @outdoor_air_stream_node_name.setter
    def outdoor_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_stream_node_name`
        Name of Outdoor Air Stream Node

        Args:
            value (str): value for IDD Field `outdoor_air_stream_node_name`
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
                                 'for field `outdoor_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_stream_node_name`')

        self._data["Outdoor Air Stream Node Name"] = value

    @property
    def relief_air_stream_node_name(self):
        """Get relief_air_stream_node_name

        Returns:
            str: the value of `relief_air_stream_node_name` or None if not set
        """
        return self._data["Relief Air Stream Node Name"]

    @relief_air_stream_node_name.setter
    def relief_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `relief_air_stream_node_name`
        Name of Relief Air Stream Node

        Args:
            value (str): value for IDD Field `relief_air_stream_node_name`
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
                                 'for field `relief_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `relief_air_stream_node_name`')

        self._data["Relief Air Stream Node Name"] = value

    @property
    def return_air_stream_node_name(self):
        """Get return_air_stream_node_name

        Returns:
            str: the value of `return_air_stream_node_name` or None if not set
        """
        return self._data["Return Air Stream Node Name"]

    @return_air_stream_node_name.setter
    def return_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `return_air_stream_node_name`
        Name of Return Air Stream Node

        Args:
            value (str): value for IDD Field `return_air_stream_node_name`
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
                                 'for field `return_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `return_air_stream_node_name`')

        self._data["Return Air Stream Node Name"] = value

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
        out.append(self._to_str(self.mixed_air_node_name))
        out.append(self._to_str(self.outdoor_air_stream_node_name))
        out.append(self._to_str(self.relief_air_stream_node_name))
        out.append(self._to_str(self.return_air_stream_node_name))
        return ",".join(out)

class OutdoorAirNode(object):
    """ Corresponds to IDD object `OutdoorAir:Node`
        This object sets the temperature and humidity conditions
        for an outdoor air node.  It allows the height above ground to be
        specified.  This object may be used more than once.
        The same node name may not appear in both an OutdoorAir:Node object and
        an OutdoorAir:NodeList object.
    """
    internal_name = "OutdoorAir:Node"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `OutdoorAir:Node`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Height Above Ground"] = None

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
            self.height_above_ground = None
        else:
            self.height_above_ground = vals[i]
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
    def height_above_ground(self):
        """Get height_above_ground

        Returns:
            float: the value of `height_above_ground` or None if not set
        """
        return self._data["Height Above Ground"]

    @height_above_ground.setter
    def height_above_ground(self, value=-1.0 ):
        """  Corresponds to IDD Field `height_above_ground`
        A value less than zero indicates that the height will be ignored and the weather file conditions will be used.

        Args:
            value (float): value for IDD Field `height_above_ground`
                Unit: m
                Default value: -1.0
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
                                 'for field `height_above_ground`'.format(value))

        self._data["Height Above Ground"] = value

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
        out.append(self._to_str(self.height_above_ground))
        return ",".join(out)

class OutdoorAirNodeList(object):
    """ Corresponds to IDD object `OutdoorAir:NodeList`
        This object sets the temperature and humidity conditions
        for an outdoor air node using the weather data values.
        to vary outdoor air node conditions with height above ground
        use OutdoorAir:Node instead of this object.
        This object may be used more than once.
        The same node name may not appear in both an OutdoorAir:Node object and
        an OutdoorAir:NodeList object.
    """
    internal_name = "OutdoorAir:NodeList"
    field_count = 140

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `OutdoorAir:NodeList`
        """
        self._data = OrderedDict()
        self._data["Node or NodeList Name 1"] = None
        self._data["Node or NodeList Name 2"] = None
        self._data["Node or NodeList Name 3"] = None
        self._data["Node or NodeList Name 4"] = None
        self._data["Node or NodeList Name 5"] = None
        self._data["Node or NodeList Name 6"] = None
        self._data["Node or NodeList Name 7"] = None
        self._data["Node or NodeList Name 8"] = None
        self._data["Node or NodeList Name 9"] = None
        self._data["Node or NodeList Name 10"] = None
        self._data["Node or NodeList Name 11"] = None
        self._data["Node or NodeList Name 12"] = None
        self._data["Node or NodeList Name 13"] = None
        self._data["Node or NodeList Name 14"] = None
        self._data["Node or NodeList Name 15"] = None
        self._data["Node or NodeList Name 16"] = None
        self._data["Node or NodeList Name 17"] = None
        self._data["Node or NodeList Name 18"] = None
        self._data["Node or NodeList Name 19"] = None
        self._data["Node or NodeList Name 20"] = None
        self._data["Node or NodeList Name 21"] = None
        self._data["Node or NodeList Name 22"] = None
        self._data["Node or NodeList Name 23"] = None
        self._data["Node or NodeList Name 24"] = None
        self._data["Node or NodeList Name 25"] = None
        self._data["Node or NodeList Name 26"] = None
        self._data["Node or NodeList Name 27"] = None
        self._data["Node or NodeList Name 28"] = None
        self._data["Node or NodeList Name 29"] = None
        self._data["Node or NodeList Name 30"] = None
        self._data["Node or NodeList Name 31"] = None
        self._data["Node or NodeList Name 32"] = None
        self._data["Node or NodeList Name 33"] = None
        self._data["Node or NodeList Name 34"] = None
        self._data["Node or NodeList Name 35"] = None
        self._data["Node or NodeList Name 36"] = None
        self._data["Node or NodeList Name 37"] = None
        self._data["Node or NodeList Name 38"] = None
        self._data["Node or NodeList Name 39"] = None
        self._data["Node or NodeList Name 40"] = None
        self._data["Node or NodeList Name 41"] = None
        self._data["Node or NodeList Name 42"] = None
        self._data["Node or NodeList Name 43"] = None
        self._data["Node or NodeList Name 44"] = None
        self._data["Node or NodeList Name 45"] = None
        self._data["Node or NodeList Name 46"] = None
        self._data["Node or NodeList Name 47"] = None
        self._data["Node or NodeList Name 48"] = None
        self._data["Node or NodeList Name 49"] = None
        self._data["Node or NodeList Name 50"] = None
        self._data["Node or NodeList Name 51"] = None
        self._data["Node or NodeList Name 52"] = None
        self._data["Node or NodeList Name 53"] = None
        self._data["Node or NodeList Name 54"] = None
        self._data["Node or NodeList Name 55"] = None
        self._data["Node or NodeList Name 56"] = None
        self._data["Node or NodeList Name 57"] = None
        self._data["Node or NodeList Name 58"] = None
        self._data["Node or NodeList Name 59"] = None
        self._data["Node or NodeList Name 60"] = None
        self._data["Node or NodeList Name 61"] = None
        self._data["Node or NodeList Name 62"] = None
        self._data["Node or NodeList Name 63"] = None
        self._data["Node or NodeList Name 64"] = None
        self._data["Node or NodeList Name 65"] = None
        self._data["Node or NodeList Name 66"] = None
        self._data["Node or NodeList Name 67"] = None
        self._data["Node or NodeList Name 68"] = None
        self._data["Node or NodeList Name 69"] = None
        self._data["Node or NodeList Name 70"] = None
        self._data["Node or NodeList Name 71"] = None
        self._data["Node or NodeList Name 72"] = None
        self._data["Node or NodeList Name 73"] = None
        self._data["Node or NodeList Name 74"] = None
        self._data["Node or NodeList Name 75"] = None
        self._data["Node or NodeList Name 76"] = None
        self._data["Node or NodeList Name 77"] = None
        self._data["Node or NodeList Name 78"] = None
        self._data["Node or NodeList Name 79"] = None
        self._data["Node or NodeList Name 80"] = None
        self._data["Node or NodeList Name 81"] = None
        self._data["Node or NodeList Name 82"] = None
        self._data["Node or NodeList Name 83"] = None
        self._data["Node or NodeList Name 84"] = None
        self._data["Node or NodeList Name 85"] = None
        self._data["Node or NodeList Name 86"] = None
        self._data["Node or NodeList Name 87"] = None
        self._data["Node or NodeList Name 88"] = None
        self._data["Node or NodeList Name 89"] = None
        self._data["Node or NodeList Name 90"] = None
        self._data["Node or NodeList Name 91"] = None
        self._data["Node or NodeList Name 92"] = None
        self._data["Node or NodeList Name 93"] = None
        self._data["Node or NodeList Name 94"] = None
        self._data["Node or NodeList Name 95"] = None
        self._data["Node or NodeList Name 96"] = None
        self._data["Node or NodeList Name 97"] = None
        self._data["Node or NodeList Name 98"] = None
        self._data["Node or NodeList Name 99"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None
        self._data["Node or NodeList Name 100"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_1 = None
        else:
            self.node_or_nodelist_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_2 = None
        else:
            self.node_or_nodelist_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_3 = None
        else:
            self.node_or_nodelist_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_4 = None
        else:
            self.node_or_nodelist_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_5 = None
        else:
            self.node_or_nodelist_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_6 = None
        else:
            self.node_or_nodelist_name_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_7 = None
        else:
            self.node_or_nodelist_name_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_8 = None
        else:
            self.node_or_nodelist_name_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_9 = None
        else:
            self.node_or_nodelist_name_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_10 = None
        else:
            self.node_or_nodelist_name_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_11 = None
        else:
            self.node_or_nodelist_name_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_12 = None
        else:
            self.node_or_nodelist_name_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_13 = None
        else:
            self.node_or_nodelist_name_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_14 = None
        else:
            self.node_or_nodelist_name_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_15 = None
        else:
            self.node_or_nodelist_name_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_16 = None
        else:
            self.node_or_nodelist_name_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_17 = None
        else:
            self.node_or_nodelist_name_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_18 = None
        else:
            self.node_or_nodelist_name_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_19 = None
        else:
            self.node_or_nodelist_name_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_20 = None
        else:
            self.node_or_nodelist_name_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_21 = None
        else:
            self.node_or_nodelist_name_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_22 = None
        else:
            self.node_or_nodelist_name_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_23 = None
        else:
            self.node_or_nodelist_name_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_24 = None
        else:
            self.node_or_nodelist_name_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_25 = None
        else:
            self.node_or_nodelist_name_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_26 = None
        else:
            self.node_or_nodelist_name_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_27 = None
        else:
            self.node_or_nodelist_name_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_28 = None
        else:
            self.node_or_nodelist_name_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_29 = None
        else:
            self.node_or_nodelist_name_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_30 = None
        else:
            self.node_or_nodelist_name_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_31 = None
        else:
            self.node_or_nodelist_name_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_32 = None
        else:
            self.node_or_nodelist_name_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_33 = None
        else:
            self.node_or_nodelist_name_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_34 = None
        else:
            self.node_or_nodelist_name_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_35 = None
        else:
            self.node_or_nodelist_name_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_36 = None
        else:
            self.node_or_nodelist_name_36 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_37 = None
        else:
            self.node_or_nodelist_name_37 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_38 = None
        else:
            self.node_or_nodelist_name_38 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_39 = None
        else:
            self.node_or_nodelist_name_39 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_40 = None
        else:
            self.node_or_nodelist_name_40 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_41 = None
        else:
            self.node_or_nodelist_name_41 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_42 = None
        else:
            self.node_or_nodelist_name_42 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_43 = None
        else:
            self.node_or_nodelist_name_43 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_44 = None
        else:
            self.node_or_nodelist_name_44 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_45 = None
        else:
            self.node_or_nodelist_name_45 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_46 = None
        else:
            self.node_or_nodelist_name_46 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_47 = None
        else:
            self.node_or_nodelist_name_47 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_48 = None
        else:
            self.node_or_nodelist_name_48 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_49 = None
        else:
            self.node_or_nodelist_name_49 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_50 = None
        else:
            self.node_or_nodelist_name_50 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_51 = None
        else:
            self.node_or_nodelist_name_51 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_52 = None
        else:
            self.node_or_nodelist_name_52 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_53 = None
        else:
            self.node_or_nodelist_name_53 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_54 = None
        else:
            self.node_or_nodelist_name_54 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_55 = None
        else:
            self.node_or_nodelist_name_55 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_56 = None
        else:
            self.node_or_nodelist_name_56 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_57 = None
        else:
            self.node_or_nodelist_name_57 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_58 = None
        else:
            self.node_or_nodelist_name_58 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_59 = None
        else:
            self.node_or_nodelist_name_59 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_60 = None
        else:
            self.node_or_nodelist_name_60 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_61 = None
        else:
            self.node_or_nodelist_name_61 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_62 = None
        else:
            self.node_or_nodelist_name_62 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_63 = None
        else:
            self.node_or_nodelist_name_63 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_64 = None
        else:
            self.node_or_nodelist_name_64 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_65 = None
        else:
            self.node_or_nodelist_name_65 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_66 = None
        else:
            self.node_or_nodelist_name_66 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_67 = None
        else:
            self.node_or_nodelist_name_67 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_68 = None
        else:
            self.node_or_nodelist_name_68 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_69 = None
        else:
            self.node_or_nodelist_name_69 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_70 = None
        else:
            self.node_or_nodelist_name_70 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_71 = None
        else:
            self.node_or_nodelist_name_71 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_72 = None
        else:
            self.node_or_nodelist_name_72 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_73 = None
        else:
            self.node_or_nodelist_name_73 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_74 = None
        else:
            self.node_or_nodelist_name_74 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_75 = None
        else:
            self.node_or_nodelist_name_75 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_76 = None
        else:
            self.node_or_nodelist_name_76 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_77 = None
        else:
            self.node_or_nodelist_name_77 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_78 = None
        else:
            self.node_or_nodelist_name_78 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_79 = None
        else:
            self.node_or_nodelist_name_79 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_80 = None
        else:
            self.node_or_nodelist_name_80 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_81 = None
        else:
            self.node_or_nodelist_name_81 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_82 = None
        else:
            self.node_or_nodelist_name_82 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_83 = None
        else:
            self.node_or_nodelist_name_83 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_84 = None
        else:
            self.node_or_nodelist_name_84 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_85 = None
        else:
            self.node_or_nodelist_name_85 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_86 = None
        else:
            self.node_or_nodelist_name_86 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_87 = None
        else:
            self.node_or_nodelist_name_87 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_88 = None
        else:
            self.node_or_nodelist_name_88 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_89 = None
        else:
            self.node_or_nodelist_name_89 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_90 = None
        else:
            self.node_or_nodelist_name_90 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_91 = None
        else:
            self.node_or_nodelist_name_91 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_92 = None
        else:
            self.node_or_nodelist_name_92 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_93 = None
        else:
            self.node_or_nodelist_name_93 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_94 = None
        else:
            self.node_or_nodelist_name_94 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_95 = None
        else:
            self.node_or_nodelist_name_95 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_96 = None
        else:
            self.node_or_nodelist_name_96 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_97 = None
        else:
            self.node_or_nodelist_name_97 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_98 = None
        else:
            self.node_or_nodelist_name_98 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_99 = None
        else:
            self.node_or_nodelist_name_99 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_or_nodelist_name_100 = None
        else:
            self.node_or_nodelist_name_100 = vals[i]
        i += 1

    @property
    def node_or_nodelist_name_1(self):
        """Get node_or_nodelist_name_1

        Returns:
            str: the value of `node_or_nodelist_name_1` or None if not set
        """
        return self._data["Node or NodeList Name 1"]

    @node_or_nodelist_name_1.setter
    def node_or_nodelist_name_1(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_1`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_1`
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
                                 'for field `node_or_nodelist_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_1`')

        self._data["Node or NodeList Name 1"] = value

    @property
    def node_or_nodelist_name_2(self):
        """Get node_or_nodelist_name_2

        Returns:
            str: the value of `node_or_nodelist_name_2` or None if not set
        """
        return self._data["Node or NodeList Name 2"]

    @node_or_nodelist_name_2.setter
    def node_or_nodelist_name_2(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_2`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_2`
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
                                 'for field `node_or_nodelist_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_2`')

        self._data["Node or NodeList Name 2"] = value

    @property
    def node_or_nodelist_name_3(self):
        """Get node_or_nodelist_name_3

        Returns:
            str: the value of `node_or_nodelist_name_3` or None if not set
        """
        return self._data["Node or NodeList Name 3"]

    @node_or_nodelist_name_3.setter
    def node_or_nodelist_name_3(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_3`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_3`
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
                                 'for field `node_or_nodelist_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_3`')

        self._data["Node or NodeList Name 3"] = value

    @property
    def node_or_nodelist_name_4(self):
        """Get node_or_nodelist_name_4

        Returns:
            str: the value of `node_or_nodelist_name_4` or None if not set
        """
        return self._data["Node or NodeList Name 4"]

    @node_or_nodelist_name_4.setter
    def node_or_nodelist_name_4(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_4`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_4`
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
                                 'for field `node_or_nodelist_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_4`')

        self._data["Node or NodeList Name 4"] = value

    @property
    def node_or_nodelist_name_5(self):
        """Get node_or_nodelist_name_5

        Returns:
            str: the value of `node_or_nodelist_name_5` or None if not set
        """
        return self._data["Node or NodeList Name 5"]

    @node_or_nodelist_name_5.setter
    def node_or_nodelist_name_5(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_5`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_5`
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
                                 'for field `node_or_nodelist_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_5`')

        self._data["Node or NodeList Name 5"] = value

    @property
    def node_or_nodelist_name_6(self):
        """Get node_or_nodelist_name_6

        Returns:
            str: the value of `node_or_nodelist_name_6` or None if not set
        """
        return self._data["Node or NodeList Name 6"]

    @node_or_nodelist_name_6.setter
    def node_or_nodelist_name_6(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_6`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_6`
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
                                 'for field `node_or_nodelist_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_6`')

        self._data["Node or NodeList Name 6"] = value

    @property
    def node_or_nodelist_name_7(self):
        """Get node_or_nodelist_name_7

        Returns:
            str: the value of `node_or_nodelist_name_7` or None if not set
        """
        return self._data["Node or NodeList Name 7"]

    @node_or_nodelist_name_7.setter
    def node_or_nodelist_name_7(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_7`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_7`
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
                                 'for field `node_or_nodelist_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_7`')

        self._data["Node or NodeList Name 7"] = value

    @property
    def node_or_nodelist_name_8(self):
        """Get node_or_nodelist_name_8

        Returns:
            str: the value of `node_or_nodelist_name_8` or None if not set
        """
        return self._data["Node or NodeList Name 8"]

    @node_or_nodelist_name_8.setter
    def node_or_nodelist_name_8(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_8`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_8`
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
                                 'for field `node_or_nodelist_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_8`')

        self._data["Node or NodeList Name 8"] = value

    @property
    def node_or_nodelist_name_9(self):
        """Get node_or_nodelist_name_9

        Returns:
            str: the value of `node_or_nodelist_name_9` or None if not set
        """
        return self._data["Node or NodeList Name 9"]

    @node_or_nodelist_name_9.setter
    def node_or_nodelist_name_9(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_9`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_9`
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
                                 'for field `node_or_nodelist_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_9`')

        self._data["Node or NodeList Name 9"] = value

    @property
    def node_or_nodelist_name_10(self):
        """Get node_or_nodelist_name_10

        Returns:
            str: the value of `node_or_nodelist_name_10` or None if not set
        """
        return self._data["Node or NodeList Name 10"]

    @node_or_nodelist_name_10.setter
    def node_or_nodelist_name_10(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_10`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_10`
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
                                 'for field `node_or_nodelist_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_10`')

        self._data["Node or NodeList Name 10"] = value

    @property
    def node_or_nodelist_name_11(self):
        """Get node_or_nodelist_name_11

        Returns:
            str: the value of `node_or_nodelist_name_11` or None if not set
        """
        return self._data["Node or NodeList Name 11"]

    @node_or_nodelist_name_11.setter
    def node_or_nodelist_name_11(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_11`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_11`
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
                                 'for field `node_or_nodelist_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_11`')

        self._data["Node or NodeList Name 11"] = value

    @property
    def node_or_nodelist_name_12(self):
        """Get node_or_nodelist_name_12

        Returns:
            str: the value of `node_or_nodelist_name_12` or None if not set
        """
        return self._data["Node or NodeList Name 12"]

    @node_or_nodelist_name_12.setter
    def node_or_nodelist_name_12(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_12`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_12`
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
                                 'for field `node_or_nodelist_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_12`')

        self._data["Node or NodeList Name 12"] = value

    @property
    def node_or_nodelist_name_13(self):
        """Get node_or_nodelist_name_13

        Returns:
            str: the value of `node_or_nodelist_name_13` or None if not set
        """
        return self._data["Node or NodeList Name 13"]

    @node_or_nodelist_name_13.setter
    def node_or_nodelist_name_13(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_13`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_13`
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
                                 'for field `node_or_nodelist_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_13`')

        self._data["Node or NodeList Name 13"] = value

    @property
    def node_or_nodelist_name_14(self):
        """Get node_or_nodelist_name_14

        Returns:
            str: the value of `node_or_nodelist_name_14` or None if not set
        """
        return self._data["Node or NodeList Name 14"]

    @node_or_nodelist_name_14.setter
    def node_or_nodelist_name_14(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_14`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_14`
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
                                 'for field `node_or_nodelist_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_14`')

        self._data["Node or NodeList Name 14"] = value

    @property
    def node_or_nodelist_name_15(self):
        """Get node_or_nodelist_name_15

        Returns:
            str: the value of `node_or_nodelist_name_15` or None if not set
        """
        return self._data["Node or NodeList Name 15"]

    @node_or_nodelist_name_15.setter
    def node_or_nodelist_name_15(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_15`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_15`
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
                                 'for field `node_or_nodelist_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_15`')

        self._data["Node or NodeList Name 15"] = value

    @property
    def node_or_nodelist_name_16(self):
        """Get node_or_nodelist_name_16

        Returns:
            str: the value of `node_or_nodelist_name_16` or None if not set
        """
        return self._data["Node or NodeList Name 16"]

    @node_or_nodelist_name_16.setter
    def node_or_nodelist_name_16(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_16`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_16`
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
                                 'for field `node_or_nodelist_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_16`')

        self._data["Node or NodeList Name 16"] = value

    @property
    def node_or_nodelist_name_17(self):
        """Get node_or_nodelist_name_17

        Returns:
            str: the value of `node_or_nodelist_name_17` or None if not set
        """
        return self._data["Node or NodeList Name 17"]

    @node_or_nodelist_name_17.setter
    def node_or_nodelist_name_17(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_17`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_17`
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
                                 'for field `node_or_nodelist_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_17`')

        self._data["Node or NodeList Name 17"] = value

    @property
    def node_or_nodelist_name_18(self):
        """Get node_or_nodelist_name_18

        Returns:
            str: the value of `node_or_nodelist_name_18` or None if not set
        """
        return self._data["Node or NodeList Name 18"]

    @node_or_nodelist_name_18.setter
    def node_or_nodelist_name_18(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_18`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_18`
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
                                 'for field `node_or_nodelist_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_18`')

        self._data["Node or NodeList Name 18"] = value

    @property
    def node_or_nodelist_name_19(self):
        """Get node_or_nodelist_name_19

        Returns:
            str: the value of `node_or_nodelist_name_19` or None if not set
        """
        return self._data["Node or NodeList Name 19"]

    @node_or_nodelist_name_19.setter
    def node_or_nodelist_name_19(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_19`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_19`
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
                                 'for field `node_or_nodelist_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_19`')

        self._data["Node or NodeList Name 19"] = value

    @property
    def node_or_nodelist_name_20(self):
        """Get node_or_nodelist_name_20

        Returns:
            str: the value of `node_or_nodelist_name_20` or None if not set
        """
        return self._data["Node or NodeList Name 20"]

    @node_or_nodelist_name_20.setter
    def node_or_nodelist_name_20(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_20`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_20`
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
                                 'for field `node_or_nodelist_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_20`')

        self._data["Node or NodeList Name 20"] = value

    @property
    def node_or_nodelist_name_21(self):
        """Get node_or_nodelist_name_21

        Returns:
            str: the value of `node_or_nodelist_name_21` or None if not set
        """
        return self._data["Node or NodeList Name 21"]

    @node_or_nodelist_name_21.setter
    def node_or_nodelist_name_21(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_21`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_21`
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
                                 'for field `node_or_nodelist_name_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_21`')

        self._data["Node or NodeList Name 21"] = value

    @property
    def node_or_nodelist_name_22(self):
        """Get node_or_nodelist_name_22

        Returns:
            str: the value of `node_or_nodelist_name_22` or None if not set
        """
        return self._data["Node or NodeList Name 22"]

    @node_or_nodelist_name_22.setter
    def node_or_nodelist_name_22(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_22`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_22`
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
                                 'for field `node_or_nodelist_name_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_22`')

        self._data["Node or NodeList Name 22"] = value

    @property
    def node_or_nodelist_name_23(self):
        """Get node_or_nodelist_name_23

        Returns:
            str: the value of `node_or_nodelist_name_23` or None if not set
        """
        return self._data["Node or NodeList Name 23"]

    @node_or_nodelist_name_23.setter
    def node_or_nodelist_name_23(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_23`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_23`
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
                                 'for field `node_or_nodelist_name_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_23`')

        self._data["Node or NodeList Name 23"] = value

    @property
    def node_or_nodelist_name_24(self):
        """Get node_or_nodelist_name_24

        Returns:
            str: the value of `node_or_nodelist_name_24` or None if not set
        """
        return self._data["Node or NodeList Name 24"]

    @node_or_nodelist_name_24.setter
    def node_or_nodelist_name_24(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_24`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_24`
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
                                 'for field `node_or_nodelist_name_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_24`')

        self._data["Node or NodeList Name 24"] = value

    @property
    def node_or_nodelist_name_25(self):
        """Get node_or_nodelist_name_25

        Returns:
            str: the value of `node_or_nodelist_name_25` or None if not set
        """
        return self._data["Node or NodeList Name 25"]

    @node_or_nodelist_name_25.setter
    def node_or_nodelist_name_25(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_25`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_25`
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
                                 'for field `node_or_nodelist_name_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_25`')

        self._data["Node or NodeList Name 25"] = value

    @property
    def node_or_nodelist_name_26(self):
        """Get node_or_nodelist_name_26

        Returns:
            str: the value of `node_or_nodelist_name_26` or None if not set
        """
        return self._data["Node or NodeList Name 26"]

    @node_or_nodelist_name_26.setter
    def node_or_nodelist_name_26(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_26`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_26`
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
                                 'for field `node_or_nodelist_name_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_26`')

        self._data["Node or NodeList Name 26"] = value

    @property
    def node_or_nodelist_name_27(self):
        """Get node_or_nodelist_name_27

        Returns:
            str: the value of `node_or_nodelist_name_27` or None if not set
        """
        return self._data["Node or NodeList Name 27"]

    @node_or_nodelist_name_27.setter
    def node_or_nodelist_name_27(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_27`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_27`
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
                                 'for field `node_or_nodelist_name_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_27`')

        self._data["Node or NodeList Name 27"] = value

    @property
    def node_or_nodelist_name_28(self):
        """Get node_or_nodelist_name_28

        Returns:
            str: the value of `node_or_nodelist_name_28` or None if not set
        """
        return self._data["Node or NodeList Name 28"]

    @node_or_nodelist_name_28.setter
    def node_or_nodelist_name_28(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_28`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_28`
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
                                 'for field `node_or_nodelist_name_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_28`')

        self._data["Node or NodeList Name 28"] = value

    @property
    def node_or_nodelist_name_29(self):
        """Get node_or_nodelist_name_29

        Returns:
            str: the value of `node_or_nodelist_name_29` or None if not set
        """
        return self._data["Node or NodeList Name 29"]

    @node_or_nodelist_name_29.setter
    def node_or_nodelist_name_29(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_29`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_29`
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
                                 'for field `node_or_nodelist_name_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_29`')

        self._data["Node or NodeList Name 29"] = value

    @property
    def node_or_nodelist_name_30(self):
        """Get node_or_nodelist_name_30

        Returns:
            str: the value of `node_or_nodelist_name_30` or None if not set
        """
        return self._data["Node or NodeList Name 30"]

    @node_or_nodelist_name_30.setter
    def node_or_nodelist_name_30(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_30`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_30`
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
                                 'for field `node_or_nodelist_name_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_30`')

        self._data["Node or NodeList Name 30"] = value

    @property
    def node_or_nodelist_name_31(self):
        """Get node_or_nodelist_name_31

        Returns:
            str: the value of `node_or_nodelist_name_31` or None if not set
        """
        return self._data["Node or NodeList Name 31"]

    @node_or_nodelist_name_31.setter
    def node_or_nodelist_name_31(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_31`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_31`
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
                                 'for field `node_or_nodelist_name_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_31`')

        self._data["Node or NodeList Name 31"] = value

    @property
    def node_or_nodelist_name_32(self):
        """Get node_or_nodelist_name_32

        Returns:
            str: the value of `node_or_nodelist_name_32` or None if not set
        """
        return self._data["Node or NodeList Name 32"]

    @node_or_nodelist_name_32.setter
    def node_or_nodelist_name_32(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_32`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_32`
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
                                 'for field `node_or_nodelist_name_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_32`')

        self._data["Node or NodeList Name 32"] = value

    @property
    def node_or_nodelist_name_33(self):
        """Get node_or_nodelist_name_33

        Returns:
            str: the value of `node_or_nodelist_name_33` or None if not set
        """
        return self._data["Node or NodeList Name 33"]

    @node_or_nodelist_name_33.setter
    def node_or_nodelist_name_33(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_33`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_33`
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
                                 'for field `node_or_nodelist_name_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_33`')

        self._data["Node or NodeList Name 33"] = value

    @property
    def node_or_nodelist_name_34(self):
        """Get node_or_nodelist_name_34

        Returns:
            str: the value of `node_or_nodelist_name_34` or None if not set
        """
        return self._data["Node or NodeList Name 34"]

    @node_or_nodelist_name_34.setter
    def node_or_nodelist_name_34(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_34`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_34`
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
                                 'for field `node_or_nodelist_name_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_34`')

        self._data["Node or NodeList Name 34"] = value

    @property
    def node_or_nodelist_name_35(self):
        """Get node_or_nodelist_name_35

        Returns:
            str: the value of `node_or_nodelist_name_35` or None if not set
        """
        return self._data["Node or NodeList Name 35"]

    @node_or_nodelist_name_35.setter
    def node_or_nodelist_name_35(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_35`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_35`
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
                                 'for field `node_or_nodelist_name_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_35`')

        self._data["Node or NodeList Name 35"] = value

    @property
    def node_or_nodelist_name_36(self):
        """Get node_or_nodelist_name_36

        Returns:
            str: the value of `node_or_nodelist_name_36` or None if not set
        """
        return self._data["Node or NodeList Name 36"]

    @node_or_nodelist_name_36.setter
    def node_or_nodelist_name_36(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_36`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_36`
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
                                 'for field `node_or_nodelist_name_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_36`')

        self._data["Node or NodeList Name 36"] = value

    @property
    def node_or_nodelist_name_37(self):
        """Get node_or_nodelist_name_37

        Returns:
            str: the value of `node_or_nodelist_name_37` or None if not set
        """
        return self._data["Node or NodeList Name 37"]

    @node_or_nodelist_name_37.setter
    def node_or_nodelist_name_37(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_37`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_37`
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
                                 'for field `node_or_nodelist_name_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_37`')

        self._data["Node or NodeList Name 37"] = value

    @property
    def node_or_nodelist_name_38(self):
        """Get node_or_nodelist_name_38

        Returns:
            str: the value of `node_or_nodelist_name_38` or None if not set
        """
        return self._data["Node or NodeList Name 38"]

    @node_or_nodelist_name_38.setter
    def node_or_nodelist_name_38(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_38`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_38`
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
                                 'for field `node_or_nodelist_name_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_38`')

        self._data["Node or NodeList Name 38"] = value

    @property
    def node_or_nodelist_name_39(self):
        """Get node_or_nodelist_name_39

        Returns:
            str: the value of `node_or_nodelist_name_39` or None if not set
        """
        return self._data["Node or NodeList Name 39"]

    @node_or_nodelist_name_39.setter
    def node_or_nodelist_name_39(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_39`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_39`
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
                                 'for field `node_or_nodelist_name_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_39`')

        self._data["Node or NodeList Name 39"] = value

    @property
    def node_or_nodelist_name_40(self):
        """Get node_or_nodelist_name_40

        Returns:
            str: the value of `node_or_nodelist_name_40` or None if not set
        """
        return self._data["Node or NodeList Name 40"]

    @node_or_nodelist_name_40.setter
    def node_or_nodelist_name_40(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_40`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_40`
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
                                 'for field `node_or_nodelist_name_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_40`')

        self._data["Node or NodeList Name 40"] = value

    @property
    def node_or_nodelist_name_41(self):
        """Get node_or_nodelist_name_41

        Returns:
            str: the value of `node_or_nodelist_name_41` or None if not set
        """
        return self._data["Node or NodeList Name 41"]

    @node_or_nodelist_name_41.setter
    def node_or_nodelist_name_41(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_41`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_41`
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
                                 'for field `node_or_nodelist_name_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_41`')

        self._data["Node or NodeList Name 41"] = value

    @property
    def node_or_nodelist_name_42(self):
        """Get node_or_nodelist_name_42

        Returns:
            str: the value of `node_or_nodelist_name_42` or None if not set
        """
        return self._data["Node or NodeList Name 42"]

    @node_or_nodelist_name_42.setter
    def node_or_nodelist_name_42(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_42`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_42`
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
                                 'for field `node_or_nodelist_name_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_42`')

        self._data["Node or NodeList Name 42"] = value

    @property
    def node_or_nodelist_name_43(self):
        """Get node_or_nodelist_name_43

        Returns:
            str: the value of `node_or_nodelist_name_43` or None if not set
        """
        return self._data["Node or NodeList Name 43"]

    @node_or_nodelist_name_43.setter
    def node_or_nodelist_name_43(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_43`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_43`
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
                                 'for field `node_or_nodelist_name_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_43`')

        self._data["Node or NodeList Name 43"] = value

    @property
    def node_or_nodelist_name_44(self):
        """Get node_or_nodelist_name_44

        Returns:
            str: the value of `node_or_nodelist_name_44` or None if not set
        """
        return self._data["Node or NodeList Name 44"]

    @node_or_nodelist_name_44.setter
    def node_or_nodelist_name_44(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_44`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_44`
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
                                 'for field `node_or_nodelist_name_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_44`')

        self._data["Node or NodeList Name 44"] = value

    @property
    def node_or_nodelist_name_45(self):
        """Get node_or_nodelist_name_45

        Returns:
            str: the value of `node_or_nodelist_name_45` or None if not set
        """
        return self._data["Node or NodeList Name 45"]

    @node_or_nodelist_name_45.setter
    def node_or_nodelist_name_45(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_45`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_45`
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
                                 'for field `node_or_nodelist_name_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_45`')

        self._data["Node or NodeList Name 45"] = value

    @property
    def node_or_nodelist_name_46(self):
        """Get node_or_nodelist_name_46

        Returns:
            str: the value of `node_or_nodelist_name_46` or None if not set
        """
        return self._data["Node or NodeList Name 46"]

    @node_or_nodelist_name_46.setter
    def node_or_nodelist_name_46(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_46`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_46`
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
                                 'for field `node_or_nodelist_name_46`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_46`')

        self._data["Node or NodeList Name 46"] = value

    @property
    def node_or_nodelist_name_47(self):
        """Get node_or_nodelist_name_47

        Returns:
            str: the value of `node_or_nodelist_name_47` or None if not set
        """
        return self._data["Node or NodeList Name 47"]

    @node_or_nodelist_name_47.setter
    def node_or_nodelist_name_47(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_47`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_47`
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
                                 'for field `node_or_nodelist_name_47`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_47`')

        self._data["Node or NodeList Name 47"] = value

    @property
    def node_or_nodelist_name_48(self):
        """Get node_or_nodelist_name_48

        Returns:
            str: the value of `node_or_nodelist_name_48` or None if not set
        """
        return self._data["Node or NodeList Name 48"]

    @node_or_nodelist_name_48.setter
    def node_or_nodelist_name_48(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_48`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_48`
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
                                 'for field `node_or_nodelist_name_48`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_48`')

        self._data["Node or NodeList Name 48"] = value

    @property
    def node_or_nodelist_name_49(self):
        """Get node_or_nodelist_name_49

        Returns:
            str: the value of `node_or_nodelist_name_49` or None if not set
        """
        return self._data["Node or NodeList Name 49"]

    @node_or_nodelist_name_49.setter
    def node_or_nodelist_name_49(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_49`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_49`
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
                                 'for field `node_or_nodelist_name_49`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_49`')

        self._data["Node or NodeList Name 49"] = value

    @property
    def node_or_nodelist_name_50(self):
        """Get node_or_nodelist_name_50

        Returns:
            str: the value of `node_or_nodelist_name_50` or None if not set
        """
        return self._data["Node or NodeList Name 50"]

    @node_or_nodelist_name_50.setter
    def node_or_nodelist_name_50(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_50`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_50`
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
                                 'for field `node_or_nodelist_name_50`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_50`')

        self._data["Node or NodeList Name 50"] = value

    @property
    def node_or_nodelist_name_51(self):
        """Get node_or_nodelist_name_51

        Returns:
            str: the value of `node_or_nodelist_name_51` or None if not set
        """
        return self._data["Node or NodeList Name 51"]

    @node_or_nodelist_name_51.setter
    def node_or_nodelist_name_51(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_51`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_51`
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
                                 'for field `node_or_nodelist_name_51`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_51`')

        self._data["Node or NodeList Name 51"] = value

    @property
    def node_or_nodelist_name_52(self):
        """Get node_or_nodelist_name_52

        Returns:
            str: the value of `node_or_nodelist_name_52` or None if not set
        """
        return self._data["Node or NodeList Name 52"]

    @node_or_nodelist_name_52.setter
    def node_or_nodelist_name_52(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_52`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_52`
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
                                 'for field `node_or_nodelist_name_52`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_52`')

        self._data["Node or NodeList Name 52"] = value

    @property
    def node_or_nodelist_name_53(self):
        """Get node_or_nodelist_name_53

        Returns:
            str: the value of `node_or_nodelist_name_53` or None if not set
        """
        return self._data["Node or NodeList Name 53"]

    @node_or_nodelist_name_53.setter
    def node_or_nodelist_name_53(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_53`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_53`
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
                                 'for field `node_or_nodelist_name_53`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_53`')

        self._data["Node or NodeList Name 53"] = value

    @property
    def node_or_nodelist_name_54(self):
        """Get node_or_nodelist_name_54

        Returns:
            str: the value of `node_or_nodelist_name_54` or None if not set
        """
        return self._data["Node or NodeList Name 54"]

    @node_or_nodelist_name_54.setter
    def node_or_nodelist_name_54(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_54`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_54`
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
                                 'for field `node_or_nodelist_name_54`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_54`')

        self._data["Node or NodeList Name 54"] = value

    @property
    def node_or_nodelist_name_55(self):
        """Get node_or_nodelist_name_55

        Returns:
            str: the value of `node_or_nodelist_name_55` or None if not set
        """
        return self._data["Node or NodeList Name 55"]

    @node_or_nodelist_name_55.setter
    def node_or_nodelist_name_55(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_55`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_55`
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
                                 'for field `node_or_nodelist_name_55`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_55`')

        self._data["Node or NodeList Name 55"] = value

    @property
    def node_or_nodelist_name_56(self):
        """Get node_or_nodelist_name_56

        Returns:
            str: the value of `node_or_nodelist_name_56` or None if not set
        """
        return self._data["Node or NodeList Name 56"]

    @node_or_nodelist_name_56.setter
    def node_or_nodelist_name_56(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_56`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_56`
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
                                 'for field `node_or_nodelist_name_56`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_56`')

        self._data["Node or NodeList Name 56"] = value

    @property
    def node_or_nodelist_name_57(self):
        """Get node_or_nodelist_name_57

        Returns:
            str: the value of `node_or_nodelist_name_57` or None if not set
        """
        return self._data["Node or NodeList Name 57"]

    @node_or_nodelist_name_57.setter
    def node_or_nodelist_name_57(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_57`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_57`
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
                                 'for field `node_or_nodelist_name_57`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_57`')

        self._data["Node or NodeList Name 57"] = value

    @property
    def node_or_nodelist_name_58(self):
        """Get node_or_nodelist_name_58

        Returns:
            str: the value of `node_or_nodelist_name_58` or None if not set
        """
        return self._data["Node or NodeList Name 58"]

    @node_or_nodelist_name_58.setter
    def node_or_nodelist_name_58(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_58`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_58`
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
                                 'for field `node_or_nodelist_name_58`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_58`')

        self._data["Node or NodeList Name 58"] = value

    @property
    def node_or_nodelist_name_59(self):
        """Get node_or_nodelist_name_59

        Returns:
            str: the value of `node_or_nodelist_name_59` or None if not set
        """
        return self._data["Node or NodeList Name 59"]

    @node_or_nodelist_name_59.setter
    def node_or_nodelist_name_59(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_59`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_59`
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
                                 'for field `node_or_nodelist_name_59`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_59`')

        self._data["Node or NodeList Name 59"] = value

    @property
    def node_or_nodelist_name_60(self):
        """Get node_or_nodelist_name_60

        Returns:
            str: the value of `node_or_nodelist_name_60` or None if not set
        """
        return self._data["Node or NodeList Name 60"]

    @node_or_nodelist_name_60.setter
    def node_or_nodelist_name_60(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_60`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_60`
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
                                 'for field `node_or_nodelist_name_60`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_60`')

        self._data["Node or NodeList Name 60"] = value

    @property
    def node_or_nodelist_name_61(self):
        """Get node_or_nodelist_name_61

        Returns:
            str: the value of `node_or_nodelist_name_61` or None if not set
        """
        return self._data["Node or NodeList Name 61"]

    @node_or_nodelist_name_61.setter
    def node_or_nodelist_name_61(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_61`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_61`
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
                                 'for field `node_or_nodelist_name_61`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_61`')

        self._data["Node or NodeList Name 61"] = value

    @property
    def node_or_nodelist_name_62(self):
        """Get node_or_nodelist_name_62

        Returns:
            str: the value of `node_or_nodelist_name_62` or None if not set
        """
        return self._data["Node or NodeList Name 62"]

    @node_or_nodelist_name_62.setter
    def node_or_nodelist_name_62(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_62`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_62`
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
                                 'for field `node_or_nodelist_name_62`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_62`')

        self._data["Node or NodeList Name 62"] = value

    @property
    def node_or_nodelist_name_63(self):
        """Get node_or_nodelist_name_63

        Returns:
            str: the value of `node_or_nodelist_name_63` or None if not set
        """
        return self._data["Node or NodeList Name 63"]

    @node_or_nodelist_name_63.setter
    def node_or_nodelist_name_63(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_63`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_63`
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
                                 'for field `node_or_nodelist_name_63`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_63`')

        self._data["Node or NodeList Name 63"] = value

    @property
    def node_or_nodelist_name_64(self):
        """Get node_or_nodelist_name_64

        Returns:
            str: the value of `node_or_nodelist_name_64` or None if not set
        """
        return self._data["Node or NodeList Name 64"]

    @node_or_nodelist_name_64.setter
    def node_or_nodelist_name_64(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_64`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_64`
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
                                 'for field `node_or_nodelist_name_64`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_64`')

        self._data["Node or NodeList Name 64"] = value

    @property
    def node_or_nodelist_name_65(self):
        """Get node_or_nodelist_name_65

        Returns:
            str: the value of `node_or_nodelist_name_65` or None if not set
        """
        return self._data["Node or NodeList Name 65"]

    @node_or_nodelist_name_65.setter
    def node_or_nodelist_name_65(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_65`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_65`
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
                                 'for field `node_or_nodelist_name_65`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_65`')

        self._data["Node or NodeList Name 65"] = value

    @property
    def node_or_nodelist_name_66(self):
        """Get node_or_nodelist_name_66

        Returns:
            str: the value of `node_or_nodelist_name_66` or None if not set
        """
        return self._data["Node or NodeList Name 66"]

    @node_or_nodelist_name_66.setter
    def node_or_nodelist_name_66(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_66`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_66`
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
                                 'for field `node_or_nodelist_name_66`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_66`')

        self._data["Node or NodeList Name 66"] = value

    @property
    def node_or_nodelist_name_67(self):
        """Get node_or_nodelist_name_67

        Returns:
            str: the value of `node_or_nodelist_name_67` or None if not set
        """
        return self._data["Node or NodeList Name 67"]

    @node_or_nodelist_name_67.setter
    def node_or_nodelist_name_67(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_67`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_67`
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
                                 'for field `node_or_nodelist_name_67`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_67`')

        self._data["Node or NodeList Name 67"] = value

    @property
    def node_or_nodelist_name_68(self):
        """Get node_or_nodelist_name_68

        Returns:
            str: the value of `node_or_nodelist_name_68` or None if not set
        """
        return self._data["Node or NodeList Name 68"]

    @node_or_nodelist_name_68.setter
    def node_or_nodelist_name_68(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_68`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_68`
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
                                 'for field `node_or_nodelist_name_68`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_68`')

        self._data["Node or NodeList Name 68"] = value

    @property
    def node_or_nodelist_name_69(self):
        """Get node_or_nodelist_name_69

        Returns:
            str: the value of `node_or_nodelist_name_69` or None if not set
        """
        return self._data["Node or NodeList Name 69"]

    @node_or_nodelist_name_69.setter
    def node_or_nodelist_name_69(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_69`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_69`
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
                                 'for field `node_or_nodelist_name_69`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_69`')

        self._data["Node or NodeList Name 69"] = value

    @property
    def node_or_nodelist_name_70(self):
        """Get node_or_nodelist_name_70

        Returns:
            str: the value of `node_or_nodelist_name_70` or None if not set
        """
        return self._data["Node or NodeList Name 70"]

    @node_or_nodelist_name_70.setter
    def node_or_nodelist_name_70(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_70`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_70`
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
                                 'for field `node_or_nodelist_name_70`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_70`')

        self._data["Node or NodeList Name 70"] = value

    @property
    def node_or_nodelist_name_71(self):
        """Get node_or_nodelist_name_71

        Returns:
            str: the value of `node_or_nodelist_name_71` or None if not set
        """
        return self._data["Node or NodeList Name 71"]

    @node_or_nodelist_name_71.setter
    def node_or_nodelist_name_71(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_71`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_71`
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
                                 'for field `node_or_nodelist_name_71`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_71`')

        self._data["Node or NodeList Name 71"] = value

    @property
    def node_or_nodelist_name_72(self):
        """Get node_or_nodelist_name_72

        Returns:
            str: the value of `node_or_nodelist_name_72` or None if not set
        """
        return self._data["Node or NodeList Name 72"]

    @node_or_nodelist_name_72.setter
    def node_or_nodelist_name_72(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_72`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_72`
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
                                 'for field `node_or_nodelist_name_72`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_72`')

        self._data["Node or NodeList Name 72"] = value

    @property
    def node_or_nodelist_name_73(self):
        """Get node_or_nodelist_name_73

        Returns:
            str: the value of `node_or_nodelist_name_73` or None if not set
        """
        return self._data["Node or NodeList Name 73"]

    @node_or_nodelist_name_73.setter
    def node_or_nodelist_name_73(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_73`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_73`
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
                                 'for field `node_or_nodelist_name_73`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_73`')

        self._data["Node or NodeList Name 73"] = value

    @property
    def node_or_nodelist_name_74(self):
        """Get node_or_nodelist_name_74

        Returns:
            str: the value of `node_or_nodelist_name_74` or None if not set
        """
        return self._data["Node or NodeList Name 74"]

    @node_or_nodelist_name_74.setter
    def node_or_nodelist_name_74(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_74`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_74`
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
                                 'for field `node_or_nodelist_name_74`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_74`')

        self._data["Node or NodeList Name 74"] = value

    @property
    def node_or_nodelist_name_75(self):
        """Get node_or_nodelist_name_75

        Returns:
            str: the value of `node_or_nodelist_name_75` or None if not set
        """
        return self._data["Node or NodeList Name 75"]

    @node_or_nodelist_name_75.setter
    def node_or_nodelist_name_75(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_75`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_75`
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
                                 'for field `node_or_nodelist_name_75`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_75`')

        self._data["Node or NodeList Name 75"] = value

    @property
    def node_or_nodelist_name_76(self):
        """Get node_or_nodelist_name_76

        Returns:
            str: the value of `node_or_nodelist_name_76` or None if not set
        """
        return self._data["Node or NodeList Name 76"]

    @node_or_nodelist_name_76.setter
    def node_or_nodelist_name_76(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_76`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_76`
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
                                 'for field `node_or_nodelist_name_76`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_76`')

        self._data["Node or NodeList Name 76"] = value

    @property
    def node_or_nodelist_name_77(self):
        """Get node_or_nodelist_name_77

        Returns:
            str: the value of `node_or_nodelist_name_77` or None if not set
        """
        return self._data["Node or NodeList Name 77"]

    @node_or_nodelist_name_77.setter
    def node_or_nodelist_name_77(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_77`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_77`
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
                                 'for field `node_or_nodelist_name_77`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_77`')

        self._data["Node or NodeList Name 77"] = value

    @property
    def node_or_nodelist_name_78(self):
        """Get node_or_nodelist_name_78

        Returns:
            str: the value of `node_or_nodelist_name_78` or None if not set
        """
        return self._data["Node or NodeList Name 78"]

    @node_or_nodelist_name_78.setter
    def node_or_nodelist_name_78(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_78`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_78`
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
                                 'for field `node_or_nodelist_name_78`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_78`')

        self._data["Node or NodeList Name 78"] = value

    @property
    def node_or_nodelist_name_79(self):
        """Get node_or_nodelist_name_79

        Returns:
            str: the value of `node_or_nodelist_name_79` or None if not set
        """
        return self._data["Node or NodeList Name 79"]

    @node_or_nodelist_name_79.setter
    def node_or_nodelist_name_79(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_79`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_79`
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
                                 'for field `node_or_nodelist_name_79`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_79`')

        self._data["Node or NodeList Name 79"] = value

    @property
    def node_or_nodelist_name_80(self):
        """Get node_or_nodelist_name_80

        Returns:
            str: the value of `node_or_nodelist_name_80` or None if not set
        """
        return self._data["Node or NodeList Name 80"]

    @node_or_nodelist_name_80.setter
    def node_or_nodelist_name_80(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_80`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_80`
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
                                 'for field `node_or_nodelist_name_80`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_80`')

        self._data["Node or NodeList Name 80"] = value

    @property
    def node_or_nodelist_name_81(self):
        """Get node_or_nodelist_name_81

        Returns:
            str: the value of `node_or_nodelist_name_81` or None if not set
        """
        return self._data["Node or NodeList Name 81"]

    @node_or_nodelist_name_81.setter
    def node_or_nodelist_name_81(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_81`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_81`
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
                                 'for field `node_or_nodelist_name_81`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_81`')

        self._data["Node or NodeList Name 81"] = value

    @property
    def node_or_nodelist_name_82(self):
        """Get node_or_nodelist_name_82

        Returns:
            str: the value of `node_or_nodelist_name_82` or None if not set
        """
        return self._data["Node or NodeList Name 82"]

    @node_or_nodelist_name_82.setter
    def node_or_nodelist_name_82(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_82`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_82`
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
                                 'for field `node_or_nodelist_name_82`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_82`')

        self._data["Node or NodeList Name 82"] = value

    @property
    def node_or_nodelist_name_83(self):
        """Get node_or_nodelist_name_83

        Returns:
            str: the value of `node_or_nodelist_name_83` or None if not set
        """
        return self._data["Node or NodeList Name 83"]

    @node_or_nodelist_name_83.setter
    def node_or_nodelist_name_83(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_83`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_83`
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
                                 'for field `node_or_nodelist_name_83`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_83`')

        self._data["Node or NodeList Name 83"] = value

    @property
    def node_or_nodelist_name_84(self):
        """Get node_or_nodelist_name_84

        Returns:
            str: the value of `node_or_nodelist_name_84` or None if not set
        """
        return self._data["Node or NodeList Name 84"]

    @node_or_nodelist_name_84.setter
    def node_or_nodelist_name_84(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_84`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_84`
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
                                 'for field `node_or_nodelist_name_84`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_84`')

        self._data["Node or NodeList Name 84"] = value

    @property
    def node_or_nodelist_name_85(self):
        """Get node_or_nodelist_name_85

        Returns:
            str: the value of `node_or_nodelist_name_85` or None if not set
        """
        return self._data["Node or NodeList Name 85"]

    @node_or_nodelist_name_85.setter
    def node_or_nodelist_name_85(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_85`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_85`
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
                                 'for field `node_or_nodelist_name_85`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_85`')

        self._data["Node or NodeList Name 85"] = value

    @property
    def node_or_nodelist_name_86(self):
        """Get node_or_nodelist_name_86

        Returns:
            str: the value of `node_or_nodelist_name_86` or None if not set
        """
        return self._data["Node or NodeList Name 86"]

    @node_or_nodelist_name_86.setter
    def node_or_nodelist_name_86(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_86`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_86`
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
                                 'for field `node_or_nodelist_name_86`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_86`')

        self._data["Node or NodeList Name 86"] = value

    @property
    def node_or_nodelist_name_87(self):
        """Get node_or_nodelist_name_87

        Returns:
            str: the value of `node_or_nodelist_name_87` or None if not set
        """
        return self._data["Node or NodeList Name 87"]

    @node_or_nodelist_name_87.setter
    def node_or_nodelist_name_87(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_87`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_87`
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
                                 'for field `node_or_nodelist_name_87`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_87`')

        self._data["Node or NodeList Name 87"] = value

    @property
    def node_or_nodelist_name_88(self):
        """Get node_or_nodelist_name_88

        Returns:
            str: the value of `node_or_nodelist_name_88` or None if not set
        """
        return self._data["Node or NodeList Name 88"]

    @node_or_nodelist_name_88.setter
    def node_or_nodelist_name_88(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_88`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_88`
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
                                 'for field `node_or_nodelist_name_88`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_88`')

        self._data["Node or NodeList Name 88"] = value

    @property
    def node_or_nodelist_name_89(self):
        """Get node_or_nodelist_name_89

        Returns:
            str: the value of `node_or_nodelist_name_89` or None if not set
        """
        return self._data["Node or NodeList Name 89"]

    @node_or_nodelist_name_89.setter
    def node_or_nodelist_name_89(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_89`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_89`
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
                                 'for field `node_or_nodelist_name_89`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_89`')

        self._data["Node or NodeList Name 89"] = value

    @property
    def node_or_nodelist_name_90(self):
        """Get node_or_nodelist_name_90

        Returns:
            str: the value of `node_or_nodelist_name_90` or None if not set
        """
        return self._data["Node or NodeList Name 90"]

    @node_or_nodelist_name_90.setter
    def node_or_nodelist_name_90(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_90`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_90`
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
                                 'for field `node_or_nodelist_name_90`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_90`')

        self._data["Node or NodeList Name 90"] = value

    @property
    def node_or_nodelist_name_91(self):
        """Get node_or_nodelist_name_91

        Returns:
            str: the value of `node_or_nodelist_name_91` or None if not set
        """
        return self._data["Node or NodeList Name 91"]

    @node_or_nodelist_name_91.setter
    def node_or_nodelist_name_91(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_91`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_91`
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
                                 'for field `node_or_nodelist_name_91`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_91`')

        self._data["Node or NodeList Name 91"] = value

    @property
    def node_or_nodelist_name_92(self):
        """Get node_or_nodelist_name_92

        Returns:
            str: the value of `node_or_nodelist_name_92` or None if not set
        """
        return self._data["Node or NodeList Name 92"]

    @node_or_nodelist_name_92.setter
    def node_or_nodelist_name_92(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_92`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_92`
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
                                 'for field `node_or_nodelist_name_92`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_92`')

        self._data["Node or NodeList Name 92"] = value

    @property
    def node_or_nodelist_name_93(self):
        """Get node_or_nodelist_name_93

        Returns:
            str: the value of `node_or_nodelist_name_93` or None if not set
        """
        return self._data["Node or NodeList Name 93"]

    @node_or_nodelist_name_93.setter
    def node_or_nodelist_name_93(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_93`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_93`
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
                                 'for field `node_or_nodelist_name_93`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_93`')

        self._data["Node or NodeList Name 93"] = value

    @property
    def node_or_nodelist_name_94(self):
        """Get node_or_nodelist_name_94

        Returns:
            str: the value of `node_or_nodelist_name_94` or None if not set
        """
        return self._data["Node or NodeList Name 94"]

    @node_or_nodelist_name_94.setter
    def node_or_nodelist_name_94(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_94`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_94`
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
                                 'for field `node_or_nodelist_name_94`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_94`')

        self._data["Node or NodeList Name 94"] = value

    @property
    def node_or_nodelist_name_95(self):
        """Get node_or_nodelist_name_95

        Returns:
            str: the value of `node_or_nodelist_name_95` or None if not set
        """
        return self._data["Node or NodeList Name 95"]

    @node_or_nodelist_name_95.setter
    def node_or_nodelist_name_95(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_95`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_95`
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
                                 'for field `node_or_nodelist_name_95`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_95`')

        self._data["Node or NodeList Name 95"] = value

    @property
    def node_or_nodelist_name_96(self):
        """Get node_or_nodelist_name_96

        Returns:
            str: the value of `node_or_nodelist_name_96` or None if not set
        """
        return self._data["Node or NodeList Name 96"]

    @node_or_nodelist_name_96.setter
    def node_or_nodelist_name_96(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_96`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_96`
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
                                 'for field `node_or_nodelist_name_96`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_96`')

        self._data["Node or NodeList Name 96"] = value

    @property
    def node_or_nodelist_name_97(self):
        """Get node_or_nodelist_name_97

        Returns:
            str: the value of `node_or_nodelist_name_97` or None if not set
        """
        return self._data["Node or NodeList Name 97"]

    @node_or_nodelist_name_97.setter
    def node_or_nodelist_name_97(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_97`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_97`
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
                                 'for field `node_or_nodelist_name_97`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_97`')

        self._data["Node or NodeList Name 97"] = value

    @property
    def node_or_nodelist_name_98(self):
        """Get node_or_nodelist_name_98

        Returns:
            str: the value of `node_or_nodelist_name_98` or None if not set
        """
        return self._data["Node or NodeList Name 98"]

    @node_or_nodelist_name_98.setter
    def node_or_nodelist_name_98(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_98`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_98`
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
                                 'for field `node_or_nodelist_name_98`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_98`')

        self._data["Node or NodeList Name 98"] = value

    @property
    def node_or_nodelist_name_99(self):
        """Get node_or_nodelist_name_99

        Returns:
            str: the value of `node_or_nodelist_name_99` or None if not set
        """
        return self._data["Node or NodeList Name 99"]

    @node_or_nodelist_name_99.setter
    def node_or_nodelist_name_99(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_99`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_99`
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
                                 'for field `node_or_nodelist_name_99`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_99`')

        self._data["Node or NodeList Name 99"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

    @property
    def node_or_nodelist_name_100(self):
        """Get node_or_nodelist_name_100

        Returns:
            str: the value of `node_or_nodelist_name_100` or None if not set
        """
        return self._data["Node or NodeList Name 100"]

    @node_or_nodelist_name_100.setter
    def node_or_nodelist_name_100(self, value=None):
        """  Corresponds to IDD Field `node_or_nodelist_name_100`

        Args:
            value (str): value for IDD Field `node_or_nodelist_name_100`
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
                                 'for field `node_or_nodelist_name_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_or_nodelist_name_100`')

        self._data["Node or NodeList Name 100"] = value

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
        out.append(self._to_str(self.node_or_nodelist_name_1))
        out.append(self._to_str(self.node_or_nodelist_name_2))
        out.append(self._to_str(self.node_or_nodelist_name_3))
        out.append(self._to_str(self.node_or_nodelist_name_4))
        out.append(self._to_str(self.node_or_nodelist_name_5))
        out.append(self._to_str(self.node_or_nodelist_name_6))
        out.append(self._to_str(self.node_or_nodelist_name_7))
        out.append(self._to_str(self.node_or_nodelist_name_8))
        out.append(self._to_str(self.node_or_nodelist_name_9))
        out.append(self._to_str(self.node_or_nodelist_name_10))
        out.append(self._to_str(self.node_or_nodelist_name_11))
        out.append(self._to_str(self.node_or_nodelist_name_12))
        out.append(self._to_str(self.node_or_nodelist_name_13))
        out.append(self._to_str(self.node_or_nodelist_name_14))
        out.append(self._to_str(self.node_or_nodelist_name_15))
        out.append(self._to_str(self.node_or_nodelist_name_16))
        out.append(self._to_str(self.node_or_nodelist_name_17))
        out.append(self._to_str(self.node_or_nodelist_name_18))
        out.append(self._to_str(self.node_or_nodelist_name_19))
        out.append(self._to_str(self.node_or_nodelist_name_20))
        out.append(self._to_str(self.node_or_nodelist_name_21))
        out.append(self._to_str(self.node_or_nodelist_name_22))
        out.append(self._to_str(self.node_or_nodelist_name_23))
        out.append(self._to_str(self.node_or_nodelist_name_24))
        out.append(self._to_str(self.node_or_nodelist_name_25))
        out.append(self._to_str(self.node_or_nodelist_name_26))
        out.append(self._to_str(self.node_or_nodelist_name_27))
        out.append(self._to_str(self.node_or_nodelist_name_28))
        out.append(self._to_str(self.node_or_nodelist_name_29))
        out.append(self._to_str(self.node_or_nodelist_name_30))
        out.append(self._to_str(self.node_or_nodelist_name_31))
        out.append(self._to_str(self.node_or_nodelist_name_32))
        out.append(self._to_str(self.node_or_nodelist_name_33))
        out.append(self._to_str(self.node_or_nodelist_name_34))
        out.append(self._to_str(self.node_or_nodelist_name_35))
        out.append(self._to_str(self.node_or_nodelist_name_36))
        out.append(self._to_str(self.node_or_nodelist_name_37))
        out.append(self._to_str(self.node_or_nodelist_name_38))
        out.append(self._to_str(self.node_or_nodelist_name_39))
        out.append(self._to_str(self.node_or_nodelist_name_40))
        out.append(self._to_str(self.node_or_nodelist_name_41))
        out.append(self._to_str(self.node_or_nodelist_name_42))
        out.append(self._to_str(self.node_or_nodelist_name_43))
        out.append(self._to_str(self.node_or_nodelist_name_44))
        out.append(self._to_str(self.node_or_nodelist_name_45))
        out.append(self._to_str(self.node_or_nodelist_name_46))
        out.append(self._to_str(self.node_or_nodelist_name_47))
        out.append(self._to_str(self.node_or_nodelist_name_48))
        out.append(self._to_str(self.node_or_nodelist_name_49))
        out.append(self._to_str(self.node_or_nodelist_name_50))
        out.append(self._to_str(self.node_or_nodelist_name_51))
        out.append(self._to_str(self.node_or_nodelist_name_52))
        out.append(self._to_str(self.node_or_nodelist_name_53))
        out.append(self._to_str(self.node_or_nodelist_name_54))
        out.append(self._to_str(self.node_or_nodelist_name_55))
        out.append(self._to_str(self.node_or_nodelist_name_56))
        out.append(self._to_str(self.node_or_nodelist_name_57))
        out.append(self._to_str(self.node_or_nodelist_name_58))
        out.append(self._to_str(self.node_or_nodelist_name_59))
        out.append(self._to_str(self.node_or_nodelist_name_60))
        out.append(self._to_str(self.node_or_nodelist_name_61))
        out.append(self._to_str(self.node_or_nodelist_name_62))
        out.append(self._to_str(self.node_or_nodelist_name_63))
        out.append(self._to_str(self.node_or_nodelist_name_64))
        out.append(self._to_str(self.node_or_nodelist_name_65))
        out.append(self._to_str(self.node_or_nodelist_name_66))
        out.append(self._to_str(self.node_or_nodelist_name_67))
        out.append(self._to_str(self.node_or_nodelist_name_68))
        out.append(self._to_str(self.node_or_nodelist_name_69))
        out.append(self._to_str(self.node_or_nodelist_name_70))
        out.append(self._to_str(self.node_or_nodelist_name_71))
        out.append(self._to_str(self.node_or_nodelist_name_72))
        out.append(self._to_str(self.node_or_nodelist_name_73))
        out.append(self._to_str(self.node_or_nodelist_name_74))
        out.append(self._to_str(self.node_or_nodelist_name_75))
        out.append(self._to_str(self.node_or_nodelist_name_76))
        out.append(self._to_str(self.node_or_nodelist_name_77))
        out.append(self._to_str(self.node_or_nodelist_name_78))
        out.append(self._to_str(self.node_or_nodelist_name_79))
        out.append(self._to_str(self.node_or_nodelist_name_80))
        out.append(self._to_str(self.node_or_nodelist_name_81))
        out.append(self._to_str(self.node_or_nodelist_name_82))
        out.append(self._to_str(self.node_or_nodelist_name_83))
        out.append(self._to_str(self.node_or_nodelist_name_84))
        out.append(self._to_str(self.node_or_nodelist_name_85))
        out.append(self._to_str(self.node_or_nodelist_name_86))
        out.append(self._to_str(self.node_or_nodelist_name_87))
        out.append(self._to_str(self.node_or_nodelist_name_88))
        out.append(self._to_str(self.node_or_nodelist_name_89))
        out.append(self._to_str(self.node_or_nodelist_name_90))
        out.append(self._to_str(self.node_or_nodelist_name_91))
        out.append(self._to_str(self.node_or_nodelist_name_92))
        out.append(self._to_str(self.node_or_nodelist_name_93))
        out.append(self._to_str(self.node_or_nodelist_name_94))
        out.append(self._to_str(self.node_or_nodelist_name_95))
        out.append(self._to_str(self.node_or_nodelist_name_96))
        out.append(self._to_str(self.node_or_nodelist_name_97))
        out.append(self._to_str(self.node_or_nodelist_name_98))
        out.append(self._to_str(self.node_or_nodelist_name_99))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        out.append(self._to_str(self.node_or_nodelist_name_100))
        return ",".join(out)