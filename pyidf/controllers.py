from collections import OrderedDict

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `control_variable`
        keys HumidityRatio or TemperatureAndHumidityRatio
        requires a ZoneControl:Humidistat object along
        with SetpointManager:SingleZone:Humidity:Maximum,
        SetpointManager:MultiZone:MaximumHumidity:Average, or
        SetpointManager:Multizone:Humidity:Maximum object

        Args:
            value (str): value for IDD Field `control_variable`
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
            except:
                raise ValueError('value {} need to be of type str '
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
            vals["temperatureandhumidityratio"] = "TemperatureAndHumidityRatio"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `control_variable`'.format(value))
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
        """  Corresponds to IDD Field `action`
        Leave blank to have this automatically selected from coil type.
        Chilled water coils should be reverse action
        Hot water coils should be normal action

        Args:
            value (str): value for IDD Field `action`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `action`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `action`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `action`')
            vals = {}
            vals["normal"] = "Normal"
            vals["reverse"] = "Reverse"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `action`'.format(value))
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
        """  Corresponds to IDD Field `actuator_variable`

        Args:
            value (str): value for IDD Field `actuator_variable`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `actuator_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuator_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `actuator_variable`')
            vals = {}
            vals["flow"] = "Flow"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `actuator_variable`'.format(value))
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
        """  Corresponds to IDD Field `sensor_node_name`

        Args:
            value (str): value for IDD Field `sensor_node_name`
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
                                 'for field `sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sensor_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `sensor_node_name`')

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
        """  Corresponds to IDD Field `actuator_node_name`

        Args:
            value (str): value for IDD Field `actuator_node_name`
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
                                 'for field `actuator_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuator_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `actuator_node_name`')

        self._data["Actuator Node Name"] = value

    @property
    def controller_convergence_tolerance(self):
        """Get controller_convergence_tolerance

        Returns:
            float: the value of `controller_convergence_tolerance` or None if not set
        """
        return self._data["Controller Convergence Tolerance"]

    @controller_convergence_tolerance.setter
    def controller_convergence_tolerance(self, value=None):
        """  Corresponds to IDD Field `controller_convergence_tolerance`

        Args:
            value (float): value for IDD Field `controller_convergence_tolerance`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `controller_convergence_tolerance`'.format(value))

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
        """  Corresponds to IDD Field `maximum_actuated_flow`

        Args:
            value (float): value for IDD Field `maximum_actuated_flow`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_actuated_flow`'.format(value))

        self._data["Maximum Actuated Flow"] = value

    @property
    def minimum_actuated_flow(self):
        """Get minimum_actuated_flow

        Returns:
            float: the value of `minimum_actuated_flow` or None if not set
        """
        return self._data["Minimum Actuated Flow"]

    @minimum_actuated_flow.setter
    def minimum_actuated_flow(self, value=1e-07 ):
        """  Corresponds to IDD Field `minimum_actuated_flow`

        Args:
            value (float): value for IDD Field `minimum_actuated_flow`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_actuated_flow`'.format(value))

        self._data["Minimum Actuated Flow"] = value

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

class ControllerOutdoorAir(object):
    """ Corresponds to IDD object `Controller:OutdoorAir`
        Controller to set the outdoor air flow rate for an air loop. Control options include
        fixed, proportional, scheduled, economizer, and demand-controlled ventilation.
    
    """
    internal_name = "Controller:OutdoorAir"
    field_count = 26
    required_fields = ["Name", "Relief Air Outlet Node Name", "Return Air Node Name", "Mixed Air Node Name", "Actuator Node Name", "Minimum Outdoor Air Flow Rate", "Maximum Outdoor Air Flow Rate"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `relief_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `relief_air_outlet_node_name`
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
                                 'for field `relief_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `relief_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `relief_air_outlet_node_name`')

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
        """  Corresponds to IDD Field `return_air_node_name`

        Args:
            value (str): value for IDD Field `return_air_node_name`
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
                                 'for field `return_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `return_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `return_air_node_name`')

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
        """  Corresponds to IDD Field `mixed_air_node_name`

        Args:
            value (str): value for IDD Field `mixed_air_node_name`
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
                                 'for field `mixed_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `mixed_air_node_name`')

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
        """  Corresponds to IDD Field `actuator_node_name`
        Outdoor air inlet node entering the first pre-treat component if any

        Args:
            value (str): value for IDD Field `actuator_node_name`
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
                                 'for field `actuator_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `actuator_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `actuator_node_name`')

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
        """  Corresponds to IDD Field `minimum_outdoor_air_flow_rate`

        Args:
            value (float): value for IDD Field `minimum_outdoor_air_flow_rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_outdoor_air_flow_rate`'.format(value))

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
        """  Corresponds to IDD Field `maximum_outdoor_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_outdoor_air_flow_rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_outdoor_air_flow_rate`'.format(value))

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
        """  Corresponds to IDD Field `economizer_control_type`

        Args:
            value (str): value for IDD Field `economizer_control_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `economizer_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `economizer_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `economizer_control_type`')
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
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `economizer_control_type`'.format(value))
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
        """  Corresponds to IDD Field `economizer_control_action_type`

        Args:
            value (str): value for IDD Field `economizer_control_action_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `economizer_control_action_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `economizer_control_action_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `economizer_control_action_type`')
            vals = {}
            vals["modulateflow"] = "ModulateFlow"
            vals["minimumflowwithbypass"] = "MinimumFlowWithBypass"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `economizer_control_action_type`'.format(value))
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
        """  Corresponds to IDD Field `economizer_maximum_limit_drybulb_temperature`
        Enter the maximum outdoor dry-bulb temperature limit for FixedDryBulb
        economizer control type. No input or blank input means this limit is
        not operative. Limit is applied regardless of economizer control type.

        Args:
            value (float): value for IDD Field `economizer_maximum_limit_drybulb_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `economizer_maximum_limit_drybulb_temperature`'.format(value))

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
        """  Corresponds to IDD Field `economizer_maximum_limit_enthalpy`
        Enter the maximum outdoor enthalpy limit for FixedEnthalpy economizer control type.
        No input or blank input means this limit is not operative
        Limit is applied regardless of economizer control type.

        Args:
            value (float): value for IDD Field `economizer_maximum_limit_enthalpy`
                Units: J/kg
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `economizer_maximum_limit_enthalpy`'.format(value))

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
        """  Corresponds to IDD Field `economizer_maximum_limit_dewpoint_temperature`
        Enter the maximum outdoor dewpoint temperature limit for FixedDewPointAndDryBulb
        economizer control type. No input or blank input means this limit is not operative.
        Limit is applied regardless of economizer control type.

        Args:
            value (float): value for IDD Field `economizer_maximum_limit_dewpoint_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `economizer_maximum_limit_dewpoint_temperature`'.format(value))

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
        """  Corresponds to IDD Field `electronic_enthalpy_limit_curve_name`
        Table:OneIndependentVariable object can also be used
        Enter the name of a quadratic or cubic curve which defines the maximum outdoor
        humidity ratio (function of outdoor dry-bulb temperature) for ElectronicEnthalpy
        economizer control type. No input or blank input means this limit is not operative
        Limit is applied regardless of economizer control type.

        Args:
            value (str): value for IDD Field `electronic_enthalpy_limit_curve_name`
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
                                 'for field `electronic_enthalpy_limit_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electronic_enthalpy_limit_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electronic_enthalpy_limit_curve_name`')

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
        """  Corresponds to IDD Field `economizer_minimum_limit_drybulb_temperature`
        Enter the minimum outdoor dry-bulb temperature limit for economizer control.
        No input or blank input means this limit is not operative
        Limit is applied regardless of economizer control type.

        Args:
            value (float): value for IDD Field `economizer_minimum_limit_drybulb_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `economizer_minimum_limit_drybulb_temperature`'.format(value))

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
        """  Corresponds to IDD Field `lockout_type`

        Args:
            value (str): value for IDD Field `lockout_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `lockout_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lockout_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lockout_type`')
            vals = {}
            vals["nolockout"] = "NoLockout"
            vals["lockoutwithheating"] = "LockoutWithHeating"
            vals["lockoutwithcompressor"] = "LockoutWithCompressor"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `lockout_type`'.format(value))
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
        """  Corresponds to IDD Field `minimum_limit_type`

        Args:
            value (str): value for IDD Field `minimum_limit_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_limit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_limit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_limit_type`')
            vals = {}
            vals["fixedminimum"] = "FixedMinimum"
            vals["proportionalminimum"] = "ProportionalMinimum"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `minimum_limit_type`'.format(value))
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
        """  Corresponds to IDD Field `minimum_outdoor_air_schedule_name`
        Schedule values multiply the minimum outdoor air flow rate

        Args:
            value (str): value for IDD Field `minimum_outdoor_air_schedule_name`
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
                                 'for field `minimum_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_outdoor_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_outdoor_air_schedule_name`')

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
        """  Corresponds to IDD Field `minimum_fraction_of_outdoor_air_schedule_name`
        schedule values multiply the design/mixed air flow rate

        Args:
            value (str): value for IDD Field `minimum_fraction_of_outdoor_air_schedule_name`
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
                                 'for field `minimum_fraction_of_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_fraction_of_outdoor_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_fraction_of_outdoor_air_schedule_name`')

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
        """  Corresponds to IDD Field `maximum_fraction_of_outdoor_air_schedule_name`
        schedule values multiply the design/mixed air flow rate

        Args:
            value (str): value for IDD Field `maximum_fraction_of_outdoor_air_schedule_name`
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
                                 'for field `maximum_fraction_of_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_fraction_of_outdoor_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `maximum_fraction_of_outdoor_air_schedule_name`')

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
        """  Corresponds to IDD Field `mechanical_ventilation_controller_name`
        Enter the name of a Controller:MechanicalVentilation object.
        Optional field for defining outdoor ventilation air based on flow rate per unit floor
        area and flow rate per person. Simplified method of demand-controlled ventilation.

        Args:
            value (str): value for IDD Field `mechanical_ventilation_controller_name`
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
                                 'for field `mechanical_ventilation_controller_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_ventilation_controller_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `mechanical_ventilation_controller_name`')

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
        """  Corresponds to IDD Field `time_of_day_economizer_control_schedule_name`
        Optional schedule to simulate "push-button" type economizer control.
        Schedule values greater than 0 indicate time-of-day economizer control is enabled.
        Economizer control may be used with or without the high humidity control option.
        When used together, high humidity control has priority over economizer control.
        If the field Economizer Control Type = NoEconomizer, then this option is disabled.

        Args:
            value (str): value for IDD Field `time_of_day_economizer_control_schedule_name`
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
                                 'for field `time_of_day_economizer_control_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_of_day_economizer_control_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `time_of_day_economizer_control_schedule_name`')

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
        """  Corresponds to IDD Field `high_humidity_control`
        Optional field to enable modified outdoor air flow rates based on zone relative humidity.
        Select Yes to modify outdoor air flow rate based on a zone humidistat.
        Select No to disable this feature.
        If the field Economizer Control Type = NoEconomizer, then this option is disabled.

        Args:
            value (str): value for IDD Field `high_humidity_control`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `high_humidity_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `high_humidity_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `high_humidity_control`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `high_humidity_control`'.format(value))
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
        """  Corresponds to IDD Field `humidistat_control_zone_name`
        Enter the name of the zone where the humidistat is located.
        This field is only used when the field High Humidity Control = Yes.

        Args:
            value (str): value for IDD Field `humidistat_control_zone_name`
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
                                 'for field `humidistat_control_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `humidistat_control_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `humidistat_control_zone_name`')

        self._data["Humidistat Control Zone Name"] = value

    @property
    def high_humidity_outdoor_air_flow_ratio(self):
        """Get high_humidity_outdoor_air_flow_ratio

        Returns:
            float: the value of `high_humidity_outdoor_air_flow_ratio` or None if not set
        """
        return self._data["High Humidity Outdoor Air Flow Ratio"]

    @high_humidity_outdoor_air_flow_ratio.setter
    def high_humidity_outdoor_air_flow_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `high_humidity_outdoor_air_flow_ratio`
        Enter the ratio of outdoor air to the maximum outdoor air flow rate when modified air
        flow rates are active based on high indoor humidity.
        The minimum value must be greater than 0.
        This field is only used when the field High Humidity Control = Yes.

        Args:
            value (float): value for IDD Field `high_humidity_outdoor_air_flow_ratio`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `high_humidity_outdoor_air_flow_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `high_humidity_outdoor_air_flow_ratio`')

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
        """  Corresponds to IDD Field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`
        If No is selected, the outdoor air flow rate is modified any time indoor relative
        humidity is above the humidistat setpoint. If Yes is selected, the outdoor air
        flow rate is modified any time the indoor relative humidity is above the humidistat
        setpoint and the outdoor humidity ratio is less than the indoor humidity ratio.
        This field is only used when the field High Humidity Control = Yes.

        Args:
            value (str): value for IDD Field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `control_high_indoor_humidity_based_on_outdoor_humidity_ratio`'.format(value))
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
        """  Corresponds to IDD Field `heat_recovery_bypass_control_type`
        BypassWhenWithinEconomizerLimits specifies that heat recovery
        is active only when the economizer is off because conditions
        are outside the economizer control limits
        BypassWhenOAFlowGreaterThanMinimum specifies enhanced economizer
        controls to allow heat recovery when economizer is active
        (within limits) but the outdoor air flow rate is at the minimum.

        Args:
            value (str): value for IDD Field `heat_recovery_bypass_control_type`
                Default value: BypassWhenWithinEconomizerLimits
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
                                 'for field `heat_recovery_bypass_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_bypass_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_recovery_bypass_control_type`')

        self._data["Heat Recovery Bypass Control Type"] = value

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
    field_count = 155
    required_fields = ["Name", "Zone 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Controller:MechanicalVentilation`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Demand Controlled Ventilation"] = None
        self._data["System Outdoor Air Method"] = None
        self._data["Zone Maximum Outdoor Air Fraction"] = None
        self._data["Zone 1 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 1"] = None
        self._data["Design Specification Zone Air Distribution Object Name 1"] = None
        self._data["Zone 2 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 2"] = None
        self._data["Design Specification Zone Air Distribution Object Name 2"] = None
        self._data["Zone 3 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 3"] = None
        self._data["Design Specification Zone Air Distribution Object Name 3"] = None
        self._data["Zone 4 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 4"] = None
        self._data["Design Specification Zone Air Distribution Object Name 4"] = None
        self._data["Zone 5 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 5"] = None
        self._data["Design Specification Zone Air Distribution Object Name 5"] = None
        self._data["Zone 6 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 6"] = None
        self._data["Design Specification Zone Air Distribution Object Name 6"] = None
        self._data["Zone 7 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 7"] = None
        self._data["Design Specification Zone Air Distribution Object Name 7"] = None
        self._data["Zone 8 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 8"] = None
        self._data["Design Specification Zone Air Distribution Object Name 8"] = None
        self._data["Zone 9 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 9"] = None
        self._data["Design Specification Zone Air Distribution Object Name 9"] = None
        self._data["Zone 10 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 10"] = None
        self._data["Design Specification Zone Air Distribution Object Name 10"] = None
        self._data["Zone 11 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 11"] = None
        self._data["Design Specification Zone Air Distribution Object Name 11"] = None
        self._data["Zone 12 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 12"] = None
        self._data["Design Specification Zone Air Distribution Object Name 12"] = None
        self._data["Zone 13 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 13"] = None
        self._data["Design Specification Zone Air Distribution Object Name 13"] = None
        self._data["Zone 14 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 14"] = None
        self._data["Design Specification Zone Air Distribution Object Name 14"] = None
        self._data["Zone 15 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 15"] = None
        self._data["Design Specification Zone Air Distribution Object Name 15"] = None
        self._data["Zone 16 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 16"] = None
        self._data["Design Specification Zone Air Distribution Object Name 16"] = None
        self._data["Zone 17 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 17"] = None
        self._data["Design Specification Zone Air Distribution Object Name 17"] = None
        self._data["Zone 18 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 18"] = None
        self._data["Design Specification Zone Air Distribution Object Name 18"] = None
        self._data["Zone 19 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 19"] = None
        self._data["Design Specification Zone Air Distribution Object Name 19"] = None
        self._data["Zone 20 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 20"] = None
        self._data["Design Specification Zone Air Distribution Object Name 20"] = None
        self._data["Zone 21 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 21"] = None
        self._data["Design Specification Zone Air Distribution Object Name 21"] = None
        self._data["Zone 22 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 22"] = None
        self._data["Design Specification Zone Air Distribution Object Name 22"] = None
        self._data["Zone 23 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 23"] = None
        self._data["Design Specification Zone Air Distribution Object Name 23"] = None
        self._data["Zone 24 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 24"] = None
        self._data["Design Specification Zone Air Distribution Object Name 24"] = None
        self._data["Zone 25 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 25"] = None
        self._data["Design Specification Zone Air Distribution Object Name 25"] = None
        self._data["Zone 26 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 26"] = None
        self._data["Design Specification Zone Air Distribution Object Name 26"] = None
        self._data["Zone 27 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 27"] = None
        self._data["Design Specification Zone Air Distribution Object Name 27"] = None
        self._data["Zone 28 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 28"] = None
        self._data["Design Specification Zone Air Distribution Object Name 28"] = None
        self._data["Zone 29 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 29"] = None
        self._data["Design Specification Zone Air Distribution Object Name 29"] = None
        self._data["Zone 30 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 30"] = None
        self._data["Design Specification Zone Air Distribution Object Name 30"] = None
        self._data["Zone 31 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 31"] = None
        self._data["Design Specification Zone Air Distribution Object Name 31"] = None
        self._data["Zone 32 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 32"] = None
        self._data["Design Specification Zone Air Distribution Object Name 32"] = None
        self._data["Zone 33 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 33"] = None
        self._data["Design Specification Zone Air Distribution Object Name 33"] = None
        self._data["Zone 34 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 34"] = None
        self._data["Design Specification Zone Air Distribution Object Name 34"] = None
        self._data["Zone 35 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 35"] = None
        self._data["Design Specification Zone Air Distribution Object Name 35"] = None
        self._data["Zone 36 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 36"] = None
        self._data["Design Specification Zone Air Distribution Object Name 36"] = None
        self._data["Zone 37 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 37"] = None
        self._data["Design Specification Zone Air Distribution Object Name 37"] = None
        self._data["Zone 38 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 38"] = None
        self._data["Design Specification Zone Air Distribution Object Name 38"] = None
        self._data["Zone 39 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 39"] = None
        self._data["Design Specification Zone Air Distribution Object Name 39"] = None
        self._data["Zone 40 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 40"] = None
        self._data["Design Specification Zone Air Distribution Object Name 40"] = None
        self._data["Zone 41 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 41"] = None
        self._data["Design Specification Zone Air Distribution Object Name 41"] = None
        self._data["Zone 42 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 42"] = None
        self._data["Design Specification Zone Air Distribution Object Name 42"] = None
        self._data["Zone 43 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 43"] = None
        self._data["Design Specification Zone Air Distribution Object Name 43"] = None
        self._data["Zone 44 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 44"] = None
        self._data["Design Specification Zone Air Distribution Object Name 44"] = None
        self._data["Zone 45 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 45"] = None
        self._data["Design Specification Zone Air Distribution Object Name 45"] = None
        self._data["Zone 46 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 46"] = None
        self._data["Design Specification Zone Air Distribution Object Name 46"] = None
        self._data["Zone 47 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 47"] = None
        self._data["Design Specification Zone Air Distribution Object Name 47"] = None
        self._data["Zone 48 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 48"] = None
        self._data["Design Specification Zone Air Distribution Object Name 48"] = None
        self._data["Zone 49 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 49"] = None
        self._data["Design Specification Zone Air Distribution Object Name 49"] = None
        self._data["Zone 50 Name"] = None
        self._data["Design Specification Outdoor Air Object Name 50"] = None
        self._data["Design Specification Zone Air Distribution Object Name 50"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        if len(vals[i]) == 0:
            self.zone_1_name = None
        else:
            self.zone_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_1 = None
        else:
            self.design_specification_outdoor_air_object_name_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_1 = None
        else:
            self.design_specification_zone_air_distribution_object_name_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_2_name = None
        else:
            self.zone_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_2 = None
        else:
            self.design_specification_outdoor_air_object_name_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_2 = None
        else:
            self.design_specification_zone_air_distribution_object_name_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_3_name = None
        else:
            self.zone_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_3 = None
        else:
            self.design_specification_outdoor_air_object_name_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_3 = None
        else:
            self.design_specification_zone_air_distribution_object_name_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_4_name = None
        else:
            self.zone_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_4 = None
        else:
            self.design_specification_outdoor_air_object_name_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_4 = None
        else:
            self.design_specification_zone_air_distribution_object_name_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_5_name = None
        else:
            self.zone_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_5 = None
        else:
            self.design_specification_outdoor_air_object_name_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_5 = None
        else:
            self.design_specification_zone_air_distribution_object_name_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_6_name = None
        else:
            self.zone_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_6 = None
        else:
            self.design_specification_outdoor_air_object_name_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_6 = None
        else:
            self.design_specification_zone_air_distribution_object_name_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_7_name = None
        else:
            self.zone_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_7 = None
        else:
            self.design_specification_outdoor_air_object_name_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_7 = None
        else:
            self.design_specification_zone_air_distribution_object_name_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_8_name = None
        else:
            self.zone_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_8 = None
        else:
            self.design_specification_outdoor_air_object_name_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_8 = None
        else:
            self.design_specification_zone_air_distribution_object_name_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_9_name = None
        else:
            self.zone_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_9 = None
        else:
            self.design_specification_outdoor_air_object_name_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_9 = None
        else:
            self.design_specification_zone_air_distribution_object_name_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_10_name = None
        else:
            self.zone_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_10 = None
        else:
            self.design_specification_outdoor_air_object_name_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_10 = None
        else:
            self.design_specification_zone_air_distribution_object_name_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_11_name = None
        else:
            self.zone_11_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_11 = None
        else:
            self.design_specification_outdoor_air_object_name_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_11 = None
        else:
            self.design_specification_zone_air_distribution_object_name_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_12_name = None
        else:
            self.zone_12_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_12 = None
        else:
            self.design_specification_outdoor_air_object_name_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_12 = None
        else:
            self.design_specification_zone_air_distribution_object_name_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_13_name = None
        else:
            self.zone_13_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_13 = None
        else:
            self.design_specification_outdoor_air_object_name_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_13 = None
        else:
            self.design_specification_zone_air_distribution_object_name_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_14_name = None
        else:
            self.zone_14_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_14 = None
        else:
            self.design_specification_outdoor_air_object_name_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_14 = None
        else:
            self.design_specification_zone_air_distribution_object_name_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_15_name = None
        else:
            self.zone_15_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_15 = None
        else:
            self.design_specification_outdoor_air_object_name_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_15 = None
        else:
            self.design_specification_zone_air_distribution_object_name_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_16_name = None
        else:
            self.zone_16_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_16 = None
        else:
            self.design_specification_outdoor_air_object_name_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_16 = None
        else:
            self.design_specification_zone_air_distribution_object_name_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_17_name = None
        else:
            self.zone_17_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_17 = None
        else:
            self.design_specification_outdoor_air_object_name_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_17 = None
        else:
            self.design_specification_zone_air_distribution_object_name_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_18_name = None
        else:
            self.zone_18_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_18 = None
        else:
            self.design_specification_outdoor_air_object_name_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_18 = None
        else:
            self.design_specification_zone_air_distribution_object_name_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_19_name = None
        else:
            self.zone_19_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_19 = None
        else:
            self.design_specification_outdoor_air_object_name_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_19 = None
        else:
            self.design_specification_zone_air_distribution_object_name_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_20_name = None
        else:
            self.zone_20_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_20 = None
        else:
            self.design_specification_outdoor_air_object_name_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_20 = None
        else:
            self.design_specification_zone_air_distribution_object_name_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_21_name = None
        else:
            self.zone_21_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_21 = None
        else:
            self.design_specification_outdoor_air_object_name_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_21 = None
        else:
            self.design_specification_zone_air_distribution_object_name_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_22_name = None
        else:
            self.zone_22_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_22 = None
        else:
            self.design_specification_outdoor_air_object_name_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_22 = None
        else:
            self.design_specification_zone_air_distribution_object_name_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_23_name = None
        else:
            self.zone_23_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_23 = None
        else:
            self.design_specification_outdoor_air_object_name_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_23 = None
        else:
            self.design_specification_zone_air_distribution_object_name_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_24_name = None
        else:
            self.zone_24_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_24 = None
        else:
            self.design_specification_outdoor_air_object_name_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_24 = None
        else:
            self.design_specification_zone_air_distribution_object_name_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_25_name = None
        else:
            self.zone_25_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_25 = None
        else:
            self.design_specification_outdoor_air_object_name_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_25 = None
        else:
            self.design_specification_zone_air_distribution_object_name_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_26_name = None
        else:
            self.zone_26_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_26 = None
        else:
            self.design_specification_outdoor_air_object_name_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_26 = None
        else:
            self.design_specification_zone_air_distribution_object_name_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_27_name = None
        else:
            self.zone_27_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_27 = None
        else:
            self.design_specification_outdoor_air_object_name_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_27 = None
        else:
            self.design_specification_zone_air_distribution_object_name_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_28_name = None
        else:
            self.zone_28_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_28 = None
        else:
            self.design_specification_outdoor_air_object_name_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_28 = None
        else:
            self.design_specification_zone_air_distribution_object_name_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_29_name = None
        else:
            self.zone_29_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_29 = None
        else:
            self.design_specification_outdoor_air_object_name_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_29 = None
        else:
            self.design_specification_zone_air_distribution_object_name_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_30_name = None
        else:
            self.zone_30_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_30 = None
        else:
            self.design_specification_outdoor_air_object_name_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_30 = None
        else:
            self.design_specification_zone_air_distribution_object_name_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_31_name = None
        else:
            self.zone_31_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_31 = None
        else:
            self.design_specification_outdoor_air_object_name_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_31 = None
        else:
            self.design_specification_zone_air_distribution_object_name_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_32_name = None
        else:
            self.zone_32_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_32 = None
        else:
            self.design_specification_outdoor_air_object_name_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_32 = None
        else:
            self.design_specification_zone_air_distribution_object_name_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_33_name = None
        else:
            self.zone_33_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_33 = None
        else:
            self.design_specification_outdoor_air_object_name_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_33 = None
        else:
            self.design_specification_zone_air_distribution_object_name_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_34_name = None
        else:
            self.zone_34_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_34 = None
        else:
            self.design_specification_outdoor_air_object_name_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_34 = None
        else:
            self.design_specification_zone_air_distribution_object_name_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_35_name = None
        else:
            self.zone_35_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_35 = None
        else:
            self.design_specification_outdoor_air_object_name_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_35 = None
        else:
            self.design_specification_zone_air_distribution_object_name_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_36_name = None
        else:
            self.zone_36_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_36 = None
        else:
            self.design_specification_outdoor_air_object_name_36 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_36 = None
        else:
            self.design_specification_zone_air_distribution_object_name_36 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_37_name = None
        else:
            self.zone_37_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_37 = None
        else:
            self.design_specification_outdoor_air_object_name_37 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_37 = None
        else:
            self.design_specification_zone_air_distribution_object_name_37 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_38_name = None
        else:
            self.zone_38_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_38 = None
        else:
            self.design_specification_outdoor_air_object_name_38 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_38 = None
        else:
            self.design_specification_zone_air_distribution_object_name_38 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_39_name = None
        else:
            self.zone_39_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_39 = None
        else:
            self.design_specification_outdoor_air_object_name_39 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_39 = None
        else:
            self.design_specification_zone_air_distribution_object_name_39 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_40_name = None
        else:
            self.zone_40_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_40 = None
        else:
            self.design_specification_outdoor_air_object_name_40 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_40 = None
        else:
            self.design_specification_zone_air_distribution_object_name_40 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_41_name = None
        else:
            self.zone_41_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_41 = None
        else:
            self.design_specification_outdoor_air_object_name_41 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_41 = None
        else:
            self.design_specification_zone_air_distribution_object_name_41 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_42_name = None
        else:
            self.zone_42_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_42 = None
        else:
            self.design_specification_outdoor_air_object_name_42 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_42 = None
        else:
            self.design_specification_zone_air_distribution_object_name_42 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_43_name = None
        else:
            self.zone_43_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_43 = None
        else:
            self.design_specification_outdoor_air_object_name_43 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_43 = None
        else:
            self.design_specification_zone_air_distribution_object_name_43 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_44_name = None
        else:
            self.zone_44_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_44 = None
        else:
            self.design_specification_outdoor_air_object_name_44 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_44 = None
        else:
            self.design_specification_zone_air_distribution_object_name_44 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_45_name = None
        else:
            self.zone_45_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_45 = None
        else:
            self.design_specification_outdoor_air_object_name_45 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_45 = None
        else:
            self.design_specification_zone_air_distribution_object_name_45 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_46_name = None
        else:
            self.zone_46_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_46 = None
        else:
            self.design_specification_outdoor_air_object_name_46 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_46 = None
        else:
            self.design_specification_zone_air_distribution_object_name_46 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_47_name = None
        else:
            self.zone_47_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_47 = None
        else:
            self.design_specification_outdoor_air_object_name_47 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_47 = None
        else:
            self.design_specification_zone_air_distribution_object_name_47 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_48_name = None
        else:
            self.zone_48_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_48 = None
        else:
            self.design_specification_outdoor_air_object_name_48 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_48 = None
        else:
            self.design_specification_zone_air_distribution_object_name_48 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_49_name = None
        else:
            self.zone_49_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_49 = None
        else:
            self.design_specification_outdoor_air_object_name_49 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_49 = None
        else:
            self.design_specification_zone_air_distribution_object_name_49 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_50_name = None
        else:
            self.zone_50_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name_50 = None
        else:
            self.design_specification_outdoor_air_object_name_50 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name_50 = None
        else:
            self.design_specification_zone_air_distribution_object_name_50 = vals[i]
        i += 1
        if i >= len(vals):
            return

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `availability_schedule_name`
        If this field is blank, the controller uses the values from the associated Controller:OutdoorAir.
        Schedule values greater than 0 indicate mechanical ventilation is enabled

        Args:
            value (str): value for IDD Field `availability_schedule_name`
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
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `demand_controlled_ventilation`

        Args:
            value (str): value for IDD Field `demand_controlled_ventilation`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_controlled_ventilation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_controlled_ventilation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_controlled_ventilation`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demand_controlled_ventilation`'.format(value))
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
        """  Corresponds to IDD Field `system_outdoor_air_method`

        Args:
            value (str): value for IDD Field `system_outdoor_air_method`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `system_outdoor_air_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `system_outdoor_air_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `system_outdoor_air_method`')
            vals = {}
            vals["zonesum"] = "ZoneSum"
            vals["ventilationrateprocedure"] = "VentilationRateProcedure"
            vals["indoorairqualityprocedure"] = "IndoorAirQualityProcedure"
            vals["proportionalcontrol"] = "ProportionalControl"
            vals["indoorairqualityproceduregenericcontaminant"] = "IndoorAirQualityProcedureGenericContaminant"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `system_outdoor_air_method`'.format(value))
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
    def zone_maximum_outdoor_air_fraction(self, value=1.0 ):
        """  Corresponds to IDD Field `zone_maximum_outdoor_air_fraction`

        Args:
            value (float): value for IDD Field `zone_maximum_outdoor_air_fraction`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `zone_maximum_outdoor_air_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `zone_maximum_outdoor_air_fraction`')

        self._data["Zone Maximum Outdoor Air Fraction"] = value

    @property
    def zone_1_name(self):
        """Get zone_1_name

        Returns:
            str: the value of `zone_1_name` or None if not set
        """
        return self._data["Zone 1 Name"]

    @zone_1_name.setter
    def zone_1_name(self, value=None):
        """  Corresponds to IDD Field `zone_1_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_1_name`
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
                                 'for field `zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_1_name`')

        self._data["Zone 1 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_1(self):
        """Get design_specification_outdoor_air_object_name_1

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_1` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 1"]

    @design_specification_outdoor_air_object_name_1.setter
    def design_specification_outdoor_air_object_name_1(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_1`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_1`
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
                                 'for field `design_specification_outdoor_air_object_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_1`')

        self._data["Design Specification Outdoor Air Object Name 1"] = value

    @property
    def design_specification_zone_air_distribution_object_name_1(self):
        """Get design_specification_zone_air_distribution_object_name_1

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_1` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 1"]

    @design_specification_zone_air_distribution_object_name_1.setter
    def design_specification_zone_air_distribution_object_name_1(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_1`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_1`
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
                                 'for field `design_specification_zone_air_distribution_object_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_1`')

        self._data["Design Specification Zone Air Distribution Object Name 1"] = value

    @property
    def zone_2_name(self):
        """Get zone_2_name

        Returns:
            str: the value of `zone_2_name` or None if not set
        """
        return self._data["Zone 2 Name"]

    @zone_2_name.setter
    def zone_2_name(self, value=None):
        """  Corresponds to IDD Field `zone_2_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_2_name`
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
                                 'for field `zone_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_2_name`')

        self._data["Zone 2 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_2(self):
        """Get design_specification_outdoor_air_object_name_2

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_2` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 2"]

    @design_specification_outdoor_air_object_name_2.setter
    def design_specification_outdoor_air_object_name_2(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_2`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_2`
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
                                 'for field `design_specification_outdoor_air_object_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_2`')

        self._data["Design Specification Outdoor Air Object Name 2"] = value

    @property
    def design_specification_zone_air_distribution_object_name_2(self):
        """Get design_specification_zone_air_distribution_object_name_2

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_2` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 2"]

    @design_specification_zone_air_distribution_object_name_2.setter
    def design_specification_zone_air_distribution_object_name_2(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_2`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_2`
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
                                 'for field `design_specification_zone_air_distribution_object_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_2`')

        self._data["Design Specification Zone Air Distribution Object Name 2"] = value

    @property
    def zone_3_name(self):
        """Get zone_3_name

        Returns:
            str: the value of `zone_3_name` or None if not set
        """
        return self._data["Zone 3 Name"]

    @zone_3_name.setter
    def zone_3_name(self, value=None):
        """  Corresponds to IDD Field `zone_3_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_3_name`
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
                                 'for field `zone_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_3_name`')

        self._data["Zone 3 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_3(self):
        """Get design_specification_outdoor_air_object_name_3

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_3` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 3"]

    @design_specification_outdoor_air_object_name_3.setter
    def design_specification_outdoor_air_object_name_3(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_3`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_3`
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
                                 'for field `design_specification_outdoor_air_object_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_3`')

        self._data["Design Specification Outdoor Air Object Name 3"] = value

    @property
    def design_specification_zone_air_distribution_object_name_3(self):
        """Get design_specification_zone_air_distribution_object_name_3

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_3` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 3"]

    @design_specification_zone_air_distribution_object_name_3.setter
    def design_specification_zone_air_distribution_object_name_3(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_3`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_3`
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
                                 'for field `design_specification_zone_air_distribution_object_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_3`')

        self._data["Design Specification Zone Air Distribution Object Name 3"] = value

    @property
    def zone_4_name(self):
        """Get zone_4_name

        Returns:
            str: the value of `zone_4_name` or None if not set
        """
        return self._data["Zone 4 Name"]

    @zone_4_name.setter
    def zone_4_name(self, value=None):
        """  Corresponds to IDD Field `zone_4_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_4_name`
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
                                 'for field `zone_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_4_name`')

        self._data["Zone 4 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_4(self):
        """Get design_specification_outdoor_air_object_name_4

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_4` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 4"]

    @design_specification_outdoor_air_object_name_4.setter
    def design_specification_outdoor_air_object_name_4(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_4`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_4`
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
                                 'for field `design_specification_outdoor_air_object_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_4`')

        self._data["Design Specification Outdoor Air Object Name 4"] = value

    @property
    def design_specification_zone_air_distribution_object_name_4(self):
        """Get design_specification_zone_air_distribution_object_name_4

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_4` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 4"]

    @design_specification_zone_air_distribution_object_name_4.setter
    def design_specification_zone_air_distribution_object_name_4(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_4`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_4`
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
                                 'for field `design_specification_zone_air_distribution_object_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_4`')

        self._data["Design Specification Zone Air Distribution Object Name 4"] = value

    @property
    def zone_5_name(self):
        """Get zone_5_name

        Returns:
            str: the value of `zone_5_name` or None if not set
        """
        return self._data["Zone 5 Name"]

    @zone_5_name.setter
    def zone_5_name(self, value=None):
        """  Corresponds to IDD Field `zone_5_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_5_name`
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
                                 'for field `zone_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_5_name`')

        self._data["Zone 5 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_5(self):
        """Get design_specification_outdoor_air_object_name_5

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_5` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 5"]

    @design_specification_outdoor_air_object_name_5.setter
    def design_specification_outdoor_air_object_name_5(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_5`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_5`
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
                                 'for field `design_specification_outdoor_air_object_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_5`')

        self._data["Design Specification Outdoor Air Object Name 5"] = value

    @property
    def design_specification_zone_air_distribution_object_name_5(self):
        """Get design_specification_zone_air_distribution_object_name_5

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_5` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 5"]

    @design_specification_zone_air_distribution_object_name_5.setter
    def design_specification_zone_air_distribution_object_name_5(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_5`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_5`
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
                                 'for field `design_specification_zone_air_distribution_object_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_5`')

        self._data["Design Specification Zone Air Distribution Object Name 5"] = value

    @property
    def zone_6_name(self):
        """Get zone_6_name

        Returns:
            str: the value of `zone_6_name` or None if not set
        """
        return self._data["Zone 6 Name"]

    @zone_6_name.setter
    def zone_6_name(self, value=None):
        """  Corresponds to IDD Field `zone_6_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_6_name`
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
                                 'for field `zone_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_6_name`')

        self._data["Zone 6 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_6(self):
        """Get design_specification_outdoor_air_object_name_6

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_6` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 6"]

    @design_specification_outdoor_air_object_name_6.setter
    def design_specification_outdoor_air_object_name_6(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_6`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_6`
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
                                 'for field `design_specification_outdoor_air_object_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_6`')

        self._data["Design Specification Outdoor Air Object Name 6"] = value

    @property
    def design_specification_zone_air_distribution_object_name_6(self):
        """Get design_specification_zone_air_distribution_object_name_6

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_6` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 6"]

    @design_specification_zone_air_distribution_object_name_6.setter
    def design_specification_zone_air_distribution_object_name_6(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_6`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_6`
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
                                 'for field `design_specification_zone_air_distribution_object_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_6`')

        self._data["Design Specification Zone Air Distribution Object Name 6"] = value

    @property
    def zone_7_name(self):
        """Get zone_7_name

        Returns:
            str: the value of `zone_7_name` or None if not set
        """
        return self._data["Zone 7 Name"]

    @zone_7_name.setter
    def zone_7_name(self, value=None):
        """  Corresponds to IDD Field `zone_7_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_7_name`
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
                                 'for field `zone_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_7_name`')

        self._data["Zone 7 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_7(self):
        """Get design_specification_outdoor_air_object_name_7

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_7` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 7"]

    @design_specification_outdoor_air_object_name_7.setter
    def design_specification_outdoor_air_object_name_7(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_7`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_7`
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
                                 'for field `design_specification_outdoor_air_object_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_7`')

        self._data["Design Specification Outdoor Air Object Name 7"] = value

    @property
    def design_specification_zone_air_distribution_object_name_7(self):
        """Get design_specification_zone_air_distribution_object_name_7

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_7` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 7"]

    @design_specification_zone_air_distribution_object_name_7.setter
    def design_specification_zone_air_distribution_object_name_7(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_7`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_7`
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
                                 'for field `design_specification_zone_air_distribution_object_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_7`')

        self._data["Design Specification Zone Air Distribution Object Name 7"] = value

    @property
    def zone_8_name(self):
        """Get zone_8_name

        Returns:
            str: the value of `zone_8_name` or None if not set
        """
        return self._data["Zone 8 Name"]

    @zone_8_name.setter
    def zone_8_name(self, value=None):
        """  Corresponds to IDD Field `zone_8_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_8_name`
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
                                 'for field `zone_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_8_name`')

        self._data["Zone 8 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_8(self):
        """Get design_specification_outdoor_air_object_name_8

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_8` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 8"]

    @design_specification_outdoor_air_object_name_8.setter
    def design_specification_outdoor_air_object_name_8(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_8`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_8`
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
                                 'for field `design_specification_outdoor_air_object_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_8`')

        self._data["Design Specification Outdoor Air Object Name 8"] = value

    @property
    def design_specification_zone_air_distribution_object_name_8(self):
        """Get design_specification_zone_air_distribution_object_name_8

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_8` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 8"]

    @design_specification_zone_air_distribution_object_name_8.setter
    def design_specification_zone_air_distribution_object_name_8(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_8`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_8`
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
                                 'for field `design_specification_zone_air_distribution_object_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_8`')

        self._data["Design Specification Zone Air Distribution Object Name 8"] = value

    @property
    def zone_9_name(self):
        """Get zone_9_name

        Returns:
            str: the value of `zone_9_name` or None if not set
        """
        return self._data["Zone 9 Name"]

    @zone_9_name.setter
    def zone_9_name(self, value=None):
        """  Corresponds to IDD Field `zone_9_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_9_name`
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
                                 'for field `zone_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_9_name`')

        self._data["Zone 9 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_9(self):
        """Get design_specification_outdoor_air_object_name_9

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_9` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 9"]

    @design_specification_outdoor_air_object_name_9.setter
    def design_specification_outdoor_air_object_name_9(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_9`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_9`
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
                                 'for field `design_specification_outdoor_air_object_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_9`')

        self._data["Design Specification Outdoor Air Object Name 9"] = value

    @property
    def design_specification_zone_air_distribution_object_name_9(self):
        """Get design_specification_zone_air_distribution_object_name_9

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_9` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 9"]

    @design_specification_zone_air_distribution_object_name_9.setter
    def design_specification_zone_air_distribution_object_name_9(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_9`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_9`
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
                                 'for field `design_specification_zone_air_distribution_object_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_9`')

        self._data["Design Specification Zone Air Distribution Object Name 9"] = value

    @property
    def zone_10_name(self):
        """Get zone_10_name

        Returns:
            str: the value of `zone_10_name` or None if not set
        """
        return self._data["Zone 10 Name"]

    @zone_10_name.setter
    def zone_10_name(self, value=None):
        """  Corresponds to IDD Field `zone_10_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_10_name`
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
                                 'for field `zone_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_10_name`')

        self._data["Zone 10 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_10(self):
        """Get design_specification_outdoor_air_object_name_10

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_10` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 10"]

    @design_specification_outdoor_air_object_name_10.setter
    def design_specification_outdoor_air_object_name_10(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_10`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_10`
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
                                 'for field `design_specification_outdoor_air_object_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_10`')

        self._data["Design Specification Outdoor Air Object Name 10"] = value

    @property
    def design_specification_zone_air_distribution_object_name_10(self):
        """Get design_specification_zone_air_distribution_object_name_10

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_10` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 10"]

    @design_specification_zone_air_distribution_object_name_10.setter
    def design_specification_zone_air_distribution_object_name_10(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_10`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_10`
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
                                 'for field `design_specification_zone_air_distribution_object_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_10`')

        self._data["Design Specification Zone Air Distribution Object Name 10"] = value

    @property
    def zone_11_name(self):
        """Get zone_11_name

        Returns:
            str: the value of `zone_11_name` or None if not set
        """
        return self._data["Zone 11 Name"]

    @zone_11_name.setter
    def zone_11_name(self, value=None):
        """  Corresponds to IDD Field `zone_11_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_11_name`
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
                                 'for field `zone_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_11_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_11_name`')

        self._data["Zone 11 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_11(self):
        """Get design_specification_outdoor_air_object_name_11

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_11` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 11"]

    @design_specification_outdoor_air_object_name_11.setter
    def design_specification_outdoor_air_object_name_11(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_11`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_11`
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
                                 'for field `design_specification_outdoor_air_object_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_11`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_11`')

        self._data["Design Specification Outdoor Air Object Name 11"] = value

    @property
    def design_specification_zone_air_distribution_object_name_11(self):
        """Get design_specification_zone_air_distribution_object_name_11

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_11` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 11"]

    @design_specification_zone_air_distribution_object_name_11.setter
    def design_specification_zone_air_distribution_object_name_11(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_11`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_11`
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
                                 'for field `design_specification_zone_air_distribution_object_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_11`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_11`')

        self._data["Design Specification Zone Air Distribution Object Name 11"] = value

    @property
    def zone_12_name(self):
        """Get zone_12_name

        Returns:
            str: the value of `zone_12_name` or None if not set
        """
        return self._data["Zone 12 Name"]

    @zone_12_name.setter
    def zone_12_name(self, value=None):
        """  Corresponds to IDD Field `zone_12_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_12_name`
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
                                 'for field `zone_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_12_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_12_name`')

        self._data["Zone 12 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_12(self):
        """Get design_specification_outdoor_air_object_name_12

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_12` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 12"]

    @design_specification_outdoor_air_object_name_12.setter
    def design_specification_outdoor_air_object_name_12(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_12`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_12`
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
                                 'for field `design_specification_outdoor_air_object_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_12`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_12`')

        self._data["Design Specification Outdoor Air Object Name 12"] = value

    @property
    def design_specification_zone_air_distribution_object_name_12(self):
        """Get design_specification_zone_air_distribution_object_name_12

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_12` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 12"]

    @design_specification_zone_air_distribution_object_name_12.setter
    def design_specification_zone_air_distribution_object_name_12(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_12`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_12`
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
                                 'for field `design_specification_zone_air_distribution_object_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_12`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_12`')

        self._data["Design Specification Zone Air Distribution Object Name 12"] = value

    @property
    def zone_13_name(self):
        """Get zone_13_name

        Returns:
            str: the value of `zone_13_name` or None if not set
        """
        return self._data["Zone 13 Name"]

    @zone_13_name.setter
    def zone_13_name(self, value=None):
        """  Corresponds to IDD Field `zone_13_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_13_name`
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
                                 'for field `zone_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_13_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_13_name`')

        self._data["Zone 13 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_13(self):
        """Get design_specification_outdoor_air_object_name_13

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_13` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 13"]

    @design_specification_outdoor_air_object_name_13.setter
    def design_specification_outdoor_air_object_name_13(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_13`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_13`
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
                                 'for field `design_specification_outdoor_air_object_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_13`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_13`')

        self._data["Design Specification Outdoor Air Object Name 13"] = value

    @property
    def design_specification_zone_air_distribution_object_name_13(self):
        """Get design_specification_zone_air_distribution_object_name_13

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_13` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 13"]

    @design_specification_zone_air_distribution_object_name_13.setter
    def design_specification_zone_air_distribution_object_name_13(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_13`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_13`
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
                                 'for field `design_specification_zone_air_distribution_object_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_13`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_13`')

        self._data["Design Specification Zone Air Distribution Object Name 13"] = value

    @property
    def zone_14_name(self):
        """Get zone_14_name

        Returns:
            str: the value of `zone_14_name` or None if not set
        """
        return self._data["Zone 14 Name"]

    @zone_14_name.setter
    def zone_14_name(self, value=None):
        """  Corresponds to IDD Field `zone_14_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_14_name`
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
                                 'for field `zone_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_14_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_14_name`')

        self._data["Zone 14 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_14(self):
        """Get design_specification_outdoor_air_object_name_14

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_14` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 14"]

    @design_specification_outdoor_air_object_name_14.setter
    def design_specification_outdoor_air_object_name_14(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_14`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_14`
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
                                 'for field `design_specification_outdoor_air_object_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_14`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_14`')

        self._data["Design Specification Outdoor Air Object Name 14"] = value

    @property
    def design_specification_zone_air_distribution_object_name_14(self):
        """Get design_specification_zone_air_distribution_object_name_14

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_14` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 14"]

    @design_specification_zone_air_distribution_object_name_14.setter
    def design_specification_zone_air_distribution_object_name_14(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_14`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_14`
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
                                 'for field `design_specification_zone_air_distribution_object_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_14`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_14`')

        self._data["Design Specification Zone Air Distribution Object Name 14"] = value

    @property
    def zone_15_name(self):
        """Get zone_15_name

        Returns:
            str: the value of `zone_15_name` or None if not set
        """
        return self._data["Zone 15 Name"]

    @zone_15_name.setter
    def zone_15_name(self, value=None):
        """  Corresponds to IDD Field `zone_15_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_15_name`
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
                                 'for field `zone_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_15_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_15_name`')

        self._data["Zone 15 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_15(self):
        """Get design_specification_outdoor_air_object_name_15

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_15` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 15"]

    @design_specification_outdoor_air_object_name_15.setter
    def design_specification_outdoor_air_object_name_15(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_15`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_15`
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
                                 'for field `design_specification_outdoor_air_object_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_15`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_15`')

        self._data["Design Specification Outdoor Air Object Name 15"] = value

    @property
    def design_specification_zone_air_distribution_object_name_15(self):
        """Get design_specification_zone_air_distribution_object_name_15

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_15` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 15"]

    @design_specification_zone_air_distribution_object_name_15.setter
    def design_specification_zone_air_distribution_object_name_15(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_15`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_15`
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
                                 'for field `design_specification_zone_air_distribution_object_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_15`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_15`')

        self._data["Design Specification Zone Air Distribution Object Name 15"] = value

    @property
    def zone_16_name(self):
        """Get zone_16_name

        Returns:
            str: the value of `zone_16_name` or None if not set
        """
        return self._data["Zone 16 Name"]

    @zone_16_name.setter
    def zone_16_name(self, value=None):
        """  Corresponds to IDD Field `zone_16_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_16_name`
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
                                 'for field `zone_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_16_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_16_name`')

        self._data["Zone 16 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_16(self):
        """Get design_specification_outdoor_air_object_name_16

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_16` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 16"]

    @design_specification_outdoor_air_object_name_16.setter
    def design_specification_outdoor_air_object_name_16(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_16`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_16`
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
                                 'for field `design_specification_outdoor_air_object_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_16`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_16`')

        self._data["Design Specification Outdoor Air Object Name 16"] = value

    @property
    def design_specification_zone_air_distribution_object_name_16(self):
        """Get design_specification_zone_air_distribution_object_name_16

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_16` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 16"]

    @design_specification_zone_air_distribution_object_name_16.setter
    def design_specification_zone_air_distribution_object_name_16(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_16`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_16`
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
                                 'for field `design_specification_zone_air_distribution_object_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_16`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_16`')

        self._data["Design Specification Zone Air Distribution Object Name 16"] = value

    @property
    def zone_17_name(self):
        """Get zone_17_name

        Returns:
            str: the value of `zone_17_name` or None if not set
        """
        return self._data["Zone 17 Name"]

    @zone_17_name.setter
    def zone_17_name(self, value=None):
        """  Corresponds to IDD Field `zone_17_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_17_name`
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
                                 'for field `zone_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_17_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_17_name`')

        self._data["Zone 17 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_17(self):
        """Get design_specification_outdoor_air_object_name_17

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_17` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 17"]

    @design_specification_outdoor_air_object_name_17.setter
    def design_specification_outdoor_air_object_name_17(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_17`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_17`
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
                                 'for field `design_specification_outdoor_air_object_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_17`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_17`')

        self._data["Design Specification Outdoor Air Object Name 17"] = value

    @property
    def design_specification_zone_air_distribution_object_name_17(self):
        """Get design_specification_zone_air_distribution_object_name_17

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_17` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 17"]

    @design_specification_zone_air_distribution_object_name_17.setter
    def design_specification_zone_air_distribution_object_name_17(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_17`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_17`
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
                                 'for field `design_specification_zone_air_distribution_object_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_17`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_17`')

        self._data["Design Specification Zone Air Distribution Object Name 17"] = value

    @property
    def zone_18_name(self):
        """Get zone_18_name

        Returns:
            str: the value of `zone_18_name` or None if not set
        """
        return self._data["Zone 18 Name"]

    @zone_18_name.setter
    def zone_18_name(self, value=None):
        """  Corresponds to IDD Field `zone_18_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_18_name`
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
                                 'for field `zone_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_18_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_18_name`')

        self._data["Zone 18 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_18(self):
        """Get design_specification_outdoor_air_object_name_18

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_18` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 18"]

    @design_specification_outdoor_air_object_name_18.setter
    def design_specification_outdoor_air_object_name_18(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_18`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_18`
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
                                 'for field `design_specification_outdoor_air_object_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_18`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_18`')

        self._data["Design Specification Outdoor Air Object Name 18"] = value

    @property
    def design_specification_zone_air_distribution_object_name_18(self):
        """Get design_specification_zone_air_distribution_object_name_18

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_18` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 18"]

    @design_specification_zone_air_distribution_object_name_18.setter
    def design_specification_zone_air_distribution_object_name_18(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_18`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_18`
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
                                 'for field `design_specification_zone_air_distribution_object_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_18`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_18`')

        self._data["Design Specification Zone Air Distribution Object Name 18"] = value

    @property
    def zone_19_name(self):
        """Get zone_19_name

        Returns:
            str: the value of `zone_19_name` or None if not set
        """
        return self._data["Zone 19 Name"]

    @zone_19_name.setter
    def zone_19_name(self, value=None):
        """  Corresponds to IDD Field `zone_19_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_19_name`
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
                                 'for field `zone_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_19_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_19_name`')

        self._data["Zone 19 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_19(self):
        """Get design_specification_outdoor_air_object_name_19

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_19` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 19"]

    @design_specification_outdoor_air_object_name_19.setter
    def design_specification_outdoor_air_object_name_19(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_19`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_19`
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
                                 'for field `design_specification_outdoor_air_object_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_19`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_19`')

        self._data["Design Specification Outdoor Air Object Name 19"] = value

    @property
    def design_specification_zone_air_distribution_object_name_19(self):
        """Get design_specification_zone_air_distribution_object_name_19

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_19` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 19"]

    @design_specification_zone_air_distribution_object_name_19.setter
    def design_specification_zone_air_distribution_object_name_19(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_19`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_19`
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
                                 'for field `design_specification_zone_air_distribution_object_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_19`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_19`')

        self._data["Design Specification Zone Air Distribution Object Name 19"] = value

    @property
    def zone_20_name(self):
        """Get zone_20_name

        Returns:
            str: the value of `zone_20_name` or None if not set
        """
        return self._data["Zone 20 Name"]

    @zone_20_name.setter
    def zone_20_name(self, value=None):
        """  Corresponds to IDD Field `zone_20_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_20_name`
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
                                 'for field `zone_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_20_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_20_name`')

        self._data["Zone 20 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_20(self):
        """Get design_specification_outdoor_air_object_name_20

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_20` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 20"]

    @design_specification_outdoor_air_object_name_20.setter
    def design_specification_outdoor_air_object_name_20(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_20`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_20`
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
                                 'for field `design_specification_outdoor_air_object_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_20`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_20`')

        self._data["Design Specification Outdoor Air Object Name 20"] = value

    @property
    def design_specification_zone_air_distribution_object_name_20(self):
        """Get design_specification_zone_air_distribution_object_name_20

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_20` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 20"]

    @design_specification_zone_air_distribution_object_name_20.setter
    def design_specification_zone_air_distribution_object_name_20(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_20`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_20`
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
                                 'for field `design_specification_zone_air_distribution_object_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_20`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_20`')

        self._data["Design Specification Zone Air Distribution Object Name 20"] = value

    @property
    def zone_21_name(self):
        """Get zone_21_name

        Returns:
            str: the value of `zone_21_name` or None if not set
        """
        return self._data["Zone 21 Name"]

    @zone_21_name.setter
    def zone_21_name(self, value=None):
        """  Corresponds to IDD Field `zone_21_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_21_name`
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
                                 'for field `zone_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_21_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_21_name`')

        self._data["Zone 21 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_21(self):
        """Get design_specification_outdoor_air_object_name_21

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_21` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 21"]

    @design_specification_outdoor_air_object_name_21.setter
    def design_specification_outdoor_air_object_name_21(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_21`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_21`
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
                                 'for field `design_specification_outdoor_air_object_name_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_21`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_21`')

        self._data["Design Specification Outdoor Air Object Name 21"] = value

    @property
    def design_specification_zone_air_distribution_object_name_21(self):
        """Get design_specification_zone_air_distribution_object_name_21

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_21` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 21"]

    @design_specification_zone_air_distribution_object_name_21.setter
    def design_specification_zone_air_distribution_object_name_21(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_21`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_21`
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
                                 'for field `design_specification_zone_air_distribution_object_name_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_21`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_21`')

        self._data["Design Specification Zone Air Distribution Object Name 21"] = value

    @property
    def zone_22_name(self):
        """Get zone_22_name

        Returns:
            str: the value of `zone_22_name` or None if not set
        """
        return self._data["Zone 22 Name"]

    @zone_22_name.setter
    def zone_22_name(self, value=None):
        """  Corresponds to IDD Field `zone_22_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_22_name`
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
                                 'for field `zone_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_22_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_22_name`')

        self._data["Zone 22 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_22(self):
        """Get design_specification_outdoor_air_object_name_22

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_22` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 22"]

    @design_specification_outdoor_air_object_name_22.setter
    def design_specification_outdoor_air_object_name_22(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_22`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_22`
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
                                 'for field `design_specification_outdoor_air_object_name_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_22`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_22`')

        self._data["Design Specification Outdoor Air Object Name 22"] = value

    @property
    def design_specification_zone_air_distribution_object_name_22(self):
        """Get design_specification_zone_air_distribution_object_name_22

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_22` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 22"]

    @design_specification_zone_air_distribution_object_name_22.setter
    def design_specification_zone_air_distribution_object_name_22(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_22`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_22`
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
                                 'for field `design_specification_zone_air_distribution_object_name_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_22`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_22`')

        self._data["Design Specification Zone Air Distribution Object Name 22"] = value

    @property
    def zone_23_name(self):
        """Get zone_23_name

        Returns:
            str: the value of `zone_23_name` or None if not set
        """
        return self._data["Zone 23 Name"]

    @zone_23_name.setter
    def zone_23_name(self, value=None):
        """  Corresponds to IDD Field `zone_23_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_23_name`
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
                                 'for field `zone_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_23_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_23_name`')

        self._data["Zone 23 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_23(self):
        """Get design_specification_outdoor_air_object_name_23

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_23` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 23"]

    @design_specification_outdoor_air_object_name_23.setter
    def design_specification_outdoor_air_object_name_23(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_23`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_23`
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
                                 'for field `design_specification_outdoor_air_object_name_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_23`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_23`')

        self._data["Design Specification Outdoor Air Object Name 23"] = value

    @property
    def design_specification_zone_air_distribution_object_name_23(self):
        """Get design_specification_zone_air_distribution_object_name_23

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_23` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 23"]

    @design_specification_zone_air_distribution_object_name_23.setter
    def design_specification_zone_air_distribution_object_name_23(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_23`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_23`
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
                                 'for field `design_specification_zone_air_distribution_object_name_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_23`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_23`')

        self._data["Design Specification Zone Air Distribution Object Name 23"] = value

    @property
    def zone_24_name(self):
        """Get zone_24_name

        Returns:
            str: the value of `zone_24_name` or None if not set
        """
        return self._data["Zone 24 Name"]

    @zone_24_name.setter
    def zone_24_name(self, value=None):
        """  Corresponds to IDD Field `zone_24_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_24_name`
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
                                 'for field `zone_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_24_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_24_name`')

        self._data["Zone 24 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_24(self):
        """Get design_specification_outdoor_air_object_name_24

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_24` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 24"]

    @design_specification_outdoor_air_object_name_24.setter
    def design_specification_outdoor_air_object_name_24(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_24`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_24`
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
                                 'for field `design_specification_outdoor_air_object_name_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_24`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_24`')

        self._data["Design Specification Outdoor Air Object Name 24"] = value

    @property
    def design_specification_zone_air_distribution_object_name_24(self):
        """Get design_specification_zone_air_distribution_object_name_24

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_24` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 24"]

    @design_specification_zone_air_distribution_object_name_24.setter
    def design_specification_zone_air_distribution_object_name_24(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_24`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_24`
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
                                 'for field `design_specification_zone_air_distribution_object_name_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_24`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_24`')

        self._data["Design Specification Zone Air Distribution Object Name 24"] = value

    @property
    def zone_25_name(self):
        """Get zone_25_name

        Returns:
            str: the value of `zone_25_name` or None if not set
        """
        return self._data["Zone 25 Name"]

    @zone_25_name.setter
    def zone_25_name(self, value=None):
        """  Corresponds to IDD Field `zone_25_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_25_name`
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
                                 'for field `zone_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_25_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_25_name`')

        self._data["Zone 25 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_25(self):
        """Get design_specification_outdoor_air_object_name_25

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_25` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 25"]

    @design_specification_outdoor_air_object_name_25.setter
    def design_specification_outdoor_air_object_name_25(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_25`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_25`
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
                                 'for field `design_specification_outdoor_air_object_name_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_25`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_25`')

        self._data["Design Specification Outdoor Air Object Name 25"] = value

    @property
    def design_specification_zone_air_distribution_object_name_25(self):
        """Get design_specification_zone_air_distribution_object_name_25

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_25` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 25"]

    @design_specification_zone_air_distribution_object_name_25.setter
    def design_specification_zone_air_distribution_object_name_25(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_25`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_25`
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
                                 'for field `design_specification_zone_air_distribution_object_name_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_25`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_25`')

        self._data["Design Specification Zone Air Distribution Object Name 25"] = value

    @property
    def zone_26_name(self):
        """Get zone_26_name

        Returns:
            str: the value of `zone_26_name` or None if not set
        """
        return self._data["Zone 26 Name"]

    @zone_26_name.setter
    def zone_26_name(self, value=None):
        """  Corresponds to IDD Field `zone_26_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_26_name`
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
                                 'for field `zone_26_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_26_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_26_name`')

        self._data["Zone 26 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_26(self):
        """Get design_specification_outdoor_air_object_name_26

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_26` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 26"]

    @design_specification_outdoor_air_object_name_26.setter
    def design_specification_outdoor_air_object_name_26(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_26`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_26`
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
                                 'for field `design_specification_outdoor_air_object_name_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_26`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_26`')

        self._data["Design Specification Outdoor Air Object Name 26"] = value

    @property
    def design_specification_zone_air_distribution_object_name_26(self):
        """Get design_specification_zone_air_distribution_object_name_26

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_26` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 26"]

    @design_specification_zone_air_distribution_object_name_26.setter
    def design_specification_zone_air_distribution_object_name_26(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_26`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_26`
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
                                 'for field `design_specification_zone_air_distribution_object_name_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_26`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_26`')

        self._data["Design Specification Zone Air Distribution Object Name 26"] = value

    @property
    def zone_27_name(self):
        """Get zone_27_name

        Returns:
            str: the value of `zone_27_name` or None if not set
        """
        return self._data["Zone 27 Name"]

    @zone_27_name.setter
    def zone_27_name(self, value=None):
        """  Corresponds to IDD Field `zone_27_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_27_name`
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
                                 'for field `zone_27_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_27_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_27_name`')

        self._data["Zone 27 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_27(self):
        """Get design_specification_outdoor_air_object_name_27

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_27` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 27"]

    @design_specification_outdoor_air_object_name_27.setter
    def design_specification_outdoor_air_object_name_27(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_27`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_27`
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
                                 'for field `design_specification_outdoor_air_object_name_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_27`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_27`')

        self._data["Design Specification Outdoor Air Object Name 27"] = value

    @property
    def design_specification_zone_air_distribution_object_name_27(self):
        """Get design_specification_zone_air_distribution_object_name_27

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_27` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 27"]

    @design_specification_zone_air_distribution_object_name_27.setter
    def design_specification_zone_air_distribution_object_name_27(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_27`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_27`
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
                                 'for field `design_specification_zone_air_distribution_object_name_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_27`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_27`')

        self._data["Design Specification Zone Air Distribution Object Name 27"] = value

    @property
    def zone_28_name(self):
        """Get zone_28_name

        Returns:
            str: the value of `zone_28_name` or None if not set
        """
        return self._data["Zone 28 Name"]

    @zone_28_name.setter
    def zone_28_name(self, value=None):
        """  Corresponds to IDD Field `zone_28_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_28_name`
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
                                 'for field `zone_28_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_28_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_28_name`')

        self._data["Zone 28 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_28(self):
        """Get design_specification_outdoor_air_object_name_28

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_28` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 28"]

    @design_specification_outdoor_air_object_name_28.setter
    def design_specification_outdoor_air_object_name_28(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_28`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_28`
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
                                 'for field `design_specification_outdoor_air_object_name_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_28`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_28`')

        self._data["Design Specification Outdoor Air Object Name 28"] = value

    @property
    def design_specification_zone_air_distribution_object_name_28(self):
        """Get design_specification_zone_air_distribution_object_name_28

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_28` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 28"]

    @design_specification_zone_air_distribution_object_name_28.setter
    def design_specification_zone_air_distribution_object_name_28(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_28`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_28`
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
                                 'for field `design_specification_zone_air_distribution_object_name_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_28`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_28`')

        self._data["Design Specification Zone Air Distribution Object Name 28"] = value

    @property
    def zone_29_name(self):
        """Get zone_29_name

        Returns:
            str: the value of `zone_29_name` or None if not set
        """
        return self._data["Zone 29 Name"]

    @zone_29_name.setter
    def zone_29_name(self, value=None):
        """  Corresponds to IDD Field `zone_29_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_29_name`
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
                                 'for field `zone_29_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_29_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_29_name`')

        self._data["Zone 29 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_29(self):
        """Get design_specification_outdoor_air_object_name_29

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_29` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 29"]

    @design_specification_outdoor_air_object_name_29.setter
    def design_specification_outdoor_air_object_name_29(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_29`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_29`
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
                                 'for field `design_specification_outdoor_air_object_name_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_29`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_29`')

        self._data["Design Specification Outdoor Air Object Name 29"] = value

    @property
    def design_specification_zone_air_distribution_object_name_29(self):
        """Get design_specification_zone_air_distribution_object_name_29

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_29` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 29"]

    @design_specification_zone_air_distribution_object_name_29.setter
    def design_specification_zone_air_distribution_object_name_29(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_29`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_29`
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
                                 'for field `design_specification_zone_air_distribution_object_name_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_29`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_29`')

        self._data["Design Specification Zone Air Distribution Object Name 29"] = value

    @property
    def zone_30_name(self):
        """Get zone_30_name

        Returns:
            str: the value of `zone_30_name` or None if not set
        """
        return self._data["Zone 30 Name"]

    @zone_30_name.setter
    def zone_30_name(self, value=None):
        """  Corresponds to IDD Field `zone_30_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_30_name`
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
                                 'for field `zone_30_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_30_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_30_name`')

        self._data["Zone 30 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_30(self):
        """Get design_specification_outdoor_air_object_name_30

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_30` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 30"]

    @design_specification_outdoor_air_object_name_30.setter
    def design_specification_outdoor_air_object_name_30(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_30`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_30`
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
                                 'for field `design_specification_outdoor_air_object_name_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_30`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_30`')

        self._data["Design Specification Outdoor Air Object Name 30"] = value

    @property
    def design_specification_zone_air_distribution_object_name_30(self):
        """Get design_specification_zone_air_distribution_object_name_30

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_30` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 30"]

    @design_specification_zone_air_distribution_object_name_30.setter
    def design_specification_zone_air_distribution_object_name_30(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_30`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_30`
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
                                 'for field `design_specification_zone_air_distribution_object_name_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_30`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_30`')

        self._data["Design Specification Zone Air Distribution Object Name 30"] = value

    @property
    def zone_31_name(self):
        """Get zone_31_name

        Returns:
            str: the value of `zone_31_name` or None if not set
        """
        return self._data["Zone 31 Name"]

    @zone_31_name.setter
    def zone_31_name(self, value=None):
        """  Corresponds to IDD Field `zone_31_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_31_name`
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
                                 'for field `zone_31_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_31_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_31_name`')

        self._data["Zone 31 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_31(self):
        """Get design_specification_outdoor_air_object_name_31

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_31` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 31"]

    @design_specification_outdoor_air_object_name_31.setter
    def design_specification_outdoor_air_object_name_31(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_31`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_31`
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
                                 'for field `design_specification_outdoor_air_object_name_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_31`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_31`')

        self._data["Design Specification Outdoor Air Object Name 31"] = value

    @property
    def design_specification_zone_air_distribution_object_name_31(self):
        """Get design_specification_zone_air_distribution_object_name_31

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_31` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 31"]

    @design_specification_zone_air_distribution_object_name_31.setter
    def design_specification_zone_air_distribution_object_name_31(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_31`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_31`
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
                                 'for field `design_specification_zone_air_distribution_object_name_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_31`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_31`')

        self._data["Design Specification Zone Air Distribution Object Name 31"] = value

    @property
    def zone_32_name(self):
        """Get zone_32_name

        Returns:
            str: the value of `zone_32_name` or None if not set
        """
        return self._data["Zone 32 Name"]

    @zone_32_name.setter
    def zone_32_name(self, value=None):
        """  Corresponds to IDD Field `zone_32_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_32_name`
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
                                 'for field `zone_32_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_32_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_32_name`')

        self._data["Zone 32 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_32(self):
        """Get design_specification_outdoor_air_object_name_32

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_32` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 32"]

    @design_specification_outdoor_air_object_name_32.setter
    def design_specification_outdoor_air_object_name_32(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_32`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_32`
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
                                 'for field `design_specification_outdoor_air_object_name_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_32`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_32`')

        self._data["Design Specification Outdoor Air Object Name 32"] = value

    @property
    def design_specification_zone_air_distribution_object_name_32(self):
        """Get design_specification_zone_air_distribution_object_name_32

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_32` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 32"]

    @design_specification_zone_air_distribution_object_name_32.setter
    def design_specification_zone_air_distribution_object_name_32(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_32`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_32`
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
                                 'for field `design_specification_zone_air_distribution_object_name_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_32`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_32`')

        self._data["Design Specification Zone Air Distribution Object Name 32"] = value

    @property
    def zone_33_name(self):
        """Get zone_33_name

        Returns:
            str: the value of `zone_33_name` or None if not set
        """
        return self._data["Zone 33 Name"]

    @zone_33_name.setter
    def zone_33_name(self, value=None):
        """  Corresponds to IDD Field `zone_33_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_33_name`
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
                                 'for field `zone_33_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_33_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_33_name`')

        self._data["Zone 33 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_33(self):
        """Get design_specification_outdoor_air_object_name_33

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_33` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 33"]

    @design_specification_outdoor_air_object_name_33.setter
    def design_specification_outdoor_air_object_name_33(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_33`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_33`
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
                                 'for field `design_specification_outdoor_air_object_name_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_33`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_33`')

        self._data["Design Specification Outdoor Air Object Name 33"] = value

    @property
    def design_specification_zone_air_distribution_object_name_33(self):
        """Get design_specification_zone_air_distribution_object_name_33

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_33` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 33"]

    @design_specification_zone_air_distribution_object_name_33.setter
    def design_specification_zone_air_distribution_object_name_33(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_33`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_33`
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
                                 'for field `design_specification_zone_air_distribution_object_name_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_33`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_33`')

        self._data["Design Specification Zone Air Distribution Object Name 33"] = value

    @property
    def zone_34_name(self):
        """Get zone_34_name

        Returns:
            str: the value of `zone_34_name` or None if not set
        """
        return self._data["Zone 34 Name"]

    @zone_34_name.setter
    def zone_34_name(self, value=None):
        """  Corresponds to IDD Field `zone_34_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_34_name`
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
                                 'for field `zone_34_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_34_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_34_name`')

        self._data["Zone 34 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_34(self):
        """Get design_specification_outdoor_air_object_name_34

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_34` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 34"]

    @design_specification_outdoor_air_object_name_34.setter
    def design_specification_outdoor_air_object_name_34(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_34`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_34`
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
                                 'for field `design_specification_outdoor_air_object_name_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_34`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_34`')

        self._data["Design Specification Outdoor Air Object Name 34"] = value

    @property
    def design_specification_zone_air_distribution_object_name_34(self):
        """Get design_specification_zone_air_distribution_object_name_34

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_34` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 34"]

    @design_specification_zone_air_distribution_object_name_34.setter
    def design_specification_zone_air_distribution_object_name_34(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_34`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_34`
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
                                 'for field `design_specification_zone_air_distribution_object_name_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_34`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_34`')

        self._data["Design Specification Zone Air Distribution Object Name 34"] = value

    @property
    def zone_35_name(self):
        """Get zone_35_name

        Returns:
            str: the value of `zone_35_name` or None if not set
        """
        return self._data["Zone 35 Name"]

    @zone_35_name.setter
    def zone_35_name(self, value=None):
        """  Corresponds to IDD Field `zone_35_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_35_name`
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
                                 'for field `zone_35_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_35_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_35_name`')

        self._data["Zone 35 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_35(self):
        """Get design_specification_outdoor_air_object_name_35

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_35` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 35"]

    @design_specification_outdoor_air_object_name_35.setter
    def design_specification_outdoor_air_object_name_35(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_35`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_35`
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
                                 'for field `design_specification_outdoor_air_object_name_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_35`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_35`')

        self._data["Design Specification Outdoor Air Object Name 35"] = value

    @property
    def design_specification_zone_air_distribution_object_name_35(self):
        """Get design_specification_zone_air_distribution_object_name_35

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_35` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 35"]

    @design_specification_zone_air_distribution_object_name_35.setter
    def design_specification_zone_air_distribution_object_name_35(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_35`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_35`
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
                                 'for field `design_specification_zone_air_distribution_object_name_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_35`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_35`')

        self._data["Design Specification Zone Air Distribution Object Name 35"] = value

    @property
    def zone_36_name(self):
        """Get zone_36_name

        Returns:
            str: the value of `zone_36_name` or None if not set
        """
        return self._data["Zone 36 Name"]

    @zone_36_name.setter
    def zone_36_name(self, value=None):
        """  Corresponds to IDD Field `zone_36_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_36_name`
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
                                 'for field `zone_36_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_36_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_36_name`')

        self._data["Zone 36 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_36(self):
        """Get design_specification_outdoor_air_object_name_36

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_36` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 36"]

    @design_specification_outdoor_air_object_name_36.setter
    def design_specification_outdoor_air_object_name_36(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_36`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_36`
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
                                 'for field `design_specification_outdoor_air_object_name_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_36`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_36`')

        self._data["Design Specification Outdoor Air Object Name 36"] = value

    @property
    def design_specification_zone_air_distribution_object_name_36(self):
        """Get design_specification_zone_air_distribution_object_name_36

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_36` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 36"]

    @design_specification_zone_air_distribution_object_name_36.setter
    def design_specification_zone_air_distribution_object_name_36(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_36`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_36`
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
                                 'for field `design_specification_zone_air_distribution_object_name_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_36`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_36`')

        self._data["Design Specification Zone Air Distribution Object Name 36"] = value

    @property
    def zone_37_name(self):
        """Get zone_37_name

        Returns:
            str: the value of `zone_37_name` or None if not set
        """
        return self._data["Zone 37 Name"]

    @zone_37_name.setter
    def zone_37_name(self, value=None):
        """  Corresponds to IDD Field `zone_37_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_37_name`
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
                                 'for field `zone_37_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_37_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_37_name`')

        self._data["Zone 37 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_37(self):
        """Get design_specification_outdoor_air_object_name_37

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_37` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 37"]

    @design_specification_outdoor_air_object_name_37.setter
    def design_specification_outdoor_air_object_name_37(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_37`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_37`
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
                                 'for field `design_specification_outdoor_air_object_name_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_37`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_37`')

        self._data["Design Specification Outdoor Air Object Name 37"] = value

    @property
    def design_specification_zone_air_distribution_object_name_37(self):
        """Get design_specification_zone_air_distribution_object_name_37

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_37` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 37"]

    @design_specification_zone_air_distribution_object_name_37.setter
    def design_specification_zone_air_distribution_object_name_37(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_37`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_37`
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
                                 'for field `design_specification_zone_air_distribution_object_name_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_37`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_37`')

        self._data["Design Specification Zone Air Distribution Object Name 37"] = value

    @property
    def zone_38_name(self):
        """Get zone_38_name

        Returns:
            str: the value of `zone_38_name` or None if not set
        """
        return self._data["Zone 38 Name"]

    @zone_38_name.setter
    def zone_38_name(self, value=None):
        """  Corresponds to IDD Field `zone_38_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_38_name`
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
                                 'for field `zone_38_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_38_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_38_name`')

        self._data["Zone 38 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_38(self):
        """Get design_specification_outdoor_air_object_name_38

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_38` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 38"]

    @design_specification_outdoor_air_object_name_38.setter
    def design_specification_outdoor_air_object_name_38(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_38`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_38`
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
                                 'for field `design_specification_outdoor_air_object_name_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_38`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_38`')

        self._data["Design Specification Outdoor Air Object Name 38"] = value

    @property
    def design_specification_zone_air_distribution_object_name_38(self):
        """Get design_specification_zone_air_distribution_object_name_38

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_38` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 38"]

    @design_specification_zone_air_distribution_object_name_38.setter
    def design_specification_zone_air_distribution_object_name_38(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_38`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_38`
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
                                 'for field `design_specification_zone_air_distribution_object_name_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_38`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_38`')

        self._data["Design Specification Zone Air Distribution Object Name 38"] = value

    @property
    def zone_39_name(self):
        """Get zone_39_name

        Returns:
            str: the value of `zone_39_name` or None if not set
        """
        return self._data["Zone 39 Name"]

    @zone_39_name.setter
    def zone_39_name(self, value=None):
        """  Corresponds to IDD Field `zone_39_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_39_name`
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
                                 'for field `zone_39_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_39_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_39_name`')

        self._data["Zone 39 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_39(self):
        """Get design_specification_outdoor_air_object_name_39

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_39` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 39"]

    @design_specification_outdoor_air_object_name_39.setter
    def design_specification_outdoor_air_object_name_39(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_39`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_39`
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
                                 'for field `design_specification_outdoor_air_object_name_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_39`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_39`')

        self._data["Design Specification Outdoor Air Object Name 39"] = value

    @property
    def design_specification_zone_air_distribution_object_name_39(self):
        """Get design_specification_zone_air_distribution_object_name_39

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_39` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 39"]

    @design_specification_zone_air_distribution_object_name_39.setter
    def design_specification_zone_air_distribution_object_name_39(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_39`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_39`
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
                                 'for field `design_specification_zone_air_distribution_object_name_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_39`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_39`')

        self._data["Design Specification Zone Air Distribution Object Name 39"] = value

    @property
    def zone_40_name(self):
        """Get zone_40_name

        Returns:
            str: the value of `zone_40_name` or None if not set
        """
        return self._data["Zone 40 Name"]

    @zone_40_name.setter
    def zone_40_name(self, value=None):
        """  Corresponds to IDD Field `zone_40_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_40_name`
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
                                 'for field `zone_40_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_40_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_40_name`')

        self._data["Zone 40 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_40(self):
        """Get design_specification_outdoor_air_object_name_40

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_40` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 40"]

    @design_specification_outdoor_air_object_name_40.setter
    def design_specification_outdoor_air_object_name_40(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_40`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_40`
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
                                 'for field `design_specification_outdoor_air_object_name_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_40`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_40`')

        self._data["Design Specification Outdoor Air Object Name 40"] = value

    @property
    def design_specification_zone_air_distribution_object_name_40(self):
        """Get design_specification_zone_air_distribution_object_name_40

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_40` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 40"]

    @design_specification_zone_air_distribution_object_name_40.setter
    def design_specification_zone_air_distribution_object_name_40(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_40`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_40`
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
                                 'for field `design_specification_zone_air_distribution_object_name_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_40`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_40`')

        self._data["Design Specification Zone Air Distribution Object Name 40"] = value

    @property
    def zone_41_name(self):
        """Get zone_41_name

        Returns:
            str: the value of `zone_41_name` or None if not set
        """
        return self._data["Zone 41 Name"]

    @zone_41_name.setter
    def zone_41_name(self, value=None):
        """  Corresponds to IDD Field `zone_41_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_41_name`
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
                                 'for field `zone_41_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_41_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_41_name`')

        self._data["Zone 41 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_41(self):
        """Get design_specification_outdoor_air_object_name_41

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_41` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 41"]

    @design_specification_outdoor_air_object_name_41.setter
    def design_specification_outdoor_air_object_name_41(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_41`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_41`
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
                                 'for field `design_specification_outdoor_air_object_name_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_41`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_41`')

        self._data["Design Specification Outdoor Air Object Name 41"] = value

    @property
    def design_specification_zone_air_distribution_object_name_41(self):
        """Get design_specification_zone_air_distribution_object_name_41

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_41` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 41"]

    @design_specification_zone_air_distribution_object_name_41.setter
    def design_specification_zone_air_distribution_object_name_41(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_41`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_41`
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
                                 'for field `design_specification_zone_air_distribution_object_name_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_41`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_41`')

        self._data["Design Specification Zone Air Distribution Object Name 41"] = value

    @property
    def zone_42_name(self):
        """Get zone_42_name

        Returns:
            str: the value of `zone_42_name` or None if not set
        """
        return self._data["Zone 42 Name"]

    @zone_42_name.setter
    def zone_42_name(self, value=None):
        """  Corresponds to IDD Field `zone_42_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_42_name`
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
                                 'for field `zone_42_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_42_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_42_name`')

        self._data["Zone 42 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_42(self):
        """Get design_specification_outdoor_air_object_name_42

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_42` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 42"]

    @design_specification_outdoor_air_object_name_42.setter
    def design_specification_outdoor_air_object_name_42(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_42`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_42`
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
                                 'for field `design_specification_outdoor_air_object_name_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_42`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_42`')

        self._data["Design Specification Outdoor Air Object Name 42"] = value

    @property
    def design_specification_zone_air_distribution_object_name_42(self):
        """Get design_specification_zone_air_distribution_object_name_42

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_42` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 42"]

    @design_specification_zone_air_distribution_object_name_42.setter
    def design_specification_zone_air_distribution_object_name_42(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_42`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_42`
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
                                 'for field `design_specification_zone_air_distribution_object_name_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_42`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_42`')

        self._data["Design Specification Zone Air Distribution Object Name 42"] = value

    @property
    def zone_43_name(self):
        """Get zone_43_name

        Returns:
            str: the value of `zone_43_name` or None if not set
        """
        return self._data["Zone 43 Name"]

    @zone_43_name.setter
    def zone_43_name(self, value=None):
        """  Corresponds to IDD Field `zone_43_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_43_name`
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
                                 'for field `zone_43_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_43_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_43_name`')

        self._data["Zone 43 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_43(self):
        """Get design_specification_outdoor_air_object_name_43

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_43` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 43"]

    @design_specification_outdoor_air_object_name_43.setter
    def design_specification_outdoor_air_object_name_43(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_43`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_43`
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
                                 'for field `design_specification_outdoor_air_object_name_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_43`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_43`')

        self._data["Design Specification Outdoor Air Object Name 43"] = value

    @property
    def design_specification_zone_air_distribution_object_name_43(self):
        """Get design_specification_zone_air_distribution_object_name_43

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_43` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 43"]

    @design_specification_zone_air_distribution_object_name_43.setter
    def design_specification_zone_air_distribution_object_name_43(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_43`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_43`
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
                                 'for field `design_specification_zone_air_distribution_object_name_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_43`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_43`')

        self._data["Design Specification Zone Air Distribution Object Name 43"] = value

    @property
    def zone_44_name(self):
        """Get zone_44_name

        Returns:
            str: the value of `zone_44_name` or None if not set
        """
        return self._data["Zone 44 Name"]

    @zone_44_name.setter
    def zone_44_name(self, value=None):
        """  Corresponds to IDD Field `zone_44_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_44_name`
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
                                 'for field `zone_44_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_44_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_44_name`')

        self._data["Zone 44 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_44(self):
        """Get design_specification_outdoor_air_object_name_44

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_44` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 44"]

    @design_specification_outdoor_air_object_name_44.setter
    def design_specification_outdoor_air_object_name_44(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_44`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_44`
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
                                 'for field `design_specification_outdoor_air_object_name_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_44`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_44`')

        self._data["Design Specification Outdoor Air Object Name 44"] = value

    @property
    def design_specification_zone_air_distribution_object_name_44(self):
        """Get design_specification_zone_air_distribution_object_name_44

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_44` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 44"]

    @design_specification_zone_air_distribution_object_name_44.setter
    def design_specification_zone_air_distribution_object_name_44(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_44`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_44`
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
                                 'for field `design_specification_zone_air_distribution_object_name_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_44`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_44`')

        self._data["Design Specification Zone Air Distribution Object Name 44"] = value

    @property
    def zone_45_name(self):
        """Get zone_45_name

        Returns:
            str: the value of `zone_45_name` or None if not set
        """
        return self._data["Zone 45 Name"]

    @zone_45_name.setter
    def zone_45_name(self, value=None):
        """  Corresponds to IDD Field `zone_45_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_45_name`
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
                                 'for field `zone_45_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_45_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_45_name`')

        self._data["Zone 45 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_45(self):
        """Get design_specification_outdoor_air_object_name_45

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_45` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 45"]

    @design_specification_outdoor_air_object_name_45.setter
    def design_specification_outdoor_air_object_name_45(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_45`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_45`
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
                                 'for field `design_specification_outdoor_air_object_name_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_45`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_45`')

        self._data["Design Specification Outdoor Air Object Name 45"] = value

    @property
    def design_specification_zone_air_distribution_object_name_45(self):
        """Get design_specification_zone_air_distribution_object_name_45

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_45` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 45"]

    @design_specification_zone_air_distribution_object_name_45.setter
    def design_specification_zone_air_distribution_object_name_45(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_45`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_45`
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
                                 'for field `design_specification_zone_air_distribution_object_name_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_45`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_45`')

        self._data["Design Specification Zone Air Distribution Object Name 45"] = value

    @property
    def zone_46_name(self):
        """Get zone_46_name

        Returns:
            str: the value of `zone_46_name` or None if not set
        """
        return self._data["Zone 46 Name"]

    @zone_46_name.setter
    def zone_46_name(self, value=None):
        """  Corresponds to IDD Field `zone_46_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_46_name`
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
                                 'for field `zone_46_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_46_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_46_name`')

        self._data["Zone 46 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_46(self):
        """Get design_specification_outdoor_air_object_name_46

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_46` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 46"]

    @design_specification_outdoor_air_object_name_46.setter
    def design_specification_outdoor_air_object_name_46(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_46`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_46`
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
                                 'for field `design_specification_outdoor_air_object_name_46`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_46`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_46`')

        self._data["Design Specification Outdoor Air Object Name 46"] = value

    @property
    def design_specification_zone_air_distribution_object_name_46(self):
        """Get design_specification_zone_air_distribution_object_name_46

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_46` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 46"]

    @design_specification_zone_air_distribution_object_name_46.setter
    def design_specification_zone_air_distribution_object_name_46(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_46`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_46`
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
                                 'for field `design_specification_zone_air_distribution_object_name_46`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_46`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_46`')

        self._data["Design Specification Zone Air Distribution Object Name 46"] = value

    @property
    def zone_47_name(self):
        """Get zone_47_name

        Returns:
            str: the value of `zone_47_name` or None if not set
        """
        return self._data["Zone 47 Name"]

    @zone_47_name.setter
    def zone_47_name(self, value=None):
        """  Corresponds to IDD Field `zone_47_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_47_name`
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
                                 'for field `zone_47_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_47_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_47_name`')

        self._data["Zone 47 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_47(self):
        """Get design_specification_outdoor_air_object_name_47

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_47` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 47"]

    @design_specification_outdoor_air_object_name_47.setter
    def design_specification_outdoor_air_object_name_47(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_47`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_47`
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
                                 'for field `design_specification_outdoor_air_object_name_47`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_47`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_47`')

        self._data["Design Specification Outdoor Air Object Name 47"] = value

    @property
    def design_specification_zone_air_distribution_object_name_47(self):
        """Get design_specification_zone_air_distribution_object_name_47

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_47` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 47"]

    @design_specification_zone_air_distribution_object_name_47.setter
    def design_specification_zone_air_distribution_object_name_47(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_47`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_47`
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
                                 'for field `design_specification_zone_air_distribution_object_name_47`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_47`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_47`')

        self._data["Design Specification Zone Air Distribution Object Name 47"] = value

    @property
    def zone_48_name(self):
        """Get zone_48_name

        Returns:
            str: the value of `zone_48_name` or None if not set
        """
        return self._data["Zone 48 Name"]

    @zone_48_name.setter
    def zone_48_name(self, value=None):
        """  Corresponds to IDD Field `zone_48_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_48_name`
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
                                 'for field `zone_48_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_48_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_48_name`')

        self._data["Zone 48 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_48(self):
        """Get design_specification_outdoor_air_object_name_48

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_48` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 48"]

    @design_specification_outdoor_air_object_name_48.setter
    def design_specification_outdoor_air_object_name_48(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_48`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_48`
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
                                 'for field `design_specification_outdoor_air_object_name_48`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_48`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_48`')

        self._data["Design Specification Outdoor Air Object Name 48"] = value

    @property
    def design_specification_zone_air_distribution_object_name_48(self):
        """Get design_specification_zone_air_distribution_object_name_48

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_48` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 48"]

    @design_specification_zone_air_distribution_object_name_48.setter
    def design_specification_zone_air_distribution_object_name_48(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_48`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_48`
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
                                 'for field `design_specification_zone_air_distribution_object_name_48`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_48`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_48`')

        self._data["Design Specification Zone Air Distribution Object Name 48"] = value

    @property
    def zone_49_name(self):
        """Get zone_49_name

        Returns:
            str: the value of `zone_49_name` or None if not set
        """
        return self._data["Zone 49 Name"]

    @zone_49_name.setter
    def zone_49_name(self, value=None):
        """  Corresponds to IDD Field `zone_49_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_49_name`
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
                                 'for field `zone_49_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_49_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_49_name`')

        self._data["Zone 49 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_49(self):
        """Get design_specification_outdoor_air_object_name_49

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_49` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 49"]

    @design_specification_outdoor_air_object_name_49.setter
    def design_specification_outdoor_air_object_name_49(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_49`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_49`
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
                                 'for field `design_specification_outdoor_air_object_name_49`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_49`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_49`')

        self._data["Design Specification Outdoor Air Object Name 49"] = value

    @property
    def design_specification_zone_air_distribution_object_name_49(self):
        """Get design_specification_zone_air_distribution_object_name_49

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_49` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 49"]

    @design_specification_zone_air_distribution_object_name_49.setter
    def design_specification_zone_air_distribution_object_name_49(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_49`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_49`
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
                                 'for field `design_specification_zone_air_distribution_object_name_49`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_49`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_49`')

        self._data["Design Specification Zone Air Distribution Object Name 49"] = value

    @property
    def zone_50_name(self):
        """Get zone_50_name

        Returns:
            str: the value of `zone_50_name` or None if not set
        """
        return self._data["Zone 50 Name"]

    @zone_50_name.setter
    def zone_50_name(self, value=None):
        """  Corresponds to IDD Field `zone_50_name`
        A zone name or a zone list name may be used here

        Args:
            value (str): value for IDD Field `zone_50_name`
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
                                 'for field `zone_50_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_50_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_50_name`')

        self._data["Zone 50 Name"] = value

    @property
    def design_specification_outdoor_air_object_name_50(self):
        """Get design_specification_outdoor_air_object_name_50

        Returns:
            str: the value of `design_specification_outdoor_air_object_name_50` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name 50"]

    @design_specification_outdoor_air_object_name_50.setter
    def design_specification_outdoor_air_object_name_50(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name_50`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name_50`
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
                                 'for field `design_specification_outdoor_air_object_name_50`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name_50`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name_50`')

        self._data["Design Specification Outdoor Air Object Name 50"] = value

    @property
    def design_specification_zone_air_distribution_object_name_50(self):
        """Get design_specification_zone_air_distribution_object_name_50

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name_50` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name 50"]

    @design_specification_zone_air_distribution_object_name_50.setter
    def design_specification_zone_air_distribution_object_name_50(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name_50`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name_50`
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
                                 'for field `design_specification_zone_air_distribution_object_name_50`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name_50`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name_50`')

        self._data["Design Specification Zone Air Distribution Object Name 50"] = value

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

class AirLoopHvacControllerList(object):
    """ Corresponds to IDD object `AirLoopHVAC:ControllerList`
        List controllers in order of control sequence
    
    """
    internal_name = "AirLoopHVAC:ControllerList"
    field_count = 17
    required_fields = ["Name", "Controller 1 Object Type", "Controller 1 Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `controller_1_object_type`

        Args:
            value (str): value for IDD Field `controller_1_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_1_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `controller_1_object_type`'.format(value))
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
        """  Corresponds to IDD Field `controller_1_name`

        Args:
            value (str): value for IDD Field `controller_1_name`
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
                                 'for field `controller_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_1_name`')

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
        """  Corresponds to IDD Field `controller_2_object_type`

        Args:
            value (str): value for IDD Field `controller_2_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_2_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `controller_2_object_type`'.format(value))
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
        """  Corresponds to IDD Field `controller_2_name`

        Args:
            value (str): value for IDD Field `controller_2_name`
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
                                 'for field `controller_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_2_name`')

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
        """  Corresponds to IDD Field `controller_3_object_type`

        Args:
            value (str): value for IDD Field `controller_3_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_3_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `controller_3_object_type`'.format(value))
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
        """  Corresponds to IDD Field `controller_3_name`

        Args:
            value (str): value for IDD Field `controller_3_name`
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
                                 'for field `controller_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_3_name`')

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
        """  Corresponds to IDD Field `controller_4_object_type`

        Args:
            value (str): value for IDD Field `controller_4_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_4_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `controller_4_object_type`'.format(value))
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
        """  Corresponds to IDD Field `controller_4_name`

        Args:
            value (str): value for IDD Field `controller_4_name`
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
                                 'for field `controller_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_4_name`')

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
        """  Corresponds to IDD Field `controller_5_object_type`

        Args:
            value (str): value for IDD Field `controller_5_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_5_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `controller_5_object_type`'.format(value))
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
        """  Corresponds to IDD Field `controller_5_name`

        Args:
            value (str): value for IDD Field `controller_5_name`
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
                                 'for field `controller_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_5_name`')

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
        """  Corresponds to IDD Field `controller_6_object_type`

        Args:
            value (str): value for IDD Field `controller_6_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_6_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `controller_6_object_type`'.format(value))
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
        """  Corresponds to IDD Field `controller_6_name`

        Args:
            value (str): value for IDD Field `controller_6_name`
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
                                 'for field `controller_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_6_name`')

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
        """  Corresponds to IDD Field `controller_7_object_type`

        Args:
            value (str): value for IDD Field `controller_7_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_7_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `controller_7_object_type`'.format(value))
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
        """  Corresponds to IDD Field `controller_7_name`

        Args:
            value (str): value for IDD Field `controller_7_name`
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
                                 'for field `controller_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_7_name`')

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
        """  Corresponds to IDD Field `controller_8_object_type`

        Args:
            value (str): value for IDD Field `controller_8_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_8_object_type`')
            vals = {}
            vals["controller:watercoil"] = "Controller:WaterCoil"
            vals["controller:outdoorair"] = "Controller:OutdoorAir"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `controller_8_object_type`'.format(value))
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
        """  Corresponds to IDD Field `controller_8_name`

        Args:
            value (str): value for IDD Field `controller_8_name`
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
                                 'for field `controller_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controller_8_name`')

        self._data["Controller 8 Name"] = value

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