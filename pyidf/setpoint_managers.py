""" Data objects in group "Setpoint Managers"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class SetpointManagerScheduled(DataObject):

    """ Corresponds to IDD object `SetpointManager:Scheduled`
        The simplest Setpoint Manager simply uses a schedule to determine one
        or more setpoints. Values of the nodes are not used as input.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature',
                                                            u'MaximumTemperature',
                                                            u'MinimumTemperature',
                                                            u'HumidityRatio',
                                                            u'MaximumHumidityRatio',
                                                            u'MinimumHumidityRatio',
                                                            u'MassFlowRate',
                                                            u'MaximumMassFlowRate',
                                                            u'MinimumMassFlowRate'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:Scheduled',
               'pyname': u'SetpointManagerScheduled',
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
    def schedule_name(self):
        """field `Schedule Name`

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerScheduledDualSetpoint(DataObject):

    """ Corresponds to IDD object `SetpointManager:Scheduled:DualSetpoint`
        This setpoint manager places a high and low schedule value
        on one or more nodes.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'high setpoint schedule name',
                                       {'name': u'High Setpoint Schedule Name',
                                        'pyname': u'high_setpoint_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'low setpoint schedule name',
                                       {'name': u'Low Setpoint Schedule Name',
                                        'pyname': u'low_setpoint_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:Scheduled:DualSetpoint',
               'pyname': u'SetpointManagerScheduledDualSetpoint',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def high_setpoint_schedule_name(self):
        """field `High Setpoint Schedule Name`

        Args:
            value (str): value for IDD Field `High Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `high_setpoint_schedule_name` or None if not set

        """
        return self["High Setpoint Schedule Name"]

    @high_setpoint_schedule_name.setter
    def high_setpoint_schedule_name(self, value=None):
        """Corresponds to IDD field `High Setpoint Schedule Name`"""
        self["High Setpoint Schedule Name"] = value

    @property
    def low_setpoint_schedule_name(self):
        """field `Low Setpoint Schedule Name`

        Args:
            value (str): value for IDD Field `Low Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `low_setpoint_schedule_name` or None if not set

        """
        return self["Low Setpoint Schedule Name"]

    @low_setpoint_schedule_name.setter
    def low_setpoint_schedule_name(self, value=None):
        """Corresponds to IDD field `Low Setpoint Schedule Name`"""
        self["Low Setpoint Schedule Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerOutdoorAirReset(DataObject):

    """ Corresponds to IDD object `SetpointManager:OutdoorAirReset`
        The Outdoor Air Reset Setpoint Manager sets the supply air
        temperature according to the outdoor air temperature using a reset rule.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'setpoint at outdoor low temperature',
                                       {'name': u'Setpoint at Outdoor Low Temperature',
                                        'pyname': u'setpoint_at_outdoor_low_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'outdoor low temperature',
                                       {'name': u'Outdoor Low Temperature',
                                        'pyname': u'outdoor_low_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'setpoint at outdoor high temperature',
                                       {'name': u'Setpoint at Outdoor High Temperature',
                                        'pyname': u'setpoint_at_outdoor_high_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'outdoor high temperature',
                                       {'name': u'Outdoor High Temperature',
                                        'pyname': u'outdoor_high_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'setpoint at outdoor low temperature 2',
                                       {'name': u'Setpoint at Outdoor Low Temperature 2',
                                        'pyname': u'setpoint_at_outdoor_low_temperature_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'outdoor low temperature 2',
                                       {'name': u'Outdoor Low Temperature 2',
                                        'pyname': u'outdoor_low_temperature_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'setpoint at outdoor high temperature 2',
                                       {'name': u'Setpoint at Outdoor High Temperature 2',
                                        'pyname': u'setpoint_at_outdoor_high_temperature_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'outdoor high temperature 2',
                                       {'name': u'Outdoor High Temperature 2',
                                        'pyname': u'outdoor_high_temperature_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:OutdoorAirReset',
               'pyname': u'SetpointManagerOutdoorAirReset',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def setpoint_at_outdoor_low_temperature(self):
        """field `Setpoint at Outdoor Low Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Setpoint at Outdoor Low Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `setpoint_at_outdoor_low_temperature` or None if not set

        """
        return self["Setpoint at Outdoor Low Temperature"]

    @setpoint_at_outdoor_low_temperature.setter
    def setpoint_at_outdoor_low_temperature(self, value=None):
        """Corresponds to IDD field `Setpoint at Outdoor Low Temperature`"""
        self["Setpoint at Outdoor Low Temperature"] = value

    @property
    def outdoor_low_temperature(self):
        """field `Outdoor Low Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Outdoor Low Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_low_temperature` or None if not set

        """
        return self["Outdoor Low Temperature"]

    @outdoor_low_temperature.setter
    def outdoor_low_temperature(self, value=None):
        """Corresponds to IDD field `Outdoor Low Temperature`"""
        self["Outdoor Low Temperature"] = value

    @property
    def setpoint_at_outdoor_high_temperature(self):
        """field `Setpoint at Outdoor High Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Setpoint at Outdoor High Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `setpoint_at_outdoor_high_temperature` or None if not set

        """
        return self["Setpoint at Outdoor High Temperature"]

    @setpoint_at_outdoor_high_temperature.setter
    def setpoint_at_outdoor_high_temperature(self, value=None):
        """Corresponds to IDD field `Setpoint at Outdoor High Temperature`"""
        self["Setpoint at Outdoor High Temperature"] = value

    @property
    def outdoor_high_temperature(self):
        """field `Outdoor High Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Outdoor High Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_high_temperature` or None if not set

        """
        return self["Outdoor High Temperature"]

    @outdoor_high_temperature.setter
    def outdoor_high_temperature(self, value=None):
        """Corresponds to IDD field `Outdoor High Temperature`"""
        self["Outdoor High Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  Optional input.
        |  Schedule allows scheduling of the outdoor air reset rule - a schedule value
        |  of 1 means use the first rule; a value of 2 means use the second rule.

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def setpoint_at_outdoor_low_temperature_2(self):
        """field `Setpoint at Outdoor Low Temperature 2`

        |  2nd outdoor air temperature reset rule
        |  Units: C

        Args:
            value (float): value for IDD Field `Setpoint at Outdoor Low Temperature 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `setpoint_at_outdoor_low_temperature_2` or None if not set

        """
        return self["Setpoint at Outdoor Low Temperature 2"]

    @setpoint_at_outdoor_low_temperature_2.setter
    def setpoint_at_outdoor_low_temperature_2(self, value=None):
        """Corresponds to IDD field `Setpoint at Outdoor Low Temperature 2`"""
        self["Setpoint at Outdoor Low Temperature 2"] = value

    @property
    def outdoor_low_temperature_2(self):
        """field `Outdoor Low Temperature 2`

        |  2nd outdoor air temperature reset rule
        |  Units: C

        Args:
            value (float): value for IDD Field `Outdoor Low Temperature 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_low_temperature_2` or None if not set

        """
        return self["Outdoor Low Temperature 2"]

    @outdoor_low_temperature_2.setter
    def outdoor_low_temperature_2(self, value=None):
        """Corresponds to IDD field `Outdoor Low Temperature 2`"""
        self["Outdoor Low Temperature 2"] = value

    @property
    def setpoint_at_outdoor_high_temperature_2(self):
        """field `Setpoint at Outdoor High Temperature 2`

        |  2nd outdoor air temperature reset rule
        |  Units: C

        Args:
            value (float): value for IDD Field `Setpoint at Outdoor High Temperature 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `setpoint_at_outdoor_high_temperature_2` or None if not set

        """
        return self["Setpoint at Outdoor High Temperature 2"]

    @setpoint_at_outdoor_high_temperature_2.setter
    def setpoint_at_outdoor_high_temperature_2(self, value=None):
        """Corresponds to IDD field `Setpoint at Outdoor High Temperature 2`"""
        self["Setpoint at Outdoor High Temperature 2"] = value

    @property
    def outdoor_high_temperature_2(self):
        """field `Outdoor High Temperature 2`

        |  2nd outdoor air temperature reset rule
        |  Units: C

        Args:
            value (float): value for IDD Field `Outdoor High Temperature 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_high_temperature_2` or None if not set

        """
        return self["Outdoor High Temperature 2"]

    @outdoor_high_temperature_2.setter
    def outdoor_high_temperature_2(self, value=None):
        """Corresponds to IDD field `Outdoor High Temperature 2`"""
        self["Outdoor High Temperature 2"] = value




class SetpointManagerSingleZoneReheat(DataObject):

    """ Corresponds to IDD object `SetpointManager:SingleZone:Reheat`
        This setpoint manager detects the control zone load, zone inlet node flow rate, and
        zone node temperature and calculates a setpoint temperature for the supply air that
        will satisfy the zone load (heating or cooling) for the control zone. This setpoint
        manager is not limited to reheat applications.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum supply air temperature',
                                       {'name': u'Minimum Supply Air Temperature',
                                        'pyname': u'minimum_supply_air_temperature',
                                        'default': -99.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'maximum supply air temperature',
                                       {'name': u'Maximum Supply Air Temperature',
                                        'pyname': u'maximum_supply_air_temperature',
                                        'default': 99.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'control zone name',
                                       {'name': u'Control Zone Name',
                                        'pyname': u'control_zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone node name',
                                       {'name': u'Zone Node Name',
                                        'pyname': u'zone_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone inlet node name',
                                       {'name': u'Zone Inlet Node Name',
                                        'pyname': u'zone_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:SingleZone:Reheat',
               'pyname': u'SetpointManagerSingleZoneReheat',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def minimum_supply_air_temperature(self):
        """field `Minimum Supply Air Temperature`

        |  Units: C
        |  Default value: -99.0

        Args:
            value (float): value for IDD Field `Minimum Supply Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_supply_air_temperature` or None if not set

        """
        return self["Minimum Supply Air Temperature"]

    @minimum_supply_air_temperature.setter
    def minimum_supply_air_temperature(self, value=-99.0):
        """Corresponds to IDD field `Minimum Supply Air Temperature`"""
        self["Minimum Supply Air Temperature"] = value

    @property
    def maximum_supply_air_temperature(self):
        """field `Maximum Supply Air Temperature`

        |  Units: C
        |  Default value: 99.0

        Args:
            value (float): value for IDD Field `Maximum Supply Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set

        """
        return self["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=99.0):
        """Corresponds to IDD field `Maximum Supply Air Temperature`"""
        self["Maximum Supply Air Temperature"] = value

    @property
    def control_zone_name(self):
        """field `Control Zone Name`

        Args:
            value (str): value for IDD Field `Control Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_zone_name` or None if not set

        """
        return self["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """Corresponds to IDD field `Control Zone Name`"""
        self["Control Zone Name"] = value

    @property
    def zone_node_name(self):
        """field `Zone Node Name`

        Args:
            value (str): value for IDD Field `Zone Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_node_name` or None if not set

        """
        return self["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """Corresponds to IDD field `Zone Node Name`"""
        self["Zone Node Name"] = value

    @property
    def zone_inlet_node_name(self):
        """field `Zone Inlet Node Name`

        Args:
            value (str): value for IDD Field `Zone Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_inlet_node_name` or None if not set

        """
        return self["Zone Inlet Node Name"]

    @zone_inlet_node_name.setter
    def zone_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Zone Inlet Node Name`"""
        self["Zone Inlet Node Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerSingleZoneHeating(DataObject):

    """ Corresponds to IDD object `SetpointManager:SingleZone:Heating`
        This setpoint manager detects the control zone load to meet the current heating
        setpoint, zone inlet node flow rate, and zone node temperature, and calculates a
        setpoint temperature for the supply air that will satisfy the zone heating load for
        the control zone.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum supply air temperature',
                                       {'name': u'Minimum Supply Air Temperature',
                                        'pyname': u'minimum_supply_air_temperature',
                                        'default': -99.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'maximum supply air temperature',
                                       {'name': u'Maximum Supply Air Temperature',
                                        'pyname': u'maximum_supply_air_temperature',
                                        'default': 99.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'control zone name',
                                       {'name': u'Control Zone Name',
                                        'pyname': u'control_zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone node name',
                                       {'name': u'Zone Node Name',
                                        'pyname': u'zone_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone inlet node name',
                                       {'name': u'Zone Inlet Node Name',
                                        'pyname': u'zone_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 8,
               'name': u'SetpointManager:SingleZone:Heating',
               'pyname': u'SetpointManagerSingleZoneHeating',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def minimum_supply_air_temperature(self):
        """field `Minimum Supply Air Temperature`

        |  Units: C
        |  Default value: -99.0

        Args:
            value (float): value for IDD Field `Minimum Supply Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_supply_air_temperature` or None if not set

        """
        return self["Minimum Supply Air Temperature"]

    @minimum_supply_air_temperature.setter
    def minimum_supply_air_temperature(self, value=-99.0):
        """Corresponds to IDD field `Minimum Supply Air Temperature`"""
        self["Minimum Supply Air Temperature"] = value

    @property
    def maximum_supply_air_temperature(self):
        """field `Maximum Supply Air Temperature`

        |  Units: C
        |  Default value: 99.0

        Args:
            value (float): value for IDD Field `Maximum Supply Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set

        """
        return self["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=99.0):
        """Corresponds to IDD field `Maximum Supply Air Temperature`"""
        self["Maximum Supply Air Temperature"] = value

    @property
    def control_zone_name(self):
        """field `Control Zone Name`

        Args:
            value (str): value for IDD Field `Control Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_zone_name` or None if not set

        """
        return self["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """Corresponds to IDD field `Control Zone Name`"""
        self["Control Zone Name"] = value

    @property
    def zone_node_name(self):
        """field `Zone Node Name`

        Args:
            value (str): value for IDD Field `Zone Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_node_name` or None if not set

        """
        return self["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """Corresponds to IDD field `Zone Node Name`"""
        self["Zone Node Name"] = value

    @property
    def zone_inlet_node_name(self):
        """field `Zone Inlet Node Name`

        Args:
            value (str): value for IDD Field `Zone Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_inlet_node_name` or None if not set

        """
        return self["Zone Inlet Node Name"]

    @zone_inlet_node_name.setter
    def zone_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Zone Inlet Node Name`"""
        self["Zone Inlet Node Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerSingleZoneCooling(DataObject):

    """ Corresponds to IDD object `SetpointManager:SingleZone:Cooling`
        This setpoint manager detects the control zone load to meet the current cooling
        setpoint, zone inlet node flow rate, and zone node temperature, and calculates a
        setpoint temperature for the supply air that will satisfy the zone cooling load for
        the control zone.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum supply air temperature',
                                       {'name': u'Minimum Supply Air Temperature',
                                        'pyname': u'minimum_supply_air_temperature',
                                        'default': -99.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'maximum supply air temperature',
                                       {'name': u'Maximum Supply Air Temperature',
                                        'pyname': u'maximum_supply_air_temperature',
                                        'default': 99.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'control zone name',
                                       {'name': u'Control Zone Name',
                                        'pyname': u'control_zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone node name',
                                       {'name': u'Zone Node Name',
                                        'pyname': u'zone_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone inlet node name',
                                       {'name': u'Zone Inlet Node Name',
                                        'pyname': u'zone_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 8,
               'name': u'SetpointManager:SingleZone:Cooling',
               'pyname': u'SetpointManagerSingleZoneCooling',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def minimum_supply_air_temperature(self):
        """field `Minimum Supply Air Temperature`

        |  Units: C
        |  Default value: -99.0

        Args:
            value (float): value for IDD Field `Minimum Supply Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_supply_air_temperature` or None if not set

        """
        return self["Minimum Supply Air Temperature"]

    @minimum_supply_air_temperature.setter
    def minimum_supply_air_temperature(self, value=-99.0):
        """Corresponds to IDD field `Minimum Supply Air Temperature`"""
        self["Minimum Supply Air Temperature"] = value

    @property
    def maximum_supply_air_temperature(self):
        """field `Maximum Supply Air Temperature`

        |  Units: C
        |  Default value: 99.0

        Args:
            value (float): value for IDD Field `Maximum Supply Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set

        """
        return self["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=99.0):
        """Corresponds to IDD field `Maximum Supply Air Temperature`"""
        self["Maximum Supply Air Temperature"] = value

    @property
    def control_zone_name(self):
        """field `Control Zone Name`

        Args:
            value (str): value for IDD Field `Control Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_zone_name` or None if not set

        """
        return self["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """Corresponds to IDD field `Control Zone Name`"""
        self["Control Zone Name"] = value

    @property
    def zone_node_name(self):
        """field `Zone Node Name`

        Args:
            value (str): value for IDD Field `Zone Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_node_name` or None if not set

        """
        return self["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """Corresponds to IDD field `Zone Node Name`"""
        self["Zone Node Name"] = value

    @property
    def zone_inlet_node_name(self):
        """field `Zone Inlet Node Name`

        Args:
            value (str): value for IDD Field `Zone Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_inlet_node_name` or None if not set

        """
        return self["Zone Inlet Node Name"]

    @zone_inlet_node_name.setter
    def zone_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Zone Inlet Node Name`"""
        self["Zone Inlet Node Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerSingleZoneHumidityMinimum(DataObject):

    """ Corresponds to IDD object `SetpointManager:SingleZone:Humidity:Minimum`
        The Single Zone Minimum Humidity Setpoint Manager allows the
        control of a single zone minimum humidity level.
        This setpoint manager can be used in conjunction with
        object ZoneControl:Humidistat to detect humidity levels.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'control zone air node name',
                                       {'name': u'Control Zone Air Node Name',
                                        'pyname': u'control_zone_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:SingleZone:Humidity:Minimum',
               'pyname': u'SetpointManagerSingleZoneHumidityMinimum',
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

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

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
    def schedule_name(self):
        """field `Schedule Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which humidity ratio setpoint will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value

    @property
    def control_zone_air_node_name(self):
        """field `Control Zone Air Node Name`

        |  Name of the zone air node for the humidity control zone

        Args:
            value (str): value for IDD Field `Control Zone Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_zone_air_node_name` or None if not set

        """
        return self["Control Zone Air Node Name"]

    @control_zone_air_node_name.setter
    def control_zone_air_node_name(self, value=None):
        """Corresponds to IDD field `Control Zone Air Node Name`"""
        self["Control Zone Air Node Name"] = value




class SetpointManagerSingleZoneHumidityMaximum(DataObject):

    """ Corresponds to IDD object `SetpointManager:SingleZone:Humidity:Maximum`
        The Single Zone Maximum Humidity Setpoint Manager allows the
        control of a single zone maximum humidity level.
        This setpoint manager can be used in conjunction with
        object ZoneControl:Humidistat to detect humidity levels.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'control zone air node name',
                                       {'name': u'Control Zone Air Node Name',
                                        'pyname': u'control_zone_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 5,
               'name': u'SetpointManager:SingleZone:Humidity:Maximum',
               'pyname': u'SetpointManagerSingleZoneHumidityMaximum',
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

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

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
    def schedule_name(self):
        """field `Schedule Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which humidity ratio setpoint will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value

    @property
    def control_zone_air_node_name(self):
        """field `Control Zone Air Node Name`

        |  Name of the zone air node for the humidity control zone

        Args:
            value (str): value for IDD Field `Control Zone Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_zone_air_node_name` or None if not set

        """
        return self["Control Zone Air Node Name"]

    @control_zone_air_node_name.setter
    def control_zone_air_node_name(self, value=None):
        """Corresponds to IDD field `Control Zone Air Node Name`"""
        self["Control Zone Air Node Name"] = value




class SetpointManagerMixedAir(DataObject):

    """ Corresponds to IDD object `SetpointManager:MixedAir`
        The Mixed Air Setpoint Manager is meant to be used in conjunction
        with a Controller:OutdoorAir object. This setpoint manager is used
        to establish a temperature setpoint at the mixed air node.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reference setpoint node name',
                                       {'name': u'Reference Setpoint Node Name',
                                        'pyname': u'reference_setpoint_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'fan inlet node name',
                                       {'name': u'Fan Inlet Node Name',
                                        'pyname': u'fan_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'fan outlet node name',
                                       {'name': u'Fan Outlet Node Name',
                                        'pyname': u'fan_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:MixedAir',
               'pyname': u'SetpointManagerMixedAir',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def reference_setpoint_node_name(self):
        """field `Reference Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Reference Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reference_setpoint_node_name` or None if not set

        """
        return self["Reference Setpoint Node Name"]

    @reference_setpoint_node_name.setter
    def reference_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Reference Setpoint Node Name`"""
        self["Reference Setpoint Node Name"] = value

    @property
    def fan_inlet_node_name(self):
        """field `Fan Inlet Node Name`

        Args:
            value (str): value for IDD Field `Fan Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_inlet_node_name` or None if not set

        """
        return self["Fan Inlet Node Name"]

    @fan_inlet_node_name.setter
    def fan_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Fan Inlet Node Name`"""
        self["Fan Inlet Node Name"] = value

    @property
    def fan_outlet_node_name(self):
        """field `Fan Outlet Node Name`

        Args:
            value (str): value for IDD Field `Fan Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_outlet_node_name` or None if not set

        """
        return self["Fan Outlet Node Name"]

    @fan_outlet_node_name.setter
    def fan_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Fan Outlet Node Name`"""
        self["Fan Outlet Node Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerOutdoorAirPretreat(DataObject):

    """ Corresponds to IDD object `SetpointManager:OutdoorAirPretreat`
        This setpoint manager determines the required
        conditions at the outdoor air stream node which will
        produce the reference setpoint condition at the
        mixed air node when mixed with the return air stream
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature',
                                                            u'HumidityRatio',
                                                            u'MaximumHumidityRatio',
                                                            u'MinimumHumidityRatio'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum setpoint temperature',
                                       {'name': u'Minimum Setpoint Temperature',
                                        'pyname': u'minimum_setpoint_temperature',
                                        'default': -99.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'maximum setpoint temperature',
                                       {'name': u'Maximum Setpoint Temperature',
                                        'pyname': u'maximum_setpoint_temperature',
                                        'default': 99.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'minimum setpoint humidity ratio',
                                       {'name': u'Minimum Setpoint Humidity Ratio',
                                        'pyname': u'minimum_setpoint_humidity_ratio',
                                        'default': 1e-05,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'maximum setpoint humidity ratio',
                                       {'name': u'Maximum Setpoint Humidity Ratio',
                                        'pyname': u'maximum_setpoint_humidity_ratio',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'reference setpoint node name',
                                       {'name': u'Reference Setpoint Node Name',
                                        'pyname': u'reference_setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'mixed air stream node name',
                                       {'name': u'Mixed Air Stream Node Name',
                                        'pyname': u'mixed_air_stream_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air stream node name',
                                       {'name': u'Outdoor Air Stream Node Name',
                                        'pyname': u'outdoor_air_stream_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'return air stream node name',
                                       {'name': u'Return Air Stream Node Name',
                                        'pyname': u'return_air_stream_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 11,
               'name': u'SetpointManager:OutdoorAirPretreat',
               'pyname': u'SetpointManagerOutdoorAirPretreat',
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
    def minimum_setpoint_temperature(self):
        """field `Minimum Setpoint Temperature`

        |  Applicable only if Control variable is Temperature
        |  Units: C
        |  Default value: -99.0

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set

        """
        return self["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=-99.0):
        """Corresponds to IDD field `Minimum Setpoint Temperature`"""
        self["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """field `Maximum Setpoint Temperature`

        |  Applicable only if Control variable is Temperature
        |  Units: C
        |  Default value: 99.0

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set

        """
        return self["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=99.0):
        """Corresponds to IDD field `Maximum Setpoint Temperature`"""
        self["Maximum Setpoint Temperature"] = value

    @property
    def minimum_setpoint_humidity_ratio(self):
        """field `Minimum Setpoint Humidity Ratio`

        |  Applicable only if Control variable is
        |  MaximumHumidityRatio, MinimumHumidityRatio, or HumidityRatio - then minimum is 0.00001
        |  Units: kgWater/kgDryAir
        |  Default value: 1e-05
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Minimum Setpoint Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_humidity_ratio` or None if not set

        """
        return self["Minimum Setpoint Humidity Ratio"]

    @minimum_setpoint_humidity_ratio.setter
    def minimum_setpoint_humidity_ratio(self, value=1e-05):
        """Corresponds to IDD field `Minimum Setpoint Humidity Ratio`"""
        self["Minimum Setpoint Humidity Ratio"] = value

    @property
    def maximum_setpoint_humidity_ratio(self):
        """field `Maximum Setpoint Humidity Ratio`

        |  Applicable only if Control variable is
        |  MaximumHumidityRatio, MinimumHumidityRatio, or HumidityRatio - then minimum is 0.00001
        |  Units: kgWater/kgDryAir
        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Maximum Setpoint Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_humidity_ratio` or None if not set

        """
        return self["Maximum Setpoint Humidity Ratio"]

    @maximum_setpoint_humidity_ratio.setter
    def maximum_setpoint_humidity_ratio(self, value=1.0):
        """Corresponds to IDD field `Maximum Setpoint Humidity Ratio`"""
        self["Maximum Setpoint Humidity Ratio"] = value

    @property
    def reference_setpoint_node_name(self):
        """field `Reference Setpoint Node Name`

        |  The current setpoint at this node is the
        |  desired condition for the Mixed Air Node
        |  This node must have a valid setpoint
        |  which has been set by another setpoint manager

        Args:
            value (str): value for IDD Field `Reference Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reference_setpoint_node_name` or None if not set

        """
        return self["Reference Setpoint Node Name"]

    @reference_setpoint_node_name.setter
    def reference_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Reference Setpoint Node Name`"""
        self["Reference Setpoint Node Name"] = value

    @property
    def mixed_air_stream_node_name(self):
        """field `Mixed Air Stream Node Name`

        |  Name of Mixed Air Node

        Args:
            value (str): value for IDD Field `Mixed Air Stream Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_air_stream_node_name` or None if not set

        """
        return self["Mixed Air Stream Node Name"]

    @mixed_air_stream_node_name.setter
    def mixed_air_stream_node_name(self, value=None):
        """Corresponds to IDD field `Mixed Air Stream Node Name`"""
        self["Mixed Air Stream Node Name"] = value

    @property
    def outdoor_air_stream_node_name(self):
        """field `Outdoor Air Stream Node Name`

        |  Name of Outdoor Air Stream Node

        Args:
            value (str): value for IDD Field `Outdoor Air Stream Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_stream_node_name` or None if not set

        """
        return self["Outdoor Air Stream Node Name"]

    @outdoor_air_stream_node_name.setter
    def outdoor_air_stream_node_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Stream Node Name`"""
        self["Outdoor Air Stream Node Name"] = value

    @property
    def return_air_stream_node_name(self):
        """field `Return Air Stream Node Name`

        |  Name of Return Air Stream Node

        Args:
            value (str): value for IDD Field `Return Air Stream Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `return_air_stream_node_name` or None if not set

        """
        return self["Return Air Stream Node Name"]

    @return_air_stream_node_name.setter
    def return_air_stream_node_name(self, value=None):
        """Corresponds to IDD field `Return Air Stream Node Name`"""
        self["Return Air Stream Node Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature or humidity
        |  ratio will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerWarmest(DataObject):

    """ Corresponds to IDD object `SetpointManager:Warmest`
        This SetpointManager resets the cooling supply air temperature
        of a central forced air HVAC system according to the
        cooling demand of the warmest zone.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum setpoint temperature',
                                       {'name': u'Minimum Setpoint Temperature',
                                        'pyname': u'minimum_setpoint_temperature',
                                        'default': 12.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum setpoint temperature',
                                       {'name': u'Maximum Setpoint Temperature',
                                        'pyname': u'maximum_setpoint_temperature',
                                        'default': 18.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'strategy',
                                       {'name': u'Strategy',
                                        'pyname': u'strategy',
                                        'default': u'MaximumTemperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MaximumTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:Warmest',
               'pyname': u'SetpointManagerWarmest',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def hvac_air_loop_name(self):
        """field `HVAC Air Loop Name`

        |  Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set

        """
        return self["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """Corresponds to IDD field `HVAC Air Loop Name`"""
        self["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_temperature(self):
        """field `Minimum Setpoint Temperature`

        |  Units: C
        |  Default value: 12.0

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set

        """
        return self["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=12.0):
        """Corresponds to IDD field `Minimum Setpoint Temperature`"""
        self["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """field `Maximum Setpoint Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set

        """
        return self["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=18.0):
        """Corresponds to IDD field `Maximum Setpoint Temperature`"""
        self["Maximum Setpoint Temperature"] = value

    @property
    def strategy(self):
        """field `Strategy`

        |  Default value: MaximumTemperature

        Args:
            value (str): value for IDD Field `Strategy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `strategy` or None if not set

        """
        return self["Strategy"]

    @strategy.setter
    def strategy(self, value="MaximumTemperature"):
        """Corresponds to IDD field `Strategy`"""
        self["Strategy"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerColdest(DataObject):

    """ Corresponds to IDD object `SetpointManager:Coldest`
        This SetpointManager is used in dual duct systems to reset
        the setpoint temperature of the air in the heating supply duct.
        Usually it is used in conjunction with a SetpointManager:Warmest
        resetting the temperature of the air in the cooling supply duct.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum setpoint temperature',
                                       {'name': u'Minimum Setpoint Temperature',
                                        'pyname': u'minimum_setpoint_temperature',
                                        'default': 20.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum setpoint temperature',
                                       {'name': u'Maximum Setpoint Temperature',
                                        'pyname': u'maximum_setpoint_temperature',
                                        'default': 50.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'strategy',
                                       {'name': u'Strategy',
                                        'pyname': u'strategy',
                                        'default': u'MinimumTemperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MinimumTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:Coldest',
               'pyname': u'SetpointManagerColdest',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def hvac_air_loop_name(self):
        """field `HVAC Air Loop Name`

        |  Enter the name of an AirLoopHVAC object.

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set

        """
        return self["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """Corresponds to IDD field `HVAC Air Loop Name`"""
        self["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_temperature(self):
        """field `Minimum Setpoint Temperature`

        |  Units: C
        |  Default value: 20.0

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set

        """
        return self["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=20.0):
        """Corresponds to IDD field `Minimum Setpoint Temperature`"""
        self["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """field `Maximum Setpoint Temperature`

        |  Units: C
        |  Default value: 50.0

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set

        """
        return self["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=50.0):
        """Corresponds to IDD field `Maximum Setpoint Temperature`"""
        self["Maximum Setpoint Temperature"] = value

    @property
    def strategy(self):
        """field `Strategy`

        |  Default value: MinimumTemperature

        Args:
            value (str): value for IDD Field `Strategy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `strategy` or None if not set

        """
        return self["Strategy"]

    @strategy.setter
    def strategy(self, value="MinimumTemperature"):
        """Corresponds to IDD field `Strategy`"""
        self["Strategy"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerReturnAirBypassFlow(DataObject):

    """ Corresponds to IDD object `SetpointManager:ReturnAirBypassFlow`
        This setpoint manager determines the required
        mass flow rate through a return air bypass duct
        to meet the specified temperature setpoint
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Flow',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'temperature setpoint schedule name',
                                       {'name': u'Temperature Setpoint Schedule Name',
                                        'pyname': u'temperature_setpoint_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 4,
               'name': u'SetpointManager:ReturnAirBypassFlow',
               'pyname': u'SetpointManagerReturnAirBypassFlow',
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

        |  Default value: Flow

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Flow"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def hvac_air_loop_name(self):
        """field `HVAC Air Loop Name`

        |  Enter the name of an AirLoopHVAC object.

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set

        """
        return self["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """Corresponds to IDD field `HVAC Air Loop Name`"""
        self["HVAC Air Loop Name"] = value

    @property
    def temperature_setpoint_schedule_name(self):
        """field `Temperature Setpoint Schedule Name`

        Args:
            value (str): value for IDD Field `Temperature Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `temperature_setpoint_schedule_name` or None if not set

        """
        return self["Temperature Setpoint Schedule Name"]

    @temperature_setpoint_schedule_name.setter
    def temperature_setpoint_schedule_name(self, value=None):
        """Corresponds to IDD field `Temperature Setpoint Schedule Name`"""
        self["Temperature Setpoint Schedule Name"] = value




class SetpointManagerWarmestTemperatureFlow(DataObject):

    """ Corresponds to IDD object `SetpointManager:WarmestTemperatureFlow`
        This setpoint manager sets both the supply air temperature
        and the supply air flow rate.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum setpoint temperature',
                                       {'name': u'Minimum Setpoint Temperature',
                                        'pyname': u'minimum_setpoint_temperature',
                                        'default': 12.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum setpoint temperature',
                                       {'name': u'Maximum Setpoint Temperature',
                                        'pyname': u'maximum_setpoint_temperature',
                                        'default': 18.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'strategy',
                                       {'name': u'Strategy',
                                        'pyname': u'strategy',
                                        'default': u'TemperatureFirst',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'TemperatureFirst',
                                                            u'FlowFirst'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'minimum turndown ratio',
                                       {'name': u'Minimum Turndown Ratio',
                                        'pyname': u'minimum_turndown_ratio',
                                        'default': 0.2,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 8,
               'name': u'SetpointManager:WarmestTemperatureFlow',
               'pyname': u'SetpointManagerWarmestTemperatureFlow',
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
    def hvac_air_loop_name(self):
        """field `HVAC Air Loop Name`

        |  Enter the name of an AirLoopHVAC object.

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set

        """
        return self["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """Corresponds to IDD field `HVAC Air Loop Name`"""
        self["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_temperature(self):
        """field `Minimum Setpoint Temperature`

        |  Units: C
        |  Default value: 12.0

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set

        """
        return self["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=12.0):
        """Corresponds to IDD field `Minimum Setpoint Temperature`"""
        self["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """field `Maximum Setpoint Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set

        """
        return self["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=18.0):
        """Corresponds to IDD field `Maximum Setpoint Temperature`"""
        self["Maximum Setpoint Temperature"] = value

    @property
    def strategy(self):
        """field `Strategy`

        |  For TemperatureFirst the manager tries to find the highest setpoint temperature
        |  that will satisfy all the zone cooling loads at minimum supply air flow rate.
        |  If this setpoint temperature is less than the minimum, the setpoint temperature is set
        |  to the minimum, and the supply air flow rate is increased to meet the loads.
        |  For FlowFirst the manager tries to find the lowest supply air flow rate
        |  that will satisfy all the zone cooling loads at the maximum setpoint temperature.
        |  If this flow is greater than the maximum, the flow is set to the maximum and the
        |  setpoint temperature is reduced to satisfy the cooling loads.
        |  Default value: TemperatureFirst

        Args:
            value (str): value for IDD Field `Strategy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `strategy` or None if not set

        """
        return self["Strategy"]

    @strategy.setter
    def strategy(self, value="TemperatureFirst"):
        """Corresponds to IDD field `Strategy`"""
        self["Strategy"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value

    @property
    def minimum_turndown_ratio(self):
        """field `Minimum Turndown Ratio`

        |  Fraction of the maximum supply air flow rate.
        |  Used to define the minimum supply flow for the TemperatureFirst strategy.
        |  Units: dimensionless
        |  Default value: 0.2

        Args:
            value (float): value for IDD Field `Minimum Turndown Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_turndown_ratio` or None if not set

        """
        return self["Minimum Turndown Ratio"]

    @minimum_turndown_ratio.setter
    def minimum_turndown_ratio(self, value=0.2):
        """Corresponds to IDD field `Minimum Turndown Ratio`"""
        self["Minimum Turndown Ratio"] = value




class SetpointManagerMultiZoneHeatingAverage(DataObject):

    """ Corresponds to IDD object `SetpointManager:MultiZone:Heating:Average`
        This setpoint manager sets the average supply air temperature based on the heating load
        requirements of all controlled zones in an air loop served by a central air-conditioner.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum setpoint temperature',
                                       {'name': u'Minimum Setpoint Temperature',
                                        'pyname': u'minimum_setpoint_temperature',
                                        'default': 20.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum setpoint temperature',
                                       {'name': u'Maximum Setpoint Temperature',
                                        'pyname': u'maximum_setpoint_temperature',
                                        'default': 50.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 5,
               'name': u'SetpointManager:MultiZone:Heating:Average',
               'pyname': u'SetpointManagerMultiZoneHeatingAverage',
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
    def hvac_air_loop_name(self):
        """field `HVAC Air Loop Name`

        |  Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set

        """
        return self["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """Corresponds to IDD field `HVAC Air Loop Name`"""
        self["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_temperature(self):
        """field `Minimum Setpoint Temperature`

        |  Units: C
        |  Default value: 20.0

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set

        """
        return self["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=20.0):
        """Corresponds to IDD field `Minimum Setpoint Temperature`"""
        self["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """field `Maximum Setpoint Temperature`

        |  Units: C
        |  Default value: 50.0

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set

        """
        return self["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=50.0):
        """Corresponds to IDD field `Maximum Setpoint Temperature`"""
        self["Maximum Setpoint Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerMultiZoneCoolingAverage(DataObject):

    """ Corresponds to IDD object `SetpointManager:MultiZone:Cooling:Average`
        This setpoint manager sets the average supply air temperature based on the cooling load
        requirements of all controlled zones in an air loop served by a central air-conditioner.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum setpoint temperature',
                                       {'name': u'Minimum Setpoint Temperature',
                                        'pyname': u'minimum_setpoint_temperature',
                                        'default': 12.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum setpoint temperature',
                                       {'name': u'Maximum Setpoint Temperature',
                                        'pyname': u'maximum_setpoint_temperature',
                                        'default': 18.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 5,
               'name': u'SetpointManager:MultiZone:Cooling:Average',
               'pyname': u'SetpointManagerMultiZoneCoolingAverage',
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
    def hvac_air_loop_name(self):
        """field `HVAC Air Loop Name`

        |  Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set

        """
        return self["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """Corresponds to IDD field `HVAC Air Loop Name`"""
        self["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_temperature(self):
        """field `Minimum Setpoint Temperature`

        |  Units: C
        |  Default value: 12.0

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set

        """
        return self["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=12.0):
        """Corresponds to IDD field `Minimum Setpoint Temperature`"""
        self["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """field `Maximum Setpoint Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set

        """
        return self["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=18.0):
        """Corresponds to IDD field `Maximum Setpoint Temperature`"""
        self["Maximum Setpoint Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerMultiZoneMinimumHumidityAverage(DataObject):

    """ Corresponds to IDD object `SetpointManager:MultiZone:MinimumHumidity:Average`
        This setpoint manager sets the average supply air minimum humidity ratio based on moisture
        load requirements of all controlled zones in an air loop served by a central air-conditioner.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum setpoint humidity ratio',
                                       {'name': u'Minimum Setpoint Humidity Ratio',
                                        'pyname': u'minimum_setpoint_humidity_ratio',
                                        'default': 0.005,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'maximum setpoint humidity ratio',
                                       {'name': u'Maximum Setpoint Humidity Ratio',
                                        'pyname': u'maximum_setpoint_humidity_ratio',
                                        'default': 0.012,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 5,
               'name': u'SetpointManager:MultiZone:MinimumHumidity:Average',
               'pyname': u'SetpointManagerMultiZoneMinimumHumidityAverage',
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
    def hvac_air_loop_name(self):
        """field `HVAC Air Loop Name`

        |  Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set

        """
        return self["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """Corresponds to IDD field `HVAC Air Loop Name`"""
        self["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_humidity_ratio(self):
        """field `Minimum Setpoint Humidity Ratio`

        |  Units: kgWater/kgDryAir
        |  Default value: 0.005

        Args:
            value (float): value for IDD Field `Minimum Setpoint Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_humidity_ratio` or None if not set

        """
        return self["Minimum Setpoint Humidity Ratio"]

    @minimum_setpoint_humidity_ratio.setter
    def minimum_setpoint_humidity_ratio(self, value=0.005):
        """Corresponds to IDD field `Minimum Setpoint Humidity Ratio`"""
        self["Minimum Setpoint Humidity Ratio"] = value

    @property
    def maximum_setpoint_humidity_ratio(self):
        """field `Maximum Setpoint Humidity Ratio`

        |  Units: kgWater/kgDryAir
        |  Default value: 0.012

        Args:
            value (float): value for IDD Field `Maximum Setpoint Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_humidity_ratio` or None if not set

        """
        return self["Maximum Setpoint Humidity Ratio"]

    @maximum_setpoint_humidity_ratio.setter
    def maximum_setpoint_humidity_ratio(self, value=0.012):
        """Corresponds to IDD field `Maximum Setpoint Humidity Ratio`"""
        self["Maximum Setpoint Humidity Ratio"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the humidity ratio will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerMultiZoneMaximumHumidityAverage(DataObject):

    """ Corresponds to IDD object `SetpointManager:MultiZone:MaximumHumidity:Average`
        This setpoint manager sets the average supply air maximum humidity ratio based on moisture
        load requirements of all controlled zones in an air loop served by a central air-conditioner.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum setpoint humidity ratio',
                                       {'name': u'Minimum Setpoint Humidity Ratio',
                                        'pyname': u'minimum_setpoint_humidity_ratio',
                                        'default': 0.008,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'maximum setpoint humidity ratio',
                                       {'name': u'Maximum Setpoint Humidity Ratio',
                                        'pyname': u'maximum_setpoint_humidity_ratio',
                                        'default': 0.015,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 5,
               'name': u'SetpointManager:MultiZone:MaximumHumidity:Average',
               'pyname': u'SetpointManagerMultiZoneMaximumHumidityAverage',
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
    def hvac_air_loop_name(self):
        """field `HVAC Air Loop Name`

        |  Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set

        """
        return self["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """Corresponds to IDD field `HVAC Air Loop Name`"""
        self["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_humidity_ratio(self):
        """field `Minimum Setpoint Humidity Ratio`

        |  Units: kgWater/kgDryAir
        |  Default value: 0.008

        Args:
            value (float): value for IDD Field `Minimum Setpoint Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_humidity_ratio` or None if not set

        """
        return self["Minimum Setpoint Humidity Ratio"]

    @minimum_setpoint_humidity_ratio.setter
    def minimum_setpoint_humidity_ratio(self, value=0.008):
        """Corresponds to IDD field `Minimum Setpoint Humidity Ratio`"""
        self["Minimum Setpoint Humidity Ratio"] = value

    @property
    def maximum_setpoint_humidity_ratio(self):
        """field `Maximum Setpoint Humidity Ratio`

        |  Units: kgWater/kgDryAir
        |  Default value: 0.015

        Args:
            value (float): value for IDD Field `Maximum Setpoint Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_humidity_ratio` or None if not set

        """
        return self["Maximum Setpoint Humidity Ratio"]

    @maximum_setpoint_humidity_ratio.setter
    def maximum_setpoint_humidity_ratio(self, value=0.015):
        """Corresponds to IDD field `Maximum Setpoint Humidity Ratio`"""
        self["Maximum Setpoint Humidity Ratio"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the humidity ratio will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerMultiZoneHumidityMinimum(DataObject):

    """ Corresponds to IDD object `SetpointManager:MultiZone:Humidity:Minimum`
        This setpoint manager sets the minimum supply air humidity ratio based on humidification
        requirements of a controlled zone with critical humidity ratio setpoint (i.e., a zone with
        the highest humidity ratio setpoint) in an air loop served by a central air-conditioner.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum setpoint humidity ratio',
                                       {'name': u'Minimum Setpoint Humidity Ratio',
                                        'pyname': u'minimum_setpoint_humidity_ratio',
                                        'default': 0.005,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'maximum setpoint humidity ratio',
                                       {'name': u'Maximum Setpoint Humidity Ratio',
                                        'pyname': u'maximum_setpoint_humidity_ratio',
                                        'default': 0.012,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 5,
               'name': u'SetpointManager:MultiZone:Humidity:Minimum',
               'pyname': u'SetpointManagerMultiZoneHumidityMinimum',
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
    def hvac_air_loop_name(self):
        """field `HVAC Air Loop Name`

        |  Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set

        """
        return self["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """Corresponds to IDD field `HVAC Air Loop Name`"""
        self["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_humidity_ratio(self):
        """field `Minimum Setpoint Humidity Ratio`

        |  Units: kgWater/kgDryAir
        |  Default value: 0.005

        Args:
            value (float): value for IDD Field `Minimum Setpoint Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_humidity_ratio` or None if not set

        """
        return self["Minimum Setpoint Humidity Ratio"]

    @minimum_setpoint_humidity_ratio.setter
    def minimum_setpoint_humidity_ratio(self, value=0.005):
        """Corresponds to IDD field `Minimum Setpoint Humidity Ratio`"""
        self["Minimum Setpoint Humidity Ratio"] = value

    @property
    def maximum_setpoint_humidity_ratio(self):
        """field `Maximum Setpoint Humidity Ratio`

        |  Units: kgWater/kgDryAir
        |  Default value: 0.012

        Args:
            value (float): value for IDD Field `Maximum Setpoint Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_humidity_ratio` or None if not set

        """
        return self["Maximum Setpoint Humidity Ratio"]

    @maximum_setpoint_humidity_ratio.setter
    def maximum_setpoint_humidity_ratio(self, value=0.012):
        """Corresponds to IDD field `Maximum Setpoint Humidity Ratio`"""
        self["Maximum Setpoint Humidity Ratio"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the humidity ratio will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerMultiZoneHumidityMaximum(DataObject):

    """ Corresponds to IDD object `SetpointManager:MultiZone:Humidity:Maximum`
        This setpoint manager sets the maximum supply air humidity ratio based on dehumidification
        requirements of a controlled zone with critical humidity ratio setpoint (i.e., a zone with
        the lowest humidity ratio setpoint) in an air loop served by a central air-conditioner.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum setpoint humidity ratio',
                                       {'name': u'Minimum Setpoint Humidity Ratio',
                                        'pyname': u'minimum_setpoint_humidity_ratio',
                                        'default': 0.008,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'maximum setpoint humidity ratio',
                                       {'name': u'Maximum Setpoint Humidity Ratio',
                                        'pyname': u'maximum_setpoint_humidity_ratio',
                                        'default': 0.015,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 5,
               'name': u'SetpointManager:MultiZone:Humidity:Maximum',
               'pyname': u'SetpointManagerMultiZoneHumidityMaximum',
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
    def hvac_air_loop_name(self):
        """field `HVAC Air Loop Name`

        |  Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set

        """
        return self["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """Corresponds to IDD field `HVAC Air Loop Name`"""
        self["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_humidity_ratio(self):
        """field `Minimum Setpoint Humidity Ratio`

        |  Units: kgWater/kgDryAir
        |  Default value: 0.008

        Args:
            value (float): value for IDD Field `Minimum Setpoint Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_humidity_ratio` or None if not set

        """
        return self["Minimum Setpoint Humidity Ratio"]

    @minimum_setpoint_humidity_ratio.setter
    def minimum_setpoint_humidity_ratio(self, value=0.008):
        """Corresponds to IDD field `Minimum Setpoint Humidity Ratio`"""
        self["Minimum Setpoint Humidity Ratio"] = value

    @property
    def maximum_setpoint_humidity_ratio(self):
        """field `Maximum Setpoint Humidity Ratio`

        |  Units: kgWater/kgDryAir
        |  Default value: 0.015

        Args:
            value (float): value for IDD Field `Maximum Setpoint Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_humidity_ratio` or None if not set

        """
        return self["Maximum Setpoint Humidity Ratio"]

    @maximum_setpoint_humidity_ratio.setter
    def maximum_setpoint_humidity_ratio(self, value=0.015):
        """Corresponds to IDD field `Maximum Setpoint Humidity Ratio`"""
        self["Maximum Setpoint Humidity Ratio"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the humidity ratio will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerFollowOutdoorAirTemperature(DataObject):

    """ Corresponds to IDD object `SetpointManager:FollowOutdoorAirTemperature`
        This setpoint manager is used to place a temperature setpoint on a system node
        that is derived from the current outdoor air environmental conditions.
        The outdoor air conditions are obtained from the weather information during the simulation.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature',
                                                            u'MinimumTemperature',
                                                            u'MaximumTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reference temperature type',
                                       {'name': u'Reference Temperature Type',
                                        'pyname': u'reference_temperature_type',
                                        'default': u'OutdoorAirWetBulb',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'OutdoorAirWetBulb',
                                                            u'OutdoorAirDryBulb'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'offset temperature difference',
                                       {'name': u'Offset Temperature Difference',
                                        'pyname': u'offset_temperature_difference',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'maximum setpoint temperature',
                                       {'name': u'Maximum Setpoint Temperature',
                                        'pyname': u'maximum_setpoint_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum setpoint temperature',
                                       {'name': u'Minimum Setpoint Temperature',
                                        'pyname': u'minimum_setpoint_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:FollowOutdoorAirTemperature',
               'pyname': u'SetpointManagerFollowOutdoorAirTemperature',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def reference_temperature_type(self):
        """field `Reference Temperature Type`

        |  Default value: OutdoorAirWetBulb

        Args:
            value (str): value for IDD Field `Reference Temperature Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reference_temperature_type` or None if not set

        """
        return self["Reference Temperature Type"]

    @reference_temperature_type.setter
    def reference_temperature_type(self, value="OutdoorAirWetBulb"):
        """Corresponds to IDD field `Reference Temperature Type`"""
        self["Reference Temperature Type"] = value

    @property
    def offset_temperature_difference(self):
        """field `Offset Temperature Difference`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Offset Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `offset_temperature_difference` or None if not set

        """
        return self["Offset Temperature Difference"]

    @offset_temperature_difference.setter
    def offset_temperature_difference(self, value=None):
        """Corresponds to IDD field `Offset Temperature Difference`"""
        self["Offset Temperature Difference"] = value

    @property
    def maximum_setpoint_temperature(self):
        """field `Maximum Setpoint Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set

        """
        return self["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=None):
        """Corresponds to IDD field `Maximum Setpoint Temperature`"""
        self["Maximum Setpoint Temperature"] = value

    @property
    def minimum_setpoint_temperature(self):
        """field `Minimum Setpoint Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set

        """
        return self["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=None):
        """Corresponds to IDD field `Minimum Setpoint Temperature`"""
        self["Minimum Setpoint Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerFollowSystemNodeTemperature(DataObject):

    """ Corresponds to IDD object `SetpointManager:FollowSystemNodeTemperature`
        This setpoint manager is used to place a temperature setpoint on a
        system node that is derived from the current temperatures at a separate
        system node.  The current value of the temperature at a reference node
        is obtained and used to generate setpoint on a second system node.
        If the reference node is also designated to be an outdoor air (intake) node,
        then this setpoint manager can be used to follow outdoor air conditions
        that are adjusted for altitude.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature',
                                                            u'MinimumTemperature',
                                                            u'MaximumTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reference node name',
                                       {'name': u'Reference Node Name',
                                        'pyname': u'reference_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'reference temperature type',
                                       {'name': u'Reference Temperature Type',
                                        'pyname': u'reference_temperature_type',
                                        'default': u'NodeDryBulb',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'NodeWetBulb',
                                                            u'NodeDryBulb'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'offset temperature difference',
                                       {'name': u'Offset Temperature Difference',
                                        'pyname': u'offset_temperature_difference',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'maximum limit setpoint temperature',
                                       {'name': u'Maximum Limit Setpoint Temperature',
                                        'pyname': u'maximum_limit_setpoint_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum limit setpoint temperature',
                                       {'name': u'Minimum Limit Setpoint Temperature',
                                        'pyname': u'minimum_limit_setpoint_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:FollowSystemNodeTemperature',
               'pyname': u'SetpointManagerFollowSystemNodeTemperature',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def reference_node_name(self):
        """field `Reference Node Name`

        Args:
            value (str): value for IDD Field `Reference Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reference_node_name` or None if not set

        """
        return self["Reference Node Name"]

    @reference_node_name.setter
    def reference_node_name(self, value=None):
        """Corresponds to IDD field `Reference Node Name`"""
        self["Reference Node Name"] = value

    @property
    def reference_temperature_type(self):
        """field `Reference Temperature Type`

        |  Default value: NodeDryBulb

        Args:
            value (str): value for IDD Field `Reference Temperature Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reference_temperature_type` or None if not set

        """
        return self["Reference Temperature Type"]

    @reference_temperature_type.setter
    def reference_temperature_type(self, value="NodeDryBulb"):
        """Corresponds to IDD field `Reference Temperature Type`"""
        self["Reference Temperature Type"] = value

    @property
    def offset_temperature_difference(self):
        """field `Offset Temperature Difference`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Offset Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `offset_temperature_difference` or None if not set

        """
        return self["Offset Temperature Difference"]

    @offset_temperature_difference.setter
    def offset_temperature_difference(self, value=None):
        """Corresponds to IDD field `Offset Temperature Difference`"""
        self["Offset Temperature Difference"] = value

    @property
    def maximum_limit_setpoint_temperature(self):
        """field `Maximum Limit Setpoint Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Limit Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_limit_setpoint_temperature` or None if not set

        """
        return self["Maximum Limit Setpoint Temperature"]

    @maximum_limit_setpoint_temperature.setter
    def maximum_limit_setpoint_temperature(self, value=None):
        """Corresponds to IDD field `Maximum Limit Setpoint Temperature`"""
        self["Maximum Limit Setpoint Temperature"] = value

    @property
    def minimum_limit_setpoint_temperature(self):
        """field `Minimum Limit Setpoint Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Limit Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_limit_setpoint_temperature` or None if not set

        """
        return self["Minimum Limit Setpoint Temperature"]

    @minimum_limit_setpoint_temperature.setter
    def minimum_limit_setpoint_temperature(self, value=None):
        """Corresponds to IDD field `Minimum Limit Setpoint Temperature`"""
        self["Minimum Limit Setpoint Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerFollowGroundTemperature(DataObject):

    """ Corresponds to IDD object `SetpointManager:FollowGroundTemperature`
        This setpoint manager is used to place a temperature setpoint on a
        system node that is derived from a current ground temperature.
        The ground temperatures are specified in different
        Site:GroundTemperature:* objects and used during the simulation.
        This setpoint manager is primarily intended for condenser or plant loops
        using some type of ground heat exchanger.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control variable',
                                       {'name': u'Control Variable',
                                        'pyname': u'control_variable',
                                        'default': u'Temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature',
                                                            u'MinimumTemperature',
                                                            u'MaximumTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reference ground temperature object type',
                                       {'name': u'Reference Ground Temperature Object Type',
                                        'pyname': u'reference_ground_temperature_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Site:GroundTemperature:BuildingSurface',
                                                            u'Site:GroundTemperature:Shallow',
                                                            u'Site:GroundTemperature:Deep',
                                                            u'Site:GroundTemperature:FCfactorMethod'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'offset temperature difference',
                                       {'name': u'Offset Temperature Difference',
                                        'pyname': u'offset_temperature_difference',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'maximum setpoint temperature',
                                       {'name': u'Maximum Setpoint Temperature',
                                        'pyname': u'maximum_setpoint_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum setpoint temperature',
                                       {'name': u'Minimum Setpoint Temperature',
                                        'pyname': u'minimum_setpoint_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:FollowGroundTemperature',
               'pyname': u'SetpointManagerFollowGroundTemperature',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def reference_ground_temperature_object_type(self):
        """field `Reference Ground Temperature Object Type`

        Args:
            value (str): value for IDD Field `Reference Ground Temperature Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reference_ground_temperature_object_type` or None if not set

        """
        return self["Reference Ground Temperature Object Type"]

    @reference_ground_temperature_object_type.setter
    def reference_ground_temperature_object_type(self, value=None):
        """Corresponds to IDD field `Reference Ground Temperature Object
        Type`"""
        self["Reference Ground Temperature Object Type"] = value

    @property
    def offset_temperature_difference(self):
        """field `Offset Temperature Difference`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Offset Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `offset_temperature_difference` or None if not set

        """
        return self["Offset Temperature Difference"]

    @offset_temperature_difference.setter
    def offset_temperature_difference(self, value=None):
        """Corresponds to IDD field `Offset Temperature Difference`"""
        self["Offset Temperature Difference"] = value

    @property
    def maximum_setpoint_temperature(self):
        """field `Maximum Setpoint Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set

        """
        return self["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=None):
        """Corresponds to IDD field `Maximum Setpoint Temperature`"""
        self["Maximum Setpoint Temperature"] = value

    @property
    def minimum_setpoint_temperature(self):
        """field `Minimum Setpoint Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set

        """
        return self["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=None):
        """Corresponds to IDD field `Minimum Setpoint Temperature`"""
        self["Minimum Setpoint Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerCondenserEnteringReset(DataObject):

    """ Corresponds to IDD object `SetpointManager:CondenserEnteringReset`
        This setpoint manager uses one curve to determine the optimum condenser entering water temperature
        for a given timestep and two other curves to place boundary conditions on the setpoint value.
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
                                        'default': u'Temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'default condenser entering water temperature schedule name',
                                       {'name': u'Default Condenser Entering Water Temperature Schedule Name',
                                        'pyname': u'default_condenser_entering_water_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum design wetbulb temperature curve name',
                                       {'name': u'Minimum Design Wetbulb Temperature Curve Name',
                                        'pyname': u'minimum_design_wetbulb_temperature_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum outside air wetbulb temperature curve name',
                                       {'name': u'Minimum Outside Air Wetbulb Temperature Curve Name',
                                        'pyname': u'minimum_outside_air_wetbulb_temperature_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'optimized cond entering water temperature curve name',
                                       {'name': u'Optimized Cond Entering Water Temperature Curve Name',
                                        'pyname': u'optimized_cond_entering_water_temperature_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum lift',
                                       {'name': u'Minimum Lift',
                                        'pyname': u'minimum_lift',
                                        'default': 11.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'maximum condenser entering water temperature',
                                       {'name': u'Maximum Condenser Entering Water Temperature',
                                        'pyname': u'maximum_condenser_entering_water_temperature',
                                        'default': 32.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'cooling tower design inlet air wet-bulb temperature',
                                       {'name': u'Cooling Tower Design Inlet Air Wet-Bulb Temperature',
                                        'pyname': u'cooling_tower_design_inlet_air_wetbulb_temperature',
                                        'default': 25.56,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 10,
               'name': u'SetpointManager:CondenserEnteringReset',
               'pyname': u'SetpointManagerCondenserEnteringReset',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def default_condenser_entering_water_temperature_schedule_name(self):
        """field `Default Condenser Entering Water Temperature Schedule Name`

        |  This scheduled setpoint value is only used in a given timestep if the
        |  "Optimized" Condenser Entering Temperature does not fall within the prescribed
        |  boundary conditions.

        Args:
            value (str): value for IDD Field `Default Condenser Entering Water Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `default_condenser_entering_water_temperature_schedule_name` or None if not set

        """
        return self[
            "Default Condenser Entering Water Temperature Schedule Name"]

    @default_condenser_entering_water_temperature_schedule_name.setter
    def default_condenser_entering_water_temperature_schedule_name(
            self,
            value=None):
        """Corresponds to IDD field `Default Condenser Entering Water
        Temperature Schedule Name`"""
        self[
            "Default Condenser Entering Water Temperature Schedule Name"] = value

    @property
    def minimum_design_wetbulb_temperature_curve_name(self):
        """field `Minimum Design Wetbulb Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Minimum Design Wetbulb Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_design_wetbulb_temperature_curve_name` or None if not set

        """
        return self["Minimum Design Wetbulb Temperature Curve Name"]

    @minimum_design_wetbulb_temperature_curve_name.setter
    def minimum_design_wetbulb_temperature_curve_name(self, value=None):
        """Corresponds to IDD field `Minimum Design Wetbulb Temperature Curve
        Name`"""
        self["Minimum Design Wetbulb Temperature Curve Name"] = value

    @property
    def minimum_outside_air_wetbulb_temperature_curve_name(self):
        """field `Minimum Outside Air Wetbulb Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Minimum Outside Air Wetbulb Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_outside_air_wetbulb_temperature_curve_name` or None if not set

        """
        return self["Minimum Outside Air Wetbulb Temperature Curve Name"]

    @minimum_outside_air_wetbulb_temperature_curve_name.setter
    def minimum_outside_air_wetbulb_temperature_curve_name(self, value=None):
        """Corresponds to IDD field `Minimum Outside Air Wetbulb Temperature
        Curve Name`"""
        self["Minimum Outside Air Wetbulb Temperature Curve Name"] = value

    @property
    def optimized_cond_entering_water_temperature_curve_name(self):
        """field `Optimized Cond Entering Water Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Optimized Cond Entering Water Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `optimized_cond_entering_water_temperature_curve_name` or None if not set

        """
        return self["Optimized Cond Entering Water Temperature Curve Name"]

    @optimized_cond_entering_water_temperature_curve_name.setter
    def optimized_cond_entering_water_temperature_curve_name(self, value=None):
        """Corresponds to IDD field `Optimized Cond Entering Water Temperature
        Curve Name`"""
        self["Optimized Cond Entering Water Temperature Curve Name"] = value

    @property
    def minimum_lift(self):
        """field `Minimum Lift`

        |  Units: deltaC
        |  Default value: 11.1

        Args:
            value (float): value for IDD Field `Minimum Lift`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_lift` or None if not set

        """
        return self["Minimum Lift"]

    @minimum_lift.setter
    def minimum_lift(self, value=11.1):
        """Corresponds to IDD field `Minimum Lift`"""
        self["Minimum Lift"] = value

    @property
    def maximum_condenser_entering_water_temperature(self):
        """field `Maximum Condenser Entering Water Temperature`

        |  Units: C
        |  Default value: 32.0

        Args:
            value (float): value for IDD Field `Maximum Condenser Entering Water Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_condenser_entering_water_temperature` or None if not set

        """
        return self["Maximum Condenser Entering Water Temperature"]

    @maximum_condenser_entering_water_temperature.setter
    def maximum_condenser_entering_water_temperature(self, value=32.0):
        """Corresponds to IDD field `Maximum Condenser Entering Water
        Temperature`"""
        self["Maximum Condenser Entering Water Temperature"] = value

    @property
    def cooling_tower_design_inlet_air_wetbulb_temperature(self):
        """field `Cooling Tower Design Inlet Air Wet-Bulb Temperature`

        |  Units: C
        |  Default value: 25.56

        Args:
            value (float): value for IDD Field `Cooling Tower Design Inlet Air Wet-Bulb Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_tower_design_inlet_air_wetbulb_temperature` or None if not set
        """
        return self["Cooling Tower Design Inlet Air Wet-Bulb Temperature"]

    @cooling_tower_design_inlet_air_wetbulb_temperature.setter
    def cooling_tower_design_inlet_air_wetbulb_temperature(self, value=25.56):
        """  Corresponds to IDD field `Cooling Tower Design Inlet Air Wet-Bulb Temperature`

        """
        self["Cooling Tower Design Inlet Air Wet-Bulb Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerCondenserEnteringResetIdeal(DataObject):

    """ Corresponds to IDD object `SetpointManager:CondenserEnteringReset:Ideal`
        This setpoint manager determine the ideal optimum condenser entering water temperature
        setpoint for a given timestep.
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
                                        'default': u'Temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Temperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum lift',
                                       {'name': u'Minimum Lift',
                                        'pyname': u'minimum_lift',
                                        'default': 11.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'maximum condenser entering water temperature',
                                       {'name': u'Maximum Condenser Entering Water Temperature',
                                        'pyname': u'maximum_condenser_entering_water_temperature',
                                        'default': 32.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 5,
               'name': u'SetpointManager:CondenserEnteringReset:Ideal',
               'pyname': u'SetpointManagerCondenserEnteringResetIdeal',
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

        |  Default value: Temperature

        Args:
            value (str): value for IDD Field `Control Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_variable` or None if not set

        """
        return self["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """Corresponds to IDD field `Control Variable`"""
        self["Control Variable"] = value

    @property
    def minimum_lift(self):
        """field `Minimum Lift`

        |  Units: deltaC
        |  Default value: 11.1

        Args:
            value (float): value for IDD Field `Minimum Lift`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_lift` or None if not set

        """
        return self["Minimum Lift"]

    @minimum_lift.setter
    def minimum_lift(self, value=11.1):
        """Corresponds to IDD field `Minimum Lift`"""
        self["Minimum Lift"] = value

    @property
    def maximum_condenser_entering_water_temperature(self):
        """field `Maximum Condenser Entering Water Temperature`

        |  Units: C
        |  Default value: 32.0

        Args:
            value (float): value for IDD Field `Maximum Condenser Entering Water Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_condenser_entering_water_temperature` or None if not set

        """
        return self["Maximum Condenser Entering Water Temperature"]

    @maximum_condenser_entering_water_temperature.setter
    def maximum_condenser_entering_water_temperature(self, value=32.0):
        """Corresponds to IDD field `Maximum Condenser Entering Water
        Temperature`"""
        self["Maximum Condenser Entering Water Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerSingleZoneOneStageCooling(DataObject):

    """ Corresponds to IDD object `SetpointManager:SingleZone:OneStageCooling`
        This object can be used with CoilSystem:Cooling:DX to model on/off cycling control
        of single stage air systems. Setpoints are modulated to run coil full on or full off
        depending on zone conditions. Intended for use with ZoneControl:Thermostat:StagedDualSetpoint
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling stage on supply air setpoint temperature',
                                       {'name': u'Cooling Stage On Supply Air Setpoint Temperature',
                                        'pyname': u'cooling_stage_on_supply_air_setpoint_temperature',
                                        'default': -99.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'cooling stage off supply air setpoint temperature',
                                       {'name': u'Cooling Stage Off Supply Air Setpoint Temperature',
                                        'pyname': u'cooling_stage_off_supply_air_setpoint_temperature',
                                        'default': 99.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'control zone name',
                                       {'name': u'Control Zone Name',
                                        'pyname': u'control_zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:SingleZone:OneStageCooling',
               'pyname': u'SetpointManagerSingleZoneOneStageCooling',
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
    def cooling_stage_on_supply_air_setpoint_temperature(self):
        """field `Cooling Stage On Supply Air Setpoint Temperature`

        |  This is the setpoint value applied when cooling device is to cycle ON
        |  Units: C
        |  Default value: -99.0

        Args:
            value (float): value for IDD Field `Cooling Stage On Supply Air Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_stage_on_supply_air_setpoint_temperature` or None if not set

        """
        return self["Cooling Stage On Supply Air Setpoint Temperature"]

    @cooling_stage_on_supply_air_setpoint_temperature.setter
    def cooling_stage_on_supply_air_setpoint_temperature(self, value=-99.0):
        """Corresponds to IDD field `Cooling Stage On Supply Air Setpoint
        Temperature`"""
        self["Cooling Stage On Supply Air Setpoint Temperature"] = value

    @property
    def cooling_stage_off_supply_air_setpoint_temperature(self):
        """field `Cooling Stage Off Supply Air Setpoint Temperature`

        |  This is the setpoint value applied when cooling device is to cycle OFF
        |  Units: C
        |  Default value: 99.0

        Args:
            value (float): value for IDD Field `Cooling Stage Off Supply Air Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_stage_off_supply_air_setpoint_temperature` or None if not set

        """
        return self["Cooling Stage Off Supply Air Setpoint Temperature"]

    @cooling_stage_off_supply_air_setpoint_temperature.setter
    def cooling_stage_off_supply_air_setpoint_temperature(self, value=99.0):
        """Corresponds to IDD field `Cooling Stage Off Supply Air Setpoint
        Temperature`"""
        self["Cooling Stage Off Supply Air Setpoint Temperature"] = value

    @property
    def control_zone_name(self):
        """field `Control Zone Name`

        Args:
            value (str): value for IDD Field `Control Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_zone_name` or None if not set

        """
        return self["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """Corresponds to IDD field `Control Zone Name`"""
        self["Control Zone Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerSingleZoneOneStageHeating(DataObject):

    """ Corresponds to IDD object `SetpointManager:SingleZone:OneStageHeating`
        This object can be used with CoilSystem:Heating:DX, Coil:Heating:Gas,
        Coil:Heating:Electric to model on/off cycling control of single stage air systems.
        Setpoints are modulated to run coil full on or full off depending on zone conditions.
        Intended for use with ZoneControl:Thermostat:StagedDualSetpoint.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating stage on supply air setpoint temperature',
                                       {'name': u'Heating Stage On Supply Air Setpoint Temperature',
                                        'pyname': u'heating_stage_on_supply_air_setpoint_temperature',
                                        'default': 99.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'heating stage off supply air setpoint temperature',
                                       {'name': u'Heating Stage Off Supply Air Setpoint Temperature',
                                        'pyname': u'heating_stage_off_supply_air_setpoint_temperature',
                                        'default': -99.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'control zone name',
                                       {'name': u'Control Zone Name',
                                        'pyname': u'control_zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'setpoint node or nodelist name',
                                       {'name': u'Setpoint Node or NodeList Name',
                                        'pyname': u'setpoint_node_or_nodelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 0,
               'name': u'SetpointManager:SingleZone:OneStageHeating',
               'pyname': u'SetpointManagerSingleZoneOneStageHeating',
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
    def heating_stage_on_supply_air_setpoint_temperature(self):
        """field `Heating Stage On Supply Air Setpoint Temperature`

        |  This is the setpoint value applied when heating device is to cycle ON
        |  Units: C
        |  Default value: 99.0

        Args:
            value (float): value for IDD Field `Heating Stage On Supply Air Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_stage_on_supply_air_setpoint_temperature` or None if not set

        """
        return self["Heating Stage On Supply Air Setpoint Temperature"]

    @heating_stage_on_supply_air_setpoint_temperature.setter
    def heating_stage_on_supply_air_setpoint_temperature(self, value=99.0):
        """Corresponds to IDD field `Heating Stage On Supply Air Setpoint
        Temperature`"""
        self["Heating Stage On Supply Air Setpoint Temperature"] = value

    @property
    def heating_stage_off_supply_air_setpoint_temperature(self):
        """field `Heating Stage Off Supply Air Setpoint Temperature`

        |  This is the setpoint value applied when heating device is to cycle OFF
        |  Units: C
        |  Default value: -99.0

        Args:
            value (float): value for IDD Field `Heating Stage Off Supply Air Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_stage_off_supply_air_setpoint_temperature` or None if not set

        """
        return self["Heating Stage Off Supply Air Setpoint Temperature"]

    @heating_stage_off_supply_air_setpoint_temperature.setter
    def heating_stage_off_supply_air_setpoint_temperature(self, value=-99.0):
        """Corresponds to IDD field `Heating Stage Off Supply Air Setpoint
        Temperature`"""
        self["Heating Stage Off Supply Air Setpoint Temperature"] = value

    @property
    def control_zone_name(self):
        """field `Control Zone Name`

        Args:
            value (str): value for IDD Field `Control Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_zone_name` or None if not set

        """
        return self["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """Corresponds to IDD field `Control Zone Name`"""
        self["Control Zone Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """field `Setpoint Node or NodeList Name`

        |  Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set

        """
        return self["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node or NodeList Name`"""
        self["Setpoint Node or NodeList Name"] = value




class SetpointManagerReturnTemperatureChilledWater(DataObject):

    """ Corresponds to IDD object `SetpointManager:ReturnTemperature:ChilledWater`
        This setpoint manager is used to place a temperature setpoint on a plant supply
        outlet node based on a target return water setpoint. The setpoint manager attempts
        to achieve the desired return water temperature by adjusting the supply temperature
        setpoint based on the plant conditions at each system time step.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant loop supply outlet node',
                                       {'name': u'Plant Loop Supply Outlet Node',
                                        'pyname': u'plant_loop_supply_outlet_node',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant loop supply inlet node',
                                       {'name': u'Plant Loop Supply Inlet Node',
                                        'pyname': u'plant_loop_supply_inlet_node',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'minimum supply temperature setpoint',
                                       {'name': u'Minimum Supply Temperature Setpoint',
                                        'pyname': u'minimum_supply_temperature_setpoint',
                                        'default': 5.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum supply temperature setpoint',
                                       {'name': u'Maximum Supply Temperature Setpoint',
                                        'pyname': u'maximum_supply_temperature_setpoint',
                                        'default': 10.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'return temperature setpoint input type',
                                       {'name': u'Return Temperature Setpoint Input Type',
                                        'pyname': u'return_temperature_setpoint_input_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Constant',
                                                            u'Scheduled',
                                                            u'ReturnTemperatureSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'return temperature setpoint constant value',
                                       {'name': u'Return Temperature Setpoint Constant Value',
                                        'pyname': u'return_temperature_setpoint_constant_value',
                                        'default': 13.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'return temperature setpoint schedule name',
                                       {'name': u'Return Temperature Setpoint Schedule Name',
                                        'pyname': u'return_temperature_setpoint_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 7,
               'name': u'SetpointManager:ReturnTemperature:ChilledWater',
               'pyname': u'SetpointManagerReturnTemperatureChilledWater',
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
    def plant_loop_supply_outlet_node(self):
        """field `Plant Loop Supply Outlet Node`

        |  This is the name of the supply outlet node for the plant being controlled by this
        |  setpoint manager.  Typically this is where the setpoint will be actuated for
        |  supply equipment to control to, but not necessarily.  This setpoint manager will
        |  mine that information from the internal plant data structures.

        Args:
            value (str): value for IDD Field `Plant Loop Supply Outlet Node`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_loop_supply_outlet_node` or None if not set

        """
        return self["Plant Loop Supply Outlet Node"]

    @plant_loop_supply_outlet_node.setter
    def plant_loop_supply_outlet_node(self, value=None):
        """Corresponds to IDD field `Plant Loop Supply Outlet Node`"""
        self["Plant Loop Supply Outlet Node"] = value

    @property
    def plant_loop_supply_inlet_node(self):
        """field `Plant Loop Supply Inlet Node`

        |  This is the name of the supply inlet node for the plant being controlled with this
        |  setpoint manager. The temperature on this node is controlled by actuating the
        |  supply setpoint.

        Args:
            value (str): value for IDD Field `Plant Loop Supply Inlet Node`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_loop_supply_inlet_node` or None if not set

        """
        return self["Plant Loop Supply Inlet Node"]

    @plant_loop_supply_inlet_node.setter
    def plant_loop_supply_inlet_node(self, value=None):
        """Corresponds to IDD field `Plant Loop Supply Inlet Node`"""
        self["Plant Loop Supply Inlet Node"] = value

    @property
    def minimum_supply_temperature_setpoint(self):
        """field `Minimum Supply Temperature Setpoint`

        |  This is the minimum chilled water supply temperature setpoint.  This is also used as the default
        |  setpoint during no-load or negative-load conditions and during initialization.
        |  Units: C
        |  Default value: 5.0

        Args:
            value (float): value for IDD Field `Minimum Supply Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_supply_temperature_setpoint` or None if not set

        """
        return self["Minimum Supply Temperature Setpoint"]

    @minimum_supply_temperature_setpoint.setter
    def minimum_supply_temperature_setpoint(self, value=5.0):
        """Corresponds to IDD field `Minimum Supply Temperature Setpoint`"""
        self["Minimum Supply Temperature Setpoint"] = value

    @property
    def maximum_supply_temperature_setpoint(self):
        """field `Maximum Supply Temperature Setpoint`

        |  This is the maximum reset temperature for the chilled water supply.
        |  Units: C
        |  Default value: 10.0

        Args:
            value (float): value for IDD Field `Maximum Supply Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_temperature_setpoint` or None if not set

        """
        return self["Maximum Supply Temperature Setpoint"]

    @maximum_supply_temperature_setpoint.setter
    def maximum_supply_temperature_setpoint(self, value=10.0):
        """Corresponds to IDD field `Maximum Supply Temperature Setpoint`"""
        self["Maximum Supply Temperature Setpoint"] = value

    @property
    def return_temperature_setpoint_input_type(self):
        """field `Return Temperature Setpoint Input Type`

        |  This defines whether the chilled water return temperature target is constant,
        |  scheduled, or specified on the supply inlet node by a separate setpoint manager.

        Args:
            value (str): value for IDD Field `Return Temperature Setpoint Input Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `return_temperature_setpoint_input_type` or None if not set

        """
        return self["Return Temperature Setpoint Input Type"]

    @return_temperature_setpoint_input_type.setter
    def return_temperature_setpoint_input_type(self, value=None):
        """Corresponds to IDD field `Return Temperature Setpoint Input Type`"""
        self["Return Temperature Setpoint Input Type"] = value

    @property
    def return_temperature_setpoint_constant_value(self):
        """field `Return Temperature Setpoint Constant Value`

        |  This is the desired return temperature target, which is met by adjusting the
        |  supply temperature setpoint. This constant value is only used if
        |  the Design Chilled Water Return Temperature Input Type is Constant
        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `Return Temperature Setpoint Constant Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `return_temperature_setpoint_constant_value` or None if not set

        """
        return self["Return Temperature Setpoint Constant Value"]

    @return_temperature_setpoint_constant_value.setter
    def return_temperature_setpoint_constant_value(self, value=13.0):
        """Corresponds to IDD field `Return Temperature Setpoint Constant
        Value`"""
        self["Return Temperature Setpoint Constant Value"] = value

    @property
    def return_temperature_setpoint_schedule_name(self):
        """field `Return Temperature Setpoint Schedule Name`

        |  This is the desired return temperature target, which is met by adjusting the
        |  supply temperature setpoint. This is a schedule name to allow the return temperature
        |  target value to be scheduled.  This field is only used if
        |  the Design Chilled Water Return Temperature Input Type is Scheduled

        Args:
            value (str): value for IDD Field `Return Temperature Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `return_temperature_setpoint_schedule_name` or None if not set

        """
        return self["Return Temperature Setpoint Schedule Name"]

    @return_temperature_setpoint_schedule_name.setter
    def return_temperature_setpoint_schedule_name(self, value=None):
        """Corresponds to IDD field `Return Temperature Setpoint Schedule
        Name`"""
        self["Return Temperature Setpoint Schedule Name"] = value




class SetpointManagerReturnTemperatureHotWater(DataObject):

    """ Corresponds to IDD object `SetpointManager:ReturnTemperature:HotWater`
        This setpoint manager is used to place a temperature setpoint on a plant supply
        outlet node based on a target return water setpoint. The setpoint manager attempts
        to achieve the desired return water temperature by adjusting the supply temperature
        setpoint based on the plant conditions at each system time step.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant loop supply outlet node',
                                       {'name': u'Plant Loop Supply Outlet Node',
                                        'pyname': u'plant_loop_supply_outlet_node',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant loop supply inlet node',
                                       {'name': u'Plant Loop Supply Inlet Node',
                                        'pyname': u'plant_loop_supply_inlet_node',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'minimum supply temperature setpoint',
                                       {'name': u'Minimum Supply Temperature Setpoint',
                                        'pyname': u'minimum_supply_temperature_setpoint',
                                        'default': 77.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum supply temperature setpoint',
                                       {'name': u'Maximum Supply Temperature Setpoint',
                                        'pyname': u'maximum_supply_temperature_setpoint',
                                        'default': 82.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'return temperature setpoint input type',
                                       {'name': u'Return Temperature Setpoint Input Type',
                                        'pyname': u'return_temperature_setpoint_input_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Constant',
                                                            u'Scheduled',
                                                            u'ReturnTemperatureSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'return temperature setpoint constant value',
                                       {'name': u'Return Temperature Setpoint Constant Value',
                                        'pyname': u'return_temperature_setpoint_constant_value',
                                        'default': 71.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'return temperature setpoint schedule name',
                                       {'name': u'Return Temperature Setpoint Schedule Name',
                                        'pyname': u'return_temperature_setpoint_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Setpoint Managers',
               'min-fields': 7,
               'name': u'SetpointManager:ReturnTemperature:HotWater',
               'pyname': u'SetpointManagerReturnTemperatureHotWater',
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
    def plant_loop_supply_outlet_node(self):
        """field `Plant Loop Supply Outlet Node`

        |  This is the name of the supply outlet node for the plant being controlled by this
        |  setpoint manager.  Typically this is where the setpoint will be actuated for
        |  supply equipment to control to, but not necessarily.  This setpoint manager will
        |  mine that information from the internal plant data structures.

        Args:
            value (str): value for IDD Field `Plant Loop Supply Outlet Node`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_loop_supply_outlet_node` or None if not set

        """
        return self["Plant Loop Supply Outlet Node"]

    @plant_loop_supply_outlet_node.setter
    def plant_loop_supply_outlet_node(self, value=None):
        """Corresponds to IDD field `Plant Loop Supply Outlet Node`"""
        self["Plant Loop Supply Outlet Node"] = value

    @property
    def plant_loop_supply_inlet_node(self):
        """field `Plant Loop Supply Inlet Node`

        |  This is the name of the supply inlet node for the plant being controlled with this
        |  setpoint manager. The temperature on this node is controlled by actuating the
        |  supply setpoint.

        Args:
            value (str): value for IDD Field `Plant Loop Supply Inlet Node`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_loop_supply_inlet_node` or None if not set

        """
        return self["Plant Loop Supply Inlet Node"]

    @plant_loop_supply_inlet_node.setter
    def plant_loop_supply_inlet_node(self, value=None):
        """Corresponds to IDD field `Plant Loop Supply Inlet Node`"""
        self["Plant Loop Supply Inlet Node"] = value

    @property
    def minimum_supply_temperature_setpoint(self):
        """field `Minimum Supply Temperature Setpoint`

        |  This is the minimum reset temperature for the hot water supply.
        |  Units: C
        |  Default value: 77.0

        Args:
            value (float): value for IDD Field `Minimum Supply Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_supply_temperature_setpoint` or None if not set

        """
        return self["Minimum Supply Temperature Setpoint"]

    @minimum_supply_temperature_setpoint.setter
    def minimum_supply_temperature_setpoint(self, value=77.0):
        """Corresponds to IDD field `Minimum Supply Temperature Setpoint`"""
        self["Minimum Supply Temperature Setpoint"] = value

    @property
    def maximum_supply_temperature_setpoint(self):
        """field `Maximum Supply Temperature Setpoint`

        |  This is the maximum hot water supply temperature setpoint.  This is also used as the default
        |  setpoint during no-load or negative-load conditions and during initialization.
        |  Units: C
        |  Default value: 82.0

        Args:
            value (float): value for IDD Field `Maximum Supply Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_temperature_setpoint` or None if not set

        """
        return self["Maximum Supply Temperature Setpoint"]

    @maximum_supply_temperature_setpoint.setter
    def maximum_supply_temperature_setpoint(self, value=82.0):
        """Corresponds to IDD field `Maximum Supply Temperature Setpoint`"""
        self["Maximum Supply Temperature Setpoint"] = value

    @property
    def return_temperature_setpoint_input_type(self):
        """field `Return Temperature Setpoint Input Type`

        |  This defines whether the hot water return temperature target is constant,
        |  scheduled, or specified on the supply inlet node by a separate setpoint manager.

        Args:
            value (str): value for IDD Field `Return Temperature Setpoint Input Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `return_temperature_setpoint_input_type` or None if not set

        """
        return self["Return Temperature Setpoint Input Type"]

    @return_temperature_setpoint_input_type.setter
    def return_temperature_setpoint_input_type(self, value=None):
        """Corresponds to IDD field `Return Temperature Setpoint Input Type`"""
        self["Return Temperature Setpoint Input Type"] = value

    @property
    def return_temperature_setpoint_constant_value(self):
        """field `Return Temperature Setpoint Constant Value`

        |  This is the desired return temperature target, which is met by adjusting the
        |  supply temperature setpoint. This constant value is only used if
        |  the Design Hot Water Return Temperature Input Type is Constant
        |  Units: C
        |  Default value: 71.0

        Args:
            value (float): value for IDD Field `Return Temperature Setpoint Constant Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `return_temperature_setpoint_constant_value` or None if not set

        """
        return self["Return Temperature Setpoint Constant Value"]

    @return_temperature_setpoint_constant_value.setter
    def return_temperature_setpoint_constant_value(self, value=71.0):
        """Corresponds to IDD field `Return Temperature Setpoint Constant
        Value`"""
        self["Return Temperature Setpoint Constant Value"] = value

    @property
    def return_temperature_setpoint_schedule_name(self):
        """field `Return Temperature Setpoint Schedule Name`

        |  This is the desired return temperature target, which is met by adjusting the
        |  supply temperature setpoint. This is a schedule name to allow the return temperature
        |  target value to be scheduled.  This field is only used if
        |  the Design Hot Water Return Temperature Input Type is Scheduled

        Args:
            value (str): value for IDD Field `Return Temperature Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `return_temperature_setpoint_schedule_name` or None if not set

        """
        return self["Return Temperature Setpoint Schedule Name"]

    @return_temperature_setpoint_schedule_name.setter
    def return_temperature_setpoint_schedule_name(self, value=None):
        """Corresponds to IDD field `Return Temperature Setpoint Schedule
        Name`"""
        self["Return Temperature Setpoint Schedule Name"] = value


