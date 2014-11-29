from collections import OrderedDict

class DehumidifierDesiccantNoFans(object):
    """ Corresponds to IDD object `Dehumidifier:Desiccant:NoFans`
        This object models a solid desiccant dehumidifier. The process
        air stream is the air which is dehumidified. The regeneration air
        stream is the air which is heated to regenerate the desiccant.
        This object determines the process air outlet conditions, the
        load on the regeneration heating coil, the electric power consumption
        for the wheel rotor motor, and the regeneration air fan mass flow rate.
        All other heat exchangers are modeled as separate objects connected
        to the inlet and outlet nodes of the dehumidifier. The solid
        desiccant dehumidifier is typically used in an AirLoopHVAC:OutdoorAirSystem,
        but can also be specified in any AirLoopHVAC.
    """
    internal_name = "Dehumidifier:Desiccant:NoFans"
    field_count = 25

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Dehumidifier:Desiccant:NoFans`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Process Air Inlet Node Name"] = None
        self._data["Process Air Outlet Node Name"] = None
        self._data["Regeneration Air Inlet Node Name"] = None
        self._data["Regeneration Fan Inlet Node Name"] = None
        self._data["Control Type"] = None
        self._data["Leaving Maximum Humidity Ratio Setpoint"] = None
        self._data["Nominal Process Air Flow Rate"] = None
        self._data["Nominal Process Air Velocity"] = None
        self._data["Rotor Power"] = None
        self._data["Regeneration Coil Object Type"] = None
        self._data["Regeneration Coil Name"] = None
        self._data["Regeneration Fan Object Type"] = None
        self._data["Regeneration Fan Name"] = None
        self._data["Performance Model Type"] = None
        self._data["Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = None
        self._data["Leaving Dry-Bulb Function of Air Velocity Curve Name"] = None
        self._data["Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = None
        self._data["Leaving Humidity Ratio Function of Air Velocity Curve Name"] = None
        self._data["Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = None
        self._data["Regeneration Energy Function of Air Velocity Curve Name"] = None
        self._data["Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = None
        self._data["Regeneration Velocity Function of Air Velocity Curve Name"] = None
        self._data["Nominal Regeneration Temperature"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.process_air_inlet_node_name = None
        else:
            self.process_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.process_air_outlet_node_name = None
        else:
            self.process_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_air_inlet_node_name = None
        else:
            self.regeneration_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_fan_inlet_node_name = None
        else:
            self.regeneration_fan_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_type = None
        else:
            self.control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leaving_maximum_humidity_ratio_setpoint = None
        else:
            self.leaving_maximum_humidity_ratio_setpoint = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_process_air_flow_rate = None
        else:
            self.nominal_process_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_process_air_velocity = None
        else:
            self.nominal_process_air_velocity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rotor_power = None
        else:
            self.rotor_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_coil_object_type = None
        else:
            self.regeneration_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_coil_name = None
        else:
            self.regeneration_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_fan_object_type = None
        else:
            self.regeneration_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_fan_name = None
        else:
            self.regeneration_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.performance_model_type = None
        else:
            self.performance_model_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name = None
        else:
            self.leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leaving_drybulb_function_of_air_velocity_curve_name = None
        else:
            self.leaving_drybulb_function_of_air_velocity_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name = None
        else:
            self.leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leaving_humidity_ratio_function_of_air_velocity_curve_name = None
        else:
            self.leaving_humidity_ratio_function_of_air_velocity_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name = None
        else:
            self.regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_energy_function_of_air_velocity_curve_name = None
        else:
            self.regeneration_energy_function_of_air_velocity_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name = None
        else:
            self.regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_velocity_function_of_air_velocity_curve_name = None
        else:
            self.regeneration_velocity_function_of_air_velocity_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_regeneration_temperature = None
        else:
            self.nominal_regeneration_temperature = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

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

        self._data["Availability Schedule Name"] = value

    @property
    def process_air_inlet_node_name(self):
        """Get process_air_inlet_node_name

        Returns:
            str: the value of `process_air_inlet_node_name` or None if not set
        """
        return self._data["Process Air Inlet Node Name"]

    @process_air_inlet_node_name.setter
    def process_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `process_air_inlet_node_name`
        This is the node entering the process side of the desiccant wheel.

        Args:
            value (str): value for IDD Field `process_air_inlet_node_name`
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
                                 'for field `process_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `process_air_inlet_node_name`')

        self._data["Process Air Inlet Node Name"] = value

    @property
    def process_air_outlet_node_name(self):
        """Get process_air_outlet_node_name

        Returns:
            str: the value of `process_air_outlet_node_name` or None if not set
        """
        return self._data["Process Air Outlet Node Name"]

    @process_air_outlet_node_name.setter
    def process_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `process_air_outlet_node_name`
        This is the node leaving the process side of the desiccant wheel.

        Args:
            value (str): value for IDD Field `process_air_outlet_node_name`
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
                                 'for field `process_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `process_air_outlet_node_name`')

        self._data["Process Air Outlet Node Name"] = value

    @property
    def regeneration_air_inlet_node_name(self):
        """Get regeneration_air_inlet_node_name

        Returns:
            str: the value of `regeneration_air_inlet_node_name` or None if not set
        """
        return self._data["Regeneration Air Inlet Node Name"]

    @regeneration_air_inlet_node_name.setter
    def regeneration_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_air_inlet_node_name`
        This is the node entering the regeneration side of the desiccant wheel
        after the regeneration coil.

        Args:
            value (str): value for IDD Field `regeneration_air_inlet_node_name`
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
                                 'for field `regeneration_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_inlet_node_name`')

        self._data["Regeneration Air Inlet Node Name"] = value

    @property
    def regeneration_fan_inlet_node_name(self):
        """Get regeneration_fan_inlet_node_name

        Returns:
            str: the value of `regeneration_fan_inlet_node_name` or None if not set
        """
        return self._data["Regeneration Fan Inlet Node Name"]

    @regeneration_fan_inlet_node_name.setter
    def regeneration_fan_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_fan_inlet_node_name`
        Node for air entering the regeneration fan, mass flow is set
        by the desiccant dehumidifier module.

        Args:
            value (str): value for IDD Field `regeneration_fan_inlet_node_name`
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
                                 'for field `regeneration_fan_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_fan_inlet_node_name`')

        self._data["Regeneration Fan Inlet Node Name"] = value

    @property
    def control_type(self):
        """Get control_type

        Returns:
            str: the value of `control_type` or None if not set
        """
        return self._data["Control Type"]

    @control_type.setter
    def control_type(self, value=None):
        """  Corresponds to IDD Field `control_type`
        Type of setpoint control:
        LeavingMaximumHumidityRatioSetpoint means that the unit is controlled
        to deliver air at the Leaving Max Humidity Ratio Setpoint (see below),
        SystemNodeMaximumHumidityRatioSetpoint means that the leaving humidity
        ratio setpoint is the System Node Humidity Ratio Max property
        of the Process Air Outlet Node.  A Setpoint
        object must be used to control this setpoint.
        Both control types use bypass dampers to prevent overdrying.

        Args:
            value (str): value for IDD Field `control_type`
                Accepted values are:
                      - LeavingMaximumHumidityRatioSetpoint
                      - SystemNodeMaximumHumidityRatioSetpoint
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
                                 'for field `control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_type`')
            vals = set()
            vals.add("LeavingMaximumHumidityRatioSetpoint")
            vals.add("SystemNodeMaximumHumidityRatioSetpoint")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_type`'.format(value))

        self._data["Control Type"] = value

    @property
    def leaving_maximum_humidity_ratio_setpoint(self):
        """Get leaving_maximum_humidity_ratio_setpoint

        Returns:
            float: the value of `leaving_maximum_humidity_ratio_setpoint` or None if not set
        """
        return self._data["Leaving Maximum Humidity Ratio Setpoint"]

    @leaving_maximum_humidity_ratio_setpoint.setter
    def leaving_maximum_humidity_ratio_setpoint(self, value=None):
        """  Corresponds to IDD Field `leaving_maximum_humidity_ratio_setpoint`
        Fixed setpoint for maximum process air leaving humidity ratio
        Applicable only when Control Type = LeavingMaximumHumidityRatioSetpoint.

        Args:
            value (float): value for IDD Field `leaving_maximum_humidity_ratio_setpoint`
                Unit: kgWater/kgDryAir
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
                                 'for field `leaving_maximum_humidity_ratio_setpoint`'.format(value))

        self._data["Leaving Maximum Humidity Ratio Setpoint"] = value

    @property
    def nominal_process_air_flow_rate(self):
        """Get nominal_process_air_flow_rate

        Returns:
            float: the value of `nominal_process_air_flow_rate` or None if not set
        """
        return self._data["Nominal Process Air Flow Rate"]

    @nominal_process_air_flow_rate.setter
    def nominal_process_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `nominal_process_air_flow_rate`
        Process air flow rate at nominal conditions

        Args:
            value (float): value for IDD Field `nominal_process_air_flow_rate`
                Unit: m3/s
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
                                 'for field `nominal_process_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_process_air_flow_rate`')

        self._data["Nominal Process Air Flow Rate"] = value

    @property
    def nominal_process_air_velocity(self):
        """Get nominal_process_air_velocity

        Returns:
            float: the value of `nominal_process_air_velocity` or None if not set
        """
        return self._data["Nominal Process Air Velocity"]

    @nominal_process_air_velocity.setter
    def nominal_process_air_velocity(self, value=None):
        """  Corresponds to IDD Field `nominal_process_air_velocity`
        Process air velocity at nominal flow
        When using Performance Model Type of Default, must be 2.032 to 4.064 m/s (400 to 800 fpm)

        Args:
            value (float): value for IDD Field `nominal_process_air_velocity`
                Unit: m/s
                value > 0.0
                value <= 6.0
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
                                 'for field `nominal_process_air_velocity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_process_air_velocity`')
            if value > 6.0:
                raise ValueError('value need to be smaller 6.0 '
                                 'for field `nominal_process_air_velocity`')

        self._data["Nominal Process Air Velocity"] = value

    @property
    def rotor_power(self):
        """Get rotor_power

        Returns:
            float: the value of `rotor_power` or None if not set
        """
        return self._data["Rotor Power"]

    @rotor_power.setter
    def rotor_power(self, value=None):
        """  Corresponds to IDD Field `rotor_power`
        Power input to wheel rotor motor

        Args:
            value (float): value for IDD Field `rotor_power`
                Unit: W
                value >= 0.0
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
                                 'for field `rotor_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rotor_power`')

        self._data["Rotor Power"] = value

    @property
    def regeneration_coil_object_type(self):
        """Get regeneration_coil_object_type

        Returns:
            str: the value of `regeneration_coil_object_type` or None if not set
        """
        return self._data["Regeneration Coil Object Type"]

    @regeneration_coil_object_type.setter
    def regeneration_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `regeneration_coil_object_type`
        heating coil type
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `regeneration_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Water
                      - Coil:Heating:Steam
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
                                 'for field `regeneration_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `regeneration_coil_object_type`'.format(value))

        self._data["Regeneration Coil Object Type"] = value

    @property
    def regeneration_coil_name(self):
        """Get regeneration_coil_name

        Returns:
            str: the value of `regeneration_coil_name` or None if not set
        """
        return self._data["Regeneration Coil Name"]

    @regeneration_coil_name.setter
    def regeneration_coil_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_coil_name`
        Name of heating coil object for regeneration air

        Args:
            value (str): value for IDD Field `regeneration_coil_name`
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
                                 'for field `regeneration_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_coil_name`')

        self._data["Regeneration Coil Name"] = value

    @property
    def regeneration_fan_object_type(self):
        """Get regeneration_fan_object_type

        Returns:
            str: the value of `regeneration_fan_object_type` or None if not set
        """
        return self._data["Regeneration Fan Object Type"]

    @regeneration_fan_object_type.setter
    def regeneration_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `regeneration_fan_object_type`
        Type of fan object for regeneration air.  When using the Default
        Performance Model Type (see below), only Fan:VariableVolume is valid.

        Args:
            value (str): value for IDD Field `regeneration_fan_object_type`
                Accepted values are:
                      - Fan:VariableVolume
                      - Fan:ConstantVolume
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
                                 'for field `regeneration_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_fan_object_type`')
            vals = set()
            vals.add("Fan:VariableVolume")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `regeneration_fan_object_type`'.format(value))

        self._data["Regeneration Fan Object Type"] = value

    @property
    def regeneration_fan_name(self):
        """Get regeneration_fan_name

        Returns:
            str: the value of `regeneration_fan_name` or None if not set
        """
        return self._data["Regeneration Fan Name"]

    @regeneration_fan_name.setter
    def regeneration_fan_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_fan_name`
        Name of fan object for regeneration air

        Args:
            value (str): value for IDD Field `regeneration_fan_name`
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
                                 'for field `regeneration_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_fan_name`')

        self._data["Regeneration Fan Name"] = value

    @property
    def performance_model_type(self):
        """Get performance_model_type

        Returns:
            str: the value of `performance_model_type` or None if not set
        """
        return self._data["Performance Model Type"]

    @performance_model_type.setter
    def performance_model_type(self, value=None):
        """  Corresponds to IDD Field `performance_model_type`
        Specifies whether the default performance model or user-specified
        curves should be used to model the performance.  The default model
        is a generic solid desiccant wheel using performance curves of the form:
        curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*vel + C7*vel**2
        + C8*edb*ew + C9*edb**2*ew**2 + C10*edb*vel + C11*edb**2*vel**2
        + C12*ew*vel + C13*ew**2*vel**2 + C14*ALOG(edb) + C15*ALOG(ew) + C16*ALOG(vel)
        edb = process entering dry-bulb temperature [C]
        ew  = process entering humidity ratio [kgWater/kgDryAir]
        vel = process air velocity [m/s]
        If UserCurves are specified, then performance is calculated as follows:
        Leaving Dry-Bulb = (Leaving Dry-Bulb fTW Curve) * (Leaving Dry-Bulb fV Curve)
        Leaving Humidity Ratio = (Leaving Humidity Ratio fTW Curve) * (Leaving Humidity Ratio fV Curve)
        Regen Energy = (Regen Energy fTW Curve) * (Regen Energy fV Curve)
        Regen Velocity = (Regen Velocity fTW Curve) * (Regen Velocity fV Curve)

        Args:
            value (str): value for IDD Field `performance_model_type`
                Accepted values are:
                      - Default
                      - UserCurves
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
                                 'for field `performance_model_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_model_type`')
            vals = set()
            vals.add("Default")
            vals.add("UserCurves")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `performance_model_type`'.format(value))

        self._data["Performance Model Type"] = value

    @property
    def leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name(self):
        """Get leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name

        Returns:
            str: the value of `leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self._data["Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name`
        Leaving dry-bulb of process air as a function of entering dry-bulb
        and entering humidity ratio, biquadratic curve
        Table:TwoIndependentVariables object can also be used
        curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        edb = process entering dry-bulb temperature [C]
        ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name`
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
                                 'for field `leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name`')

        self._data["Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def leaving_drybulb_function_of_air_velocity_curve_name(self):
        """Get leaving_drybulb_function_of_air_velocity_curve_name

        Returns:
            str: the value of `leaving_drybulb_function_of_air_velocity_curve_name` or None if not set
        """
        return self._data["Leaving Dry-Bulb Function of Air Velocity Curve Name"]

    @leaving_drybulb_function_of_air_velocity_curve_name.setter
    def leaving_drybulb_function_of_air_velocity_curve_name(self, value=None):
        """  Corresponds to IDD Field `leaving_drybulb_function_of_air_velocity_curve_name`
        Leaving dry-bulb of process air as a function of air velocity,
        quadratic curve.
        Table:OneIndependentVariable object can also be used
        curve = C1 + C2*v + C3*v**2
        v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `leaving_drybulb_function_of_air_velocity_curve_name`
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
                                 'for field `leaving_drybulb_function_of_air_velocity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `leaving_drybulb_function_of_air_velocity_curve_name`')

        self._data["Leaving Dry-Bulb Function of Air Velocity Curve Name"] = value

    @property
    def leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name(self):
        """Get leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name

        Returns:
            str: the value of `leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self._data["Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name`
        Leaving humidity ratio of process air as a function of entering dry-bulb
        and entering humidity ratio, biquadratic curve
        Table:TwoIndependentVariables object can also be used
        curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        edb = process entering dry-bulb temperature [C]
        ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name`
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
                                 'for field `leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name`')

        self._data["Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def leaving_humidity_ratio_function_of_air_velocity_curve_name(self):
        """Get leaving_humidity_ratio_function_of_air_velocity_curve_name

        Returns:
            str: the value of `leaving_humidity_ratio_function_of_air_velocity_curve_name` or None if not set
        """
        return self._data["Leaving Humidity Ratio Function of Air Velocity Curve Name"]

    @leaving_humidity_ratio_function_of_air_velocity_curve_name.setter
    def leaving_humidity_ratio_function_of_air_velocity_curve_name(self, value=None):
        """  Corresponds to IDD Field `leaving_humidity_ratio_function_of_air_velocity_curve_name`
        Leaving humidity ratio of process air as a function of
        process air velocity, quadratic curve.
        Table:OneIndependentVariable object can also be used
        curve = C1 + C2*v + C3*v**2
        v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `leaving_humidity_ratio_function_of_air_velocity_curve_name`
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
                                 'for field `leaving_humidity_ratio_function_of_air_velocity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `leaving_humidity_ratio_function_of_air_velocity_curve_name`')

        self._data["Leaving Humidity Ratio Function of Air Velocity Curve Name"] = value

    @property
    def regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name(self):
        """Get regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name

        Returns:
            str: the value of `regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self._data["Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name`
        Regeneration energy [J/kg of water removed] as a function of
        entering dry-bulb and entering humidity ratio, biquadratic curve
        Table:TwoIndependentVariables object can also be used
        curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        edb = process entering dry-bulb temperature [C]
        ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name`
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
                                 'for field `regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name`')

        self._data["Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def regeneration_energy_function_of_air_velocity_curve_name(self):
        """Get regeneration_energy_function_of_air_velocity_curve_name

        Returns:
            str: the value of `regeneration_energy_function_of_air_velocity_curve_name` or None if not set
        """
        return self._data["Regeneration Energy Function of Air Velocity Curve Name"]

    @regeneration_energy_function_of_air_velocity_curve_name.setter
    def regeneration_energy_function_of_air_velocity_curve_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_energy_function_of_air_velocity_curve_name`
        Regeneration energy [J/kg of water removed] as a function of
        process air velocity, quadratic curve.
        Table:OneIndependentVariable object can also be used
        curve = C1 + C2*v + C3*v**2
        v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `regeneration_energy_function_of_air_velocity_curve_name`
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
                                 'for field `regeneration_energy_function_of_air_velocity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_energy_function_of_air_velocity_curve_name`')

        self._data["Regeneration Energy Function of Air Velocity Curve Name"] = value

    @property
    def regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name(self):
        """Get regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name

        Returns:
            str: the value of `regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self._data["Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name`
        Regeneration velocity [m/s] as a function of
        entering dry-bulb and entering humidity ratio, biquadratic curve
        Table:TwoIndependentVariables object can also be used
        curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        edb = process entering dry-bulb temperature [C]
        ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name`
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
                                 'for field `regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name`')

        self._data["Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def regeneration_velocity_function_of_air_velocity_curve_name(self):
        """Get regeneration_velocity_function_of_air_velocity_curve_name

        Returns:
            str: the value of `regeneration_velocity_function_of_air_velocity_curve_name` or None if not set
        """
        return self._data["Regeneration Velocity Function of Air Velocity Curve Name"]

    @regeneration_velocity_function_of_air_velocity_curve_name.setter
    def regeneration_velocity_function_of_air_velocity_curve_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_velocity_function_of_air_velocity_curve_name`
        Regeneration velocity [m/s] as a function of
        process air velocity, quadratic curve.
        Table:OneIndependentVariable object can also be used
        curve = C1 + C2*v + C3*v**2
        v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `regeneration_velocity_function_of_air_velocity_curve_name`
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
                                 'for field `regeneration_velocity_function_of_air_velocity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_velocity_function_of_air_velocity_curve_name`')

        self._data["Regeneration Velocity Function of Air Velocity Curve Name"] = value

    @property
    def nominal_regeneration_temperature(self):
        """Get nominal_regeneration_temperature

        Returns:
            float: the value of `nominal_regeneration_temperature` or None if not set
        """
        return self._data["Nominal Regeneration Temperature"]

    @nominal_regeneration_temperature.setter
    def nominal_regeneration_temperature(self, value=None):
        """  Corresponds to IDD Field `nominal_regeneration_temperature`
        Nominal regen temperature upon which the regen energy modifier
        curve is based.  Not used if Default if chosen for the field Performance Mode Type.
        121 C is a commonly used value.

        Args:
            value (float): value for IDD Field `nominal_regeneration_temperature`
                Unit: C
                value >= 40.0
                value <= 250.0
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
                                 'for field `nominal_regeneration_temperature`'.format(value))
            if value < 40.0:
                raise ValueError('value need to be greater or equal 40.0 '
                                 'for field `nominal_regeneration_temperature`')
            if value > 250.0:
                raise ValueError('value need to be smaller 250.0 '
                                 'for field `nominal_regeneration_temperature`')

        self._data["Nominal Regeneration Temperature"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.process_air_inlet_node_name))
        out.append(self._to_str(self.process_air_outlet_node_name))
        out.append(self._to_str(self.regeneration_air_inlet_node_name))
        out.append(self._to_str(self.regeneration_fan_inlet_node_name))
        out.append(self._to_str(self.control_type))
        out.append(self._to_str(self.leaving_maximum_humidity_ratio_setpoint))
        out.append(self._to_str(self.nominal_process_air_flow_rate))
        out.append(self._to_str(self.nominal_process_air_velocity))
        out.append(self._to_str(self.rotor_power))
        out.append(self._to_str(self.regeneration_coil_object_type))
        out.append(self._to_str(self.regeneration_coil_name))
        out.append(self._to_str(self.regeneration_fan_object_type))
        out.append(self._to_str(self.regeneration_fan_name))
        out.append(self._to_str(self.performance_model_type))
        out.append(self._to_str(self.leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name))
        out.append(self._to_str(self.leaving_drybulb_function_of_air_velocity_curve_name))
        out.append(self._to_str(self.leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name))
        out.append(self._to_str(self.leaving_humidity_ratio_function_of_air_velocity_curve_name))
        out.append(self._to_str(self.regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name))
        out.append(self._to_str(self.regeneration_energy_function_of_air_velocity_curve_name))
        out.append(self._to_str(self.regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name))
        out.append(self._to_str(self.regeneration_velocity_function_of_air_velocity_curve_name))
        out.append(self._to_str(self.nominal_regeneration_temperature))
        return ",".join(out)

class DehumidifierDesiccantSystem(object):
    """ Corresponds to IDD object `Dehumidifier:Desiccant:System`
        This compound object models a desiccant heat exchanger, an optional
        heater, and associated fans. The process air stream is the air which
        is dehumidified. The regeneration air stream is the air which is
        heated to regenerate the desiccant. The desiccant heat exchanger
        transfers both sensible and latent energy between the process and
        regeneration air streams. The desiccant dehumidifier is typically used
        in an AirLoopHVAC:OutdoorAirSystem, but can also be specified in any AirLoopHVAC.
    """
    internal_name = "Dehumidifier:Desiccant:System"
    field_count = 18

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Dehumidifier:Desiccant:System`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Desiccant Heat Exchanger Object Type"] = None
        self._data["Desiccant Heat Exchanger Name"] = None
        self._data["Sensor Node Name"] = None
        self._data["Regeneration Air Fan Object Type"] = None
        self._data["Regeneration Air Fan Name"] = None
        self._data["Regeneration Air Fan Placement"] = None
        self._data["Regeneration Air Heater Object Type"] = None
        self._data["Regeneration Air Heater Name"] = None
        self._data["Regeneration Inlet Air Setpoint Temperature"] = None
        self._data["Companion Cooling Coil Object Type"] = None
        self._data["Companion Cooling Coil Name"] = None
        self._data["Companion Cooling Coil Upstream of Dehumidifier Process Inlet"] = None
        self._data["Companion Coil Regeneration Air Heating"] = None
        self._data["Exhaust Fan Maximum Flow Rate"] = None
        self._data["Exhaust Fan Maximum Power"] = None
        self._data["Exhaust Fan Power Curve Name"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.desiccant_heat_exchanger_object_type = None
        else:
            self.desiccant_heat_exchanger_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.desiccant_heat_exchanger_name = None
        else:
            self.desiccant_heat_exchanger_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sensor_node_name = None
        else:
            self.sensor_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_air_fan_object_type = None
        else:
            self.regeneration_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_air_fan_name = None
        else:
            self.regeneration_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_air_fan_placement = None
        else:
            self.regeneration_air_fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_air_heater_object_type = None
        else:
            self.regeneration_air_heater_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_air_heater_name = None
        else:
            self.regeneration_air_heater_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_inlet_air_setpoint_temperature = None
        else:
            self.regeneration_inlet_air_setpoint_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.companion_cooling_coil_object_type = None
        else:
            self.companion_cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.companion_cooling_coil_name = None
        else:
            self.companion_cooling_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.companion_cooling_coil_upstream_of_dehumidifier_process_inlet = None
        else:
            self.companion_cooling_coil_upstream_of_dehumidifier_process_inlet = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.companion_coil_regeneration_air_heating = None
        else:
            self.companion_coil_regeneration_air_heating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_fan_maximum_flow_rate = None
        else:
            self.exhaust_fan_maximum_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_fan_maximum_power = None
        else:
            self.exhaust_fan_maximum_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_fan_power_curve_name = None
        else:
            self.exhaust_fan_power_curve_name = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

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

        self._data["Availability Schedule Name"] = value

    @property
    def desiccant_heat_exchanger_object_type(self):
        """Get desiccant_heat_exchanger_object_type

        Returns:
            str: the value of `desiccant_heat_exchanger_object_type` or None if not set
        """
        return self._data["Desiccant Heat Exchanger Object Type"]

    @desiccant_heat_exchanger_object_type.setter
    def desiccant_heat_exchanger_object_type(self, value=None):
        """  Corresponds to IDD Field `desiccant_heat_exchanger_object_type`

        Args:
            value (str): value for IDD Field `desiccant_heat_exchanger_object_type`
                Accepted values are:
                      - HeatExchanger:Desiccant:BalancedFlow
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
                                 'for field `desiccant_heat_exchanger_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `desiccant_heat_exchanger_object_type`')
            vals = set()
            vals.add("HeatExchanger:Desiccant:BalancedFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `desiccant_heat_exchanger_object_type`'.format(value))

        self._data["Desiccant Heat Exchanger Object Type"] = value

    @property
    def desiccant_heat_exchanger_name(self):
        """Get desiccant_heat_exchanger_name

        Returns:
            str: the value of `desiccant_heat_exchanger_name` or None if not set
        """
        return self._data["Desiccant Heat Exchanger Name"]

    @desiccant_heat_exchanger_name.setter
    def desiccant_heat_exchanger_name(self, value=None):
        """  Corresponds to IDD Field `desiccant_heat_exchanger_name`

        Args:
            value (str): value for IDD Field `desiccant_heat_exchanger_name`
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
                                 'for field `desiccant_heat_exchanger_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `desiccant_heat_exchanger_name`')

        self._data["Desiccant Heat Exchanger Name"] = value

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

        self._data["Sensor Node Name"] = value

    @property
    def regeneration_air_fan_object_type(self):
        """Get regeneration_air_fan_object_type

        Returns:
            str: the value of `regeneration_air_fan_object_type` or None if not set
        """
        return self._data["Regeneration Air Fan Object Type"]

    @regeneration_air_fan_object_type.setter
    def regeneration_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `regeneration_air_fan_object_type`

        Args:
            value (str): value for IDD Field `regeneration_air_fan_object_type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
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
                                 'for field `regeneration_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `regeneration_air_fan_object_type`'.format(value))

        self._data["Regeneration Air Fan Object Type"] = value

    @property
    def regeneration_air_fan_name(self):
        """Get regeneration_air_fan_name

        Returns:
            str: the value of `regeneration_air_fan_name` or None if not set
        """
        return self._data["Regeneration Air Fan Name"]

    @regeneration_air_fan_name.setter
    def regeneration_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_air_fan_name`

        Args:
            value (str): value for IDD Field `regeneration_air_fan_name`
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
                                 'for field `regeneration_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_fan_name`')

        self._data["Regeneration Air Fan Name"] = value

    @property
    def regeneration_air_fan_placement(self):
        """Get regeneration_air_fan_placement

        Returns:
            str: the value of `regeneration_air_fan_placement` or None if not set
        """
        return self._data["Regeneration Air Fan Placement"]

    @regeneration_air_fan_placement.setter
    def regeneration_air_fan_placement(self, value="DrawThrough"):
        """  Corresponds to IDD Field `regeneration_air_fan_placement`

        Args:
            value (str): value for IDD Field `regeneration_air_fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: DrawThrough
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
                                 'for field `regeneration_air_fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `regeneration_air_fan_placement`'.format(value))

        self._data["Regeneration Air Fan Placement"] = value

    @property
    def regeneration_air_heater_object_type(self):
        """Get regeneration_air_heater_object_type

        Returns:
            str: the value of `regeneration_air_heater_object_type` or None if not set
        """
        return self._data["Regeneration Air Heater Object Type"]

    @regeneration_air_heater_object_type.setter
    def regeneration_air_heater_object_type(self, value=None):
        """  Corresponds to IDD Field `regeneration_air_heater_object_type`
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `regeneration_air_heater_object_type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Water
                      - Coil:Heating:Steam
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
                                 'for field `regeneration_air_heater_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_heater_object_type`')
            vals = set()
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `regeneration_air_heater_object_type`'.format(value))

        self._data["Regeneration Air Heater Object Type"] = value

    @property
    def regeneration_air_heater_name(self):
        """Get regeneration_air_heater_name

        Returns:
            str: the value of `regeneration_air_heater_name` or None if not set
        """
        return self._data["Regeneration Air Heater Name"]

    @regeneration_air_heater_name.setter
    def regeneration_air_heater_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_air_heater_name`

        Args:
            value (str): value for IDD Field `regeneration_air_heater_name`
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
                                 'for field `regeneration_air_heater_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_heater_name`')

        self._data["Regeneration Air Heater Name"] = value

    @property
    def regeneration_inlet_air_setpoint_temperature(self):
        """Get regeneration_inlet_air_setpoint_temperature

        Returns:
            float: the value of `regeneration_inlet_air_setpoint_temperature` or None if not set
        """
        return self._data["Regeneration Inlet Air Setpoint Temperature"]

    @regeneration_inlet_air_setpoint_temperature.setter
    def regeneration_inlet_air_setpoint_temperature(self, value=None):
        """  Corresponds to IDD Field `regeneration_inlet_air_setpoint_temperature`

        Args:
            value (float): value for IDD Field `regeneration_inlet_air_setpoint_temperature`
                Unit: C
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
                                 'for field `regeneration_inlet_air_setpoint_temperature`'.format(value))

        self._data["Regeneration Inlet Air Setpoint Temperature"] = value

    @property
    def companion_cooling_coil_object_type(self):
        """Get companion_cooling_coil_object_type

        Returns:
            str: the value of `companion_cooling_coil_object_type` or None if not set
        """
        return self._data["Companion Cooling Coil Object Type"]

    @companion_cooling_coil_object_type.setter
    def companion_cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `companion_cooling_coil_object_type`

        Args:
            value (str): value for IDD Field `companion_cooling_coil_object_type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - Coil:Cooling:DX:TwoStageWithHumidityControlMode
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
                                 'for field `companion_cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `companion_cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:DX:SingleSpeed")
            vals.add("Coil:Cooling:DX:TwoStageWithHumidityControlMode")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `companion_cooling_coil_object_type`'.format(value))

        self._data["Companion Cooling Coil Object Type"] = value

    @property
    def companion_cooling_coil_name(self):
        """Get companion_cooling_coil_name

        Returns:
            str: the value of `companion_cooling_coil_name` or None if not set
        """
        return self._data["Companion Cooling Coil Name"]

    @companion_cooling_coil_name.setter
    def companion_cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `companion_cooling_coil_name`

        Args:
            value (str): value for IDD Field `companion_cooling_coil_name`
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
                                 'for field `companion_cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `companion_cooling_coil_name`')

        self._data["Companion Cooling Coil Name"] = value

    @property
    def companion_cooling_coil_upstream_of_dehumidifier_process_inlet(self):
        """Get companion_cooling_coil_upstream_of_dehumidifier_process_inlet

        Returns:
            str: the value of `companion_cooling_coil_upstream_of_dehumidifier_process_inlet` or None if not set
        """
        return self._data["Companion Cooling Coil Upstream of Dehumidifier Process Inlet"]

    @companion_cooling_coil_upstream_of_dehumidifier_process_inlet.setter
    def companion_cooling_coil_upstream_of_dehumidifier_process_inlet(self, value="No"):
        """  Corresponds to IDD Field `companion_cooling_coil_upstream_of_dehumidifier_process_inlet`
        Select Yes if the companion cooling coil is located directly upstream
        of the desiccant heat exchanger's process air inlet node.

        Args:
            value (str): value for IDD Field `companion_cooling_coil_upstream_of_dehumidifier_process_inlet`
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
                                 'for field `companion_cooling_coil_upstream_of_dehumidifier_process_inlet`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `companion_cooling_coil_upstream_of_dehumidifier_process_inlet`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `companion_cooling_coil_upstream_of_dehumidifier_process_inlet`'.format(value))

        self._data["Companion Cooling Coil Upstream of Dehumidifier Process Inlet"] = value

    @property
    def companion_coil_regeneration_air_heating(self):
        """Get companion_coil_regeneration_air_heating

        Returns:
            str: the value of `companion_coil_regeneration_air_heating` or None if not set
        """
        return self._data["Companion Coil Regeneration Air Heating"]

    @companion_coil_regeneration_air_heating.setter
    def companion_coil_regeneration_air_heating(self, value="No"):
        """  Corresponds to IDD Field `companion_coil_regeneration_air_heating`

        Args:
            value (str): value for IDD Field `companion_coil_regeneration_air_heating`
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
                                 'for field `companion_coil_regeneration_air_heating`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `companion_coil_regeneration_air_heating`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `companion_coil_regeneration_air_heating`'.format(value))

        self._data["Companion Coil Regeneration Air Heating"] = value

    @property
    def exhaust_fan_maximum_flow_rate(self):
        """Get exhaust_fan_maximum_flow_rate

        Returns:
            float: the value of `exhaust_fan_maximum_flow_rate` or None if not set
        """
        return self._data["Exhaust Fan Maximum Flow Rate"]

    @exhaust_fan_maximum_flow_rate.setter
    def exhaust_fan_maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `exhaust_fan_maximum_flow_rate`

        Args:
            value (float): value for IDD Field `exhaust_fan_maximum_flow_rate`
                Unit: m3/s
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
                                 'for field `exhaust_fan_maximum_flow_rate`'.format(value))

        self._data["Exhaust Fan Maximum Flow Rate"] = value

    @property
    def exhaust_fan_maximum_power(self):
        """Get exhaust_fan_maximum_power

        Returns:
            float: the value of `exhaust_fan_maximum_power` or None if not set
        """
        return self._data["Exhaust Fan Maximum Power"]

    @exhaust_fan_maximum_power.setter
    def exhaust_fan_maximum_power(self, value=None):
        """  Corresponds to IDD Field `exhaust_fan_maximum_power`

        Args:
            value (float): value for IDD Field `exhaust_fan_maximum_power`
                Unit: W
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
                                 'for field `exhaust_fan_maximum_power`'.format(value))

        self._data["Exhaust Fan Maximum Power"] = value

    @property
    def exhaust_fan_power_curve_name(self):
        """Get exhaust_fan_power_curve_name

        Returns:
            str: the value of `exhaust_fan_power_curve_name` or None if not set
        """
        return self._data["Exhaust Fan Power Curve Name"]

    @exhaust_fan_power_curve_name.setter
    def exhaust_fan_power_curve_name(self, value=None):
        """  Corresponds to IDD Field `exhaust_fan_power_curve_name`
        Curve object type must be Curve:Quadratic or Curve:Cubic
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `exhaust_fan_power_curve_name`
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
                                 'for field `exhaust_fan_power_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_fan_power_curve_name`')

        self._data["Exhaust Fan Power Curve Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.desiccant_heat_exchanger_object_type))
        out.append(self._to_str(self.desiccant_heat_exchanger_name))
        out.append(self._to_str(self.sensor_node_name))
        out.append(self._to_str(self.regeneration_air_fan_object_type))
        out.append(self._to_str(self.regeneration_air_fan_name))
        out.append(self._to_str(self.regeneration_air_fan_placement))
        out.append(self._to_str(self.regeneration_air_heater_object_type))
        out.append(self._to_str(self.regeneration_air_heater_name))
        out.append(self._to_str(self.regeneration_inlet_air_setpoint_temperature))
        out.append(self._to_str(self.companion_cooling_coil_object_type))
        out.append(self._to_str(self.companion_cooling_coil_name))
        out.append(self._to_str(self.companion_cooling_coil_upstream_of_dehumidifier_process_inlet))
        out.append(self._to_str(self.companion_coil_regeneration_air_heating))
        out.append(self._to_str(self.exhaust_fan_maximum_flow_rate))
        out.append(self._to_str(self.exhaust_fan_maximum_power))
        out.append(self._to_str(self.exhaust_fan_power_curve_name))
        return ",".join(out)