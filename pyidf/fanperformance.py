from collections import OrderedDict

class FanPerformanceNightVentilation(object):
    """ Corresponds to IDD object `FanPerformance:NightVentilation`
        Specifies an alternate set of performance parameters for a fan. These alternate
        parameters are used when a system manager (such as AvailabilityManager:NightVentilation)
        sets a specified flow rate.  May be used with any type of fan except not with
        Fan:ComponentModel. If the fan model senses that a fixed flow rate has been set, it
        will use these alternate performance parameters. It is assumed that the fan will
        run at a fixed speed in the alternate mode.
    """
    internal_name = "FanPerformance:NightVentilation"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `FanPerformance:NightVentilation`
        """
        self._data = OrderedDict()
        self._data["Fan Name"] = None
        self._data["Fan Total Efficiency"] = None
        self._data["Pressure Rise"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Motor Efficiency"] = None
        self._data["Motor in Airstream Fraction"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.fan_name = None
        else:
            self.fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_total_efficiency = None
        else:
            self.fan_total_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pressure_rise = None
        else:
            self.pressure_rise = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.motor_in_airstream_fraction = None
        else:
            self.motor_in_airstream_fraction = vals[i]
        i += 1

    @property
    def fan_name(self):
        """Get fan_name

        Returns:
            str: the value of `fan_name` or None if not set
        """
        return self._data["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """  Corresponds to IDD Field `fan_name`

        Args:
            value (str): value for IDD Field `fan_name`
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
                                 'for field `fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_name`')

        self._data["Fan Name"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency

        Returns:
            float: the value of `fan_total_efficiency` or None if not set
        """
        return self._data["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=None):
        """  Corresponds to IDD Field `fan_total_efficiency`

        Args:
            value (float): value for IDD Field `fan_total_efficiency`
                value > 0.0
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
                                 'for field `fan_total_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `fan_total_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fan_total_efficiency`')

        self._data["Fan Total Efficiency"] = value

    @property
    def pressure_rise(self):
        """Get pressure_rise

        Returns:
            float: the value of `pressure_rise` or None if not set
        """
        return self._data["Pressure Rise"]

    @pressure_rise.setter
    def pressure_rise(self, value=None):
        """  Corresponds to IDD Field `pressure_rise`

        Args:
            value (float): value for IDD Field `pressure_rise`
                Unit: Pa
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
                                 'for field `pressure_rise`'.format(value))

        self._data["Pressure Rise"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `maximum_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_flow_rate`
                Unit: m3/s
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
                                 'for field `maximum_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_flow_rate`')

        self._data["Maximum Flow Rate"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency

        Returns:
            float: the value of `motor_efficiency` or None if not set
        """
        return self._data["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=None):
        """  Corresponds to IDD Field `motor_efficiency`

        Args:
            value (float): value for IDD Field `motor_efficiency`
                value > 0.0
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
                                 'for field `motor_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `motor_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_efficiency`')

        self._data["Motor Efficiency"] = value

    @property
    def motor_in_airstream_fraction(self):
        """Get motor_in_airstream_fraction

        Returns:
            float: the value of `motor_in_airstream_fraction` or None if not set
        """
        return self._data["Motor in Airstream Fraction"]

    @motor_in_airstream_fraction.setter
    def motor_in_airstream_fraction(self, value=1.0 ):
        """  Corresponds to IDD Field `motor_in_airstream_fraction`
        0.0 means fan motor outside of airstream
        1.0 means fan motor inside of airstream

        Args:
            value (float): value for IDD Field `motor_in_airstream_fraction`
                Default value: 1.0
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
                                 'for field `motor_in_airstream_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `motor_in_airstream_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_in_airstream_fraction`')

        self._data["Motor in Airstream Fraction"] = value

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
        out.append(self._to_str(self.fan_name))
        out.append(self._to_str(self.fan_total_efficiency))
        out.append(self._to_str(self.pressure_rise))
        out.append(self._to_str(self.maximum_flow_rate))
        out.append(self._to_str(self.motor_efficiency))
        out.append(self._to_str(self.motor_in_airstream_fraction))
        return ",".join(out)