from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class ScheduleTypeLimits(object):
    """ Corresponds to IDD object `ScheduleTypeLimits`
        ScheduleTypeLimits specifies the data types and limits for the values contained in schedules
    """
    internal_name = "ScheduleTypeLimits"
    field_count = 5
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ScheduleTypeLimits`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Lower Limit Value"] = None
        self._data["Upper Limit Value"] = None
        self._data["Numeric Type"] = None
        self._data["Unit Type"] = None
        self._data["extensibles"] = []
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
            self.lower_limit_value = None
        else:
            self.lower_limit_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.upper_limit_value = None
        else:
            self.upper_limit_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.numeric_type = None
        else:
            self.numeric_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.unit_type = None
        else:
            self.unit_type = vals[i]
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
        used to validate schedule types in various schedule objects

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
                                 ' for field `ScheduleTypeLimits.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleTypeLimits.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleTypeLimits.name`')
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
        """  Corresponds to IDD Field `Lower Limit Value`
        lower limit (real or integer) for the Schedule Type.  e.g. if fraction, this is 0.0

        Args:
            value (float): value for IDD Field `Lower Limit Value`
                Units are based on field `A3`
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
                                 ' for field `ScheduleTypeLimits.lower_limit_value`'.format(value))
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
        """  Corresponds to IDD Field `Upper Limit Value`
        upper limit (real or integer) for the Schedule Type.  e.g. if fraction, this is 1.0

        Args:
            value (float): value for IDD Field `Upper Limit Value`
                Units are based on field `A3`
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
                                 ' for field `ScheduleTypeLimits.upper_limit_value`'.format(value))
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
        """  Corresponds to IDD Field `Numeric Type`
        Numeric type is either Continuous (all numbers within the min and
        max are valid or Discrete (only integer numbers between min and
        max are valid.  (Could also allow REAL and INTEGER to mean the
        same things)

        Args:
            value (str): value for IDD Field `Numeric Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ScheduleTypeLimits.numeric_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleTypeLimits.numeric_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleTypeLimits.numeric_type`')
            vals = {}
            vals["continuous"] = "Continuous"
            vals["discrete"] = "Discrete"
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
                                     'field `ScheduleTypeLimits.numeric_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ScheduleTypeLimits.numeric_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Unit Type`
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
            value (str): value for IDD Field `Unit Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ScheduleTypeLimits.unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleTypeLimits.unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleTypeLimits.unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["deltatemperature"] = "DeltaTemperature"
            vals["precipitationrate"] = "PrecipitationRate"
            vals["angle"] = "Angle"
            vals["convectioncoefficient"] = "ConvectionCoefficient"
            vals["activitylevel"] = "ActivityLevel"
            vals["velocity"] = "Velocity"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
            vals["availability"] = "Availability"
            vals["percent"] = "Percent"
            vals["control"] = "Control"
            vals["mode"] = "Mode"
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
                                     'field `ScheduleTypeLimits.unit_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ScheduleTypeLimits.unit_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Unit Type"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ScheduleTypeLimits:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ScheduleTypeLimits:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ScheduleTypeLimits: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ScheduleTypeLimits: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ScheduleDayHourly(object):
    """ Corresponds to IDD object `Schedule:Day:Hourly`
        A Schedule:Day:Hourly contains 24 values for each hour of the day.
    """
    internal_name = "Schedule:Day:Hourly"
    field_count = 26
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 26
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Day:Hourly`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["Hour 1"] = None
        self._data["Hour 2"] = None
        self._data["Hour 3"] = None
        self._data["Hour 4"] = None
        self._data["Hour 5"] = None
        self._data["Hour 6"] = None
        self._data["Hour 7"] = None
        self._data["Hour 8"] = None
        self._data["Hour 9"] = None
        self._data["Hour 10"] = None
        self._data["Hour 11"] = None
        self._data["Hour 12"] = None
        self._data["Hour 13"] = None
        self._data["Hour 14"] = None
        self._data["Hour 15"] = None
        self._data["Hour 16"] = None
        self._data["Hour 17"] = None
        self._data["Hour 18"] = None
        self._data["Hour 19"] = None
        self._data["Hour 20"] = None
        self._data["Hour 21"] = None
        self._data["Hour 22"] = None
        self._data["Hour 23"] = None
        self._data["Hour 24"] = None
        self._data["extensibles"] = []
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
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_1 = None
        else:
            self.hour_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_2 = None
        else:
            self.hour_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_3 = None
        else:
            self.hour_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_4 = None
        else:
            self.hour_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_5 = None
        else:
            self.hour_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_6 = None
        else:
            self.hour_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_7 = None
        else:
            self.hour_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_8 = None
        else:
            self.hour_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_9 = None
        else:
            self.hour_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_10 = None
        else:
            self.hour_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_11 = None
        else:
            self.hour_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_12 = None
        else:
            self.hour_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_13 = None
        else:
            self.hour_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_14 = None
        else:
            self.hour_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_15 = None
        else:
            self.hour_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_16 = None
        else:
            self.hour_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_17 = None
        else:
            self.hour_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_18 = None
        else:
            self.hour_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_19 = None
        else:
            self.hour_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_20 = None
        else:
            self.hour_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_21 = None
        else:
            self.hour_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_22 = None
        else:
            self.hour_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_23 = None
        else:
            self.hour_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hour_24 = None
        else:
            self.hour_24 = vals[i]
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
                                 ' for field `ScheduleDayHourly.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleDayHourly.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleDayHourly.name`')
        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`
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
                                 ' for field `ScheduleDayHourly.schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleDayHourly.schedule_type_limits_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleDayHourly.schedule_type_limits_name`')
        self._data["Schedule Type Limits Name"] = value

    @property
    def hour_1(self):
        """Get hour_1

        Returns:
            float: the value of `hour_1` or None if not set
        """
        return self._data["Hour 1"]

    @hour_1.setter
    def hour_1(self, value=0.0):
        """  Corresponds to IDD Field `Hour 1`

        Args:
            value (float): value for IDD Field `Hour 1`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_1`'.format(value))
        self._data["Hour 1"] = value

    @property
    def hour_2(self):
        """Get hour_2

        Returns:
            float: the value of `hour_2` or None if not set
        """
        return self._data["Hour 2"]

    @hour_2.setter
    def hour_2(self, value=0.0):
        """  Corresponds to IDD Field `Hour 2`

        Args:
            value (float): value for IDD Field `Hour 2`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_2`'.format(value))
        self._data["Hour 2"] = value

    @property
    def hour_3(self):
        """Get hour_3

        Returns:
            float: the value of `hour_3` or None if not set
        """
        return self._data["Hour 3"]

    @hour_3.setter
    def hour_3(self, value=0.0):
        """  Corresponds to IDD Field `Hour 3`

        Args:
            value (float): value for IDD Field `Hour 3`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_3`'.format(value))
        self._data["Hour 3"] = value

    @property
    def hour_4(self):
        """Get hour_4

        Returns:
            float: the value of `hour_4` or None if not set
        """
        return self._data["Hour 4"]

    @hour_4.setter
    def hour_4(self, value=0.0):
        """  Corresponds to IDD Field `Hour 4`

        Args:
            value (float): value for IDD Field `Hour 4`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_4`'.format(value))
        self._data["Hour 4"] = value

    @property
    def hour_5(self):
        """Get hour_5

        Returns:
            float: the value of `hour_5` or None if not set
        """
        return self._data["Hour 5"]

    @hour_5.setter
    def hour_5(self, value=0.0):
        """  Corresponds to IDD Field `Hour 5`

        Args:
            value (float): value for IDD Field `Hour 5`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_5`'.format(value))
        self._data["Hour 5"] = value

    @property
    def hour_6(self):
        """Get hour_6

        Returns:
            float: the value of `hour_6` or None if not set
        """
        return self._data["Hour 6"]

    @hour_6.setter
    def hour_6(self, value=0.0):
        """  Corresponds to IDD Field `Hour 6`

        Args:
            value (float): value for IDD Field `Hour 6`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_6`'.format(value))
        self._data["Hour 6"] = value

    @property
    def hour_7(self):
        """Get hour_7

        Returns:
            float: the value of `hour_7` or None if not set
        """
        return self._data["Hour 7"]

    @hour_7.setter
    def hour_7(self, value=0.0):
        """  Corresponds to IDD Field `Hour 7`

        Args:
            value (float): value for IDD Field `Hour 7`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_7`'.format(value))
        self._data["Hour 7"] = value

    @property
    def hour_8(self):
        """Get hour_8

        Returns:
            float: the value of `hour_8` or None if not set
        """
        return self._data["Hour 8"]

    @hour_8.setter
    def hour_8(self, value=0.0):
        """  Corresponds to IDD Field `Hour 8`

        Args:
            value (float): value for IDD Field `Hour 8`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_8`'.format(value))
        self._data["Hour 8"] = value

    @property
    def hour_9(self):
        """Get hour_9

        Returns:
            float: the value of `hour_9` or None if not set
        """
        return self._data["Hour 9"]

    @hour_9.setter
    def hour_9(self, value=0.0):
        """  Corresponds to IDD Field `Hour 9`

        Args:
            value (float): value for IDD Field `Hour 9`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_9`'.format(value))
        self._data["Hour 9"] = value

    @property
    def hour_10(self):
        """Get hour_10

        Returns:
            float: the value of `hour_10` or None if not set
        """
        return self._data["Hour 10"]

    @hour_10.setter
    def hour_10(self, value=0.0):
        """  Corresponds to IDD Field `Hour 10`

        Args:
            value (float): value for IDD Field `Hour 10`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_10`'.format(value))
        self._data["Hour 10"] = value

    @property
    def hour_11(self):
        """Get hour_11

        Returns:
            float: the value of `hour_11` or None if not set
        """
        return self._data["Hour 11"]

    @hour_11.setter
    def hour_11(self, value=0.0):
        """  Corresponds to IDD Field `Hour 11`

        Args:
            value (float): value for IDD Field `Hour 11`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_11`'.format(value))
        self._data["Hour 11"] = value

    @property
    def hour_12(self):
        """Get hour_12

        Returns:
            float: the value of `hour_12` or None if not set
        """
        return self._data["Hour 12"]

    @hour_12.setter
    def hour_12(self, value=0.0):
        """  Corresponds to IDD Field `Hour 12`

        Args:
            value (float): value for IDD Field `Hour 12`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_12`'.format(value))
        self._data["Hour 12"] = value

    @property
    def hour_13(self):
        """Get hour_13

        Returns:
            float: the value of `hour_13` or None if not set
        """
        return self._data["Hour 13"]

    @hour_13.setter
    def hour_13(self, value=0.0):
        """  Corresponds to IDD Field `Hour 13`

        Args:
            value (float): value for IDD Field `Hour 13`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_13`'.format(value))
        self._data["Hour 13"] = value

    @property
    def hour_14(self):
        """Get hour_14

        Returns:
            float: the value of `hour_14` or None if not set
        """
        return self._data["Hour 14"]

    @hour_14.setter
    def hour_14(self, value=0.0):
        """  Corresponds to IDD Field `Hour 14`

        Args:
            value (float): value for IDD Field `Hour 14`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_14`'.format(value))
        self._data["Hour 14"] = value

    @property
    def hour_15(self):
        """Get hour_15

        Returns:
            float: the value of `hour_15` or None if not set
        """
        return self._data["Hour 15"]

    @hour_15.setter
    def hour_15(self, value=0.0):
        """  Corresponds to IDD Field `Hour 15`

        Args:
            value (float): value for IDD Field `Hour 15`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_15`'.format(value))
        self._data["Hour 15"] = value

    @property
    def hour_16(self):
        """Get hour_16

        Returns:
            float: the value of `hour_16` or None if not set
        """
        return self._data["Hour 16"]

    @hour_16.setter
    def hour_16(self, value=0.0):
        """  Corresponds to IDD Field `Hour 16`

        Args:
            value (float): value for IDD Field `Hour 16`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_16`'.format(value))
        self._data["Hour 16"] = value

    @property
    def hour_17(self):
        """Get hour_17

        Returns:
            float: the value of `hour_17` or None if not set
        """
        return self._data["Hour 17"]

    @hour_17.setter
    def hour_17(self, value=0.0):
        """  Corresponds to IDD Field `Hour 17`

        Args:
            value (float): value for IDD Field `Hour 17`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_17`'.format(value))
        self._data["Hour 17"] = value

    @property
    def hour_18(self):
        """Get hour_18

        Returns:
            float: the value of `hour_18` or None if not set
        """
        return self._data["Hour 18"]

    @hour_18.setter
    def hour_18(self, value=0.0):
        """  Corresponds to IDD Field `Hour 18`

        Args:
            value (float): value for IDD Field `Hour 18`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_18`'.format(value))
        self._data["Hour 18"] = value

    @property
    def hour_19(self):
        """Get hour_19

        Returns:
            float: the value of `hour_19` or None if not set
        """
        return self._data["Hour 19"]

    @hour_19.setter
    def hour_19(self, value=0.0):
        """  Corresponds to IDD Field `Hour 19`

        Args:
            value (float): value for IDD Field `Hour 19`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_19`'.format(value))
        self._data["Hour 19"] = value

    @property
    def hour_20(self):
        """Get hour_20

        Returns:
            float: the value of `hour_20` or None if not set
        """
        return self._data["Hour 20"]

    @hour_20.setter
    def hour_20(self, value=0.0):
        """  Corresponds to IDD Field `Hour 20`

        Args:
            value (float): value for IDD Field `Hour 20`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_20`'.format(value))
        self._data["Hour 20"] = value

    @property
    def hour_21(self):
        """Get hour_21

        Returns:
            float: the value of `hour_21` or None if not set
        """
        return self._data["Hour 21"]

    @hour_21.setter
    def hour_21(self, value=0.0):
        """  Corresponds to IDD Field `Hour 21`

        Args:
            value (float): value for IDD Field `Hour 21`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_21`'.format(value))
        self._data["Hour 21"] = value

    @property
    def hour_22(self):
        """Get hour_22

        Returns:
            float: the value of `hour_22` or None if not set
        """
        return self._data["Hour 22"]

    @hour_22.setter
    def hour_22(self, value=0.0):
        """  Corresponds to IDD Field `Hour 22`

        Args:
            value (float): value for IDD Field `Hour 22`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_22`'.format(value))
        self._data["Hour 22"] = value

    @property
    def hour_23(self):
        """Get hour_23

        Returns:
            float: the value of `hour_23` or None if not set
        """
        return self._data["Hour 23"]

    @hour_23.setter
    def hour_23(self, value=0.0):
        """  Corresponds to IDD Field `Hour 23`

        Args:
            value (float): value for IDD Field `Hour 23`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_23`'.format(value))
        self._data["Hour 23"] = value

    @property
    def hour_24(self):
        """Get hour_24

        Returns:
            float: the value of `hour_24` or None if not set
        """
        return self._data["Hour 24"]

    @hour_24.setter
    def hour_24(self, value=0.0):
        """  Corresponds to IDD Field `Hour 24`

        Args:
            value (float): value for IDD Field `Hour 24`
                Default value: 0.0
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
                                 ' for field `ScheduleDayHourly.hour_24`'.format(value))
        self._data["Hour 24"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ScheduleDayHourly:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ScheduleDayHourly:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ScheduleDayHourly: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ScheduleDayHourly: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ScheduleDayInterval(object):
    """ Corresponds to IDD object `Schedule:Day:Interval`
        A Schedule:Day:Interval contains a full day of values with specified end times for each value
        Currently, is set up to allow for 10 minute intervals for an entire day.
    """
    internal_name = "Schedule:Day:Interval"
    field_count = 3
    required_fields = ["Name"]
    extensible_fields = 2
    format = None
    min_fields = 5
    extensible_keys = ["Time 1", "Value Until Time 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Day:Interval`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["Interpolate to Timestep"] = None
        self._data["extensibles"] = []
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
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.interpolate_to_timestep = None
        else:
            self.interpolate_to_timestep = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `ScheduleDayInterval.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleDayInterval.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleDayInterval.name`')
        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`
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
                                 ' for field `ScheduleDayInterval.schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleDayInterval.schedule_type_limits_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleDayInterval.schedule_type_limits_name`')
        self._data["Schedule Type Limits Name"] = value

    @property
    def interpolate_to_timestep(self):
        """Get interpolate_to_timestep

        Returns:
            str: the value of `interpolate_to_timestep` or None if not set
        """
        return self._data["Interpolate to Timestep"]

    @interpolate_to_timestep.setter
    def interpolate_to_timestep(self, value="No"):
        """  Corresponds to IDD Field `Interpolate to Timestep`
        when the interval does not match the user specified timestep a Yes choice will average between the intervals request (to
        timestep resolution.  a No choice will use the interval value at the simulation timestep without regard to if it matches
        the boundary or not.

        Args:
            value (str): value for IDD Field `Interpolate to Timestep`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `ScheduleDayInterval.interpolate_to_timestep`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleDayInterval.interpolate_to_timestep`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleDayInterval.interpolate_to_timestep`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `ScheduleDayInterval.interpolate_to_timestep`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ScheduleDayInterval.interpolate_to_timestep`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Interpolate to Timestep"] = value

    def add_extensible(self,
                       time_1=None,
                       value_until_time_1=None,
                       ):
        """ Add values for extensible fields

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
        vals.append(self._check_time_1(time_1))
        vals.append(self._check_value_until_time_1(value_until_time_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_time_1(self, value):
        """ Validates falue of field `Time 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ScheduleDayInterval.time_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleDayInterval.time_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleDayInterval.time_1`')
        return value

    def _check_value_until_time_1(self, value):
        """ Validates falue of field `Value Until Time 1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ScheduleDayInterval.value_until_time_1`'.format(value))
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ScheduleDayInterval:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ScheduleDayInterval:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ScheduleDayInterval: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ScheduleDayInterval: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ScheduleDayList(object):
    """ Corresponds to IDD object `Schedule:Day:List`
        Schedule:Day:List will allow the user to list 24 hours worth of values, which can be sub-hourly in nature.
    """
    internal_name = "Schedule:Day:List"
    field_count = 4
    required_fields = ["Name"]
    extensible_fields = 1
    format = None
    min_fields = 5
    extensible_keys = ["Value"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Day:List`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["Interpolate to Timestep"] = None
        self._data["Minutes per Item"] = None
        self._data["extensibles"] = []
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
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.interpolate_to_timestep = None
        else:
            self.interpolate_to_timestep = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minutes_per_item = None
        else:
            self.minutes_per_item = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `ScheduleDayList.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleDayList.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleDayList.name`')
        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`
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
                                 ' for field `ScheduleDayList.schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleDayList.schedule_type_limits_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleDayList.schedule_type_limits_name`')
        self._data["Schedule Type Limits Name"] = value

    @property
    def interpolate_to_timestep(self):
        """Get interpolate_to_timestep

        Returns:
            str: the value of `interpolate_to_timestep` or None if not set
        """
        return self._data["Interpolate to Timestep"]

    @interpolate_to_timestep.setter
    def interpolate_to_timestep(self, value="No"):
        """  Corresponds to IDD Field `Interpolate to Timestep`
        when the interval does not match the user specified timestep a "Yes" choice will average between the intervals request (to
        timestep resolution.  a "No" choice will use the interval value at the simulation timestep without regard to if it matches
        the boundary or not.

        Args:
            value (str): value for IDD Field `Interpolate to Timestep`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `ScheduleDayList.interpolate_to_timestep`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleDayList.interpolate_to_timestep`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleDayList.interpolate_to_timestep`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `ScheduleDayList.interpolate_to_timestep`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ScheduleDayList.interpolate_to_timestep`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Interpolate to Timestep"] = value

    @property
    def minutes_per_item(self):
        """Get minutes_per_item

        Returns:
            int: the value of `minutes_per_item` or None if not set
        """
        return self._data["Minutes per Item"]

    @minutes_per_item.setter
    def minutes_per_item(self, value=None):
        """  Corresponds to IDD Field `Minutes per Item`
        Must be evenly divisible into 60

        Args:
            value (int): value for IDD Field `Minutes per Item`
                value >= 1
                value <= 60
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ScheduleDayList.minutes_per_item`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ScheduleDayList.minutes_per_item`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ScheduleDayList.minutes_per_item`')
            if value > 60:
                raise ValueError('value need to be smaller 60 '
                                 'for field `ScheduleDayList.minutes_per_item`')
        self._data["Minutes per Item"] = value

    def add_extensible(self,
                       value=0.0,
                       ):
        """ Add values for extensible fields

        Args:

            value (float): value for IDD Field `Value`
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_value(value))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_value(self, value):
        """ Validates falue of field `Value`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ScheduleDayList.value`'.format(value))
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ScheduleDayList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ScheduleDayList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ScheduleDayList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ScheduleDayList: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ScheduleWeekDaily(object):
    """ Corresponds to IDD object `Schedule:Week:Daily`
        A Schedule:Week:Daily contains 12 Schedule:Day:Hourly objects, one for each day type.
    """
    internal_name = "Schedule:Week:Daily"
    field_count = 13
    required_fields = ["Name", "Sunday Schedule:Day Name", "Monday Schedule:Day Name", "Tuesday Schedule:Day Name", "Wednesday Schedule:Day Name", "Thursday Schedule:Day Name", "Friday Schedule:Day Name", "Saturday Schedule:Day Name", "Holiday Schedule:Day Name", "SummerDesignDay Schedule:Day Name", "WinterDesignDay Schedule:Day Name", "CustomDay1 Schedule:Day Name", "CustomDay2 Schedule:Day Name"]
    extensible_fields = 0
    format = None
    min_fields = 13
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Week:Daily`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Sunday Schedule:Day Name"] = None
        self._data["Monday Schedule:Day Name"] = None
        self._data["Tuesday Schedule:Day Name"] = None
        self._data["Wednesday Schedule:Day Name"] = None
        self._data["Thursday Schedule:Day Name"] = None
        self._data["Friday Schedule:Day Name"] = None
        self._data["Saturday Schedule:Day Name"] = None
        self._data["Holiday Schedule:Day Name"] = None
        self._data["SummerDesignDay Schedule:Day Name"] = None
        self._data["WinterDesignDay Schedule:Day Name"] = None
        self._data["CustomDay1 Schedule:Day Name"] = None
        self._data["CustomDay2 Schedule:Day Name"] = None
        self._data["extensibles"] = []
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
            self.sunday_scheduleday_name = None
        else:
            self.sunday_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.monday_scheduleday_name = None
        else:
            self.monday_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tuesday_scheduleday_name = None
        else:
            self.tuesday_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wednesday_scheduleday_name = None
        else:
            self.wednesday_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thursday_scheduleday_name = None
        else:
            self.thursday_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.friday_scheduleday_name = None
        else:
            self.friday_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.saturday_scheduleday_name = None
        else:
            self.saturday_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.holiday_scheduleday_name = None
        else:
            self.holiday_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.summerdesignday_scheduleday_name = None
        else:
            self.summerdesignday_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.winterdesignday_scheduleday_name = None
        else:
            self.winterdesignday_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.customday1_scheduleday_name = None
        else:
            self.customday1_scheduleday_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.customday2_scheduleday_name = None
        else:
            self.customday2_scheduleday_name = vals[i]
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
                                 ' for field `ScheduleWeekDaily.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.name`')
        self._data["Name"] = value

    @property
    def sunday_scheduleday_name(self):
        """Get sunday_scheduleday_name

        Returns:
            str: the value of `sunday_scheduleday_name` or None if not set
        """
        return self._data["Sunday Schedule:Day Name"]

    @sunday_scheduleday_name.setter
    def sunday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `Sunday Schedule:Day Name`

        Args:
            value (str): value for IDD Field `Sunday Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.sunday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.sunday_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.sunday_scheduleday_name`')
        self._data["Sunday Schedule:Day Name"] = value

    @property
    def monday_scheduleday_name(self):
        """Get monday_scheduleday_name

        Returns:
            str: the value of `monday_scheduleday_name` or None if not set
        """
        return self._data["Monday Schedule:Day Name"]

    @monday_scheduleday_name.setter
    def monday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `Monday Schedule:Day Name`

        Args:
            value (str): value for IDD Field `Monday Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.monday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.monday_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.monday_scheduleday_name`')
        self._data["Monday Schedule:Day Name"] = value

    @property
    def tuesday_scheduleday_name(self):
        """Get tuesday_scheduleday_name

        Returns:
            str: the value of `tuesday_scheduleday_name` or None if not set
        """
        return self._data["Tuesday Schedule:Day Name"]

    @tuesday_scheduleday_name.setter
    def tuesday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `Tuesday Schedule:Day Name`

        Args:
            value (str): value for IDD Field `Tuesday Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.tuesday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.tuesday_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.tuesday_scheduleday_name`')
        self._data["Tuesday Schedule:Day Name"] = value

    @property
    def wednesday_scheduleday_name(self):
        """Get wednesday_scheduleday_name

        Returns:
            str: the value of `wednesday_scheduleday_name` or None if not set
        """
        return self._data["Wednesday Schedule:Day Name"]

    @wednesday_scheduleday_name.setter
    def wednesday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `Wednesday Schedule:Day Name`

        Args:
            value (str): value for IDD Field `Wednesday Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.wednesday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.wednesday_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.wednesday_scheduleday_name`')
        self._data["Wednesday Schedule:Day Name"] = value

    @property
    def thursday_scheduleday_name(self):
        """Get thursday_scheduleday_name

        Returns:
            str: the value of `thursday_scheduleday_name` or None if not set
        """
        return self._data["Thursday Schedule:Day Name"]

    @thursday_scheduleday_name.setter
    def thursday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `Thursday Schedule:Day Name`

        Args:
            value (str): value for IDD Field `Thursday Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.thursday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.thursday_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.thursday_scheduleday_name`')
        self._data["Thursday Schedule:Day Name"] = value

    @property
    def friday_scheduleday_name(self):
        """Get friday_scheduleday_name

        Returns:
            str: the value of `friday_scheduleday_name` or None if not set
        """
        return self._data["Friday Schedule:Day Name"]

    @friday_scheduleday_name.setter
    def friday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `Friday Schedule:Day Name`

        Args:
            value (str): value for IDD Field `Friday Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.friday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.friday_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.friday_scheduleday_name`')
        self._data["Friday Schedule:Day Name"] = value

    @property
    def saturday_scheduleday_name(self):
        """Get saturday_scheduleday_name

        Returns:
            str: the value of `saturday_scheduleday_name` or None if not set
        """
        return self._data["Saturday Schedule:Day Name"]

    @saturday_scheduleday_name.setter
    def saturday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `Saturday Schedule:Day Name`

        Args:
            value (str): value for IDD Field `Saturday Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.saturday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.saturday_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.saturday_scheduleday_name`')
        self._data["Saturday Schedule:Day Name"] = value

    @property
    def holiday_scheduleday_name(self):
        """Get holiday_scheduleday_name

        Returns:
            str: the value of `holiday_scheduleday_name` or None if not set
        """
        return self._data["Holiday Schedule:Day Name"]

    @holiday_scheduleday_name.setter
    def holiday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `Holiday Schedule:Day Name`

        Args:
            value (str): value for IDD Field `Holiday Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.holiday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.holiday_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.holiday_scheduleday_name`')
        self._data["Holiday Schedule:Day Name"] = value

    @property
    def summerdesignday_scheduleday_name(self):
        """Get summerdesignday_scheduleday_name

        Returns:
            str: the value of `summerdesignday_scheduleday_name` or None if not set
        """
        return self._data["SummerDesignDay Schedule:Day Name"]

    @summerdesignday_scheduleday_name.setter
    def summerdesignday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `SummerDesignDay Schedule:Day Name`

        Args:
            value (str): value for IDD Field `SummerDesignDay Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.summerdesignday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.summerdesignday_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.summerdesignday_scheduleday_name`')
        self._data["SummerDesignDay Schedule:Day Name"] = value

    @property
    def winterdesignday_scheduleday_name(self):
        """Get winterdesignday_scheduleday_name

        Returns:
            str: the value of `winterdesignday_scheduleday_name` or None if not set
        """
        return self._data["WinterDesignDay Schedule:Day Name"]

    @winterdesignday_scheduleday_name.setter
    def winterdesignday_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `WinterDesignDay Schedule:Day Name`

        Args:
            value (str): value for IDD Field `WinterDesignDay Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.winterdesignday_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.winterdesignday_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.winterdesignday_scheduleday_name`')
        self._data["WinterDesignDay Schedule:Day Name"] = value

    @property
    def customday1_scheduleday_name(self):
        """Get customday1_scheduleday_name

        Returns:
            str: the value of `customday1_scheduleday_name` or None if not set
        """
        return self._data["CustomDay1 Schedule:Day Name"]

    @customday1_scheduleday_name.setter
    def customday1_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `CustomDay1 Schedule:Day Name`

        Args:
            value (str): value for IDD Field `CustomDay1 Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.customday1_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.customday1_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.customday1_scheduleday_name`')
        self._data["CustomDay1 Schedule:Day Name"] = value

    @property
    def customday2_scheduleday_name(self):
        """Get customday2_scheduleday_name

        Returns:
            str: the value of `customday2_scheduleday_name` or None if not set
        """
        return self._data["CustomDay2 Schedule:Day Name"]

    @customday2_scheduleday_name.setter
    def customday2_scheduleday_name(self, value=None):
        """  Corresponds to IDD Field `CustomDay2 Schedule:Day Name`

        Args:
            value (str): value for IDD Field `CustomDay2 Schedule:Day Name`
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
                                 ' for field `ScheduleWeekDaily.customday2_scheduleday_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekDaily.customday2_scheduleday_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekDaily.customday2_scheduleday_name`')
        self._data["CustomDay2 Schedule:Day Name"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ScheduleWeekDaily:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ScheduleWeekDaily:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ScheduleWeekDaily: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ScheduleWeekDaily: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ScheduleWeekCompact(object):
    """ Corresponds to IDD object `Schedule:Week:Compact`
        Compact definition for Schedule:Day:List
    """
    internal_name = "Schedule:Week:Compact"
    field_count = 1
    required_fields = ["Name"]
    extensible_fields = 2
    format = None
    min_fields = 3
    extensible_keys = ["DayType List 1", "Schedule:Day Name 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Week:Compact`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["extensibles"] = []
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
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `ScheduleWeekCompact.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekCompact.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekCompact.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       daytype_list_1=None,
                       scheduleday_name_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            daytype_list_1 (str): value for IDD Field `DayType List 1`
                Accepted values are:
                      - AllDays
                      - Weekdays
                      - Weekends
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - Holiday
                      - SummerDesignDay
                      - WinterDesignDay
                      - CustomDay1
                      - CustomDay2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            scheduleday_name_1 (str): value for IDD Field `Schedule:Day Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_daytype_list_1(daytype_list_1))
        vals.append(self._check_scheduleday_name_1(scheduleday_name_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_daytype_list_1(self, value):
        """ Validates falue of field `DayType List 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ScheduleWeekCompact.daytype_list_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekCompact.daytype_list_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekCompact.daytype_list_1`')
            vals = {}
            vals["alldays"] = "AllDays"
            vals["weekdays"] = "Weekdays"
            vals["weekends"] = "Weekends"
            vals["sunday"] = "Sunday"
            vals["monday"] = "Monday"
            vals["tuesday"] = "Tuesday"
            vals["wednesday"] = "Wednesday"
            vals["thursday"] = "Thursday"
            vals["friday"] = "Friday"
            vals["saturday"] = "Saturday"
            vals["holiday"] = "Holiday"
            vals["summerdesignday"] = "SummerDesignDay"
            vals["winterdesignday"] = "WinterDesignDay"
            vals["customday1"] = "CustomDay1"
            vals["customday2"] = "CustomDay2"
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
                                     'field `ScheduleWeekCompact.daytype_list_1`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ScheduleWeekCompact.daytype_list_1`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        return value

    def _check_scheduleday_name_1(self, value):
        """ Validates falue of field `Schedule:Day Name 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ScheduleWeekCompact.scheduleday_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleWeekCompact.scheduleday_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleWeekCompact.scheduleday_name_1`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ScheduleWeekCompact:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ScheduleWeekCompact:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ScheduleWeekCompact: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ScheduleWeekCompact: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ScheduleYear(object):
    """ Corresponds to IDD object `Schedule:Year`
        A Schedule:Year contains from 1 to 52 week schedules
    """
    internal_name = "Schedule:Year"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 5
    format = None
    min_fields = 7
    extensible_keys = ["Schedule:Week", "Start Month", "Start Day", "End Month", "End Day"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Year`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["extensibles"] = []
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
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `ScheduleYear.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleYear.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleYear.name`')
        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`
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
                                 ' for field `ScheduleYear.schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleYear.schedule_type_limits_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleYear.schedule_type_limits_name`')
        self._data["Schedule Type Limits Name"] = value

    def add_extensible(self,
                       scheduleweek=None,
                       start_month=None,
                       start_day=None,
                       end_month=None,
                       end_day=None,
                       ):
        """ Add values for extensible fields

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
        vals.append(self._check_scheduleweek(scheduleweek))
        vals.append(self._check_start_month(start_month))
        vals.append(self._check_start_day(start_day))
        vals.append(self._check_end_month(end_month))
        vals.append(self._check_end_day(end_day))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_scheduleweek(self, value):
        """ Validates falue of field `Schedule:Week`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ScheduleYear.scheduleweek`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleYear.scheduleweek`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleYear.scheduleweek`')
        return value

    def _check_start_month(self, value):
        """ Validates falue of field `Start Month`
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ScheduleYear.start_month`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ScheduleYear.start_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ScheduleYear.start_month`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `ScheduleYear.start_month`')
        return value

    def _check_start_day(self, value):
        """ Validates falue of field `Start Day`
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ScheduleYear.start_day`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ScheduleYear.start_day`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ScheduleYear.start_day`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `ScheduleYear.start_day`')
        return value

    def _check_end_month(self, value):
        """ Validates falue of field `End Month`
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ScheduleYear.end_month`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ScheduleYear.end_month`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ScheduleYear.end_month`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `ScheduleYear.end_month`')
        return value

    def _check_end_day(self, value):
        """ Validates falue of field `End Day`
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ScheduleYear.end_day`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ScheduleYear.end_day`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ScheduleYear.end_day`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `ScheduleYear.end_day`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ScheduleYear:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ScheduleYear:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ScheduleYear: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ScheduleYear: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ScheduleCompact(object):
    """ Corresponds to IDD object `Schedule:Compact`
        Irregular object.  Does not follow the usual definition for fields.  Fields A3... are:
        Through: Date
        For: Applicable days (ref: Schedule:Week:Compact)
        Interpolate: Yes/No (ref: Schedule:Day:Interval) -- optional, if not used will be "No"
        Until: <Time> (ref: Schedule:Day:Interval)
        <numeric value>
        words "Through","For","Interpolate","Until" must be included.
    """
    internal_name = "Schedule:Compact"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 1
    format = "compactschedule"
    min_fields = 5
    extensible_keys = ["Field"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Compact`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["extensibles"] = []
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
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `ScheduleCompact.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleCompact.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleCompact.name`')
        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`
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
                                 ' for field `ScheduleCompact.schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleCompact.schedule_type_limits_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleCompact.schedule_type_limits_name`')
        self._data["Schedule Type Limits Name"] = value

    def add_extensible(self,
                       field=None,
                       ):
        """ Add values for extensible fields

        Args:

            field (str): value for IDD Field `Field`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_field(field))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_field(self, value):
        """ Validates falue of field `Field`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ScheduleCompact.field`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleCompact.field`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleCompact.field`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ScheduleCompact:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ScheduleCompact:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ScheduleCompact: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ScheduleCompact: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ScheduleConstant(object):
    """ Corresponds to IDD object `Schedule:Constant`
        Constant hourly value for entire year.
    """
    internal_name = "Schedule:Constant"
    field_count = 3
    required_fields = ["Name"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:Constant`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["Hourly Value"] = None
        self._data["extensibles"] = []
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
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hourly_value = None
        else:
            self.hourly_value = vals[i]
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
                                 ' for field `ScheduleConstant.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleConstant.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleConstant.name`')
        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`
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
                                 ' for field `ScheduleConstant.schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleConstant.schedule_type_limits_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleConstant.schedule_type_limits_name`')
        self._data["Schedule Type Limits Name"] = value

    @property
    def hourly_value(self):
        """Get hourly_value

        Returns:
            float: the value of `hourly_value` or None if not set
        """
        return self._data["Hourly Value"]

    @hourly_value.setter
    def hourly_value(self, value=0.0):
        """  Corresponds to IDD Field `Hourly Value`

        Args:
            value (float): value for IDD Field `Hourly Value`
                Default value: 0.0
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
                                 ' for field `ScheduleConstant.hourly_value`'.format(value))
        self._data["Hourly Value"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ScheduleConstant:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ScheduleConstant:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ScheduleConstant: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ScheduleConstant: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ScheduleFile(object):
    """ Corresponds to IDD object `Schedule:File`
        A Schedule:File points to a text computer file that has 8760-8784 hours of data.
    """
    internal_name = "Schedule:File"
    field_count = 9
    required_fields = ["Name", "File Name", "Column Number", "Rows to Skip at Top"]
    extensible_fields = 0
    format = None
    min_fields = 5
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Schedule:File`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Type Limits Name"] = None
        self._data["File Name"] = None
        self._data["Column Number"] = None
        self._data["Rows to Skip at Top"] = None
        self._data["Number of Hours of Data"] = None
        self._data["Column Separator"] = None
        self._data["Interpolate to Timestep"] = None
        self._data["Minutes per Item"] = None
        self._data["extensibles"] = []
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
            self.schedule_type_limits_name = None
        else:
            self.schedule_type_limits_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.file_name = None
        else:
            self.file_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.column_number = None
        else:
            self.column_number = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rows_to_skip_at_top = None
        else:
            self.rows_to_skip_at_top = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_hours_of_data = None
        else:
            self.number_of_hours_of_data = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.column_separator = None
        else:
            self.column_separator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.interpolate_to_timestep = None
        else:
            self.interpolate_to_timestep = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minutes_per_item = None
        else:
            self.minutes_per_item = vals[i]
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
                                 ' for field `ScheduleFile.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleFile.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleFile.name`')
        self._data["Name"] = value

    @property
    def schedule_type_limits_name(self):
        """Get schedule_type_limits_name

        Returns:
            str: the value of `schedule_type_limits_name` or None if not set
        """
        return self._data["Schedule Type Limits Name"]

    @schedule_type_limits_name.setter
    def schedule_type_limits_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Type Limits Name`

        Args:
            value (str): value for IDD Field `Schedule Type Limits Name`
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
                                 ' for field `ScheduleFile.schedule_type_limits_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleFile.schedule_type_limits_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleFile.schedule_type_limits_name`')
        self._data["Schedule Type Limits Name"] = value

    @property
    def file_name(self):
        """Get file_name

        Returns:
            str: the value of `file_name` or None if not set
        """
        return self._data["File Name"]

    @file_name.setter
    def file_name(self, value=None):
        """  Corresponds to IDD Field `File Name`

        Args:
            value (str): value for IDD Field `File Name`
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
                                 ' for field `ScheduleFile.file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleFile.file_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleFile.file_name`')
        self._data["File Name"] = value

    @property
    def column_number(self):
        """Get column_number

        Returns:
            int: the value of `column_number` or None if not set
        """
        return self._data["Column Number"]

    @column_number.setter
    def column_number(self, value=None):
        """  Corresponds to IDD Field `Column Number`

        Args:
            value (int): value for IDD Field `Column Number`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ScheduleFile.column_number`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ScheduleFile.column_number`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ScheduleFile.column_number`')
        self._data["Column Number"] = value

    @property
    def rows_to_skip_at_top(self):
        """Get rows_to_skip_at_top

        Returns:
            int: the value of `rows_to_skip_at_top` or None if not set
        """
        return self._data["Rows to Skip at Top"]

    @rows_to_skip_at_top.setter
    def rows_to_skip_at_top(self, value=None):
        """  Corresponds to IDD Field `Rows to Skip at Top`

        Args:
            value (int): value for IDD Field `Rows to Skip at Top`
                value >= 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ScheduleFile.rows_to_skip_at_top`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ScheduleFile.rows_to_skip_at_top`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `ScheduleFile.rows_to_skip_at_top`')
        self._data["Rows to Skip at Top"] = value

    @property
    def number_of_hours_of_data(self):
        """Get number_of_hours_of_data

        Returns:
            float: the value of `number_of_hours_of_data` or None if not set
        """
        return self._data["Number of Hours of Data"]

    @number_of_hours_of_data.setter
    def number_of_hours_of_data(self, value=8760.0):
        """  Corresponds to IDD Field `Number of Hours of Data`
        8760 hours does not account for leap years, 8784 does.
        should be either 8760 or 8784

        Args:
            value (float): value for IDD Field `Number of Hours of Data`
                Default value: 8760.0
                value >= 8760.0
                value <= 8784.0
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
                                 ' for field `ScheduleFile.number_of_hours_of_data`'.format(value))
            if value < 8760.0:
                raise ValueError('value need to be greater or equal 8760.0 '
                                 'for field `ScheduleFile.number_of_hours_of_data`')
            if value > 8784.0:
                raise ValueError('value need to be smaller 8784.0 '
                                 'for field `ScheduleFile.number_of_hours_of_data`')
        self._data["Number of Hours of Data"] = value

    @property
    def column_separator(self):
        """Get column_separator

        Returns:
            str: the value of `column_separator` or None if not set
        """
        return self._data["Column Separator"]

    @column_separator.setter
    def column_separator(self, value="Comma"):
        """  Corresponds to IDD Field `Column Separator`

        Args:
            value (str): value for IDD Field `Column Separator`
                Accepted values are:
                      - Comma
                      - Tab
                      - Fixed
                      - Semicolon
                Default value: Comma
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
                                 ' for field `ScheduleFile.column_separator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleFile.column_separator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleFile.column_separator`')
            vals = {}
            vals["comma"] = "Comma"
            vals["tab"] = "Tab"
            vals["fixed"] = "Fixed"
            vals["semicolon"] = "Semicolon"
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
                                     'field `ScheduleFile.column_separator`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ScheduleFile.column_separator`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Column Separator"] = value

    @property
    def interpolate_to_timestep(self):
        """Get interpolate_to_timestep

        Returns:
            str: the value of `interpolate_to_timestep` or None if not set
        """
        return self._data["Interpolate to Timestep"]

    @interpolate_to_timestep.setter
    def interpolate_to_timestep(self, value="No"):
        """  Corresponds to IDD Field `Interpolate to Timestep`
        when the interval does not match the user specified timestep a "Yes" choice will average between the intervals request (to
        timestep resolution.  a "No" choice will use the interval value at the simulation timestep without regard to if it matches
        the boundary or not.

        Args:
            value (str): value for IDD Field `Interpolate to Timestep`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `ScheduleFile.interpolate_to_timestep`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ScheduleFile.interpolate_to_timestep`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ScheduleFile.interpolate_to_timestep`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `ScheduleFile.interpolate_to_timestep`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ScheduleFile.interpolate_to_timestep`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Interpolate to Timestep"] = value

    @property
    def minutes_per_item(self):
        """Get minutes_per_item

        Returns:
            int: the value of `minutes_per_item` or None if not set
        """
        return self._data["Minutes per Item"]

    @minutes_per_item.setter
    def minutes_per_item(self, value=None):
        """  Corresponds to IDD Field `Minutes per Item`
        Must be evenly divisible into 60

        Args:
            value (int): value for IDD Field `Minutes per Item`
                value >= 1
                value <= 60
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ScheduleFile.minutes_per_item`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ScheduleFile.minutes_per_item`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ScheduleFile.minutes_per_item`')
            if value > 60:
                raise ValueError('value need to be smaller 60 '
                                 'for field `ScheduleFile.minutes_per_item`')
        self._data["Minutes per Item"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ScheduleFile:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ScheduleFile:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ScheduleFile: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ScheduleFile: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])