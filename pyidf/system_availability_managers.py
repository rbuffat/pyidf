""" Data objects in group "System Availability Managers"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class AvailabilityManagerScheduled(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:Scheduled`
        Determines the availability of a loop or system: whether it is on or off.
        Schedule overrides fan/pump schedule.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 2,
               'name': u'AvailabilityManager:Scheduled',
               'pyname': u'AvailabilityManagerScheduled',
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




class AvailabilityManagerScheduledOn(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:ScheduledOn`
        Determines the availability of a loop or system: only controls the turn on action.
        Schedule overrides fan/pump schedule.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 2,
               'name': u'AvailabilityManager:ScheduledOn',
               'pyname': u'AvailabilityManagerScheduledOn',
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




class AvailabilityManagerScheduledOff(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:ScheduledOff`
        Determines the availability of a loop or system: only controls the turn off action.
        Schedule overrides fan/pump schedule.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 2,
               'name': u'AvailabilityManager:ScheduledOff',
               'pyname': u'AvailabilityManagerScheduledOff',
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




class AvailabilityManagerOptimumStart(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:OptimumStart`
        Determines the optimal start of HVAC systems before occupancy.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'applicability schedule name',
                                       {'name': u'Applicability Schedule Name',
                                        'pyname': u'applicability_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan schedule name',
                                       {'name': u'Fan Schedule Name',
                                        'pyname': u'fan_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control type',
                                       {'name': u'Control Type',
                                        'pyname': u'control_type',
                                        'default': u'ControlZone',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'StayOff',
                                                            u'ControlZone',
                                                            u'MaximumofZoneList'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control zone name',
                                       {'name': u'Control Zone Name',
                                        'pyname': u'control_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone list name',
                                       {'name': u'Zone List Name',
                                        'pyname': u'zone_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum value for optimum start time',
                                       {'name': u'Maximum Value for Optimum Start Time',
                                        'pyname': u'maximum_value_for_optimum_start_time',
                                        'default': 6.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'hr'}),
                                      (u'control algorithm',
                                       {'name': u'Control Algorithm',
                                        'pyname': u'control_algorithm',
                                        'default': u'AdaptiveASHRAE',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ConstantTemperatureGradient',
                                                            u'AdaptiveTemperatureGradient',
                                                            u'AdaptiveASHRAE',
                                                            u'ConstantStartTime'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'constant temperature gradient during cooling',
                                       {'name': u'Constant Temperature Gradient during Cooling',
                                        'pyname': u'constant_temperature_gradient_during_cooling',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC/hr'}),
                                      (u'constant temperature gradient during heating',
                                       {'name': u'Constant Temperature Gradient during Heating',
                                        'pyname': u'constant_temperature_gradient_during_heating',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC/hr'}),
                                      (u'initial temperature gradient during cooling',
                                       {'name': u'Initial Temperature Gradient during Cooling',
                                        'pyname': u'initial_temperature_gradient_during_cooling',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC/hr'}),
                                      (u'initial temperature gradient during heating',
                                       {'name': u'Initial Temperature Gradient during Heating',
                                        'pyname': u'initial_temperature_gradient_during_heating',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC/hr'}),
                                      (u'constant start time',
                                       {'name': u'Constant Start Time',
                                        'pyname': u'constant_start_time',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'number of previous days',
                                       {'name': u'Number of Previous Days',
                                        'pyname': u'number_of_previous_days',
                                        'default': 2,
                                        'maximum': 5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 2,
                                        'autocalculatable': False,
                                        'type': u'integer',
                                        'unit': u'days'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 0,
               'name': u'AvailabilityManager:OptimumStart',
               'pyname': u'AvailabilityManagerOptimumStart',
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
    def applicability_schedule_name(self):
        """field `Applicability Schedule Name`

        Args:
            value (str): value for IDD Field `Applicability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `applicability_schedule_name` or None if not set

        """
        return self["Applicability Schedule Name"]

    @applicability_schedule_name.setter
    def applicability_schedule_name(self, value=None):
        """Corresponds to IDD field `Applicability Schedule Name`"""
        self["Applicability Schedule Name"] = value

    @property
    def fan_schedule_name(self):
        """field `Fan Schedule Name`

        Args:
            value (str): value for IDD Field `Fan Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_schedule_name` or None if not set

        """
        return self["Fan Schedule Name"]

    @fan_schedule_name.setter
    def fan_schedule_name(self, value=None):
        """Corresponds to IDD field `Fan Schedule Name`"""
        self["Fan Schedule Name"] = value

    @property
    def control_type(self):
        """field `Control Type`

        |  Default value: ControlZone

        Args:
            value (str): value for IDD Field `Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_type` or None if not set

        """
        return self["Control Type"]

    @control_type.setter
    def control_type(self, value="ControlZone"):
        """Corresponds to IDD field `Control Type`"""
        self["Control Type"] = value

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
    def zone_list_name(self):
        """field `Zone List Name`

        Args:
            value (str): value for IDD Field `Zone List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_list_name` or None if not set

        """
        return self["Zone List Name"]

    @zone_list_name.setter
    def zone_list_name(self, value=None):
        """Corresponds to IDD field `Zone List Name`"""
        self["Zone List Name"] = value

    @property
    def maximum_value_for_optimum_start_time(self):
        """field `Maximum Value for Optimum Start Time`

        |  this is the maximum number of hours that a system can start before occupancy
        |  Units: hr
        |  Default value: 6.0

        Args:
            value (float): value for IDD Field `Maximum Value for Optimum Start Time`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_for_optimum_start_time` or None if not set

        """
        return self["Maximum Value for Optimum Start Time"]

    @maximum_value_for_optimum_start_time.setter
    def maximum_value_for_optimum_start_time(self, value=6.0):
        """Corresponds to IDD field `Maximum Value for Optimum Start Time`"""
        self["Maximum Value for Optimum Start Time"] = value

    @property
    def control_algorithm(self):
        """field `Control Algorithm`

        |  Default value: AdaptiveASHRAE

        Args:
            value (str): value for IDD Field `Control Algorithm`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_algorithm` or None if not set

        """
        return self["Control Algorithm"]

    @control_algorithm.setter
    def control_algorithm(self, value="AdaptiveASHRAE"):
        """Corresponds to IDD field `Control Algorithm`"""
        self["Control Algorithm"] = value

    @property
    def constant_temperature_gradient_during_cooling(self):
        """field `Constant Temperature Gradient during Cooling`

        |  Units: deltaC/hr

        Args:
            value (float): value for IDD Field `Constant Temperature Gradient during Cooling`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_temperature_gradient_during_cooling` or None if not set

        """
        return self["Constant Temperature Gradient during Cooling"]

    @constant_temperature_gradient_during_cooling.setter
    def constant_temperature_gradient_during_cooling(self, value=None):
        """Corresponds to IDD field `Constant Temperature Gradient during
        Cooling`"""
        self["Constant Temperature Gradient during Cooling"] = value

    @property
    def constant_temperature_gradient_during_heating(self):
        """field `Constant Temperature Gradient during Heating`

        |  Units: deltaC/hr

        Args:
            value (float): value for IDD Field `Constant Temperature Gradient during Heating`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_temperature_gradient_during_heating` or None if not set

        """
        return self["Constant Temperature Gradient during Heating"]

    @constant_temperature_gradient_during_heating.setter
    def constant_temperature_gradient_during_heating(self, value=None):
        """Corresponds to IDD field `Constant Temperature Gradient during
        Heating`"""
        self["Constant Temperature Gradient during Heating"] = value

    @property
    def initial_temperature_gradient_during_cooling(self):
        """field `Initial Temperature Gradient during Cooling`

        |  Units: deltaC/hr

        Args:
            value (float): value for IDD Field `Initial Temperature Gradient during Cooling`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_temperature_gradient_during_cooling` or None if not set

        """
        return self["Initial Temperature Gradient during Cooling"]

    @initial_temperature_gradient_during_cooling.setter
    def initial_temperature_gradient_during_cooling(self, value=None):
        """Corresponds to IDD field `Initial Temperature Gradient during
        Cooling`"""
        self["Initial Temperature Gradient during Cooling"] = value

    @property
    def initial_temperature_gradient_during_heating(self):
        """field `Initial Temperature Gradient during Heating`

        |  Units: deltaC/hr

        Args:
            value (float): value for IDD Field `Initial Temperature Gradient during Heating`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_temperature_gradient_during_heating` or None if not set

        """
        return self["Initial Temperature Gradient during Heating"]

    @initial_temperature_gradient_during_heating.setter
    def initial_temperature_gradient_during_heating(self, value=None):
        """Corresponds to IDD field `Initial Temperature Gradient during
        Heating`"""
        self["Initial Temperature Gradient during Heating"] = value

    @property
    def constant_start_time(self):
        """field `Constant Start Time`

        |  this is the number of hours before occupancy for a system
        |  Units: hr

        Args:
            value (float): value for IDD Field `Constant Start Time`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_start_time` or None if not set

        """
        return self["Constant Start Time"]

    @constant_start_time.setter
    def constant_start_time(self, value=None):
        """Corresponds to IDD field `Constant Start Time`"""
        self["Constant Start Time"] = value

    @property
    def number_of_previous_days(self):
        """field `Number of Previous Days`

        |  this is the number of days that their actual temperature
        |  gradients will be used in the AdaptiveTemperatureGradient method
        |  Units: days
        |  Default value: 2
        |  value >= 2
        |  value <= 5

        Args:
            value (int): value for IDD Field `Number of Previous Days`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_previous_days` or None if not set

        """
        return self["Number of Previous Days"]

    @number_of_previous_days.setter
    def number_of_previous_days(self, value=2):
        """Corresponds to IDD field `Number of Previous Days`"""
        self["Number of Previous Days"] = value




class AvailabilityManagerNightCycle(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:NightCycle`
        Determines the availability of a loop or system: whether it is on or off.
        Depending on zone temperatures, overrides Schedules and forces system Fans on.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'applicability schedule name',
                                       {'name': u'Applicability Schedule Name',
                                        'pyname': u'applicability_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan schedule name',
                                       {'name': u'Fan Schedule Name',
                                        'pyname': u'fan_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control type',
                                       {'name': u'Control Type',
                                        'pyname': u'control_type',
                                        'default': u'StayOff',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'StayOff',
                                                            u'CycleOnAny',
                                                            u'CycleOnControlZone',
                                                            u'CycleOnAnyZoneFansOnly'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermostat tolerance',
                                       {'name': u'Thermostat Tolerance',
                                        'pyname': u'thermostat_tolerance',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'cycling run time',
                                       {'name': u'Cycling Run Time',
                                        'pyname': u'cycling_run_time',
                                        'default': 3600.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u's'}),
                                      (u'control zone name',
                                       {'name': u'Control Zone Name',
                                        'pyname': u'control_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 6,
               'name': u'AvailabilityManager:NightCycle',
               'pyname': u'AvailabilityManagerNightCycle',
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
    def applicability_schedule_name(self):
        """field `Applicability Schedule Name`

        Args:
            value (str): value for IDD Field `Applicability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `applicability_schedule_name` or None if not set

        """
        return self["Applicability Schedule Name"]

    @applicability_schedule_name.setter
    def applicability_schedule_name(self, value=None):
        """Corresponds to IDD field `Applicability Schedule Name`"""
        self["Applicability Schedule Name"] = value

    @property
    def fan_schedule_name(self):
        """field `Fan Schedule Name`

        Args:
            value (str): value for IDD Field `Fan Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_schedule_name` or None if not set

        """
        return self["Fan Schedule Name"]

    @fan_schedule_name.setter
    def fan_schedule_name(self, value=None):
        """Corresponds to IDD field `Fan Schedule Name`"""
        self["Fan Schedule Name"] = value

    @property
    def control_type(self):
        """field `Control Type`

        |  When AvailabilityManager:NightCycle is used in the zone component availability
        |  manager assignment list, the key choices for Control Type would only be
        |  StayOff and CycleOnControlZone
        |  Default value: StayOff

        Args:
            value (str): value for IDD Field `Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_type` or None if not set

        """
        return self["Control Type"]

    @control_type.setter
    def control_type(self, value="StayOff"):
        """Corresponds to IDD field `Control Type`"""
        self["Control Type"] = value

    @property
    def thermostat_tolerance(self):
        """field `Thermostat Tolerance`

        |  Units: deltaC
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Thermostat Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermostat_tolerance` or None if not set

        """
        return self["Thermostat Tolerance"]

    @thermostat_tolerance.setter
    def thermostat_tolerance(self, value=1.0):
        """Corresponds to IDD field `Thermostat Tolerance`"""
        self["Thermostat Tolerance"] = value

    @property
    def cycling_run_time(self):
        """field `Cycling Run Time`

        |  Units: s
        |  Default value: 3600.0

        Args:
            value (float): value for IDD Field `Cycling Run Time`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cycling_run_time` or None if not set

        """
        return self["Cycling Run Time"]

    @cycling_run_time.setter
    def cycling_run_time(self, value=3600.0):
        """Corresponds to IDD field `Cycling Run Time`"""
        self["Cycling Run Time"] = value

    @property
    def control_zone_name(self):
        """field `Control Zone Name`

        |  When AvailabilityManager:NightCycle is used in the zone component availability
        |  manager assignment list, the Control Zone Name should be the name of the zone in which the
        |  zone component is.

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




class AvailabilityManagerDifferentialThermostat(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:DifferentialThermostat`
        Overrides fan/pump schedules depending on temperature difference between two nodes.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'hot node name',
                                       {'name': u'Hot Node Name',
                                        'pyname': u'hot_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'cold node name',
                                       {'name': u'Cold Node Name',
                                        'pyname': u'cold_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'temperature difference on limit',
                                       {'name': u'Temperature Difference On Limit',
                                        'pyname': u'temperature_difference_on_limit',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'temperature difference off limit',
                                       {'name': u'Temperature Difference Off Limit',
                                        'pyname': u'temperature_difference_off_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 0,
               'name': u'AvailabilityManager:DifferentialThermostat',
               'pyname': u'AvailabilityManagerDifferentialThermostat',
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
    def hot_node_name(self):
        """field `Hot Node Name`

        Args:
            value (str): value for IDD Field `Hot Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_node_name` or None if not set

        """
        return self["Hot Node Name"]

    @hot_node_name.setter
    def hot_node_name(self, value=None):
        """Corresponds to IDD field `Hot Node Name`"""
        self["Hot Node Name"] = value

    @property
    def cold_node_name(self):
        """field `Cold Node Name`

        Args:
            value (str): value for IDD Field `Cold Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cold_node_name` or None if not set

        """
        return self["Cold Node Name"]

    @cold_node_name.setter
    def cold_node_name(self, value=None):
        """Corresponds to IDD field `Cold Node Name`"""
        self["Cold Node Name"] = value

    @property
    def temperature_difference_on_limit(self):
        """field `Temperature Difference On Limit`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Temperature Difference On Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_difference_on_limit` or None if not set

        """
        return self["Temperature Difference On Limit"]

    @temperature_difference_on_limit.setter
    def temperature_difference_on_limit(self, value=None):
        """Corresponds to IDD field `Temperature Difference On Limit`"""
        self["Temperature Difference On Limit"] = value

    @property
    def temperature_difference_off_limit(self):
        """field `Temperature Difference Off Limit`

        |  Defaults to Temperature Difference On Limit.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Temperature Difference Off Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_difference_off_limit` or None if not set

        """
        return self["Temperature Difference Off Limit"]

    @temperature_difference_off_limit.setter
    def temperature_difference_off_limit(self, value=None):
        """Corresponds to IDD field `Temperature Difference Off Limit`"""
        self["Temperature Difference Off Limit"] = value




class AvailabilityManagerHighTemperatureTurnOff(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:HighTemperatureTurnOff`
        Overrides fan/pump schedules depending on temperature at sensor node.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'sensor node name',
                                       {'name': u'Sensor Node Name',
                                        'pyname': u'sensor_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'temperature',
                                       {'name': u'Temperature',
                                        'pyname': u'temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 0,
               'name': u'AvailabilityManager:HighTemperatureTurnOff',
               'pyname': u'AvailabilityManagerHighTemperatureTurnOff',
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
    def temperature(self):
        """field `Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature` or None if not set

        """
        return self["Temperature"]

    @temperature.setter
    def temperature(self, value=None):
        """Corresponds to IDD field `Temperature`"""
        self["Temperature"] = value




class AvailabilityManagerHighTemperatureTurnOn(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:HighTemperatureTurnOn`
        Overrides fan/pump schedules depending on temperature at sensor node.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'sensor node name',
                                       {'name': u'Sensor Node Name',
                                        'pyname': u'sensor_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'temperature',
                                       {'name': u'Temperature',
                                        'pyname': u'temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 0,
               'name': u'AvailabilityManager:HighTemperatureTurnOn',
               'pyname': u'AvailabilityManagerHighTemperatureTurnOn',
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
    def temperature(self):
        """field `Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature` or None if not set

        """
        return self["Temperature"]

    @temperature.setter
    def temperature(self, value=None):
        """Corresponds to IDD field `Temperature`"""
        self["Temperature"] = value




class AvailabilityManagerLowTemperatureTurnOff(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:LowTemperatureTurnOff`
        Overrides fan/pump schedules depending on temperature at sensor node.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'sensor node name',
                                       {'name': u'Sensor Node Name',
                                        'pyname': u'sensor_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'temperature',
                                       {'name': u'Temperature',
                                        'pyname': u'temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'applicability schedule name',
                                       {'name': u'Applicability Schedule Name',
                                        'pyname': u'applicability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 0,
               'name': u'AvailabilityManager:LowTemperatureTurnOff',
               'pyname': u'AvailabilityManagerLowTemperatureTurnOff',
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
    def temperature(self):
        """field `Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature` or None if not set

        """
        return self["Temperature"]

    @temperature.setter
    def temperature(self, value=None):
        """Corresponds to IDD field `Temperature`"""
        self["Temperature"] = value

    @property
    def applicability_schedule_name(self):
        """field `Applicability Schedule Name`

        |  If blank, defaults to always active

        Args:
            value (str): value for IDD Field `Applicability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `applicability_schedule_name` or None if not set

        """
        return self["Applicability Schedule Name"]

    @applicability_schedule_name.setter
    def applicability_schedule_name(self, value=None):
        """Corresponds to IDD field `Applicability Schedule Name`"""
        self["Applicability Schedule Name"] = value




class AvailabilityManagerLowTemperatureTurnOn(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:LowTemperatureTurnOn`
        Overrides fan/pump schedules depending on temperature at sensor node.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'sensor node name',
                                       {'name': u'Sensor Node Name',
                                        'pyname': u'sensor_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'temperature',
                                       {'name': u'Temperature',
                                        'pyname': u'temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 0,
               'name': u'AvailabilityManager:LowTemperatureTurnOn',
               'pyname': u'AvailabilityManagerLowTemperatureTurnOn',
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
    def temperature(self):
        """field `Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature` or None if not set

        """
        return self["Temperature"]

    @temperature.setter
    def temperature(self, value=None):
        """Corresponds to IDD field `Temperature`"""
        self["Temperature"] = value




class AvailabilityManagerNightVentilation(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:NightVentilation`
        depending on zone and outdoor conditions overrides fan schedule to do
        precooling with outdoor air
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'applicability schedule name',
                                       {'name': u'Applicability Schedule Name',
                                        'pyname': u'applicability_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan schedule name',
                                       {'name': u'Fan Schedule Name',
                                        'pyname': u'fan_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ventilation temperature schedule name',
                                       {'name': u'Ventilation Temperature Schedule Name',
                                        'pyname': u'ventilation_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ventilation temperature difference',
                                       {'name': u'Ventilation Temperature Difference',
                                        'pyname': u'ventilation_temperature_difference',
                                        'default': 2.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'ventilation temperature low limit',
                                       {'name': u'Ventilation Temperature Low Limit',
                                        'pyname': u'ventilation_temperature_low_limit',
                                        'default': 15.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'night venting flow fraction',
                                       {'name': u'Night Venting Flow Fraction',
                                        'pyname': u'night_venting_flow_fraction',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'control zone name',
                                       {'name': u'Control Zone Name',
                                        'pyname': u'control_zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 7,
               'name': u'AvailabilityManager:NightVentilation',
               'pyname': u'AvailabilityManagerNightVentilation',
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
    def applicability_schedule_name(self):
        """field `Applicability Schedule Name`

        Args:
            value (str): value for IDD Field `Applicability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `applicability_schedule_name` or None if not set

        """
        return self["Applicability Schedule Name"]

    @applicability_schedule_name.setter
    def applicability_schedule_name(self, value=None):
        """Corresponds to IDD field `Applicability Schedule Name`"""
        self["Applicability Schedule Name"] = value

    @property
    def fan_schedule_name(self):
        """field `Fan Schedule Name`

        Args:
            value (str): value for IDD Field `Fan Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_schedule_name` or None if not set

        """
        return self["Fan Schedule Name"]

    @fan_schedule_name.setter
    def fan_schedule_name(self, value=None):
        """Corresponds to IDD field `Fan Schedule Name`"""
        self["Fan Schedule Name"] = value

    @property
    def ventilation_temperature_schedule_name(self):
        """field `Ventilation Temperature Schedule Name`

        |  One zone temperature must be above this scheduled temperature
        |  for night ventilation to be enabled

        Args:
            value (str): value for IDD Field `Ventilation Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ventilation_temperature_schedule_name` or None if not set

        """
        return self["Ventilation Temperature Schedule Name"]

    @ventilation_temperature_schedule_name.setter
    def ventilation_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Ventilation Temperature Schedule Name`"""
        self["Ventilation Temperature Schedule Name"] = value

    @property
    def ventilation_temperature_difference(self):
        """field `Ventilation Temperature Difference`

        |  The outdoor air temperature minus the control zone temperature
        |  must be greater than the ventilation delta T
        |  Units: deltaC
        |  Default value: 2.0

        Args:
            value (float): value for IDD Field `Ventilation Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ventilation_temperature_difference` or None if not set

        """
        return self["Ventilation Temperature Difference"]

    @ventilation_temperature_difference.setter
    def ventilation_temperature_difference(self, value=2.0):
        """Corresponds to IDD field `Ventilation Temperature Difference`"""
        self["Ventilation Temperature Difference"] = value

    @property
    def ventilation_temperature_low_limit(self):
        """field `Ventilation Temperature Low Limit`

        |  Night ventilation is disabled if any conditioned zone served by
        |  the system falls below this temperature
        |  Units: C
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `Ventilation Temperature Low Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ventilation_temperature_low_limit` or None if not set

        """
        return self["Ventilation Temperature Low Limit"]

    @ventilation_temperature_low_limit.setter
    def ventilation_temperature_low_limit(self, value=15.0):
        """Corresponds to IDD field `Ventilation Temperature Low Limit`"""
        self["Ventilation Temperature Low Limit"] = value

    @property
    def night_venting_flow_fraction(self):
        """field `Night Venting Flow Fraction`

        |  the fraction (could be > 1) of the design system Flow Rate at which
        |  night ventilation will be done
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Night Venting Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `night_venting_flow_fraction` or None if not set

        """
        return self["Night Venting Flow Fraction"]

    @night_venting_flow_fraction.setter
    def night_venting_flow_fraction(self, value=1.0):
        """Corresponds to IDD field `Night Venting Flow Fraction`"""
        self["Night Venting Flow Fraction"] = value

    @property
    def control_zone_name(self):
        """field `Control Zone Name`

        |  When AvailabilityManager:NightVentilation is used in the zone component availability
        |  manager assignment list, the Control Zone Name should be the name of the zone in which the
        |  zone component is.

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




class AvailabilityManagerHybridVentilation(DataObject):

    """ Corresponds to IDD object `AvailabilityManager:HybridVentilation`
        Depending on zone and outdoor conditions overrides window/door opening controls
        to maximize natural ventilation and turn off an HVAC system when ventilation control
        conditions are met.
        This object (zone ventilation object name) has not been instrumented to work with
        global Zone or Zone List names option for Ventilation:DesignFlowRate.  In order to
        use, you must enter the single <Ventilation:DesignFlowRate> name in that
        field. If it is a part of a global ventilation assignment the name will be
        <Zone Name> <global Ventilation:DesignFlowRate> name.
        Currently, hybrid ventilation manager is restricted to one per zone. It can either be applied
        through the air loop or directly to the zone. If hybrid ventilation manager is applied to an
        air loop and one of the zones served by that air loop also has hybrid ventilation manager,
        then zone hybrid ventilation manager is disabled.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'hvac air loop name',
                                       {'name': u'HVAC Air Loop Name',
                                        'pyname': u'hvac_air_loop_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controlled zone name',
                                       {'name': u'Controlled Zone Name',
                                        'pyname': u'controlled_zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ventilation control mode schedule name',
                                       {'name': u'Ventilation Control Mode Schedule Name',
                                        'pyname': u'ventilation_control_mode_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'use weather file rain indicators',
                                       {'name': u'Use Weather File Rain Indicators',
                                        'pyname': u'use_weather_file_rain_indicators',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'maximum wind speed',
                                       {'name': u'Maximum Wind Speed',
                                        'pyname': u'maximum_wind_speed',
                                        'default': 40.0,
                                        'maximum': 40.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'minimum outdoor temperature',
                                       {'name': u'Minimum Outdoor Temperature',
                                        'pyname': u'minimum_outdoor_temperature',
                                        'default': -100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor temperature',
                                       {'name': u'Maximum Outdoor Temperature',
                                        'pyname': u'maximum_outdoor_temperature',
                                        'default': 100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum outdoor enthalpy',
                                       {'name': u'Minimum Outdoor Enthalpy',
                                        'pyname': u'minimum_outdoor_enthalpy',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 300000.0,
                                        'unit': u'J/kg'}),
                                      (u'maximum outdoor enthalpy',
                                       {'name': u'Maximum Outdoor Enthalpy',
                                        'pyname': u'maximum_outdoor_enthalpy',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 300000.0,
                                        'unit': u'J/kg'}),
                                      (u'minimum outdoor dewpoint',
                                       {'name': u'Minimum Outdoor Dewpoint',
                                        'pyname': u'minimum_outdoor_dewpoint',
                                        'default': -100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor dewpoint',
                                       {'name': u'Maximum Outdoor Dewpoint',
                                        'pyname': u'maximum_outdoor_dewpoint',
                                        'default': 100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum outdoor ventilation air schedule name',
                                       {'name': u'Minimum Outdoor Ventilation Air Schedule Name',
                                        'pyname': u'minimum_outdoor_ventilation_air_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'opening factor function of wind speed curve name',
                                       {'name': u'Opening Factor Function of Wind Speed Curve Name',
                                        'pyname': u'opening_factor_function_of_wind_speed_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'airflownetwork control type schedule name',
                                       {'name': u'AirflowNetwork Control Type Schedule Name',
                                        'pyname': u'airflownetwork_control_type_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'simple airflow control type schedule name',
                                       {'name': u'Simple Airflow Control Type Schedule Name',
                                        'pyname': u'simple_airflow_control_type_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zoneventilation object name',
                                       {'name': u'ZoneVentilation Object Name',
                                        'pyname': u'zoneventilation_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 13,
               'name': u'AvailabilityManager:HybridVentilation',
               'pyname': u'AvailabilityManagerHybridVentilation',
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

        |  Enter the name of an AirLoopHVAC or HVACTemplate:System:* object.
        |  If this field is left blank, hybrid ventilation managers will be
        |  simulated for zone equipment control

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
    def controlled_zone_name(self):
        """field `Controlled Zone Name`

        |  the controlled zone name should be a zone where a thermostat or humidistat is located
        |  served by an air primary loop.

        Args:
            value (str): value for IDD Field `Controlled Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controlled_zone_name` or None if not set

        """
        return self["Controlled Zone Name"]

    @controlled_zone_name.setter
    def controlled_zone_name(self, value=None):
        """Corresponds to IDD field `Controlled Zone Name`"""
        self["Controlled Zone Name"] = value

    @property
    def ventilation_control_mode_schedule_name(self):
        """field `Ventilation Control Mode Schedule Name`

        |  The Ventilation control mode contains appropriate integer control types.
        |  0 - uncontrolled (Natural ventilation and HVAC system are controlled by themselves)
        |  1 = Temperature control
        |  2 = Enthalpy control
        |  3 = Dewpoint control
        |  4 = Outdoor ventilation air control

        Args:
            value (str): value for IDD Field `Ventilation Control Mode Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ventilation_control_mode_schedule_name` or None if not set

        """
        return self["Ventilation Control Mode Schedule Name"]

    @ventilation_control_mode_schedule_name.setter
    def ventilation_control_mode_schedule_name(self, value=None):
        """Corresponds to IDD field `Ventilation Control Mode Schedule Name`"""
        self["Ventilation Control Mode Schedule Name"] = value

    @property
    def use_weather_file_rain_indicators(self):
        """field `Use Weather File Rain Indicators`

        |  If Yes, ventilation is shutoff when there is rain
        |  If No, there is no rain control
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Rain Indicators`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_rain_indicators` or None if not set

        """
        return self["Use Weather File Rain Indicators"]

    @use_weather_file_rain_indicators.setter
    def use_weather_file_rain_indicators(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Rain Indicators`"""
        self["Use Weather File Rain Indicators"] = value

    @property
    def maximum_wind_speed(self):
        """field `Maximum Wind Speed`

        |  this is the wind speed above which ventilation is shutoff
        |  Units: m/s
        |  Default value: 40.0
        |  value <= 40.0

        Args:
            value (float): value for IDD Field `Maximum Wind Speed`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_wind_speed` or None if not set

        """
        return self["Maximum Wind Speed"]

    @maximum_wind_speed.setter
    def maximum_wind_speed(self, value=40.0):
        """Corresponds to IDD field `Maximum Wind Speed`"""
        self["Maximum Wind Speed"] = value

    @property
    def minimum_outdoor_temperature(self):
        """field `Minimum Outdoor Temperature`

        |  this is the outdoor temperature below which ventilation is shutoff
        |  Units: C
        |  Default value: -100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Outdoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_temperature` or None if not set

        """
        return self["Minimum Outdoor Temperature"]

    @minimum_outdoor_temperature.setter
    def minimum_outdoor_temperature(self, value=-100.0):
        """Corresponds to IDD field `Minimum Outdoor Temperature`"""
        self["Minimum Outdoor Temperature"] = value

    @property
    def maximum_outdoor_temperature(self):
        """field `Maximum Outdoor Temperature`

        |  this is the outdoor temperature above which ventilation is shutoff
        |  Units: C
        |  Default value: 100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_temperature` or None if not set

        """
        return self["Maximum Outdoor Temperature"]

    @maximum_outdoor_temperature.setter
    def maximum_outdoor_temperature(self, value=100.0):
        """Corresponds to IDD field `Maximum Outdoor Temperature`"""
        self["Maximum Outdoor Temperature"] = value

    @property
    def minimum_outdoor_enthalpy(self):
        """field `Minimum Outdoor Enthalpy`

        |  this is the outdoor Enthalpy below which ventilation is shutoff
        |  Units: J/kg
        |  value < 300000.0

        Args:
            value (float): value for IDD Field `Minimum Outdoor Enthalpy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_enthalpy` or None if not set

        """
        return self["Minimum Outdoor Enthalpy"]

    @minimum_outdoor_enthalpy.setter
    def minimum_outdoor_enthalpy(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Enthalpy`"""
        self["Minimum Outdoor Enthalpy"] = value

    @property
    def maximum_outdoor_enthalpy(self):
        """field `Maximum Outdoor Enthalpy`

        |  this is the outdoor Enthalpy above which ventilation is shutoff
        |  Units: J/kg
        |  value < 300000.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Enthalpy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_enthalpy` or None if not set

        """
        return self["Maximum Outdoor Enthalpy"]

    @maximum_outdoor_enthalpy.setter
    def maximum_outdoor_enthalpy(self, value=None):
        """Corresponds to IDD field `Maximum Outdoor Enthalpy`"""
        self["Maximum Outdoor Enthalpy"] = value

    @property
    def minimum_outdoor_dewpoint(self):
        """field `Minimum Outdoor Dewpoint`

        |  this is the outdoor temperature below which ventilation is shutoff
        |  Applicable only if Ventilation Control Mode = 3
        |  Units: C
        |  Default value: -100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Outdoor Dewpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_dewpoint` or None if not set

        """
        return self["Minimum Outdoor Dewpoint"]

    @minimum_outdoor_dewpoint.setter
    def minimum_outdoor_dewpoint(self, value=-100.0):
        """Corresponds to IDD field `Minimum Outdoor Dewpoint`"""
        self["Minimum Outdoor Dewpoint"] = value

    @property
    def maximum_outdoor_dewpoint(self):
        """field `Maximum Outdoor Dewpoint`

        |  this is the outdoor dewpoint above which ventilation is shutoff
        |  Applicable only if Ventilation Control Mode = 3
        |  Units: C
        |  Default value: 100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dewpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_dewpoint` or None if not set

        """
        return self["Maximum Outdoor Dewpoint"]

    @maximum_outdoor_dewpoint.setter
    def maximum_outdoor_dewpoint(self, value=100.0):
        """Corresponds to IDD field `Maximum Outdoor Dewpoint`"""
        self["Maximum Outdoor Dewpoint"] = value

    @property
    def minimum_outdoor_ventilation_air_schedule_name(self):
        """field `Minimum Outdoor Ventilation Air Schedule Name`

        |  Used only if Ventilation Control Mode = 4

        Args:
            value (str): value for IDD Field `Minimum Outdoor Ventilation Air Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_outdoor_ventilation_air_schedule_name` or None if not set

        """
        return self["Minimum Outdoor Ventilation Air Schedule Name"]

    @minimum_outdoor_ventilation_air_schedule_name.setter
    def minimum_outdoor_ventilation_air_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Ventilation Air Schedule
        Name`"""
        self["Minimum Outdoor Ventilation Air Schedule Name"] = value

    @property
    def opening_factor_function_of_wind_speed_curve_name(self):
        """field `Opening Factor Function of Wind Speed Curve Name`

        |  linear curve = a + b*WS
        |  quadratic curve = a + b*WS + c*WS**2
        |  WS = wind speed (m/s)

        Args:
            value (str): value for IDD Field `Opening Factor Function of Wind Speed Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `opening_factor_function_of_wind_speed_curve_name` or None if not set

        """
        return self["Opening Factor Function of Wind Speed Curve Name"]

    @opening_factor_function_of_wind_speed_curve_name.setter
    def opening_factor_function_of_wind_speed_curve_name(self, value=None):
        """Corresponds to IDD field `Opening Factor Function of Wind Speed
        Curve Name`"""
        self["Opening Factor Function of Wind Speed Curve Name"] = value

    @property
    def airflownetwork_control_type_schedule_name(self):
        """field `AirflowNetwork Control Type Schedule Name`

        |  The schedule is used to incorporate operation of AirflowNetwork large opening
        |  objects and HVAC system operation.

        Args:
            value (str): value for IDD Field `AirflowNetwork Control Type Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `airflownetwork_control_type_schedule_name` or None if not set

        """
        return self["AirflowNetwork Control Type Schedule Name"]

    @airflownetwork_control_type_schedule_name.setter
    def airflownetwork_control_type_schedule_name(self, value=None):
        """Corresponds to IDD field `AirflowNetwork Control Type Schedule
        Name`"""
        self["AirflowNetwork Control Type Schedule Name"] = value

    @property
    def simple_airflow_control_type_schedule_name(self):
        """field `Simple Airflow Control Type Schedule Name`

        |  The schedule is used to incorporate operation of simple airflow objects and HVAC
        |  system operation.
        |  The simple airflow objects are Ventilation and Mixing only

        Args:
            value (str): value for IDD Field `Simple Airflow Control Type Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_airflow_control_type_schedule_name` or None if not set

        """
        return self["Simple Airflow Control Type Schedule Name"]

    @simple_airflow_control_type_schedule_name.setter
    def simple_airflow_control_type_schedule_name(self, value=None):
        """Corresponds to IDD field `Simple Airflow Control Type Schedule
        Name`"""
        self["Simple Airflow Control Type Schedule Name"] = value

    @property
    def zoneventilation_object_name(self):
        """field `ZoneVentilation Object Name`

        |  This field has not been instrumented to work with
        |  global Zone or Zone List names option for Ventilation:DesignFlowRate.  In order to
        |  use, you must enter the single <Ventilation:DesignFlowRate> name in this field.
        |  If it is a part of a global ventilation assignment the name will be
        |  <Zone Name> <global Ventilation:DesignFlowRate> name.
        |  The other ZoneVentilation:* and ZoneMixing objects controlled in the same AirLoopHVAC
        |  will work in the same way as this ventilation object.

        Args:
            value (str): value for IDD Field `ZoneVentilation Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zoneventilation_object_name` or None if not set

        """
        return self["ZoneVentilation Object Name"]

    @zoneventilation_object_name.setter
    def zoneventilation_object_name(self, value=None):
        """Corresponds to IDD field `ZoneVentilation Object Name`"""
        self["ZoneVentilation Object Name"] = value




class AvailabilityManagerAssignmentList(DataObject):

    """Corresponds to IDD object `AvailabilityManagerAssignmentList` Defines
    the applicable managers used for an AirLoopHVAC or PlantLoop.

    The priority of
    availability managers is based on a set of rules and are specific to the type of loop.
    The output from each availability manager is an availability status flag:
    NoAction, ForceOff, CycleOn, or CycleOnZoneFansOnly (used only for air loops).

    """
    _schema = {'extensible-fields': OrderedDict([(u'availability manager 1 object type',
                                                  {'name': u'Availability Manager 1 Object Type',
                                                   'pyname': u'availability_manager_1_object_type',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'accepted-values': [u'AvailabilityManager:Scheduled',
                                                                       u'AvailabilityManager:ScheduledOn',
                                                                       u'AvailabilityManager:ScheduledOff',
                                                                       u'AvailabilityManager:NightCycle',
                                                                       u'AvailabilityManager:DifferentialThermostat',
                                                                       u'AvailabilityManager:HighTemperatureTurnOff',
                                                                       u'AvailabilityManager:HighTemperatureTurnOn',
                                                                       u'AvailabilityManager:LowTemperatureTurnOff',
                                                                       u'AvailabilityManager:LowTemperatureTurnOn',
                                                                       u'AvailabilityManager:NightVentilation'],
                                                      'autocalculatable': False,
                                                      'type': 'alpha'}),
                                                 (u'availability manager 1 name',
                                                  {'name': u'Availability Manager 1 Name',
                                                   'pyname': u'availability_manager_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'System Availability Managers',
               'min-fields': 3,
               'name': u'AvailabilityManagerAssignmentList',
               'pyname': u'AvailabilityManagerAssignmentList',
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

    def add_extensible(self,
                       availability_manager_1_object_type=None,
                       availability_manager_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            availability_manager_1_object_type (str): value for IDD Field `Availability Manager 1 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            availability_manager_1_name (str): value for IDD Field `Availability Manager 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        availability_manager_1_object_type = self.check_value(
            "Availability Manager 1 Object Type",
            availability_manager_1_object_type)
        vals.append(availability_manager_1_object_type)
        availability_manager_1_name = self.check_value(
            "Availability Manager 1 Name",
            availability_manager_1_name)
        vals.append(availability_manager_1_name)
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


