from collections import OrderedDict
import logging
import re

class FanConstantVolume(object):
    """ Corresponds to IDD object `Fan:ConstantVolume`
        Constant volume fan that is intended to operate continuously based on a time schedule.
        This fan will not cycle on and off based on cooling/heating load or other control
        signals.
    """
    internal_name = "Fan:ConstantVolume"
    field_count = 10
    required_fields = ["Name", "Pressure Rise", "Air Inlet Node Name", "Air Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Fan:ConstantVolume`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Fan Total Efficiency"] = None
        self._data["Pressure Rise"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Motor Efficiency"] = None
        self._data["Motor In Airstream Fraction"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["End-Use Subcategory"] = None
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_total_efficiency = None
        else:
            self.fan_total_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pressure_rise = None
        else:
            self.pressure_rise = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_in_airstream_fraction = None
        else:
            self.motor_in_airstream_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency

        Returns:
            float: the value of `fan_total_efficiency` or None if not set
        """
        return self._data["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=0.7):
        """  Corresponds to IDD Field `Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`
                Default value: 0.7
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Pressure Rise`

        Args:
            value (float): value for IDD Field `Pressure Rise`
                Units: Pa
                IP-Units: inH2O
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `maximum_flow_rate`'.format(value))
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
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
    def motor_efficiency(self, value=0.9):
        """  Corresponds to IDD Field `Motor Efficiency`

        Args:
            value (float): value for IDD Field `Motor Efficiency`
                Default value: 0.9
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        return self._data["Motor In Airstream Fraction"]

    @motor_in_airstream_fraction.setter
    def motor_in_airstream_fraction(self, value=1.0):
        """  Corresponds to IDD Field `Motor In Airstream Fraction`
        0.0 means fan motor outside of air stream, 1.0 means motor inside of air stream

        Args:
            value (float): value for IDD Field `Motor In Airstream Fraction`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `motor_in_airstream_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `motor_in_airstream_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_in_airstream_fraction`')
        self._data["Motor In Airstream Fraction"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class FanVariableVolume(object):
    """ Corresponds to IDD object `Fan:VariableVolume`
        Variable air volume fan where the electric power input varies according to a
        performance curve as a function of flow fraction.
    """
    internal_name = "Fan:VariableVolume"
    field_count = 18
    required_fields = ["Name", "Pressure Rise", "Air Inlet Node Name", "Air Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Fan:VariableVolume`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Fan Total Efficiency"] = None
        self._data["Pressure Rise"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Fan Power Minimum Flow Rate Input Method"] = None
        self._data["Fan Power Minimum Flow Fraction"] = None
        self._data["Fan Power Minimum Air Flow Rate"] = None
        self._data["Motor Efficiency"] = None
        self._data["Motor In Airstream Fraction"] = None
        self._data["Fan Power Coefficient 1"] = None
        self._data["Fan Power Coefficient 2"] = None
        self._data["Fan Power Coefficient 3"] = None
        self._data["Fan Power Coefficient 4"] = None
        self._data["Fan Power Coefficient 5"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["End-Use Subcategory"] = None
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_total_efficiency = None
        else:
            self.fan_total_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pressure_rise = None
        else:
            self.pressure_rise = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_minimum_flow_rate_input_method = None
        else:
            self.fan_power_minimum_flow_rate_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_minimum_flow_fraction = None
        else:
            self.fan_power_minimum_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_minimum_air_flow_rate = None
        else:
            self.fan_power_minimum_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_in_airstream_fraction = None
        else:
            self.motor_in_airstream_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_coefficient_1 = None
        else:
            self.fan_power_coefficient_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_coefficient_2 = None
        else:
            self.fan_power_coefficient_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_coefficient_3 = None
        else:
            self.fan_power_coefficient_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_coefficient_4 = None
        else:
            self.fan_power_coefficient_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_coefficient_5 = None
        else:
            self.fan_power_coefficient_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency

        Returns:
            float: the value of `fan_total_efficiency` or None if not set
        """
        return self._data["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=0.7):
        """  Corresponds to IDD Field `Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`
                Default value: 0.7
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Pressure Rise`

        Args:
            value (float): value for IDD Field `Pressure Rise`
                Units: Pa
                IP-Units: inH2O
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `maximum_flow_rate`'.format(value))
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 'for field `maximum_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_flow_rate`')
        self._data["Maximum Flow Rate"] = value

    @property
    def fan_power_minimum_flow_rate_input_method(self):
        """Get fan_power_minimum_flow_rate_input_method

        Returns:
            str: the value of `fan_power_minimum_flow_rate_input_method` or None if not set
        """
        return self._data["Fan Power Minimum Flow Rate Input Method"]

    @fan_power_minimum_flow_rate_input_method.setter
    def fan_power_minimum_flow_rate_input_method(self, value="Fraction"):
        """  Corresponds to IDD Field `Fan Power Minimum Flow Rate Input Method`

        Args:
            value (str): value for IDD Field `Fan Power Minimum Flow Rate Input Method`
                Accepted values are:
                      - Fraction
                      - FixedFlowRate
                Default value: Fraction
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `fan_power_minimum_flow_rate_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_power_minimum_flow_rate_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_power_minimum_flow_rate_input_method`')
            vals = {}
            vals["fraction"] = "Fraction"
            vals["fixedflowrate"] = "FixedFlowRate"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `fan_power_minimum_flow_rate_input_method`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `fan_power_minimum_flow_rate_input_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Fan Power Minimum Flow Rate Input Method"] = value

    @property
    def fan_power_minimum_flow_fraction(self):
        """Get fan_power_minimum_flow_fraction

        Returns:
            float: the value of `fan_power_minimum_flow_fraction` or None if not set
        """
        return self._data["Fan Power Minimum Flow Fraction"]

    @fan_power_minimum_flow_fraction.setter
    def fan_power_minimum_flow_fraction(self, value=0.25):
        """  Corresponds to IDD Field `Fan Power Minimum Flow Fraction`

        Args:
            value (float): value for IDD Field `Fan Power Minimum Flow Fraction`
                Default value: 0.25
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `fan_power_minimum_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fan_power_minimum_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fan_power_minimum_flow_fraction`')
        self._data["Fan Power Minimum Flow Fraction"] = value

    @property
    def fan_power_minimum_air_flow_rate(self):
        """Get fan_power_minimum_air_flow_rate

        Returns:
            float: the value of `fan_power_minimum_air_flow_rate` or None if not set
        """
        return self._data["Fan Power Minimum Air Flow Rate"]

    @fan_power_minimum_air_flow_rate.setter
    def fan_power_minimum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Fan Power Minimum Air Flow Rate`

        Args:
            value (float): value for IDD Field `Fan Power Minimum Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `fan_power_minimum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fan_power_minimum_air_flow_rate`')
        self._data["Fan Power Minimum Air Flow Rate"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency

        Returns:
            float: the value of `motor_efficiency` or None if not set
        """
        return self._data["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=0.9):
        """  Corresponds to IDD Field `Motor Efficiency`

        Args:
            value (float): value for IDD Field `Motor Efficiency`
                Default value: 0.9
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        return self._data["Motor In Airstream Fraction"]

    @motor_in_airstream_fraction.setter
    def motor_in_airstream_fraction(self, value=1.0):
        """  Corresponds to IDD Field `Motor In Airstream Fraction`
        0.0 means fan motor outside of air stream, 1.0 means motor inside of air stream

        Args:
            value (float): value for IDD Field `Motor In Airstream Fraction`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `motor_in_airstream_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `motor_in_airstream_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_in_airstream_fraction`')
        self._data["Motor In Airstream Fraction"] = value

    @property
    def fan_power_coefficient_1(self):
        """Get fan_power_coefficient_1

        Returns:
            float: the value of `fan_power_coefficient_1` or None if not set
        """
        return self._data["Fan Power Coefficient 1"]

    @fan_power_coefficient_1.setter
    def fan_power_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `Fan Power Coefficient 1`
        all Fan Power Coefficients should not be 0.0 or no fan power will be consumed.
        Fan Power Coefficents are specified as function of full flow rate/power
        Equation:

        Args:
            value (float): value for IDD Field `Fan Power Coefficient 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `fan_power_coefficient_1`'.format(value))
        self._data["Fan Power Coefficient 1"] = value

    @property
    def fan_power_coefficient_2(self):
        """Get fan_power_coefficient_2

        Returns:
            float: the value of `fan_power_coefficient_2` or None if not set
        """
        return self._data["Fan Power Coefficient 2"]

    @fan_power_coefficient_2.setter
    def fan_power_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `Fan Power Coefficient 2`

        Args:
            value (float): value for IDD Field `Fan Power Coefficient 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `fan_power_coefficient_2`'.format(value))
        self._data["Fan Power Coefficient 2"] = value

    @property
    def fan_power_coefficient_3(self):
        """Get fan_power_coefficient_3

        Returns:
            float: the value of `fan_power_coefficient_3` or None if not set
        """
        return self._data["Fan Power Coefficient 3"]

    @fan_power_coefficient_3.setter
    def fan_power_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `Fan Power Coefficient 3`

        Args:
            value (float): value for IDD Field `Fan Power Coefficient 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `fan_power_coefficient_3`'.format(value))
        self._data["Fan Power Coefficient 3"] = value

    @property
    def fan_power_coefficient_4(self):
        """Get fan_power_coefficient_4

        Returns:
            float: the value of `fan_power_coefficient_4` or None if not set
        """
        return self._data["Fan Power Coefficient 4"]

    @fan_power_coefficient_4.setter
    def fan_power_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `Fan Power Coefficient 4`

        Args:
            value (float): value for IDD Field `Fan Power Coefficient 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `fan_power_coefficient_4`'.format(value))
        self._data["Fan Power Coefficient 4"] = value

    @property
    def fan_power_coefficient_5(self):
        """Get fan_power_coefficient_5

        Returns:
            float: the value of `fan_power_coefficient_5` or None if not set
        """
        return self._data["Fan Power Coefficient 5"]

    @fan_power_coefficient_5.setter
    def fan_power_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `Fan Power Coefficient 5`

        Args:
            value (float): value for IDD Field `Fan Power Coefficient 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `fan_power_coefficient_5`'.format(value))
        self._data["Fan Power Coefficient 5"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class FanOnOff(object):
    """ Corresponds to IDD object `Fan:OnOff`
        Constant volume fan that is intended to cycle on and off based on cooling/heating load
        or other control signals. This fan can also operate continuously like
        Fan:ConstantVolume.
    """
    internal_name = "Fan:OnOff"
    field_count = 12
    required_fields = ["Name", "Pressure Rise", "Air Inlet Node Name", "Air Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Fan:OnOff`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Fan Total Efficiency"] = None
        self._data["Pressure Rise"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Motor Efficiency"] = None
        self._data["Motor In Airstream Fraction"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Fan Power Ratio Function of Speed Ratio Curve Name"] = None
        self._data["Fan Efficiency Ratio Function of Speed Ratio Curve Name"] = None
        self._data["End-Use Subcategory"] = None
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_total_efficiency = None
        else:
            self.fan_total_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pressure_rise = None
        else:
            self.pressure_rise = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_in_airstream_fraction = None
        else:
            self.motor_in_airstream_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_power_ratio_function_of_speed_ratio_curve_name = None
        else:
            self.fan_power_ratio_function_of_speed_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_efficiency_ratio_function_of_speed_ratio_curve_name = None
        else:
            self.fan_efficiency_ratio_function_of_speed_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency

        Returns:
            float: the value of `fan_total_efficiency` or None if not set
        """
        return self._data["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=0.6):
        """  Corresponds to IDD Field `Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`
                Default value: 0.6
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Pressure Rise`

        Args:
            value (float): value for IDD Field `Pressure Rise`
                Units: Pa
                IP-Units: inH2O
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `maximum_flow_rate`'.format(value))
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
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
    def motor_efficiency(self, value=0.8):
        """  Corresponds to IDD Field `Motor Efficiency`

        Args:
            value (float): value for IDD Field `Motor Efficiency`
                Default value: 0.8
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        return self._data["Motor In Airstream Fraction"]

    @motor_in_airstream_fraction.setter
    def motor_in_airstream_fraction(self, value=1.0):
        """  Corresponds to IDD Field `Motor In Airstream Fraction`
        0.0 means fan motor outside of air stream, 1.0 means motor inside of air stream

        Args:
            value (float): value for IDD Field `Motor In Airstream Fraction`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `motor_in_airstream_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `motor_in_airstream_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_in_airstream_fraction`')
        self._data["Motor In Airstream Fraction"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def fan_power_ratio_function_of_speed_ratio_curve_name(self):
        """Get fan_power_ratio_function_of_speed_ratio_curve_name

        Returns:
            str: the value of `fan_power_ratio_function_of_speed_ratio_curve_name` or None if not set
        """
        return self._data["Fan Power Ratio Function of Speed Ratio Curve Name"]

    @fan_power_ratio_function_of_speed_ratio_curve_name.setter
    def fan_power_ratio_function_of_speed_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `Fan Power Ratio Function of Speed Ratio Curve Name`
        Table:OneIndependentVariable can also be used

        Args:
            value (str): value for IDD Field `Fan Power Ratio Function of Speed Ratio Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `fan_power_ratio_function_of_speed_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_power_ratio_function_of_speed_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_power_ratio_function_of_speed_ratio_curve_name`')
        self._data["Fan Power Ratio Function of Speed Ratio Curve Name"] = value

    @property
    def fan_efficiency_ratio_function_of_speed_ratio_curve_name(self):
        """Get fan_efficiency_ratio_function_of_speed_ratio_curve_name

        Returns:
            str: the value of `fan_efficiency_ratio_function_of_speed_ratio_curve_name` or None if not set
        """
        return self._data["Fan Efficiency Ratio Function of Speed Ratio Curve Name"]

    @fan_efficiency_ratio_function_of_speed_ratio_curve_name.setter
    def fan_efficiency_ratio_function_of_speed_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `Fan Efficiency Ratio Function of Speed Ratio Curve Name`
        Table:OneIndependentVariable can also be used

        Args:
            value (str): value for IDD Field `Fan Efficiency Ratio Function of Speed Ratio Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `fan_efficiency_ratio_function_of_speed_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_efficiency_ratio_function_of_speed_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_efficiency_ratio_function_of_speed_ratio_curve_name`')
        self._data["Fan Efficiency Ratio Function of Speed Ratio Curve Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class FanZoneExhaust(object):
    """ Corresponds to IDD object `Fan:ZoneExhaust`
        Models a fan that exhausts air from a zone.
    """
    internal_name = "Fan:ZoneExhaust"
    field_count = 12
    required_fields = ["Name", "Pressure Rise", "Air Inlet Node Name", "Air Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Fan:ZoneExhaust`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Fan Total Efficiency"] = None
        self._data["Pressure Rise"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Flow Fraction Schedule Name"] = None
        self._data["System Availability Manager Coupling Mode"] = None
        self._data["Minimum Zone Temperature Limit Schedule Name"] = None
        self._data["Balanced Exhaust Fraction Schedule Name"] = None
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_total_efficiency = None
        else:
            self.fan_total_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pressure_rise = None
        else:
            self.pressure_rise = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.flow_fraction_schedule_name = None
        else:
            self.flow_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.system_availability_manager_coupling_mode = None
        else:
            self.system_availability_manager_coupling_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_zone_temperature_limit_schedule_name = None
        else:
            self.minimum_zone_temperature_limit_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.balanced_exhaust_fraction_schedule_name = None
        else:
            self.balanced_exhaust_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency

        Returns:
            float: the value of `fan_total_efficiency` or None if not set
        """
        return self._data["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=0.6):
        """  Corresponds to IDD Field `Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`
                Default value: 0.6
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Pressure Rise`

        Args:
            value (float): value for IDD Field `Pressure Rise`
                Units: Pa
                IP-Units: inH2O
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Maximum Flow Rate`

        Args:
            value (float): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `maximum_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_flow_rate`')
        self._data["Maximum Flow Rate"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    @property
    def flow_fraction_schedule_name(self):
        """Get flow_fraction_schedule_name

        Returns:
            str: the value of `flow_fraction_schedule_name` or None if not set
        """
        return self._data["Flow Fraction Schedule Name"]

    @flow_fraction_schedule_name.setter
    def flow_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Flow Fraction Schedule Name`
        If field is used, then when fan runs the exhausted air flow rate is controlled to be the scheduled fraction times the Maximum Flow Rate

        Args:
            value (str): value for IDD Field `Flow Fraction Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `flow_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `flow_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `flow_fraction_schedule_name`')
        self._data["Flow Fraction Schedule Name"] = value

    @property
    def system_availability_manager_coupling_mode(self):
        """Get system_availability_manager_coupling_mode

        Returns:
            str: the value of `system_availability_manager_coupling_mode` or None if not set
        """
        return self._data["System Availability Manager Coupling Mode"]

    @system_availability_manager_coupling_mode.setter
    def system_availability_manager_coupling_mode(self, value="Coupled"):
        """  Corresponds to IDD Field `System Availability Manager Coupling Mode`
        Control if fan is to be interlocked with HVAC system Availability Managerrs or not.

        Args:
            value (str): value for IDD Field `System Availability Manager Coupling Mode`
                Accepted values are:
                      - Coupled
                      - Decoupled
                Default value: Coupled
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `system_availability_manager_coupling_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `system_availability_manager_coupling_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `system_availability_manager_coupling_mode`')
            vals = {}
            vals["coupled"] = "Coupled"
            vals["decoupled"] = "Decoupled"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `system_availability_manager_coupling_mode`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `system_availability_manager_coupling_mode`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["System Availability Manager Coupling Mode"] = value

    @property
    def minimum_zone_temperature_limit_schedule_name(self):
        """Get minimum_zone_temperature_limit_schedule_name

        Returns:
            str: the value of `minimum_zone_temperature_limit_schedule_name` or None if not set
        """
        return self._data["Minimum Zone Temperature Limit Schedule Name"]

    @minimum_zone_temperature_limit_schedule_name.setter
    def minimum_zone_temperature_limit_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Zone Temperature Limit Schedule Name`
        If field is used, the exhaust fan will not run if the zone temperature is lower than this limit

        Args:
            value (str): value for IDD Field `Minimum Zone Temperature Limit Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `minimum_zone_temperature_limit_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_zone_temperature_limit_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_zone_temperature_limit_schedule_name`')
        self._data["Minimum Zone Temperature Limit Schedule Name"] = value

    @property
    def balanced_exhaust_fraction_schedule_name(self):
        """Get balanced_exhaust_fraction_schedule_name

        Returns:
            str: the value of `balanced_exhaust_fraction_schedule_name` or None if not set
        """
        return self._data["Balanced Exhaust Fraction Schedule Name"]

    @balanced_exhaust_fraction_schedule_name.setter
    def balanced_exhaust_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Balanced Exhaust Fraction Schedule Name`
        Used to control fan's impact on flow at the return air node. Enter the portion of the exhaust that is balanced by simple airflows.
        

        Args:
            value (str): value for IDD Field `Balanced Exhaust Fraction Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `balanced_exhaust_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `balanced_exhaust_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `balanced_exhaust_fraction_schedule_name`')
        self._data["Balanced Exhaust Fraction Schedule Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

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
    required_fields = ["Fan Name", "Fan Total Efficiency", "Pressure Rise", "Motor Efficiency"]

    def __init__(self):
        """ Init data dictionary object for IDD  `FanPerformance:NightVentilation`
        """
        self._data = OrderedDict()
        self._data["Fan Name"] = None
        self._data["Fan Total Efficiency"] = None
        self._data["Pressure Rise"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Motor Efficiency"] = None
        self._data["Motor in Airstream Fraction"] = None
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.fan_name = None
        else:
            self.fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_total_efficiency = None
        else:
            self.fan_total_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pressure_rise = None
        else:
            self.pressure_rise = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_in_airstream_fraction = None
        else:
            self.motor_in_airstream_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def fan_name(self):
        """Get fan_name

        Returns:
            str: the value of `fan_name` or None if not set
        """
        return self._data["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """  Corresponds to IDD Field `Fan Name`

        Args:
            value (str): value for IDD Field `Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Pressure Rise`

        Args:
            value (float): value for IDD Field `Pressure Rise`
                Units: Pa
                IP-Units: inH2O
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `maximum_flow_rate`'.format(value))
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
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
        """  Corresponds to IDD Field `Motor Efficiency`

        Args:
            value (float): value for IDD Field `Motor Efficiency`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
    def motor_in_airstream_fraction(self, value=1.0):
        """  Corresponds to IDD Field `Motor in Airstream Fraction`
        0.0 means fan motor outside of airstream
        1.0 means fan motor inside of airstream

        Args:
            value (float): value for IDD Field `Motor in Airstream Fraction`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `motor_in_airstream_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `motor_in_airstream_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_in_airstream_fraction`')
        self._data["Motor in Airstream Fraction"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class FanComponentModel(object):
    """ Corresponds to IDD object `Fan:ComponentModel`
        A detailed fan type for constant-air-volume (CAV) and variable-air-volume (VAV)
        systems. It includes inputs that describe the air-distribution system as well as the
        fan, drive belt (if used), motor, and variable-frequency-drive (if used).
    """
    internal_name = "Fan:ComponentModel"
    field_count = 37
    required_fields = ["Name", "Air Inlet Node Name", "Air Outlet Node Name", "Fan Wheel Diameter", "Fan Outlet Area", "Maximum Fan Static Efficiency", "Euler Number at Maximum Fan Static Efficiency", "Maximum Dimensionless Fan Airflow", "Belt Maximum Torque", "Motor Maximum Speed", "Maximum Motor Output Power", "Maximum VFD Output Power", "Fan Pressure Rise Curve Name", "Duct Static Pressure Reset Curve Name", "Normalized Fan Static Efficiency Curve Name-Non-Stall Region", "Normalized Fan Static Efficiency Curve Name-Stall Region", "Normalized Dimensionless Airflow Curve Name-Non-Stall Region", "Normalized Dimensionless Airflow Curve Name-Stall Region"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Fan:ComponentModel`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Minimum Flow Rate"] = None
        self._data["Fan Sizing Factor"] = None
        self._data["Fan Wheel Diameter"] = None
        self._data["Fan Outlet Area"] = None
        self._data["Maximum Fan Static Efficiency"] = None
        self._data["Euler Number at Maximum Fan Static Efficiency"] = None
        self._data["Maximum Dimensionless Fan Airflow"] = None
        self._data["Motor Fan Pulley Ratio"] = None
        self._data["Belt Maximum Torque"] = None
        self._data["Belt Sizing Factor"] = None
        self._data["Belt Fractional Torque Transition"] = None
        self._data["Motor Maximum Speed"] = None
        self._data["Maximum Motor Output Power"] = None
        self._data["Motor Sizing Factor"] = None
        self._data["Motor In Airstream Fraction"] = None
        self._data["VFD Efficiency Type"] = None
        self._data["Maximum VFD Output Power"] = None
        self._data["VFD Sizing Factor"] = None
        self._data["Fan Pressure Rise Curve Name"] = None
        self._data["Duct Static Pressure Reset Curve Name"] = None
        self._data["Normalized Fan Static Efficiency Curve Name-Non-Stall Region"] = None
        self._data["Normalized Fan Static Efficiency Curve Name-Stall Region"] = None
        self._data["Normalized Dimensionless Airflow Curve Name-Non-Stall Region"] = None
        self._data["Normalized Dimensionless Airflow Curve Name-Stall Region"] = None
        self._data["Maximum Belt Efficiency Curve Name"] = None
        self._data["Normalized Belt Efficiency Curve Name - Region 1"] = None
        self._data["Normalized Belt Efficiency Curve Name - Region 2"] = None
        self._data["Normalized Belt Efficiency Curve Name - Region 3"] = None
        self._data["Maximum Motor Efficiency Curve Name"] = None
        self._data["Normalized Motor Efficiency Curve Name"] = None
        self._data["VFD Efficiency Curve Name"] = None
        self._data["End-Use Subcategory"] = None
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_flow_rate = None
        else:
            self.minimum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_sizing_factor = None
        else:
            self.fan_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_wheel_diameter = None
        else:
            self.fan_wheel_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_outlet_area = None
        else:
            self.fan_outlet_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_fan_static_efficiency = None
        else:
            self.maximum_fan_static_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.euler_number_at_maximum_fan_static_efficiency = None
        else:
            self.euler_number_at_maximum_fan_static_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_dimensionless_fan_airflow = None
        else:
            self.maximum_dimensionless_fan_airflow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_fan_pulley_ratio = None
        else:
            self.motor_fan_pulley_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.belt_maximum_torque = None
        else:
            self.belt_maximum_torque = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.belt_sizing_factor = None
        else:
            self.belt_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.belt_fractional_torque_transition = None
        else:
            self.belt_fractional_torque_transition = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_maximum_speed = None
        else:
            self.motor_maximum_speed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_motor_output_power = None
        else:
            self.maximum_motor_output_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_sizing_factor = None
        else:
            self.motor_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_in_airstream_fraction = None
        else:
            self.motor_in_airstream_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vfd_efficiency_type = None
        else:
            self.vfd_efficiency_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_vfd_output_power = None
        else:
            self.maximum_vfd_output_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vfd_sizing_factor = None
        else:
            self.vfd_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_pressure_rise_curve_name = None
        else:
            self.fan_pressure_rise_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.duct_static_pressure_reset_curve_name = None
        else:
            self.duct_static_pressure_reset_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.normalized_fan_static_efficiency_curve_namenonstall_region = None
        else:
            self.normalized_fan_static_efficiency_curve_namenonstall_region = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.normalized_fan_static_efficiency_curve_namestall_region = None
        else:
            self.normalized_fan_static_efficiency_curve_namestall_region = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.normalized_dimensionless_airflow_curve_namenonstall_region = None
        else:
            self.normalized_dimensionless_airflow_curve_namenonstall_region = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.normalized_dimensionless_airflow_curve_namestall_region = None
        else:
            self.normalized_dimensionless_airflow_curve_namestall_region = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_belt_efficiency_curve_name = None
        else:
            self.maximum_belt_efficiency_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.normalized_belt_efficiency_curve_name_region_1 = None
        else:
            self.normalized_belt_efficiency_curve_name_region_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.normalized_belt_efficiency_curve_name_region_2 = None
        else:
            self.normalized_belt_efficiency_curve_name_region_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.normalized_belt_efficiency_curve_name_region_3 = None
        else:
            self.normalized_belt_efficiency_curve_name_region_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_motor_efficiency_curve_name = None
        else:
            self.maximum_motor_efficiency_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.normalized_motor_efficiency_curve_name = None
        else:
            self.normalized_motor_efficiency_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vfd_efficiency_curve_name = None
        else:
            self.vfd_efficiency_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `maximum_flow_rate`'.format(value))
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 'for field `maximum_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_flow_rate`')
        self._data["Maximum Flow Rate"] = value

    @property
    def minimum_flow_rate(self):
        """Get minimum_flow_rate

        Returns:
            float: the value of `minimum_flow_rate` or None if not set
        """
        return self._data["Minimum Flow Rate"]

    @minimum_flow_rate.setter
    def minimum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Minimum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Minimum Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `minimum_flow_rate`'.format(value))
                    self._data["Minimum Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 'for field `minimum_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_flow_rate`')
        self._data["Minimum Flow Rate"] = value

    @property
    def fan_sizing_factor(self):
        """Get fan_sizing_factor

        Returns:
            float: the value of `fan_sizing_factor` or None if not set
        """
        return self._data["Fan Sizing Factor"]

    @fan_sizing_factor.setter
    def fan_sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Fan Sizing Factor`
        Applied to specified or autosized max fan airflow

        Args:
            value (float): value for IDD Field `Fan Sizing Factor`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `fan_sizing_factor`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `fan_sizing_factor`')
        self._data["Fan Sizing Factor"] = value

    @property
    def fan_wheel_diameter(self):
        """Get fan_wheel_diameter

        Returns:
            float: the value of `fan_wheel_diameter` or None if not set
        """
        return self._data["Fan Wheel Diameter"]

    @fan_wheel_diameter.setter
    def fan_wheel_diameter(self, value=None):
        """  Corresponds to IDD Field `Fan Wheel Diameter`
        Diameter of wheel outer circumference

        Args:
            value (float): value for IDD Field `Fan Wheel Diameter`
                Units: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `fan_wheel_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `fan_wheel_diameter`')
        self._data["Fan Wheel Diameter"] = value

    @property
    def fan_outlet_area(self):
        """Get fan_outlet_area

        Returns:
            float: the value of `fan_outlet_area` or None if not set
        """
        return self._data["Fan Outlet Area"]

    @fan_outlet_area.setter
    def fan_outlet_area(self, value=None):
        """  Corresponds to IDD Field `Fan Outlet Area`
        Area at fan outlet plane for determining discharge velocity pressure

        Args:
            value (float): value for IDD Field `Fan Outlet Area`
                Units: m2
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `fan_outlet_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `fan_outlet_area`')
        self._data["Fan Outlet Area"] = value

    @property
    def maximum_fan_static_efficiency(self):
        """Get maximum_fan_static_efficiency

        Returns:
            float: the value of `maximum_fan_static_efficiency` or None if not set
        """
        return self._data["Maximum Fan Static Efficiency"]

    @maximum_fan_static_efficiency.setter
    def maximum_fan_static_efficiency(self, value=None):
        """  Corresponds to IDD Field `Maximum Fan Static Efficiency`
        Maximum ratio between power delivered to air and fan shaft input power
        Determined from fan performance data

        Args:
            value (float): value for IDD Field `Maximum Fan Static Efficiency`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `maximum_fan_static_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_fan_static_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_fan_static_efficiency`')
        self._data["Maximum Fan Static Efficiency"] = value

    @property
    def euler_number_at_maximum_fan_static_efficiency(self):
        """Get euler_number_at_maximum_fan_static_efficiency

        Returns:
            float: the value of `euler_number_at_maximum_fan_static_efficiency` or None if not set
        """
        return self._data["Euler Number at Maximum Fan Static Efficiency"]

    @euler_number_at_maximum_fan_static_efficiency.setter
    def euler_number_at_maximum_fan_static_efficiency(self, value=None):
        """  Corresponds to IDD Field `Euler Number at Maximum Fan Static Efficiency`
        Euler number (Eu) determined from fan performance data

        Args:
            value (float): value for IDD Field `Euler Number at Maximum Fan Static Efficiency`
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `euler_number_at_maximum_fan_static_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `euler_number_at_maximum_fan_static_efficiency`')
        self._data["Euler Number at Maximum Fan Static Efficiency"] = value

    @property
    def maximum_dimensionless_fan_airflow(self):
        """Get maximum_dimensionless_fan_airflow

        Returns:
            float: the value of `maximum_dimensionless_fan_airflow` or None if not set
        """
        return self._data["Maximum Dimensionless Fan Airflow"]

    @maximum_dimensionless_fan_airflow.setter
    def maximum_dimensionless_fan_airflow(self, value=None):
        """  Corresponds to IDD Field `Maximum Dimensionless Fan Airflow`
        Corresponds to maximum ratio between fan airflow and
        fan shaft rotational speed for specified fan wheel diameter
        Determined from fan performance data

        Args:
            value (float): value for IDD Field `Maximum Dimensionless Fan Airflow`
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `maximum_dimensionless_fan_airflow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_dimensionless_fan_airflow`')
        self._data["Maximum Dimensionless Fan Airflow"] = value

    @property
    def motor_fan_pulley_ratio(self):
        """Get motor_fan_pulley_ratio

        Returns:
            float: the value of `motor_fan_pulley_ratio` or None if not set
        """
        return self._data["Motor Fan Pulley Ratio"]

    @motor_fan_pulley_ratio.setter
    def motor_fan_pulley_ratio(self, value=1.0):
        """  Corresponds to IDD Field `Motor Fan Pulley Ratio`
        Ratio of motor pulley diameter to fan pulley diameter

        Args:
            value (float or "Autosize"): value for IDD Field `Motor Fan Pulley Ratio`
                Default value: 1.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Motor Fan Pulley Ratio"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `motor_fan_pulley_ratio`'.format(value))
                    self._data["Motor Fan Pulley Ratio"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 'for field `motor_fan_pulley_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `motor_fan_pulley_ratio`')
        self._data["Motor Fan Pulley Ratio"] = value

    @property
    def belt_maximum_torque(self):
        """Get belt_maximum_torque

        Returns:
            float: the value of `belt_maximum_torque` or None if not set
        """
        return self._data["Belt Maximum Torque"]

    @belt_maximum_torque.setter
    def belt_maximum_torque(self, value=None):
        """  Corresponds to IDD Field `Belt Maximum Torque`
        Maximum torque transmitted by belt

        Args:
            value (float or "Autosize"): value for IDD Field `Belt Maximum Torque`
                Units: N-m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Belt Maximum Torque"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `belt_maximum_torque`'.format(value))
                    self._data["Belt Maximum Torque"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 'for field `belt_maximum_torque`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `belt_maximum_torque`')
        self._data["Belt Maximum Torque"] = value

    @property
    def belt_sizing_factor(self):
        """Get belt_sizing_factor

        Returns:
            float: the value of `belt_sizing_factor` or None if not set
        """
        return self._data["Belt Sizing Factor"]

    @belt_sizing_factor.setter
    def belt_sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Belt Sizing Factor`
        Applied to specified or autosized max torque transmitted by belt

        Args:
            value (float): value for IDD Field `Belt Sizing Factor`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `belt_sizing_factor`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `belt_sizing_factor`')
        self._data["Belt Sizing Factor"] = value

    @property
    def belt_fractional_torque_transition(self):
        """Get belt_fractional_torque_transition

        Returns:
            float: the value of `belt_fractional_torque_transition` or None if not set
        """
        return self._data["Belt Fractional Torque Transition"]

    @belt_fractional_torque_transition.setter
    def belt_fractional_torque_transition(self, value=0.167):
        """  Corresponds to IDD Field `Belt Fractional Torque Transition`
        Region 1 to 2 curve transition for belt normalized efficiency

        Args:
            value (float): value for IDD Field `Belt Fractional Torque Transition`
                Default value: 0.167
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `belt_fractional_torque_transition`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `belt_fractional_torque_transition`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `belt_fractional_torque_transition`')
        self._data["Belt Fractional Torque Transition"] = value

    @property
    def motor_maximum_speed(self):
        """Get motor_maximum_speed

        Returns:
            float: the value of `motor_maximum_speed` or None if not set
        """
        return self._data["Motor Maximum Speed"]

    @motor_maximum_speed.setter
    def motor_maximum_speed(self, value=None):
        """  Corresponds to IDD Field `Motor Maximum Speed`
        Maximum rotational speed of fan motor shaft

        Args:
            value (float): value for IDD Field `Motor Maximum Speed`
                Units: rev/min
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `motor_maximum_speed`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `motor_maximum_speed`')
        self._data["Motor Maximum Speed"] = value

    @property
    def maximum_motor_output_power(self):
        """Get maximum_motor_output_power

        Returns:
            float: the value of `maximum_motor_output_power` or None if not set
        """
        return self._data["Maximum Motor Output Power"]

    @maximum_motor_output_power.setter
    def maximum_motor_output_power(self, value=None):
        """  Corresponds to IDD Field `Maximum Motor Output Power`
        Maximum power input to drive belt by motor

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Motor Output Power`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Motor Output Power"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `maximum_motor_output_power`'.format(value))
                    self._data["Maximum Motor Output Power"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 'for field `maximum_motor_output_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_motor_output_power`')
        self._data["Maximum Motor Output Power"] = value

    @property
    def motor_sizing_factor(self):
        """Get motor_sizing_factor

        Returns:
            float: the value of `motor_sizing_factor` or None if not set
        """
        return self._data["Motor Sizing Factor"]

    @motor_sizing_factor.setter
    def motor_sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Motor Sizing Factor`
        Applied to specified or autosized motor output power

        Args:
            value (float): value for IDD Field `Motor Sizing Factor`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `motor_sizing_factor`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `motor_sizing_factor`')
        self._data["Motor Sizing Factor"] = value

    @property
    def motor_in_airstream_fraction(self):
        """Get motor_in_airstream_fraction

        Returns:
            float: the value of `motor_in_airstream_fraction` or None if not set
        """
        return self._data["Motor In Airstream Fraction"]

    @motor_in_airstream_fraction.setter
    def motor_in_airstream_fraction(self, value=1.0):
        """  Corresponds to IDD Field `Motor In Airstream Fraction`
        0.0 means motor outside air stream
        1.0 means motor inside air stream

        Args:
            value (float): value for IDD Field `Motor In Airstream Fraction`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `motor_in_airstream_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `motor_in_airstream_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_in_airstream_fraction`')
        self._data["Motor In Airstream Fraction"] = value

    @property
    def vfd_efficiency_type(self):
        """Get vfd_efficiency_type

        Returns:
            str: the value of `vfd_efficiency_type` or None if not set
        """
        return self._data["VFD Efficiency Type"]

    @vfd_efficiency_type.setter
    def vfd_efficiency_type(self, value=None):
        """  Corresponds to IDD Field `VFD Efficiency Type`
        Efficiency depends on fraction of full-load motor speed
        Efficiency depends on  fraction of full-load motor input power
        If field blank, then assumes constant VFD efficiency (0.97)

        Args:
            value (str): value for IDD Field `VFD Efficiency Type`
                Accepted values are:
                      - Speed
                      - Power
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `vfd_efficiency_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `vfd_efficiency_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `vfd_efficiency_type`')
            vals = {}
            vals["speed"] = "Speed"
            vals["power"] = "Power"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `vfd_efficiency_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `vfd_efficiency_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["VFD Efficiency Type"] = value

    @property
    def maximum_vfd_output_power(self):
        """Get maximum_vfd_output_power

        Returns:
            float: the value of `maximum_vfd_output_power` or None if not set
        """
        return self._data["Maximum VFD Output Power"]

    @maximum_vfd_output_power.setter
    def maximum_vfd_output_power(self, value=None):
        """  Corresponds to IDD Field `Maximum VFD Output Power`
        Maximum power input to motor by VFD

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum VFD Output Power`
                Units: W
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum VFD Output Power"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `maximum_vfd_output_power`'.format(value))
                    self._data["Maximum VFD Output Power"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 'for field `maximum_vfd_output_power`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_vfd_output_power`')
        self._data["Maximum VFD Output Power"] = value

    @property
    def vfd_sizing_factor(self):
        """Get vfd_sizing_factor

        Returns:
            float: the value of `vfd_sizing_factor` or None if not set
        """
        return self._data["VFD Sizing Factor"]

    @vfd_sizing_factor.setter
    def vfd_sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `VFD Sizing Factor`
        Applied to specified or autosized VFD output power

        Args:
            value (float): value for IDD Field `VFD Sizing Factor`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `vfd_sizing_factor`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `vfd_sizing_factor`')
        self._data["VFD Sizing Factor"] = value

    @property
    def fan_pressure_rise_curve_name(self):
        """Get fan_pressure_rise_curve_name

        Returns:
            str: the value of `fan_pressure_rise_curve_name` or None if not set
        """
        return self._data["Fan Pressure Rise Curve Name"]

    @fan_pressure_rise_curve_name.setter
    def fan_pressure_rise_curve_name(self, value=None):
        """  Corresponds to IDD Field `Fan Pressure Rise Curve Name`
        Table:OneIndependentVariable object can also be used
        Pressure rise depends on volumetric flow, system resistances,
        system leakage, and duct static pressure set point

        Args:
            value (str): value for IDD Field `Fan Pressure Rise Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `fan_pressure_rise_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_pressure_rise_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_pressure_rise_curve_name`')
        self._data["Fan Pressure Rise Curve Name"] = value

    @property
    def duct_static_pressure_reset_curve_name(self):
        """Get duct_static_pressure_reset_curve_name

        Returns:
            str: the value of `duct_static_pressure_reset_curve_name` or None if not set
        """
        return self._data["Duct Static Pressure Reset Curve Name"]

    @duct_static_pressure_reset_curve_name.setter
    def duct_static_pressure_reset_curve_name(self, value=None):
        """  Corresponds to IDD Field `Duct Static Pressure Reset Curve Name`
        Table:OneIndependentVariable object can also be used
        Function of fan volumetric flow
        Minimum and maximum fan airflows correspond respectively to
        minimum and maximum duct static pressure set points

        Args:
            value (str): value for IDD Field `Duct Static Pressure Reset Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `duct_static_pressure_reset_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `duct_static_pressure_reset_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `duct_static_pressure_reset_curve_name`')
        self._data["Duct Static Pressure Reset Curve Name"] = value

    @property
    def normalized_fan_static_efficiency_curve_namenonstall_region(self):
        """Get normalized_fan_static_efficiency_curve_namenonstall_region

        Returns:
            str: the value of `normalized_fan_static_efficiency_curve_namenonstall_region` or None if not set
        """
        return self._data["Normalized Fan Static Efficiency Curve Name-Non-Stall Region"]

    @normalized_fan_static_efficiency_curve_namenonstall_region.setter
    def normalized_fan_static_efficiency_curve_namenonstall_region(self, value=None):
        """  Corresponds to IDD Field `Normalized Fan Static Efficiency Curve Name-Non-Stall Region`
        Table:OneIndependentVariable object can also be used
        xfan <= 0
        Curve should have maximum of 1.0

        Args:
            value (str): value for IDD Field `Normalized Fan Static Efficiency Curve Name-Non-Stall Region`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `normalized_fan_static_efficiency_curve_namenonstall_region`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `normalized_fan_static_efficiency_curve_namenonstall_region`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `normalized_fan_static_efficiency_curve_namenonstall_region`')
        self._data["Normalized Fan Static Efficiency Curve Name-Non-Stall Region"] = value

    @property
    def normalized_fan_static_efficiency_curve_namestall_region(self):
        """Get normalized_fan_static_efficiency_curve_namestall_region

        Returns:
            str: the value of `normalized_fan_static_efficiency_curve_namestall_region` or None if not set
        """
        return self._data["Normalized Fan Static Efficiency Curve Name-Stall Region"]

    @normalized_fan_static_efficiency_curve_namestall_region.setter
    def normalized_fan_static_efficiency_curve_namestall_region(self, value=None):
        """  Corresponds to IDD Field `Normalized Fan Static Efficiency Curve Name-Stall Region`
        Table:OneIndependentVariable object can also be used
        xfan > 0
        Curve should have maximum of 1.0

        Args:
            value (str): value for IDD Field `Normalized Fan Static Efficiency Curve Name-Stall Region`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `normalized_fan_static_efficiency_curve_namestall_region`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `normalized_fan_static_efficiency_curve_namestall_region`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `normalized_fan_static_efficiency_curve_namestall_region`')
        self._data["Normalized Fan Static Efficiency Curve Name-Stall Region"] = value

    @property
    def normalized_dimensionless_airflow_curve_namenonstall_region(self):
        """Get normalized_dimensionless_airflow_curve_namenonstall_region

        Returns:
            str: the value of `normalized_dimensionless_airflow_curve_namenonstall_region` or None if not set
        """
        return self._data["Normalized Dimensionless Airflow Curve Name-Non-Stall Region"]

    @normalized_dimensionless_airflow_curve_namenonstall_region.setter
    def normalized_dimensionless_airflow_curve_namenonstall_region(self, value=None):
        """  Corresponds to IDD Field `Normalized Dimensionless Airflow Curve Name-Non-Stall Region`
        Table:OneIndependentVariable object can also be used
        xspd <= 0
        Curve should have maximum of 1.0

        Args:
            value (str): value for IDD Field `Normalized Dimensionless Airflow Curve Name-Non-Stall Region`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `normalized_dimensionless_airflow_curve_namenonstall_region`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `normalized_dimensionless_airflow_curve_namenonstall_region`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `normalized_dimensionless_airflow_curve_namenonstall_region`')
        self._data["Normalized Dimensionless Airflow Curve Name-Non-Stall Region"] = value

    @property
    def normalized_dimensionless_airflow_curve_namestall_region(self):
        """Get normalized_dimensionless_airflow_curve_namestall_region

        Returns:
            str: the value of `normalized_dimensionless_airflow_curve_namestall_region` or None if not set
        """
        return self._data["Normalized Dimensionless Airflow Curve Name-Stall Region"]

    @normalized_dimensionless_airflow_curve_namestall_region.setter
    def normalized_dimensionless_airflow_curve_namestall_region(self, value=None):
        """  Corresponds to IDD Field `Normalized Dimensionless Airflow Curve Name-Stall Region`
        Table:OneIndependentVariable object can also be used
        xspd > 0
        Curve should have maximum of 1.0

        Args:
            value (str): value for IDD Field `Normalized Dimensionless Airflow Curve Name-Stall Region`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `normalized_dimensionless_airflow_curve_namestall_region`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `normalized_dimensionless_airflow_curve_namestall_region`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `normalized_dimensionless_airflow_curve_namestall_region`')
        self._data["Normalized Dimensionless Airflow Curve Name-Stall Region"] = value

    @property
    def maximum_belt_efficiency_curve_name(self):
        """Get maximum_belt_efficiency_curve_name

        Returns:
            str: the value of `maximum_belt_efficiency_curve_name` or None if not set
        """
        return self._data["Maximum Belt Efficiency Curve Name"]

    @maximum_belt_efficiency_curve_name.setter
    def maximum_belt_efficiency_curve_name(self, value=None):
        """  Corresponds to IDD Field `Maximum Belt Efficiency Curve Name`
        Table:OneIndependentVariable object can also be used
        Determines maximum fan drive belt efficiency in log space
        as function of xbelt,max
        Curve should have minimum of -4.6 and maximum of 0.0
        If field blank, assumes output of curve is always 1.0

        Args:
            value (str): value for IDD Field `Maximum Belt Efficiency Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `maximum_belt_efficiency_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_belt_efficiency_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `maximum_belt_efficiency_curve_name`')
        self._data["Maximum Belt Efficiency Curve Name"] = value

    @property
    def normalized_belt_efficiency_curve_name_region_1(self):
        """Get normalized_belt_efficiency_curve_name_region_1

        Returns:
            str: the value of `normalized_belt_efficiency_curve_name_region_1` or None if not set
        """
        return self._data["Normalized Belt Efficiency Curve Name - Region 1"]

    @normalized_belt_efficiency_curve_name_region_1.setter
    def normalized_belt_efficiency_curve_name_region_1(self, value=None):
        """  Corresponds to IDD Field `Normalized Belt Efficiency Curve Name - Region 1`
        Table:OneIndependentVariable object can also be used
        Region 1 (0 <= xbelt < xbelt,trans)
        Curve should have minimum > 0.0 and maximum of 1.0
        If field blank, assumes output of curve is always 1.0 in Region 1

        Args:
            value (str): value for IDD Field `Normalized Belt Efficiency Curve Name - Region 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `normalized_belt_efficiency_curve_name_region_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `normalized_belt_efficiency_curve_name_region_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `normalized_belt_efficiency_curve_name_region_1`')
        self._data["Normalized Belt Efficiency Curve Name - Region 1"] = value

    @property
    def normalized_belt_efficiency_curve_name_region_2(self):
        """Get normalized_belt_efficiency_curve_name_region_2

        Returns:
            str: the value of `normalized_belt_efficiency_curve_name_region_2` or None if not set
        """
        return self._data["Normalized Belt Efficiency Curve Name - Region 2"]

    @normalized_belt_efficiency_curve_name_region_2.setter
    def normalized_belt_efficiency_curve_name_region_2(self, value=None):
        """  Corresponds to IDD Field `Normalized Belt Efficiency Curve Name - Region 2`
        Table:OneIndependentVariable object can also be used
        Region 2 (xbelt,trans <= xbelt <= 1)
        Curve should have minimum > 0.0 and maximum of 1.0
        If field blank, assumes output of curve is always 1.0 in Region 2

        Args:
            value (str): value for IDD Field `Normalized Belt Efficiency Curve Name - Region 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `normalized_belt_efficiency_curve_name_region_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `normalized_belt_efficiency_curve_name_region_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `normalized_belt_efficiency_curve_name_region_2`')
        self._data["Normalized Belt Efficiency Curve Name - Region 2"] = value

    @property
    def normalized_belt_efficiency_curve_name_region_3(self):
        """Get normalized_belt_efficiency_curve_name_region_3

        Returns:
            str: the value of `normalized_belt_efficiency_curve_name_region_3` or None if not set
        """
        return self._data["Normalized Belt Efficiency Curve Name - Region 3"]

    @normalized_belt_efficiency_curve_name_region_3.setter
    def normalized_belt_efficiency_curve_name_region_3(self, value=None):
        """  Corresponds to IDD Field `Normalized Belt Efficiency Curve Name - Region 3`
        Table:OneIndependentVariable object can also be used
        Determines normalized drive belt efficiency Region 3 (xbelt > 1)
        Curve should have minimum > 0.0 and maximum of 1.0
        If field blank, assumes output of curve is always 1.0 in Region 3

        Args:
            value (str): value for IDD Field `Normalized Belt Efficiency Curve Name - Region 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `normalized_belt_efficiency_curve_name_region_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `normalized_belt_efficiency_curve_name_region_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `normalized_belt_efficiency_curve_name_region_3`')
        self._data["Normalized Belt Efficiency Curve Name - Region 3"] = value

    @property
    def maximum_motor_efficiency_curve_name(self):
        """Get maximum_motor_efficiency_curve_name

        Returns:
            str: the value of `maximum_motor_efficiency_curve_name` or None if not set
        """
        return self._data["Maximum Motor Efficiency Curve Name"]

    @maximum_motor_efficiency_curve_name.setter
    def maximum_motor_efficiency_curve_name(self, value=None):
        """  Corresponds to IDD Field `Maximum Motor Efficiency Curve Name`
        Table:OneIndependentVariable object can also be used
        Curve should have minimum > 0.0 and maximum of 1.0
        If field blank, assumes output of curve is always 1.0

        Args:
            value (str): value for IDD Field `Maximum Motor Efficiency Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `maximum_motor_efficiency_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_motor_efficiency_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `maximum_motor_efficiency_curve_name`')
        self._data["Maximum Motor Efficiency Curve Name"] = value

    @property
    def normalized_motor_efficiency_curve_name(self):
        """Get normalized_motor_efficiency_curve_name

        Returns:
            str: the value of `normalized_motor_efficiency_curve_name` or None if not set
        """
        return self._data["Normalized Motor Efficiency Curve Name"]

    @normalized_motor_efficiency_curve_name.setter
    def normalized_motor_efficiency_curve_name(self, value=None):
        """  Corresponds to IDD Field `Normalized Motor Efficiency Curve Name`
        Table:OneIndependentVariable object can also be used
        Curve should have minimum > 0.0 and maximum of 1.0
        If field blank, assumes output of curve is always 1.0

        Args:
            value (str): value for IDD Field `Normalized Motor Efficiency Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `normalized_motor_efficiency_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `normalized_motor_efficiency_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `normalized_motor_efficiency_curve_name`')
        self._data["Normalized Motor Efficiency Curve Name"] = value

    @property
    def vfd_efficiency_curve_name(self):
        """Get vfd_efficiency_curve_name

        Returns:
            str: the value of `vfd_efficiency_curve_name` or None if not set
        """
        return self._data["VFD Efficiency Curve Name"]

    @vfd_efficiency_curve_name.setter
    def vfd_efficiency_curve_name(self, value=None):
        """  Corresponds to IDD Field `VFD Efficiency Curve Name`
        Table:OneIndependentVariable object can also be used
        Determines VFD efficiency as function of motor load or speed fraction
        Curve should have minimum > 0.0 and maximum of 1.0
        If field blank, assumes constant VFD efficiency (0.97)

        Args:
            value (str): value for IDD Field `VFD Efficiency Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `vfd_efficiency_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `vfd_efficiency_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `vfd_efficiency_curve_name`')
        self._data["VFD Efficiency Curve Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])