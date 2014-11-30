from collections import OrderedDict

class AirLoopHvac(object):
    """ Corresponds to IDD object `AirLoopHVAC`
        Defines a central forced air system.
    """
    internal_name = "AirLoopHVAC"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Controller List Name"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Design Supply Air Flow Rate"] = None
        self._data["Branch List Name"] = None
        self._data["Connector List Name"] = None
        self._data["Supply Side Inlet Node Name"] = None
        self._data["Demand Side Outlet Node Name"] = None
        self._data["Demand Side Inlet Node Names"] = None
        self._data["Supply Side Outlet Node Names"] = None

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
            self.controller_list_name = None
        else:
            self.controller_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate = None
        else:
            self.design_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_list_name = None
        else:
            self.branch_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.connector_list_name = None
        else:
            self.connector_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_side_inlet_node_name = None
        else:
            self.supply_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_side_outlet_node_name = None
        else:
            self.demand_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_side_inlet_node_names = None
        else:
            self.demand_side_inlet_node_names = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_side_outlet_node_names = None
        else:
            self.supply_side_outlet_node_names = vals[i]
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
    def controller_list_name(self):
        """Get controller_list_name

        Returns:
            str: the value of `controller_list_name` or None if not set
        """
        return self._data["Controller List Name"]

    @controller_list_name.setter
    def controller_list_name(self, value=None):
        """  Corresponds to IDD Field `controller_list_name`
        Enter the name of an AirLoopHVAC:ControllerList object.

        Args:
            value (str): value for IDD Field `controller_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_list_name`')

        self._data["Controller List Name"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')

        self._data["Availability Manager List Name"] = value

    @property
    def design_supply_air_flow_rate(self):
        """Get design_supply_air_flow_rate

        Returns:
            float: the value of `design_supply_air_flow_rate` or None if not set
        """
        return self._data["Design Supply Air Flow Rate"]

    @design_supply_air_flow_rate.setter
    def design_supply_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `design_supply_air_flow_rate`

        Args:
            value (float): value for IDD Field `design_supply_air_flow_rate`
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
                                 'for field `design_supply_air_flow_rate`'.format(value))

        self._data["Design Supply Air Flow Rate"] = value

    @property
    def branch_list_name(self):
        """Get branch_list_name

        Returns:
            str: the value of `branch_list_name` or None if not set
        """
        return self._data["Branch List Name"]

    @branch_list_name.setter
    def branch_list_name(self, value=None):
        """  Corresponds to IDD Field `branch_list_name`
        Name of a BranchList containing all the branches in this air loop

        Args:
            value (str): value for IDD Field `branch_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_list_name`')

        self._data["Branch List Name"] = value

    @property
    def connector_list_name(self):
        """Get connector_list_name

        Returns:
            str: the value of `connector_list_name` or None if not set
        """
        return self._data["Connector List Name"]

    @connector_list_name.setter
    def connector_list_name(self, value=None):
        """  Corresponds to IDD Field `connector_list_name`
        Name of a ConnectorList containing all the splitters and mixers in the loop

        Args:
            value (str): value for IDD Field `connector_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `connector_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `connector_list_name`')

        self._data["Connector List Name"] = value

    @property
    def supply_side_inlet_node_name(self):
        """Get supply_side_inlet_node_name

        Returns:
            str: the value of `supply_side_inlet_node_name` or None if not set
        """
        return self._data["Supply Side Inlet Node Name"]

    @supply_side_inlet_node_name.setter
    def supply_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `supply_side_inlet_node_name`
        Name of inlet node where return air enters the supply side of the air loop

        Args:
            value (str): value for IDD Field `supply_side_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_side_inlet_node_name`')

        self._data["Supply Side Inlet Node Name"] = value

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
        Name of outlet node where return air leaves the demand side and enters the supply side.

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
    def demand_side_inlet_node_names(self):
        """Get demand_side_inlet_node_names

        Returns:
            str: the value of `demand_side_inlet_node_names` or None if not set
        """
        return self._data["Demand Side Inlet Node Names"]

    @demand_side_inlet_node_names.setter
    def demand_side_inlet_node_names(self, value=None):
        """  Corresponds to IDD Field `demand_side_inlet_node_names`
        Name of a Node or NodeList containing the inlet node(s) supplying air to zone equipment.

        Args:
            value (str): value for IDD Field `demand_side_inlet_node_names`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_side_inlet_node_names`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_inlet_node_names`')

        self._data["Demand Side Inlet Node Names"] = value

    @property
    def supply_side_outlet_node_names(self):
        """Get supply_side_outlet_node_names

        Returns:
            str: the value of `supply_side_outlet_node_names` or None if not set
        """
        return self._data["Supply Side Outlet Node Names"]

    @supply_side_outlet_node_names.setter
    def supply_side_outlet_node_names(self, value=None):
        """  Corresponds to IDD Field `supply_side_outlet_node_names`
        Name of a Node or NodeList containing the outlet node(s) supplying air to the demand side.

        Args:
            value (str): value for IDD Field `supply_side_outlet_node_names`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_side_outlet_node_names`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_side_outlet_node_names`')

        self._data["Supply Side Outlet Node Names"] = value

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
        out.append(self._to_str(self.controller_list_name))
        out.append(self._to_str(self.availability_manager_list_name))
        out.append(self._to_str(self.design_supply_air_flow_rate))
        out.append(self._to_str(self.branch_list_name))
        out.append(self._to_str(self.connector_list_name))
        out.append(self._to_str(self.supply_side_inlet_node_name))
        out.append(self._to_str(self.demand_side_outlet_node_name))
        out.append(self._to_str(self.demand_side_inlet_node_names))
        out.append(self._to_str(self.supply_side_outlet_node_names))
        return ",".join(out)

class AirLoopHvacOutdoorAirSystemEquipmentList(object):
    """ Corresponds to IDD object `AirLoopHVAC:OutdoorAirSystem:EquipmentList`
        List equipment in simulation order
    """
    internal_name = "AirLoopHVAC:OutdoorAirSystem:EquipmentList"
    field_count = 19

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:OutdoorAirSystem:EquipmentList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Component 1 Object Type"] = None
        self._data["Component 1 Name"] = None
        self._data["Component 2 Object Type"] = None
        self._data["Component 2 Name"] = None
        self._data["Component 3 Object Type"] = None
        self._data["Component 3 Name"] = None
        self._data["Component 4 Object Type"] = None
        self._data["Component 4 Name"] = None
        self._data["Component 5 Object Type"] = None
        self._data["Component 5 Name"] = None
        self._data["Component 6 Object Type"] = None
        self._data["Component 6 Name"] = None
        self._data["Component 7 Object Type"] = None
        self._data["Component 7 Name"] = None
        self._data["Component 8 Object Type"] = None
        self._data["Component 8 Name"] = None
        self._data["Component 9 Object Type"] = None
        self._data["Component 9 Name"] = None

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
            self.component_1_object_type = None
        else:
            self.component_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_1_name = None
        else:
            self.component_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_object_type = None
        else:
            self.component_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_name = None
        else:
            self.component_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_object_type = None
        else:
            self.component_3_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_name = None
        else:
            self.component_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_object_type = None
        else:
            self.component_4_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_name = None
        else:
            self.component_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_object_type = None
        else:
            self.component_5_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_name = None
        else:
            self.component_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_object_type = None
        else:
            self.component_6_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_name = None
        else:
            self.component_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_object_type = None
        else:
            self.component_7_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_name = None
        else:
            self.component_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_object_type = None
        else:
            self.component_8_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_name = None
        else:
            self.component_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_9_object_type = None
        else:
            self.component_9_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_9_name = None
        else:
            self.component_9_name = vals[i]
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
    def component_1_object_type(self):
        """Get component_1_object_type

        Returns:
            str: the value of `component_1_object_type` or None if not set
        """
        return self._data["Component 1 Object Type"]

    @component_1_object_type.setter
    def component_1_object_type(self, value=None):
        """  Corresponds to IDD Field `component_1_object_type`

        Args:
            value (str): value for IDD Field `component_1_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_object_type`')

        self._data["Component 1 Object Type"] = value

    @property
    def component_1_name(self):
        """Get component_1_name

        Returns:
            str: the value of `component_1_name` or None if not set
        """
        return self._data["Component 1 Name"]

    @component_1_name.setter
    def component_1_name(self, value=None):
        """  Corresponds to IDD Field `component_1_name`

        Args:
            value (str): value for IDD Field `component_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_name`')

        self._data["Component 1 Name"] = value

    @property
    def component_2_object_type(self):
        """Get component_2_object_type

        Returns:
            str: the value of `component_2_object_type` or None if not set
        """
        return self._data["Component 2 Object Type"]

    @component_2_object_type.setter
    def component_2_object_type(self, value=None):
        """  Corresponds to IDD Field `component_2_object_type`

        Args:
            value (str): value for IDD Field `component_2_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_object_type`')

        self._data["Component 2 Object Type"] = value

    @property
    def component_2_name(self):
        """Get component_2_name

        Returns:
            str: the value of `component_2_name` or None if not set
        """
        return self._data["Component 2 Name"]

    @component_2_name.setter
    def component_2_name(self, value=None):
        """  Corresponds to IDD Field `component_2_name`

        Args:
            value (str): value for IDD Field `component_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_name`')

        self._data["Component 2 Name"] = value

    @property
    def component_3_object_type(self):
        """Get component_3_object_type

        Returns:
            str: the value of `component_3_object_type` or None if not set
        """
        return self._data["Component 3 Object Type"]

    @component_3_object_type.setter
    def component_3_object_type(self, value=None):
        """  Corresponds to IDD Field `component_3_object_type`

        Args:
            value (str): value for IDD Field `component_3_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_object_type`')

        self._data["Component 3 Object Type"] = value

    @property
    def component_3_name(self):
        """Get component_3_name

        Returns:
            str: the value of `component_3_name` or None if not set
        """
        return self._data["Component 3 Name"]

    @component_3_name.setter
    def component_3_name(self, value=None):
        """  Corresponds to IDD Field `component_3_name`

        Args:
            value (str): value for IDD Field `component_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_name`')

        self._data["Component 3 Name"] = value

    @property
    def component_4_object_type(self):
        """Get component_4_object_type

        Returns:
            str: the value of `component_4_object_type` or None if not set
        """
        return self._data["Component 4 Object Type"]

    @component_4_object_type.setter
    def component_4_object_type(self, value=None):
        """  Corresponds to IDD Field `component_4_object_type`

        Args:
            value (str): value for IDD Field `component_4_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_object_type`')

        self._data["Component 4 Object Type"] = value

    @property
    def component_4_name(self):
        """Get component_4_name

        Returns:
            str: the value of `component_4_name` or None if not set
        """
        return self._data["Component 4 Name"]

    @component_4_name.setter
    def component_4_name(self, value=None):
        """  Corresponds to IDD Field `component_4_name`

        Args:
            value (str): value for IDD Field `component_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_name`')

        self._data["Component 4 Name"] = value

    @property
    def component_5_object_type(self):
        """Get component_5_object_type

        Returns:
            str: the value of `component_5_object_type` or None if not set
        """
        return self._data["Component 5 Object Type"]

    @component_5_object_type.setter
    def component_5_object_type(self, value=None):
        """  Corresponds to IDD Field `component_5_object_type`

        Args:
            value (str): value for IDD Field `component_5_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_object_type`')

        self._data["Component 5 Object Type"] = value

    @property
    def component_5_name(self):
        """Get component_5_name

        Returns:
            str: the value of `component_5_name` or None if not set
        """
        return self._data["Component 5 Name"]

    @component_5_name.setter
    def component_5_name(self, value=None):
        """  Corresponds to IDD Field `component_5_name`

        Args:
            value (str): value for IDD Field `component_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_name`')

        self._data["Component 5 Name"] = value

    @property
    def component_6_object_type(self):
        """Get component_6_object_type

        Returns:
            str: the value of `component_6_object_type` or None if not set
        """
        return self._data["Component 6 Object Type"]

    @component_6_object_type.setter
    def component_6_object_type(self, value=None):
        """  Corresponds to IDD Field `component_6_object_type`

        Args:
            value (str): value for IDD Field `component_6_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_object_type`')

        self._data["Component 6 Object Type"] = value

    @property
    def component_6_name(self):
        """Get component_6_name

        Returns:
            str: the value of `component_6_name` or None if not set
        """
        return self._data["Component 6 Name"]

    @component_6_name.setter
    def component_6_name(self, value=None):
        """  Corresponds to IDD Field `component_6_name`

        Args:
            value (str): value for IDD Field `component_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_name`')

        self._data["Component 6 Name"] = value

    @property
    def component_7_object_type(self):
        """Get component_7_object_type

        Returns:
            str: the value of `component_7_object_type` or None if not set
        """
        return self._data["Component 7 Object Type"]

    @component_7_object_type.setter
    def component_7_object_type(self, value=None):
        """  Corresponds to IDD Field `component_7_object_type`

        Args:
            value (str): value for IDD Field `component_7_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_object_type`')

        self._data["Component 7 Object Type"] = value

    @property
    def component_7_name(self):
        """Get component_7_name

        Returns:
            str: the value of `component_7_name` or None if not set
        """
        return self._data["Component 7 Name"]

    @component_7_name.setter
    def component_7_name(self, value=None):
        """  Corresponds to IDD Field `component_7_name`

        Args:
            value (str): value for IDD Field `component_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_name`')

        self._data["Component 7 Name"] = value

    @property
    def component_8_object_type(self):
        """Get component_8_object_type

        Returns:
            str: the value of `component_8_object_type` or None if not set
        """
        return self._data["Component 8 Object Type"]

    @component_8_object_type.setter
    def component_8_object_type(self, value=None):
        """  Corresponds to IDD Field `component_8_object_type`

        Args:
            value (str): value for IDD Field `component_8_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_object_type`')

        self._data["Component 8 Object Type"] = value

    @property
    def component_8_name(self):
        """Get component_8_name

        Returns:
            str: the value of `component_8_name` or None if not set
        """
        return self._data["Component 8 Name"]

    @component_8_name.setter
    def component_8_name(self, value=None):
        """  Corresponds to IDD Field `component_8_name`

        Args:
            value (str): value for IDD Field `component_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_name`')

        self._data["Component 8 Name"] = value

    @property
    def component_9_object_type(self):
        """Get component_9_object_type

        Returns:
            str: the value of `component_9_object_type` or None if not set
        """
        return self._data["Component 9 Object Type"]

    @component_9_object_type.setter
    def component_9_object_type(self, value=None):
        """  Corresponds to IDD Field `component_9_object_type`

        Args:
            value (str): value for IDD Field `component_9_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_object_type`')

        self._data["Component 9 Object Type"] = value

    @property
    def component_9_name(self):
        """Get component_9_name

        Returns:
            str: the value of `component_9_name` or None if not set
        """
        return self._data["Component 9 Name"]

    @component_9_name.setter
    def component_9_name(self, value=None):
        """  Corresponds to IDD Field `component_9_name`

        Args:
            value (str): value for IDD Field `component_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_name`')

        self._data["Component 9 Name"] = value

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
        out.append(self._to_str(self.component_1_object_type))
        out.append(self._to_str(self.component_1_name))
        out.append(self._to_str(self.component_2_object_type))
        out.append(self._to_str(self.component_2_name))
        out.append(self._to_str(self.component_3_object_type))
        out.append(self._to_str(self.component_3_name))
        out.append(self._to_str(self.component_4_object_type))
        out.append(self._to_str(self.component_4_name))
        out.append(self._to_str(self.component_5_object_type))
        out.append(self._to_str(self.component_5_name))
        out.append(self._to_str(self.component_6_object_type))
        out.append(self._to_str(self.component_6_name))
        out.append(self._to_str(self.component_7_object_type))
        out.append(self._to_str(self.component_7_name))
        out.append(self._to_str(self.component_8_object_type))
        out.append(self._to_str(self.component_8_name))
        out.append(self._to_str(self.component_9_object_type))
        out.append(self._to_str(self.component_9_name))
        return ",".join(out)

class AirLoopHvacOutdoorAirSystem(object):
    """ Corresponds to IDD object `AirLoopHVAC:OutdoorAirSystem`
        Outdoor air subsystem for an AirLoopHVAC. Includes an outdoor air mixing box and
        optional outdoor air conditioning equipment such as heat recovery, preheat, and precool
        coils. From the perspective of the primary air loop the outdoor air system is treated
        as a single component.
    """
    internal_name = "AirLoopHVAC:OutdoorAirSystem"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:OutdoorAirSystem`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Controller List Name"] = None
        self._data["Outdoor Air Equipment List Name"] = None
        self._data["Availability Manager List Name"] = None

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
            self.controller_list_name = None
        else:
            self.controller_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_equipment_list_name = None
        else:
            self.outdoor_air_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
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
    def controller_list_name(self):
        """Get controller_list_name

        Returns:
            str: the value of `controller_list_name` or None if not set
        """
        return self._data["Controller List Name"]

    @controller_list_name.setter
    def controller_list_name(self, value=None):
        """  Corresponds to IDD Field `controller_list_name`
        Enter the name of an AirLoopHVAC:ControllerList object.

        Args:
            value (str): value for IDD Field `controller_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_list_name`')

        self._data["Controller List Name"] = value

    @property
    def outdoor_air_equipment_list_name(self):
        """Get outdoor_air_equipment_list_name

        Returns:
            str: the value of `outdoor_air_equipment_list_name` or None if not set
        """
        return self._data["Outdoor Air Equipment List Name"]

    @outdoor_air_equipment_list_name.setter
    def outdoor_air_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_equipment_list_name`
        Enter the name of an AirLoopHVAC:OutdoorAirSystem:EquipmentList object.

        Args:
            value (str): value for IDD Field `outdoor_air_equipment_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_equipment_list_name`')

        self._data["Outdoor Air Equipment List Name"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `availability_manager_list_name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `availability_manager_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')

        self._data["Availability Manager List Name"] = value

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
        out.append(self._to_str(self.controller_list_name))
        out.append(self._to_str(self.outdoor_air_equipment_list_name))
        out.append(self._to_str(self.availability_manager_list_name))
        return ",".join(out)

class OutdoorAirMixer(object):
    """ Corresponds to IDD object `OutdoorAir:Mixer`
        Outdoor air mixer. Node names cannot be duplicated within a single OutdoorAir:Mixer
        object or across all outdoor air mixers.
    """
    internal_name = "OutdoorAir:Mixer"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for IDD  `OutdoorAir:Mixer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Mixed Air Node Name"] = None
        self._data["Outdoor Air Stream Node Name"] = None
        self._data["Relief Air Stream Node Name"] = None
        self._data["Return Air Stream Node Name"] = None

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
            self.mixed_air_node_name = None
        else:
            self.mixed_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_stream_node_name = None
        else:
            self.outdoor_air_stream_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relief_air_stream_node_name = None
        else:
            self.relief_air_stream_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.return_air_stream_node_name = None
        else:
            self.return_air_stream_node_name = vals[i]
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
    def mixed_air_node_name(self):
        """Get mixed_air_node_name

        Returns:
            str: the value of `mixed_air_node_name` or None if not set
        """
        return self._data["Mixed Air Node Name"]

    @mixed_air_node_name.setter
    def mixed_air_node_name(self, value=None):
        """  Corresponds to IDD Field `mixed_air_node_name`
        Name of Mixed Air Node

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

        self._data["Mixed Air Node Name"] = value

    @property
    def outdoor_air_stream_node_name(self):
        """Get outdoor_air_stream_node_name

        Returns:
            str: the value of `outdoor_air_stream_node_name` or None if not set
        """
        return self._data["Outdoor Air Stream Node Name"]

    @outdoor_air_stream_node_name.setter
    def outdoor_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_stream_node_name`
        Name of Outdoor Air Stream Node

        Args:
            value (str): value for IDD Field `outdoor_air_stream_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_stream_node_name`')

        self._data["Outdoor Air Stream Node Name"] = value

    @property
    def relief_air_stream_node_name(self):
        """Get relief_air_stream_node_name

        Returns:
            str: the value of `relief_air_stream_node_name` or None if not set
        """
        return self._data["Relief Air Stream Node Name"]

    @relief_air_stream_node_name.setter
    def relief_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `relief_air_stream_node_name`
        Name of Relief Air Stream Node

        Args:
            value (str): value for IDD Field `relief_air_stream_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `relief_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `relief_air_stream_node_name`')

        self._data["Relief Air Stream Node Name"] = value

    @property
    def return_air_stream_node_name(self):
        """Get return_air_stream_node_name

        Returns:
            str: the value of `return_air_stream_node_name` or None if not set
        """
        return self._data["Return Air Stream Node Name"]

    @return_air_stream_node_name.setter
    def return_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `return_air_stream_node_name`
        Name of Return Air Stream Node

        Args:
            value (str): value for IDD Field `return_air_stream_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `return_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `return_air_stream_node_name`')

        self._data["Return Air Stream Node Name"] = value

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
        out.append(self._to_str(self.mixed_air_node_name))
        out.append(self._to_str(self.outdoor_air_stream_node_name))
        out.append(self._to_str(self.relief_air_stream_node_name))
        out.append(self._to_str(self.return_air_stream_node_name))
        return ",".join(out)

class AirLoopHvacSupplyPath(object):
    """ Corresponds to IDD object `AirLoopHVAC:SupplyPath`
        A supply path can only contain AirLoopHVAC:ZoneSplitter and AirLoopHVAC:SupplyPlenum objects
        which may be in series or parallel.
    """
    internal_name = "AirLoopHVAC:SupplyPath"
    field_count = 52

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:SupplyPath`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Supply Air Path Inlet Node Name"] = None
        self._data["Component 1 Object Type"] = None
        self._data["Component 1 Name"] = None
        self._data["Component 2 Object Type"] = None
        self._data["Component 2 Name"] = None
        self._data["Component 3 Object Type"] = None
        self._data["Component 3 Name"] = None
        self._data["Component 4 Object Type"] = None
        self._data["Component 4 Name"] = None
        self._data["Component 5 Object Type"] = None
        self._data["Component 5 Name"] = None
        self._data["Component 6 Object Type"] = None
        self._data["Component 6 Name"] = None
        self._data["Component 7 Object Type"] = None
        self._data["Component 7 Name"] = None
        self._data["Component 8 Object Type"] = None
        self._data["Component 8 Name"] = None
        self._data["Component 9 Object Type"] = None
        self._data["Component 9 Name"] = None
        self._data["Component 10 Object Type"] = None
        self._data["Component 10 Name"] = None
        self._data["Component 11 Object Type"] = None
        self._data["Component 11 Name"] = None
        self._data["Component 12 Object Type"] = None
        self._data["Component 12 Name"] = None
        self._data["Component 13 Object Type"] = None
        self._data["Component 13 Name"] = None
        self._data["Component 14 Object Type"] = None
        self._data["Component 14 Name"] = None
        self._data["Component 15 Object Type"] = None
        self._data["Component 15 Name"] = None
        self._data["Component 16 Object Type"] = None
        self._data["Component 16 Name"] = None
        self._data["Component 17 Object Type"] = None
        self._data["Component 17 Name"] = None
        self._data["Component 18 Object Type"] = None
        self._data["Component 18 Name"] = None
        self._data["Component 19 Object Type"] = None
        self._data["Component 19 Name"] = None
        self._data["Component 20 Object Type"] = None
        self._data["Component 20 Name"] = None
        self._data["Component 21 Object Type"] = None
        self._data["Component 21 Name"] = None
        self._data["Component 22 Object Type"] = None
        self._data["Component 22 Name"] = None
        self._data["Component 23 Object Type"] = None
        self._data["Component 23 Name"] = None
        self._data["Component 24 Object Type"] = None
        self._data["Component 24 Name"] = None
        self._data["Component 25 Object Type"] = None
        self._data["Component 25 Name"] = None

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
            self.supply_air_path_inlet_node_name = None
        else:
            self.supply_air_path_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_1_object_type = None
        else:
            self.component_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_1_name = None
        else:
            self.component_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_object_type = None
        else:
            self.component_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_name = None
        else:
            self.component_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_object_type = None
        else:
            self.component_3_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_name = None
        else:
            self.component_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_object_type = None
        else:
            self.component_4_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_name = None
        else:
            self.component_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_object_type = None
        else:
            self.component_5_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_name = None
        else:
            self.component_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_object_type = None
        else:
            self.component_6_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_name = None
        else:
            self.component_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_object_type = None
        else:
            self.component_7_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_name = None
        else:
            self.component_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_object_type = None
        else:
            self.component_8_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_name = None
        else:
            self.component_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_9_object_type = None
        else:
            self.component_9_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_9_name = None
        else:
            self.component_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_10_object_type = None
        else:
            self.component_10_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_10_name = None
        else:
            self.component_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_11_object_type = None
        else:
            self.component_11_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_11_name = None
        else:
            self.component_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_12_object_type = None
        else:
            self.component_12_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_12_name = None
        else:
            self.component_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_13_object_type = None
        else:
            self.component_13_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_13_name = None
        else:
            self.component_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_14_object_type = None
        else:
            self.component_14_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_14_name = None
        else:
            self.component_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_15_object_type = None
        else:
            self.component_15_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_15_name = None
        else:
            self.component_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_16_object_type = None
        else:
            self.component_16_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_16_name = None
        else:
            self.component_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_17_object_type = None
        else:
            self.component_17_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_17_name = None
        else:
            self.component_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_18_object_type = None
        else:
            self.component_18_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_18_name = None
        else:
            self.component_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_19_object_type = None
        else:
            self.component_19_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_19_name = None
        else:
            self.component_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_20_object_type = None
        else:
            self.component_20_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_20_name = None
        else:
            self.component_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_21_object_type = None
        else:
            self.component_21_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_21_name = None
        else:
            self.component_21_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_22_object_type = None
        else:
            self.component_22_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_22_name = None
        else:
            self.component_22_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_23_object_type = None
        else:
            self.component_23_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_23_name = None
        else:
            self.component_23_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_24_object_type = None
        else:
            self.component_24_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_24_name = None
        else:
            self.component_24_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_25_object_type = None
        else:
            self.component_25_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_25_name = None
        else:
            self.component_25_name = vals[i]
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
    def supply_air_path_inlet_node_name(self):
        """Get supply_air_path_inlet_node_name

        Returns:
            str: the value of `supply_air_path_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Path Inlet Node Name"]

    @supply_air_path_inlet_node_name.setter
    def supply_air_path_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `supply_air_path_inlet_node_name`

        Args:
            value (str): value for IDD Field `supply_air_path_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_path_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_path_inlet_node_name`')

        self._data["Supply Air Path Inlet Node Name"] = value

    @property
    def component_1_object_type(self):
        """Get component_1_object_type

        Returns:
            str: the value of `component_1_object_type` or None if not set
        """
        return self._data["Component 1 Object Type"]

    @component_1_object_type.setter
    def component_1_object_type(self, value=None):
        """  Corresponds to IDD Field `component_1_object_type`
        Supply path components must be listed in flow order.

        Args:
            value (str): value for IDD Field `component_1_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_1_object_type`'.format(value))

        self._data["Component 1 Object Type"] = value

    @property
    def component_1_name(self):
        """Get component_1_name

        Returns:
            str: the value of `component_1_name` or None if not set
        """
        return self._data["Component 1 Name"]

    @component_1_name.setter
    def component_1_name(self, value=None):
        """  Corresponds to IDD Field `component_1_name`

        Args:
            value (str): value for IDD Field `component_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_name`')

        self._data["Component 1 Name"] = value

    @property
    def component_2_object_type(self):
        """Get component_2_object_type

        Returns:
            str: the value of `component_2_object_type` or None if not set
        """
        return self._data["Component 2 Object Type"]

    @component_2_object_type.setter
    def component_2_object_type(self, value=None):
        """  Corresponds to IDD Field `component_2_object_type`

        Args:
            value (str): value for IDD Field `component_2_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_2_object_type`'.format(value))

        self._data["Component 2 Object Type"] = value

    @property
    def component_2_name(self):
        """Get component_2_name

        Returns:
            str: the value of `component_2_name` or None if not set
        """
        return self._data["Component 2 Name"]

    @component_2_name.setter
    def component_2_name(self, value=None):
        """  Corresponds to IDD Field `component_2_name`

        Args:
            value (str): value for IDD Field `component_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_name`')

        self._data["Component 2 Name"] = value

    @property
    def component_3_object_type(self):
        """Get component_3_object_type

        Returns:
            str: the value of `component_3_object_type` or None if not set
        """
        return self._data["Component 3 Object Type"]

    @component_3_object_type.setter
    def component_3_object_type(self, value=None):
        """  Corresponds to IDD Field `component_3_object_type`

        Args:
            value (str): value for IDD Field `component_3_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_3_object_type`'.format(value))

        self._data["Component 3 Object Type"] = value

    @property
    def component_3_name(self):
        """Get component_3_name

        Returns:
            str: the value of `component_3_name` or None if not set
        """
        return self._data["Component 3 Name"]

    @component_3_name.setter
    def component_3_name(self, value=None):
        """  Corresponds to IDD Field `component_3_name`

        Args:
            value (str): value for IDD Field `component_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_name`')

        self._data["Component 3 Name"] = value

    @property
    def component_4_object_type(self):
        """Get component_4_object_type

        Returns:
            str: the value of `component_4_object_type` or None if not set
        """
        return self._data["Component 4 Object Type"]

    @component_4_object_type.setter
    def component_4_object_type(self, value=None):
        """  Corresponds to IDD Field `component_4_object_type`

        Args:
            value (str): value for IDD Field `component_4_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_4_object_type`'.format(value))

        self._data["Component 4 Object Type"] = value

    @property
    def component_4_name(self):
        """Get component_4_name

        Returns:
            str: the value of `component_4_name` or None if not set
        """
        return self._data["Component 4 Name"]

    @component_4_name.setter
    def component_4_name(self, value=None):
        """  Corresponds to IDD Field `component_4_name`

        Args:
            value (str): value for IDD Field `component_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_name`')

        self._data["Component 4 Name"] = value

    @property
    def component_5_object_type(self):
        """Get component_5_object_type

        Returns:
            str: the value of `component_5_object_type` or None if not set
        """
        return self._data["Component 5 Object Type"]

    @component_5_object_type.setter
    def component_5_object_type(self, value=None):
        """  Corresponds to IDD Field `component_5_object_type`

        Args:
            value (str): value for IDD Field `component_5_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_5_object_type`'.format(value))

        self._data["Component 5 Object Type"] = value

    @property
    def component_5_name(self):
        """Get component_5_name

        Returns:
            str: the value of `component_5_name` or None if not set
        """
        return self._data["Component 5 Name"]

    @component_5_name.setter
    def component_5_name(self, value=None):
        """  Corresponds to IDD Field `component_5_name`

        Args:
            value (str): value for IDD Field `component_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_name`')

        self._data["Component 5 Name"] = value

    @property
    def component_6_object_type(self):
        """Get component_6_object_type

        Returns:
            str: the value of `component_6_object_type` or None if not set
        """
        return self._data["Component 6 Object Type"]

    @component_6_object_type.setter
    def component_6_object_type(self, value=None):
        """  Corresponds to IDD Field `component_6_object_type`

        Args:
            value (str): value for IDD Field `component_6_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_6_object_type`'.format(value))

        self._data["Component 6 Object Type"] = value

    @property
    def component_6_name(self):
        """Get component_6_name

        Returns:
            str: the value of `component_6_name` or None if not set
        """
        return self._data["Component 6 Name"]

    @component_6_name.setter
    def component_6_name(self, value=None):
        """  Corresponds to IDD Field `component_6_name`

        Args:
            value (str): value for IDD Field `component_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_name`')

        self._data["Component 6 Name"] = value

    @property
    def component_7_object_type(self):
        """Get component_7_object_type

        Returns:
            str: the value of `component_7_object_type` or None if not set
        """
        return self._data["Component 7 Object Type"]

    @component_7_object_type.setter
    def component_7_object_type(self, value=None):
        """  Corresponds to IDD Field `component_7_object_type`

        Args:
            value (str): value for IDD Field `component_7_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_7_object_type`'.format(value))

        self._data["Component 7 Object Type"] = value

    @property
    def component_7_name(self):
        """Get component_7_name

        Returns:
            str: the value of `component_7_name` or None if not set
        """
        return self._data["Component 7 Name"]

    @component_7_name.setter
    def component_7_name(self, value=None):
        """  Corresponds to IDD Field `component_7_name`

        Args:
            value (str): value for IDD Field `component_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_name`')

        self._data["Component 7 Name"] = value

    @property
    def component_8_object_type(self):
        """Get component_8_object_type

        Returns:
            str: the value of `component_8_object_type` or None if not set
        """
        return self._data["Component 8 Object Type"]

    @component_8_object_type.setter
    def component_8_object_type(self, value=None):
        """  Corresponds to IDD Field `component_8_object_type`

        Args:
            value (str): value for IDD Field `component_8_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_8_object_type`'.format(value))

        self._data["Component 8 Object Type"] = value

    @property
    def component_8_name(self):
        """Get component_8_name

        Returns:
            str: the value of `component_8_name` or None if not set
        """
        return self._data["Component 8 Name"]

    @component_8_name.setter
    def component_8_name(self, value=None):
        """  Corresponds to IDD Field `component_8_name`

        Args:
            value (str): value for IDD Field `component_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_name`')

        self._data["Component 8 Name"] = value

    @property
    def component_9_object_type(self):
        """Get component_9_object_type

        Returns:
            str: the value of `component_9_object_type` or None if not set
        """
        return self._data["Component 9 Object Type"]

    @component_9_object_type.setter
    def component_9_object_type(self, value=None):
        """  Corresponds to IDD Field `component_9_object_type`

        Args:
            value (str): value for IDD Field `component_9_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_9_object_type`'.format(value))

        self._data["Component 9 Object Type"] = value

    @property
    def component_9_name(self):
        """Get component_9_name

        Returns:
            str: the value of `component_9_name` or None if not set
        """
        return self._data["Component 9 Name"]

    @component_9_name.setter
    def component_9_name(self, value=None):
        """  Corresponds to IDD Field `component_9_name`

        Args:
            value (str): value for IDD Field `component_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_name`')

        self._data["Component 9 Name"] = value

    @property
    def component_10_object_type(self):
        """Get component_10_object_type

        Returns:
            str: the value of `component_10_object_type` or None if not set
        """
        return self._data["Component 10 Object Type"]

    @component_10_object_type.setter
    def component_10_object_type(self, value=None):
        """  Corresponds to IDD Field `component_10_object_type`

        Args:
            value (str): value for IDD Field `component_10_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_10_object_type`'.format(value))

        self._data["Component 10 Object Type"] = value

    @property
    def component_10_name(self):
        """Get component_10_name

        Returns:
            str: the value of `component_10_name` or None if not set
        """
        return self._data["Component 10 Name"]

    @component_10_name.setter
    def component_10_name(self, value=None):
        """  Corresponds to IDD Field `component_10_name`

        Args:
            value (str): value for IDD Field `component_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_name`')

        self._data["Component 10 Name"] = value

    @property
    def component_11_object_type(self):
        """Get component_11_object_type

        Returns:
            str: the value of `component_11_object_type` or None if not set
        """
        return self._data["Component 11 Object Type"]

    @component_11_object_type.setter
    def component_11_object_type(self, value=None):
        """  Corresponds to IDD Field `component_11_object_type`

        Args:
            value (str): value for IDD Field `component_11_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_11_object_type`'.format(value))

        self._data["Component 11 Object Type"] = value

    @property
    def component_11_name(self):
        """Get component_11_name

        Returns:
            str: the value of `component_11_name` or None if not set
        """
        return self._data["Component 11 Name"]

    @component_11_name.setter
    def component_11_name(self, value=None):
        """  Corresponds to IDD Field `component_11_name`

        Args:
            value (str): value for IDD Field `component_11_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_name`')

        self._data["Component 11 Name"] = value

    @property
    def component_12_object_type(self):
        """Get component_12_object_type

        Returns:
            str: the value of `component_12_object_type` or None if not set
        """
        return self._data["Component 12 Object Type"]

    @component_12_object_type.setter
    def component_12_object_type(self, value=None):
        """  Corresponds to IDD Field `component_12_object_type`

        Args:
            value (str): value for IDD Field `component_12_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_12_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_12_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_12_object_type`'.format(value))

        self._data["Component 12 Object Type"] = value

    @property
    def component_12_name(self):
        """Get component_12_name

        Returns:
            str: the value of `component_12_name` or None if not set
        """
        return self._data["Component 12 Name"]

    @component_12_name.setter
    def component_12_name(self, value=None):
        """  Corresponds to IDD Field `component_12_name`

        Args:
            value (str): value for IDD Field `component_12_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_12_name`')

        self._data["Component 12 Name"] = value

    @property
    def component_13_object_type(self):
        """Get component_13_object_type

        Returns:
            str: the value of `component_13_object_type` or None if not set
        """
        return self._data["Component 13 Object Type"]

    @component_13_object_type.setter
    def component_13_object_type(self, value=None):
        """  Corresponds to IDD Field `component_13_object_type`

        Args:
            value (str): value for IDD Field `component_13_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_13_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_13_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_13_object_type`'.format(value))

        self._data["Component 13 Object Type"] = value

    @property
    def component_13_name(self):
        """Get component_13_name

        Returns:
            str: the value of `component_13_name` or None if not set
        """
        return self._data["Component 13 Name"]

    @component_13_name.setter
    def component_13_name(self, value=None):
        """  Corresponds to IDD Field `component_13_name`

        Args:
            value (str): value for IDD Field `component_13_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_13_name`')

        self._data["Component 13 Name"] = value

    @property
    def component_14_object_type(self):
        """Get component_14_object_type

        Returns:
            str: the value of `component_14_object_type` or None if not set
        """
        return self._data["Component 14 Object Type"]

    @component_14_object_type.setter
    def component_14_object_type(self, value=None):
        """  Corresponds to IDD Field `component_14_object_type`

        Args:
            value (str): value for IDD Field `component_14_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_14_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_14_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_14_object_type`'.format(value))

        self._data["Component 14 Object Type"] = value

    @property
    def component_14_name(self):
        """Get component_14_name

        Returns:
            str: the value of `component_14_name` or None if not set
        """
        return self._data["Component 14 Name"]

    @component_14_name.setter
    def component_14_name(self, value=None):
        """  Corresponds to IDD Field `component_14_name`

        Args:
            value (str): value for IDD Field `component_14_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_14_name`')

        self._data["Component 14 Name"] = value

    @property
    def component_15_object_type(self):
        """Get component_15_object_type

        Returns:
            str: the value of `component_15_object_type` or None if not set
        """
        return self._data["Component 15 Object Type"]

    @component_15_object_type.setter
    def component_15_object_type(self, value=None):
        """  Corresponds to IDD Field `component_15_object_type`

        Args:
            value (str): value for IDD Field `component_15_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_15_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_15_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_15_object_type`'.format(value))

        self._data["Component 15 Object Type"] = value

    @property
    def component_15_name(self):
        """Get component_15_name

        Returns:
            str: the value of `component_15_name` or None if not set
        """
        return self._data["Component 15 Name"]

    @component_15_name.setter
    def component_15_name(self, value=None):
        """  Corresponds to IDD Field `component_15_name`

        Args:
            value (str): value for IDD Field `component_15_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_15_name`')

        self._data["Component 15 Name"] = value

    @property
    def component_16_object_type(self):
        """Get component_16_object_type

        Returns:
            str: the value of `component_16_object_type` or None if not set
        """
        return self._data["Component 16 Object Type"]

    @component_16_object_type.setter
    def component_16_object_type(self, value=None):
        """  Corresponds to IDD Field `component_16_object_type`

        Args:
            value (str): value for IDD Field `component_16_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_16_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_16_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_16_object_type`'.format(value))

        self._data["Component 16 Object Type"] = value

    @property
    def component_16_name(self):
        """Get component_16_name

        Returns:
            str: the value of `component_16_name` or None if not set
        """
        return self._data["Component 16 Name"]

    @component_16_name.setter
    def component_16_name(self, value=None):
        """  Corresponds to IDD Field `component_16_name`

        Args:
            value (str): value for IDD Field `component_16_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_16_name`')

        self._data["Component 16 Name"] = value

    @property
    def component_17_object_type(self):
        """Get component_17_object_type

        Returns:
            str: the value of `component_17_object_type` or None if not set
        """
        return self._data["Component 17 Object Type"]

    @component_17_object_type.setter
    def component_17_object_type(self, value=None):
        """  Corresponds to IDD Field `component_17_object_type`

        Args:
            value (str): value for IDD Field `component_17_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_17_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_17_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_17_object_type`'.format(value))

        self._data["Component 17 Object Type"] = value

    @property
    def component_17_name(self):
        """Get component_17_name

        Returns:
            str: the value of `component_17_name` or None if not set
        """
        return self._data["Component 17 Name"]

    @component_17_name.setter
    def component_17_name(self, value=None):
        """  Corresponds to IDD Field `component_17_name`

        Args:
            value (str): value for IDD Field `component_17_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_17_name`')

        self._data["Component 17 Name"] = value

    @property
    def component_18_object_type(self):
        """Get component_18_object_type

        Returns:
            str: the value of `component_18_object_type` or None if not set
        """
        return self._data["Component 18 Object Type"]

    @component_18_object_type.setter
    def component_18_object_type(self, value=None):
        """  Corresponds to IDD Field `component_18_object_type`

        Args:
            value (str): value for IDD Field `component_18_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_18_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_18_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_18_object_type`'.format(value))

        self._data["Component 18 Object Type"] = value

    @property
    def component_18_name(self):
        """Get component_18_name

        Returns:
            str: the value of `component_18_name` or None if not set
        """
        return self._data["Component 18 Name"]

    @component_18_name.setter
    def component_18_name(self, value=None):
        """  Corresponds to IDD Field `component_18_name`

        Args:
            value (str): value for IDD Field `component_18_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_18_name`')

        self._data["Component 18 Name"] = value

    @property
    def component_19_object_type(self):
        """Get component_19_object_type

        Returns:
            str: the value of `component_19_object_type` or None if not set
        """
        return self._data["Component 19 Object Type"]

    @component_19_object_type.setter
    def component_19_object_type(self, value=None):
        """  Corresponds to IDD Field `component_19_object_type`

        Args:
            value (str): value for IDD Field `component_19_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_19_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_19_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_19_object_type`'.format(value))

        self._data["Component 19 Object Type"] = value

    @property
    def component_19_name(self):
        """Get component_19_name

        Returns:
            str: the value of `component_19_name` or None if not set
        """
        return self._data["Component 19 Name"]

    @component_19_name.setter
    def component_19_name(self, value=None):
        """  Corresponds to IDD Field `component_19_name`

        Args:
            value (str): value for IDD Field `component_19_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_19_name`')

        self._data["Component 19 Name"] = value

    @property
    def component_20_object_type(self):
        """Get component_20_object_type

        Returns:
            str: the value of `component_20_object_type` or None if not set
        """
        return self._data["Component 20 Object Type"]

    @component_20_object_type.setter
    def component_20_object_type(self, value=None):
        """  Corresponds to IDD Field `component_20_object_type`

        Args:
            value (str): value for IDD Field `component_20_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_20_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_20_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_20_object_type`'.format(value))

        self._data["Component 20 Object Type"] = value

    @property
    def component_20_name(self):
        """Get component_20_name

        Returns:
            str: the value of `component_20_name` or None if not set
        """
        return self._data["Component 20 Name"]

    @component_20_name.setter
    def component_20_name(self, value=None):
        """  Corresponds to IDD Field `component_20_name`

        Args:
            value (str): value for IDD Field `component_20_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_20_name`')

        self._data["Component 20 Name"] = value

    @property
    def component_21_object_type(self):
        """Get component_21_object_type

        Returns:
            str: the value of `component_21_object_type` or None if not set
        """
        return self._data["Component 21 Object Type"]

    @component_21_object_type.setter
    def component_21_object_type(self, value=None):
        """  Corresponds to IDD Field `component_21_object_type`

        Args:
            value (str): value for IDD Field `component_21_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_21_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_21_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_21_object_type`'.format(value))

        self._data["Component 21 Object Type"] = value

    @property
    def component_21_name(self):
        """Get component_21_name

        Returns:
            str: the value of `component_21_name` or None if not set
        """
        return self._data["Component 21 Name"]

    @component_21_name.setter
    def component_21_name(self, value=None):
        """  Corresponds to IDD Field `component_21_name`

        Args:
            value (str): value for IDD Field `component_21_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_21_name`')

        self._data["Component 21 Name"] = value

    @property
    def component_22_object_type(self):
        """Get component_22_object_type

        Returns:
            str: the value of `component_22_object_type` or None if not set
        """
        return self._data["Component 22 Object Type"]

    @component_22_object_type.setter
    def component_22_object_type(self, value=None):
        """  Corresponds to IDD Field `component_22_object_type`

        Args:
            value (str): value for IDD Field `component_22_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_22_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_22_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_22_object_type`'.format(value))

        self._data["Component 22 Object Type"] = value

    @property
    def component_22_name(self):
        """Get component_22_name

        Returns:
            str: the value of `component_22_name` or None if not set
        """
        return self._data["Component 22 Name"]

    @component_22_name.setter
    def component_22_name(self, value=None):
        """  Corresponds to IDD Field `component_22_name`

        Args:
            value (str): value for IDD Field `component_22_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_22_name`')

        self._data["Component 22 Name"] = value

    @property
    def component_23_object_type(self):
        """Get component_23_object_type

        Returns:
            str: the value of `component_23_object_type` or None if not set
        """
        return self._data["Component 23 Object Type"]

    @component_23_object_type.setter
    def component_23_object_type(self, value=None):
        """  Corresponds to IDD Field `component_23_object_type`

        Args:
            value (str): value for IDD Field `component_23_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_23_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_23_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_23_object_type`'.format(value))

        self._data["Component 23 Object Type"] = value

    @property
    def component_23_name(self):
        """Get component_23_name

        Returns:
            str: the value of `component_23_name` or None if not set
        """
        return self._data["Component 23 Name"]

    @component_23_name.setter
    def component_23_name(self, value=None):
        """  Corresponds to IDD Field `component_23_name`

        Args:
            value (str): value for IDD Field `component_23_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_23_name`')

        self._data["Component 23 Name"] = value

    @property
    def component_24_object_type(self):
        """Get component_24_object_type

        Returns:
            str: the value of `component_24_object_type` or None if not set
        """
        return self._data["Component 24 Object Type"]

    @component_24_object_type.setter
    def component_24_object_type(self, value=None):
        """  Corresponds to IDD Field `component_24_object_type`

        Args:
            value (str): value for IDD Field `component_24_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_24_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_24_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_24_object_type`'.format(value))

        self._data["Component 24 Object Type"] = value

    @property
    def component_24_name(self):
        """Get component_24_name

        Returns:
            str: the value of `component_24_name` or None if not set
        """
        return self._data["Component 24 Name"]

    @component_24_name.setter
    def component_24_name(self, value=None):
        """  Corresponds to IDD Field `component_24_name`

        Args:
            value (str): value for IDD Field `component_24_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_24_name`')

        self._data["Component 24 Name"] = value

    @property
    def component_25_object_type(self):
        """Get component_25_object_type

        Returns:
            str: the value of `component_25_object_type` or None if not set
        """
        return self._data["Component 25 Object Type"]

    @component_25_object_type.setter
    def component_25_object_type(self, value=None):
        """  Corresponds to IDD Field `component_25_object_type`

        Args:
            value (str): value for IDD Field `component_25_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_25_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_25_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:SupplyPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_25_object_type`'.format(value))

        self._data["Component 25 Object Type"] = value

    @property
    def component_25_name(self):
        """Get component_25_name

        Returns:
            str: the value of `component_25_name` or None if not set
        """
        return self._data["Component 25 Name"]

    @component_25_name.setter
    def component_25_name(self, value=None):
        """  Corresponds to IDD Field `component_25_name`

        Args:
            value (str): value for IDD Field `component_25_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_25_name`')

        self._data["Component 25 Name"] = value

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
        out.append(self._to_str(self.supply_air_path_inlet_node_name))
        out.append(self._to_str(self.component_1_object_type))
        out.append(self._to_str(self.component_1_name))
        out.append(self._to_str(self.component_2_object_type))
        out.append(self._to_str(self.component_2_name))
        out.append(self._to_str(self.component_3_object_type))
        out.append(self._to_str(self.component_3_name))
        out.append(self._to_str(self.component_4_object_type))
        out.append(self._to_str(self.component_4_name))
        out.append(self._to_str(self.component_5_object_type))
        out.append(self._to_str(self.component_5_name))
        out.append(self._to_str(self.component_6_object_type))
        out.append(self._to_str(self.component_6_name))
        out.append(self._to_str(self.component_7_object_type))
        out.append(self._to_str(self.component_7_name))
        out.append(self._to_str(self.component_8_object_type))
        out.append(self._to_str(self.component_8_name))
        out.append(self._to_str(self.component_9_object_type))
        out.append(self._to_str(self.component_9_name))
        out.append(self._to_str(self.component_10_object_type))
        out.append(self._to_str(self.component_10_name))
        out.append(self._to_str(self.component_11_object_type))
        out.append(self._to_str(self.component_11_name))
        out.append(self._to_str(self.component_12_object_type))
        out.append(self._to_str(self.component_12_name))
        out.append(self._to_str(self.component_13_object_type))
        out.append(self._to_str(self.component_13_name))
        out.append(self._to_str(self.component_14_object_type))
        out.append(self._to_str(self.component_14_name))
        out.append(self._to_str(self.component_15_object_type))
        out.append(self._to_str(self.component_15_name))
        out.append(self._to_str(self.component_16_object_type))
        out.append(self._to_str(self.component_16_name))
        out.append(self._to_str(self.component_17_object_type))
        out.append(self._to_str(self.component_17_name))
        out.append(self._to_str(self.component_18_object_type))
        out.append(self._to_str(self.component_18_name))
        out.append(self._to_str(self.component_19_object_type))
        out.append(self._to_str(self.component_19_name))
        out.append(self._to_str(self.component_20_object_type))
        out.append(self._to_str(self.component_20_name))
        out.append(self._to_str(self.component_21_object_type))
        out.append(self._to_str(self.component_21_name))
        out.append(self._to_str(self.component_22_object_type))
        out.append(self._to_str(self.component_22_name))
        out.append(self._to_str(self.component_23_object_type))
        out.append(self._to_str(self.component_23_name))
        out.append(self._to_str(self.component_24_object_type))
        out.append(self._to_str(self.component_24_name))
        out.append(self._to_str(self.component_25_object_type))
        out.append(self._to_str(self.component_25_name))
        return ",".join(out)

class AirLoopHvacReturnPath(object):
    """ Corresponds to IDD object `AirLoopHVAC:ReturnPath`
        A return air path can only contain one AirLoopHVAC:ZoneMixer
        and one or more AirLoopHVAC:ReturnPlenum objects.
    """
    internal_name = "AirLoopHVAC:ReturnPath"
    field_count = 52

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:ReturnPath`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Return Air Path Outlet Node Name"] = None
        self._data["Component 1 Object Type"] = None
        self._data["Component 1 Name"] = None
        self._data["Component 2 Object Type"] = None
        self._data["Component 2 Name"] = None
        self._data["Component 3 Object Type"] = None
        self._data["Component 3 Name"] = None
        self._data["Component 4 Object Type"] = None
        self._data["Component 4 Name"] = None
        self._data["Component 5 Object Type"] = None
        self._data["Component 5 Name"] = None
        self._data["Component 6 Object Type"] = None
        self._data["Component 6 Name"] = None
        self._data["Component 7 Object Type"] = None
        self._data["Component 7 Name"] = None
        self._data["Component 8 Object Type"] = None
        self._data["Component 8 Name"] = None
        self._data["Component 9 Object Type"] = None
        self._data["Component 9 Name"] = None
        self._data["Component 10 Object Type"] = None
        self._data["Component 10 Name"] = None
        self._data["Component 11 Object Type"] = None
        self._data["Component 11 Name"] = None
        self._data["Component 12 Object Type"] = None
        self._data["Component 12 Name"] = None
        self._data["Component 13 Object Type"] = None
        self._data["Component 13 Name"] = None
        self._data["Component 14 Object Type"] = None
        self._data["Component 14 Name"] = None
        self._data["Component 15 Object Type"] = None
        self._data["Component 15 Name"] = None
        self._data["Component 16 Object Type"] = None
        self._data["Component 16 Name"] = None
        self._data["Component 17 Object Type"] = None
        self._data["Component 17 Name"] = None
        self._data["Component 18 Object Type"] = None
        self._data["Component 18 Name"] = None
        self._data["Component 19 Object Type"] = None
        self._data["Component 19 Name"] = None
        self._data["Component 20 Object Type"] = None
        self._data["Component 20 Name"] = None
        self._data["Component 21 Object Type"] = None
        self._data["Component 21 Name"] = None
        self._data["Component 22 Object Type"] = None
        self._data["Component 22 Name"] = None
        self._data["Component 23 Object Type"] = None
        self._data["Component 23 Name"] = None
        self._data["Component 24 Object Type"] = None
        self._data["Component 24 Name"] = None
        self._data["Component 25 Object Type"] = None
        self._data["Component 25 Name"] = None

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
            self.return_air_path_outlet_node_name = None
        else:
            self.return_air_path_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_1_object_type = None
        else:
            self.component_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_1_name = None
        else:
            self.component_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_object_type = None
        else:
            self.component_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_name = None
        else:
            self.component_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_object_type = None
        else:
            self.component_3_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_name = None
        else:
            self.component_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_object_type = None
        else:
            self.component_4_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_name = None
        else:
            self.component_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_object_type = None
        else:
            self.component_5_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_name = None
        else:
            self.component_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_object_type = None
        else:
            self.component_6_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_name = None
        else:
            self.component_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_object_type = None
        else:
            self.component_7_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_name = None
        else:
            self.component_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_object_type = None
        else:
            self.component_8_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_name = None
        else:
            self.component_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_9_object_type = None
        else:
            self.component_9_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_9_name = None
        else:
            self.component_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_10_object_type = None
        else:
            self.component_10_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_10_name = None
        else:
            self.component_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_11_object_type = None
        else:
            self.component_11_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_11_name = None
        else:
            self.component_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_12_object_type = None
        else:
            self.component_12_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_12_name = None
        else:
            self.component_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_13_object_type = None
        else:
            self.component_13_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_13_name = None
        else:
            self.component_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_14_object_type = None
        else:
            self.component_14_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_14_name = None
        else:
            self.component_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_15_object_type = None
        else:
            self.component_15_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_15_name = None
        else:
            self.component_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_16_object_type = None
        else:
            self.component_16_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_16_name = None
        else:
            self.component_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_17_object_type = None
        else:
            self.component_17_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_17_name = None
        else:
            self.component_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_18_object_type = None
        else:
            self.component_18_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_18_name = None
        else:
            self.component_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_19_object_type = None
        else:
            self.component_19_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_19_name = None
        else:
            self.component_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_20_object_type = None
        else:
            self.component_20_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_20_name = None
        else:
            self.component_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_21_object_type = None
        else:
            self.component_21_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_21_name = None
        else:
            self.component_21_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_22_object_type = None
        else:
            self.component_22_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_22_name = None
        else:
            self.component_22_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_23_object_type = None
        else:
            self.component_23_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_23_name = None
        else:
            self.component_23_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_24_object_type = None
        else:
            self.component_24_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_24_name = None
        else:
            self.component_24_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_25_object_type = None
        else:
            self.component_25_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_25_name = None
        else:
            self.component_25_name = vals[i]
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
    def return_air_path_outlet_node_name(self):
        """Get return_air_path_outlet_node_name

        Returns:
            str: the value of `return_air_path_outlet_node_name` or None if not set
        """
        return self._data["Return Air Path Outlet Node Name"]

    @return_air_path_outlet_node_name.setter
    def return_air_path_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `return_air_path_outlet_node_name`

        Args:
            value (str): value for IDD Field `return_air_path_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `return_air_path_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `return_air_path_outlet_node_name`')

        self._data["Return Air Path Outlet Node Name"] = value

    @property
    def component_1_object_type(self):
        """Get component_1_object_type

        Returns:
            str: the value of `component_1_object_type` or None if not set
        """
        return self._data["Component 1 Object Type"]

    @component_1_object_type.setter
    def component_1_object_type(self, value=None):
        """  Corresponds to IDD Field `component_1_object_type`

        Args:
            value (str): value for IDD Field `component_1_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_1_object_type`'.format(value))

        self._data["Component 1 Object Type"] = value

    @property
    def component_1_name(self):
        """Get component_1_name

        Returns:
            str: the value of `component_1_name` or None if not set
        """
        return self._data["Component 1 Name"]

    @component_1_name.setter
    def component_1_name(self, value=None):
        """  Corresponds to IDD Field `component_1_name`

        Args:
            value (str): value for IDD Field `component_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_name`')

        self._data["Component 1 Name"] = value

    @property
    def component_2_object_type(self):
        """Get component_2_object_type

        Returns:
            str: the value of `component_2_object_type` or None if not set
        """
        return self._data["Component 2 Object Type"]

    @component_2_object_type.setter
    def component_2_object_type(self, value=None):
        """  Corresponds to IDD Field `component_2_object_type`

        Args:
            value (str): value for IDD Field `component_2_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_2_object_type`'.format(value))

        self._data["Component 2 Object Type"] = value

    @property
    def component_2_name(self):
        """Get component_2_name

        Returns:
            str: the value of `component_2_name` or None if not set
        """
        return self._data["Component 2 Name"]

    @component_2_name.setter
    def component_2_name(self, value=None):
        """  Corresponds to IDD Field `component_2_name`

        Args:
            value (str): value for IDD Field `component_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_name`')

        self._data["Component 2 Name"] = value

    @property
    def component_3_object_type(self):
        """Get component_3_object_type

        Returns:
            str: the value of `component_3_object_type` or None if not set
        """
        return self._data["Component 3 Object Type"]

    @component_3_object_type.setter
    def component_3_object_type(self, value=None):
        """  Corresponds to IDD Field `component_3_object_type`

        Args:
            value (str): value for IDD Field `component_3_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_3_object_type`'.format(value))

        self._data["Component 3 Object Type"] = value

    @property
    def component_3_name(self):
        """Get component_3_name

        Returns:
            str: the value of `component_3_name` or None if not set
        """
        return self._data["Component 3 Name"]

    @component_3_name.setter
    def component_3_name(self, value=None):
        """  Corresponds to IDD Field `component_3_name`

        Args:
            value (str): value for IDD Field `component_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_name`')

        self._data["Component 3 Name"] = value

    @property
    def component_4_object_type(self):
        """Get component_4_object_type

        Returns:
            str: the value of `component_4_object_type` or None if not set
        """
        return self._data["Component 4 Object Type"]

    @component_4_object_type.setter
    def component_4_object_type(self, value=None):
        """  Corresponds to IDD Field `component_4_object_type`

        Args:
            value (str): value for IDD Field `component_4_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_4_object_type`'.format(value))

        self._data["Component 4 Object Type"] = value

    @property
    def component_4_name(self):
        """Get component_4_name

        Returns:
            str: the value of `component_4_name` or None if not set
        """
        return self._data["Component 4 Name"]

    @component_4_name.setter
    def component_4_name(self, value=None):
        """  Corresponds to IDD Field `component_4_name`

        Args:
            value (str): value for IDD Field `component_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_name`')

        self._data["Component 4 Name"] = value

    @property
    def component_5_object_type(self):
        """Get component_5_object_type

        Returns:
            str: the value of `component_5_object_type` or None if not set
        """
        return self._data["Component 5 Object Type"]

    @component_5_object_type.setter
    def component_5_object_type(self, value=None):
        """  Corresponds to IDD Field `component_5_object_type`

        Args:
            value (str): value for IDD Field `component_5_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_5_object_type`'.format(value))

        self._data["Component 5 Object Type"] = value

    @property
    def component_5_name(self):
        """Get component_5_name

        Returns:
            str: the value of `component_5_name` or None if not set
        """
        return self._data["Component 5 Name"]

    @component_5_name.setter
    def component_5_name(self, value=None):
        """  Corresponds to IDD Field `component_5_name`

        Args:
            value (str): value for IDD Field `component_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_name`')

        self._data["Component 5 Name"] = value

    @property
    def component_6_object_type(self):
        """Get component_6_object_type

        Returns:
            str: the value of `component_6_object_type` or None if not set
        """
        return self._data["Component 6 Object Type"]

    @component_6_object_type.setter
    def component_6_object_type(self, value=None):
        """  Corresponds to IDD Field `component_6_object_type`

        Args:
            value (str): value for IDD Field `component_6_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_6_object_type`'.format(value))

        self._data["Component 6 Object Type"] = value

    @property
    def component_6_name(self):
        """Get component_6_name

        Returns:
            str: the value of `component_6_name` or None if not set
        """
        return self._data["Component 6 Name"]

    @component_6_name.setter
    def component_6_name(self, value=None):
        """  Corresponds to IDD Field `component_6_name`

        Args:
            value (str): value for IDD Field `component_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_name`')

        self._data["Component 6 Name"] = value

    @property
    def component_7_object_type(self):
        """Get component_7_object_type

        Returns:
            str: the value of `component_7_object_type` or None if not set
        """
        return self._data["Component 7 Object Type"]

    @component_7_object_type.setter
    def component_7_object_type(self, value=None):
        """  Corresponds to IDD Field `component_7_object_type`

        Args:
            value (str): value for IDD Field `component_7_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_7_object_type`'.format(value))

        self._data["Component 7 Object Type"] = value

    @property
    def component_7_name(self):
        """Get component_7_name

        Returns:
            str: the value of `component_7_name` or None if not set
        """
        return self._data["Component 7 Name"]

    @component_7_name.setter
    def component_7_name(self, value=None):
        """  Corresponds to IDD Field `component_7_name`

        Args:
            value (str): value for IDD Field `component_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_name`')

        self._data["Component 7 Name"] = value

    @property
    def component_8_object_type(self):
        """Get component_8_object_type

        Returns:
            str: the value of `component_8_object_type` or None if not set
        """
        return self._data["Component 8 Object Type"]

    @component_8_object_type.setter
    def component_8_object_type(self, value=None):
        """  Corresponds to IDD Field `component_8_object_type`

        Args:
            value (str): value for IDD Field `component_8_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_8_object_type`'.format(value))

        self._data["Component 8 Object Type"] = value

    @property
    def component_8_name(self):
        """Get component_8_name

        Returns:
            str: the value of `component_8_name` or None if not set
        """
        return self._data["Component 8 Name"]

    @component_8_name.setter
    def component_8_name(self, value=None):
        """  Corresponds to IDD Field `component_8_name`

        Args:
            value (str): value for IDD Field `component_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_name`')

        self._data["Component 8 Name"] = value

    @property
    def component_9_object_type(self):
        """Get component_9_object_type

        Returns:
            str: the value of `component_9_object_type` or None if not set
        """
        return self._data["Component 9 Object Type"]

    @component_9_object_type.setter
    def component_9_object_type(self, value=None):
        """  Corresponds to IDD Field `component_9_object_type`

        Args:
            value (str): value for IDD Field `component_9_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_9_object_type`'.format(value))

        self._data["Component 9 Object Type"] = value

    @property
    def component_9_name(self):
        """Get component_9_name

        Returns:
            str: the value of `component_9_name` or None if not set
        """
        return self._data["Component 9 Name"]

    @component_9_name.setter
    def component_9_name(self, value=None):
        """  Corresponds to IDD Field `component_9_name`

        Args:
            value (str): value for IDD Field `component_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_name`')

        self._data["Component 9 Name"] = value

    @property
    def component_10_object_type(self):
        """Get component_10_object_type

        Returns:
            str: the value of `component_10_object_type` or None if not set
        """
        return self._data["Component 10 Object Type"]

    @component_10_object_type.setter
    def component_10_object_type(self, value=None):
        """  Corresponds to IDD Field `component_10_object_type`

        Args:
            value (str): value for IDD Field `component_10_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_10_object_type`'.format(value))

        self._data["Component 10 Object Type"] = value

    @property
    def component_10_name(self):
        """Get component_10_name

        Returns:
            str: the value of `component_10_name` or None if not set
        """
        return self._data["Component 10 Name"]

    @component_10_name.setter
    def component_10_name(self, value=None):
        """  Corresponds to IDD Field `component_10_name`

        Args:
            value (str): value for IDD Field `component_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_name`')

        self._data["Component 10 Name"] = value

    @property
    def component_11_object_type(self):
        """Get component_11_object_type

        Returns:
            str: the value of `component_11_object_type` or None if not set
        """
        return self._data["Component 11 Object Type"]

    @component_11_object_type.setter
    def component_11_object_type(self, value=None):
        """  Corresponds to IDD Field `component_11_object_type`

        Args:
            value (str): value for IDD Field `component_11_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_11_object_type`'.format(value))

        self._data["Component 11 Object Type"] = value

    @property
    def component_11_name(self):
        """Get component_11_name

        Returns:
            str: the value of `component_11_name` or None if not set
        """
        return self._data["Component 11 Name"]

    @component_11_name.setter
    def component_11_name(self, value=None):
        """  Corresponds to IDD Field `component_11_name`

        Args:
            value (str): value for IDD Field `component_11_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_name`')

        self._data["Component 11 Name"] = value

    @property
    def component_12_object_type(self):
        """Get component_12_object_type

        Returns:
            str: the value of `component_12_object_type` or None if not set
        """
        return self._data["Component 12 Object Type"]

    @component_12_object_type.setter
    def component_12_object_type(self, value=None):
        """  Corresponds to IDD Field `component_12_object_type`

        Args:
            value (str): value for IDD Field `component_12_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_12_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_12_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_12_object_type`'.format(value))

        self._data["Component 12 Object Type"] = value

    @property
    def component_12_name(self):
        """Get component_12_name

        Returns:
            str: the value of `component_12_name` or None if not set
        """
        return self._data["Component 12 Name"]

    @component_12_name.setter
    def component_12_name(self, value=None):
        """  Corresponds to IDD Field `component_12_name`

        Args:
            value (str): value for IDD Field `component_12_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_12_name`')

        self._data["Component 12 Name"] = value

    @property
    def component_13_object_type(self):
        """Get component_13_object_type

        Returns:
            str: the value of `component_13_object_type` or None if not set
        """
        return self._data["Component 13 Object Type"]

    @component_13_object_type.setter
    def component_13_object_type(self, value=None):
        """  Corresponds to IDD Field `component_13_object_type`

        Args:
            value (str): value for IDD Field `component_13_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_13_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_13_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_13_object_type`'.format(value))

        self._data["Component 13 Object Type"] = value

    @property
    def component_13_name(self):
        """Get component_13_name

        Returns:
            str: the value of `component_13_name` or None if not set
        """
        return self._data["Component 13 Name"]

    @component_13_name.setter
    def component_13_name(self, value=None):
        """  Corresponds to IDD Field `component_13_name`

        Args:
            value (str): value for IDD Field `component_13_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_13_name`')

        self._data["Component 13 Name"] = value

    @property
    def component_14_object_type(self):
        """Get component_14_object_type

        Returns:
            str: the value of `component_14_object_type` or None if not set
        """
        return self._data["Component 14 Object Type"]

    @component_14_object_type.setter
    def component_14_object_type(self, value=None):
        """  Corresponds to IDD Field `component_14_object_type`

        Args:
            value (str): value for IDD Field `component_14_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_14_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_14_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_14_object_type`'.format(value))

        self._data["Component 14 Object Type"] = value

    @property
    def component_14_name(self):
        """Get component_14_name

        Returns:
            str: the value of `component_14_name` or None if not set
        """
        return self._data["Component 14 Name"]

    @component_14_name.setter
    def component_14_name(self, value=None):
        """  Corresponds to IDD Field `component_14_name`

        Args:
            value (str): value for IDD Field `component_14_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_14_name`')

        self._data["Component 14 Name"] = value

    @property
    def component_15_object_type(self):
        """Get component_15_object_type

        Returns:
            str: the value of `component_15_object_type` or None if not set
        """
        return self._data["Component 15 Object Type"]

    @component_15_object_type.setter
    def component_15_object_type(self, value=None):
        """  Corresponds to IDD Field `component_15_object_type`

        Args:
            value (str): value for IDD Field `component_15_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_15_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_15_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_15_object_type`'.format(value))

        self._data["Component 15 Object Type"] = value

    @property
    def component_15_name(self):
        """Get component_15_name

        Returns:
            str: the value of `component_15_name` or None if not set
        """
        return self._data["Component 15 Name"]

    @component_15_name.setter
    def component_15_name(self, value=None):
        """  Corresponds to IDD Field `component_15_name`

        Args:
            value (str): value for IDD Field `component_15_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_15_name`')

        self._data["Component 15 Name"] = value

    @property
    def component_16_object_type(self):
        """Get component_16_object_type

        Returns:
            str: the value of `component_16_object_type` or None if not set
        """
        return self._data["Component 16 Object Type"]

    @component_16_object_type.setter
    def component_16_object_type(self, value=None):
        """  Corresponds to IDD Field `component_16_object_type`

        Args:
            value (str): value for IDD Field `component_16_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_16_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_16_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_16_object_type`'.format(value))

        self._data["Component 16 Object Type"] = value

    @property
    def component_16_name(self):
        """Get component_16_name

        Returns:
            str: the value of `component_16_name` or None if not set
        """
        return self._data["Component 16 Name"]

    @component_16_name.setter
    def component_16_name(self, value=None):
        """  Corresponds to IDD Field `component_16_name`

        Args:
            value (str): value for IDD Field `component_16_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_16_name`')

        self._data["Component 16 Name"] = value

    @property
    def component_17_object_type(self):
        """Get component_17_object_type

        Returns:
            str: the value of `component_17_object_type` or None if not set
        """
        return self._data["Component 17 Object Type"]

    @component_17_object_type.setter
    def component_17_object_type(self, value=None):
        """  Corresponds to IDD Field `component_17_object_type`

        Args:
            value (str): value for IDD Field `component_17_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_17_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_17_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_17_object_type`'.format(value))

        self._data["Component 17 Object Type"] = value

    @property
    def component_17_name(self):
        """Get component_17_name

        Returns:
            str: the value of `component_17_name` or None if not set
        """
        return self._data["Component 17 Name"]

    @component_17_name.setter
    def component_17_name(self, value=None):
        """  Corresponds to IDD Field `component_17_name`

        Args:
            value (str): value for IDD Field `component_17_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_17_name`')

        self._data["Component 17 Name"] = value

    @property
    def component_18_object_type(self):
        """Get component_18_object_type

        Returns:
            str: the value of `component_18_object_type` or None if not set
        """
        return self._data["Component 18 Object Type"]

    @component_18_object_type.setter
    def component_18_object_type(self, value=None):
        """  Corresponds to IDD Field `component_18_object_type`

        Args:
            value (str): value for IDD Field `component_18_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_18_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_18_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_18_object_type`'.format(value))

        self._data["Component 18 Object Type"] = value

    @property
    def component_18_name(self):
        """Get component_18_name

        Returns:
            str: the value of `component_18_name` or None if not set
        """
        return self._data["Component 18 Name"]

    @component_18_name.setter
    def component_18_name(self, value=None):
        """  Corresponds to IDD Field `component_18_name`

        Args:
            value (str): value for IDD Field `component_18_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_18_name`')

        self._data["Component 18 Name"] = value

    @property
    def component_19_object_type(self):
        """Get component_19_object_type

        Returns:
            str: the value of `component_19_object_type` or None if not set
        """
        return self._data["Component 19 Object Type"]

    @component_19_object_type.setter
    def component_19_object_type(self, value=None):
        """  Corresponds to IDD Field `component_19_object_type`

        Args:
            value (str): value for IDD Field `component_19_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_19_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_19_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_19_object_type`'.format(value))

        self._data["Component 19 Object Type"] = value

    @property
    def component_19_name(self):
        """Get component_19_name

        Returns:
            str: the value of `component_19_name` or None if not set
        """
        return self._data["Component 19 Name"]

    @component_19_name.setter
    def component_19_name(self, value=None):
        """  Corresponds to IDD Field `component_19_name`

        Args:
            value (str): value for IDD Field `component_19_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_19_name`')

        self._data["Component 19 Name"] = value

    @property
    def component_20_object_type(self):
        """Get component_20_object_type

        Returns:
            str: the value of `component_20_object_type` or None if not set
        """
        return self._data["Component 20 Object Type"]

    @component_20_object_type.setter
    def component_20_object_type(self, value=None):
        """  Corresponds to IDD Field `component_20_object_type`

        Args:
            value (str): value for IDD Field `component_20_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_20_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_20_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_20_object_type`'.format(value))

        self._data["Component 20 Object Type"] = value

    @property
    def component_20_name(self):
        """Get component_20_name

        Returns:
            str: the value of `component_20_name` or None if not set
        """
        return self._data["Component 20 Name"]

    @component_20_name.setter
    def component_20_name(self, value=None):
        """  Corresponds to IDD Field `component_20_name`

        Args:
            value (str): value for IDD Field `component_20_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_20_name`')

        self._data["Component 20 Name"] = value

    @property
    def component_21_object_type(self):
        """Get component_21_object_type

        Returns:
            str: the value of `component_21_object_type` or None if not set
        """
        return self._data["Component 21 Object Type"]

    @component_21_object_type.setter
    def component_21_object_type(self, value=None):
        """  Corresponds to IDD Field `component_21_object_type`

        Args:
            value (str): value for IDD Field `component_21_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_21_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_21_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_21_object_type`'.format(value))

        self._data["Component 21 Object Type"] = value

    @property
    def component_21_name(self):
        """Get component_21_name

        Returns:
            str: the value of `component_21_name` or None if not set
        """
        return self._data["Component 21 Name"]

    @component_21_name.setter
    def component_21_name(self, value=None):
        """  Corresponds to IDD Field `component_21_name`

        Args:
            value (str): value for IDD Field `component_21_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_21_name`')

        self._data["Component 21 Name"] = value

    @property
    def component_22_object_type(self):
        """Get component_22_object_type

        Returns:
            str: the value of `component_22_object_type` or None if not set
        """
        return self._data["Component 22 Object Type"]

    @component_22_object_type.setter
    def component_22_object_type(self, value=None):
        """  Corresponds to IDD Field `component_22_object_type`

        Args:
            value (str): value for IDD Field `component_22_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_22_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_22_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_22_object_type`'.format(value))

        self._data["Component 22 Object Type"] = value

    @property
    def component_22_name(self):
        """Get component_22_name

        Returns:
            str: the value of `component_22_name` or None if not set
        """
        return self._data["Component 22 Name"]

    @component_22_name.setter
    def component_22_name(self, value=None):
        """  Corresponds to IDD Field `component_22_name`

        Args:
            value (str): value for IDD Field `component_22_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_22_name`')

        self._data["Component 22 Name"] = value

    @property
    def component_23_object_type(self):
        """Get component_23_object_type

        Returns:
            str: the value of `component_23_object_type` or None if not set
        """
        return self._data["Component 23 Object Type"]

    @component_23_object_type.setter
    def component_23_object_type(self, value=None):
        """  Corresponds to IDD Field `component_23_object_type`

        Args:
            value (str): value for IDD Field `component_23_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_23_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_23_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_23_object_type`'.format(value))

        self._data["Component 23 Object Type"] = value

    @property
    def component_23_name(self):
        """Get component_23_name

        Returns:
            str: the value of `component_23_name` or None if not set
        """
        return self._data["Component 23 Name"]

    @component_23_name.setter
    def component_23_name(self, value=None):
        """  Corresponds to IDD Field `component_23_name`

        Args:
            value (str): value for IDD Field `component_23_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_23_name`')

        self._data["Component 23 Name"] = value

    @property
    def component_24_object_type(self):
        """Get component_24_object_type

        Returns:
            str: the value of `component_24_object_type` or None if not set
        """
        return self._data["Component 24 Object Type"]

    @component_24_object_type.setter
    def component_24_object_type(self, value=None):
        """  Corresponds to IDD Field `component_24_object_type`

        Args:
            value (str): value for IDD Field `component_24_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_24_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_24_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_24_object_type`'.format(value))

        self._data["Component 24 Object Type"] = value

    @property
    def component_24_name(self):
        """Get component_24_name

        Returns:
            str: the value of `component_24_name` or None if not set
        """
        return self._data["Component 24 Name"]

    @component_24_name.setter
    def component_24_name(self, value=None):
        """  Corresponds to IDD Field `component_24_name`

        Args:
            value (str): value for IDD Field `component_24_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_24_name`')

        self._data["Component 24 Name"] = value

    @property
    def component_25_object_type(self):
        """Get component_25_object_type

        Returns:
            str: the value of `component_25_object_type` or None if not set
        """
        return self._data["Component 25 Object Type"]

    @component_25_object_type.setter
    def component_25_object_type(self, value=None):
        """  Corresponds to IDD Field `component_25_object_type`

        Args:
            value (str): value for IDD Field `component_25_object_type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_25_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_25_object_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ReturnPlenum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_25_object_type`'.format(value))

        self._data["Component 25 Object Type"] = value

    @property
    def component_25_name(self):
        """Get component_25_name

        Returns:
            str: the value of `component_25_name` or None if not set
        """
        return self._data["Component 25 Name"]

    @component_25_name.setter
    def component_25_name(self, value=None):
        """  Corresponds to IDD Field `component_25_name`

        Args:
            value (str): value for IDD Field `component_25_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_25_name`')

        self._data["Component 25 Name"] = value

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
        out.append(self._to_str(self.return_air_path_outlet_node_name))
        out.append(self._to_str(self.component_1_object_type))
        out.append(self._to_str(self.component_1_name))
        out.append(self._to_str(self.component_2_object_type))
        out.append(self._to_str(self.component_2_name))
        out.append(self._to_str(self.component_3_object_type))
        out.append(self._to_str(self.component_3_name))
        out.append(self._to_str(self.component_4_object_type))
        out.append(self._to_str(self.component_4_name))
        out.append(self._to_str(self.component_5_object_type))
        out.append(self._to_str(self.component_5_name))
        out.append(self._to_str(self.component_6_object_type))
        out.append(self._to_str(self.component_6_name))
        out.append(self._to_str(self.component_7_object_type))
        out.append(self._to_str(self.component_7_name))
        out.append(self._to_str(self.component_8_object_type))
        out.append(self._to_str(self.component_8_name))
        out.append(self._to_str(self.component_9_object_type))
        out.append(self._to_str(self.component_9_name))
        out.append(self._to_str(self.component_10_object_type))
        out.append(self._to_str(self.component_10_name))
        out.append(self._to_str(self.component_11_object_type))
        out.append(self._to_str(self.component_11_name))
        out.append(self._to_str(self.component_12_object_type))
        out.append(self._to_str(self.component_12_name))
        out.append(self._to_str(self.component_13_object_type))
        out.append(self._to_str(self.component_13_name))
        out.append(self._to_str(self.component_14_object_type))
        out.append(self._to_str(self.component_14_name))
        out.append(self._to_str(self.component_15_object_type))
        out.append(self._to_str(self.component_15_name))
        out.append(self._to_str(self.component_16_object_type))
        out.append(self._to_str(self.component_16_name))
        out.append(self._to_str(self.component_17_object_type))
        out.append(self._to_str(self.component_17_name))
        out.append(self._to_str(self.component_18_object_type))
        out.append(self._to_str(self.component_18_name))
        out.append(self._to_str(self.component_19_object_type))
        out.append(self._to_str(self.component_19_name))
        out.append(self._to_str(self.component_20_object_type))
        out.append(self._to_str(self.component_20_name))
        out.append(self._to_str(self.component_21_object_type))
        out.append(self._to_str(self.component_21_name))
        out.append(self._to_str(self.component_22_object_type))
        out.append(self._to_str(self.component_22_name))
        out.append(self._to_str(self.component_23_object_type))
        out.append(self._to_str(self.component_23_name))
        out.append(self._to_str(self.component_24_object_type))
        out.append(self._to_str(self.component_24_name))
        out.append(self._to_str(self.component_25_object_type))
        out.append(self._to_str(self.component_25_name))
        return ",".join(out)