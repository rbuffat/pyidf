from collections import OrderedDict

class AirLoopHvac(object):
    """ Corresponds to IDD object `AirLoopHVAC`
        Defines a central forced air system.
    
    """
    internal_name = "AirLoopHVAC"
    field_count = 10
    required_fields = ["Name", "Branch List Name", "Supply Side Inlet Node Name", "Demand Side Outlet Node Name", "Demand Side Inlet Node Names", "Supply Side Outlet Node Names"]

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
            self.controller_list_name = None
        else:
            self.controller_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate = None
        else:
            self.design_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.branch_list_name = None
        else:
            self.branch_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.connector_list_name = None
        else:
            self.connector_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_side_inlet_node_name = None
        else:
            self.supply_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_side_outlet_node_name = None
        else:
            self.demand_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_side_inlet_node_names = None
        else:
            self.demand_side_inlet_node_names = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_side_outlet_node_names = None
        else:
            self.supply_side_outlet_node_names = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'alpha', u'reference': u'AirPrimaryLoops', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def controller_list_name(self):
        """Get controller_list_name

        Returns:
            str: the value of `controller_list_name` or None if not set
        """
        return self._data["Controller List Name"]

    @controller_list_name.setter
    def controller_list_name(self, value=None):
        """  Corresponds to IDD Field `Controller List Name`
        Enter the name of an AirLoopHVAC:ControllerList object.
        
        {u'note': [u'Enter the name of an AirLoopHVAC:ControllerList object.'], u'type': u'object-list', u'object-list': u'ControllerLists', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Controller List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.
        
        {u'note': [u'Enter the name of an AvailabilityManagerAssignmentList object.'], u'type': u'object-list', u'object-list': u'SystemAvailabilityManagerLists', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Design Supply Air Flow Rate`
        
        {u'default': '0.0', u'units': u'm3/s', u'autosizable': u'', 'type': 'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Design Supply Air Flow Rate`
                Units: m3/s
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Branch List Name`
        Name of a BranchList containing all the branches in this air loop
        
        {u'note': [u'Name of a BranchList containing all the branches in this air loop'], u'type': u'object-list', u'object-list': u'BranchLists', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Branch List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Connector List Name`
        Name of a ConnectorList containing all the splitters and mixers in the loop
        
        {u'note': [u'Name of a ConnectorList containing all the splitters and mixers in the loop'], u'type': u'object-list', u'object-list': u'ConnectorLists', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Connector List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `connector_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `connector_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Supply Side Inlet Node Name`
        Name of inlet node where return air enters the supply side of the air loop
        
        {u'note': [u'Name of inlet node where return air enters the supply side of the air loop'], u'type': u'node', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Supply Side Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Demand Side Outlet Node Name`
        Name of outlet node where return air leaves the demand side and enters the supply side.
        
        {u'note': [u'Name of outlet node where return air leaves the demand side and enters the supply side.'], u'type': u'node', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Demand Side Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Demand Side Inlet Node Names`
        Name of a Node or NodeList containing the inlet node(s) supplying air to zone equipment.
        
        {u'note': [u'Name of a Node or NodeList containing the inlet node(s) supplying air to zone equipment.'], u'type': u'node', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Demand Side Inlet Node Names`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_side_inlet_node_names`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_side_inlet_node_names`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Supply Side Outlet Node Names`
        Name of a Node or NodeList containing the outlet node(s) supplying air to the demand side.
        
        {u'note': [u'Name of a Node or NodeList containing the outlet node(s) supplying air to the demand side.'], u'type': u'node', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Supply Side Outlet Node Names`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_side_outlet_node_names`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_side_outlet_node_names`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_side_outlet_node_names`')
        self._data["Supply Side Outlet Node Names"] = value

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

class AirLoopHvacOutdoorAirSystemEquipmentList(object):
    """ Corresponds to IDD object `AirLoopHVAC:OutdoorAirSystem:EquipmentList`
        List equipment in simulation order
    
    """
    internal_name = "AirLoopHVAC:OutdoorAirSystem:EquipmentList"
    field_count = 19
    required_fields = ["Name", "Component 1 Object Type", "Component 1 Name"]

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
            self.component_1_object_type = None
        else:
            self.component_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_1_name = None
        else:
            self.component_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_object_type = None
        else:
            self.component_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_name = None
        else:
            self.component_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_object_type = None
        else:
            self.component_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_name = None
        else:
            self.component_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_object_type = None
        else:
            self.component_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_name = None
        else:
            self.component_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_object_type = None
        else:
            self.component_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_name = None
        else:
            self.component_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_object_type = None
        else:
            self.component_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_name = None
        else:
            self.component_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_object_type = None
        else:
            self.component_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_name = None
        else:
            self.component_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_object_type = None
        else:
            self.component_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_name = None
        else:
            self.component_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_object_type = None
        else:
            self.component_9_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_name = None
        else:
            self.component_9_name = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'alpha', u'reference': u'AirLoopOAEquipmentLists', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def component_1_object_type(self):
        """Get component_1_object_type

        Returns:
            str: the value of `component_1_object_type` or None if not set
        """
        return self._data["Component 1 Object Type"]

    @component_1_object_type.setter
    def component_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 1 Object Type`
        
        {'type': 'alpha', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 1 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 1 Name`
        
        {'type': 'alpha', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 2 Object Type`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 2 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 2 Name`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 3 Object Type`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 3 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 3 Name`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 4 Object Type`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 4 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 4 Name`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 5 Object Type`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 5 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 5 Name`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 6 Object Type`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 6 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 6 Name`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 7 Object Type`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 7 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 7 Name`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 8 Object Type`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 8 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 8 Name`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 9 Object Type`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 9 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 9 Name`
        
        {'type': 'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 9 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_9_name`')
        self._data["Component 9 Name"] = value

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

class AirLoopHvacOutdoorAirSystem(object):
    """ Corresponds to IDD object `AirLoopHVAC:OutdoorAirSystem`
        Outdoor air subsystem for an AirLoopHVAC. Includes an outdoor air mixing box and
        optional outdoor air conditioning equipment such as heat recovery, preheat, and precool
        coils. From the perspective of the primary air loop the outdoor air system is treated
        as a single component.
    
    """
    internal_name = "AirLoopHVAC:OutdoorAirSystem"
    field_count = 4
    required_fields = ["Name", "Controller List Name", "Outdoor Air Equipment List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:OutdoorAirSystem`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Controller List Name"] = None
        self._data["Outdoor Air Equipment List Name"] = None
        self._data["Availability Manager List Name"] = None
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
            self.controller_list_name = None
        else:
            self.controller_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_equipment_list_name = None
        else:
            self.outdoor_air_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'alpha', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def controller_list_name(self):
        """Get controller_list_name

        Returns:
            str: the value of `controller_list_name` or None if not set
        """
        return self._data["Controller List Name"]

    @controller_list_name.setter
    def controller_list_name(self, value=None):
        """  Corresponds to IDD Field `Controller List Name`
        Enter the name of an AirLoopHVAC:ControllerList object.
        
        {u'note': [u'Enter the name of an AirLoopHVAC:ControllerList object.'], u'type': u'object-list', u'object-list': u'ControllerLists', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Controller List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `controller_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controller_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Outdoor Air Equipment List Name`
        Enter the name of an AirLoopHVAC:OutdoorAirSystem:EquipmentList object.
        
        {u'note': [u'Enter the name of an AirLoopHVAC:OutdoorAirSystem:EquipmentList object.'], u'type': u'object-list', u'object-list': u'AirLoopOAEquipmentLists', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Outdoor Air Equipment List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.
        
        {u'note': [u'Enter the name of an AvailabilityManagerAssignmentList object.'], u'type': u'object-list', u'object-list': u'SystemAvailabilityManagerLists', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

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

class OutdoorAirMixer(object):
    """ Corresponds to IDD object `OutdoorAir:Mixer`
        Outdoor air mixer. Node names cannot be duplicated within a single OutdoorAir:Mixer
        object or across all outdoor air mixers.
    
    """
    internal_name = "OutdoorAir:Mixer"
    field_count = 5
    required_fields = ["Name", "Mixed Air Node Name", "Outdoor Air Stream Node Name", "Relief Air Stream Node Name", "Return Air Stream Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `OutdoorAir:Mixer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Mixed Air Node Name"] = None
        self._data["Outdoor Air Stream Node Name"] = None
        self._data["Relief Air Stream Node Name"] = None
        self._data["Return Air Stream Node Name"] = None
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
            self.mixed_air_node_name = None
        else:
            self.mixed_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_stream_node_name = None
        else:
            self.outdoor_air_stream_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relief_air_stream_node_name = None
        else:
            self.relief_air_stream_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.return_air_stream_node_name = None
        else:
            self.return_air_stream_node_name = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'alpha', u'reference': u'OutdoorAirMixers', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def mixed_air_node_name(self):
        """Get mixed_air_node_name

        Returns:
            str: the value of `mixed_air_node_name` or None if not set
        """
        return self._data["Mixed Air Node Name"]

    @mixed_air_node_name.setter
    def mixed_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Air Node Name`
        Name of Mixed Air Node
        
        {u'note': [u'Name of Mixed Air Node'], u'type': u'node', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Mixed Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def outdoor_air_stream_node_name(self):
        """Get outdoor_air_stream_node_name

        Returns:
            str: the value of `outdoor_air_stream_node_name` or None if not set
        """
        return self._data["Outdoor Air Stream Node Name"]

    @outdoor_air_stream_node_name.setter
    def outdoor_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Stream Node Name`
        Name of Outdoor Air Stream Node
        
        {u'note': [u'Name of Outdoor Air Stream Node'], u'type': u'node', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Outdoor Air Stream Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_stream_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Relief Air Stream Node Name`
        Name of Relief Air Stream Node
        
        {u'note': [u'Name of Relief Air Stream Node'], u'type': u'node', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Relief Air Stream Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `relief_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `relief_air_stream_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Return Air Stream Node Name`
        Name of Return Air Stream Node
        
        {u'note': [u'Name of Return Air Stream Node'], u'type': u'node', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Return Air Stream Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `return_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `return_air_stream_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `return_air_stream_node_name`')
        self._data["Return Air Stream Node Name"] = value

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

class AirLoopHvacSupplyPath(object):
    """ Corresponds to IDD object `AirLoopHVAC:SupplyPath`
        A supply path can only contain AirLoopHVAC:ZoneSplitter and AirLoopHVAC:SupplyPlenum objects
        which may be in series or parallel.
    
    """
    internal_name = "AirLoopHVAC:SupplyPath"
    field_count = 52
    required_fields = ["Name", "Supply Air Path Inlet Node Name", "Component 1 Object Type", "Component 1 Name"]

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
            self.supply_air_path_inlet_node_name = None
        else:
            self.supply_air_path_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_1_object_type = None
        else:
            self.component_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_1_name = None
        else:
            self.component_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_object_type = None
        else:
            self.component_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_name = None
        else:
            self.component_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_object_type = None
        else:
            self.component_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_name = None
        else:
            self.component_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_object_type = None
        else:
            self.component_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_name = None
        else:
            self.component_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_object_type = None
        else:
            self.component_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_name = None
        else:
            self.component_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_object_type = None
        else:
            self.component_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_name = None
        else:
            self.component_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_object_type = None
        else:
            self.component_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_name = None
        else:
            self.component_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_object_type = None
        else:
            self.component_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_name = None
        else:
            self.component_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_object_type = None
        else:
            self.component_9_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_name = None
        else:
            self.component_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_10_object_type = None
        else:
            self.component_10_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_10_name = None
        else:
            self.component_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_11_object_type = None
        else:
            self.component_11_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_11_name = None
        else:
            self.component_11_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_12_object_type = None
        else:
            self.component_12_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_12_name = None
        else:
            self.component_12_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_13_object_type = None
        else:
            self.component_13_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_13_name = None
        else:
            self.component_13_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_14_object_type = None
        else:
            self.component_14_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_14_name = None
        else:
            self.component_14_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_15_object_type = None
        else:
            self.component_15_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_15_name = None
        else:
            self.component_15_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_16_object_type = None
        else:
            self.component_16_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_16_name = None
        else:
            self.component_16_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_17_object_type = None
        else:
            self.component_17_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_17_name = None
        else:
            self.component_17_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_18_object_type = None
        else:
            self.component_18_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_18_name = None
        else:
            self.component_18_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_19_object_type = None
        else:
            self.component_19_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_19_name = None
        else:
            self.component_19_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_20_object_type = None
        else:
            self.component_20_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_20_name = None
        else:
            self.component_20_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_21_object_type = None
        else:
            self.component_21_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_21_name = None
        else:
            self.component_21_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_22_object_type = None
        else:
            self.component_22_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_22_name = None
        else:
            self.component_22_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_23_object_type = None
        else:
            self.component_23_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_23_name = None
        else:
            self.component_23_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_24_object_type = None
        else:
            self.component_24_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_24_name = None
        else:
            self.component_24_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_25_object_type = None
        else:
            self.component_25_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_25_name = None
        else:
            self.component_25_name = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {'type': 'alpha', u'reference': u'ZoneSupplyAirPaths', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def supply_air_path_inlet_node_name(self):
        """Get supply_air_path_inlet_node_name

        Returns:
            str: the value of `supply_air_path_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Path Inlet Node Name"]

    @supply_air_path_inlet_node_name.setter
    def supply_air_path_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Path Inlet Node Name`
        
        {u'type': u'node', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Supply Air Path Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_path_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_path_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 1 Object Type`
        Supply path components must be listed in flow order.
        
        {'pytype': 'str', u'begin-extensible': u'', u'required-field': True, u'note': [u'Supply path components must be listed in flow order.'], u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], u'type': u'choice'}

        Args:
            value (str): value for IDD Field `Component 1 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_1_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_1_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 1 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 2 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 2 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_2_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_2_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 2 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 3 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 3 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_3_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_3_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 3 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 4 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 4 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_4_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_4_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 4 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 5 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 5 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_5_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_5_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 5 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 6 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 6 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_6_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_6_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 6 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 7 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 7 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_7_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_7_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 7 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 8 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 8 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_8_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_8_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 8 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 9 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 9 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_9_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_9_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 9 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 9 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 10 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 10 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_10_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_10_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 10 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 10 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 11 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 11 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_11_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_11_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 11 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 11 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 12 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 12 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_12_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_12_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_12_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_12_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 12 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 12 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_12_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 13 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 13 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_13_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_13_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_13_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_13_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 13 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 13 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_13_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 14 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 14 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_14_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_14_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_14_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_14_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 14 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 14 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_14_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 15 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 15 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_15_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_15_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_15_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_15_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 15 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 15 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_15_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 16 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 16 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_16_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_16_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_16_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_16_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 16 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 16 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_16_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 17 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 17 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_17_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_17_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_17_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_17_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 17 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 17 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_17_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 18 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 18 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_18_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_18_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_18_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_18_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 18 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 18 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_18_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 19 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 19 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_19_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_19_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_19_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_19_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 19 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 19 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_19_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 20 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 20 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_20_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_20_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_20_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_20_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 20 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 20 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_20_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 21 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 21 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_21_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_21_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_21_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_21_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 21 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 21 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_21_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 22 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 22 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_22_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_22_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_22_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_22_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 22 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 22 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_22_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 23 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 23 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_23_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_23_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_23_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_23_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 23 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 23 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_23_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 24 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 24 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_24_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_24_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_24_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_24_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 24 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 24 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_24_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 25 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:SupplyPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 25 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_25_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_25_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_25_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `component_25_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 25 Name`
        
        {u'type': u'object-list', u'object-list': u'SupplyPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 25 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_25_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_25_name`')
        self._data["Component 25 Name"] = value

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

class AirLoopHvacReturnPath(object):
    """ Corresponds to IDD object `AirLoopHVAC:ReturnPath`
        A return air path can only contain one AirLoopHVAC:ZoneMixer
        and one or more AirLoopHVAC:ReturnPlenum objects.
    
    """
    internal_name = "AirLoopHVAC:ReturnPath"
    field_count = 52
    required_fields = ["Name", "Return Air Path Outlet Node Name", "Component 1 Object Type", "Component 1 Name"]

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
            self.return_air_path_outlet_node_name = None
        else:
            self.return_air_path_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_1_object_type = None
        else:
            self.component_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_1_name = None
        else:
            self.component_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_object_type = None
        else:
            self.component_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_name = None
        else:
            self.component_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_object_type = None
        else:
            self.component_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_name = None
        else:
            self.component_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_object_type = None
        else:
            self.component_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_name = None
        else:
            self.component_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_object_type = None
        else:
            self.component_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_name = None
        else:
            self.component_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_object_type = None
        else:
            self.component_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_name = None
        else:
            self.component_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_object_type = None
        else:
            self.component_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_name = None
        else:
            self.component_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_object_type = None
        else:
            self.component_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_name = None
        else:
            self.component_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_object_type = None
        else:
            self.component_9_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_name = None
        else:
            self.component_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_10_object_type = None
        else:
            self.component_10_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_10_name = None
        else:
            self.component_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_11_object_type = None
        else:
            self.component_11_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_11_name = None
        else:
            self.component_11_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_12_object_type = None
        else:
            self.component_12_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_12_name = None
        else:
            self.component_12_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_13_object_type = None
        else:
            self.component_13_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_13_name = None
        else:
            self.component_13_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_14_object_type = None
        else:
            self.component_14_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_14_name = None
        else:
            self.component_14_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_15_object_type = None
        else:
            self.component_15_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_15_name = None
        else:
            self.component_15_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_16_object_type = None
        else:
            self.component_16_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_16_name = None
        else:
            self.component_16_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_17_object_type = None
        else:
            self.component_17_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_17_name = None
        else:
            self.component_17_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_18_object_type = None
        else:
            self.component_18_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_18_name = None
        else:
            self.component_18_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_19_object_type = None
        else:
            self.component_19_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_19_name = None
        else:
            self.component_19_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_20_object_type = None
        else:
            self.component_20_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_20_name = None
        else:
            self.component_20_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_21_object_type = None
        else:
            self.component_21_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_21_name = None
        else:
            self.component_21_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_22_object_type = None
        else:
            self.component_22_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_22_name = None
        else:
            self.component_22_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_23_object_type = None
        else:
            self.component_23_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_23_name = None
        else:
            self.component_23_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_24_object_type = None
        else:
            self.component_24_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_24_name = None
        else:
            self.component_24_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_25_object_type = None
        else:
            self.component_25_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_25_name = None
        else:
            self.component_25_name = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {'type': 'alpha', u'reference': u'ZoneReturnAirPaths', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def return_air_path_outlet_node_name(self):
        """Get return_air_path_outlet_node_name

        Returns:
            str: the value of `return_air_path_outlet_node_name` or None if not set
        """
        return self._data["Return Air Path Outlet Node Name"]

    @return_air_path_outlet_node_name.setter
    def return_air_path_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Return Air Path Outlet Node Name`
        
        {u'type': u'node', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Return Air Path Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `return_air_path_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `return_air_path_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 1 Object Type`
        
        {'pytype': 'str', u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], u'required-field': True, u'begin-extensible': u''}

        Args:
            value (str): value for IDD Field `Component 1 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_1_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_1_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 1 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 2 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 2 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_2_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_2_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 2 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 3 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 3 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_3_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_3_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 3 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 4 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 4 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_4_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_4_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 4 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 5 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 5 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_5_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_5_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 5 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 6 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 6 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_6_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_6_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 6 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 7 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 7 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_7_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_7_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 7 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 8 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 8 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_8_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_8_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 8 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 9 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 9 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_9_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_9_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 9 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 9 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 10 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 10 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_10_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_10_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 10 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 10 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 11 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 11 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_11_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_11_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 11 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 11 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 12 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 12 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_12_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_12_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_12_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_12_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 12 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 12 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_12_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 13 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 13 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_13_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_13_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_13_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_13_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 13 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 13 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_13_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 14 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 14 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_14_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_14_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_14_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_14_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 14 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 14 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_14_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 15 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 15 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_15_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_15_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_15_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_15_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 15 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 15 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_15_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 16 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 16 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_16_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_16_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_16_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_16_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 16 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 16 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_16_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 17 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 17 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_17_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_17_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_17_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_17_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 17 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 17 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_17_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 18 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 18 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_18_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_18_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_18_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_18_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 18 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 18 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_18_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 19 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 19 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_19_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_19_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_19_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_19_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 19 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 19 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_19_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 20 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 20 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_20_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_20_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_20_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_20_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 20 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 20 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_20_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 21 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 21 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_21_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_21_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_21_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_21_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 21 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 21 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_21_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 22 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 22 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_22_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_22_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_22_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_22_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 22 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 22 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_22_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 23 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 23 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_23_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_23_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_23_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_23_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 23 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 23 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_23_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 24 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 24 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_24_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_24_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_24_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_24_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 24 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 24 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_24_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Component 25 Object Type`
        
        {u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ReturnPlenum'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 25 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_25_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_25_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_25_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `component_25_object_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Component 25 Name`
        
        {u'type': u'object-list', u'object-list': u'ReturnPathComponentNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component 25 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_25_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_25_name`')
        self._data["Component 25 Name"] = value

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