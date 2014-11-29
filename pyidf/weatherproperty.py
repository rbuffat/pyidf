from collections import OrderedDict

class WeatherPropertySkyTemperature(object):
    """ Corresponds to IDD object `WeatherProperty:SkyTemperature`
        This object is used to override internal sky temperature calculations.
    """
    internal_name = "WeatherProperty:SkyTemperature"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WeatherProperty:SkyTemperature`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Calculation Type"] = None
        self._data["Schedule Name"] = None

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
            self.calculation_type = None
        else:
            self.calculation_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
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
        blank in this field will apply to all run periods (that is, all objects=
        SizingPeriod:WeatherFileDays, SizingPeriod:WeatherFileConditionType or RunPeriod
        otherwise, this name must match one of the environment object names.

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
    def calculation_type(self):
        """Get calculation_type

        Returns:
            str: the value of `calculation_type` or None if not set
        """
        return self._data["Calculation Type"]

    @calculation_type.setter
    def calculation_type(self, value=None):
        """  Corresponds to IDD Field `calculation_type`

        Args:
            value (str): value for IDD Field `calculation_type`
                Accepted values are:
                      - ScheduleValue
                      - DifferenceScheduleDryBulbValue
                      - DifferenceScheduleDewPointValue
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `calculation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `calculation_type`')
            vals = set()
            vals.add("ScheduleValue")
            vals.add("DifferenceScheduleDryBulbValue")
            vals.add("DifferenceScheduleDewPointValue")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `calculation_type`'.format(value))

        self._data["Calculation Type"] = value

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
        if name matches a SizingPeriod:DesignDay, put in a day schedule of this name
        if name is for a SizingPeriod:WeatherFileDays, SizingPeriod:WeatherFileConditionType or
        RunPeriod, put in a full year schedule that covers the appropriate days.

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
        out.append(self._to_str(self.calculation_type))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)