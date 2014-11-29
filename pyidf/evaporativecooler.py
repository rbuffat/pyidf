from collections import OrderedDict

class EvaporativeCoolerDirectCelDekPad(object):
    """ Corresponds to IDD object `EvaporativeCooler:Direct:CelDekPad`
        Direct evaporative cooler with rigid media evaporative pad and recirculating water
        pump. This model has no controls other than its availability schedule.
    """
    internal_name = "EvaporativeCooler:Direct:CelDekPad"
    field_count = 9

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EvaporativeCooler:Direct:CelDekPad`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Direct Pad Area"] = None
        self._data["Direct Pad Depth"] = None
        self._data["Recirculating Water Pump Power Consumption"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None

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
            self.direct_pad_area = None
        else:
            self.direct_pad_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.direct_pad_depth = None
        else:
            self.direct_pad_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.recirculating_water_pump_power_consumption = None
        else:
            self.recirculating_water_pump_power_consumption = vals[i]
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
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
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
    def direct_pad_area(self):
        """Get direct_pad_area

        Returns:
            float: the value of `direct_pad_area` or None if not set
        """
        return self._data["Direct Pad Area"]

    @direct_pad_area.setter
    def direct_pad_area(self, value=None):
        """  Corresponds to IDD Field `direct_pad_area`

        Args:
            value (float): value for IDD Field `direct_pad_area`
                Unit: m2
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
                                 'for field `direct_pad_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `direct_pad_area`')

        self._data["Direct Pad Area"] = value

    @property
    def direct_pad_depth(self):
        """Get direct_pad_depth

        Returns:
            float: the value of `direct_pad_depth` or None if not set
        """
        return self._data["Direct Pad Depth"]

    @direct_pad_depth.setter
    def direct_pad_depth(self, value=None):
        """  Corresponds to IDD Field `direct_pad_depth`

        Args:
            value (float): value for IDD Field `direct_pad_depth`
                Unit: m
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
                                 'for field `direct_pad_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `direct_pad_depth`')

        self._data["Direct Pad Depth"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """Get recirculating_water_pump_power_consumption

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set
        """
        return self._data["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """  Corresponds to IDD Field `recirculating_water_pump_power_consumption`

        Args:
            value (float): value for IDD Field `recirculating_water_pump_power_consumption`
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
                                 'for field `recirculating_water_pump_power_consumption`'.format(value))

        self._data["Recirculating Water Pump Power Consumption"] = value

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
        This field is not currently used and can be left blank

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
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_outlet_node_name`
        This field is not currently used and can be left blank

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
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_outlet_node_name`
        This field is not currently used and can be left blank

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
        out.append(self._to_str(self.direct_pad_area))
        out.append(self._to_str(self.direct_pad_depth))
        out.append(self._to_str(self.recirculating_water_pump_power_consumption))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        return ",".join(out)

class EvaporativeCoolerIndirectCelDekPad(object):
    """ Corresponds to IDD object `EvaporativeCooler:Indirect:CelDekPad`
        Indirect evaporative cooler with rigid media evaporative pad, recirculating water
        pump, and secondary air fan. This model has no controls other than its availability
        schedule.
    """
    internal_name = "EvaporativeCooler:Indirect:CelDekPad"
    field_count = 14

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EvaporativeCooler:Indirect:CelDekPad`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Direct Pad Area"] = None
        self._data["Direct Pad Depth"] = None
        self._data["Recirculating Water Pump Power Consumption"] = None
        self._data["Secondary Fan Flow Rate"] = None
        self._data["Secondary Fan Total Efficiency"] = None
        self._data["Secondary Fan Delta Pressure"] = None
        self._data["Indirect Heat Exchanger Effectiveness"] = None
        self._data["Primary Air Inlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Secondary Air Inlet Node Name"] = None

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
            self.direct_pad_area = None
        else:
            self.direct_pad_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.direct_pad_depth = None
        else:
            self.direct_pad_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.recirculating_water_pump_power_consumption = None
        else:
            self.recirculating_water_pump_power_consumption = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_fan_flow_rate = None
        else:
            self.secondary_fan_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_fan_total_efficiency = None
        else:
            self.secondary_fan_total_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_fan_delta_pressure = None
        else:
            self.secondary_fan_delta_pressure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.indirect_heat_exchanger_effectiveness = None
        else:
            self.indirect_heat_exchanger_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_inlet_node_name = None
        else:
            self.primary_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_air_inlet_node_name = None
        else:
            self.secondary_air_inlet_node_name = vals[i]
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
    def direct_pad_area(self):
        """Get direct_pad_area

        Returns:
            float: the value of `direct_pad_area` or None if not set
        """
        return self._data["Direct Pad Area"]

    @direct_pad_area.setter
    def direct_pad_area(self, value=None):
        """  Corresponds to IDD Field `direct_pad_area`

        Args:
            value (float): value for IDD Field `direct_pad_area`
                Unit: m2
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
                                 'for field `direct_pad_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `direct_pad_area`')

        self._data["Direct Pad Area"] = value

    @property
    def direct_pad_depth(self):
        """Get direct_pad_depth

        Returns:
            float: the value of `direct_pad_depth` or None if not set
        """
        return self._data["Direct Pad Depth"]

    @direct_pad_depth.setter
    def direct_pad_depth(self, value=None):
        """  Corresponds to IDD Field `direct_pad_depth`

        Args:
            value (float): value for IDD Field `direct_pad_depth`
                Unit: m
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
                                 'for field `direct_pad_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `direct_pad_depth`')

        self._data["Direct Pad Depth"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """Get recirculating_water_pump_power_consumption

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set
        """
        return self._data["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """  Corresponds to IDD Field `recirculating_water_pump_power_consumption`

        Args:
            value (float): value for IDD Field `recirculating_water_pump_power_consumption`
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
                                 'for field `recirculating_water_pump_power_consumption`'.format(value))

        self._data["Recirculating Water Pump Power Consumption"] = value

    @property
    def secondary_fan_flow_rate(self):
        """Get secondary_fan_flow_rate

        Returns:
            float: the value of `secondary_fan_flow_rate` or None if not set
        """
        return self._data["Secondary Fan Flow Rate"]

    @secondary_fan_flow_rate.setter
    def secondary_fan_flow_rate(self, value=None):
        """  Corresponds to IDD Field `secondary_fan_flow_rate`

        Args:
            value (float): value for IDD Field `secondary_fan_flow_rate`
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
                                 'for field `secondary_fan_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `secondary_fan_flow_rate`')

        self._data["Secondary Fan Flow Rate"] = value

    @property
    def secondary_fan_total_efficiency(self):
        """Get secondary_fan_total_efficiency

        Returns:
            float: the value of `secondary_fan_total_efficiency` or None if not set
        """
        return self._data["Secondary Fan Total Efficiency"]

    @secondary_fan_total_efficiency.setter
    def secondary_fan_total_efficiency(self, value=None):
        """  Corresponds to IDD Field `secondary_fan_total_efficiency`

        Args:
            value (float): value for IDD Field `secondary_fan_total_efficiency`
                value > 0.0
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
                                 'for field `secondary_fan_total_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `secondary_fan_total_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `secondary_fan_total_efficiency`')

        self._data["Secondary Fan Total Efficiency"] = value

    @property
    def secondary_fan_delta_pressure(self):
        """Get secondary_fan_delta_pressure

        Returns:
            float: the value of `secondary_fan_delta_pressure` or None if not set
        """
        return self._data["Secondary Fan Delta Pressure"]

    @secondary_fan_delta_pressure.setter
    def secondary_fan_delta_pressure(self, value=None):
        """  Corresponds to IDD Field `secondary_fan_delta_pressure`

        Args:
            value (float): value for IDD Field `secondary_fan_delta_pressure`
                Unit: Pa
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
                                 'for field `secondary_fan_delta_pressure`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `secondary_fan_delta_pressure`')

        self._data["Secondary Fan Delta Pressure"] = value

    @property
    def indirect_heat_exchanger_effectiveness(self):
        """Get indirect_heat_exchanger_effectiveness

        Returns:
            float: the value of `indirect_heat_exchanger_effectiveness` or None if not set
        """
        return self._data["Indirect Heat Exchanger Effectiveness"]

    @indirect_heat_exchanger_effectiveness.setter
    def indirect_heat_exchanger_effectiveness(self, value=None):
        """  Corresponds to IDD Field `indirect_heat_exchanger_effectiveness`

        Args:
            value (float): value for IDD Field `indirect_heat_exchanger_effectiveness`
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
                                 'for field `indirect_heat_exchanger_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `indirect_heat_exchanger_effectiveness`')

        self._data["Indirect Heat Exchanger Effectiveness"] = value

    @property
    def primary_air_inlet_node_name(self):
        """Get primary_air_inlet_node_name

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set
        """
        return self._data["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `primary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_inlet_node_name`')

        self._data["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_outlet_node_name`
        This field is not currently used and can be left blank

        Args:
            value (str): value for IDD Field `primary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_outlet_node_name`')

        self._data["Primary Air Outlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_outlet_node_name`
        This field is not currently used and can be left blank

        Args:
            value (str): value for IDD Field `primary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_outlet_node_name`')

        self._data["Primary Air Outlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_outlet_node_name`
        This field is not currently used and can be left blank

        Args:
            value (str): value for IDD Field `primary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_outlet_node_name`')

        self._data["Primary Air Outlet Node Name"] = value

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
        Enter the name of an outdoor air node

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
        out.append(self._to_str(self.direct_pad_area))
        out.append(self._to_str(self.direct_pad_depth))
        out.append(self._to_str(self.recirculating_water_pump_power_consumption))
        out.append(self._to_str(self.secondary_fan_flow_rate))
        out.append(self._to_str(self.secondary_fan_total_efficiency))
        out.append(self._to_str(self.secondary_fan_delta_pressure))
        out.append(self._to_str(self.indirect_heat_exchanger_effectiveness))
        out.append(self._to_str(self.primary_air_inlet_node_name))
        out.append(self._to_str(self.primary_air_outlet_node_name))
        out.append(self._to_str(self.primary_air_outlet_node_name))
        out.append(self._to_str(self.primary_air_outlet_node_name))
        out.append(self._to_str(self.secondary_air_inlet_node_name))
        return ",".join(out)

class EvaporativeCoolerIndirectWetCoil(object):
    """ Corresponds to IDD object `EvaporativeCooler:Indirect:WetCoil`
        Indirect evaporative cooler with wetted coil, recirculating water pump, and secondary
        air fan. This model has no controls other than its availability schedule.
    """
    internal_name = "EvaporativeCooler:Indirect:WetCoil"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EvaporativeCooler:Indirect:WetCoil`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Coil Maximum Efficiency"] = None
        self._data["Coil Flow Ratio"] = None
        self._data["Recirculating Water Pump Power Consumption"] = None
        self._data["Secondary Fan Flow Rate"] = None
        self._data["Secondary Fan Total Efficiency"] = None
        self._data["Secondary Fan Delta Pressure"] = None
        self._data["Primary Air Inlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Secondary Air Inlet Node Name"] = None

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
            self.coil_maximum_efficiency = None
        else:
            self.coil_maximum_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coil_flow_ratio = None
        else:
            self.coil_flow_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.recirculating_water_pump_power_consumption = None
        else:
            self.recirculating_water_pump_power_consumption = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_fan_flow_rate = None
        else:
            self.secondary_fan_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_fan_total_efficiency = None
        else:
            self.secondary_fan_total_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_fan_delta_pressure = None
        else:
            self.secondary_fan_delta_pressure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_inlet_node_name = None
        else:
            self.primary_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_air_inlet_node_name = None
        else:
            self.secondary_air_inlet_node_name = vals[i]
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
    def coil_maximum_efficiency(self):
        """Get coil_maximum_efficiency

        Returns:
            float: the value of `coil_maximum_efficiency` or None if not set
        """
        return self._data["Coil Maximum Efficiency"]

    @coil_maximum_efficiency.setter
    def coil_maximum_efficiency(self, value=None):
        """  Corresponds to IDD Field `coil_maximum_efficiency`

        Args:
            value (float): value for IDD Field `coil_maximum_efficiency`
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
                                 'for field `coil_maximum_efficiency`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `coil_maximum_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `coil_maximum_efficiency`')

        self._data["Coil Maximum Efficiency"] = value

    @property
    def coil_flow_ratio(self):
        """Get coil_flow_ratio

        Returns:
            float: the value of `coil_flow_ratio` or None if not set
        """
        return self._data["Coil Flow Ratio"]

    @coil_flow_ratio.setter
    def coil_flow_ratio(self, value=None):
        """  Corresponds to IDD Field `coil_flow_ratio`

        Args:
            value (float): value for IDD Field `coil_flow_ratio`
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
                                 'for field `coil_flow_ratio`'.format(value))

        self._data["Coil Flow Ratio"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """Get recirculating_water_pump_power_consumption

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set
        """
        return self._data["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """  Corresponds to IDD Field `recirculating_water_pump_power_consumption`

        Args:
            value (float): value for IDD Field `recirculating_water_pump_power_consumption`
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
                                 'for field `recirculating_water_pump_power_consumption`'.format(value))

        self._data["Recirculating Water Pump Power Consumption"] = value

    @property
    def secondary_fan_flow_rate(self):
        """Get secondary_fan_flow_rate

        Returns:
            float: the value of `secondary_fan_flow_rate` or None if not set
        """
        return self._data["Secondary Fan Flow Rate"]

    @secondary_fan_flow_rate.setter
    def secondary_fan_flow_rate(self, value=None):
        """  Corresponds to IDD Field `secondary_fan_flow_rate`

        Args:
            value (float): value for IDD Field `secondary_fan_flow_rate`
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
                                 'for field `secondary_fan_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `secondary_fan_flow_rate`')

        self._data["Secondary Fan Flow Rate"] = value

    @property
    def secondary_fan_total_efficiency(self):
        """Get secondary_fan_total_efficiency

        Returns:
            float: the value of `secondary_fan_total_efficiency` or None if not set
        """
        return self._data["Secondary Fan Total Efficiency"]

    @secondary_fan_total_efficiency.setter
    def secondary_fan_total_efficiency(self, value=None):
        """  Corresponds to IDD Field `secondary_fan_total_efficiency`

        Args:
            value (float): value for IDD Field `secondary_fan_total_efficiency`
                value > 0.0
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
                                 'for field `secondary_fan_total_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `secondary_fan_total_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `secondary_fan_total_efficiency`')

        self._data["Secondary Fan Total Efficiency"] = value

    @property
    def secondary_fan_delta_pressure(self):
        """Get secondary_fan_delta_pressure

        Returns:
            float: the value of `secondary_fan_delta_pressure` or None if not set
        """
        return self._data["Secondary Fan Delta Pressure"]

    @secondary_fan_delta_pressure.setter
    def secondary_fan_delta_pressure(self, value=None):
        """  Corresponds to IDD Field `secondary_fan_delta_pressure`

        Args:
            value (float): value for IDD Field `secondary_fan_delta_pressure`
                Unit: Pa
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
                                 'for field `secondary_fan_delta_pressure`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `secondary_fan_delta_pressure`')

        self._data["Secondary Fan Delta Pressure"] = value

    @property
    def primary_air_inlet_node_name(self):
        """Get primary_air_inlet_node_name

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set
        """
        return self._data["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `primary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_inlet_node_name`')

        self._data["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_outlet_node_name`
        This field is not currently used and can be left blank

        Args:
            value (str): value for IDD Field `primary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_outlet_node_name`')

        self._data["Primary Air Outlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_outlet_node_name`
        This field is not currently used and can be left blank

        Args:
            value (str): value for IDD Field `primary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_outlet_node_name`')

        self._data["Primary Air Outlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_outlet_node_name`
        This field is not currently used and can be left blank

        Args:
            value (str): value for IDD Field `primary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_outlet_node_name`')

        self._data["Primary Air Outlet Node Name"] = value

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
        Enter the name of an outdoor air node

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
        out.append(self._to_str(self.coil_maximum_efficiency))
        out.append(self._to_str(self.coil_flow_ratio))
        out.append(self._to_str(self.recirculating_water_pump_power_consumption))
        out.append(self._to_str(self.secondary_fan_flow_rate))
        out.append(self._to_str(self.secondary_fan_total_efficiency))
        out.append(self._to_str(self.secondary_fan_delta_pressure))
        out.append(self._to_str(self.primary_air_inlet_node_name))
        out.append(self._to_str(self.primary_air_outlet_node_name))
        out.append(self._to_str(self.primary_air_outlet_node_name))
        out.append(self._to_str(self.primary_air_outlet_node_name))
        out.append(self._to_str(self.secondary_air_inlet_node_name))
        return ",".join(out)

class EvaporativeCoolerIndirectResearchSpecial(object):
    """ Corresponds to IDD object `EvaporativeCooler:Indirect:ResearchSpecial`
        Indirect evaporative cooler with user-specified effectiveness (can represent rigid pad
        or wetted coil), recirculating water pump, and secondary air fan. This model is
        controlled to meet the primary air outlet temperature setpoint.
    """
    internal_name = "EvaporativeCooler:Indirect:ResearchSpecial"
    field_count = 18

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EvaporativeCooler:Indirect:ResearchSpecial`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Cooler Maximum Effectiveness"] = None
        self._data["Cooler Flow Ratio"] = None
        self._data["Recirculating Water Pump Power Consumption"] = None
        self._data["Secondary Fan Flow Rate"] = None
        self._data["Secondary Fan Total Efficiency"] = None
        self._data["Secondary Fan Delta Pressure"] = None
        self._data["Primary Air Inlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Dewpoint Effectiveness Factor"] = None
        self._data["Dewpoint Effectiveness Factor"] = None
        self._data["Dewpoint Effectiveness Factor"] = None
        self._data["Dewpoint Effectiveness Factor"] = None
        self._data["Dewpoint Effectiveness Factor"] = None
        self._data["Drift Loss Fraction"] = None
        self._data["Blowdown Concentration Ratio"] = None

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
            self.cooler_maximum_effectiveness = None
        else:
            self.cooler_maximum_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooler_flow_ratio = None
        else:
            self.cooler_flow_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.recirculating_water_pump_power_consumption = None
        else:
            self.recirculating_water_pump_power_consumption = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_fan_flow_rate = None
        else:
            self.secondary_fan_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_fan_total_efficiency = None
        else:
            self.secondary_fan_total_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_fan_delta_pressure = None
        else:
            self.secondary_fan_delta_pressure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_inlet_node_name = None
        else:
            self.primary_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_effectiveness_factor = None
        else:
            self.dewpoint_effectiveness_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_effectiveness_factor = None
        else:
            self.dewpoint_effectiveness_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_effectiveness_factor = None
        else:
            self.dewpoint_effectiveness_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_effectiveness_factor = None
        else:
            self.dewpoint_effectiveness_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_effectiveness_factor = None
        else:
            self.dewpoint_effectiveness_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drift_loss_fraction = None
        else:
            self.drift_loss_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
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
    def cooler_maximum_effectiveness(self):
        """Get cooler_maximum_effectiveness

        Returns:
            float: the value of `cooler_maximum_effectiveness` or None if not set
        """
        return self._data["Cooler Maximum Effectiveness"]

    @cooler_maximum_effectiveness.setter
    def cooler_maximum_effectiveness(self, value=None):
        """  Corresponds to IDD Field `cooler_maximum_effectiveness`

        Args:
            value (float): value for IDD Field `cooler_maximum_effectiveness`
                value >= 0.0
                value <= 2.0
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
                                 'for field `cooler_maximum_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooler_maximum_effectiveness`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `cooler_maximum_effectiveness`')

        self._data["Cooler Maximum Effectiveness"] = value

    @property
    def cooler_flow_ratio(self):
        """Get cooler_flow_ratio

        Returns:
            float: the value of `cooler_flow_ratio` or None if not set
        """
        return self._data["Cooler Flow Ratio"]

    @cooler_flow_ratio.setter
    def cooler_flow_ratio(self, value=None):
        """  Corresponds to IDD Field `cooler_flow_ratio`

        Args:
            value (float): value for IDD Field `cooler_flow_ratio`
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
                                 'for field `cooler_flow_ratio`'.format(value))

        self._data["Cooler Flow Ratio"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """Get recirculating_water_pump_power_consumption

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set
        """
        return self._data["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """  Corresponds to IDD Field `recirculating_water_pump_power_consumption`

        Args:
            value (float): value for IDD Field `recirculating_water_pump_power_consumption`
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
                                 'for field `recirculating_water_pump_power_consumption`'.format(value))

        self._data["Recirculating Water Pump Power Consumption"] = value

    @property
    def secondary_fan_flow_rate(self):
        """Get secondary_fan_flow_rate

        Returns:
            float: the value of `secondary_fan_flow_rate` or None if not set
        """
        return self._data["Secondary Fan Flow Rate"]

    @secondary_fan_flow_rate.setter
    def secondary_fan_flow_rate(self, value=None):
        """  Corresponds to IDD Field `secondary_fan_flow_rate`

        Args:
            value (float): value for IDD Field `secondary_fan_flow_rate`
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
                                 'for field `secondary_fan_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `secondary_fan_flow_rate`')

        self._data["Secondary Fan Flow Rate"] = value

    @property
    def secondary_fan_total_efficiency(self):
        """Get secondary_fan_total_efficiency

        Returns:
            float: the value of `secondary_fan_total_efficiency` or None if not set
        """
        return self._data["Secondary Fan Total Efficiency"]

    @secondary_fan_total_efficiency.setter
    def secondary_fan_total_efficiency(self, value=None):
        """  Corresponds to IDD Field `secondary_fan_total_efficiency`

        Args:
            value (float): value for IDD Field `secondary_fan_total_efficiency`
                value > 0.0
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
                                 'for field `secondary_fan_total_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `secondary_fan_total_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `secondary_fan_total_efficiency`')

        self._data["Secondary Fan Total Efficiency"] = value

    @property
    def secondary_fan_delta_pressure(self):
        """Get secondary_fan_delta_pressure

        Returns:
            float: the value of `secondary_fan_delta_pressure` or None if not set
        """
        return self._data["Secondary Fan Delta Pressure"]

    @secondary_fan_delta_pressure.setter
    def secondary_fan_delta_pressure(self, value=None):
        """  Corresponds to IDD Field `secondary_fan_delta_pressure`

        Args:
            value (float): value for IDD Field `secondary_fan_delta_pressure`
                Unit: Pa
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
                                 'for field `secondary_fan_delta_pressure`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `secondary_fan_delta_pressure`')

        self._data["Secondary Fan Delta Pressure"] = value

    @property
    def primary_air_inlet_node_name(self):
        """Get primary_air_inlet_node_name

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set
        """
        return self._data["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `primary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_inlet_node_name`')

        self._data["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `primary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_outlet_node_name`')

        self._data["Primary Air Outlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `primary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_outlet_node_name`')

        self._data["Primary Air Outlet Node Name"] = value

    @property
    def dewpoint_effectiveness_factor(self):
        """Get dewpoint_effectiveness_factor

        Returns:
            str: the value of `dewpoint_effectiveness_factor` or None if not set
        """
        return self._data["Dewpoint Effectiveness Factor"]

    @dewpoint_effectiveness_factor.setter
    def dewpoint_effectiveness_factor(self, value=None):
        """  Corresponds to IDD Field `dewpoint_effectiveness_factor`

        Args:
            value (str): value for IDD Field `dewpoint_effectiveness_factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dewpoint_effectiveness_factor`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dewpoint_effectiveness_factor`')

        self._data["Dewpoint Effectiveness Factor"] = value

    @property
    def dewpoint_effectiveness_factor(self):
        """Get dewpoint_effectiveness_factor

        Returns:
            str: the value of `dewpoint_effectiveness_factor` or None if not set
        """
        return self._data["Dewpoint Effectiveness Factor"]

    @dewpoint_effectiveness_factor.setter
    def dewpoint_effectiveness_factor(self, value=None):
        """  Corresponds to IDD Field `dewpoint_effectiveness_factor`

        Args:
            value (str): value for IDD Field `dewpoint_effectiveness_factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dewpoint_effectiveness_factor`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dewpoint_effectiveness_factor`')

        self._data["Dewpoint Effectiveness Factor"] = value

    @property
    def dewpoint_effectiveness_factor(self):
        """Get dewpoint_effectiveness_factor

        Returns:
            str: the value of `dewpoint_effectiveness_factor` or None if not set
        """
        return self._data["Dewpoint Effectiveness Factor"]

    @dewpoint_effectiveness_factor.setter
    def dewpoint_effectiveness_factor(self, value=None):
        """  Corresponds to IDD Field `dewpoint_effectiveness_factor`

        Args:
            value (str): value for IDD Field `dewpoint_effectiveness_factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dewpoint_effectiveness_factor`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dewpoint_effectiveness_factor`')

        self._data["Dewpoint Effectiveness Factor"] = value

    @property
    def dewpoint_effectiveness_factor(self):
        """Get dewpoint_effectiveness_factor

        Returns:
            str: the value of `dewpoint_effectiveness_factor` or None if not set
        """
        return self._data["Dewpoint Effectiveness Factor"]

    @dewpoint_effectiveness_factor.setter
    def dewpoint_effectiveness_factor(self, value=None):
        """  Corresponds to IDD Field `dewpoint_effectiveness_factor`

        Args:
            value (str): value for IDD Field `dewpoint_effectiveness_factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dewpoint_effectiveness_factor`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dewpoint_effectiveness_factor`')

        self._data["Dewpoint Effectiveness Factor"] = value

    @property
    def dewpoint_effectiveness_factor(self):
        """Get dewpoint_effectiveness_factor

        Returns:
            str: the value of `dewpoint_effectiveness_factor` or None if not set
        """
        return self._data["Dewpoint Effectiveness Factor"]

    @dewpoint_effectiveness_factor.setter
    def dewpoint_effectiveness_factor(self, value=None):
        """  Corresponds to IDD Field `dewpoint_effectiveness_factor`

        Args:
            value (str): value for IDD Field `dewpoint_effectiveness_factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dewpoint_effectiveness_factor`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dewpoint_effectiveness_factor`')

        self._data["Dewpoint Effectiveness Factor"] = value

    @property
    def drift_loss_fraction(self):
        """Get drift_loss_fraction

        Returns:
            float: the value of `drift_loss_fraction` or None if not set
        """
        return self._data["Drift Loss Fraction"]

    @drift_loss_fraction.setter
    def drift_loss_fraction(self, value=None):
        """  Corresponds to IDD Field `drift_loss_fraction`
        Rate of drift loss as a fraction of evaporated water flow rate

        Args:
            value (float): value for IDD Field `drift_loss_fraction`
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
                                 'for field `drift_loss_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `drift_loss_fraction`')

        self._data["Drift Loss Fraction"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=None):
        """  Corresponds to IDD Field `blowdown_concentration_ratio`
        Characterizes the rate of blowdown in the evaporative cooler.
        Blowdown is water intentionally drained from the cooler in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        A typical value is 3.  If left blank then there is no blowdown.

        Args:
            value (float): value for IDD Field `blowdown_concentration_ratio`
                value >= 2.0
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
                                 'for field `blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `blowdown_concentration_ratio`')

        self._data["Blowdown Concentration Ratio"] = value

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
        out.append(self._to_str(self.cooler_maximum_effectiveness))
        out.append(self._to_str(self.cooler_flow_ratio))
        out.append(self._to_str(self.recirculating_water_pump_power_consumption))
        out.append(self._to_str(self.secondary_fan_flow_rate))
        out.append(self._to_str(self.secondary_fan_total_efficiency))
        out.append(self._to_str(self.secondary_fan_delta_pressure))
        out.append(self._to_str(self.primary_air_inlet_node_name))
        out.append(self._to_str(self.primary_air_outlet_node_name))
        out.append(self._to_str(self.primary_air_outlet_node_name))
        out.append(self._to_str(self.dewpoint_effectiveness_factor))
        out.append(self._to_str(self.dewpoint_effectiveness_factor))
        out.append(self._to_str(self.dewpoint_effectiveness_factor))
        out.append(self._to_str(self.dewpoint_effectiveness_factor))
        out.append(self._to_str(self.dewpoint_effectiveness_factor))
        out.append(self._to_str(self.drift_loss_fraction))
        out.append(self._to_str(self.blowdown_concentration_ratio))
        return ",".join(out)

class EvaporativeCoolerDirectResearchSpecial(object):
    """ Corresponds to IDD object `EvaporativeCooler:Direct:ResearchSpecial`
        Direct evaporative cooler with user-specified effectiveness (can represent rigid pad
        or similar media), and recirculating water pump, and secondary air fan. This model is
        controlled to meet the primary air outlet temperature setpoint.
    """
    internal_name = "EvaporativeCooler:Direct:ResearchSpecial"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EvaporativeCooler:Direct:ResearchSpecial`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Cooler Effectiveness"] = None
        self._data["Recirculating Water Pump Power Consumption"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Drift Loss Fraction"] = None
        self._data["Blowdown Concentration Ratio"] = None

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
            self.cooler_effectiveness = None
        else:
            self.cooler_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.recirculating_water_pump_power_consumption = None
        else:
            self.recirculating_water_pump_power_consumption = vals[i]
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
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drift_loss_fraction = None
        else:
            self.drift_loss_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
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
    def cooler_effectiveness(self):
        """Get cooler_effectiveness

        Returns:
            float: the value of `cooler_effectiveness` or None if not set
        """
        return self._data["Cooler Effectiveness"]

    @cooler_effectiveness.setter
    def cooler_effectiveness(self, value=None):
        """  Corresponds to IDD Field `cooler_effectiveness`
        effectiveness with respect to wetbulb depression

        Args:
            value (float): value for IDD Field `cooler_effectiveness`
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
                                 'for field `cooler_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooler_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `cooler_effectiveness`')

        self._data["Cooler Effectiveness"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """Get recirculating_water_pump_power_consumption

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set
        """
        return self._data["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """  Corresponds to IDD Field `recirculating_water_pump_power_consumption`

        Args:
            value (float): value for IDD Field `recirculating_water_pump_power_consumption`
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
                                 'for field `recirculating_water_pump_power_consumption`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `recirculating_water_pump_power_consumption`')

        self._data["Recirculating Water Pump Power Consumption"] = value

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
    def drift_loss_fraction(self):
        """Get drift_loss_fraction

        Returns:
            float: the value of `drift_loss_fraction` or None if not set
        """
        return self._data["Drift Loss Fraction"]

    @drift_loss_fraction.setter
    def drift_loss_fraction(self, value=None):
        """  Corresponds to IDD Field `drift_loss_fraction`
        Rate of drift loss as a fraction of evaporated water flow rate

        Args:
            value (float): value for IDD Field `drift_loss_fraction`
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
                                 'for field `drift_loss_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `drift_loss_fraction`')

        self._data["Drift Loss Fraction"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=None):
        """  Corresponds to IDD Field `blowdown_concentration_ratio`
        Characterizes the rate of blowdown in the evaporative cooler.
        Blowdown is water intentionally drained from the cooler in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        A typical value is 3. If left blank then there is no blowdown.

        Args:
            value (float): value for IDD Field `blowdown_concentration_ratio`
                value >= 2.0
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
                                 'for field `blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `blowdown_concentration_ratio`')

        self._data["Blowdown Concentration Ratio"] = value

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
        out.append(self._to_str(self.cooler_effectiveness))
        out.append(self._to_str(self.recirculating_water_pump_power_consumption))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.drift_loss_fraction))
        out.append(self._to_str(self.blowdown_concentration_ratio))
        return ",".join(out)