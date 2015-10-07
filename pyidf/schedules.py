""" Data objects in group "Schedules"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ScheduleTypeLimits(DataObject):

    """Corresponds to IDD object `ScheduleTypeLimits` ScheduleTypeLimits
    specifies the data types and limits for the values contained in
    schedules."""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'lower limit value',
                                       {'name': u'Lower Limit Value',
                                        'pyname': u'lower_limit_value',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'upper limit value',
                                       {'name': u'Upper Limit Value',
                                        'pyname': u'upper_limit_value',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'numeric type',
                                       {'name': u'Numeric Type',
                                        'pyname': u'numeric_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Continuous',
                                                            u'Discrete'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'unit type',
                                       {'name': u'Unit Type',
                                        'pyname': u'unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'DeltaTemperature',
                                                            u'PrecipitationRate',
                                                            u'Angle',
                                                            u'ConvectionCoefficient',
                                                            u'ActivityLevel',
                                                            u'Velocity',
                                                            u'Capacity',
                                                            u'Power',
                                                            u'Availability',
                                                            u'Percent',
                                                            u'Control',
                                                            u'Mode'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Schedules',
               'min-fields': 0,
               'name': u'ScheduleTypeLimits',
               'pyname': u'ScheduleTypeLimits',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  used to validate schedule types in various schedule objects

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
    def lower_limit_value(self):
        """field `Lower Limit Value`

        |  lower limit (real or integer) for the Schedule Type.  e.g. if fraction, this is 0.0
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Lower Limit Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `lower_limit_value` or None if not set

        """
        return self["Lower Limit Value"]

    @lower_limit_value.setter
    def lower_limit_value(self, value=None):
        """Corresponds to IDD field `Lower Limit Value`"""
        self["Lower Limit Value"] = value

    @property
    def upper_limit_value(self):
        """field `Upper Limit Value`

        |  upper limit (real or integer) for the Schedule Type.  e.g. if fraction, this is 1.0
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Upper Limit Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `upper_limit_value` or None if not set

        """
        return self["Upper Limit Value"]

    @upper_limit_value.setter
    def upper_limit_value(self, value=None):
        """Corresponds to IDD field `Upper Limit Value`"""
        self["Upper Limit Value"] = value

    @property
    def numeric_type(self):
        """field `Numeric Type`

        |  Numeric type is either Continuous (all numbers within the min and
        |  max are valid or Discrete (only integer numbers between min and
        |  max are valid.  (Could also allow REAL and INTEGER to mean the
        |  same things)

        Args:
            value (str): value for IDD Field `Numeric Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `numeric_type` or None if not set

        """
        return self["Numeric Type"]

    @numeric_type.setter
    def numeric_type(self, value=None):
        """Corresponds to IDD field `Numeric Type`"""
        self["Numeric Type"] = value

    @property
    def unit_type(self):
        """field `Unit Type`

        |  Temperature (C or F)
        |  DeltaTemperature (C or F)
        |  PrecipitationRate (m/hr or ft/hr)
        |  Angle (degrees)
        |  Convection Coefficient (W/m2-K or Btu/sqft-hr-F)
        |  Activity Level (W/person)
        |  Velocity (m/s or ft/min)
        |  Capacity (W or Btu/h)
        |  Power (W)
        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Unit Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `unit_type` or None if not set

        """
        return self["Unit Type"]

    @unit_type.setter
    def unit_type(self, value="Dimensionless"):
        """Corresponds to IDD field `Unit Type`"""
        self["Unit Type"] = value




class ScheduleDayHourly(DataObject):

    """ Corresponds to IDD object `Schedule:Day:Hourly`
        A Schedule:Day:Hourly contains 24 values for each hour of the day.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule type limits name',
                                       {'name': u'Schedule Type Limits Name',
                                        'pyname': u'schedule_type_limits_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hour 1',
                                       {'name': u'Hour 1',
                                        'pyname': u'hour_1',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 2',
                                       {'name': u'Hour 2',
                                        'pyname': u'hour_2',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 3',
                                       {'name': u'Hour 3',
                                        'pyname': u'hour_3',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 4',
                                       {'name': u'Hour 4',
                                        'pyname': u'hour_4',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 5',
                                       {'name': u'Hour 5',
                                        'pyname': u'hour_5',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 6',
                                       {'name': u'Hour 6',
                                        'pyname': u'hour_6',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 7',
                                       {'name': u'Hour 7',
                                        'pyname': u'hour_7',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 8',
                                       {'name': u'Hour 8',
                                        'pyname': u'hour_8',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 9',
                                       {'name': u'Hour 9',
                                        'pyname': u'hour_9',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 10',
                                       {'name': u'Hour 10',
                                        'pyname': u'hour_10',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 11',
                                       {'name': u'Hour 11',
                                        'pyname': u'hour_11',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 12',
                                       {'name': u'Hour 12',
                                        'pyname': u'hour_12',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 13',
                                       {'name': u'Hour 13',
                                        'pyname': u'hour_13',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 14',
                                       {'name': u'Hour 14',
                                        'pyname': u'hour_14',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 15',
                                       {'name': u'Hour 15',
                                        'pyname': u'hour_15',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 16',
                                       {'name': u'Hour 16',
                                        'pyname': u'hour_16',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 17',
                                       {'name': u'Hour 17',
                                        'pyname': u'hour_17',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 18',
                                       {'name': u'Hour 18',
                                        'pyname': u'hour_18',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 19',
                                       {'name': u'Hour 19',
                                        'pyname': u'hour_19',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 20',
                                       {'name': u'Hour 20',
                                        'pyname': u'hour_20',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 21',
                                       {'name': u'Hour 21',
                                        'pyname': u'hour_21',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 22',
                                       {'name': u'Hour 22',
                                        'pyname': u'hour_22',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 23',
                                       {'name': u'Hour 23',
                                        'pyname': u'hour_23',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'hour 24',
                                       {'name': u'Hour 24',
                                        'pyname': u'hour_24',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Schedules',
               'min-fields': 26,
               'name': u'Schedule:Day:Hourly',
               'pyname': u'ScheduleDayHourly',
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
    def schedule_type_limits_name(self):
        """field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set

        """
        return self["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """Corresponds to IDD field `Schedule Type Limits Name`"""
        self["Schedule Type Limits Name"] = value

    @property
    def hour_1(self):
        """field `Hour 1`

        Args:
            value (float): value for IDD Field `Hour 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_1` or None if not set

        """
        return self["Hour 1"]

    @hour_1.setter
    def hour_1(self, value=None):
        """Corresponds to IDD field `Hour 1`"""
        self["Hour 1"] = value

    @property
    def hour_2(self):
        """field `Hour 2`

        Args:
            value (float): value for IDD Field `Hour 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_2` or None if not set

        """
        return self["Hour 2"]

    @hour_2.setter
    def hour_2(self, value=None):
        """Corresponds to IDD field `Hour 2`"""
        self["Hour 2"] = value

    @property
    def hour_3(self):
        """field `Hour 3`

        Args:
            value (float): value for IDD Field `Hour 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_3` or None if not set

        """
        return self["Hour 3"]

    @hour_3.setter
    def hour_3(self, value=None):
        """Corresponds to IDD field `Hour 3`"""
        self["Hour 3"] = value

    @property
    def hour_4(self):
        """field `Hour 4`

        Args:
            value (float): value for IDD Field `Hour 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_4` or None if not set

        """
        return self["Hour 4"]

    @hour_4.setter
    def hour_4(self, value=None):
        """Corresponds to IDD field `Hour 4`"""
        self["Hour 4"] = value

    @property
    def hour_5(self):
        """field `Hour 5`

        Args:
            value (float): value for IDD Field `Hour 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_5` or None if not set

        """
        return self["Hour 5"]

    @hour_5.setter
    def hour_5(self, value=None):
        """Corresponds to IDD field `Hour 5`"""
        self["Hour 5"] = value

    @property
    def hour_6(self):
        """field `Hour 6`

        Args:
            value (float): value for IDD Field `Hour 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_6` or None if not set

        """
        return self["Hour 6"]

    @hour_6.setter
    def hour_6(self, value=None):
        """Corresponds to IDD field `Hour 6`"""
        self["Hour 6"] = value

    @property
    def hour_7(self):
        """field `Hour 7`

        Args:
            value (float): value for IDD Field `Hour 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_7` or None if not set

        """
        return self["Hour 7"]

    @hour_7.setter
    def hour_7(self, value=None):
        """Corresponds to IDD field `Hour 7`"""
        self["Hour 7"] = value

    @property
    def hour_8(self):
        """field `Hour 8`

        Args:
            value (float): value for IDD Field `Hour 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_8` or None if not set

        """
        return self["Hour 8"]

    @hour_8.setter
    def hour_8(self, value=None):
        """Corresponds to IDD field `Hour 8`"""
        self["Hour 8"] = value

    @property
    def hour_9(self):
        """field `Hour 9`

        Args:
            value (float): value for IDD Field `Hour 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_9` or None if not set

        """
        return self["Hour 9"]

    @hour_9.setter
    def hour_9(self, value=None):
        """Corresponds to IDD field `Hour 9`"""
        self["Hour 9"] = value

    @property
    def hour_10(self):
        """field `Hour 10`

        Args:
            value (float): value for IDD Field `Hour 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_10` or None if not set

        """
        return self["Hour 10"]

    @hour_10.setter
    def hour_10(self, value=None):
        """Corresponds to IDD field `Hour 10`"""
        self["Hour 10"] = value

    @property
    def hour_11(self):
        """field `Hour 11`

        Args:
            value (float): value for IDD Field `Hour 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_11` or None if not set

        """
        return self["Hour 11"]

    @hour_11.setter
    def hour_11(self, value=None):
        """Corresponds to IDD field `Hour 11`"""
        self["Hour 11"] = value

    @property
    def hour_12(self):
        """field `Hour 12`

        Args:
            value (float): value for IDD Field `Hour 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_12` or None if not set

        """
        return self["Hour 12"]

    @hour_12.setter
    def hour_12(self, value=None):
        """Corresponds to IDD field `Hour 12`"""
        self["Hour 12"] = value

    @property
    def hour_13(self):
        """field `Hour 13`

        Args:
            value (float): value for IDD Field `Hour 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_13` or None if not set

        """
        return self["Hour 13"]

    @hour_13.setter
    def hour_13(self, value=None):
        """Corresponds to IDD field `Hour 13`"""
        self["Hour 13"] = value

    @property
    def hour_14(self):
        """field `Hour 14`

        Args:
            value (float): value for IDD Field `Hour 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_14` or None if not set

        """
        return self["Hour 14"]

    @hour_14.setter
    def hour_14(self, value=None):
        """Corresponds to IDD field `Hour 14`"""
        self["Hour 14"] = value

    @property
    def hour_15(self):
        """field `Hour 15`

        Args:
            value (float): value for IDD Field `Hour 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_15` or None if not set

        """
        return self["Hour 15"]

    @hour_15.setter
    def hour_15(self, value=None):
        """Corresponds to IDD field `Hour 15`"""
        self["Hour 15"] = value

    @property
    def hour_16(self):
        """field `Hour 16`

        Args:
            value (float): value for IDD Field `Hour 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_16` or None if not set

        """
        return self["Hour 16"]

    @hour_16.setter
    def hour_16(self, value=None):
        """Corresponds to IDD field `Hour 16`"""
        self["Hour 16"] = value

    @property
    def hour_17(self):
        """field `Hour 17`

        Args:
            value (float): value for IDD Field `Hour 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_17` or None if not set

        """
        return self["Hour 17"]

    @hour_17.setter
    def hour_17(self, value=None):
        """Corresponds to IDD field `Hour 17`"""
        self["Hour 17"] = value

    @property
    def hour_18(self):
        """field `Hour 18`

        Args:
            value (float): value for IDD Field `Hour 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_18` or None if not set

        """
        return self["Hour 18"]

    @hour_18.setter
    def hour_18(self, value=None):
        """Corresponds to IDD field `Hour 18`"""
        self["Hour 18"] = value

    @property
    def hour_19(self):
        """field `Hour 19`

        Args:
            value (float): value for IDD Field `Hour 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_19` or None if not set

        """
        return self["Hour 19"]

    @hour_19.setter
    def hour_19(self, value=None):
        """Corresponds to IDD field `Hour 19`"""
        self["Hour 19"] = value

    @property
    def hour_20(self):
        """field `Hour 20`

        Args:
            value (float): value for IDD Field `Hour 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_20` or None if not set

        """
        return self["Hour 20"]

    @hour_20.setter
    def hour_20(self, value=None):
        """Corresponds to IDD field `Hour 20`"""
        self["Hour 20"] = value

    @property
    def hour_21(self):
        """field `Hour 21`

        Args:
            value (float): value for IDD Field `Hour 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_21` or None if not set

        """
        return self["Hour 21"]

    @hour_21.setter
    def hour_21(self, value=None):
        """Corresponds to IDD field `Hour 21`"""
        self["Hour 21"] = value

    @property
    def hour_22(self):
        """field `Hour 22`

        Args:
            value (float): value for IDD Field `Hour 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_22` or None if not set

        """
        return self["Hour 22"]

    @hour_22.setter
    def hour_22(self, value=None):
        """Corresponds to IDD field `Hour 22`"""
        self["Hour 22"] = value

    @property
    def hour_23(self):
        """field `Hour 23`

        Args:
            value (float): value for IDD Field `Hour 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_23` or None if not set

        """
        return self["Hour 23"]

    @hour_23.setter
    def hour_23(self, value=None):
        """Corresponds to IDD field `Hour 23`"""
        self["Hour 23"] = value

    @property
    def hour_24(self):
        """field `Hour 24`

        Args:
            value (float): value for IDD Field `Hour 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hour_24` or None if not set

        """
        return self["Hour 24"]

    @hour_24.setter
    def hour_24(self, value=None):
        """Corresponds to IDD field `Hour 24`"""
        self["Hour 24"] = value




class ScheduleDayInterval(DataObject):

    """ Corresponds to IDD object `Schedule:Day:Interval`
        A Schedule:Day:Interval contains a full day of values with specified end times for each value
        Currently, is set up to allow for 10 minute intervals for an entire day.
    """
    _schema = {'extensible-fields': OrderedDict([(u'time 1',
                                                  {'name': u'Time 1',
                                                   'pyname': u'time_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'alpha',
                                                   'unit': u'hh:mm'}),
                                                 (u'value until time 1',
                                                  {'name': u'Value Until Time 1',
                                                   'pyname': u'value_until_time_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'real'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule type limits name',
                                       {'name': u'Schedule Type Limits Name',
                                        'pyname': u'schedule_type_limits_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'interpolate to timestep',
                                       {'name': u'Interpolate to Timestep',
                                        'pyname': u'interpolate_to_timestep',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Schedules',
               'min-fields': 5,
               'name': u'Schedule:Day:Interval',
               'pyname': u'ScheduleDayInterval',
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
    def schedule_type_limits_name(self):
        """field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set

        """
        return self["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """Corresponds to IDD field `Schedule Type Limits Name`"""
        self["Schedule Type Limits Name"] = value

    @property
    def interpolate_to_timestep(self):
        """field `Interpolate to Timestep`

        |  when the interval does not match the user specified timestep a Yes choice will average between the intervals request (to
        |  timestep resolution.  a No choice will use the interval value at the simulation timestep without regard to if it matches
        |  the boundary or not.
        |  Default value: No

        Args:
            value (str): value for IDD Field `Interpolate to Timestep`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `interpolate_to_timestep` or None if not set

        """
        return self["Interpolate to Timestep"]

    @interpolate_to_timestep.setter
    def interpolate_to_timestep(self, value="No"):
        """Corresponds to IDD field `Interpolate to Timestep`"""
        self["Interpolate to Timestep"] = value

    def add_extensible(self,
                       time_1=None,
                       value_until_time_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            time_1 (str): value for IDD Field `Time 1`
                Units: hh:mm
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            value_until_time_1 (float): value for IDD Field `Value Until Time 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        time_1 = self.check_value("Time 1", time_1)
        vals.append(time_1)
        value_until_time_1 = self.check_value(
            "Value Until Time 1",
            value_until_time_1)
        vals.append(value_until_time_1)
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




class ScheduleDayList(DataObject):

    """ Corresponds to IDD object `Schedule:Day:List`
        Schedule:Day:List will allow the user to list 24 hours worth of values, which can be sub-hourly in nature.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule type limits name',
                                       {'name': u'Schedule Type Limits Name',
                                        'pyname': u'schedule_type_limits_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'interpolate to timestep',
                                       {'name': u'Interpolate to Timestep',
                                        'pyname': u'interpolate_to_timestep',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minutes per item',
                                       {'name': u'Minutes per Item',
                                        'pyname': u'minutes_per_item',
                                        'maximum': 60,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      ('value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3',
                                       {'name': 'Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3',
                                        'pyname': 'value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Schedules',
               'min-fields': 5,
               'name': u'Schedule:Day:List',
               'pyname': u'ScheduleDayList',
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
    def schedule_type_limits_name(self):
        """field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set

        """
        return self["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """Corresponds to IDD field `Schedule Type Limits Name`"""
        self["Schedule Type Limits Name"] = value

    @property
    def interpolate_to_timestep(self):
        """field `Interpolate to Timestep`

        |  when the interval does not match the user specified timestep a "Yes" choice will average between the intervals request (to
        |  timestep resolution.  a "No" choice will use the interval value at the simulation timestep without regard to if it matches
        |  the boundary or not.
        |  Default value: No

        Args:
            value (str): value for IDD Field `Interpolate to Timestep`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `interpolate_to_timestep` or None if not set

        """
        return self["Interpolate to Timestep"]

    @interpolate_to_timestep.setter
    def interpolate_to_timestep(self, value="No"):
        """Corresponds to IDD field `Interpolate to Timestep`"""
        self["Interpolate to Timestep"] = value

    @property
    def minutes_per_item(self):
        """field `Minutes per Item`

        |  Must be evenly divisible into 60
        |  value >= 1
        |  value <= 60

        Args:
            value (int): value for IDD Field `Minutes per Item`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `minutes_per_item` or None if not set

        """
        return self["Minutes per Item"]

    @minutes_per_item.setter
    def minutes_per_item(self, value=None):
        """Corresponds to IDD field `Minutes per Item`"""
        self["Minutes per Item"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3`

        Args:
            value (float): value for IDD Field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def value_1_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "Value 1 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value




class ScheduleWeekDaily(DataObject):

    """ Corresponds to IDD object `Schedule:Week:Daily`
        A Schedule:Week:Daily contains 12 Schedule:Day:Hourly objects, one for each day type.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'sunday schedule:day name',
                                       {'name': u'Sunday Schedule:Day Name',
                                        'pyname': u'sunday_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'monday schedule:day name',
                                       {'name': u'Monday Schedule:Day Name',
                                        'pyname': u'monday_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'tuesday schedule:day name',
                                       {'name': u'Tuesday Schedule:Day Name',
                                        'pyname': u'tuesday_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wednesday schedule:day name',
                                       {'name': u'Wednesday Schedule:Day Name',
                                        'pyname': u'wednesday_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'thursday schedule:day name',
                                       {'name': u'Thursday Schedule:Day Name',
                                        'pyname': u'thursday_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'friday schedule:day name',
                                       {'name': u'Friday Schedule:Day Name',
                                        'pyname': u'friday_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'saturday schedule:day name',
                                       {'name': u'Saturday Schedule:Day Name',
                                        'pyname': u'saturday_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'holiday schedule:day name',
                                       {'name': u'Holiday Schedule:Day Name',
                                        'pyname': u'holiday_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'summerdesignday schedule:day name',
                                       {'name': u'SummerDesignDay Schedule:Day Name',
                                        'pyname': u'summerdesignday_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'winterdesignday schedule:day name',
                                       {'name': u'WinterDesignDay Schedule:Day Name',
                                        'pyname': u'winterdesignday_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'customday1 schedule:day name',
                                       {'name': u'CustomDay1 Schedule:Day Name',
                                        'pyname': u'customday1_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'customday2 schedule:day name',
                                       {'name': u'CustomDay2 Schedule:Day Name',
                                        'pyname': u'customday2_scheduleday_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Schedules',
               'min-fields': 13,
               'name': u'Schedule:Week:Daily',
               'pyname': u'ScheduleWeekDaily',
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
    def sunday_scheduleday_name(self):
        """field `Sunday Schedule:Day Name`


        Args:
            value (str): value for IDD Field `Sunday Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `sunday_scheduleday_name` or None if not set
        """
        return self["Sunday Schedule:Day Name"]

    @sunday_scheduleday_name.setter
    def sunday_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `Sunday Schedule:Day Name`

        """
        self["Sunday Schedule:Day Name"] = value

    @property
    def monday_scheduleday_name(self):
        """field `Monday Schedule:Day Name`


        Args:
            value (str): value for IDD Field `Monday Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `monday_scheduleday_name` or None if not set
        """
        return self["Monday Schedule:Day Name"]

    @monday_scheduleday_name.setter
    def monday_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `Monday Schedule:Day Name`

        """
        self["Monday Schedule:Day Name"] = value

    @property
    def tuesday_scheduleday_name(self):
        """field `Tuesday Schedule:Day Name`


        Args:
            value (str): value for IDD Field `Tuesday Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tuesday_scheduleday_name` or None if not set
        """
        return self["Tuesday Schedule:Day Name"]

    @tuesday_scheduleday_name.setter
    def tuesday_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `Tuesday Schedule:Day Name`

        """
        self["Tuesday Schedule:Day Name"] = value

    @property
    def wednesday_scheduleday_name(self):
        """field `Wednesday Schedule:Day Name`


        Args:
            value (str): value for IDD Field `Wednesday Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wednesday_scheduleday_name` or None if not set
        """
        return self["Wednesday Schedule:Day Name"]

    @wednesday_scheduleday_name.setter
    def wednesday_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `Wednesday Schedule:Day Name`

        """
        self["Wednesday Schedule:Day Name"] = value

    @property
    def thursday_scheduleday_name(self):
        """field `Thursday Schedule:Day Name`


        Args:
            value (str): value for IDD Field `Thursday Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thursday_scheduleday_name` or None if not set
        """
        return self["Thursday Schedule:Day Name"]

    @thursday_scheduleday_name.setter
    def thursday_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `Thursday Schedule:Day Name`

        """
        self["Thursday Schedule:Day Name"] = value

    @property
    def friday_scheduleday_name(self):
        """field `Friday Schedule:Day Name`


        Args:
            value (str): value for IDD Field `Friday Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `friday_scheduleday_name` or None if not set
        """
        return self["Friday Schedule:Day Name"]

    @friday_scheduleday_name.setter
    def friday_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `Friday Schedule:Day Name`

        """
        self["Friday Schedule:Day Name"] = value

    @property
    def saturday_scheduleday_name(self):
        """field `Saturday Schedule:Day Name`


        Args:
            value (str): value for IDD Field `Saturday Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `saturday_scheduleday_name` or None if not set
        """
        return self["Saturday Schedule:Day Name"]

    @saturday_scheduleday_name.setter
    def saturday_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `Saturday Schedule:Day Name`

        """
        self["Saturday Schedule:Day Name"] = value

    @property
    def holiday_scheduleday_name(self):
        """field `Holiday Schedule:Day Name`


        Args:
            value (str): value for IDD Field `Holiday Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `holiday_scheduleday_name` or None if not set
        """
        return self["Holiday Schedule:Day Name"]

    @holiday_scheduleday_name.setter
    def holiday_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `Holiday Schedule:Day Name`

        """
        self["Holiday Schedule:Day Name"] = value

    @property
    def summerdesignday_scheduleday_name(self):
        """field `SummerDesignDay Schedule:Day Name`


        Args:
            value (str): value for IDD Field `SummerDesignDay Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `summerdesignday_scheduleday_name` or None if not set
        """
        return self["SummerDesignDay Schedule:Day Name"]

    @summerdesignday_scheduleday_name.setter
    def summerdesignday_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `SummerDesignDay Schedule:Day Name`

        """
        self["SummerDesignDay Schedule:Day Name"] = value

    @property
    def winterdesignday_scheduleday_name(self):
        """field `WinterDesignDay Schedule:Day Name`


        Args:
            value (str): value for IDD Field `WinterDesignDay Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `winterdesignday_scheduleday_name` or None if not set
        """
        return self["WinterDesignDay Schedule:Day Name"]

    @winterdesignday_scheduleday_name.setter
    def winterdesignday_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `WinterDesignDay Schedule:Day Name`

        """
        self["WinterDesignDay Schedule:Day Name"] = value

    @property
    def customday1_scheduleday_name(self):
        """field `CustomDay1 Schedule:Day Name`


        Args:
            value (str): value for IDD Field `CustomDay1 Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `customday1_scheduleday_name` or None if not set
        """
        return self["CustomDay1 Schedule:Day Name"]

    @customday1_scheduleday_name.setter
    def customday1_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `CustomDay1 Schedule:Day Name`

        """
        self["CustomDay1 Schedule:Day Name"] = value

    @property
    def customday2_scheduleday_name(self):
        """field `CustomDay2 Schedule:Day Name`


        Args:
            value (str): value for IDD Field `CustomDay2 Schedule:Day Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `customday2_scheduleday_name` or None if not set
        """
        return self["CustomDay2 Schedule:Day Name"]

    @customday2_scheduleday_name.setter
    def customday2_scheduleday_name(self, value=None):
        """  Corresponds to IDD field `CustomDay2 Schedule:Day Name`

        """
        self["CustomDay2 Schedule:Day Name"] = value




class ScheduleWeekCompact(DataObject):

    """ Corresponds to IDD object `Schedule:Week:Compact`
        Compact definition for Schedule:Day:List
    """
    _schema = {'extensible-fields': OrderedDict([(u'daytype list 1',
                                                  {'name': u'DayType List 1',
                                                   'pyname': u'daytype_list_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'accepted-values': [u'AllDays',
                                                                       u'Weekdays',
                                                                       u'Weekends',
                                                                       u'Sunday',
                                                                       u'Monday',
                                                                       u'Tuesday',
                                                                       u'Wednesday',
                                                                       u'Thursday',
                                                                       u'Friday',
                                                                       u'Saturday',
                                                                       u'Holiday',
                                                                       u'SummerDesignDay',
                                                                       u'WinterDesignDay',
                                                                       u'CustomDay1',
                                                                       u'CustomDay2'],
                                                      'autocalculatable': False,
                                                      'type': 'alpha'}),
                                                 (u'schedule:day name 1',
                                                  {'name': u'Schedule:Day Name 1',
                                                   'pyname': u'scheduleday_name_1',
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
               'group': u'Schedules',
               'min-fields': 3,
               'name': u'Schedule:Week:Compact',
               'pyname': u'ScheduleWeekCompact',
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
                       daytype_list_1=None,
                       scheduleday_name_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            daytype_list_1 (str): value for IDD Field `DayType List 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            scheduleday_name_1 (str): value for IDD Field `Schedule:Day Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        daytype_list_1 = self.check_value("DayType List 1", daytype_list_1)
        vals.append(daytype_list_1)
        scheduleday_name_1 = self.check_value(
            "Schedule:Day Name 1",
            scheduleday_name_1)
        vals.append(scheduleday_name_1)
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




class ScheduleYear(DataObject):

    """ Corresponds to IDD object `Schedule:Year`
        A Schedule:Year contains from 1 to 52 week schedules
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule type limits name',
                                       {'name': u'Schedule Type Limits Name',
                                        'pyname': u'schedule_type_limits_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'schedule:week name 1',
                                       {'name': u'Schedule:Week Name 1',
                                        'pyname': u'scheduleweek_name_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 1',
                                       {'name': u'Start Month 1',
                                        'pyname': u'start_month_1',
                                        'maximum': 12,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 1',
                                       {'name': u'Start Day 1',
                                        'pyname': u'start_day_1',
                                        'maximum': 31,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 1',
                                       {'name': u'End Month 1',
                                        'pyname': u'end_month_1',
                                        'maximum': 12,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 1',
                                       {'name': u'End Day 1',
                                        'pyname': u'end_day_1',
                                        'maximum': 31,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 2',
                                       {'name': u'Schedule:Week Name 2',
                                        'pyname': u'scheduleweek_name_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 2',
                                       {'name': u'Start Month 2',
                                        'pyname': u'start_month_2',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 2',
                                       {'name': u'Start Day 2',
                                        'pyname': u'start_day_2',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 2',
                                       {'name': u'End Month 2',
                                        'pyname': u'end_month_2',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 2',
                                       {'name': u'End Day 2',
                                        'pyname': u'end_day_2',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 3',
                                       {'name': u'Schedule:Week Name 3',
                                        'pyname': u'scheduleweek_name_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 3',
                                       {'name': u'Start Month 3',
                                        'pyname': u'start_month_3',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 3',
                                       {'name': u'Start Day 3',
                                        'pyname': u'start_day_3',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 3',
                                       {'name': u'End Month 3',
                                        'pyname': u'end_month_3',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 3',
                                       {'name': u'End Day 3',
                                        'pyname': u'end_day_3',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 4',
                                       {'name': u'Schedule:Week Name 4',
                                        'pyname': u'scheduleweek_name_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 4',
                                       {'name': u'Start Month 4',
                                        'pyname': u'start_month_4',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 4',
                                       {'name': u'Start Day 4',
                                        'pyname': u'start_day_4',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 4',
                                       {'name': u'End Month 4',
                                        'pyname': u'end_month_4',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 4',
                                       {'name': u'End Day 4',
                                        'pyname': u'end_day_4',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 5',
                                       {'name': u'Schedule:Week Name 5',
                                        'pyname': u'scheduleweek_name_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 5',
                                       {'name': u'Start Month 5',
                                        'pyname': u'start_month_5',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 5',
                                       {'name': u'Start Day 5',
                                        'pyname': u'start_day_5',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 5',
                                       {'name': u'End Month 5',
                                        'pyname': u'end_month_5',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 5',
                                       {'name': u'End Day 5',
                                        'pyname': u'end_day_5',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 6',
                                       {'name': u'Schedule:Week Name 6',
                                        'pyname': u'scheduleweek_name_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 6',
                                       {'name': u'Start Month 6',
                                        'pyname': u'start_month_6',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 6',
                                       {'name': u'Start Day 6',
                                        'pyname': u'start_day_6',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 6',
                                       {'name': u'End Month 6',
                                        'pyname': u'end_month_6',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 6',
                                       {'name': u'End Day 6',
                                        'pyname': u'end_day_6',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 7',
                                       {'name': u'Schedule:Week Name 7',
                                        'pyname': u'scheduleweek_name_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 7',
                                       {'name': u'Start Month 7',
                                        'pyname': u'start_month_7',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 7',
                                       {'name': u'Start Day 7',
                                        'pyname': u'start_day_7',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 7',
                                       {'name': u'End Month 7',
                                        'pyname': u'end_month_7',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 7',
                                       {'name': u'End Day 7',
                                        'pyname': u'end_day_7',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 8',
                                       {'name': u'Schedule:Week Name 8',
                                        'pyname': u'scheduleweek_name_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 8',
                                       {'name': u'Start Month 8',
                                        'pyname': u'start_month_8',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 8',
                                       {'name': u'Start Day 8',
                                        'pyname': u'start_day_8',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 8',
                                       {'name': u'End Month 8',
                                        'pyname': u'end_month_8',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 8',
                                       {'name': u'End Day 8',
                                        'pyname': u'end_day_8',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 9',
                                       {'name': u'Schedule:Week Name 9',
                                        'pyname': u'scheduleweek_name_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 9',
                                       {'name': u'Start Month 9',
                                        'pyname': u'start_month_9',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 9',
                                       {'name': u'Start Day 9',
                                        'pyname': u'start_day_9',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 9',
                                       {'name': u'End Month 9',
                                        'pyname': u'end_month_9',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 9',
                                       {'name': u'End Day 9',
                                        'pyname': u'end_day_9',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 10',
                                       {'name': u'Schedule:Week Name 10',
                                        'pyname': u'scheduleweek_name_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 10',
                                       {'name': u'Start Month 10',
                                        'pyname': u'start_month_10',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 10',
                                       {'name': u'Start Day 10',
                                        'pyname': u'start_day_10',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 10',
                                       {'name': u'End Month 10',
                                        'pyname': u'end_month_10',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 10',
                                       {'name': u'End Day 10',
                                        'pyname': u'end_day_10',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 11',
                                       {'name': u'Schedule:Week Name 11',
                                        'pyname': u'scheduleweek_name_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 11',
                                       {'name': u'Start Month 11',
                                        'pyname': u'start_month_11',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 11',
                                       {'name': u'Start Day 11',
                                        'pyname': u'start_day_11',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 11',
                                       {'name': u'End Month 11',
                                        'pyname': u'end_month_11',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 11',
                                       {'name': u'End Day 11',
                                        'pyname': u'end_day_11',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 12',
                                       {'name': u'Schedule:Week Name 12',
                                        'pyname': u'scheduleweek_name_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 12',
                                       {'name': u'Start Month 12',
                                        'pyname': u'start_month_12',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 12',
                                       {'name': u'Start Day 12',
                                        'pyname': u'start_day_12',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 12',
                                       {'name': u'End Month 12',
                                        'pyname': u'end_month_12',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 12',
                                       {'name': u'End Day 12',
                                        'pyname': u'end_day_12',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 13',
                                       {'name': u'Schedule:Week Name 13',
                                        'pyname': u'scheduleweek_name_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 13',
                                       {'name': u'Start Month 13',
                                        'pyname': u'start_month_13',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 13',
                                       {'name': u'Start Day 13',
                                        'pyname': u'start_day_13',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 13',
                                       {'name': u'End Month 13',
                                        'pyname': u'end_month_13',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 13',
                                       {'name': u'End Day 13',
                                        'pyname': u'end_day_13',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 14',
                                       {'name': u'Schedule:Week Name 14',
                                        'pyname': u'scheduleweek_name_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 14',
                                       {'name': u'Start Month 14',
                                        'pyname': u'start_month_14',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 14',
                                       {'name': u'Start Day 14',
                                        'pyname': u'start_day_14',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 14',
                                       {'name': u'End Month 14',
                                        'pyname': u'end_month_14',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 14',
                                       {'name': u'End Day 14',
                                        'pyname': u'end_day_14',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 15',
                                       {'name': u'Schedule:Week Name 15',
                                        'pyname': u'scheduleweek_name_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 15',
                                       {'name': u'Start Month 15',
                                        'pyname': u'start_month_15',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 15',
                                       {'name': u'Start Day 15',
                                        'pyname': u'start_day_15',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 15',
                                       {'name': u'End Month 15',
                                        'pyname': u'end_month_15',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 15',
                                       {'name': u'End Day 15',
                                        'pyname': u'end_day_15',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 16',
                                       {'name': u'Schedule:Week Name 16',
                                        'pyname': u'scheduleweek_name_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 16',
                                       {'name': u'Start Month 16',
                                        'pyname': u'start_month_16',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 16',
                                       {'name': u'Start Day 16',
                                        'pyname': u'start_day_16',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 16',
                                       {'name': u'End Month 16',
                                        'pyname': u'end_month_16',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 16',
                                       {'name': u'End Day 16',
                                        'pyname': u'end_day_16',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 17',
                                       {'name': u'Schedule:Week Name 17',
                                        'pyname': u'scheduleweek_name_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 17',
                                       {'name': u'Start Month 17',
                                        'pyname': u'start_month_17',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 17',
                                       {'name': u'Start Day 17',
                                        'pyname': u'start_day_17',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 17',
                                       {'name': u'End Month 17',
                                        'pyname': u'end_month_17',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 17',
                                       {'name': u'End Day 17',
                                        'pyname': u'end_day_17',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 18',
                                       {'name': u'Schedule:Week Name 18',
                                        'pyname': u'scheduleweek_name_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 18',
                                       {'name': u'Start Month 18',
                                        'pyname': u'start_month_18',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 18',
                                       {'name': u'Start Day 18',
                                        'pyname': u'start_day_18',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 18',
                                       {'name': u'End Month 18',
                                        'pyname': u'end_month_18',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 18',
                                       {'name': u'End Day 18',
                                        'pyname': u'end_day_18',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 19',
                                       {'name': u'Schedule:Week Name 19',
                                        'pyname': u'scheduleweek_name_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 19',
                                       {'name': u'Start Month 19',
                                        'pyname': u'start_month_19',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 19',
                                       {'name': u'Start Day 19',
                                        'pyname': u'start_day_19',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 19',
                                       {'name': u'End Month 19',
                                        'pyname': u'end_month_19',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 19',
                                       {'name': u'End Day 19',
                                        'pyname': u'end_day_19',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 20',
                                       {'name': u'Schedule:Week Name 20',
                                        'pyname': u'scheduleweek_name_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 20',
                                       {'name': u'Start Month 20',
                                        'pyname': u'start_month_20',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 20',
                                       {'name': u'Start Day 20',
                                        'pyname': u'start_day_20',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 20',
                                       {'name': u'End Month 20',
                                        'pyname': u'end_month_20',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 20',
                                       {'name': u'End Day 20',
                                        'pyname': u'end_day_20',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 21',
                                       {'name': u'Schedule:Week Name 21',
                                        'pyname': u'scheduleweek_name_21',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 21',
                                       {'name': u'Start Month 21',
                                        'pyname': u'start_month_21',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 21',
                                       {'name': u'Start Day 21',
                                        'pyname': u'start_day_21',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 21',
                                       {'name': u'End Month 21',
                                        'pyname': u'end_month_21',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 21',
                                       {'name': u'End Day 21',
                                        'pyname': u'end_day_21',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 22',
                                       {'name': u'Schedule:Week Name 22',
                                        'pyname': u'scheduleweek_name_22',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 22',
                                       {'name': u'Start Month 22',
                                        'pyname': u'start_month_22',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 22',
                                       {'name': u'Start Day 22',
                                        'pyname': u'start_day_22',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 22',
                                       {'name': u'End Month 22',
                                        'pyname': u'end_month_22',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 22',
                                       {'name': u'End Day 22',
                                        'pyname': u'end_day_22',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 23',
                                       {'name': u'Schedule:Week Name 23',
                                        'pyname': u'scheduleweek_name_23',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 23',
                                       {'name': u'Start Month 23',
                                        'pyname': u'start_month_23',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 23',
                                       {'name': u'Start Day 23',
                                        'pyname': u'start_day_23',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 23',
                                       {'name': u'End Month 23',
                                        'pyname': u'end_month_23',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 23',
                                       {'name': u'End Day 23',
                                        'pyname': u'end_day_23',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 24',
                                       {'name': u'Schedule:Week Name 24',
                                        'pyname': u'scheduleweek_name_24',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 24',
                                       {'name': u'Start Month 24',
                                        'pyname': u'start_month_24',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 24',
                                       {'name': u'Start Day 24',
                                        'pyname': u'start_day_24',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 24',
                                       {'name': u'End Month 24',
                                        'pyname': u'end_month_24',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 24',
                                       {'name': u'End Day 24',
                                        'pyname': u'end_day_24',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 25',
                                       {'name': u'Schedule:Week Name 25',
                                        'pyname': u'scheduleweek_name_25',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 25',
                                       {'name': u'Start Month 25',
                                        'pyname': u'start_month_25',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 25',
                                       {'name': u'Start Day 25',
                                        'pyname': u'start_day_25',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 25',
                                       {'name': u'End Month 25',
                                        'pyname': u'end_month_25',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day 25',
                                       {'name': u'End Day 25',
                                        'pyname': u'end_day_25',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule:week name 26',
                                       {'name': u'Schedule:Week Name 26',
                                        'pyname': u'scheduleweek_name_26',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'start month 26',
                                       {'name': u'Start Month 26',
                                        'pyname': u'start_month_26',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'start day 26',
                                       {'name': u'Start Day 26',
                                        'pyname': u'start_day_26',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month 26',
                                       {'name': u'End Month 26',
                                        'pyname': u'end_month_26',
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      ('end day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3',
                                       {'name': 'End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3',
                                        'pyname': 'end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3',
                                        'maximum': 31,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'Schedules',
               'min-fields': 7,
               'name': u'Schedule:Year',
               'pyname': u'ScheduleYear',
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
    def schedule_type_limits_name(self):
        """field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set

        """
        return self["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """Corresponds to IDD field `Schedule Type Limits Name`"""
        self["Schedule Type Limits Name"] = value

    @property
    def scheduleweek_name_1(self):
        """field `Schedule:Week Name 1`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_1` or None if not set
        """
        return self["Schedule:Week Name 1"]

    @scheduleweek_name_1.setter
    def scheduleweek_name_1(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 1`

        """
        self["Schedule:Week Name 1"] = value

    @property
    def start_month_1(self):
        """field `Start Month 1`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_1` or None if not set

        """
        return self["Start Month 1"]

    @start_month_1.setter
    def start_month_1(self, value=None):
        """Corresponds to IDD field `Start Month 1`"""
        self["Start Month 1"] = value

    @property
    def start_day_1(self):
        """field `Start Day 1`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_1` or None if not set

        """
        return self["Start Day 1"]

    @start_day_1.setter
    def start_day_1(self, value=None):
        """Corresponds to IDD field `Start Day 1`"""
        self["Start Day 1"] = value

    @property
    def end_month_1(self):
        """field `End Month 1`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_1` or None if not set

        """
        return self["End Month 1"]

    @end_month_1.setter
    def end_month_1(self, value=None):
        """Corresponds to IDD field `End Month 1`"""
        self["End Month 1"] = value

    @property
    def end_day_1(self):
        """field `End Day 1`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_1` or None if not set

        """
        return self["End Day 1"]

    @end_day_1.setter
    def end_day_1(self, value=None):
        """Corresponds to IDD field `End Day 1`"""
        self["End Day 1"] = value

    @property
    def scheduleweek_name_2(self):
        """field `Schedule:Week Name 2`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_2` or None if not set
        """
        return self["Schedule:Week Name 2"]

    @scheduleweek_name_2.setter
    def scheduleweek_name_2(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 2`

        """
        self["Schedule:Week Name 2"] = value

    @property
    def start_month_2(self):
        """field `Start Month 2`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_2` or None if not set

        """
        return self["Start Month 2"]

    @start_month_2.setter
    def start_month_2(self, value=None):
        """Corresponds to IDD field `Start Month 2`"""
        self["Start Month 2"] = value

    @property
    def start_day_2(self):
        """field `Start Day 2`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_2` or None if not set

        """
        return self["Start Day 2"]

    @start_day_2.setter
    def start_day_2(self, value=None):
        """Corresponds to IDD field `Start Day 2`"""
        self["Start Day 2"] = value

    @property
    def end_month_2(self):
        """field `End Month 2`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_2` or None if not set

        """
        return self["End Month 2"]

    @end_month_2.setter
    def end_month_2(self, value=None):
        """Corresponds to IDD field `End Month 2`"""
        self["End Month 2"] = value

    @property
    def end_day_2(self):
        """field `End Day 2`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_2` or None if not set

        """
        return self["End Day 2"]

    @end_day_2.setter
    def end_day_2(self, value=None):
        """Corresponds to IDD field `End Day 2`"""
        self["End Day 2"] = value

    @property
    def scheduleweek_name_3(self):
        """field `Schedule:Week Name 3`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_3` or None if not set
        """
        return self["Schedule:Week Name 3"]

    @scheduleweek_name_3.setter
    def scheduleweek_name_3(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 3`

        """
        self["Schedule:Week Name 3"] = value

    @property
    def start_month_3(self):
        """field `Start Month 3`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_3` or None if not set

        """
        return self["Start Month 3"]

    @start_month_3.setter
    def start_month_3(self, value=None):
        """Corresponds to IDD field `Start Month 3`"""
        self["Start Month 3"] = value

    @property
    def start_day_3(self):
        """field `Start Day 3`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_3` or None if not set

        """
        return self["Start Day 3"]

    @start_day_3.setter
    def start_day_3(self, value=None):
        """Corresponds to IDD field `Start Day 3`"""
        self["Start Day 3"] = value

    @property
    def end_month_3(self):
        """field `End Month 3`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_3` or None if not set

        """
        return self["End Month 3"]

    @end_month_3.setter
    def end_month_3(self, value=None):
        """Corresponds to IDD field `End Month 3`"""
        self["End Month 3"] = value

    @property
    def end_day_3(self):
        """field `End Day 3`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_3` or None if not set

        """
        return self["End Day 3"]

    @end_day_3.setter
    def end_day_3(self, value=None):
        """Corresponds to IDD field `End Day 3`"""
        self["End Day 3"] = value

    @property
    def scheduleweek_name_4(self):
        """field `Schedule:Week Name 4`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_4` or None if not set
        """
        return self["Schedule:Week Name 4"]

    @scheduleweek_name_4.setter
    def scheduleweek_name_4(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 4`

        """
        self["Schedule:Week Name 4"] = value

    @property
    def start_month_4(self):
        """field `Start Month 4`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_4` or None if not set

        """
        return self["Start Month 4"]

    @start_month_4.setter
    def start_month_4(self, value=None):
        """Corresponds to IDD field `Start Month 4`"""
        self["Start Month 4"] = value

    @property
    def start_day_4(self):
        """field `Start Day 4`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_4` or None if not set

        """
        return self["Start Day 4"]

    @start_day_4.setter
    def start_day_4(self, value=None):
        """Corresponds to IDD field `Start Day 4`"""
        self["Start Day 4"] = value

    @property
    def end_month_4(self):
        """field `End Month 4`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_4` or None if not set

        """
        return self["End Month 4"]

    @end_month_4.setter
    def end_month_4(self, value=None):
        """Corresponds to IDD field `End Month 4`"""
        self["End Month 4"] = value

    @property
    def end_day_4(self):
        """field `End Day 4`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_4` or None if not set

        """
        return self["End Day 4"]

    @end_day_4.setter
    def end_day_4(self, value=None):
        """Corresponds to IDD field `End Day 4`"""
        self["End Day 4"] = value

    @property
    def scheduleweek_name_5(self):
        """field `Schedule:Week Name 5`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_5` or None if not set
        """
        return self["Schedule:Week Name 5"]

    @scheduleweek_name_5.setter
    def scheduleweek_name_5(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 5`

        """
        self["Schedule:Week Name 5"] = value

    @property
    def start_month_5(self):
        """field `Start Month 5`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_5` or None if not set

        """
        return self["Start Month 5"]

    @start_month_5.setter
    def start_month_5(self, value=None):
        """Corresponds to IDD field `Start Month 5`"""
        self["Start Month 5"] = value

    @property
    def start_day_5(self):
        """field `Start Day 5`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_5` or None if not set

        """
        return self["Start Day 5"]

    @start_day_5.setter
    def start_day_5(self, value=None):
        """Corresponds to IDD field `Start Day 5`"""
        self["Start Day 5"] = value

    @property
    def end_month_5(self):
        """field `End Month 5`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_5` or None if not set

        """
        return self["End Month 5"]

    @end_month_5.setter
    def end_month_5(self, value=None):
        """Corresponds to IDD field `End Month 5`"""
        self["End Month 5"] = value

    @property
    def end_day_5(self):
        """field `End Day 5`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_5` or None if not set

        """
        return self["End Day 5"]

    @end_day_5.setter
    def end_day_5(self, value=None):
        """Corresponds to IDD field `End Day 5`"""
        self["End Day 5"] = value

    @property
    def scheduleweek_name_6(self):
        """field `Schedule:Week Name 6`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_6` or None if not set
        """
        return self["Schedule:Week Name 6"]

    @scheduleweek_name_6.setter
    def scheduleweek_name_6(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 6`

        """
        self["Schedule:Week Name 6"] = value

    @property
    def start_month_6(self):
        """field `Start Month 6`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_6` or None if not set

        """
        return self["Start Month 6"]

    @start_month_6.setter
    def start_month_6(self, value=None):
        """Corresponds to IDD field `Start Month 6`"""
        self["Start Month 6"] = value

    @property
    def start_day_6(self):
        """field `Start Day 6`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_6` or None if not set

        """
        return self["Start Day 6"]

    @start_day_6.setter
    def start_day_6(self, value=None):
        """Corresponds to IDD field `Start Day 6`"""
        self["Start Day 6"] = value

    @property
    def end_month_6(self):
        """field `End Month 6`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_6` or None if not set

        """
        return self["End Month 6"]

    @end_month_6.setter
    def end_month_6(self, value=None):
        """Corresponds to IDD field `End Month 6`"""
        self["End Month 6"] = value

    @property
    def end_day_6(self):
        """field `End Day 6`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_6` or None if not set

        """
        return self["End Day 6"]

    @end_day_6.setter
    def end_day_6(self, value=None):
        """Corresponds to IDD field `End Day 6`"""
        self["End Day 6"] = value

    @property
    def scheduleweek_name_7(self):
        """field `Schedule:Week Name 7`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_7` or None if not set
        """
        return self["Schedule:Week Name 7"]

    @scheduleweek_name_7.setter
    def scheduleweek_name_7(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 7`

        """
        self["Schedule:Week Name 7"] = value

    @property
    def start_month_7(self):
        """field `Start Month 7`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_7` or None if not set

        """
        return self["Start Month 7"]

    @start_month_7.setter
    def start_month_7(self, value=None):
        """Corresponds to IDD field `Start Month 7`"""
        self["Start Month 7"] = value

    @property
    def start_day_7(self):
        """field `Start Day 7`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_7` or None if not set

        """
        return self["Start Day 7"]

    @start_day_7.setter
    def start_day_7(self, value=None):
        """Corresponds to IDD field `Start Day 7`"""
        self["Start Day 7"] = value

    @property
    def end_month_7(self):
        """field `End Month 7`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_7` or None if not set

        """
        return self["End Month 7"]

    @end_month_7.setter
    def end_month_7(self, value=None):
        """Corresponds to IDD field `End Month 7`"""
        self["End Month 7"] = value

    @property
    def end_day_7(self):
        """field `End Day 7`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_7` or None if not set

        """
        return self["End Day 7"]

    @end_day_7.setter
    def end_day_7(self, value=None):
        """Corresponds to IDD field `End Day 7`"""
        self["End Day 7"] = value

    @property
    def scheduleweek_name_8(self):
        """field `Schedule:Week Name 8`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_8` or None if not set
        """
        return self["Schedule:Week Name 8"]

    @scheduleweek_name_8.setter
    def scheduleweek_name_8(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 8`

        """
        self["Schedule:Week Name 8"] = value

    @property
    def start_month_8(self):
        """field `Start Month 8`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_8` or None if not set

        """
        return self["Start Month 8"]

    @start_month_8.setter
    def start_month_8(self, value=None):
        """Corresponds to IDD field `Start Month 8`"""
        self["Start Month 8"] = value

    @property
    def start_day_8(self):
        """field `Start Day 8`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_8` or None if not set

        """
        return self["Start Day 8"]

    @start_day_8.setter
    def start_day_8(self, value=None):
        """Corresponds to IDD field `Start Day 8`"""
        self["Start Day 8"] = value

    @property
    def end_month_8(self):
        """field `End Month 8`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_8` or None if not set

        """
        return self["End Month 8"]

    @end_month_8.setter
    def end_month_8(self, value=None):
        """Corresponds to IDD field `End Month 8`"""
        self["End Month 8"] = value

    @property
    def end_day_8(self):
        """field `End Day 8`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_8` or None if not set

        """
        return self["End Day 8"]

    @end_day_8.setter
    def end_day_8(self, value=None):
        """Corresponds to IDD field `End Day 8`"""
        self["End Day 8"] = value

    @property
    def scheduleweek_name_9(self):
        """field `Schedule:Week Name 9`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_9` or None if not set
        """
        return self["Schedule:Week Name 9"]

    @scheduleweek_name_9.setter
    def scheduleweek_name_9(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 9`

        """
        self["Schedule:Week Name 9"] = value

    @property
    def start_month_9(self):
        """field `Start Month 9`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_9` or None if not set

        """
        return self["Start Month 9"]

    @start_month_9.setter
    def start_month_9(self, value=None):
        """Corresponds to IDD field `Start Month 9`"""
        self["Start Month 9"] = value

    @property
    def start_day_9(self):
        """field `Start Day 9`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_9` or None if not set

        """
        return self["Start Day 9"]

    @start_day_9.setter
    def start_day_9(self, value=None):
        """Corresponds to IDD field `Start Day 9`"""
        self["Start Day 9"] = value

    @property
    def end_month_9(self):
        """field `End Month 9`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_9` or None if not set

        """
        return self["End Month 9"]

    @end_month_9.setter
    def end_month_9(self, value=None):
        """Corresponds to IDD field `End Month 9`"""
        self["End Month 9"] = value

    @property
    def end_day_9(self):
        """field `End Day 9`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_9` or None if not set

        """
        return self["End Day 9"]

    @end_day_9.setter
    def end_day_9(self, value=None):
        """Corresponds to IDD field `End Day 9`"""
        self["End Day 9"] = value

    @property
    def scheduleweek_name_10(self):
        """field `Schedule:Week Name 10`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_10` or None if not set
        """
        return self["Schedule:Week Name 10"]

    @scheduleweek_name_10.setter
    def scheduleweek_name_10(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 10`

        """
        self["Schedule:Week Name 10"] = value

    @property
    def start_month_10(self):
        """field `Start Month 10`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_10` or None if not set

        """
        return self["Start Month 10"]

    @start_month_10.setter
    def start_month_10(self, value=None):
        """Corresponds to IDD field `Start Month 10`"""
        self["Start Month 10"] = value

    @property
    def start_day_10(self):
        """field `Start Day 10`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_10` or None if not set

        """
        return self["Start Day 10"]

    @start_day_10.setter
    def start_day_10(self, value=None):
        """Corresponds to IDD field `Start Day 10`"""
        self["Start Day 10"] = value

    @property
    def end_month_10(self):
        """field `End Month 10`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_10` or None if not set

        """
        return self["End Month 10"]

    @end_month_10.setter
    def end_month_10(self, value=None):
        """Corresponds to IDD field `End Month 10`"""
        self["End Month 10"] = value

    @property
    def end_day_10(self):
        """field `End Day 10`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_10` or None if not set

        """
        return self["End Day 10"]

    @end_day_10.setter
    def end_day_10(self, value=None):
        """Corresponds to IDD field `End Day 10`"""
        self["End Day 10"] = value

    @property
    def scheduleweek_name_11(self):
        """field `Schedule:Week Name 11`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_11` or None if not set
        """
        return self["Schedule:Week Name 11"]

    @scheduleweek_name_11.setter
    def scheduleweek_name_11(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 11`

        """
        self["Schedule:Week Name 11"] = value

    @property
    def start_month_11(self):
        """field `Start Month 11`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_11` or None if not set

        """
        return self["Start Month 11"]

    @start_month_11.setter
    def start_month_11(self, value=None):
        """Corresponds to IDD field `Start Month 11`"""
        self["Start Month 11"] = value

    @property
    def start_day_11(self):
        """field `Start Day 11`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_11` or None if not set

        """
        return self["Start Day 11"]

    @start_day_11.setter
    def start_day_11(self, value=None):
        """Corresponds to IDD field `Start Day 11`"""
        self["Start Day 11"] = value

    @property
    def end_month_11(self):
        """field `End Month 11`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_11` or None if not set

        """
        return self["End Month 11"]

    @end_month_11.setter
    def end_month_11(self, value=None):
        """Corresponds to IDD field `End Month 11`"""
        self["End Month 11"] = value

    @property
    def end_day_11(self):
        """field `End Day 11`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_11` or None if not set

        """
        return self["End Day 11"]

    @end_day_11.setter
    def end_day_11(self, value=None):
        """Corresponds to IDD field `End Day 11`"""
        self["End Day 11"] = value

    @property
    def scheduleweek_name_12(self):
        """field `Schedule:Week Name 12`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_12` or None if not set
        """
        return self["Schedule:Week Name 12"]

    @scheduleweek_name_12.setter
    def scheduleweek_name_12(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 12`

        """
        self["Schedule:Week Name 12"] = value

    @property
    def start_month_12(self):
        """field `Start Month 12`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_12` or None if not set

        """
        return self["Start Month 12"]

    @start_month_12.setter
    def start_month_12(self, value=None):
        """Corresponds to IDD field `Start Month 12`"""
        self["Start Month 12"] = value

    @property
    def start_day_12(self):
        """field `Start Day 12`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_12` or None if not set

        """
        return self["Start Day 12"]

    @start_day_12.setter
    def start_day_12(self, value=None):
        """Corresponds to IDD field `Start Day 12`"""
        self["Start Day 12"] = value

    @property
    def end_month_12(self):
        """field `End Month 12`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_12` or None if not set

        """
        return self["End Month 12"]

    @end_month_12.setter
    def end_month_12(self, value=None):
        """Corresponds to IDD field `End Month 12`"""
        self["End Month 12"] = value

    @property
    def end_day_12(self):
        """field `End Day 12`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_12` or None if not set

        """
        return self["End Day 12"]

    @end_day_12.setter
    def end_day_12(self, value=None):
        """Corresponds to IDD field `End Day 12`"""
        self["End Day 12"] = value

    @property
    def scheduleweek_name_13(self):
        """field `Schedule:Week Name 13`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_13` or None if not set
        """
        return self["Schedule:Week Name 13"]

    @scheduleweek_name_13.setter
    def scheduleweek_name_13(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 13`

        """
        self["Schedule:Week Name 13"] = value

    @property
    def start_month_13(self):
        """field `Start Month 13`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_13` or None if not set

        """
        return self["Start Month 13"]

    @start_month_13.setter
    def start_month_13(self, value=None):
        """Corresponds to IDD field `Start Month 13`"""
        self["Start Month 13"] = value

    @property
    def start_day_13(self):
        """field `Start Day 13`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_13` or None if not set

        """
        return self["Start Day 13"]

    @start_day_13.setter
    def start_day_13(self, value=None):
        """Corresponds to IDD field `Start Day 13`"""
        self["Start Day 13"] = value

    @property
    def end_month_13(self):
        """field `End Month 13`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_13` or None if not set

        """
        return self["End Month 13"]

    @end_month_13.setter
    def end_month_13(self, value=None):
        """Corresponds to IDD field `End Month 13`"""
        self["End Month 13"] = value

    @property
    def end_day_13(self):
        """field `End Day 13`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_13` or None if not set

        """
        return self["End Day 13"]

    @end_day_13.setter
    def end_day_13(self, value=None):
        """Corresponds to IDD field `End Day 13`"""
        self["End Day 13"] = value

    @property
    def scheduleweek_name_14(self):
        """field `Schedule:Week Name 14`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_14` or None if not set
        """
        return self["Schedule:Week Name 14"]

    @scheduleweek_name_14.setter
    def scheduleweek_name_14(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 14`

        """
        self["Schedule:Week Name 14"] = value

    @property
    def start_month_14(self):
        """field `Start Month 14`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_14` or None if not set

        """
        return self["Start Month 14"]

    @start_month_14.setter
    def start_month_14(self, value=None):
        """Corresponds to IDD field `Start Month 14`"""
        self["Start Month 14"] = value

    @property
    def start_day_14(self):
        """field `Start Day 14`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_14` or None if not set

        """
        return self["Start Day 14"]

    @start_day_14.setter
    def start_day_14(self, value=None):
        """Corresponds to IDD field `Start Day 14`"""
        self["Start Day 14"] = value

    @property
    def end_month_14(self):
        """field `End Month 14`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_14` or None if not set

        """
        return self["End Month 14"]

    @end_month_14.setter
    def end_month_14(self, value=None):
        """Corresponds to IDD field `End Month 14`"""
        self["End Month 14"] = value

    @property
    def end_day_14(self):
        """field `End Day 14`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_14` or None if not set

        """
        return self["End Day 14"]

    @end_day_14.setter
    def end_day_14(self, value=None):
        """Corresponds to IDD field `End Day 14`"""
        self["End Day 14"] = value

    @property
    def scheduleweek_name_15(self):
        """field `Schedule:Week Name 15`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_15` or None if not set
        """
        return self["Schedule:Week Name 15"]

    @scheduleweek_name_15.setter
    def scheduleweek_name_15(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 15`

        """
        self["Schedule:Week Name 15"] = value

    @property
    def start_month_15(self):
        """field `Start Month 15`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_15` or None if not set

        """
        return self["Start Month 15"]

    @start_month_15.setter
    def start_month_15(self, value=None):
        """Corresponds to IDD field `Start Month 15`"""
        self["Start Month 15"] = value

    @property
    def start_day_15(self):
        """field `Start Day 15`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_15` or None if not set

        """
        return self["Start Day 15"]

    @start_day_15.setter
    def start_day_15(self, value=None):
        """Corresponds to IDD field `Start Day 15`"""
        self["Start Day 15"] = value

    @property
    def end_month_15(self):
        """field `End Month 15`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_15` or None if not set

        """
        return self["End Month 15"]

    @end_month_15.setter
    def end_month_15(self, value=None):
        """Corresponds to IDD field `End Month 15`"""
        self["End Month 15"] = value

    @property
    def end_day_15(self):
        """field `End Day 15`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_15` or None if not set

        """
        return self["End Day 15"]

    @end_day_15.setter
    def end_day_15(self, value=None):
        """Corresponds to IDD field `End Day 15`"""
        self["End Day 15"] = value

    @property
    def scheduleweek_name_16(self):
        """field `Schedule:Week Name 16`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_16` or None if not set
        """
        return self["Schedule:Week Name 16"]

    @scheduleweek_name_16.setter
    def scheduleweek_name_16(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 16`

        """
        self["Schedule:Week Name 16"] = value

    @property
    def start_month_16(self):
        """field `Start Month 16`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_16` or None if not set

        """
        return self["Start Month 16"]

    @start_month_16.setter
    def start_month_16(self, value=None):
        """Corresponds to IDD field `Start Month 16`"""
        self["Start Month 16"] = value

    @property
    def start_day_16(self):
        """field `Start Day 16`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_16` or None if not set

        """
        return self["Start Day 16"]

    @start_day_16.setter
    def start_day_16(self, value=None):
        """Corresponds to IDD field `Start Day 16`"""
        self["Start Day 16"] = value

    @property
    def end_month_16(self):
        """field `End Month 16`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_16` or None if not set

        """
        return self["End Month 16"]

    @end_month_16.setter
    def end_month_16(self, value=None):
        """Corresponds to IDD field `End Month 16`"""
        self["End Month 16"] = value

    @property
    def end_day_16(self):
        """field `End Day 16`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_16` or None if not set

        """
        return self["End Day 16"]

    @end_day_16.setter
    def end_day_16(self, value=None):
        """Corresponds to IDD field `End Day 16`"""
        self["End Day 16"] = value

    @property
    def scheduleweek_name_17(self):
        """field `Schedule:Week Name 17`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_17` or None if not set
        """
        return self["Schedule:Week Name 17"]

    @scheduleweek_name_17.setter
    def scheduleweek_name_17(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 17`

        """
        self["Schedule:Week Name 17"] = value

    @property
    def start_month_17(self):
        """field `Start Month 17`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_17` or None if not set

        """
        return self["Start Month 17"]

    @start_month_17.setter
    def start_month_17(self, value=None):
        """Corresponds to IDD field `Start Month 17`"""
        self["Start Month 17"] = value

    @property
    def start_day_17(self):
        """field `Start Day 17`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_17` or None if not set

        """
        return self["Start Day 17"]

    @start_day_17.setter
    def start_day_17(self, value=None):
        """Corresponds to IDD field `Start Day 17`"""
        self["Start Day 17"] = value

    @property
    def end_month_17(self):
        """field `End Month 17`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_17` or None if not set

        """
        return self["End Month 17"]

    @end_month_17.setter
    def end_month_17(self, value=None):
        """Corresponds to IDD field `End Month 17`"""
        self["End Month 17"] = value

    @property
    def end_day_17(self):
        """field `End Day 17`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_17` or None if not set

        """
        return self["End Day 17"]

    @end_day_17.setter
    def end_day_17(self, value=None):
        """Corresponds to IDD field `End Day 17`"""
        self["End Day 17"] = value

    @property
    def scheduleweek_name_18(self):
        """field `Schedule:Week Name 18`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_18` or None if not set
        """
        return self["Schedule:Week Name 18"]

    @scheduleweek_name_18.setter
    def scheduleweek_name_18(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 18`

        """
        self["Schedule:Week Name 18"] = value

    @property
    def start_month_18(self):
        """field `Start Month 18`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_18` or None if not set

        """
        return self["Start Month 18"]

    @start_month_18.setter
    def start_month_18(self, value=None):
        """Corresponds to IDD field `Start Month 18`"""
        self["Start Month 18"] = value

    @property
    def start_day_18(self):
        """field `Start Day 18`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_18` or None if not set

        """
        return self["Start Day 18"]

    @start_day_18.setter
    def start_day_18(self, value=None):
        """Corresponds to IDD field `Start Day 18`"""
        self["Start Day 18"] = value

    @property
    def end_month_18(self):
        """field `End Month 18`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_18` or None if not set

        """
        return self["End Month 18"]

    @end_month_18.setter
    def end_month_18(self, value=None):
        """Corresponds to IDD field `End Month 18`"""
        self["End Month 18"] = value

    @property
    def end_day_18(self):
        """field `End Day 18`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_18` or None if not set

        """
        return self["End Day 18"]

    @end_day_18.setter
    def end_day_18(self, value=None):
        """Corresponds to IDD field `End Day 18`"""
        self["End Day 18"] = value

    @property
    def scheduleweek_name_19(self):
        """field `Schedule:Week Name 19`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_19` or None if not set
        """
        return self["Schedule:Week Name 19"]

    @scheduleweek_name_19.setter
    def scheduleweek_name_19(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 19`

        """
        self["Schedule:Week Name 19"] = value

    @property
    def start_month_19(self):
        """field `Start Month 19`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_19` or None if not set

        """
        return self["Start Month 19"]

    @start_month_19.setter
    def start_month_19(self, value=None):
        """Corresponds to IDD field `Start Month 19`"""
        self["Start Month 19"] = value

    @property
    def start_day_19(self):
        """field `Start Day 19`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_19` or None if not set

        """
        return self["Start Day 19"]

    @start_day_19.setter
    def start_day_19(self, value=None):
        """Corresponds to IDD field `Start Day 19`"""
        self["Start Day 19"] = value

    @property
    def end_month_19(self):
        """field `End Month 19`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_19` or None if not set

        """
        return self["End Month 19"]

    @end_month_19.setter
    def end_month_19(self, value=None):
        """Corresponds to IDD field `End Month 19`"""
        self["End Month 19"] = value

    @property
    def end_day_19(self):
        """field `End Day 19`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_19` or None if not set

        """
        return self["End Day 19"]

    @end_day_19.setter
    def end_day_19(self, value=None):
        """Corresponds to IDD field `End Day 19`"""
        self["End Day 19"] = value

    @property
    def scheduleweek_name_20(self):
        """field `Schedule:Week Name 20`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_20` or None if not set
        """
        return self["Schedule:Week Name 20"]

    @scheduleweek_name_20.setter
    def scheduleweek_name_20(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 20`

        """
        self["Schedule:Week Name 20"] = value

    @property
    def start_month_20(self):
        """field `Start Month 20`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_20` or None if not set

        """
        return self["Start Month 20"]

    @start_month_20.setter
    def start_month_20(self, value=None):
        """Corresponds to IDD field `Start Month 20`"""
        self["Start Month 20"] = value

    @property
    def start_day_20(self):
        """field `Start Day 20`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_20` or None if not set

        """
        return self["Start Day 20"]

    @start_day_20.setter
    def start_day_20(self, value=None):
        """Corresponds to IDD field `Start Day 20`"""
        self["Start Day 20"] = value

    @property
    def end_month_20(self):
        """field `End Month 20`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_20` or None if not set

        """
        return self["End Month 20"]

    @end_month_20.setter
    def end_month_20(self, value=None):
        """Corresponds to IDD field `End Month 20`"""
        self["End Month 20"] = value

    @property
    def end_day_20(self):
        """field `End Day 20`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_20` or None if not set

        """
        return self["End Day 20"]

    @end_day_20.setter
    def end_day_20(self, value=None):
        """Corresponds to IDD field `End Day 20`"""
        self["End Day 20"] = value

    @property
    def scheduleweek_name_21(self):
        """field `Schedule:Week Name 21`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_21` or None if not set
        """
        return self["Schedule:Week Name 21"]

    @scheduleweek_name_21.setter
    def scheduleweek_name_21(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 21`

        """
        self["Schedule:Week Name 21"] = value

    @property
    def start_month_21(self):
        """field `Start Month 21`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_21` or None if not set

        """
        return self["Start Month 21"]

    @start_month_21.setter
    def start_month_21(self, value=None):
        """Corresponds to IDD field `Start Month 21`"""
        self["Start Month 21"] = value

    @property
    def start_day_21(self):
        """field `Start Day 21`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_21` or None if not set

        """
        return self["Start Day 21"]

    @start_day_21.setter
    def start_day_21(self, value=None):
        """Corresponds to IDD field `Start Day 21`"""
        self["Start Day 21"] = value

    @property
    def end_month_21(self):
        """field `End Month 21`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_21` or None if not set

        """
        return self["End Month 21"]

    @end_month_21.setter
    def end_month_21(self, value=None):
        """Corresponds to IDD field `End Month 21`"""
        self["End Month 21"] = value

    @property
    def end_day_21(self):
        """field `End Day 21`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_21` or None if not set

        """
        return self["End Day 21"]

    @end_day_21.setter
    def end_day_21(self, value=None):
        """Corresponds to IDD field `End Day 21`"""
        self["End Day 21"] = value

    @property
    def scheduleweek_name_22(self):
        """field `Schedule:Week Name 22`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_22` or None if not set
        """
        return self["Schedule:Week Name 22"]

    @scheduleweek_name_22.setter
    def scheduleweek_name_22(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 22`

        """
        self["Schedule:Week Name 22"] = value

    @property
    def start_month_22(self):
        """field `Start Month 22`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_22` or None if not set

        """
        return self["Start Month 22"]

    @start_month_22.setter
    def start_month_22(self, value=None):
        """Corresponds to IDD field `Start Month 22`"""
        self["Start Month 22"] = value

    @property
    def start_day_22(self):
        """field `Start Day 22`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_22` or None if not set

        """
        return self["Start Day 22"]

    @start_day_22.setter
    def start_day_22(self, value=None):
        """Corresponds to IDD field `Start Day 22`"""
        self["Start Day 22"] = value

    @property
    def end_month_22(self):
        """field `End Month 22`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_22` or None if not set

        """
        return self["End Month 22"]

    @end_month_22.setter
    def end_month_22(self, value=None):
        """Corresponds to IDD field `End Month 22`"""
        self["End Month 22"] = value

    @property
    def end_day_22(self):
        """field `End Day 22`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_22` or None if not set

        """
        return self["End Day 22"]

    @end_day_22.setter
    def end_day_22(self, value=None):
        """Corresponds to IDD field `End Day 22`"""
        self["End Day 22"] = value

    @property
    def scheduleweek_name_23(self):
        """field `Schedule:Week Name 23`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_23` or None if not set
        """
        return self["Schedule:Week Name 23"]

    @scheduleweek_name_23.setter
    def scheduleweek_name_23(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 23`

        """
        self["Schedule:Week Name 23"] = value

    @property
    def start_month_23(self):
        """field `Start Month 23`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_23` or None if not set

        """
        return self["Start Month 23"]

    @start_month_23.setter
    def start_month_23(self, value=None):
        """Corresponds to IDD field `Start Month 23`"""
        self["Start Month 23"] = value

    @property
    def start_day_23(self):
        """field `Start Day 23`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_23` or None if not set

        """
        return self["Start Day 23"]

    @start_day_23.setter
    def start_day_23(self, value=None):
        """Corresponds to IDD field `Start Day 23`"""
        self["Start Day 23"] = value

    @property
    def end_month_23(self):
        """field `End Month 23`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_23` or None if not set

        """
        return self["End Month 23"]

    @end_month_23.setter
    def end_month_23(self, value=None):
        """Corresponds to IDD field `End Month 23`"""
        self["End Month 23"] = value

    @property
    def end_day_23(self):
        """field `End Day 23`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_23` or None if not set

        """
        return self["End Day 23"]

    @end_day_23.setter
    def end_day_23(self, value=None):
        """Corresponds to IDD field `End Day 23`"""
        self["End Day 23"] = value

    @property
    def scheduleweek_name_24(self):
        """field `Schedule:Week Name 24`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_24` or None if not set
        """
        return self["Schedule:Week Name 24"]

    @scheduleweek_name_24.setter
    def scheduleweek_name_24(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 24`

        """
        self["Schedule:Week Name 24"] = value

    @property
    def start_month_24(self):
        """field `Start Month 24`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_24` or None if not set

        """
        return self["Start Month 24"]

    @start_month_24.setter
    def start_month_24(self, value=None):
        """Corresponds to IDD field `Start Month 24`"""
        self["Start Month 24"] = value

    @property
    def start_day_24(self):
        """field `Start Day 24`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_24` or None if not set

        """
        return self["Start Day 24"]

    @start_day_24.setter
    def start_day_24(self, value=None):
        """Corresponds to IDD field `Start Day 24`"""
        self["Start Day 24"] = value

    @property
    def end_month_24(self):
        """field `End Month 24`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_24` or None if not set

        """
        return self["End Month 24"]

    @end_month_24.setter
    def end_month_24(self, value=None):
        """Corresponds to IDD field `End Month 24`"""
        self["End Month 24"] = value

    @property
    def end_day_24(self):
        """field `End Day 24`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_24` or None if not set

        """
        return self["End Day 24"]

    @end_day_24.setter
    def end_day_24(self, value=None):
        """Corresponds to IDD field `End Day 24`"""
        self["End Day 24"] = value

    @property
    def scheduleweek_name_25(self):
        """field `Schedule:Week Name 25`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_25` or None if not set
        """
        return self["Schedule:Week Name 25"]

    @scheduleweek_name_25.setter
    def scheduleweek_name_25(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 25`

        """
        self["Schedule:Week Name 25"] = value

    @property
    def start_month_25(self):
        """field `Start Month 25`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_25` or None if not set

        """
        return self["Start Month 25"]

    @start_month_25.setter
    def start_month_25(self, value=None):
        """Corresponds to IDD field `Start Month 25`"""
        self["Start Month 25"] = value

    @property
    def start_day_25(self):
        """field `Start Day 25`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_25` or None if not set

        """
        return self["Start Day 25"]

    @start_day_25.setter
    def start_day_25(self, value=None):
        """Corresponds to IDD field `Start Day 25`"""
        self["Start Day 25"] = value

    @property
    def end_month_25(self):
        """field `End Month 25`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_25` or None if not set

        """
        return self["End Month 25"]

    @end_month_25.setter
    def end_month_25(self, value=None):
        """Corresponds to IDD field `End Month 25`"""
        self["End Month 25"] = value

    @property
    def end_day_25(self):
        """field `End Day 25`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_25` or None if not set

        """
        return self["End Day 25"]

    @end_day_25.setter
    def end_day_25(self, value=None):
        """Corresponds to IDD field `End Day 25`"""
        self["End Day 25"] = value

    @property
    def scheduleweek_name_26(self):
        """field `Schedule:Week Name 26`


        Args:
            value (str): value for IDD Field `Schedule:Week Name 26`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `scheduleweek_name_26` or None if not set
        """
        return self["Schedule:Week Name 26"]

    @scheduleweek_name_26.setter
    def scheduleweek_name_26(self, value=None):
        """  Corresponds to IDD field `Schedule:Week Name 26`

        """
        self["Schedule:Week Name 26"] = value

    @property
    def start_month_26(self):
        """field `Start Month 26`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Start Month 26`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_month_26` or None if not set

        """
        return self["Start Month 26"]

    @start_month_26.setter
    def start_month_26(self, value=None):
        """Corresponds to IDD field `Start Month 26`"""
        self["Start Month 26"] = value

    @property
    def start_day_26(self):
        """field `Start Day 26`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Start Day 26`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `start_day_26` or None if not set

        """
        return self["Start Day 26"]

    @start_day_26.setter
    def start_day_26(self, value=None):
        """Corresponds to IDD field `Start Day 26`"""
        self["Start Day 26"] = value

    @property
    def end_month_26(self):
        """field `End Month 26`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month 26`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month_26` or None if not set

        """
        return self["End Month 26"]

    @end_month_26.setter
    def end_month_26(self, value=None):
        """Corresponds to IDD field `End Month 26`"""
        self["End Month 26"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value

    @property
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self):
        """field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        |  Schedule:Week for Weeks 27-53 are condensed
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3` or None if not set

        """
        return self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"]

    @end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3.setter
    def end_day_26_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3(
            self,
            value=None):
        """Corresponds to IDD field `End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3
        v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3`"""
        self[
            "End Day 26 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3 v3"] = value




class ScheduleCompact(DataObject):

    """ Corresponds to IDD object `Schedule:Compact`
        Irregular object.  Does not follow the usual definition for fields.  Fields A3... are:
        Through: Date
        For: Applicable days (ref: Schedule:Week:Compact)
        Interpolate: Yes/No (ref: Schedule:Day:Interval) -- optional, if not used will be "No"
        Until: <Time> (ref: Schedule:Day:Interval)
        <numeric value>
        words "Through","For","Interpolate","Until" must be included.
    """
    _schema = {'extensible-fields': OrderedDict([(u'field 1',
                                                  {'name': u'Field 1',
                                                   'pyname': u'field_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'alpha'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule type limits name',
                                       {'name': u'Schedule Type Limits Name',
                                        'pyname': u'schedule_type_limits_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': u'compactschedule',
               'group': u'Schedules',
               'min-fields': 5,
               'name': u'Schedule:Compact',
               'pyname': u'ScheduleCompact',
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
    def schedule_type_limits_name(self):
        """field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set

        """
        return self["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """Corresponds to IDD field `Schedule Type Limits Name`"""
        self["Schedule Type Limits Name"] = value

    def add_extensible(self,
                       field_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            field_1 (str): value for IDD Field `Field 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        field_1 = self.check_value("Field 1", field_1)
        vals.append(field_1)
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




class ScheduleConstant(DataObject):

    """ Corresponds to IDD object `Schedule:Constant`
        Constant hourly value for entire year.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule type limits name',
                                       {'name': u'Schedule Type Limits Name',
                                        'pyname': u'schedule_type_limits_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hourly value',
                                       {'name': u'Hourly Value',
                                        'pyname': u'hourly_value',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': u'singleline',
               'group': u'Schedules',
               'min-fields': 0,
               'name': u'Schedule:Constant',
               'pyname': u'ScheduleConstant',
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
    def schedule_type_limits_name(self):
        """field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set

        """
        return self["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """Corresponds to IDD field `Schedule Type Limits Name`"""
        self["Schedule Type Limits Name"] = value

    @property
    def hourly_value(self):
        """field `Hourly Value`

        Args:
            value (float): value for IDD Field `Hourly Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hourly_value` or None if not set

        """
        return self["Hourly Value"]

    @hourly_value.setter
    def hourly_value(self, value=None):
        """Corresponds to IDD field `Hourly Value`"""
        self["Hourly Value"] = value




class ScheduleFile(DataObject):

    """ Corresponds to IDD object `Schedule:File`
        A Schedule:File points to a text computer file that has 8760-8784 hours of data.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule type limits name',
                                       {'name': u'Schedule Type Limits Name',
                                        'pyname': u'schedule_type_limits_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'file name',
                                       {'name': u'File Name',
                                        'pyname': u'file_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'column number',
                                       {'name': u'Column Number',
                                        'pyname': u'column_number',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'rows to skip at top',
                                       {'name': u'Rows to Skip at Top',
                                        'pyname': u'rows_to_skip_at_top',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'number of hours of data',
                                       {'name': u'Number of Hours of Data',
                                        'pyname': u'number_of_hours_of_data',
                                        'default': 8760.0,
                                        'maximum': 8784.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 8760.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'column separator',
                                       {'name': u'Column Separator',
                                        'pyname': u'column_separator',
                                        'default': u'Comma',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Comma',
                                                            u'Tab',
                                                            u'Fixed',
                                                            u'Semicolon'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'interpolate to timestep',
                                       {'name': u'Interpolate to Timestep',
                                        'pyname': u'interpolate_to_timestep',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minutes per item',
                                       {'name': u'Minutes per Item',
                                        'pyname': u'minutes_per_item',
                                        'maximum': 60,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'Schedules',
               'min-fields': 5,
               'name': u'Schedule:File',
               'pyname': u'ScheduleFile',
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
    def schedule_type_limits_name(self):
        """field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set

        """
        return self["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """Corresponds to IDD field `Schedule Type Limits Name`"""
        self["Schedule Type Limits Name"] = value

    @property
    def file_name(self):
        """field `File Name`

        Args:
            value (str): value for IDD Field `File Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `file_name` or None if not set

        """
        return self["File Name"]

    @file_name.setter
    def file_name(self, value=None):
        """Corresponds to IDD field `File Name`"""
        self["File Name"] = value

    @property
    def column_number(self):
        """field `Column Number`

        |  value >= 1

        Args:
            value (int): value for IDD Field `Column Number`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `column_number` or None if not set

        """
        return self["Column Number"]

    @column_number.setter
    def column_number(self, value=None):
        """Corresponds to IDD field `Column Number`"""
        self["Column Number"] = value

    @property
    def rows_to_skip_at_top(self):
        """field `Rows to Skip at Top`

        Args:
            value (int): value for IDD Field `Rows to Skip at Top`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `rows_to_skip_at_top` or None if not set

        """
        return self["Rows to Skip at Top"]

    @rows_to_skip_at_top.setter
    def rows_to_skip_at_top(self, value=None):
        """Corresponds to IDD field `Rows to Skip at Top`"""
        self["Rows to Skip at Top"] = value

    @property
    def number_of_hours_of_data(self):
        """field `Number of Hours of Data`

        |  8760 hours does not account for leap years, 8784 does.
        |  should be either 8760 or 8784
        |  Default value: 8760.0
        |  value >= 8760.0
        |  value <= 8784.0

        Args:
            value (float): value for IDD Field `Number of Hours of Data`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `number_of_hours_of_data` or None if not set

        """
        return self["Number of Hours of Data"]

    @number_of_hours_of_data.setter
    def number_of_hours_of_data(self, value=8760.0):
        """Corresponds to IDD field `Number of Hours of Data`"""
        self["Number of Hours of Data"] = value

    @property
    def column_separator(self):
        """field `Column Separator`

        |  Default value: Comma

        Args:
            value (str): value for IDD Field `Column Separator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `column_separator` or None if not set

        """
        return self["Column Separator"]

    @column_separator.setter
    def column_separator(self, value="Comma"):
        """Corresponds to IDD field `Column Separator`"""
        self["Column Separator"] = value

    @property
    def interpolate_to_timestep(self):
        """field `Interpolate to Timestep`

        |  when the interval does not match the user specified timestep a "Yes" choice will average between the intervals request (to
        |  timestep resolution.  a "No" choice will use the interval value at the simulation timestep without regard to if it matches
        |  the boundary or not.
        |  Default value: No

        Args:
            value (str): value for IDD Field `Interpolate to Timestep`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `interpolate_to_timestep` or None if not set

        """
        return self["Interpolate to Timestep"]

    @interpolate_to_timestep.setter
    def interpolate_to_timestep(self, value="No"):
        """Corresponds to IDD field `Interpolate to Timestep`"""
        self["Interpolate to Timestep"] = value

    @property
    def minutes_per_item(self):
        """field `Minutes per Item`

        |  Must be evenly divisible into 60
        |  value >= 1
        |  value <= 60

        Args:
            value (int): value for IDD Field `Minutes per Item`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `minutes_per_item` or None if not set

        """
        return self["Minutes per Item"]

    @minutes_per_item.setter
    def minutes_per_item(self, value=None):
        """Corresponds to IDD field `Minutes per Item`"""
        self["Minutes per Item"] = value


