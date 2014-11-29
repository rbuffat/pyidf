from collections import OrderedDict

class HeatPumpWaterToWaterEquationFitHeating(object):
    """ Corresponds to IDD object `HeatPump:WaterToWater:EquationFit:Heating`
        simple water-water hp curve-fit model
    """
    internal_name = "HeatPump:WaterToWater:EquationFit:Heating"
    field_count = 19

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatPump:WaterToWater:EquationFit:Heating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Source Side Inlet Node Name"] = None
        self._data["Source Side Outlet Node Name"] = None
        self._data["Load Side Inlet Node Name"] = None
        self._data["Load Side Outlet Node Name"] = None
        self._data["Rated Load Side Flow Rate"] = None
        self._data["Rated Source Side Flow Rate"] = None
        self._data["Rated Heating Capacity"] = None
        self._data["Rated Heating Power Consumption"] = None
        self._data["Heating Capacity Coefficient 1"] = None
        self._data["Heating Capacity Coefficient 2"] = None
        self._data["Heating Capacity Coefficient 3"] = None
        self._data["Heating Capacity Coefficient 4"] = None
        self._data["Heating Capacity Coefficient 5"] = None
        self._data["Heating Compressor Power Coefficient 1"] = None
        self._data["Heating Compressor Power Coefficient 2"] = None
        self._data["Heating Compressor Power Coefficient 3"] = None
        self._data["Heating Compressor Power Coefficient 4"] = None
        self._data["Heating Compressor Power Coefficient 5"] = None

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
            self.source_side_inlet_node_name = None
        else:
            self.source_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_outlet_node_name = None
        else:
            self.source_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_inlet_node_name = None
        else:
            self.load_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_outlet_node_name = None
        else:
            self.load_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_load_side_flow_rate = None
        else:
            self.rated_load_side_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_source_side_flow_rate = None
        else:
            self.rated_source_side_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_heating_capacity = None
        else:
            self.rated_heating_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_heating_power_consumption = None
        else:
            self.rated_heating_power_consumption = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_capacity_coefficient_1 = None
        else:
            self.heating_capacity_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_capacity_coefficient_2 = None
        else:
            self.heating_capacity_coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_capacity_coefficient_3 = None
        else:
            self.heating_capacity_coefficient_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_capacity_coefficient_4 = None
        else:
            self.heating_capacity_coefficient_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_capacity_coefficient_5 = None
        else:
            self.heating_capacity_coefficient_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_compressor_power_coefficient_1 = None
        else:
            self.heating_compressor_power_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_compressor_power_coefficient_2 = None
        else:
            self.heating_compressor_power_coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_compressor_power_coefficient_3 = None
        else:
            self.heating_compressor_power_coefficient_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_compressor_power_coefficient_4 = None
        else:
            self.heating_compressor_power_coefficient_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_compressor_power_coefficient_5 = None
        else:
            self.heating_compressor_power_coefficient_5 = vals[i]
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
    def source_side_inlet_node_name(self):
        """Get source_side_inlet_node_name

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set
        """
        return self._data["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_inlet_node_name`')

        self._data["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """Get source_side_outlet_node_name

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set
        """
        return self._data["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_outlet_node_name`')

        self._data["Source Side Outlet Node Name"] = value

    @property
    def load_side_inlet_node_name(self):
        """Get load_side_inlet_node_name

        Returns:
            str: the value of `load_side_inlet_node_name` or None if not set
        """
        return self._data["Load Side Inlet Node Name"]

    @load_side_inlet_node_name.setter
    def load_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `load_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `load_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `load_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_side_inlet_node_name`')

        self._data["Load Side Inlet Node Name"] = value

    @property
    def load_side_outlet_node_name(self):
        """Get load_side_outlet_node_name

        Returns:
            str: the value of `load_side_outlet_node_name` or None if not set
        """
        return self._data["Load Side Outlet Node Name"]

    @load_side_outlet_node_name.setter
    def load_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `load_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `load_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `load_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_side_outlet_node_name`')

        self._data["Load Side Outlet Node Name"] = value

    @property
    def rated_load_side_flow_rate(self):
        """Get rated_load_side_flow_rate

        Returns:
            float: the value of `rated_load_side_flow_rate` or None if not set
        """
        return self._data["Rated Load Side Flow Rate"]

    @rated_load_side_flow_rate.setter
    def rated_load_side_flow_rate(self, value=None):
        """  Corresponds to IDD Field `rated_load_side_flow_rate`

        Args:
            value (float): value for IDD Field `rated_load_side_flow_rate`
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
                                 'for field `rated_load_side_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_load_side_flow_rate`')

        self._data["Rated Load Side Flow Rate"] = value

    @property
    def rated_source_side_flow_rate(self):
        """Get rated_source_side_flow_rate

        Returns:
            float: the value of `rated_source_side_flow_rate` or None if not set
        """
        return self._data["Rated Source Side Flow Rate"]

    @rated_source_side_flow_rate.setter
    def rated_source_side_flow_rate(self, value=None):
        """  Corresponds to IDD Field `rated_source_side_flow_rate`

        Args:
            value (float): value for IDD Field `rated_source_side_flow_rate`
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
                                 'for field `rated_source_side_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_source_side_flow_rate`')

        self._data["Rated Source Side Flow Rate"] = value

    @property
    def rated_heating_capacity(self):
        """Get rated_heating_capacity

        Returns:
            float: the value of `rated_heating_capacity` or None if not set
        """
        return self._data["Rated Heating Capacity"]

    @rated_heating_capacity.setter
    def rated_heating_capacity(self, value=None):
        """  Corresponds to IDD Field `rated_heating_capacity`

        Args:
            value (float): value for IDD Field `rated_heating_capacity`
                Unit: W
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
                                 'for field `rated_heating_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_heating_capacity`')

        self._data["Rated Heating Capacity"] = value

    @property
    def rated_heating_power_consumption(self):
        """Get rated_heating_power_consumption

        Returns:
            float: the value of `rated_heating_power_consumption` or None if not set
        """
        return self._data["Rated Heating Power Consumption"]

    @rated_heating_power_consumption.setter
    def rated_heating_power_consumption(self, value=None):
        """  Corresponds to IDD Field `rated_heating_power_consumption`

        Args:
            value (float): value for IDD Field `rated_heating_power_consumption`
                Unit: W
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
                                 'for field `rated_heating_power_consumption`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_heating_power_consumption`')

        self._data["Rated Heating Power Consumption"] = value

    @property
    def heating_capacity_coefficient_1(self):
        """Get heating_capacity_coefficient_1

        Returns:
            float: the value of `heating_capacity_coefficient_1` or None if not set
        """
        return self._data["Heating Capacity Coefficient 1"]

    @heating_capacity_coefficient_1.setter
    def heating_capacity_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `heating_capacity_coefficient_1`

        Args:
            value (float): value for IDD Field `heating_capacity_coefficient_1`
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
                                 'for field `heating_capacity_coefficient_1`'.format(value))

        self._data["Heating Capacity Coefficient 1"] = value

    @property
    def heating_capacity_coefficient_2(self):
        """Get heating_capacity_coefficient_2

        Returns:
            float: the value of `heating_capacity_coefficient_2` or None if not set
        """
        return self._data["Heating Capacity Coefficient 2"]

    @heating_capacity_coefficient_2.setter
    def heating_capacity_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `heating_capacity_coefficient_2`

        Args:
            value (float): value for IDD Field `heating_capacity_coefficient_2`
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
                                 'for field `heating_capacity_coefficient_2`'.format(value))

        self._data["Heating Capacity Coefficient 2"] = value

    @property
    def heating_capacity_coefficient_3(self):
        """Get heating_capacity_coefficient_3

        Returns:
            float: the value of `heating_capacity_coefficient_3` or None if not set
        """
        return self._data["Heating Capacity Coefficient 3"]

    @heating_capacity_coefficient_3.setter
    def heating_capacity_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `heating_capacity_coefficient_3`

        Args:
            value (float): value for IDD Field `heating_capacity_coefficient_3`
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
                                 'for field `heating_capacity_coefficient_3`'.format(value))

        self._data["Heating Capacity Coefficient 3"] = value

    @property
    def heating_capacity_coefficient_4(self):
        """Get heating_capacity_coefficient_4

        Returns:
            float: the value of `heating_capacity_coefficient_4` or None if not set
        """
        return self._data["Heating Capacity Coefficient 4"]

    @heating_capacity_coefficient_4.setter
    def heating_capacity_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `heating_capacity_coefficient_4`

        Args:
            value (float): value for IDD Field `heating_capacity_coefficient_4`
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
                                 'for field `heating_capacity_coefficient_4`'.format(value))

        self._data["Heating Capacity Coefficient 4"] = value

    @property
    def heating_capacity_coefficient_5(self):
        """Get heating_capacity_coefficient_5

        Returns:
            float: the value of `heating_capacity_coefficient_5` or None if not set
        """
        return self._data["Heating Capacity Coefficient 5"]

    @heating_capacity_coefficient_5.setter
    def heating_capacity_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `heating_capacity_coefficient_5`

        Args:
            value (float): value for IDD Field `heating_capacity_coefficient_5`
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
                                 'for field `heating_capacity_coefficient_5`'.format(value))

        self._data["Heating Capacity Coefficient 5"] = value

    @property
    def heating_compressor_power_coefficient_1(self):
        """Get heating_compressor_power_coefficient_1

        Returns:
            float: the value of `heating_compressor_power_coefficient_1` or None if not set
        """
        return self._data["Heating Compressor Power Coefficient 1"]

    @heating_compressor_power_coefficient_1.setter
    def heating_compressor_power_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `heating_compressor_power_coefficient_1`

        Args:
            value (float): value for IDD Field `heating_compressor_power_coefficient_1`
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
                                 'for field `heating_compressor_power_coefficient_1`'.format(value))

        self._data["Heating Compressor Power Coefficient 1"] = value

    @property
    def heating_compressor_power_coefficient_2(self):
        """Get heating_compressor_power_coefficient_2

        Returns:
            float: the value of `heating_compressor_power_coefficient_2` or None if not set
        """
        return self._data["Heating Compressor Power Coefficient 2"]

    @heating_compressor_power_coefficient_2.setter
    def heating_compressor_power_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `heating_compressor_power_coefficient_2`

        Args:
            value (float): value for IDD Field `heating_compressor_power_coefficient_2`
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
                                 'for field `heating_compressor_power_coefficient_2`'.format(value))

        self._data["Heating Compressor Power Coefficient 2"] = value

    @property
    def heating_compressor_power_coefficient_3(self):
        """Get heating_compressor_power_coefficient_3

        Returns:
            float: the value of `heating_compressor_power_coefficient_3` or None if not set
        """
        return self._data["Heating Compressor Power Coefficient 3"]

    @heating_compressor_power_coefficient_3.setter
    def heating_compressor_power_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `heating_compressor_power_coefficient_3`

        Args:
            value (float): value for IDD Field `heating_compressor_power_coefficient_3`
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
                                 'for field `heating_compressor_power_coefficient_3`'.format(value))

        self._data["Heating Compressor Power Coefficient 3"] = value

    @property
    def heating_compressor_power_coefficient_4(self):
        """Get heating_compressor_power_coefficient_4

        Returns:
            float: the value of `heating_compressor_power_coefficient_4` or None if not set
        """
        return self._data["Heating Compressor Power Coefficient 4"]

    @heating_compressor_power_coefficient_4.setter
    def heating_compressor_power_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `heating_compressor_power_coefficient_4`

        Args:
            value (float): value for IDD Field `heating_compressor_power_coefficient_4`
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
                                 'for field `heating_compressor_power_coefficient_4`'.format(value))

        self._data["Heating Compressor Power Coefficient 4"] = value

    @property
    def heating_compressor_power_coefficient_5(self):
        """Get heating_compressor_power_coefficient_5

        Returns:
            float: the value of `heating_compressor_power_coefficient_5` or None if not set
        """
        return self._data["Heating Compressor Power Coefficient 5"]

    @heating_compressor_power_coefficient_5.setter
    def heating_compressor_power_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `heating_compressor_power_coefficient_5`

        Args:
            value (float): value for IDD Field `heating_compressor_power_coefficient_5`
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
                                 'for field `heating_compressor_power_coefficient_5`'.format(value))

        self._data["Heating Compressor Power Coefficient 5"] = value

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
        out.append(self._to_str(self.source_side_inlet_node_name))
        out.append(self._to_str(self.source_side_outlet_node_name))
        out.append(self._to_str(self.load_side_inlet_node_name))
        out.append(self._to_str(self.load_side_outlet_node_name))
        out.append(self._to_str(self.rated_load_side_flow_rate))
        out.append(self._to_str(self.rated_source_side_flow_rate))
        out.append(self._to_str(self.rated_heating_capacity))
        out.append(self._to_str(self.rated_heating_power_consumption))
        out.append(self._to_str(self.heating_capacity_coefficient_1))
        out.append(self._to_str(self.heating_capacity_coefficient_2))
        out.append(self._to_str(self.heating_capacity_coefficient_3))
        out.append(self._to_str(self.heating_capacity_coefficient_4))
        out.append(self._to_str(self.heating_capacity_coefficient_5))
        out.append(self._to_str(self.heating_compressor_power_coefficient_1))
        out.append(self._to_str(self.heating_compressor_power_coefficient_2))
        out.append(self._to_str(self.heating_compressor_power_coefficient_3))
        out.append(self._to_str(self.heating_compressor_power_coefficient_4))
        out.append(self._to_str(self.heating_compressor_power_coefficient_5))
        return ",".join(out)

class HeatPumpWaterToWaterEquationFitCooling(object):
    """ Corresponds to IDD object `HeatPump:WaterToWater:EquationFit:Cooling`
        simple water-water heatpump curve-fit model
    """
    internal_name = "HeatPump:WaterToWater:EquationFit:Cooling"
    field_count = 19

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatPump:WaterToWater:EquationFit:Cooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Source Side Inlet Node Name"] = None
        self._data["Source Side Outlet Node Name"] = None
        self._data["Load Side Inlet Node Name"] = None
        self._data["Load Side Outlet Node Name"] = None
        self._data["Rated Load Side Flow Rate"] = None
        self._data["Rated Source Side Flow Rate"] = None
        self._data["Rated Cooling Capacity"] = None
        self._data["Rated Cooling Power Consumption"] = None
        self._data["Cooling Capacity Coefficient 1"] = None
        self._data["Cooling Capacity Coefficient 2"] = None
        self._data["Cooling Capacity Coefficient 3"] = None
        self._data["Cooling Capacity Coefficient 4"] = None
        self._data["Cooling Capacity Coefficient 5"] = None
        self._data["Cooling Compressor Power Coefficient 1"] = None
        self._data["Cooling Compressor Power Coefficient 2"] = None
        self._data["Cooling Compressor Power Coefficient 3"] = None
        self._data["Cooling Compressor Power Coefficient 4"] = None
        self._data["Cooling Compressor Power Coefficient 5"] = None

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
            self.source_side_inlet_node_name = None
        else:
            self.source_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_outlet_node_name = None
        else:
            self.source_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_inlet_node_name = None
        else:
            self.load_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_outlet_node_name = None
        else:
            self.load_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_load_side_flow_rate = None
        else:
            self.rated_load_side_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_source_side_flow_rate = None
        else:
            self.rated_source_side_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_cooling_capacity = None
        else:
            self.rated_cooling_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_cooling_power_consumption = None
        else:
            self.rated_cooling_power_consumption = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_capacity_coefficient_1 = None
        else:
            self.cooling_capacity_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_capacity_coefficient_2 = None
        else:
            self.cooling_capacity_coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_capacity_coefficient_3 = None
        else:
            self.cooling_capacity_coefficient_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_capacity_coefficient_4 = None
        else:
            self.cooling_capacity_coefficient_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_capacity_coefficient_5 = None
        else:
            self.cooling_capacity_coefficient_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_compressor_power_coefficient_1 = None
        else:
            self.cooling_compressor_power_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_compressor_power_coefficient_2 = None
        else:
            self.cooling_compressor_power_coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_compressor_power_coefficient_3 = None
        else:
            self.cooling_compressor_power_coefficient_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_compressor_power_coefficient_4 = None
        else:
            self.cooling_compressor_power_coefficient_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_compressor_power_coefficient_5 = None
        else:
            self.cooling_compressor_power_coefficient_5 = vals[i]
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
    def source_side_inlet_node_name(self):
        """Get source_side_inlet_node_name

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set
        """
        return self._data["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_inlet_node_name`')

        self._data["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """Get source_side_outlet_node_name

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set
        """
        return self._data["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_outlet_node_name`')

        self._data["Source Side Outlet Node Name"] = value

    @property
    def load_side_inlet_node_name(self):
        """Get load_side_inlet_node_name

        Returns:
            str: the value of `load_side_inlet_node_name` or None if not set
        """
        return self._data["Load Side Inlet Node Name"]

    @load_side_inlet_node_name.setter
    def load_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `load_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `load_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `load_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_side_inlet_node_name`')

        self._data["Load Side Inlet Node Name"] = value

    @property
    def load_side_outlet_node_name(self):
        """Get load_side_outlet_node_name

        Returns:
            str: the value of `load_side_outlet_node_name` or None if not set
        """
        return self._data["Load Side Outlet Node Name"]

    @load_side_outlet_node_name.setter
    def load_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `load_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `load_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `load_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_side_outlet_node_name`')

        self._data["Load Side Outlet Node Name"] = value

    @property
    def rated_load_side_flow_rate(self):
        """Get rated_load_side_flow_rate

        Returns:
            float: the value of `rated_load_side_flow_rate` or None if not set
        """
        return self._data["Rated Load Side Flow Rate"]

    @rated_load_side_flow_rate.setter
    def rated_load_side_flow_rate(self, value=None):
        """  Corresponds to IDD Field `rated_load_side_flow_rate`

        Args:
            value (float): value for IDD Field `rated_load_side_flow_rate`
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
                                 'for field `rated_load_side_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_load_side_flow_rate`')

        self._data["Rated Load Side Flow Rate"] = value

    @property
    def rated_source_side_flow_rate(self):
        """Get rated_source_side_flow_rate

        Returns:
            float: the value of `rated_source_side_flow_rate` or None if not set
        """
        return self._data["Rated Source Side Flow Rate"]

    @rated_source_side_flow_rate.setter
    def rated_source_side_flow_rate(self, value=None):
        """  Corresponds to IDD Field `rated_source_side_flow_rate`

        Args:
            value (float): value for IDD Field `rated_source_side_flow_rate`
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
                                 'for field `rated_source_side_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_source_side_flow_rate`')

        self._data["Rated Source Side Flow Rate"] = value

    @property
    def rated_cooling_capacity(self):
        """Get rated_cooling_capacity

        Returns:
            float: the value of `rated_cooling_capacity` or None if not set
        """
        return self._data["Rated Cooling Capacity"]

    @rated_cooling_capacity.setter
    def rated_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `rated_cooling_capacity`

        Args:
            value (float): value for IDD Field `rated_cooling_capacity`
                Unit: W
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
                                 'for field `rated_cooling_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_cooling_capacity`')

        self._data["Rated Cooling Capacity"] = value

    @property
    def rated_cooling_power_consumption(self):
        """Get rated_cooling_power_consumption

        Returns:
            float: the value of `rated_cooling_power_consumption` or None if not set
        """
        return self._data["Rated Cooling Power Consumption"]

    @rated_cooling_power_consumption.setter
    def rated_cooling_power_consumption(self, value=None):
        """  Corresponds to IDD Field `rated_cooling_power_consumption`

        Args:
            value (float): value for IDD Field `rated_cooling_power_consumption`
                Unit: W
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
                                 'for field `rated_cooling_power_consumption`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_cooling_power_consumption`')

        self._data["Rated Cooling Power Consumption"] = value

    @property
    def cooling_capacity_coefficient_1(self):
        """Get cooling_capacity_coefficient_1

        Returns:
            float: the value of `cooling_capacity_coefficient_1` or None if not set
        """
        return self._data["Cooling Capacity Coefficient 1"]

    @cooling_capacity_coefficient_1.setter
    def cooling_capacity_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_coefficient_1`

        Args:
            value (float): value for IDD Field `cooling_capacity_coefficient_1`
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
                                 'for field `cooling_capacity_coefficient_1`'.format(value))

        self._data["Cooling Capacity Coefficient 1"] = value

    @property
    def cooling_capacity_coefficient_2(self):
        """Get cooling_capacity_coefficient_2

        Returns:
            float: the value of `cooling_capacity_coefficient_2` or None if not set
        """
        return self._data["Cooling Capacity Coefficient 2"]

    @cooling_capacity_coefficient_2.setter
    def cooling_capacity_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_coefficient_2`

        Args:
            value (float): value for IDD Field `cooling_capacity_coefficient_2`
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
                                 'for field `cooling_capacity_coefficient_2`'.format(value))

        self._data["Cooling Capacity Coefficient 2"] = value

    @property
    def cooling_capacity_coefficient_3(self):
        """Get cooling_capacity_coefficient_3

        Returns:
            float: the value of `cooling_capacity_coefficient_3` or None if not set
        """
        return self._data["Cooling Capacity Coefficient 3"]

    @cooling_capacity_coefficient_3.setter
    def cooling_capacity_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_coefficient_3`

        Args:
            value (float): value for IDD Field `cooling_capacity_coefficient_3`
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
                                 'for field `cooling_capacity_coefficient_3`'.format(value))

        self._data["Cooling Capacity Coefficient 3"] = value

    @property
    def cooling_capacity_coefficient_4(self):
        """Get cooling_capacity_coefficient_4

        Returns:
            float: the value of `cooling_capacity_coefficient_4` or None if not set
        """
        return self._data["Cooling Capacity Coefficient 4"]

    @cooling_capacity_coefficient_4.setter
    def cooling_capacity_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_coefficient_4`

        Args:
            value (float): value for IDD Field `cooling_capacity_coefficient_4`
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
                                 'for field `cooling_capacity_coefficient_4`'.format(value))

        self._data["Cooling Capacity Coefficient 4"] = value

    @property
    def cooling_capacity_coefficient_5(self):
        """Get cooling_capacity_coefficient_5

        Returns:
            float: the value of `cooling_capacity_coefficient_5` or None if not set
        """
        return self._data["Cooling Capacity Coefficient 5"]

    @cooling_capacity_coefficient_5.setter
    def cooling_capacity_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_coefficient_5`

        Args:
            value (float): value for IDD Field `cooling_capacity_coefficient_5`
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
                                 'for field `cooling_capacity_coefficient_5`'.format(value))

        self._data["Cooling Capacity Coefficient 5"] = value

    @property
    def cooling_compressor_power_coefficient_1(self):
        """Get cooling_compressor_power_coefficient_1

        Returns:
            float: the value of `cooling_compressor_power_coefficient_1` or None if not set
        """
        return self._data["Cooling Compressor Power Coefficient 1"]

    @cooling_compressor_power_coefficient_1.setter
    def cooling_compressor_power_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `cooling_compressor_power_coefficient_1`

        Args:
            value (float): value for IDD Field `cooling_compressor_power_coefficient_1`
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
                                 'for field `cooling_compressor_power_coefficient_1`'.format(value))

        self._data["Cooling Compressor Power Coefficient 1"] = value

    @property
    def cooling_compressor_power_coefficient_2(self):
        """Get cooling_compressor_power_coefficient_2

        Returns:
            float: the value of `cooling_compressor_power_coefficient_2` or None if not set
        """
        return self._data["Cooling Compressor Power Coefficient 2"]

    @cooling_compressor_power_coefficient_2.setter
    def cooling_compressor_power_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `cooling_compressor_power_coefficient_2`

        Args:
            value (float): value for IDD Field `cooling_compressor_power_coefficient_2`
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
                                 'for field `cooling_compressor_power_coefficient_2`'.format(value))

        self._data["Cooling Compressor Power Coefficient 2"] = value

    @property
    def cooling_compressor_power_coefficient_3(self):
        """Get cooling_compressor_power_coefficient_3

        Returns:
            float: the value of `cooling_compressor_power_coefficient_3` or None if not set
        """
        return self._data["Cooling Compressor Power Coefficient 3"]

    @cooling_compressor_power_coefficient_3.setter
    def cooling_compressor_power_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `cooling_compressor_power_coefficient_3`

        Args:
            value (float): value for IDD Field `cooling_compressor_power_coefficient_3`
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
                                 'for field `cooling_compressor_power_coefficient_3`'.format(value))

        self._data["Cooling Compressor Power Coefficient 3"] = value

    @property
    def cooling_compressor_power_coefficient_4(self):
        """Get cooling_compressor_power_coefficient_4

        Returns:
            float: the value of `cooling_compressor_power_coefficient_4` or None if not set
        """
        return self._data["Cooling Compressor Power Coefficient 4"]

    @cooling_compressor_power_coefficient_4.setter
    def cooling_compressor_power_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `cooling_compressor_power_coefficient_4`

        Args:
            value (float): value for IDD Field `cooling_compressor_power_coefficient_4`
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
                                 'for field `cooling_compressor_power_coefficient_4`'.format(value))

        self._data["Cooling Compressor Power Coefficient 4"] = value

    @property
    def cooling_compressor_power_coefficient_5(self):
        """Get cooling_compressor_power_coefficient_5

        Returns:
            float: the value of `cooling_compressor_power_coefficient_5` or None if not set
        """
        return self._data["Cooling Compressor Power Coefficient 5"]

    @cooling_compressor_power_coefficient_5.setter
    def cooling_compressor_power_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `cooling_compressor_power_coefficient_5`

        Args:
            value (float): value for IDD Field `cooling_compressor_power_coefficient_5`
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
                                 'for field `cooling_compressor_power_coefficient_5`'.format(value))

        self._data["Cooling Compressor Power Coefficient 5"] = value

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
        out.append(self._to_str(self.source_side_inlet_node_name))
        out.append(self._to_str(self.source_side_outlet_node_name))
        out.append(self._to_str(self.load_side_inlet_node_name))
        out.append(self._to_str(self.load_side_outlet_node_name))
        out.append(self._to_str(self.rated_load_side_flow_rate))
        out.append(self._to_str(self.rated_source_side_flow_rate))
        out.append(self._to_str(self.rated_cooling_capacity))
        out.append(self._to_str(self.rated_cooling_power_consumption))
        out.append(self._to_str(self.cooling_capacity_coefficient_1))
        out.append(self._to_str(self.cooling_capacity_coefficient_2))
        out.append(self._to_str(self.cooling_capacity_coefficient_3))
        out.append(self._to_str(self.cooling_capacity_coefficient_4))
        out.append(self._to_str(self.cooling_capacity_coefficient_5))
        out.append(self._to_str(self.cooling_compressor_power_coefficient_1))
        out.append(self._to_str(self.cooling_compressor_power_coefficient_2))
        out.append(self._to_str(self.cooling_compressor_power_coefficient_3))
        out.append(self._to_str(self.cooling_compressor_power_coefficient_4))
        out.append(self._to_str(self.cooling_compressor_power_coefficient_5))
        return ",".join(out)

class HeatPumpWaterToWaterParameterEstimationCooling(object):
    """ Corresponds to IDD object `HeatPump:WaterToWater:ParameterEstimation:Cooling`
        OSU parameter estimation model
    """
    internal_name = "HeatPump:WaterToWater:ParameterEstimation:Cooling"
    field_count = 22

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatPump:WaterToWater:ParameterEstimation:Cooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Source Side Inlet Node Name"] = None
        self._data["Source Side Outlet Node Name"] = None
        self._data["Load Side Inlet Node Name"] = None
        self._data["Load Side Outlet Node Name"] = None
        self._data["Nominal COP"] = None
        self._data["Nominal Capacity"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Load Side Flow Rate"] = None
        self._data["Source Side Flow Rate"] = None
        self._data["Load Side Heat Transfer Coefficient"] = None
        self._data["Source Side Heat Transfer Coefficient"] = None
        self._data["Piston Displacement"] = None
        self._data["Compressor Clearance Factor"] = None
        self._data["Compressor Suction and Discharge Pressure Drop"] = None
        self._data["Superheating"] = None
        self._data["Constant Part of Electromechanical Power Losses"] = None
        self._data["Loss Factor"] = None
        self._data["High Pressure Cut Off"] = None
        self._data["Low Pressure Cut Off"] = None

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
            self.source_side_inlet_node_name = None
        else:
            self.source_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_outlet_node_name = None
        else:
            self.source_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_inlet_node_name = None
        else:
            self.load_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_outlet_node_name = None
        else:
            self.load_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_cop = None
        else:
            self.nominal_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_part_load_ratio = None
        else:
            self.minimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_part_load_ratio = None
        else:
            self.maximum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optimum_part_load_ratio = None
        else:
            self.optimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_flow_rate = None
        else:
            self.load_side_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_flow_rate = None
        else:
            self.source_side_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_heat_transfer_coefficient = None
        else:
            self.load_side_heat_transfer_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_heat_transfer_coefficient = None
        else:
            self.source_side_heat_transfer_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.piston_displacement = None
        else:
            self.piston_displacement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compressor_clearance_factor = None
        else:
            self.compressor_clearance_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compressor_suction_and_discharge_pressure_drop = None
        else:
            self.compressor_suction_and_discharge_pressure_drop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.superheating = None
        else:
            self.superheating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_part_of_electromechanical_power_losses = None
        else:
            self.constant_part_of_electromechanical_power_losses = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.loss_factor = None
        else:
            self.loss_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_pressure_cut_off = None
        else:
            self.high_pressure_cut_off = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_pressure_cut_off = None
        else:
            self.low_pressure_cut_off = vals[i]
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
    def source_side_inlet_node_name(self):
        """Get source_side_inlet_node_name

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set
        """
        return self._data["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_inlet_node_name`')

        self._data["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """Get source_side_outlet_node_name

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set
        """
        return self._data["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_outlet_node_name`')

        self._data["Source Side Outlet Node Name"] = value

    @property
    def load_side_inlet_node_name(self):
        """Get load_side_inlet_node_name

        Returns:
            str: the value of `load_side_inlet_node_name` or None if not set
        """
        return self._data["Load Side Inlet Node Name"]

    @load_side_inlet_node_name.setter
    def load_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `load_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `load_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `load_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_side_inlet_node_name`')

        self._data["Load Side Inlet Node Name"] = value

    @property
    def load_side_outlet_node_name(self):
        """Get load_side_outlet_node_name

        Returns:
            str: the value of `load_side_outlet_node_name` or None if not set
        """
        return self._data["Load Side Outlet Node Name"]

    @load_side_outlet_node_name.setter
    def load_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `load_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `load_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `load_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_side_outlet_node_name`')

        self._data["Load Side Outlet Node Name"] = value

    @property
    def nominal_cop(self):
        """Get nominal_cop

        Returns:
            float: the value of `nominal_cop` or None if not set
        """
        return self._data["Nominal COP"]

    @nominal_cop.setter
    def nominal_cop(self, value=None):
        """  Corresponds to IDD Field `nominal_cop`

        Args:
            value (float): value for IDD Field `nominal_cop`
                Unit: W/W
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
                                 'for field `nominal_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_cop`')

        self._data["Nominal COP"] = value

    @property
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_capacity`

        Args:
            value (float): value for IDD Field `nominal_capacity`
                Unit: W
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
                                 'for field `nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_capacity`')

        self._data["Nominal Capacity"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_part_load_ratio`')

        self._data["Minimum Part Load Ratio"] = value

    @property
    def maximum_part_load_ratio(self):
        """Get maximum_part_load_ratio

        Returns:
            float: the value of `maximum_part_load_ratio` or None if not set
        """
        return self._data["Maximum Part Load Ratio"]

    @maximum_part_load_ratio.setter
    def maximum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `maximum_part_load_ratio`

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
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
                                 'for field `maximum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_part_load_ratio`')

        self._data["Maximum Part Load Ratio"] = value

    @property
    def optimum_part_load_ratio(self):
        """Get optimum_part_load_ratio

        Returns:
            float: the value of `optimum_part_load_ratio` or None if not set
        """
        return self._data["Optimum Part Load Ratio"]

    @optimum_part_load_ratio.setter
    def optimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `optimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def load_side_flow_rate(self):
        """Get load_side_flow_rate

        Returns:
            float: the value of `load_side_flow_rate` or None if not set
        """
        return self._data["Load Side Flow Rate"]

    @load_side_flow_rate.setter
    def load_side_flow_rate(self, value=None):
        """  Corresponds to IDD Field `load_side_flow_rate`

        Args:
            value (float): value for IDD Field `load_side_flow_rate`
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
                                 'for field `load_side_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `load_side_flow_rate`')

        self._data["Load Side Flow Rate"] = value

    @property
    def source_side_flow_rate(self):
        """Get source_side_flow_rate

        Returns:
            float: the value of `source_side_flow_rate` or None if not set
        """
        return self._data["Source Side Flow Rate"]

    @source_side_flow_rate.setter
    def source_side_flow_rate(self, value=None):
        """  Corresponds to IDD Field `source_side_flow_rate`

        Args:
            value (float): value for IDD Field `source_side_flow_rate`
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
                                 'for field `source_side_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `source_side_flow_rate`')

        self._data["Source Side Flow Rate"] = value

    @property
    def load_side_heat_transfer_coefficient(self):
        """Get load_side_heat_transfer_coefficient

        Returns:
            float: the value of `load_side_heat_transfer_coefficient` or None if not set
        """
        return self._data["Load Side Heat Transfer Coefficient"]

    @load_side_heat_transfer_coefficient.setter
    def load_side_heat_transfer_coefficient(self, value=None):
        """  Corresponds to IDD Field `load_side_heat_transfer_coefficient`

        Args:
            value (float): value for IDD Field `load_side_heat_transfer_coefficient`
                Unit: W/K
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
                                 'for field `load_side_heat_transfer_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `load_side_heat_transfer_coefficient`')

        self._data["Load Side Heat Transfer Coefficient"] = value

    @property
    def source_side_heat_transfer_coefficient(self):
        """Get source_side_heat_transfer_coefficient

        Returns:
            float: the value of `source_side_heat_transfer_coefficient` or None if not set
        """
        return self._data["Source Side Heat Transfer Coefficient"]

    @source_side_heat_transfer_coefficient.setter
    def source_side_heat_transfer_coefficient(self, value=None):
        """  Corresponds to IDD Field `source_side_heat_transfer_coefficient`

        Args:
            value (float): value for IDD Field `source_side_heat_transfer_coefficient`
                Unit: W/K
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
                                 'for field `source_side_heat_transfer_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `source_side_heat_transfer_coefficient`')

        self._data["Source Side Heat Transfer Coefficient"] = value

    @property
    def piston_displacement(self):
        """Get piston_displacement

        Returns:
            float: the value of `piston_displacement` or None if not set
        """
        return self._data["Piston Displacement"]

    @piston_displacement.setter
    def piston_displacement(self, value=None):
        """  Corresponds to IDD Field `piston_displacement`

        Args:
            value (float): value for IDD Field `piston_displacement`
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
                                 'for field `piston_displacement`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `piston_displacement`')

        self._data["Piston Displacement"] = value

    @property
    def compressor_clearance_factor(self):
        """Get compressor_clearance_factor

        Returns:
            float: the value of `compressor_clearance_factor` or None if not set
        """
        return self._data["Compressor Clearance Factor"]

    @compressor_clearance_factor.setter
    def compressor_clearance_factor(self, value=None):
        """  Corresponds to IDD Field `compressor_clearance_factor`

        Args:
            value (float): value for IDD Field `compressor_clearance_factor`
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
                                 'for field `compressor_clearance_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `compressor_clearance_factor`')

        self._data["Compressor Clearance Factor"] = value

    @property
    def compressor_suction_and_discharge_pressure_drop(self):
        """Get compressor_suction_and_discharge_pressure_drop

        Returns:
            float: the value of `compressor_suction_and_discharge_pressure_drop` or None if not set
        """
        return self._data["Compressor Suction and Discharge Pressure Drop"]

    @compressor_suction_and_discharge_pressure_drop.setter
    def compressor_suction_and_discharge_pressure_drop(self, value=None):
        """  Corresponds to IDD Field `compressor_suction_and_discharge_pressure_drop`

        Args:
            value (float): value for IDD Field `compressor_suction_and_discharge_pressure_drop`
                Unit: Pa
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
                                 'for field `compressor_suction_and_discharge_pressure_drop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `compressor_suction_and_discharge_pressure_drop`')

        self._data["Compressor Suction and Discharge Pressure Drop"] = value

    @property
    def superheating(self):
        """Get superheating

        Returns:
            float: the value of `superheating` or None if not set
        """
        return self._data["Superheating"]

    @superheating.setter
    def superheating(self, value=None):
        """  Corresponds to IDD Field `superheating`

        Args:
            value (float): value for IDD Field `superheating`
                Unit: C
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
                                 'for field `superheating`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `superheating`')

        self._data["Superheating"] = value

    @property
    def constant_part_of_electromechanical_power_losses(self):
        """Get constant_part_of_electromechanical_power_losses

        Returns:
            float: the value of `constant_part_of_electromechanical_power_losses` or None if not set
        """
        return self._data["Constant Part of Electromechanical Power Losses"]

    @constant_part_of_electromechanical_power_losses.setter
    def constant_part_of_electromechanical_power_losses(self, value=None):
        """  Corresponds to IDD Field `constant_part_of_electromechanical_power_losses`

        Args:
            value (float): value for IDD Field `constant_part_of_electromechanical_power_losses`
                Unit: W
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
                                 'for field `constant_part_of_electromechanical_power_losses`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `constant_part_of_electromechanical_power_losses`')

        self._data["Constant Part of Electromechanical Power Losses"] = value

    @property
    def loss_factor(self):
        """Get loss_factor

        Returns:
            float: the value of `loss_factor` or None if not set
        """
        return self._data["Loss Factor"]

    @loss_factor.setter
    def loss_factor(self, value=None):
        """  Corresponds to IDD Field `loss_factor`
        Used to define electromechanical loss that is proportional
        to the theoretical power %

        Args:
            value (float): value for IDD Field `loss_factor`
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
                                 'for field `loss_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `loss_factor`')

        self._data["Loss Factor"] = value

    @property
    def high_pressure_cut_off(self):
        """Get high_pressure_cut_off

        Returns:
            float: the value of `high_pressure_cut_off` or None if not set
        """
        return self._data["High Pressure Cut Off"]

    @high_pressure_cut_off.setter
    def high_pressure_cut_off(self, value=500000000.0 ):
        """  Corresponds to IDD Field `high_pressure_cut_off`

        Args:
            value (float): value for IDD Field `high_pressure_cut_off`
                Unit: Pa
                Default value: 500000000.0
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
                                 'for field `high_pressure_cut_off`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `high_pressure_cut_off`')

        self._data["High Pressure Cut Off"] = value

    @property
    def low_pressure_cut_off(self):
        """Get low_pressure_cut_off

        Returns:
            float: the value of `low_pressure_cut_off` or None if not set
        """
        return self._data["Low Pressure Cut Off"]

    @low_pressure_cut_off.setter
    def low_pressure_cut_off(self, value=0.0 ):
        """  Corresponds to IDD Field `low_pressure_cut_off`

        Args:
            value (float): value for IDD Field `low_pressure_cut_off`
                Unit: Pa
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
                                 'for field `low_pressure_cut_off`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `low_pressure_cut_off`')

        self._data["Low Pressure Cut Off"] = value

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
        out.append(self._to_str(self.source_side_inlet_node_name))
        out.append(self._to_str(self.source_side_outlet_node_name))
        out.append(self._to_str(self.load_side_inlet_node_name))
        out.append(self._to_str(self.load_side_outlet_node_name))
        out.append(self._to_str(self.nominal_cop))
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.load_side_flow_rate))
        out.append(self._to_str(self.source_side_flow_rate))
        out.append(self._to_str(self.load_side_heat_transfer_coefficient))
        out.append(self._to_str(self.source_side_heat_transfer_coefficient))
        out.append(self._to_str(self.piston_displacement))
        out.append(self._to_str(self.compressor_clearance_factor))
        out.append(self._to_str(self.compressor_suction_and_discharge_pressure_drop))
        out.append(self._to_str(self.superheating))
        out.append(self._to_str(self.constant_part_of_electromechanical_power_losses))
        out.append(self._to_str(self.loss_factor))
        out.append(self._to_str(self.high_pressure_cut_off))
        out.append(self._to_str(self.low_pressure_cut_off))
        return ",".join(out)

class HeatPumpWaterToWaterParameterEstimationHeating(object):
    """ Corresponds to IDD object `HeatPump:WaterToWater:ParameterEstimation:Heating`
        OSU parameter estimation model
    """
    internal_name = "HeatPump:WaterToWater:ParameterEstimation:Heating"
    field_count = 22

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatPump:WaterToWater:ParameterEstimation:Heating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Source Side Inlet Node Name"] = None
        self._data["Source Side Outlet Node Name"] = None
        self._data["Load Side Inlet Node Name"] = None
        self._data["Load Side Outlet Node Name"] = None
        self._data["Nominal COP"] = None
        self._data["Nominal Capacity"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Load Side Flow Rate"] = None
        self._data["Source Side Flow Rate"] = None
        self._data["Load Side Heat Transfer Coefficient"] = None
        self._data["Source Side Heat Transfer Coefficient"] = None
        self._data["Piston Displacement"] = None
        self._data["Compressor Clearance Factor"] = None
        self._data["Compressor Suction and Discharge Pressure Drop"] = None
        self._data["Superheating"] = None
        self._data["Constant Part of Electromechanical Power Losses"] = None
        self._data["Loss Factor"] = None
        self._data["High Pressure Cut Off"] = None
        self._data["Low Pressure Cut Off"] = None

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
            self.source_side_inlet_node_name = None
        else:
            self.source_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_outlet_node_name = None
        else:
            self.source_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_inlet_node_name = None
        else:
            self.load_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_outlet_node_name = None
        else:
            self.load_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_cop = None
        else:
            self.nominal_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_part_load_ratio = None
        else:
            self.minimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_part_load_ratio = None
        else:
            self.maximum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optimum_part_load_ratio = None
        else:
            self.optimum_part_load_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_flow_rate = None
        else:
            self.load_side_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_flow_rate = None
        else:
            self.source_side_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_side_heat_transfer_coefficient = None
        else:
            self.load_side_heat_transfer_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_heat_transfer_coefficient = None
        else:
            self.source_side_heat_transfer_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.piston_displacement = None
        else:
            self.piston_displacement = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compressor_clearance_factor = None
        else:
            self.compressor_clearance_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compressor_suction_and_discharge_pressure_drop = None
        else:
            self.compressor_suction_and_discharge_pressure_drop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.superheating = None
        else:
            self.superheating = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_part_of_electromechanical_power_losses = None
        else:
            self.constant_part_of_electromechanical_power_losses = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.loss_factor = None
        else:
            self.loss_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_pressure_cut_off = None
        else:
            self.high_pressure_cut_off = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_pressure_cut_off = None
        else:
            self.low_pressure_cut_off = vals[i]
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
    def source_side_inlet_node_name(self):
        """Get source_side_inlet_node_name

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set
        """
        return self._data["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_inlet_node_name`')

        self._data["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """Get source_side_outlet_node_name

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set
        """
        return self._data["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_outlet_node_name`')

        self._data["Source Side Outlet Node Name"] = value

    @property
    def load_side_inlet_node_name(self):
        """Get load_side_inlet_node_name

        Returns:
            str: the value of `load_side_inlet_node_name` or None if not set
        """
        return self._data["Load Side Inlet Node Name"]

    @load_side_inlet_node_name.setter
    def load_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `load_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `load_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `load_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_side_inlet_node_name`')

        self._data["Load Side Inlet Node Name"] = value

    @property
    def load_side_outlet_node_name(self):
        """Get load_side_outlet_node_name

        Returns:
            str: the value of `load_side_outlet_node_name` or None if not set
        """
        return self._data["Load Side Outlet Node Name"]

    @load_side_outlet_node_name.setter
    def load_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `load_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `load_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `load_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_side_outlet_node_name`')

        self._data["Load Side Outlet Node Name"] = value

    @property
    def nominal_cop(self):
        """Get nominal_cop

        Returns:
            float: the value of `nominal_cop` or None if not set
        """
        return self._data["Nominal COP"]

    @nominal_cop.setter
    def nominal_cop(self, value=None):
        """  Corresponds to IDD Field `nominal_cop`

        Args:
            value (float): value for IDD Field `nominal_cop`
                Unit: W/W
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
                                 'for field `nominal_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_cop`')

        self._data["Nominal COP"] = value

    @property
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_capacity`

        Args:
            value (float): value for IDD Field `nominal_capacity`
                Unit: W
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
                                 'for field `nominal_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_capacity`')

        self._data["Nominal Capacity"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_part_load_ratio`')

        self._data["Minimum Part Load Ratio"] = value

    @property
    def maximum_part_load_ratio(self):
        """Get maximum_part_load_ratio

        Returns:
            float: the value of `maximum_part_load_ratio` or None if not set
        """
        return self._data["Maximum Part Load Ratio"]

    @maximum_part_load_ratio.setter
    def maximum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `maximum_part_load_ratio`

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
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
                                 'for field `maximum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_part_load_ratio`')

        self._data["Maximum Part Load Ratio"] = value

    @property
    def optimum_part_load_ratio(self):
        """Get optimum_part_load_ratio

        Returns:
            float: the value of `optimum_part_load_ratio` or None if not set
        """
        return self._data["Optimum Part Load Ratio"]

    @optimum_part_load_ratio.setter
    def optimum_part_load_ratio(self, value=None):
        """  Corresponds to IDD Field `optimum_part_load_ratio`

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def load_side_flow_rate(self):
        """Get load_side_flow_rate

        Returns:
            float: the value of `load_side_flow_rate` or None if not set
        """
        return self._data["Load Side Flow Rate"]

    @load_side_flow_rate.setter
    def load_side_flow_rate(self, value=None):
        """  Corresponds to IDD Field `load_side_flow_rate`

        Args:
            value (float): value for IDD Field `load_side_flow_rate`
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
                                 'for field `load_side_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `load_side_flow_rate`')

        self._data["Load Side Flow Rate"] = value

    @property
    def source_side_flow_rate(self):
        """Get source_side_flow_rate

        Returns:
            float: the value of `source_side_flow_rate` or None if not set
        """
        return self._data["Source Side Flow Rate"]

    @source_side_flow_rate.setter
    def source_side_flow_rate(self, value=None):
        """  Corresponds to IDD Field `source_side_flow_rate`

        Args:
            value (float): value for IDD Field `source_side_flow_rate`
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
                                 'for field `source_side_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `source_side_flow_rate`')

        self._data["Source Side Flow Rate"] = value

    @property
    def load_side_heat_transfer_coefficient(self):
        """Get load_side_heat_transfer_coefficient

        Returns:
            float: the value of `load_side_heat_transfer_coefficient` or None if not set
        """
        return self._data["Load Side Heat Transfer Coefficient"]

    @load_side_heat_transfer_coefficient.setter
    def load_side_heat_transfer_coefficient(self, value=None):
        """  Corresponds to IDD Field `load_side_heat_transfer_coefficient`

        Args:
            value (float): value for IDD Field `load_side_heat_transfer_coefficient`
                Unit: W/K
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
                                 'for field `load_side_heat_transfer_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `load_side_heat_transfer_coefficient`')

        self._data["Load Side Heat Transfer Coefficient"] = value

    @property
    def source_side_heat_transfer_coefficient(self):
        """Get source_side_heat_transfer_coefficient

        Returns:
            float: the value of `source_side_heat_transfer_coefficient` or None if not set
        """
        return self._data["Source Side Heat Transfer Coefficient"]

    @source_side_heat_transfer_coefficient.setter
    def source_side_heat_transfer_coefficient(self, value=None):
        """  Corresponds to IDD Field `source_side_heat_transfer_coefficient`

        Args:
            value (float): value for IDD Field `source_side_heat_transfer_coefficient`
                Unit: W/K
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
                                 'for field `source_side_heat_transfer_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `source_side_heat_transfer_coefficient`')

        self._data["Source Side Heat Transfer Coefficient"] = value

    @property
    def piston_displacement(self):
        """Get piston_displacement

        Returns:
            float: the value of `piston_displacement` or None if not set
        """
        return self._data["Piston Displacement"]

    @piston_displacement.setter
    def piston_displacement(self, value=None):
        """  Corresponds to IDD Field `piston_displacement`

        Args:
            value (float): value for IDD Field `piston_displacement`
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
                                 'for field `piston_displacement`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `piston_displacement`')

        self._data["Piston Displacement"] = value

    @property
    def compressor_clearance_factor(self):
        """Get compressor_clearance_factor

        Returns:
            float: the value of `compressor_clearance_factor` or None if not set
        """
        return self._data["Compressor Clearance Factor"]

    @compressor_clearance_factor.setter
    def compressor_clearance_factor(self, value=None):
        """  Corresponds to IDD Field `compressor_clearance_factor`

        Args:
            value (float): value for IDD Field `compressor_clearance_factor`
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
                                 'for field `compressor_clearance_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `compressor_clearance_factor`')

        self._data["Compressor Clearance Factor"] = value

    @property
    def compressor_suction_and_discharge_pressure_drop(self):
        """Get compressor_suction_and_discharge_pressure_drop

        Returns:
            float: the value of `compressor_suction_and_discharge_pressure_drop` or None if not set
        """
        return self._data["Compressor Suction and Discharge Pressure Drop"]

    @compressor_suction_and_discharge_pressure_drop.setter
    def compressor_suction_and_discharge_pressure_drop(self, value=None):
        """  Corresponds to IDD Field `compressor_suction_and_discharge_pressure_drop`

        Args:
            value (float): value for IDD Field `compressor_suction_and_discharge_pressure_drop`
                Unit: Pa
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
                                 'for field `compressor_suction_and_discharge_pressure_drop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `compressor_suction_and_discharge_pressure_drop`')

        self._data["Compressor Suction and Discharge Pressure Drop"] = value

    @property
    def superheating(self):
        """Get superheating

        Returns:
            float: the value of `superheating` or None if not set
        """
        return self._data["Superheating"]

    @superheating.setter
    def superheating(self, value=None):
        """  Corresponds to IDD Field `superheating`

        Args:
            value (float): value for IDD Field `superheating`
                Unit: C
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
                                 'for field `superheating`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `superheating`')

        self._data["Superheating"] = value

    @property
    def constant_part_of_electromechanical_power_losses(self):
        """Get constant_part_of_electromechanical_power_losses

        Returns:
            float: the value of `constant_part_of_electromechanical_power_losses` or None if not set
        """
        return self._data["Constant Part of Electromechanical Power Losses"]

    @constant_part_of_electromechanical_power_losses.setter
    def constant_part_of_electromechanical_power_losses(self, value=None):
        """  Corresponds to IDD Field `constant_part_of_electromechanical_power_losses`

        Args:
            value (float): value for IDD Field `constant_part_of_electromechanical_power_losses`
                Unit: W
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
                                 'for field `constant_part_of_electromechanical_power_losses`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `constant_part_of_electromechanical_power_losses`')

        self._data["Constant Part of Electromechanical Power Losses"] = value

    @property
    def loss_factor(self):
        """Get loss_factor

        Returns:
            float: the value of `loss_factor` or None if not set
        """
        return self._data["Loss Factor"]

    @loss_factor.setter
    def loss_factor(self, value=None):
        """  Corresponds to IDD Field `loss_factor`
        Used to define electromechanical loss that is proportional
        to the theoretical power %

        Args:
            value (float): value for IDD Field `loss_factor`
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
                                 'for field `loss_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `loss_factor`')

        self._data["Loss Factor"] = value

    @property
    def high_pressure_cut_off(self):
        """Get high_pressure_cut_off

        Returns:
            float: the value of `high_pressure_cut_off` or None if not set
        """
        return self._data["High Pressure Cut Off"]

    @high_pressure_cut_off.setter
    def high_pressure_cut_off(self, value=500000000.0 ):
        """  Corresponds to IDD Field `high_pressure_cut_off`

        Args:
            value (float): value for IDD Field `high_pressure_cut_off`
                Unit: Pa
                Default value: 500000000.0
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
                                 'for field `high_pressure_cut_off`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `high_pressure_cut_off`')

        self._data["High Pressure Cut Off"] = value

    @property
    def low_pressure_cut_off(self):
        """Get low_pressure_cut_off

        Returns:
            float: the value of `low_pressure_cut_off` or None if not set
        """
        return self._data["Low Pressure Cut Off"]

    @low_pressure_cut_off.setter
    def low_pressure_cut_off(self, value=0.0 ):
        """  Corresponds to IDD Field `low_pressure_cut_off`

        Args:
            value (float): value for IDD Field `low_pressure_cut_off`
                Unit: Pa
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
                                 'for field `low_pressure_cut_off`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `low_pressure_cut_off`')

        self._data["Low Pressure Cut Off"] = value

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
        out.append(self._to_str(self.source_side_inlet_node_name))
        out.append(self._to_str(self.source_side_outlet_node_name))
        out.append(self._to_str(self.load_side_inlet_node_name))
        out.append(self._to_str(self.load_side_outlet_node_name))
        out.append(self._to_str(self.nominal_cop))
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.load_side_flow_rate))
        out.append(self._to_str(self.source_side_flow_rate))
        out.append(self._to_str(self.load_side_heat_transfer_coefficient))
        out.append(self._to_str(self.source_side_heat_transfer_coefficient))
        out.append(self._to_str(self.piston_displacement))
        out.append(self._to_str(self.compressor_clearance_factor))
        out.append(self._to_str(self.compressor_suction_and_discharge_pressure_drop))
        out.append(self._to_str(self.superheating))
        out.append(self._to_str(self.constant_part_of_electromechanical_power_losses))
        out.append(self._to_str(self.loss_factor))
        out.append(self._to_str(self.high_pressure_cut_off))
        out.append(self._to_str(self.low_pressure_cut_off))
        return ",".join(out)