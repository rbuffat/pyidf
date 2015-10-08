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




class ScheduleDayList(DataObject):

    """ Corresponds to IDD object `Schedule:Day:List`
        Schedule:Day:List will allow the user to list 24 hours worth of values, which can be sub-hourly in nature.
    """
    _schema = {'extensible-fields': OrderedDict([(u'value',
                                                  {'name': u'Value',
                                                   'pyname': u'value',
                                                   'default': 0.0,
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

    def add_extensible(self,
                       value=None,
                       ):
        """Add values for extensible fields.

        Args:

            value (float): value for IDD Field `Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        value = self.check_value("Value", value)
        vals.append(value)
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
    _schema = {'extensible-fields': OrderedDict([(u'schedule:week',
                                                  {'name': u'Schedule:Week',
                                                   'pyname': u'scheduleweek',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'start month',
                                                  {'name': u'Start Month',
                                                   'pyname': u'start_month',
                                                   'maximum': 12,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'minimum': 1,
                                                   'autocalculatable': False,
                                                   'type': u'integer'}),
                                                 (u'start day',
                                                  {'name': u'Start Day',
                                                   'pyname': u'start_day',
                                                   'maximum': 31,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'minimum': 1,
                                                   'autocalculatable': False,
                                                   'type': u'integer'}),
                                                 (u'end month',
                                                  {'name': u'End Month',
                                                   'pyname': u'end_month',
                                                   'maximum': 12,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'minimum': 1,
                                                   'autocalculatable': False,
                                                   'type': u'integer'}),
                                                 (u'end day',
                                                  {'name': u'End Day',
                                                   'pyname': u'end_day',
                                                   'maximum': 31,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'minimum': 1,
                                                   'autocalculatable': False,
                                                   'type': u'integer'})]),
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

    def add_extensible(self,
                       scheduleweek=None,
                       start_month=None,
                       start_day=None,
                       end_month=None,
                       end_day=None,
                       ):
        """Add values for extensible fields.

        Args:

            scheduleweek (str): value for IDD Field `Schedule:Week`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            start_month (int): value for IDD Field `Start Month`
                value >= 1
                value <= 12
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            start_day (int): value for IDD Field `Start Day`
                value >= 1
                value <= 31
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            end_month (int): value for IDD Field `End Month`
                value >= 1
                value <= 12
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            end_day (int): value for IDD Field `End Day`
                value >= 1
                value <= 31
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        scheduleweek = self.check_value("Schedule:Week", scheduleweek)
        vals.append(scheduleweek)
        start_month = self.check_value("Start Month", start_month)
        vals.append(start_month)
        start_day = self.check_value("Start Day", start_day)
        vals.append(start_day)
        end_month = self.check_value("End Month", end_month)
        vals.append(end_month)
        end_day = self.check_value("End Day", end_day)
        vals.append(end_day)
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
    _schema = {'extensible-fields': OrderedDict([(u'field',
                                                  {'name': u'Field',
                                                   'pyname': u'field',
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
                       field=None,
                       ):
        """Add values for extensible fields.

        Args:

            field (str): value for IDD Field `Field`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        field = self.check_value("Field", field)
        vals.append(field)
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


