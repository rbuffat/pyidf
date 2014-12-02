from collections import OrderedDict
import logging
import re

class SetpointManagerScheduled(object):
    """ Corresponds to IDD object `SetpointManager:Scheduled`
        The simplest Setpoint Manager simply uses a schedule to determine one
        or more setpoints. Values of the nodes are not used as input.
    """
    internal_name = "SetpointManager:Scheduled"
    field_count = 4
    required_fields = ["Name", "Control Variable", "Schedule Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:Scheduled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Schedule Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value=None):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                      - MaximumTemperature
                      - MinimumTemperature
                      - HumidityRatio
                      - MaximumHumidityRatio
                      - MinimumHumidityRatio
                      - MassFlowRate
                      - MaximumMassFlowRate
                      - MinimumMassFlowRate
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
            vals["maximumtemperature"] = "MaximumTemperature"
            vals["minimumtemperature"] = "MinimumTemperature"
            vals["humidityratio"] = "HumidityRatio"
            vals["maximumhumidityratio"] = "MaximumHumidityRatio"
            vals["minimumhumidityratio"] = "MinimumHumidityRatio"
            vals["massflowrate"] = "MassFlowRate"
            vals["maximummassflowrate"] = "MaximumMassFlowRate"
            vals["minimummassflowrate"] = "MinimumMassFlowRate"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Name`

        Args:
            value (str): value for IDD Field `Schedule Name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `schedule_name`')
        self._data["Schedule Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerScheduledDualSetpoint(object):
    """ Corresponds to IDD object `SetpointManager:Scheduled:DualSetpoint`
        This setpoint manager places a high and low schedule value
        on one or more nodes.
    """
    internal_name = "SetpointManager:Scheduled:DualSetpoint"
    field_count = 5
    required_fields = ["Name", "High Setpoint Schedule Name", "Low Setpoint Schedule Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:Scheduled:DualSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["High Setpoint Schedule Name"] = None
        self._data["Low Setpoint Schedule Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_setpoint_schedule_name = None
        else:
            self.high_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_setpoint_schedule_name = None
        else:
            self.low_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def high_setpoint_schedule_name(self):
        """Get high_setpoint_schedule_name

        Returns:
            str: the value of `high_setpoint_schedule_name` or None if not set
        """
        return self._data["High Setpoint Schedule Name"]

    @high_setpoint_schedule_name.setter
    def high_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `High Setpoint Schedule Name`

        Args:
            value (str): value for IDD Field `High Setpoint Schedule Name`
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
                                 'for field `high_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `high_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `high_setpoint_schedule_name`')
        self._data["High Setpoint Schedule Name"] = value

    @property
    def low_setpoint_schedule_name(self):
        """Get low_setpoint_schedule_name

        Returns:
            str: the value of `low_setpoint_schedule_name` or None if not set
        """
        return self._data["Low Setpoint Schedule Name"]

    @low_setpoint_schedule_name.setter
    def low_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Low Setpoint Schedule Name`

        Args:
            value (str): value for IDD Field `Low Setpoint Schedule Name`
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
                                 'for field `low_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `low_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `low_setpoint_schedule_name`')
        self._data["Low Setpoint Schedule Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerOutdoorAirReset(object):
    """ Corresponds to IDD object `SetpointManager:OutdoorAirReset`
        The Outdoor Air Reset Setpoint Manager sets the supply air
        temperature according to the outdoor air temperature using a reset rule.
    """
    internal_name = "SetpointManager:OutdoorAirReset"
    field_count = 12
    required_fields = ["Name", "Setpoint at Outdoor Low Temperature", "Outdoor Low Temperature", "Setpoint at Outdoor High Temperature", "Outdoor High Temperature", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:OutdoorAirReset`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Setpoint at Outdoor Low Temperature"] = None
        self._data["Outdoor Low Temperature"] = None
        self._data["Setpoint at Outdoor High Temperature"] = None
        self._data["Outdoor High Temperature"] = None
        self._data["Setpoint Node or NodeList Name"] = None
        self._data["Schedule Name"] = None
        self._data["Setpoint at Outdoor Low Temperature 2"] = None
        self._data["Outdoor Low Temperature 2"] = None
        self._data["Setpoint at Outdoor High Temperature 2"] = None
        self._data["Outdoor High Temperature 2"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_at_outdoor_low_temperature = None
        else:
            self.setpoint_at_outdoor_low_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_low_temperature = None
        else:
            self.outdoor_low_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_at_outdoor_high_temperature = None
        else:
            self.setpoint_at_outdoor_high_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_high_temperature = None
        else:
            self.outdoor_high_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_at_outdoor_low_temperature_2 = None
        else:
            self.setpoint_at_outdoor_low_temperature_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_low_temperature_2 = None
        else:
            self.outdoor_low_temperature_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_at_outdoor_high_temperature_2 = None
        else:
            self.setpoint_at_outdoor_high_temperature_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_high_temperature_2 = None
        else:
            self.outdoor_high_temperature_2 = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def setpoint_at_outdoor_low_temperature(self):
        """Get setpoint_at_outdoor_low_temperature

        Returns:
            float: the value of `setpoint_at_outdoor_low_temperature` or None if not set
        """
        return self._data["Setpoint at Outdoor Low Temperature"]

    @setpoint_at_outdoor_low_temperature.setter
    def setpoint_at_outdoor_low_temperature(self, value=None):
        """  Corresponds to IDD Field `Setpoint at Outdoor Low Temperature`

        Args:
            value (float): value for IDD Field `Setpoint at Outdoor Low Temperature`
                Units: C
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
                                 'for field `setpoint_at_outdoor_low_temperature`'.format(value))
        self._data["Setpoint at Outdoor Low Temperature"] = value

    @property
    def outdoor_low_temperature(self):
        """Get outdoor_low_temperature

        Returns:
            float: the value of `outdoor_low_temperature` or None if not set
        """
        return self._data["Outdoor Low Temperature"]

    @outdoor_low_temperature.setter
    def outdoor_low_temperature(self, value=None):
        """  Corresponds to IDD Field `Outdoor Low Temperature`

        Args:
            value (float): value for IDD Field `Outdoor Low Temperature`
                Units: C
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
                                 'for field `outdoor_low_temperature`'.format(value))
        self._data["Outdoor Low Temperature"] = value

    @property
    def setpoint_at_outdoor_high_temperature(self):
        """Get setpoint_at_outdoor_high_temperature

        Returns:
            float: the value of `setpoint_at_outdoor_high_temperature` or None if not set
        """
        return self._data["Setpoint at Outdoor High Temperature"]

    @setpoint_at_outdoor_high_temperature.setter
    def setpoint_at_outdoor_high_temperature(self, value=None):
        """  Corresponds to IDD Field `Setpoint at Outdoor High Temperature`

        Args:
            value (float): value for IDD Field `Setpoint at Outdoor High Temperature`
                Units: C
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
                                 'for field `setpoint_at_outdoor_high_temperature`'.format(value))
        self._data["Setpoint at Outdoor High Temperature"] = value

    @property
    def outdoor_high_temperature(self):
        """Get outdoor_high_temperature

        Returns:
            float: the value of `outdoor_high_temperature` or None if not set
        """
        return self._data["Outdoor High Temperature"]

    @outdoor_high_temperature.setter
    def outdoor_high_temperature(self, value=None):
        """  Corresponds to IDD Field `Outdoor High Temperature`

        Args:
            value (float): value for IDD Field `Outdoor High Temperature`
                Units: C
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
                                 'for field `outdoor_high_temperature`'.format(value))
        self._data["Outdoor High Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Name`
        Optional input.
        Schedule allows scheduling of the outdoor air reset rule - a schedule value
        of 1 means use the first rule; a value of 2 means use the second rule.

        Args:
            value (str): value for IDD Field `Schedule Name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `schedule_name`')
        self._data["Schedule Name"] = value

    @property
    def setpoint_at_outdoor_low_temperature_2(self):
        """Get setpoint_at_outdoor_low_temperature_2

        Returns:
            float: the value of `setpoint_at_outdoor_low_temperature_2` or None if not set
        """
        return self._data["Setpoint at Outdoor Low Temperature 2"]

    @setpoint_at_outdoor_low_temperature_2.setter
    def setpoint_at_outdoor_low_temperature_2(self, value=None):
        """  Corresponds to IDD Field `Setpoint at Outdoor Low Temperature 2`
        2nd outdoor air temperature reset rule

        Args:
            value (float): value for IDD Field `Setpoint at Outdoor Low Temperature 2`
                Units: C
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
                                 'for field `setpoint_at_outdoor_low_temperature_2`'.format(value))
        self._data["Setpoint at Outdoor Low Temperature 2"] = value

    @property
    def outdoor_low_temperature_2(self):
        """Get outdoor_low_temperature_2

        Returns:
            float: the value of `outdoor_low_temperature_2` or None if not set
        """
        return self._data["Outdoor Low Temperature 2"]

    @outdoor_low_temperature_2.setter
    def outdoor_low_temperature_2(self, value=None):
        """  Corresponds to IDD Field `Outdoor Low Temperature 2`
        2nd outdoor air temperature reset rule

        Args:
            value (float): value for IDD Field `Outdoor Low Temperature 2`
                Units: C
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
                                 'for field `outdoor_low_temperature_2`'.format(value))
        self._data["Outdoor Low Temperature 2"] = value

    @property
    def setpoint_at_outdoor_high_temperature_2(self):
        """Get setpoint_at_outdoor_high_temperature_2

        Returns:
            float: the value of `setpoint_at_outdoor_high_temperature_2` or None if not set
        """
        return self._data["Setpoint at Outdoor High Temperature 2"]

    @setpoint_at_outdoor_high_temperature_2.setter
    def setpoint_at_outdoor_high_temperature_2(self, value=None):
        """  Corresponds to IDD Field `Setpoint at Outdoor High Temperature 2`
        2nd outdoor air temperature reset rule

        Args:
            value (float): value for IDD Field `Setpoint at Outdoor High Temperature 2`
                Units: C
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
                                 'for field `setpoint_at_outdoor_high_temperature_2`'.format(value))
        self._data["Setpoint at Outdoor High Temperature 2"] = value

    @property
    def outdoor_high_temperature_2(self):
        """Get outdoor_high_temperature_2

        Returns:
            float: the value of `outdoor_high_temperature_2` or None if not set
        """
        return self._data["Outdoor High Temperature 2"]

    @outdoor_high_temperature_2.setter
    def outdoor_high_temperature_2(self, value=None):
        """  Corresponds to IDD Field `Outdoor High Temperature 2`
        2nd outdoor air temperature reset rule

        Args:
            value (float): value for IDD Field `Outdoor High Temperature 2`
                Units: C
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
                                 'for field `outdoor_high_temperature_2`'.format(value))
        self._data["Outdoor High Temperature 2"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerSingleZoneReheat(object):
    """ Corresponds to IDD object `SetpointManager:SingleZone:Reheat`
        This setpoint manager detects the control zone load, zone inlet node flow rate, and
        zone node temperature and calculates a setpoint temperature for the supply air that
        will satisfy the zone load (heating or cooling) for the control zone. This setpoint
        manager is not limited to reheat applications.
    """
    internal_name = "SetpointManager:SingleZone:Reheat"
    field_count = 8
    required_fields = ["Name", "Control Zone Name", "Zone Node Name", "Zone Inlet Node Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:SingleZone:Reheat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Minimum Supply Air Temperature"] = None
        self._data["Maximum Supply Air Temperature"] = None
        self._data["Control Zone Name"] = None
        self._data["Zone Node Name"] = None
        self._data["Zone Inlet Node Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_supply_air_temperature = None
        else:
            self.minimum_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature = None
        else:
            self.maximum_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_zone_name = None
        else:
            self.control_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_node_name = None
        else:
            self.zone_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_inlet_node_name = None
        else:
            self.zone_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def minimum_supply_air_temperature(self):
        """Get minimum_supply_air_temperature

        Returns:
            float: the value of `minimum_supply_air_temperature` or None if not set
        """
        return self._data["Minimum Supply Air Temperature"]

    @minimum_supply_air_temperature.setter
    def minimum_supply_air_temperature(self, value=-99.0):
        """  Corresponds to IDD Field `Minimum Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Minimum Supply Air Temperature`
                Units: C
                Default value: -99.0
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
                                 'for field `minimum_supply_air_temperature`'.format(value))
        self._data["Minimum Supply Air Temperature"] = value

    @property
    def maximum_supply_air_temperature(self):
        """Get maximum_supply_air_temperature

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set
        """
        return self._data["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=99.0):
        """  Corresponds to IDD Field `Maximum Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Maximum Supply Air Temperature`
                Units: C
                Default value: 99.0
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
                                 'for field `maximum_supply_air_temperature`'.format(value))
        self._data["Maximum Supply Air Temperature"] = value

    @property
    def control_zone_name(self):
        """Get control_zone_name

        Returns:
            str: the value of `control_zone_name` or None if not set
        """
        return self._data["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """  Corresponds to IDD Field `Control Zone Name`

        Args:
            value (str): value for IDD Field `Control Zone Name`
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
                                 'for field `control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_zone_name`')
        self._data["Control Zone Name"] = value

    @property
    def zone_node_name(self):
        """Get zone_node_name

        Returns:
            str: the value of `zone_node_name` or None if not set
        """
        return self._data["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Node Name`

        Args:
            value (str): value for IDD Field `Zone Node Name`
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
                                 'for field `zone_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_node_name`')
        self._data["Zone Node Name"] = value

    @property
    def zone_inlet_node_name(self):
        """Get zone_inlet_node_name

        Returns:
            str: the value of `zone_inlet_node_name` or None if not set
        """
        return self._data["Zone Inlet Node Name"]

    @zone_inlet_node_name.setter
    def zone_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Inlet Node Name`

        Args:
            value (str): value for IDD Field `Zone Inlet Node Name`
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
                                 'for field `zone_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_inlet_node_name`')
        self._data["Zone Inlet Node Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerSingleZoneHeating(object):
    """ Corresponds to IDD object `SetpointManager:SingleZone:Heating`
        This setpoint manager detects the control zone load to meet the current heating
        setpoint, zone inlet node flow rate, and zone node temperature, and calculates a
        setpoint temperature for the supply air that will satisfy the zone heating load for
        the control zone.
    """
    internal_name = "SetpointManager:SingleZone:Heating"
    field_count = 8
    required_fields = ["Name", "Control Zone Name", "Zone Node Name", "Zone Inlet Node Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:SingleZone:Heating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Minimum Supply Air Temperature"] = None
        self._data["Maximum Supply Air Temperature"] = None
        self._data["Control Zone Name"] = None
        self._data["Zone Node Name"] = None
        self._data["Zone Inlet Node Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_supply_air_temperature = None
        else:
            self.minimum_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature = None
        else:
            self.maximum_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_zone_name = None
        else:
            self.control_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_node_name = None
        else:
            self.zone_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_inlet_node_name = None
        else:
            self.zone_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def minimum_supply_air_temperature(self):
        """Get minimum_supply_air_temperature

        Returns:
            float: the value of `minimum_supply_air_temperature` or None if not set
        """
        return self._data["Minimum Supply Air Temperature"]

    @minimum_supply_air_temperature.setter
    def minimum_supply_air_temperature(self, value=-99.0):
        """  Corresponds to IDD Field `Minimum Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Minimum Supply Air Temperature`
                Units: C
                Default value: -99.0
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
                                 'for field `minimum_supply_air_temperature`'.format(value))
        self._data["Minimum Supply Air Temperature"] = value

    @property
    def maximum_supply_air_temperature(self):
        """Get maximum_supply_air_temperature

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set
        """
        return self._data["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=99.0):
        """  Corresponds to IDD Field `Maximum Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Maximum Supply Air Temperature`
                Units: C
                Default value: 99.0
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
                                 'for field `maximum_supply_air_temperature`'.format(value))
        self._data["Maximum Supply Air Temperature"] = value

    @property
    def control_zone_name(self):
        """Get control_zone_name

        Returns:
            str: the value of `control_zone_name` or None if not set
        """
        return self._data["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """  Corresponds to IDD Field `Control Zone Name`

        Args:
            value (str): value for IDD Field `Control Zone Name`
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
                                 'for field `control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_zone_name`')
        self._data["Control Zone Name"] = value

    @property
    def zone_node_name(self):
        """Get zone_node_name

        Returns:
            str: the value of `zone_node_name` or None if not set
        """
        return self._data["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Node Name`

        Args:
            value (str): value for IDD Field `Zone Node Name`
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
                                 'for field `zone_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_node_name`')
        self._data["Zone Node Name"] = value

    @property
    def zone_inlet_node_name(self):
        """Get zone_inlet_node_name

        Returns:
            str: the value of `zone_inlet_node_name` or None if not set
        """
        return self._data["Zone Inlet Node Name"]

    @zone_inlet_node_name.setter
    def zone_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Inlet Node Name`

        Args:
            value (str): value for IDD Field `Zone Inlet Node Name`
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
                                 'for field `zone_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_inlet_node_name`')
        self._data["Zone Inlet Node Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerSingleZoneCooling(object):
    """ Corresponds to IDD object `SetpointManager:SingleZone:Cooling`
        This setpoint manager detects the control zone load to meet the current cooling
        setpoint, zone inlet node flow rate, and zone node temperature, and calculates a
        setpoint temperature for the supply air that will satisfy the zone cooling load for
        the control zone.
    """
    internal_name = "SetpointManager:SingleZone:Cooling"
    field_count = 8
    required_fields = ["Name", "Control Zone Name", "Zone Node Name", "Zone Inlet Node Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:SingleZone:Cooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Minimum Supply Air Temperature"] = None
        self._data["Maximum Supply Air Temperature"] = None
        self._data["Control Zone Name"] = None
        self._data["Zone Node Name"] = None
        self._data["Zone Inlet Node Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_supply_air_temperature = None
        else:
            self.minimum_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature = None
        else:
            self.maximum_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_zone_name = None
        else:
            self.control_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_node_name = None
        else:
            self.zone_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_inlet_node_name = None
        else:
            self.zone_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def minimum_supply_air_temperature(self):
        """Get minimum_supply_air_temperature

        Returns:
            float: the value of `minimum_supply_air_temperature` or None if not set
        """
        return self._data["Minimum Supply Air Temperature"]

    @minimum_supply_air_temperature.setter
    def minimum_supply_air_temperature(self, value=-99.0):
        """  Corresponds to IDD Field `Minimum Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Minimum Supply Air Temperature`
                Units: C
                Default value: -99.0
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
                                 'for field `minimum_supply_air_temperature`'.format(value))
        self._data["Minimum Supply Air Temperature"] = value

    @property
    def maximum_supply_air_temperature(self):
        """Get maximum_supply_air_temperature

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set
        """
        return self._data["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=99.0):
        """  Corresponds to IDD Field `Maximum Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Maximum Supply Air Temperature`
                Units: C
                Default value: 99.0
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
                                 'for field `maximum_supply_air_temperature`'.format(value))
        self._data["Maximum Supply Air Temperature"] = value

    @property
    def control_zone_name(self):
        """Get control_zone_name

        Returns:
            str: the value of `control_zone_name` or None if not set
        """
        return self._data["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """  Corresponds to IDD Field `Control Zone Name`

        Args:
            value (str): value for IDD Field `Control Zone Name`
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
                                 'for field `control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_zone_name`')
        self._data["Control Zone Name"] = value

    @property
    def zone_node_name(self):
        """Get zone_node_name

        Returns:
            str: the value of `zone_node_name` or None if not set
        """
        return self._data["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Node Name`

        Args:
            value (str): value for IDD Field `Zone Node Name`
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
                                 'for field `zone_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_node_name`')
        self._data["Zone Node Name"] = value

    @property
    def zone_inlet_node_name(self):
        """Get zone_inlet_node_name

        Returns:
            str: the value of `zone_inlet_node_name` or None if not set
        """
        return self._data["Zone Inlet Node Name"]

    @zone_inlet_node_name.setter
    def zone_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Inlet Node Name`

        Args:
            value (str): value for IDD Field `Zone Inlet Node Name`
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
                                 'for field `zone_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_inlet_node_name`')
        self._data["Zone Inlet Node Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerSingleZoneHumidityMinimum(object):
    """ Corresponds to IDD object `SetpointManager:SingleZone:Humidity:Minimum`
        The Single Zone Minimum Humidity Setpoint Manager allows the
        control of a single zone minimum humidity level.
        This setpoint manager can be used in conjunction with
        object ZoneControl:Humidistat to detect humidity levels.
    """
    internal_name = "SetpointManager:SingleZone:Humidity:Minimum"
    field_count = 5
    required_fields = ["Name", "Setpoint Node or NodeList Name", "Control Zone Air Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:SingleZone:Humidity:Minimum`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Schedule Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
        self._data["Control Zone Air Node Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_zone_air_node_name = None
        else:
            self.control_zone_air_node_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value=None):
        """  Corresponds to IDD Field `Control Variable`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Control Variable`
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
        self._data["Control Variable"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Schedule Name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `schedule_name`')
        self._data["Schedule Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which humidity ratio setpoint will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    @property
    def control_zone_air_node_name(self):
        """Get control_zone_air_node_name

        Returns:
            str: the value of `control_zone_air_node_name` or None if not set
        """
        return self._data["Control Zone Air Node Name"]

    @control_zone_air_node_name.setter
    def control_zone_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Control Zone Air Node Name`
        Name of the zone air node for the humidity control zone

        Args:
            value (str): value for IDD Field `Control Zone Air Node Name`
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
                                 'for field `control_zone_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_zone_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_zone_air_node_name`')
        self._data["Control Zone Air Node Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerSingleZoneHumidityMaximum(object):
    """ Corresponds to IDD object `SetpointManager:SingleZone:Humidity:Maximum`
        The Single Zone Maximum Humidity Setpoint Manager allows the
        control of a single zone maximum humidity level.
        This setpoint manager can be used in conjunction with
        object ZoneControl:Humidistat to detect humidity levels.
    """
    internal_name = "SetpointManager:SingleZone:Humidity:Maximum"
    field_count = 5
    required_fields = ["Name", "Setpoint Node or NodeList Name", "Control Zone Air Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:SingleZone:Humidity:Maximum`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Schedule Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
        self._data["Control Zone Air Node Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_zone_air_node_name = None
        else:
            self.control_zone_air_node_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value=None):
        """  Corresponds to IDD Field `Control Variable`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Control Variable`
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
        self._data["Control Variable"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Schedule Name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `schedule_name`')
        self._data["Schedule Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which humidity ratio setpoint will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    @property
    def control_zone_air_node_name(self):
        """Get control_zone_air_node_name

        Returns:
            str: the value of `control_zone_air_node_name` or None if not set
        """
        return self._data["Control Zone Air Node Name"]

    @control_zone_air_node_name.setter
    def control_zone_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Control Zone Air Node Name`
        Name of the zone air node for the humidity control zone

        Args:
            value (str): value for IDD Field `Control Zone Air Node Name`
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
                                 'for field `control_zone_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_zone_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_zone_air_node_name`')
        self._data["Control Zone Air Node Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerMixedAir(object):
    """ Corresponds to IDD object `SetpointManager:MixedAir`
        The Mixed Air Setpoint Manager is meant to be used in conjunction
        with a Controller:OutdoorAir object. This setpoint manager is used
        to establish a temperature setpoint at the mixed air node.
    """
    internal_name = "SetpointManager:MixedAir"
    field_count = 6
    required_fields = ["Name", "Reference Setpoint Node Name", "Fan Inlet Node Name", "Fan Outlet Node Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:MixedAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Reference Setpoint Node Name"] = None
        self._data["Fan Inlet Node Name"] = None
        self._data["Fan Outlet Node Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_setpoint_node_name = None
        else:
            self.reference_setpoint_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_inlet_node_name = None
        else:
            self.fan_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_outlet_node_name = None
        else:
            self.fan_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def reference_setpoint_node_name(self):
        """Get reference_setpoint_node_name

        Returns:
            str: the value of `reference_setpoint_node_name` or None if not set
        """
        return self._data["Reference Setpoint Node Name"]

    @reference_setpoint_node_name.setter
    def reference_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `Reference Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Reference Setpoint Node Name`
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
                                 'for field `reference_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_setpoint_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_setpoint_node_name`')
        self._data["Reference Setpoint Node Name"] = value

    @property
    def fan_inlet_node_name(self):
        """Get fan_inlet_node_name

        Returns:
            str: the value of `fan_inlet_node_name` or None if not set
        """
        return self._data["Fan Inlet Node Name"]

    @fan_inlet_node_name.setter
    def fan_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fan Inlet Node Name`

        Args:
            value (str): value for IDD Field `Fan Inlet Node Name`
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
                                 'for field `fan_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_inlet_node_name`')
        self._data["Fan Inlet Node Name"] = value

    @property
    def fan_outlet_node_name(self):
        """Get fan_outlet_node_name

        Returns:
            str: the value of `fan_outlet_node_name` or None if not set
        """
        return self._data["Fan Outlet Node Name"]

    @fan_outlet_node_name.setter
    def fan_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fan Outlet Node Name`

        Args:
            value (str): value for IDD Field `Fan Outlet Node Name`
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
                                 'for field `fan_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_outlet_node_name`')
        self._data["Fan Outlet Node Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerOutdoorAirPretreat(object):
    """ Corresponds to IDD object `SetpointManager:OutdoorAirPretreat`
        This setpoint manager determines the required
        conditions at the outdoor air stream node which will
        produce the reference setpoint condition at the
        mixed air node when mixed with the return air stream
    """
    internal_name = "SetpointManager:OutdoorAirPretreat"
    field_count = 11
    required_fields = ["Name", "Mixed Air Stream Node Name", "Outdoor Air Stream Node Name", "Return Air Stream Node Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:OutdoorAirPretreat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Minimum Setpoint Temperature"] = None
        self._data["Maximum Setpoint Temperature"] = None
        self._data["Minimum Setpoint Humidity Ratio"] = None
        self._data["Maximum Setpoint Humidity Ratio"] = None
        self._data["Reference Setpoint Node Name"] = None
        self._data["Mixed Air Stream Node Name"] = None
        self._data["Outdoor Air Stream Node Name"] = None
        self._data["Return Air Stream Node Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_temperature = None
        else:
            self.minimum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_temperature = None
        else:
            self.maximum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_humidity_ratio = None
        else:
            self.minimum_setpoint_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_humidity_ratio = None
        else:
            self.maximum_setpoint_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_setpoint_node_name = None
        else:
            self.reference_setpoint_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_air_stream_node_name = None
        else:
            self.mixed_air_stream_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_stream_node_name = None
        else:
            self.outdoor_air_stream_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.return_air_stream_node_name = None
        else:
            self.return_air_stream_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value=None):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                      - HumidityRatio
                      - MaximumHumidityRatio
                      - MinimumHumidityRatio
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
            vals["humidityratio"] = "HumidityRatio"
            vals["maximumhumidityratio"] = "MaximumHumidityRatio"
            vals["minimumhumidityratio"] = "MinimumHumidityRatio"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def minimum_setpoint_temperature(self):
        """Get minimum_setpoint_temperature

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set
        """
        return self._data["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=-99.0):
        """  Corresponds to IDD Field `Minimum Setpoint Temperature`
        Applicable only if Control variable is Temperature

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`
                Units: C
                Default value: -99.0
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
                                 'for field `minimum_setpoint_temperature`'.format(value))
        self._data["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """Get maximum_setpoint_temperature

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set
        """
        return self._data["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=99.0):
        """  Corresponds to IDD Field `Maximum Setpoint Temperature`
        Applicable only if Control variable is Temperature

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`
                Units: C
                Default value: 99.0
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
                                 'for field `maximum_setpoint_temperature`'.format(value))
        self._data["Maximum Setpoint Temperature"] = value

    @property
    def minimum_setpoint_humidity_ratio(self):
        """Get minimum_setpoint_humidity_ratio

        Returns:
            float: the value of `minimum_setpoint_humidity_ratio` or None if not set
        """
        return self._data["Minimum Setpoint Humidity Ratio"]

    @minimum_setpoint_humidity_ratio.setter
    def minimum_setpoint_humidity_ratio(self, value=1e-05):
        """  Corresponds to IDD Field `Minimum Setpoint Humidity Ratio`
        Applicable only if Control variable is
        MaximumHumidityRatio, MinimumHumidityRatio, or HumidityRatio - then minimum is 0.00001

        Args:
            value (float): value for IDD Field `Minimum Setpoint Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 1e-05
                value <= 1.0
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
                                 'for field `minimum_setpoint_humidity_ratio`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_setpoint_humidity_ratio`')
        self._data["Minimum Setpoint Humidity Ratio"] = value

    @property
    def maximum_setpoint_humidity_ratio(self):
        """Get maximum_setpoint_humidity_ratio

        Returns:
            float: the value of `maximum_setpoint_humidity_ratio` or None if not set
        """
        return self._data["Maximum Setpoint Humidity Ratio"]

    @maximum_setpoint_humidity_ratio.setter
    def maximum_setpoint_humidity_ratio(self, value=1.0):
        """  Corresponds to IDD Field `Maximum Setpoint Humidity Ratio`
        Applicable only if Control variable is
        MaximumHumidityRatio, MinimumHumidityRatio, or HumidityRatio - then minimum is 0.00001

        Args:
            value (float): value for IDD Field `Maximum Setpoint Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 1.0
                value <= 1.0
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
                                 'for field `maximum_setpoint_humidity_ratio`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_setpoint_humidity_ratio`')
        self._data["Maximum Setpoint Humidity Ratio"] = value

    @property
    def reference_setpoint_node_name(self):
        """Get reference_setpoint_node_name

        Returns:
            str: the value of `reference_setpoint_node_name` or None if not set
        """
        return self._data["Reference Setpoint Node Name"]

    @reference_setpoint_node_name.setter
    def reference_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `Reference Setpoint Node Name`
        The current setpoint at this node is the
        desired condition for the Mixed Air Node
        This node must have a valid setpoint
        which has been set by another setpoint manager

        Args:
            value (str): value for IDD Field `Reference Setpoint Node Name`
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
                                 'for field `reference_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_setpoint_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_setpoint_node_name`')
        self._data["Reference Setpoint Node Name"] = value

    @property
    def mixed_air_stream_node_name(self):
        """Get mixed_air_stream_node_name

        Returns:
            str: the value of `mixed_air_stream_node_name` or None if not set
        """
        return self._data["Mixed Air Stream Node Name"]

    @mixed_air_stream_node_name.setter
    def mixed_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Air Stream Node Name`
        Name of Mixed Air Node

        Args:
            value (str): value for IDD Field `Mixed Air Stream Node Name`
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
                                 'for field `mixed_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_air_stream_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `mixed_air_stream_node_name`')
        self._data["Mixed Air Stream Node Name"] = value

    @property
    def outdoor_air_stream_node_name(self):
        """Get outdoor_air_stream_node_name

        Returns:
            str: the value of `outdoor_air_stream_node_name` or None if not set
        """
        return self._data["Outdoor Air Stream Node Name"]

    @outdoor_air_stream_node_name.setter
    def outdoor_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Stream Node Name`
        Name of Outdoor Air Stream Node

        Args:
            value (str): value for IDD Field `Outdoor Air Stream Node Name`
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
                                 'for field `outdoor_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_stream_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_stream_node_name`')
        self._data["Outdoor Air Stream Node Name"] = value

    @property
    def return_air_stream_node_name(self):
        """Get return_air_stream_node_name

        Returns:
            str: the value of `return_air_stream_node_name` or None if not set
        """
        return self._data["Return Air Stream Node Name"]

    @return_air_stream_node_name.setter
    def return_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `Return Air Stream Node Name`
        Name of Return Air Stream Node

        Args:
            value (str): value for IDD Field `Return Air Stream Node Name`
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
                                 'for field `return_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `return_air_stream_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `return_air_stream_node_name`')
        self._data["Return Air Stream Node Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature or humidity
        ratio will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerWarmest(object):
    """ Corresponds to IDD object `SetpointManager:Warmest`
        This SetpointManager resets the cooling supply air temperature
        of a central forced air HVAC system according to the
        cooling demand of the warmest zone.
    """
    internal_name = "SetpointManager:Warmest"
    field_count = 7
    required_fields = ["Name", "HVAC Air Loop Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:Warmest`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Minimum Setpoint Temperature"] = None
        self._data["Maximum Setpoint Temperature"] = None
        self._data["Strategy"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_temperature = None
        else:
            self.minimum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_temperature = None
        else:
            self.maximum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.strategy = None
        else:
            self.strategy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `HVAC Air Loop Name`
        Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hvac_air_loop_name`')
        self._data["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_temperature(self):
        """Get minimum_setpoint_temperature

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set
        """
        return self._data["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=12.0):
        """  Corresponds to IDD Field `Minimum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`
                Units: C
                Default value: 12.0
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
                                 'for field `minimum_setpoint_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_setpoint_temperature`')
        self._data["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """Get maximum_setpoint_temperature

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set
        """
        return self._data["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=18.0):
        """  Corresponds to IDD Field `Maximum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`
                Units: C
                Default value: 18.0
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
                                 'for field `maximum_setpoint_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_setpoint_temperature`')
        self._data["Maximum Setpoint Temperature"] = value

    @property
    def strategy(self):
        """Get strategy

        Returns:
            str: the value of `strategy` or None if not set
        """
        return self._data["Strategy"]

    @strategy.setter
    def strategy(self, value="MaximumTemperature"):
        """  Corresponds to IDD Field `Strategy`

        Args:
            value (str): value for IDD Field `Strategy`
                Accepted values are:
                      - MaximumTemperature
                Default value: MaximumTemperature
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
                                 'for field `strategy`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `strategy`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `strategy`')
            vals = {}
            vals["maximumtemperature"] = "MaximumTemperature"
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
                                     'field `strategy`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `strategy`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Strategy"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerColdest(object):
    """ Corresponds to IDD object `SetpointManager:Coldest`
        This SetpointManager is used in dual duct systems to reset
        the setpoint temperature of the air in the heating supply duct.
        Usually it is used in conjunction with a SetpointManager:Warmest
        resetting the temperature of the air in the cooling supply duct.
    """
    internal_name = "SetpointManager:Coldest"
    field_count = 7
    required_fields = ["Name", "HVAC Air Loop Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:Coldest`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Minimum Setpoint Temperature"] = None
        self._data["Maximum Setpoint Temperature"] = None
        self._data["Strategy"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_temperature = None
        else:
            self.minimum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_temperature = None
        else:
            self.maximum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.strategy = None
        else:
            self.strategy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `HVAC Air Loop Name`
        Enter the name of an AirLoopHVAC object.

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hvac_air_loop_name`')
        self._data["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_temperature(self):
        """Get minimum_setpoint_temperature

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set
        """
        return self._data["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=20.0):
        """  Corresponds to IDD Field `Minimum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`
                Units: C
                Default value: 20.0
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
                                 'for field `minimum_setpoint_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_setpoint_temperature`')
        self._data["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """Get maximum_setpoint_temperature

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set
        """
        return self._data["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=50.0):
        """  Corresponds to IDD Field `Maximum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`
                Units: C
                Default value: 50.0
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
                                 'for field `maximum_setpoint_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_setpoint_temperature`')
        self._data["Maximum Setpoint Temperature"] = value

    @property
    def strategy(self):
        """Get strategy

        Returns:
            str: the value of `strategy` or None if not set
        """
        return self._data["Strategy"]

    @strategy.setter
    def strategy(self, value="MinimumTemperature"):
        """  Corresponds to IDD Field `Strategy`

        Args:
            value (str): value for IDD Field `Strategy`
                Accepted values are:
                      - MinimumTemperature
                Default value: MinimumTemperature
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
                                 'for field `strategy`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `strategy`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `strategy`')
            vals = {}
            vals["minimumtemperature"] = "MinimumTemperature"
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
                                     'field `strategy`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `strategy`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Strategy"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerReturnAirBypassFlow(object):
    """ Corresponds to IDD object `SetpointManager:ReturnAirBypassFlow`
        This setpoint manager determines the required
        mass flow rate through a return air bypass duct
        to meet the specified temperature setpoint
    """
    internal_name = "SetpointManager:ReturnAirBypassFlow"
    field_count = 4
    required_fields = ["Name", "HVAC Air Loop Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:ReturnAirBypassFlow`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Temperature Setpoint Schedule Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_setpoint_schedule_name = None
        else:
            self.temperature_setpoint_schedule_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Flow"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Flow
                Default value: Flow
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["flow"] = "Flow"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `HVAC Air Loop Name`
        Enter the name of an AirLoopHVAC object.

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hvac_air_loop_name`')
        self._data["HVAC Air Loop Name"] = value

    @property
    def temperature_setpoint_schedule_name(self):
        """Get temperature_setpoint_schedule_name

        Returns:
            str: the value of `temperature_setpoint_schedule_name` or None if not set
        """
        return self._data["Temperature Setpoint Schedule Name"]

    @temperature_setpoint_schedule_name.setter
    def temperature_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Temperature Setpoint Schedule Name`

        Args:
            value (str): value for IDD Field `Temperature Setpoint Schedule Name`
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
                                 'for field `temperature_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `temperature_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `temperature_setpoint_schedule_name`')
        self._data["Temperature Setpoint Schedule Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerWarmestTemperatureFlow(object):
    """ Corresponds to IDD object `SetpointManager:WarmestTemperatureFlow`
        This setpoint manager sets both the supply air temperature
        and the supply air flow rate.
    """
    internal_name = "SetpointManager:WarmestTemperatureFlow"
    field_count = 8
    required_fields = ["Name", "HVAC Air Loop Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:WarmestTemperatureFlow`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Minimum Setpoint Temperature"] = None
        self._data["Maximum Setpoint Temperature"] = None
        self._data["Strategy"] = None
        self._data["Setpoint Node or NodeList Name"] = None
        self._data["Minimum Turndown Ratio"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_temperature = None
        else:
            self.minimum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_temperature = None
        else:
            self.maximum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.strategy = None
        else:
            self.strategy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_turndown_ratio = None
        else:
            self.minimum_turndown_ratio = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value=None):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `HVAC Air Loop Name`
        Enter the name of an AirLoopHVAC object.

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hvac_air_loop_name`')
        self._data["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_temperature(self):
        """Get minimum_setpoint_temperature

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set
        """
        return self._data["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=12.0):
        """  Corresponds to IDD Field `Minimum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`
                Units: C
                Default value: 12.0
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
                                 'for field `minimum_setpoint_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_setpoint_temperature`')
        self._data["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """Get maximum_setpoint_temperature

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set
        """
        return self._data["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=18.0):
        """  Corresponds to IDD Field `Maximum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`
                Units: C
                Default value: 18.0
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
                                 'for field `maximum_setpoint_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_setpoint_temperature`')
        self._data["Maximum Setpoint Temperature"] = value

    @property
    def strategy(self):
        """Get strategy

        Returns:
            str: the value of `strategy` or None if not set
        """
        return self._data["Strategy"]

    @strategy.setter
    def strategy(self, value="TemperatureFirst"):
        """  Corresponds to IDD Field `Strategy`
        For TemperatureFirst the manager tries to find the highest setpoint temperature
        that will satisfy all the zone cooling loads at minimum supply air flow rate.
        If this setpoint temperature is less than the minimum, the setpoint temperature is set
        to the minimum, and the supply air flow rate is increased to meet the loads.
        For FlowFirst the manager tries to find the lowest supply air flow rate
        that will satisfy all the zone cooling loads at the maximum setpoint temperature.
        If this flow is greater than the maximum, the flow is set to the maximum and the
        setpoint temperature is reduced to satisfy the cooling loads.

        Args:
            value (str): value for IDD Field `Strategy`
                Accepted values are:
                      - TemperatureFirst
                      - FlowFirst
                Default value: TemperatureFirst
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
                                 'for field `strategy`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `strategy`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `strategy`')
            vals = {}
            vals["temperaturefirst"] = "TemperatureFirst"
            vals["flowfirst"] = "FlowFirst"
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
                                     'field `strategy`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `strategy`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Strategy"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    @property
    def minimum_turndown_ratio(self):
        """Get minimum_turndown_ratio

        Returns:
            float: the value of `minimum_turndown_ratio` or None if not set
        """
        return self._data["Minimum Turndown Ratio"]

    @minimum_turndown_ratio.setter
    def minimum_turndown_ratio(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Turndown Ratio`
        Fraction of the maximum supply air flow rate.
        Used to define the minimum supply flow for the TemperatureFirst strategy.

        Args:
            value (float): value for IDD Field `Minimum Turndown Ratio`
                Units: dimensionless
                Default value: 0.2
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
                                 'for field `minimum_turndown_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_turndown_ratio`')
        self._data["Minimum Turndown Ratio"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerMultiZoneHeatingAverage(object):
    """ Corresponds to IDD object `SetpointManager:MultiZone:Heating:Average`
        This setpoint manager sets the average supply air temperature based on the heating load
        requirements of all controlled zones in an air loop served by a central air-conditioner.
    """
    internal_name = "SetpointManager:MultiZone:Heating:Average"
    field_count = 5
    required_fields = ["Name", "HVAC Air Loop Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:MultiZone:Heating:Average`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Minimum Setpoint Temperature"] = None
        self._data["Maximum Setpoint Temperature"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_temperature = None
        else:
            self.minimum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_temperature = None
        else:
            self.maximum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `HVAC Air Loop Name`
        Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hvac_air_loop_name`')
        self._data["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_temperature(self):
        """Get minimum_setpoint_temperature

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set
        """
        return self._data["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=20.0):
        """  Corresponds to IDD Field `Minimum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`
                Units: C
                Default value: 20.0
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
                                 'for field `minimum_setpoint_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_setpoint_temperature`')
        self._data["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """Get maximum_setpoint_temperature

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set
        """
        return self._data["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=50.0):
        """  Corresponds to IDD Field `Maximum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`
                Units: C
                Default value: 50.0
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
                                 'for field `maximum_setpoint_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_setpoint_temperature`')
        self._data["Maximum Setpoint Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerMultiZoneCoolingAverage(object):
    """ Corresponds to IDD object `SetpointManager:MultiZone:Cooling:Average`
        This setpoint manager sets the average supply air temperature based on the cooling load
        requirements of all controlled zones in an air loop served by a central air-conditioner.
    """
    internal_name = "SetpointManager:MultiZone:Cooling:Average"
    field_count = 5
    required_fields = ["Name", "HVAC Air Loop Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:MultiZone:Cooling:Average`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Minimum Setpoint Temperature"] = None
        self._data["Maximum Setpoint Temperature"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_temperature = None
        else:
            self.minimum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_temperature = None
        else:
            self.maximum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `HVAC Air Loop Name`
        Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hvac_air_loop_name`')
        self._data["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_temperature(self):
        """Get minimum_setpoint_temperature

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set
        """
        return self._data["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=12.0):
        """  Corresponds to IDD Field `Minimum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`
                Units: C
                Default value: 12.0
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
                                 'for field `minimum_setpoint_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_setpoint_temperature`')
        self._data["Minimum Setpoint Temperature"] = value

    @property
    def maximum_setpoint_temperature(self):
        """Get maximum_setpoint_temperature

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set
        """
        return self._data["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=18.0):
        """  Corresponds to IDD Field `Maximum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`
                Units: C
                Default value: 18.0
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
                                 'for field `maximum_setpoint_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_setpoint_temperature`')
        self._data["Maximum Setpoint Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerMultiZoneMinimumHumidityAverage(object):
    """ Corresponds to IDD object `SetpointManager:MultiZone:MinimumHumidity:Average`
        This setpoint manager sets the average supply air minimum humidity ratio based on moisture
        load requirements of all controlled zones in an air loop served by a central air-conditioner.
    """
    internal_name = "SetpointManager:MultiZone:MinimumHumidity:Average"
    field_count = 5
    required_fields = ["Name", "HVAC Air Loop Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:MultiZone:MinimumHumidity:Average`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Minimum Setpoint Humidity Ratio"] = None
        self._data["Maximum Setpoint Humidity Ratio"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_humidity_ratio = None
        else:
            self.minimum_setpoint_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_humidity_ratio = None
        else:
            self.maximum_setpoint_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `HVAC Air Loop Name`
        Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hvac_air_loop_name`')
        self._data["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_humidity_ratio(self):
        """Get minimum_setpoint_humidity_ratio

        Returns:
            float: the value of `minimum_setpoint_humidity_ratio` or None if not set
        """
        return self._data["Minimum Setpoint Humidity Ratio"]

    @minimum_setpoint_humidity_ratio.setter
    def minimum_setpoint_humidity_ratio(self, value=0.005):
        """  Corresponds to IDD Field `Minimum Setpoint Humidity Ratio`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.005
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
                                 'for field `minimum_setpoint_humidity_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_setpoint_humidity_ratio`')
        self._data["Minimum Setpoint Humidity Ratio"] = value

    @property
    def maximum_setpoint_humidity_ratio(self):
        """Get maximum_setpoint_humidity_ratio

        Returns:
            float: the value of `maximum_setpoint_humidity_ratio` or None if not set
        """
        return self._data["Maximum Setpoint Humidity Ratio"]

    @maximum_setpoint_humidity_ratio.setter
    def maximum_setpoint_humidity_ratio(self, value=0.012):
        """  Corresponds to IDD Field `Maximum Setpoint Humidity Ratio`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.012
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
                                 'for field `maximum_setpoint_humidity_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_setpoint_humidity_ratio`')
        self._data["Maximum Setpoint Humidity Ratio"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the humidity ratio will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerMultiZoneMaximumHumidityAverage(object):
    """ Corresponds to IDD object `SetpointManager:MultiZone:MaximumHumidity:Average`
        This setpoint manager sets the average supply air maximum humidity ratio based on moisture
        load requirements of all controlled zones in an air loop served by a central air-conditioner.
    """
    internal_name = "SetpointManager:MultiZone:MaximumHumidity:Average"
    field_count = 5
    required_fields = ["Name", "HVAC Air Loop Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:MultiZone:MaximumHumidity:Average`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Minimum Setpoint Humidity Ratio"] = None
        self._data["Maximum Setpoint Humidity Ratio"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_humidity_ratio = None
        else:
            self.minimum_setpoint_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_humidity_ratio = None
        else:
            self.maximum_setpoint_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `HVAC Air Loop Name`
        Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hvac_air_loop_name`')
        self._data["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_humidity_ratio(self):
        """Get minimum_setpoint_humidity_ratio

        Returns:
            float: the value of `minimum_setpoint_humidity_ratio` or None if not set
        """
        return self._data["Minimum Setpoint Humidity Ratio"]

    @minimum_setpoint_humidity_ratio.setter
    def minimum_setpoint_humidity_ratio(self, value=0.008):
        """  Corresponds to IDD Field `Minimum Setpoint Humidity Ratio`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.008
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
                                 'for field `minimum_setpoint_humidity_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_setpoint_humidity_ratio`')
        self._data["Minimum Setpoint Humidity Ratio"] = value

    @property
    def maximum_setpoint_humidity_ratio(self):
        """Get maximum_setpoint_humidity_ratio

        Returns:
            float: the value of `maximum_setpoint_humidity_ratio` or None if not set
        """
        return self._data["Maximum Setpoint Humidity Ratio"]

    @maximum_setpoint_humidity_ratio.setter
    def maximum_setpoint_humidity_ratio(self, value=0.015):
        """  Corresponds to IDD Field `Maximum Setpoint Humidity Ratio`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.015
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
                                 'for field `maximum_setpoint_humidity_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_setpoint_humidity_ratio`')
        self._data["Maximum Setpoint Humidity Ratio"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the humidity ratio will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerMultiZoneHumidityMinimum(object):
    """ Corresponds to IDD object `SetpointManager:MultiZone:Humidity:Minimum`
        This setpoint manager sets the minimum supply air humidity ratio based on humidification
        requirements of a controlled zone with critical humidity ratio setpoint (i.e., a zone with
        the highest humidity ratio setpoint) in an air loop served by a central air-conditioner.
    """
    internal_name = "SetpointManager:MultiZone:Humidity:Minimum"
    field_count = 5
    required_fields = ["Name", "HVAC Air Loop Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:MultiZone:Humidity:Minimum`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Minimum Setpoint Humidity Ratio"] = None
        self._data["Maximum Setpoint Humidity Ratio"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_humidity_ratio = None
        else:
            self.minimum_setpoint_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_humidity_ratio = None
        else:
            self.maximum_setpoint_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `HVAC Air Loop Name`
        Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hvac_air_loop_name`')
        self._data["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_humidity_ratio(self):
        """Get minimum_setpoint_humidity_ratio

        Returns:
            float: the value of `minimum_setpoint_humidity_ratio` or None if not set
        """
        return self._data["Minimum Setpoint Humidity Ratio"]

    @minimum_setpoint_humidity_ratio.setter
    def minimum_setpoint_humidity_ratio(self, value=0.005):
        """  Corresponds to IDD Field `Minimum Setpoint Humidity Ratio`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.005
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
                                 'for field `minimum_setpoint_humidity_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_setpoint_humidity_ratio`')
        self._data["Minimum Setpoint Humidity Ratio"] = value

    @property
    def maximum_setpoint_humidity_ratio(self):
        """Get maximum_setpoint_humidity_ratio

        Returns:
            float: the value of `maximum_setpoint_humidity_ratio` or None if not set
        """
        return self._data["Maximum Setpoint Humidity Ratio"]

    @maximum_setpoint_humidity_ratio.setter
    def maximum_setpoint_humidity_ratio(self, value=0.012):
        """  Corresponds to IDD Field `Maximum Setpoint Humidity Ratio`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.012
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
                                 'for field `maximum_setpoint_humidity_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_setpoint_humidity_ratio`')
        self._data["Maximum Setpoint Humidity Ratio"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the humidity ratio will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerMultiZoneHumidityMaximum(object):
    """ Corresponds to IDD object `SetpointManager:MultiZone:Humidity:Maximum`
        This setpoint manager sets the maximum supply air humidity ratio based on dehumidification
        requirements of a controlled zone with critical humidity ratio setpoint (i.e., a zone with
        the lowest humidity ratio setpoint) in an air loop served by a central air-conditioner.
    """
    internal_name = "SetpointManager:MultiZone:Humidity:Maximum"
    field_count = 5
    required_fields = ["Name", "HVAC Air Loop Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:MultiZone:Humidity:Maximum`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["HVAC Air Loop Name"] = None
        self._data["Minimum Setpoint Humidity Ratio"] = None
        self._data["Maximum Setpoint Humidity Ratio"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.hvac_air_loop_name = None
        else:
            self.hvac_air_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_humidity_ratio = None
        else:
            self.minimum_setpoint_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_humidity_ratio = None
        else:
            self.maximum_setpoint_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def hvac_air_loop_name(self):
        """Get hvac_air_loop_name

        Returns:
            str: the value of `hvac_air_loop_name` or None if not set
        """
        return self._data["HVAC Air Loop Name"]

    @hvac_air_loop_name.setter
    def hvac_air_loop_name(self, value=None):
        """  Corresponds to IDD Field `HVAC Air Loop Name`
        Enter the name of an AirLoopHVAC object

        Args:
            value (str): value for IDD Field `HVAC Air Loop Name`
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
                                 'for field `hvac_air_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hvac_air_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hvac_air_loop_name`')
        self._data["HVAC Air Loop Name"] = value

    @property
    def minimum_setpoint_humidity_ratio(self):
        """Get minimum_setpoint_humidity_ratio

        Returns:
            float: the value of `minimum_setpoint_humidity_ratio` or None if not set
        """
        return self._data["Minimum Setpoint Humidity Ratio"]

    @minimum_setpoint_humidity_ratio.setter
    def minimum_setpoint_humidity_ratio(self, value=0.008):
        """  Corresponds to IDD Field `Minimum Setpoint Humidity Ratio`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.008
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
                                 'for field `minimum_setpoint_humidity_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_setpoint_humidity_ratio`')
        self._data["Minimum Setpoint Humidity Ratio"] = value

    @property
    def maximum_setpoint_humidity_ratio(self):
        """Get maximum_setpoint_humidity_ratio

        Returns:
            float: the value of `maximum_setpoint_humidity_ratio` or None if not set
        """
        return self._data["Maximum Setpoint Humidity Ratio"]

    @maximum_setpoint_humidity_ratio.setter
    def maximum_setpoint_humidity_ratio(self, value=0.015):
        """  Corresponds to IDD Field `Maximum Setpoint Humidity Ratio`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.015
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
                                 'for field `maximum_setpoint_humidity_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_setpoint_humidity_ratio`')
        self._data["Maximum Setpoint Humidity Ratio"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the humidity ratio will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerFollowOutdoorAirTemperature(object):
    """ Corresponds to IDD object `SetpointManager:FollowOutdoorAirTemperature`
        This setpoint manager is used to place a temperature setpoint on a system node
        that is derived from the current outdoor air environmental conditions.
        The outdoor air conditions are obtained from the weather information during the simulation.
    """
    internal_name = "SetpointManager:FollowOutdoorAirTemperature"
    field_count = 7
    required_fields = ["Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:FollowOutdoorAirTemperature`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Reference Temperature Type"] = None
        self._data["Offset Temperature Difference"] = None
        self._data["Maximum Setpoint Temperature"] = None
        self._data["Minimum Setpoint Temperature"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_temperature_type = None
        else:
            self.reference_temperature_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.offset_temperature_difference = None
        else:
            self.offset_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_temperature = None
        else:
            self.maximum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_temperature = None
        else:
            self.minimum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                      - MinimumTemperature
                      - MaximumTemperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
            vals["minimumtemperature"] = "MinimumTemperature"
            vals["maximumtemperature"] = "MaximumTemperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def reference_temperature_type(self):
        """Get reference_temperature_type

        Returns:
            str: the value of `reference_temperature_type` or None if not set
        """
        return self._data["Reference Temperature Type"]

    @reference_temperature_type.setter
    def reference_temperature_type(self, value="OutdoorAirWetBulb"):
        """  Corresponds to IDD Field `Reference Temperature Type`

        Args:
            value (str): value for IDD Field `Reference Temperature Type`
                Accepted values are:
                      - OutdoorAirWetBulb
                      - OutdoorAirDryBulb
                Default value: OutdoorAirWetBulb
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
                                 'for field `reference_temperature_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_temperature_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_temperature_type`')
            vals = {}
            vals["outdoorairwetbulb"] = "OutdoorAirWetBulb"
            vals["outdoorairdrybulb"] = "OutdoorAirDryBulb"
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
                                     'field `reference_temperature_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `reference_temperature_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reference Temperature Type"] = value

    @property
    def offset_temperature_difference(self):
        """Get offset_temperature_difference

        Returns:
            float: the value of `offset_temperature_difference` or None if not set
        """
        return self._data["Offset Temperature Difference"]

    @offset_temperature_difference.setter
    def offset_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `Offset Temperature Difference`

        Args:
            value (float): value for IDD Field `Offset Temperature Difference`
                Units: deltaC
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
                                 'for field `offset_temperature_difference`'.format(value))
        self._data["Offset Temperature Difference"] = value

    @property
    def maximum_setpoint_temperature(self):
        """Get maximum_setpoint_temperature

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set
        """
        return self._data["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`
                Units: C
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
                                 'for field `maximum_setpoint_temperature`'.format(value))
        self._data["Maximum Setpoint Temperature"] = value

    @property
    def minimum_setpoint_temperature(self):
        """Get minimum_setpoint_temperature

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set
        """
        return self._data["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`
                Units: C
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
                                 'for field `minimum_setpoint_temperature`'.format(value))
        self._data["Minimum Setpoint Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerFollowSystemNodeTemperature(object):
    """ Corresponds to IDD object `SetpointManager:FollowSystemNodeTemperature`
        This setpoint manager is used to place a temperature setpoint on a
        system node that is derived from the current temperatures at a separate
        system node.  The current value of the temperature at a reference node
        is obtained and used to generate setpoint on a second system node.
        If the reference node is also designated to be an outdoor air (intake) node,
        then this setpoint manager can be used to follow outdoor air conditions
        that are adjusted for altitude.
    """
    internal_name = "SetpointManager:FollowSystemNodeTemperature"
    field_count = 8
    required_fields = ["Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:FollowSystemNodeTemperature`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Reference Node Name"] = None
        self._data["Reference Temperature Type"] = None
        self._data["Offset Temperature Difference"] = None
        self._data["Maximum Limit Setpoint Temperature"] = None
        self._data["Minimum Limit Setpoint Temperature"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_node_name = None
        else:
            self.reference_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_temperature_type = None
        else:
            self.reference_temperature_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.offset_temperature_difference = None
        else:
            self.offset_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_limit_setpoint_temperature = None
        else:
            self.maximum_limit_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_limit_setpoint_temperature = None
        else:
            self.minimum_limit_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                      - MinimumTemperature
                      - MaximumTemperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
            vals["minimumtemperature"] = "MinimumTemperature"
            vals["maximumtemperature"] = "MaximumTemperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def reference_node_name(self):
        """Get reference_node_name

        Returns:
            str: the value of `reference_node_name` or None if not set
        """
        return self._data["Reference Node Name"]

    @reference_node_name.setter
    def reference_node_name(self, value=None):
        """  Corresponds to IDD Field `Reference Node Name`

        Args:
            value (str): value for IDD Field `Reference Node Name`
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
                                 'for field `reference_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_node_name`')
        self._data["Reference Node Name"] = value

    @property
    def reference_temperature_type(self):
        """Get reference_temperature_type

        Returns:
            str: the value of `reference_temperature_type` or None if not set
        """
        return self._data["Reference Temperature Type"]

    @reference_temperature_type.setter
    def reference_temperature_type(self, value="NodeDryBulb"):
        """  Corresponds to IDD Field `Reference Temperature Type`

        Args:
            value (str): value for IDD Field `Reference Temperature Type`
                Accepted values are:
                      - NodeWetBulb
                      - NodeDryBulb
                Default value: NodeDryBulb
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
                                 'for field `reference_temperature_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_temperature_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_temperature_type`')
            vals = {}
            vals["nodewetbulb"] = "NodeWetBulb"
            vals["nodedrybulb"] = "NodeDryBulb"
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
                                     'field `reference_temperature_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `reference_temperature_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reference Temperature Type"] = value

    @property
    def offset_temperature_difference(self):
        """Get offset_temperature_difference

        Returns:
            float: the value of `offset_temperature_difference` or None if not set
        """
        return self._data["Offset Temperature Difference"]

    @offset_temperature_difference.setter
    def offset_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `Offset Temperature Difference`

        Args:
            value (float): value for IDD Field `Offset Temperature Difference`
                Units: deltaC
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
                                 'for field `offset_temperature_difference`'.format(value))
        self._data["Offset Temperature Difference"] = value

    @property
    def maximum_limit_setpoint_temperature(self):
        """Get maximum_limit_setpoint_temperature

        Returns:
            float: the value of `maximum_limit_setpoint_temperature` or None if not set
        """
        return self._data["Maximum Limit Setpoint Temperature"]

    @maximum_limit_setpoint_temperature.setter
    def maximum_limit_setpoint_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Limit Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Maximum Limit Setpoint Temperature`
                Units: C
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
                                 'for field `maximum_limit_setpoint_temperature`'.format(value))
        self._data["Maximum Limit Setpoint Temperature"] = value

    @property
    def minimum_limit_setpoint_temperature(self):
        """Get minimum_limit_setpoint_temperature

        Returns:
            float: the value of `minimum_limit_setpoint_temperature` or None if not set
        """
        return self._data["Minimum Limit Setpoint Temperature"]

    @minimum_limit_setpoint_temperature.setter
    def minimum_limit_setpoint_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Limit Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Minimum Limit Setpoint Temperature`
                Units: C
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
                                 'for field `minimum_limit_setpoint_temperature`'.format(value))
        self._data["Minimum Limit Setpoint Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerFollowGroundTemperature(object):
    """ Corresponds to IDD object `SetpointManager:FollowGroundTemperature`
        This setpoint manager is used to place a temperature setpoint on a
        system node that is derived from a current ground temperature.
        The ground temperatures are specified in different
        Site:GroundTemperature:* objects and used during the simulation.
        This setpoint manager is primarily intended for condenser or plant loops
        using some type of ground heat exchanger.
    """
    internal_name = "SetpointManager:FollowGroundTemperature"
    field_count = 7
    required_fields = ["Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:FollowGroundTemperature`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Reference Ground Temperature Object Type"] = None
        self._data["Offset Temperature Difference"] = None
        self._data["Maximum Setpoint Temperature"] = None
        self._data["Minimum Setpoint Temperature"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_ground_temperature_object_type = None
        else:
            self.reference_ground_temperature_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.offset_temperature_difference = None
        else:
            self.offset_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_setpoint_temperature = None
        else:
            self.maximum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_setpoint_temperature = None
        else:
            self.minimum_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                      - MinimumTemperature
                      - MaximumTemperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
            vals["minimumtemperature"] = "MinimumTemperature"
            vals["maximumtemperature"] = "MaximumTemperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def reference_ground_temperature_object_type(self):
        """Get reference_ground_temperature_object_type

        Returns:
            str: the value of `reference_ground_temperature_object_type` or None if not set
        """
        return self._data["Reference Ground Temperature Object Type"]

    @reference_ground_temperature_object_type.setter
    def reference_ground_temperature_object_type(self, value=None):
        """  Corresponds to IDD Field `Reference Ground Temperature Object Type`

        Args:
            value (str): value for IDD Field `Reference Ground Temperature Object Type`
                Accepted values are:
                      - Site:GroundTemperature:BuildingSurface
                      - Site:GroundTemperature:Shallow
                      - Site:GroundTemperature:Deep
                      - Site:GroundTemperature:FCfactorMethod
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
                                 'for field `reference_ground_temperature_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_ground_temperature_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_ground_temperature_object_type`')
            vals = {}
            vals["site:groundtemperature:buildingsurface"] = "Site:GroundTemperature:BuildingSurface"
            vals["site:groundtemperature:shallow"] = "Site:GroundTemperature:Shallow"
            vals["site:groundtemperature:deep"] = "Site:GroundTemperature:Deep"
            vals["site:groundtemperature:fcfactormethod"] = "Site:GroundTemperature:FCfactorMethod"
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
                                     'field `reference_ground_temperature_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `reference_ground_temperature_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reference Ground Temperature Object Type"] = value

    @property
    def offset_temperature_difference(self):
        """Get offset_temperature_difference

        Returns:
            float: the value of `offset_temperature_difference` or None if not set
        """
        return self._data["Offset Temperature Difference"]

    @offset_temperature_difference.setter
    def offset_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `Offset Temperature Difference`

        Args:
            value (float): value for IDD Field `Offset Temperature Difference`
                Units: deltaC
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
                                 'for field `offset_temperature_difference`'.format(value))
        self._data["Offset Temperature Difference"] = value

    @property
    def maximum_setpoint_temperature(self):
        """Get maximum_setpoint_temperature

        Returns:
            float: the value of `maximum_setpoint_temperature` or None if not set
        """
        return self._data["Maximum Setpoint Temperature"]

    @maximum_setpoint_temperature.setter
    def maximum_setpoint_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Maximum Setpoint Temperature`
                Units: C
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
                                 'for field `maximum_setpoint_temperature`'.format(value))
        self._data["Maximum Setpoint Temperature"] = value

    @property
    def minimum_setpoint_temperature(self):
        """Get minimum_setpoint_temperature

        Returns:
            float: the value of `minimum_setpoint_temperature` or None if not set
        """
        return self._data["Minimum Setpoint Temperature"]

    @minimum_setpoint_temperature.setter
    def minimum_setpoint_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Minimum Setpoint Temperature`
                Units: C
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
                                 'for field `minimum_setpoint_temperature`'.format(value))
        self._data["Minimum Setpoint Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerCondenserEnteringReset(object):
    """ Corresponds to IDD object `SetpointManager:CondenserEnteringReset`
        This setpoint manager uses one curve to determine the optimum condenser entering water temperature
        for a given timestep and two other curves to place boundary conditions on the setpoint value.
    """
    internal_name = "SetpointManager:CondenserEnteringReset"
    field_count = 10
    required_fields = ["Name", "Control Variable", "Default Condenser Entering Water Temperature Schedule Name", "Minimum Design Wetbulb Temperature Curve Name", "Minimum Outside Air Wetbulb Temperature Curve Name", "Optimized Cond Entering Water Temperature Curve Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:CondenserEnteringReset`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Default Condenser Entering Water Temperature Schedule Name"] = None
        self._data["Minimum Design Wetbulb Temperature Curve Name"] = None
        self._data["Minimum Outside Air Wetbulb Temperature Curve Name"] = None
        self._data["Optimized Cond Entering Water Temperature Curve Name"] = None
        self._data["Minimum Lift"] = None
        self._data["Maximum Condenser Entering Water Temperature"] = None
        self._data["Cooling Tower Design Inlet Air Wet-Bulb Temperature"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.default_condenser_entering_water_temperature_schedule_name = None
        else:
            self.default_condenser_entering_water_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_design_wetbulb_temperature_curve_name = None
        else:
            self.minimum_design_wetbulb_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outside_air_wetbulb_temperature_curve_name = None
        else:
            self.minimum_outside_air_wetbulb_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.optimized_cond_entering_water_temperature_curve_name = None
        else:
            self.optimized_cond_entering_water_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_lift = None
        else:
            self.minimum_lift = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_condenser_entering_water_temperature = None
        else:
            self.maximum_condenser_entering_water_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_tower_design_inlet_air_wetbulb_temperature = None
        else:
            self.cooling_tower_design_inlet_air_wetbulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def default_condenser_entering_water_temperature_schedule_name(self):
        """Get default_condenser_entering_water_temperature_schedule_name

        Returns:
            str: the value of `default_condenser_entering_water_temperature_schedule_name` or None if not set
        """
        return self._data["Default Condenser Entering Water Temperature Schedule Name"]

    @default_condenser_entering_water_temperature_schedule_name.setter
    def default_condenser_entering_water_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Default Condenser Entering Water Temperature Schedule Name`
        This scheduled setpoint value is only used in a given timestep if the
        "Optimized" Condenser Entering Temperature does not fall within the prescribed
        boundary conditions.

        Args:
            value (str): value for IDD Field `Default Condenser Entering Water Temperature Schedule Name`
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
                                 'for field `default_condenser_entering_water_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `default_condenser_entering_water_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `default_condenser_entering_water_temperature_schedule_name`')
        self._data["Default Condenser Entering Water Temperature Schedule Name"] = value

    @property
    def minimum_design_wetbulb_temperature_curve_name(self):
        """Get minimum_design_wetbulb_temperature_curve_name

        Returns:
            str: the value of `minimum_design_wetbulb_temperature_curve_name` or None if not set
        """
        return self._data["Minimum Design Wetbulb Temperature Curve Name"]

    @minimum_design_wetbulb_temperature_curve_name.setter
    def minimum_design_wetbulb_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Design Wetbulb Temperature Curve Name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `Minimum Design Wetbulb Temperature Curve Name`
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
                                 'for field `minimum_design_wetbulb_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_design_wetbulb_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_design_wetbulb_temperature_curve_name`')
        self._data["Minimum Design Wetbulb Temperature Curve Name"] = value

    @property
    def minimum_outside_air_wetbulb_temperature_curve_name(self):
        """Get minimum_outside_air_wetbulb_temperature_curve_name

        Returns:
            str: the value of `minimum_outside_air_wetbulb_temperature_curve_name` or None if not set
        """
        return self._data["Minimum Outside Air Wetbulb Temperature Curve Name"]

    @minimum_outside_air_wetbulb_temperature_curve_name.setter
    def minimum_outside_air_wetbulb_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Outside Air Wetbulb Temperature Curve Name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `Minimum Outside Air Wetbulb Temperature Curve Name`
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
                                 'for field `minimum_outside_air_wetbulb_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_outside_air_wetbulb_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_outside_air_wetbulb_temperature_curve_name`')
        self._data["Minimum Outside Air Wetbulb Temperature Curve Name"] = value

    @property
    def optimized_cond_entering_water_temperature_curve_name(self):
        """Get optimized_cond_entering_water_temperature_curve_name

        Returns:
            str: the value of `optimized_cond_entering_water_temperature_curve_name` or None if not set
        """
        return self._data["Optimized Cond Entering Water Temperature Curve Name"]

    @optimized_cond_entering_water_temperature_curve_name.setter
    def optimized_cond_entering_water_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `Optimized Cond Entering Water Temperature Curve Name`
        Table:OneIndependentVariable

        Args:
            value (str): value for IDD Field `Optimized Cond Entering Water Temperature Curve Name`
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
                                 'for field `optimized_cond_entering_water_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `optimized_cond_entering_water_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `optimized_cond_entering_water_temperature_curve_name`')
        self._data["Optimized Cond Entering Water Temperature Curve Name"] = value

    @property
    def minimum_lift(self):
        """Get minimum_lift

        Returns:
            float: the value of `minimum_lift` or None if not set
        """
        return self._data["Minimum Lift"]

    @minimum_lift.setter
    def minimum_lift(self, value=11.1):
        """  Corresponds to IDD Field `Minimum Lift`

        Args:
            value (float): value for IDD Field `Minimum Lift`
                Units: deltaC
                Default value: 11.1
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
                                 'for field `minimum_lift`'.format(value))
        self._data["Minimum Lift"] = value

    @property
    def maximum_condenser_entering_water_temperature(self):
        """Get maximum_condenser_entering_water_temperature

        Returns:
            float: the value of `maximum_condenser_entering_water_temperature` or None if not set
        """
        return self._data["Maximum Condenser Entering Water Temperature"]

    @maximum_condenser_entering_water_temperature.setter
    def maximum_condenser_entering_water_temperature(self, value=32.0):
        """  Corresponds to IDD Field `Maximum Condenser Entering Water Temperature`

        Args:
            value (float): value for IDD Field `Maximum Condenser Entering Water Temperature`
                Units: C
                Default value: 32.0
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
                                 'for field `maximum_condenser_entering_water_temperature`'.format(value))
        self._data["Maximum Condenser Entering Water Temperature"] = value

    @property
    def cooling_tower_design_inlet_air_wetbulb_temperature(self):
        """Get cooling_tower_design_inlet_air_wetbulb_temperature

        Returns:
            float: the value of `cooling_tower_design_inlet_air_wetbulb_temperature` or None if not set
        """
        return self._data["Cooling Tower Design Inlet Air Wet-Bulb Temperature"]

    @cooling_tower_design_inlet_air_wetbulb_temperature.setter
    def cooling_tower_design_inlet_air_wetbulb_temperature(self, value=25.56):
        """  Corresponds to IDD Field `Cooling Tower Design Inlet Air Wet-Bulb Temperature`

        Args:
            value (float): value for IDD Field `Cooling Tower Design Inlet Air Wet-Bulb Temperature`
                Units: C
                Default value: 25.56
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
                                 'for field `cooling_tower_design_inlet_air_wetbulb_temperature`'.format(value))
        self._data["Cooling Tower Design Inlet Air Wet-Bulb Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerCondenserEnteringResetIdeal(object):
    """ Corresponds to IDD object `SetpointManager:CondenserEnteringReset:Ideal`
        This setpoint manager determine the ideal optimum condenser entering water temperature
        setpoint for a given timestep.
    """
    internal_name = "SetpointManager:CondenserEnteringReset:Ideal"
    field_count = 5
    required_fields = ["Name", "Control Variable", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:CondenserEnteringReset:Ideal`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Minimum Lift"] = None
        self._data["Maximum Condenser Entering Water Temperature"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_lift = None
        else:
            self.minimum_lift = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_condenser_entering_water_temperature = None
        else:
            self.maximum_condenser_entering_water_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def control_variable(self):
        """Get control_variable

        Returns:
            str: the value of `control_variable` or None if not set
        """
        return self._data["Control Variable"]

    @control_variable.setter
    def control_variable(self, value="Temperature"):
        """  Corresponds to IDD Field `Control Variable`

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                Default value: Temperature
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
                                 'for field `control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
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
                                     'field `control_variable`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def minimum_lift(self):
        """Get minimum_lift

        Returns:
            float: the value of `minimum_lift` or None if not set
        """
        return self._data["Minimum Lift"]

    @minimum_lift.setter
    def minimum_lift(self, value=11.1):
        """  Corresponds to IDD Field `Minimum Lift`

        Args:
            value (float): value for IDD Field `Minimum Lift`
                Units: deltaC
                Default value: 11.1
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
                                 'for field `minimum_lift`'.format(value))
        self._data["Minimum Lift"] = value

    @property
    def maximum_condenser_entering_water_temperature(self):
        """Get maximum_condenser_entering_water_temperature

        Returns:
            float: the value of `maximum_condenser_entering_water_temperature` or None if not set
        """
        return self._data["Maximum Condenser Entering Water Temperature"]

    @maximum_condenser_entering_water_temperature.setter
    def maximum_condenser_entering_water_temperature(self, value=32.0):
        """  Corresponds to IDD Field `Maximum Condenser Entering Water Temperature`

        Args:
            value (float): value for IDD Field `Maximum Condenser Entering Water Temperature`
                Units: C
                Default value: 32.0
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
                                 'for field `maximum_condenser_entering_water_temperature`'.format(value))
        self._data["Maximum Condenser Entering Water Temperature"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which control variable will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerSingleZoneOneStageCooling(object):
    """ Corresponds to IDD object `SetpointManager:SingleZone:OneStageCooling`
        This object can be used with CoilSystem:Cooling:DX to model on/off cycling control
        of single stage air systems. Setpoints are modulated to run coil full on or full off
        depending on zone conditions. Intended for use with ZoneControl:Thermostat:StagedDualSetpoint
    """
    internal_name = "SetpointManager:SingleZone:OneStageCooling"
    field_count = 5
    required_fields = ["Name", "Cooling Stage On Supply Air Setpoint Temperature", "Cooling Stage Off Supply Air Setpoint Temperature", "Control Zone Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:SingleZone:OneStageCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Cooling Stage On Supply Air Setpoint Temperature"] = None
        self._data["Cooling Stage Off Supply Air Setpoint Temperature"] = None
        self._data["Control Zone Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.cooling_stage_on_supply_air_setpoint_temperature = None
        else:
            self.cooling_stage_on_supply_air_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_stage_off_supply_air_setpoint_temperature = None
        else:
            self.cooling_stage_off_supply_air_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_zone_name = None
        else:
            self.control_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def cooling_stage_on_supply_air_setpoint_temperature(self):
        """Get cooling_stage_on_supply_air_setpoint_temperature

        Returns:
            float: the value of `cooling_stage_on_supply_air_setpoint_temperature` or None if not set
        """
        return self._data["Cooling Stage On Supply Air Setpoint Temperature"]

    @cooling_stage_on_supply_air_setpoint_temperature.setter
    def cooling_stage_on_supply_air_setpoint_temperature(self, value=-99.0):
        """  Corresponds to IDD Field `Cooling Stage On Supply Air Setpoint Temperature`
        This is the setpoint value applied when cooling device is to cycle ON

        Args:
            value (float): value for IDD Field `Cooling Stage On Supply Air Setpoint Temperature`
                Units: C
                Default value: -99.0
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
                                 'for field `cooling_stage_on_supply_air_setpoint_temperature`'.format(value))
        self._data["Cooling Stage On Supply Air Setpoint Temperature"] = value

    @property
    def cooling_stage_off_supply_air_setpoint_temperature(self):
        """Get cooling_stage_off_supply_air_setpoint_temperature

        Returns:
            float: the value of `cooling_stage_off_supply_air_setpoint_temperature` or None if not set
        """
        return self._data["Cooling Stage Off Supply Air Setpoint Temperature"]

    @cooling_stage_off_supply_air_setpoint_temperature.setter
    def cooling_stage_off_supply_air_setpoint_temperature(self, value=99.0):
        """  Corresponds to IDD Field `Cooling Stage Off Supply Air Setpoint Temperature`
        This is the setpoint value applied when cooling device is to cycle OFF

        Args:
            value (float): value for IDD Field `Cooling Stage Off Supply Air Setpoint Temperature`
                Units: C
                Default value: 99.0
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
                                 'for field `cooling_stage_off_supply_air_setpoint_temperature`'.format(value))
        self._data["Cooling Stage Off Supply Air Setpoint Temperature"] = value

    @property
    def control_zone_name(self):
        """Get control_zone_name

        Returns:
            str: the value of `control_zone_name` or None if not set
        """
        return self._data["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """  Corresponds to IDD Field `Control Zone Name`

        Args:
            value (str): value for IDD Field `Control Zone Name`
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
                                 'for field `control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_zone_name`')
        self._data["Control Zone Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class SetpointManagerSingleZoneOneStageHeating(object):
    """ Corresponds to IDD object `SetpointManager:SingleZone:OneStageHeating`
        This object can be used with CoilSystem:Heating:DX, Coil:Heating:Gas,
        Coil:Heating:Electric to model on/off cycling control of single stage air systems.
        Setpoints are modulated to run coil full on or full off depending on zone conditions.
        Intended for use with ZoneControl:Thermostat:StagedDualSetpoint.
    """
    internal_name = "SetpointManager:SingleZone:OneStageHeating"
    field_count = 5
    required_fields = ["Name", "Heating Stage On Supply Air Setpoint Temperature", "Heating Stage Off Supply Air Setpoint Temperature", "Control Zone Name", "Setpoint Node or NodeList Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SetpointManager:SingleZone:OneStageHeating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Heating Stage On Supply Air Setpoint Temperature"] = None
        self._data["Heating Stage Off Supply Air Setpoint Temperature"] = None
        self._data["Control Zone Name"] = None
        self._data["Setpoint Node or NodeList Name"] = None
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
            self.heating_stage_on_supply_air_setpoint_temperature = None
        else:
            self.heating_stage_on_supply_air_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_stage_off_supply_air_setpoint_temperature = None
        else:
            self.heating_stage_off_supply_air_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_zone_name = None
        else:
            self.control_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_node_or_nodelist_name = None
        else:
            self.setpoint_node_or_nodelist_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def heating_stage_on_supply_air_setpoint_temperature(self):
        """Get heating_stage_on_supply_air_setpoint_temperature

        Returns:
            float: the value of `heating_stage_on_supply_air_setpoint_temperature` or None if not set
        """
        return self._data["Heating Stage On Supply Air Setpoint Temperature"]

    @heating_stage_on_supply_air_setpoint_temperature.setter
    def heating_stage_on_supply_air_setpoint_temperature(self, value=99.0):
        """  Corresponds to IDD Field `Heating Stage On Supply Air Setpoint Temperature`
        This is the setpoint value applied when heating device is to cycle ON

        Args:
            value (float): value for IDD Field `Heating Stage On Supply Air Setpoint Temperature`
                Units: C
                Default value: 99.0
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
                                 'for field `heating_stage_on_supply_air_setpoint_temperature`'.format(value))
        self._data["Heating Stage On Supply Air Setpoint Temperature"] = value

    @property
    def heating_stage_off_supply_air_setpoint_temperature(self):
        """Get heating_stage_off_supply_air_setpoint_temperature

        Returns:
            float: the value of `heating_stage_off_supply_air_setpoint_temperature` or None if not set
        """
        return self._data["Heating Stage Off Supply Air Setpoint Temperature"]

    @heating_stage_off_supply_air_setpoint_temperature.setter
    def heating_stage_off_supply_air_setpoint_temperature(self, value=-99.0):
        """  Corresponds to IDD Field `Heating Stage Off Supply Air Setpoint Temperature`
        This is the setpoint value applied when heating device is to cycle OFF

        Args:
            value (float): value for IDD Field `Heating Stage Off Supply Air Setpoint Temperature`
                Units: C
                Default value: -99.0
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
                                 'for field `heating_stage_off_supply_air_setpoint_temperature`'.format(value))
        self._data["Heating Stage Off Supply Air Setpoint Temperature"] = value

    @property
    def control_zone_name(self):
        """Get control_zone_name

        Returns:
            str: the value of `control_zone_name` or None if not set
        """
        return self._data["Control Zone Name"]

    @control_zone_name.setter
    def control_zone_name(self, value=None):
        """  Corresponds to IDD Field `Control Zone Name`

        Args:
            value (str): value for IDD Field `Control Zone Name`
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
                                 'for field `control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_zone_name`')
        self._data["Control Zone Name"] = value

    @property
    def setpoint_node_or_nodelist_name(self):
        """Get setpoint_node_or_nodelist_name

        Returns:
            str: the value of `setpoint_node_or_nodelist_name` or None if not set
        """
        return self._data["Setpoint Node or NodeList Name"]

    @setpoint_node_or_nodelist_name.setter
    def setpoint_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node or NodeList Name`
        Node(s) at which the temperature will be set

        Args:
            value (str): value for IDD Field `Setpoint Node or NodeList Name`
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
                                 'for field `setpoint_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_node_or_nodelist_name`')
        self._data["Setpoint Node or NodeList Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])