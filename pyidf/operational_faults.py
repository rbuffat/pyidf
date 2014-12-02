from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class FaultModelTemperatureSensorOffsetOutdoorAir(object):
    """ Corresponds to IDD object `FaultModel:TemperatureSensorOffset:OutdoorAir`
        This object describes outdoor air temperature sensor offset
    """
    internal_name = "FaultModel:TemperatureSensorOffset:OutdoorAir"
    field_count = 6
    required_fields = ["Controller Object Type", "Controller Object Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `FaultModel:TemperatureSensorOffset:OutdoorAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Severity Schedule Name"] = None
        self._data["Controller Object Type"] = None
        self._data["Controller Object Name"] = None
        self._data["Temperature Sensor Offset"] = None
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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.severity_schedule_name = None
        else:
            self.severity_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_type = None
        else:
            self.controller_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_name = None
        else:
            self.controller_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_sensor_offset = None
        else:
            self.temperature_sensor_offset = vals[i]
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
                                 ' for field `FaultModelTemperatureSensorOffsetOutdoorAir.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.name`')
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
                                 ' for field `FaultModelTemperatureSensorOffsetOutdoorAir.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """Get severity_schedule_name

        Returns:
            str: the value of `severity_schedule_name` or None if not set
        """
        return self._data["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`
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
                                 ' for field `FaultModelTemperatureSensorOffsetOutdoorAir.severity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.severity_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.severity_schedule_name`')
        self._data["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """Get controller_object_type

        Returns:
            str: the value of `controller_object_type` or None if not set
        """
        return self._data["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`
                Accepted values are:
                      - Controller:OutdoorAir
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
                                 ' for field `FaultModelTemperatureSensorOffsetOutdoorAir.controller_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.controller_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.controller_object_type`')
            vals = {}
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
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
                                     'field `FaultModelTemperatureSensorOffsetOutdoorAir.controller_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FaultModelTemperatureSensorOffsetOutdoorAir.controller_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """Get controller_object_name

        Returns:
            str: the value of `controller_object_name` or None if not set
        """
        return self._data["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """  Corresponds to IDD Field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`
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
                                 ' for field `FaultModelTemperatureSensorOffsetOutdoorAir.controller_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.controller_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.controller_object_name`')
        self._data["Controller Object Name"] = value

    @property
    def temperature_sensor_offset(self):
        """Get temperature_sensor_offset

        Returns:
            float: the value of `temperature_sensor_offset` or None if not set
        """
        return self._data["Temperature Sensor Offset"]

    @temperature_sensor_offset.setter
    def temperature_sensor_offset(self, value=0.0):
        """  Corresponds to IDD Field `Temperature Sensor Offset`

        Args:
            value (float): value for IDD Field `Temperature Sensor Offset`
                Units: deltaC
                Default value: 0.0
                value > -10.0
                value < 10.0
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
                                 ' for field `FaultModelTemperatureSensorOffsetOutdoorAir.temperature_sensor_offset`'.format(value))
            if value <= -10.0:
                raise ValueError('value need to be greater -10.0 '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.temperature_sensor_offset`')
            if value >= 10.0:
                raise ValueError('value need to be smaller 10.0 '
                                 'for field `FaultModelTemperatureSensorOffsetOutdoorAir.temperature_sensor_offset`')
        self._data["Temperature Sensor Offset"] = value

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
                    raise ValueError("Required field FaultModelTemperatureSensorOffsetOutdoorAir:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FaultModelTemperatureSensorOffsetOutdoorAir:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FaultModelTemperatureSensorOffsetOutdoorAir: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FaultModelTemperatureSensorOffsetOutdoorAir: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class FaultModelHumiditySensorOffsetOutdoorAir(object):
    """ Corresponds to IDD object `FaultModel:HumiditySensorOffset:OutdoorAir`
        This object describes outdoor air humidity sensor offset
    """
    internal_name = "FaultModel:HumiditySensorOffset:OutdoorAir"
    field_count = 6
    required_fields = ["Name", "Controller Object Type", "Controller Object Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `FaultModel:HumiditySensorOffset:OutdoorAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Severity Schedule Name"] = None
        self._data["Controller Object Type"] = None
        self._data["Controller Object Name"] = None
        self._data["Humidity Sensor Offset"] = None
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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.severity_schedule_name = None
        else:
            self.severity_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_type = None
        else:
            self.controller_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_name = None
        else:
            self.controller_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_sensor_offset = None
        else:
            self.humidity_sensor_offset = vals[i]
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
                                 ' for field `FaultModelHumiditySensorOffsetOutdoorAir.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.name`')
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
                                 ' for field `FaultModelHumiditySensorOffsetOutdoorAir.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """Get severity_schedule_name

        Returns:
            str: the value of `severity_schedule_name` or None if not set
        """
        return self._data["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`
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
                                 ' for field `FaultModelHumiditySensorOffsetOutdoorAir.severity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.severity_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.severity_schedule_name`')
        self._data["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """Get controller_object_type

        Returns:
            str: the value of `controller_object_type` or None if not set
        """
        return self._data["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`
                Accepted values are:
                      - Controller:OutdoorAir
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
                                 ' for field `FaultModelHumiditySensorOffsetOutdoorAir.controller_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.controller_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.controller_object_type`')
            vals = {}
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
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
                                     'field `FaultModelHumiditySensorOffsetOutdoorAir.controller_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FaultModelHumiditySensorOffsetOutdoorAir.controller_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """Get controller_object_name

        Returns:
            str: the value of `controller_object_name` or None if not set
        """
        return self._data["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """  Corresponds to IDD Field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`
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
                                 ' for field `FaultModelHumiditySensorOffsetOutdoorAir.controller_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.controller_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.controller_object_name`')
        self._data["Controller Object Name"] = value

    @property
    def humidity_sensor_offset(self):
        """Get humidity_sensor_offset

        Returns:
            float: the value of `humidity_sensor_offset` or None if not set
        """
        return self._data["Humidity Sensor Offset"]

    @humidity_sensor_offset.setter
    def humidity_sensor_offset(self, value=0.0):
        """  Corresponds to IDD Field `Humidity Sensor Offset`

        Args:
            value (float): value for IDD Field `Humidity Sensor Offset`
                Units: kgWater/kgDryAir
                Default value: 0.0
                value > -0.02
                value < 0.02
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
                                 ' for field `FaultModelHumiditySensorOffsetOutdoorAir.humidity_sensor_offset`'.format(value))
            if value <= -0.02:
                raise ValueError('value need to be greater -0.02 '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.humidity_sensor_offset`')
            if value >= 0.02:
                raise ValueError('value need to be smaller 0.02 '
                                 'for field `FaultModelHumiditySensorOffsetOutdoorAir.humidity_sensor_offset`')
        self._data["Humidity Sensor Offset"] = value

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
                    raise ValueError("Required field FaultModelHumiditySensorOffsetOutdoorAir:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FaultModelHumiditySensorOffsetOutdoorAir:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FaultModelHumiditySensorOffsetOutdoorAir: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FaultModelHumiditySensorOffsetOutdoorAir: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class FaultModelEnthalpySensorOffsetOutdoorAir(object):
    """ Corresponds to IDD object `FaultModel:EnthalpySensorOffset:OutdoorAir`
        This object describes outdoor air enthalpy sensor offset
    """
    internal_name = "FaultModel:EnthalpySensorOffset:OutdoorAir"
    field_count = 6
    required_fields = ["Name", "Controller Object Type", "Controller Object Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `FaultModel:EnthalpySensorOffset:OutdoorAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Severity Schedule Name"] = None
        self._data["Controller Object Type"] = None
        self._data["Controller Object Name"] = None
        self._data["Enthalpy Sensor Offset"] = None
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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.severity_schedule_name = None
        else:
            self.severity_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_type = None
        else:
            self.controller_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_name = None
        else:
            self.controller_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enthalpy_sensor_offset = None
        else:
            self.enthalpy_sensor_offset = vals[i]
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
                                 ' for field `FaultModelEnthalpySensorOffsetOutdoorAir.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.name`')
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
                                 ' for field `FaultModelEnthalpySensorOffsetOutdoorAir.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """Get severity_schedule_name

        Returns:
            str: the value of `severity_schedule_name` or None if not set
        """
        return self._data["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`
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
                                 ' for field `FaultModelEnthalpySensorOffsetOutdoorAir.severity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.severity_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.severity_schedule_name`')
        self._data["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """Get controller_object_type

        Returns:
            str: the value of `controller_object_type` or None if not set
        """
        return self._data["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`
                Accepted values are:
                      - Controller:OutdoorAir
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
                                 ' for field `FaultModelEnthalpySensorOffsetOutdoorAir.controller_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.controller_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.controller_object_type`')
            vals = {}
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
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
                                     'field `FaultModelEnthalpySensorOffsetOutdoorAir.controller_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FaultModelEnthalpySensorOffsetOutdoorAir.controller_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """Get controller_object_name

        Returns:
            str: the value of `controller_object_name` or None if not set
        """
        return self._data["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """  Corresponds to IDD Field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`
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
                                 ' for field `FaultModelEnthalpySensorOffsetOutdoorAir.controller_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.controller_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.controller_object_name`')
        self._data["Controller Object Name"] = value

    @property
    def enthalpy_sensor_offset(self):
        """Get enthalpy_sensor_offset

        Returns:
            float: the value of `enthalpy_sensor_offset` or None if not set
        """
        return self._data["Enthalpy Sensor Offset"]

    @enthalpy_sensor_offset.setter
    def enthalpy_sensor_offset(self, value=0.0):
        """  Corresponds to IDD Field `Enthalpy Sensor Offset`

        Args:
            value (float): value for IDD Field `Enthalpy Sensor Offset`
                Units: J/kg
                Default value: 0.0
                value > -20000.0
                value < 20000.0
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
                                 ' for field `FaultModelEnthalpySensorOffsetOutdoorAir.enthalpy_sensor_offset`'.format(value))
            if value <= -20000.0:
                raise ValueError('value need to be greater -20000.0 '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.enthalpy_sensor_offset`')
            if value >= 20000.0:
                raise ValueError('value need to be smaller 20000.0 '
                                 'for field `FaultModelEnthalpySensorOffsetOutdoorAir.enthalpy_sensor_offset`')
        self._data["Enthalpy Sensor Offset"] = value

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
                    raise ValueError("Required field FaultModelEnthalpySensorOffsetOutdoorAir:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FaultModelEnthalpySensorOffsetOutdoorAir:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FaultModelEnthalpySensorOffsetOutdoorAir: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FaultModelEnthalpySensorOffsetOutdoorAir: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class FaultModelPressureSensorOffsetOutdoorAir(object):
    """ Corresponds to IDD object `FaultModel:PressureSensorOffset:OutdoorAir`
        This object describes outdoor air pressure sensor offset
    """
    internal_name = "FaultModel:PressureSensorOffset:OutdoorAir"
    field_count = 6
    required_fields = ["Name", "Controller Object Type", "Controller Object Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `FaultModel:PressureSensorOffset:OutdoorAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Severity Schedule Name"] = None
        self._data["Controller Object Type"] = None
        self._data["Controller Object Name"] = None
        self._data["Pressure Sensor Offset"] = None
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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.severity_schedule_name = None
        else:
            self.severity_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_type = None
        else:
            self.controller_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_name = None
        else:
            self.controller_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pressure_sensor_offset = None
        else:
            self.pressure_sensor_offset = vals[i]
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
                                 ' for field `FaultModelPressureSensorOffsetOutdoorAir.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.name`')
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
                                 ' for field `FaultModelPressureSensorOffsetOutdoorAir.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """Get severity_schedule_name

        Returns:
            str: the value of `severity_schedule_name` or None if not set
        """
        return self._data["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`
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
                                 ' for field `FaultModelPressureSensorOffsetOutdoorAir.severity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.severity_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.severity_schedule_name`')
        self._data["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """Get controller_object_type

        Returns:
            str: the value of `controller_object_type` or None if not set
        """
        return self._data["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`
                Accepted values are:
                      - Controller:OutdoorAir
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
                                 ' for field `FaultModelPressureSensorOffsetOutdoorAir.controller_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.controller_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.controller_object_type`')
            vals = {}
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
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
                                     'field `FaultModelPressureSensorOffsetOutdoorAir.controller_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FaultModelPressureSensorOffsetOutdoorAir.controller_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """Get controller_object_name

        Returns:
            str: the value of `controller_object_name` or None if not set
        """
        return self._data["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """  Corresponds to IDD Field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`
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
                                 ' for field `FaultModelPressureSensorOffsetOutdoorAir.controller_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.controller_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.controller_object_name`')
        self._data["Controller Object Name"] = value

    @property
    def pressure_sensor_offset(self):
        """Get pressure_sensor_offset

        Returns:
            float: the value of `pressure_sensor_offset` or None if not set
        """
        return self._data["Pressure Sensor Offset"]

    @pressure_sensor_offset.setter
    def pressure_sensor_offset(self, value=0.0):
        """  Corresponds to IDD Field `Pressure Sensor Offset`

        Args:
            value (float): value for IDD Field `Pressure Sensor Offset`
                Units: Pa
                Default value: 0.0
                value > -10000.0
                value < 10000.0
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
                                 ' for field `FaultModelPressureSensorOffsetOutdoorAir.pressure_sensor_offset`'.format(value))
            if value <= -10000.0:
                raise ValueError('value need to be greater -10000.0 '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.pressure_sensor_offset`')
            if value >= 10000.0:
                raise ValueError('value need to be smaller 10000.0 '
                                 'for field `FaultModelPressureSensorOffsetOutdoorAir.pressure_sensor_offset`')
        self._data["Pressure Sensor Offset"] = value

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
                    raise ValueError("Required field FaultModelPressureSensorOffsetOutdoorAir:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FaultModelPressureSensorOffsetOutdoorAir:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FaultModelPressureSensorOffsetOutdoorAir: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FaultModelPressureSensorOffsetOutdoorAir: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class FaultModelTemperatureSensorOffsetReturnAir(object):
    """ Corresponds to IDD object `FaultModel:TemperatureSensorOffset:ReturnAir`
        This object describes return air temperature sensor offset
    """
    internal_name = "FaultModel:TemperatureSensorOffset:ReturnAir"
    field_count = 6
    required_fields = ["Name", "Controller Object Type", "Controller Object Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `FaultModel:TemperatureSensorOffset:ReturnAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Severity Schedule Name"] = None
        self._data["Controller Object Type"] = None
        self._data["Controller Object Name"] = None
        self._data["Temperature Sensor Offset"] = None
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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.severity_schedule_name = None
        else:
            self.severity_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_type = None
        else:
            self.controller_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_name = None
        else:
            self.controller_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_sensor_offset = None
        else:
            self.temperature_sensor_offset = vals[i]
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
                                 ' for field `FaultModelTemperatureSensorOffsetReturnAir.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.name`')
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
                                 ' for field `FaultModelTemperatureSensorOffsetReturnAir.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """Get severity_schedule_name

        Returns:
            str: the value of `severity_schedule_name` or None if not set
        """
        return self._data["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`
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
                                 ' for field `FaultModelTemperatureSensorOffsetReturnAir.severity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.severity_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.severity_schedule_name`')
        self._data["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """Get controller_object_type

        Returns:
            str: the value of `controller_object_type` or None if not set
        """
        return self._data["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`
                Accepted values are:
                      - Controller:OutdoorAir
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
                                 ' for field `FaultModelTemperatureSensorOffsetReturnAir.controller_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.controller_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.controller_object_type`')
            vals = {}
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
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
                                     'field `FaultModelTemperatureSensorOffsetReturnAir.controller_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FaultModelTemperatureSensorOffsetReturnAir.controller_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """Get controller_object_name

        Returns:
            str: the value of `controller_object_name` or None if not set
        """
        return self._data["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """  Corresponds to IDD Field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`
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
                                 ' for field `FaultModelTemperatureSensorOffsetReturnAir.controller_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.controller_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.controller_object_name`')
        self._data["Controller Object Name"] = value

    @property
    def temperature_sensor_offset(self):
        """Get temperature_sensor_offset

        Returns:
            float: the value of `temperature_sensor_offset` or None if not set
        """
        return self._data["Temperature Sensor Offset"]

    @temperature_sensor_offset.setter
    def temperature_sensor_offset(self, value=0.0):
        """  Corresponds to IDD Field `Temperature Sensor Offset`

        Args:
            value (float): value for IDD Field `Temperature Sensor Offset`
                Units: deltaC
                Default value: 0.0
                value > -10.0
                value < 10.0
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
                                 ' for field `FaultModelTemperatureSensorOffsetReturnAir.temperature_sensor_offset`'.format(value))
            if value <= -10.0:
                raise ValueError('value need to be greater -10.0 '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.temperature_sensor_offset`')
            if value >= 10.0:
                raise ValueError('value need to be smaller 10.0 '
                                 'for field `FaultModelTemperatureSensorOffsetReturnAir.temperature_sensor_offset`')
        self._data["Temperature Sensor Offset"] = value

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
                    raise ValueError("Required field FaultModelTemperatureSensorOffsetReturnAir:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FaultModelTemperatureSensorOffsetReturnAir:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FaultModelTemperatureSensorOffsetReturnAir: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FaultModelTemperatureSensorOffsetReturnAir: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class FaultModelEnthalpySensorOffsetReturnAir(object):
    """ Corresponds to IDD object `FaultModel:EnthalpySensorOffset:ReturnAir`
        This object describes return air enthalpy sensor offset
    """
    internal_name = "FaultModel:EnthalpySensorOffset:ReturnAir"
    field_count = 6
    required_fields = ["Name", "Controller Object Type", "Controller Object Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `FaultModel:EnthalpySensorOffset:ReturnAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Severity Schedule Name"] = None
        self._data["Controller Object Type"] = None
        self._data["Controller Object Name"] = None
        self._data["Enthalpy Sensor Offset"] = None
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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.severity_schedule_name = None
        else:
            self.severity_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_type = None
        else:
            self.controller_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_object_name = None
        else:
            self.controller_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enthalpy_sensor_offset = None
        else:
            self.enthalpy_sensor_offset = vals[i]
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
                                 ' for field `FaultModelEnthalpySensorOffsetReturnAir.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.name`')
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
                                 ' for field `FaultModelEnthalpySensorOffsetReturnAir.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """Get severity_schedule_name

        Returns:
            str: the value of `severity_schedule_name` or None if not set
        """
        return self._data["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`
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
                                 ' for field `FaultModelEnthalpySensorOffsetReturnAir.severity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.severity_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.severity_schedule_name`')
        self._data["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """Get controller_object_type

        Returns:
            str: the value of `controller_object_type` or None if not set
        """
        return self._data["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`
                Accepted values are:
                      - Controller:OutdoorAir
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
                                 ' for field `FaultModelEnthalpySensorOffsetReturnAir.controller_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.controller_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.controller_object_type`')
            vals = {}
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
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
                                     'field `FaultModelEnthalpySensorOffsetReturnAir.controller_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FaultModelEnthalpySensorOffsetReturnAir.controller_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """Get controller_object_name

        Returns:
            str: the value of `controller_object_name` or None if not set
        """
        return self._data["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """  Corresponds to IDD Field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`
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
                                 ' for field `FaultModelEnthalpySensorOffsetReturnAir.controller_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.controller_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.controller_object_name`')
        self._data["Controller Object Name"] = value

    @property
    def enthalpy_sensor_offset(self):
        """Get enthalpy_sensor_offset

        Returns:
            float: the value of `enthalpy_sensor_offset` or None if not set
        """
        return self._data["Enthalpy Sensor Offset"]

    @enthalpy_sensor_offset.setter
    def enthalpy_sensor_offset(self, value=0.0):
        """  Corresponds to IDD Field `Enthalpy Sensor Offset`

        Args:
            value (float): value for IDD Field `Enthalpy Sensor Offset`
                Units: J/kg
                Default value: 0.0
                value > -20000.0
                value < 20000.0
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
                                 ' for field `FaultModelEnthalpySensorOffsetReturnAir.enthalpy_sensor_offset`'.format(value))
            if value <= -20000.0:
                raise ValueError('value need to be greater -20000.0 '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.enthalpy_sensor_offset`')
            if value >= 20000.0:
                raise ValueError('value need to be smaller 20000.0 '
                                 'for field `FaultModelEnthalpySensorOffsetReturnAir.enthalpy_sensor_offset`')
        self._data["Enthalpy Sensor Offset"] = value

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
                    raise ValueError("Required field FaultModelEnthalpySensorOffsetReturnAir:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FaultModelEnthalpySensorOffsetReturnAir:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FaultModelEnthalpySensorOffsetReturnAir: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FaultModelEnthalpySensorOffsetReturnAir: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class FaultModelFoulingCoil(object):
    """ Corresponds to IDD object `FaultModel:Fouling:Coil`
        This object describes fouling water heating or cooling coils
    """
    internal_name = "FaultModel:Fouling:Coil"
    field_count = 10
    required_fields = ["Name", "Coil Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `FaultModel:Fouling:Coil`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coil Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Severity Schedule Name"] = None
        self._data["Fouling Input Method"] = None
        self._data["UAFouled"] = None
        self._data["Water Side Fouling Factor"] = None
        self._data["Air Side Fouling Factor"] = None
        self._data["Outside Coil Surface Area"] = None
        self._data["Inside to Outside Coil Surface Area Ratio"] = None
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
            self.coil_name = None
        else:
            self.coil_name = vals[i]
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
            self.severity_schedule_name = None
        else:
            self.severity_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fouling_input_method = None
        else:
            self.fouling_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.uafouled = None
        else:
            self.uafouled = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_side_fouling_factor = None
        else:
            self.water_side_fouling_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_side_fouling_factor = None
        else:
            self.air_side_fouling_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_coil_surface_area = None
        else:
            self.outside_coil_surface_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inside_to_outside_coil_surface_area_ratio = None
        else:
            self.inside_to_outside_coil_surface_area_ratio = vals[i]
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
                                 ' for field `FaultModelFoulingCoil.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelFoulingCoil.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelFoulingCoil.name`')
        self._data["Name"] = value

    @property
    def coil_name(self):
        """Get coil_name

        Returns:
            str: the value of `coil_name` or None if not set
        """
        return self._data["Coil Name"]

    @coil_name.setter
    def coil_name(self, value=None):
        """  Corresponds to IDD Field `Coil Name`

        Args:
            value (str): value for IDD Field `Coil Name`
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
                                 ' for field `FaultModelFoulingCoil.coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelFoulingCoil.coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelFoulingCoil.coil_name`')
        self._data["Coil Name"] = value

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
                                 ' for field `FaultModelFoulingCoil.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelFoulingCoil.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelFoulingCoil.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """Get severity_schedule_name

        Returns:
            str: the value of `severity_schedule_name` or None if not set
        """
        return self._data["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`
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
                                 ' for field `FaultModelFoulingCoil.severity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelFoulingCoil.severity_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelFoulingCoil.severity_schedule_name`')
        self._data["Severity Schedule Name"] = value

    @property
    def fouling_input_method(self):
        """Get fouling_input_method

        Returns:
            str: the value of `fouling_input_method` or None if not set
        """
        return self._data["Fouling Input Method"]

    @fouling_input_method.setter
    def fouling_input_method(self, value="FouledUARated"):
        """  Corresponds to IDD Field `Fouling Input Method`

        Args:
            value (str): value for IDD Field `Fouling Input Method`
                Accepted values are:
                      - FouledUARated
                      - FoulingFactor
                Default value: FouledUARated
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
                                 ' for field `FaultModelFoulingCoil.fouling_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FaultModelFoulingCoil.fouling_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FaultModelFoulingCoil.fouling_input_method`')
            vals = {}
            vals["fouleduarated"] = "FouledUARated"
            vals["foulingfactor"] = "FoulingFactor"
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
                                     'field `FaultModelFoulingCoil.fouling_input_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FaultModelFoulingCoil.fouling_input_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Fouling Input Method"] = value

    @property
    def uafouled(self):
        """Get uafouled

        Returns:
            float: the value of `uafouled` or None if not set
        """
        return self._data["UAFouled"]

    @uafouled.setter
    def uafouled(self, value=None):
        """  Corresponds to IDD Field `UAFouled`
        Fouling coil UA value under rating conditions
        For Fouling Input Method: FouledUARated

        Args:
            value (float): value for IDD Field `UAFouled`
                Units: W/K
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
                                 ' for field `FaultModelFoulingCoil.uafouled`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `FaultModelFoulingCoil.uafouled`')
        self._data["UAFouled"] = value

    @property
    def water_side_fouling_factor(self):
        """Get water_side_fouling_factor

        Returns:
            float: the value of `water_side_fouling_factor` or None if not set
        """
        return self._data["Water Side Fouling Factor"]

    @water_side_fouling_factor.setter
    def water_side_fouling_factor(self, value=0.0):
        """  Corresponds to IDD Field `Water Side Fouling Factor`
        For Fouling Input Method: FoulingFactor

        Args:
            value (float): value for IDD Field `Water Side Fouling Factor`
                Units: m2-K/W
                Default value: 0.0
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
                                 ' for field `FaultModelFoulingCoil.water_side_fouling_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `FaultModelFoulingCoil.water_side_fouling_factor`')
        self._data["Water Side Fouling Factor"] = value

    @property
    def air_side_fouling_factor(self):
        """Get air_side_fouling_factor

        Returns:
            float: the value of `air_side_fouling_factor` or None if not set
        """
        return self._data["Air Side Fouling Factor"]

    @air_side_fouling_factor.setter
    def air_side_fouling_factor(self, value=0.0):
        """  Corresponds to IDD Field `Air Side Fouling Factor`
        For Fouling Input Method: FoulingFactor

        Args:
            value (float): value for IDD Field `Air Side Fouling Factor`
                Units: m2-K/W
                Default value: 0.0
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
                                 ' for field `FaultModelFoulingCoil.air_side_fouling_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `FaultModelFoulingCoil.air_side_fouling_factor`')
        self._data["Air Side Fouling Factor"] = value

    @property
    def outside_coil_surface_area(self):
        """Get outside_coil_surface_area

        Returns:
            float: the value of `outside_coil_surface_area` or None if not set
        """
        return self._data["Outside Coil Surface Area"]

    @outside_coil_surface_area.setter
    def outside_coil_surface_area(self, value=None):
        """  Corresponds to IDD Field `Outside Coil Surface Area`
        For Fouling Input Method: FoulingFactor

        Args:
            value (float): value for IDD Field `Outside Coil Surface Area`
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
                                 ' for field `FaultModelFoulingCoil.outside_coil_surface_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `FaultModelFoulingCoil.outside_coil_surface_area`')
        self._data["Outside Coil Surface Area"] = value

    @property
    def inside_to_outside_coil_surface_area_ratio(self):
        """Get inside_to_outside_coil_surface_area_ratio

        Returns:
            float: the value of `inside_to_outside_coil_surface_area_ratio` or None if not set
        """
        return self._data["Inside to Outside Coil Surface Area Ratio"]

    @inside_to_outside_coil_surface_area_ratio.setter
    def inside_to_outside_coil_surface_area_ratio(self, value=0.07):
        """  Corresponds to IDD Field `Inside to Outside Coil Surface Area Ratio`
        For Fouling Input Method: FoulingFactor

        Args:
            value (float): value for IDD Field `Inside to Outside Coil Surface Area Ratio`
                Units: dimensionless
                Default value: 0.07
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
                                 ' for field `FaultModelFoulingCoil.inside_to_outside_coil_surface_area_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `FaultModelFoulingCoil.inside_to_outside_coil_surface_area_ratio`')
        self._data["Inside to Outside Coil Surface Area Ratio"] = value

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
                    raise ValueError("Required field FaultModelFoulingCoil:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FaultModelFoulingCoil:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FaultModelFoulingCoil: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FaultModelFoulingCoil: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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