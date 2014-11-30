from collections import OrderedDict

class AirLoopHvacUnitarySystem(object):
    """ Corresponds to IDD object `AirLoopHVAC:UnitarySystem`
        AirloopHVAC:UnitarySystem is a generic HVAC system type that allows any
        configuration of coils and/or fan. This object is a replacement of other
        AirloopHVAC objects. This object can be used in outdoor air systems,
        outdoor air units, air loops, and as zone equipment if desired.
    """
    internal_name = "AirLoopHVAC:UnitarySystem"
    field_count = 53

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:UnitarySystem`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Type"] = None
        self._data["Controlling Zone or Thermostat Location"] = None
        self._data["Dehumidification Control Type"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Supply Fan Object Type"] = None
        self._data["Supply Fan Name"] = None
        self._data["Fan Placement"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["DX Heating Coil Sizing Ratio"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Use DOAS DX Cooling Coil"] = None
        self._data["DOAS DX Cooling Coil Leaving Minimum Air Temperature"] = None
        self._data["Latent Load Control"] = None
        self._data["Supplemental Heating Coil Object Type"] = None
        self._data["Supplemental Heating Coil Name"] = None
        self._data["Supply Air Flow Rate Method During Cooling Operation"] = None
        self._data["Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Supply Air Flow Rate Per Floor Area During Cooling Operation"] = None
        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"] = None
        self._data["Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation"] = None
        self._data["Supply air Flow Rate Method During Heating Operation"] = None
        self._data["Supply Air Flow Rate During Heating Operation"] = None
        self._data["Supply Air Flow Rate Per Floor Area during Heating Operation"] = None
        self._data["Fraction of Autosized Design Heating Supply Air Flow Rate"] = None
        self._data["Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation"] = None
        self._data["Supply Air Flow Rate Method When No Cooling or Heating is Required"] = None
        self._data["Supply Air Flow Rate When No Cooling or Heating is Required"] = None
        self._data["Supply Air Flow Rate Per Floor Area When No Cooling or Heating is Required"] = None
        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate v2"] = None
        self._data["Fraction of Autosized Design Heating Supply Air Flow Rate v2"] = None
        self._data["Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation v2"] = None
        self._data["Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation v2"] = None
        self._data["Maximum Supply Air Temperature"] = None
        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = None
        self._data["Outdoor Dry-Bulb Temperature Sensor Node Name"] = None
        self._data["Maximum Cycling Rate"] = None
        self._data["Heat Pump Time Constant"] = None
        self._data["Fraction of On-Cycle Power Use"] = None
        self._data["Heat Pump Fan Delay Time"] = None
        self._data["Ancilliary On-Cycle Electric Power"] = None
        self._data["Ancilliary Off-Cycle Electric Power"] = None
        self._data["Design Heat Recovery Water Flow Rate"] = None
        self._data["Maximum Temperature for Heat Recovery"] = None
        self._data["Heat Recovery Water Inlet Node Name"] = None
        self._data["Heat Recovery Water Outlet Node Name"] = None
        self._data["Design Specification Multispeed Heat Pump Object Type"] = None
        self._data["Design Specification Multispeed Heat Pump Object Name"] = None

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
            self.control_type = None
        else:
            self.control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.controlling_zone_or_thermostat_location = None
        else:
            self.controlling_zone_or_thermostat_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dehumidification_control_type = None
        else:
            self.dehumidification_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_object_type = None
        else:
            self.supply_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_name = None
        else:
            self.supply_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
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
        if len(vals[i]) == 0:
            self.dx_heating_coil_sizing_ratio = None
        else:
            self.dx_heating_coil_sizing_ratio = vals[i]
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
            self.use_doas_dx_cooling_coil = None
        else:
            self.use_doas_dx_cooling_coil = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.doas_dx_cooling_coil_leaving_minimum_air_temperature = None
        else:
            self.doas_dx_cooling_coil_leaving_minimum_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.latent_load_control = None
        else:
            self.latent_load_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_object_type = None
        else:
            self.supplemental_heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_name = None
        else:
            self.supplemental_heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_method_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_method_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_per_floor_area_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_per_floor_area_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate = None
        else:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation = None
        else:
            self.design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_method_during_heating_operation = None
        else:
            self.supply_air_flow_rate_method_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_per_floor_area_during_heating_operation = None
        else:
            self.supply_air_flow_rate_per_floor_area_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_design_heating_supply_air_flow_rate = None
        else:
            self.fraction_of_autosized_design_heating_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation = None
        else:
            self.design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_method_when_no_cooling_or_heating_is_required = None
        else:
            self.supply_air_flow_rate_method_when_no_cooling_or_heating_is_required = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_required = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_required = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required = None
        else:
            self.supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate_v2 = None
        else:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate_v2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_design_heating_supply_air_flow_rate_v2 = None
        else:
            self.fraction_of_autosized_design_heating_supply_air_flow_rate_v2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2 = None
        else:
            self.design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2 = None
        else:
            self.design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature = None
        else:
            self.maximum_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = None
        else:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_drybulb_temperature_sensor_node_name = None
        else:
            self.outdoor_drybulb_temperature_sensor_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_cycling_rate = None
        else:
            self.maximum_cycling_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_pump_time_constant = None
        else:
            self.heat_pump_time_constant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_oncycle_power_use = None
        else:
            self.fraction_of_oncycle_power_use = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_pump_fan_delay_time = None
        else:
            self.heat_pump_fan_delay_time = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ancilliary_oncycle_electric_power = None
        else:
            self.ancilliary_oncycle_electric_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ancilliary_offcycle_electric_power = None
        else:
            self.ancilliary_offcycle_electric_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_heat_recovery_water_flow_rate = None
        else:
            self.design_heat_recovery_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_temperature_for_heat_recovery = None
        else:
            self.maximum_temperature_for_heat_recovery = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_water_inlet_node_name = None
        else:
            self.heat_recovery_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_water_outlet_node_name = None
        else:
            self.heat_recovery_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_multispeed_heat_pump_object_type = None
        else:
            self.design_specification_multispeed_heat_pump_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_specification_multispeed_heat_pump_object_name = None
        else:
            self.design_specification_multispeed_heat_pump_object_name = vals[i]
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
        Unique name for the Unitary System.

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
    def control_type(self):
        """Get control_type

        Returns:
            str: the value of `control_type` or None if not set
        """
        return self._data["Control Type"]

    @control_type.setter
    def control_type(self, value="Load"):
        """  Corresponds to IDD Field `control_type`
        Load control requires a Controlling Zone name.
        SetPoint control requires set points at coil outlet node.

        Args:
            value (str): value for IDD Field `control_type`
                Accepted values are:
                      - Load
                      - SetPoint
                Default value: Load
                if `value` is None it will not be checked against the
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
            vals.add("Load")
            vals.add("SetPoint")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_type`'.format(value))

        self._data["Control Type"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """Get controlling_zone_or_thermostat_location

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set
        """
        return self._data["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """  Corresponds to IDD Field `controlling_zone_or_thermostat_location`
        Used only for Load based control
        Zone name where thermostat is located. Required when Control Type = Load.

        Args:
            value (str): value for IDD Field `controlling_zone_or_thermostat_location`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controlling_zone_or_thermostat_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controlling_zone_or_thermostat_location`')

        self._data["Controlling Zone or Thermostat Location"] = value

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
        as needed and meet sensible load.  Valid only with
        cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted.
        This control mode allows the heat exchanger to be turned
        on and off based on the zone dehumidification requirements.
        A ZoneControl:Humidistat object is also required.
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.  Valid with all
        cooling coil types. When a heat exchanger assisted cooling
        coil is used, the heat exchanger is locked on at all times.
        A ZoneControl:Humidistat object is also required.

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
        A schedule value greater than zero (usually 1 is used) indicates that the unit is
        available to operate as needed. A value less than or equal to zero (usually zero
        is used) denotes that the unit must be off.

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
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_inlet_node_name`
        Enter the node name used as the inlet air node for the unitary system.

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')

        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_outlet_node_name`
        Enter the node name used as the outlet air node for the unitary system.

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')

        self._data["Air Outlet Node Name"] = value

    @property
    def supply_fan_object_type(self):
        """Get supply_fan_object_type

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self._data["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `supply_fan_object_type`
        Enter the type of supply air fan if included in the unitary system.
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. supply
        air fan operating mode schedule values greater than 0).
        Specify a Fan:OnOff object when the Supply Air Fan Operating Mode Schedule Name
        input field above is left blank.
        Specifiy a Fan:VariableVolume when modeling VAV systems which used setpoint based control
        if the fan is included in the unitary system object.
        The variable or constant volume fan may be specified on the branch instead of contained
        within the unitary system object (i.e., this field may be blank for certain configurations).

        Args:
            value (str): value for IDD Field `supply_fan_object_type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
                      - Fan:VariableVolume
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            vals.add("Fan:VariableVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_fan_object_type`'.format(value))

        self._data["Supply Fan Object Type"] = value

    @property
    def supply_fan_name(self):
        """Get supply_fan_name

        Returns:
            str: the value of `supply_fan_name` or None if not set
        """
        return self._data["Supply Fan Name"]

    @supply_fan_name.setter
    def supply_fan_name(self, value=None):
        """  Corresponds to IDD Field `supply_fan_name`
        Enter the name of the supply air fan if included in the unitary system.

        Args:
            value (str): value for IDD Field `supply_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_name`')

        self._data["Supply Fan Name"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value=None):
        """  Corresponds to IDD Field `fan_placement`
        Enter the type of supply air fan if included in the unitary system.

        Args:
            value (str): value for IDD Field `fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

        self._data["Fan Placement"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        A fan operating mode schedule value of 0 indicates cycling fan mode (supply air
        fan cycles on and off in tandem with the cooling or heating coil).
        Any other schedule value indicates continuous fan mode (supply air fan operates
        continuously regardless of cooling or heating coil operation). Provide a schedule
        with non-zero values when high humidity control is specified.
        Leaving this schedule name blank will default to constant fan mode for the
        entire simulation period.
        This field is not used when set point based control is used where a set point
        controls the coil (i.e., model assumes constant fan mode operation).

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')

        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

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
        Enter the type of heating coil if included in the unitary system.

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:DX:SingleSpeed
                      - Coil:Heating:DX:MultiSpeed
                      - Coil:Heating:DX:VariableSpeed
                      - Coil:Heating:WaterToAirHeatPump:ParameterEstimation
                      - Coil:Heating:WaterToAirHeatPump:EquationFit
                      - Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit
                      - Coil:Heating:Gas
                      - Coil:Heating:Gas:MultiStage
                      - Coil:Heating:Electric
                      - Coil:Heating:Electric:MultiStage
                      - Coil:Heating:Water
                      - Coil:Heating:Steam
                      - Coil:Heating:Desuperheater
                if `value` is None it will not be checked against the
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
            vals.add("Coil:Heating:DX:MultiSpeed")
            vals.add("Coil:Heating:DX:VariableSpeed")
            vals.add("Coil:Heating:WaterToAirHeatPump:ParameterEstimation")
            vals.add("Coil:Heating:WaterToAirHeatPump:EquationFit")
            vals.add("Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Gas:MultiStage")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Electric:MultiStage")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            vals.add("Coil:Heating:Desuperheater")
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
        Enter the name of the heating coil if included in the unitary system.

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

    @property
    def dx_heating_coil_sizing_ratio(self):
        """Get dx_heating_coil_sizing_ratio

        Returns:
            float: the value of `dx_heating_coil_sizing_ratio` or None if not set
        """
        return self._data["DX Heating Coil Sizing Ratio"]

    @dx_heating_coil_sizing_ratio.setter
    def dx_heating_coil_sizing_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `dx_heating_coil_sizing_ratio`
        Used to adjust heat pump heating capacity with respect to DX cooling capacity
        used only for heat pump configurations (i.e., a cooling and DX heating coil is used).

        Args:
            value (float): value for IDD Field `dx_heating_coil_sizing_ratio`
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
                                 'for field `dx_heating_coil_sizing_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `dx_heating_coil_sizing_ratio`')

        self._data["DX Heating Coil Sizing Ratio"] = value

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
        Enter the type of cooling coil if included in the unitary system.

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - Coil:Cooling:DX:TwoSpeed
                      - Coil:Cooling:DX:MultiSpeed
                      - Coil:Cooling:DX:VariableSpeed
                      - Coil:Cooling:DX:TwoStageWithHumidityControlMode
                      - CoilSystem:Cooling:DX:HeatExchangerAssisted
                      - Coil:Cooling:WaterToAirHeatPump:ParameterEstimation
                      - Coil:Cooling:WaterToAirHeatPump:EquationFit
                      - Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatExchangerAssisted
                if `value` is None it will not be checked against the
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
            vals.add("Coil:Cooling:DX:TwoSpeed")
            vals.add("Coil:Cooling:DX:MultiSpeed")
            vals.add("Coil:Cooling:DX:VariableSpeed")
            vals.add("Coil:Cooling:DX:TwoStageWithHumidityControlMode")
            vals.add("CoilSystem:Cooling:DX:HeatExchangerAssisted")
            vals.add("Coil:Cooling:WaterToAirHeatPump:ParameterEstimation")
            vals.add("Coil:Cooling:WaterToAirHeatPump:EquationFit")
            vals.add("Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit")
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("CoilSystem:Cooling:Water:HeatExchangerAssisted")
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
        Enter the name of the cooling coil if included in the unitary system.

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
    def use_doas_dx_cooling_coil(self):
        """Get use_doas_dx_cooling_coil

        Returns:
            str: the value of `use_doas_dx_cooling_coil` or None if not set
        """
        return self._data["Use DOAS DX Cooling Coil"]

    @use_doas_dx_cooling_coil.setter
    def use_doas_dx_cooling_coil(self, value="No"):
        """  Corresponds to IDD Field `use_doas_dx_cooling_coil`
        If Yes, the DX cooling coil runs as 100% DOAS DX coil.
        If No, the DX cooling coil runs as a regular DX coil.
        If left blank the default is regular dx coil.

        Args:
            value (str): value for IDD Field `use_doas_dx_cooling_coil`
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
                                 'for field `use_doas_dx_cooling_coil`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_doas_dx_cooling_coil`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `use_doas_dx_cooling_coil`'.format(value))

        self._data["Use DOAS DX Cooling Coil"] = value

    @property
    def doas_dx_cooling_coil_leaving_minimum_air_temperature(self):
        """Get doas_dx_cooling_coil_leaving_minimum_air_temperature

        Returns:
            float: the value of `doas_dx_cooling_coil_leaving_minimum_air_temperature` or None if not set
        """
        return self._data["DOAS DX Cooling Coil Leaving Minimum Air Temperature"]

    @doas_dx_cooling_coil_leaving_minimum_air_temperature.setter
    def doas_dx_cooling_coil_leaving_minimum_air_temperature(self, value=2.0 ):
        """  Corresponds to IDD Field `doas_dx_cooling_coil_leaving_minimum_air_temperature`
        DX cooling coil leaving minimum air temperature defines the minimum DOAS DX cooling coil
        leaving air temperature that should be maintained to avoid frost formation. This input
        field is optional and only used along with the input field above.

        Args:
            value (float): value for IDD Field `doas_dx_cooling_coil_leaving_minimum_air_temperature`
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
                                 'for field `doas_dx_cooling_coil_leaving_minimum_air_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `doas_dx_cooling_coil_leaving_minimum_air_temperature`')
            if value > 7.2:
                raise ValueError('value need to be smaller 7.2 '
                                 'for field `doas_dx_cooling_coil_leaving_minimum_air_temperature`')

        self._data["DOAS DX Cooling Coil Leaving Minimum Air Temperature"] = value

    @property
    def latent_load_control(self):
        """Get latent_load_control

        Returns:
            str: the value of `latent_load_control` or None if not set
        """
        return self._data["Latent Load Control"]

    @latent_load_control.setter
    def latent_load_control(self, value=None):
        """  Corresponds to IDD Field `latent_load_control`
        SensibleOnlyLoadControl is selected when thermostat control is used.
        LatentOnlyLoadControl is selected when humidistat control is used.
        LatentWithSensibleLoadControl is selected when thermostat control is used and
        dehumidification is required only when a sensible load exists.
        LatentOrSensibleLoadControl is selected when thermostat control is used and
        dehumidification is required any time the humidistat set point is exceeded.

        Args:
            value (str): value for IDD Field `latent_load_control`
                Accepted values are:
                      - SensibleOnlyLoadControl
                      - LatentOnlyLoadControl
                      - LatentWithSensibleLoadControl
                      - LatentOrSensibleLoadControl
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `latent_load_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `latent_load_control`')
            vals = set()
            vals.add("SensibleOnlyLoadControl")
            vals.add("LatentOnlyLoadControl")
            vals.add("LatentWithSensibleLoadControl")
            vals.add("LatentOrSensibleLoadControl")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `latent_load_control`'.format(value))

        self._data["Latent Load Control"] = value

    @property
    def supplemental_heating_coil_object_type(self):
        """Get supplemental_heating_coil_object_type

        Returns:
            str: the value of `supplemental_heating_coil_object_type` or None if not set
        """
        return self._data["Supplemental Heating Coil Object Type"]

    @supplemental_heating_coil_object_type.setter
    def supplemental_heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `supplemental_heating_coil_object_type`
        Enter the type of supplemental heating coil if included in the unitary system.
        Only required if dehumidification control type is "CoolReheat".

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
                      - Coil:Heating:Desuperheater
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
                                 'for field `supplemental_heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Desuperheater")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supplemental_heating_coil_object_type`'.format(value))

        self._data["Supplemental Heating Coil Object Type"] = value

    @property
    def supplemental_heating_coil_name(self):
        """Get supplemental_heating_coil_name

        Returns:
            str: the value of `supplemental_heating_coil_name` or None if not set
        """
        return self._data["Supplemental Heating Coil Name"]

    @supplemental_heating_coil_name.setter
    def supplemental_heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `supplemental_heating_coil_name`
        Enter the name of the supplemental heating coil if included in the unitary system.
        Only required if dehumidification control type is "CoolReheat".

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_name`')

        self._data["Supplemental Heating Coil Name"] = value

    @property
    def supply_air_flow_rate_method_during_cooling_operation(self):
        """Get supply_air_flow_rate_method_during_cooling_operation

        Returns:
            str: the value of `supply_air_flow_rate_method_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate Method During Cooling Operation"]

    @supply_air_flow_rate_method_during_cooling_operation.setter
    def supply_air_flow_rate_method_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_method_during_cooling_operation`
        Enter the method used to determine the cooling supply air volume flow rate.
        None is used when a cooling coil is not included in the unitary system or this field may be blank.
        SupplyAirFlowRate is selected when the magnitude of the supply air volume is used.
        FlowPerFloorArea is selected when the supply air volume flow rate is based on total floor area
        served by the unitary system.
        FractionOfAutosizedCoolingValue is selected when the supply air volume is a fraction of the
        value determined by the simulation.
        FlowPerCoolingCapacity is selected when the supply air volume is a fraction of the cooling
        capacity as determined by the simulation.

        Args:
            value (str): value for IDD Field `supply_air_flow_rate_method_during_cooling_operation`
                Accepted values are:
                      - None
                      - SupplyAirFlowRate
                      - FlowPerFloorArea
                      - FractionOfAutosizedCoolingValue
                      - FlowPerCoolingCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_flow_rate_method_during_cooling_operation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_flow_rate_method_during_cooling_operation`')
            vals = set()
            vals.add("None")
            vals.add("SupplyAirFlowRate")
            vals.add("FlowPerFloorArea")
            vals.add("FractionOfAutosizedCoolingValue")
            vals.add("FlowPerCoolingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_flow_rate_method_during_cooling_operation`'.format(value))

        self._data["Supply Air Flow Rate Method During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """Get supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_during_cooling_operation`
        Enter the magnitude of the supply air volume flow rate during cooling operation.
        Required field when Supply air Flow Rate Method During Cooling Operation is SupplyAirFlowRate.
        This field may be blank if a cooling coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_cooling_operation`
                Unit: m3/s
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
                                 'for field `supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_during_cooling_operation`')

        self._data["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_per_floor_area_during_cooling_operation(self):
        """Get supply_air_flow_rate_per_floor_area_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate Per Floor Area During Cooling Operation"]

    @supply_air_flow_rate_per_floor_area_during_cooling_operation.setter
    def supply_air_flow_rate_per_floor_area_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_per_floor_area_during_cooling_operation`
        Enter the supply air volume flow rate per total floor area fraction.
        Required field when Supply air Flow Rate Method During Cooling Operation is FlowPerFloorArea.
        This field may be blank if a cooling coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_per_floor_area_during_cooling_operation`
                Unit: m3/s-m2
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
                                 'for field `supply_air_flow_rate_per_floor_area_during_cooling_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_per_floor_area_during_cooling_operation`')

        self._data["Supply Air Flow Rate Per Floor Area During Cooling Operation"] = value

    @property
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(self):
        """Get fraction_of_autosized_design_cooling_supply_air_flow_rate

        Returns:
            float: the value of `fraction_of_autosized_design_cooling_supply_air_flow_rate` or None if not set
        """
        return self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"]

    @fraction_of_autosized_design_cooling_supply_air_flow_rate.setter
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method During Cooling Operation is FractionOfAutosizedCoolingValue.
        This field may be blank if a cooling coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate`
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
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate`')

        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"] = value

    @property
    def design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation(self):
        """Get design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation` or None if not set
        """
        return self._data["Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation"]

    @design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation.setter
    def design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation`
        Enter the supply air volume flow rate as a fraction of the cooling capacity.
        Required field when Supply air Flow Rate Method During Cooling Operation is FlowPerCoolingCapacity.
        This field may be blank if a cooling coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation`
                Unit: m3/s-W
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
                                 'for field `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation`')

        self._data["Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_method_during_heating_operation(self):
        """Get supply_air_flow_rate_method_during_heating_operation

        Returns:
            str: the value of `supply_air_flow_rate_method_during_heating_operation` or None if not set
        """
        return self._data["Supply air Flow Rate Method During Heating Operation"]

    @supply_air_flow_rate_method_during_heating_operation.setter
    def supply_air_flow_rate_method_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_method_during_heating_operation`
        Enter the method used to determine the heating supply air volume flow rate.
        None is used when a heating coil is not included in the unitary system or this field may be blank.
        SupplyAirFlowRate is selected when the magnitude of the supply air volume is used.
        FlowPerFloorArea is selected when the supply air volume flow rate is based on total floor area
        served by the unitary system.
        FractionOfAutosizedHeatingValue is selected when the supply air volume is a fraction of the
        value determined by the simulation.
        FlowPerHeatingCapacity is selected when the supply air volume is a fraction of the heating
        capacity as determined by the simulation.

        Args:
            value (str): value for IDD Field `supply_air_flow_rate_method_during_heating_operation`
                Accepted values are:
                      - None
                      - SupplyAirFlowRate
                      - FlowPerFloorArea
                      - FractionOfAutosizedHeatingValue
                      - FlowPerHeatingCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_flow_rate_method_during_heating_operation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_flow_rate_method_during_heating_operation`')
            vals = set()
            vals.add("None")
            vals.add("SupplyAirFlowRate")
            vals.add("FlowPerFloorArea")
            vals.add("FractionOfAutosizedHeatingValue")
            vals.add("FlowPerHeatingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_flow_rate_method_during_heating_operation`'.format(value))

        self._data["Supply air Flow Rate Method During Heating Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """Get supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_during_heating_operation`
        Enter the magnitude of the supply air volume flow rate during heating operation.
        Required field when Supply air Flow Rate Method During Heating Operation is SupplyAirFlowRate.
        This field may be blank if a heating coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_heating_operation`
                Unit: m3/s
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
                                 'for field `supply_air_flow_rate_during_heating_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_during_heating_operation`')

        self._data["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_per_floor_area_during_heating_operation(self):
        """Get supply_air_flow_rate_per_floor_area_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate Per Floor Area during Heating Operation"]

    @supply_air_flow_rate_per_floor_area_during_heating_operation.setter
    def supply_air_flow_rate_per_floor_area_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_per_floor_area_during_heating_operation`
        Enter the supply air volume flow rate per total floor area fraction.
        Required field when Supply air Flow Rate Method During Heating Operation is FlowPerFloorArea.
        This field may be blank if a heating coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_per_floor_area_during_heating_operation`
                Unit: m3/s-m2
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
                                 'for field `supply_air_flow_rate_per_floor_area_during_heating_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_per_floor_area_during_heating_operation`')

        self._data["Supply Air Flow Rate Per Floor Area during Heating Operation"] = value

    @property
    def fraction_of_autosized_design_heating_supply_air_flow_rate(self):
        """Get fraction_of_autosized_design_heating_supply_air_flow_rate

        Returns:
            float: the value of `fraction_of_autosized_design_heating_supply_air_flow_rate` or None if not set
        """
        return self._data["Fraction of Autosized Design Heating Supply Air Flow Rate"]

    @fraction_of_autosized_design_heating_supply_air_flow_rate.setter
    def fraction_of_autosized_design_heating_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_design_heating_supply_air_flow_rate`
        Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        Required field when Supply air Flow Rate Method During Heating Operation is FractionOfAutosizedHeatingValue.
        This field may be blank if a heating coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_design_heating_supply_air_flow_rate`
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
                                 'for field `fraction_of_autosized_design_heating_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_design_heating_supply_air_flow_rate`')

        self._data["Fraction of Autosized Design Heating Supply Air Flow Rate"] = value

    @property
    def design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation(self):
        """Get design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation` or None if not set
        """
        return self._data["Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation"]

    @design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation.setter
    def design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation`
        Enter the supply air volume flow rate as a fraction of the heating capacity.
        Required field when Supply air Flow Rate Method During Heating Operation is FlowPerHeatingCapacity.
        This field may be blank if a heating coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation`
                Unit: m3/s-W
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
                                 'for field `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation`')

        self._data["Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation"] = value

    @property
    def supply_air_flow_rate_method_when_no_cooling_or_heating_is_required(self):
        """Get supply_air_flow_rate_method_when_no_cooling_or_heating_is_required

        Returns:
            str: the value of `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required` or None if not set
        """
        return self._data["Supply Air Flow Rate Method When No Cooling or Heating is Required"]

    @supply_air_flow_rate_method_when_no_cooling_or_heating_is_required.setter
    def supply_air_flow_rate_method_when_no_cooling_or_heating_is_required(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`
        Enter the method used to determine the supply air volume flow rate when no cooling or heating is required.
        None is used when a heating coil is not included in the unitary system or this field may be blank.
        SupplyAirFlowRate is selected when the magnitude of the supply air volume is used.
        FlowPerFloorArea is selected when the supply air volume flow rate is based on total floor area
        served by the unitary system.
        FractionOfAutosizedCoolingValue is selected when the supply air volume is a fraction of the
        cooling value determined by the simulation.
        FractionOfAutosizedHeatingValue is selected when the supply air volume is a fraction of the
        heating value determined by the simulation.
        FlowPerCoolingCapacity is selected when the supply air volume is a fraction of the cooling
        capacity as determined by the simulation.
        FlowPerHeatingCapacity is selected when the supply air volume is a fraction of the heating
        capacity as determined by the simulation.

        Args:
            value (str): value for IDD Field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`
                Accepted values are:
                      - None
                      - SupplyAirFlowRate
                      - FlowPerFloorArea
                      - FractionOfAutosizedCoolingValue
                      - FractionOfAutosizedHeatingValue
                      - FlowPerCoolingCapacity
                      - FlowPerHeatingCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`')
            vals = set()
            vals.add("None")
            vals.add("SupplyAirFlowRate")
            vals.add("FlowPerFloorArea")
            vals.add("FractionOfAutosizedCoolingValue")
            vals.add("FractionOfAutosizedHeatingValue")
            vals.add("FlowPerCoolingCapacity")
            vals.add("FlowPerHeatingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`'.format(value))

        self._data["Supply Air Flow Rate Method When No Cooling or Heating is Required"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_required(self):
        """Get supply_air_flow_rate_when_no_cooling_or_heating_is_required

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_required` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Cooling or Heating is Required"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_required.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_required(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_required`
        Enter the magnitude of the supply air volume flow rate during when no cooling or heating is required.
        Required field when Supply air Flow Rate Method When No Cooling or Heating is Required is SupplyAirFlowRate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_required`
                Unit: m3/s
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
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_required`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_required`')

        self._data["Supply Air Flow Rate When No Cooling or Heating is Required"] = value

    @property
    def supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required(self):
        """Get supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required` or None if not set
        """
        return self._data["Supply Air Flow Rate Per Floor Area When No Cooling or Heating is Required"]

    @supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required.setter
    def supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required`
        Enter the supply air volume flow rate per total floor area fraction.
        Required field when Supply air Flow Rate Method When No Cooling or Heating is Required is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required`
                Unit: m3/s-m2
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
                                 'for field `supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required`')

        self._data["Supply Air Flow Rate Per Floor Area When No Cooling or Heating is Required"] = value

    @property
    def fraction_of_autosized_design_cooling_supply_air_flow_rate_v2(self):
        """Get fraction_of_autosized_design_cooling_supply_air_flow_rate_v2

        Returns:
            float: the value of `fraction_of_autosized_design_cooling_supply_air_flow_rate_v2` or None if not set
        """
        return self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate v2"]

    @fraction_of_autosized_design_cooling_supply_air_flow_rate_v2.setter
    def fraction_of_autosized_design_cooling_supply_air_flow_rate_v2(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate_v2`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method When No Cooling or Heating is Required is FractionOfAutosizedCoolingValue.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate_v2`
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
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate_v2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate_v2`')

        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate v2"] = value

    @property
    def fraction_of_autosized_design_heating_supply_air_flow_rate_v2(self):
        """Get fraction_of_autosized_design_heating_supply_air_flow_rate_v2

        Returns:
            float: the value of `fraction_of_autosized_design_heating_supply_air_flow_rate_v2` or None if not set
        """
        return self._data["Fraction of Autosized Design Heating Supply Air Flow Rate v2"]

    @fraction_of_autosized_design_heating_supply_air_flow_rate_v2.setter
    def fraction_of_autosized_design_heating_supply_air_flow_rate_v2(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_design_heating_supply_air_flow_rate_v2`
        Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        Required field when Supply air Flow Rate Method When No Cooling or Heating is Required is FractionOfAutosizedHeatingValue.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_design_heating_supply_air_flow_rate_v2`
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
                                 'for field `fraction_of_autosized_design_heating_supply_air_flow_rate_v2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_design_heating_supply_air_flow_rate_v2`')

        self._data["Fraction of Autosized Design Heating Supply Air Flow Rate v2"] = value

    @property
    def design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2(self):
        """Get design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2` or None if not set
        """
        return self._data["Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation v2"]

    @design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2.setter
    def design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2(self, value=None):
        """  Corresponds to IDD Field `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2`
        Enter the supply air volume flow rate as a fraction of the cooling capacity.
        Required field when Supply air Flow Rate Method During Heating Operation is FlowPerCoolingCapacity.

        Args:
            value (float): value for IDD Field `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2`
                Unit: m3/s-W
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
                                 'for field `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2`')

        self._data["Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation v2"] = value

    @property
    def design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2(self):
        """Get design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2` or None if not set
        """
        return self._data["Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation v2"]

    @design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2.setter
    def design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2(self, value=None):
        """  Corresponds to IDD Field `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2`
        Enter the supply air volume flow rate as a fraction of the heating capacity.
        Required field when Supply air Flow Rate Method During Heating Operation is FlowPerHeatingCapacity.

        Args:
            value (float): value for IDD Field `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2`
                Unit: m3/s-W
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
                                 'for field `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2`')

        self._data["Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation v2"] = value

    @property
    def maximum_supply_air_temperature(self):
        """Get maximum_supply_air_temperature

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set
        """
        return self._data["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=80.0 ):
        """  Corresponds to IDD Field `maximum_supply_air_temperature`
        Enter the maximum supply air temperature leaving the heating coil.

        Args:
            value (float): value for IDD Field `maximum_supply_air_temperature`
                Unit: C
                Default value: 80.0
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
                                 'for field `maximum_supply_air_temperature`'.format(value))

        self._data["Maximum Supply Air Temperature"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self):
        """Get maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation` or None if not set
        """
        return self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"]

    @maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation.setter
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self, value=21.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`
        Enter the maximum outdoor dry-bulb temperature for supplemental heater operation.

        Args:
            value (float): value for IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`
                Unit: C
                Default value: 21.0
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
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`'.format(value))

        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = value

    @property
    def outdoor_drybulb_temperature_sensor_node_name(self):
        """Get outdoor_drybulb_temperature_sensor_node_name

        Returns:
            str: the value of `outdoor_drybulb_temperature_sensor_node_name` or None if not set
        """
        return self._data["Outdoor Dry-Bulb Temperature Sensor Node Name"]

    @outdoor_drybulb_temperature_sensor_node_name.setter
    def outdoor_drybulb_temperature_sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_drybulb_temperature_sensor_node_name`
        If this field is blank, outdoor temperature from the weather file is used.
        If this field is not blank, the node name specified determines the outdoor temperature used
        for controlling supplemental heater operation.

        Args:
            value (str): value for IDD Field `outdoor_drybulb_temperature_sensor_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_drybulb_temperature_sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_drybulb_temperature_sensor_node_name`')

        self._data["Outdoor Dry-Bulb Temperature Sensor Node Name"] = value

    @property
    def maximum_cycling_rate(self):
        """Get maximum_cycling_rate

        Returns:
            float: the value of `maximum_cycling_rate` or None if not set
        """
        return self._data["Maximum Cycling Rate"]

    @maximum_cycling_rate.setter
    def maximum_cycling_rate(self, value=2.5 ):
        """  Corresponds to IDD Field `maximum_cycling_rate`
        Used only for water source heat pump.
        The maximum on-off cycling rate for the compressor.
        Suggested value is 2.5 for a typical heat pump.

        Args:
            value (float): value for IDD Field `maximum_cycling_rate`
                Unit: cycles/hr
                Default value: 2.5
                value >= 0.0
                value <= 5.0
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
                                 'for field `maximum_cycling_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_cycling_rate`')
            if value > 5.0:
                raise ValueError('value need to be smaller 5.0 '
                                 'for field `maximum_cycling_rate`')

        self._data["Maximum Cycling Rate"] = value

    @property
    def heat_pump_time_constant(self):
        """Get heat_pump_time_constant

        Returns:
            float: the value of `heat_pump_time_constant` or None if not set
        """
        return self._data["Heat Pump Time Constant"]

    @heat_pump_time_constant.setter
    def heat_pump_time_constant(self, value=60.0 ):
        """  Corresponds to IDD Field `heat_pump_time_constant`
        Used only for water source heat pump.
        Time constant for the cooling coil's capacity to reach steady state after startup.
        Suggested value is 60 for a typical heat pump.

        Args:
            value (float): value for IDD Field `heat_pump_time_constant`
                Unit: s
                Default value: 60.0
                value >= 0.0
                value <= 500.0
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
                                 'for field `heat_pump_time_constant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heat_pump_time_constant`')
            if value > 500.0:
                raise ValueError('value need to be smaller 500.0 '
                                 'for field `heat_pump_time_constant`')

        self._data["Heat Pump Time Constant"] = value

    @property
    def fraction_of_oncycle_power_use(self):
        """Get fraction_of_oncycle_power_use

        Returns:
            float: the value of `fraction_of_oncycle_power_use` or None if not set
        """
        return self._data["Fraction of On-Cycle Power Use"]

    @fraction_of_oncycle_power_use.setter
    def fraction_of_oncycle_power_use(self, value=0.01 ):
        """  Corresponds to IDD Field `fraction_of_oncycle_power_use`
        Used only for water source heat pump.
        The fraction of on-cycle power use to adjust the part load fraction based on
        the off-cycle power consumption due to crankcase heaters, controls, fans, and etc.
        Suggested value is 0.01 for a typical heat pump.

        Args:
            value (float): value for IDD Field `fraction_of_oncycle_power_use`
                Default value: 0.01
                value >= 0.0
                value <= 0.05
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
                                 'for field `fraction_of_oncycle_power_use`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_oncycle_power_use`')
            if value > 0.05:
                raise ValueError('value need to be smaller 0.05 '
                                 'for field `fraction_of_oncycle_power_use`')

        self._data["Fraction of On-Cycle Power Use"] = value

    @property
    def heat_pump_fan_delay_time(self):
        """Get heat_pump_fan_delay_time

        Returns:
            float: the value of `heat_pump_fan_delay_time` or None if not set
        """
        return self._data["Heat Pump Fan Delay Time"]

    @heat_pump_fan_delay_time.setter
    def heat_pump_fan_delay_time(self, value=60.0 ):
        """  Corresponds to IDD Field `heat_pump_fan_delay_time`
        Used only for water source heat pump.
        Programmed time delay for heat pump fan to shut off after compressor cycle off.
        Only required when fan operating mode is cycling.
        Enter 0 when fan operating mode is continuous.

        Args:
            value (float): value for IDD Field `heat_pump_fan_delay_time`
                Unit: s
                Default value: 60.0
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
                                 'for field `heat_pump_fan_delay_time`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heat_pump_fan_delay_time`')

        self._data["Heat Pump Fan Delay Time"] = value

    @property
    def ancilliary_oncycle_electric_power(self):
        """Get ancilliary_oncycle_electric_power

        Returns:
            float: the value of `ancilliary_oncycle_electric_power` or None if not set
        """
        return self._data["Ancilliary On-Cycle Electric Power"]

    @ancilliary_oncycle_electric_power.setter
    def ancilliary_oncycle_electric_power(self, value=0.0 ):
        """  Corresponds to IDD Field `ancilliary_oncycle_electric_power`
        Enter the value of ancilliary electric power for controls or other devices consumed during the on cycle.

        Args:
            value (float): value for IDD Field `ancilliary_oncycle_electric_power`
                Unit: W
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ancilliary_oncycle_electric_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ancilliary_oncycle_electric_power`')

        self._data["Ancilliary On-Cycle Electric Power"] = value

    @property
    def ancilliary_offcycle_electric_power(self):
        """Get ancilliary_offcycle_electric_power

        Returns:
            float: the value of `ancilliary_offcycle_electric_power` or None if not set
        """
        return self._data["Ancilliary Off-Cycle Electric Power"]

    @ancilliary_offcycle_electric_power.setter
    def ancilliary_offcycle_electric_power(self, value=0.0 ):
        """  Corresponds to IDD Field `ancilliary_offcycle_electric_power`
        Enter the value of ancilliary electric power for controls or other devices consumed during the off cycle.

        Args:
            value (float): value for IDD Field `ancilliary_offcycle_electric_power`
                Unit: W
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ancilliary_offcycle_electric_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ancilliary_offcycle_electric_power`')

        self._data["Ancilliary Off-Cycle Electric Power"] = value

    @property
    def design_heat_recovery_water_flow_rate(self):
        """Get design_heat_recovery_water_flow_rate

        Returns:
            float: the value of `design_heat_recovery_water_flow_rate` or None if not set
        """
        return self._data["Design Heat Recovery Water Flow Rate"]

    @design_heat_recovery_water_flow_rate.setter
    def design_heat_recovery_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `design_heat_recovery_water_flow_rate`
        If non-zero, then the heat recovery inlet and outlet node names must be entered.
        Used for heat recovery to an EnergyPlus plant loop.

        Args:
            value (float): value for IDD Field `design_heat_recovery_water_flow_rate`
                Unit: m3/s
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_heat_recovery_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_heat_recovery_water_flow_rate`')

        self._data["Design Heat Recovery Water Flow Rate"] = value

    @property
    def maximum_temperature_for_heat_recovery(self):
        """Get maximum_temperature_for_heat_recovery

        Returns:
            float: the value of `maximum_temperature_for_heat_recovery` or None if not set
        """
        return self._data["Maximum Temperature for Heat Recovery"]

    @maximum_temperature_for_heat_recovery.setter
    def maximum_temperature_for_heat_recovery(self, value=80.0 ):
        """  Corresponds to IDD Field `maximum_temperature_for_heat_recovery`
        Enter the maximum heat recovery inlet temperature allowed for heat recovery.

        Args:
            value (float): value for IDD Field `maximum_temperature_for_heat_recovery`
                Unit: C
                Default value: 80.0
                value >= 0.0
                value <= 100.0
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
                                 'for field `maximum_temperature_for_heat_recovery`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_temperature_for_heat_recovery`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_temperature_for_heat_recovery`')

        self._data["Maximum Temperature for Heat Recovery"] = value

    @property
    def heat_recovery_water_inlet_node_name(self):
        """Get heat_recovery_water_inlet_node_name

        Returns:
            str: the value of `heat_recovery_water_inlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Water Inlet Node Name"]

    @heat_recovery_water_inlet_node_name.setter
    def heat_recovery_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_water_inlet_node_name`
        Enter the name of the heat recovery water inlet node if plant water loop connections are present.

        Args:
            value (str): value for IDD Field `heat_recovery_water_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_recovery_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_water_inlet_node_name`')

        self._data["Heat Recovery Water Inlet Node Name"] = value

    @property
    def heat_recovery_water_outlet_node_name(self):
        """Get heat_recovery_water_outlet_node_name

        Returns:
            str: the value of `heat_recovery_water_outlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Water Outlet Node Name"]

    @heat_recovery_water_outlet_node_name.setter
    def heat_recovery_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_water_outlet_node_name`
        Enter the name of the heat recovery water outlet node if plant water loop connections are present.

        Args:
            value (str): value for IDD Field `heat_recovery_water_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_recovery_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_water_outlet_node_name`')

        self._data["Heat Recovery Water Outlet Node Name"] = value

    @property
    def design_specification_multispeed_heat_pump_object_type(self):
        """Get design_specification_multispeed_heat_pump_object_type

        Returns:
            str: the value of `design_specification_multispeed_heat_pump_object_type` or None if not set
        """
        return self._data["Design Specification Multispeed Heat Pump Object Type"]

    @design_specification_multispeed_heat_pump_object_type.setter
    def design_specification_multispeed_heat_pump_object_type(self, value=None):
        """  Corresponds to IDD Field `design_specification_multispeed_heat_pump_object_type`
        Enter the type of performance specification object used to describe the multispeed coil.

        Args:
            value (str): value for IDD Field `design_specification_multispeed_heat_pump_object_type`
                Accepted values are:
                      - UnitarySystemPerformance:HeatPump:Multispeed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_multispeed_heat_pump_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_multispeed_heat_pump_object_type`')
            vals = set()
            vals.add("UnitarySystemPerformance:HeatPump:Multispeed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_specification_multispeed_heat_pump_object_type`'.format(value))

        self._data["Design Specification Multispeed Heat Pump Object Type"] = value

    @property
    def design_specification_multispeed_heat_pump_object_name(self):
        """Get design_specification_multispeed_heat_pump_object_name

        Returns:
            str: the value of `design_specification_multispeed_heat_pump_object_name` or None if not set
        """
        return self._data["Design Specification Multispeed Heat Pump Object Name"]

    @design_specification_multispeed_heat_pump_object_name.setter
    def design_specification_multispeed_heat_pump_object_name(self, value=None):
        """  Corresponds to IDD Field `design_specification_multispeed_heat_pump_object_name`
        Enter the name of the performance specification object used to describe the multispeed coil.

        Args:
            value (str): value for IDD Field `design_specification_multispeed_heat_pump_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_multispeed_heat_pump_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_multispeed_heat_pump_object_name`')

        self._data["Design Specification Multispeed Heat Pump Object Name"] = value

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
        out.append(self._to_str(self.control_type))
        out.append(self._to_str(self.controlling_zone_or_thermostat_location))
        out.append(self._to_str(self.dehumidification_control_type))
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.supply_fan_object_type))
        out.append(self._to_str(self.supply_fan_name))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.dx_heating_coil_sizing_ratio))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.use_doas_dx_cooling_coil))
        out.append(self._to_str(self.doas_dx_cooling_coil_leaving_minimum_air_temperature))
        out.append(self._to_str(self.latent_load_control))
        out.append(self._to_str(self.supplemental_heating_coil_object_type))
        out.append(self._to_str(self.supplemental_heating_coil_name))
        out.append(self._to_str(self.supply_air_flow_rate_method_during_cooling_operation))
        out.append(self._to_str(self.supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.supply_air_flow_rate_per_floor_area_during_cooling_operation))
        out.append(self._to_str(self.fraction_of_autosized_design_cooling_supply_air_flow_rate))
        out.append(self._to_str(self.design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation))
        out.append(self._to_str(self.supply_air_flow_rate_method_during_heating_operation))
        out.append(self._to_str(self.supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.supply_air_flow_rate_per_floor_area_during_heating_operation))
        out.append(self._to_str(self.fraction_of_autosized_design_heating_supply_air_flow_rate))
        out.append(self._to_str(self.design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation))
        out.append(self._to_str(self.supply_air_flow_rate_method_when_no_cooling_or_heating_is_required))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_cooling_or_heating_is_required))
        out.append(self._to_str(self.supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required))
        out.append(self._to_str(self.fraction_of_autosized_design_cooling_supply_air_flow_rate_v2))
        out.append(self._to_str(self.fraction_of_autosized_design_heating_supply_air_flow_rate_v2))
        out.append(self._to_str(self.design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v2))
        out.append(self._to_str(self.design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v2))
        out.append(self._to_str(self.maximum_supply_air_temperature))
        out.append(self._to_str(self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation))
        out.append(self._to_str(self.outdoor_drybulb_temperature_sensor_node_name))
        out.append(self._to_str(self.maximum_cycling_rate))
        out.append(self._to_str(self.heat_pump_time_constant))
        out.append(self._to_str(self.fraction_of_oncycle_power_use))
        out.append(self._to_str(self.heat_pump_fan_delay_time))
        out.append(self._to_str(self.ancilliary_oncycle_electric_power))
        out.append(self._to_str(self.ancilliary_offcycle_electric_power))
        out.append(self._to_str(self.design_heat_recovery_water_flow_rate))
        out.append(self._to_str(self.maximum_temperature_for_heat_recovery))
        out.append(self._to_str(self.heat_recovery_water_inlet_node_name))
        out.append(self._to_str(self.heat_recovery_water_outlet_node_name))
        out.append(self._to_str(self.design_specification_multispeed_heat_pump_object_type))
        out.append(self._to_str(self.design_specification_multispeed_heat_pump_object_name))
        return ",".join(out)

class UnitarySystemPerformanceHeatPumpMultispeed(object):
    """ Corresponds to IDD object `UnitarySystemPerformance:HeatPump:Multispeed`
        The UnitarySystemPerformance object is used to specify the air flow ratio at each
        operating speed. This object is primarily used for multispeed coils to allow operation
        at alternate flow rates different from those specified in the coil object.
    """
    internal_name = "UnitarySystemPerformance:HeatPump:Multispeed"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for IDD  `UnitarySystemPerformance:HeatPump:Multispeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Number of Speeds for Heating"] = None
        self._data["Number of Speeds for Cooling"] = None
        self._data["Speed 1 Supply Air Flow Ratio During Heating Operation"] = None
        self._data["Speed 1 Supply Air Flow Ratio During Cooling Operation"] = None
        self._data["Speed 2 Supply Air Flow Ratio During Heating Operation"] = None
        self._data["Speed 2 Supply Air Flow Ratio During Cooling Operation"] = None
        self._data["Speed 3 Supply Air Flow Ratio During Heating Operation"] = None
        self._data["Speed 3 Supply Air Flow Ratio During Cooling Operation"] = None
        self._data["Speed 4 Supply Air Flow Ratio During Heating Operation"] = None
        self._data["Speed 4 Supply Air Flow Ratio During Cooling Operation"] = None

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
            self.number_of_speeds_for_heating = None
        else:
            self.number_of_speeds_for_heating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_speeds_for_cooling = None
        else:
            self.number_of_speeds_for_cooling = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_1_supply_air_flow_ratio_during_heating_operation = None
        else:
            self.speed_1_supply_air_flow_ratio_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_1_supply_air_flow_ratio_during_cooling_operation = None
        else:
            self.speed_1_supply_air_flow_ratio_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_2_supply_air_flow_ratio_during_heating_operation = None
        else:
            self.speed_2_supply_air_flow_ratio_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_2_supply_air_flow_ratio_during_cooling_operation = None
        else:
            self.speed_2_supply_air_flow_ratio_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_3_supply_air_flow_ratio_during_heating_operation = None
        else:
            self.speed_3_supply_air_flow_ratio_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_3_supply_air_flow_ratio_during_cooling_operation = None
        else:
            self.speed_3_supply_air_flow_ratio_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_4_supply_air_flow_ratio_during_heating_operation = None
        else:
            self.speed_4_supply_air_flow_ratio_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_4_supply_air_flow_ratio_during_cooling_operation = None
        else:
            self.speed_4_supply_air_flow_ratio_during_cooling_operation = vals[i]
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
    def number_of_speeds_for_heating(self):
        """Get number_of_speeds_for_heating

        Returns:
            int: the value of `number_of_speeds_for_heating` or None if not set
        """
        return self._data["Number of Speeds for Heating"]

    @number_of_speeds_for_heating.setter
    def number_of_speeds_for_heating(self, value=None):
        """  Corresponds to IDD Field `number_of_speeds_for_heating`
        Used only for Multi speed coils
        Enter the number of the following sets of data for air flow rates.

        Args:
            value (int): value for IDD Field `number_of_speeds_for_heating`
                value >= 0
                value <= 10
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_speeds_for_heating`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `number_of_speeds_for_heating`')
            if value > 10:
                raise ValueError('value need to be smaller 10 '
                                 'for field `number_of_speeds_for_heating`')

        self._data["Number of Speeds for Heating"] = value

    @property
    def number_of_speeds_for_cooling(self):
        """Get number_of_speeds_for_cooling

        Returns:
            int: the value of `number_of_speeds_for_cooling` or None if not set
        """
        return self._data["Number of Speeds for Cooling"]

    @number_of_speeds_for_cooling.setter
    def number_of_speeds_for_cooling(self, value=None):
        """  Corresponds to IDD Field `number_of_speeds_for_cooling`
        Used only for Multi speed coils
        Enter the number of the following sets of data for air flow rates.

        Args:
            value (int): value for IDD Field `number_of_speeds_for_cooling`
                value >= 0
                value <= 10
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_speeds_for_cooling`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `number_of_speeds_for_cooling`')
            if value > 10:
                raise ValueError('value need to be smaller 10 '
                                 'for field `number_of_speeds_for_cooling`')

        self._data["Number of Speeds for Cooling"] = value

    @property
    def speed_1_supply_air_flow_ratio_during_heating_operation(self):
        """Get speed_1_supply_air_flow_ratio_during_heating_operation

        Returns:
            float: the value of `speed_1_supply_air_flow_ratio_during_heating_operation` or None if not set
        """
        return self._data["Speed 1 Supply Air Flow Ratio During Heating Operation"]

    @speed_1_supply_air_flow_ratio_during_heating_operation.setter
    def speed_1_supply_air_flow_ratio_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_1_supply_air_flow_ratio_during_heating_operation`
        Used only for Multi speed coils
        Enter the lowest operating supply air flow ratio during heating
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_1_supply_air_flow_ratio_during_heating_operation`
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
                                 'for field `speed_1_supply_air_flow_ratio_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_1_supply_air_flow_ratio_during_heating_operation`')

        self._data["Speed 1 Supply Air Flow Ratio During Heating Operation"] = value

    @property
    def speed_1_supply_air_flow_ratio_during_cooling_operation(self):
        """Get speed_1_supply_air_flow_ratio_during_cooling_operation

        Returns:
            float: the value of `speed_1_supply_air_flow_ratio_during_cooling_operation` or None if not set
        """
        return self._data["Speed 1 Supply Air Flow Ratio During Cooling Operation"]

    @speed_1_supply_air_flow_ratio_during_cooling_operation.setter
    def speed_1_supply_air_flow_ratio_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_1_supply_air_flow_ratio_during_cooling_operation`
        Used only for Multi speed coils
        Enter the lowest operating supply air flow ratio during cooling
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_1_supply_air_flow_ratio_during_cooling_operation`
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
                                 'for field `speed_1_supply_air_flow_ratio_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_1_supply_air_flow_ratio_during_cooling_operation`')

        self._data["Speed 1 Supply Air Flow Ratio During Cooling Operation"] = value

    @property
    def speed_2_supply_air_flow_ratio_during_heating_operation(self):
        """Get speed_2_supply_air_flow_ratio_during_heating_operation

        Returns:
            float: the value of `speed_2_supply_air_flow_ratio_during_heating_operation` or None if not set
        """
        return self._data["Speed 2 Supply Air Flow Ratio During Heating Operation"]

    @speed_2_supply_air_flow_ratio_during_heating_operation.setter
    def speed_2_supply_air_flow_ratio_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_2_supply_air_flow_ratio_during_heating_operation`
        Used only for Multi speed coils
        Enter the next highest operating supply air flow ratio during heating
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_2_supply_air_flow_ratio_during_heating_operation`
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
                                 'for field `speed_2_supply_air_flow_ratio_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_2_supply_air_flow_ratio_during_heating_operation`')

        self._data["Speed 2 Supply Air Flow Ratio During Heating Operation"] = value

    @property
    def speed_2_supply_air_flow_ratio_during_cooling_operation(self):
        """Get speed_2_supply_air_flow_ratio_during_cooling_operation

        Returns:
            float: the value of `speed_2_supply_air_flow_ratio_during_cooling_operation` or None if not set
        """
        return self._data["Speed 2 Supply Air Flow Ratio During Cooling Operation"]

    @speed_2_supply_air_flow_ratio_during_cooling_operation.setter
    def speed_2_supply_air_flow_ratio_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_2_supply_air_flow_ratio_during_cooling_operation`
        Used only for Multi speed coils
        Enter the lowest operating supply air flow ratio during cooling
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_2_supply_air_flow_ratio_during_cooling_operation`
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
                                 'for field `speed_2_supply_air_flow_ratio_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_2_supply_air_flow_ratio_during_cooling_operation`')

        self._data["Speed 2 Supply Air Flow Ratio During Cooling Operation"] = value

    @property
    def speed_3_supply_air_flow_ratio_during_heating_operation(self):
        """Get speed_3_supply_air_flow_ratio_during_heating_operation

        Returns:
            float: the value of `speed_3_supply_air_flow_ratio_during_heating_operation` or None if not set
        """
        return self._data["Speed 3 Supply Air Flow Ratio During Heating Operation"]

    @speed_3_supply_air_flow_ratio_during_heating_operation.setter
    def speed_3_supply_air_flow_ratio_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_3_supply_air_flow_ratio_during_heating_operation`
        Used only for Multi speed coils
        Enter the next highest operating supply air flow ratio during heating
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_3_supply_air_flow_ratio_during_heating_operation`
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
                                 'for field `speed_3_supply_air_flow_ratio_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_3_supply_air_flow_ratio_during_heating_operation`')

        self._data["Speed 3 Supply Air Flow Ratio During Heating Operation"] = value

    @property
    def speed_3_supply_air_flow_ratio_during_cooling_operation(self):
        """Get speed_3_supply_air_flow_ratio_during_cooling_operation

        Returns:
            float: the value of `speed_3_supply_air_flow_ratio_during_cooling_operation` or None if not set
        """
        return self._data["Speed 3 Supply Air Flow Ratio During Cooling Operation"]

    @speed_3_supply_air_flow_ratio_during_cooling_operation.setter
    def speed_3_supply_air_flow_ratio_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_3_supply_air_flow_ratio_during_cooling_operation`
        Used only for Multi speed coils
        Enter the lowest operating supply air flow ratio during cooling
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_3_supply_air_flow_ratio_during_cooling_operation`
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
                                 'for field `speed_3_supply_air_flow_ratio_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_3_supply_air_flow_ratio_during_cooling_operation`')

        self._data["Speed 3 Supply Air Flow Ratio During Cooling Operation"] = value

    @property
    def speed_4_supply_air_flow_ratio_during_heating_operation(self):
        """Get speed_4_supply_air_flow_ratio_during_heating_operation

        Returns:
            float: the value of `speed_4_supply_air_flow_ratio_during_heating_operation` or None if not set
        """
        return self._data["Speed 4 Supply Air Flow Ratio During Heating Operation"]

    @speed_4_supply_air_flow_ratio_during_heating_operation.setter
    def speed_4_supply_air_flow_ratio_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_4_supply_air_flow_ratio_during_heating_operation`
        Used only for Multi speed coils
        Enter the next highest operating supply air flow ratio during heating
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_4_supply_air_flow_ratio_during_heating_operation`
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
                                 'for field `speed_4_supply_air_flow_ratio_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_4_supply_air_flow_ratio_during_heating_operation`')

        self._data["Speed 4 Supply Air Flow Ratio During Heating Operation"] = value

    @property
    def speed_4_supply_air_flow_ratio_during_cooling_operation(self):
        """Get speed_4_supply_air_flow_ratio_during_cooling_operation

        Returns:
            float: the value of `speed_4_supply_air_flow_ratio_during_cooling_operation` or None if not set
        """
        return self._data["Speed 4 Supply Air Flow Ratio During Cooling Operation"]

    @speed_4_supply_air_flow_ratio_during_cooling_operation.setter
    def speed_4_supply_air_flow_ratio_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_4_supply_air_flow_ratio_during_cooling_operation`
        Used only for Multi speed coils
        Enter the lowest operating supply air flow ratio during cooling
        operation or specify autosize. This value is the ratio of air flow
        at this speed to the maximum air flow rate.

        Args:
            value (float): value for IDD Field `speed_4_supply_air_flow_ratio_during_cooling_operation`
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
                                 'for field `speed_4_supply_air_flow_ratio_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_4_supply_air_flow_ratio_during_cooling_operation`')

        self._data["Speed 4 Supply Air Flow Ratio During Cooling Operation"] = value

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
        out.append(self._to_str(self.number_of_speeds_for_heating))
        out.append(self._to_str(self.number_of_speeds_for_cooling))
        out.append(self._to_str(self.speed_1_supply_air_flow_ratio_during_heating_operation))
        out.append(self._to_str(self.speed_1_supply_air_flow_ratio_during_cooling_operation))
        out.append(self._to_str(self.speed_2_supply_air_flow_ratio_during_heating_operation))
        out.append(self._to_str(self.speed_2_supply_air_flow_ratio_during_cooling_operation))
        out.append(self._to_str(self.speed_3_supply_air_flow_ratio_during_heating_operation))
        out.append(self._to_str(self.speed_3_supply_air_flow_ratio_during_cooling_operation))
        out.append(self._to_str(self.speed_4_supply_air_flow_ratio_during_heating_operation))
        out.append(self._to_str(self.speed_4_supply_air_flow_ratio_during_cooling_operation))
        return ",".join(out)

class AirLoopHvacUnitaryFurnaceHeatOnly(object):
    """ Corresponds to IDD object `AirLoopHVAC:Unitary:Furnace:HeatOnly`
        Unitary system, heating-only with constant volume supply fan (continuous or cycling)
        and heating coil (gas, electric, hot water, or steam). Identical to
        AirLoopHVAC:UnitaryHeatOnly.
    """
    internal_name = "AirLoopHVAC:Unitary:Furnace:HeatOnly"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:Unitary:Furnace:HeatOnly`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Furnace Air Inlet Node Name"] = None
        self._data["Furnace Air Outlet Node Name"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Maximum Supply Air Temperature"] = None
        self._data["Supply Air Flow Rate"] = None
        self._data["Controlling Zone or Thermostat Location"] = None
        self._data["Supply Fan Object Type"] = None
        self._data["Supply Fan Name"] = None
        self._data["Fan Placement"] = None
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
            self.furnace_air_inlet_node_name = None
        else:
            self.furnace_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.furnace_air_outlet_node_name = None
        else:
            self.furnace_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature = None
        else:
            self.maximum_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate = None
        else:
            self.supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.controlling_zone_or_thermostat_location = None
        else:
            self.controlling_zone_or_thermostat_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_object_type = None
        else:
            self.supply_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_name = None
        else:
            self.supply_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
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
    def furnace_air_inlet_node_name(self):
        """Get furnace_air_inlet_node_name

        Returns:
            str: the value of `furnace_air_inlet_node_name` or None if not set
        """
        return self._data["Furnace Air Inlet Node Name"]

    @furnace_air_inlet_node_name.setter
    def furnace_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `furnace_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `furnace_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `furnace_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `furnace_air_inlet_node_name`')

        self._data["Furnace Air Inlet Node Name"] = value

    @property
    def furnace_air_outlet_node_name(self):
        """Get furnace_air_outlet_node_name

        Returns:
            str: the value of `furnace_air_outlet_node_name` or None if not set
        """
        return self._data["Furnace Air Outlet Node Name"]

    @furnace_air_outlet_node_name.setter
    def furnace_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `furnace_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `furnace_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `furnace_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `furnace_air_outlet_node_name`')

        self._data["Furnace Air Outlet Node Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        A fan operating mode schedule value of 0 indicates cycling fan mode (supply air
        fan cycles on and off in tandem with the heating coil).
        Any other schedule value indicates continuous fan mode (supply air fan operates
        continuously regardless of heating coil operation).
        Leaving this schedule name blank will default to cycling fan mode for the
        entire simulation period.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')

        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def maximum_supply_air_temperature(self):
        """Get maximum_supply_air_temperature

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set
        """
        return self._data["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=80.0 ):
        """  Corresponds to IDD Field `maximum_supply_air_temperature`

        Args:
            value (float): value for IDD Field `maximum_supply_air_temperature`
                Unit: C
                Default value: 80.0
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
                                 'for field `maximum_supply_air_temperature`'.format(value))

        self._data["Maximum Supply Air Temperature"] = value

    @property
    def supply_air_flow_rate(self):
        """Get supply_air_flow_rate

        Returns:
            float: the value of `supply_air_flow_rate` or None if not set
        """
        return self._data["Supply Air Flow Rate"]

    @supply_air_flow_rate.setter
    def supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate`
        This value should be > 0 and <= than the fan air flow rate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate`
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
                                 'for field `supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate`')

        self._data["Supply Air Flow Rate"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """Get controlling_zone_or_thermostat_location

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set
        """
        return self._data["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """  Corresponds to IDD Field `controlling_zone_or_thermostat_location`

        Args:
            value (str): value for IDD Field `controlling_zone_or_thermostat_location`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controlling_zone_or_thermostat_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controlling_zone_or_thermostat_location`')

        self._data["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_fan_object_type(self):
        """Get supply_fan_object_type

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self._data["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `supply_fan_object_type`
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. fan
        operating mode schedule values are greater than 0).

        Args:
            value (str): value for IDD Field `supply_fan_object_type`
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
                                 'for field `supply_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_fan_object_type`'.format(value))

        self._data["Supply Fan Object Type"] = value

    @property
    def supply_fan_name(self):
        """Get supply_fan_name

        Returns:
            str: the value of `supply_fan_name` or None if not set
        """
        return self._data["Supply Fan Name"]

    @supply_fan_name.setter
    def supply_fan_name(self, value=None):
        """  Corresponds to IDD Field `supply_fan_name`

        Args:
            value (str): value for IDD Field `supply_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_name`')

        self._data["Supply Fan Name"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="BlowThrough"):
        """  Corresponds to IDD Field `fan_placement`

        Args:
            value (str): value for IDD Field `fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: BlowThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

        self._data["Fan Placement"] = value

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
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
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
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
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
        out.append(self._to_str(self.furnace_air_inlet_node_name))
        out.append(self._to_str(self.furnace_air_outlet_node_name))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.maximum_supply_air_temperature))
        out.append(self._to_str(self.supply_air_flow_rate))
        out.append(self._to_str(self.controlling_zone_or_thermostat_location))
        out.append(self._to_str(self.supply_fan_object_type))
        out.append(self._to_str(self.supply_fan_name))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        return ",".join(out)

class AirLoopHvacUnitaryFurnaceHeatCool(object):
    """ Corresponds to IDD object `AirLoopHVAC:Unitary:Furnace:HeatCool`
        Unitary system, heating and cooling with constant volume supply fan (continuous or
        cycling), direct expansion (DX) cooling coil, heating coil (gas, electric,
        hot water, or steam), and optional reheat coil for dehumidification control.
        Identical to AirLoopHVAC:UnitaryHeatCool.
    """
    internal_name = "AirLoopHVAC:Unitary:Furnace:HeatCool"
    field_count = 20

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:Unitary:Furnace:HeatCool`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Furnace Air Inlet Node Name"] = None
        self._data["Furnace Air Outlet Node Name"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Maximum Supply Air Temperature"] = None
        self._data["Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Supply Air Flow Rate During Heating Operation"] = None
        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Controlling Zone or Thermostat Location"] = None
        self._data["Supply Fan Object Type"] = None
        self._data["Supply Fan Name"] = None
        self._data["Fan Placement"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Dehumidification Control Type"] = None
        self._data["Reheat Coil Object Type"] = None
        self._data["Reheat Coil Name"] = None

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
            self.furnace_air_inlet_node_name = None
        else:
            self.furnace_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.furnace_air_outlet_node_name = None
        else:
            self.furnace_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature = None
        else:
            self.maximum_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.controlling_zone_or_thermostat_location = None
        else:
            self.controlling_zone_or_thermostat_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_object_type = None
        else:
            self.supply_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_name = None
        else:
            self.supply_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
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
            self.reheat_coil_object_type = None
        else:
            self.reheat_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reheat_coil_name = None
        else:
            self.reheat_coil_name = vals[i]
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
        A schedule value greater than zero (usually 1 is used) indicates that the unit is
        available to operate as needed. A value less than or equal to zero (usually zero
        is used) denotes that the unit must be off.

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
    def furnace_air_inlet_node_name(self):
        """Get furnace_air_inlet_node_name

        Returns:
            str: the value of `furnace_air_inlet_node_name` or None if not set
        """
        return self._data["Furnace Air Inlet Node Name"]

    @furnace_air_inlet_node_name.setter
    def furnace_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `furnace_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `furnace_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `furnace_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `furnace_air_inlet_node_name`')

        self._data["Furnace Air Inlet Node Name"] = value

    @property
    def furnace_air_outlet_node_name(self):
        """Get furnace_air_outlet_node_name

        Returns:
            str: the value of `furnace_air_outlet_node_name` or None if not set
        """
        return self._data["Furnace Air Outlet Node Name"]

    @furnace_air_outlet_node_name.setter
    def furnace_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `furnace_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `furnace_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `furnace_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `furnace_air_outlet_node_name`')

        self._data["Furnace Air Outlet Node Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        A fan operating mode schedule value of 0 indicates cycling fan mode (supply air
        fan cycles on and off in tandem with the cooling or heating coil).
        Any other schedule value indicates continuous fan mode (supply air fan operates
        continuously regardless of cooling or heating coil operation). Provide a schedule
        with non-zero values when high humidity control is specified.
        Leaving this schedule name blank will default to cycling fan mode for the
        entire simulation period.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')

        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def maximum_supply_air_temperature(self):
        """Get maximum_supply_air_temperature

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set
        """
        return self._data["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=80.0 ):
        """  Corresponds to IDD Field `maximum_supply_air_temperature`

        Args:
            value (float): value for IDD Field `maximum_supply_air_temperature`
                Unit: C
                Default value: 80.0
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
                                 'for field `maximum_supply_air_temperature`'.format(value))

        self._data["Maximum Supply Air Temperature"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """Get supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_during_cooling_operation`
        Must be less than or equal to the fan's maximum flow rate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_cooling_operation`
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
                                 'for field `supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_cooling_operation`')

        self._data["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """Get supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_during_heating_operation`
        Must be less than or equal to the fan's maximum flow fate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_heating_operation`
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
                                 'for field `supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_heating_operation`')

        self._data["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get supply_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Must be less than or equal to the fan's maximum flow rate.
        Only used when fan operating mode is continuous (disregarded for cycling fan mode).
        This air flow rate is used when no heating or cooling is required (i.e., the DX coil
        compressor and heating coil are off). If this field is left blank or zero, the supply
        air flow rate from the previous on cycle (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
                Unit: m3/s
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
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`')

        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """Get controlling_zone_or_thermostat_location

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set
        """
        return self._data["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """  Corresponds to IDD Field `controlling_zone_or_thermostat_location`

        Args:
            value (str): value for IDD Field `controlling_zone_or_thermostat_location`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controlling_zone_or_thermostat_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controlling_zone_or_thermostat_location`')

        self._data["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_fan_object_type(self):
        """Get supply_fan_object_type

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self._data["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `supply_fan_object_type`
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. supply
        air fan operating mode schedule values not equal to 0).

        Args:
            value (str): value for IDD Field `supply_fan_object_type`
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
                                 'for field `supply_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_fan_object_type`'.format(value))

        self._data["Supply Fan Object Type"] = value

    @property
    def supply_fan_name(self):
        """Get supply_fan_name

        Returns:
            str: the value of `supply_fan_name` or None if not set
        """
        return self._data["Supply Fan Name"]

    @supply_fan_name.setter
    def supply_fan_name(self, value=None):
        """  Corresponds to IDD Field `supply_fan_name`

        Args:
            value (str): value for IDD Field `supply_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_name`')

        self._data["Supply Fan Name"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="BlowThrough"):
        """  Corresponds to IDD Field `fan_placement`

        Args:
            value (str): value for IDD Field `fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: BlowThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

        self._data["Fan Placement"] = value

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
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
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
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
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
        Only works with DX cooling coil types

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - CoilSystem:Cooling:DX:HeatExchangerAssisted
                if `value` is None it will not be checked against the
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
        as needed and meet sensible load.  Valid only with
        cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted.
        This control mode allows the heat exchanger to be turned
        on and off based on the zone dehumidification requirements.
        A ZoneControl:Humidistat object is also required.
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.  Valid with all
        cooling coil types. When a heat exchanger assisted cooling
        coil is used, the heat exchanger is locked on at all times.
        A ZoneControl:Humidistat object is also required.

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
    def reheat_coil_object_type(self):
        """Get reheat_coil_object_type

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set
        """
        return self._data["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `reheat_coil_object_type`
        Only required if dehumidification control type is "CoolReheat"
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `reheat_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
                      - Coil:Heating:Desuperheater
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
                                 'for field `reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Desuperheater")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `reheat_coil_object_type`'.format(value))

        self._data["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """Get reheat_coil_name

        Returns:
            str: the value of `reheat_coil_name` or None if not set
        """
        return self._data["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """  Corresponds to IDD Field `reheat_coil_name`
        Only required if dehumidification control type is "CoolReheat"

        Args:
            value (str): value for IDD Field `reheat_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_name`')

        self._data["Reheat Coil Name"] = value

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
        out.append(self._to_str(self.furnace_air_inlet_node_name))
        out.append(self._to_str(self.furnace_air_outlet_node_name))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.maximum_supply_air_temperature))
        out.append(self._to_str(self.supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.controlling_zone_or_thermostat_location))
        out.append(self._to_str(self.supply_fan_object_type))
        out.append(self._to_str(self.supply_fan_name))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.dehumidification_control_type))
        out.append(self._to_str(self.reheat_coil_object_type))
        out.append(self._to_str(self.reheat_coil_name))
        return ",".join(out)

class AirLoopHvacUnitaryHeatOnly(object):
    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatOnly`
        Unitary system, heating-only with constant volume supply fan (continuous or cycling)
        and heating coil (gas, electric, hot water, or steam). Identical to
        AirLoopHVAC:Unitary:Furnace:HeatOnly.
    """
    internal_name = "AirLoopHVAC:UnitaryHeatOnly"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:UnitaryHeatOnly`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Unitary System Air Inlet Node Name"] = None
        self._data["Unitary System Air Outlet Node Name"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Maximum Supply Air Temperature"] = None
        self._data["Supply Air Flow Rate"] = None
        self._data["Controlling Zone or Thermostat Location"] = None
        self._data["Supply Fan Object Type"] = None
        self._data["Supply Fan Name"] = None
        self._data["Fan Placement"] = None
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
            self.unitary_system_air_inlet_node_name = None
        else:
            self.unitary_system_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.unitary_system_air_outlet_node_name = None
        else:
            self.unitary_system_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature = None
        else:
            self.maximum_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate = None
        else:
            self.supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.controlling_zone_or_thermostat_location = None
        else:
            self.controlling_zone_or_thermostat_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_object_type = None
        else:
            self.supply_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_name = None
        else:
            self.supply_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
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
    def unitary_system_air_inlet_node_name(self):
        """Get unitary_system_air_inlet_node_name

        Returns:
            str: the value of `unitary_system_air_inlet_node_name` or None if not set
        """
        return self._data["Unitary System Air Inlet Node Name"]

    @unitary_system_air_inlet_node_name.setter
    def unitary_system_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `unitary_system_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `unitary_system_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `unitary_system_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `unitary_system_air_inlet_node_name`')

        self._data["Unitary System Air Inlet Node Name"] = value

    @property
    def unitary_system_air_outlet_node_name(self):
        """Get unitary_system_air_outlet_node_name

        Returns:
            str: the value of `unitary_system_air_outlet_node_name` or None if not set
        """
        return self._data["Unitary System Air Outlet Node Name"]

    @unitary_system_air_outlet_node_name.setter
    def unitary_system_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `unitary_system_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `unitary_system_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `unitary_system_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `unitary_system_air_outlet_node_name`')

        self._data["Unitary System Air Outlet Node Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        A fan operating mode schedule value of 0 indicates cycling fan mode (supply air
        fan cycles on and off in tandem with the heating coil).
        Any other schedule value indicates continuous fan mode (supply air fan operates
        continuously regardless of heating coil operation).
        Leaving this schedule name blank will default to cycling fan mode for the
        entire simulation period.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')

        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def maximum_supply_air_temperature(self):
        """Get maximum_supply_air_temperature

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set
        """
        return self._data["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=80.0 ):
        """  Corresponds to IDD Field `maximum_supply_air_temperature`

        Args:
            value (float): value for IDD Field `maximum_supply_air_temperature`
                Unit: C
                Default value: 80.0
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
                                 'for field `maximum_supply_air_temperature`'.format(value))

        self._data["Maximum Supply Air Temperature"] = value

    @property
    def supply_air_flow_rate(self):
        """Get supply_air_flow_rate

        Returns:
            float: the value of `supply_air_flow_rate` or None if not set
        """
        return self._data["Supply Air Flow Rate"]

    @supply_air_flow_rate.setter
    def supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate`
        This value should be > 0 and <= than the fan air flow rate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate`
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
                                 'for field `supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate`')

        self._data["Supply Air Flow Rate"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """Get controlling_zone_or_thermostat_location

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set
        """
        return self._data["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """  Corresponds to IDD Field `controlling_zone_or_thermostat_location`

        Args:
            value (str): value for IDD Field `controlling_zone_or_thermostat_location`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controlling_zone_or_thermostat_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controlling_zone_or_thermostat_location`')

        self._data["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_fan_object_type(self):
        """Get supply_fan_object_type

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self._data["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `supply_fan_object_type`
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. fan
        operating mode schedule values are greater than 0).

        Args:
            value (str): value for IDD Field `supply_fan_object_type`
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
                                 'for field `supply_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_fan_object_type`'.format(value))

        self._data["Supply Fan Object Type"] = value

    @property
    def supply_fan_name(self):
        """Get supply_fan_name

        Returns:
            str: the value of `supply_fan_name` or None if not set
        """
        return self._data["Supply Fan Name"]

    @supply_fan_name.setter
    def supply_fan_name(self, value=None):
        """  Corresponds to IDD Field `supply_fan_name`

        Args:
            value (str): value for IDD Field `supply_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_name`')

        self._data["Supply Fan Name"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="BlowThrough"):
        """  Corresponds to IDD Field `fan_placement`

        Args:
            value (str): value for IDD Field `fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: BlowThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

        self._data["Fan Placement"] = value

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
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
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
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
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
        out.append(self._to_str(self.unitary_system_air_inlet_node_name))
        out.append(self._to_str(self.unitary_system_air_outlet_node_name))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.maximum_supply_air_temperature))
        out.append(self._to_str(self.supply_air_flow_rate))
        out.append(self._to_str(self.controlling_zone_or_thermostat_location))
        out.append(self._to_str(self.supply_fan_object_type))
        out.append(self._to_str(self.supply_fan_name))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        return ",".join(out)

class AirLoopHvacUnitaryHeatCool(object):
    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatCool`
        Unitary system, heating and cooling with constant volume supply fan (continuous or
        cycling), direct expansion (DX) cooling coil, heating coil (gas, electric,
        hot water, or steam), and optional reheat coil for dehumidification control.
        Identical to AirLoopHVAC:Unitary:Furnace:HeatCool.
    """
    internal_name = "AirLoopHVAC:UnitaryHeatCool"
    field_count = 20

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:UnitaryHeatCool`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Unitary System Air Inlet Node Name"] = None
        self._data["Unitary System Air Outlet Node Name"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Maximum Supply Air Temperature"] = None
        self._data["Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Supply Air Flow Rate During Heating Operation"] = None
        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Controlling Zone or Thermostat Location"] = None
        self._data["Supply Fan Object Type"] = None
        self._data["Supply Fan Name"] = None
        self._data["Fan Placement"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Dehumidification Control Type"] = None
        self._data["Reheat Coil Object Type"] = None
        self._data["Reheat Coil Name"] = None

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
            self.unitary_system_air_inlet_node_name = None
        else:
            self.unitary_system_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.unitary_system_air_outlet_node_name = None
        else:
            self.unitary_system_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature = None
        else:
            self.maximum_supply_air_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.controlling_zone_or_thermostat_location = None
        else:
            self.controlling_zone_or_thermostat_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_object_type = None
        else:
            self.supply_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_name = None
        else:
            self.supply_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
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
            self.reheat_coil_object_type = None
        else:
            self.reheat_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reheat_coil_name = None
        else:
            self.reheat_coil_name = vals[i]
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
    def unitary_system_air_inlet_node_name(self):
        """Get unitary_system_air_inlet_node_name

        Returns:
            str: the value of `unitary_system_air_inlet_node_name` or None if not set
        """
        return self._data["Unitary System Air Inlet Node Name"]

    @unitary_system_air_inlet_node_name.setter
    def unitary_system_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `unitary_system_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `unitary_system_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `unitary_system_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `unitary_system_air_inlet_node_name`')

        self._data["Unitary System Air Inlet Node Name"] = value

    @property
    def unitary_system_air_outlet_node_name(self):
        """Get unitary_system_air_outlet_node_name

        Returns:
            str: the value of `unitary_system_air_outlet_node_name` or None if not set
        """
        return self._data["Unitary System Air Outlet Node Name"]

    @unitary_system_air_outlet_node_name.setter
    def unitary_system_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `unitary_system_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `unitary_system_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `unitary_system_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `unitary_system_air_outlet_node_name`')

        self._data["Unitary System Air Outlet Node Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        A fan operating mode schedule value of 0 indicates cycling fan mode (supply air
        fan cycles on and off in tandem with the cooling or heating coil).
        Any other schedule value indicates continuous fan mode (supply air fan operates
        continuously regardless of cooling or heating coil operation). Provide a schedule
        with non-zero values when high humidity control is specified.
        Leaving this schedule name blank will default to cycling fan mode for the
        entire simulation period.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')

        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def maximum_supply_air_temperature(self):
        """Get maximum_supply_air_temperature

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set
        """
        return self._data["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=80.0 ):
        """  Corresponds to IDD Field `maximum_supply_air_temperature`

        Args:
            value (float): value for IDD Field `maximum_supply_air_temperature`
                Unit: C
                Default value: 80.0
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
                                 'for field `maximum_supply_air_temperature`'.format(value))

        self._data["Maximum Supply Air Temperature"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """Get supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_during_cooling_operation`
        Must be less than or equal to the fan's maximum flow rate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_cooling_operation`
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
                                 'for field `supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_cooling_operation`')

        self._data["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """Get supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_during_heating_operation`
        Must be less than or equal to the fan's maximum flow rate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_heating_operation`
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
                                 'for field `supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_heating_operation`')

        self._data["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get supply_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Must be less than or equal to the fan's maximum flow rate.
        Only used when fan operating mode is continuous (disregarded for cycling fan mode).
        This air flow rate is used when no heating or cooling is required (i.e., the DX coil
        compressor and heating coil are off). If this field is left blank or zero, the supply
        air flow rate from the previous on cycle (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
                Unit: m3/s
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
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`')

        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """Get controlling_zone_or_thermostat_location

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set
        """
        return self._data["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """  Corresponds to IDD Field `controlling_zone_or_thermostat_location`

        Args:
            value (str): value for IDD Field `controlling_zone_or_thermostat_location`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controlling_zone_or_thermostat_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controlling_zone_or_thermostat_location`')

        self._data["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_fan_object_type(self):
        """Get supply_fan_object_type

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self._data["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `supply_fan_object_type`
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. supply
        air fan operating mode schedule values not equal to 0).

        Args:
            value (str): value for IDD Field `supply_fan_object_type`
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
                                 'for field `supply_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_fan_object_type`'.format(value))

        self._data["Supply Fan Object Type"] = value

    @property
    def supply_fan_name(self):
        """Get supply_fan_name

        Returns:
            str: the value of `supply_fan_name` or None if not set
        """
        return self._data["Supply Fan Name"]

    @supply_fan_name.setter
    def supply_fan_name(self, value=None):
        """  Corresponds to IDD Field `supply_fan_name`

        Args:
            value (str): value for IDD Field `supply_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_name`')

        self._data["Supply Fan Name"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="BlowThrough"):
        """  Corresponds to IDD Field `fan_placement`

        Args:
            value (str): value for IDD Field `fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: BlowThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

        self._data["Fan Placement"] = value

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
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
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
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
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
        Only works with DX cooling coil types or
        Coil:Cooling:DX:VariableSpeed.

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - Coil:Cooling:DX:VariableSpeed
                      - CoilSystem:Cooling:DX:HeatExchangerAssisted
                if `value` is None it will not be checked against the
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
            vals.add("Coil:Cooling:DX:VariableSpeed")
            vals.add("CoilSystem:Cooling:DX:HeatExchangerAssisted")
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
        as needed and meet sensible load.  Valid only with
        cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted.
        This control mode allows the heat exchanger to be turned
        on and off based on the zone dehumidification requirements.
        A ZoneControl:Humidistat object is also required.
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.  Valid with all
        cooling coil types. When a heat exchanger assisted Cooling
        coil is used, the heat exchanger is locked on at all times.
        A ZoneControl:Humidistat object is also required.

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
    def reheat_coil_object_type(self):
        """Get reheat_coil_object_type

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set
        """
        return self._data["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `reheat_coil_object_type`
        Only required if dehumidification control type is "CoolReheat"
        works with gas, electric, desuperheating, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `reheat_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
                      - Coil:Heating:Desuperheater
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
                                 'for field `reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Desuperheater")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `reheat_coil_object_type`'.format(value))

        self._data["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """Get reheat_coil_name

        Returns:
            str: the value of `reheat_coil_name` or None if not set
        """
        return self._data["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """  Corresponds to IDD Field `reheat_coil_name`
        Only required if dehumidification control type is "CoolReheat"

        Args:
            value (str): value for IDD Field `reheat_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_name`')

        self._data["Reheat Coil Name"] = value

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
        out.append(self._to_str(self.unitary_system_air_inlet_node_name))
        out.append(self._to_str(self.unitary_system_air_outlet_node_name))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.maximum_supply_air_temperature))
        out.append(self._to_str(self.supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.controlling_zone_or_thermostat_location))
        out.append(self._to_str(self.supply_fan_object_type))
        out.append(self._to_str(self.supply_fan_name))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.dehumidification_control_type))
        out.append(self._to_str(self.reheat_coil_object_type))
        out.append(self._to_str(self.reheat_coil_name))
        return ",".join(out)

class AirLoopHvacUnitaryHeatPumpAirToAir(object):
    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatPump:AirToAir`
        Unitary heat pump system, heating and cooling, single-speed with supply fan, direct
        expansion (DX) cooling coil, DX heating coil (air-to-air heat pump), and supplemental
        heating coil (gas, electric, hot water, or steam).
    """
    internal_name = "AirLoopHVAC:UnitaryHeatPump:AirToAir"
    field_count = 21

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:UnitaryHeatPump:AirToAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Supply Air Flow Rate During Heating Operation"] = None
        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Controlling Zone or Thermostat Location"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Supplemental Heating Coil Object Type"] = None
        self._data["Supplemental Heating Coil Name"] = None
        self._data["Maximum Supply Air Temperature from Supplemental Heater"] = None
        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = None
        self._data["Fan Placement"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Dehumidification Control Type"] = None

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
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_during_heating_operation = None
        else:
            self.supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.controlling_zone_or_thermostat_location = None
        else:
            self.controlling_zone_or_thermostat_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
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
            self.supplemental_heating_coil_object_type = None
        else:
            self.supplemental_heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_name = None
        else:
            self.supplemental_heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature_from_supplemental_heater = None
        else:
            self.maximum_supply_air_temperature_from_supplemental_heater = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = None
        else:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dehumidification_control_type = None
        else:
            self.dehumidification_control_type = vals[i]
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
        A schedule value greater than zero (usually 1 is used) indicates that the unit is
        available to operate as needed. A value less than or equal to zero (usually zero
        is used) denotes that the unit must be off.

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
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_inlet_node_name`

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')

        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_outlet_node_name`

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')

        self._data["Air Outlet Node Name"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """Get supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_during_cooling_operation`
        Must be less than or equal to the fan's maximum flow rate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_cooling_operation`
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
                                 'for field `supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_cooling_operation`')

        self._data["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """Get supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_during_heating_operation`
        Must be less than or equal to the fan's maximum flow rate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_during_heating_operation`
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
                                 'for field `supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate_during_heating_operation`')

        self._data["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get supply_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Must be less than or equal to the fans maximum flow rate.
        Only used when fan operating mode is continuous (disregarded for cycling fan mode).
        This air flow rate is used when no heating or cooling is required (i.e., the DX coil
        compressor and supplemental heating coil are off). If this field is left blank or zero,
        the supply air flow rate from the previous on cycle (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
                Unit: m3/s
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
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`')

        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """Get controlling_zone_or_thermostat_location

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set
        """
        return self._data["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """  Corresponds to IDD Field `controlling_zone_or_thermostat_location`

        Args:
            value (str): value for IDD Field `controlling_zone_or_thermostat_location`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controlling_zone_or_thermostat_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controlling_zone_or_thermostat_location`')

        self._data["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. fan
        operating mode schedule values are greater than 0 or the fan operating mode
        schedule name field is left blank).

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_name`
        Needs to match in the fan object

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')

        self._data["Supply Air Fan Name"] = value

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
        Only works with Coil:Heating:DX:SingleSpeed or
        Coil:Heating:DX:VariableSpeed

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
        Needs to match in the DX heating coil object

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
        Only works with Coil:Cooling:DX:SingleSpeed or
        CoilSystem:Cooling:DX:HeatExchangerAssisted or
        Coil:Cooling:DX:VariableSpeed

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - Coil:Cooling:DX:VariableSpeed
                      - CoilSystem:Cooling:DX:HeatExchangerAssisted
                if `value` is None it will not be checked against the
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
            vals.add("Coil:Cooling:DX:VariableSpeed")
            vals.add("CoilSystem:Cooling:DX:HeatExchangerAssisted")
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
        Needs to match in the DX cooling coil object

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
    def supplemental_heating_coil_object_type(self):
        """Get supplemental_heating_coil_object_type

        Returns:
            str: the value of `supplemental_heating_coil_object_type` or None if not set
        """
        return self._data["Supplemental Heating Coil Object Type"]

    @supplemental_heating_coil_object_type.setter
    def supplemental_heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `supplemental_heating_coil_object_type`
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
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
                                 'for field `supplemental_heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supplemental_heating_coil_object_type`'.format(value))

        self._data["Supplemental Heating Coil Object Type"] = value

    @property
    def supplemental_heating_coil_name(self):
        """Get supplemental_heating_coil_name

        Returns:
            str: the value of `supplemental_heating_coil_name` or None if not set
        """
        return self._data["Supplemental Heating Coil Name"]

    @supplemental_heating_coil_name.setter
    def supplemental_heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `supplemental_heating_coil_name`
        Needs to match in the supplemental heating coil object

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_name`')

        self._data["Supplemental Heating Coil Name"] = value

    @property
    def maximum_supply_air_temperature_from_supplemental_heater(self):
        """Get maximum_supply_air_temperature_from_supplemental_heater

        Returns:
            float: the value of `maximum_supply_air_temperature_from_supplemental_heater` or None if not set
        """
        return self._data["Maximum Supply Air Temperature from Supplemental Heater"]

    @maximum_supply_air_temperature_from_supplemental_heater.setter
    def maximum_supply_air_temperature_from_supplemental_heater(self, value=None):
        """  Corresponds to IDD Field `maximum_supply_air_temperature_from_supplemental_heater`

        Args:
            value (float): value for IDD Field `maximum_supply_air_temperature_from_supplemental_heater`
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
                                 'for field `maximum_supply_air_temperature_from_supplemental_heater`'.format(value))

        self._data["Maximum Supply Air Temperature from Supplemental Heater"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self):
        """Get maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation` or None if not set
        """
        return self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"]

    @maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation.setter
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self, value=21.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`

        Args:
            value (float): value for IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`
                Unit: C
                Default value: 21.0
                value <= 21.0
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
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`'.format(value))
            if value > 21.0:
                raise ValueError('value need to be smaller 21.0 '
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`')

        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="BlowThrough"):
        """  Corresponds to IDD Field `fan_placement`

        Args:
            value (str): value for IDD Field `fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: BlowThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

        self._data["Fan Placement"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        A fan operating mode schedule value of 0 indicates cycling fan mode (supply air
        fan cycles on and off in tandem with the cooling or heating coil).
        Any other schedule value indicates continuous fan mode (supply air fan operates
        continuously regardless of cooling or heating coil operation).
        Leaving this schedule name blank will default to cycling fan mode for the
        entire simulation period.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')

        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

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
        as needed and meet sensible load.  Valid only with
        cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted.
        This control mode allows the heat exchanger to be turned
        on and off based on the zone dehumidification requirements.
        A ZoneControl:Humidistat object is also required.
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.  Valid with all
        cooling coil types. When a heat exchanger assisted Cooling
        coil is used, the heat exchanger is locked on at all times.
        A ZoneControl:Humidistat object is also required.

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
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.controlling_zone_or_thermostat_location))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.supplemental_heating_coil_object_type))
        out.append(self._to_str(self.supplemental_heating_coil_name))
        out.append(self._to_str(self.maximum_supply_air_temperature_from_supplemental_heater))
        out.append(self._to_str(self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.dehumidification_control_type))
        return ",".join(out)

class AirLoopHvacUnitaryHeatPumpWaterToAir(object):
    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatPump:WaterToAir`
        Unitary heat pump system, heating and cooling, single-speed with constant volume
        supply fan (continuous or cycling), direct expansion (DX) cooling coil, DX heating
        coil (water-to-air heat pump), and supplemental heating coil (gas, electric,
        hot water, or steam).
    """
    internal_name = "AirLoopHVAC:UnitaryHeatPump:WaterToAir"
    field_count = 27

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:UnitaryHeatPump:WaterToAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Supply Air Flow Rate"] = None
        self._data["Controlling Zone or Thermostat Location"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Heating Convergence"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Cooling Convergence"] = None
        self._data["Maximum Cycling Rate"] = None
        self._data["Heat Pump Time Constant"] = None
        self._data["Fraction of On-Cycle Power Use"] = None
        self._data["Heat Pump Fan Delay Time"] = None
        self._data["Supplemental Heating Coil Object Type"] = None
        self._data["Supplemental Heating Coil Name"] = None
        self._data["Maximum Supply Air Temperature from Supplemental Heater"] = None
        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = None
        self._data["Outdoor Dry-Bulb Temperature Sensor Node Name"] = None
        self._data["Fan Placement"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Dehumidification Control Type"] = None
        self._data["Heat Pump Coil Water Flow Mode"] = None

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
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate = None
        else:
            self.supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.controlling_zone_or_thermostat_location = None
        else:
            self.controlling_zone_or_thermostat_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
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
        if len(vals[i]) == 0:
            self.heating_convergence = None
        else:
            self.heating_convergence = vals[i]
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
            self.cooling_convergence = None
        else:
            self.cooling_convergence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_cycling_rate = None
        else:
            self.maximum_cycling_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_pump_time_constant = None
        else:
            self.heat_pump_time_constant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_oncycle_power_use = None
        else:
            self.fraction_of_oncycle_power_use = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_pump_fan_delay_time = None
        else:
            self.heat_pump_fan_delay_time = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_object_type = None
        else:
            self.supplemental_heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_name = None
        else:
            self.supplemental_heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature_from_supplemental_heater = None
        else:
            self.maximum_supply_air_temperature_from_supplemental_heater = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = None
        else:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_drybulb_temperature_sensor_node_name = None
        else:
            self.outdoor_drybulb_temperature_sensor_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fan_placement = None
        else:
            self.fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dehumidification_control_type = None
        else:
            self.dehumidification_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_pump_coil_water_flow_mode = None
        else:
            self.heat_pump_coil_water_flow_mode = vals[i]
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
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_inlet_node_name`

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')

        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_outlet_node_name`

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')

        self._data["Air Outlet Node Name"] = value

    @property
    def supply_air_flow_rate(self):
        """Get supply_air_flow_rate

        Returns:
            float: the value of `supply_air_flow_rate` or None if not set
        """
        return self._data["Supply Air Flow Rate"]

    @supply_air_flow_rate.setter
    def supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate`
        This value should be > 0 and <= than the fan air flow rate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate`
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
                                 'for field `supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `supply_air_flow_rate`')

        self._data["Supply Air Flow Rate"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """Get controlling_zone_or_thermostat_location

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set
        """
        return self._data["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """  Corresponds to IDD Field `controlling_zone_or_thermostat_location`

        Args:
            value (str): value for IDD Field `controlling_zone_or_thermostat_location`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controlling_zone_or_thermostat_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controlling_zone_or_thermostat_location`')

        self._data["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Only works with On/Off Fan

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
                Accepted values are:
                      - Fan:OnOff
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_name`
        Needs to match Fan:OnOff object

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')

        self._data["Supply Air Fan Name"] = value

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
                      - Coil:Heating:WaterToAirHeatPump:ParameterEstimation
                      - Coil:Heating:WaterToAirHeatPump:EquationFit
                      - Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit
                if `value` is None it will not be checked against the
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
            vals.add("Coil:Heating:WaterToAirHeatPump:ParameterEstimation")
            vals.add("Coil:Heating:WaterToAirHeatPump:EquationFit")
            vals.add("Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit")
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
        Needs to match in the water-to-air heatpump heating coil object

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

    @property
    def heating_convergence(self):
        """Get heating_convergence

        Returns:
            float: the value of `heating_convergence` or None if not set
        """
        return self._data["Heating Convergence"]

    @heating_convergence.setter
    def heating_convergence(self, value=0.001 ):
        """  Corresponds to IDD Field `heating_convergence`

        Args:
            value (float): value for IDD Field `heating_convergence`
                Default value: 0.001
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
                                 'for field `heating_convergence`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heating_convergence`')

        self._data["Heating Convergence"] = value

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
                      - Coil:Cooling:WaterToAirHeatPump:ParameterEstimation
                      - Coil:Cooling:WaterToAirHeatPump:EquationFit
                      - Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit
                if `value` is None it will not be checked against the
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
            vals.add("Coil:Cooling:WaterToAirHeatPump:ParameterEstimation")
            vals.add("Coil:Cooling:WaterToAirHeatPump:EquationFit")
            vals.add("Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit")
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
        Needs to match in the water-to-air heatpump cooling coil object

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
    def cooling_convergence(self):
        """Get cooling_convergence

        Returns:
            float: the value of `cooling_convergence` or None if not set
        """
        return self._data["Cooling Convergence"]

    @cooling_convergence.setter
    def cooling_convergence(self, value=0.001 ):
        """  Corresponds to IDD Field `cooling_convergence`

        Args:
            value (float): value for IDD Field `cooling_convergence`
                Default value: 0.001
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
                                 'for field `cooling_convergence`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_convergence`')

        self._data["Cooling Convergence"] = value

    @property
    def maximum_cycling_rate(self):
        """Get maximum_cycling_rate

        Returns:
            float: the value of `maximum_cycling_rate` or None if not set
        """
        return self._data["Maximum Cycling Rate"]

    @maximum_cycling_rate.setter
    def maximum_cycling_rate(self, value=2.5 ):
        """  Corresponds to IDD Field `maximum_cycling_rate`
        The maximum on-off cycling rate for the compressor
        Suggested value is 2.5 for a typical heat pump

        Args:
            value (float): value for IDD Field `maximum_cycling_rate`
                Unit: cycles/hr
                Default value: 2.5
                value >= 0.0
                value <= 5.0
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
                                 'for field `maximum_cycling_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_cycling_rate`')
            if value > 5.0:
                raise ValueError('value need to be smaller 5.0 '
                                 'for field `maximum_cycling_rate`')

        self._data["Maximum Cycling Rate"] = value

    @property
    def heat_pump_time_constant(self):
        """Get heat_pump_time_constant

        Returns:
            float: the value of `heat_pump_time_constant` or None if not set
        """
        return self._data["Heat Pump Time Constant"]

    @heat_pump_time_constant.setter
    def heat_pump_time_constant(self, value=60.0 ):
        """  Corresponds to IDD Field `heat_pump_time_constant`
        Time constant for the cooling coil's capacity to reach steady state after startup
        Suggested value is 60 for a typical heat pump

        Args:
            value (float): value for IDD Field `heat_pump_time_constant`
                Unit: s
                Default value: 60.0
                value >= 0.0
                value <= 500.0
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
                                 'for field `heat_pump_time_constant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heat_pump_time_constant`')
            if value > 500.0:
                raise ValueError('value need to be smaller 500.0 '
                                 'for field `heat_pump_time_constant`')

        self._data["Heat Pump Time Constant"] = value

    @property
    def fraction_of_oncycle_power_use(self):
        """Get fraction_of_oncycle_power_use

        Returns:
            float: the value of `fraction_of_oncycle_power_use` or None if not set
        """
        return self._data["Fraction of On-Cycle Power Use"]

    @fraction_of_oncycle_power_use.setter
    def fraction_of_oncycle_power_use(self, value=0.01 ):
        """  Corresponds to IDD Field `fraction_of_oncycle_power_use`
        The fraction of on-cycle power use to adjust the part load fraction based on
        the off-cycle power consumption due to crankcase heaters, controls, fans, and etc.
        Suggested value is 0.01 for a typical heat pump

        Args:
            value (float): value for IDD Field `fraction_of_oncycle_power_use`
                Default value: 0.01
                value >= 0.0
                value <= 0.05
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
                                 'for field `fraction_of_oncycle_power_use`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_oncycle_power_use`')
            if value > 0.05:
                raise ValueError('value need to be smaller 0.05 '
                                 'for field `fraction_of_oncycle_power_use`')

        self._data["Fraction of On-Cycle Power Use"] = value

    @property
    def heat_pump_fan_delay_time(self):
        """Get heat_pump_fan_delay_time

        Returns:
            float: the value of `heat_pump_fan_delay_time` or None if not set
        """
        return self._data["Heat Pump Fan Delay Time"]

    @heat_pump_fan_delay_time.setter
    def heat_pump_fan_delay_time(self, value=60.0 ):
        """  Corresponds to IDD Field `heat_pump_fan_delay_time`
        Programmed time delay for heat pump fan to shut off after compressor cycle off.
        Only required when fan operating mode is cycling
        Enter 0 when fan operating mode is continuous

        Args:
            value (float): value for IDD Field `heat_pump_fan_delay_time`
                Unit: s
                Default value: 60.0
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
                                 'for field `heat_pump_fan_delay_time`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heat_pump_fan_delay_time`')

        self._data["Heat Pump Fan Delay Time"] = value

    @property
    def supplemental_heating_coil_object_type(self):
        """Get supplemental_heating_coil_object_type

        Returns:
            str: the value of `supplemental_heating_coil_object_type` or None if not set
        """
        return self._data["Supplemental Heating Coil Object Type"]

    @supplemental_heating_coil_object_type.setter
    def supplemental_heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `supplemental_heating_coil_object_type`
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
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
                                 'for field `supplemental_heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supplemental_heating_coil_object_type`'.format(value))

        self._data["Supplemental Heating Coil Object Type"] = value

    @property
    def supplemental_heating_coil_name(self):
        """Get supplemental_heating_coil_name

        Returns:
            str: the value of `supplemental_heating_coil_name` or None if not set
        """
        return self._data["Supplemental Heating Coil Name"]

    @supplemental_heating_coil_name.setter
    def supplemental_heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `supplemental_heating_coil_name`
        Needs to match in the supplemental heating coil object

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_name`')

        self._data["Supplemental Heating Coil Name"] = value

    @property
    def maximum_supply_air_temperature_from_supplemental_heater(self):
        """Get maximum_supply_air_temperature_from_supplemental_heater

        Returns:
            float: the value of `maximum_supply_air_temperature_from_supplemental_heater` or None if not set
        """
        return self._data["Maximum Supply Air Temperature from Supplemental Heater"]

    @maximum_supply_air_temperature_from_supplemental_heater.setter
    def maximum_supply_air_temperature_from_supplemental_heater(self, value=None):
        """  Corresponds to IDD Field `maximum_supply_air_temperature_from_supplemental_heater`

        Args:
            value (float): value for IDD Field `maximum_supply_air_temperature_from_supplemental_heater`
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
                                 'for field `maximum_supply_air_temperature_from_supplemental_heater`'.format(value))

        self._data["Maximum Supply Air Temperature from Supplemental Heater"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self):
        """Get maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation` or None if not set
        """
        return self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"]

    @maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation.setter
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self, value=21.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`

        Args:
            value (float): value for IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`
                Unit: C
                Default value: 21.0
                value <= 21.0
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
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`'.format(value))
            if value > 21.0:
                raise ValueError('value need to be smaller 21.0 '
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`')

        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = value

    @property
    def outdoor_drybulb_temperature_sensor_node_name(self):
        """Get outdoor_drybulb_temperature_sensor_node_name

        Returns:
            str: the value of `outdoor_drybulb_temperature_sensor_node_name` or None if not set
        """
        return self._data["Outdoor Dry-Bulb Temperature Sensor Node Name"]

    @outdoor_drybulb_temperature_sensor_node_name.setter
    def outdoor_drybulb_temperature_sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_drybulb_temperature_sensor_node_name`

        Args:
            value (str): value for IDD Field `outdoor_drybulb_temperature_sensor_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_drybulb_temperature_sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_drybulb_temperature_sensor_node_name`')

        self._data["Outdoor Dry-Bulb Temperature Sensor Node Name"] = value

    @property
    def fan_placement(self):
        """Get fan_placement

        Returns:
            str: the value of `fan_placement` or None if not set
        """
        return self._data["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="BlowThrough"):
        """  Corresponds to IDD Field `fan_placement`

        Args:
            value (str): value for IDD Field `fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: BlowThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fan_placement`'.format(value))

        self._data["Fan Placement"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        Enter the name of a schedule that controls fan operation. Schedule values of 0 denote
        cycling fan operation (fan cycles with cooling or heating coil). Schedule values greater
        than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        The fan operating mode defaults to cycling fan operation if this field is left blank.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')

        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

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
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.  Valid only with
        Coil:Cooling:WaterToAirHeatPump:EquationFit or
        Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit

        Args:
            value (str): value for IDD Field `dehumidification_control_type`
                Accepted values are:
                      - None
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
            vals.add("CoolReheat")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `dehumidification_control_type`'.format(value))

        self._data["Dehumidification Control Type"] = value

    @property
    def heat_pump_coil_water_flow_mode(self):
        """Get heat_pump_coil_water_flow_mode

        Returns:
            str: the value of `heat_pump_coil_water_flow_mode` or None if not set
        """
        return self._data["Heat Pump Coil Water Flow Mode"]

    @heat_pump_coil_water_flow_mode.setter
    def heat_pump_coil_water_flow_mode(self, value="Cycling"):
        """  Corresponds to IDD Field `heat_pump_coil_water_flow_mode`
        used only when the heat pump coils are of the type WaterToAirHeatPump:EquationFit
        Constant results in 100% water flow regardless of compressor PLR
        Cycling results in water flow that matches compressor PLR
        ConstantOnDemand results in 100% water flow whenever the coil is on, but is 0% whenever the coil has no load

        Args:
            value (str): value for IDD Field `heat_pump_coil_water_flow_mode`
                Accepted values are:
                      - Constant
                      - Cycling
                      - ConstantOnDemand
                Default value: Cycling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_pump_coil_water_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_pump_coil_water_flow_mode`')
            vals = set()
            vals.add("Constant")
            vals.add("Cycling")
            vals.add("ConstantOnDemand")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heat_pump_coil_water_flow_mode`'.format(value))

        self._data["Heat Pump Coil Water Flow Mode"] = value

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
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.supply_air_flow_rate))
        out.append(self._to_str(self.controlling_zone_or_thermostat_location))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.heating_convergence))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.cooling_convergence))
        out.append(self._to_str(self.maximum_cycling_rate))
        out.append(self._to_str(self.heat_pump_time_constant))
        out.append(self._to_str(self.fraction_of_oncycle_power_use))
        out.append(self._to_str(self.heat_pump_fan_delay_time))
        out.append(self._to_str(self.supplemental_heating_coil_object_type))
        out.append(self._to_str(self.supplemental_heating_coil_name))
        out.append(self._to_str(self.maximum_supply_air_temperature_from_supplemental_heater))
        out.append(self._to_str(self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation))
        out.append(self._to_str(self.outdoor_drybulb_temperature_sensor_node_name))
        out.append(self._to_str(self.fan_placement))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.dehumidification_control_type))
        out.append(self._to_str(self.heat_pump_coil_water_flow_mode))
        return ",".join(out)

class AirLoopHvacUnitaryHeatCoolVavchangeoverBypass(object):
    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass`
        Unitary system, heating and cooling with constant volume supply fan (continuous or
        cycling), direct expansion (DX) cooling coil, heating coil (gas, electric,
        hot water, steam, or DX air-to-air heat pump) and bypass damper for variable volume
        flow to terminal units. Used with AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat
        or AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat.
    """
    internal_name = "AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass"
    field_count = 27

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["System Air Flow Rate During Cooling Operation"] = None
        self._data["System Air Flow Rate During Heating Operation"] = None
        self._data["System Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Outdoor Air Flow Rate During Cooling Operation"] = None
        self._data["Outdoor Air Flow Rate During Heating Operation"] = None
        self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Outdoor Air Flow Rate Multiplier Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Bypass Duct Mixer Node Name"] = None
        self._data["Bypass Duct Splitter Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Outdoor Air Mixer Object Type"] = None
        self._data["Outdoor Air Mixer Name"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Supply Air Fan Placement"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Priority Control Mode"] = None
        self._data["Minimum Outlet Air Temperature During Cooling Operation"] = None
        self._data["Maximum Outlet Air Temperature During Heating Operation"] = None
        self._data["Dehumidification Control Type"] = None

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
            self.system_air_flow_rate_during_cooling_operation = None
        else:
            self.system_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.system_air_flow_rate_during_heating_operation = None
        else:
            self.system_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.system_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.system_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_cooling_operation = None
        else:
            self.outdoor_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_during_heating_operation = None
        else:
            self.outdoor_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_multiplier_schedule_name = None
        else:
            self.outdoor_air_flow_rate_multiplier_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.bypass_duct_mixer_node_name = None
        else:
            self.bypass_duct_mixer_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.bypass_duct_splitter_node_name = None
        else:
            self.bypass_duct_splitter_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_object_type = None
        else:
            self.outdoor_air_mixer_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_name = None
        else:
            self.outdoor_air_mixer_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_placement = None
        else:
            self.supply_air_fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
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
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.priority_control_mode = None
        else:
            self.priority_control_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outlet_air_temperature_during_cooling_operation = None
        else:
            self.minimum_outlet_air_temperature_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outlet_air_temperature_during_heating_operation = None
        else:
            self.maximum_outlet_air_temperature_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dehumidification_control_type = None
        else:
            self.dehumidification_control_type = vals[i]
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
        Enter a unique name for this unitary system.

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
        Enter the availability schedule name. Schedule values of zero denote system
        is Off. Non-zero schedule values denote system is available to operate.

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
    def system_air_flow_rate_during_cooling_operation(self):
        """Get system_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `system_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["System Air Flow Rate During Cooling Operation"]

    @system_air_flow_rate_during_cooling_operation.setter
    def system_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `system_air_flow_rate_during_cooling_operation`
        Enter the system air flow rate during cooling
        operation or specify autosize.

        Args:
            value (float): value for IDD Field `system_air_flow_rate_during_cooling_operation`
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
                                 'for field `system_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `system_air_flow_rate_during_cooling_operation`')

        self._data["System Air Flow Rate During Cooling Operation"] = value

    @property
    def system_air_flow_rate_during_heating_operation(self):
        """Get system_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `system_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["System Air Flow Rate During Heating Operation"]

    @system_air_flow_rate_during_heating_operation.setter
    def system_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `system_air_flow_rate_during_heating_operation`
        Enter the system air flow rate during heating
        operation or specify autosize.

        Args:
            value (float): value for IDD Field `system_air_flow_rate_during_heating_operation`
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
                                 'for field `system_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `system_air_flow_rate_during_heating_operation`')

        self._data["System Air Flow Rate During Heating Operation"] = value

    @property
    def system_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get system_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `system_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["System Air Flow Rate When No Cooling or Heating is Needed"]

    @system_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def system_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `system_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Only used when the supply air fan operating mode is continuous (see field
        Supply air fan operating mode schedule name). This system air flow rate
        is used when no heating or cooling is required and the coils are off.
        If this field is left blank or zero, the system air flow rate from the
        previous on cycle (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `system_air_flow_rate_when_no_cooling_or_heating_is_needed`
                Unit: m3/s
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
                                 'for field `system_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `system_air_flow_rate_when_no_cooling_or_heating_is_needed`')

        self._data["System Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def outdoor_air_flow_rate_during_cooling_operation(self):
        """Get outdoor_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `outdoor_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Outdoor Air Flow Rate During Cooling Operation"]

    @outdoor_air_flow_rate_during_cooling_operation.setter
    def outdoor_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_flow_rate_during_cooling_operation`
        Enter the outdoor air flow rate during
        cooling operation or specify autosize.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_during_cooling_operation`
                Unit: m3/s
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
                                 'for field `outdoor_air_flow_rate_during_cooling_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_during_cooling_operation`')

        self._data["Outdoor Air Flow Rate During Cooling Operation"] = value

    @property
    def outdoor_air_flow_rate_during_heating_operation(self):
        """Get outdoor_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `outdoor_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Outdoor Air Flow Rate During Heating Operation"]

    @outdoor_air_flow_rate_during_heating_operation.setter
    def outdoor_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_flow_rate_during_heating_operation`
        Enter the outdoor air flow rate during
        heating operation or specify autosize.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_during_heating_operation`
                Unit: m3/s
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
                                 'for field `outdoor_air_flow_rate_during_heating_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_during_heating_operation`')

        self._data["Outdoor Air Flow Rate During Heating Operation"] = value

    @property
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"]

    @outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Only used when the supply air fan operating mode is continuous (see field
        Supply air fan operating mode schedule name). This outdoor air flow rate
        is used when no heating or cooling is required and the coils are off.
        If this field is left blank or zero, the outdoor air flow rate from the previous on cycle
        (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`
                Unit: m3/s
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
                                 'for field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed`')

        self._data["Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def outdoor_air_flow_rate_multiplier_schedule_name(self):
        """Get outdoor_air_flow_rate_multiplier_schedule_name

        Returns:
            str: the value of `outdoor_air_flow_rate_multiplier_schedule_name` or None if not set
        """
        return self._data["Outdoor Air Flow Rate Multiplier Schedule Name"]

    @outdoor_air_flow_rate_multiplier_schedule_name.setter
    def outdoor_air_flow_rate_multiplier_schedule_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_flow_rate_multiplier_schedule_name`
        Enter the name of a schedule that contains multipliers for the outdoor air
        flow rates. Schedule values must be from 0 to 1.
        If field is left blank, model assumes multiplier is 1 for the entire simulation period.

        Args:
            value (str): value for IDD Field `outdoor_air_flow_rate_multiplier_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_flow_rate_multiplier_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_flow_rate_multiplier_schedule_name`')

        self._data["Outdoor Air Flow Rate Multiplier Schedule Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_inlet_node_name`
        Enter the name of the unitary system's air inlet node.

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')

        self._data["Air Inlet Node Name"] = value

    @property
    def bypass_duct_mixer_node_name(self):
        """Get bypass_duct_mixer_node_name

        Returns:
            str: the value of `bypass_duct_mixer_node_name` or None if not set
        """
        return self._data["Bypass Duct Mixer Node Name"]

    @bypass_duct_mixer_node_name.setter
    def bypass_duct_mixer_node_name(self, value=None):
        """  Corresponds to IDD Field `bypass_duct_mixer_node_name`
        Enter the name of the bypass duct mixer node. This name should be the name
        of the return air node for the outdoor air mixer associated with this system.
        This node name must be different from the air inlet node name.

        Args:
            value (str): value for IDD Field `bypass_duct_mixer_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `bypass_duct_mixer_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `bypass_duct_mixer_node_name`')

        self._data["Bypass Duct Mixer Node Name"] = value

    @property
    def bypass_duct_splitter_node_name(self):
        """Get bypass_duct_splitter_node_name

        Returns:
            str: the value of `bypass_duct_splitter_node_name` or None if not set
        """
        return self._data["Bypass Duct Splitter Node Name"]

    @bypass_duct_splitter_node_name.setter
    def bypass_duct_splitter_node_name(self, value=None):
        """  Corresponds to IDD Field `bypass_duct_splitter_node_name`
        Enter the name of the bypass duct splitter node.
        This splitter air node is the outlet node of the last component in this unitary
        system. For blow through fan placement, the splitter air node is the outlet
        node of the heating coil. For draw through fan placement, the splitter node
        is the outlet node of the supply air fan.

        Args:
            value (str): value for IDD Field `bypass_duct_splitter_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `bypass_duct_splitter_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `bypass_duct_splitter_node_name`')

        self._data["Bypass Duct Splitter Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_outlet_node_name`
        Enter the name of the unitary system's air outlet node.

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')

        self._data["Air Outlet Node Name"] = value

    @property
    def outdoor_air_mixer_object_type(self):
        """Get outdoor_air_mixer_object_type

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set
        """
        return self._data["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_mixer_object_type`
        currently only one type OutdoorAir:Mixer object is available.

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_object_type`
                Accepted values are:
                      - OutdoorAir:Mixer
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_object_type`')
            vals = set()
            vals.add("OutdoorAir:Mixer")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outdoor_air_mixer_object_type`'.format(value))

        self._data["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """Get outdoor_air_mixer_name

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set
        """
        return self._data["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_mixer_name`
        Enter the name of the outdoor air mixer used with this unitary system.

        Args:
            value (str): value for IDD Field `outdoor_air_mixer_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_mixer_name`')

        self._data["Outdoor Air Mixer Name"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Specify the type of supply air fan used in this unitary system.

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_name`
        Enter the name of the supply air fan used in this unitary system.

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')

        self._data["Supply Air Fan Name"] = value

    @property
    def supply_air_fan_placement(self):
        """Get supply_air_fan_placement

        Returns:
            str: the value of `supply_air_fan_placement` or None if not set
        """
        return self._data["Supply Air Fan Placement"]

    @supply_air_fan_placement.setter
    def supply_air_fan_placement(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_placement`
        Specify supply air fan placement as either blow through or draw through.
        BlowThrough means the supply air fan is located before the cooling
        coil. DrawThrough means the supply air fan is located after the heating coil.

        Args:
            value (str): value for IDD Field `supply_air_fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_placement`'.format(value))

        self._data["Supply Air Fan Placement"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        Enter the name of a schedule to control the supply air fan. Schedule Name values of zero
        mean that the supply air fan will cycle off if there is no cooling or heating load
        in any of the zones being served by this system. Non-zero schedule values mean
        that the supply air fan will operate continuously even if there is no cooling or
        heating load in any of the zones being served. If this field is left blank,
        the supply air fan will operate continuously for the entire simulation period.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')

        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

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
        Specify the type of cooling coil used in this unitary system.

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - CoilSystem:Cooling:DX:HeatExchangerAssisted
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
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:DX:SingleSpeed")
            vals.add("CoilSystem:Cooling:DX:HeatExchangerAssisted")
            vals.add("Coil:Cooling:DX:TwoStageWithHumidityControlMode")
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
        Enter the name of the cooling coil used in this unitary system.

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
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `heating_coil_object_type`
        works with DX, gas, electric, hot water and steam heating coils
        Specify the type of heating coil used in this unitary system.

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:DX:SingleSpeed
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
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
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:DX:SingleSpeed")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
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
        Enter the name of the heating coil used in this unitary system.

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

    @property
    def priority_control_mode(self):
        """Get priority_control_mode

        Returns:
            str: the value of `priority_control_mode` or None if not set
        """
        return self._data["Priority Control Mode"]

    @priority_control_mode.setter
    def priority_control_mode(self, value="ZonePriority"):
        """  Corresponds to IDD Field `priority_control_mode`
        CoolingPriority = system provides cooling if any zone requires cooling.
        HeatingPriority = system provides heating if any zone requires heating.
        ZonePriority = system controlled based on the total number of zones
        requiring cooling or heating (highest number of zones
        in cooling or heating determines the system's operating mode).

        Args:
            value (str): value for IDD Field `priority_control_mode`
                Accepted values are:
                      - CoolingPriority
                      - HeatingPriority
                      - ZonePriority
                Default value: ZonePriority
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `priority_control_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `priority_control_mode`')
            vals = set()
            vals.add("CoolingPriority")
            vals.add("HeatingPriority")
            vals.add("ZonePriority")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `priority_control_mode`'.format(value))

        self._data["Priority Control Mode"] = value

    @property
    def minimum_outlet_air_temperature_during_cooling_operation(self):
        """Get minimum_outlet_air_temperature_during_cooling_operation

        Returns:
            float: the value of `minimum_outlet_air_temperature_during_cooling_operation` or None if not set
        """
        return self._data["Minimum Outlet Air Temperature During Cooling Operation"]

    @minimum_outlet_air_temperature_during_cooling_operation.setter
    def minimum_outlet_air_temperature_during_cooling_operation(self, value=8.0 ):
        """  Corresponds to IDD Field `minimum_outlet_air_temperature_during_cooling_operation`
        Specify the minimum outlet air temperature allowed for this unitary system
        during cooling operation. This value should be less than the maximum outlet
        air temperature during heating operation.

        Args:
            value (float): value for IDD Field `minimum_outlet_air_temperature_during_cooling_operation`
                Unit: C
                Default value: 8.0
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
                                 'for field `minimum_outlet_air_temperature_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_outlet_air_temperature_during_cooling_operation`')

        self._data["Minimum Outlet Air Temperature During Cooling Operation"] = value

    @property
    def maximum_outlet_air_temperature_during_heating_operation(self):
        """Get maximum_outlet_air_temperature_during_heating_operation

        Returns:
            float: the value of `maximum_outlet_air_temperature_during_heating_operation` or None if not set
        """
        return self._data["Maximum Outlet Air Temperature During Heating Operation"]

    @maximum_outlet_air_temperature_during_heating_operation.setter
    def maximum_outlet_air_temperature_during_heating_operation(self, value=50.0 ):
        """  Corresponds to IDD Field `maximum_outlet_air_temperature_during_heating_operation`
        Specify the maximum outlet air temperature allowed for this unitary system
        during heating operation. This value should be greater than the minimum outlet
        air temperature during cooling operation.

        Args:
            value (float): value for IDD Field `maximum_outlet_air_temperature_during_heating_operation`
                Unit: C
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_outlet_air_temperature_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_outlet_air_temperature_during_heating_operation`')

        self._data["Maximum Outlet Air Temperature During Heating Operation"] = value

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
        None = meet sensible load only.
        Multimode = activate enhanced dehumidification mode
        as needed and meet sensible load.  Valid only with
        Coil:Cooling:DX:TwoStageWithHumidityControlMode.
        CoolReheat = cool beyond the Dry-Bulb temperature setpoint
        as required to meet the humidity setpoint.  Valid only with
        Coil:Cooling:DX:TwoStageWithHumidityControlMode.
        For all dehumidification controls, the max humidity setpoint
        on this unitary system's air outlet node is used.
        This must be set using ZoneControl:Humidistat and
        SetpointManager:SingleZone:Humidity:Maximum,
        SetpointManager:MultiZone:Humidity:Maximum or
        SetpointManager:MultiZone:MaximumHumidity:Average objects.

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
        out.append(self._to_str(self.system_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.system_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.system_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.outdoor_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.outdoor_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.outdoor_air_flow_rate_multiplier_schedule_name))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.bypass_duct_mixer_node_name))
        out.append(self._to_str(self.bypass_duct_splitter_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.outdoor_air_mixer_object_type))
        out.append(self._to_str(self.outdoor_air_mixer_name))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.supply_air_fan_placement))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.priority_control_mode))
        out.append(self._to_str(self.minimum_outlet_air_temperature_during_cooling_operation))
        out.append(self._to_str(self.maximum_outlet_air_temperature_during_heating_operation))
        out.append(self._to_str(self.dehumidification_control_type))
        return ",".join(out)

class AirLoopHvacUnitaryHeatPumpAirToAirMultiSpeed(object):
    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed`
        Unitary system, heating and cooling, multi-speed with constant volume supply fan
        (continuous or cycling), direct expansion (DX) cooling coil, heating coil
        (DX air-to-air heat pump, gas, electric, hot water, or steam), and supplemental
        heating coil (gas, electric, hot water, or steam).
    """
    internal_name = "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed"
    field_count = 35

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Controlling Zone or Thermostat Location"] = None
        self._data["Supply Air Fan Object Type"] = None
        self._data["Supply Air Fan Name"] = None
        self._data["Supply Air Fan Placement"] = None
        self._data["Supply Air Fan Operating Mode Schedule Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Minimum Outdoor Dry-Bulb Temperature for Compressor Operation"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Supplemental Heating Coil Object Type"] = None
        self._data["Supplemental Heating Coil Name"] = None
        self._data["Maximum Supply Air Temperature from Supplemental Heater"] = None
        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = None
        self._data["Auxiliary On-Cycle Electric Power"] = None
        self._data["Auxiliary Off-Cycle Electric Power"] = None
        self._data["Design Heat Recovery Water Flow Rate"] = None
        self._data["Maximum Temperature for Heat Recovery"] = None
        self._data["Heat Recovery Water Inlet Node Name"] = None
        self._data["Heat Recovery Water Outlet Node Name"] = None
        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = None
        self._data["Number of Speeds for Heating"] = None
        self._data["Number of Speeds for Cooling"] = None
        self._data["Speed 1 Supply Air Flow Rate During Heating Operation"] = None
        self._data["Speed 2 Supply Air Flow Rate During Heating Operation"] = None
        self._data["Speed 3 Supply Air Flow Rate During Heating Operation"] = None
        self._data["Speed 4 Supply Air Flow Rate During Heating Operation"] = None
        self._data["Speed 1 Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Speed 2 Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Speed 3 Supply Air Flow Rate During Cooling Operation"] = None
        self._data["Speed 4 Supply Air Flow Rate During Cooling Operation"] = None

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
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.controlling_zone_or_thermostat_location = None
        else:
            self.controlling_zone_or_thermostat_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_object_type = None
        else:
            self.supply_air_fan_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_name = None
        else:
            self.supply_air_fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_placement = None
        else:
            self.supply_air_fan_placement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_fan_operating_mode_schedule_name = None
        else:
            self.supply_air_fan_operating_mode_schedule_name = vals[i]
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
        if len(vals[i]) == 0:
            self.minimum_outdoor_drybulb_temperature_for_compressor_operation = None
        else:
            self.minimum_outdoor_drybulb_temperature_for_compressor_operation = vals[i]
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
            self.supplemental_heating_coil_object_type = None
        else:
            self.supplemental_heating_coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supplemental_heating_coil_name = None
        else:
            self.supplemental_heating_coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_supply_air_temperature_from_supplemental_heater = None
        else:
            self.maximum_supply_air_temperature_from_supplemental_heater = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = None
        else:
            self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.auxiliary_oncycle_electric_power = None
        else:
            self.auxiliary_oncycle_electric_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.auxiliary_offcycle_electric_power = None
        else:
            self.auxiliary_offcycle_electric_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_heat_recovery_water_flow_rate = None
        else:
            self.design_heat_recovery_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_temperature_for_heat_recovery = None
        else:
            self.maximum_temperature_for_heat_recovery = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_water_inlet_node_name = None
        else:
            self.heat_recovery_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_recovery_water_outlet_node_name = None
        else:
            self.heat_recovery_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_speeds_for_heating = None
        else:
            self.number_of_speeds_for_heating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_speeds_for_cooling = None
        else:
            self.number_of_speeds_for_cooling = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_1_supply_air_flow_rate_during_heating_operation = None
        else:
            self.speed_1_supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_2_supply_air_flow_rate_during_heating_operation = None
        else:
            self.speed_2_supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_3_supply_air_flow_rate_during_heating_operation = None
        else:
            self.speed_3_supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_4_supply_air_flow_rate_during_heating_operation = None
        else:
            self.speed_4_supply_air_flow_rate_during_heating_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_1_supply_air_flow_rate_during_cooling_operation = None
        else:
            self.speed_1_supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_2_supply_air_flow_rate_during_cooling_operation = None
        else:
            self.speed_2_supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_3_supply_air_flow_rate_during_cooling_operation = None
        else:
            self.speed_3_supply_air_flow_rate_during_cooling_operation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.speed_4_supply_air_flow_rate_during_cooling_operation = None
        else:
            self.speed_4_supply_air_flow_rate_during_cooling_operation = vals[i]
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
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_inlet_node_name`

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')

        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_outlet_node_name`

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')

        self._data["Air Outlet Node Name"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """Get controlling_zone_or_thermostat_location

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set
        """
        return self._data["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """  Corresponds to IDD Field `controlling_zone_or_thermostat_location`

        Args:
            value (str): value for IDD Field `controlling_zone_or_thermostat_location`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controlling_zone_or_thermostat_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controlling_zone_or_thermostat_location`')

        self._data["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_air_fan_object_type(self):
        """Get supply_air_fan_object_type

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set
        """
        return self._data["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_object_type`
        Select the type of supply air fan used in this unitary system.

        Args:
            value (str): value for IDD Field `supply_air_fan_object_type`
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
                                 'for field `supply_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_object_type`'.format(value))

        self._data["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """Get supply_air_fan_name

        Returns:
            str: the value of `supply_air_fan_name` or None if not set
        """
        return self._data["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_name`
        Enter the name of the supply air fan used in this unitary system.

        Args:
            value (str): value for IDD Field `supply_air_fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_name`')

        self._data["Supply Air Fan Name"] = value

    @property
    def supply_air_fan_placement(self):
        """Get supply_air_fan_placement

        Returns:
            str: the value of `supply_air_fan_placement` or None if not set
        """
        return self._data["Supply Air Fan Placement"]

    @supply_air_fan_placement.setter
    def supply_air_fan_placement(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_placement`
        Select supply air fan placement as either BlowThrough or DrawThrough.
        BlowThrough means the supply air fan is located before the cooling
        coil. DrawThrough means the supply air fan is located after the heating coil
        but before the optional supplemental heating coil.

        Args:
            value (str): value for IDD Field `supply_air_fan_placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_placement`')
            vals = set()
            vals.add("BlowThrough")
            vals.add("DrawThrough")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_fan_placement`'.format(value))

        self._data["Supply Air Fan Placement"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """Get supply_air_fan_operating_mode_schedule_name

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set
        """
        return self._data["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_fan_operating_mode_schedule_name`
        Enter the name of a schedule to control the supply air fan. Schedule values of zero
        mean that the supply air fan will cycle off if there is no cooling or heating load
        in the control zone. Non-zero schedule values mean that the supply air fan
        will operate continuously even if there is no cooling or heating load
        in the control zone. If this field is left blank, the supply air fan will
        operate continuously for the entire simulation period.

        Args:
            value (str): value for IDD Field `supply_air_fan_operating_mode_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_fan_operating_mode_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_fan_operating_mode_schedule_name`')

        self._data["Supply Air Fan Operating Mode Schedule Name"] = value

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
        Multi Speed DX, Electric, Gas, and Single speed Water and Steam coils

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:DX:MultiSpeed
                      - Coil:Heating:Electric:MultiStage
                      - Coil:Heating:Gas:MultiStage
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
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:DX:MultiSpeed")
            vals.add("Coil:Heating:Electric:MultiStage")
            vals.add("Coil:Heating:Gas:MultiStage")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
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

    @property
    def minimum_outdoor_drybulb_temperature_for_compressor_operation(self):
        """Get minimum_outdoor_drybulb_temperature_for_compressor_operation

        Returns:
            float: the value of `minimum_outdoor_drybulb_temperature_for_compressor_operation` or None if not set
        """
        return self._data["Minimum Outdoor Dry-Bulb Temperature for Compressor Operation"]

    @minimum_outdoor_drybulb_temperature_for_compressor_operation.setter
    def minimum_outdoor_drybulb_temperature_for_compressor_operation(self, value=-8.0 ):
        """  Corresponds to IDD Field `minimum_outdoor_drybulb_temperature_for_compressor_operation`
        Needs to match the corresponding minimum outdoor temperature defined
        in the DX heating coil object.

        Args:
            value (float): value for IDD Field `minimum_outdoor_drybulb_temperature_for_compressor_operation`
                Unit: C
                Default value: -8.0
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
                                 'for field `minimum_outdoor_drybulb_temperature_for_compressor_operation`'.format(value))

        self._data["Minimum Outdoor Dry-Bulb Temperature for Compressor Operation"] = value

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
        Only works with Coil:Cooling:DX:MultiSpeed

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
                Accepted values are:
                      - Coil:Cooling:DX:MultiSpeed
                if `value` is None it will not be checked against the
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
            vals.add("Coil:Cooling:DX:MultiSpeed")
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
        Needs to match in the DX Cooling Coil object

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
    def supplemental_heating_coil_object_type(self):
        """Get supplemental_heating_coil_object_type

        Returns:
            str: the value of `supplemental_heating_coil_object_type` or None if not set
        """
        return self._data["Supplemental Heating Coil Object Type"]

    @supplemental_heating_coil_object_type.setter
    def supplemental_heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `supplemental_heating_coil_object_type`
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_object_type`
                Accepted values are:
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
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
                                 'for field `supplemental_heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_object_type`')
            vals = set()
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Heating:Steam")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supplemental_heating_coil_object_type`'.format(value))

        self._data["Supplemental Heating Coil Object Type"] = value

    @property
    def supplemental_heating_coil_name(self):
        """Get supplemental_heating_coil_name

        Returns:
            str: the value of `supplemental_heating_coil_name` or None if not set
        """
        return self._data["Supplemental Heating Coil Name"]

    @supplemental_heating_coil_name.setter
    def supplemental_heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `supplemental_heating_coil_name`
        Needs to match in the supplemental heating coil object

        Args:
            value (str): value for IDD Field `supplemental_heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supplemental_heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supplemental_heating_coil_name`')

        self._data["Supplemental Heating Coil Name"] = value

    @property
    def maximum_supply_air_temperature_from_supplemental_heater(self):
        """Get maximum_supply_air_temperature_from_supplemental_heater

        Returns:
            float: the value of `maximum_supply_air_temperature_from_supplemental_heater` or None if not set
        """
        return self._data["Maximum Supply Air Temperature from Supplemental Heater"]

    @maximum_supply_air_temperature_from_supplemental_heater.setter
    def maximum_supply_air_temperature_from_supplemental_heater(self, value=None):
        """  Corresponds to IDD Field `maximum_supply_air_temperature_from_supplemental_heater`

        Args:
            value (float): value for IDD Field `maximum_supply_air_temperature_from_supplemental_heater`
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
                                 'for field `maximum_supply_air_temperature_from_supplemental_heater`'.format(value))

        self._data["Maximum Supply Air Temperature from Supplemental Heater"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self):
        """Get maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation` or None if not set
        """
        return self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"]

    @maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation.setter
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(self, value=21.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`

        Args:
            value (float): value for IDD Field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`
                Unit: C
                Default value: 21.0
                value <= 21.0
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
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`'.format(value))
            if value > 21.0:
                raise ValueError('value need to be smaller 21.0 '
                                 'for field `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation`')

        self._data["Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = value

    @property
    def auxiliary_oncycle_electric_power(self):
        """Get auxiliary_oncycle_electric_power

        Returns:
            float: the value of `auxiliary_oncycle_electric_power` or None if not set
        """
        return self._data["Auxiliary On-Cycle Electric Power"]

    @auxiliary_oncycle_electric_power.setter
    def auxiliary_oncycle_electric_power(self, value=0.0 ):
        """  Corresponds to IDD Field `auxiliary_oncycle_electric_power`

        Args:
            value (float): value for IDD Field `auxiliary_oncycle_electric_power`
                Unit: W
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `auxiliary_oncycle_electric_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `auxiliary_oncycle_electric_power`')

        self._data["Auxiliary On-Cycle Electric Power"] = value

    @property
    def auxiliary_offcycle_electric_power(self):
        """Get auxiliary_offcycle_electric_power

        Returns:
            float: the value of `auxiliary_offcycle_electric_power` or None if not set
        """
        return self._data["Auxiliary Off-Cycle Electric Power"]

    @auxiliary_offcycle_electric_power.setter
    def auxiliary_offcycle_electric_power(self, value=0.0 ):
        """  Corresponds to IDD Field `auxiliary_offcycle_electric_power`

        Args:
            value (float): value for IDD Field `auxiliary_offcycle_electric_power`
                Unit: W
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `auxiliary_offcycle_electric_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `auxiliary_offcycle_electric_power`')

        self._data["Auxiliary Off-Cycle Electric Power"] = value

    @property
    def design_heat_recovery_water_flow_rate(self):
        """Get design_heat_recovery_water_flow_rate

        Returns:
            float: the value of `design_heat_recovery_water_flow_rate` or None if not set
        """
        return self._data["Design Heat Recovery Water Flow Rate"]

    @design_heat_recovery_water_flow_rate.setter
    def design_heat_recovery_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `design_heat_recovery_water_flow_rate`
        If non-zero, then the heat recovery inlet and outlet node names must be entered.
        Used for heat recovery to an EnergyPlus plant loop.

        Args:
            value (float): value for IDD Field `design_heat_recovery_water_flow_rate`
                Unit: m3/s
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_heat_recovery_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_heat_recovery_water_flow_rate`')

        self._data["Design Heat Recovery Water Flow Rate"] = value

    @property
    def maximum_temperature_for_heat_recovery(self):
        """Get maximum_temperature_for_heat_recovery

        Returns:
            float: the value of `maximum_temperature_for_heat_recovery` or None if not set
        """
        return self._data["Maximum Temperature for Heat Recovery"]

    @maximum_temperature_for_heat_recovery.setter
    def maximum_temperature_for_heat_recovery(self, value=80.0 ):
        """  Corresponds to IDD Field `maximum_temperature_for_heat_recovery`

        Args:
            value (float): value for IDD Field `maximum_temperature_for_heat_recovery`
                Unit: C
                Default value: 80.0
                value >= 0.0
                value <= 100.0
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
                                 'for field `maximum_temperature_for_heat_recovery`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_temperature_for_heat_recovery`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_temperature_for_heat_recovery`')

        self._data["Maximum Temperature for Heat Recovery"] = value

    @property
    def heat_recovery_water_inlet_node_name(self):
        """Get heat_recovery_water_inlet_node_name

        Returns:
            str: the value of `heat_recovery_water_inlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Water Inlet Node Name"]

    @heat_recovery_water_inlet_node_name.setter
    def heat_recovery_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_water_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_recovery_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_water_inlet_node_name`')

        self._data["Heat Recovery Water Inlet Node Name"] = value

    @property
    def heat_recovery_water_outlet_node_name(self):
        """Get heat_recovery_water_outlet_node_name

        Returns:
            str: the value of `heat_recovery_water_outlet_node_name` or None if not set
        """
        return self._data["Heat Recovery Water Outlet Node Name"]

    @heat_recovery_water_outlet_node_name.setter
    def heat_recovery_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `heat_recovery_water_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_recovery_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_water_outlet_node_name`')

        self._data["Heat Recovery Water Outlet Node Name"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """Get supply_air_flow_rate_when_no_cooling_or_heating_is_needed

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
        Only used when the supply air fan operating mode is continuous (see field
        Supply Air Fan Operating Mode Schedule Name). This air flow rate
        is used when no heating or cooling is required and the coils are off.
        If this field is left blank or zero, the supply air flow rate from the
        previous on cycle (either cooling or heating) is used.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`
                Unit: m3/s
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
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_needed`')

        self._data["Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def number_of_speeds_for_heating(self):
        """Get number_of_speeds_for_heating

        Returns:
            int: the value of `number_of_speeds_for_heating` or None if not set
        """
        return self._data["Number of Speeds for Heating"]

    @number_of_speeds_for_heating.setter
    def number_of_speeds_for_heating(self, value=None):
        """  Corresponds to IDD Field `number_of_speeds_for_heating`
        Enter the number of the following sets of data for air flow rates.
        If Heating Coil Object Type is Coil:Heating:Water or Coil:Heating:Steam,
        this field should be 1.

        Args:
            value (int): value for IDD Field `number_of_speeds_for_heating`
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
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_speeds_for_heating`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_speeds_for_heating`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `number_of_speeds_for_heating`')

        self._data["Number of Speeds for Heating"] = value

    @property
    def number_of_speeds_for_cooling(self):
        """Get number_of_speeds_for_cooling

        Returns:
            int: the value of `number_of_speeds_for_cooling` or None if not set
        """
        return self._data["Number of Speeds for Cooling"]

    @number_of_speeds_for_cooling.setter
    def number_of_speeds_for_cooling(self, value=None):
        """  Corresponds to IDD Field `number_of_speeds_for_cooling`
        Enter the number of the following sets of data for air flow rates.

        Args:
            value (int): value for IDD Field `number_of_speeds_for_cooling`
                value >= 2
                value <= 4
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_speeds_for_cooling`'.format(value))
            if value < 2:
                raise ValueError('value need to be greater or equal 2 '
                                 'for field `number_of_speeds_for_cooling`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `number_of_speeds_for_cooling`')

        self._data["Number of Speeds for Cooling"] = value

    @property
    def speed_1_supply_air_flow_rate_during_heating_operation(self):
        """Get speed_1_supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `speed_1_supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Speed 1 Supply Air Flow Rate During Heating Operation"]

    @speed_1_supply_air_flow_rate_during_heating_operation.setter
    def speed_1_supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_1_supply_air_flow_rate_during_heating_operation`
        Enter the operating supply air flow rate during heating
        operation or specify autosize.

        Args:
            value (float): value for IDD Field `speed_1_supply_air_flow_rate_during_heating_operation`
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
                                 'for field `speed_1_supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_1_supply_air_flow_rate_during_heating_operation`')

        self._data["Speed 1 Supply Air Flow Rate During Heating Operation"] = value

    @property
    def speed_2_supply_air_flow_rate_during_heating_operation(self):
        """Get speed_2_supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `speed_2_supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Speed 2 Supply Air Flow Rate During Heating Operation"]

    @speed_2_supply_air_flow_rate_during_heating_operation.setter
    def speed_2_supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_2_supply_air_flow_rate_during_heating_operation`
        Enter the operating supply air flow rate during heating
        operation or specify autosize.

        Args:
            value (float): value for IDD Field `speed_2_supply_air_flow_rate_during_heating_operation`
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
                                 'for field `speed_2_supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_2_supply_air_flow_rate_during_heating_operation`')

        self._data["Speed 2 Supply Air Flow Rate During Heating Operation"] = value

    @property
    def speed_3_supply_air_flow_rate_during_heating_operation(self):
        """Get speed_3_supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `speed_3_supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Speed 3 Supply Air Flow Rate During Heating Operation"]

    @speed_3_supply_air_flow_rate_during_heating_operation.setter
    def speed_3_supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_3_supply_air_flow_rate_during_heating_operation`
        Enter the operating supply air flow rate during heating
        operation or specify autosize.

        Args:
            value (float): value for IDD Field `speed_3_supply_air_flow_rate_during_heating_operation`
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
                                 'for field `speed_3_supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_3_supply_air_flow_rate_during_heating_operation`')

        self._data["Speed 3 Supply Air Flow Rate During Heating Operation"] = value

    @property
    def speed_4_supply_air_flow_rate_during_heating_operation(self):
        """Get speed_4_supply_air_flow_rate_during_heating_operation

        Returns:
            float: the value of `speed_4_supply_air_flow_rate_during_heating_operation` or None if not set
        """
        return self._data["Speed 4 Supply Air Flow Rate During Heating Operation"]

    @speed_4_supply_air_flow_rate_during_heating_operation.setter
    def speed_4_supply_air_flow_rate_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `speed_4_supply_air_flow_rate_during_heating_operation`
        Enter the operating supply air flow rate during heating
        operation or specify autosize.

        Args:
            value (float): value for IDD Field `speed_4_supply_air_flow_rate_during_heating_operation`
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
                                 'for field `speed_4_supply_air_flow_rate_during_heating_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_4_supply_air_flow_rate_during_heating_operation`')

        self._data["Speed 4 Supply Air Flow Rate During Heating Operation"] = value

    @property
    def speed_1_supply_air_flow_rate_during_cooling_operation(self):
        """Get speed_1_supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `speed_1_supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Speed 1 Supply Air Flow Rate During Cooling Operation"]

    @speed_1_supply_air_flow_rate_during_cooling_operation.setter
    def speed_1_supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_1_supply_air_flow_rate_during_cooling_operation`
        Enter the operating supply air flow rate during cooling
        operation or specify autosize.

        Args:
            value (float): value for IDD Field `speed_1_supply_air_flow_rate_during_cooling_operation`
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
                                 'for field `speed_1_supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_1_supply_air_flow_rate_during_cooling_operation`')

        self._data["Speed 1 Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def speed_2_supply_air_flow_rate_during_cooling_operation(self):
        """Get speed_2_supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `speed_2_supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Speed 2 Supply Air Flow Rate During Cooling Operation"]

    @speed_2_supply_air_flow_rate_during_cooling_operation.setter
    def speed_2_supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_2_supply_air_flow_rate_during_cooling_operation`
        Enter the operating supply air flow rate during cooling
        operation or specify autosize.

        Args:
            value (float): value for IDD Field `speed_2_supply_air_flow_rate_during_cooling_operation`
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
                                 'for field `speed_2_supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_2_supply_air_flow_rate_during_cooling_operation`')

        self._data["Speed 2 Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def speed_3_supply_air_flow_rate_during_cooling_operation(self):
        """Get speed_3_supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `speed_3_supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Speed 3 Supply Air Flow Rate During Cooling Operation"]

    @speed_3_supply_air_flow_rate_during_cooling_operation.setter
    def speed_3_supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_3_supply_air_flow_rate_during_cooling_operation`
        Enter the operating supply air flow rate during cooling
        operation or specify autosize.

        Args:
            value (float): value for IDD Field `speed_3_supply_air_flow_rate_during_cooling_operation`
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
                                 'for field `speed_3_supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_3_supply_air_flow_rate_during_cooling_operation`')

        self._data["Speed 3 Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def speed_4_supply_air_flow_rate_during_cooling_operation(self):
        """Get speed_4_supply_air_flow_rate_during_cooling_operation

        Returns:
            float: the value of `speed_4_supply_air_flow_rate_during_cooling_operation` or None if not set
        """
        return self._data["Speed 4 Supply Air Flow Rate During Cooling Operation"]

    @speed_4_supply_air_flow_rate_during_cooling_operation.setter
    def speed_4_supply_air_flow_rate_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `speed_4_supply_air_flow_rate_during_cooling_operation`
        Enter the operating supply air flow rate during cooling
        operation or specify autosize.

        Args:
            value (float): value for IDD Field `speed_4_supply_air_flow_rate_during_cooling_operation`
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
                                 'for field `speed_4_supply_air_flow_rate_during_cooling_operation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `speed_4_supply_air_flow_rate_during_cooling_operation`')

        self._data["Speed 4 Supply Air Flow Rate During Cooling Operation"] = value

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
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.controlling_zone_or_thermostat_location))
        out.append(self._to_str(self.supply_air_fan_object_type))
        out.append(self._to_str(self.supply_air_fan_name))
        out.append(self._to_str(self.supply_air_fan_placement))
        out.append(self._to_str(self.supply_air_fan_operating_mode_schedule_name))
        out.append(self._to_str(self.heating_coil_object_type))
        out.append(self._to_str(self.heating_coil_name))
        out.append(self._to_str(self.minimum_outdoor_drybulb_temperature_for_compressor_operation))
        out.append(self._to_str(self.cooling_coil_object_type))
        out.append(self._to_str(self.cooling_coil_name))
        out.append(self._to_str(self.supplemental_heating_coil_object_type))
        out.append(self._to_str(self.supplemental_heating_coil_name))
        out.append(self._to_str(self.maximum_supply_air_temperature_from_supplemental_heater))
        out.append(self._to_str(self.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation))
        out.append(self._to_str(self.auxiliary_oncycle_electric_power))
        out.append(self._to_str(self.auxiliary_offcycle_electric_power))
        out.append(self._to_str(self.design_heat_recovery_water_flow_rate))
        out.append(self._to_str(self.maximum_temperature_for_heat_recovery))
        out.append(self._to_str(self.heat_recovery_water_inlet_node_name))
        out.append(self._to_str(self.heat_recovery_water_outlet_node_name))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_cooling_or_heating_is_needed))
        out.append(self._to_str(self.number_of_speeds_for_heating))
        out.append(self._to_str(self.number_of_speeds_for_cooling))
        out.append(self._to_str(self.speed_1_supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.speed_2_supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.speed_3_supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.speed_4_supply_air_flow_rate_during_heating_operation))
        out.append(self._to_str(self.speed_1_supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.speed_2_supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.speed_3_supply_air_flow_rate_during_cooling_operation))
        out.append(self._to_str(self.speed_4_supply_air_flow_rate_during_cooling_operation))
        return ",".join(out)