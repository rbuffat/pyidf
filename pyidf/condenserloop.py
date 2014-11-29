from collections import OrderedDict

class CondenserLoop(object):
    """ Corresponds to IDD object `CondenserLoop`
        Defines a central plant condenser loop. CondenserLoop and PlantLoop are nearly
        identical except some components and operation schemes are applicable to only one
        loop type or the other.
    """
    internal_name = "CondenserLoop"
    field_count = 20

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CondenserLoop`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fluid Type"] = None
        self._data["User Defined Fluid Type"] = None
        self._data["Condenser Equipment Operation Scheme Name"] = None
        self._data["Condenser Loop Temperature Setpoint Node Name"] = None
        self._data["Maximum Loop Temperature"] = None
        self._data["Minimum Loop Temperature"] = None
        self._data["Maximum Loop Flow Rate"] = None
        self._data["Minimum Loop Flow Rate"] = None
        self._data["Condenser Loop Volume"] = None
        self._data["Condenser Side Inlet Node Name"] = None
        self._data["Condenser Side Outlet Node Name"] = None
        self._data["Condenser Side Branch List Name"] = None
        self._data["Condenser Side Connector List Name"] = None
        self._data["Demand Side Inlet Node Name"] = None
        self._data["Demand Side Outlet Node Name"] = None
        self._data["Condenser Demand Side Branch List Name"] = None
        self._data["Condenser Demand Side Connector List Name"] = None
        self._data["Load Distribution Scheme"] = None
        self._data["Pressure Simulation Type"] = None

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
            self.fluid_type = None
        else:
            self.fluid_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.user_defined_fluid_type = None
        else:
            self.user_defined_fluid_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_equipment_operation_scheme_name = None
        else:
            self.condenser_equipment_operation_scheme_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_loop_temperature_setpoint_node_name = None
        else:
            self.condenser_loop_temperature_setpoint_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_loop_temperature = None
        else:
            self.maximum_loop_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_loop_temperature = None
        else:
            self.minimum_loop_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_loop_flow_rate = None
        else:
            self.maximum_loop_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_loop_flow_rate = None
        else:
            self.minimum_loop_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_loop_volume = None
        else:
            self.condenser_loop_volume = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_side_inlet_node_name = None
        else:
            self.condenser_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_side_outlet_node_name = None
        else:
            self.condenser_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_side_branch_list_name = None
        else:
            self.condenser_side_branch_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_side_connector_list_name = None
        else:
            self.condenser_side_connector_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_side_inlet_node_name = None
        else:
            self.demand_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_side_outlet_node_name = None
        else:
            self.demand_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_demand_side_branch_list_name = None
        else:
            self.condenser_demand_side_branch_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.condenser_demand_side_connector_list_name = None
        else:
            self.condenser_demand_side_connector_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_distribution_scheme = None
        else:
            self.load_distribution_scheme = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pressure_simulation_type = None
        else:
            self.pressure_simulation_type = vals[i]
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
    def fluid_type(self):
        """Get fluid_type

        Returns:
            str: the value of `fluid_type` or None if not set
        """
        return self._data["Fluid Type"]

    @fluid_type.setter
    def fluid_type(self, value="Water"):
        """  Corresponds to IDD Field `fluid_type`

        Args:
            value (str): value for IDD Field `fluid_type`
                Accepted values are:
                      - Water
                      - UserDefinedFluidType
                Default value: Water
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_type`')
            vals = set()
            vals.add("Water")
            vals.add("UserDefinedFluidType")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `fluid_type`'.format(value))

        self._data["Fluid Type"] = value

    @property
    def user_defined_fluid_type(self):
        """Get user_defined_fluid_type

        Returns:
            str: the value of `user_defined_fluid_type` or None if not set
        """
        return self._data["User Defined Fluid Type"]

    @user_defined_fluid_type.setter
    def user_defined_fluid_type(self, value=None):
        """  Corresponds to IDD Field `user_defined_fluid_type`
        This field is only required when Fluid Type is UserDefinedFluidType

        Args:
            value (str): value for IDD Field `user_defined_fluid_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `user_defined_fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `user_defined_fluid_type`')

        self._data["User Defined Fluid Type"] = value

    @property
    def condenser_equipment_operation_scheme_name(self):
        """Get condenser_equipment_operation_scheme_name

        Returns:
            str: the value of `condenser_equipment_operation_scheme_name` or None if not set
        """
        return self._data["Condenser Equipment Operation Scheme Name"]

    @condenser_equipment_operation_scheme_name.setter
    def condenser_equipment_operation_scheme_name(self, value=None):
        """  Corresponds to IDD Field `condenser_equipment_operation_scheme_name`

        Args:
            value (str): value for IDD Field `condenser_equipment_operation_scheme_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_equipment_operation_scheme_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_equipment_operation_scheme_name`')

        self._data["Condenser Equipment Operation Scheme Name"] = value

    @property
    def condenser_loop_temperature_setpoint_node_name(self):
        """Get condenser_loop_temperature_setpoint_node_name

        Returns:
            str: the value of `condenser_loop_temperature_setpoint_node_name` or None if not set
        """
        return self._data["Condenser Loop Temperature Setpoint Node Name"]

    @condenser_loop_temperature_setpoint_node_name.setter
    def condenser_loop_temperature_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_loop_temperature_setpoint_node_name`

        Args:
            value (str): value for IDD Field `condenser_loop_temperature_setpoint_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_loop_temperature_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_loop_temperature_setpoint_node_name`')

        self._data["Condenser Loop Temperature Setpoint Node Name"] = value

    @property
    def maximum_loop_temperature(self):
        """Get maximum_loop_temperature

        Returns:
            float: the value of `maximum_loop_temperature` or None if not set
        """
        return self._data["Maximum Loop Temperature"]

    @maximum_loop_temperature.setter
    def maximum_loop_temperature(self, value=None):
        """  Corresponds to IDD Field `maximum_loop_temperature`

        Args:
            value (float): value for IDD Field `maximum_loop_temperature`
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
                                 'for field `maximum_loop_temperature`'.format(value))

        self._data["Maximum Loop Temperature"] = value

    @property
    def minimum_loop_temperature(self):
        """Get minimum_loop_temperature

        Returns:
            float: the value of `minimum_loop_temperature` or None if not set
        """
        return self._data["Minimum Loop Temperature"]

    @minimum_loop_temperature.setter
    def minimum_loop_temperature(self, value=None):
        """  Corresponds to IDD Field `minimum_loop_temperature`

        Args:
            value (float): value for IDD Field `minimum_loop_temperature`
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
                                 'for field `minimum_loop_temperature`'.format(value))

        self._data["Minimum Loop Temperature"] = value

    @property
    def maximum_loop_flow_rate(self):
        """Get maximum_loop_flow_rate

        Returns:
            float: the value of `maximum_loop_flow_rate` or None if not set
        """
        return self._data["Maximum Loop Flow Rate"]

    @maximum_loop_flow_rate.setter
    def maximum_loop_flow_rate(self, value=None):
        """  Corresponds to IDD Field `maximum_loop_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_loop_flow_rate`
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
                                 'for field `maximum_loop_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_loop_flow_rate`')

        self._data["Maximum Loop Flow Rate"] = value

    @property
    def minimum_loop_flow_rate(self):
        """Get minimum_loop_flow_rate

        Returns:
            float: the value of `minimum_loop_flow_rate` or None if not set
        """
        return self._data["Minimum Loop Flow Rate"]

    @minimum_loop_flow_rate.setter
    def minimum_loop_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_loop_flow_rate`

        Args:
            value (float): value for IDD Field `minimum_loop_flow_rate`
                Unit: m3/s
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
                                 'for field `minimum_loop_flow_rate`'.format(value))

        self._data["Minimum Loop Flow Rate"] = value

    @property
    def condenser_loop_volume(self):
        """Get condenser_loop_volume

        Returns:
            float: the value of `condenser_loop_volume` or None if not set
        """
        return self._data["Condenser Loop Volume"]

    @condenser_loop_volume.setter
    def condenser_loop_volume(self, value=None):
        """  Corresponds to IDD Field `condenser_loop_volume`

        Args:
            value (float): value for IDD Field `condenser_loop_volume`
                Unit: m3
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
                                 'for field `condenser_loop_volume`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `condenser_loop_volume`')

        self._data["Condenser Loop Volume"] = value

    @property
    def condenser_side_inlet_node_name(self):
        """Get condenser_side_inlet_node_name

        Returns:
            str: the value of `condenser_side_inlet_node_name` or None if not set
        """
        return self._data["Condenser Side Inlet Node Name"]

    @condenser_side_inlet_node_name.setter
    def condenser_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_side_inlet_node_name`')

        self._data["Condenser Side Inlet Node Name"] = value

    @property
    def condenser_side_outlet_node_name(self):
        """Get condenser_side_outlet_node_name

        Returns:
            str: the value of `condenser_side_outlet_node_name` or None if not set
        """
        return self._data["Condenser Side Outlet Node Name"]

    @condenser_side_outlet_node_name.setter
    def condenser_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `condenser_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_side_outlet_node_name`')

        self._data["Condenser Side Outlet Node Name"] = value

    @property
    def condenser_side_branch_list_name(self):
        """Get condenser_side_branch_list_name

        Returns:
            str: the value of `condenser_side_branch_list_name` or None if not set
        """
        return self._data["Condenser Side Branch List Name"]

    @condenser_side_branch_list_name.setter
    def condenser_side_branch_list_name(self, value=None):
        """  Corresponds to IDD Field `condenser_side_branch_list_name`

        Args:
            value (str): value for IDD Field `condenser_side_branch_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_side_branch_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_side_branch_list_name`')

        self._data["Condenser Side Branch List Name"] = value

    @property
    def condenser_side_connector_list_name(self):
        """Get condenser_side_connector_list_name

        Returns:
            str: the value of `condenser_side_connector_list_name` or None if not set
        """
        return self._data["Condenser Side Connector List Name"]

    @condenser_side_connector_list_name.setter
    def condenser_side_connector_list_name(self, value=None):
        """  Corresponds to IDD Field `condenser_side_connector_list_name`

        Args:
            value (str): value for IDD Field `condenser_side_connector_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_side_connector_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_side_connector_list_name`')

        self._data["Condenser Side Connector List Name"] = value

    @property
    def demand_side_inlet_node_name(self):
        """Get demand_side_inlet_node_name

        Returns:
            str: the value of `demand_side_inlet_node_name` or None if not set
        """
        return self._data["Demand Side Inlet Node Name"]

    @demand_side_inlet_node_name.setter
    def demand_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `demand_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_inlet_node_name`')

        self._data["Demand Side Inlet Node Name"] = value

    @property
    def demand_side_outlet_node_name(self):
        """Get demand_side_outlet_node_name

        Returns:
            str: the value of `demand_side_outlet_node_name` or None if not set
        """
        return self._data["Demand Side Outlet Node Name"]

    @demand_side_outlet_node_name.setter
    def demand_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `demand_side_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_outlet_node_name`')

        self._data["Demand Side Outlet Node Name"] = value

    @property
    def condenser_demand_side_branch_list_name(self):
        """Get condenser_demand_side_branch_list_name

        Returns:
            str: the value of `condenser_demand_side_branch_list_name` or None if not set
        """
        return self._data["Condenser Demand Side Branch List Name"]

    @condenser_demand_side_branch_list_name.setter
    def condenser_demand_side_branch_list_name(self, value=None):
        """  Corresponds to IDD Field `condenser_demand_side_branch_list_name`

        Args:
            value (str): value for IDD Field `condenser_demand_side_branch_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_demand_side_branch_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_demand_side_branch_list_name`')

        self._data["Condenser Demand Side Branch List Name"] = value

    @property
    def condenser_demand_side_connector_list_name(self):
        """Get condenser_demand_side_connector_list_name

        Returns:
            str: the value of `condenser_demand_side_connector_list_name` or None if not set
        """
        return self._data["Condenser Demand Side Connector List Name"]

    @condenser_demand_side_connector_list_name.setter
    def condenser_demand_side_connector_list_name(self, value=None):
        """  Corresponds to IDD Field `condenser_demand_side_connector_list_name`

        Args:
            value (str): value for IDD Field `condenser_demand_side_connector_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `condenser_demand_side_connector_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_demand_side_connector_list_name`')

        self._data["Condenser Demand Side Connector List Name"] = value

    @property
    def load_distribution_scheme(self):
        """Get load_distribution_scheme

        Returns:
            str: the value of `load_distribution_scheme` or None if not set
        """
        return self._data["Load Distribution Scheme"]

    @load_distribution_scheme.setter
    def load_distribution_scheme(self, value="SequentialLoad"):
        """  Corresponds to IDD Field `load_distribution_scheme`

        Args:
            value (str): value for IDD Field `load_distribution_scheme`
                Accepted values are:
                      - Optimal
                      - SequentialLoad
                      - UniformLoad
                      - UniformPLR
                      - SequentialUniformPLR
                Default value: SequentialLoad
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `load_distribution_scheme`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_distribution_scheme`')
            vals = set()
            vals.add("Optimal")
            vals.add("SequentialLoad")
            vals.add("UniformLoad")
            vals.add("UniformPLR")
            vals.add("SequentialUniformPLR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `load_distribution_scheme`'.format(value))

        self._data["Load Distribution Scheme"] = value

    @property
    def pressure_simulation_type(self):
        """Get pressure_simulation_type

        Returns:
            str: the value of `pressure_simulation_type` or None if not set
        """
        return self._data["Pressure Simulation Type"]

    @pressure_simulation_type.setter
    def pressure_simulation_type(self, value="None"):
        """  Corresponds to IDD Field `pressure_simulation_type`

        Args:
            value (str): value for IDD Field `pressure_simulation_type`
                Accepted values are:
                      - PumpPowerCorrection
                      - LoopFlowCorrection
                      - None
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
                                 'for field `pressure_simulation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pressure_simulation_type`')
            vals = set()
            vals.add("PumpPowerCorrection")
            vals.add("LoopFlowCorrection")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `pressure_simulation_type`'.format(value))

        self._data["Pressure Simulation Type"] = value

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
        out.append(self._to_str(self.fluid_type))
        out.append(self._to_str(self.user_defined_fluid_type))
        out.append(self._to_str(self.condenser_equipment_operation_scheme_name))
        out.append(self._to_str(self.condenser_loop_temperature_setpoint_node_name))
        out.append(self._to_str(self.maximum_loop_temperature))
        out.append(self._to_str(self.minimum_loop_temperature))
        out.append(self._to_str(self.maximum_loop_flow_rate))
        out.append(self._to_str(self.minimum_loop_flow_rate))
        out.append(self._to_str(self.condenser_loop_volume))
        out.append(self._to_str(self.condenser_side_inlet_node_name))
        out.append(self._to_str(self.condenser_side_outlet_node_name))
        out.append(self._to_str(self.condenser_side_branch_list_name))
        out.append(self._to_str(self.condenser_side_connector_list_name))
        out.append(self._to_str(self.demand_side_inlet_node_name))
        out.append(self._to_str(self.demand_side_outlet_node_name))
        out.append(self._to_str(self.condenser_demand_side_branch_list_name))
        out.append(self._to_str(self.condenser_demand_side_connector_list_name))
        out.append(self._to_str(self.load_distribution_scheme))
        out.append(self._to_str(self.pressure_simulation_type))
        return ",".join(out)