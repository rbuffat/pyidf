from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class ControllerWaterCoil(object):
    """ Corresponds to IDD object `Controller:WaterCoil`
        Controller for a water coil which is located directly in an air loop branch or
        outdoor air equipment list. Controls the coil water flow to meet the specified
        leaving air setpoint(s). Used with Coil:Heating:Water, Coil:Cooling:Water,
        Coil:Cooling:Water:DetailedGeometry, and
        CoilSystem:Cooling:Water:HeatexchangerAssisted.
    """
    internal_name = "Controller:WaterCoil"
    field_count = 9
    required_fields = ["Name", "Control Variable", "Actuator Variable", "Sensor Node Name", "Actuator Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 9
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Controller:WaterCoil`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Variable"] = None
        self._data["Action"] = None
        self._data["Actuator Variable"] = None
        self._data["Sensor Node Name"] = None
        self._data["Actuator Node Name"] = None
        self._data["Controller Convergence Tolerance"] = None
        self._data["Maximum Actuated Flow"] = None
        self._data["Minimum Actuated Flow"] = None
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
            self.control_variable = None
        else:
            self.control_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.action = None
        else:
            self.action = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuator_variable = None
        else:
            self.actuator_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sensor_node_name = None
        else:
            self.sensor_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuator_node_name = None
        else:
            self.actuator_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_convergence_tolerance = None
        else:
            self.controller_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_actuated_flow = None
        else:
            self.maximum_actuated_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_actuated_flow = None
        else:
            self.minimum_actuated_flow = vals[i]
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
                                 ' for field `ControllerWaterCoil.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerWaterCoil.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerWaterCoil.name`')
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
        keys HumidityRatio or TemperatureAndHumidityRatio
        requires a ZoneControl:Humidistat object along
        with SetpointManager:SingleZone:Humidity:Maximum,
        SetpointManager:MultiZone:MaximumHumidity:Average, or
        SetpointManager:Multizone:Humidity:Maximum object

        Args:
            value (str): value for IDD Field `Control Variable`
                Accepted values are:
                      - Temperature
                      - HumidityRatio
                      - TemperatureAndHumidityRatio
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
                                 ' for field `ControllerWaterCoil.control_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerWaterCoil.control_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerWaterCoil.control_variable`')
            vals = {}
            vals["temperature"] = "Temperature"
            vals["humidityratio"] = "HumidityRatio"
            vals["temperatureandhumidityratio"] = "TemperatureAndHumidityRatio"
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
                                     'field `ControllerWaterCoil.control_variable`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerWaterCoil.control_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Variable"] = value

    @property
    def action(self):
        """Get action

        Returns:
            str: the value of `action` or None if not set
        """
        return self._data["Action"]

    @action.setter
    def action(self, value=None):
        """  Corresponds to IDD Field `Action`
        Leave blank to have this automatically selected from coil type.
        Chilled water coils should be reverse action
        Hot water coils should be normal action

        Args:
            value (str): value for IDD Field `Action`
                Accepted values are:
                      - Normal
                      - Reverse
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
                                 ' for field `ControllerWaterCoil.action`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerWaterCoil.action`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerWaterCoil.action`')
            vals = {}
            vals["normal"] = "Normal"
            vals["reverse"] = "Reverse"
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
                                     'field `ControllerWaterCoil.action`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerWaterCoil.action`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Action"] = value

    @property
    def actuator_variable(self):
        """Get actuator_variable

        Returns:
            str: the value of `actuator_variable` or None if not set
        """
        return self._data["Actuator Variable"]

    @actuator_variable.setter
    def actuator_variable(self, value=None):
        """  Corresponds to IDD Field `Actuator Variable`

        Args:
            value (str): value for IDD Field `Actuator Variable`
                Accepted values are:
                      - Flow
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
                                 ' for field `ControllerWaterCoil.actuator_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerWaterCoil.actuator_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerWaterCoil.actuator_variable`')
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
                                     'field `ControllerWaterCoil.actuator_variable`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerWaterCoil.actuator_variable`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Actuator Variable"] = value

    @property
    def sensor_node_name(self):
        """Get sensor_node_name

        Returns:
            str: the value of `sensor_node_name` or None if not set
        """
        return self._data["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `Sensor Node Name`

        Args:
            value (str): value for IDD Field `Sensor Node Name`
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
                                 ' for field `ControllerWaterCoil.sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerWaterCoil.sensor_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerWaterCoil.sensor_node_name`')
        self._data["Sensor Node Name"] = value

    @property
    def actuator_node_name(self):
        """Get actuator_node_name

        Returns:
            str: the value of `actuator_node_name` or None if not set
        """
        return self._data["Actuator Node Name"]

    @actuator_node_name.setter
    def actuator_node_name(self, value=None):
        """  Corresponds to IDD Field `Actuator Node Name`

        Args:
            value (str): value for IDD Field `Actuator Node Name`
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
                                 ' for field `ControllerWaterCoil.actuator_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerWaterCoil.actuator_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerWaterCoil.actuator_node_name`')
        self._data["Actuator Node Name"] = value

    @property
    def controller_convergence_tolerance(self):
        """Get controller_convergence_tolerance

        Returns:
            float: the value of `controller_convergence_tolerance` or None if not set
        """
        return self._data["Controller Convergence Tolerance"]

    @controller_convergence_tolerance.setter
    def controller_convergence_tolerance(self, value="autosize"):
        """  Corresponds to IDD Field `Controller Convergence Tolerance`

        Args:
            value (float or "Autosize"): value for IDD Field `Controller Convergence Tolerance`
                Units: deltaC
                Default value: "autosize"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Controller Convergence Tolerance"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ControllerWaterCoil.controller_convergence_tolerance`'.format(value))
                    self._data["Controller Convergence Tolerance"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ControllerWaterCoil.controller_convergence_tolerance`'.format(value))
        self._data["Controller Convergence Tolerance"] = value

    @property
    def maximum_actuated_flow(self):
        """Get maximum_actuated_flow

        Returns:
            float: the value of `maximum_actuated_flow` or None if not set
        """
        return self._data["Maximum Actuated Flow"]

    @maximum_actuated_flow.setter
    def maximum_actuated_flow(self, value=None):
        """  Corresponds to IDD Field `Maximum Actuated Flow`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Actuated Flow`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Actuated Flow"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ControllerWaterCoil.maximum_actuated_flow`'.format(value))
                    self._data["Maximum Actuated Flow"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ControllerWaterCoil.maximum_actuated_flow`'.format(value))
        self._data["Maximum Actuated Flow"] = value

    @property
    def minimum_actuated_flow(self):
        """Get minimum_actuated_flow

        Returns:
            float: the value of `minimum_actuated_flow` or None if not set
        """
        return self._data["Minimum Actuated Flow"]

    @minimum_actuated_flow.setter
    def minimum_actuated_flow(self, value=1e-07):
        """  Corresponds to IDD Field `Minimum Actuated Flow`

        Args:
            value (float): value for IDD Field `Minimum Actuated Flow`
                Units: m3/s
                Default value: 1e-07
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
                                 ' for field `ControllerWaterCoil.minimum_actuated_flow`'.format(value))
        self._data["Minimum Actuated Flow"] = value

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
                    raise ValueError("Required field ControllerWaterCoil:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ControllerWaterCoil:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ControllerWaterCoil: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ControllerWaterCoil: {} / {}".format(out_fields,
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

class ControllerOutdoorAir(object):
    """ Corresponds to IDD object `Controller:OutdoorAir`
        Controller to set the outdoor air flow rate for an air loop. Control options include
        fixed, proportional, scheduled, economizer, and demand-controlled ventilation.
    """
    internal_name = "Controller:OutdoorAir"
    field_count = 26
    required_fields = ["Name", "Relief Air Outlet Node Name", "Return Air Node Name", "Mixed Air Node Name", "Actuator Node Name", "Minimum Outdoor Air Flow Rate", "Maximum Outdoor Air Flow Rate"]
    extensible_fields = 0
    format = None
    min_fields = 16
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Controller:OutdoorAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Relief Air Outlet Node Name"] = None
        self._data["Return Air Node Name"] = None
        self._data["Mixed Air Node Name"] = None
        self._data["Actuator Node Name"] = None
        self._data["Minimum Outdoor Air Flow Rate"] = None
        self._data["Maximum Outdoor Air Flow Rate"] = None
        self._data["Economizer Control Type"] = None
        self._data["Economizer Control Action Type"] = None
        self._data["Economizer Maximum Limit Dry-Bulb Temperature"] = None
        self._data["Economizer Maximum Limit Enthalpy"] = None
        self._data["Economizer Maximum Limit Dewpoint Temperature"] = None
        self._data["Electronic Enthalpy Limit Curve Name"] = None
        self._data["Economizer Minimum Limit Dry-Bulb Temperature"] = None
        self._data["Lockout Type"] = None
        self._data["Minimum Limit Type"] = None
        self._data["Minimum Outdoor Air Schedule Name"] = None
        self._data["Minimum Fraction of Outdoor Air Schedule Name"] = None
        self._data["Maximum Fraction of Outdoor Air Schedule Name"] = None
        self._data["Mechanical Ventilation Controller Name"] = None
        self._data["Time of Day Economizer Control Schedule Name"] = None
        self._data["High Humidity Control"] = None
        self._data["Humidistat Control Zone Name"] = None
        self._data["High Humidity Outdoor Air Flow Ratio"] = None
        self._data["Control High Indoor Humidity Based on Outdoor Humidity Ratio"] = None
        self._data["Heat Recovery Bypass Control Type"] = None
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
            self.relief_air_outlet_node_name = None
        else:
            self.relief_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.return_air_node_name = None
        else:
            self.return_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_air_node_name = None
        else:
            self.mixed_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.actuator_node_name = None
        else:
            self.actuator_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outdoor_air_flow_rate = None
        else:
            self.minimum_outdoor_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_flow_rate = None
        else:
            self.maximum_outdoor_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.economizer_control_type = None
        else:
            self.economizer_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.economizer_control_action_type = None
        else:
            self.economizer_control_action_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.economizer_maximum_limit_drybulb_temperature = None
        else:
            self.economizer_maximum_limit_drybulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.economizer_maximum_limit_enthalpy = None
        else:
            self.economizer_maximum_limit_enthalpy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.economizer_maximum_limit_dewpoint_temperature = None
        else:
            self.economizer_maximum_limit_dewpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electronic_enthalpy_limit_curve_name = None
        else:
            self.electronic_enthalpy_limit_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.economizer_minimum_limit_drybulb_temperature = None
        else:
            self.economizer_minimum_limit_drybulb_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lockout_type = None
        else:
            self.lockout_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_limit_type = None
        else:
            self.minimum_limit_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outdoor_air_schedule_name = None
        else:
            self.minimum_outdoor_air_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_fraction_of_outdoor_air_schedule_name = None
        else:
            self.minimum_fraction_of_outdoor_air_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_fraction_of_outdoor_air_schedule_name = None
        else:
            self.maximum_fraction_of_outdoor_air_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_ventilation_controller_name = None
        else:
            self.mechanical_ventilation_controller_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.time_of_day_economizer_control_schedule_name = None
        else:
            self.time_of_day_economizer_control_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_humidity_control = None
        else:
            self.high_humidity_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidistat_control_zone_name = None
        else:
            self.humidistat_control_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_humidity_outdoor_air_flow_ratio = None
        else:
            self.high_humidity_outdoor_air_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_high_indoor_humidity_based_on_outdoor_humidity_ratio = None
        else:
            self.control_high_indoor_humidity_based_on_outdoor_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_recovery_bypass_control_type = None
        else:
            self.heat_recovery_bypass_control_type = vals[i]
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
                                 ' for field `ControllerOutdoorAir.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.name`')
        self._data["Name"] = value

    @property
    def relief_air_outlet_node_name(self):
        """Get relief_air_outlet_node_name

        Returns:
            str: the value of `relief_air_outlet_node_name` or None if not set
        """
        return self._data["Relief Air Outlet Node Name"]

    @relief_air_outlet_node_name.setter
    def relief_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Relief Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Relief Air Outlet Node Name`
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
                                 ' for field `ControllerOutdoorAir.relief_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.relief_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.relief_air_outlet_node_name`')
        self._data["Relief Air Outlet Node Name"] = value

    @property
    def return_air_node_name(self):
        """Get return_air_node_name

        Returns:
            str: the value of `return_air_node_name` or None if not set
        """
        return self._data["Return Air Node Name"]

    @return_air_node_name.setter
    def return_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Return Air Node Name`

        Args:
            value (str): value for IDD Field `Return Air Node Name`
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
                                 ' for field `ControllerOutdoorAir.return_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.return_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.return_air_node_name`')
        self._data["Return Air Node Name"] = value

    @property
    def mixed_air_node_name(self):
        """Get mixed_air_node_name

        Returns:
            str: the value of `mixed_air_node_name` or None if not set
        """
        return self._data["Mixed Air Node Name"]

    @mixed_air_node_name.setter
    def mixed_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Air Node Name`

        Args:
            value (str): value for IDD Field `Mixed Air Node Name`
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
                                 ' for field `ControllerOutdoorAir.mixed_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.mixed_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.mixed_air_node_name`')
        self._data["Mixed Air Node Name"] = value

    @property
    def actuator_node_name(self):
        """Get actuator_node_name

        Returns:
            str: the value of `actuator_node_name` or None if not set
        """
        return self._data["Actuator Node Name"]

    @actuator_node_name.setter
    def actuator_node_name(self, value=None):
        """  Corresponds to IDD Field `Actuator Node Name`
        Outdoor air inlet node entering the first pre-treat component if any

        Args:
            value (str): value for IDD Field `Actuator Node Name`
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
                                 ' for field `ControllerOutdoorAir.actuator_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.actuator_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.actuator_node_name`')
        self._data["Actuator Node Name"] = value

    @property
    def minimum_outdoor_air_flow_rate(self):
        """Get minimum_outdoor_air_flow_rate

        Returns:
            float: the value of `minimum_outdoor_air_flow_rate` or None if not set
        """
        return self._data["Minimum Outdoor Air Flow Rate"]

    @minimum_outdoor_air_flow_rate.setter
    def minimum_outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Minimum Outdoor Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Outdoor Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Minimum Outdoor Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ControllerOutdoorAir.minimum_outdoor_air_flow_rate`'.format(value))
                    self._data["Minimum Outdoor Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ControllerOutdoorAir.minimum_outdoor_air_flow_rate`'.format(value))
        self._data["Minimum Outdoor Air Flow Rate"] = value

    @property
    def maximum_outdoor_air_flow_rate(self):
        """Get maximum_outdoor_air_flow_rate

        Returns:
            float: the value of `maximum_outdoor_air_flow_rate` or None if not set
        """
        return self._data["Maximum Outdoor Air Flow Rate"]

    @maximum_outdoor_air_flow_rate.setter
    def maximum_outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Outdoor Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Outdoor Air Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Outdoor Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ControllerOutdoorAir.maximum_outdoor_air_flow_rate`'.format(value))
                    self._data["Maximum Outdoor Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ControllerOutdoorAir.maximum_outdoor_air_flow_rate`'.format(value))
        self._data["Maximum Outdoor Air Flow Rate"] = value

    @property
    def economizer_control_type(self):
        """Get economizer_control_type

        Returns:
            str: the value of `economizer_control_type` or None if not set
        """
        return self._data["Economizer Control Type"]

    @economizer_control_type.setter
    def economizer_control_type(self, value="NoEconomizer"):
        """  Corresponds to IDD Field `Economizer Control Type`

        Args:
            value (str): value for IDD Field `Economizer Control Type`
                Accepted values are:
                      - FixedDryBulb
                      - FixedEnthalpy
                      - DifferentialDryBulb
                      - DifferentialEnthalpy
                      - FixedDewPointAndDryBulb
                      - ElectronicEnthalpy
                      - DifferentialDryBulbAndEnthalpy
                      - NoEconomizer
                Default value: NoEconomizer
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
                                 ' for field `ControllerOutdoorAir.economizer_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.economizer_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.economizer_control_type`')
            vals = {}
            vals["fixeddrybulb"] = "FixedDryBulb"
            vals["fixedenthalpy"] = "FixedEnthalpy"
            vals["differentialdrybulb"] = "DifferentialDryBulb"
            vals["differentialenthalpy"] = "DifferentialEnthalpy"
            vals["fixeddewpointanddrybulb"] = "FixedDewPointAndDryBulb"
            vals["electronicenthalpy"] = "ElectronicEnthalpy"
            vals["differentialdrybulbandenthalpy"] = "DifferentialDryBulbAndEnthalpy"
            vals["noeconomizer"] = "NoEconomizer"
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
                                     'field `ControllerOutdoorAir.economizer_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerOutdoorAir.economizer_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Economizer Control Type"] = value

    @property
    def economizer_control_action_type(self):
        """Get economizer_control_action_type

        Returns:
            str: the value of `economizer_control_action_type` or None if not set
        """
        return self._data["Economizer Control Action Type"]

    @economizer_control_action_type.setter
    def economizer_control_action_type(self, value="ModulateFlow"):
        """  Corresponds to IDD Field `Economizer Control Action Type`

        Args:
            value (str): value for IDD Field `Economizer Control Action Type`
                Accepted values are:
                      - ModulateFlow
                      - MinimumFlowWithBypass
                Default value: ModulateFlow
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
                                 ' for field `ControllerOutdoorAir.economizer_control_action_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.economizer_control_action_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.economizer_control_action_type`')
            vals = {}
            vals["modulateflow"] = "ModulateFlow"
            vals["minimumflowwithbypass"] = "MinimumFlowWithBypass"
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
                                     'field `ControllerOutdoorAir.economizer_control_action_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerOutdoorAir.economizer_control_action_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Economizer Control Action Type"] = value

    @property
    def economizer_maximum_limit_drybulb_temperature(self):
        """Get economizer_maximum_limit_drybulb_temperature

        Returns:
            float: the value of `economizer_maximum_limit_drybulb_temperature` or None if not set
        """
        return self._data["Economizer Maximum Limit Dry-Bulb Temperature"]

    @economizer_maximum_limit_drybulb_temperature.setter
    def economizer_maximum_limit_drybulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Economizer Maximum Limit Dry-Bulb Temperature`
        Enter the maximum outdoor dry-bulb temperature limit for FixedDryBulb
        economizer control type. No input or blank input means this limit is
        not operative. Limit is applied regardless of economizer control type.

        Args:
            value (float): value for IDD Field `Economizer Maximum Limit Dry-Bulb Temperature`
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
                                 ' for field `ControllerOutdoorAir.economizer_maximum_limit_drybulb_temperature`'.format(value))
        self._data["Economizer Maximum Limit Dry-Bulb Temperature"] = value

    @property
    def economizer_maximum_limit_enthalpy(self):
        """Get economizer_maximum_limit_enthalpy

        Returns:
            float: the value of `economizer_maximum_limit_enthalpy` or None if not set
        """
        return self._data["Economizer Maximum Limit Enthalpy"]

    @economizer_maximum_limit_enthalpy.setter
    def economizer_maximum_limit_enthalpy(self, value=None):
        """  Corresponds to IDD Field `Economizer Maximum Limit Enthalpy`
        Enter the maximum outdoor enthalpy limit for FixedEnthalpy economizer control type.
        No input or blank input means this limit is not operative
        Limit is applied regardless of economizer control type.

        Args:
            value (float): value for IDD Field `Economizer Maximum Limit Enthalpy`
                Units: J/kg
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
                                 ' for field `ControllerOutdoorAir.economizer_maximum_limit_enthalpy`'.format(value))
        self._data["Economizer Maximum Limit Enthalpy"] = value

    @property
    def economizer_maximum_limit_dewpoint_temperature(self):
        """Get economizer_maximum_limit_dewpoint_temperature

        Returns:
            float: the value of `economizer_maximum_limit_dewpoint_temperature` or None if not set
        """
        return self._data["Economizer Maximum Limit Dewpoint Temperature"]

    @economizer_maximum_limit_dewpoint_temperature.setter
    def economizer_maximum_limit_dewpoint_temperature(self, value=None):
        """  Corresponds to IDD Field `Economizer Maximum Limit Dewpoint Temperature`
        Enter the maximum outdoor dewpoint temperature limit for FixedDewPointAndDryBulb
        economizer control type. No input or blank input means this limit is not operative.
        Limit is applied regardless of economizer control type.

        Args:
            value (float): value for IDD Field `Economizer Maximum Limit Dewpoint Temperature`
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
                                 ' for field `ControllerOutdoorAir.economizer_maximum_limit_dewpoint_temperature`'.format(value))
        self._data["Economizer Maximum Limit Dewpoint Temperature"] = value

    @property
    def electronic_enthalpy_limit_curve_name(self):
        """Get electronic_enthalpy_limit_curve_name

        Returns:
            str: the value of `electronic_enthalpy_limit_curve_name` or None if not set
        """
        return self._data["Electronic Enthalpy Limit Curve Name"]

    @electronic_enthalpy_limit_curve_name.setter
    def electronic_enthalpy_limit_curve_name(self, value=None):
        """  Corresponds to IDD Field `Electronic Enthalpy Limit Curve Name`
        Table:OneIndependentVariable object can also be used
        Enter the name of a quadratic or cubic curve which defines the maximum outdoor
        humidity ratio (function of outdoor dry-bulb temperature) for ElectronicEnthalpy
        economizer control type. No input or blank input means this limit is not operative
        Limit is applied regardless of economizer control type.

        Args:
            value (str): value for IDD Field `Electronic Enthalpy Limit Curve Name`
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
                                 ' for field `ControllerOutdoorAir.electronic_enthalpy_limit_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.electronic_enthalpy_limit_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.electronic_enthalpy_limit_curve_name`')
        self._data["Electronic Enthalpy Limit Curve Name"] = value

    @property
    def economizer_minimum_limit_drybulb_temperature(self):
        """Get economizer_minimum_limit_drybulb_temperature

        Returns:
            float: the value of `economizer_minimum_limit_drybulb_temperature` or None if not set
        """
        return self._data["Economizer Minimum Limit Dry-Bulb Temperature"]

    @economizer_minimum_limit_drybulb_temperature.setter
    def economizer_minimum_limit_drybulb_temperature(self, value=None):
        """  Corresponds to IDD Field `Economizer Minimum Limit Dry-Bulb Temperature`
        Enter the minimum outdoor dry-bulb temperature limit for economizer control.
        No input or blank input means this limit is not operative
        Limit is applied regardless of economizer control type.

        Args:
            value (float): value for IDD Field `Economizer Minimum Limit Dry-Bulb Temperature`
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
                                 ' for field `ControllerOutdoorAir.economizer_minimum_limit_drybulb_temperature`'.format(value))
        self._data["Economizer Minimum Limit Dry-Bulb Temperature"] = value

    @property
    def lockout_type(self):
        """Get lockout_type

        Returns:
            str: the value of `lockout_type` or None if not set
        """
        return self._data["Lockout Type"]

    @lockout_type.setter
    def lockout_type(self, value="NoLockout"):
        """  Corresponds to IDD Field `Lockout Type`

        Args:
            value (str): value for IDD Field `Lockout Type`
                Accepted values are:
                      - NoLockout
                      - LockoutWithHeating
                      - LockoutWithCompressor
                Default value: NoLockout
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
                                 ' for field `ControllerOutdoorAir.lockout_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.lockout_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.lockout_type`')
            vals = {}
            vals["nolockout"] = "NoLockout"
            vals["lockoutwithheating"] = "LockoutWithHeating"
            vals["lockoutwithcompressor"] = "LockoutWithCompressor"
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
                                     'field `ControllerOutdoorAir.lockout_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerOutdoorAir.lockout_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Lockout Type"] = value

    @property
    def minimum_limit_type(self):
        """Get minimum_limit_type

        Returns:
            str: the value of `minimum_limit_type` or None if not set
        """
        return self._data["Minimum Limit Type"]

    @minimum_limit_type.setter
    def minimum_limit_type(self, value="ProportionalMinimum"):
        """  Corresponds to IDD Field `Minimum Limit Type`

        Args:
            value (str): value for IDD Field `Minimum Limit Type`
                Accepted values are:
                      - FixedMinimum
                      - ProportionalMinimum
                Default value: ProportionalMinimum
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
                                 ' for field `ControllerOutdoorAir.minimum_limit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.minimum_limit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.minimum_limit_type`')
            vals = {}
            vals["fixedminimum"] = "FixedMinimum"
            vals["proportionalminimum"] = "ProportionalMinimum"
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
                                     'field `ControllerOutdoorAir.minimum_limit_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerOutdoorAir.minimum_limit_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Minimum Limit Type"] = value

    @property
    def minimum_outdoor_air_schedule_name(self):
        """Get minimum_outdoor_air_schedule_name

        Returns:
            str: the value of `minimum_outdoor_air_schedule_name` or None if not set
        """
        return self._data["Minimum Outdoor Air Schedule Name"]

    @minimum_outdoor_air_schedule_name.setter
    def minimum_outdoor_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Outdoor Air Schedule Name`
        Schedule values multiply the minimum outdoor air flow rate

        Args:
            value (str): value for IDD Field `Minimum Outdoor Air Schedule Name`
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
                                 ' for field `ControllerOutdoorAir.minimum_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.minimum_outdoor_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.minimum_outdoor_air_schedule_name`')
        self._data["Minimum Outdoor Air Schedule Name"] = value

    @property
    def minimum_fraction_of_outdoor_air_schedule_name(self):
        """Get minimum_fraction_of_outdoor_air_schedule_name

        Returns:
            str: the value of `minimum_fraction_of_outdoor_air_schedule_name` or None if not set
        """
        return self._data["Minimum Fraction of Outdoor Air Schedule Name"]

    @minimum_fraction_of_outdoor_air_schedule_name.setter
    def minimum_fraction_of_outdoor_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Fraction of Outdoor Air Schedule Name`
        schedule values multiply the design/mixed air flow rate

        Args:
            value (str): value for IDD Field `Minimum Fraction of Outdoor Air Schedule Name`
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
                                 ' for field `ControllerOutdoorAir.minimum_fraction_of_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.minimum_fraction_of_outdoor_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.minimum_fraction_of_outdoor_air_schedule_name`')
        self._data["Minimum Fraction of Outdoor Air Schedule Name"] = value

    @property
    def maximum_fraction_of_outdoor_air_schedule_name(self):
        """Get maximum_fraction_of_outdoor_air_schedule_name

        Returns:
            str: the value of `maximum_fraction_of_outdoor_air_schedule_name` or None if not set
        """
        return self._data["Maximum Fraction of Outdoor Air Schedule Name"]

    @maximum_fraction_of_outdoor_air_schedule_name.setter
    def maximum_fraction_of_outdoor_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Maximum Fraction of Outdoor Air Schedule Name`
        schedule values multiply the design/mixed air flow rate

        Args:
            value (str): value for IDD Field `Maximum Fraction of Outdoor Air Schedule Name`
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
                                 ' for field `ControllerOutdoorAir.maximum_fraction_of_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.maximum_fraction_of_outdoor_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.maximum_fraction_of_outdoor_air_schedule_name`')
        self._data["Maximum Fraction of Outdoor Air Schedule Name"] = value

    @property
    def mechanical_ventilation_controller_name(self):
        """Get mechanical_ventilation_controller_name

        Returns:
            str: the value of `mechanical_ventilation_controller_name` or None if not set
        """
        return self._data["Mechanical Ventilation Controller Name"]

    @mechanical_ventilation_controller_name.setter
    def mechanical_ventilation_controller_name(self, value=None):
        """  Corresponds to IDD Field `Mechanical Ventilation Controller Name`
        Enter the name of a Controller:MechanicalVentilation object.
        Optional field for defining outdoor ventilation air based on flow rate per unit floor
        area and flow rate per person. Simplified method of demand-controlled ventilation.

        Args:
            value (str): value for IDD Field `Mechanical Ventilation Controller Name`
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
                                 ' for field `ControllerOutdoorAir.mechanical_ventilation_controller_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.mechanical_ventilation_controller_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.mechanical_ventilation_controller_name`')
        self._data["Mechanical Ventilation Controller Name"] = value

    @property
    def time_of_day_economizer_control_schedule_name(self):
        """Get time_of_day_economizer_control_schedule_name

        Returns:
            str: the value of `time_of_day_economizer_control_schedule_name` or None if not set
        """
        return self._data["Time of Day Economizer Control Schedule Name"]

    @time_of_day_economizer_control_schedule_name.setter
    def time_of_day_economizer_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Time of Day Economizer Control Schedule Name`
        Optional schedule to simulate "push-button" type economizer control.
        Schedule values greater than 0 indicate time-of-day economizer control is enabled.
        Economizer control may be used with or without the high humidity control option.
        When used together, high humidity control has priority over economizer control.
        If the field Economizer Control Type = NoEconomizer, then this option is disabled.

        Args:
            value (str): value for IDD Field `Time of Day Economizer Control Schedule Name`
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
                                 ' for field `ControllerOutdoorAir.time_of_day_economizer_control_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.time_of_day_economizer_control_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.time_of_day_economizer_control_schedule_name`')
        self._data["Time of Day Economizer Control Schedule Name"] = value

    @property
    def high_humidity_control(self):
        """Get high_humidity_control

        Returns:
            str: the value of `high_humidity_control` or None if not set
        """
        return self._data["High Humidity Control"]

    @high_humidity_control.setter
    def high_humidity_control(self, value="No"):
        """  Corresponds to IDD Field `High Humidity Control`
        Optional field to enable modified outdoor air flow rates based on zone relative humidity.
        Select Yes to modify outdoor air flow rate based on a zone humidistat.
        Select No to disable this feature.
        If the field Economizer Control Type = NoEconomizer, then this option is disabled.

        Args:
            value (str): value for IDD Field `High Humidity Control`
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
                                 ' for field `ControllerOutdoorAir.high_humidity_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.high_humidity_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.high_humidity_control`')
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
                                     'field `ControllerOutdoorAir.high_humidity_control`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerOutdoorAir.high_humidity_control`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["High Humidity Control"] = value

    @property
    def humidistat_control_zone_name(self):
        """Get humidistat_control_zone_name

        Returns:
            str: the value of `humidistat_control_zone_name` or None if not set
        """
        return self._data["Humidistat Control Zone Name"]

    @humidistat_control_zone_name.setter
    def humidistat_control_zone_name(self, value=None):
        """  Corresponds to IDD Field `Humidistat Control Zone Name`
        Enter the name of the zone where the humidistat is located.
        This field is only used when the field High Humidity Control = Yes.

        Args:
            value (str): value for IDD Field `Humidistat Control Zone Name`
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
                                 ' for field `ControllerOutdoorAir.humidistat_control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.humidistat_control_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.humidistat_control_zone_name`')
        self._data["Humidistat Control Zone Name"] = value

    @property
    def high_humidity_outdoor_air_flow_ratio(self):
        """Get high_humidity_outdoor_air_flow_ratio

        Returns:
            float: the value of `high_humidity_outdoor_air_flow_ratio` or None if not set
        """
        return self._data["High Humidity Outdoor Air Flow Ratio"]

    @high_humidity_outdoor_air_flow_ratio.setter
    def high_humidity_outdoor_air_flow_ratio(self, value=1.0):
        """  Corresponds to IDD Field `High Humidity Outdoor Air Flow Ratio`
        Enter the ratio of outdoor air to the maximum outdoor air flow rate when modified air
        flow rates are active based on high indoor humidity.
        The minimum value must be greater than 0.
        This field is only used when the field High Humidity Control = Yes.

        Args:
            value (float): value for IDD Field `High Humidity Outdoor Air Flow Ratio`
                Default value: 1.0
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
                                 ' for field `ControllerOutdoorAir.high_humidity_outdoor_air_flow_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ControllerOutdoorAir.high_humidity_outdoor_air_flow_ratio`')
        self._data["High Humidity Outdoor Air Flow Ratio"] = value

    @property
    def control_high_indoor_humidity_based_on_outdoor_humidity_ratio(self):
        """Get control_high_indoor_humidity_based_on_outdoor_humidity_ratio

        Returns:
            str: the value of `control_high_indoor_humidity_based_on_outdoor_humidity_ratio` or None if not set
        """
        return self._data["Control High Indoor Humidity Based on Outdoor Humidity Ratio"]

    @control_high_indoor_humidity_based_on_outdoor_humidity_ratio.setter
    def control_high_indoor_humidity_based_on_outdoor_humidity_ratio(self, value="Yes"):
        """  Corresponds to IDD Field `Control High Indoor Humidity Based on Outdoor Humidity Ratio`
        If No is selected, the outdoor air flow rate is modified any time indoor relative
        humidity is above the humidistat setpoint. If Yes is selected, the outdoor air
        flow rate is modified any time the indoor relative humidity is above the humidistat
        setpoint and the outdoor humidity ratio is less than the indoor humidity ratio.
        This field is only used when the field High Humidity Control = Yes.

        Args:
            value (str): value for IDD Field `Control High Indoor Humidity Based on Outdoor Humidity Ratio`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
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
                                 ' for field `ControllerOutdoorAir.control_high_indoor_humidity_based_on_outdoor_humidity_ratio`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.control_high_indoor_humidity_based_on_outdoor_humidity_ratio`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.control_high_indoor_humidity_based_on_outdoor_humidity_ratio`')
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
                                     'field `ControllerOutdoorAir.control_high_indoor_humidity_based_on_outdoor_humidity_ratio`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerOutdoorAir.control_high_indoor_humidity_based_on_outdoor_humidity_ratio`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control High Indoor Humidity Based on Outdoor Humidity Ratio"] = value

    @property
    def heat_recovery_bypass_control_type(self):
        """Get heat_recovery_bypass_control_type

        Returns:
            str: the value of `heat_recovery_bypass_control_type` or None if not set
        """
        return self._data["Heat Recovery Bypass Control Type"]

    @heat_recovery_bypass_control_type.setter
    def heat_recovery_bypass_control_type(self, value="BypassWhenWithinEconomizerLimits"):
        """  Corresponds to IDD Field `Heat Recovery Bypass Control Type`
        BypassWhenWithinEconomizerLimits specifies that heat recovery
        is active only when the economizer is off because conditions
        are outside the economizer control limits
        BypassWhenOAFlowGreaterThanMinimum specifies enhanced economizer
        controls to allow heat recovery when economizer is active
        (within limits) but the outdoor air flow rate is at the minimum.

        Args:
            value (str): value for IDD Field `Heat Recovery Bypass Control Type`
                Default value: BypassWhenWithinEconomizerLimits
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
                                 ' for field `ControllerOutdoorAir.heat_recovery_bypass_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerOutdoorAir.heat_recovery_bypass_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerOutdoorAir.heat_recovery_bypass_control_type`')
        self._data["Heat Recovery Bypass Control Type"] = value

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
                    raise ValueError("Required field ControllerOutdoorAir:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ControllerOutdoorAir:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ControllerOutdoorAir: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ControllerOutdoorAir: {} / {}".format(out_fields,
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

class ControllerMechanicalVentilation(object):
    """ Corresponds to IDD object `Controller:MechanicalVentilation`
        This object is used in conjuction with Controller:OutdoorAir to specify outdoor
        ventilation air based on outdoor air specified in the DesignSpecification:OutdoorAir object
        The Controller:OutdoorAir object is associated with a specific air loop, so the
        outdoor air flow rates specified in Controller:MechanicalVentilation correspond to the zones
        attached to that specific air loop.
        Duplicate groups of Zone name, Design Specification Outdoor Air Object Name,
        and Design Specification Zone Air Distribution Object Name to increase allowable number of entries
    """
    internal_name = "Controller:MechanicalVentilation"
    field_count = 5
    required_fields = ["Name"]
    extensible_fields = 3
    format = None
    min_fields = 8
    extensible_keys = ["Zone 1 Name", "Design Specification Outdoor Air Object Name 1", "Design Specification Zone Air Distribution Object Name 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Controller:MechanicalVentilation`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Demand Controlled Ventilation"] = None
        self._data["System Outdoor Air Method"] = None
        self._data["Zone Maximum Outdoor Air Fraction"] = None
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
            self.demand_controlled_ventilation = None
        else:
            self.demand_controlled_ventilation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.system_outdoor_air_method = None
        else:
            self.system_outdoor_air_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_maximum_outdoor_air_fraction = None
        else:
            self.zone_maximum_outdoor_air_fraction = vals[i]
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
                                 ' for field `ControllerMechanicalVentilation.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerMechanicalVentilation.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerMechanicalVentilation.name`')
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
        If this field is blank, the controller uses the values from the associated Controller:OutdoorAir.
        Schedule values greater than 0 indicate mechanical ventilation is enabled

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
                                 ' for field `ControllerMechanicalVentilation.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerMechanicalVentilation.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerMechanicalVentilation.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def demand_controlled_ventilation(self):
        """Get demand_controlled_ventilation

        Returns:
            str: the value of `demand_controlled_ventilation` or None if not set
        """
        return self._data["Demand Controlled Ventilation"]

    @demand_controlled_ventilation.setter
    def demand_controlled_ventilation(self, value="No"):
        """  Corresponds to IDD Field `Demand Controlled Ventilation`

        Args:
            value (str): value for IDD Field `Demand Controlled Ventilation`
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
                                 ' for field `ControllerMechanicalVentilation.demand_controlled_ventilation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerMechanicalVentilation.demand_controlled_ventilation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerMechanicalVentilation.demand_controlled_ventilation`')
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
                                     'field `ControllerMechanicalVentilation.demand_controlled_ventilation`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerMechanicalVentilation.demand_controlled_ventilation`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Demand Controlled Ventilation"] = value

    @property
    def system_outdoor_air_method(self):
        """Get system_outdoor_air_method

        Returns:
            str: the value of `system_outdoor_air_method` or None if not set
        """
        return self._data["System Outdoor Air Method"]

    @system_outdoor_air_method.setter
    def system_outdoor_air_method(self, value="VentilationRateProcedure"):
        """  Corresponds to IDD Field `System Outdoor Air Method`

        Args:
            value (str): value for IDD Field `System Outdoor Air Method`
                Accepted values are:
                      - ZoneSum
                      - VentilationRateProcedure
                      - IndoorAirQualityProcedure
                      - ProportionalControl
                      - IndoorAirQualityProcedureGenericContaminant
                Default value: VentilationRateProcedure
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
                                 ' for field `ControllerMechanicalVentilation.system_outdoor_air_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerMechanicalVentilation.system_outdoor_air_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerMechanicalVentilation.system_outdoor_air_method`')
            vals = {}
            vals["zonesum"] = "ZoneSum"
            vals["ventilationrateprocedure"] = "VentilationRateProcedure"
            vals["indoorairqualityprocedure"] = "IndoorAirQualityProcedure"
            vals["proportionalcontrol"] = "ProportionalControl"
            vals["indoorairqualityproceduregenericcontaminant"] = "IndoorAirQualityProcedureGenericContaminant"
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
                                     'field `ControllerMechanicalVentilation.system_outdoor_air_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ControllerMechanicalVentilation.system_outdoor_air_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["System Outdoor Air Method"] = value

    @property
    def zone_maximum_outdoor_air_fraction(self):
        """Get zone_maximum_outdoor_air_fraction

        Returns:
            float: the value of `zone_maximum_outdoor_air_fraction` or None if not set
        """
        return self._data["Zone Maximum Outdoor Air Fraction"]

    @zone_maximum_outdoor_air_fraction.setter
    def zone_maximum_outdoor_air_fraction(self, value=1.0):
        """  Corresponds to IDD Field `Zone Maximum Outdoor Air Fraction`

        Args:
            value (float): value for IDD Field `Zone Maximum Outdoor Air Fraction`
                Units: dimensionless
                Default value: 1.0
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
                                 ' for field `ControllerMechanicalVentilation.zone_maximum_outdoor_air_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ControllerMechanicalVentilation.zone_maximum_outdoor_air_fraction`')
        self._data["Zone Maximum Outdoor Air Fraction"] = value

    def add_extensible(self,
                       zone_1_name=None,
                       design_specification_outdoor_air_object_name_1=None,
                       design_specification_zone_air_distribution_object_name_1=None,
                       ):
        """ Add values for extensible fields

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
        vals.append(self._check_zone_1_name(zone_1_name))
        vals.append(self._check_design_specification_outdoor_air_object_name_1(design_specification_outdoor_air_object_name_1))
        vals.append(self._check_design_specification_zone_air_distribution_object_name_1(design_specification_zone_air_distribution_object_name_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_zone_1_name(self, value):
        """ Validates falue of field `Zone 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ControllerMechanicalVentilation.zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerMechanicalVentilation.zone_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerMechanicalVentilation.zone_1_name`')
        return value

    def _check_design_specification_outdoor_air_object_name_1(self, value):
        """ Validates falue of field `Design Specification Outdoor Air Object Name 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ControllerMechanicalVentilation.design_specification_outdoor_air_object_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerMechanicalVentilation.design_specification_outdoor_air_object_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerMechanicalVentilation.design_specification_outdoor_air_object_name_1`')
        return value

    def _check_design_specification_zone_air_distribution_object_name_1(self, value):
        """ Validates falue of field `Design Specification Zone Air Distribution Object Name 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ControllerMechanicalVentilation.design_specification_zone_air_distribution_object_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ControllerMechanicalVentilation.design_specification_zone_air_distribution_object_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ControllerMechanicalVentilation.design_specification_zone_air_distribution_object_name_1`')
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
                    raise ValueError("Required field ControllerMechanicalVentilation:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ControllerMechanicalVentilation:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ControllerMechanicalVentilation: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ControllerMechanicalVentilation: {} / {}".format(out_fields,
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

class AirLoopHvacControllerList(object):
    """ Corresponds to IDD object `AirLoopHVAC:ControllerList`
        List controllers in order of control sequence
    """
    internal_name = "AirLoopHVAC:ControllerList"
    field_count = 17
    required_fields = ["Name", "Controller 1 Object Type", "Controller 1 Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:ControllerList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Controller 1 Object Type"] = None
        self._data["Controller 1 Name"] = None
        self._data["Controller 2 Object Type"] = None
        self._data["Controller 2 Name"] = None
        self._data["Controller 3 Object Type"] = None
        self._data["Controller 3 Name"] = None
        self._data["Controller 4 Object Type"] = None
        self._data["Controller 4 Name"] = None
        self._data["Controller 5 Object Type"] = None
        self._data["Controller 5 Name"] = None
        self._data["Controller 6 Object Type"] = None
        self._data["Controller 6 Name"] = None
        self._data["Controller 7 Object Type"] = None
        self._data["Controller 7 Name"] = None
        self._data["Controller 8 Object Type"] = None
        self._data["Controller 8 Name"] = None
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
            self.controller_1_object_type = None
        else:
            self.controller_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_1_name = None
        else:
            self.controller_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_2_object_type = None
        else:
            self.controller_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_2_name = None
        else:
            self.controller_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_3_object_type = None
        else:
            self.controller_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_3_name = None
        else:
            self.controller_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_4_object_type = None
        else:
            self.controller_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_4_name = None
        else:
            self.controller_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_5_object_type = None
        else:
            self.controller_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_5_name = None
        else:
            self.controller_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_6_object_type = None
        else:
            self.controller_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_6_name = None
        else:
            self.controller_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_7_object_type = None
        else:
            self.controller_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_7_name = None
        else:
            self.controller_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_8_object_type = None
        else:
            self.controller_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.controller_8_name = None
        else:
            self.controller_8_name = vals[i]
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
                                 ' for field `AirLoopHvacControllerList.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.name`')
        self._data["Name"] = value

    @property
    def controller_1_object_type(self):
        """Get controller_1_object_type

        Returns:
            str: the value of `controller_1_object_type` or None if not set
        """
        return self._data["Controller 1 Object Type"]

    @controller_1_object_type.setter
    def controller_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller 1 Object Type`

        Args:
            value (str): value for IDD Field `Controller 1 Object Type`
                Accepted values are:
                      - Controller:WaterCoil
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
                                 ' for field `AirLoopHvacControllerList.controller_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_1_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
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
                                     'field `AirLoopHvacControllerList.controller_1_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirLoopHvacControllerList.controller_1_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller 1 Object Type"] = value

    @property
    def controller_1_name(self):
        """Get controller_1_name

        Returns:
            str: the value of `controller_1_name` or None if not set
        """
        return self._data["Controller 1 Name"]

    @controller_1_name.setter
    def controller_1_name(self, value=None):
        """  Corresponds to IDD Field `Controller 1 Name`

        Args:
            value (str): value for IDD Field `Controller 1 Name`
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
                                 ' for field `AirLoopHvacControllerList.controller_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_1_name`')
        self._data["Controller 1 Name"] = value

    @property
    def controller_2_object_type(self):
        """Get controller_2_object_type

        Returns:
            str: the value of `controller_2_object_type` or None if not set
        """
        return self._data["Controller 2 Object Type"]

    @controller_2_object_type.setter
    def controller_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller 2 Object Type`

        Args:
            value (str): value for IDD Field `Controller 2 Object Type`
                Accepted values are:
                      - Controller:WaterCoil
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
                                 ' for field `AirLoopHvacControllerList.controller_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_2_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
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
                                     'field `AirLoopHvacControllerList.controller_2_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirLoopHvacControllerList.controller_2_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller 2 Object Type"] = value

    @property
    def controller_2_name(self):
        """Get controller_2_name

        Returns:
            str: the value of `controller_2_name` or None if not set
        """
        return self._data["Controller 2 Name"]

    @controller_2_name.setter
    def controller_2_name(self, value=None):
        """  Corresponds to IDD Field `Controller 2 Name`

        Args:
            value (str): value for IDD Field `Controller 2 Name`
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
                                 ' for field `AirLoopHvacControllerList.controller_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_2_name`')
        self._data["Controller 2 Name"] = value

    @property
    def controller_3_object_type(self):
        """Get controller_3_object_type

        Returns:
            str: the value of `controller_3_object_type` or None if not set
        """
        return self._data["Controller 3 Object Type"]

    @controller_3_object_type.setter
    def controller_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller 3 Object Type`

        Args:
            value (str): value for IDD Field `Controller 3 Object Type`
                Accepted values are:
                      - Controller:WaterCoil
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
                                 ' for field `AirLoopHvacControllerList.controller_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_3_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
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
                                     'field `AirLoopHvacControllerList.controller_3_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirLoopHvacControllerList.controller_3_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller 3 Object Type"] = value

    @property
    def controller_3_name(self):
        """Get controller_3_name

        Returns:
            str: the value of `controller_3_name` or None if not set
        """
        return self._data["Controller 3 Name"]

    @controller_3_name.setter
    def controller_3_name(self, value=None):
        """  Corresponds to IDD Field `Controller 3 Name`

        Args:
            value (str): value for IDD Field `Controller 3 Name`
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
                                 ' for field `AirLoopHvacControllerList.controller_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_3_name`')
        self._data["Controller 3 Name"] = value

    @property
    def controller_4_object_type(self):
        """Get controller_4_object_type

        Returns:
            str: the value of `controller_4_object_type` or None if not set
        """
        return self._data["Controller 4 Object Type"]

    @controller_4_object_type.setter
    def controller_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller 4 Object Type`

        Args:
            value (str): value for IDD Field `Controller 4 Object Type`
                Accepted values are:
                      - Controller:WaterCoil
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
                                 ' for field `AirLoopHvacControllerList.controller_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_4_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
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
                                     'field `AirLoopHvacControllerList.controller_4_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirLoopHvacControllerList.controller_4_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller 4 Object Type"] = value

    @property
    def controller_4_name(self):
        """Get controller_4_name

        Returns:
            str: the value of `controller_4_name` or None if not set
        """
        return self._data["Controller 4 Name"]

    @controller_4_name.setter
    def controller_4_name(self, value=None):
        """  Corresponds to IDD Field `Controller 4 Name`

        Args:
            value (str): value for IDD Field `Controller 4 Name`
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
                                 ' for field `AirLoopHvacControllerList.controller_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_4_name`')
        self._data["Controller 4 Name"] = value

    @property
    def controller_5_object_type(self):
        """Get controller_5_object_type

        Returns:
            str: the value of `controller_5_object_type` or None if not set
        """
        return self._data["Controller 5 Object Type"]

    @controller_5_object_type.setter
    def controller_5_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller 5 Object Type`

        Args:
            value (str): value for IDD Field `Controller 5 Object Type`
                Accepted values are:
                      - Controller:WaterCoil
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
                                 ' for field `AirLoopHvacControllerList.controller_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_5_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
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
                                     'field `AirLoopHvacControllerList.controller_5_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirLoopHvacControllerList.controller_5_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller 5 Object Type"] = value

    @property
    def controller_5_name(self):
        """Get controller_5_name

        Returns:
            str: the value of `controller_5_name` or None if not set
        """
        return self._data["Controller 5 Name"]

    @controller_5_name.setter
    def controller_5_name(self, value=None):
        """  Corresponds to IDD Field `Controller 5 Name`

        Args:
            value (str): value for IDD Field `Controller 5 Name`
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
                                 ' for field `AirLoopHvacControllerList.controller_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_5_name`')
        self._data["Controller 5 Name"] = value

    @property
    def controller_6_object_type(self):
        """Get controller_6_object_type

        Returns:
            str: the value of `controller_6_object_type` or None if not set
        """
        return self._data["Controller 6 Object Type"]

    @controller_6_object_type.setter
    def controller_6_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller 6 Object Type`

        Args:
            value (str): value for IDD Field `Controller 6 Object Type`
                Accepted values are:
                      - Controller:WaterCoil
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
                                 ' for field `AirLoopHvacControllerList.controller_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_6_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
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
                                     'field `AirLoopHvacControllerList.controller_6_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirLoopHvacControllerList.controller_6_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller 6 Object Type"] = value

    @property
    def controller_6_name(self):
        """Get controller_6_name

        Returns:
            str: the value of `controller_6_name` or None if not set
        """
        return self._data["Controller 6 Name"]

    @controller_6_name.setter
    def controller_6_name(self, value=None):
        """  Corresponds to IDD Field `Controller 6 Name`

        Args:
            value (str): value for IDD Field `Controller 6 Name`
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
                                 ' for field `AirLoopHvacControllerList.controller_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_6_name`')
        self._data["Controller 6 Name"] = value

    @property
    def controller_7_object_type(self):
        """Get controller_7_object_type

        Returns:
            str: the value of `controller_7_object_type` or None if not set
        """
        return self._data["Controller 7 Object Type"]

    @controller_7_object_type.setter
    def controller_7_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller 7 Object Type`

        Args:
            value (str): value for IDD Field `Controller 7 Object Type`
                Accepted values are:
                      - Controller:WaterCoil
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
                                 ' for field `AirLoopHvacControllerList.controller_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_7_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
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
                                     'field `AirLoopHvacControllerList.controller_7_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirLoopHvacControllerList.controller_7_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller 7 Object Type"] = value

    @property
    def controller_7_name(self):
        """Get controller_7_name

        Returns:
            str: the value of `controller_7_name` or None if not set
        """
        return self._data["Controller 7 Name"]

    @controller_7_name.setter
    def controller_7_name(self, value=None):
        """  Corresponds to IDD Field `Controller 7 Name`

        Args:
            value (str): value for IDD Field `Controller 7 Name`
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
                                 ' for field `AirLoopHvacControllerList.controller_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_7_name`')
        self._data["Controller 7 Name"] = value

    @property
    def controller_8_object_type(self):
        """Get controller_8_object_type

        Returns:
            str: the value of `controller_8_object_type` or None if not set
        """
        return self._data["Controller 8 Object Type"]

    @controller_8_object_type.setter
    def controller_8_object_type(self, value=None):
        """  Corresponds to IDD Field `Controller 8 Object Type`

        Args:
            value (str): value for IDD Field `Controller 8 Object Type`
                Accepted values are:
                      - Controller:WaterCoil
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
                                 ' for field `AirLoopHvacControllerList.controller_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_8_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
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
                                     'field `AirLoopHvacControllerList.controller_8_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirLoopHvacControllerList.controller_8_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Controller 8 Object Type"] = value

    @property
    def controller_8_name(self):
        """Get controller_8_name

        Returns:
            str: the value of `controller_8_name` or None if not set
        """
        return self._data["Controller 8 Name"]

    @controller_8_name.setter
    def controller_8_name(self, value=None):
        """  Corresponds to IDD Field `Controller 8 Name`

        Args:
            value (str): value for IDD Field `Controller 8 Name`
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
                                 ' for field `AirLoopHvacControllerList.controller_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacControllerList.controller_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacControllerList.controller_8_name`')
        self._data["Controller 8 Name"] = value

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
                    raise ValueError("Required field AirLoopHvacControllerList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirLoopHvacControllerList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirLoopHvacControllerList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirLoopHvacControllerList: {} / {}".format(out_fields,
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