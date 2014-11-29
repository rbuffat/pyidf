from collections import OrderedDict

class ZoneBaseboardOutdoorTemperatureControlled(object):
    """ Corresponds to IDD object `ZoneBaseboard:OutdoorTemperatureControlled`
        Specifies outside temperature-controlled electric baseboard heating.
    """
    internal_name = "ZoneBaseboard:OutdoorTemperatureControlled"
    field_count = 9

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneBaseboard:OutdoorTemperatureControlled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Schedule Name"] = None
        self._data["Capacity at Low Temperature"] = None
        self._data["Low Temperature"] = None
        self._data["Capacity at High Temperature"] = None
        self._data["High Temperature"] = None
        self._data["Fraction Radiant"] = None
        self._data["End-Use Subcategory"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity_at_low_temperature = None
        else:
            self.capacity_at_low_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_temperature = None
        else:
            self.low_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity_at_high_temperature = None
        else:
            self.capacity_at_high_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_temperature = None
        else:
            self.high_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`

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
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        units in Schedule should be fraction applied to capacity of the baseboard heat equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def capacity_at_low_temperature(self):
        """Get capacity_at_low_temperature

        Returns:
            float: the value of `capacity_at_low_temperature` or None if not set
        """
        return self._data["Capacity at Low Temperature"]

    @capacity_at_low_temperature.setter
    def capacity_at_low_temperature(self, value=None):
        """  Corresponds to IDD Field `capacity_at_low_temperature`

        Args:
            value (float): value for IDD Field `capacity_at_low_temperature`
                Unit: W
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
                                 'for field `capacity_at_low_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `capacity_at_low_temperature`')

        self._data["Capacity at Low Temperature"] = value

    @property
    def low_temperature(self):
        """Get low_temperature

        Returns:
            float: the value of `low_temperature` or None if not set
        """
        return self._data["Low Temperature"]

    @low_temperature.setter
    def low_temperature(self, value=None):
        """  Corresponds to IDD Field `low_temperature`

        Args:
            value (float): value for IDD Field `low_temperature`
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
                                 'for field `low_temperature`'.format(value))

        self._data["Low Temperature"] = value

    @property
    def capacity_at_high_temperature(self):
        """Get capacity_at_high_temperature

        Returns:
            float: the value of `capacity_at_high_temperature` or None if not set
        """
        return self._data["Capacity at High Temperature"]

    @capacity_at_high_temperature.setter
    def capacity_at_high_temperature(self, value=None):
        """  Corresponds to IDD Field `capacity_at_high_temperature`

        Args:
            value (float): value for IDD Field `capacity_at_high_temperature`
                Unit: W
                value >= 0.0
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
                                 'for field `capacity_at_high_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `capacity_at_high_temperature`')

        self._data["Capacity at High Temperature"] = value

    @property
    def high_temperature(self):
        """Get high_temperature

        Returns:
            float: the value of `high_temperature` or None if not set
        """
        return self._data["High Temperature"]

    @high_temperature.setter
    def high_temperature(self, value=None):
        """  Corresponds to IDD Field `high_temperature`

        Args:
            value (float): value for IDD Field `high_temperature`
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
                                 'for field `high_temperature`'.format(value))

        self._data["High Temperature"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_radiant`

        Args:
            value (float): value for IDD Field `fraction_radiant`
                Default value: 0.0
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
                                 'for field `fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_radiant`')

        self._data["Fraction Radiant"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `enduse_subcategory`

        Args:
            value (str): value for IDD Field `enduse_subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')

        self._data["End-Use Subcategory"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.capacity_at_low_temperature))
        out.append(self._to_str(self.low_temperature))
        out.append(self._to_str(self.capacity_at_high_temperature))
        out.append(self._to_str(self.high_temperature))
        out.append(self._to_str(self.fraction_radiant))
        out.append(self._to_str(self.enduse_subcategory))
        return ",".join(out)