""" Data objects in group "Controllers"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ControllerWaterCoil(DataObject):

    """ Corresponds to IDD object `Controller:WaterCoil`
        Controller for a water coil which is located directly in an air loop branch or
        outdoor air equipment list. Controls the coil water flow to meet the specified
        leaving air setpoint(s). Used with Coil:Heating:Water, Coil:Cooling:Water,
        Coil:Cooling:Water:DetailedGeometry, and
        CoilSystem:Cooling:Water:HeatexchangerAssisted.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature',
                                                            u'HumidityRatio',
                                                            u'TemperatureAndHumidityRatio'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'action',
                                       {'name': u'Action',
                                        'pyname': u'action',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Normal',
                                                            u'Reverse'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'actuator variable',
                                       {'name': u'Actuator Variable',
                                        'pyname': u'actuator_variable',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'sensor node name',
                                       {'name': u'Sensor Node Name',
                                        'pyname': u'sensor_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'actuator node name',
                                       {'name': u'Actuator Node Name',
                                        'pyname': u'actuator_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'controller convergence tolerance',
                                       {'name': u'Controller Convergence Tolerance',
                                        'pyname': u'controller_convergence_tolerance',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'maximum actuated flow',
                                       {'name': u'Maximum Actuated Flow',
                                        'pyname': u'maximum_actuated_flow',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum actuated flow',
                                       {'name': u'Minimum Actuated Flow',
                                        'pyname': u'minimum_actuated_flow',
                                        'default': 1e-07,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'})]),
               'format': None,
               'group': u'Controllers',
               'min-fields': 9,
               'name': u'Controller:WaterCoil',
               'pyname': u'ControllerWaterCoil',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def control_variable(self):
        """field `Control Variable`

        |  keys HumidityRatio or TemperatureAndHumidityRatio
        |  requires a ZoneControl:Humidistat object along
        |  with SetpointManager:SingleZone:Humidity:Maximum,
        |  SetpointManager:MultiZone:MaximumHumidity:Average, or
        |  SetpointManager:Multizone:Humidity:Maximum object

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value=None):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def action(self):
        """field `Action`

        |  Leave blank to have this automatically selected from coil type.
        |  Chilled water coils should be reverse action
        |  Hot water coils should be normal action

        Args:
            value (str): value for IDD Field `Action`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `action` or None if not set

        """
        return self["Action"]

    @action.setter
    def action(self, value=None):
        """Corresponds to IDD field `Action`"""
        self["Action"] = value

    @property
    def actuator_variable(self):
        """field `Actuator Variable`

        Args:
            value (str): value for IDD Field `Actuator Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuator_variable` or None if not set

        """
        return self["Actuator Variable"]

    @actuator_variable.setter
    def actuator_variable(self, value=None):
        """Corresponds to IDD field `Actuator Variable`"""
        self["Actuator Variable"] = value

    @property
    def sensor_node_name(self):
        """field `Sensor Node Name`

        Args:
            value (str): value for IDD Field `Sensor Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `sensor_node_name` or None if not set

        """
        return self["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """Corresponds to IDD field `Sensor Node Name`"""
        self["Sensor Node Name"] = value

    @property
    def actuator_node_name(self):
        """field `Actuator Node Name`

        Args:
            value (str): value for IDD Field `Actuator Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuator_node_name` or None if not set

        """
        return self["Actuator Node Name"]

    @actuator_node_name.setter
    def actuator_node_name(self, value=None):
        """Corresponds to IDD field `Actuator Node Name`"""
        self["Actuator Node Name"] = value

    @property
    def controller_convergence_tolerance(self):
        """field `Controller Convergence Tolerance`

        |  Units: deltaC
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Controller Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `controller_convergence_tolerance` or None if not set

        """
        return self["Controller Convergence Tolerance"]

    @controller_convergence_tolerance.setter
    def controller_convergence_tolerance(self, value="autosize"):
        """Corresponds to IDD field `Controller Convergence Tolerance`"""
        self["Controller Convergence Tolerance"] = value

    @property
    def maximum_actuated_flow(self):
        """field `Maximum Actuated Flow`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Actuated Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_actuated_flow` or None if not set

        """
        return self["Maximum Actuated Flow"]

    @maximum_actuated_flow.setter
    def maximum_actuated_flow(self, value=None):
        """Corresponds to IDD field `Maximum Actuated Flow`"""
        self["Maximum Actuated Flow"] = value

    @property
    def minimum_actuated_flow(self):
        """field `Minimum Actuated Flow`

        |  Units: m3/s
        |  Default value: 1e-07

        Args:
            value (float): value for IDD Field `Minimum Actuated Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_actuated_flow` or None if not set

        """
        return self["Minimum Actuated Flow"]

    @minimum_actuated_flow.setter
    def minimum_actuated_flow(self, value=1e-07):
        """Corresponds to IDD field `Minimum Actuated Flow`"""
        self["Minimum Actuated Flow"] = value




class ControllerOutdoorAir(DataObject):

    """ Corresponds to IDD object `Controller:OutdoorAir`
        Controller to set the outdoor air flow rate for an air loop. Control options include
        fixed, proportional, scheduled, economizer, and demand-controlled ventilation.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'relief air outlet node name',
                                       {'name': u'Relief Air Outlet Node Name',
                                        'pyname': u'relief_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'return air node name',
                                       {'name': u'Return Air Node Name',
                                        'pyname': u'return_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'mixed air node name',
                                       {'name': u'Mixed Air Node Name',
                                        'pyname': u'mixed_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'actuator node name',
                                       {'name': u'Actuator Node Name',
                                        'pyname': u'actuator_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'minimum outdoor air flow rate',
                                       {'name': u'Minimum Outdoor Air Flow Rate',
                                        'pyname': u'minimum_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum outdoor air flow rate',
                                       {'name': u'Maximum Outdoor Air Flow Rate',
                                        'pyname': u'maximum_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'economizer control type',
                                       {'name': u'Economizer Control Type',
                                        'pyname': u'economizer_control_type',
                                        'default': u'NoEconomizer',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'FixedDryBulb',
                                                            u'FixedEnthalpy',
                                                            u'DifferentialDryBulb',
                                                            u'DifferentialEnthalpy',
                                                            u'FixedDewPointAndDryBulb',
                                                            u'ElectronicEnthalpy',
                                                            u'DifferentialDryBulbAndEnthalpy',
                                                            u'NoEconomizer'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'economizer control action type',
                                       {'name': u'Economizer Control Action Type',
                                        'pyname': u'economizer_control_action_type',
                                        'default': u'ModulateFlow',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ModulateFlow',
                                                            u'MinimumFlowWithBypass'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'economizer maximum limit dry-bulb temperature',
                                       {'name': u'Economizer Maximum Limit Dry-Bulb Temperature',
                                        'pyname': u'economizer_maximum_limit_drybulb_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'economizer maximum limit enthalpy',
                                       {'name': u'Economizer Maximum Limit Enthalpy',
                                        'pyname': u'economizer_maximum_limit_enthalpy',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'economizer maximum limit dewpoint temperature',
                                       {'name': u'Economizer Maximum Limit Dewpoint Temperature',
                                        'pyname': u'economizer_maximum_limit_dewpoint_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'electronic enthalpy limit curve name',
                                       {'name': u'Electronic Enthalpy Limit Curve Name',
                                        'pyname': u'electronic_enthalpy_limit_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'economizer minimum limit dry-bulb temperature',
                                       {'name': u'Economizer Minimum Limit Dry-Bulb Temperature',
                                        'pyname': u'economizer_minimum_limit_drybulb_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'lockout type',
                                       {'name': u'Lockout Type',
                                        'pyname': u'lockout_type',
                                        'default': u'NoLockout',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'NoLockout',
                                                            u'LockoutWithHeating',
                                                            u'LockoutWithCompressor'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum limit type',
                                       {'name': u'Minimum Limit Type',
                                        'pyname': u'minimum_limit_type',
                                        'default': u'ProportionalMinimum',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'FixedMinimum',
                                                            u'ProportionalMinimum'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum outdoor air schedule name',
                                       {'name': u'Minimum Outdoor Air Schedule Name',
                                        'pyname': u'minimum_outdoor_air_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum fraction of outdoor air schedule name',
                                       {'name': u'Minimum Fraction of Outdoor Air Schedule Name',
                                        'pyname': u'minimum_fraction_of_outdoor_air_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum fraction of outdoor air schedule name',
                                       {'name': u'Maximum Fraction of Outdoor Air Schedule Name',
                                        'pyname': u'maximum_fraction_of_outdoor_air_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mechanical ventilation controller name',
                                       {'name': u'Mechanical Ventilation Controller Name',
                                        'pyname': u'mechanical_ventilation_controller_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'time of day economizer control schedule name',
                                       {'name': u'Time of Day Economizer Control Schedule Name',
                                        'pyname': u'time_of_day_economizer_control_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'high humidity control',
                                       {'name': u'High Humidity Control',
                                        'pyname': u'high_humidity_control',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'humidistat control zone name',
                                       {'name': u'Humidistat Control Zone Name',
                                        'pyname': u'humidistat_control_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'high humidity outdoor air flow ratio',
                                       {'name': u'High Humidity Outdoor Air Flow Ratio',
                                        'pyname': u'high_humidity_outdoor_air_flow_ratio',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'control high indoor humidity based on outdoor humidity ratio',
                                       {'name': u'Control High Indoor Humidity Based on Outdoor Humidity Ratio',
                                        'pyname': u'control_high_indoor_humidity_based_on_outdoor_humidity_ratio',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heat recovery bypass control type',
                                       {'name': u'Heat Recovery Bypass Control Type',
                                        'pyname': u'heat_recovery_bypass_control_type',
                                        'default': u'BypassWhenWithinEconomizerLimits',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BypassWhenWithinEconomizerLimits',
                                                            u'BypassWhenOAFlowGreaterThanMinimum'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Controllers',
               'min-fields': 16,
               'name': u'Controller:OutdoorAir',
               'pyname': u'ControllerOutdoorAir',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def relief_air_outlet_node_name(self):
        """field `Relief Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Relief Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `relief_air_outlet_node_name` or None if not set

        """
        return self["Relief Air Outlet Node Name"]

    @relief_air_outlet_node_name.setter
    def relief_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Relief Air Outlet Node Name`"""
        self["Relief Air Outlet Node Name"] = value

    @property
    def return_air_node_name(self):
        """field `Return Air Node Name`

        Args:
            value (str): value for IDD Field `Return Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `return_air_node_name` or None if not set

        """
        return self["Return Air Node Name"]

    @return_air_node_name.setter
    def return_air_node_name(self, value=None):
        """Corresponds to IDD field `Return Air Node Name`"""
        self["Return Air Node Name"] = value

    @property
    def mixed_air_node_name(self):
        """field `Mixed Air Node Name`

        Args:
            value (str): value for IDD Field `Mixed Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_air_node_name` or None if not set

        """
        return self["Mixed Air Node Name"]

    @mixed_air_node_name.setter
    def mixed_air_node_name(self, value=None):
        """Corresponds to IDD field `Mixed Air Node Name`"""
        self["Mixed Air Node Name"] = value

    @property
    def actuator_node_name(self):
        """field `Actuator Node Name`

        |  Outdoor air inlet node entering the first pre-treat component if any

        Args:
            value (str): value for IDD Field `Actuator Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuator_node_name` or None if not set

        """
        return self["Actuator Node Name"]

    @actuator_node_name.setter
    def actuator_node_name(self, value=None):
        """Corresponds to IDD field `Actuator Node Name`"""
        self["Actuator Node Name"] = value

    @property
    def minimum_outdoor_air_flow_rate(self):
        """field `Minimum Outdoor Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `minimum_outdoor_air_flow_rate` or None if not set

        """
        return self["Minimum Outdoor Air Flow Rate"]

    @minimum_outdoor_air_flow_rate.setter
    def minimum_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Air Flow Rate`"""
        self["Minimum Outdoor Air Flow Rate"] = value

    @property
    def maximum_outdoor_air_flow_rate(self):
        """field `Maximum Outdoor Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_outdoor_air_flow_rate` or None if not set

        """
        return self["Maximum Outdoor Air Flow Rate"]

    @maximum_outdoor_air_flow_rate.setter
    def maximum_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Outdoor Air Flow Rate`"""
        self["Maximum Outdoor Air Flow Rate"] = value

    @property
    def economizer_control_type(self):
        """field `Economizer Control Type`

        |  Default value: NoEconomizer

        Args:
            value (str): value for IDD Field `Economizer Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `economizer_control_type` or None if not set

        """
        return self["Economizer Control Type"]

    @economizer_control_type.setter
    def economizer_control_type(self, value="NoEconomizer"):
        """Corresponds to IDD field `Economizer Control Type`"""
        self["Economizer Control Type"] = value

    @property
    def economizer_control_action_type(self):
        """field `Economizer Control Action Type`

        |  Default value: ModulateFlow

        Args:
            value (str): value for IDD Field `Economizer Control Action Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `economizer_control_action_type` or None if not set

        """
        return self["Economizer Control Action Type"]

    @economizer_control_action_type.setter
    def economizer_control_action_type(self, value="ModulateFlow"):
        """Corresponds to IDD field `Economizer Control Action Type`"""
        self["Economizer Control Action Type"] = value

    @property
    def economizer_maximum_limit_drybulb_temperature(self):
        """field `Economizer Maximum Limit Dry-Bulb Temperature`

        |  Enter the maximum outdoor dry-bulb temperature limit for FixedDryBulb
        |  economizer control type. No input or blank input means this limit is
        |  not operative. Limit is applied regardless of economizer control type.
        |  Units: C

        Args:
            value (float): value for IDD Field `Economizer Maximum Limit Dry-Bulb Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `economizer_maximum_limit_drybulb_temperature` or None if not set
        """
        return self["Economizer Maximum Limit Dry-Bulb Temperature"]

    @economizer_maximum_limit_drybulb_temperature.setter
    def economizer_maximum_limit_drybulb_temperature(self, value=None):
        """  Corresponds to IDD field `Economizer Maximum Limit Dry-Bulb Temperature`

        """
        self["Economizer Maximum Limit Dry-Bulb Temperature"] = value

    @property
    def economizer_maximum_limit_enthalpy(self):
        """field `Economizer Maximum Limit Enthalpy`

        |  Enter the maximum outdoor enthalpy limit for FixedEnthalpy economizer control type.
        |  No input or blank input means this limit is not operative
        |  Limit is applied regardless of economizer control type.
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Economizer Maximum Limit Enthalpy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `economizer_maximum_limit_enthalpy` or None if not set

        """
        return self["Economizer Maximum Limit Enthalpy"]

    @economizer_maximum_limit_enthalpy.setter
    def economizer_maximum_limit_enthalpy(self, value=None):
        """Corresponds to IDD field `Economizer Maximum Limit Enthalpy`"""
        self["Economizer Maximum Limit Enthalpy"] = value

    @property
    def economizer_maximum_limit_dewpoint_temperature(self):
        """field `Economizer Maximum Limit Dewpoint Temperature`

        |  Enter the maximum outdoor dewpoint temperature limit for FixedDewPointAndDryBulb
        |  economizer control type. No input or blank input means this limit is not operative.
        |  Limit is applied regardless of economizer control type.
        |  Units: C

        Args:
            value (float): value for IDD Field `Economizer Maximum Limit Dewpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `economizer_maximum_limit_dewpoint_temperature` or None if not set

        """
        return self["Economizer Maximum Limit Dewpoint Temperature"]

    @economizer_maximum_limit_dewpoint_temperature.setter
    def economizer_maximum_limit_dewpoint_temperature(self, value=None):
        """Corresponds to IDD field `Economizer Maximum Limit Dewpoint
        Temperature`"""
        self["Economizer Maximum Limit Dewpoint Temperature"] = value

    @property
    def electronic_enthalpy_limit_curve_name(self):
        """field `Electronic Enthalpy Limit Curve Name`

        |  Enter the name of a quadratic or cubic curve which defines the maximum outdoor
        |  humidity ratio (function of outdoor dry-bulb temperature) for ElectronicEnthalpy
        |  economizer control type. No input or blank input means this limit is not operative
        |  Limit is applied regardless of economizer control type.

        Args:
            value (str): value for IDD Field `Electronic Enthalpy Limit Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `electronic_enthalpy_limit_curve_name` or None if not set

        """
        return self["Electronic Enthalpy Limit Curve Name"]

    @electronic_enthalpy_limit_curve_name.setter
    def electronic_enthalpy_limit_curve_name(self, value=None):
        """Corresponds to IDD field `Electronic Enthalpy Limit Curve Name`"""
        self["Electronic Enthalpy Limit Curve Name"] = value

    @property
    def economizer_minimum_limit_drybulb_temperature(self):
        """field `Economizer Minimum Limit Dry-Bulb Temperature`

        |  Enter the minimum outdoor dry-bulb temperature limit for economizer control.
        |  No input or blank input means this limit is not operative
        |  Limit is applied regardless of economizer control type.
        |  Units: C

        Args:
            value (float): value for IDD Field `Economizer Minimum Limit Dry-Bulb Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `economizer_minimum_limit_drybulb_temperature` or None if not set
        """
        return self["Economizer Minimum Limit Dry-Bulb Temperature"]

    @economizer_minimum_limit_drybulb_temperature.setter
    def economizer_minimum_limit_drybulb_temperature(self, value=None):
        """  Corresponds to IDD field `Economizer Minimum Limit Dry-Bulb Temperature`

        """
        self["Economizer Minimum Limit Dry-Bulb Temperature"] = value

    @property
    def lockout_type(self):
        """field `Lockout Type`

        |  Default value: NoLockout

        Args:
            value (str): value for IDD Field `Lockout Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `lockout_type` or None if not set

        """
        return self["Lockout Type"]

    @lockout_type.setter
    def lockout_type(self, value="NoLockout"):
        """Corresponds to IDD field `Lockout Type`"""
        self["Lockout Type"] = value

    @property
    def minimum_limit_type(self):
        """field `Minimum Limit Type`

        |  Default value: ProportionalMinimum

        Args:
            value (str): value for IDD Field `Minimum Limit Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_limit_type` or None if not set

        """
        return self["Minimum Limit Type"]

    @minimum_limit_type.setter
    def minimum_limit_type(self, value="ProportionalMinimum"):
        """Corresponds to IDD field `Minimum Limit Type`"""
        self["Minimum Limit Type"] = value

    @property
    def minimum_outdoor_air_schedule_name(self):
        """field `Minimum Outdoor Air Schedule Name`

        |  Schedule values multiply the minimum outdoor air flow rate

        Args:
            value (str): value for IDD Field `Minimum Outdoor Air Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_outdoor_air_schedule_name` or None if not set

        """
        return self["Minimum Outdoor Air Schedule Name"]

    @minimum_outdoor_air_schedule_name.setter
    def minimum_outdoor_air_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Air Schedule Name`"""
        self["Minimum Outdoor Air Schedule Name"] = value

    @property
    def minimum_fraction_of_outdoor_air_schedule_name(self):
        """field `Minimum Fraction of Outdoor Air Schedule Name`

        |  schedule values multiply the design/mixed air flow rate

        Args:
            value (str): value for IDD Field `Minimum Fraction of Outdoor Air Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_fraction_of_outdoor_air_schedule_name` or None if not set

        """
        return self["Minimum Fraction of Outdoor Air Schedule Name"]

    @minimum_fraction_of_outdoor_air_schedule_name.setter
    def minimum_fraction_of_outdoor_air_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Fraction of Outdoor Air Schedule
        Name`"""
        self["Minimum Fraction of Outdoor Air Schedule Name"] = value

    @property
    def maximum_fraction_of_outdoor_air_schedule_name(self):
        """field `Maximum Fraction of Outdoor Air Schedule Name`

        |  schedule values multiply the design/mixed air flow rate

        Args:
            value (str): value for IDD Field `Maximum Fraction of Outdoor Air Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_fraction_of_outdoor_air_schedule_name` or None if not set

        """
        return self["Maximum Fraction of Outdoor Air Schedule Name"]

    @maximum_fraction_of_outdoor_air_schedule_name.setter
    def maximum_fraction_of_outdoor_air_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Fraction of Outdoor Air Schedule
        Name`"""
        self["Maximum Fraction of Outdoor Air Schedule Name"] = value

    @property
    def mechanical_ventilation_controller_name(self):
        """field `Mechanical Ventilation Controller Name`

        |  Enter the name of a Controller:MechanicalVentilation object.
        |  Optional field for defining outdoor ventilation air based on flow rate per unit floor
        |  area and flow rate per person. Simplified method of demand-controlled ventilation.

        Args:
            value (str): value for IDD Field `Mechanical Ventilation Controller Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_ventilation_controller_name` or None if not set

        """
        return self["Mechanical Ventilation Controller Name"]

    @mechanical_ventilation_controller_name.setter
    def mechanical_ventilation_controller_name(self, value=None):
        """Corresponds to IDD field `Mechanical Ventilation Controller Name`"""
        self["Mechanical Ventilation Controller Name"] = value

    @property
    def time_of_day_economizer_control_schedule_name(self):
        """field `Time of Day Economizer Control Schedule Name`

        |  Optional schedule to simulate "push-button" type economizer control.
        |  Schedule values greater than 0 indicate time-of-day economizer control is enabled.
        |  Economizer control may be used with or without the high humidity control option.
        |  When used together, high humidity control has priority over economizer control.
        |  If the field Economizer Control Type = NoEconomizer, then this option is disabled.

        Args:
            value (str): value for IDD Field `Time of Day Economizer Control Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `time_of_day_economizer_control_schedule_name` or None if not set

        """
        return self["Time of Day Economizer Control Schedule Name"]

    @time_of_day_economizer_control_schedule_name.setter
    def time_of_day_economizer_control_schedule_name(self, value=None):
        """Corresponds to IDD field `Time of Day Economizer Control Schedule
        Name`"""
        self["Time of Day Economizer Control Schedule Name"] = value

    @property
    def high_humidity_control(self):
        """field `High Humidity Control`

        |  Optional field to enable modified outdoor air flow rates based on zone relative humidity.
        |  Select Yes to modify outdoor air flow rate based on a zone humidistat.
        |  Select No to disable this feature.
        |  If the field Economizer Control Type = NoEconomizer, then this option is disabled.
        |  Default value: No

        Args:
            value (str): value for IDD Field `High Humidity Control`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `high_humidity_control` or None if not set

        """
        return self["High Humidity Control"]

    @high_humidity_control.setter
    def high_humidity_control(self, value="No"):
        """Corresponds to IDD field `High Humidity Control`"""
        self["High Humidity Control"] = value

    @property
    def humidistat_control_zone_name(self):
        """field `Humidistat Control Zone Name`

        |  Enter the name of the zone where the humidistat is located.
        |  This field is only used when the field High Humidity Control = Yes.

        Args:
            value (str): value for IDD Field `Humidistat Control Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `humidistat_control_zone_name` or None if not set

        """
        return self["Humidistat Control Zone Name"]

    @humidistat_control_zone_name.setter
    def humidistat_control_zone_name(self, value=None):
        """Corresponds to IDD field `Humidistat Control Zone Name`"""
        self["Humidistat Control Zone Name"] = value

    @property
    def high_humidity_outdoor_air_flow_ratio(self):
        """field `High Humidity Outdoor Air Flow Ratio`

        |  Enter the ratio of outdoor air to the maximum outdoor air flow rate when modified air
        |  flow rates are active based on high indoor humidity.
        |  The minimum value must be greater than 0.
        |  This field is only used when the field High Humidity Control = Yes.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `High Humidity Outdoor Air Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `high_humidity_outdoor_air_flow_ratio` or None if not set

        """
        return self["High Humidity Outdoor Air Flow Ratio"]

    @high_humidity_outdoor_air_flow_ratio.setter
    def high_humidity_outdoor_air_flow_ratio(self, value=1.0):
        """Corresponds to IDD field `High Humidity Outdoor Air Flow Ratio`"""
        self["High Humidity Outdoor Air Flow Ratio"] = value

    @property
    def control_high_indoor_humidity_based_on_outdoor_humidity_ratio(self):
        """field `Control High Indoor Humidity Based on Outdoor Humidity Ratio`

        |  If No is selected, the outdoor air flow rate is modified any time indoor relative
        |  humidity is above the humidistat setpoint. If Yes is selected, the outdoor air
        |  flow rate is modified any time the indoor relative humidity is above the humidistat
        |  setpoint and the outdoor humidity ratio is less than the indoor humidity ratio.
        |  This field is only used when the field High Humidity Control = Yes.
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Control High Indoor Humidity Based on Outdoor Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_high_indoor_humidity_based_on_outdoor_humidity_ratio` or None if not set

        """
        return self[
            "Control High Indoor Humidity Based on Outdoor Humidity Ratio"]

    @control_high_indoor_humidity_based_on_outdoor_humidity_ratio.setter
    def control_high_indoor_humidity_based_on_outdoor_humidity_ratio(
            self,
            value="Yes"):
        """Corresponds to IDD field `Control High Indoor Humidity Based on
        Outdoor Humidity Ratio`"""
        self[
            "Control High Indoor Humidity Based on Outdoor Humidity Ratio"] = value

    @property
    def heat_recovery_bypass_control_type(self):
        """field `Heat Recovery Bypass Control Type`

        |  BypassWhenWithinEconomizerLimits specifies that heat recovery
        |  is active only when the economizer is off because conditions
        |  are outside the economizer control limits
        |  BypassWhenOAFlowGreaterThanMinimum specifies enhanced economizer
        |  controls to allow heat recovery when economizer is active
        |  (within limits) but the outdoor air flow rate is at the minimum.
        |  Default value: BypassWhenWithinEconomizerLimits

        Args:
            value (str): value for IDD Field `Heat Recovery Bypass Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_recovery_bypass_control_type` or None if not set

        """
        return self["Heat Recovery Bypass Control Type"]

    @heat_recovery_bypass_control_type.setter
    def heat_recovery_bypass_control_type(
            self,
            value="BypassWhenWithinEconomizerLimits"):
        """Corresponds to IDD field `Heat Recovery Bypass Control Type`"""
        self["Heat Recovery Bypass Control Type"] = value




class ControllerMechanicalVentilation(DataObject):

    """ Corresponds to IDD object `Controller:MechanicalVentilation`
        This object is used in conjunction with Controller:OutdoorAir to specify outdoor
        ventilation air based on outdoor air specified in the DesignSpecification:OutdoorAir object
        The Controller:OutdoorAir object is associated with a specific air loop, so the
        outdoor air flow rates specified in Controller:MechanicalVentilation correspond to the zones
        attached to that specific air loop.
        Duplicate groups of Zone name, Design Specification Outdoor Air Object Name,
        and Design Specification Zone Air Distribution Object Name to increase allowable number of entries
    """
    _schema = {'extensible-fields': OrderedDict([(u'zone 1 name',
                                                  {'name': u'Zone 1 Name',
                                                   'pyname': u'zone_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'design specification outdoor air object name 1',
                                                  {'name': u'Design Specification Outdoor Air Object Name 1',
                                                   'pyname': u'design_specification_outdoor_air_object_name_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'design specification zone air distribution object name 1',
                                                  {'name': u'Design Specification Zone Air Distribution Object Name 1',
                                                   'pyname': u'design_specification_zone_air_distribution_object_name_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'demand controlled ventilation',
                                       {'name': u'Demand Controlled Ventilation',
                                        'pyname': u'demand_controlled_ventilation',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'system outdoor air method',
                                       {'name': u'System Outdoor Air Method',
                                        'pyname': u'system_outdoor_air_method',
                                        'default': u'VentilationRateProcedure',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ZoneSum',
                                                            u'VentilationRateProcedure',
                                                            u'IndoorAirQualityProcedure',
                                                            u'ProportionalControlBasedOnDesignOccupancy',
                                                            u'ProportionalControlBasedonOccupancySchedule',
                                                            u'IndoorAirQualityProcedureGenericContaminant'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zone maximum outdoor air fraction',
                                       {'name': u'Zone Maximum Outdoor Air Fraction',
                                        'pyname': u'zone_maximum_outdoor_air_fraction',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Controllers',
               'min-fields': 8,
               'name': u'Controller:MechanicalVentilation',
               'pyname': u'ControllerMechanicalVentilation',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        |  If this field is blank, the controller uses the values from the associated Controller:OutdoorAir.
        |  Schedule values greater than 0 indicate mechanical ventilation is enabled

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def demand_controlled_ventilation(self):
        """field `Demand Controlled Ventilation`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Demand Controlled Ventilation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_controlled_ventilation` or None if not set

        """
        return self["Demand Controlled Ventilation"]

    @demand_controlled_ventilation.setter
    def demand_controlled_ventilation(self, value="No"):
        """Corresponds to IDD field `Demand Controlled Ventilation`"""
        self["Demand Controlled Ventilation"] = value

    @property
    def system_outdoor_air_method(self):
        """field `System Outdoor Air Method`

        |  Default value: VentilationRateProcedure

        Args:
            value (str): value for IDD Field `System Outdoor Air Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `system_outdoor_air_method` or None if not set

        """
        return self["System Outdoor Air Method"]

    @system_outdoor_air_method.setter
    def system_outdoor_air_method(self, value="VentilationRateProcedure"):
        """Corresponds to IDD field `System Outdoor Air Method`"""
        self["System Outdoor Air Method"] = value

    @property
    def zone_maximum_outdoor_air_fraction(self):
        """field `Zone Maximum Outdoor Air Fraction`

        |  Units: dimensionless
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Zone Maximum Outdoor Air Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_maximum_outdoor_air_fraction` or None if not set

        """
        return self["Zone Maximum Outdoor Air Fraction"]

    @zone_maximum_outdoor_air_fraction.setter
    def zone_maximum_outdoor_air_fraction(self, value=1.0):
        """Corresponds to IDD field `Zone Maximum Outdoor Air Fraction`"""
        self["Zone Maximum Outdoor Air Fraction"] = value

    def add_extensible(
        self,
        zone_1_name=None,
        design_specification_outdoor_air_object_name_1=None,
        design_specification_zone_air_distribution_object_name_1=None,
    ):
        """Add values for extensible fields.

        Args:

            zone_1_name (str): value for IDD Field `Zone 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            design_specification_outdoor_air_object_name_1 (str): value for IDD Field `Design Specification Outdoor Air Object Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            design_specification_zone_air_distribution_object_name_1 (str): value for IDD Field `Design Specification Zone Air Distribution Object Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        zone_1_name = self.check_value("Zone 1 Name", zone_1_name)
        vals.append(zone_1_name)
        design_specification_outdoor_air_object_name_1 = self.check_value(
            "Design Specification Outdoor Air Object Name 1",
            design_specification_outdoor_air_object_name_1)
        vals.append(design_specification_outdoor_air_object_name_1)
        design_specification_zone_air_distribution_object_name_1 = self.check_value(
            "Design Specification Zone Air Distribution Object Name 1",
            design_specification_zone_air_distribution_object_name_1)
        vals.append(design_specification_zone_air_distribution_object_name_1)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class AirLoopHvacControllerList(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:ControllerList`
        List controllers in order of control sequence
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'controller 1 object type',
                                       {'name': u'Controller 1 Object Type',
                                        'pyname': u'controller_1_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:WaterCoil',
                                                            u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller 1 name',
                                       {'name': u'Controller 1 Name',
                                        'pyname': u'controller_1_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller 2 object type',
                                       {'name': u'Controller 2 Object Type',
                                        'pyname': u'controller_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:WaterCoil',
                                                            u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller 2 name',
                                       {'name': u'Controller 2 Name',
                                        'pyname': u'controller_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller 3 object type',
                                       {'name': u'Controller 3 Object Type',
                                        'pyname': u'controller_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:WaterCoil',
                                                            u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller 3 name',
                                       {'name': u'Controller 3 Name',
                                        'pyname': u'controller_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller 4 object type',
                                       {'name': u'Controller 4 Object Type',
                                        'pyname': u'controller_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:WaterCoil',
                                                            u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller 4 name',
                                       {'name': u'Controller 4 Name',
                                        'pyname': u'controller_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller 5 object type',
                                       {'name': u'Controller 5 Object Type',
                                        'pyname': u'controller_5_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:WaterCoil',
                                                            u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller 5 name',
                                       {'name': u'Controller 5 Name',
                                        'pyname': u'controller_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller 6 object type',
                                       {'name': u'Controller 6 Object Type',
                                        'pyname': u'controller_6_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:WaterCoil',
                                                            u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller 6 name',
                                       {'name': u'Controller 6 Name',
                                        'pyname': u'controller_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller 7 object type',
                                       {'name': u'Controller 7 Object Type',
                                        'pyname': u'controller_7_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:WaterCoil',
                                                            u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller 7 name',
                                       {'name': u'Controller 7 Name',
                                        'pyname': u'controller_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller 8 object type',
                                       {'name': u'Controller 8 Object Type',
                                        'pyname': u'controller_8_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:WaterCoil',
                                                            u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller 8 name',
                                       {'name': u'Controller 8 Name',
                                        'pyname': u'controller_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Controllers',
               'min-fields': 0,
               'name': u'AirLoopHVAC:ControllerList',
               'pyname': u'AirLoopHvacControllerList',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def controller_1_object_type(self):
        """field `Controller 1 Object Type`

        Args:
            value (str): value for IDD Field `Controller 1 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_1_object_type` or None if not set

        """
        return self["Controller 1 Object Type"]

    @controller_1_object_type.setter
    def controller_1_object_type(self, value=None):
        """Corresponds to IDD field `Controller 1 Object Type`"""
        self["Controller 1 Object Type"] = value

    @property
    def controller_1_name(self):
        """field `Controller 1 Name`

        Args:
            value (str): value for IDD Field `Controller 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_1_name` or None if not set

        """
        return self["Controller 1 Name"]

    @controller_1_name.setter
    def controller_1_name(self, value=None):
        """Corresponds to IDD field `Controller 1 Name`"""
        self["Controller 1 Name"] = value

    @property
    def controller_2_object_type(self):
        """field `Controller 2 Object Type`

        Args:
            value (str): value for IDD Field `Controller 2 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_2_object_type` or None if not set

        """
        return self["Controller 2 Object Type"]

    @controller_2_object_type.setter
    def controller_2_object_type(self, value=None):
        """Corresponds to IDD field `Controller 2 Object Type`"""
        self["Controller 2 Object Type"] = value

    @property
    def controller_2_name(self):
        """field `Controller 2 Name`

        Args:
            value (str): value for IDD Field `Controller 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_2_name` or None if not set

        """
        return self["Controller 2 Name"]

    @controller_2_name.setter
    def controller_2_name(self, value=None):
        """Corresponds to IDD field `Controller 2 Name`"""
        self["Controller 2 Name"] = value

    @property
    def controller_3_object_type(self):
        """field `Controller 3 Object Type`

        Args:
            value (str): value for IDD Field `Controller 3 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_3_object_type` or None if not set

        """
        return self["Controller 3 Object Type"]

    @controller_3_object_type.setter
    def controller_3_object_type(self, value=None):
        """Corresponds to IDD field `Controller 3 Object Type`"""
        self["Controller 3 Object Type"] = value

    @property
    def controller_3_name(self):
        """field `Controller 3 Name`

        Args:
            value (str): value for IDD Field `Controller 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_3_name` or None if not set

        """
        return self["Controller 3 Name"]

    @controller_3_name.setter
    def controller_3_name(self, value=None):
        """Corresponds to IDD field `Controller 3 Name`"""
        self["Controller 3 Name"] = value

    @property
    def controller_4_object_type(self):
        """field `Controller 4 Object Type`

        Args:
            value (str): value for IDD Field `Controller 4 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_4_object_type` or None if not set

        """
        return self["Controller 4 Object Type"]

    @controller_4_object_type.setter
    def controller_4_object_type(self, value=None):
        """Corresponds to IDD field `Controller 4 Object Type`"""
        self["Controller 4 Object Type"] = value

    @property
    def controller_4_name(self):
        """field `Controller 4 Name`

        Args:
            value (str): value for IDD Field `Controller 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_4_name` or None if not set

        """
        return self["Controller 4 Name"]

    @controller_4_name.setter
    def controller_4_name(self, value=None):
        """Corresponds to IDD field `Controller 4 Name`"""
        self["Controller 4 Name"] = value

    @property
    def controller_5_object_type(self):
        """field `Controller 5 Object Type`

        Args:
            value (str): value for IDD Field `Controller 5 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_5_object_type` or None if not set

        """
        return self["Controller 5 Object Type"]

    @controller_5_object_type.setter
    def controller_5_object_type(self, value=None):
        """Corresponds to IDD field `Controller 5 Object Type`"""
        self["Controller 5 Object Type"] = value

    @property
    def controller_5_name(self):
        """field `Controller 5 Name`

        Args:
            value (str): value for IDD Field `Controller 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_5_name` or None if not set

        """
        return self["Controller 5 Name"]

    @controller_5_name.setter
    def controller_5_name(self, value=None):
        """Corresponds to IDD field `Controller 5 Name`"""
        self["Controller 5 Name"] = value

    @property
    def controller_6_object_type(self):
        """field `Controller 6 Object Type`

        Args:
            value (str): value for IDD Field `Controller 6 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_6_object_type` or None if not set

        """
        return self["Controller 6 Object Type"]

    @controller_6_object_type.setter
    def controller_6_object_type(self, value=None):
        """Corresponds to IDD field `Controller 6 Object Type`"""
        self["Controller 6 Object Type"] = value

    @property
    def controller_6_name(self):
        """field `Controller 6 Name`

        Args:
            value (str): value for IDD Field `Controller 6 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_6_name` or None if not set

        """
        return self["Controller 6 Name"]

    @controller_6_name.setter
    def controller_6_name(self, value=None):
        """Corresponds to IDD field `Controller 6 Name`"""
        self["Controller 6 Name"] = value

    @property
    def controller_7_object_type(self):
        """field `Controller 7 Object Type`

        Args:
            value (str): value for IDD Field `Controller 7 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_7_object_type` or None if not set

        """
        return self["Controller 7 Object Type"]

    @controller_7_object_type.setter
    def controller_7_object_type(self, value=None):
        """Corresponds to IDD field `Controller 7 Object Type`"""
        self["Controller 7 Object Type"] = value

    @property
    def controller_7_name(self):
        """field `Controller 7 Name`

        Args:
            value (str): value for IDD Field `Controller 7 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_7_name` or None if not set

        """
        return self["Controller 7 Name"]

    @controller_7_name.setter
    def controller_7_name(self, value=None):
        """Corresponds to IDD field `Controller 7 Name`"""
        self["Controller 7 Name"] = value

    @property
    def controller_8_object_type(self):
        """field `Controller 8 Object Type`

        Args:
            value (str): value for IDD Field `Controller 8 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_8_object_type` or None if not set

        """
        return self["Controller 8 Object Type"]

    @controller_8_object_type.setter
    def controller_8_object_type(self, value=None):
        """Corresponds to IDD field `Controller 8 Object Type`"""
        self["Controller 8 Object Type"] = value

    @property
    def controller_8_name(self):
        """field `Controller 8 Name`

        Args:
            value (str): value for IDD Field `Controller 8 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_8_name` or None if not set

        """
        return self["Controller 8 Name"]

    @controller_8_name.setter
    def controller_8_name(self, value=None):
        """Corresponds to IDD field `Controller 8 Name`"""
        self["Controller 8 Name"] = value


