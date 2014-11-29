from collections import OrderedDict

class ScheduleTypeLimits(object):
    """ Corresponds to IDD object `ScheduleTypeLimits`
        ScheduleTypeLimits specifies the data types and limits for the values contained in schedules
    """
    internal_name = "ScheduleTypeLimits"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ScheduleTypeLimits`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Lower Limit Value"] = None
        self._data["Upper Limit Value"] = None
        self._data["Numeric Type"] = None
        self._data["Unit Type"] = None

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
            self.lower_limit_value = None
        else:
            self.lower_limit_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.upper_limit_value = None
        else:
            self.upper_limit_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.numeric_type = None
        else:
            self.numeric_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.unit_type = None
        else:
            self.unit_type = vals[i]
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
        used to validate schedule types in various schedule objects

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
    def lower_limit_value(self):
        """Get lower_limit_value

        Returns:
            float: the value of `lower_limit_value` or None if not set
        """
        return self._data["Lower Limit Value"]

    @lower_limit_value.setter
    def lower_limit_value(self, value=None):
        """  Corresponds to IDD Field `lower_limit_value`
        lower limit (real or integer) for the Schedule Type.  e.g. if fraction, this is 0.0

        Args:
            value (float): value for IDD Field `lower_limit_value`
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
                                 'for field `lower_limit_value`'.format(value))

        self._data["Lower Limit Value"] = value

    @property
    def upper_limit_value(self):
        """Get upper_limit_value

        Returns:
            float: the value of `upper_limit_value` or None if not set
        """
        return self._data["Upper Limit Value"]

    @upper_limit_value.setter
    def upper_limit_value(self, value=None):
        """  Corresponds to IDD Field `upper_limit_value`
        upper limit (real or integer) for the Schedule Type.  e.g. if fraction, this is 1.0

        Args:
            value (float): value for IDD Field `upper_limit_value`
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
                                 'for field `upper_limit_value`'.format(value))

        self._data["Upper Limit Value"] = value

    @property
    def numeric_type(self):
        """Get numeric_type

        Returns:
            str: the value of `numeric_type` or None if not set
        """
        return self._data["Numeric Type"]

    @numeric_type.setter
    def numeric_type(self, value=None):
        """  Corresponds to IDD Field `numeric_type`
        Numeric type is either Continuous (all numbers within the min and
        max are valid or Discrete (only integer numbers between min and
        max are valid.  (Could also allow REAL and INTEGER to mean the
        same things)

        Args:
            value (str): value for IDD Field `numeric_type`
                Accepted values are:
                      - Continuous
                      - Discrete
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
                                 'for field `numeric_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `numeric_type`')
            vals = set()
            vals.add("Continuous")
            vals.add("Discrete")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `numeric_type`'.format(value))

        self._data["Numeric Type"] = value

    @property
    def unit_type(self):
        """Get unit_type

        Returns:
            str: the value of `unit_type` or None if not set
        """
        return self._data["Unit Type"]

    @unit_type.setter
    def unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `unit_type`
        Temperature (C or F)
        DeltaTemperature (C or F)
        PrecipitationRate (m/hr or ft/hr)
        Angle (degrees)
        Convection Coefficient (W/m2-K or Btu/sqft-hr-F)
        Activity Level (W/person)
        Velocity (m/s or ft/min)
        Capacity (W or Btu/h)
        Power (W)

        Args:
            value (str): value for IDD Field `unit_type`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - DeltaTemperature
                      - PrecipitationRate
                      - Angle
                      - ConvectionCoefficient
                      - ActivityLevel
                      - Velocity
                      - Capacity
                      - Power
                      - Availability
                      - Percent
                      - Control
                      - Mode
                Default value: Dimensionless
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
                                 'for field `unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `unit_type`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Temperature")
            vals.add("DeltaTemperature")
            vals.add("PrecipitationRate")
            vals.add("Angle")
            vals.add("ConvectionCoefficient")
            vals.add("ActivityLevel")
            vals.add("Velocity")
            vals.add("Capacity")
            vals.add("Power")
            vals.add("Availability")
            vals.add("Percent")
            vals.add("Control")
            vals.add("Mode")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `unit_type`'.format(value))

        self._data["Unit Type"] = value

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
        out.append(self._to_str(self.lower_limit_value))
        out.append(self._to_str(self.upper_limit_value))
        out.append(self._to_str(self.numeric_type))
        out.append(self._to_str(self.unit_type))
        return ",".join(out)