from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class ZoneControlHumidistat(object):
    """ Corresponds to IDD object `ZoneControl:Humidistat`
        Specifies zone relative humidity setpoint schedules for humidifying and dehumidifying.
    """
    internal_name = "ZoneControl:Humidistat"
    field_count = 4
    required_fields = ["Name", "Zone Name", "Humidifying Relative Humidity Setpoint Schedule Name"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Humidistat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Humidifying Relative Humidity Setpoint Schedule Name"] = None
        self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"] = None
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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidifying_relative_humidity_setpoint_schedule_name = None
        else:
            self.humidifying_relative_humidity_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dehumidifying_relative_humidity_setpoint_schedule_name = None
        else:
            self.dehumidifying_relative_humidity_setpoint_schedule_name = vals[i]
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
                                 ' for field `ZoneControlHumidistat.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlHumidistat.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlHumidistat.name`')
        self._data["Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `ZoneControlHumidistat.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlHumidistat.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlHumidistat.zone_name`')
        self._data["Zone Name"] = value

    @property
    def humidifying_relative_humidity_setpoint_schedule_name(self):
        """Get humidifying_relative_humidity_setpoint_schedule_name

        Returns:
            str: the value of `humidifying_relative_humidity_setpoint_schedule_name` or None if not set
        """
        return self._data["Humidifying Relative Humidity Setpoint Schedule Name"]

    @humidifying_relative_humidity_setpoint_schedule_name.setter
    def humidifying_relative_humidity_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Humidifying Relative Humidity Setpoint Schedule Name`
        hourly schedule values should be in Relative Humidity (percent)

        Args:
            value (str): value for IDD Field `Humidifying Relative Humidity Setpoint Schedule Name`
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
                                 ' for field `ZoneControlHumidistat.humidifying_relative_humidity_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlHumidistat.humidifying_relative_humidity_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlHumidistat.humidifying_relative_humidity_setpoint_schedule_name`')
        self._data["Humidifying Relative Humidity Setpoint Schedule Name"] = value

    @property
    def dehumidifying_relative_humidity_setpoint_schedule_name(self):
        """Get dehumidifying_relative_humidity_setpoint_schedule_name

        Returns:
            str: the value of `dehumidifying_relative_humidity_setpoint_schedule_name` or None if not set
        """
        return self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"]

    @dehumidifying_relative_humidity_setpoint_schedule_name.setter
    def dehumidifying_relative_humidity_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Dehumidifying Relative Humidity Setpoint Schedule Name`
        hourly schedule values should be in Relative Humidity (percent)

        Args:
            value (str): value for IDD Field `Dehumidifying Relative Humidity Setpoint Schedule Name`
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
                                 ' for field `ZoneControlHumidistat.dehumidifying_relative_humidity_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlHumidistat.dehumidifying_relative_humidity_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlHumidistat.dehumidifying_relative_humidity_setpoint_schedule_name`')
        self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"] = value

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
                    raise ValueError("Required field ZoneControlHumidistat:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneControlHumidistat:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneControlHumidistat: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneControlHumidistat: {} / {}".format(out_fields,
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

class ZoneControlThermostat(object):
    """ Corresponds to IDD object `ZoneControl:Thermostat`
        Define the Thermostat settings for a zone or list of zones.
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    """
    internal_name = "ZoneControl:Thermostat"
    field_count = 11
    required_fields = ["Name", "Zone or ZoneList Name", "Control Type Schedule Name", "Control 1 Object Type", "Control 1 Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Thermostat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Control Type Schedule Name"] = None
        self._data["Control 1 Object Type"] = None
        self._data["Control 1 Name"] = None
        self._data["Control 2 Object Type"] = None
        self._data["Control 2 Name"] = None
        self._data["Control 3 Object Type"] = None
        self._data["Control 3 Name"] = None
        self._data["Control 4 Object Type"] = None
        self._data["Control 4 Name"] = None
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
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_type_schedule_name = None
        else:
            self.control_type_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_1_object_type = None
        else:
            self.control_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_1_name = None
        else:
            self.control_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_2_object_type = None
        else:
            self.control_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_2_name = None
        else:
            self.control_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_3_object_type = None
        else:
            self.control_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_3_name = None
        else:
            self.control_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_4_object_type = None
        else:
            self.control_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_4_name = None
        else:
            self.control_4_name = vals[i]
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
                                 ' for field `ZoneControlThermostat.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.name`')
        self._data["Name"] = value

    @property
    def zone_or_zonelist_name(self):
        """Get zone_or_zonelist_name

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set
        """
        return self._data["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """  Corresponds to IDD Field `Zone or ZoneList Name`

        Args:
            value (str): value for IDD Field `Zone or ZoneList Name`
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
                                 ' for field `ZoneControlThermostat.zone_or_zonelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.zone_or_zonelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.zone_or_zonelist_name`')
        self._data["Zone or ZoneList Name"] = value

    @property
    def control_type_schedule_name(self):
        """Get control_type_schedule_name

        Returns:
            str: the value of `control_type_schedule_name` or None if not set
        """
        return self._data["Control Type Schedule Name"]

    @control_type_schedule_name.setter
    def control_type_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Type Schedule Name`
        This schedule contains appropriate control types for thermostat.
        Control types are integers: 0 - Uncontrolled (floating, no thermostat), 1 = ThermostatSetpoint:SingleHeating,
        2 = ThermostatSetpoint:SingleCooling, 3 = ThermostatSetpoint:SingleHeatingOrCooling, 4 = ThermostatSetpoint:DualSetpoint

        Args:
            value (str): value for IDD Field `Control Type Schedule Name`
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
                                 ' for field `ZoneControlThermostat.control_type_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.control_type_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.control_type_schedule_name`')
        self._data["Control Type Schedule Name"] = value

    @property
    def control_1_object_type(self):
        """Get control_1_object_type

        Returns:
            str: the value of `control_1_object_type` or None if not set
        """
        return self._data["Control 1 Object Type"]

    @control_1_object_type.setter
    def control_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Control 1 Object Type`

        Args:
            value (str): value for IDD Field `Control 1 Object Type`
                Accepted values are:
                      - ThermostatSetpoint:SingleHeating
                      - ThermostatSetpoint:SingleCooling
                      - ThermostatSetpoint:SingleHeatingOrCooling
                      - ThermostatSetpoint:DualSetpoint
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
                                 ' for field `ZoneControlThermostat.control_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.control_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.control_1_object_type`')
            vals = {}
            vals["thermostatsetpoint:singleheating"] = "ThermostatSetpoint:SingleHeating"
            vals["thermostatsetpoint:singlecooling"] = "ThermostatSetpoint:SingleCooling"
            vals["thermostatsetpoint:singleheatingorcooling"] = "ThermostatSetpoint:SingleHeatingOrCooling"
            vals["thermostatsetpoint:dualsetpoint"] = "ThermostatSetpoint:DualSetpoint"
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
                                     'field `ZoneControlThermostat.control_1_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostat.control_1_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control 1 Object Type"] = value

    @property
    def control_1_name(self):
        """Get control_1_name

        Returns:
            str: the value of `control_1_name` or None if not set
        """
        return self._data["Control 1 Name"]

    @control_1_name.setter
    def control_1_name(self, value=None):
        """  Corresponds to IDD Field `Control 1 Name`
        Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Control 1 Name`
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
                                 ' for field `ZoneControlThermostat.control_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.control_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.control_1_name`')
        self._data["Control 1 Name"] = value

    @property
    def control_2_object_type(self):
        """Get control_2_object_type

        Returns:
            str: the value of `control_2_object_type` or None if not set
        """
        return self._data["Control 2 Object Type"]

    @control_2_object_type.setter
    def control_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Control 2 Object Type`

        Args:
            value (str): value for IDD Field `Control 2 Object Type`
                Accepted values are:
                      - ThermostatSetpoint:SingleHeating
                      - ThermostatSetpoint:SingleCooling
                      - ThermostatSetpoint:SingleHeatingOrCooling
                      - ThermostatSetpoint:DualSetpoint
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
                                 ' for field `ZoneControlThermostat.control_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.control_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.control_2_object_type`')
            vals = {}
            vals["thermostatsetpoint:singleheating"] = "ThermostatSetpoint:SingleHeating"
            vals["thermostatsetpoint:singlecooling"] = "ThermostatSetpoint:SingleCooling"
            vals["thermostatsetpoint:singleheatingorcooling"] = "ThermostatSetpoint:SingleHeatingOrCooling"
            vals["thermostatsetpoint:dualsetpoint"] = "ThermostatSetpoint:DualSetpoint"
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
                                     'field `ZoneControlThermostat.control_2_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostat.control_2_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control 2 Object Type"] = value

    @property
    def control_2_name(self):
        """Get control_2_name

        Returns:
            str: the value of `control_2_name` or None if not set
        """
        return self._data["Control 2 Name"]

    @control_2_name.setter
    def control_2_name(self, value=None):
        """  Corresponds to IDD Field `Control 2 Name`
        Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Control 2 Name`
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
                                 ' for field `ZoneControlThermostat.control_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.control_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.control_2_name`')
        self._data["Control 2 Name"] = value

    @property
    def control_3_object_type(self):
        """Get control_3_object_type

        Returns:
            str: the value of `control_3_object_type` or None if not set
        """
        return self._data["Control 3 Object Type"]

    @control_3_object_type.setter
    def control_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Control 3 Object Type`

        Args:
            value (str): value for IDD Field `Control 3 Object Type`
                Accepted values are:
                      - ThermostatSetpoint:SingleHeating
                      - ThermostatSetpoint:SingleCooling
                      - ThermostatSetpoint:SingleHeatingOrCooling
                      - ThermostatSetpoint:DualSetpoint
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
                                 ' for field `ZoneControlThermostat.control_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.control_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.control_3_object_type`')
            vals = {}
            vals["thermostatsetpoint:singleheating"] = "ThermostatSetpoint:SingleHeating"
            vals["thermostatsetpoint:singlecooling"] = "ThermostatSetpoint:SingleCooling"
            vals["thermostatsetpoint:singleheatingorcooling"] = "ThermostatSetpoint:SingleHeatingOrCooling"
            vals["thermostatsetpoint:dualsetpoint"] = "ThermostatSetpoint:DualSetpoint"
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
                                     'field `ZoneControlThermostat.control_3_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostat.control_3_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control 3 Object Type"] = value

    @property
    def control_3_name(self):
        """Get control_3_name

        Returns:
            str: the value of `control_3_name` or None if not set
        """
        return self._data["Control 3 Name"]

    @control_3_name.setter
    def control_3_name(self, value=None):
        """  Corresponds to IDD Field `Control 3 Name`
        Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Control 3 Name`
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
                                 ' for field `ZoneControlThermostat.control_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.control_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.control_3_name`')
        self._data["Control 3 Name"] = value

    @property
    def control_4_object_type(self):
        """Get control_4_object_type

        Returns:
            str: the value of `control_4_object_type` or None if not set
        """
        return self._data["Control 4 Object Type"]

    @control_4_object_type.setter
    def control_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Control 4 Object Type`

        Args:
            value (str): value for IDD Field `Control 4 Object Type`
                Accepted values are:
                      - ThermostatSetpoint:SingleHeating
                      - ThermostatSetpoint:SingleCooling
                      - ThermostatSetpoint:SingleHeatingOrCooling
                      - ThermostatSetpoint:DualSetpoint
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
                                 ' for field `ZoneControlThermostat.control_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.control_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.control_4_object_type`')
            vals = {}
            vals["thermostatsetpoint:singleheating"] = "ThermostatSetpoint:SingleHeating"
            vals["thermostatsetpoint:singlecooling"] = "ThermostatSetpoint:SingleCooling"
            vals["thermostatsetpoint:singleheatingorcooling"] = "ThermostatSetpoint:SingleHeatingOrCooling"
            vals["thermostatsetpoint:dualsetpoint"] = "ThermostatSetpoint:DualSetpoint"
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
                                     'field `ZoneControlThermostat.control_4_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostat.control_4_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control 4 Object Type"] = value

    @property
    def control_4_name(self):
        """Get control_4_name

        Returns:
            str: the value of `control_4_name` or None if not set
        """
        return self._data["Control 4 Name"]

    @control_4_name.setter
    def control_4_name(self, value=None):
        """  Corresponds to IDD Field `Control 4 Name`
        Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Control 4 Name`
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
                                 ' for field `ZoneControlThermostat.control_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostat.control_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostat.control_4_name`')
        self._data["Control 4 Name"] = value

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
                    raise ValueError("Required field ZoneControlThermostat:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneControlThermostat:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneControlThermostat: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneControlThermostat: {} / {}".format(out_fields,
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

class ZoneControlThermostatOperativeTemperature(object):
    """ Corresponds to IDD object `ZoneControl:Thermostat:OperativeTemperature`
        This object can be used with the ZoneList option on a thermostat or with one
        of the zones on that list (but you won't be able to use the object list to
        pick only one of those zones.  Thermostat names are <Zone Name> <global Thermostat name> internally.
    """
    internal_name = "ZoneControl:Thermostat:OperativeTemperature"
    field_count = 4
    required_fields = ["Thermostat Name", "Radiative Fraction Input Mode"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Thermostat:OperativeTemperature`
        """
        self._data = OrderedDict()
        self._data["Thermostat Name"] = None
        self._data["Radiative Fraction Input Mode"] = None
        self._data["Fixed Radiative Fraction"] = None
        self._data["Radiative Fraction Schedule Name"] = None
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
            self.thermostat_name = None
        else:
            self.thermostat_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.radiative_fraction_input_mode = None
        else:
            self.radiative_fraction_input_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fixed_radiative_fraction = None
        else:
            self.fixed_radiative_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.radiative_fraction_schedule_name = None
        else:
            self.radiative_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def thermostat_name(self):
        """Get thermostat_name

        Returns:
            str: the value of `thermostat_name` or None if not set
        """
        return self._data["Thermostat Name"]

    @thermostat_name.setter
    def thermostat_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat Name`
        Enter the name of a ZoneControl:Thermostat object.
        This object modifies a ZoneControl:Thermostat object to add a
        radiative fraction.

        Args:
            value (str): value for IDD Field `Thermostat Name`
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
                                 ' for field `ZoneControlThermostatOperativeTemperature.thermostat_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatOperativeTemperature.thermostat_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatOperativeTemperature.thermostat_name`')
        self._data["Thermostat Name"] = value

    @property
    def radiative_fraction_input_mode(self):
        """Get radiative_fraction_input_mode

        Returns:
            str: the value of `radiative_fraction_input_mode` or None if not set
        """
        return self._data["Radiative Fraction Input Mode"]

    @radiative_fraction_input_mode.setter
    def radiative_fraction_input_mode(self, value=None):
        """  Corresponds to IDD Field `Radiative Fraction Input Mode`

        Args:
            value (str): value for IDD Field `Radiative Fraction Input Mode`
                Accepted values are:
                      - Constant
                      - Scheduled
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
                                 ' for field `ZoneControlThermostatOperativeTemperature.radiative_fraction_input_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatOperativeTemperature.radiative_fraction_input_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatOperativeTemperature.radiative_fraction_input_mode`')
            vals = {}
            vals["constant"] = "Constant"
            vals["scheduled"] = "Scheduled"
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
                                     'field `ZoneControlThermostatOperativeTemperature.radiative_fraction_input_mode`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostatOperativeTemperature.radiative_fraction_input_mode`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Radiative Fraction Input Mode"] = value

    @property
    def fixed_radiative_fraction(self):
        """Get fixed_radiative_fraction

        Returns:
            float: the value of `fixed_radiative_fraction` or None if not set
        """
        return self._data["Fixed Radiative Fraction"]

    @fixed_radiative_fraction.setter
    def fixed_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `Fixed Radiative Fraction`

        Args:
            value (float): value for IDD Field `Fixed Radiative Fraction`
                value >= 0.0
                value < 0.9
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
                                 ' for field `ZoneControlThermostatOperativeTemperature.fixed_radiative_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatOperativeTemperature.fixed_radiative_fraction`')
            if value >= 0.9:
                raise ValueError('value need to be smaller 0.9 '
                                 'for field `ZoneControlThermostatOperativeTemperature.fixed_radiative_fraction`')
        self._data["Fixed Radiative Fraction"] = value

    @property
    def radiative_fraction_schedule_name(self):
        """Get radiative_fraction_schedule_name

        Returns:
            str: the value of `radiative_fraction_schedule_name` or None if not set
        """
        return self._data["Radiative Fraction Schedule Name"]

    @radiative_fraction_schedule_name.setter
    def radiative_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Radiative Fraction Schedule Name`
        Schedule values of 0.0 indicate no operative temperature control

        Args:
            value (str): value for IDD Field `Radiative Fraction Schedule Name`
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
                                 ' for field `ZoneControlThermostatOperativeTemperature.radiative_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatOperativeTemperature.radiative_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatOperativeTemperature.radiative_fraction_schedule_name`')
        self._data["Radiative Fraction Schedule Name"] = value

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
                    raise ValueError("Required field ZoneControlThermostatOperativeTemperature:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneControlThermostatOperativeTemperature:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneControlThermostatOperativeTemperature: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneControlThermostatOperativeTemperature: {} / {}".format(out_fields,
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

class ZoneControlThermostatThermalComfort(object):
    """ Corresponds to IDD object `ZoneControl:Thermostat:ThermalComfort`
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    """
    internal_name = "ZoneControl:Thermostat:ThermalComfort"
    field_count = 15
    required_fields = ["Name", "Zone or ZoneList Name", "Minimum Dry-Bulb Temperature Setpoint", "Maximum Dry-Bulb Temperature Setpoint", "Thermal Comfort Control Type Schedule Name", "Thermal Comfort Control 1 Object Type", "Thermal Comfort Control 1 Name"]
    extensible_fields = 0
    format = None
    min_fields = 9
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Thermostat:ThermalComfort`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Averaging Method"] = None
        self._data["Specific People Name"] = None
        self._data["Minimum Dry-Bulb Temperature Setpoint"] = None
        self._data["Maximum Dry-Bulb Temperature Setpoint"] = None
        self._data["Thermal Comfort Control Type Schedule Name"] = None
        self._data["Thermal Comfort Control 1 Object Type"] = None
        self._data["Thermal Comfort Control 1 Name"] = None
        self._data["Thermal Comfort Control 2 Object Type"] = None
        self._data["Thermal Comfort Control 2 Name"] = None
        self._data["Thermal Comfort Control 3 Object Type"] = None
        self._data["Thermal Comfort Control 3 Name"] = None
        self._data["Thermal Comfort Control 4 Object Type"] = None
        self._data["Thermal Comfort Control 4 Name"] = None
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
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.averaging_method = None
        else:
            self.averaging_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.specific_people_name = None
        else:
            self.specific_people_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_drybulb_temperature_setpoint = None
        else:
            self.minimum_drybulb_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_drybulb_temperature_setpoint = None
        else:
            self.maximum_drybulb_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_type_schedule_name = None
        else:
            self.thermal_comfort_control_type_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_1_object_type = None
        else:
            self.thermal_comfort_control_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_1_name = None
        else:
            self.thermal_comfort_control_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_2_object_type = None
        else:
            self.thermal_comfort_control_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_2_name = None
        else:
            self.thermal_comfort_control_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_3_object_type = None
        else:
            self.thermal_comfort_control_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_3_name = None
        else:
            self.thermal_comfort_control_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_4_object_type = None
        else:
            self.thermal_comfort_control_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_4_name = None
        else:
            self.thermal_comfort_control_4_name = vals[i]
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
                                 ' for field `ZoneControlThermostatThermalComfort.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.name`')
        self._data["Name"] = value

    @property
    def zone_or_zonelist_name(self):
        """Get zone_or_zonelist_name

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set
        """
        return self._data["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """  Corresponds to IDD Field `Zone or ZoneList Name`

        Args:
            value (str): value for IDD Field `Zone or ZoneList Name`
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
                                 ' for field `ZoneControlThermostatThermalComfort.zone_or_zonelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.zone_or_zonelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.zone_or_zonelist_name`')
        self._data["Zone or ZoneList Name"] = value

    @property
    def averaging_method(self):
        """Get averaging_method

        Returns:
            str: the value of `averaging_method` or None if not set
        """
        return self._data["Averaging Method"]

    @averaging_method.setter
    def averaging_method(self, value="PeopleAverage"):
        """  Corresponds to IDD Field `Averaging Method`
        The method used to calculate thermal comfort dry-bulb temperature setpoint
        for multiple people objects in a zone

        Args:
            value (str): value for IDD Field `Averaging Method`
                Accepted values are:
                      - SpecificObject
                      - ObjectAverage
                      - PeopleAverage
                Default value: PeopleAverage
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
                                 ' for field `ZoneControlThermostatThermalComfort.averaging_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.averaging_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.averaging_method`')
            vals = {}
            vals["specificobject"] = "SpecificObject"
            vals["objectaverage"] = "ObjectAverage"
            vals["peopleaverage"] = "PeopleAverage"
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
                                     'field `ZoneControlThermostatThermalComfort.averaging_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostatThermalComfort.averaging_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Averaging Method"] = value

    @property
    def specific_people_name(self):
        """Get specific_people_name

        Returns:
            str: the value of `specific_people_name` or None if not set
        """
        return self._data["Specific People Name"]

    @specific_people_name.setter
    def specific_people_name(self, value=None):
        """  Corresponds to IDD Field `Specific People Name`
        Used only when Averaging Method = SpecificObject in the previous field.

        Args:
            value (str): value for IDD Field `Specific People Name`
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
                                 ' for field `ZoneControlThermostatThermalComfort.specific_people_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.specific_people_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.specific_people_name`')
        self._data["Specific People Name"] = value

    @property
    def minimum_drybulb_temperature_setpoint(self):
        """Get minimum_drybulb_temperature_setpoint

        Returns:
            float: the value of `minimum_drybulb_temperature_setpoint` or None if not set
        """
        return self._data["Minimum Dry-Bulb Temperature Setpoint"]

    @minimum_drybulb_temperature_setpoint.setter
    def minimum_drybulb_temperature_setpoint(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Dry-Bulb Temperature Setpoint`

        Args:
            value (float): value for IDD Field `Minimum Dry-Bulb Temperature Setpoint`
                Units: C
                Default value: 0.0
                value >= 0.0
                value <= 50.0
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
                                 ' for field `ZoneControlThermostatThermalComfort.minimum_drybulb_temperature_setpoint`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatThermalComfort.minimum_drybulb_temperature_setpoint`')
            if value > 50.0:
                raise ValueError('value need to be smaller 50.0 '
                                 'for field `ZoneControlThermostatThermalComfort.minimum_drybulb_temperature_setpoint`')
        self._data["Minimum Dry-Bulb Temperature Setpoint"] = value

    @property
    def maximum_drybulb_temperature_setpoint(self):
        """Get maximum_drybulb_temperature_setpoint

        Returns:
            float: the value of `maximum_drybulb_temperature_setpoint` or None if not set
        """
        return self._data["Maximum Dry-Bulb Temperature Setpoint"]

    @maximum_drybulb_temperature_setpoint.setter
    def maximum_drybulb_temperature_setpoint(self, value=50.0):
        """  Corresponds to IDD Field `Maximum Dry-Bulb Temperature Setpoint`

        Args:
            value (float): value for IDD Field `Maximum Dry-Bulb Temperature Setpoint`
                Units: C
                Default value: 50.0
                value >= 0.0
                value <= 50.0
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
                                 ' for field `ZoneControlThermostatThermalComfort.maximum_drybulb_temperature_setpoint`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatThermalComfort.maximum_drybulb_temperature_setpoint`')
            if value > 50.0:
                raise ValueError('value need to be smaller 50.0 '
                                 'for field `ZoneControlThermostatThermalComfort.maximum_drybulb_temperature_setpoint`')
        self._data["Maximum Dry-Bulb Temperature Setpoint"] = value

    @property
    def thermal_comfort_control_type_schedule_name(self):
        """Get thermal_comfort_control_type_schedule_name

        Returns:
            str: the value of `thermal_comfort_control_type_schedule_name` or None if not set
        """
        return self._data["Thermal Comfort Control Type Schedule Name"]

    @thermal_comfort_control_type_schedule_name.setter
    def thermal_comfort_control_type_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Thermal Comfort Control Type Schedule Name`
        The Thermal Comfort Control Type Schedule contains values that are appropriate control types.
        Thermal Comfort Control types are integers: 0 - Uncontrolled (floating),
        1 = ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
        2 = ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
        3 = ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
        4 = ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint

        Args:
            value (str): value for IDD Field `Thermal Comfort Control Type Schedule Name`
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
                                 ' for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_type_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_type_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_type_schedule_name`')
        self._data["Thermal Comfort Control Type Schedule Name"] = value

    @property
    def thermal_comfort_control_1_object_type(self):
        """Get thermal_comfort_control_1_object_type

        Returns:
            str: the value of `thermal_comfort_control_1_object_type` or None if not set
        """
        return self._data["Thermal Comfort Control 1 Object Type"]

    @thermal_comfort_control_1_object_type.setter
    def thermal_comfort_control_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Thermal Comfort Control 1 Object Type`

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 1 Object Type`
                Accepted values are:
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint
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
                                 ' for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_1_object_type`')
            vals = {}
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheating"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
            vals["thermostatsetpoint:thermalcomfort:fanger:singlecooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:dualsetpoint"] = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
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
                                     'field `ZoneControlThermostatThermalComfort.thermal_comfort_control_1_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostatThermalComfort.thermal_comfort_control_1_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Thermal Comfort Control 1 Object Type"] = value

    @property
    def thermal_comfort_control_1_name(self):
        """Get thermal_comfort_control_1_name

        Returns:
            str: the value of `thermal_comfort_control_1_name` or None if not set
        """
        return self._data["Thermal Comfort Control 1 Name"]

    @thermal_comfort_control_1_name.setter
    def thermal_comfort_control_1_name(self, value=None):
        """  Corresponds to IDD Field `Thermal Comfort Control 1 Name`
        Control type names are names for individual control type objects.
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 1 Name`
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
                                 ' for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_1_name`')
        self._data["Thermal Comfort Control 1 Name"] = value

    @property
    def thermal_comfort_control_2_object_type(self):
        """Get thermal_comfort_control_2_object_type

        Returns:
            str: the value of `thermal_comfort_control_2_object_type` or None if not set
        """
        return self._data["Thermal Comfort Control 2 Object Type"]

    @thermal_comfort_control_2_object_type.setter
    def thermal_comfort_control_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Thermal Comfort Control 2 Object Type`

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 2 Object Type`
                Accepted values are:
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint
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
                                 ' for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_2_object_type`')
            vals = {}
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheating"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
            vals["thermostatsetpoint:thermalcomfort:fanger:singlecooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:dualsetpoint"] = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
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
                                     'field `ZoneControlThermostatThermalComfort.thermal_comfort_control_2_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostatThermalComfort.thermal_comfort_control_2_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Thermal Comfort Control 2 Object Type"] = value

    @property
    def thermal_comfort_control_2_name(self):
        """Get thermal_comfort_control_2_name

        Returns:
            str: the value of `thermal_comfort_control_2_name` or None if not set
        """
        return self._data["Thermal Comfort Control 2 Name"]

    @thermal_comfort_control_2_name.setter
    def thermal_comfort_control_2_name(self, value=None):
        """  Corresponds to IDD Field `Thermal Comfort Control 2 Name`
        Control Type names are names for individual control type objects.
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 2 Name`
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
                                 ' for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_2_name`')
        self._data["Thermal Comfort Control 2 Name"] = value

    @property
    def thermal_comfort_control_3_object_type(self):
        """Get thermal_comfort_control_3_object_type

        Returns:
            str: the value of `thermal_comfort_control_3_object_type` or None if not set
        """
        return self._data["Thermal Comfort Control 3 Object Type"]

    @thermal_comfort_control_3_object_type.setter
    def thermal_comfort_control_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Thermal Comfort Control 3 Object Type`

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 3 Object Type`
                Accepted values are:
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint
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
                                 ' for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_3_object_type`')
            vals = {}
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheating"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
            vals["thermostatsetpoint:thermalcomfort:fanger:singlecooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:dualsetpoint"] = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
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
                                     'field `ZoneControlThermostatThermalComfort.thermal_comfort_control_3_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostatThermalComfort.thermal_comfort_control_3_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Thermal Comfort Control 3 Object Type"] = value

    @property
    def thermal_comfort_control_3_name(self):
        """Get thermal_comfort_control_3_name

        Returns:
            str: the value of `thermal_comfort_control_3_name` or None if not set
        """
        return self._data["Thermal Comfort Control 3 Name"]

    @thermal_comfort_control_3_name.setter
    def thermal_comfort_control_3_name(self, value=None):
        """  Corresponds to IDD Field `Thermal Comfort Control 3 Name`
        Control type names are names for individual control type objects.
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 3 Name`
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
                                 ' for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_3_name`')
        self._data["Thermal Comfort Control 3 Name"] = value

    @property
    def thermal_comfort_control_4_object_type(self):
        """Get thermal_comfort_control_4_object_type

        Returns:
            str: the value of `thermal_comfort_control_4_object_type` or None if not set
        """
        return self._data["Thermal Comfort Control 4 Object Type"]

    @thermal_comfort_control_4_object_type.setter
    def thermal_comfort_control_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Thermal Comfort Control 4 Object Type`

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 4 Object Type`
                Accepted values are:
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint
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
                                 ' for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_4_object_type`')
            vals = {}
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheating"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
            vals["thermostatsetpoint:thermalcomfort:fanger:singlecooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:dualsetpoint"] = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
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
                                     'field `ZoneControlThermostatThermalComfort.thermal_comfort_control_4_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostatThermalComfort.thermal_comfort_control_4_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Thermal Comfort Control 4 Object Type"] = value

    @property
    def thermal_comfort_control_4_name(self):
        """Get thermal_comfort_control_4_name

        Returns:
            str: the value of `thermal_comfort_control_4_name` or None if not set
        """
        return self._data["Thermal Comfort Control 4 Name"]

    @thermal_comfort_control_4_name.setter
    def thermal_comfort_control_4_name(self, value=None):
        """  Corresponds to IDD Field `Thermal Comfort Control 4 Name`
        Control type names are names for individual control type objects.
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 4 Name`
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
                                 ' for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatThermalComfort.thermal_comfort_control_4_name`')
        self._data["Thermal Comfort Control 4 Name"] = value

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
                    raise ValueError("Required field ZoneControlThermostatThermalComfort:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneControlThermostatThermalComfort:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneControlThermostatThermalComfort: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneControlThermostatThermalComfort: {} / {}".format(out_fields,
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

class ZoneControlThermostatTemperatureAndHumidity(object):
    """ Corresponds to IDD object `ZoneControl:Thermostat:TemperatureAndHumidity`
        This object modifies a ZoneControl:Thermostat object to effect temperature control based on
        zone air humidity conditions.
    """
    internal_name = "ZoneControl:Thermostat:TemperatureAndHumidity"
    field_count = 7
    required_fields = ["Thermostat Name", "Dehumidifying Relative Humidity Setpoint Schedule Name"]
    extensible_fields = 0
    format = None
    min_fields = 2
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Thermostat:TemperatureAndHumidity`
        """
        self._data = OrderedDict()
        self._data["Thermostat Name"] = None
        self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"] = None
        self._data["Dehumidification Control Type"] = None
        self._data["Overcool Range Input Method"] = None
        self._data["Overcool Constant Range"] = None
        self._data["Overcool Range Schedule Name"] = None
        self._data["Overcool Control Ratio"] = None
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
            self.thermostat_name = None
        else:
            self.thermostat_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dehumidifying_relative_humidity_setpoint_schedule_name = None
        else:
            self.dehumidifying_relative_humidity_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dehumidification_control_type = None
        else:
            self.dehumidification_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overcool_range_input_method = None
        else:
            self.overcool_range_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overcool_constant_range = None
        else:
            self.overcool_constant_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overcool_range_schedule_name = None
        else:
            self.overcool_range_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overcool_control_ratio = None
        else:
            self.overcool_control_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def thermostat_name(self):
        """Get thermostat_name

        Returns:
            str: the value of `thermostat_name` or None if not set
        """
        return self._data["Thermostat Name"]

    @thermostat_name.setter
    def thermostat_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat Name`
        Enter the name of a ZoneControl:Thermostat object whose operation is to be modified to
        effect temperature control based on zone air humidity conditions. If the ZoneControl:
        Thermostat object references a ZoneList, simply enter the name of the ZoneControl:Thermostat
        object and this temperature and humidity thermostat control will be applied to all zones
        in the ZoneList. If the ZoneControl:Thermostat object references a ZoneList but it is
        desired that only a single zone within the ZoneList be controlled based on temperature and
        humidity control, then the name to be put here is <Zone Name> <Thermostat Name> where the
        Thermostat Name is the the name of the ZoneControl:Thermostat object.

        Args:
            value (str): value for IDD Field `Thermostat Name`
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
                                 ' for field `ZoneControlThermostatTemperatureAndHumidity.thermostat_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.thermostat_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.thermostat_name`')
        self._data["Thermostat Name"] = value

    @property
    def dehumidifying_relative_humidity_setpoint_schedule_name(self):
        """Get dehumidifying_relative_humidity_setpoint_schedule_name

        Returns:
            str: the value of `dehumidifying_relative_humidity_setpoint_schedule_name` or None if not set
        """
        return self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"]

    @dehumidifying_relative_humidity_setpoint_schedule_name.setter
    def dehumidifying_relative_humidity_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Dehumidifying Relative Humidity Setpoint Schedule Name`
        Schedule values should be in Relative Humidity (percent)

        Args:
            value (str): value for IDD Field `Dehumidifying Relative Humidity Setpoint Schedule Name`
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
                                 ' for field `ZoneControlThermostatTemperatureAndHumidity.dehumidifying_relative_humidity_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.dehumidifying_relative_humidity_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.dehumidifying_relative_humidity_setpoint_schedule_name`')
        self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"] = value

    @property
    def dehumidification_control_type(self):
        """Get dehumidification_control_type

        Returns:
            str: the value of `dehumidification_control_type` or None if not set
        """
        return self._data["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="Overcool"):
        """  Corresponds to IDD Field `Dehumidification Control Type`

        Args:
            value (str): value for IDD Field `Dehumidification Control Type`
                Accepted values are:
                      - Overcool
                      - None
                Default value: Overcool
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
                                 ' for field `ZoneControlThermostatTemperatureAndHumidity.dehumidification_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.dehumidification_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.dehumidification_control_type`')
            vals = {}
            vals["overcool"] = "Overcool"
            vals["none"] = "None"
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
                                     'field `ZoneControlThermostatTemperatureAndHumidity.dehumidification_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostatTemperatureAndHumidity.dehumidification_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Dehumidification Control Type"] = value

    @property
    def overcool_range_input_method(self):
        """Get overcool_range_input_method

        Returns:
            str: the value of `overcool_range_input_method` or None if not set
        """
        return self._data["Overcool Range Input Method"]

    @overcool_range_input_method.setter
    def overcool_range_input_method(self, value="Constant"):
        """  Corresponds to IDD Field `Overcool Range Input Method`

        Args:
            value (str): value for IDD Field `Overcool Range Input Method`
                Accepted values are:
                      - Constant
                      - Scheduled
                Default value: Constant
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
                                 ' for field `ZoneControlThermostatTemperatureAndHumidity.overcool_range_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.overcool_range_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.overcool_range_input_method`')
            vals = {}
            vals["constant"] = "Constant"
            vals["scheduled"] = "Scheduled"
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
                                     'field `ZoneControlThermostatTemperatureAndHumidity.overcool_range_input_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneControlThermostatTemperatureAndHumidity.overcool_range_input_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Overcool Range Input Method"] = value

    @property
    def overcool_constant_range(self):
        """Get overcool_constant_range

        Returns:
            float: the value of `overcool_constant_range` or None if not set
        """
        return self._data["Overcool Constant Range"]

    @overcool_constant_range.setter
    def overcool_constant_range(self, value=1.7):
        """  Corresponds to IDD Field `Overcool Constant Range`
        Maximum Overcool temperature range for cooling setpoint reduction.
        Used with Dehumidification Control Type = Overcool.
        A value of 0.0 indicates no zone temperature overcooling will be provided to
        gain additional dehumidification.

        Args:
            value (float): value for IDD Field `Overcool Constant Range`
                Units: deltaC
                Default value: 1.7
                value >= 0.0
                value <= 3.0
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
                                 ' for field `ZoneControlThermostatTemperatureAndHumidity.overcool_constant_range`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.overcool_constant_range`')
            if value > 3.0:
                raise ValueError('value need to be smaller 3.0 '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.overcool_constant_range`')
        self._data["Overcool Constant Range"] = value

    @property
    def overcool_range_schedule_name(self):
        """Get overcool_range_schedule_name

        Returns:
            str: the value of `overcool_range_schedule_name` or None if not set
        """
        return self._data["Overcool Range Schedule Name"]

    @overcool_range_schedule_name.setter
    def overcool_range_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Overcool Range Schedule Name`
        Schedule values of 0.0 indicates no zone temperature overcooling will be
        provided to gain additional dehumidification.
        Schedule values should be >= 0 and <= 3 (deltaC).

        Args:
            value (str): value for IDD Field `Overcool Range Schedule Name`
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
                                 ' for field `ZoneControlThermostatTemperatureAndHumidity.overcool_range_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.overcool_range_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.overcool_range_schedule_name`')
        self._data["Overcool Range Schedule Name"] = value

    @property
    def overcool_control_ratio(self):
        """Get overcool_control_ratio

        Returns:
            float: the value of `overcool_control_ratio` or None if not set
        """
        return self._data["Overcool Control Ratio"]

    @overcool_control_ratio.setter
    def overcool_control_ratio(self, value=3.6):
        """  Corresponds to IDD Field `Overcool Control Ratio`
        The value of this input field is used to adjust the cooling setpoint temperature
        (established by the associated ZoneControl:Thermostat object) downward based on the
        difference between the zone air relative humidity level and the dehumidifying
        relative humidity setpoint.

        Args:
            value (float): value for IDD Field `Overcool Control Ratio`
                Units: percent/K
                Default value: 3.6
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
                                 ' for field `ZoneControlThermostatTemperatureAndHumidity.overcool_control_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatTemperatureAndHumidity.overcool_control_ratio`')
        self._data["Overcool Control Ratio"] = value

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
                    raise ValueError("Required field ZoneControlThermostatTemperatureAndHumidity:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneControlThermostatTemperatureAndHumidity:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneControlThermostatTemperatureAndHumidity: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneControlThermostatTemperatureAndHumidity: {} / {}".format(out_fields,
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

class ThermostatSetpointSingleHeating(object):
    """ Corresponds to IDD object `ThermostatSetpoint:SingleHeating`
        Used for a heating only thermostat. The setpoint can be scheduled and varied throughout
        the simulation but only heating is allowed with this control type.
    """
    internal_name = "ThermostatSetpoint:SingleHeating"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:SingleHeating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
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
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
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
                                 ' for field `ThermostatSetpointSingleHeating.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointSingleHeating.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointSingleHeating.name`')
        self._data["Name"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Setpoint Temperature Schedule Name`
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
                                 ' for field `ThermostatSetpointSingleHeating.setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointSingleHeating.setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointSingleHeating.setpoint_temperature_schedule_name`')
        self._data["Setpoint Temperature Schedule Name"] = value

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
                    raise ValueError("Required field ThermostatSetpointSingleHeating:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ThermostatSetpointSingleHeating:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ThermostatSetpointSingleHeating: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ThermostatSetpointSingleHeating: {} / {}".format(out_fields,
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

class ThermostatSetpointSingleCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:SingleCooling`
        Used for a cooling only thermostat. The setpoint can be scheduled and varied throughout
        the simulation but only cooling is allowed.
    """
    internal_name = "ThermostatSetpoint:SingleCooling"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:SingleCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
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
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
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
                                 ' for field `ThermostatSetpointSingleCooling.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointSingleCooling.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointSingleCooling.name`')
        self._data["Name"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Setpoint Temperature Schedule Name`
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
                                 ' for field `ThermostatSetpointSingleCooling.setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointSingleCooling.setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointSingleCooling.setpoint_temperature_schedule_name`')
        self._data["Setpoint Temperature Schedule Name"] = value

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
                    raise ValueError("Required field ThermostatSetpointSingleCooling:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ThermostatSetpointSingleCooling:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ThermostatSetpointSingleCooling: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ThermostatSetpointSingleCooling: {} / {}".format(out_fields,
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

class ThermostatSetpointSingleHeatingOrCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:SingleHeatingOrCooling`
        Used for a heating and cooling thermostat with a single setpoint. The setpoint can be
        scheduled and varied throughout the simulation for both heating and cooling.
    """
    internal_name = "ThermostatSetpoint:SingleHeatingOrCooling"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:SingleHeatingOrCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
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
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
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
                                 ' for field `ThermostatSetpointSingleHeatingOrCooling.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointSingleHeatingOrCooling.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointSingleHeatingOrCooling.name`')
        self._data["Name"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Setpoint Temperature Schedule Name`
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
                                 ' for field `ThermostatSetpointSingleHeatingOrCooling.setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointSingleHeatingOrCooling.setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointSingleHeatingOrCooling.setpoint_temperature_schedule_name`')
        self._data["Setpoint Temperature Schedule Name"] = value

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
                    raise ValueError("Required field ThermostatSetpointSingleHeatingOrCooling:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ThermostatSetpointSingleHeatingOrCooling:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ThermostatSetpointSingleHeatingOrCooling: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ThermostatSetpointSingleHeatingOrCooling: {} / {}".format(out_fields,
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

class ThermostatSetpointDualSetpoint(object):
    """ Corresponds to IDD object `ThermostatSetpoint:DualSetpoint`
        Used for a heating and cooling thermostat with dual setpoints. The setpoints can be
        scheduled and varied throughout the simulation for both heating and cooling.
    """
    internal_name = "ThermostatSetpoint:DualSetpoint"
    field_count = 3
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:DualSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Heating Setpoint Temperature Schedule Name"] = None
        self._data["Cooling Setpoint Temperature Schedule Name"] = None
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
            self.heating_setpoint_temperature_schedule_name = None
        else:
            self.heating_setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_setpoint_temperature_schedule_name = None
        else:
            self.cooling_setpoint_temperature_schedule_name = vals[i]
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
                                 ' for field `ThermostatSetpointDualSetpoint.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointDualSetpoint.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointDualSetpoint.name`')
        self._data["Name"] = value

    @property
    def heating_setpoint_temperature_schedule_name(self):
        """Get heating_setpoint_temperature_schedule_name

        Returns:
            str: the value of `heating_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Heating Setpoint Temperature Schedule Name"]

    @heating_setpoint_temperature_schedule_name.setter
    def heating_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Setpoint Temperature Schedule Name`
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
                                 ' for field `ThermostatSetpointDualSetpoint.heating_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointDualSetpoint.heating_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointDualSetpoint.heating_setpoint_temperature_schedule_name`')
        self._data["Heating Setpoint Temperature Schedule Name"] = value

    @property
    def cooling_setpoint_temperature_schedule_name(self):
        """Get cooling_setpoint_temperature_schedule_name

        Returns:
            str: the value of `cooling_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling Setpoint Temperature Schedule Name"]

    @cooling_setpoint_temperature_schedule_name.setter
    def cooling_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Setpoint Temperature Schedule Name`
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
                                 ' for field `ThermostatSetpointDualSetpoint.cooling_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointDualSetpoint.cooling_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointDualSetpoint.cooling_setpoint_temperature_schedule_name`')
        self._data["Cooling Setpoint Temperature Schedule Name"] = value

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
                    raise ValueError("Required field ThermostatSetpointDualSetpoint:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ThermostatSetpointDualSetpoint:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ThermostatSetpointDualSetpoint: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ThermostatSetpointDualSetpoint: {} / {}".format(out_fields,
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

class ThermostatSetpointThermalComfortFangerSingleHeating(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating`
        Used for heating only thermal comfort control. The PMV setpoint can be scheduled and
        varied throughout the simulation but only heating is allowed with this control type.
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
    field_count = 2
    required_fields = ["Name", "Fanger Thermal Comfort Schedule Name"]
    extensible_fields = 0
    format = None
    min_fields = 2
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Schedule Name"] = None
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
            self.fanger_thermal_comfort_schedule_name = None
        else:
            self.fanger_thermal_comfort_schedule_name = vals[i]
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
                                 ' for field `ThermostatSetpointThermalComfortFangerSingleHeating.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleHeating.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleHeating.name`')
        self._data["Name"] = value

    @property
    def fanger_thermal_comfort_schedule_name(self):
        """Get fanger_thermal_comfort_schedule_name

        Returns:
            str: the value of `fanger_thermal_comfort_schedule_name` or None if not set
        """
        return self._data["Fanger Thermal Comfort Schedule Name"]

    @fanger_thermal_comfort_schedule_name.setter
    def fanger_thermal_comfort_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Fanger Thermal Comfort Schedule Name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `Fanger Thermal Comfort Schedule Name`
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
                                 ' for field `ThermostatSetpointThermalComfortFangerSingleHeating.fanger_thermal_comfort_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleHeating.fanger_thermal_comfort_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleHeating.fanger_thermal_comfort_schedule_name`')
        self._data["Fanger Thermal Comfort Schedule Name"] = value

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
                    raise ValueError("Required field ThermostatSetpointThermalComfortFangerSingleHeating:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ThermostatSetpointThermalComfortFangerSingleHeating:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ThermostatSetpointThermalComfortFangerSingleHeating: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ThermostatSetpointThermalComfortFangerSingleHeating: {} / {}".format(out_fields,
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

class ThermostatSetpointThermalComfortFangerSingleCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling`
        Used for cooling only thermal comfort control. The PMV setpoint can be scheduled and
        varied throughout the simulation but only cooling is allowed with this control type.
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
    field_count = 2
    required_fields = ["Name", "Fanger Thermal Comfort Schedule Name"]
    extensible_fields = 0
    format = None
    min_fields = 2
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Schedule Name"] = None
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
            self.fanger_thermal_comfort_schedule_name = None
        else:
            self.fanger_thermal_comfort_schedule_name = vals[i]
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
                                 ' for field `ThermostatSetpointThermalComfortFangerSingleCooling.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleCooling.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleCooling.name`')
        self._data["Name"] = value

    @property
    def fanger_thermal_comfort_schedule_name(self):
        """Get fanger_thermal_comfort_schedule_name

        Returns:
            str: the value of `fanger_thermal_comfort_schedule_name` or None if not set
        """
        return self._data["Fanger Thermal Comfort Schedule Name"]

    @fanger_thermal_comfort_schedule_name.setter
    def fanger_thermal_comfort_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Fanger Thermal Comfort Schedule Name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `Fanger Thermal Comfort Schedule Name`
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
                                 ' for field `ThermostatSetpointThermalComfortFangerSingleCooling.fanger_thermal_comfort_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleCooling.fanger_thermal_comfort_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleCooling.fanger_thermal_comfort_schedule_name`')
        self._data["Fanger Thermal Comfort Schedule Name"] = value

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
                    raise ValueError("Required field ThermostatSetpointThermalComfortFangerSingleCooling:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ThermostatSetpointThermalComfortFangerSingleCooling:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ThermostatSetpointThermalComfortFangerSingleCooling: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ThermostatSetpointThermalComfortFangerSingleCooling: {} / {}".format(out_fields,
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

class ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling`
        Used for heating and cooling thermal comfort control with a single setpoint. The PMV
        setpoint can be scheduled and varied throughout the simulation for both heating and
        cooling.
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
    field_count = 2
    required_fields = ["Name", "Fanger Thermal Comfort Schedule Name"]
    extensible_fields = 0
    format = None
    min_fields = 2
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Schedule Name"] = None
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
            self.fanger_thermal_comfort_schedule_name = None
        else:
            self.fanger_thermal_comfort_schedule_name = vals[i]
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
                                 ' for field `ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling.name`')
        self._data["Name"] = value

    @property
    def fanger_thermal_comfort_schedule_name(self):
        """Get fanger_thermal_comfort_schedule_name

        Returns:
            str: the value of `fanger_thermal_comfort_schedule_name` or None if not set
        """
        return self._data["Fanger Thermal Comfort Schedule Name"]

    @fanger_thermal_comfort_schedule_name.setter
    def fanger_thermal_comfort_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Fanger Thermal Comfort Schedule Name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `Fanger Thermal Comfort Schedule Name`
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
                                 ' for field `ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling.fanger_thermal_comfort_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling.fanger_thermal_comfort_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling.fanger_thermal_comfort_schedule_name`')
        self._data["Fanger Thermal Comfort Schedule Name"] = value

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
                    raise ValueError("Required field ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling: {} / {}".format(out_fields,
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

class ThermostatSetpointThermalComfortFangerDualSetpoint(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint`
        Used for heating and cooling thermal comfort control with dual setpoints. The PMV
        setpoints can be scheduled and varied throughout the simulation for both heating and
        cooling.
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
    field_count = 3
    required_fields = ["Name", "Fanger Thermal Comfort Heating Schedule Name", "Fanger Thermal Comfort Cooling Schedule Name"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Heating Schedule Name"] = None
        self._data["Fanger Thermal Comfort Cooling Schedule Name"] = None
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
            self.fanger_thermal_comfort_heating_schedule_name = None
        else:
            self.fanger_thermal_comfort_heating_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fanger_thermal_comfort_cooling_schedule_name = None
        else:
            self.fanger_thermal_comfort_cooling_schedule_name = vals[i]
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
                                 ' for field `ThermostatSetpointThermalComfortFangerDualSetpoint.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointThermalComfortFangerDualSetpoint.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointThermalComfortFangerDualSetpoint.name`')
        self._data["Name"] = value

    @property
    def fanger_thermal_comfort_heating_schedule_name(self):
        """Get fanger_thermal_comfort_heating_schedule_name

        Returns:
            str: the value of `fanger_thermal_comfort_heating_schedule_name` or None if not set
        """
        return self._data["Fanger Thermal Comfort Heating Schedule Name"]

    @fanger_thermal_comfort_heating_schedule_name.setter
    def fanger_thermal_comfort_heating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Fanger Thermal Comfort Heating Schedule Name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `Fanger Thermal Comfort Heating Schedule Name`
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
                                 ' for field `ThermostatSetpointThermalComfortFangerDualSetpoint.fanger_thermal_comfort_heating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointThermalComfortFangerDualSetpoint.fanger_thermal_comfort_heating_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointThermalComfortFangerDualSetpoint.fanger_thermal_comfort_heating_schedule_name`')
        self._data["Fanger Thermal Comfort Heating Schedule Name"] = value

    @property
    def fanger_thermal_comfort_cooling_schedule_name(self):
        """Get fanger_thermal_comfort_cooling_schedule_name

        Returns:
            str: the value of `fanger_thermal_comfort_cooling_schedule_name` or None if not set
        """
        return self._data["Fanger Thermal Comfort Cooling Schedule Name"]

    @fanger_thermal_comfort_cooling_schedule_name.setter
    def fanger_thermal_comfort_cooling_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Fanger Thermal Comfort Cooling Schedule Name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `Fanger Thermal Comfort Cooling Schedule Name`
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
                                 ' for field `ThermostatSetpointThermalComfortFangerDualSetpoint.fanger_thermal_comfort_cooling_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ThermostatSetpointThermalComfortFangerDualSetpoint.fanger_thermal_comfort_cooling_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ThermostatSetpointThermalComfortFangerDualSetpoint.fanger_thermal_comfort_cooling_schedule_name`')
        self._data["Fanger Thermal Comfort Cooling Schedule Name"] = value

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
                    raise ValueError("Required field ThermostatSetpointThermalComfortFangerDualSetpoint:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ThermostatSetpointThermalComfortFangerDualSetpoint:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ThermostatSetpointThermalComfortFangerDualSetpoint: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ThermostatSetpointThermalComfortFangerDualSetpoint: {} / {}".format(out_fields,
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

class ZoneControlThermostatStagedDualSetpoint(object):
    """ Corresponds to IDD object `ZoneControl:Thermostat:StagedDualSetpoint`
        Define the Thermostat StagedDualSetpoint settings for a zone or list of zones.
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    """
    internal_name = "ZoneControl:Thermostat:StagedDualSetpoint"
    field_count = 16
    required_fields = ["Name", "Zone or ZoneList Name", "Number of Heating Stages", "Stage 1 Heating Temperature Offset", "Number of Cooling Stages", "Stage 1 Cooling Temperature Offset"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Thermostat:StagedDualSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Number of Heating Stages"] = None
        self._data["Heating Temperature Setpoint Schedule Name"] = None
        self._data["Heating Throttling Temperature Range"] = None
        self._data["Stage 1 Heating Temperature Offset"] = None
        self._data["Stage 2 Heating Temperature Offset"] = None
        self._data["Stage 3 Heating Temperature Offset"] = None
        self._data["Stage 4 Heating Temperature Offset"] = None
        self._data["Number of Cooling Stages"] = None
        self._data["Cooling Temperature Setpoint Base Schedule Name"] = None
        self._data["Cooling Throttling Temperature Range"] = None
        self._data["Stage 1 Cooling Temperature Offset"] = None
        self._data["Stage 2 Cooling Temperature Offset"] = None
        self._data["Stage 3 Cooling Temperature Offset"] = None
        self._data["Stage 4 Cooling Temperature Offset"] = None
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
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_heating_stages = None
        else:
            self.number_of_heating_stages = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_temperature_setpoint_schedule_name = None
        else:
            self.heating_temperature_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_throttling_temperature_range = None
        else:
            self.heating_throttling_temperature_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_1_heating_temperature_offset = None
        else:
            self.stage_1_heating_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_2_heating_temperature_offset = None
        else:
            self.stage_2_heating_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_3_heating_temperature_offset = None
        else:
            self.stage_3_heating_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_4_heating_temperature_offset = None
        else:
            self.stage_4_heating_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_cooling_stages = None
        else:
            self.number_of_cooling_stages = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_temperature_setpoint_base_schedule_name = None
        else:
            self.cooling_temperature_setpoint_base_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_throttling_temperature_range = None
        else:
            self.cooling_throttling_temperature_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_1_cooling_temperature_offset = None
        else:
            self.stage_1_cooling_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_2_cooling_temperature_offset = None
        else:
            self.stage_2_cooling_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_3_cooling_temperature_offset = None
        else:
            self.stage_3_cooling_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_4_cooling_temperature_offset = None
        else:
            self.stage_4_cooling_temperature_offset = vals[i]
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.name`')
        self._data["Name"] = value

    @property
    def zone_or_zonelist_name(self):
        """Get zone_or_zonelist_name

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set
        """
        return self._data["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """  Corresponds to IDD Field `Zone or ZoneList Name`

        Args:
            value (str): value for IDD Field `Zone or ZoneList Name`
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.zone_or_zonelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.zone_or_zonelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.zone_or_zonelist_name`')
        self._data["Zone or ZoneList Name"] = value

    @property
    def number_of_heating_stages(self):
        """Get number_of_heating_stages

        Returns:
            int: the value of `number_of_heating_stages` or None if not set
        """
        return self._data["Number of Heating Stages"]

    @number_of_heating_stages.setter
    def number_of_heating_stages(self, value=None):
        """  Corresponds to IDD Field `Number of Heating Stages`
        Enter the number of the following sets of data for heating temperature offset

        Args:
            value (int): value for IDD Field `Number of Heating Stages`
                value >= 1
                value <= 4
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
                                     'for field `ZoneControlThermostatStagedDualSetpoint.number_of_heating_stages`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ZoneControlThermostatStagedDualSetpoint.number_of_heating_stages`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.number_of_heating_stages`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.number_of_heating_stages`')
        self._data["Number of Heating Stages"] = value

    @property
    def heating_temperature_setpoint_schedule_name(self):
        """Get heating_temperature_setpoint_schedule_name

        Returns:
            str: the value of `heating_temperature_setpoint_schedule_name` or None if not set
        """
        return self._data["Heating Temperature Setpoint Schedule Name"]

    @heating_temperature_setpoint_schedule_name.setter
    def heating_temperature_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Temperature Setpoint Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Temperature Setpoint Schedule Name`
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.heating_temperature_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.heating_temperature_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.heating_temperature_setpoint_schedule_name`')
        self._data["Heating Temperature Setpoint Schedule Name"] = value

    @property
    def heating_throttling_temperature_range(self):
        """Get heating_throttling_temperature_range

        Returns:
            float: the value of `heating_throttling_temperature_range` or None if not set
        """
        return self._data["Heating Throttling Temperature Range"]

    @heating_throttling_temperature_range.setter
    def heating_throttling_temperature_range(self, value=1.1):
        """  Corresponds to IDD Field `Heating Throttling Temperature Range`

        Args:
            value (float): value for IDD Field `Heating Throttling Temperature Range`
                Units: deltaC
                Default value: 1.1
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.heating_throttling_temperature_range`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.heating_throttling_temperature_range`')
        self._data["Heating Throttling Temperature Range"] = value

    @property
    def stage_1_heating_temperature_offset(self):
        """Get stage_1_heating_temperature_offset

        Returns:
            float: the value of `stage_1_heating_temperature_offset` or None if not set
        """
        return self._data["Stage 1 Heating Temperature Offset"]

    @stage_1_heating_temperature_offset.setter
    def stage_1_heating_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `Stage 1 Heating Temperature Offset`
        The heating temperature offset is used to determine heating stage number for
        multi stage equipment.
        When the temperature difference of the heating setpoint and the controlled zone
        temperature at previous time step is less than Stage 1 value and greater than
        Stage 2 value, the stage number is 1.

        Args:
            value (float): value for IDD Field `Stage 1 Heating Temperature Offset`
                Units: deltaC
                value <= 0.0
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.stage_1_heating_temperature_offset`'.format(value))
            if value > 0.0:
                raise ValueError('value need to be smaller 0.0 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.stage_1_heating_temperature_offset`')
        self._data["Stage 1 Heating Temperature Offset"] = value

    @property
    def stage_2_heating_temperature_offset(self):
        """Get stage_2_heating_temperature_offset

        Returns:
            float: the value of `stage_2_heating_temperature_offset` or None if not set
        """
        return self._data["Stage 2 Heating Temperature Offset"]

    @stage_2_heating_temperature_offset.setter
    def stage_2_heating_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `Stage 2 Heating Temperature Offset`
        The heating temperature offset is used to determine heating stage number for
        multi stage equipment.
        When the temperature difference of the heating setpoint and the controlled zone
        temperature at previous time step is less than Stage 2 value and greater than
        Stage 3 value, the stage number is 2.
        The value of this field has to be less the value at the previous field.

        Args:
            value (float): value for IDD Field `Stage 2 Heating Temperature Offset`
                Units: deltaC
                value <= 0.0
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.stage_2_heating_temperature_offset`'.format(value))
            if value > 0.0:
                raise ValueError('value need to be smaller 0.0 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.stage_2_heating_temperature_offset`')
        self._data["Stage 2 Heating Temperature Offset"] = value

    @property
    def stage_3_heating_temperature_offset(self):
        """Get stage_3_heating_temperature_offset

        Returns:
            float: the value of `stage_3_heating_temperature_offset` or None if not set
        """
        return self._data["Stage 3 Heating Temperature Offset"]

    @stage_3_heating_temperature_offset.setter
    def stage_3_heating_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `Stage 3 Heating Temperature Offset`
        The heating temperature offset is used to determine heating stage number for
        multi stage equipment.
        When the temperature difference of the heating setpoint and the controlled zone
        temperature at previous time step is less than Stage 3 value and greater than
        Stage 4 value, the stage number is 3.
        The value of this field has to be less the value at the previous field.

        Args:
            value (float): value for IDD Field `Stage 3 Heating Temperature Offset`
                Units: deltaC
                value <= 0.0
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.stage_3_heating_temperature_offset`'.format(value))
            if value > 0.0:
                raise ValueError('value need to be smaller 0.0 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.stage_3_heating_temperature_offset`')
        self._data["Stage 3 Heating Temperature Offset"] = value

    @property
    def stage_4_heating_temperature_offset(self):
        """Get stage_4_heating_temperature_offset

        Returns:
            float: the value of `stage_4_heating_temperature_offset` or None if not set
        """
        return self._data["Stage 4 Heating Temperature Offset"]

    @stage_4_heating_temperature_offset.setter
    def stage_4_heating_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `Stage 4 Heating Temperature Offset`
        The heating temperature offset is used to determine heating stage number for
        multi stage equipment.
        When the temperature difference of the heating setpoint and the controlled zone
        temperature at previous time step is less than Stage 4 value, the stage number is 4.
        The value of this field has to be less the value at the previous field.

        Args:
            value (float): value for IDD Field `Stage 4 Heating Temperature Offset`
                Units: deltaC
                value <= 0.0
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.stage_4_heating_temperature_offset`'.format(value))
            if value > 0.0:
                raise ValueError('value need to be smaller 0.0 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.stage_4_heating_temperature_offset`')
        self._data["Stage 4 Heating Temperature Offset"] = value

    @property
    def number_of_cooling_stages(self):
        """Get number_of_cooling_stages

        Returns:
            int: the value of `number_of_cooling_stages` or None if not set
        """
        return self._data["Number of Cooling Stages"]

    @number_of_cooling_stages.setter
    def number_of_cooling_stages(self, value=None):
        """  Corresponds to IDD Field `Number of Cooling Stages`
        Enter the number of the following sets of data for cooling temperature offset

        Args:
            value (int): value for IDD Field `Number of Cooling Stages`
                value >= 1
                value <= 4
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
                                     'for field `ZoneControlThermostatStagedDualSetpoint.number_of_cooling_stages`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ZoneControlThermostatStagedDualSetpoint.number_of_cooling_stages`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.number_of_cooling_stages`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.number_of_cooling_stages`')
        self._data["Number of Cooling Stages"] = value

    @property
    def cooling_temperature_setpoint_base_schedule_name(self):
        """Get cooling_temperature_setpoint_base_schedule_name

        Returns:
            str: the value of `cooling_temperature_setpoint_base_schedule_name` or None if not set
        """
        return self._data["Cooling Temperature Setpoint Base Schedule Name"]

    @cooling_temperature_setpoint_base_schedule_name.setter
    def cooling_temperature_setpoint_base_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Temperature Setpoint Base Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Temperature Setpoint Base Schedule Name`
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.cooling_temperature_setpoint_base_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.cooling_temperature_setpoint_base_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.cooling_temperature_setpoint_base_schedule_name`')
        self._data["Cooling Temperature Setpoint Base Schedule Name"] = value

    @property
    def cooling_throttling_temperature_range(self):
        """Get cooling_throttling_temperature_range

        Returns:
            float: the value of `cooling_throttling_temperature_range` or None if not set
        """
        return self._data["Cooling Throttling Temperature Range"]

    @cooling_throttling_temperature_range.setter
    def cooling_throttling_temperature_range(self, value=1.1):
        """  Corresponds to IDD Field `Cooling Throttling Temperature Range`

        Args:
            value (float): value for IDD Field `Cooling Throttling Temperature Range`
                Units: deltaC
                Default value: 1.1
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.cooling_throttling_temperature_range`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.cooling_throttling_temperature_range`')
        self._data["Cooling Throttling Temperature Range"] = value

    @property
    def stage_1_cooling_temperature_offset(self):
        """Get stage_1_cooling_temperature_offset

        Returns:
            float: the value of `stage_1_cooling_temperature_offset` or None if not set
        """
        return self._data["Stage 1 Cooling Temperature Offset"]

    @stage_1_cooling_temperature_offset.setter
    def stage_1_cooling_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `Stage 1 Cooling Temperature Offset`
        The cooling temperature offset is used to determine cooling stage number for
        multi stage equipment.
        When the temperature difference of the cooling setpoint and the controlled zone
        temperature at previous time step is greater than Stage 1 value and less than
        Stage 2 value, the stage number is 1.

        Args:
            value (float): value for IDD Field `Stage 1 Cooling Temperature Offset`
                Units: deltaC
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.stage_1_cooling_temperature_offset`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.stage_1_cooling_temperature_offset`')
        self._data["Stage 1 Cooling Temperature Offset"] = value

    @property
    def stage_2_cooling_temperature_offset(self):
        """Get stage_2_cooling_temperature_offset

        Returns:
            float: the value of `stage_2_cooling_temperature_offset` or None if not set
        """
        return self._data["Stage 2 Cooling Temperature Offset"]

    @stage_2_cooling_temperature_offset.setter
    def stage_2_cooling_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `Stage 2 Cooling Temperature Offset`
        The cooling temperature offset is used to determine cooling stage number for
        multi stage equipment.
        When the temperature difference of the cooling setpoint and the controlled zone
        temperature at previous time step is greater than Stage 2 value and less than
        Stage 3 value, the stage number is 2.
        The value of this field has to be greater than the value at the previous field.

        Args:
            value (float): value for IDD Field `Stage 2 Cooling Temperature Offset`
                Units: deltaC
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.stage_2_cooling_temperature_offset`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.stage_2_cooling_temperature_offset`')
        self._data["Stage 2 Cooling Temperature Offset"] = value

    @property
    def stage_3_cooling_temperature_offset(self):
        """Get stage_3_cooling_temperature_offset

        Returns:
            float: the value of `stage_3_cooling_temperature_offset` or None if not set
        """
        return self._data["Stage 3 Cooling Temperature Offset"]

    @stage_3_cooling_temperature_offset.setter
    def stage_3_cooling_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `Stage 3 Cooling Temperature Offset`
        The cooling temperature offset is used to determine cooling stage number for
        multi stage equipment.
        When the temperature difference of the cooling setpoint and the controlled zone
        temperature at previous time step is greater than Stage 3 value and less than
        Stage 4 value, the stage number is 3.
        The value of this field has to be greater than the value at the previous field.

        Args:
            value (float): value for IDD Field `Stage 3 Cooling Temperature Offset`
                Units: deltaC
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.stage_3_cooling_temperature_offset`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.stage_3_cooling_temperature_offset`')
        self._data["Stage 3 Cooling Temperature Offset"] = value

    @property
    def stage_4_cooling_temperature_offset(self):
        """Get stage_4_cooling_temperature_offset

        Returns:
            float: the value of `stage_4_cooling_temperature_offset` or None if not set
        """
        return self._data["Stage 4 Cooling Temperature Offset"]

    @stage_4_cooling_temperature_offset.setter
    def stage_4_cooling_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `Stage 4 Cooling Temperature Offset`
        The cooling temperature offset is used to determine cooling stage number for
        multi stage equipment.
        When the temperature difference of the cooling setpoint and the controlled zone
        temperature at previous time step is greater than Stage 4 value, the stage number is 4.
        The value of this field has to be greater than the value at the previous field.

        Args:
            value (float): value for IDD Field `Stage 4 Cooling Temperature Offset`
                Units: deltaC
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
                                 ' for field `ZoneControlThermostatStagedDualSetpoint.stage_4_cooling_temperature_offset`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneControlThermostatStagedDualSetpoint.stage_4_cooling_temperature_offset`')
        self._data["Stage 4 Cooling Temperature Offset"] = value

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
                    raise ValueError("Required field ZoneControlThermostatStagedDualSetpoint:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneControlThermostatStagedDualSetpoint:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneControlThermostatStagedDualSetpoint: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneControlThermostatStagedDualSetpoint: {} / {}".format(out_fields,
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

class ZoneControlContaminantController(object):
    """ Corresponds to IDD object `ZoneControl:ContaminantController`
        Used to control a zone to a specified indoor level of CO2 or generic contaminants, or
        to specify minimum CO2 concentration schedule name for a zone.
    """
    internal_name = "ZoneControl:ContaminantController"
    field_count = 7
    required_fields = ["Name", "Controlled Zone Name"]
    extensible_fields = 0
    format = None
    min_fields = 4
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:ContaminantController`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Controlled Zone Name"] = None
        self._data["Carbon Dioxide Control Availability Schedule Name"] = None
        self._data["Carbon Dioxide Setpoint Schedule Name"] = None
        self._data["Minimum Carbon Dioxide Concentration Schedule Name"] = None
        self._data["Generic Contaminant Control Availability Schedule Name"] = None
        self._data["Generic Contaminant Setpoint Schedule Name"] = None
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
            self.controlled_zone_name = None
        else:
            self.controlled_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.carbon_dioxide_control_availability_schedule_name = None
        else:
            self.carbon_dioxide_control_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.carbon_dioxide_setpoint_schedule_name = None
        else:
            self.carbon_dioxide_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_carbon_dioxide_concentration_schedule_name = None
        else:
            self.minimum_carbon_dioxide_concentration_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.generic_contaminant_control_availability_schedule_name = None
        else:
            self.generic_contaminant_control_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.generic_contaminant_setpoint_schedule_name = None
        else:
            self.generic_contaminant_setpoint_schedule_name = vals[i]
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
                                 ' for field `ZoneControlContaminantController.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlContaminantController.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlContaminantController.name`')
        self._data["Name"] = value

    @property
    def controlled_zone_name(self):
        """Get controlled_zone_name

        Returns:
            str: the value of `controlled_zone_name` or None if not set
        """
        return self._data["Controlled Zone Name"]

    @controlled_zone_name.setter
    def controlled_zone_name(self, value=None):
        """  Corresponds to IDD Field `Controlled Zone Name`

        Args:
            value (str): value for IDD Field `Controlled Zone Name`
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
                                 ' for field `ZoneControlContaminantController.controlled_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlContaminantController.controlled_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlContaminantController.controlled_zone_name`')
        self._data["Controlled Zone Name"] = value

    @property
    def carbon_dioxide_control_availability_schedule_name(self):
        """Get carbon_dioxide_control_availability_schedule_name

        Returns:
            str: the value of `carbon_dioxide_control_availability_schedule_name` or None if not set
        """
        return self._data["Carbon Dioxide Control Availability Schedule Name"]

    @carbon_dioxide_control_availability_schedule_name.setter
    def carbon_dioxide_control_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Carbon Dioxide Control Availability Schedule Name`
        Availability schedule name for CO2 controller. Schedule value > 0 means the CO2
        controller is enabled. If this field is blank, then CO2  controller is always enabled.

        Args:
            value (str): value for IDD Field `Carbon Dioxide Control Availability Schedule Name`
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
                                 ' for field `ZoneControlContaminantController.carbon_dioxide_control_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlContaminantController.carbon_dioxide_control_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlContaminantController.carbon_dioxide_control_availability_schedule_name`')
        self._data["Carbon Dioxide Control Availability Schedule Name"] = value

    @property
    def carbon_dioxide_setpoint_schedule_name(self):
        """Get carbon_dioxide_setpoint_schedule_name

        Returns:
            str: the value of `carbon_dioxide_setpoint_schedule_name` or None if not set
        """
        return self._data["Carbon Dioxide Setpoint Schedule Name"]

    @carbon_dioxide_setpoint_schedule_name.setter
    def carbon_dioxide_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Carbon Dioxide Setpoint Schedule Name`
        Schedule values should be carbon dioxide concentration in parts per million (ppm)

        Args:
            value (str): value for IDD Field `Carbon Dioxide Setpoint Schedule Name`
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
                                 ' for field `ZoneControlContaminantController.carbon_dioxide_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlContaminantController.carbon_dioxide_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlContaminantController.carbon_dioxide_setpoint_schedule_name`')
        self._data["Carbon Dioxide Setpoint Schedule Name"] = value

    @property
    def minimum_carbon_dioxide_concentration_schedule_name(self):
        """Get minimum_carbon_dioxide_concentration_schedule_name

        Returns:
            str: the value of `minimum_carbon_dioxide_concentration_schedule_name` or None if not set
        """
        return self._data["Minimum Carbon Dioxide Concentration Schedule Name"]

    @minimum_carbon_dioxide_concentration_schedule_name.setter
    def minimum_carbon_dioxide_concentration_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Carbon Dioxide Concentration Schedule Name`
        Schedule values should be carbon dioxide concentration in parts per
        million (ppm)
        This field is used when the field System Outdoor Air Method =
        ProportionalControl in Controller:MechanicalVentilation

        Args:
            value (str): value for IDD Field `Minimum Carbon Dioxide Concentration Schedule Name`
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
                                 ' for field `ZoneControlContaminantController.minimum_carbon_dioxide_concentration_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlContaminantController.minimum_carbon_dioxide_concentration_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlContaminantController.minimum_carbon_dioxide_concentration_schedule_name`')
        self._data["Minimum Carbon Dioxide Concentration Schedule Name"] = value

    @property
    def generic_contaminant_control_availability_schedule_name(self):
        """Get generic_contaminant_control_availability_schedule_name

        Returns:
            str: the value of `generic_contaminant_control_availability_schedule_name` or None if not set
        """
        return self._data["Generic Contaminant Control Availability Schedule Name"]

    @generic_contaminant_control_availability_schedule_name.setter
    def generic_contaminant_control_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Generic Contaminant Control Availability Schedule Name`
        Availability schedule name for generic contaminant controller. Schedule value > 0 means
        the generic contaminant controller is enabled. If this field is blank, then generic
        contaminant controller is always enabled.

        Args:
            value (str): value for IDD Field `Generic Contaminant Control Availability Schedule Name`
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
                                 ' for field `ZoneControlContaminantController.generic_contaminant_control_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlContaminantController.generic_contaminant_control_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlContaminantController.generic_contaminant_control_availability_schedule_name`')
        self._data["Generic Contaminant Control Availability Schedule Name"] = value

    @property
    def generic_contaminant_setpoint_schedule_name(self):
        """Get generic_contaminant_setpoint_schedule_name

        Returns:
            str: the value of `generic_contaminant_setpoint_schedule_name` or None if not set
        """
        return self._data["Generic Contaminant Setpoint Schedule Name"]

    @generic_contaminant_setpoint_schedule_name.setter
    def generic_contaminant_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Generic Contaminant Setpoint Schedule Name`
        Schedule values should be generic contaminant concentration in parts per
        million (ppm)
        This field is used when the field System Outdoor Air Method =
        IndoorAirQualityProcedureGenericContaminant in Controller:MechanicalVentilation

        Args:
            value (str): value for IDD Field `Generic Contaminant Setpoint Schedule Name`
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
                                 ' for field `ZoneControlContaminantController.generic_contaminant_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneControlContaminantController.generic_contaminant_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneControlContaminantController.generic_contaminant_setpoint_schedule_name`')
        self._data["Generic Contaminant Setpoint Schedule Name"] = value

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
                    raise ValueError("Required field ZoneControlContaminantController:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneControlContaminantController:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneControlContaminantController: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneControlContaminantController: {} / {}".format(out_fields,
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