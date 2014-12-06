""" Data objects in group "Fans"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class FanConstantVolume(DataObject):

    """ Corresponds to IDD object `Fan:ConstantVolume`
        Constant volume fan that is intended to operate continuously based on a time schedule.
        This fan will not cycle on and off based on cooling/heating load or other control
        signals.
    """
    schema = {'min-fields': 9,
              'name': u'Fan:ConstantVolume',
              'pyname': u'FanConstantVolume',
              'format': None,
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'availability schedule name',
                                      {'name': u'Availability Schedule Name',
                                       'pyname': u'availability_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'fan total efficiency',
                                      {'name': u'Fan Total Efficiency',
                                       'pyname': u'fan_total_efficiency',
                                       'default': 0.7,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'pressure rise',
                                      {'name': u'Pressure Rise',
                                       'pyname': u'pressure_rise',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'Pa'}),
                                     (u'maximum flow rate',
                                      {'name': u'Maximum Flow Rate',
                                       'pyname': u'maximum_flow_rate',
                                       'required-field': False,
                                       'autosizable': True,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'm3/s'}),
                                     (u'motor efficiency',
                                      {'name': u'Motor Efficiency',
                                       'pyname': u'motor_efficiency',
                                       'default': 0.9,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'motor in airstream fraction',
                                      {'name': u'Motor In Airstream Fraction',
                                       'pyname': u'motor_in_airstream_fraction',
                                       'default': 1.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'air inlet node name',
                                      {'name': u'Air Inlet Node Name',
                                       'pyname': u'air_inlet_node_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'node'}),
                                     (u'air outlet node name',
                                      {'name': u'Air Outlet Node Name',
                                       'pyname': u'air_outlet_node_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'node'}),
                                     (u'end-use subcategory',
                                      {'name': u'End-Use Subcategory',
                                       'pyname': u'enduse_subcategory',
                                       'default': u'General',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'})]),
              'extensible-fields': OrderedDict(),
              'unique-object': False,
              'required-object': False,
              'group': u'Fans'}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name.

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name` Availability
        schedule name for this system. Schedule value > 0 means the system is
        available. If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Availability Schedule Name"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency.

        Returns:
            float: the value of `fan_total_efficiency` or None if not set

        """
        return self["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=0.7):
        """Corresponds to IDD field `Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`
                Default value: 0.7
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Total Efficiency"] = value

    @property
    def pressure_rise(self):
        """Get pressure_rise.

        Returns:
            float: the value of `pressure_rise` or None if not set

        """
        return self["Pressure Rise"]

    @pressure_rise.setter
    def pressure_rise(self, value=None):
        """Corresponds to IDD field `Pressure Rise`

        Args:
            value (float): value for IDD Field `Pressure Rise`
                Units: Pa
                IP-Units: inH2O
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Pressure Rise"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate.

        Returns:
            float: the value of `maximum_flow_rate` or None if not set

        """
        return self["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Flow Rate"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency.

        Returns:
            float: the value of `motor_efficiency` or None if not set

        """
        return self["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=0.9):
        """Corresponds to IDD field `Motor Efficiency`

        Args:
            value (float): value for IDD Field `Motor Efficiency`
                Default value: 0.9
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Motor Efficiency"] = value

    @property
    def motor_in_airstream_fraction(self):
        """Get motor_in_airstream_fraction.

        Returns:
            float: the value of `motor_in_airstream_fraction` or None if not set

        """
        return self["Motor In Airstream Fraction"]

    @motor_in_airstream_fraction.setter
    def motor_in_airstream_fraction(self, value=1.0):
        """  Corresponds to IDD field `Motor In Airstream Fraction`
        0.0 means fan motor outside of air stream, 1.0 means motor inside of air stream

        Args:
            value (float): value for IDD Field `Motor In Airstream Fraction`
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Motor In Airstream Fraction"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name.

        Returns:
            str: the value of `air_inlet_node_name` or None if not set

        """
        return self["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name.

        Returns:
            str: the value of `air_outlet_node_name` or None if not set

        """
        return self["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Outlet Node Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory.

        Returns:
            str: the value of `enduse_subcategory` or None if not set

        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["End-Use Subcategory"] = value




class FanVariableVolume(DataObject):

    """ Corresponds to IDD object `Fan:VariableVolume`
        Variable air volume fan where the electric power input varies according to a
        performance curve as a function of flow fraction.
    """
    schema = {'min-fields': 17,
              'name': u'Fan:VariableVolume',
              'pyname': u'FanVariableVolume',
              'format': None,
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'availability schedule name',
                                      {'name': u'Availability Schedule Name',
                                       'pyname': u'availability_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'fan total efficiency',
                                      {'name': u'Fan Total Efficiency',
                                       'pyname': u'fan_total_efficiency',
                                       'default': 0.7,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'pressure rise',
                                      {'name': u'Pressure Rise',
                                       'pyname': u'pressure_rise',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'Pa'}),
                                     (u'maximum flow rate',
                                      {'name': u'Maximum Flow Rate',
                                       'pyname': u'maximum_flow_rate',
                                       'required-field': False,
                                       'autosizable': True,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'm3/s'}),
                                     (u'fan power minimum flow rate input method',
                                      {'name': u'Fan Power Minimum Flow Rate Input Method',
                                       'pyname': u'fan_power_minimum_flow_rate_input_method',
                                       'default': u'Fraction',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'Fraction',
                                                           u'FixedFlowRate'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'fan power minimum flow fraction',
                                      {'name': u'Fan Power Minimum Flow Fraction',
                                       'pyname': u'fan_power_minimum_flow_fraction',
                                       'default': 0.25,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'fan power minimum air flow rate',
                                      {'name': u'Fan Power Minimum Air Flow Rate',
                                       'pyname': u'fan_power_minimum_air_flow_rate',
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm3/s'}),
                                     (u'motor efficiency',
                                      {'name': u'Motor Efficiency',
                                       'pyname': u'motor_efficiency',
                                       'default': 0.9,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'motor in airstream fraction',
                                      {'name': u'Motor In Airstream Fraction',
                                       'pyname': u'motor_in_airstream_fraction',
                                       'default': 1.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'fan power coefficient 1',
                                      {'name': u'Fan Power Coefficient 1',
                                       'pyname': u'fan_power_coefficient_1',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'real'}),
                                     (u'fan power coefficient 2',
                                      {'name': u'Fan Power Coefficient 2',
                                       'pyname': u'fan_power_coefficient_2',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'real'}),
                                     (u'fan power coefficient 3',
                                      {'name': u'Fan Power Coefficient 3',
                                       'pyname': u'fan_power_coefficient_3',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'real'}),
                                     (u'fan power coefficient 4',
                                      {'name': u'Fan Power Coefficient 4',
                                       'pyname': u'fan_power_coefficient_4',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'real'}),
                                     (u'fan power coefficient 5',
                                      {'name': u'Fan Power Coefficient 5',
                                       'pyname': u'fan_power_coefficient_5',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'real'}),
                                     (u'air inlet node name',
                                      {'name': u'Air Inlet Node Name',
                                       'pyname': u'air_inlet_node_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'node'}),
                                     (u'air outlet node name',
                                      {'name': u'Air Outlet Node Name',
                                       'pyname': u'air_outlet_node_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'node'}),
                                     (u'end-use subcategory',
                                      {'name': u'End-Use Subcategory',
                                       'pyname': u'enduse_subcategory',
                                       'default': u'General',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'})]),
              'extensible-fields': OrderedDict(),
              'unique-object': False,
              'required-object': False,
              'group': u'Fans'}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name.

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name` Availability
        schedule name for this system. Schedule value > 0 means the system is
        available. If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Availability Schedule Name"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency.

        Returns:
            float: the value of `fan_total_efficiency` or None if not set

        """
        return self["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=0.7):
        """Corresponds to IDD field `Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`
                Default value: 0.7
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Total Efficiency"] = value

    @property
    def pressure_rise(self):
        """Get pressure_rise.

        Returns:
            float: the value of `pressure_rise` or None if not set

        """
        return self["Pressure Rise"]

    @pressure_rise.setter
    def pressure_rise(self, value=None):
        """Corresponds to IDD field `Pressure Rise`

        Args:
            value (float): value for IDD Field `Pressure Rise`
                Units: Pa
                IP-Units: inH2O
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Pressure Rise"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate.

        Returns:
            float: the value of `maximum_flow_rate` or None if not set

        """
        return self["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Flow Rate"] = value

    @property
    def fan_power_minimum_flow_rate_input_method(self):
        """Get fan_power_minimum_flow_rate_input_method.

        Returns:
            str: the value of `fan_power_minimum_flow_rate_input_method` or None if not set

        """
        return self["Fan Power Minimum Flow Rate Input Method"]

    @fan_power_minimum_flow_rate_input_method.setter
    def fan_power_minimum_flow_rate_input_method(self, value="Fraction"):
        """Corresponds to IDD field `Fan Power Minimum Flow Rate Input Method`

        Args:
            value (str): value for IDD Field `Fan Power Minimum Flow Rate Input Method`
                Default value: Fraction
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Power Minimum Flow Rate Input Method"] = value

    @property
    def fan_power_minimum_flow_fraction(self):
        """Get fan_power_minimum_flow_fraction.

        Returns:
            float: the value of `fan_power_minimum_flow_fraction` or None if not set

        """
        return self["Fan Power Minimum Flow Fraction"]

    @fan_power_minimum_flow_fraction.setter
    def fan_power_minimum_flow_fraction(self, value=0.25):
        """Corresponds to IDD field `Fan Power Minimum Flow Fraction`

        Args:
            value (float): value for IDD Field `Fan Power Minimum Flow Fraction`
                Default value: 0.25
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Power Minimum Flow Fraction"] = value

    @property
    def fan_power_minimum_air_flow_rate(self):
        """Get fan_power_minimum_air_flow_rate.

        Returns:
            float: the value of `fan_power_minimum_air_flow_rate` or None if not set

        """
        return self["Fan Power Minimum Air Flow Rate"]

    @fan_power_minimum_air_flow_rate.setter
    def fan_power_minimum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Fan Power Minimum Air Flow Rate`

        Args:
            value (float): value for IDD Field `Fan Power Minimum Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Power Minimum Air Flow Rate"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency.

        Returns:
            float: the value of `motor_efficiency` or None if not set

        """
        return self["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=0.9):
        """Corresponds to IDD field `Motor Efficiency`

        Args:
            value (float): value for IDD Field `Motor Efficiency`
                Default value: 0.9
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Motor Efficiency"] = value

    @property
    def motor_in_airstream_fraction(self):
        """Get motor_in_airstream_fraction.

        Returns:
            float: the value of `motor_in_airstream_fraction` or None if not set

        """
        return self["Motor In Airstream Fraction"]

    @motor_in_airstream_fraction.setter
    def motor_in_airstream_fraction(self, value=1.0):
        """  Corresponds to IDD field `Motor In Airstream Fraction`
        0.0 means fan motor outside of air stream, 1.0 means motor inside of air stream

        Args:
            value (float): value for IDD Field `Motor In Airstream Fraction`
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Motor In Airstream Fraction"] = value

    @property
    def fan_power_coefficient_1(self):
        """Get fan_power_coefficient_1.

        Returns:
            float: the value of `fan_power_coefficient_1` or None if not set

        """
        return self["Fan Power Coefficient 1"]

    @fan_power_coefficient_1.setter
    def fan_power_coefficient_1(self, value=None):
        """  Corresponds to IDD field `Fan Power Coefficient 1`
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
        self["Fan Power Coefficient 1"] = value

    @property
    def fan_power_coefficient_2(self):
        """Get fan_power_coefficient_2.

        Returns:
            float: the value of `fan_power_coefficient_2` or None if not set

        """
        return self["Fan Power Coefficient 2"]

    @fan_power_coefficient_2.setter
    def fan_power_coefficient_2(self, value=None):
        """Corresponds to IDD field `Fan Power Coefficient 2`

        Args:
            value (float): value for IDD Field `Fan Power Coefficient 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Power Coefficient 2"] = value

    @property
    def fan_power_coefficient_3(self):
        """Get fan_power_coefficient_3.

        Returns:
            float: the value of `fan_power_coefficient_3` or None if not set

        """
        return self["Fan Power Coefficient 3"]

    @fan_power_coefficient_3.setter
    def fan_power_coefficient_3(self, value=None):
        """Corresponds to IDD field `Fan Power Coefficient 3`

        Args:
            value (float): value for IDD Field `Fan Power Coefficient 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Power Coefficient 3"] = value

    @property
    def fan_power_coefficient_4(self):
        """Get fan_power_coefficient_4.

        Returns:
            float: the value of `fan_power_coefficient_4` or None if not set

        """
        return self["Fan Power Coefficient 4"]

    @fan_power_coefficient_4.setter
    def fan_power_coefficient_4(self, value=None):
        """Corresponds to IDD field `Fan Power Coefficient 4`

        Args:
            value (float): value for IDD Field `Fan Power Coefficient 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Power Coefficient 4"] = value

    @property
    def fan_power_coefficient_5(self):
        """Get fan_power_coefficient_5.

        Returns:
            float: the value of `fan_power_coefficient_5` or None if not set

        """
        return self["Fan Power Coefficient 5"]

    @fan_power_coefficient_5.setter
    def fan_power_coefficient_5(self, value=None):
        """Corresponds to IDD field `Fan Power Coefficient 5`

        Args:
            value (float): value for IDD Field `Fan Power Coefficient 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Power Coefficient 5"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name.

        Returns:
            str: the value of `air_inlet_node_name` or None if not set

        """
        return self["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name.

        Returns:
            str: the value of `air_outlet_node_name` or None if not set

        """
        return self["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Outlet Node Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory.

        Returns:
            str: the value of `enduse_subcategory` or None if not set

        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["End-Use Subcategory"] = value




class FanOnOff(DataObject):

    """ Corresponds to IDD object `Fan:OnOff`
        Constant volume fan that is intended to cycle on and off based on cooling/heating load
        or other control signals. This fan can also operate continuously like
        Fan:ConstantVolume.
    """
    schema = {'min-fields': 9,
              'name': u'Fan:OnOff',
              'pyname': u'FanOnOff',
              'format': None,
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'availability schedule name',
                                      {'name': u'Availability Schedule Name',
                                       'pyname': u'availability_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'fan total efficiency',
                                      {'name': u'Fan Total Efficiency',
                                       'pyname': u'fan_total_efficiency',
                                       'default': 0.6,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'pressure rise',
                                      {'name': u'Pressure Rise',
                                       'pyname': u'pressure_rise',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'Pa'}),
                                     (u'maximum flow rate',
                                      {'name': u'Maximum Flow Rate',
                                       'pyname': u'maximum_flow_rate',
                                       'required-field': False,
                                       'autosizable': True,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'm3/s'}),
                                     (u'motor efficiency',
                                      {'name': u'Motor Efficiency',
                                       'pyname': u'motor_efficiency',
                                       'default': 0.8,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'motor in airstream fraction',
                                      {'name': u'Motor In Airstream Fraction',
                                       'pyname': u'motor_in_airstream_fraction',
                                       'default': 1.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'air inlet node name',
                                      {'name': u'Air Inlet Node Name',
                                       'pyname': u'air_inlet_node_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'node'}),
                                     (u'air outlet node name',
                                      {'name': u'Air Outlet Node Name',
                                       'pyname': u'air_outlet_node_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'node'}),
                                     (u'fan power ratio function of speed ratio curve name',
                                      {'name': u'Fan Power Ratio Function of Speed Ratio Curve Name',
                                       'pyname': u'fan_power_ratio_function_of_speed_ratio_curve_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'fan efficiency ratio function of speed ratio curve name',
                                      {'name': u'Fan Efficiency Ratio Function of Speed Ratio Curve Name',
                                       'pyname': u'fan_efficiency_ratio_function_of_speed_ratio_curve_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'end-use subcategory',
                                      {'name': u'End-Use Subcategory',
                                       'pyname': u'enduse_subcategory',
                                       'default': u'General',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'})]),
              'extensible-fields': OrderedDict(),
              'unique-object': False,
              'required-object': False,
              'group': u'Fans'}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name.

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name` Availability
        schedule name for this system. Schedule value > 0 means the system is
        available. If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Availability Schedule Name"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency.

        Returns:
            float: the value of `fan_total_efficiency` or None if not set

        """
        return self["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=0.6):
        """Corresponds to IDD field `Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`
                Default value: 0.6
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Total Efficiency"] = value

    @property
    def pressure_rise(self):
        """Get pressure_rise.

        Returns:
            float: the value of `pressure_rise` or None if not set

        """
        return self["Pressure Rise"]

    @pressure_rise.setter
    def pressure_rise(self, value=None):
        """Corresponds to IDD field `Pressure Rise`

        Args:
            value (float): value for IDD Field `Pressure Rise`
                Units: Pa
                IP-Units: inH2O
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Pressure Rise"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate.

        Returns:
            float: the value of `maximum_flow_rate` or None if not set

        """
        return self["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Flow Rate"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency.

        Returns:
            float: the value of `motor_efficiency` or None if not set

        """
        return self["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=0.8):
        """Corresponds to IDD field `Motor Efficiency`

        Args:
            value (float): value for IDD Field `Motor Efficiency`
                Default value: 0.8
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Motor Efficiency"] = value

    @property
    def motor_in_airstream_fraction(self):
        """Get motor_in_airstream_fraction.

        Returns:
            float: the value of `motor_in_airstream_fraction` or None if not set

        """
        return self["Motor In Airstream Fraction"]

    @motor_in_airstream_fraction.setter
    def motor_in_airstream_fraction(self, value=1.0):
        """  Corresponds to IDD field `Motor In Airstream Fraction`
        0.0 means fan motor outside of air stream, 1.0 means motor inside of air stream

        Args:
            value (float): value for IDD Field `Motor In Airstream Fraction`
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Motor In Airstream Fraction"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name.

        Returns:
            str: the value of `air_inlet_node_name` or None if not set

        """
        return self["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name.

        Returns:
            str: the value of `air_outlet_node_name` or None if not set

        """
        return self["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Outlet Node Name"] = value

    @property
    def fan_power_ratio_function_of_speed_ratio_curve_name(self):
        """Get fan_power_ratio_function_of_speed_ratio_curve_name.

        Returns:
            str: the value of `fan_power_ratio_function_of_speed_ratio_curve_name` or None if not set

        """
        return self["Fan Power Ratio Function of Speed Ratio Curve Name"]

    @fan_power_ratio_function_of_speed_ratio_curve_name.setter
    def fan_power_ratio_function_of_speed_ratio_curve_name(self, value=None):
        """  Corresponds to IDD field `Fan Power Ratio Function of Speed Ratio Curve Name`
        Table:OneIndependentVariable can also be used

        Args:
            value (str): value for IDD Field `Fan Power Ratio Function of Speed Ratio Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fan Power Ratio Function of Speed Ratio Curve Name"] = value

    @property
    def fan_efficiency_ratio_function_of_speed_ratio_curve_name(self):
        """Get fan_efficiency_ratio_function_of_speed_ratio_curve_name.

        Returns:
            str: the value of `fan_efficiency_ratio_function_of_speed_ratio_curve_name` or None if not set

        """
        return self["Fan Efficiency Ratio Function of Speed Ratio Curve Name"]

    @fan_efficiency_ratio_function_of_speed_ratio_curve_name.setter
    def fan_efficiency_ratio_function_of_speed_ratio_curve_name(
            self,
            value=None):
        """  Corresponds to IDD field `Fan Efficiency Ratio Function of Speed Ratio Curve Name`
        Table:OneIndependentVariable can also be used

        Args:
            value (str): value for IDD Field `Fan Efficiency Ratio Function of Speed Ratio Curve Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Fan Efficiency Ratio Function of Speed Ratio Curve Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory.

        Returns:
            str: the value of `enduse_subcategory` or None if not set

        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["End-Use Subcategory"] = value




class FanZoneExhaust(DataObject):

    """ Corresponds to IDD object `Fan:ZoneExhaust`
        Models a fan that exhausts air from a zone.
    """
    schema = {'min-fields': 7,
              'name': u'Fan:ZoneExhaust',
              'pyname': u'FanZoneExhaust',
              'format': None,
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'availability schedule name',
                                      {'name': u'Availability Schedule Name',
                                       'pyname': u'availability_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'fan total efficiency',
                                      {'name': u'Fan Total Efficiency',
                                       'pyname': u'fan_total_efficiency',
                                       'default': 0.6,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'pressure rise',
                                      {'name': u'Pressure Rise',
                                       'pyname': u'pressure_rise',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'Pa'}),
                                     (u'maximum flow rate',
                                      {'name': u'Maximum Flow Rate',
                                       'pyname': u'maximum_flow_rate',
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'm3/s'}),
                                     (u'air inlet node name',
                                      {'name': u'Air Inlet Node Name',
                                       'pyname': u'air_inlet_node_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'node'}),
                                     (u'air outlet node name',
                                      {'name': u'Air Outlet Node Name',
                                       'pyname': u'air_outlet_node_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'node'}),
                                     (u'end-use subcategory',
                                      {'name': u'End-Use Subcategory',
                                       'pyname': u'enduse_subcategory',
                                       'default': u'General',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'flow fraction schedule name',
                                      {'name': u'Flow Fraction Schedule Name',
                                       'pyname': u'flow_fraction_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'system availability manager coupling mode',
                                      {'name': u'System Availability Manager Coupling Mode',
                                       'pyname': u'system_availability_manager_coupling_mode',
                                       'default': u'Coupled',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'Coupled',
                                                           u'Decoupled'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'minimum zone temperature limit schedule name',
                                      {'name': u'Minimum Zone Temperature Limit Schedule Name',
                                       'pyname': u'minimum_zone_temperature_limit_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'balanced exhaust fraction schedule name',
                                      {'name': u'Balanced Exhaust Fraction Schedule Name',
                                       'pyname': u'balanced_exhaust_fraction_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'})]),
              'extensible-fields': OrderedDict(),
              'unique-object': False,
              'required-object': False,
              'group': u'Fans'}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name.

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name` Availability
        schedule name for this system. Schedule value > 0 means the system is
        available. If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Availability Schedule Name"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency.

        Returns:
            float: the value of `fan_total_efficiency` or None if not set

        """
        return self["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=0.6):
        """Corresponds to IDD field `Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`
                Default value: 0.6
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Total Efficiency"] = value

    @property
    def pressure_rise(self):
        """Get pressure_rise.

        Returns:
            float: the value of `pressure_rise` or None if not set

        """
        return self["Pressure Rise"]

    @pressure_rise.setter
    def pressure_rise(self, value=None):
        """Corresponds to IDD field `Pressure Rise`

        Args:
            value (float): value for IDD Field `Pressure Rise`
                Units: Pa
                IP-Units: inH2O
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Pressure Rise"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate.

        Returns:
            float: the value of `maximum_flow_rate` or None if not set

        """
        return self["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Flow Rate`

        Args:
            value (float): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Flow Rate"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name.

        Returns:
            str: the value of `air_inlet_node_name` or None if not set

        """
        return self["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name.

        Returns:
            str: the value of `air_outlet_node_name` or None if not set

        """
        return self["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Outlet Node Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory.

        Returns:
            str: the value of `enduse_subcategory` or None if not set

        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["End-Use Subcategory"] = value

    @property
    def flow_fraction_schedule_name(self):
        """Get flow_fraction_schedule_name.

        Returns:
            str: the value of `flow_fraction_schedule_name` or None if not set

        """
        return self["Flow Fraction Schedule Name"]

    @flow_fraction_schedule_name.setter
    def flow_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Flow Fraction Schedule Name` If field is
        used, then when fan runs the exhausted air flow rate is controlled to
        be the scheduled fraction times the Maximum Flow Rate.

        Args:
            value (str): value for IDD Field `Flow Fraction Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Flow Fraction Schedule Name"] = value

    @property
    def system_availability_manager_coupling_mode(self):
        """Get system_availability_manager_coupling_mode.

        Returns:
            str: the value of `system_availability_manager_coupling_mode` or None if not set

        """
        return self["System Availability Manager Coupling Mode"]

    @system_availability_manager_coupling_mode.setter
    def system_availability_manager_coupling_mode(self, value="Coupled"):
        """Corresponds to IDD field `System Availability Manager Coupling Mode`
        Control if fan is to be interlocked with HVAC system Availability
        Managerrs or not.

        Args:
            value (str): value for IDD Field `System Availability Manager Coupling Mode`
                Default value: Coupled
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["System Availability Manager Coupling Mode"] = value

    @property
    def minimum_zone_temperature_limit_schedule_name(self):
        """Get minimum_zone_temperature_limit_schedule_name.

        Returns:
            str: the value of `minimum_zone_temperature_limit_schedule_name` or None if not set

        """
        return self["Minimum Zone Temperature Limit Schedule Name"]

    @minimum_zone_temperature_limit_schedule_name.setter
    def minimum_zone_temperature_limit_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Zone Temperature Limit Schedule
        Name` If field is used, the exhaust fan will not run if the zone
        temperature is lower than this limit.

        Args:
            value (str): value for IDD Field `Minimum Zone Temperature Limit Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Minimum Zone Temperature Limit Schedule Name"] = value

    @property
    def balanced_exhaust_fraction_schedule_name(self):
        """Get balanced_exhaust_fraction_schedule_name.

        Returns:
            str: the value of `balanced_exhaust_fraction_schedule_name` or None if not set

        """
        return self["Balanced Exhaust Fraction Schedule Name"]

    @balanced_exhaust_fraction_schedule_name.setter
    def balanced_exhaust_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Balanced Exhaust Fraction Schedule Name`
        Used to control fan's impact on flow at the return air node. Enter the
        portion of the exhaust that is balanced by simple airflows.

        Args:
            value (str): value for IDD Field `Balanced Exhaust Fraction Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Balanced Exhaust Fraction Schedule Name"] = value




class FanPerformanceNightVentilation(DataObject):

    """ Corresponds to IDD object `FanPerformance:NightVentilation`
        Specifies an alternate set of performance parameters for a fan. These alternate
        parameters are used when a system manager (such as AvailabilityManager:NightVentilation)
        sets a specified flow rate.  May be used with any type of fan except not with
        Fan:ComponentModel. If the fan model senses that a fixed flow rate has been set, it
        will use these alternate performance parameters. It is assumed that the fan will
        run at a fixed speed in the alternate mode.
    """
    schema = {'min-fields': 0,
              'name': u'FanPerformance:NightVentilation',
              'pyname': u'FanPerformanceNightVentilation',
              'format': None,
              'fields': OrderedDict([(u'fan name',
                                      {'name': u'Fan Name',
                                       'pyname': u'fan_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'fan total efficiency',
                                      {'name': u'Fan Total Efficiency',
                                       'pyname': u'fan_total_efficiency',
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'pressure rise',
                                      {'name': u'Pressure Rise',
                                       'pyname': u'pressure_rise',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'Pa'}),
                                     (u'maximum flow rate',
                                      {'name': u'Maximum Flow Rate',
                                       'pyname': u'maximum_flow_rate',
                                       'required-field': False,
                                       'autosizable': True,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'm3/s'}),
                                     (u'motor efficiency',
                                      {'name': u'Motor Efficiency',
                                       'pyname': u'motor_efficiency',
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'motor in airstream fraction',
                                      {'name': u'Motor in Airstream Fraction',
                                       'pyname': u'motor_in_airstream_fraction',
                                       'default': 1.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real'})]),
              'extensible-fields': OrderedDict(),
              'unique-object': False,
              'required-object': False,
              'group': u'Fans'}

    @property
    def fan_name(self):
        """Get fan_name.

        Returns:
            str: the value of `fan_name` or None if not set

        """
        return self["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """Corresponds to IDD field `Fan Name`

        Args:
            value (str): value for IDD Field `Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Name"] = value

    @property
    def fan_total_efficiency(self):
        """Get fan_total_efficiency.

        Returns:
            float: the value of `fan_total_efficiency` or None if not set

        """
        return self["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=None):
        """Corresponds to IDD field `Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Total Efficiency"] = value

    @property
    def pressure_rise(self):
        """Get pressure_rise.

        Returns:
            float: the value of `pressure_rise` or None if not set

        """
        return self["Pressure Rise"]

    @pressure_rise.setter
    def pressure_rise(self, value=None):
        """Corresponds to IDD field `Pressure Rise`

        Args:
            value (float): value for IDD Field `Pressure Rise`
                Units: Pa
                IP-Units: inH2O
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Pressure Rise"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate.

        Returns:
            float: the value of `maximum_flow_rate` or None if not set

        """
        return self["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Flow Rate"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency.

        Returns:
            float: the value of `motor_efficiency` or None if not set

        """
        return self["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=None):
        """Corresponds to IDD field `Motor Efficiency`

        Args:
            value (float): value for IDD Field `Motor Efficiency`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Motor Efficiency"] = value

    @property
    def motor_in_airstream_fraction(self):
        """Get motor_in_airstream_fraction.

        Returns:
            float: the value of `motor_in_airstream_fraction` or None if not set

        """
        return self["Motor in Airstream Fraction"]

    @motor_in_airstream_fraction.setter
    def motor_in_airstream_fraction(self, value=1.0):
        """  Corresponds to IDD field `Motor in Airstream Fraction`
        0.0 means fan motor outside of airstream
        1.0 means fan motor inside of airstream

        Args:
            value (float): value for IDD Field `Motor in Airstream Fraction`
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Motor in Airstream Fraction"] = value




class FanComponentModel(DataObject):

    """ Corresponds to IDD object `Fan:ComponentModel`
        A detailed fan type for constant-air-volume (CAV) and variable-air-volume (VAV)
        systems. It includes inputs that describe the air-distribution system as well as the
        fan, drive belt (if used), motor, and variable-frequency-drive (if used).
    """
    schema = {'min-fields': 0,
              'name': u'Fan:ComponentModel',
              'pyname': u'FanComponentModel',
              'format': None,
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'air inlet node name',
                                      {'name': u'Air Inlet Node Name',
                                       'pyname': u'air_inlet_node_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'node'}),
                                     (u'air outlet node name',
                                      {'name': u'Air Outlet Node Name',
                                       'pyname': u'air_outlet_node_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'node'}),
                                     (u'availability schedule name',
                                      {'name': u'Availability Schedule Name',
                                       'pyname': u'availability_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'maximum flow rate',
                                      {'name': u'Maximum Flow Rate',
                                       'pyname': u'maximum_flow_rate',
                                       'required-field': False,
                                       'autosizable': True,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'm3/s'}),
                                     (u'minimum flow rate',
                                      {'name': u'Minimum Flow Rate',
                                       'pyname': u'minimum_flow_rate',
                                       'required-field': False,
                                       'autosizable': True,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': 'real',
                                       'unit': u'm3/s'}),
                                     (u'fan sizing factor',
                                      {'name': u'Fan Sizing Factor',
                                       'pyname': u'fan_sizing_factor',
                                       'default': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 1.0,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'fan wheel diameter',
                                      {'name': u'Fan Wheel Diameter',
                                       'pyname': u'fan_wheel_diameter',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'}),
                                     (u'fan outlet area',
                                      {'name': u'Fan Outlet Area',
                                       'pyname': u'fan_outlet_area',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm2'}),
                                     (u'maximum fan static efficiency',
                                      {'name': u'Maximum Fan Static Efficiency',
                                       'pyname': u'maximum_fan_static_efficiency',
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'euler number at maximum fan static efficiency',
                                      {'name': u'Euler Number at Maximum Fan Static Efficiency',
                                       'pyname': u'euler_number_at_maximum_fan_static_efficiency',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'maximum dimensionless fan airflow',
                                      {'name': u'Maximum Dimensionless Fan Airflow',
                                       'pyname': u'maximum_dimensionless_fan_airflow',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'motor fan pulley ratio',
                                      {'name': u'Motor Fan Pulley Ratio',
                                       'pyname': u'motor_fan_pulley_ratio',
                                       'default': 1.0,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': True,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'belt maximum torque',
                                      {'name': u'Belt Maximum Torque',
                                       'pyname': u'belt_maximum_torque',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': True,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'N-m'}),
                                     (u'belt sizing factor',
                                      {'name': u'Belt Sizing Factor',
                                       'pyname': u'belt_sizing_factor',
                                       'default': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 1.0,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'belt fractional torque transition',
                                      {'name': u'Belt Fractional Torque Transition',
                                       'pyname': u'belt_fractional_torque_transition',
                                       'default': 0.167,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'motor maximum speed',
                                      {'name': u'Motor Maximum Speed',
                                       'pyname': u'motor_maximum_speed',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'rev/min'}),
                                     (u'maximum motor output power',
                                      {'name': u'Maximum Motor Output Power',
                                       'pyname': u'maximum_motor_output_power',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': True,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'W'}),
                                     (u'motor sizing factor',
                                      {'name': u'Motor Sizing Factor',
                                       'pyname': u'motor_sizing_factor',
                                       'default': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 1.0,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'motor in airstream fraction',
                                      {'name': u'Motor In Airstream Fraction',
                                       'pyname': u'motor_in_airstream_fraction',
                                       'default': 1.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'vfd efficiency type',
                                      {'name': u'VFD Efficiency Type',
                                       'pyname': u'vfd_efficiency_type',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'Speed',
                                                           u'Power'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'maximum vfd output power',
                                      {'name': u'Maximum VFD Output Power',
                                       'pyname': u'maximum_vfd_output_power',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': True,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'W'}),
                                     (u'vfd sizing factor',
                                      {'name': u'VFD Sizing Factor',
                                       'pyname': u'vfd_sizing_factor',
                                       'default': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 1.0,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'fan pressure rise curve name',
                                      {'name': u'Fan Pressure Rise Curve Name',
                                       'pyname': u'fan_pressure_rise_curve_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'duct static pressure reset curve name',
                                      {'name': u'Duct Static Pressure Reset Curve Name',
                                       'pyname': u'duct_static_pressure_reset_curve_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'normalized fan static efficiency curve name-non-stall region',
                                      {'name': u'Normalized Fan Static Efficiency Curve Name-Non-Stall Region',
                                       'pyname': u'normalized_fan_static_efficiency_curve_namenonstall_region',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'normalized fan static efficiency curve name-stall region',
                                      {'name': u'Normalized Fan Static Efficiency Curve Name-Stall Region',
                                       'pyname': u'normalized_fan_static_efficiency_curve_namestall_region',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'normalized dimensionless airflow curve name-non-stall region',
                                      {'name': u'Normalized Dimensionless Airflow Curve Name-Non-Stall Region',
                                       'pyname': u'normalized_dimensionless_airflow_curve_namenonstall_region',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'normalized dimensionless airflow curve name-stall region',
                                      {'name': u'Normalized Dimensionless Airflow Curve Name-Stall Region',
                                       'pyname': u'normalized_dimensionless_airflow_curve_namestall_region',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'maximum belt efficiency curve name',
                                      {'name': u'Maximum Belt Efficiency Curve Name',
                                       'pyname': u'maximum_belt_efficiency_curve_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'normalized belt efficiency curve name - region 1',
                                      {'name': u'Normalized Belt Efficiency Curve Name - Region 1',
                                       'pyname': u'normalized_belt_efficiency_curve_name_region_1',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'normalized belt efficiency curve name - region 2',
                                      {'name': u'Normalized Belt Efficiency Curve Name - Region 2',
                                       'pyname': u'normalized_belt_efficiency_curve_name_region_2',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'normalized belt efficiency curve name - region 3',
                                      {'name': u'Normalized Belt Efficiency Curve Name - Region 3',
                                       'pyname': u'normalized_belt_efficiency_curve_name_region_3',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'maximum motor efficiency curve name',
                                      {'name': u'Maximum Motor Efficiency Curve Name',
                                       'pyname': u'maximum_motor_efficiency_curve_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'normalized motor efficiency curve name',
                                      {'name': u'Normalized Motor Efficiency Curve Name',
                                       'pyname': u'normalized_motor_efficiency_curve_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'vfd efficiency curve name',
                                      {'name': u'VFD Efficiency Curve Name',
                                       'pyname': u'vfd_efficiency_curve_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'end-use subcategory',
                                      {'name': u'End-Use Subcategory',
                                       'pyname': u'enduse_subcategory',
                                       'default': u'General',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'})]),
              'extensible-fields': OrderedDict(),
              'unique-object': False,
              'required-object': False,
              'group': u'Fans'}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name.

        Returns:
            str: the value of `air_inlet_node_name` or None if not set

        """
        return self["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name.

        Returns:
            str: the value of `air_outlet_node_name` or None if not set

        """
        return self["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Outlet Node Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name.

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name` Availability
        schedule name for this system. Schedule value > 0 means the system is
        available. If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Availability Schedule Name"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate.

        Returns:
            float: the value of `maximum_flow_rate` or None if not set

        """
        return self["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Flow Rate"] = value

    @property
    def minimum_flow_rate(self):
        """Get minimum_flow_rate.

        Returns:
            float: the value of `minimum_flow_rate` or None if not set

        """
        return self["Minimum Flow Rate"]

    @minimum_flow_rate.setter
    def minimum_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Minimum Flow Rate"] = value

    @property
    def fan_sizing_factor(self):
        """Get fan_sizing_factor.

        Returns:
            float: the value of `fan_sizing_factor` or None if not set

        """
        return self["Fan Sizing Factor"]

    @fan_sizing_factor.setter
    def fan_sizing_factor(self, value=1.0):
        """Corresponds to IDD field `Fan Sizing Factor` Applied to specified or
        autosized max fan airflow.

        Args:
            value (float): value for IDD Field `Fan Sizing Factor`
                Default value: 1.0
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Sizing Factor"] = value

    @property
    def fan_wheel_diameter(self):
        """Get fan_wheel_diameter.

        Returns:
            float: the value of `fan_wheel_diameter` or None if not set

        """
        return self["Fan Wheel Diameter"]

    @fan_wheel_diameter.setter
    def fan_wheel_diameter(self, value=None):
        """Corresponds to IDD field `Fan Wheel Diameter` Diameter of wheel
        outer circumference.

        Args:
            value (float): value for IDD Field `Fan Wheel Diameter`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Wheel Diameter"] = value

    @property
    def fan_outlet_area(self):
        """Get fan_outlet_area.

        Returns:
            float: the value of `fan_outlet_area` or None if not set

        """
        return self["Fan Outlet Area"]

    @fan_outlet_area.setter
    def fan_outlet_area(self, value=None):
        """Corresponds to IDD field `Fan Outlet Area` Area at fan outlet plane
        for determining discharge velocity pressure.

        Args:
            value (float): value for IDD Field `Fan Outlet Area`
                Units: m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Outlet Area"] = value

    @property
    def maximum_fan_static_efficiency(self):
        """Get maximum_fan_static_efficiency.

        Returns:
            float: the value of `maximum_fan_static_efficiency` or None if not set

        """
        return self["Maximum Fan Static Efficiency"]

    @maximum_fan_static_efficiency.setter
    def maximum_fan_static_efficiency(self, value=None):
        """Corresponds to IDD field `Maximum Fan Static Efficiency` Maximum
        ratio between power delivered to air and fan shaft input power
        Determined from fan performance data.

        Args:
            value (float): value for IDD Field `Maximum Fan Static Efficiency`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Fan Static Efficiency"] = value

    @property
    def euler_number_at_maximum_fan_static_efficiency(self):
        """Get euler_number_at_maximum_fan_static_efficiency.

        Returns:
            float: the value of `euler_number_at_maximum_fan_static_efficiency` or None if not set

        """
        return self["Euler Number at Maximum Fan Static Efficiency"]

    @euler_number_at_maximum_fan_static_efficiency.setter
    def euler_number_at_maximum_fan_static_efficiency(self, value=None):
        """Corresponds to IDD field `Euler Number at Maximum Fan Static
        Efficiency` Euler number (Eu) determined from fan performance data.

        Args:
            value (float): value for IDD Field `Euler Number at Maximum Fan Static Efficiency`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Euler Number at Maximum Fan Static Efficiency"] = value

    @property
    def maximum_dimensionless_fan_airflow(self):
        """Get maximum_dimensionless_fan_airflow.

        Returns:
            float: the value of `maximum_dimensionless_fan_airflow` or None if not set

        """
        return self["Maximum Dimensionless Fan Airflow"]

    @maximum_dimensionless_fan_airflow.setter
    def maximum_dimensionless_fan_airflow(self, value=None):
        """Corresponds to IDD field `Maximum Dimensionless Fan Airflow`
        Corresponds to maximum ratio between fan airflow and fan shaft
        rotational speed for specified fan wheel diameter Determined from fan
        performance data.

        Args:
            value (float): value for IDD Field `Maximum Dimensionless Fan Airflow`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Dimensionless Fan Airflow"] = value

    @property
    def motor_fan_pulley_ratio(self):
        """Get motor_fan_pulley_ratio.

        Returns:
            float: the value of `motor_fan_pulley_ratio` or None if not set

        """
        return self["Motor Fan Pulley Ratio"]

    @motor_fan_pulley_ratio.setter
    def motor_fan_pulley_ratio(self, value=1.0):
        """Corresponds to IDD field `Motor Fan Pulley Ratio` Ratio of motor
        pulley diameter to fan pulley diameter.

        Args:
            value (float or "Autosize"): value for IDD Field `Motor Fan Pulley Ratio`
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Motor Fan Pulley Ratio"] = value

    @property
    def belt_maximum_torque(self):
        """Get belt_maximum_torque.

        Returns:
            float: the value of `belt_maximum_torque` or None if not set

        """
        return self["Belt Maximum Torque"]

    @belt_maximum_torque.setter
    def belt_maximum_torque(self, value=None):
        """Corresponds to IDD field `Belt Maximum Torque` Maximum torque
        transmitted by belt.

        Args:
            value (float or "Autosize"): value for IDD Field `Belt Maximum Torque`
                Units: N-m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Belt Maximum Torque"] = value

    @property
    def belt_sizing_factor(self):
        """Get belt_sizing_factor.

        Returns:
            float: the value of `belt_sizing_factor` or None if not set

        """
        return self["Belt Sizing Factor"]

    @belt_sizing_factor.setter
    def belt_sizing_factor(self, value=1.0):
        """Corresponds to IDD field `Belt Sizing Factor` Applied to specified
        or autosized max torque transmitted by belt.

        Args:
            value (float): value for IDD Field `Belt Sizing Factor`
                Default value: 1.0
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Belt Sizing Factor"] = value

    @property
    def belt_fractional_torque_transition(self):
        """Get belt_fractional_torque_transition.

        Returns:
            float: the value of `belt_fractional_torque_transition` or None if not set

        """
        return self["Belt Fractional Torque Transition"]

    @belt_fractional_torque_transition.setter
    def belt_fractional_torque_transition(self, value=0.167):
        """Corresponds to IDD field `Belt Fractional Torque Transition` Region
        1 to 2 curve transition for belt normalized efficiency.

        Args:
            value (float): value for IDD Field `Belt Fractional Torque Transition`
                Default value: 0.167
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Belt Fractional Torque Transition"] = value

    @property
    def motor_maximum_speed(self):
        """Get motor_maximum_speed.

        Returns:
            float: the value of `motor_maximum_speed` or None if not set

        """
        return self["Motor Maximum Speed"]

    @motor_maximum_speed.setter
    def motor_maximum_speed(self, value=None):
        """Corresponds to IDD field `Motor Maximum Speed` Maximum rotational
        speed of fan motor shaft.

        Args:
            value (float): value for IDD Field `Motor Maximum Speed`
                Units: rev/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Motor Maximum Speed"] = value

    @property
    def maximum_motor_output_power(self):
        """Get maximum_motor_output_power.

        Returns:
            float: the value of `maximum_motor_output_power` or None if not set

        """
        return self["Maximum Motor Output Power"]

    @maximum_motor_output_power.setter
    def maximum_motor_output_power(self, value=None):
        """Corresponds to IDD field `Maximum Motor Output Power` Maximum power
        input to drive belt by motor.

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Motor Output Power`
                Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Motor Output Power"] = value

    @property
    def motor_sizing_factor(self):
        """Get motor_sizing_factor.

        Returns:
            float: the value of `motor_sizing_factor` or None if not set

        """
        return self["Motor Sizing Factor"]

    @motor_sizing_factor.setter
    def motor_sizing_factor(self, value=1.0):
        """Corresponds to IDD field `Motor Sizing Factor` Applied to specified
        or autosized motor output power.

        Args:
            value (float): value for IDD Field `Motor Sizing Factor`
                Default value: 1.0
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Motor Sizing Factor"] = value

    @property
    def motor_in_airstream_fraction(self):
        """Get motor_in_airstream_fraction.

        Returns:
            float: the value of `motor_in_airstream_fraction` or None if not set

        """
        return self["Motor In Airstream Fraction"]

    @motor_in_airstream_fraction.setter
    def motor_in_airstream_fraction(self, value=1.0):
        """  Corresponds to IDD field `Motor In Airstream Fraction`
        0.0 means motor outside air stream
        1.0 means motor inside air stream

        Args:
            value (float): value for IDD Field `Motor In Airstream Fraction`
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Motor In Airstream Fraction"] = value

    @property
    def vfd_efficiency_type(self):
        """Get vfd_efficiency_type.

        Returns:
            str: the value of `vfd_efficiency_type` or None if not set

        """
        return self["VFD Efficiency Type"]

    @vfd_efficiency_type.setter
    def vfd_efficiency_type(self, value=None):
        """  Corresponds to IDD field `VFD Efficiency Type`
        Efficiency depends on fraction of full-load motor speed
        Efficiency depends on  fraction of full-load motor input power
        If field blank, then assumes constant VFD efficiency (0.97)

        Args:
            value (str): value for IDD Field `VFD Efficiency Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["VFD Efficiency Type"] = value

    @property
    def maximum_vfd_output_power(self):
        """Get maximum_vfd_output_power.

        Returns:
            float: the value of `maximum_vfd_output_power` or None if not set

        """
        return self["Maximum VFD Output Power"]

    @maximum_vfd_output_power.setter
    def maximum_vfd_output_power(self, value=None):
        """Corresponds to IDD field `Maximum VFD Output Power` Maximum power
        input to motor by VFD.

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum VFD Output Power`
                Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum VFD Output Power"] = value

    @property
    def vfd_sizing_factor(self):
        """Get vfd_sizing_factor.

        Returns:
            float: the value of `vfd_sizing_factor` or None if not set

        """
        return self["VFD Sizing Factor"]

    @vfd_sizing_factor.setter
    def vfd_sizing_factor(self, value=1.0):
        """Corresponds to IDD field `VFD Sizing Factor` Applied to specified or
        autosized VFD output power.

        Args:
            value (float): value for IDD Field `VFD Sizing Factor`
                Default value: 1.0
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["VFD Sizing Factor"] = value

    @property
    def fan_pressure_rise_curve_name(self):
        """Get fan_pressure_rise_curve_name.

        Returns:
            str: the value of `fan_pressure_rise_curve_name` or None if not set

        """
        return self["Fan Pressure Rise Curve Name"]

    @fan_pressure_rise_curve_name.setter
    def fan_pressure_rise_curve_name(self, value=None):
        """  Corresponds to IDD field `Fan Pressure Rise Curve Name`
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
        self["Fan Pressure Rise Curve Name"] = value

    @property
    def duct_static_pressure_reset_curve_name(self):
        """Get duct_static_pressure_reset_curve_name.

        Returns:
            str: the value of `duct_static_pressure_reset_curve_name` or None if not set

        """
        return self["Duct Static Pressure Reset Curve Name"]

    @duct_static_pressure_reset_curve_name.setter
    def duct_static_pressure_reset_curve_name(self, value=None):
        """  Corresponds to IDD field `Duct Static Pressure Reset Curve Name`
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
        self["Duct Static Pressure Reset Curve Name"] = value

    @property
    def normalized_fan_static_efficiency_curve_namenonstall_region(self):
        """Get normalized_fan_static_efficiency_curve_namenonstall_region.

        Returns:
            str: the value of `normalized_fan_static_efficiency_curve_namenonstall_region` or None if not set

        """
        return self[
            "Normalized Fan Static Efficiency Curve Name-Non-Stall Region"]

    @normalized_fan_static_efficiency_curve_namenonstall_region.setter
    def normalized_fan_static_efficiency_curve_namenonstall_region(
            self,
            value=None):
        """  Corresponds to IDD field `Normalized Fan Static Efficiency Curve Name-Non-Stall Region`
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
        self[
            "Normalized Fan Static Efficiency Curve Name-Non-Stall Region"] = value

    @property
    def normalized_fan_static_efficiency_curve_namestall_region(self):
        """Get normalized_fan_static_efficiency_curve_namestall_region.

        Returns:
            str: the value of `normalized_fan_static_efficiency_curve_namestall_region` or None if not set

        """
        return self["Normalized Fan Static Efficiency Curve Name-Stall Region"]

    @normalized_fan_static_efficiency_curve_namestall_region.setter
    def normalized_fan_static_efficiency_curve_namestall_region(
            self,
            value=None):
        """  Corresponds to IDD field `Normalized Fan Static Efficiency Curve Name-Stall Region`
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
        self[
            "Normalized Fan Static Efficiency Curve Name-Stall Region"] = value

    @property
    def normalized_dimensionless_airflow_curve_namenonstall_region(self):
        """Get normalized_dimensionless_airflow_curve_namenonstall_region.

        Returns:
            str: the value of `normalized_dimensionless_airflow_curve_namenonstall_region` or None if not set

        """
        return self[
            "Normalized Dimensionless Airflow Curve Name-Non-Stall Region"]

    @normalized_dimensionless_airflow_curve_namenonstall_region.setter
    def normalized_dimensionless_airflow_curve_namenonstall_region(
            self,
            value=None):
        """  Corresponds to IDD field `Normalized Dimensionless Airflow Curve Name-Non-Stall Region`
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
        self[
            "Normalized Dimensionless Airflow Curve Name-Non-Stall Region"] = value

    @property
    def normalized_dimensionless_airflow_curve_namestall_region(self):
        """Get normalized_dimensionless_airflow_curve_namestall_region.

        Returns:
            str: the value of `normalized_dimensionless_airflow_curve_namestall_region` or None if not set

        """
        return self["Normalized Dimensionless Airflow Curve Name-Stall Region"]

    @normalized_dimensionless_airflow_curve_namestall_region.setter
    def normalized_dimensionless_airflow_curve_namestall_region(
            self,
            value=None):
        """  Corresponds to IDD field `Normalized Dimensionless Airflow Curve Name-Stall Region`
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
        self[
            "Normalized Dimensionless Airflow Curve Name-Stall Region"] = value

    @property
    def maximum_belt_efficiency_curve_name(self):
        """Get maximum_belt_efficiency_curve_name.

        Returns:
            str: the value of `maximum_belt_efficiency_curve_name` or None if not set

        """
        return self["Maximum Belt Efficiency Curve Name"]

    @maximum_belt_efficiency_curve_name.setter
    def maximum_belt_efficiency_curve_name(self, value=None):
        """  Corresponds to IDD field `Maximum Belt Efficiency Curve Name`
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
        self["Maximum Belt Efficiency Curve Name"] = value

    @property
    def normalized_belt_efficiency_curve_name_region_1(self):
        """Get normalized_belt_efficiency_curve_name_region_1.

        Returns:
            str: the value of `normalized_belt_efficiency_curve_name_region_1` or None if not set

        """
        return self["Normalized Belt Efficiency Curve Name - Region 1"]

    @normalized_belt_efficiency_curve_name_region_1.setter
    def normalized_belt_efficiency_curve_name_region_1(self, value=None):
        """  Corresponds to IDD field `Normalized Belt Efficiency Curve Name - Region 1`
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
        self["Normalized Belt Efficiency Curve Name - Region 1"] = value

    @property
    def normalized_belt_efficiency_curve_name_region_2(self):
        """Get normalized_belt_efficiency_curve_name_region_2.

        Returns:
            str: the value of `normalized_belt_efficiency_curve_name_region_2` or None if not set

        """
        return self["Normalized Belt Efficiency Curve Name - Region 2"]

    @normalized_belt_efficiency_curve_name_region_2.setter
    def normalized_belt_efficiency_curve_name_region_2(self, value=None):
        """  Corresponds to IDD field `Normalized Belt Efficiency Curve Name - Region 2`
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
        self["Normalized Belt Efficiency Curve Name - Region 2"] = value

    @property
    def normalized_belt_efficiency_curve_name_region_3(self):
        """Get normalized_belt_efficiency_curve_name_region_3.

        Returns:
            str: the value of `normalized_belt_efficiency_curve_name_region_3` or None if not set

        """
        return self["Normalized Belt Efficiency Curve Name - Region 3"]

    @normalized_belt_efficiency_curve_name_region_3.setter
    def normalized_belt_efficiency_curve_name_region_3(self, value=None):
        """  Corresponds to IDD field `Normalized Belt Efficiency Curve Name - Region 3`
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
        self["Normalized Belt Efficiency Curve Name - Region 3"] = value

    @property
    def maximum_motor_efficiency_curve_name(self):
        """Get maximum_motor_efficiency_curve_name.

        Returns:
            str: the value of `maximum_motor_efficiency_curve_name` or None if not set

        """
        return self["Maximum Motor Efficiency Curve Name"]

    @maximum_motor_efficiency_curve_name.setter
    def maximum_motor_efficiency_curve_name(self, value=None):
        """  Corresponds to IDD field `Maximum Motor Efficiency Curve Name`
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
        self["Maximum Motor Efficiency Curve Name"] = value

    @property
    def normalized_motor_efficiency_curve_name(self):
        """Get normalized_motor_efficiency_curve_name.

        Returns:
            str: the value of `normalized_motor_efficiency_curve_name` or None if not set

        """
        return self["Normalized Motor Efficiency Curve Name"]

    @normalized_motor_efficiency_curve_name.setter
    def normalized_motor_efficiency_curve_name(self, value=None):
        """  Corresponds to IDD field `Normalized Motor Efficiency Curve Name`
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
        self["Normalized Motor Efficiency Curve Name"] = value

    @property
    def vfd_efficiency_curve_name(self):
        """Get vfd_efficiency_curve_name.

        Returns:
            str: the value of `vfd_efficiency_curve_name` or None if not set

        """
        return self["VFD Efficiency Curve Name"]

    @vfd_efficiency_curve_name.setter
    def vfd_efficiency_curve_name(self, value=None):
        """  Corresponds to IDD field `VFD Efficiency Curve Name`
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
        self["VFD Efficiency Curve Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory.

        Returns:
            str: the value of `enduse_subcategory` or None if not set

        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["End-Use Subcategory"] = value


