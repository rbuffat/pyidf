from collections import OrderedDict

class CoilSystemCoolingDx(object):
    """ Corresponds to IDD object `CoilSystem:Cooling:DX`
        Virtual container component that consists of a DX cooling coil and its associated
        controls. This control object supports several different types of DX cooling coils
        and may be placed directly in an air loop branch or outdoor air equipment list.
    """
    internal_name = "CoilSystem:Cooling:DX"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoilSystem:Cooling:DX`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["DX Cooling Coil System Inlet Node Name"] = None
        self._data["DX Cooling Coil System Outlet Node Name"] = None
        self._data["DX Cooling Coil System Sensor Node Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Dehumidification Control Type"] = None
        self._data["Run on Sensible Load"] = None
        self._data["Run on Latent Load"] = None
        self._data["Use Outdoor Air DX Cooling Coil"] = None
        self._data["Outdoor Air DX Cooling Coil Leaving Minimum Air Temperature"] = None

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
            self.dx_cooling_coil_system_inlet_node_name = None
        else:
            self.dx_cooling_coil_system_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dx_cooling_coil_system_outlet_node_name = None
        else:
            self.dx_cooling_coil_system_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dx_cooling_coil_system_sensor_node_name = None
        else:
            self.dx_cooling_coil_system_sensor_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dehumidification_control_type = None
        else:
            self.dehumidification_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.run_on_sensible_load = None
        else:
            self.run_on_sensible_load = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.run_on_latent_load = None
        else:
            self.run_on_latent_load = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_outdoor_air_dx_cooling_coil = None
        else:
            self.use_outdoor_air_dx_cooling_coil = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature = None
        else:
            self.outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature = vals[i]
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
    def dx_cooling_coil_system_inlet_node_name(self):
        """Get dx_cooling_coil_system_inlet_node_name

        Returns:
            str: the value of `dx_cooling_coil_system_inlet_node_name` or None if not set
        """
        return self._data["DX Cooling Coil System Inlet Node Name"]

    @dx_cooling_coil_system_inlet_node_name.setter
    def dx_cooling_coil_system_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `dx_cooling_coil_system_inlet_node_name`

        Args:
            value (str): value for IDD Field `dx_cooling_coil_system_inlet_node_name`
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
                                 'for field `dx_cooling_coil_system_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dx_cooling_coil_system_inlet_node_name`')

        self._data["DX Cooling Coil System Inlet Node Name"] = value

    @property
    def dx_cooling_coil_system_outlet_node_name(self):
        """Get dx_cooling_coil_system_outlet_node_name

        Returns:
            str: the value of `dx_cooling_coil_system_outlet_node_name` or None if not set
        """
        return self._data["DX Cooling Coil System Outlet Node Name"]

    @dx_cooling_coil_system_outlet_node_name.setter
    def dx_cooling_coil_system_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `dx_cooling_coil_system_outlet_node_name`

        Args:
            value (str): value for IDD Field `dx_cooling_coil_system_outlet_node_name`
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
                                 'for field `dx_cooling_coil_system_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dx_cooling_coil_system_outlet_node_name`')

        self._data["DX Cooling Coil System Outlet Node Name"] = value

    @property
    def dx_cooling_coil_system_sensor_node_name(self):
        """Get dx_cooling_coil_system_sensor_node_name

        Returns:
            str: the value of `dx_cooling_coil_system_sensor_node_name` or None if not set
        """
        return self._data["DX Cooling Coil System Sensor Node Name"]

    @dx_cooling_coil_system_sensor_node_name.setter
    def dx_cooling_coil_system_sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `dx_cooling_coil_system_sensor_node_name`

        Args:
            value (str): value for IDD Field `dx_cooling_coil_system_sensor_node_name`
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
                                 'for field `dx_cooling_coil_system_sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dx_cooling_coil_system_sensor_node_name`')

        self._data["DX Cooling Coil System Sensor Node Name"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `cooling_coil_object_type`

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - CoilSystem:Cooling:DX:HeatExchangerAssisted
                      - Coil:Cooling:DX:TwoSpeed
                      - Coil:Cooling:DX:TwoStageWithHumidityControlMode
                      - Coil:Cooling:DX:VariableSpeed
                      - Coil:Cooling:DX:SingleSpeed:ThermalStorage
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
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:DX:SingleSpeed")
            vals.add("CoilSystem:Cooling:DX:HeatExchangerAssisted")
            vals.add("Coil:Cooling:DX:TwoSpeed")
            vals.add("Coil:Cooling:DX:TwoStageWithHumidityControlMode")
            vals.add("Coil:Cooling:DX:VariableSpeed")
            vals.add("Coil:Cooling:DX:SingleSpeed:ThermalStorage")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_coil_object_type`'.format(value))

        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """Get cooling_coil_name

        Returns:
            str: the value of `cooling_coil_name` or None if not set
        """
        return self._data["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `cooling_coil_name`

        Args:
            value (str): value for IDD Field `cooling_coil_name`
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
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_name`')

        self._data["Cooling Coil Name"] = value

    @property
    def dehumidification_control_type(self):
        """Get dehumidification_control_type

        Returns:
            str: the value of `dehumidification_control_type` or None if not set
        """
        return self._data["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="None"):
        """  Corresponds to IDD Field `dehumidification_control_type`
        None = meet sensible load only
        Multimode = activate enhanced dehumidification mode
        as needed and meet sensible load. If no sensible load
        exists, and Run on Latent Load = Yes, and a latent
        load exists, the unit will operate to meet the latent load.
        Valid only with Coil:Cooling:DX:TwoStageWithHumidityControlMode
        or CoilSystem:Cooling:DX:HeatExchangerAssisted.
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.
        Valid for all coil types.
        For all dehumidification controls, the max
        humidity setpoint on the Sensor Node is used.
        SetpointManager:SingleZone:Humidity:Maximum,
        SetpointManager:MultiZone:Humidity:Maximum, or
        SetpointManager:MultiZone:MaximumHumidity:Average, and
        SetpointManager:OutdoorAirPretreat (optional) objects.

        Args:
            value (str): value for IDD Field `dehumidification_control_type`
                Accepted values are:
                      - None
                      - Multimode
                      - CoolReheat
                Default value: None
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
                                 'for field `dehumidification_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dehumidification_control_type`')
            vals = set()
            vals.add("None")
            vals.add("Multimode")
            vals.add("CoolReheat")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `dehumidification_control_type`'.format(value))

        self._data["Dehumidification Control Type"] = value

    @property
    def run_on_sensible_load(self):
        """Get run_on_sensible_load

        Returns:
            str: the value of `run_on_sensible_load` or None if not set
        """
        return self._data["Run on Sensible Load"]

    @run_on_sensible_load.setter
    def run_on_sensible_load(self, value="Yes"):
        """  Corresponds to IDD Field `run_on_sensible_load`
        If Yes, unit will run if there is a sensible load.
        If No, unit will not run if there is only a sensible load.
        Dehumidification controls will be active if specified.

        Args:
            value (str): value for IDD Field `run_on_sensible_load`
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
                                 'for field `run_on_sensible_load`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `run_on_sensible_load`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `run_on_sensible_load`'.format(value))

        self._data["Run on Sensible Load"] = value

    @property
    def run_on_latent_load(self):
        """Get run_on_latent_load

        Returns:
            str: the value of `run_on_latent_load` or None if not set
        """
        return self._data["Run on Latent Load"]

    @run_on_latent_load.setter
    def run_on_latent_load(self, value="No"):
        """  Corresponds to IDD Field `run_on_latent_load`
        If Yes, unit will run if there is a latent load.
        even if there is no sensible load.
        If No, unit will not run only if there is a latent load.
        Dehumidification controls will be active if specified.

        Args:
            value (str): value for IDD Field `run_on_latent_load`
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
                                 'for field `run_on_latent_load`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `run_on_latent_load`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `run_on_latent_load`'.format(value))

        self._data["Run on Latent Load"] = value

    @property
    def use_outdoor_air_dx_cooling_coil(self):
        """Get use_outdoor_air_dx_cooling_coil

        Returns:
            str: the value of `use_outdoor_air_dx_cooling_coil` or None if not set
        """
        return self._data["Use Outdoor Air DX Cooling Coil"]

    @use_outdoor_air_dx_cooling_coil.setter
    def use_outdoor_air_dx_cooling_coil(self, value="No"):
        """  Corresponds to IDD Field `use_outdoor_air_dx_cooling_coil`
        This input field is designed for use with DX cooling coils with low air flow
        to capacity ratio range (100 - 300 cfm/ton). Typical application is 100% dedicated
        outdoor air system (DOAS). Other air loop or zone HVAC systems with low flow
        to capacity ratio range may also use this input field.  If Yes, the DX cooling
        coil runs as 100% DOAS DX coil or low flow to capacity ratio range.
        If No, the DX cooling coil runs as a regular DX coil. If left blank the
        default is regular DX coil.

        Args:
            value (str): value for IDD Field `use_outdoor_air_dx_cooling_coil`
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
                                 'for field `use_outdoor_air_dx_cooling_coil`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_outdoor_air_dx_cooling_coil`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_outdoor_air_dx_cooling_coil`'.format(value))

        self._data["Use Outdoor Air DX Cooling Coil"] = value

    @property
    def outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature(self):
        """Get outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature

        Returns:
            float: the value of `outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature` or None if not set
        """
        return self._data["Outdoor Air DX Cooling Coil Leaving Minimum Air Temperature"]

    @outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature.setter
    def outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature(self, value=2.0 ):
        """  Corresponds to IDD Field `outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature`
        DX cooling coil leaving minimum air temperature defines the minimum DX cooling coil
        leaving air temperature that should be maintained to avoid frost formation. This input
        field is optional and only used along with the input field above.

        Args:
            value (float): value for IDD Field `outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature`
                Unit: C
                Default value: 2.0
                value >= 0.0
                value <= 7.2
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
                                 'for field `outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature`')
            if value > 7.2:
                raise ValueError('value need to be smaller 7.2 '
                                 'for field `outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature`')

        self._data["Outdoor Air DX Cooling Coil Leaving Minimum Air Temperature"] = value

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
        out.append(self._to_str(self.dx_cooling_coil_system_inlet_node_name))
        out.append(self._to_str(self.dx_cooling_coil_system_outlet_node_name))
        out.append(self._to_str(self.dx_cooling_coil_system_sensor_node_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.dehumidification_control_type))
        out.append(self._to_str(self.run_on_sensible_load))
        out.append(self._to_str(self.run_on_latent_load))
        out.append(self._to_str(self.use_outdoor_air_dx_cooling_coil))
        out.append(self._to_str(self.outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature))
        return ",".join(out)

class CoilSystemHeatingDx(object):
    """ Corresponds to IDD object `CoilSystem:Heating:DX`
        Virtual container component that consists of a DX heating coil (heat pump) and its
        associated controls. This control object supports two different types of DX heating
        coils and may be placed directly in an air loop branch or outdoor air equipment list.
    """
    internal_name = "CoilSystem:Heating:DX"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoilSystem:Heating:DX`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None

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
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
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
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `heating_coil_object_type`

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:DX:SingleSpeed
                      - Coil:Heating:DX:VariableSpeed
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
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:DX:SingleSpeed")
            vals.add("Coil:Heating:DX:VariableSpeed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_coil_object_type`'.format(value))

        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """Get heating_coil_name

        Returns:
            str: the value of `heating_coil_name` or None if not set
        """
        return self._data["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `heating_coil_name`

        Args:
            value (str): value for IDD Field `heating_coil_name`
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
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_name`')

        self._data["Heating Coil Name"] = value

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
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        return ",".join(out)

class CoilSystemCoolingWaterHeatExchangerAssisted(object):
    """ Corresponds to IDD object `CoilSystem:Cooling:Water:HeatExchangerAssisted`
        Virtual component consisting of a chilled-water cooling coil and an air-to-air heat
        exchanger. The air-to-air heat exchanger precools the air entering the cooling coil
        and reuses this energy to reheat the supply air leaving the cooling coil. This heat
        exchange process improves the latent removal performance of the cooling coil (lower
        sensible heat ratio).
    """
    internal_name = "CoilSystem:Cooling:Water:HeatExchangerAssisted"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoilSystem:Cooling:Water:HeatExchangerAssisted`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Heat Exchanger Object Type"] = None
        self._data["Heat Exchanger Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None

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
            self.heat_exchanger_object_type = None
        else:
            self.heat_exchanger_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_exchanger_name = None
        else:
            self.heat_exchanger_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
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
    def heat_exchanger_object_type(self):
        """Get heat_exchanger_object_type

        Returns:
            str: the value of `heat_exchanger_object_type` or None if not set
        """
        return self._data["Heat Exchanger Object Type"]

    @heat_exchanger_object_type.setter
    def heat_exchanger_object_type(self, value=None):
        """  Corresponds to IDD Field `heat_exchanger_object_type`

        Args:
            value (str): value for IDD Field `heat_exchanger_object_type`
                Accepted values are:
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
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
                                 'for field `heat_exchanger_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchanger_object_type`')
            vals = set()
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heat_exchanger_object_type`'.format(value))

        self._data["Heat Exchanger Object Type"] = value

    @property
    def heat_exchanger_name(self):
        """Get heat_exchanger_name

        Returns:
            str: the value of `heat_exchanger_name` or None if not set
        """
        return self._data["Heat Exchanger Name"]

    @heat_exchanger_name.setter
    def heat_exchanger_name(self, value=None):
        """  Corresponds to IDD Field `heat_exchanger_name`

        Args:
            value (str): value for IDD Field `heat_exchanger_name`
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
                                 'for field `heat_exchanger_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchanger_name`')

        self._data["Heat Exchanger Name"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `cooling_coil_object_type`

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
                Accepted values are:
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
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
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_coil_object_type`'.format(value))

        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """Get cooling_coil_name

        Returns:
            str: the value of `cooling_coil_name` or None if not set
        """
        return self._data["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `cooling_coil_name`

        Args:
            value (str): value for IDD Field `cooling_coil_name`
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
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_name`')

        self._data["Cooling Coil Name"] = value

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
        out.append(self._to_str(self.heat_exchanger_object_type))
        out.append(self._to_str(self.heat_exchanger_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        return ",".join(out)

class CoilSystemCoolingDxHeatExchangerAssisted(object):
    """ Corresponds to IDD object `CoilSystem:Cooling:DX:HeatExchangerAssisted`
        Virtual component consisting of a direct expansion (DX) cooling coil and an
        air-to-air heat exchanger. The air-to-air heat exchanger precools the air entering the
        cooling coil and reuses this energy to reheat the supply air leaving the cooling
        coil. This heat exchange process improves the latent removal performance of the
        cooling coil (lower sensible heat ratio).
    """
    internal_name = "CoilSystem:Cooling:DX:HeatExchangerAssisted"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CoilSystem:Cooling:DX:HeatExchangerAssisted`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Heat Exchanger Object Type"] = None
        self._data["Heat Exchanger Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None

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
            self.heat_exchanger_object_type = None
        else:
            self.heat_exchanger_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_exchanger_name = None
        else:
            self.heat_exchanger_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
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
    def heat_exchanger_object_type(self):
        """Get heat_exchanger_object_type

        Returns:
            str: the value of `heat_exchanger_object_type` or None if not set
        """
        return self._data["Heat Exchanger Object Type"]

    @heat_exchanger_object_type.setter
    def heat_exchanger_object_type(self, value=None):
        """  Corresponds to IDD Field `heat_exchanger_object_type`

        Args:
            value (str): value for IDD Field `heat_exchanger_object_type`
                Accepted values are:
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
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
                                 'for field `heat_exchanger_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchanger_object_type`')
            vals = set()
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            vals.add("HeatExchanger:Desiccant:BalancedFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heat_exchanger_object_type`'.format(value))

        self._data["Heat Exchanger Object Type"] = value

    @property
    def heat_exchanger_name(self):
        """Get heat_exchanger_name

        Returns:
            str: the value of `heat_exchanger_name` or None if not set
        """
        return self._data["Heat Exchanger Name"]

    @heat_exchanger_name.setter
    def heat_exchanger_name(self, value=None):
        """  Corresponds to IDD Field `heat_exchanger_name`

        Args:
            value (str): value for IDD Field `heat_exchanger_name`
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
                                 'for field `heat_exchanger_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchanger_name`')

        self._data["Heat Exchanger Name"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `cooling_coil_object_type`

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
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
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:DX:SingleSpeed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_coil_object_type`'.format(value))

        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """Get cooling_coil_name

        Returns:
            str: the value of `cooling_coil_name` or None if not set
        """
        return self._data["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `cooling_coil_name`

        Args:
            value (str): value for IDD Field `cooling_coil_name`
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
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_name`')

        self._data["Cooling Coil Name"] = value

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
        out.append(self._to_str(self.heat_exchanger_object_type))
        out.append(self._to_str(self.heat_exchanger_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        return ",".join(out)