from collections import OrderedDict

class ThermostatSetpointSingleHeating(object):
    """ Corresponds to IDD object `ThermostatSetpoint:SingleHeating`
        Used for a heating only thermostat. The setpoint can be scheduled and varied throughout
        the simulation but only heating is allowed with this control type.
    """
    internal_name = "ThermostatSetpoint:SingleHeating"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermostatSetpoint:SingleHeating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Setpoint Temperature Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.setpoint_temperature_schedule_name))
        return ",".join(out)

class ThermostatSetpointSingleCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:SingleCooling`
        Used for a cooling only thermostat. The setpoint can be scheduled and varied throughout
        the simulation but only cooling is allowed.
    """
    internal_name = "ThermostatSetpoint:SingleCooling"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermostatSetpoint:SingleCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Setpoint Temperature Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.setpoint_temperature_schedule_name))
        return ",".join(out)

class ThermostatSetpointSingleHeatingOrCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:SingleHeatingOrCooling`
        Used for a heating and cooling thermostat with a single setpoint. The setpoint can be
        scheduled and varied throughout the simulation for both heating and cooling.
    """
    internal_name = "ThermostatSetpoint:SingleHeatingOrCooling"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermostatSetpoint:SingleHeatingOrCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Setpoint Temperature Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.setpoint_temperature_schedule_name))
        return ",".join(out)

class ThermostatSetpointDualSetpoint(object):
    """ Corresponds to IDD object `ThermostatSetpoint:DualSetpoint`
        Used for a heating and cooling thermostat with dual setpoints. The setpoints can be
        scheduled and varied throughout the simulation for both heating and cooling.
    """
    internal_name = "ThermostatSetpoint:DualSetpoint"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermostatSetpoint:DualSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Heating Setpoint Temperature Schedule Name"] = None
        self._data["Cooling Setpoint Temperature Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_setpoint_temperature_schedule_name = None
        else:
            self.heating_setpoint_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_setpoint_temperature_schedule_name = None
        else:
            self.cooling_setpoint_temperature_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `heating_setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `heating_setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_setpoint_temperature_schedule_name`')

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
        """  Corresponds to IDD Field `cooling_setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `cooling_setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_setpoint_temperature_schedule_name`')

        self._data["Cooling Setpoint Temperature Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.heating_setpoint_temperature_schedule_name))
        out.append(self._to_str(self.cooling_setpoint_temperature_schedule_name))
        return ",".join(out)

class ThermostatSetpointThermalComfortFangerSingleHeating(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating`
        Used for heating only thermal comfort control. The PMV setpoint can be scheduled and
        varied throughout the simulation but only heating is allowed with this control type.
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fanger_thermal_comfort_schedule_name = None
        else:
            self.fanger_thermal_comfort_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `fanger_thermal_comfort_schedule_name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `fanger_thermal_comfort_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fanger_thermal_comfort_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fanger_thermal_comfort_schedule_name`')

        self._data["Fanger Thermal Comfort Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.fanger_thermal_comfort_schedule_name))
        return ",".join(out)

class ThermostatSetpointThermalComfortFangerSingleCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling`
        Used for cooling only thermal comfort control. The PMV setpoint can be scheduled and
        varied throughout the simulation but only cooling is allowed with this control type.
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fanger_thermal_comfort_schedule_name = None
        else:
            self.fanger_thermal_comfort_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `fanger_thermal_comfort_schedule_name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `fanger_thermal_comfort_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fanger_thermal_comfort_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fanger_thermal_comfort_schedule_name`')

        self._data["Fanger Thermal Comfort Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.fanger_thermal_comfort_schedule_name))
        return ",".join(out)

class ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling`
        Used for heating and cooling thermal comfort control with a single setpoint. The PMV
        setpoint can be scheduled and varied throughout the simulation for both heating and
        cooling.
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fanger_thermal_comfort_schedule_name = None
        else:
            self.fanger_thermal_comfort_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `fanger_thermal_comfort_schedule_name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `fanger_thermal_comfort_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fanger_thermal_comfort_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fanger_thermal_comfort_schedule_name`')

        self._data["Fanger Thermal Comfort Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.fanger_thermal_comfort_schedule_name))
        return ",".join(out)

class ThermostatSetpointThermalComfortFangerDualSetpoint(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint`
        Used for heating and cooling thermal comfort control with dual setpoints. The PMV
        setpoints can be scheduled and varied throughout the simulation for both heating and
        cooling.
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Heating Schedule Name"] = None
        self._data["Fanger Thermal Comfort Cooling Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fanger_thermal_comfort_heating_schedule_name = None
        else:
            self.fanger_thermal_comfort_heating_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fanger_thermal_comfort_cooling_schedule_name = None
        else:
            self.fanger_thermal_comfort_cooling_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `fanger_thermal_comfort_heating_schedule_name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `fanger_thermal_comfort_heating_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fanger_thermal_comfort_heating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fanger_thermal_comfort_heating_schedule_name`')

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
        """  Corresponds to IDD Field `fanger_thermal_comfort_cooling_schedule_name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `fanger_thermal_comfort_cooling_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fanger_thermal_comfort_cooling_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fanger_thermal_comfort_cooling_schedule_name`')

        self._data["Fanger Thermal Comfort Cooling Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.fanger_thermal_comfort_heating_schedule_name))
        out.append(self._to_str(self.fanger_thermal_comfort_cooling_schedule_name))
        return ",".join(out)