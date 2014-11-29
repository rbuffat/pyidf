from collections import OrderedDict

class HeatExchangerAirToAirFlatPlate(object):
    """ Corresponds to IDD object `HeatExchanger:AirToAir:FlatPlate`
        Flat plate air-to-air heat exchanger, typically used for exhaust or relief air heat
        recovery.
    """
    internal_name = "HeatExchanger:AirToAir:FlatPlate"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatExchanger:AirToAir:FlatPlate`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Flow Arrangement Type"] = None
        self._data["Economizer Lockout"] = None
        self._data["Ratio of Supply to Secondary hA Values"] = None
        self._data["Nominal Supply Air Flow Rate"] = None
        self._data["Nominal Supply Air Inlet Temperature"] = None
        self._data["Nominal Supply Air Outlet Temperature"] = None
        self._data["Nominal Secondary Air Flow Rate"] = None
        self._data["Nominal Secondary Air Inlet Temperature"] = None
        self._data["Nominal Electric Power"] = None
        self._data["Supply Air Inlet Node Name"] = None
        self._data["Supply Air Outlet Node Name"] = None
        self._data["Secondary Air Inlet Node Name"] = None
        self._data["Secondary Air Outlet Node Name"] = None

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
            self.flow_arrangement_type = None
        else:
            self.flow_arrangement_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.economizer_lockout = None
        else:
            self.economizer_lockout = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ratio_of_supply_to_secondary_ha_values = None
        else:
            self.ratio_of_supply_to_secondary_ha_values = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_supply_air_flow_rate = None
        else:
            self.nominal_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_supply_air_inlet_temperature = None
        else:
            self.nominal_supply_air_inlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_supply_air_outlet_temperature = None
        else:
            self.nominal_supply_air_outlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_secondary_air_flow_rate = None
        else:
            self.nominal_secondary_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_secondary_air_inlet_temperature = None
        else:
            self.nominal_secondary_air_inlet_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_electric_power = None
        else:
            self.nominal_electric_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_inlet_node_name = None
        else:
            self.supply_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_outlet_node_name = None
        else:
            self.supply_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_air_inlet_node_name = None
        else:
            self.secondary_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_air_outlet_node_name = None
        else:
            self.secondary_air_outlet_node_name = vals[i]
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
    def flow_arrangement_type(self):
        """Get flow_arrangement_type

        Returns:
            str: the value of `flow_arrangement_type` or None if not set
        """
        return self._data["Flow Arrangement Type"]

    @flow_arrangement_type.setter
    def flow_arrangement_type(self, value=None):
        """  Corresponds to IDD Field `flow_arrangement_type`

        Args:
            value (str): value for IDD Field `flow_arrangement_type`
                Accepted values are:
                      - CounterFlow
                      - ParallelFlow
                      - CrossFlowBothUnmixed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `flow_arrangement_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `flow_arrangement_type`')
            vals = set()
            vals.add("CounterFlow")
            vals.add("ParallelFlow")
            vals.add("CrossFlowBothUnmixed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `flow_arrangement_type`'.format(value))

        self._data["Flow Arrangement Type"] = value

    @property
    def economizer_lockout(self):
        """Get economizer_lockout

        Returns:
            str: the value of `economizer_lockout` or None if not set
        """
        return self._data["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="Yes"):
        """  Corresponds to IDD Field `economizer_lockout`
        Yes means that the heat exchanger will be locked out (off)
        when the economizer is operating or high humidity control is active

        Args:
            value (str): value for IDD Field `economizer_lockout`
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
                                 'for field `economizer_lockout`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `economizer_lockout`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `economizer_lockout`'.format(value))

        self._data["Economizer Lockout"] = value

    @property
    def ratio_of_supply_to_secondary_ha_values(self):
        """Get ratio_of_supply_to_secondary_ha_values

        Returns:
            float: the value of `ratio_of_supply_to_secondary_ha_values` or None if not set
        """
        return self._data["Ratio of Supply to Secondary hA Values"]

    @ratio_of_supply_to_secondary_ha_values.setter
    def ratio_of_supply_to_secondary_ha_values(self, value=None):
        """  Corresponds to IDD Field `ratio_of_supply_to_secondary_ha_values`
        Ratio of h*A for supply side to h*A for exhaust side

        Args:
            value (float): value for IDD Field `ratio_of_supply_to_secondary_ha_values`
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
                                 'for field `ratio_of_supply_to_secondary_ha_values`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ratio_of_supply_to_secondary_ha_values`')

        self._data["Ratio of Supply to Secondary hA Values"] = value

    @property
    def nominal_supply_air_flow_rate(self):
        """Get nominal_supply_air_flow_rate

        Returns:
            float: the value of `nominal_supply_air_flow_rate` or None if not set
        """
        return self._data["Nominal Supply Air Flow Rate"]

    @nominal_supply_air_flow_rate.setter
    def nominal_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `nominal_supply_air_flow_rate`

        Args:
            value (float): value for IDD Field `nominal_supply_air_flow_rate`
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
                                 'for field `nominal_supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_supply_air_flow_rate`')

        self._data["Nominal Supply Air Flow Rate"] = value

    @property
    def nominal_supply_air_inlet_temperature(self):
        """Get nominal_supply_air_inlet_temperature

        Returns:
            float: the value of `nominal_supply_air_inlet_temperature` or None if not set
        """
        return self._data["Nominal Supply Air Inlet Temperature"]

    @nominal_supply_air_inlet_temperature.setter
    def nominal_supply_air_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `nominal_supply_air_inlet_temperature`

        Args:
            value (float): value for IDD Field `nominal_supply_air_inlet_temperature`
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
                                 'for field `nominal_supply_air_inlet_temperature`'.format(value))

        self._data["Nominal Supply Air Inlet Temperature"] = value

    @property
    def nominal_supply_air_outlet_temperature(self):
        """Get nominal_supply_air_outlet_temperature

        Returns:
            float: the value of `nominal_supply_air_outlet_temperature` or None if not set
        """
        return self._data["Nominal Supply Air Outlet Temperature"]

    @nominal_supply_air_outlet_temperature.setter
    def nominal_supply_air_outlet_temperature(self, value=None):
        """  Corresponds to IDD Field `nominal_supply_air_outlet_temperature`

        Args:
            value (float): value for IDD Field `nominal_supply_air_outlet_temperature`
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
                                 'for field `nominal_supply_air_outlet_temperature`'.format(value))

        self._data["Nominal Supply Air Outlet Temperature"] = value

    @property
    def nominal_secondary_air_flow_rate(self):
        """Get nominal_secondary_air_flow_rate

        Returns:
            float: the value of `nominal_secondary_air_flow_rate` or None if not set
        """
        return self._data["Nominal Secondary Air Flow Rate"]

    @nominal_secondary_air_flow_rate.setter
    def nominal_secondary_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `nominal_secondary_air_flow_rate`

        Args:
            value (float): value for IDD Field `nominal_secondary_air_flow_rate`
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
                                 'for field `nominal_secondary_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_secondary_air_flow_rate`')

        self._data["Nominal Secondary Air Flow Rate"] = value

    @property
    def nominal_secondary_air_inlet_temperature(self):
        """Get nominal_secondary_air_inlet_temperature

        Returns:
            float: the value of `nominal_secondary_air_inlet_temperature` or None if not set
        """
        return self._data["Nominal Secondary Air Inlet Temperature"]

    @nominal_secondary_air_inlet_temperature.setter
    def nominal_secondary_air_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `nominal_secondary_air_inlet_temperature`

        Args:
            value (float): value for IDD Field `nominal_secondary_air_inlet_temperature`
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
                                 'for field `nominal_secondary_air_inlet_temperature`'.format(value))

        self._data["Nominal Secondary Air Inlet Temperature"] = value

    @property
    def nominal_electric_power(self):
        """Get nominal_electric_power

        Returns:
            float: the value of `nominal_electric_power` or None if not set
        """
        return self._data["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=None):
        """  Corresponds to IDD Field `nominal_electric_power`

        Args:
            value (float): value for IDD Field `nominal_electric_power`
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
                                 'for field `nominal_electric_power`'.format(value))

        self._data["Nominal Electric Power"] = value

    @property
    def supply_air_inlet_node_name(self):
        """Get supply_air_inlet_node_name

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `supply_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_inlet_node_name`')

        self._data["Supply Air Inlet Node Name"] = value

    @property
    def supply_air_outlet_node_name(self):
        """Get supply_air_outlet_node_name

        Returns:
            str: the value of `supply_air_outlet_node_name` or None if not set
        """
        return self._data["Supply Air Outlet Node Name"]

    @supply_air_outlet_node_name.setter
    def supply_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `supply_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_outlet_node_name`')

        self._data["Supply Air Outlet Node Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """Get secondary_air_inlet_node_name

        Returns:
            str: the value of `secondary_air_inlet_node_name` or None if not set
        """
        return self._data["Secondary Air Inlet Node Name"]

    @secondary_air_inlet_node_name.setter
    def secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `secondary_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `secondary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `secondary_air_inlet_node_name`')

        self._data["Secondary Air Inlet Node Name"] = value

    @property
    def secondary_air_outlet_node_name(self):
        """Get secondary_air_outlet_node_name

        Returns:
            str: the value of `secondary_air_outlet_node_name` or None if not set
        """
        return self._data["Secondary Air Outlet Node Name"]

    @secondary_air_outlet_node_name.setter
    def secondary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `secondary_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `secondary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `secondary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `secondary_air_outlet_node_name`')

        self._data["Secondary Air Outlet Node Name"] = value

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
        out.append(self._to_str(self.flow_arrangement_type))
        out.append(self._to_str(self.economizer_lockout))
        out.append(self._to_str(self.ratio_of_supply_to_secondary_ha_values))
        out.append(self._to_str(self.nominal_supply_air_flow_rate))
        out.append(self._to_str(self.nominal_supply_air_inlet_temperature))
        out.append(self._to_str(self.nominal_supply_air_outlet_temperature))
        out.append(self._to_str(self.nominal_secondary_air_flow_rate))
        out.append(self._to_str(self.nominal_secondary_air_inlet_temperature))
        out.append(self._to_str(self.nominal_electric_power))
        out.append(self._to_str(self.supply_air_inlet_node_name))
        out.append(self._to_str(self.supply_air_outlet_node_name))
        out.append(self._to_str(self.secondary_air_inlet_node_name))
        out.append(self._to_str(self.secondary_air_outlet_node_name))
        return ",".join(out)

class HeatExchangerAirToAirSensibleAndLatent(object):
    """ Corresponds to IDD object `HeatExchanger:AirToAir:SensibleAndLatent`
        This object models an air-to-air heat exchanger using effectiveness relationships.
        The heat exchanger can transfer sensible energy, latent energy, or both between the
        supply (primary) and exhaust (secondary) air streams.
    """
    internal_name = "HeatExchanger:AirToAir:SensibleAndLatent"
    field_count = 23

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatExchanger:AirToAir:SensibleAndLatent`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Nominal Supply Air Flow Rate"] = None
        self._data["Sensible Effectiveness at 100% Heating Air Flow"] = None
        self._data["Latent Effectiveness at 100% Heating Air Flow"] = None
        self._data["Sensible Effectiveness at 75% Heating Air Flow"] = None
        self._data["Latent Effectiveness at 75% Heating Air Flow"] = None
        self._data["Sensible Effectiveness at 100% Cooling Air Flow"] = None
        self._data["Latent Effectiveness at 100% Cooling Air Flow"] = None
        self._data["Sensible Effectiveness at 75% Cooling Air Flow"] = None
        self._data["Latent Effectiveness at 75% Cooling Air Flow"] = None
        self._data["Supply Air Inlet Node Name"] = None
        self._data["Supply Air Outlet Node Name"] = None
        self._data["Exhaust Air Inlet Node Name"] = None
        self._data["Exhaust Air Outlet Node Name"] = None
        self._data["Nominal Electric Power"] = None
        self._data["Supply Air Outlet Temperature Control"] = None
        self._data["Heat Exchanger Type"] = None
        self._data["Frost Control Type"] = None
        self._data["Threshold Temperature"] = None
        self._data["Initial Defrost Time Fraction"] = None
        self._data["Rate of Defrost Time Fraction Increase"] = None
        self._data["Economizer Lockout"] = None

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
            self.nominal_supply_air_flow_rate = None
        else:
            self.nominal_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sensible_effectiveness_at_100_heating_air_flow = None
        else:
            self.sensible_effectiveness_at_100_heating_air_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.latent_effectiveness_at_100_heating_air_flow = None
        else:
            self.latent_effectiveness_at_100_heating_air_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sensible_effectiveness_at_75_heating_air_flow = None
        else:
            self.sensible_effectiveness_at_75_heating_air_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.latent_effectiveness_at_75_heating_air_flow = None
        else:
            self.latent_effectiveness_at_75_heating_air_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sensible_effectiveness_at_100_cooling_air_flow = None
        else:
            self.sensible_effectiveness_at_100_cooling_air_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.latent_effectiveness_at_100_cooling_air_flow = None
        else:
            self.latent_effectiveness_at_100_cooling_air_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sensible_effectiveness_at_75_cooling_air_flow = None
        else:
            self.sensible_effectiveness_at_75_cooling_air_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.latent_effectiveness_at_75_cooling_air_flow = None
        else:
            self.latent_effectiveness_at_75_cooling_air_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_inlet_node_name = None
        else:
            self.supply_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_outlet_node_name = None
        else:
            self.supply_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_inlet_node_name = None
        else:
            self.exhaust_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_air_outlet_node_name = None
        else:
            self.exhaust_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_electric_power = None
        else:
            self.nominal_electric_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_outlet_temperature_control = None
        else:
            self.supply_air_outlet_temperature_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_exchanger_type = None
        else:
            self.heat_exchanger_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.frost_control_type = None
        else:
            self.frost_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.threshold_temperature = None
        else:
            self.threshold_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_defrost_time_fraction = None
        else:
            self.initial_defrost_time_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rate_of_defrost_time_fraction_increase = None
        else:
            self.rate_of_defrost_time_fraction_increase = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.economizer_lockout = None
        else:
            self.economizer_lockout = vals[i]
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
    def nominal_supply_air_flow_rate(self):
        """Get nominal_supply_air_flow_rate

        Returns:
            float: the value of `nominal_supply_air_flow_rate` or None if not set
        """
        return self._data["Nominal Supply Air Flow Rate"]

    @nominal_supply_air_flow_rate.setter
    def nominal_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `nominal_supply_air_flow_rate`

        Args:
            value (float): value for IDD Field `nominal_supply_air_flow_rate`
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
                                 'for field `nominal_supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_supply_air_flow_rate`')

        self._data["Nominal Supply Air Flow Rate"] = value

    @property
    def sensible_effectiveness_at_100_heating_air_flow(self):
        """Get sensible_effectiveness_at_100_heating_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_100_heating_air_flow` or None if not set
        """
        return self._data["Sensible Effectiveness at 100% Heating Air Flow"]

    @sensible_effectiveness_at_100_heating_air_flow.setter
    def sensible_effectiveness_at_100_heating_air_flow(self, value=0.0 ):
        """  Corresponds to IDD Field `sensible_effectiveness_at_100_heating_air_flow`

        Args:
            value (float): value for IDD Field `sensible_effectiveness_at_100_heating_air_flow`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `sensible_effectiveness_at_100_heating_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `sensible_effectiveness_at_100_heating_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `sensible_effectiveness_at_100_heating_air_flow`')

        self._data["Sensible Effectiveness at 100% Heating Air Flow"] = value

    @property
    def latent_effectiveness_at_100_heating_air_flow(self):
        """Get latent_effectiveness_at_100_heating_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_100_heating_air_flow` or None if not set
        """
        return self._data["Latent Effectiveness at 100% Heating Air Flow"]

    @latent_effectiveness_at_100_heating_air_flow.setter
    def latent_effectiveness_at_100_heating_air_flow(self, value=0.0 ):
        """  Corresponds to IDD Field `latent_effectiveness_at_100_heating_air_flow`

        Args:
            value (float): value for IDD Field `latent_effectiveness_at_100_heating_air_flow`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `latent_effectiveness_at_100_heating_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `latent_effectiveness_at_100_heating_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `latent_effectiveness_at_100_heating_air_flow`')

        self._data["Latent Effectiveness at 100% Heating Air Flow"] = value

    @property
    def sensible_effectiveness_at_75_heating_air_flow(self):
        """Get sensible_effectiveness_at_75_heating_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_75_heating_air_flow` or None if not set
        """
        return self._data["Sensible Effectiveness at 75% Heating Air Flow"]

    @sensible_effectiveness_at_75_heating_air_flow.setter
    def sensible_effectiveness_at_75_heating_air_flow(self, value=0.0 ):
        """  Corresponds to IDD Field `sensible_effectiveness_at_75_heating_air_flow`

        Args:
            value (float): value for IDD Field `sensible_effectiveness_at_75_heating_air_flow`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `sensible_effectiveness_at_75_heating_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `sensible_effectiveness_at_75_heating_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `sensible_effectiveness_at_75_heating_air_flow`')

        self._data["Sensible Effectiveness at 75% Heating Air Flow"] = value

    @property
    def latent_effectiveness_at_75_heating_air_flow(self):
        """Get latent_effectiveness_at_75_heating_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_75_heating_air_flow` or None if not set
        """
        return self._data["Latent Effectiveness at 75% Heating Air Flow"]

    @latent_effectiveness_at_75_heating_air_flow.setter
    def latent_effectiveness_at_75_heating_air_flow(self, value=0.0 ):
        """  Corresponds to IDD Field `latent_effectiveness_at_75_heating_air_flow`

        Args:
            value (float): value for IDD Field `latent_effectiveness_at_75_heating_air_flow`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `latent_effectiveness_at_75_heating_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `latent_effectiveness_at_75_heating_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `latent_effectiveness_at_75_heating_air_flow`')

        self._data["Latent Effectiveness at 75% Heating Air Flow"] = value

    @property
    def sensible_effectiveness_at_100_cooling_air_flow(self):
        """Get sensible_effectiveness_at_100_cooling_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_100_cooling_air_flow` or None if not set
        """
        return self._data["Sensible Effectiveness at 100% Cooling Air Flow"]

    @sensible_effectiveness_at_100_cooling_air_flow.setter
    def sensible_effectiveness_at_100_cooling_air_flow(self, value=0.0 ):
        """  Corresponds to IDD Field `sensible_effectiveness_at_100_cooling_air_flow`

        Args:
            value (float): value for IDD Field `sensible_effectiveness_at_100_cooling_air_flow`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `sensible_effectiveness_at_100_cooling_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `sensible_effectiveness_at_100_cooling_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `sensible_effectiveness_at_100_cooling_air_flow`')

        self._data["Sensible Effectiveness at 100% Cooling Air Flow"] = value

    @property
    def latent_effectiveness_at_100_cooling_air_flow(self):
        """Get latent_effectiveness_at_100_cooling_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_100_cooling_air_flow` or None if not set
        """
        return self._data["Latent Effectiveness at 100% Cooling Air Flow"]

    @latent_effectiveness_at_100_cooling_air_flow.setter
    def latent_effectiveness_at_100_cooling_air_flow(self, value=0.0 ):
        """  Corresponds to IDD Field `latent_effectiveness_at_100_cooling_air_flow`

        Args:
            value (float): value for IDD Field `latent_effectiveness_at_100_cooling_air_flow`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `latent_effectiveness_at_100_cooling_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `latent_effectiveness_at_100_cooling_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `latent_effectiveness_at_100_cooling_air_flow`')

        self._data["Latent Effectiveness at 100% Cooling Air Flow"] = value

    @property
    def sensible_effectiveness_at_75_cooling_air_flow(self):
        """Get sensible_effectiveness_at_75_cooling_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_75_cooling_air_flow` or None if not set
        """
        return self._data["Sensible Effectiveness at 75% Cooling Air Flow"]

    @sensible_effectiveness_at_75_cooling_air_flow.setter
    def sensible_effectiveness_at_75_cooling_air_flow(self, value=0.0 ):
        """  Corresponds to IDD Field `sensible_effectiveness_at_75_cooling_air_flow`

        Args:
            value (float): value for IDD Field `sensible_effectiveness_at_75_cooling_air_flow`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `sensible_effectiveness_at_75_cooling_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `sensible_effectiveness_at_75_cooling_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `sensible_effectiveness_at_75_cooling_air_flow`')

        self._data["Sensible Effectiveness at 75% Cooling Air Flow"] = value

    @property
    def latent_effectiveness_at_75_cooling_air_flow(self):
        """Get latent_effectiveness_at_75_cooling_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_75_cooling_air_flow` or None if not set
        """
        return self._data["Latent Effectiveness at 75% Cooling Air Flow"]

    @latent_effectiveness_at_75_cooling_air_flow.setter
    def latent_effectiveness_at_75_cooling_air_flow(self, value=0.0 ):
        """  Corresponds to IDD Field `latent_effectiveness_at_75_cooling_air_flow`

        Args:
            value (float): value for IDD Field `latent_effectiveness_at_75_cooling_air_flow`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `latent_effectiveness_at_75_cooling_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `latent_effectiveness_at_75_cooling_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `latent_effectiveness_at_75_cooling_air_flow`')

        self._data["Latent Effectiveness at 75% Cooling Air Flow"] = value

    @property
    def supply_air_inlet_node_name(self):
        """Get supply_air_inlet_node_name

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `supply_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_inlet_node_name`')

        self._data["Supply Air Inlet Node Name"] = value

    @property
    def supply_air_outlet_node_name(self):
        """Get supply_air_outlet_node_name

        Returns:
            str: the value of `supply_air_outlet_node_name` or None if not set
        """
        return self._data["Supply Air Outlet Node Name"]

    @supply_air_outlet_node_name.setter
    def supply_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `supply_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_outlet_node_name`')

        self._data["Supply Air Outlet Node Name"] = value

    @property
    def exhaust_air_inlet_node_name(self):
        """Get exhaust_air_inlet_node_name

        Returns:
            str: the value of `exhaust_air_inlet_node_name` or None if not set
        """
        return self._data["Exhaust Air Inlet Node Name"]

    @exhaust_air_inlet_node_name.setter
    def exhaust_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `exhaust_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `exhaust_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_air_inlet_node_name`')

        self._data["Exhaust Air Inlet Node Name"] = value

    @property
    def exhaust_air_outlet_node_name(self):
        """Get exhaust_air_outlet_node_name

        Returns:
            str: the value of `exhaust_air_outlet_node_name` or None if not set
        """
        return self._data["Exhaust Air Outlet Node Name"]

    @exhaust_air_outlet_node_name.setter
    def exhaust_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `exhaust_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `exhaust_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_air_outlet_node_name`')

        self._data["Exhaust Air Outlet Node Name"] = value

    @property
    def nominal_electric_power(self):
        """Get nominal_electric_power

        Returns:
            float: the value of `nominal_electric_power` or None if not set
        """
        return self._data["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=0.0 ):
        """  Corresponds to IDD Field `nominal_electric_power`

        Args:
            value (float): value for IDD Field `nominal_electric_power`
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
                                 'for field `nominal_electric_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_electric_power`')

        self._data["Nominal Electric Power"] = value

    @property
    def supply_air_outlet_temperature_control(self):
        """Get supply_air_outlet_temperature_control

        Returns:
            str: the value of `supply_air_outlet_temperature_control` or None if not set
        """
        return self._data["Supply Air Outlet Temperature Control"]

    @supply_air_outlet_temperature_control.setter
    def supply_air_outlet_temperature_control(self, value="No"):
        """  Corresponds to IDD Field `supply_air_outlet_temperature_control`

        Args:
            value (str): value for IDD Field `supply_air_outlet_temperature_control`
                Accepted values are:
                      - No
                      - Yes
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
                                 'for field `supply_air_outlet_temperature_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_outlet_temperature_control`')
            vals = set()
            vals.add("No")
            vals.add("Yes")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_outlet_temperature_control`'.format(value))

        self._data["Supply Air Outlet Temperature Control"] = value

    @property
    def heat_exchanger_type(self):
        """Get heat_exchanger_type

        Returns:
            str: the value of `heat_exchanger_type` or None if not set
        """
        return self._data["Heat Exchanger Type"]

    @heat_exchanger_type.setter
    def heat_exchanger_type(self, value="Plate"):
        """  Corresponds to IDD Field `heat_exchanger_type`

        Args:
            value (str): value for IDD Field `heat_exchanger_type`
                Accepted values are:
                      - Plate
                      - Rotary
                Default value: Plate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_exchanger_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchanger_type`')
            vals = set()
            vals.add("Plate")
            vals.add("Rotary")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heat_exchanger_type`'.format(value))

        self._data["Heat Exchanger Type"] = value

    @property
    def frost_control_type(self):
        """Get frost_control_type

        Returns:
            str: the value of `frost_control_type` or None if not set
        """
        return self._data["Frost Control Type"]

    @frost_control_type.setter
    def frost_control_type(self, value="None"):
        """  Corresponds to IDD Field `frost_control_type`

        Args:
            value (str): value for IDD Field `frost_control_type`
                Accepted values are:
                      - None
                      - ExhaustAirRecirculation
                      - ExhaustOnly
                      - MinimumExhaustTemperature
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
                                 'for field `frost_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `frost_control_type`')
            vals = set()
            vals.add("None")
            vals.add("ExhaustAirRecirculation")
            vals.add("ExhaustOnly")
            vals.add("MinimumExhaustTemperature")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `frost_control_type`'.format(value))

        self._data["Frost Control Type"] = value

    @property
    def threshold_temperature(self):
        """Get threshold_temperature

        Returns:
            float: the value of `threshold_temperature` or None if not set
        """
        return self._data["Threshold Temperature"]

    @threshold_temperature.setter
    def threshold_temperature(self, value=1.7 ):
        """  Corresponds to IDD Field `threshold_temperature`
        Supply (outdoor) air inlet temp threshold for exhaust air recirculation and
        exhaust only frost control types. Exhaust air outlet threshold Temperature for
        minimum exhaust temperature frost control type.

        Args:
            value (float): value for IDD Field `threshold_temperature`
                Unit: C
                Default value: 1.7
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
                                 'for field `threshold_temperature`'.format(value))

        self._data["Threshold Temperature"] = value

    @property
    def initial_defrost_time_fraction(self):
        """Get initial_defrost_time_fraction

        Returns:
            float: the value of `initial_defrost_time_fraction` or None if not set
        """
        return self._data["Initial Defrost Time Fraction"]

    @initial_defrost_time_fraction.setter
    def initial_defrost_time_fraction(self, value=0.083 ):
        """  Corresponds to IDD Field `initial_defrost_time_fraction`
        Fraction of the time when frost control will be invoked at the threshold temperature.
        This field only used for exhaust air recirc and exhaust-only frost control types.

        Args:
            value (float): value for IDD Field `initial_defrost_time_fraction`
                Unit: dimensionless
                Default value: 0.083
                value >= 0.0
                value <= 1.0
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
                                 'for field `initial_defrost_time_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `initial_defrost_time_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `initial_defrost_time_fraction`')

        self._data["Initial Defrost Time Fraction"] = value

    @property
    def rate_of_defrost_time_fraction_increase(self):
        """Get rate_of_defrost_time_fraction_increase

        Returns:
            float: the value of `rate_of_defrost_time_fraction_increase` or None if not set
        """
        return self._data["Rate of Defrost Time Fraction Increase"]

    @rate_of_defrost_time_fraction_increase.setter
    def rate_of_defrost_time_fraction_increase(self, value=0.012 ):
        """  Corresponds to IDD Field `rate_of_defrost_time_fraction_increase`
        Rate of increase in defrost time fraction as actual temp falls below threshold temperature.
        This field only used for exhaust air recirc and exhaust-only frost control types.

        Args:
            value (float): value for IDD Field `rate_of_defrost_time_fraction_increase`
                Unit: 1/K
                Default value: 0.012
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
                                 'for field `rate_of_defrost_time_fraction_increase`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rate_of_defrost_time_fraction_increase`')

        self._data["Rate of Defrost Time Fraction Increase"] = value

    @property
    def economizer_lockout(self):
        """Get economizer_lockout

        Returns:
            str: the value of `economizer_lockout` or None if not set
        """
        return self._data["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="Yes"):
        """  Corresponds to IDD Field `economizer_lockout`
        Yes means that the heat exchanger will be locked out (off)
        when the economizer is operating or high humidity control is active

        Args:
            value (str): value for IDD Field `economizer_lockout`
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
                                 'for field `economizer_lockout`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `economizer_lockout`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `economizer_lockout`'.format(value))

        self._data["Economizer Lockout"] = value

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
        out.append(self._to_str(self.nominal_supply_air_flow_rate))
        out.append(self._to_str(self.sensible_effectiveness_at_100_heating_air_flow))
        out.append(self._to_str(self.latent_effectiveness_at_100_heating_air_flow))
        out.append(self._to_str(self.sensible_effectiveness_at_75_heating_air_flow))
        out.append(self._to_str(self.latent_effectiveness_at_75_heating_air_flow))
        out.append(self._to_str(self.sensible_effectiveness_at_100_cooling_air_flow))
        out.append(self._to_str(self.latent_effectiveness_at_100_cooling_air_flow))
        out.append(self._to_str(self.sensible_effectiveness_at_75_cooling_air_flow))
        out.append(self._to_str(self.latent_effectiveness_at_75_cooling_air_flow))
        out.append(self._to_str(self.supply_air_inlet_node_name))
        out.append(self._to_str(self.supply_air_outlet_node_name))
        out.append(self._to_str(self.exhaust_air_inlet_node_name))
        out.append(self._to_str(self.exhaust_air_outlet_node_name))
        out.append(self._to_str(self.nominal_electric_power))
        out.append(self._to_str(self.supply_air_outlet_temperature_control))
        out.append(self._to_str(self.heat_exchanger_type))
        out.append(self._to_str(self.frost_control_type))
        out.append(self._to_str(self.threshold_temperature))
        out.append(self._to_str(self.initial_defrost_time_fraction))
        out.append(self._to_str(self.rate_of_defrost_time_fraction_increase))
        out.append(self._to_str(self.economizer_lockout))
        return ",".join(out)

class HeatExchangerDesiccantBalancedFlow(object):
    """ Corresponds to IDD object `HeatExchanger:Desiccant:BalancedFlow`
        This object models a balanced desiccant heat exchanger.
        The heat exchanger transfers both sensible and latent energy between the
        process and regeneration air streams. The air flow rate and face velocity
        are assumed to be the same on both the process and regeneration sides of the
        heat exchanger.
    """
    internal_name = "HeatExchanger:Desiccant:BalancedFlow"
    field_count = 9

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatExchanger:Desiccant:BalancedFlow`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Regeneration Air Inlet Node Name"] = None
        self._data["Regeneration Air Outlet Node Name"] = None
        self._data["Process Air Inlet Node Name"] = None
        self._data["Process Air Outlet Node Name"] = None
        self._data["Heat Exchanger Performance Object Type"] = None
        self._data["Heat Exchanger Performance Name"] = None
        self._data["Economizer Lockout"] = None

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
            self.regeneration_air_inlet_node_name = None
        else:
            self.regeneration_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regeneration_air_outlet_node_name = None
        else:
            self.regeneration_air_outlet_node_name = vals[i]
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
            self.heat_exchanger_performance_object_type = None
        else:
            self.heat_exchanger_performance_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_exchanger_performance_name = None
        else:
            self.heat_exchanger_performance_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.economizer_lockout = None
        else:
            self.economizer_lockout = vals[i]
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
    def regeneration_air_inlet_node_name(self):
        """Get regeneration_air_inlet_node_name

        Returns:
            str: the value of `regeneration_air_inlet_node_name` or None if not set
        """
        return self._data["Regeneration Air Inlet Node Name"]

    @regeneration_air_inlet_node_name.setter
    def regeneration_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_air_inlet_node_name`

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
    def regeneration_air_outlet_node_name(self):
        """Get regeneration_air_outlet_node_name

        Returns:
            str: the value of `regeneration_air_outlet_node_name` or None if not set
        """
        return self._data["Regeneration Air Outlet Node Name"]

    @regeneration_air_outlet_node_name.setter
    def regeneration_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `regeneration_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `regeneration_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `regeneration_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_outlet_node_name`')

        self._data["Regeneration Air Outlet Node Name"] = value

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
    def heat_exchanger_performance_object_type(self):
        """Get heat_exchanger_performance_object_type

        Returns:
            str: the value of `heat_exchanger_performance_object_type` or None if not set
        """
        return self._data["Heat Exchanger Performance Object Type"]

    @heat_exchanger_performance_object_type.setter
    def heat_exchanger_performance_object_type(self, value="HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"):
        """  Corresponds to IDD Field `heat_exchanger_performance_object_type`

        Args:
            value (str): value for IDD Field `heat_exchanger_performance_object_type`
                Accepted values are:
                      - HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1
                Default value: HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_exchanger_performance_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchanger_performance_object_type`')
            vals = set()
            vals.add("HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heat_exchanger_performance_object_type`'.format(value))

        self._data["Heat Exchanger Performance Object Type"] = value

    @property
    def heat_exchanger_performance_name(self):
        """Get heat_exchanger_performance_name

        Returns:
            str: the value of `heat_exchanger_performance_name` or None if not set
        """
        return self._data["Heat Exchanger Performance Name"]

    @heat_exchanger_performance_name.setter
    def heat_exchanger_performance_name(self, value=None):
        """  Corresponds to IDD Field `heat_exchanger_performance_name`

        Args:
            value (str): value for IDD Field `heat_exchanger_performance_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_exchanger_performance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchanger_performance_name`')

        self._data["Heat Exchanger Performance Name"] = value

    @property
    def economizer_lockout(self):
        """Get economizer_lockout

        Returns:
            str: the value of `economizer_lockout` or None if not set
        """
        return self._data["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="No"):
        """  Corresponds to IDD Field `economizer_lockout`
        Yes means that the heat exchanger will be locked out (off)
        when the economizer is operating or high humidity control is active

        Args:
            value (str): value for IDD Field `economizer_lockout`
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
                                 'for field `economizer_lockout`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `economizer_lockout`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `economizer_lockout`'.format(value))

        self._data["Economizer Lockout"] = value

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
        out.append(self._to_str(self.regeneration_air_inlet_node_name))
        out.append(self._to_str(self.regeneration_air_outlet_node_name))
        out.append(self._to_str(self.process_air_inlet_node_name))
        out.append(self._to_str(self.process_air_outlet_node_name))
        out.append(self._to_str(self.heat_exchanger_performance_object_type))
        out.append(self._to_str(self.heat_exchanger_performance_name))
        out.append(self._to_str(self.economizer_lockout))
        return ",".join(out)

class HeatExchangerDesiccantBalancedFlowPerformanceDataType1(object):
    """ Corresponds to IDD object `HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1`
        RTO = B1 + B2*RWI + B3*RTI + B4*(RWI/RTI) + B5*PWI + B6*PTI + B7*(PWI/PTI)
        + B8*RFV
        RWO = C1 + C2*RWI + C3*RTI + C4*(RWI/RTI) + C5*PWI + C6*PTI + C7*(PWI/PTI)
        + C8*RFV
        where,
        RTO = Dry-bulb temperature of the regeneration outlet air (C)
        RWO = Humidity ratio of the regeneration outlet air (kgWater/kgDryAir)
        RWI = Humidity ratio of the regeneration inlet air (kgWater/kgDryAir)
        RTI = Dry-bulb temperature of the regeneration inlet air (C)
        PWI = Humidity ratio of the process inlet air (kgWater/kgDryAir)
        PTI = Dry-bulb temperature of the process inlet air (C)
        RFV = Regeneration Face Velocity (m/s)
    """
    internal_name = "HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"
    field_count = 52

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Nominal Air Flow Rate"] = None
        self._data["Nominal Air Face Velocity"] = None
        self._data["Nominal Electric Power"] = None
        self._data["Temperature Equation Coefficient 1"] = None
        self._data["Temperature Equation Coefficient 2"] = None
        self._data["Temperature Equation Coefficient 3"] = None
        self._data["Temperature Equation Coefficient 4"] = None
        self._data["Temperature Equation Coefficient 5"] = None
        self._data["Temperature Equation Coefficient 6"] = None
        self._data["Temperature Equation Coefficient 7"] = None
        self._data["Temperature Equation Coefficient 8"] = None
        self._data["Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = None
        self._data["Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = None
        self._data["Minimum Regeneration Inlet Air Temperature for Temperature Equation"] = None
        self._data["Maximum Regeneration Inlet Air Temperature for Temperature Equation"] = None
        self._data["Minimum Process Inlet Air Humidity Ratio for Temperature Equation"] = None
        self._data["Maximum Process Inlet Air Humidity Ratio for Temperature Equation"] = None
        self._data["Minimum Process Inlet Air Temperature for Temperature Equation"] = None
        self._data["Maximum Process Inlet Air Temperature for Temperature Equation"] = None
        self._data["Minimum Regeneration Air Velocity for Temperature Equation"] = None
        self._data["Maximum Regeneration Air Velocity for Temperature Equation"] = None
        self._data["Minimum Regeneration Outlet Air Temperature for Temperature Equation"] = None
        self._data["Maximum Regeneration Outlet Air Temperature for Temperature Equation"] = None
        self._data["Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = None
        self._data["Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = None
        self._data["Minimum Process Inlet Air Relative Humidity for Temperature Equation"] = None
        self._data["Maximum Process Inlet Air Relative Humidity for Temperature Equation"] = None
        self._data["Humidity Ratio Equation Coefficient 1"] = None
        self._data["Humidity Ratio Equation Coefficient 2"] = None
        self._data["Humidity Ratio Equation Coefficient 3"] = None
        self._data["Humidity Ratio Equation Coefficient 4"] = None
        self._data["Humidity Ratio Equation Coefficient 5"] = None
        self._data["Humidity Ratio Equation Coefficient 6"] = None
        self._data["Humidity Ratio Equation Coefficient 7"] = None
        self._data["Humidity Ratio Equation Coefficient 8"] = None
        self._data["Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = None
        self._data["Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = None
        self._data["Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Minimum Process Inlet Air Temperature for Humidity Ratio Equation"] = None
        self._data["Maximum Process Inlet Air Temperature for Humidity Ratio Equation"] = None
        self._data["Minimum Regeneration Air Velocity for Humidity Ratio Equation"] = None
        self._data["Maximum Regeneration Air Velocity for Humidity Ratio Equation"] = None
        self._data["Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = None
        self._data["Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = None
        self._data["Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = None
        self._data["Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = None

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
            self.nominal_air_flow_rate = None
        else:
            self.nominal_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_air_face_velocity = None
        else:
            self.nominal_air_face_velocity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_electric_power = None
        else:
            self.nominal_electric_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_1 = None
        else:
            self.temperature_equation_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_2 = None
        else:
            self.temperature_equation_coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_3 = None
        else:
            self.temperature_equation_coefficient_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_4 = None
        else:
            self.temperature_equation_coefficient_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_5 = None
        else:
            self.temperature_equation_coefficient_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_6 = None
        else:
            self.temperature_equation_coefficient_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_7 = None
        else:
            self.temperature_equation_coefficient_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_8 = None
        else:
            self.temperature_equation_coefficient_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = None
        else:
            self.minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = None
        else:
            self.maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_temperature_for_temperature_equation = None
        else:
            self.minimum_regeneration_inlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_temperature_for_temperature_equation = None
        else:
            self.maximum_regeneration_inlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_humidity_ratio_for_temperature_equation = None
        else:
            self.minimum_process_inlet_air_humidity_ratio_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_humidity_ratio_for_temperature_equation = None
        else:
            self.maximum_process_inlet_air_humidity_ratio_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_temperature_for_temperature_equation = None
        else:
            self.minimum_process_inlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_temperature_for_temperature_equation = None
        else:
            self.maximum_process_inlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_regeneration_air_velocity_for_temperature_equation = None
        else:
            self.minimum_regeneration_air_velocity_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_regeneration_air_velocity_for_temperature_equation = None
        else:
            self.maximum_regeneration_air_velocity_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_regeneration_outlet_air_temperature_for_temperature_equation = None
        else:
            self.minimum_regeneration_outlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_regeneration_outlet_air_temperature_for_temperature_equation = None
        else:
            self.maximum_regeneration_outlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation = None
        else:
            self.minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation = None
        else:
            self.maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_relative_humidity_for_temperature_equation = None
        else:
            self.minimum_process_inlet_air_relative_humidity_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_relative_humidity_for_temperature_equation = None
        else:
            self.maximum_process_inlet_air_relative_humidity_for_temperature_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_1 = None
        else:
            self.humidity_ratio_equation_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_2 = None
        else:
            self.humidity_ratio_equation_coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_3 = None
        else:
            self.humidity_ratio_equation_coefficient_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_4 = None
        else:
            self.humidity_ratio_equation_coefficient_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_5 = None
        else:
            self.humidity_ratio_equation_coefficient_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_6 = None
        else:
            self.humidity_ratio_equation_coefficient_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_7 = None
        else:
            self.humidity_ratio_equation_coefficient_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_8 = None
        else:
            self.humidity_ratio_equation_coefficient_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = None
        else:
            self.minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = None
        else:
            self.maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_temperature_for_humidity_ratio_equation = None
        else:
            self.minimum_process_inlet_air_temperature_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_temperature_for_humidity_ratio_equation = None
        else:
            self.maximum_process_inlet_air_temperature_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_regeneration_air_velocity_for_humidity_ratio_equation = None
        else:
            self.minimum_regeneration_air_velocity_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_regeneration_air_velocity_for_humidity_ratio_equation = None
        else:
            self.maximum_regeneration_air_velocity_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = None
        else:
            self.minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = None
        else:
            self.maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = None
        else:
            self.minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = None
        else:
            self.maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = vals[i]
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
    def nominal_air_flow_rate(self):
        """Get nominal_air_flow_rate

        Returns:
            float: the value of `nominal_air_flow_rate` or None if not set
        """
        return self._data["Nominal Air Flow Rate"]

    @nominal_air_flow_rate.setter
    def nominal_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `nominal_air_flow_rate`
        Air flow rate at nominal conditions (assumed to be the same for both sides
        of the heat exchanger).

        Args:
            value (float): value for IDD Field `nominal_air_flow_rate`
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
                                 'for field `nominal_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_air_flow_rate`')

        self._data["Nominal Air Flow Rate"] = value

    @property
    def nominal_air_face_velocity(self):
        """Get nominal_air_face_velocity

        Returns:
            float: the value of `nominal_air_face_velocity` or None if not set
        """
        return self._data["Nominal Air Face Velocity"]

    @nominal_air_face_velocity.setter
    def nominal_air_face_velocity(self, value=None):
        """  Corresponds to IDD Field `nominal_air_face_velocity`

        Args:
            value (float): value for IDD Field `nominal_air_face_velocity`
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
                                 'for field `nominal_air_face_velocity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_air_face_velocity`')
            if value > 6.0:
                raise ValueError('value need to be smaller 6.0 '
                                 'for field `nominal_air_face_velocity`')

        self._data["Nominal Air Face Velocity"] = value

    @property
    def nominal_electric_power(self):
        """Get nominal_electric_power

        Returns:
            float: the value of `nominal_electric_power` or None if not set
        """
        return self._data["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=0.0 ):
        """  Corresponds to IDD Field `nominal_electric_power`
        Parasitic electric power (e.g., desiccant wheel motor)

        Args:
            value (float): value for IDD Field `nominal_electric_power`
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
                                 'for field `nominal_electric_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_electric_power`')

        self._data["Nominal Electric Power"] = value

    @property
    def temperature_equation_coefficient_1(self):
        """Get temperature_equation_coefficient_1

        Returns:
            float: the value of `temperature_equation_coefficient_1` or None if not set
        """
        return self._data["Temperature Equation Coefficient 1"]

    @temperature_equation_coefficient_1.setter
    def temperature_equation_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `temperature_equation_coefficient_1`

        Args:
            value (float): value for IDD Field `temperature_equation_coefficient_1`
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
                                 'for field `temperature_equation_coefficient_1`'.format(value))

        self._data["Temperature Equation Coefficient 1"] = value

    @property
    def temperature_equation_coefficient_2(self):
        """Get temperature_equation_coefficient_2

        Returns:
            float: the value of `temperature_equation_coefficient_2` or None if not set
        """
        return self._data["Temperature Equation Coefficient 2"]

    @temperature_equation_coefficient_2.setter
    def temperature_equation_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `temperature_equation_coefficient_2`

        Args:
            value (float): value for IDD Field `temperature_equation_coefficient_2`
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
                                 'for field `temperature_equation_coefficient_2`'.format(value))

        self._data["Temperature Equation Coefficient 2"] = value

    @property
    def temperature_equation_coefficient_3(self):
        """Get temperature_equation_coefficient_3

        Returns:
            float: the value of `temperature_equation_coefficient_3` or None if not set
        """
        return self._data["Temperature Equation Coefficient 3"]

    @temperature_equation_coefficient_3.setter
    def temperature_equation_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `temperature_equation_coefficient_3`

        Args:
            value (float): value for IDD Field `temperature_equation_coefficient_3`
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
                                 'for field `temperature_equation_coefficient_3`'.format(value))

        self._data["Temperature Equation Coefficient 3"] = value

    @property
    def temperature_equation_coefficient_4(self):
        """Get temperature_equation_coefficient_4

        Returns:
            float: the value of `temperature_equation_coefficient_4` or None if not set
        """
        return self._data["Temperature Equation Coefficient 4"]

    @temperature_equation_coefficient_4.setter
    def temperature_equation_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `temperature_equation_coefficient_4`

        Args:
            value (float): value for IDD Field `temperature_equation_coefficient_4`
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
                                 'for field `temperature_equation_coefficient_4`'.format(value))

        self._data["Temperature Equation Coefficient 4"] = value

    @property
    def temperature_equation_coefficient_5(self):
        """Get temperature_equation_coefficient_5

        Returns:
            float: the value of `temperature_equation_coefficient_5` or None if not set
        """
        return self._data["Temperature Equation Coefficient 5"]

    @temperature_equation_coefficient_5.setter
    def temperature_equation_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `temperature_equation_coefficient_5`

        Args:
            value (float): value for IDD Field `temperature_equation_coefficient_5`
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
                                 'for field `temperature_equation_coefficient_5`'.format(value))

        self._data["Temperature Equation Coefficient 5"] = value

    @property
    def temperature_equation_coefficient_6(self):
        """Get temperature_equation_coefficient_6

        Returns:
            float: the value of `temperature_equation_coefficient_6` or None if not set
        """
        return self._data["Temperature Equation Coefficient 6"]

    @temperature_equation_coefficient_6.setter
    def temperature_equation_coefficient_6(self, value=None):
        """  Corresponds to IDD Field `temperature_equation_coefficient_6`

        Args:
            value (float): value for IDD Field `temperature_equation_coefficient_6`
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
                                 'for field `temperature_equation_coefficient_6`'.format(value))

        self._data["Temperature Equation Coefficient 6"] = value

    @property
    def temperature_equation_coefficient_7(self):
        """Get temperature_equation_coefficient_7

        Returns:
            float: the value of `temperature_equation_coefficient_7` or None if not set
        """
        return self._data["Temperature Equation Coefficient 7"]

    @temperature_equation_coefficient_7.setter
    def temperature_equation_coefficient_7(self, value=None):
        """  Corresponds to IDD Field `temperature_equation_coefficient_7`

        Args:
            value (float): value for IDD Field `temperature_equation_coefficient_7`
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
                                 'for field `temperature_equation_coefficient_7`'.format(value))

        self._data["Temperature Equation Coefficient 7"] = value

    @property
    def temperature_equation_coefficient_8(self):
        """Get temperature_equation_coefficient_8

        Returns:
            float: the value of `temperature_equation_coefficient_8` or None if not set
        """
        return self._data["Temperature Equation Coefficient 8"]

    @temperature_equation_coefficient_8.setter
    def temperature_equation_coefficient_8(self, value=None):
        """  Corresponds to IDD Field `temperature_equation_coefficient_8`

        Args:
            value (float): value for IDD Field `temperature_equation_coefficient_8`
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
                                 'for field `temperature_equation_coefficient_8`'.format(value))

        self._data["Temperature Equation Coefficient 8"] = value

    @property
    def minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation"]

    @minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`

        Args:
            value (float): value for IDD Field `minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`
                Unit: kgWater/kgDryAir
                value >= 0.0
                value <= 1.0
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
                                 'for field `minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`')

        self._data["Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation"]

    @maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`

        Args:
            value (float): value for IDD Field `maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`
                Unit: kgWater/kgDryAir
                value >= 0.0
                value <= 1.0
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
                                 'for field `maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`')

        self._data["Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def minimum_regeneration_inlet_air_temperature_for_temperature_equation(self):
        """Get minimum_regeneration_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Temperature for Temperature Equation"]

    @minimum_regeneration_inlet_air_temperature_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_regeneration_inlet_air_temperature_for_temperature_equation`

        Args:
            value (float): value for IDD Field `minimum_regeneration_inlet_air_temperature_for_temperature_equation`
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
                                 'for field `minimum_regeneration_inlet_air_temperature_for_temperature_equation`'.format(value))

        self._data["Minimum Regeneration Inlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_temperature_for_temperature_equation(self):
        """Get maximum_regeneration_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Temperature for Temperature Equation"]

    @maximum_regeneration_inlet_air_temperature_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_regeneration_inlet_air_temperature_for_temperature_equation`

        Args:
            value (float): value for IDD Field `maximum_regeneration_inlet_air_temperature_for_temperature_equation`
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
                                 'for field `maximum_regeneration_inlet_air_temperature_for_temperature_equation`'.format(value))

        self._data["Maximum Regeneration Inlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get minimum_process_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `minimum_process_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Humidity Ratio for Temperature Equation"]

    @minimum_process_inlet_air_humidity_ratio_for_temperature_equation.setter
    def minimum_process_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_process_inlet_air_humidity_ratio_for_temperature_equation`

        Args:
            value (float): value for IDD Field `minimum_process_inlet_air_humidity_ratio_for_temperature_equation`
                Unit: kgWater/kgDryAir
                value >= 0.0
                value <= 1.0
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
                                 'for field `minimum_process_inlet_air_humidity_ratio_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_process_inlet_air_humidity_ratio_for_temperature_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_process_inlet_air_humidity_ratio_for_temperature_equation`')

        self._data["Minimum Process Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get maximum_process_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `maximum_process_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Humidity Ratio for Temperature Equation"]

    @maximum_process_inlet_air_humidity_ratio_for_temperature_equation.setter
    def maximum_process_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_process_inlet_air_humidity_ratio_for_temperature_equation`

        Args:
            value (float): value for IDD Field `maximum_process_inlet_air_humidity_ratio_for_temperature_equation`
                Unit: kgWater/kgDryAir
                value >= 0.0
                value <= 1.0
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
                                 'for field `maximum_process_inlet_air_humidity_ratio_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_process_inlet_air_humidity_ratio_for_temperature_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_process_inlet_air_humidity_ratio_for_temperature_equation`')

        self._data["Maximum Process Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_temperature_for_temperature_equation(self):
        """Get minimum_process_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `minimum_process_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Temperature for Temperature Equation"]

    @minimum_process_inlet_air_temperature_for_temperature_equation.setter
    def minimum_process_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_process_inlet_air_temperature_for_temperature_equation`

        Args:
            value (float): value for IDD Field `minimum_process_inlet_air_temperature_for_temperature_equation`
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
                                 'for field `minimum_process_inlet_air_temperature_for_temperature_equation`'.format(value))

        self._data["Minimum Process Inlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_temperature_for_temperature_equation(self):
        """Get maximum_process_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `maximum_process_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Temperature for Temperature Equation"]

    @maximum_process_inlet_air_temperature_for_temperature_equation.setter
    def maximum_process_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_process_inlet_air_temperature_for_temperature_equation`

        Args:
            value (float): value for IDD Field `maximum_process_inlet_air_temperature_for_temperature_equation`
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
                                 'for field `maximum_process_inlet_air_temperature_for_temperature_equation`'.format(value))

        self._data["Maximum Process Inlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_regeneration_air_velocity_for_temperature_equation(self):
        """Get minimum_regeneration_air_velocity_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_air_velocity_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Regeneration Air Velocity for Temperature Equation"]

    @minimum_regeneration_air_velocity_for_temperature_equation.setter
    def minimum_regeneration_air_velocity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_regeneration_air_velocity_for_temperature_equation`

        Args:
            value (float): value for IDD Field `minimum_regeneration_air_velocity_for_temperature_equation`
                Unit: m/s
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
                                 'for field `minimum_regeneration_air_velocity_for_temperature_equation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_regeneration_air_velocity_for_temperature_equation`')

        self._data["Minimum Regeneration Air Velocity for Temperature Equation"] = value

    @property
    def maximum_regeneration_air_velocity_for_temperature_equation(self):
        """Get maximum_regeneration_air_velocity_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_air_velocity_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Regeneration Air Velocity for Temperature Equation"]

    @maximum_regeneration_air_velocity_for_temperature_equation.setter
    def maximum_regeneration_air_velocity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_regeneration_air_velocity_for_temperature_equation`

        Args:
            value (float): value for IDD Field `maximum_regeneration_air_velocity_for_temperature_equation`
                Unit: m/s
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
                                 'for field `maximum_regeneration_air_velocity_for_temperature_equation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_regeneration_air_velocity_for_temperature_equation`')

        self._data["Maximum Regeneration Air Velocity for Temperature Equation"] = value

    @property
    def minimum_regeneration_outlet_air_temperature_for_temperature_equation(self):
        """Get minimum_regeneration_outlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_outlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Regeneration Outlet Air Temperature for Temperature Equation"]

    @minimum_regeneration_outlet_air_temperature_for_temperature_equation.setter
    def minimum_regeneration_outlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_regeneration_outlet_air_temperature_for_temperature_equation`

        Args:
            value (float): value for IDD Field `minimum_regeneration_outlet_air_temperature_for_temperature_equation`
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
                                 'for field `minimum_regeneration_outlet_air_temperature_for_temperature_equation`'.format(value))

        self._data["Minimum Regeneration Outlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_regeneration_outlet_air_temperature_for_temperature_equation(self):
        """Get maximum_regeneration_outlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_outlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Regeneration Outlet Air Temperature for Temperature Equation"]

    @maximum_regeneration_outlet_air_temperature_for_temperature_equation.setter
    def maximum_regeneration_outlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_regeneration_outlet_air_temperature_for_temperature_equation`

        Args:
            value (float): value for IDD Field `maximum_regeneration_outlet_air_temperature_for_temperature_equation`
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
                                 'for field `maximum_regeneration_outlet_air_temperature_for_temperature_equation`'.format(value))

        self._data["Maximum Regeneration Outlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation"]

    @minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation`

        Args:
            value (float): value for IDD Field `minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation`
                Unit: percent
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
                                 'for field `minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation`')

        self._data["Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation"]

    @maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation`

        Args:
            value (float): value for IDD Field `maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation`
                Unit: percent
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
                                 'for field `maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation`')

        self._data["Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get minimum_process_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `minimum_process_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Relative Humidity for Temperature Equation"]

    @minimum_process_inlet_air_relative_humidity_for_temperature_equation.setter
    def minimum_process_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_process_inlet_air_relative_humidity_for_temperature_equation`

        Args:
            value (float): value for IDD Field `minimum_process_inlet_air_relative_humidity_for_temperature_equation`
                Unit: percent
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
                                 'for field `minimum_process_inlet_air_relative_humidity_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_process_inlet_air_relative_humidity_for_temperature_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_process_inlet_air_relative_humidity_for_temperature_equation`')

        self._data["Minimum Process Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get maximum_process_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `maximum_process_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Relative Humidity for Temperature Equation"]

    @maximum_process_inlet_air_relative_humidity_for_temperature_equation.setter
    def maximum_process_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_process_inlet_air_relative_humidity_for_temperature_equation`

        Args:
            value (float): value for IDD Field `maximum_process_inlet_air_relative_humidity_for_temperature_equation`
                Unit: percent
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
                                 'for field `maximum_process_inlet_air_relative_humidity_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_process_inlet_air_relative_humidity_for_temperature_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_process_inlet_air_relative_humidity_for_temperature_equation`')

        self._data["Maximum Process Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def humidity_ratio_equation_coefficient_1(self):
        """Get humidity_ratio_equation_coefficient_1

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_1` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 1"]

    @humidity_ratio_equation_coefficient_1.setter
    def humidity_ratio_equation_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `humidity_ratio_equation_coefficient_1`

        Args:
            value (float): value for IDD Field `humidity_ratio_equation_coefficient_1`
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
                                 'for field `humidity_ratio_equation_coefficient_1`'.format(value))

        self._data["Humidity Ratio Equation Coefficient 1"] = value

    @property
    def humidity_ratio_equation_coefficient_2(self):
        """Get humidity_ratio_equation_coefficient_2

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_2` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 2"]

    @humidity_ratio_equation_coefficient_2.setter
    def humidity_ratio_equation_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `humidity_ratio_equation_coefficient_2`

        Args:
            value (float): value for IDD Field `humidity_ratio_equation_coefficient_2`
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
                                 'for field `humidity_ratio_equation_coefficient_2`'.format(value))

        self._data["Humidity Ratio Equation Coefficient 2"] = value

    @property
    def humidity_ratio_equation_coefficient_3(self):
        """Get humidity_ratio_equation_coefficient_3

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_3` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 3"]

    @humidity_ratio_equation_coefficient_3.setter
    def humidity_ratio_equation_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `humidity_ratio_equation_coefficient_3`

        Args:
            value (float): value for IDD Field `humidity_ratio_equation_coefficient_3`
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
                                 'for field `humidity_ratio_equation_coefficient_3`'.format(value))

        self._data["Humidity Ratio Equation Coefficient 3"] = value

    @property
    def humidity_ratio_equation_coefficient_4(self):
        """Get humidity_ratio_equation_coefficient_4

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_4` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 4"]

    @humidity_ratio_equation_coefficient_4.setter
    def humidity_ratio_equation_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `humidity_ratio_equation_coefficient_4`

        Args:
            value (float): value for IDD Field `humidity_ratio_equation_coefficient_4`
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
                                 'for field `humidity_ratio_equation_coefficient_4`'.format(value))

        self._data["Humidity Ratio Equation Coefficient 4"] = value

    @property
    def humidity_ratio_equation_coefficient_5(self):
        """Get humidity_ratio_equation_coefficient_5

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_5` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 5"]

    @humidity_ratio_equation_coefficient_5.setter
    def humidity_ratio_equation_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `humidity_ratio_equation_coefficient_5`

        Args:
            value (float): value for IDD Field `humidity_ratio_equation_coefficient_5`
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
                                 'for field `humidity_ratio_equation_coefficient_5`'.format(value))

        self._data["Humidity Ratio Equation Coefficient 5"] = value

    @property
    def humidity_ratio_equation_coefficient_6(self):
        """Get humidity_ratio_equation_coefficient_6

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_6` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 6"]

    @humidity_ratio_equation_coefficient_6.setter
    def humidity_ratio_equation_coefficient_6(self, value=None):
        """  Corresponds to IDD Field `humidity_ratio_equation_coefficient_6`

        Args:
            value (float): value for IDD Field `humidity_ratio_equation_coefficient_6`
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
                                 'for field `humidity_ratio_equation_coefficient_6`'.format(value))

        self._data["Humidity Ratio Equation Coefficient 6"] = value

    @property
    def humidity_ratio_equation_coefficient_7(self):
        """Get humidity_ratio_equation_coefficient_7

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_7` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 7"]

    @humidity_ratio_equation_coefficient_7.setter
    def humidity_ratio_equation_coefficient_7(self, value=None):
        """  Corresponds to IDD Field `humidity_ratio_equation_coefficient_7`

        Args:
            value (float): value for IDD Field `humidity_ratio_equation_coefficient_7`
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
                                 'for field `humidity_ratio_equation_coefficient_7`'.format(value))

        self._data["Humidity Ratio Equation Coefficient 7"] = value

    @property
    def humidity_ratio_equation_coefficient_8(self):
        """Get humidity_ratio_equation_coefficient_8

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_8` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 8"]

    @humidity_ratio_equation_coefficient_8.setter
    def humidity_ratio_equation_coefficient_8(self, value=None):
        """  Corresponds to IDD Field `humidity_ratio_equation_coefficient_8`

        Args:
            value (float): value for IDD Field `humidity_ratio_equation_coefficient_8`
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
                                 'for field `humidity_ratio_equation_coefficient_8`'.format(value))

        self._data["Humidity Ratio Equation Coefficient 8"] = value

    @property
    def minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`
                Unit: kgWater/kgDryAir
                value >= 0.0
                value <= 1.0
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
                                 'for field `minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`')

        self._data["Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`
                Unit: kgWater/kgDryAir
                value >= 0.0
                value <= 1.0
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
                                 'for field `maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`')

        self._data["Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation`
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
                                 'for field `minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation`'.format(value))

        self._data["Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation`
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
                                 'for field `maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation`'.format(value))

        self._data["Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`
                Unit: kgWater/kgDryAir
                value >= 0.0
                value <= 1.0
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
                                 'for field `minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`')

        self._data["Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`
                Unit: kgWater/kgDryAir
                value >= 0.0
                value <= 1.0
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
                                 'for field `maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`')

        self._data["Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get minimum_process_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_process_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Temperature for Humidity Ratio Equation"]

    @minimum_process_inlet_air_temperature_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_process_inlet_air_temperature_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `minimum_process_inlet_air_temperature_for_humidity_ratio_equation`
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
                                 'for field `minimum_process_inlet_air_temperature_for_humidity_ratio_equation`'.format(value))

        self._data["Minimum Process Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get maximum_process_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_process_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Temperature for Humidity Ratio Equation"]

    @maximum_process_inlet_air_temperature_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_process_inlet_air_temperature_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `maximum_process_inlet_air_temperature_for_humidity_ratio_equation`
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
                                 'for field `maximum_process_inlet_air_temperature_for_humidity_ratio_equation`'.format(value))

        self._data["Maximum Process Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_air_velocity_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_air_velocity_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_air_velocity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Regeneration Air Velocity for Humidity Ratio Equation"]

    @minimum_regeneration_air_velocity_for_humidity_ratio_equation.setter
    def minimum_regeneration_air_velocity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_regeneration_air_velocity_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `minimum_regeneration_air_velocity_for_humidity_ratio_equation`
                Unit: m/s
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
                                 'for field `minimum_regeneration_air_velocity_for_humidity_ratio_equation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_regeneration_air_velocity_for_humidity_ratio_equation`')

        self._data["Minimum Regeneration Air Velocity for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_air_velocity_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_air_velocity_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_air_velocity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Regeneration Air Velocity for Humidity Ratio Equation"]

    @maximum_regeneration_air_velocity_for_humidity_ratio_equation.setter
    def maximum_regeneration_air_velocity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_regeneration_air_velocity_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `maximum_regeneration_air_velocity_for_humidity_ratio_equation`
                Unit: m/s
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
                                 'for field `maximum_regeneration_air_velocity_for_humidity_ratio_equation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_regeneration_air_velocity_for_humidity_ratio_equation`')

        self._data["Maximum Regeneration Air Velocity for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`
                Unit: kgWater/kgDryAir
                value >= 0.0
                value <= 1.0
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
                                 'for field `minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`')

        self._data["Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`
                Unit: kgWater/kgDryAir
                value >= 0.0
                value <= 1.0
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
                                 'for field `maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`')

        self._data["Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`
                Unit: percent
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
                                 'for field `minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`')

        self._data["Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`
                Unit: percent
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
                                 'for field `maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`')

        self._data["Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`
                Unit: percent
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
                                 'for field `minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`')

        self._data["Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`

        Args:
            value (float): value for IDD Field `maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`
                Unit: percent
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
                                 'for field `maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`')

        self._data["Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

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
        out.append(self._to_str(self.nominal_air_flow_rate))
        out.append(self._to_str(self.nominal_air_face_velocity))
        out.append(self._to_str(self.nominal_electric_power))
        out.append(self._to_str(self.temperature_equation_coefficient_1))
        out.append(self._to_str(self.temperature_equation_coefficient_2))
        out.append(self._to_str(self.temperature_equation_coefficient_3))
        out.append(self._to_str(self.temperature_equation_coefficient_4))
        out.append(self._to_str(self.temperature_equation_coefficient_5))
        out.append(self._to_str(self.temperature_equation_coefficient_6))
        out.append(self._to_str(self.temperature_equation_coefficient_7))
        out.append(self._to_str(self.temperature_equation_coefficient_8))
        out.append(self._to_str(self.minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation))
        out.append(self._to_str(self.maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation))
        out.append(self._to_str(self.minimum_regeneration_inlet_air_temperature_for_temperature_equation))
        out.append(self._to_str(self.maximum_regeneration_inlet_air_temperature_for_temperature_equation))
        out.append(self._to_str(self.minimum_process_inlet_air_humidity_ratio_for_temperature_equation))
        out.append(self._to_str(self.maximum_process_inlet_air_humidity_ratio_for_temperature_equation))
        out.append(self._to_str(self.minimum_process_inlet_air_temperature_for_temperature_equation))
        out.append(self._to_str(self.maximum_process_inlet_air_temperature_for_temperature_equation))
        out.append(self._to_str(self.minimum_regeneration_air_velocity_for_temperature_equation))
        out.append(self._to_str(self.maximum_regeneration_air_velocity_for_temperature_equation))
        out.append(self._to_str(self.minimum_regeneration_outlet_air_temperature_for_temperature_equation))
        out.append(self._to_str(self.maximum_regeneration_outlet_air_temperature_for_temperature_equation))
        out.append(self._to_str(self.minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation))
        out.append(self._to_str(self.maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation))
        out.append(self._to_str(self.minimum_process_inlet_air_relative_humidity_for_temperature_equation))
        out.append(self._to_str(self.maximum_process_inlet_air_relative_humidity_for_temperature_equation))
        out.append(self._to_str(self.humidity_ratio_equation_coefficient_1))
        out.append(self._to_str(self.humidity_ratio_equation_coefficient_2))
        out.append(self._to_str(self.humidity_ratio_equation_coefficient_3))
        out.append(self._to_str(self.humidity_ratio_equation_coefficient_4))
        out.append(self._to_str(self.humidity_ratio_equation_coefficient_5))
        out.append(self._to_str(self.humidity_ratio_equation_coefficient_6))
        out.append(self._to_str(self.humidity_ratio_equation_coefficient_7))
        out.append(self._to_str(self.humidity_ratio_equation_coefficient_8))
        out.append(self._to_str(self.minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation))
        out.append(self._to_str(self.maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation))
        out.append(self._to_str(self.minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation))
        out.append(self._to_str(self.maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation))
        out.append(self._to_str(self.minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation))
        out.append(self._to_str(self.maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation))
        out.append(self._to_str(self.minimum_process_inlet_air_temperature_for_humidity_ratio_equation))
        out.append(self._to_str(self.maximum_process_inlet_air_temperature_for_humidity_ratio_equation))
        out.append(self._to_str(self.minimum_regeneration_air_velocity_for_humidity_ratio_equation))
        out.append(self._to_str(self.maximum_regeneration_air_velocity_for_humidity_ratio_equation))
        out.append(self._to_str(self.minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation))
        out.append(self._to_str(self.maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation))
        out.append(self._to_str(self.minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation))
        out.append(self._to_str(self.maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation))
        out.append(self._to_str(self.minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation))
        out.append(self._to_str(self.maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation))
        return ",".join(out)

class HeatExchangerFluidToFluid(object):
    """ Corresponds to IDD object `HeatExchanger:FluidToFluid`
        A fluid/fluid heat exchanger designed to couple the supply side of one loop to the demand side of another loop
        Loops can be either plant or condenser loops but no air side connections are allowed
    """
    internal_name = "HeatExchanger:FluidToFluid"
    field_count = 20

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatExchanger:FluidToFluid`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Loop Demand Side Inlet Node Name"] = None
        self._data["Loop Demand Side Outlet Node Name"] = None
        self._data["Loop Demand Side Design Flow Rate"] = None
        self._data["Loop Supply Side Inlet Node Name"] = None
        self._data["Loop Supply Side Outlet Node Name"] = None
        self._data["Loop Supply Side Design Flow Rate"] = None
        self._data["Heat Exchange Model Type"] = None
        self._data["Heat Exchanger U-Factor Times Area Value"] = None
        self._data["Control Type"] = None
        self._data["Heat Exchanger Setpoint Node Name"] = None
        self._data["Minimum Temperature Difference to Activate Heat Exchanger"] = None
        self._data["Heat Transfer Metering End Use Type"] = None
        self._data["Component Override Loop Supply Side Inlet Node Name"] = None
        self._data["Component Override Loop Demand Side Inlet Node Name"] = None
        self._data["Component Override Cooling Control Temperature Mode"] = None
        self._data["Sizing Factor"] = None
        self._data["Operation Minimum Temperature Limit"] = None
        self._data["Operation Maximum Temperature Limit"] = None

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
            self.loop_demand_side_inlet_node_name = None
        else:
            self.loop_demand_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.loop_demand_side_outlet_node_name = None
        else:
            self.loop_demand_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.loop_demand_side_design_flow_rate = None
        else:
            self.loop_demand_side_design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.loop_supply_side_inlet_node_name = None
        else:
            self.loop_supply_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.loop_supply_side_outlet_node_name = None
        else:
            self.loop_supply_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.loop_supply_side_design_flow_rate = None
        else:
            self.loop_supply_side_design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_exchange_model_type = None
        else:
            self.heat_exchange_model_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_exchanger_ufactor_times_area_value = None
        else:
            self.heat_exchanger_ufactor_times_area_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_type = None
        else:
            self.control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_exchanger_setpoint_node_name = None
        else:
            self.heat_exchanger_setpoint_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_temperature_difference_to_activate_heat_exchanger = None
        else:
            self.minimum_temperature_difference_to_activate_heat_exchanger = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_transfer_metering_end_use_type = None
        else:
            self.heat_transfer_metering_end_use_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_override_loop_supply_side_inlet_node_name = None
        else:
            self.component_override_loop_supply_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_override_loop_demand_side_inlet_node_name = None
        else:
            self.component_override_loop_demand_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_override_cooling_control_temperature_mode = None
        else:
            self.component_override_cooling_control_temperature_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_minimum_temperature_limit = None
        else:
            self.operation_minimum_temperature_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_maximum_temperature_limit = None
        else:
            self.operation_maximum_temperature_limit = vals[i]
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
        default is that heat exchanger is on

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
    def loop_demand_side_inlet_node_name(self):
        """Get loop_demand_side_inlet_node_name

        Returns:
            str: the value of `loop_demand_side_inlet_node_name` or None if not set
        """
        return self._data["Loop Demand Side Inlet Node Name"]

    @loop_demand_side_inlet_node_name.setter
    def loop_demand_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `loop_demand_side_inlet_node_name`
        This connection is to the demand side of a loop and is the inlet to the heat exchanger

        Args:
            value (str): value for IDD Field `loop_demand_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `loop_demand_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_demand_side_inlet_node_name`')

        self._data["Loop Demand Side Inlet Node Name"] = value

    @property
    def loop_demand_side_outlet_node_name(self):
        """Get loop_demand_side_outlet_node_name

        Returns:
            str: the value of `loop_demand_side_outlet_node_name` or None if not set
        """
        return self._data["Loop Demand Side Outlet Node Name"]

    @loop_demand_side_outlet_node_name.setter
    def loop_demand_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `loop_demand_side_outlet_node_name`
        This connection is to the demand side of a loop

        Args:
            value (str): value for IDD Field `loop_demand_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `loop_demand_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_demand_side_outlet_node_name`')

        self._data["Loop Demand Side Outlet Node Name"] = value

    @property
    def loop_demand_side_design_flow_rate(self):
        """Get loop_demand_side_design_flow_rate

        Returns:
            float: the value of `loop_demand_side_design_flow_rate` or None if not set
        """
        return self._data["Loop Demand Side Design Flow Rate"]

    @loop_demand_side_design_flow_rate.setter
    def loop_demand_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `loop_demand_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `loop_demand_side_design_flow_rate`
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
                                 'for field `loop_demand_side_design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `loop_demand_side_design_flow_rate`')

        self._data["Loop Demand Side Design Flow Rate"] = value

    @property
    def loop_supply_side_inlet_node_name(self):
        """Get loop_supply_side_inlet_node_name

        Returns:
            str: the value of `loop_supply_side_inlet_node_name` or None if not set
        """
        return self._data["Loop Supply Side Inlet Node Name"]

    @loop_supply_side_inlet_node_name.setter
    def loop_supply_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `loop_supply_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `loop_supply_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `loop_supply_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_supply_side_inlet_node_name`')

        self._data["Loop Supply Side Inlet Node Name"] = value

    @property
    def loop_supply_side_outlet_node_name(self):
        """Get loop_supply_side_outlet_node_name

        Returns:
            str: the value of `loop_supply_side_outlet_node_name` or None if not set
        """
        return self._data["Loop Supply Side Outlet Node Name"]

    @loop_supply_side_outlet_node_name.setter
    def loop_supply_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `loop_supply_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `loop_supply_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `loop_supply_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_supply_side_outlet_node_name`')

        self._data["Loop Supply Side Outlet Node Name"] = value

    @property
    def loop_supply_side_design_flow_rate(self):
        """Get loop_supply_side_design_flow_rate

        Returns:
            float: the value of `loop_supply_side_design_flow_rate` or None if not set
        """
        return self._data["Loop Supply Side Design Flow Rate"]

    @loop_supply_side_design_flow_rate.setter
    def loop_supply_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `loop_supply_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `loop_supply_side_design_flow_rate`
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
                                 'for field `loop_supply_side_design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `loop_supply_side_design_flow_rate`')

        self._data["Loop Supply Side Design Flow Rate"] = value

    @property
    def heat_exchange_model_type(self):
        """Get heat_exchange_model_type

        Returns:
            str: the value of `heat_exchange_model_type` or None if not set
        """
        return self._data["Heat Exchange Model Type"]

    @heat_exchange_model_type.setter
    def heat_exchange_model_type(self, value="Ideal"):
        """  Corresponds to IDD Field `heat_exchange_model_type`

        Args:
            value (str): value for IDD Field `heat_exchange_model_type`
                Accepted values are:
                      - CrossFlowBothUnMixed
                      - CrossFlowBothMixed
                      - CrossFlowSupplyMixedDemandUnMixed
                      - CrossFlowSupplyUnMixedDemandMixed
                      - ParallelFlow
                      - CounterFlow
                      - Ideal
                Default value: Ideal
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_exchange_model_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchange_model_type`')
            vals = set()
            vals.add("CrossFlowBothUnMixed")
            vals.add("CrossFlowBothMixed")
            vals.add("CrossFlowSupplyMixedDemandUnMixed")
            vals.add("CrossFlowSupplyUnMixedDemandMixed")
            vals.add("ParallelFlow")
            vals.add("CounterFlow")
            vals.add("Ideal")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heat_exchange_model_type`'.format(value))

        self._data["Heat Exchange Model Type"] = value

    @property
    def heat_exchanger_ufactor_times_area_value(self):
        """Get heat_exchanger_ufactor_times_area_value

        Returns:
            float: the value of `heat_exchanger_ufactor_times_area_value` or None if not set
        """
        return self._data["Heat Exchanger U-Factor Times Area Value"]

    @heat_exchanger_ufactor_times_area_value.setter
    def heat_exchanger_ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `heat_exchanger_ufactor_times_area_value`

        Args:
            value (float): value for IDD Field `heat_exchanger_ufactor_times_area_value`
                Unit: W/k
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
                                 'for field `heat_exchanger_ufactor_times_area_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heat_exchanger_ufactor_times_area_value`')

        self._data["Heat Exchanger U-Factor Times Area Value"] = value

    @property
    def control_type(self):
        """Get control_type

        Returns:
            str: the value of `control_type` or None if not set
        """
        return self._data["Control Type"]

    @control_type.setter
    def control_type(self, value="UncontrolledOn"):
        """  Corresponds to IDD Field `control_type`

        Args:
            value (str): value for IDD Field `control_type`
                Accepted values are:
                      - UncontrolledOn
                      - OperationSchemeModulated
                      - OperationSchemeOnOff
                      - HeatingSetpointModulated
                      - HeatingSetpointOnOff
                      - CoolingSetpointModulated
                      - CoolingSetpointOnOff
                      - DualDeadbandSetpointModulated
                      - DualDeadbandSetpointOnOff
                      - CoolingDifferentialOnOff
                      - CoolingSetpointOnOffWithComponentOverride
                Default value: UncontrolledOn
                if `value` is None it will not be checked against the
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
            vals.add("UncontrolledOn")
            vals.add("OperationSchemeModulated")
            vals.add("OperationSchemeOnOff")
            vals.add("HeatingSetpointModulated")
            vals.add("HeatingSetpointOnOff")
            vals.add("CoolingSetpointModulated")
            vals.add("CoolingSetpointOnOff")
            vals.add("DualDeadbandSetpointModulated")
            vals.add("DualDeadbandSetpointOnOff")
            vals.add("CoolingDifferentialOnOff")
            vals.add("CoolingSetpointOnOffWithComponentOverride")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_type`'.format(value))

        self._data["Control Type"] = value

    @property
    def heat_exchanger_setpoint_node_name(self):
        """Get heat_exchanger_setpoint_node_name

        Returns:
            str: the value of `heat_exchanger_setpoint_node_name` or None if not set
        """
        return self._data["Heat Exchanger Setpoint Node Name"]

    @heat_exchanger_setpoint_node_name.setter
    def heat_exchanger_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `heat_exchanger_setpoint_node_name`
        Setpoint node is needed with any Control Type that is "*Setpoint*"

        Args:
            value (str): value for IDD Field `heat_exchanger_setpoint_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_exchanger_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchanger_setpoint_node_name`')

        self._data["Heat Exchanger Setpoint Node Name"] = value

    @property
    def minimum_temperature_difference_to_activate_heat_exchanger(self):
        """Get minimum_temperature_difference_to_activate_heat_exchanger

        Returns:
            float: the value of `minimum_temperature_difference_to_activate_heat_exchanger` or None if not set
        """
        return self._data["Minimum Temperature Difference to Activate Heat Exchanger"]

    @minimum_temperature_difference_to_activate_heat_exchanger.setter
    def minimum_temperature_difference_to_activate_heat_exchanger(self, value=0.01 ):
        """  Corresponds to IDD Field `minimum_temperature_difference_to_activate_heat_exchanger`
        Tolerance between control temperatures used to determine if heat exchanger should run.

        Args:
            value (float): value for IDD Field `minimum_temperature_difference_to_activate_heat_exchanger`
                Unit: deltaC
                Default value: 0.01
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_temperature_difference_to_activate_heat_exchanger`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_temperature_difference_to_activate_heat_exchanger`')
            if value > 50.0:
                raise ValueError('value need to be smaller 50.0 '
                                 'for field `minimum_temperature_difference_to_activate_heat_exchanger`')

        self._data["Minimum Temperature Difference to Activate Heat Exchanger"] = value

    @property
    def heat_transfer_metering_end_use_type(self):
        """Get heat_transfer_metering_end_use_type

        Returns:
            str: the value of `heat_transfer_metering_end_use_type` or None if not set
        """
        return self._data["Heat Transfer Metering End Use Type"]

    @heat_transfer_metering_end_use_type.setter
    def heat_transfer_metering_end_use_type(self, value="LoopToLoop"):
        """  Corresponds to IDD Field `heat_transfer_metering_end_use_type`
        This feild controls end use reporting for heat transfer meters

        Args:
            value (str): value for IDD Field `heat_transfer_metering_end_use_type`
                Accepted values are:
                      - FreeCooling
                      - HeatRecovery
                      - HeatRejection
                      - HeatRecoveryForCooling
                      - HeatRecoveryForHeating
                      - LoopToLoop
                Default value: LoopToLoop
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_transfer_metering_end_use_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_transfer_metering_end_use_type`')
            vals = set()
            vals.add("FreeCooling")
            vals.add("HeatRecovery")
            vals.add("HeatRejection")
            vals.add("HeatRecoveryForCooling")
            vals.add("HeatRecoveryForHeating")
            vals.add("LoopToLoop")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heat_transfer_metering_end_use_type`'.format(value))

        self._data["Heat Transfer Metering End Use Type"] = value

    @property
    def component_override_loop_supply_side_inlet_node_name(self):
        """Get component_override_loop_supply_side_inlet_node_name

        Returns:
            str: the value of `component_override_loop_supply_side_inlet_node_name` or None if not set
        """
        return self._data["Component Override Loop Supply Side Inlet Node Name"]

    @component_override_loop_supply_side_inlet_node_name.setter
    def component_override_loop_supply_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_override_loop_supply_side_inlet_node_name`
        This field is only used if Control Type is set to CoolingSetpointOnOffWithComponentOverride

        Args:
            value (str): value for IDD Field `component_override_loop_supply_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_override_loop_supply_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_override_loop_supply_side_inlet_node_name`')

        self._data["Component Override Loop Supply Side Inlet Node Name"] = value

    @property
    def component_override_loop_demand_side_inlet_node_name(self):
        """Get component_override_loop_demand_side_inlet_node_name

        Returns:
            str: the value of `component_override_loop_demand_side_inlet_node_name` or None if not set
        """
        return self._data["Component Override Loop Demand Side Inlet Node Name"]

    @component_override_loop_demand_side_inlet_node_name.setter
    def component_override_loop_demand_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_override_loop_demand_side_inlet_node_name`
        This field is only used if Control Type is set to CoolingSetpointOnOffWithComponentOverride

        Args:
            value (str): value for IDD Field `component_override_loop_demand_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_override_loop_demand_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_override_loop_demand_side_inlet_node_name`')

        self._data["Component Override Loop Demand Side Inlet Node Name"] = value

    @property
    def component_override_cooling_control_temperature_mode(self):
        """Get component_override_cooling_control_temperature_mode

        Returns:
            str: the value of `component_override_cooling_control_temperature_mode` or None if not set
        """
        return self._data["Component Override Cooling Control Temperature Mode"]

    @component_override_cooling_control_temperature_mode.setter
    def component_override_cooling_control_temperature_mode(self, value="Loop"):
        """  Corresponds to IDD Field `component_override_cooling_control_temperature_mode`
        This field is only used if Control Type is set to CoolingSetpointOnOffWithComponentOverride

        Args:
            value (str): value for IDD Field `component_override_cooling_control_temperature_mode`
                Accepted values are:
                      - WetBulbTemperature
                      - DryBulbTemperature
                      - Loop
                Default value: Loop
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_override_cooling_control_temperature_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_override_cooling_control_temperature_mode`')
            vals = set()
            vals.add("WetBulbTemperature")
            vals.add("DryBulbTemperature")
            vals.add("Loop")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_override_cooling_control_temperature_mode`'.format(value))

        self._data["Component Override Cooling Control Temperature Mode"] = value

    @property
    def sizing_factor(self):
        """Get sizing_factor

        Returns:
            float: the value of `sizing_factor` or None if not set
        """
        return self._data["Sizing Factor"]

    @sizing_factor.setter
    def sizing_factor(self, value=1.0 ):
        """  Corresponds to IDD Field `sizing_factor`
        Multiplies the autosized flow rates for this device

        Args:
            value (float): value for IDD Field `sizing_factor`
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
                                 'for field `sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `sizing_factor`')

        self._data["Sizing Factor"] = value

    @property
    def operation_minimum_temperature_limit(self):
        """Get operation_minimum_temperature_limit

        Returns:
            float: the value of `operation_minimum_temperature_limit` or None if not set
        """
        return self._data["Operation Minimum Temperature Limit"]

    @operation_minimum_temperature_limit.setter
    def operation_minimum_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `operation_minimum_temperature_limit`
        Lower limit on inlet temperatures, heat exchanger will not operate if either inlet is below this limit

        Args:
            value (float): value for IDD Field `operation_minimum_temperature_limit`
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
                                 'for field `operation_minimum_temperature_limit`'.format(value))

        self._data["Operation Minimum Temperature Limit"] = value

    @property
    def operation_maximum_temperature_limit(self):
        """Get operation_maximum_temperature_limit

        Returns:
            float: the value of `operation_maximum_temperature_limit` or None if not set
        """
        return self._data["Operation Maximum Temperature Limit"]

    @operation_maximum_temperature_limit.setter
    def operation_maximum_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `operation_maximum_temperature_limit`
        Upper limit on inlet temperatures, heat exchanger will not operate if either inlet is above this limit

        Args:
            value (float): value for IDD Field `operation_maximum_temperature_limit`
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
                                 'for field `operation_maximum_temperature_limit`'.format(value))

        self._data["Operation Maximum Temperature Limit"] = value

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
        out.append(self._to_str(self.loop_demand_side_inlet_node_name))
        out.append(self._to_str(self.loop_demand_side_outlet_node_name))
        out.append(self._to_str(self.loop_demand_side_design_flow_rate))
        out.append(self._to_str(self.loop_supply_side_inlet_node_name))
        out.append(self._to_str(self.loop_supply_side_outlet_node_name))
        out.append(self._to_str(self.loop_supply_side_design_flow_rate))
        out.append(self._to_str(self.heat_exchange_model_type))
        out.append(self._to_str(self.heat_exchanger_ufactor_times_area_value))
        out.append(self._to_str(self.control_type))
        out.append(self._to_str(self.heat_exchanger_setpoint_node_name))
        out.append(self._to_str(self.minimum_temperature_difference_to_activate_heat_exchanger))
        out.append(self._to_str(self.heat_transfer_metering_end_use_type))
        out.append(self._to_str(self.component_override_loop_supply_side_inlet_node_name))
        out.append(self._to_str(self.component_override_loop_demand_side_inlet_node_name))
        out.append(self._to_str(self.component_override_cooling_control_temperature_mode))
        out.append(self._to_str(self.sizing_factor))
        out.append(self._to_str(self.operation_minimum_temperature_limit))
        out.append(self._to_str(self.operation_maximum_temperature_limit))
        return ",".join(out)