from collections import OrderedDict

class ZoneGroup(object):
    """ Corresponds to IDD object `ZoneGroup`
        Adds a multiplier to a ZoneList. This can be used to reduce the amount of input
        necessary for simulating repetitive structures, such as the identical floors of a
        multi-story building.
    """
    internal_name = "ZoneGroup"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneGroup`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone List Name"] = None
        self._data["Zone List Multiplier"] = None

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
            self.zone_list_name = None
        else:
            self.zone_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_list_multiplier = None
        else:
            self.zone_list_multiplier = vals[i]
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
        Name of the Zone Group

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
    def zone_list_name(self):
        """Get zone_list_name

        Returns:
            str: the value of `zone_list_name` or None if not set
        """
        return self._data["Zone List Name"]

    @zone_list_name.setter
    def zone_list_name(self, value=None):
        """  Corresponds to IDD Field `zone_list_name`

        Args:
            value (str): value for IDD Field `zone_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_list_name`')

        self._data["Zone List Name"] = value

    @property
    def zone_list_multiplier(self):
        """Get zone_list_multiplier

        Returns:
            int: the value of `zone_list_multiplier` or None if not set
        """
        return self._data["Zone List Multiplier"]

    @zone_list_multiplier.setter
    def zone_list_multiplier(self, value=1 ):
        """  Corresponds to IDD Field `zone_list_multiplier`

        Args:
            value (int): value for IDD Field `zone_list_multiplier`
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
                                 'for field `zone_list_multiplier`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_list_multiplier`')

        self._data["Zone List Multiplier"] = value

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
        out.append(self._to_str(self.zone_list_name))
        out.append(self._to_str(self.zone_list_multiplier))
        return ",".join(out)