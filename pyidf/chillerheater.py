from collections import OrderedDict

class ChillerHeaterAbsorptionDirectFired(object):
    """ Corresponds to IDD object `ChillerHeater:Absorption:DirectFired`
        Direct fired gas absorption chiller-heater using performance curves similar to DOE-2
    """
    internal_name = "ChillerHeater:Absorption:DirectFired"
    field_count = 35

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ChillerHeater:Absorption:DirectFired`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Nominal Cooling Capacity"] = None
        self._data["Heating to Cooling Capacity Ratio"] = None
        self._data["Fuel Input to Cooling Output Ratio"] = None
        self._data["Fuel Input to Heating Output Ratio"] = None
        self._data["Electric Input to Cooling Output Ratio"] = None
        self._data["Electric Input to Heating Output Ratio"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Hot Water Inlet Node Name"] = None
        self._data["Hot Water Outlet Node Name"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Design Entering Condenser Water Temperature"] = None
        self._data["Design Leaving Chilled Water Temperature"] = None
        self._data["Design Chilled Water Flow Rate"] = None
        self._data["Design Condenser Water Flow Rate"] = None
        self._data["Design Hot Water Flow Rate"] = None
        self._data["Cooling Capacity Function of Temperature Curve Name"] = None
        self._data["Fuel Input to Cooling Output Ratio Function of Temperature Curve Name"] = None
        self._data["Fuel Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = None
        self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = None
        self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = None
        self._data["Heating Capacity Function of Cooling Capacity Curve Name"] = None
        self._data["Fuel Input to Heat Output Ratio During Heating Only Operation Curve Name"] = None
        self._data["Temperature Curve Input Variable"] = None
        self._data["Condenser Type"] = None
        self._data["Chilled Water Temperature Lower Limit"] = None
        self._data["Fuel Higher Heating Value"] = None
        self._data["Chiller Flow Mode"] = None
        self._data["Fuel Type"] = None
        self._data["Sizing Factor"] = None

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
            self.nominal_cooling_capacity = None
        else:
            self.nominal_cooling_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_to_cooling_capacity_ratio = None
        else:
            self.heating_to_cooling_capacity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_input_to_cooling_output_ratio = None
        else:
            self.fuel_input_to_cooling_output_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_input_to_heating_output_ratio = None
        else:
            self.fuel_input_to_heating_output_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_cooling_output_ratio = None
        else:
            self.electric_input_to_cooling_output_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_heating_output_ratio = None
        else:
            self.electric_input_to_heating_output_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hot_water_inlet_node_name = None
        else:
            self.hot_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hot_water_outlet_node_name = None
        else:
            self.hot_water_outlet_node_name = vals[i]
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
            self.design_entering_condenser_water_temperature = None
        else:
            self.design_entering_condenser_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_leaving_chilled_water_temperature = None
        else:
            self.design_leaving_chilled_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_flow_rate = None
        else:
            self.design_chilled_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_water_flow_rate = None
        else:
            self.design_condenser_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_hot_water_flow_rate = None
        else:
            self.design_hot_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_capacity_function_of_temperature_curve_name = None
        else:
            self.cooling_capacity_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name = None
        else:
            self.fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = None
        else:
            self.fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = None
        else:
            self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = None
        else:
            self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_capacity_function_of_cooling_capacity_curve_name = None
        else:
            self.heating_capacity_function_of_cooling_capacity_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name = None
        else:
            self.fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_curve_input_variable = None
        else:
            self.temperature_curve_input_variable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_temperature_lower_limit = None
        else:
            self.chilled_water_temperature_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_higher_heating_value = None
        else:
            self.fuel_higher_heating_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_flow_mode = None
        else:
            self.chiller_flow_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_type = None
        else:
            self.fuel_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
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
    def nominal_cooling_capacity(self):
        """Get nominal_cooling_capacity

        Returns:
            float: the value of `nominal_cooling_capacity` or None if not set
        """
        return self._data["Nominal Cooling Capacity"]

    @nominal_cooling_capacity.setter
    def nominal_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_cooling_capacity`

        Args:
            value (float): value for IDD Field `nominal_cooling_capacity`
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
                                 'for field `nominal_cooling_capacity`'.format(value))

        self._data["Nominal Cooling Capacity"] = value

    @property
    def heating_to_cooling_capacity_ratio(self):
        """Get heating_to_cooling_capacity_ratio

        Returns:
            float: the value of `heating_to_cooling_capacity_ratio` or None if not set
        """
        return self._data["Heating to Cooling Capacity Ratio"]

    @heating_to_cooling_capacity_ratio.setter
    def heating_to_cooling_capacity_ratio(self, value=0.8 ):
        """  Corresponds to IDD Field `heating_to_cooling_capacity_ratio`
        A positive fraction that represents the ratio of the
        heating capacity divided by the cooling capacity at rated conditions.

        Args:
            value (float): value for IDD Field `heating_to_cooling_capacity_ratio`
                Default value: 0.8
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
                                 'for field `heating_to_cooling_capacity_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_to_cooling_capacity_ratio`')

        self._data["Heating to Cooling Capacity Ratio"] = value

    @property
    def fuel_input_to_cooling_output_ratio(self):
        """Get fuel_input_to_cooling_output_ratio

        Returns:
            float: the value of `fuel_input_to_cooling_output_ratio` or None if not set
        """
        return self._data["Fuel Input to Cooling Output Ratio"]

    @fuel_input_to_cooling_output_ratio.setter
    def fuel_input_to_cooling_output_ratio(self, value=0.97 ):
        """  Corresponds to IDD Field `fuel_input_to_cooling_output_ratio`
        The positive fraction that represents the ratio of the
        instantaneous fuel used divided by the cooling capacity at rated conditions.

        Args:
            value (float): value for IDD Field `fuel_input_to_cooling_output_ratio`
                Default value: 0.97
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
                                 'for field `fuel_input_to_cooling_output_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `fuel_input_to_cooling_output_ratio`')

        self._data["Fuel Input to Cooling Output Ratio"] = value

    @property
    def fuel_input_to_heating_output_ratio(self):
        """Get fuel_input_to_heating_output_ratio

        Returns:
            float: the value of `fuel_input_to_heating_output_ratio` or None if not set
        """
        return self._data["Fuel Input to Heating Output Ratio"]

    @fuel_input_to_heating_output_ratio.setter
    def fuel_input_to_heating_output_ratio(self, value=1.25 ):
        """  Corresponds to IDD Field `fuel_input_to_heating_output_ratio`
        The positive fraction that represents the ratio of the
        instantaneous fuel used divided by the nominal heating capacity.

        Args:
            value (float): value for IDD Field `fuel_input_to_heating_output_ratio`
                Default value: 1.25
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
                                 'for field `fuel_input_to_heating_output_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fuel_input_to_heating_output_ratio`')

        self._data["Fuel Input to Heating Output Ratio"] = value

    @property
    def electric_input_to_cooling_output_ratio(self):
        """Get electric_input_to_cooling_output_ratio

        Returns:
            float: the value of `electric_input_to_cooling_output_ratio` or None if not set
        """
        return self._data["Electric Input to Cooling Output Ratio"]

    @electric_input_to_cooling_output_ratio.setter
    def electric_input_to_cooling_output_ratio(self, value=0.01 ):
        """  Corresponds to IDD Field `electric_input_to_cooling_output_ratio`
        The positive fraction that represents the ratio of the
        instantaneous electricity used divided by the cooling capacity at rated conditions.
        If the chiller is both heating and cooling only the cooling electricity is used.

        Args:
            value (float): value for IDD Field `electric_input_to_cooling_output_ratio`
                Default value: 0.01
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
                                 'for field `electric_input_to_cooling_output_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `electric_input_to_cooling_output_ratio`')

        self._data["Electric Input to Cooling Output Ratio"] = value

    @property
    def electric_input_to_heating_output_ratio(self):
        """Get electric_input_to_heating_output_ratio

        Returns:
            float: the value of `electric_input_to_heating_output_ratio` or None if not set
        """
        return self._data["Electric Input to Heating Output Ratio"]

    @electric_input_to_heating_output_ratio.setter
    def electric_input_to_heating_output_ratio(self, value=0.0 ):
        """  Corresponds to IDD Field `electric_input_to_heating_output_ratio`
        The positive fraction that represents the ratio of the
        instantaneous electricity used divided by the nominal heating capacity.
        If the chiller is both heating and cooling only the cooling electricity is used.

        Args:
            value (float): value for IDD Field `electric_input_to_heating_output_ratio`
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
                                 'for field `electric_input_to_heating_output_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `electric_input_to_heating_output_ratio`')

        self._data["Electric Input to Heating Output Ratio"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')

        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def hot_water_inlet_node_name(self):
        """Get hot_water_inlet_node_name

        Returns:
            str: the value of `hot_water_inlet_node_name` or None if not set
        """
        return self._data["Hot Water Inlet Node Name"]

    @hot_water_inlet_node_name.setter
    def hot_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `hot_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_inlet_node_name`')

        self._data["Hot Water Inlet Node Name"] = value

    @property
    def hot_water_outlet_node_name(self):
        """Get hot_water_outlet_node_name

        Returns:
            str: the value of `hot_water_outlet_node_name` or None if not set
        """
        return self._data["Hot Water Outlet Node Name"]

    @hot_water_outlet_node_name.setter
    def hot_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `hot_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_outlet_node_name`')

        self._data["Hot Water Outlet Node Name"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=0.1 ):
        """  Corresponds to IDD Field `minimum_part_load_ratio`
        The positive fraction that represents the minimum cooling output possible when
        operated continually at rated temperature conditions divided by the nominal
        cooling capacity at those same conditions.  If the load on the chiller is below
        this fraction the chiller will cycle.

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
                Default value: 0.1
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
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
    def maximum_part_load_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `maximum_part_load_ratio`
        The positive fraction that represents the maximum cooling output possible at
        rated temperature conditions divided by the nominal cooling capacity at those
        same conditions.  If greater than 1.0, the chiller is typically thought of as
        capable of being overloaded.

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
                Default value: 1.0
                value >= 0.5
                if `value` is None it will not be checked against the
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
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
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
    def optimum_part_load_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `optimum_part_load_ratio`
        The positive fraction that represents the optimal cooling output at rated
        temperature conditions divided by the nominal cooling capacity at those same
        conditions.  It represents the most desirable operating point for the chiller.

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def design_entering_condenser_water_temperature(self):
        """Get design_entering_condenser_water_temperature

        Returns:
            float: the value of `design_entering_condenser_water_temperature` or None if not set
        """
        return self._data["Design Entering Condenser Water Temperature"]

    @design_entering_condenser_water_temperature.setter
    def design_entering_condenser_water_temperature(self, value=29.0 ):
        """  Corresponds to IDD Field `design_entering_condenser_water_temperature`
        The temperature of the water entering the condenser of the chiller when
        operating at design conditions.  This is usually based on the temperature
        delivered by the cooling tower in a water cooled application.

        Args:
            value (float): value for IDD Field `design_entering_condenser_water_temperature`
                Unit: C
                Default value: 29.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_condenser_water_temperature`'.format(value))

        self._data["Design Entering Condenser Water Temperature"] = value

    @property
    def design_leaving_chilled_water_temperature(self):
        """Get design_leaving_chilled_water_temperature

        Returns:
            float: the value of `design_leaving_chilled_water_temperature` or None if not set
        """
        return self._data["Design Leaving Chilled Water Temperature"]

    @design_leaving_chilled_water_temperature.setter
    def design_leaving_chilled_water_temperature(self, value=7.0 ):
        """  Corresponds to IDD Field `design_leaving_chilled_water_temperature`
        The temperature of the water leaving the evaporator of the chiller when
        operating at design conditions also called the chilled water supply temperature
        or leaving chilled water temperature.

        Args:
            value (float): value for IDD Field `design_leaving_chilled_water_temperature`
                Unit: C
                Default value: 7.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_leaving_chilled_water_temperature`'.format(value))

        self._data["Design Leaving Chilled Water Temperature"] = value

    @property
    def design_chilled_water_flow_rate(self):
        """Get design_chilled_water_flow_rate

        Returns:
            float: the value of `design_chilled_water_flow_rate` or None if not set
        """
        return self._data["Design Chilled Water Flow Rate"]

    @design_chilled_water_flow_rate.setter
    def design_chilled_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_flow_rate`
        For variable volume this is the max flow & for constant flow this is the flow.

        Args:
            value (float): value for IDD Field `design_chilled_water_flow_rate`
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
                                 'for field `design_chilled_water_flow_rate`'.format(value))

        self._data["Design Chilled Water Flow Rate"] = value

    @property
    def design_condenser_water_flow_rate(self):
        """Get design_condenser_water_flow_rate

        Returns:
            float: the value of `design_condenser_water_flow_rate` or None if not set
        """
        return self._data["Design Condenser Water Flow Rate"]

    @design_condenser_water_flow_rate.setter
    def design_condenser_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_condenser_water_flow_rate`
        The water flow rate at design conditions through the condenser.
        This field is not used for Condenser Type = AirCooled

        Args:
            value (float): value for IDD Field `design_condenser_water_flow_rate`
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
                                 'for field `design_condenser_water_flow_rate`'.format(value))

        self._data["Design Condenser Water Flow Rate"] = value

    @property
    def design_hot_water_flow_rate(self):
        """Get design_hot_water_flow_rate

        Returns:
            float: the value of `design_hot_water_flow_rate` or None if not set
        """
        return self._data["Design Hot Water Flow Rate"]

    @design_hot_water_flow_rate.setter
    def design_hot_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_hot_water_flow_rate`
        The water flow rate at design conditions through the heater side.

        Args:
            value (float): value for IDD Field `design_hot_water_flow_rate`
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
                                 'for field `design_hot_water_flow_rate`'.format(value))

        self._data["Design Hot Water Flow Rate"] = value

    @property
    def cooling_capacity_function_of_temperature_curve_name(self):
        """Get cooling_capacity_function_of_temperature_curve_name

        Returns:
            str: the value of `cooling_capacity_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Cooling Capacity Function of Temperature Curve Name"]

    @cooling_capacity_function_of_temperature_curve_name.setter
    def cooling_capacity_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_function_of_temperature_curve_name`
        The CoolCapFT curve represents the fraction of the cooling capacity of the chiller as it
        varies by temperature.  The curve is normalized so that at design conditions the
        value of the curve should be 1.0.  This is a biquadratic curve with the
        input variables being the leaving chilled water temperature and either
        the entering or leaving condenser water temperature.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `cooling_capacity_function_of_temperature_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_capacity_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_capacity_function_of_temperature_curve_name`')

        self._data["Cooling Capacity Function of Temperature Curve Name"] = value

    @property
    def fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name(self):
        """Get fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name

        Returns:
            str: the value of `fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Fuel Input to Cooling Output Ratio Function of Temperature Curve Name"]

    @fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name.setter
    def fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name`
        The curve represents the fraction of the fuel input to the chiller at full load as
        it varies by temperature.  The curve is normalized so that at design conditions the
        value of the curve should be 1.0.  This is a biquadratic curve with the
        input variables being the leaving chilled water temperature and either
        the entering or leaving condenser water temperature.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name`')

        self._data["Fuel Input to Cooling Output Ratio Function of Temperature Curve Name"] = value

    @property
    def fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self):
        """Get fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name

        Returns:
            str: the value of `fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name` or None if not set
        """
        return self._data["Fuel Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"]

    @fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name.setter
    def fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
        The curve represents the fraction of the fuel input to the chiller as the load on
        the chiller varies but the operating temperatures remain at the design values.
        The curve is normalized so that at full load the value of the curve should be 1.0.
        The curve is usually linear or quadratic.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`')

        self._data["Fuel Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = value

    @property
    def electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self):
        """Get electric_input_to_cooling_output_ratio_function_of_temperature_curve_name

        Returns:
            str: the value of `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"]

    @electric_input_to_cooling_output_ratio_function_of_temperature_curve_name.setter
    def electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
        The curve represents the fraction of the electricity to the chiller at full load as
        it varies by temperature.  The curve is normalized so that at design conditions the
        value of the curve should be 1.0.  This is a biquadratic curve with the
        input variables being the leaving chilled water temperature and either
        the entering or leaving condenser water temperature.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`')

        self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = value

    @property
    def electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self):
        """Get electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name

        Returns:
            str: the value of `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name` or None if not set
        """
        return self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"]

    @electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name.setter
    def electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
        The curve represents the fraction of the electricity to the chiller as the load on
        the chiller varies but the operating temperatures remain at the design values.
        The curve is normalized so that at full load the value of the curve should be 1.0.
        The curve is usually linear or quadratic.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`')

        self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = value

    @property
    def heating_capacity_function_of_cooling_capacity_curve_name(self):
        """Get heating_capacity_function_of_cooling_capacity_curve_name

        Returns:
            str: the value of `heating_capacity_function_of_cooling_capacity_curve_name` or None if not set
        """
        return self._data["Heating Capacity Function of Cooling Capacity Curve Name"]

    @heating_capacity_function_of_cooling_capacity_curve_name.setter
    def heating_capacity_function_of_cooling_capacity_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_capacity_function_of_cooling_capacity_curve_name`
        The curve represents how the heating capacity of the chiller varies with cooling
        capacity when the chiller is simultaeous heating and cooling.  The curve is normalized
        so an input of 1.0 represents the nominal cooling capacity and an output of 1.0
        represents the full heating capacity (see the Heating to cooling capacity ratio input)
        The curve is usually linear or quadratic.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `heating_capacity_function_of_cooling_capacity_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_capacity_function_of_cooling_capacity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_capacity_function_of_cooling_capacity_curve_name`')

        self._data["Heating Capacity Function of Cooling Capacity Curve Name"] = value

    @property
    def fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name(self):
        """Get fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name

        Returns:
            str: the value of `fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name` or None if not set
        """
        return self._data["Fuel Input to Heat Output Ratio During Heating Only Operation Curve Name"]

    @fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name.setter
    def fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name(self, value=None):
        """  Corresponds to IDD Field `fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name`
        When the chiller is operating as only a heater, this curve is used to represent the
        fraction of fuel used as the heating load varies.  It is normalized so that a value
        of 1.0 is the full heating capacity.  The curve is usually linear or quadratic and
        will probably be similar to a boiler curve for most chillers.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name`')

        self._data["Fuel Input to Heat Output Ratio During Heating Only Operation Curve Name"] = value

    @property
    def temperature_curve_input_variable(self):
        """Get temperature_curve_input_variable

        Returns:
            str: the value of `temperature_curve_input_variable` or None if not set
        """
        return self._data["Temperature Curve Input Variable"]

    @temperature_curve_input_variable.setter
    def temperature_curve_input_variable(self, value="EnteringCondenser"):
        """  Corresponds to IDD Field `temperature_curve_input_variable`
        Sets the second independent variable in the three temperature dependent performance
        curves to either the leaving or entering condenser water temperature.  Manufacturers
        express the performance of their chillers using either the leaving condenser water
        temperature (to the tower) or the entering condenser water temperature (from the tower).

        Args:
            value (str): value for IDD Field `temperature_curve_input_variable`
                Accepted values are:
                      - LeavingCondenser
                      - EnteringCondenser
                Default value: EnteringCondenser
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `temperature_curve_input_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `temperature_curve_input_variable`')
            vals = set()
            vals.add("LeavingCondenser")
            vals.add("EnteringCondenser")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `temperature_curve_input_variable`'.format(value))

        self._data["Temperature Curve Input Variable"] = value

    @property
    def condenser_type(self):
        """Get condenser_type

        Returns:
            str: the value of `condenser_type` or None if not set
        """
        return self._data["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="WaterCooled"):
        """  Corresponds to IDD Field `condenser_type`
        The condenser can either be air cooled or connected to a cooling tower.

        Args:
            value (str): value for IDD Field `condenser_type`
                Accepted values are:
                      - AirCooled
                      - WaterCooled
                Default value: WaterCooled
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_type`')
            vals = set()
            vals.add("AirCooled")
            vals.add("WaterCooled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `condenser_type`'.format(value))

        self._data["Condenser Type"] = value

    @property
    def chilled_water_temperature_lower_limit(self):
        """Get chilled_water_temperature_lower_limit

        Returns:
            float: the value of `chilled_water_temperature_lower_limit` or None if not set
        """
        return self._data["Chilled Water Temperature Lower Limit"]

    @chilled_water_temperature_lower_limit.setter
    def chilled_water_temperature_lower_limit(self, value=2.0 ):
        """  Corresponds to IDD Field `chilled_water_temperature_lower_limit`
        The chilled water supply temperature below which the chiller
        will shut off.

        Args:
            value (float): value for IDD Field `chilled_water_temperature_lower_limit`
                Unit: C
                Default value: 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `chilled_water_temperature_lower_limit`'.format(value))

        self._data["Chilled Water Temperature Lower Limit"] = value

    @property
    def fuel_higher_heating_value(self):
        """Get fuel_higher_heating_value

        Returns:
            float: the value of `fuel_higher_heating_value` or None if not set
        """
        return self._data["Fuel Higher Heating Value"]

    @fuel_higher_heating_value.setter
    def fuel_higher_heating_value(self, value=0.0 ):
        """  Corresponds to IDD Field `fuel_higher_heating_value`
        Not currently used.

        Args:
            value (float): value for IDD Field `fuel_higher_heating_value`
                Unit: kJ/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fuel_higher_heating_value`'.format(value))

        self._data["Fuel Higher Heating Value"] = value

    @property
    def chiller_flow_mode(self):
        """Get chiller_flow_mode

        Returns:
            str: the value of `chiller_flow_mode` or None if not set
        """
        return self._data["Chiller Flow Mode"]

    @chiller_flow_mode.setter
    def chiller_flow_mode(self, value=None):
        """  Corresponds to IDD Field `chiller_flow_mode`

        Args:
            value (str): value for IDD Field `chiller_flow_mode`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `chiller_flow_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_flow_mode`')

        self._data["Chiller Flow Mode"] = value

    @property
    def fuel_type(self):
        """Get fuel_type

        Returns:
            str: the value of `fuel_type` or None if not set
        """
        return self._data["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value="NaturalGas"):
        """  Corresponds to IDD Field `fuel_type`

        Args:
            value (str): value for IDD Field `fuel_type`
                Accepted values are:
                      - NaturalGas
                      - PropaneGas
                      - Diesel
                      - Gasoline
                      - FuelOil#1
                      - FuelOil#2
                      - OtherFuel1
                      - OtherFuel2
                Default value: NaturalGas
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_type`')
            vals = set()
            vals.add("NaturalGas")
            vals.add("PropaneGas")
            vals.add("Diesel")
            vals.add("Gasoline")
            vals.add("FuelOil#1")
            vals.add("FuelOil#2")
            vals.add("OtherFuel1")
            vals.add("OtherFuel2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fuel_type`'.format(value))

        self._data["Fuel Type"] = value

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
        Multiplies the autosized capacity and flow rates

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
        out.append(self._to_str(self.nominal_cooling_capacity))
        out.append(self._to_str(self.heating_to_cooling_capacity_ratio))
        out.append(self._to_str(self.fuel_input_to_cooling_output_ratio))
        out.append(self._to_str(self.fuel_input_to_heating_output_ratio))
        out.append(self._to_str(self.electric_input_to_cooling_output_ratio))
        out.append(self._to_str(self.electric_input_to_heating_output_ratio))
        out.append(self._to_str(self.chilled_water_inlet_node_name))
        out.append(self._to_str(self.chilled_water_outlet_node_name))
        out.append(self._to_str(self.condenser_inlet_node_name))
        out.append(self._to_str(self.condenser_outlet_node_name))
        out.append(self._to_str(self.hot_water_inlet_node_name))
        out.append(self._to_str(self.hot_water_outlet_node_name))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.design_entering_condenser_water_temperature))
        out.append(self._to_str(self.design_leaving_chilled_water_temperature))
        out.append(self._to_str(self.design_chilled_water_flow_rate))
        out.append(self._to_str(self.design_condenser_water_flow_rate))
        out.append(self._to_str(self.design_hot_water_flow_rate))
        out.append(self._to_str(self.cooling_capacity_function_of_temperature_curve_name))
        out.append(self._to_str(self.fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name))
        out.append(self._to_str(self.fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name))
        out.append(self._to_str(self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name))
        out.append(self._to_str(self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name))
        out.append(self._to_str(self.heating_capacity_function_of_cooling_capacity_curve_name))
        out.append(self._to_str(self.fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name))
        out.append(self._to_str(self.temperature_curve_input_variable))
        out.append(self._to_str(self.condenser_type))
        out.append(self._to_str(self.chilled_water_temperature_lower_limit))
        out.append(self._to_str(self.fuel_higher_heating_value))
        out.append(self._to_str(self.chiller_flow_mode))
        out.append(self._to_str(self.fuel_type))
        out.append(self._to_str(self.sizing_factor))
        return ",".join(out)

class ChillerHeaterAbsorptionDoubleEffect(object):
    """ Corresponds to IDD object `ChillerHeater:Absorption:DoubleEffect`
        Exhaust fired absorption chiller-heater using performance curves similar to DOE-2
    """
    internal_name = "ChillerHeater:Absorption:DoubleEffect"
    field_count = 34

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ChillerHeater:Absorption:DoubleEffect`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Nominal Cooling Capacity"] = None
        self._data["Heating to Cooling Capacity Ratio"] = None
        self._data["Thermal Energy Input to Cooling Output Ratio"] = None
        self._data["Thermal Energy Input to Heating Output Ratio"] = None
        self._data["Electric Input to Cooling Output Ratio"] = None
        self._data["Electric Input to Heating Output Ratio"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Hot Water Inlet Node Name"] = None
        self._data["Hot Water Outlet Node Name"] = None
        self._data["Minimum Part Load Ratio"] = None
        self._data["Maximum Part Load Ratio"] = None
        self._data["Optimum Part Load Ratio"] = None
        self._data["Design Entering Condenser Water Temperature"] = None
        self._data["Design Leaving Chilled Water Temperature"] = None
        self._data["Design Chilled Water Flow Rate"] = None
        self._data["Design Condenser Water Flow Rate"] = None
        self._data["Design Hot Water Flow Rate"] = None
        self._data["Cooling Capacity Function of Temperature Curve Name"] = None
        self._data["Fuel Input to Cooling Output Ratio Function of Temperature Curve Name"] = None
        self._data["Fuel Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = None
        self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = None
        self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = None
        self._data["Heating Capacity Function of Cooling Capacity Curve Name"] = None
        self._data["Fuel Input to Heat Output Ratio During Heating Only Operation Curve Name"] = None
        self._data["Temperature Curve Input Variable"] = None
        self._data["Condenser Type"] = None
        self._data["Chilled Water Temperature Lower Limit"] = None
        self._data["Exhaust Source Object Type"] = None
        self._data["Exhaust Source Object Name"] = None
        self._data["Sizing Factor"] = None

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
            self.nominal_cooling_capacity = None
        else:
            self.nominal_cooling_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_to_cooling_capacity_ratio = None
        else:
            self.heating_to_cooling_capacity_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_energy_input_to_cooling_output_ratio = None
        else:
            self.thermal_energy_input_to_cooling_output_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_energy_input_to_heating_output_ratio = None
        else:
            self.thermal_energy_input_to_heating_output_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_cooling_output_ratio = None
        else:
            self.electric_input_to_cooling_output_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_heating_output_ratio = None
        else:
            self.electric_input_to_heating_output_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hot_water_inlet_node_name = None
        else:
            self.hot_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hot_water_outlet_node_name = None
        else:
            self.hot_water_outlet_node_name = vals[i]
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
            self.design_entering_condenser_water_temperature = None
        else:
            self.design_entering_condenser_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_leaving_chilled_water_temperature = None
        else:
            self.design_leaving_chilled_water_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_chilled_water_flow_rate = None
        else:
            self.design_chilled_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_condenser_water_flow_rate = None
        else:
            self.design_condenser_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_hot_water_flow_rate = None
        else:
            self.design_hot_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_capacity_function_of_temperature_curve_name = None
        else:
            self.cooling_capacity_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name = None
        else:
            self.fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = None
        else:
            self.fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = None
        else:
            self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = None
        else:
            self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_capacity_function_of_cooling_capacity_curve_name = None
        else:
            self.heating_capacity_function_of_cooling_capacity_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name = None
        else:
            self.fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_curve_input_variable = None
        else:
            self.temperature_curve_input_variable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chilled_water_temperature_lower_limit = None
        else:
            self.chilled_water_temperature_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_source_object_type = None
        else:
            self.exhaust_source_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exhaust_source_object_name = None
        else:
            self.exhaust_source_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sizing_factor = None
        else:
            self.sizing_factor = vals[i]
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
    def nominal_cooling_capacity(self):
        """Get nominal_cooling_capacity

        Returns:
            float: the value of `nominal_cooling_capacity` or None if not set
        """
        return self._data["Nominal Cooling Capacity"]

    @nominal_cooling_capacity.setter
    def nominal_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_cooling_capacity`

        Args:
            value (float): value for IDD Field `nominal_cooling_capacity`
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
                                 'for field `nominal_cooling_capacity`'.format(value))

        self._data["Nominal Cooling Capacity"] = value

    @property
    def heating_to_cooling_capacity_ratio(self):
        """Get heating_to_cooling_capacity_ratio

        Returns:
            float: the value of `heating_to_cooling_capacity_ratio` or None if not set
        """
        return self._data["Heating to Cooling Capacity Ratio"]

    @heating_to_cooling_capacity_ratio.setter
    def heating_to_cooling_capacity_ratio(self, value=0.8 ):
        """  Corresponds to IDD Field `heating_to_cooling_capacity_ratio`
        A positive fraction that represents the ratio of the
        heating capacity divided by the cooling capacity at rated conditions.

        Args:
            value (float): value for IDD Field `heating_to_cooling_capacity_ratio`
                Default value: 0.8
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
                                 'for field `heating_to_cooling_capacity_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_to_cooling_capacity_ratio`')

        self._data["Heating to Cooling Capacity Ratio"] = value

    @property
    def thermal_energy_input_to_cooling_output_ratio(self):
        """Get thermal_energy_input_to_cooling_output_ratio

        Returns:
            float: the value of `thermal_energy_input_to_cooling_output_ratio` or None if not set
        """
        return self._data["Thermal Energy Input to Cooling Output Ratio"]

    @thermal_energy_input_to_cooling_output_ratio.setter
    def thermal_energy_input_to_cooling_output_ratio(self, value=0.97 ):
        """  Corresponds to IDD Field `thermal_energy_input_to_cooling_output_ratio`
        The positive fraction that represents the ratio of the
        instantaneous fuel used divided by the cooling capacity at rated conditions.

        Args:
            value (float): value for IDD Field `thermal_energy_input_to_cooling_output_ratio`
                Default value: 0.97
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
                                 'for field `thermal_energy_input_to_cooling_output_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_energy_input_to_cooling_output_ratio`')

        self._data["Thermal Energy Input to Cooling Output Ratio"] = value

    @property
    def thermal_energy_input_to_heating_output_ratio(self):
        """Get thermal_energy_input_to_heating_output_ratio

        Returns:
            float: the value of `thermal_energy_input_to_heating_output_ratio` or None if not set
        """
        return self._data["Thermal Energy Input to Heating Output Ratio"]

    @thermal_energy_input_to_heating_output_ratio.setter
    def thermal_energy_input_to_heating_output_ratio(self, value=1.25 ):
        """  Corresponds to IDD Field `thermal_energy_input_to_heating_output_ratio`
        The positive fraction that represents the ratio of the
        instantaneous fuel used divided by the nominal heating capacity.

        Args:
            value (float): value for IDD Field `thermal_energy_input_to_heating_output_ratio`
                Default value: 1.25
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
                                 'for field `thermal_energy_input_to_heating_output_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `thermal_energy_input_to_heating_output_ratio`')

        self._data["Thermal Energy Input to Heating Output Ratio"] = value

    @property
    def electric_input_to_cooling_output_ratio(self):
        """Get electric_input_to_cooling_output_ratio

        Returns:
            float: the value of `electric_input_to_cooling_output_ratio` or None if not set
        """
        return self._data["Electric Input to Cooling Output Ratio"]

    @electric_input_to_cooling_output_ratio.setter
    def electric_input_to_cooling_output_ratio(self, value=0.01 ):
        """  Corresponds to IDD Field `electric_input_to_cooling_output_ratio`
        The positive fraction that represents the ratio of the
        instantaneous electricity used divided by the cooling capacity at rated conditions.
        If the chiller is both heating and cooling only the cooling electricity is used.

        Args:
            value (float): value for IDD Field `electric_input_to_cooling_output_ratio`
                Default value: 0.01
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
                                 'for field `electric_input_to_cooling_output_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `electric_input_to_cooling_output_ratio`')

        self._data["Electric Input to Cooling Output Ratio"] = value

    @property
    def electric_input_to_heating_output_ratio(self):
        """Get electric_input_to_heating_output_ratio

        Returns:
            float: the value of `electric_input_to_heating_output_ratio` or None if not set
        """
        return self._data["Electric Input to Heating Output Ratio"]

    @electric_input_to_heating_output_ratio.setter
    def electric_input_to_heating_output_ratio(self, value=0.0 ):
        """  Corresponds to IDD Field `electric_input_to_heating_output_ratio`
        The positive fraction that represents the ratio of the
        instantaneous electricity used divided by the nominal heating capacity.
        If the chiller is both heating and cooling only the cooling electricity is used.

        Args:
            value (float): value for IDD Field `electric_input_to_heating_output_ratio`
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
                                 'for field `electric_input_to_heating_output_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `electric_input_to_heating_output_ratio`')

        self._data["Electric Input to Heating Output Ratio"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')

        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def hot_water_inlet_node_name(self):
        """Get hot_water_inlet_node_name

        Returns:
            str: the value of `hot_water_inlet_node_name` or None if not set
        """
        return self._data["Hot Water Inlet Node Name"]

    @hot_water_inlet_node_name.setter
    def hot_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `hot_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_inlet_node_name`')

        self._data["Hot Water Inlet Node Name"] = value

    @property
    def hot_water_outlet_node_name(self):
        """Get hot_water_outlet_node_name

        Returns:
            str: the value of `hot_water_outlet_node_name` or None if not set
        """
        return self._data["Hot Water Outlet Node Name"]

    @hot_water_outlet_node_name.setter
    def hot_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `hot_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_outlet_node_name`')

        self._data["Hot Water Outlet Node Name"] = value

    @property
    def minimum_part_load_ratio(self):
        """Get minimum_part_load_ratio

        Returns:
            float: the value of `minimum_part_load_ratio` or None if not set
        """
        return self._data["Minimum Part Load Ratio"]

    @minimum_part_load_ratio.setter
    def minimum_part_load_ratio(self, value=0.1 ):
        """  Corresponds to IDD Field `minimum_part_load_ratio`
        The positive fraction that represents the minimum cooling output possible when
        operated continually at rated temperature conditions divided by the nominal
        cooling capacity at those same conditions.  If the load on the chiller is below
        this fraction the chiller will cycle.

        Args:
            value (float): value for IDD Field `minimum_part_load_ratio`
                Default value: 0.1
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
                                 'for field `minimum_part_load_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
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
    def maximum_part_load_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `maximum_part_load_ratio`
        The positive fraction that represents the maximum cooling output possible at
        rated temperature conditions divided by the nominal cooling capacity at those
        same conditions.  If greater than 1.0, the chiller is typically thought of as
        capable of being overloaded.

        Args:
            value (float): value for IDD Field `maximum_part_load_ratio`
                Default value: 1.0
                value >= 0.5
                if `value` is None it will not be checked against the
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
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
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
    def optimum_part_load_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `optimum_part_load_ratio`
        The positive fraction that represents the optimal cooling output at rated
        temperature conditions divided by the nominal cooling capacity at those same
        conditions.  It represents the most desirable operating point for the chiller.

        Args:
            value (float): value for IDD Field `optimum_part_load_ratio`
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
                                 'for field `optimum_part_load_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `optimum_part_load_ratio`')

        self._data["Optimum Part Load Ratio"] = value

    @property
    def design_entering_condenser_water_temperature(self):
        """Get design_entering_condenser_water_temperature

        Returns:
            float: the value of `design_entering_condenser_water_temperature` or None if not set
        """
        return self._data["Design Entering Condenser Water Temperature"]

    @design_entering_condenser_water_temperature.setter
    def design_entering_condenser_water_temperature(self, value=29.0 ):
        """  Corresponds to IDD Field `design_entering_condenser_water_temperature`
        The temperature of the water entering the condenser of the chiller when
        operating at design conditions.  This is usually based on the temperature
        delivered by the cooling tower in a water cooled application.

        Args:
            value (float): value for IDD Field `design_entering_condenser_water_temperature`
                Unit: C
                Default value: 29.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_entering_condenser_water_temperature`'.format(value))

        self._data["Design Entering Condenser Water Temperature"] = value

    @property
    def design_leaving_chilled_water_temperature(self):
        """Get design_leaving_chilled_water_temperature

        Returns:
            float: the value of `design_leaving_chilled_water_temperature` or None if not set
        """
        return self._data["Design Leaving Chilled Water Temperature"]

    @design_leaving_chilled_water_temperature.setter
    def design_leaving_chilled_water_temperature(self, value=7.0 ):
        """  Corresponds to IDD Field `design_leaving_chilled_water_temperature`
        The temperature of the water leaving the evaporator of the chiller when
        operating at design conditions also called the chilled water supply temperature
        or leaving chilled water temperature.

        Args:
            value (float): value for IDD Field `design_leaving_chilled_water_temperature`
                Unit: C
                Default value: 7.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_leaving_chilled_water_temperature`'.format(value))

        self._data["Design Leaving Chilled Water Temperature"] = value

    @property
    def design_chilled_water_flow_rate(self):
        """Get design_chilled_water_flow_rate

        Returns:
            float: the value of `design_chilled_water_flow_rate` or None if not set
        """
        return self._data["Design Chilled Water Flow Rate"]

    @design_chilled_water_flow_rate.setter
    def design_chilled_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_chilled_water_flow_rate`
        For variable volume this is the max flow & for constant flow this is the flow.

        Args:
            value (float): value for IDD Field `design_chilled_water_flow_rate`
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
                                 'for field `design_chilled_water_flow_rate`'.format(value))

        self._data["Design Chilled Water Flow Rate"] = value

    @property
    def design_condenser_water_flow_rate(self):
        """Get design_condenser_water_flow_rate

        Returns:
            float: the value of `design_condenser_water_flow_rate` or None if not set
        """
        return self._data["Design Condenser Water Flow Rate"]

    @design_condenser_water_flow_rate.setter
    def design_condenser_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_condenser_water_flow_rate`
        The water flow rate at design conditions through the condenser.
        This field is not used for Condenser Type = AirCooled

        Args:
            value (float): value for IDD Field `design_condenser_water_flow_rate`
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
                                 'for field `design_condenser_water_flow_rate`'.format(value))

        self._data["Design Condenser Water Flow Rate"] = value

    @property
    def design_hot_water_flow_rate(self):
        """Get design_hot_water_flow_rate

        Returns:
            float: the value of `design_hot_water_flow_rate` or None if not set
        """
        return self._data["Design Hot Water Flow Rate"]

    @design_hot_water_flow_rate.setter
    def design_hot_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_hot_water_flow_rate`
        The water flow rate at design conditions through the heater side.

        Args:
            value (float): value for IDD Field `design_hot_water_flow_rate`
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
                                 'for field `design_hot_water_flow_rate`'.format(value))

        self._data["Design Hot Water Flow Rate"] = value

    @property
    def cooling_capacity_function_of_temperature_curve_name(self):
        """Get cooling_capacity_function_of_temperature_curve_name

        Returns:
            str: the value of `cooling_capacity_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Cooling Capacity Function of Temperature Curve Name"]

    @cooling_capacity_function_of_temperature_curve_name.setter
    def cooling_capacity_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_function_of_temperature_curve_name`
        The CoolCapFT curve represents the fraction of the cooling capacity of the chiller as it
        varies by temperature.  The curve is normalized so that at design conditions the
        value of the curve should be 1.0.  This is a biquadratic curve with the
        input variables being the leaving chilled water temperature and either
        the entering or leaving condenser water temperature.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `cooling_capacity_function_of_temperature_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_capacity_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_capacity_function_of_temperature_curve_name`')

        self._data["Cooling Capacity Function of Temperature Curve Name"] = value

    @property
    def fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name(self):
        """Get fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name

        Returns:
            str: the value of `fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Fuel Input to Cooling Output Ratio Function of Temperature Curve Name"]

    @fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name.setter
    def fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name`
        The curve represents the fraction of the fuel input to the chiller at full load as
        it varies by temperature.  The curve is normalized so that at design conditions the
        value of the curve should be 1.0.  This is a biquadratic curve with the
        input variables being the leaving chilled water temperature and either
        the entering or leaving condenser water temperature.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name`')

        self._data["Fuel Input to Cooling Output Ratio Function of Temperature Curve Name"] = value

    @property
    def fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self):
        """Get fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name

        Returns:
            str: the value of `fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name` or None if not set
        """
        return self._data["Fuel Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"]

    @fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name.setter
    def fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
        The curve represents the fraction of the fuel input to the chiller as the load on
        the chiller varies but the operating temperatures remain at the design values.
        The curve is normalized so that at full load the value of the curve should be 1.0.
        The curve is usually linear or quadratic.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`')

        self._data["Fuel Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = value

    @property
    def electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self):
        """Get electric_input_to_cooling_output_ratio_function_of_temperature_curve_name

        Returns:
            str: the value of `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"]

    @electric_input_to_cooling_output_ratio_function_of_temperature_curve_name.setter
    def electric_input_to_cooling_output_ratio_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
        The curve represents the fraction of the electricity to the chiller at full load as
        it varies by temperature.  The curve is normalized so that at design conditions the
        value of the curve should be 1.0.  This is a biquadratic curve with the
        input variables being the leaving chilled water temperature and either
        the entering or leaving condenser water temperature.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_temperature_curve_name`')

        self._data["Electric Input to Cooling Output Ratio Function of Temperature Curve Name"] = value

    @property
    def electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self):
        """Get electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name

        Returns:
            str: the value of `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name` or None if not set
        """
        return self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"]

    @electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name.setter
    def electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
        The curve represents the fraction of the electricity to the chiller as the load on
        the chiller varies but the operating temperatures remain at the design values.
        The curve is normalized so that at full load the value of the curve should be 1.0.
        The curve is usually linear or quadratic.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name`')

        self._data["Electric Input to Cooling Output Ratio Function of Part Load Ratio Curve Name"] = value

    @property
    def heating_capacity_function_of_cooling_capacity_curve_name(self):
        """Get heating_capacity_function_of_cooling_capacity_curve_name

        Returns:
            str: the value of `heating_capacity_function_of_cooling_capacity_curve_name` or None if not set
        """
        return self._data["Heating Capacity Function of Cooling Capacity Curve Name"]

    @heating_capacity_function_of_cooling_capacity_curve_name.setter
    def heating_capacity_function_of_cooling_capacity_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_capacity_function_of_cooling_capacity_curve_name`
        The curve represents how the heating capacity of the chiller varies with cooling
        capacity when the chiller is simultaeous heating and cooling.  The curve is normalized
        so an input of 1.0 represents the nominal cooling capacity and an output of 1.0
        represents the full heating capacity (see the Heating to cooling capacity ratio input)
        The curve is usually linear or quadratic.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `heating_capacity_function_of_cooling_capacity_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_capacity_function_of_cooling_capacity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_capacity_function_of_cooling_capacity_curve_name`')

        self._data["Heating Capacity Function of Cooling Capacity Curve Name"] = value

    @property
    def fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name(self):
        """Get fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name

        Returns:
            str: the value of `fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name` or None if not set
        """
        return self._data["Fuel Input to Heat Output Ratio During Heating Only Operation Curve Name"]

    @fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name.setter
    def fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name(self, value=None):
        """  Corresponds to IDD Field `fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name`
        When the chiller is operating as only a heater, this curve is used to represent the
        fraction of fuel used as the heating load varies.  It is normalized so that a value
        of 1.0 is the full heating capacity.  The curve is usually linear or quadratic and
        will probably be similar to a boiler curve for most chillers.
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name`')

        self._data["Fuel Input to Heat Output Ratio During Heating Only Operation Curve Name"] = value

    @property
    def temperature_curve_input_variable(self):
        """Get temperature_curve_input_variable

        Returns:
            str: the value of `temperature_curve_input_variable` or None if not set
        """
        return self._data["Temperature Curve Input Variable"]

    @temperature_curve_input_variable.setter
    def temperature_curve_input_variable(self, value="EnteringCondenser"):
        """  Corresponds to IDD Field `temperature_curve_input_variable`
        Sets the second independent variable in the three temperature dependent performance
        curves to either the leaving or entering condenser water temperature.  Manufacturers
        express the performance of their chillers using either the leaving condenser water
        temperature (to the tower) or the entering condenser water temperature (from the tower).

        Args:
            value (str): value for IDD Field `temperature_curve_input_variable`
                Accepted values are:
                      - LeavingCondenser
                      - EnteringCondenser
                Default value: EnteringCondenser
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `temperature_curve_input_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `temperature_curve_input_variable`')
            vals = set()
            vals.add("LeavingCondenser")
            vals.add("EnteringCondenser")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `temperature_curve_input_variable`'.format(value))

        self._data["Temperature Curve Input Variable"] = value

    @property
    def condenser_type(self):
        """Get condenser_type

        Returns:
            str: the value of `condenser_type` or None if not set
        """
        return self._data["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="WaterCooled"):
        """  Corresponds to IDD Field `condenser_type`
        The condenser can either be air cooled or connected to a cooling tower.

        Args:
            value (str): value for IDD Field `condenser_type`
                Accepted values are:
                      - AirCooled
                      - WaterCooled
                Default value: WaterCooled
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_type`')
            vals = set()
            vals.add("AirCooled")
            vals.add("WaterCooled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `condenser_type`'.format(value))

        self._data["Condenser Type"] = value

    @property
    def chilled_water_temperature_lower_limit(self):
        """Get chilled_water_temperature_lower_limit

        Returns:
            float: the value of `chilled_water_temperature_lower_limit` or None if not set
        """
        return self._data["Chilled Water Temperature Lower Limit"]

    @chilled_water_temperature_lower_limit.setter
    def chilled_water_temperature_lower_limit(self, value=2.0 ):
        """  Corresponds to IDD Field `chilled_water_temperature_lower_limit`
        The chilled water supply temperature below which the chiller
        will shut off.

        Args:
            value (float): value for IDD Field `chilled_water_temperature_lower_limit`
                Unit: C
                Default value: 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `chilled_water_temperature_lower_limit`'.format(value))

        self._data["Chilled Water Temperature Lower Limit"] = value

    @property
    def exhaust_source_object_type(self):
        """Get exhaust_source_object_type

        Returns:
            str: the value of `exhaust_source_object_type` or None if not set
        """
        return self._data["Exhaust Source Object Type"]

    @exhaust_source_object_type.setter
    def exhaust_source_object_type(self, value=None):
        """  Corresponds to IDD Field `exhaust_source_object_type`

        Args:
            value (str): value for IDD Field `exhaust_source_object_type`
                Accepted values are:
                      - Generator:MicroTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_source_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_source_object_type`')
            vals = set()
            vals.add("Generator:MicroTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `exhaust_source_object_type`'.format(value))

        self._data["Exhaust Source Object Type"] = value

    @property
    def exhaust_source_object_name(self):
        """Get exhaust_source_object_name

        Returns:
            str: the value of `exhaust_source_object_name` or None if not set
        """
        return self._data["Exhaust Source Object Name"]

    @exhaust_source_object_name.setter
    def exhaust_source_object_name(self, value=None):
        """  Corresponds to IDD Field `exhaust_source_object_name`

        Args:
            value (str): value for IDD Field `exhaust_source_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `exhaust_source_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_source_object_name`')

        self._data["Exhaust Source Object Name"] = value

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
        Multiplies the autosized capacity and flow rates

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
        out.append(self._to_str(self.nominal_cooling_capacity))
        out.append(self._to_str(self.heating_to_cooling_capacity_ratio))
        out.append(self._to_str(self.thermal_energy_input_to_cooling_output_ratio))
        out.append(self._to_str(self.thermal_energy_input_to_heating_output_ratio))
        out.append(self._to_str(self.electric_input_to_cooling_output_ratio))
        out.append(self._to_str(self.electric_input_to_heating_output_ratio))
        out.append(self._to_str(self.chilled_water_inlet_node_name))
        out.append(self._to_str(self.chilled_water_outlet_node_name))
        out.append(self._to_str(self.condenser_inlet_node_name))
        out.append(self._to_str(self.condenser_outlet_node_name))
        out.append(self._to_str(self.hot_water_inlet_node_name))
        out.append(self._to_str(self.hot_water_outlet_node_name))
        out.append(self._to_str(self.minimum_part_load_ratio))
        out.append(self._to_str(self.maximum_part_load_ratio))
        out.append(self._to_str(self.optimum_part_load_ratio))
        out.append(self._to_str(self.design_entering_condenser_water_temperature))
        out.append(self._to_str(self.design_leaving_chilled_water_temperature))
        out.append(self._to_str(self.design_chilled_water_flow_rate))
        out.append(self._to_str(self.design_condenser_water_flow_rate))
        out.append(self._to_str(self.design_hot_water_flow_rate))
        out.append(self._to_str(self.cooling_capacity_function_of_temperature_curve_name))
        out.append(self._to_str(self.fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name))
        out.append(self._to_str(self.fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name))
        out.append(self._to_str(self.electric_input_to_cooling_output_ratio_function_of_temperature_curve_name))
        out.append(self._to_str(self.electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name))
        out.append(self._to_str(self.heating_capacity_function_of_cooling_capacity_curve_name))
        out.append(self._to_str(self.fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name))
        out.append(self._to_str(self.temperature_curve_input_variable))
        out.append(self._to_str(self.condenser_type))
        out.append(self._to_str(self.chilled_water_temperature_lower_limit))
        out.append(self._to_str(self.exhaust_source_object_type))
        out.append(self._to_str(self.exhaust_source_object_name))
        out.append(self._to_str(self.sizing_factor))
        return ",".join(out)