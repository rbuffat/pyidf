from collections import OrderedDict

class Branch(object):
    """ Corresponds to IDD object `Branch`
        List components on the branch in simulation and connection order
        Note: this should NOT include splitters or mixers which define
        endpoints of branches
    
    """
    internal_name = "Branch"
    field_count = 58
    required_fields = ["Name", "Component 1 Object Type", "Component 1 Name", "Component 1 Inlet Node Name", "Component 1 Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Branch`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Pressure Drop Curve Name"] = None
        self._data["Component 1 Object Type"] = None
        self._data["Component 1 Name"] = None
        self._data["Component 1 Inlet Node Name"] = None
        self._data["Component 1 Outlet Node Name"] = None
        self._data["Component 1 Branch Control Type"] = None
        self._data["Component 2 Object Type"] = None
        self._data["Component 2 Name"] = None
        self._data["Component 2 Inlet Node Name"] = None
        self._data["Component 2 Outlet Node Name"] = None
        self._data["Component 2 Branch Control Type"] = None
        self._data["Component 3 Object Type"] = None
        self._data["Component 3 Name"] = None
        self._data["Component 3 Inlet Node Name"] = None
        self._data["Component 3 Outlet Node Name"] = None
        self._data["Component 3 Branch Control Type"] = None
        self._data["Component 4 Object Type"] = None
        self._data["Component 4 Name"] = None
        self._data["Component 4 Inlet Node Name"] = None
        self._data["Component 4 Outlet Node Name"] = None
        self._data["Component 4 Branch Control Type"] = None
        self._data["Component 5 Object Type"] = None
        self._data["Component 5 Name"] = None
        self._data["Component 5 Inlet Node Name"] = None
        self._data["Component 5 Outlet Node Name"] = None
        self._data["Component 5 Branch Control Type"] = None
        self._data["Component 6 Object Type"] = None
        self._data["Component 6 Name"] = None
        self._data["Component 6 Inlet Node Name"] = None
        self._data["Component 6 Outlet Node Name"] = None
        self._data["Component 6 Branch Control Type"] = None
        self._data["Component 7 Object Type"] = None
        self._data["Component 7 Name"] = None
        self._data["Component 7 Inlet Node Name"] = None
        self._data["Component 7 Outlet Node Name"] = None
        self._data["Component 7 Branch Control Type"] = None
        self._data["Component 8 Object Type"] = None
        self._data["Component 8 Name"] = None
        self._data["Component 8 Inlet Node Name"] = None
        self._data["Component 8 Outlet Node Name"] = None
        self._data["Component 8 Branch Control Type"] = None
        self._data["Component 9 Object Type"] = None
        self._data["Component 9 Name"] = None
        self._data["Component 9 Inlet Node Name"] = None
        self._data["Component 9 Outlet Node Name"] = None
        self._data["Component 9 Branch Control Type"] = None
        self._data["Component 10 Object Type"] = None
        self._data["Component 10 Name"] = None
        self._data["Component 10 Inlet Node Name"] = None
        self._data["Component 10 Outlet Node Name"] = None
        self._data["Component 10 Branch Control Type"] = None
        self._data["Component 11 Object Type"] = None
        self._data["Component 11 Name"] = None
        self._data["Component 11 Inlet Node Name"] = None
        self._data["Component 11 Outlet Node Name"] = None
        self._data["Component 11 Branch Control Type"] = None
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
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pressure_drop_curve_name = None
        else:
            self.pressure_drop_curve_name = vals[i]
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
            self.component_1_inlet_node_name = None
        else:
            self.component_1_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_1_outlet_node_name = None
        else:
            self.component_1_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_1_branch_control_type = None
        else:
            self.component_1_branch_control_type = vals[i]
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
            self.component_2_inlet_node_name = None
        else:
            self.component_2_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_outlet_node_name = None
        else:
            self.component_2_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_branch_control_type = None
        else:
            self.component_2_branch_control_type = vals[i]
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
            self.component_3_inlet_node_name = None
        else:
            self.component_3_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_outlet_node_name = None
        else:
            self.component_3_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_branch_control_type = None
        else:
            self.component_3_branch_control_type = vals[i]
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
            self.component_4_inlet_node_name = None
        else:
            self.component_4_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_outlet_node_name = None
        else:
            self.component_4_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_branch_control_type = None
        else:
            self.component_4_branch_control_type = vals[i]
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
            self.component_5_inlet_node_name = None
        else:
            self.component_5_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_outlet_node_name = None
        else:
            self.component_5_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_branch_control_type = None
        else:
            self.component_5_branch_control_type = vals[i]
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
            self.component_6_inlet_node_name = None
        else:
            self.component_6_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_outlet_node_name = None
        else:
            self.component_6_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_branch_control_type = None
        else:
            self.component_6_branch_control_type = vals[i]
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
            self.component_7_inlet_node_name = None
        else:
            self.component_7_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_outlet_node_name = None
        else:
            self.component_7_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_branch_control_type = None
        else:
            self.component_7_branch_control_type = vals[i]
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
            self.component_8_inlet_node_name = None
        else:
            self.component_8_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_outlet_node_name = None
        else:
            self.component_8_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_branch_control_type = None
        else:
            self.component_8_branch_control_type = vals[i]
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
            self.component_9_inlet_node_name = None
        else:
            self.component_9_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_outlet_node_name = None
        else:
            self.component_9_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_branch_control_type = None
        else:
            self.component_9_branch_control_type = vals[i]
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
            self.component_10_inlet_node_name = None
        else:
            self.component_10_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_10_outlet_node_name = None
        else:
            self.component_10_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_10_branch_control_type = None
        else:
            self.component_10_branch_control_type = vals[i]
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
            self.component_11_inlet_node_name = None
        else:
            self.component_11_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_11_outlet_node_name = None
        else:
            self.component_11_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_11_branch_control_type = None
        else:
            self.component_11_branch_control_type = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `maximum_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_flow_rate`')

        self._data["Maximum Flow Rate"] = value

    @property
    def pressure_drop_curve_name(self):
        """Get pressure_drop_curve_name

        Returns:
            str: the value of `pressure_drop_curve_name` or None if not set
        """
        return self._data["Pressure Drop Curve Name"]

    @pressure_drop_curve_name.setter
    def pressure_drop_curve_name(self, value=None):
        """  Corresponds to IDD Field `pressure_drop_curve_name`
        Optional field to include this branch in plant pressure drop calculations
        This field is only relevant for branches in PlantLoops and CondenserLoops
        Air loops do not account for pressure drop using this field
        Valid curve types are: Curve:Functional:PressureDrop or
        one of Curve:{Linear,Quadratic,Cubic,Exponent}')
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `pressure_drop_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pressure_drop_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pressure_drop_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pressure_drop_curve_name`')

        self._data["Pressure Drop Curve Name"] = value

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_1_name`')

        self._data["Component 1 Name"] = value

    @property
    def component_1_inlet_node_name(self):
        """Get component_1_inlet_node_name

        Returns:
            str: the value of `component_1_inlet_node_name` or None if not set
        """
        return self._data["Component 1 Inlet Node Name"]

    @component_1_inlet_node_name.setter
    def component_1_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_1_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_1_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_1_inlet_node_name`')

        self._data["Component 1 Inlet Node Name"] = value

    @property
    def component_1_outlet_node_name(self):
        """Get component_1_outlet_node_name

        Returns:
            str: the value of `component_1_outlet_node_name` or None if not set
        """
        return self._data["Component 1 Outlet Node Name"]

    @component_1_outlet_node_name.setter
    def component_1_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_1_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_1_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_1_outlet_node_name`')

        self._data["Component 1 Outlet Node Name"] = value

    @property
    def component_1_branch_control_type(self):
        """Get component_1_branch_control_type

        Returns:
            str: the value of `component_1_branch_control_type` or None if not set
        """
        return self._data["Component 1 Branch Control Type"]

    @component_1_branch_control_type.setter
    def component_1_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_1_branch_control_type`
        field is no longer used

        Args:
            value (str): value for IDD Field `component_1_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_1_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_1_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_1_branch_control_type`')

        self._data["Component 1 Branch Control Type"] = value

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_2_name`')

        self._data["Component 2 Name"] = value

    @property
    def component_2_inlet_node_name(self):
        """Get component_2_inlet_node_name

        Returns:
            str: the value of `component_2_inlet_node_name` or None if not set
        """
        return self._data["Component 2 Inlet Node Name"]

    @component_2_inlet_node_name.setter
    def component_2_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_2_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_2_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_2_inlet_node_name`')

        self._data["Component 2 Inlet Node Name"] = value

    @property
    def component_2_outlet_node_name(self):
        """Get component_2_outlet_node_name

        Returns:
            str: the value of `component_2_outlet_node_name` or None if not set
        """
        return self._data["Component 2 Outlet Node Name"]

    @component_2_outlet_node_name.setter
    def component_2_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_2_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_2_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_2_outlet_node_name`')

        self._data["Component 2 Outlet Node Name"] = value

    @property
    def component_2_branch_control_type(self):
        """Get component_2_branch_control_type

        Returns:
            str: the value of `component_2_branch_control_type` or None if not set
        """
        return self._data["Component 2 Branch Control Type"]

    @component_2_branch_control_type.setter
    def component_2_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_2_branch_control_type`
        field is no longer used

        Args:
            value (str): value for IDD Field `component_2_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_2_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_2_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_2_branch_control_type`')

        self._data["Component 2 Branch Control Type"] = value

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_3_name`')

        self._data["Component 3 Name"] = value

    @property
    def component_3_inlet_node_name(self):
        """Get component_3_inlet_node_name

        Returns:
            str: the value of `component_3_inlet_node_name` or None if not set
        """
        return self._data["Component 3 Inlet Node Name"]

    @component_3_inlet_node_name.setter
    def component_3_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_3_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_3_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_3_inlet_node_name`')

        self._data["Component 3 Inlet Node Name"] = value

    @property
    def component_3_outlet_node_name(self):
        """Get component_3_outlet_node_name

        Returns:
            str: the value of `component_3_outlet_node_name` or None if not set
        """
        return self._data["Component 3 Outlet Node Name"]

    @component_3_outlet_node_name.setter
    def component_3_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_3_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_3_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_3_outlet_node_name`')

        self._data["Component 3 Outlet Node Name"] = value

    @property
    def component_3_branch_control_type(self):
        """Get component_3_branch_control_type

        Returns:
            str: the value of `component_3_branch_control_type` or None if not set
        """
        return self._data["Component 3 Branch Control Type"]

    @component_3_branch_control_type.setter
    def component_3_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_3_branch_control_type`
        field is no longer useds

        Args:
            value (str): value for IDD Field `component_3_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_3_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_3_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_3_branch_control_type`')

        self._data["Component 3 Branch Control Type"] = value

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_4_name`')

        self._data["Component 4 Name"] = value

    @property
    def component_4_inlet_node_name(self):
        """Get component_4_inlet_node_name

        Returns:
            str: the value of `component_4_inlet_node_name` or None if not set
        """
        return self._data["Component 4 Inlet Node Name"]

    @component_4_inlet_node_name.setter
    def component_4_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_4_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_4_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_4_inlet_node_name`')

        self._data["Component 4 Inlet Node Name"] = value

    @property
    def component_4_outlet_node_name(self):
        """Get component_4_outlet_node_name

        Returns:
            str: the value of `component_4_outlet_node_name` or None if not set
        """
        return self._data["Component 4 Outlet Node Name"]

    @component_4_outlet_node_name.setter
    def component_4_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_4_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_4_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_4_outlet_node_name`')

        self._data["Component 4 Outlet Node Name"] = value

    @property
    def component_4_branch_control_type(self):
        """Get component_4_branch_control_type

        Returns:
            str: the value of `component_4_branch_control_type` or None if not set
        """
        return self._data["Component 4 Branch Control Type"]

    @component_4_branch_control_type.setter
    def component_4_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_4_branch_control_type`
        field is no longer used

        Args:
            value (str): value for IDD Field `component_4_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_4_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_4_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_4_branch_control_type`')

        self._data["Component 4 Branch Control Type"] = value

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_5_name`')

        self._data["Component 5 Name"] = value

    @property
    def component_5_inlet_node_name(self):
        """Get component_5_inlet_node_name

        Returns:
            str: the value of `component_5_inlet_node_name` or None if not set
        """
        return self._data["Component 5 Inlet Node Name"]

    @component_5_inlet_node_name.setter
    def component_5_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_5_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_5_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_5_inlet_node_name`')

        self._data["Component 5 Inlet Node Name"] = value

    @property
    def component_5_outlet_node_name(self):
        """Get component_5_outlet_node_name

        Returns:
            str: the value of `component_5_outlet_node_name` or None if not set
        """
        return self._data["Component 5 Outlet Node Name"]

    @component_5_outlet_node_name.setter
    def component_5_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_5_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_5_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_5_outlet_node_name`')

        self._data["Component 5 Outlet Node Name"] = value

    @property
    def component_5_branch_control_type(self):
        """Get component_5_branch_control_type

        Returns:
            str: the value of `component_5_branch_control_type` or None if not set
        """
        return self._data["Component 5 Branch Control Type"]

    @component_5_branch_control_type.setter
    def component_5_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_5_branch_control_type`
        field is no longer used

        Args:
            value (str): value for IDD Field `component_5_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_5_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_5_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_5_branch_control_type`')

        self._data["Component 5 Branch Control Type"] = value

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_6_name`')

        self._data["Component 6 Name"] = value

    @property
    def component_6_inlet_node_name(self):
        """Get component_6_inlet_node_name

        Returns:
            str: the value of `component_6_inlet_node_name` or None if not set
        """
        return self._data["Component 6 Inlet Node Name"]

    @component_6_inlet_node_name.setter
    def component_6_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_6_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_6_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_6_inlet_node_name`')

        self._data["Component 6 Inlet Node Name"] = value

    @property
    def component_6_outlet_node_name(self):
        """Get component_6_outlet_node_name

        Returns:
            str: the value of `component_6_outlet_node_name` or None if not set
        """
        return self._data["Component 6 Outlet Node Name"]

    @component_6_outlet_node_name.setter
    def component_6_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_6_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_6_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_6_outlet_node_name`')

        self._data["Component 6 Outlet Node Name"] = value

    @property
    def component_6_branch_control_type(self):
        """Get component_6_branch_control_type

        Returns:
            str: the value of `component_6_branch_control_type` or None if not set
        """
        return self._data["Component 6 Branch Control Type"]

    @component_6_branch_control_type.setter
    def component_6_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_6_branch_control_type`
        field is no longer used

        Args:
            value (str): value for IDD Field `component_6_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_6_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_6_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_6_branch_control_type`')

        self._data["Component 6 Branch Control Type"] = value

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_7_name`')

        self._data["Component 7 Name"] = value

    @property
    def component_7_inlet_node_name(self):
        """Get component_7_inlet_node_name

        Returns:
            str: the value of `component_7_inlet_node_name` or None if not set
        """
        return self._data["Component 7 Inlet Node Name"]

    @component_7_inlet_node_name.setter
    def component_7_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_7_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_7_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_7_inlet_node_name`')

        self._data["Component 7 Inlet Node Name"] = value

    @property
    def component_7_outlet_node_name(self):
        """Get component_7_outlet_node_name

        Returns:
            str: the value of `component_7_outlet_node_name` or None if not set
        """
        return self._data["Component 7 Outlet Node Name"]

    @component_7_outlet_node_name.setter
    def component_7_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_7_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_7_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_7_outlet_node_name`')

        self._data["Component 7 Outlet Node Name"] = value

    @property
    def component_7_branch_control_type(self):
        """Get component_7_branch_control_type

        Returns:
            str: the value of `component_7_branch_control_type` or None if not set
        """
        return self._data["Component 7 Branch Control Type"]

    @component_7_branch_control_type.setter
    def component_7_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_7_branch_control_type`
        field is no longer used

        Args:
            value (str): value for IDD Field `component_7_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_7_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_7_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_7_branch_control_type`')

        self._data["Component 7 Branch Control Type"] = value

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_8_name`')

        self._data["Component 8 Name"] = value

    @property
    def component_8_inlet_node_name(self):
        """Get component_8_inlet_node_name

        Returns:
            str: the value of `component_8_inlet_node_name` or None if not set
        """
        return self._data["Component 8 Inlet Node Name"]

    @component_8_inlet_node_name.setter
    def component_8_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_8_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_8_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_8_inlet_node_name`')

        self._data["Component 8 Inlet Node Name"] = value

    @property
    def component_8_outlet_node_name(self):
        """Get component_8_outlet_node_name

        Returns:
            str: the value of `component_8_outlet_node_name` or None if not set
        """
        return self._data["Component 8 Outlet Node Name"]

    @component_8_outlet_node_name.setter
    def component_8_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_8_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_8_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_8_outlet_node_name`')

        self._data["Component 8 Outlet Node Name"] = value

    @property
    def component_8_branch_control_type(self):
        """Get component_8_branch_control_type

        Returns:
            str: the value of `component_8_branch_control_type` or None if not set
        """
        return self._data["Component 8 Branch Control Type"]

    @component_8_branch_control_type.setter
    def component_8_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_8_branch_control_type`
        field is no longer used

        Args:
            value (str): value for IDD Field `component_8_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_8_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_8_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_8_branch_control_type`')

        self._data["Component 8 Branch Control Type"] = value

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_9_name`')

        self._data["Component 9 Name"] = value

    @property
    def component_9_inlet_node_name(self):
        """Get component_9_inlet_node_name

        Returns:
            str: the value of `component_9_inlet_node_name` or None if not set
        """
        return self._data["Component 9 Inlet Node Name"]

    @component_9_inlet_node_name.setter
    def component_9_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_9_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_9_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_9_inlet_node_name`')

        self._data["Component 9 Inlet Node Name"] = value

    @property
    def component_9_outlet_node_name(self):
        """Get component_9_outlet_node_name

        Returns:
            str: the value of `component_9_outlet_node_name` or None if not set
        """
        return self._data["Component 9 Outlet Node Name"]

    @component_9_outlet_node_name.setter
    def component_9_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_9_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_9_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_9_outlet_node_name`')

        self._data["Component 9 Outlet Node Name"] = value

    @property
    def component_9_branch_control_type(self):
        """Get component_9_branch_control_type

        Returns:
            str: the value of `component_9_branch_control_type` or None if not set
        """
        return self._data["Component 9 Branch Control Type"]

    @component_9_branch_control_type.setter
    def component_9_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_9_branch_control_type`
        field is no longer used

        Args:
            value (str): value for IDD Field `component_9_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_9_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_9_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_9_branch_control_type`')

        self._data["Component 9 Branch Control Type"] = value

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
                if `value` is None it will not be checked against the
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_10_object_type`')

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_10_name`')

        self._data["Component 10 Name"] = value

    @property
    def component_10_inlet_node_name(self):
        """Get component_10_inlet_node_name

        Returns:
            str: the value of `component_10_inlet_node_name` or None if not set
        """
        return self._data["Component 10 Inlet Node Name"]

    @component_10_inlet_node_name.setter
    def component_10_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_10_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_10_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_10_inlet_node_name`')

        self._data["Component 10 Inlet Node Name"] = value

    @property
    def component_10_outlet_node_name(self):
        """Get component_10_outlet_node_name

        Returns:
            str: the value of `component_10_outlet_node_name` or None if not set
        """
        return self._data["Component 10 Outlet Node Name"]

    @component_10_outlet_node_name.setter
    def component_10_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_10_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_10_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_10_outlet_node_name`')

        self._data["Component 10 Outlet Node Name"] = value

    @property
    def component_10_branch_control_type(self):
        """Get component_10_branch_control_type

        Returns:
            str: the value of `component_10_branch_control_type` or None if not set
        """
        return self._data["Component 10 Branch Control Type"]

    @component_10_branch_control_type.setter
    def component_10_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_10_branch_control_type`
        field is no longer used

        Args:
            value (str): value for IDD Field `component_10_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_10_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_10_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_10_branch_control_type`')

        self._data["Component 10 Branch Control Type"] = value

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
                if `value` is None it will not be checked against the
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_11_object_type`')

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_11_name`')

        self._data["Component 11 Name"] = value

    @property
    def component_11_inlet_node_name(self):
        """Get component_11_inlet_node_name

        Returns:
            str: the value of `component_11_inlet_node_name` or None if not set
        """
        return self._data["Component 11 Inlet Node Name"]

    @component_11_inlet_node_name.setter
    def component_11_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_11_inlet_node_name`

        Args:
            value (str): value for IDD Field `component_11_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_11_inlet_node_name`')

        self._data["Component 11 Inlet Node Name"] = value

    @property
    def component_11_outlet_node_name(self):
        """Get component_11_outlet_node_name

        Returns:
            str: the value of `component_11_outlet_node_name` or None if not set
        """
        return self._data["Component 11 Outlet Node Name"]

    @component_11_outlet_node_name.setter
    def component_11_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `component_11_outlet_node_name`

        Args:
            value (str): value for IDD Field `component_11_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_11_outlet_node_name`')

        self._data["Component 11 Outlet Node Name"] = value

    @property
    def component_11_branch_control_type(self):
        """Get component_11_branch_control_type

        Returns:
            str: the value of `component_11_branch_control_type` or None if not set
        """
        return self._data["Component 11 Branch Control Type"]

    @component_11_branch_control_type.setter
    def component_11_branch_control_type(self, value=None):
        """  Corresponds to IDD Field `component_11_branch_control_type`
        field is no longer used

        Args:
            value (str): value for IDD Field `component_11_branch_control_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_11_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_11_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_11_branch_control_type`')

        self._data["Component 11 Branch Control Type"] = value

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

class ConnectorList(object):
    """ Corresponds to IDD object `ConnectorList`
        only two connectors allowed per loop
        if two entered, one must be Connector:Splitter and one must be Connector:Mixer
    
    """
    internal_name = "ConnectorList"
    field_count = 5
    required_fields = ["Name", "Connector 1 Object Type", "Connector 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ConnectorList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Connector 1 Object Type"] = None
        self._data["Connector 1 Name"] = None
        self._data["Connector 2 Object Type"] = None
        self._data["Connector 2 Name"] = None
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
            self.connector_1_object_type = None
        else:
            self.connector_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.connector_1_name = None
        else:
            self.connector_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.connector_2_object_type = None
        else:
            self.connector_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.connector_2_name = None
        else:
            self.connector_2_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def connector_1_object_type(self):
        """Get connector_1_object_type

        Returns:
            str: the value of `connector_1_object_type` or None if not set
        """
        return self._data["Connector 1 Object Type"]

    @connector_1_object_type.setter
    def connector_1_object_type(self, value=None):
        """  Corresponds to IDD Field `connector_1_object_type`

        Args:
            value (str): value for IDD Field `connector_1_object_type`
                Accepted values are:
                      - Connector:Splitter
                      - Connector:Mixer
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `connector_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `connector_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `connector_1_object_type`')
            vals = {}
            vals["connector:splitter"] = "Connector:Splitter"
            vals["connector:mixer"] = "Connector:Mixer"
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
                                     'field `connector_1_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Connector 1 Object Type"] = value

    @property
    def connector_1_name(self):
        """Get connector_1_name

        Returns:
            str: the value of `connector_1_name` or None if not set
        """
        return self._data["Connector 1 Name"]

    @connector_1_name.setter
    def connector_1_name(self, value=None):
        """  Corresponds to IDD Field `connector_1_name`

        Args:
            value (str): value for IDD Field `connector_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `connector_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `connector_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `connector_1_name`')

        self._data["Connector 1 Name"] = value

    @property
    def connector_2_object_type(self):
        """Get connector_2_object_type

        Returns:
            str: the value of `connector_2_object_type` or None if not set
        """
        return self._data["Connector 2 Object Type"]

    @connector_2_object_type.setter
    def connector_2_object_type(self, value=None):
        """  Corresponds to IDD Field `connector_2_object_type`

        Args:
            value (str): value for IDD Field `connector_2_object_type`
                Accepted values are:
                      - Connector:Splitter
                      - Connector:Mixer
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `connector_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `connector_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `connector_2_object_type`')
            vals = {}
            vals["connector:splitter"] = "Connector:Splitter"
            vals["connector:mixer"] = "Connector:Mixer"
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
                                     'field `connector_2_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Connector 2 Object Type"] = value

    @property
    def connector_2_name(self):
        """Get connector_2_name

        Returns:
            str: the value of `connector_2_name` or None if not set
        """
        return self._data["Connector 2 Name"]

    @connector_2_name.setter
    def connector_2_name(self, value=None):
        """  Corresponds to IDD Field `connector_2_name`

        Args:
            value (str): value for IDD Field `connector_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `connector_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `connector_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `connector_2_name`')

        self._data["Connector 2 Name"] = value

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

class OutdoorAirNode(object):
    """ Corresponds to IDD object `OutdoorAir:Node`
        This object sets the temperature and humidity conditions
        for an outdoor air node.  It allows the height above ground to be
        specified.  This object may be used more than once.
        The same node name may not appear in both an OutdoorAir:Node object and
        an OutdoorAir:NodeList object.
    
    """
    internal_name = "OutdoorAir:Node"
    field_count = 2
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `OutdoorAir:Node`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Height Above Ground"] = None
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
            self.height_above_ground = None
        else:
            self.height_above_ground = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def height_above_ground(self):
        """Get height_above_ground

        Returns:
            float: the value of `height_above_ground` or None if not set
        """
        return self._data["Height Above Ground"]

    @height_above_ground.setter
    def height_above_ground(self, value=-1.0 ):
        """  Corresponds to IDD Field `height_above_ground`
        A value less than zero indicates that the height will be ignored and the weather file conditions will be used.

        Args:
            value (float): value for IDD Field `height_above_ground`
                Units: m
                Default value: -1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `height_above_ground`'.format(value))

        self._data["Height Above Ground"] = value

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

class PipeAdiabatic(object):
    """ Corresponds to IDD object `Pipe:Adiabatic`
        Passes Inlet Node state variables to Outlet Node state variables
    
    """
    internal_name = "Pipe:Adiabatic"
    field_count = 3
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Pipe:Adiabatic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

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

class PipeAdiabaticSteam(object):
    """ Corresponds to IDD object `Pipe:Adiabatic:Steam`
        Passes Inlet Node state variables to Outlet Node state variables
    
    """
    internal_name = "Pipe:Adiabatic:Steam"
    field_count = 3
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Pipe:Adiabatic:Steam`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

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

class PipeIndoor(object):
    """ Corresponds to IDD object `Pipe:Indoor`
        Pipe model with transport delay and heat transfer to the environment.
    
    """
    internal_name = "Pipe:Indoor"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Fluid Inlet Node Name", "Fluid Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Pipe:Indoor`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Fluid Inlet Node Name"] = None
        self._data["Fluid Outlet Node Name"] = None
        self._data["Environment Type"] = None
        self._data["Ambient Temperature Zone Name"] = None
        self._data["Ambient Temperature Schedule Name"] = None
        self._data["Ambient Air Velocity Schedule Name"] = None
        self._data["Pipe Inside Diameter"] = None
        self._data["Pipe Length"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_inlet_node_name = None
        else:
            self.fluid_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_outlet_node_name = None
        else:
            self.fluid_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.environment_type = None
        else:
            self.environment_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_zone_name = None
        else:
            self.ambient_temperature_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_schedule_name = None
        else:
            self.ambient_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_air_velocity_schedule_name = None
        else:
            self.ambient_air_velocity_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_inside_diameter = None
        else:
            self.pipe_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_length = None
        else:
            self.pipe_length = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`

        Args:
            value (str): value for IDD Field `construction_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def fluid_inlet_node_name(self):
        """Get fluid_inlet_node_name

        Returns:
            str: the value of `fluid_inlet_node_name` or None if not set
        """
        return self._data["Fluid Inlet Node Name"]

    @fluid_inlet_node_name.setter
    def fluid_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `fluid_inlet_node_name`

        Args:
            value (str): value for IDD Field `fluid_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_inlet_node_name`')

        self._data["Fluid Inlet Node Name"] = value

    @property
    def fluid_outlet_node_name(self):
        """Get fluid_outlet_node_name

        Returns:
            str: the value of `fluid_outlet_node_name` or None if not set
        """
        return self._data["Fluid Outlet Node Name"]

    @fluid_outlet_node_name.setter
    def fluid_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `fluid_outlet_node_name`

        Args:
            value (str): value for IDD Field `fluid_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_outlet_node_name`')

        self._data["Fluid Outlet Node Name"] = value

    @property
    def environment_type(self):
        """Get environment_type

        Returns:
            str: the value of `environment_type` or None if not set
        """
        return self._data["Environment Type"]

    @environment_type.setter
    def environment_type(self, value="Zone"):
        """  Corresponds to IDD Field `environment_type`

        Args:
            value (str): value for IDD Field `environment_type`
                Accepted values are:
                      - Zone
                      - Schedule
                Default value: Zone
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `environment_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `environment_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `environment_type`')
            vals = {}
            vals["zone"] = "Zone"
            vals["schedule"] = "Schedule"
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
                                     'field `environment_type`'.format(value))
            value = vals[value_lower]

        self._data["Environment Type"] = value

    @property
    def ambient_temperature_zone_name(self):
        """Get ambient_temperature_zone_name

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set
        """
        return self._data["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_zone_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_zone_name`')

        self._data["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """Get ambient_temperature_schedule_name

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set
        """
        return self._data["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_schedule_name`')

        self._data["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_air_velocity_schedule_name(self):
        """Get ambient_air_velocity_schedule_name

        Returns:
            str: the value of `ambient_air_velocity_schedule_name` or None if not set
        """
        return self._data["Ambient Air Velocity Schedule Name"]

    @ambient_air_velocity_schedule_name.setter
    def ambient_air_velocity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ambient_air_velocity_schedule_name`

        Args:
            value (str): value for IDD Field `ambient_air_velocity_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_air_velocity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_air_velocity_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_air_velocity_schedule_name`')

        self._data["Ambient Air Velocity Schedule Name"] = value

    @property
    def pipe_inside_diameter(self):
        """Get pipe_inside_diameter

        Returns:
            float: the value of `pipe_inside_diameter` or None if not set
        """
        return self._data["Pipe Inside Diameter"]

    @pipe_inside_diameter.setter
    def pipe_inside_diameter(self, value=None):
        """  Corresponds to IDD Field `pipe_inside_diameter`

        Args:
            value (float): value for IDD Field `pipe_inside_diameter`
                Units: m
                IP-Units: in
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
                                 'for field `pipe_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_inside_diameter`')

        self._data["Pipe Inside Diameter"] = value

    @property
    def pipe_length(self):
        """Get pipe_length

        Returns:
            float: the value of `pipe_length` or None if not set
        """
        return self._data["Pipe Length"]

    @pipe_length.setter
    def pipe_length(self, value=None):
        """  Corresponds to IDD Field `pipe_length`

        Args:
            value (float): value for IDD Field `pipe_length`
                Units: m
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
                                 'for field `pipe_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_length`')

        self._data["Pipe Length"] = value

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

class PipeOutdoor(object):
    """ Corresponds to IDD object `Pipe:Outdoor`
        Pipe model with transport delay and heat transfer to the environment.
    
    """
    internal_name = "Pipe:Outdoor"
    field_count = 7
    required_fields = ["Name", "Construction Name", "Fluid Inlet Node Name", "Fluid Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Pipe:Outdoor`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Fluid Inlet Node Name"] = None
        self._data["Fluid Outlet Node Name"] = None
        self._data["Ambient Temperature Outdoor Air Node Name"] = None
        self._data["Pipe Inside Diameter"] = None
        self._data["Pipe Length"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_inlet_node_name = None
        else:
            self.fluid_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_outlet_node_name = None
        else:
            self.fluid_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_outdoor_air_node_name = None
        else:
            self.ambient_temperature_outdoor_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_inside_diameter = None
        else:
            self.pipe_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_length = None
        else:
            self.pipe_length = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`

        Args:
            value (str): value for IDD Field `construction_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def fluid_inlet_node_name(self):
        """Get fluid_inlet_node_name

        Returns:
            str: the value of `fluid_inlet_node_name` or None if not set
        """
        return self._data["Fluid Inlet Node Name"]

    @fluid_inlet_node_name.setter
    def fluid_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `fluid_inlet_node_name`

        Args:
            value (str): value for IDD Field `fluid_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_inlet_node_name`')

        self._data["Fluid Inlet Node Name"] = value

    @property
    def fluid_outlet_node_name(self):
        """Get fluid_outlet_node_name

        Returns:
            str: the value of `fluid_outlet_node_name` or None if not set
        """
        return self._data["Fluid Outlet Node Name"]

    @fluid_outlet_node_name.setter
    def fluid_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `fluid_outlet_node_name`

        Args:
            value (str): value for IDD Field `fluid_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_outlet_node_name`')

        self._data["Fluid Outlet Node Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """Get ambient_temperature_outdoor_air_node_name

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set
        """
        return self._data["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_outdoor_air_node_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_outdoor_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_temperature_outdoor_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_outdoor_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_outdoor_air_node_name`')

        self._data["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def pipe_inside_diameter(self):
        """Get pipe_inside_diameter

        Returns:
            float: the value of `pipe_inside_diameter` or None if not set
        """
        return self._data["Pipe Inside Diameter"]

    @pipe_inside_diameter.setter
    def pipe_inside_diameter(self, value=None):
        """  Corresponds to IDD Field `pipe_inside_diameter`

        Args:
            value (float): value for IDD Field `pipe_inside_diameter`
                Units: m
                IP-Units: in
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
                                 'for field `pipe_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_inside_diameter`')

        self._data["Pipe Inside Diameter"] = value

    @property
    def pipe_length(self):
        """Get pipe_length

        Returns:
            float: the value of `pipe_length` or None if not set
        """
        return self._data["Pipe Length"]

    @pipe_length.setter
    def pipe_length(self, value=None):
        """  Corresponds to IDD Field `pipe_length`

        Args:
            value (float): value for IDD Field `pipe_length`
                Units: m
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
                                 'for field `pipe_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_length`')

        self._data["Pipe Length"] = value

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

class PipeUnderground(object):
    """ Corresponds to IDD object `Pipe:Underground`
        Buried Pipe model: For pipes buried at a depth less
        than one meter, this is an alternative object to:
        HeatExchanger:Surface
    
    """
    internal_name = "Pipe:Underground"
    field_count = 11
    required_fields = ["Name", "Construction Name", "Fluid Inlet Node Name", "Fluid Outlet Node Name", "Sun Exposure", "Soil Material Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Pipe:Underground`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Fluid Inlet Node Name"] = None
        self._data["Fluid Outlet Node Name"] = None
        self._data["Sun Exposure"] = None
        self._data["Pipe Inside Diameter"] = None
        self._data["Pipe Length"] = None
        self._data["Soil Material Name"] = None
        self._data["Average Soil Surface Temperature"] = None
        self._data["Amplitude of Soil Surface Temperature"] = None
        self._data["Phase Constant of Soil Surface Temperature"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_inlet_node_name = None
        else:
            self.fluid_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_outlet_node_name = None
        else:
            self.fluid_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sun_exposure = None
        else:
            self.sun_exposure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_inside_diameter = None
        else:
            self.pipe_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_length = None
        else:
            self.pipe_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_material_name = None
        else:
            self.soil_material_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.average_soil_surface_temperature = None
        else:
            self.average_soil_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.amplitude_of_soil_surface_temperature = None
        else:
            self.amplitude_of_soil_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.phase_constant_of_soil_surface_temperature = None
        else:
            self.phase_constant_of_soil_surface_temperature = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`

        Args:
            value (str): value for IDD Field `construction_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def fluid_inlet_node_name(self):
        """Get fluid_inlet_node_name

        Returns:
            str: the value of `fluid_inlet_node_name` or None if not set
        """
        return self._data["Fluid Inlet Node Name"]

    @fluid_inlet_node_name.setter
    def fluid_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `fluid_inlet_node_name`

        Args:
            value (str): value for IDD Field `fluid_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_inlet_node_name`')

        self._data["Fluid Inlet Node Name"] = value

    @property
    def fluid_outlet_node_name(self):
        """Get fluid_outlet_node_name

        Returns:
            str: the value of `fluid_outlet_node_name` or None if not set
        """
        return self._data["Fluid Outlet Node Name"]

    @fluid_outlet_node_name.setter
    def fluid_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `fluid_outlet_node_name`

        Args:
            value (str): value for IDD Field `fluid_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fluid_outlet_node_name`')

        self._data["Fluid Outlet Node Name"] = value

    @property
    def sun_exposure(self):
        """Get sun_exposure

        Returns:
            str: the value of `sun_exposure` or None if not set
        """
        return self._data["Sun Exposure"]

    @sun_exposure.setter
    def sun_exposure(self, value=None):
        """  Corresponds to IDD Field `sun_exposure`

        Args:
            value (str): value for IDD Field `sun_exposure`
                Accepted values are:
                      - SunExposed
                      - NoSun
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `sun_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sun_exposure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `sun_exposure`')
            vals = {}
            vals["sunexposed"] = "SunExposed"
            vals["nosun"] = "NoSun"
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
                                     'field `sun_exposure`'.format(value))
            value = vals[value_lower]

        self._data["Sun Exposure"] = value

    @property
    def pipe_inside_diameter(self):
        """Get pipe_inside_diameter

        Returns:
            float: the value of `pipe_inside_diameter` or None if not set
        """
        return self._data["Pipe Inside Diameter"]

    @pipe_inside_diameter.setter
    def pipe_inside_diameter(self, value=None):
        """  Corresponds to IDD Field `pipe_inside_diameter`
        pipe thickness is defined in the Construction object

        Args:
            value (float): value for IDD Field `pipe_inside_diameter`
                Units: m
                IP-Units: in
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
                                 'for field `pipe_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_inside_diameter`')

        self._data["Pipe Inside Diameter"] = value

    @property
    def pipe_length(self):
        """Get pipe_length

        Returns:
            float: the value of `pipe_length` or None if not set
        """
        return self._data["Pipe Length"]

    @pipe_length.setter
    def pipe_length(self, value=None):
        """  Corresponds to IDD Field `pipe_length`

        Args:
            value (float): value for IDD Field `pipe_length`
                Units: m
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
                                 'for field `pipe_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_length`')

        self._data["Pipe Length"] = value

    @property
    def soil_material_name(self):
        """Get soil_material_name

        Returns:
            str: the value of `soil_material_name` or None if not set
        """
        return self._data["Soil Material Name"]

    @soil_material_name.setter
    def soil_material_name(self, value=None):
        """  Corresponds to IDD Field `soil_material_name`

        Args:
            value (str): value for IDD Field `soil_material_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `soil_material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `soil_material_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `soil_material_name`')

        self._data["Soil Material Name"] = value

    @property
    def average_soil_surface_temperature(self):
        """Get average_soil_surface_temperature

        Returns:
            float: the value of `average_soil_surface_temperature` or None if not set
        """
        return self._data["Average Soil Surface Temperature"]

    @average_soil_surface_temperature.setter
    def average_soil_surface_temperature(self, value=0.0 ):
        """  Corresponds to IDD Field `average_soil_surface_temperature`
        optional

        Args:
            value (float): value for IDD Field `average_soil_surface_temperature`
                Units: C
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
                                 'for field `average_soil_surface_temperature`'.format(value))

        self._data["Average Soil Surface Temperature"] = value

    @property
    def amplitude_of_soil_surface_temperature(self):
        """Get amplitude_of_soil_surface_temperature

        Returns:
            float: the value of `amplitude_of_soil_surface_temperature` or None if not set
        """
        return self._data["Amplitude of Soil Surface Temperature"]

    @amplitude_of_soil_surface_temperature.setter
    def amplitude_of_soil_surface_temperature(self, value=0.0 ):
        """  Corresponds to IDD Field `amplitude_of_soil_surface_temperature`
        optional

        Args:
            value (float): value for IDD Field `amplitude_of_soil_surface_temperature`
                Units: C
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
                                 'for field `amplitude_of_soil_surface_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `amplitude_of_soil_surface_temperature`')

        self._data["Amplitude of Soil Surface Temperature"] = value

    @property
    def phase_constant_of_soil_surface_temperature(self):
        """Get phase_constant_of_soil_surface_temperature

        Returns:
            float: the value of `phase_constant_of_soil_surface_temperature` or None if not set
        """
        return self._data["Phase Constant of Soil Surface Temperature"]

    @phase_constant_of_soil_surface_temperature.setter
    def phase_constant_of_soil_surface_temperature(self, value=0.0 ):
        """  Corresponds to IDD Field `phase_constant_of_soil_surface_temperature`
        optional

        Args:
            value (float): value for IDD Field `phase_constant_of_soil_surface_temperature`
                Units: days
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
                                 'for field `phase_constant_of_soil_surface_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `phase_constant_of_soil_surface_temperature`')

        self._data["Phase Constant of Soil Surface Temperature"] = value

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

class PipingSystemUndergroundDomain(object):
    """ Corresponds to IDD object `PipingSystem:Underground:Domain`
        The ground domain object for underground piping system simulation.
    
    """
    internal_name = "PipingSystem:Underground:Domain"
    field_count = 37
    required_fields = ["Name", "Xmax", "Ymax", "Zmax", "X-Direction Mesh Type", "Y-Direction Mesh Type", "Z-Direction Mesh Type", "Soil Thermal Conductivity", "Soil Density", "Soil Specific Heat", "Kusuda-Achenbach Average Surface Temperature", "Kusuda-Achenbach Average Amplitude of Surface Temperature", "Kusuda-Achenbach Phase Shift of Minimum Surface Temperature", "Number of Pipe Circuits Entered for this Domain", "Pipe Circuit 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PipingSystem:Underground:Domain`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Xmax"] = None
        self._data["Ymax"] = None
        self._data["Zmax"] = None
        self._data["X-Direction Mesh Density Parameter"] = None
        self._data["X-Direction Mesh Type"] = None
        self._data["X-Direction Geometric Coefficient"] = None
        self._data["Y-Direction Mesh Density Parameter"] = None
        self._data["Y-Direction Mesh Type"] = None
        self._data["Y-Direction Geometric Coefficient"] = None
        self._data["Z-Direction Mesh Density Parameter"] = None
        self._data["Z-Direction Mesh Type"] = None
        self._data["Z-Direction Geometric Coefficient"] = None
        self._data["Soil Thermal Conductivity"] = None
        self._data["Soil Density"] = None
        self._data["Soil Specific Heat"] = None
        self._data["Soil Moisture Content Volume Fraction"] = None
        self._data["Soil Moisture Content Volume Fraction at Saturation"] = None
        self._data["Kusuda-Achenbach Average Surface Temperature"] = None
        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = None
        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = None
        self._data["This Domain Includes Basement Surface Interaction"] = None
        self._data["Width of Basement Floor in Ground Domain"] = None
        self._data["Depth of Basement Wall In Ground Domain"] = None
        self._data["Shift Pipe X Coordinates By Basement Width"] = None
        self._data["Name of Basement Wall Boundary Condition Model"] = None
        self._data["Name of Basement Floor Boundary Condition Model"] = None
        self._data["Convergence Criterion for the Outer Cartesian Domain Iteration Loop"] = None
        self._data["Maximum Iterations in the Outer Cartesian Domain Iteration Loop"] = None
        self._data["Evapotranspiration Ground Cover Parameter"] = None
        self._data["Number of Pipe Circuits Entered for this Domain"] = None
        self._data["Pipe Circuit 1"] = None
        self._data["Pipe Circuit 2"] = None
        self._data["Pipe Circuit 3"] = None
        self._data["Pipe Circuit 4"] = None
        self._data["Pipe Circuit 5"] = None
        self._data["Pipe Circuit 6"] = None
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
            self.xmax = None
        else:
            self.xmax = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ymax = None
        else:
            self.ymax = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zmax = None
        else:
            self.zmax = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.xdirection_mesh_density_parameter = None
        else:
            self.xdirection_mesh_density_parameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.xdirection_mesh_type = None
        else:
            self.xdirection_mesh_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.xdirection_geometric_coefficient = None
        else:
            self.xdirection_geometric_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ydirection_mesh_density_parameter = None
        else:
            self.ydirection_mesh_density_parameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ydirection_mesh_type = None
        else:
            self.ydirection_mesh_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ydirection_geometric_coefficient = None
        else:
            self.ydirection_geometric_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zdirection_mesh_density_parameter = None
        else:
            self.zdirection_mesh_density_parameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zdirection_mesh_type = None
        else:
            self.zdirection_mesh_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zdirection_geometric_coefficient = None
        else:
            self.zdirection_geometric_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_thermal_conductivity = None
        else:
            self.soil_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_density = None
        else:
            self.soil_density = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_specific_heat = None
        else:
            self.soil_specific_heat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_moisture_content_volume_fraction = None
        else:
            self.soil_moisture_content_volume_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_moisture_content_volume_fraction_at_saturation = None
        else:
            self.soil_moisture_content_volume_fraction_at_saturation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_surface_temperature = None
        else:
            self.kusudaachenbach_average_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = None
        else:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = None
        else:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.this_domain_includes_basement_surface_interaction = None
        else:
            self.this_domain_includes_basement_surface_interaction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width_of_basement_floor_in_ground_domain = None
        else:
            self.width_of_basement_floor_in_ground_domain = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.depth_of_basement_wall_in_ground_domain = None
        else:
            self.depth_of_basement_wall_in_ground_domain = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shift_pipe_x_coordinates_by_basement_width = None
        else:
            self.shift_pipe_x_coordinates_by_basement_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.name_of_basement_wall_boundary_condition_model = None
        else:
            self.name_of_basement_wall_boundary_condition_model = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.name_of_basement_floor_boundary_condition_model = None
        else:
            self.name_of_basement_floor_boundary_condition_model = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop = None
        else:
            self.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop = None
        else:
            self.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evapotranspiration_ground_cover_parameter = None
        else:
            self.evapotranspiration_ground_cover_parameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_pipe_circuits_entered_for_this_domain = None
        else:
            self.number_of_pipe_circuits_entered_for_this_domain = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_circuit_1 = None
        else:
            self.pipe_circuit_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_circuit_2 = None
        else:
            self.pipe_circuit_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_circuit_3 = None
        else:
            self.pipe_circuit_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_circuit_4 = None
        else:
            self.pipe_circuit_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_circuit_5 = None
        else:
            self.pipe_circuit_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_circuit_6 = None
        else:
            self.pipe_circuit_6 = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def xmax(self):
        """Get xmax

        Returns:
            float: the value of `xmax` or None if not set
        """
        return self._data["Xmax"]

    @xmax.setter
    def xmax(self, value=None):
        """  Corresponds to IDD Field `xmax`
        Domain extent in the local 'X' direction

        Args:
            value (float): value for IDD Field `xmax`
                Units: m
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
                                 'for field `xmax`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `xmax`')

        self._data["Xmax"] = value

    @property
    def ymax(self):
        """Get ymax

        Returns:
            float: the value of `ymax` or None if not set
        """
        return self._data["Ymax"]

    @ymax.setter
    def ymax(self, value=None):
        """  Corresponds to IDD Field `ymax`
        Domain extent in the local 'Y' direction

        Args:
            value (float): value for IDD Field `ymax`
                Units: m
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
                                 'for field `ymax`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ymax`')

        self._data["Ymax"] = value

    @property
    def zmax(self):
        """Get zmax

        Returns:
            float: the value of `zmax` or None if not set
        """
        return self._data["Zmax"]

    @zmax.setter
    def zmax(self, value=None):
        """  Corresponds to IDD Field `zmax`
        Domain extent in the local 'Y' direction

        Args:
            value (float): value for IDD Field `zmax`
                Units: m
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
                                 'for field `zmax`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `zmax`')

        self._data["Zmax"] = value

    @property
    def xdirection_mesh_density_parameter(self):
        """Get xdirection_mesh_density_parameter

        Returns:
            int: the value of `xdirection_mesh_density_parameter` or None if not set
        """
        return self._data["X-Direction Mesh Density Parameter"]

    @xdirection_mesh_density_parameter.setter
    def xdirection_mesh_density_parameter(self, value=4 ):
        """  Corresponds to IDD Field `xdirection_mesh_density_parameter`
        If mesh type is symmetric geometric, this should be an even number.

        Args:
            value (int): value for IDD Field `xdirection_mesh_density_parameter`
                Default value: 4
                value > 0
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
                                 'for field `xdirection_mesh_density_parameter`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `xdirection_mesh_density_parameter`')

        self._data["X-Direction Mesh Density Parameter"] = value

    @property
    def xdirection_mesh_type(self):
        """Get xdirection_mesh_type

        Returns:
            str: the value of `xdirection_mesh_type` or None if not set
        """
        return self._data["X-Direction Mesh Type"]

    @xdirection_mesh_type.setter
    def xdirection_mesh_type(self, value=None):
        """  Corresponds to IDD Field `xdirection_mesh_type`

        Args:
            value (str): value for IDD Field `xdirection_mesh_type`
                Accepted values are:
                      - Uniform
                      - SymmetricGeometric
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `xdirection_mesh_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `xdirection_mesh_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `xdirection_mesh_type`')
            vals = {}
            vals["uniform"] = "Uniform"
            vals["symmetricgeometric"] = "SymmetricGeometric"
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
                                     'field `xdirection_mesh_type`'.format(value))
            value = vals[value_lower]

        self._data["X-Direction Mesh Type"] = value

    @property
    def xdirection_geometric_coefficient(self):
        """Get xdirection_geometric_coefficient

        Returns:
            float: the value of `xdirection_geometric_coefficient` or None if not set
        """
        return self._data["X-Direction Geometric Coefficient"]

    @xdirection_geometric_coefficient.setter
    def xdirection_geometric_coefficient(self, value=1.3 ):
        """  Corresponds to IDD Field `xdirection_geometric_coefficient`
        optional
        Only used if mesh type is symmetric geometric

        Args:
            value (float): value for IDD Field `xdirection_geometric_coefficient`
                Default value: 1.3
                value >= 1.0
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
                                 'for field `xdirection_geometric_coefficient`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `xdirection_geometric_coefficient`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `xdirection_geometric_coefficient`')

        self._data["X-Direction Geometric Coefficient"] = value

    @property
    def ydirection_mesh_density_parameter(self):
        """Get ydirection_mesh_density_parameter

        Returns:
            int: the value of `ydirection_mesh_density_parameter` or None if not set
        """
        return self._data["Y-Direction Mesh Density Parameter"]

    @ydirection_mesh_density_parameter.setter
    def ydirection_mesh_density_parameter(self, value=4 ):
        """  Corresponds to IDD Field `ydirection_mesh_density_parameter`
        If mesh type is symmetric geometric, this should be an even number.

        Args:
            value (int): value for IDD Field `ydirection_mesh_density_parameter`
                Default value: 4
                value > 0
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
                                 'for field `ydirection_mesh_density_parameter`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `ydirection_mesh_density_parameter`')

        self._data["Y-Direction Mesh Density Parameter"] = value

    @property
    def ydirection_mesh_type(self):
        """Get ydirection_mesh_type

        Returns:
            str: the value of `ydirection_mesh_type` or None if not set
        """
        return self._data["Y-Direction Mesh Type"]

    @ydirection_mesh_type.setter
    def ydirection_mesh_type(self, value=None):
        """  Corresponds to IDD Field `ydirection_mesh_type`

        Args:
            value (str): value for IDD Field `ydirection_mesh_type`
                Accepted values are:
                      - Uniform
                      - SymmetricGeometric
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ydirection_mesh_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ydirection_mesh_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ydirection_mesh_type`')
            vals = {}
            vals["uniform"] = "Uniform"
            vals["symmetricgeometric"] = "SymmetricGeometric"
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
                                     'field `ydirection_mesh_type`'.format(value))
            value = vals[value_lower]

        self._data["Y-Direction Mesh Type"] = value

    @property
    def ydirection_geometric_coefficient(self):
        """Get ydirection_geometric_coefficient

        Returns:
            float: the value of `ydirection_geometric_coefficient` or None if not set
        """
        return self._data["Y-Direction Geometric Coefficient"]

    @ydirection_geometric_coefficient.setter
    def ydirection_geometric_coefficient(self, value=1.3 ):
        """  Corresponds to IDD Field `ydirection_geometric_coefficient`
        optional
        Only used if mesh type is symmetric geometric

        Args:
            value (float): value for IDD Field `ydirection_geometric_coefficient`
                Default value: 1.3
                value >= 1.0
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
                                 'for field `ydirection_geometric_coefficient`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `ydirection_geometric_coefficient`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `ydirection_geometric_coefficient`')

        self._data["Y-Direction Geometric Coefficient"] = value

    @property
    def zdirection_mesh_density_parameter(self):
        """Get zdirection_mesh_density_parameter

        Returns:
            int: the value of `zdirection_mesh_density_parameter` or None if not set
        """
        return self._data["Z-Direction Mesh Density Parameter"]

    @zdirection_mesh_density_parameter.setter
    def zdirection_mesh_density_parameter(self, value=4 ):
        """  Corresponds to IDD Field `zdirection_mesh_density_parameter`
        If mesh type is symmetric geometric, this should be an even number.

        Args:
            value (int): value for IDD Field `zdirection_mesh_density_parameter`
                Default value: 4
                value > 0
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
                                 'for field `zdirection_mesh_density_parameter`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `zdirection_mesh_density_parameter`')

        self._data["Z-Direction Mesh Density Parameter"] = value

    @property
    def zdirection_mesh_type(self):
        """Get zdirection_mesh_type

        Returns:
            str: the value of `zdirection_mesh_type` or None if not set
        """
        return self._data["Z-Direction Mesh Type"]

    @zdirection_mesh_type.setter
    def zdirection_mesh_type(self, value=None):
        """  Corresponds to IDD Field `zdirection_mesh_type`

        Args:
            value (str): value for IDD Field `zdirection_mesh_type`
                Accepted values are:
                      - Uniform
                      - SymmetricGeometric
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zdirection_mesh_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zdirection_mesh_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zdirection_mesh_type`')
            vals = {}
            vals["uniform"] = "Uniform"
            vals["symmetricgeometric"] = "SymmetricGeometric"
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
                                     'field `zdirection_mesh_type`'.format(value))
            value = vals[value_lower]

        self._data["Z-Direction Mesh Type"] = value

    @property
    def zdirection_geometric_coefficient(self):
        """Get zdirection_geometric_coefficient

        Returns:
            float: the value of `zdirection_geometric_coefficient` or None if not set
        """
        return self._data["Z-Direction Geometric Coefficient"]

    @zdirection_geometric_coefficient.setter
    def zdirection_geometric_coefficient(self, value=1.3 ):
        """  Corresponds to IDD Field `zdirection_geometric_coefficient`
        optional
        Only used if mesh type is symmetric geometric

        Args:
            value (float): value for IDD Field `zdirection_geometric_coefficient`
                Default value: 1.3
                value >= 1.0
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
                                 'for field `zdirection_geometric_coefficient`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `zdirection_geometric_coefficient`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `zdirection_geometric_coefficient`')

        self._data["Z-Direction Geometric Coefficient"] = value

    @property
    def soil_thermal_conductivity(self):
        """Get soil_thermal_conductivity

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set
        """
        return self._data["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `soil_thermal_conductivity`

        Args:
            value (float): value for IDD Field `soil_thermal_conductivity`
                Units: W/m-K
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
                                 'for field `soil_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_thermal_conductivity`')

        self._data["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """Get soil_density

        Returns:
            float: the value of `soil_density` or None if not set
        """
        return self._data["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=None):
        """  Corresponds to IDD Field `soil_density`

        Args:
            value (float): value for IDD Field `soil_density`
                Units: kg/m3
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
                                 'for field `soil_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_density`')

        self._data["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """Get soil_specific_heat

        Returns:
            float: the value of `soil_specific_heat` or None if not set
        """
        return self._data["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=None):
        """  Corresponds to IDD Field `soil_specific_heat`
        This is a dry soil property, which is adjusted for freezing effects
        by the simulation algorithm.

        Args:
            value (float): value for IDD Field `soil_specific_heat`
                Units: J/kg-K
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
                                 'for field `soil_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_specific_heat`')

        self._data["Soil Specific Heat"] = value

    @property
    def soil_moisture_content_volume_fraction(self):
        """Get soil_moisture_content_volume_fraction

        Returns:
            float: the value of `soil_moisture_content_volume_fraction` or None if not set
        """
        return self._data["Soil Moisture Content Volume Fraction"]

    @soil_moisture_content_volume_fraction.setter
    def soil_moisture_content_volume_fraction(self, value=30.0 ):
        """  Corresponds to IDD Field `soil_moisture_content_volume_fraction`

        Args:
            value (float): value for IDD Field `soil_moisture_content_volume_fraction`
                Units: percent
                Default value: 30.0
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
                                 'for field `soil_moisture_content_volume_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `soil_moisture_content_volume_fraction`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `soil_moisture_content_volume_fraction`')

        self._data["Soil Moisture Content Volume Fraction"] = value

    @property
    def soil_moisture_content_volume_fraction_at_saturation(self):
        """Get soil_moisture_content_volume_fraction_at_saturation

        Returns:
            float: the value of `soil_moisture_content_volume_fraction_at_saturation` or None if not set
        """
        return self._data["Soil Moisture Content Volume Fraction at Saturation"]

    @soil_moisture_content_volume_fraction_at_saturation.setter
    def soil_moisture_content_volume_fraction_at_saturation(self, value=50.0 ):
        """  Corresponds to IDD Field `soil_moisture_content_volume_fraction_at_saturation`

        Args:
            value (float): value for IDD Field `soil_moisture_content_volume_fraction_at_saturation`
                Units: percent
                Default value: 50.0
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
                                 'for field `soil_moisture_content_volume_fraction_at_saturation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `soil_moisture_content_volume_fraction_at_saturation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `soil_moisture_content_volume_fraction_at_saturation`')

        self._data["Soil Moisture Content Volume Fraction at Saturation"] = value

    @property
    def kusudaachenbach_average_surface_temperature(self):
        """Get kusudaachenbach_average_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Surface Temperature"]

    @kusudaachenbach_average_surface_temperature.setter
    def kusudaachenbach_average_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_average_surface_temperature`

        Args:
            value (float): value for IDD Field `kusudaachenbach_average_surface_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_average_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Average Surface Temperature"] = value

    @property
    def kusudaachenbach_average_amplitude_of_surface_temperature(self):
        """Get kusudaachenbach_average_amplitude_of_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_amplitude_of_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"]

    @kusudaachenbach_average_amplitude_of_surface_temperature.setter
    def kusudaachenbach_average_amplitude_of_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_average_amplitude_of_surface_temperature`

        Args:
            value (float): value for IDD Field `kusudaachenbach_average_amplitude_of_surface_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_average_amplitude_of_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = value

    @property
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self):
        """Get kusudaachenbach_phase_shift_of_minimum_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_phase_shift_of_minimum_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"]

    @kusudaachenbach_phase_shift_of_minimum_surface_temperature.setter
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`

        Args:
            value (float): value for IDD Field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`
                Units: days
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = value

    @property
    def this_domain_includes_basement_surface_interaction(self):
        """Get this_domain_includes_basement_surface_interaction

        Returns:
            str: the value of `this_domain_includes_basement_surface_interaction` or None if not set
        """
        return self._data["This Domain Includes Basement Surface Interaction"]

    @this_domain_includes_basement_surface_interaction.setter
    def this_domain_includes_basement_surface_interaction(self, value="No"):
        """  Corresponds to IDD Field `this_domain_includes_basement_surface_interaction`
        if Yes, then the following basement inputs are used
        if No, then the following basement inputs are *ignored*

        Args:
            value (str): value for IDD Field `this_domain_includes_basement_surface_interaction`
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
                                 'for field `this_domain_includes_basement_surface_interaction`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `this_domain_includes_basement_surface_interaction`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `this_domain_includes_basement_surface_interaction`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `this_domain_includes_basement_surface_interaction`'.format(value))
            value = vals[value_lower]

        self._data["This Domain Includes Basement Surface Interaction"] = value

    @property
    def width_of_basement_floor_in_ground_domain(self):
        """Get width_of_basement_floor_in_ground_domain

        Returns:
            float: the value of `width_of_basement_floor_in_ground_domain` or None if not set
        """
        return self._data["Width of Basement Floor in Ground Domain"]

    @width_of_basement_floor_in_ground_domain.setter
    def width_of_basement_floor_in_ground_domain(self, value=None):
        """  Corresponds to IDD Field `width_of_basement_floor_in_ground_domain`
        Required only if Domain Has Basement Interaction

        Args:
            value (float): value for IDD Field `width_of_basement_floor_in_ground_domain`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `width_of_basement_floor_in_ground_domain`'.format(value))

        self._data["Width of Basement Floor in Ground Domain"] = value

    @property
    def depth_of_basement_wall_in_ground_domain(self):
        """Get depth_of_basement_wall_in_ground_domain

        Returns:
            float: the value of `depth_of_basement_wall_in_ground_domain` or None if not set
        """
        return self._data["Depth of Basement Wall In Ground Domain"]

    @depth_of_basement_wall_in_ground_domain.setter
    def depth_of_basement_wall_in_ground_domain(self, value=None):
        """  Corresponds to IDD Field `depth_of_basement_wall_in_ground_domain`
        Required only if Domain Has Basement Interaction

        Args:
            value (float): value for IDD Field `depth_of_basement_wall_in_ground_domain`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `depth_of_basement_wall_in_ground_domain`'.format(value))

        self._data["Depth of Basement Wall In Ground Domain"] = value

    @property
    def shift_pipe_x_coordinates_by_basement_width(self):
        """Get shift_pipe_x_coordinates_by_basement_width

        Returns:
            str: the value of `shift_pipe_x_coordinates_by_basement_width` or None if not set
        """
        return self._data["Shift Pipe X Coordinates By Basement Width"]

    @shift_pipe_x_coordinates_by_basement_width.setter
    def shift_pipe_x_coordinates_by_basement_width(self, value=None):
        """  Corresponds to IDD Field `shift_pipe_x_coordinates_by_basement_width`
        Required only if Domain Has Basement Interaction

        Args:
            value (str): value for IDD Field `shift_pipe_x_coordinates_by_basement_width`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `shift_pipe_x_coordinates_by_basement_width`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `shift_pipe_x_coordinates_by_basement_width`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `shift_pipe_x_coordinates_by_basement_width`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `shift_pipe_x_coordinates_by_basement_width`'.format(value))
            value = vals[value_lower]

        self._data["Shift Pipe X Coordinates By Basement Width"] = value

    @property
    def name_of_basement_wall_boundary_condition_model(self):
        """Get name_of_basement_wall_boundary_condition_model

        Returns:
            str: the value of `name_of_basement_wall_boundary_condition_model` or None if not set
        """
        return self._data["Name of Basement Wall Boundary Condition Model"]

    @name_of_basement_wall_boundary_condition_model.setter
    def name_of_basement_wall_boundary_condition_model(self, value=None):
        """  Corresponds to IDD Field `name_of_basement_wall_boundary_condition_model`
        Required only if Domain Has Basement Interaction

        Args:
            value (str): value for IDD Field `name_of_basement_wall_boundary_condition_model`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name_of_basement_wall_boundary_condition_model`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name_of_basement_wall_boundary_condition_model`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name_of_basement_wall_boundary_condition_model`')

        self._data["Name of Basement Wall Boundary Condition Model"] = value

    @property
    def name_of_basement_floor_boundary_condition_model(self):
        """Get name_of_basement_floor_boundary_condition_model

        Returns:
            str: the value of `name_of_basement_floor_boundary_condition_model` or None if not set
        """
        return self._data["Name of Basement Floor Boundary Condition Model"]

    @name_of_basement_floor_boundary_condition_model.setter
    def name_of_basement_floor_boundary_condition_model(self, value=None):
        """  Corresponds to IDD Field `name_of_basement_floor_boundary_condition_model`
        Required only if Domain Has Basement Interaction

        Args:
            value (str): value for IDD Field `name_of_basement_floor_boundary_condition_model`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name_of_basement_floor_boundary_condition_model`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name_of_basement_floor_boundary_condition_model`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name_of_basement_floor_boundary_condition_model`')

        self._data["Name of Basement Floor Boundary Condition Model"] = value

    @property
    def convergence_criterion_for_the_outer_cartesian_domain_iteration_loop(self):
        """Get convergence_criterion_for_the_outer_cartesian_domain_iteration_loop

        Returns:
            float: the value of `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop` or None if not set
        """
        return self._data["Convergence Criterion for the Outer Cartesian Domain Iteration Loop"]

    @convergence_criterion_for_the_outer_cartesian_domain_iteration_loop.setter
    def convergence_criterion_for_the_outer_cartesian_domain_iteration_loop(self, value=0.001 ):
        """  Corresponds to IDD Field `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`

        Args:
            value (float): value for IDD Field `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`
                Units: deltaC
                Default value: 0.001
                value >= 1e-06
                value <= 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`'.format(value))
            if value < 1e-06:
                raise ValueError('value need to be greater or equal 1e-06 '
                                 'for field `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`')

        self._data["Convergence Criterion for the Outer Cartesian Domain Iteration Loop"] = value

    @property
    def maximum_iterations_in_the_outer_cartesian_domain_iteration_loop(self):
        """Get maximum_iterations_in_the_outer_cartesian_domain_iteration_loop

        Returns:
            int: the value of `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop` or None if not set
        """
        return self._data["Maximum Iterations in the Outer Cartesian Domain Iteration Loop"]

    @maximum_iterations_in_the_outer_cartesian_domain_iteration_loop.setter
    def maximum_iterations_in_the_outer_cartesian_domain_iteration_loop(self, value=500 ):
        """  Corresponds to IDD Field `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`

        Args:
            value (int): value for IDD Field `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`
                Default value: 500
                value >= 3
                value <= 10000
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
                                 'for field `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`'.format(value))
            if value < 3:
                raise ValueError('value need to be greater or equal 3 '
                                 'for field `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`')
            if value > 10000:
                raise ValueError('value need to be smaller 10000 '
                                 'for field `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`')

        self._data["Maximum Iterations in the Outer Cartesian Domain Iteration Loop"] = value

    @property
    def evapotranspiration_ground_cover_parameter(self):
        """Get evapotranspiration_ground_cover_parameter

        Returns:
            float: the value of `evapotranspiration_ground_cover_parameter` or None if not set
        """
        return self._data["Evapotranspiration Ground Cover Parameter"]

    @evapotranspiration_ground_cover_parameter.setter
    def evapotranspiration_ground_cover_parameter(self, value=0.4 ):
        """  Corresponds to IDD Field `evapotranspiration_ground_cover_parameter`
        This specifies the ground cover effects during evapotranspiration
        calculations.  The value roughly represents the following cases:
        = 0   : concrete or other solid, non-permeable ground surface material
        = 0.5 : short grass, much like a manicured lawn
        = 1   : standard reference state (12 cm grass)
        = 1.5 : wild growth

        Args:
            value (float): value for IDD Field `evapotranspiration_ground_cover_parameter`
                Default value: 0.4
                value >= 0.0
                value <= 1.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `evapotranspiration_ground_cover_parameter`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evapotranspiration_ground_cover_parameter`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `evapotranspiration_ground_cover_parameter`')

        self._data["Evapotranspiration Ground Cover Parameter"] = value

    @property
    def number_of_pipe_circuits_entered_for_this_domain(self):
        """Get number_of_pipe_circuits_entered_for_this_domain

        Returns:
            int: the value of `number_of_pipe_circuits_entered_for_this_domain` or None if not set
        """
        return self._data["Number of Pipe Circuits Entered for this Domain"]

    @number_of_pipe_circuits_entered_for_this_domain.setter
    def number_of_pipe_circuits_entered_for_this_domain(self, value=None):
        """  Corresponds to IDD Field `number_of_pipe_circuits_entered_for_this_domain`

        Args:
            value (int): value for IDD Field `number_of_pipe_circuits_entered_for_this_domain`
                value >= 1
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
                                 'for field `number_of_pipe_circuits_entered_for_this_domain`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_pipe_circuits_entered_for_this_domain`')

        self._data["Number of Pipe Circuits Entered for this Domain"] = value

    @property
    def pipe_circuit_1(self):
        """Get pipe_circuit_1

        Returns:
            str: the value of `pipe_circuit_1` or None if not set
        """
        return self._data["Pipe Circuit 1"]

    @pipe_circuit_1.setter
    def pipe_circuit_1(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_1`
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_circuit_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_circuit_1`')

        self._data["Pipe Circuit 1"] = value

    @property
    def pipe_circuit_2(self):
        """Get pipe_circuit_2

        Returns:
            str: the value of `pipe_circuit_2` or None if not set
        """
        return self._data["Pipe Circuit 2"]

    @pipe_circuit_2.setter
    def pipe_circuit_2(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_2`
        optional
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_circuit_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_circuit_2`')

        self._data["Pipe Circuit 2"] = value

    @property
    def pipe_circuit_3(self):
        """Get pipe_circuit_3

        Returns:
            str: the value of `pipe_circuit_3` or None if not set
        """
        return self._data["Pipe Circuit 3"]

    @pipe_circuit_3.setter
    def pipe_circuit_3(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_3`
        optional
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_circuit_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_circuit_3`')

        self._data["Pipe Circuit 3"] = value

    @property
    def pipe_circuit_4(self):
        """Get pipe_circuit_4

        Returns:
            str: the value of `pipe_circuit_4` or None if not set
        """
        return self._data["Pipe Circuit 4"]

    @pipe_circuit_4.setter
    def pipe_circuit_4(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_4`
        optional
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_circuit_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_circuit_4`')

        self._data["Pipe Circuit 4"] = value

    @property
    def pipe_circuit_5(self):
        """Get pipe_circuit_5

        Returns:
            str: the value of `pipe_circuit_5` or None if not set
        """
        return self._data["Pipe Circuit 5"]

    @pipe_circuit_5.setter
    def pipe_circuit_5(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_5`
        optional
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_circuit_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_circuit_5`')

        self._data["Pipe Circuit 5"] = value

    @property
    def pipe_circuit_6(self):
        """Get pipe_circuit_6

        Returns:
            str: the value of `pipe_circuit_6` or None if not set
        """
        return self._data["Pipe Circuit 6"]

    @pipe_circuit_6.setter
    def pipe_circuit_6(self, value=None):
        """  Corresponds to IDD Field `pipe_circuit_6`
        optional
        Name of a pipe circuit to be simulated in this domain

        Args:
            value (str): value for IDD Field `pipe_circuit_6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_circuit_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_circuit_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_circuit_6`')

        self._data["Pipe Circuit 6"] = value

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

class PipingSystemUndergroundPipeCircuit(object):
    """ Corresponds to IDD object `PipingSystem:Underground:PipeCircuit`
        The pipe circuit object in an underground piping system.
        This object is simulated within an underground piping domain object
        and connected on a branch on a plant loop.
    
    """
    internal_name = "PipingSystem:Underground:PipeCircuit"
    field_count = 20
    required_fields = ["Name", "Pipe Thermal Conductivity", "Pipe Density", "Pipe Specific Heat", "Pipe Inner Diameter", "Pipe Outer Diameter", "Design Flow Rate", "Circuit Inlet Node", "Circuit Outlet Node", "Radial Thickness of Inner Radial Near Pipe Mesh Region", "Number of Pipe Segments Entered for this Pipe Circuit", "Pipe Segment 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PipingSystem:Underground:PipeCircuit`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Pipe Thermal Conductivity"] = None
        self._data["Pipe Density"] = None
        self._data["Pipe Specific Heat"] = None
        self._data["Pipe Inner Diameter"] = None
        self._data["Pipe Outer Diameter"] = None
        self._data["Design Flow Rate"] = None
        self._data["Circuit Inlet Node"] = None
        self._data["Circuit Outlet Node"] = None
        self._data["Convergence Criterion for the Inner Radial Iteration Loop"] = None
        self._data["Maximum Iterations in the Inner Radial Iteration Loop"] = None
        self._data["Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region"] = None
        self._data["Radial Thickness of Inner Radial Near Pipe Mesh Region"] = None
        self._data["Number of Pipe Segments Entered for this Pipe Circuit"] = None
        self._data["Pipe Segment 1"] = None
        self._data["Pipe Segment 2"] = None
        self._data["Pipe Segment 3"] = None
        self._data["Pipe Segment 4"] = None
        self._data["Pipe Segment 5"] = None
        self._data["Pipe Segment 6"] = None
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
            self.pipe_thermal_conductivity = None
        else:
            self.pipe_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_density = None
        else:
            self.pipe_density = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_specific_heat = None
        else:
            self.pipe_specific_heat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_inner_diameter = None
        else:
            self.pipe_inner_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_outer_diameter = None
        else:
            self.pipe_outer_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.circuit_inlet_node = None
        else:
            self.circuit_inlet_node = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.circuit_outlet_node = None
        else:
            self.circuit_outlet_node = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_criterion_for_the_inner_radial_iteration_loop = None
        else:
            self.convergence_criterion_for_the_inner_radial_iteration_loop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_iterations_in_the_inner_radial_iteration_loop = None
        else:
            self.maximum_iterations_in_the_inner_radial_iteration_loop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region = None
        else:
            self.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.radial_thickness_of_inner_radial_near_pipe_mesh_region = None
        else:
            self.radial_thickness_of_inner_radial_near_pipe_mesh_region = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_pipe_segments_entered_for_this_pipe_circuit = None
        else:
            self.number_of_pipe_segments_entered_for_this_pipe_circuit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_segment_1 = None
        else:
            self.pipe_segment_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_segment_2 = None
        else:
            self.pipe_segment_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_segment_3 = None
        else:
            self.pipe_segment_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_segment_4 = None
        else:
            self.pipe_segment_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_segment_5 = None
        else:
            self.pipe_segment_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_segment_6 = None
        else:
            self.pipe_segment_6 = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def pipe_thermal_conductivity(self):
        """Get pipe_thermal_conductivity

        Returns:
            float: the value of `pipe_thermal_conductivity` or None if not set
        """
        return self._data["Pipe Thermal Conductivity"]

    @pipe_thermal_conductivity.setter
    def pipe_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `pipe_thermal_conductivity`

        Args:
            value (float): value for IDD Field `pipe_thermal_conductivity`
                Units: W/m-K
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
                                 'for field `pipe_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_thermal_conductivity`')

        self._data["Pipe Thermal Conductivity"] = value

    @property
    def pipe_density(self):
        """Get pipe_density

        Returns:
            float: the value of `pipe_density` or None if not set
        """
        return self._data["Pipe Density"]

    @pipe_density.setter
    def pipe_density(self, value=None):
        """  Corresponds to IDD Field `pipe_density`

        Args:
            value (float): value for IDD Field `pipe_density`
                Units: kg/m3
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
                                 'for field `pipe_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_density`')

        self._data["Pipe Density"] = value

    @property
    def pipe_specific_heat(self):
        """Get pipe_specific_heat

        Returns:
            float: the value of `pipe_specific_heat` or None if not set
        """
        return self._data["Pipe Specific Heat"]

    @pipe_specific_heat.setter
    def pipe_specific_heat(self, value=None):
        """  Corresponds to IDD Field `pipe_specific_heat`

        Args:
            value (float): value for IDD Field `pipe_specific_heat`
                Units: J/kg-K
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
                                 'for field `pipe_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_specific_heat`')

        self._data["Pipe Specific Heat"] = value

    @property
    def pipe_inner_diameter(self):
        """Get pipe_inner_diameter

        Returns:
            float: the value of `pipe_inner_diameter` or None if not set
        """
        return self._data["Pipe Inner Diameter"]

    @pipe_inner_diameter.setter
    def pipe_inner_diameter(self, value=None):
        """  Corresponds to IDD Field `pipe_inner_diameter`

        Args:
            value (float): value for IDD Field `pipe_inner_diameter`
                Units: m
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
                                 'for field `pipe_inner_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_inner_diameter`')

        self._data["Pipe Inner Diameter"] = value

    @property
    def pipe_outer_diameter(self):
        """Get pipe_outer_diameter

        Returns:
            float: the value of `pipe_outer_diameter` or None if not set
        """
        return self._data["Pipe Outer Diameter"]

    @pipe_outer_diameter.setter
    def pipe_outer_diameter(self, value=None):
        """  Corresponds to IDD Field `pipe_outer_diameter`

        Args:
            value (float): value for IDD Field `pipe_outer_diameter`
                Units: m
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
                                 'for field `pipe_outer_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_outer_diameter`')

        self._data["Pipe Outer Diameter"] = value

    @property
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_flow_rate`

        Args:
            value (float): value for IDD Field `design_flow_rate`
                Units: m3/s
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
                                 'for field `design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_flow_rate`')

        self._data["Design Flow Rate"] = value

    @property
    def circuit_inlet_node(self):
        """Get circuit_inlet_node

        Returns:
            str: the value of `circuit_inlet_node` or None if not set
        """
        return self._data["Circuit Inlet Node"]

    @circuit_inlet_node.setter
    def circuit_inlet_node(self, value=None):
        """  Corresponds to IDD Field `circuit_inlet_node`

        Args:
            value (str): value for IDD Field `circuit_inlet_node`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `circuit_inlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `circuit_inlet_node`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `circuit_inlet_node`')

        self._data["Circuit Inlet Node"] = value

    @property
    def circuit_outlet_node(self):
        """Get circuit_outlet_node

        Returns:
            str: the value of `circuit_outlet_node` or None if not set
        """
        return self._data["Circuit Outlet Node"]

    @circuit_outlet_node.setter
    def circuit_outlet_node(self, value=None):
        """  Corresponds to IDD Field `circuit_outlet_node`

        Args:
            value (str): value for IDD Field `circuit_outlet_node`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `circuit_outlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `circuit_outlet_node`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `circuit_outlet_node`')

        self._data["Circuit Outlet Node"] = value

    @property
    def convergence_criterion_for_the_inner_radial_iteration_loop(self):
        """Get convergence_criterion_for_the_inner_radial_iteration_loop

        Returns:
            float: the value of `convergence_criterion_for_the_inner_radial_iteration_loop` or None if not set
        """
        return self._data["Convergence Criterion for the Inner Radial Iteration Loop"]

    @convergence_criterion_for_the_inner_radial_iteration_loop.setter
    def convergence_criterion_for_the_inner_radial_iteration_loop(self, value=0.001 ):
        """  Corresponds to IDD Field `convergence_criterion_for_the_inner_radial_iteration_loop`

        Args:
            value (float): value for IDD Field `convergence_criterion_for_the_inner_radial_iteration_loop`
                Units: deltaC
                Default value: 0.001
                value >= 1e-06
                value <= 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `convergence_criterion_for_the_inner_radial_iteration_loop`'.format(value))
            if value < 1e-06:
                raise ValueError('value need to be greater or equal 1e-06 '
                                 'for field `convergence_criterion_for_the_inner_radial_iteration_loop`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `convergence_criterion_for_the_inner_radial_iteration_loop`')

        self._data["Convergence Criterion for the Inner Radial Iteration Loop"] = value

    @property
    def maximum_iterations_in_the_inner_radial_iteration_loop(self):
        """Get maximum_iterations_in_the_inner_radial_iteration_loop

        Returns:
            int: the value of `maximum_iterations_in_the_inner_radial_iteration_loop` or None if not set
        """
        return self._data["Maximum Iterations in the Inner Radial Iteration Loop"]

    @maximum_iterations_in_the_inner_radial_iteration_loop.setter
    def maximum_iterations_in_the_inner_radial_iteration_loop(self, value=500 ):
        """  Corresponds to IDD Field `maximum_iterations_in_the_inner_radial_iteration_loop`

        Args:
            value (int): value for IDD Field `maximum_iterations_in_the_inner_radial_iteration_loop`
                Default value: 500
                value >= 3
                value <= 10000
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
                                 'for field `maximum_iterations_in_the_inner_radial_iteration_loop`'.format(value))
            if value < 3:
                raise ValueError('value need to be greater or equal 3 '
                                 'for field `maximum_iterations_in_the_inner_radial_iteration_loop`')
            if value > 10000:
                raise ValueError('value need to be smaller 10000 '
                                 'for field `maximum_iterations_in_the_inner_radial_iteration_loop`')

        self._data["Maximum Iterations in the Inner Radial Iteration Loop"] = value

    @property
    def number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region(self):
        """Get number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region

        Returns:
            int: the value of `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region` or None if not set
        """
        return self._data["Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region"]

    @number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region.setter
    def number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region(self, value=3 ):
        """  Corresponds to IDD Field `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`

        Args:
            value (int): value for IDD Field `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`
                Default value: 3
                value >= 1
                value <= 15
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
                                 'for field `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`')
            if value > 15:
                raise ValueError('value need to be smaller 15 '
                                 'for field `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`')

        self._data["Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region"] = value

    @property
    def radial_thickness_of_inner_radial_near_pipe_mesh_region(self):
        """Get radial_thickness_of_inner_radial_near_pipe_mesh_region

        Returns:
            float: the value of `radial_thickness_of_inner_radial_near_pipe_mesh_region` or None if not set
        """
        return self._data["Radial Thickness of Inner Radial Near Pipe Mesh Region"]

    @radial_thickness_of_inner_radial_near_pipe_mesh_region.setter
    def radial_thickness_of_inner_radial_near_pipe_mesh_region(self, value=None):
        """  Corresponds to IDD Field `radial_thickness_of_inner_radial_near_pipe_mesh_region`
        Required because it must be selected by user instead of being
        inferred from circuit/domain object inputs.

        Args:
            value (float): value for IDD Field `radial_thickness_of_inner_radial_near_pipe_mesh_region`
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
                                 'for field `radial_thickness_of_inner_radial_near_pipe_mesh_region`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `radial_thickness_of_inner_radial_near_pipe_mesh_region`')

        self._data["Radial Thickness of Inner Radial Near Pipe Mesh Region"] = value

    @property
    def number_of_pipe_segments_entered_for_this_pipe_circuit(self):
        """Get number_of_pipe_segments_entered_for_this_pipe_circuit

        Returns:
            int: the value of `number_of_pipe_segments_entered_for_this_pipe_circuit` or None if not set
        """
        return self._data["Number of Pipe Segments Entered for this Pipe Circuit"]

    @number_of_pipe_segments_entered_for_this_pipe_circuit.setter
    def number_of_pipe_segments_entered_for_this_pipe_circuit(self, value=None):
        """  Corresponds to IDD Field `number_of_pipe_segments_entered_for_this_pipe_circuit`

        Args:
            value (int): value for IDD Field `number_of_pipe_segments_entered_for_this_pipe_circuit`
                value >= 1
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
                                 'for field `number_of_pipe_segments_entered_for_this_pipe_circuit`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_pipe_segments_entered_for_this_pipe_circuit`')

        self._data["Number of Pipe Segments Entered for this Pipe Circuit"] = value

    @property
    def pipe_segment_1(self):
        """Get pipe_segment_1

        Returns:
            str: the value of `pipe_segment_1` or None if not set
        """
        return self._data["Pipe Segment 1"]

    @pipe_segment_1.setter
    def pipe_segment_1(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_1`
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_segment_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_segment_1`')

        self._data["Pipe Segment 1"] = value

    @property
    def pipe_segment_2(self):
        """Get pipe_segment_2

        Returns:
            str: the value of `pipe_segment_2` or None if not set
        """
        return self._data["Pipe Segment 2"]

    @pipe_segment_2.setter
    def pipe_segment_2(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_2`
        optional
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_segment_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_segment_2`')

        self._data["Pipe Segment 2"] = value

    @property
    def pipe_segment_3(self):
        """Get pipe_segment_3

        Returns:
            str: the value of `pipe_segment_3` or None if not set
        """
        return self._data["Pipe Segment 3"]

    @pipe_segment_3.setter
    def pipe_segment_3(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_3`
        optional
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_segment_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_segment_3`')

        self._data["Pipe Segment 3"] = value

    @property
    def pipe_segment_4(self):
        """Get pipe_segment_4

        Returns:
            str: the value of `pipe_segment_4` or None if not set
        """
        return self._data["Pipe Segment 4"]

    @pipe_segment_4.setter
    def pipe_segment_4(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_4`
        optional
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_segment_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_segment_4`')

        self._data["Pipe Segment 4"] = value

    @property
    def pipe_segment_5(self):
        """Get pipe_segment_5

        Returns:
            str: the value of `pipe_segment_5` or None if not set
        """
        return self._data["Pipe Segment 5"]

    @pipe_segment_5.setter
    def pipe_segment_5(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_5`
        optional
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_segment_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_segment_5`')

        self._data["Pipe Segment 5"] = value

    @property
    def pipe_segment_6(self):
        """Get pipe_segment_6

        Returns:
            str: the value of `pipe_segment_6` or None if not set
        """
        return self._data["Pipe Segment 6"]

    @pipe_segment_6.setter
    def pipe_segment_6(self, value=None):
        """  Corresponds to IDD Field `pipe_segment_6`
        optional
        Name of a pipe segment to be included in this pipe circuit

        Args:
            value (str): value for IDD Field `pipe_segment_6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pipe_segment_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pipe_segment_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pipe_segment_6`')

        self._data["Pipe Segment 6"] = value

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

class PipingSystemUndergroundPipeSegment(object):
    """ Corresponds to IDD object `PipingSystem:Underground:PipeSegment`
        The pipe segment to be used in an underground piping system
        This object represents a single pipe leg positioned axially
        in the local z-direction, at a given x, y location in the domain
    
    """
    internal_name = "PipingSystem:Underground:PipeSegment"
    field_count = 4
    required_fields = ["Name", "X Position", "Y Position", "Flow Direction"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PipingSystem:Underground:PipeSegment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["X Position"] = None
        self._data["Y Position"] = None
        self._data["Flow Direction"] = None
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
            self.x_position = None
        else:
            self.x_position = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.y_position = None
        else:
            self.y_position = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.flow_direction = None
        else:
            self.flow_direction = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def x_position(self):
        """Get x_position

        Returns:
            float: the value of `x_position` or None if not set
        """
        return self._data["X Position"]

    @x_position.setter
    def x_position(self, value=None):
        """  Corresponds to IDD Field `x_position`
        This segment will be centered at this distance from the x=0
        domain surface or the basement wall surface, based on whether
        a basement exists in this domain and the selection of the
        shift input field found in the domain object.

        Args:
            value (float): value for IDD Field `x_position`
                Units: m
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
                                 'for field `x_position`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `x_position`')

        self._data["X Position"] = value

    @property
    def y_position(self):
        """Get y_position

        Returns:
            float: the value of `y_position` or None if not set
        """
        return self._data["Y Position"]

    @y_position.setter
    def y_position(self, value=None):
        """  Corresponds to IDD Field `y_position`
        This segment will be centered at this distance away from the
        ground surface; thus this value represents the burial depth
        of this pipe segment.

        Args:
            value (float): value for IDD Field `y_position`
                Units: m
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
                                 'for field `y_position`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `y_position`')

        self._data["Y Position"] = value

    @property
    def flow_direction(self):
        """Get flow_direction

        Returns:
            str: the value of `flow_direction` or None if not set
        """
        return self._data["Flow Direction"]

    @flow_direction.setter
    def flow_direction(self, value=None):
        """  Corresponds to IDD Field `flow_direction`
        This segment will be simulated such that the flow is in the
        selected direction.  This can allow for detailed analysis
        of circuiting effects in a single domain.

        Args:
            value (str): value for IDD Field `flow_direction`
                Accepted values are:
                      - IncreasingZ
                      - DecreasingZ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `flow_direction`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `flow_direction`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `flow_direction`')
            vals = {}
            vals["increasingz"] = "IncreasingZ"
            vals["decreasingz"] = "DecreasingZ"
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
                                     'field `flow_direction`'.format(value))
            value = vals[value_lower]

        self._data["Flow Direction"] = value

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

class Duct(object):
    """ Corresponds to IDD object `Duct`
        Passes inlet node state variables to outlet node state variables
    
    """
    internal_name = "Duct"
    field_count = 3
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Duct`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

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

class PumpVariableSpeed(object):
    """ Corresponds to IDD object `Pump:VariableSpeed`
        This pump model is described in the ASHRAE secondary HVAC toolkit.
    
    """
    internal_name = "Pump:VariableSpeed"
    field_count = 25
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Pump:VariableSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Rated Flow Rate"] = None
        self._data["Rated Pump Head"] = None
        self._data["Rated Power Consumption"] = None
        self._data["Motor Efficiency"] = None
        self._data["Fraction of Motor Inefficiencies to Fluid Stream"] = None
        self._data["Coefficient 1 of the Part Load Performance Curve"] = None
        self._data["Coefficient 2 of the Part Load Performance Curve"] = None
        self._data["Coefficient 3 of the Part Load Performance Curve"] = None
        self._data["Coefficient 4 of the Part Load Performance Curve"] = None
        self._data["Minimum Flow Rate"] = None
        self._data["Pump Control Type"] = None
        self._data["Pump Flow Rate Schedule Name"] = None
        self._data["Pump Curve Name"] = None
        self._data["Impeller Diameter"] = None
        self._data["VFD Control Type"] = None
        self._data["Pump rpm Schedule Name"] = None
        self._data["Minimum Pressure Schedule"] = None
        self._data["Maximum Pressure Schedule"] = None
        self._data["Minimum RPM Schedule"] = None
        self._data["Maximum RPM Schedule"] = None
        self._data["Zone Name"] = None
        self._data["Skin Loss Radiative Fraction"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_flow_rate = None
        else:
            self.rated_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_pump_head = None
        else:
            self.rated_pump_head = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_power_consumption = None
        else:
            self.rated_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = None
        else:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_1_of_the_part_load_performance_curve = None
        else:
            self.coefficient_1_of_the_part_load_performance_curve = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_2_of_the_part_load_performance_curve = None
        else:
            self.coefficient_2_of_the_part_load_performance_curve = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_3_of_the_part_load_performance_curve = None
        else:
            self.coefficient_3_of_the_part_load_performance_curve = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_4_of_the_part_load_performance_curve = None
        else:
            self.coefficient_4_of_the_part_load_performance_curve = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_flow_rate = None
        else:
            self.minimum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_control_type = None
        else:
            self.pump_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_flow_rate_schedule_name = None
        else:
            self.pump_flow_rate_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_curve_name = None
        else:
            self.pump_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.impeller_diameter = None
        else:
            self.impeller_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vfd_control_type = None
        else:
            self.vfd_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_rpm_schedule_name = None
        else:
            self.pump_rpm_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_pressure_schedule = None
        else:
            self.minimum_pressure_schedule = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_pressure_schedule = None
        else:
            self.maximum_pressure_schedule = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_rpm_schedule = None
        else:
            self.minimum_rpm_schedule = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_rpm_schedule = None
        else:
            self.maximum_rpm_schedule = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.skin_loss_radiative_fraction = None
        else:
            self.skin_loss_radiative_fraction = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

    @property
    def rated_flow_rate(self):
        """Get rated_flow_rate

        Returns:
            float: the value of `rated_flow_rate` or None if not set
        """
        return self._data["Rated Flow Rate"]

    @rated_flow_rate.setter
    def rated_flow_rate(self, value=None):
        """  Corresponds to IDD Field `rated_flow_rate`

        Args:
            value (float): value for IDD Field `rated_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `rated_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_flow_rate`')

        self._data["Rated Flow Rate"] = value

    @property
    def rated_pump_head(self):
        """Get rated_pump_head

        Returns:
            float: the value of `rated_pump_head` or None if not set
        """
        return self._data["Rated Pump Head"]

    @rated_pump_head.setter
    def rated_pump_head(self, value=179352.0 ):
        """  Corresponds to IDD Field `rated_pump_head`
        default head is 60 feet

        Args:
            value (float): value for IDD Field `rated_pump_head`
                Units: Pa
                IP-Units: ftH2O
                Default value: 179352.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_pump_head`'.format(value))

        self._data["Rated Pump Head"] = value

    @property
    def rated_power_consumption(self):
        """Get rated_power_consumption

        Returns:
            float: the value of `rated_power_consumption` or None if not set
        """
        return self._data["Rated Power Consumption"]

    @rated_power_consumption.setter
    def rated_power_consumption(self, value=None):
        """  Corresponds to IDD Field `rated_power_consumption`
        If this field is autosized, an impeller efficiency of 0.78 is assumed.
        autosized Rated Power Consumption = Rated Flow Rate * Rated Pump Head / (0.78 * Motor Efficiency)

        Args:
            value (float): value for IDD Field `rated_power_consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_power_consumption`'.format(value))

        self._data["Rated Power Consumption"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency

        Returns:
            float: the value of `motor_efficiency` or None if not set
        """
        return self._data["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=0.9 ):
        """  Corresponds to IDD Field `motor_efficiency`
        This is the motor efficiency only. When the Rated Power Consumption if autosized,
        an impeller efficiency of 0.78 is assumed in addition to the motor efficiency.

        Args:
            value (float): value for IDD Field `motor_efficiency`
                Default value: 0.9
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
                                 'for field `motor_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `motor_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_efficiency`')

        self._data["Motor Efficiency"] = value

    @property
    def fraction_of_motor_inefficiencies_to_fluid_stream(self):
        """Get fraction_of_motor_inefficiencies_to_fluid_stream

        Returns:
            float: the value of `fraction_of_motor_inefficiencies_to_fluid_stream` or None if not set
        """
        return self._data["Fraction of Motor Inefficiencies to Fluid Stream"]

    @fraction_of_motor_inefficiencies_to_fluid_stream.setter
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_of_motor_inefficiencies_to_fluid_stream`

        Args:
            value (float): value for IDD Field `fraction_of_motor_inefficiencies_to_fluid_stream`
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
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`')

        self._data["Fraction of Motor Inefficiencies to Fluid Stream"] = value

    @property
    def coefficient_1_of_the_part_load_performance_curve(self):
        """Get coefficient_1_of_the_part_load_performance_curve

        Returns:
            float: the value of `coefficient_1_of_the_part_load_performance_curve` or None if not set
        """
        return self._data["Coefficient 1 of the Part Load Performance Curve"]

    @coefficient_1_of_the_part_load_performance_curve.setter
    def coefficient_1_of_the_part_load_performance_curve(self, value=0.0 ):
        """  Corresponds to IDD Field `coefficient_1_of_the_part_load_performance_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_the_part_load_performance_curve`
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
                                 'for field `coefficient_1_of_the_part_load_performance_curve`'.format(value))

        self._data["Coefficient 1 of the Part Load Performance Curve"] = value

    @property
    def coefficient_2_of_the_part_load_performance_curve(self):
        """Get coefficient_2_of_the_part_load_performance_curve

        Returns:
            float: the value of `coefficient_2_of_the_part_load_performance_curve` or None if not set
        """
        return self._data["Coefficient 2 of the Part Load Performance Curve"]

    @coefficient_2_of_the_part_load_performance_curve.setter
    def coefficient_2_of_the_part_load_performance_curve(self, value=1.0 ):
        """  Corresponds to IDD Field `coefficient_2_of_the_part_load_performance_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_the_part_load_performance_curve`
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_2_of_the_part_load_performance_curve`'.format(value))

        self._data["Coefficient 2 of the Part Load Performance Curve"] = value

    @property
    def coefficient_3_of_the_part_load_performance_curve(self):
        """Get coefficient_3_of_the_part_load_performance_curve

        Returns:
            float: the value of `coefficient_3_of_the_part_load_performance_curve` or None if not set
        """
        return self._data["Coefficient 3 of the Part Load Performance Curve"]

    @coefficient_3_of_the_part_load_performance_curve.setter
    def coefficient_3_of_the_part_load_performance_curve(self, value=0.0 ):
        """  Corresponds to IDD Field `coefficient_3_of_the_part_load_performance_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_the_part_load_performance_curve`
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
                                 'for field `coefficient_3_of_the_part_load_performance_curve`'.format(value))

        self._data["Coefficient 3 of the Part Load Performance Curve"] = value

    @property
    def coefficient_4_of_the_part_load_performance_curve(self):
        """Get coefficient_4_of_the_part_load_performance_curve

        Returns:
            float: the value of `coefficient_4_of_the_part_load_performance_curve` or None if not set
        """
        return self._data["Coefficient 4 of the Part Load Performance Curve"]

    @coefficient_4_of_the_part_load_performance_curve.setter
    def coefficient_4_of_the_part_load_performance_curve(self, value=0.0 ):
        """  Corresponds to IDD Field `coefficient_4_of_the_part_load_performance_curve`

        Args:
            value (float): value for IDD Field `coefficient_4_of_the_part_load_performance_curve`
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
                                 'for field `coefficient_4_of_the_part_load_performance_curve`'.format(value))

        self._data["Coefficient 4 of the Part Load Performance Curve"] = value

    @property
    def minimum_flow_rate(self):
        """Get minimum_flow_rate

        Returns:
            float: the value of `minimum_flow_rate` or None if not set
        """
        return self._data["Minimum Flow Rate"]

    @minimum_flow_rate.setter
    def minimum_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_flow_rate`
        This value can be zero and will be defaulted to that if not specified.

        Args:
            value (float): value for IDD Field `minimum_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `minimum_flow_rate`'.format(value))

        self._data["Minimum Flow Rate"] = value

    @property
    def pump_control_type(self):
        """Get pump_control_type

        Returns:
            str: the value of `pump_control_type` or None if not set
        """
        return self._data["Pump Control Type"]

    @pump_control_type.setter
    def pump_control_type(self, value="Continuous"):
        """  Corresponds to IDD Field `pump_control_type`

        Args:
            value (str): value for IDD Field `pump_control_type`
                Accepted values are:
                      - Continuous
                      - Intermittent
                Default value: Continuous
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_control_type`')
            vals = {}
            vals["continuous"] = "Continuous"
            vals["intermittent"] = "Intermittent"
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
                                     'field `pump_control_type`'.format(value))
            value = vals[value_lower]

        self._data["Pump Control Type"] = value

    @property
    def pump_flow_rate_schedule_name(self):
        """Get pump_flow_rate_schedule_name

        Returns:
            str: the value of `pump_flow_rate_schedule_name` or None if not set
        """
        return self._data["Pump Flow Rate Schedule Name"]

    @pump_flow_rate_schedule_name.setter
    def pump_flow_rate_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pump_flow_rate_schedule_name`
        Modifies the rated flow rate of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `pump_flow_rate_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_flow_rate_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_flow_rate_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_flow_rate_schedule_name`')

        self._data["Pump Flow Rate Schedule Name"] = value

    @property
    def pump_curve_name(self):
        """Get pump_curve_name

        Returns:
            str: the value of `pump_curve_name` or None if not set
        """
        return self._data["Pump Curve Name"]

    @pump_curve_name.setter
    def pump_curve_name(self, value=None):
        """  Corresponds to IDD Field `pump_curve_name`
        This references any single independent variable polynomial curve in order to
        do pressure vs. flow calculations for this pump.  The available types are then:
        Linear, Quadratic, Cubic, and Quartic
        The non-dimensional pump pressure relationship is of the following form:
        (psi = C4*phi^4 + C3*phi^3 + C2*phi^2 + C1*phi + C0)
        Where the nondimensional variables are defined as:
        delP = rho * ((N/60)^2) * (D^2) * psi
        mdot = rho * (N/60) * (D^3) * phi
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `pump_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_curve_name`')

        self._data["Pump Curve Name"] = value

    @property
    def impeller_diameter(self):
        """Get impeller_diameter

        Returns:
            float: the value of `impeller_diameter` or None if not set
        """
        return self._data["Impeller Diameter"]

    @impeller_diameter.setter
    def impeller_diameter(self, value=None):
        """  Corresponds to IDD Field `impeller_diameter`
        "D" in above expression in field A6

        Args:
            value (float): value for IDD Field `impeller_diameter`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `impeller_diameter`'.format(value))

        self._data["Impeller Diameter"] = value

    @property
    def vfd_control_type(self):
        """Get vfd_control_type

        Returns:
            str: the value of `vfd_control_type` or None if not set
        """
        return self._data["VFD Control Type"]

    @vfd_control_type.setter
    def vfd_control_type(self, value=None):
        """  Corresponds to IDD Field `vfd_control_type`

        Args:
            value (str): value for IDD Field `vfd_control_type`
                Accepted values are:
                      - ManualControl
                      - PressureSetpointControl
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `vfd_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `vfd_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `vfd_control_type`')
            vals = {}
            vals["manualcontrol"] = "ManualControl"
            vals["pressuresetpointcontrol"] = "PressureSetpointControl"
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
                                     'field `vfd_control_type`'.format(value))
            value = vals[value_lower]

        self._data["VFD Control Type"] = value

    @property
    def pump_rpm_schedule_name(self):
        """Get pump_rpm_schedule_name

        Returns:
            str: the value of `pump_rpm_schedule_name` or None if not set
        """
        return self._data["Pump rpm Schedule Name"]

    @pump_rpm_schedule_name.setter
    def pump_rpm_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pump_rpm_schedule_name`
        Modifies the rpm of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `pump_rpm_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_rpm_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_rpm_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_rpm_schedule_name`')

        self._data["Pump rpm Schedule Name"] = value

    @property
    def minimum_pressure_schedule(self):
        """Get minimum_pressure_schedule

        Returns:
            str: the value of `minimum_pressure_schedule` or None if not set
        """
        return self._data["Minimum Pressure Schedule"]

    @minimum_pressure_schedule.setter
    def minimum_pressure_schedule(self, value=None):
        """  Corresponds to IDD Field `minimum_pressure_schedule`

        Args:
            value (str): value for IDD Field `minimum_pressure_schedule`
                Units: Pa
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_pressure_schedule`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_pressure_schedule`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_pressure_schedule`')

        self._data["Minimum Pressure Schedule"] = value

    @property
    def maximum_pressure_schedule(self):
        """Get maximum_pressure_schedule

        Returns:
            str: the value of `maximum_pressure_schedule` or None if not set
        """
        return self._data["Maximum Pressure Schedule"]

    @maximum_pressure_schedule.setter
    def maximum_pressure_schedule(self, value=None):
        """  Corresponds to IDD Field `maximum_pressure_schedule`

        Args:
            value (str): value for IDD Field `maximum_pressure_schedule`
                Units: Pa
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_pressure_schedule`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_pressure_schedule`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `maximum_pressure_schedule`')

        self._data["Maximum Pressure Schedule"] = value

    @property
    def minimum_rpm_schedule(self):
        """Get minimum_rpm_schedule

        Returns:
            str: the value of `minimum_rpm_schedule` or None if not set
        """
        return self._data["Minimum RPM Schedule"]

    @minimum_rpm_schedule.setter
    def minimum_rpm_schedule(self, value=None):
        """  Corresponds to IDD Field `minimum_rpm_schedule`

        Args:
            value (str): value for IDD Field `minimum_rpm_schedule`
                Units: Rotations Per Minute
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_rpm_schedule`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_rpm_schedule`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_rpm_schedule`')

        self._data["Minimum RPM Schedule"] = value

    @property
    def maximum_rpm_schedule(self):
        """Get maximum_rpm_schedule

        Returns:
            str: the value of `maximum_rpm_schedule` or None if not set
        """
        return self._data["Maximum RPM Schedule"]

    @maximum_rpm_schedule.setter
    def maximum_rpm_schedule(self, value=None):
        """  Corresponds to IDD Field `maximum_rpm_schedule`

        Args:
            value (str): value for IDD Field `maximum_rpm_schedule`
                Units: Rotations Per Minute
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `maximum_rpm_schedule`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_rpm_schedule`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `maximum_rpm_schedule`')

        self._data["Maximum RPM Schedule"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        optional, if used pump losses transfered to zone as internal gains

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def skin_loss_radiative_fraction(self):
        """Get skin_loss_radiative_fraction

        Returns:
            float: the value of `skin_loss_radiative_fraction` or None if not set
        """
        return self._data["Skin Loss Radiative Fraction"]

    @skin_loss_radiative_fraction.setter
    def skin_loss_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `skin_loss_radiative_fraction`
        optional. If zone identified in previous field then this determines
        the split between convection and radiation for the skin losses

        Args:
            value (float): value for IDD Field `skin_loss_radiative_fraction`
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
                                 'for field `skin_loss_radiative_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `skin_loss_radiative_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `skin_loss_radiative_fraction`')

        self._data["Skin Loss Radiative Fraction"] = value

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

class PumpConstantSpeed(object):
    """ Corresponds to IDD object `Pump:ConstantSpeed`
        This pump model is described in the ASHRAE secondary HVAC toolkit.
    
    """
    internal_name = "Pump:ConstantSpeed"
    field_count = 15
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Pump:ConstantSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Rated Flow Rate"] = None
        self._data["Rated Pump Head"] = None
        self._data["Rated Power Consumption"] = None
        self._data["Motor Efficiency"] = None
        self._data["Fraction of Motor Inefficiencies to Fluid Stream"] = None
        self._data["Pump Control Type"] = None
        self._data["Pump Flow Rate Schedule Name"] = None
        self._data["Pump Curve Name"] = None
        self._data["Impeller Diameter"] = None
        self._data["Rotational Speed"] = None
        self._data["Zone Name"] = None
        self._data["Skin Loss Radiative Fraction"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_flow_rate = None
        else:
            self.rated_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_pump_head = None
        else:
            self.rated_pump_head = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_power_consumption = None
        else:
            self.rated_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = None
        else:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_control_type = None
        else:
            self.pump_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_flow_rate_schedule_name = None
        else:
            self.pump_flow_rate_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_curve_name = None
        else:
            self.pump_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.impeller_diameter = None
        else:
            self.impeller_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rotational_speed = None
        else:
            self.rotational_speed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.skin_loss_radiative_fraction = None
        else:
            self.skin_loss_radiative_fraction = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

    @property
    def rated_flow_rate(self):
        """Get rated_flow_rate

        Returns:
            float: the value of `rated_flow_rate` or None if not set
        """
        return self._data["Rated Flow Rate"]

    @rated_flow_rate.setter
    def rated_flow_rate(self, value=None):
        """  Corresponds to IDD Field `rated_flow_rate`

        Args:
            value (float): value for IDD Field `rated_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `rated_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_flow_rate`')

        self._data["Rated Flow Rate"] = value

    @property
    def rated_pump_head(self):
        """Get rated_pump_head

        Returns:
            float: the value of `rated_pump_head` or None if not set
        """
        return self._data["Rated Pump Head"]

    @rated_pump_head.setter
    def rated_pump_head(self, value=179352.0 ):
        """  Corresponds to IDD Field `rated_pump_head`
        default head is 60 feet

        Args:
            value (float): value for IDD Field `rated_pump_head`
                Units: Pa
                IP-Units: ftH2O
                Default value: 179352.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_pump_head`'.format(value))

        self._data["Rated Pump Head"] = value

    @property
    def rated_power_consumption(self):
        """Get rated_power_consumption

        Returns:
            float: the value of `rated_power_consumption` or None if not set
        """
        return self._data["Rated Power Consumption"]

    @rated_power_consumption.setter
    def rated_power_consumption(self, value=None):
        """  Corresponds to IDD Field `rated_power_consumption`
        If this field is autosized, an impeller efficiency of 0.78 is assumed.
        autosized Rated Power Consumption = Rated Flow Rate * Rated Pump Head / (0.78 * Motor Efficiency)

        Args:
            value (float): value for IDD Field `rated_power_consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_power_consumption`'.format(value))

        self._data["Rated Power Consumption"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency

        Returns:
            float: the value of `motor_efficiency` or None if not set
        """
        return self._data["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=0.9 ):
        """  Corresponds to IDD Field `motor_efficiency`
        This is the motor efficiency only. When the Rated Power Consumption if autosized,
        an impeller efficiency of 0.78 is assumed in addition to the motor efficiency.

        Args:
            value (float): value for IDD Field `motor_efficiency`
                Default value: 0.9
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
                                 'for field `motor_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `motor_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_efficiency`')

        self._data["Motor Efficiency"] = value

    @property
    def fraction_of_motor_inefficiencies_to_fluid_stream(self):
        """Get fraction_of_motor_inefficiencies_to_fluid_stream

        Returns:
            float: the value of `fraction_of_motor_inefficiencies_to_fluid_stream` or None if not set
        """
        return self._data["Fraction of Motor Inefficiencies to Fluid Stream"]

    @fraction_of_motor_inefficiencies_to_fluid_stream.setter
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_of_motor_inefficiencies_to_fluid_stream`

        Args:
            value (float): value for IDD Field `fraction_of_motor_inefficiencies_to_fluid_stream`
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
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`')

        self._data["Fraction of Motor Inefficiencies to Fluid Stream"] = value

    @property
    def pump_control_type(self):
        """Get pump_control_type

        Returns:
            str: the value of `pump_control_type` or None if not set
        """
        return self._data["Pump Control Type"]

    @pump_control_type.setter
    def pump_control_type(self, value="Continuous"):
        """  Corresponds to IDD Field `pump_control_type`

        Args:
            value (str): value for IDD Field `pump_control_type`
                Accepted values are:
                      - Continuous
                      - Intermittent
                Default value: Continuous
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_control_type`')
            vals = {}
            vals["continuous"] = "Continuous"
            vals["intermittent"] = "Intermittent"
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
                                     'field `pump_control_type`'.format(value))
            value = vals[value_lower]

        self._data["Pump Control Type"] = value

    @property
    def pump_flow_rate_schedule_name(self):
        """Get pump_flow_rate_schedule_name

        Returns:
            str: the value of `pump_flow_rate_schedule_name` or None if not set
        """
        return self._data["Pump Flow Rate Schedule Name"]

    @pump_flow_rate_schedule_name.setter
    def pump_flow_rate_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pump_flow_rate_schedule_name`
        Modifies the rated flow rate of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `pump_flow_rate_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_flow_rate_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_flow_rate_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_flow_rate_schedule_name`')

        self._data["Pump Flow Rate Schedule Name"] = value

    @property
    def pump_curve_name(self):
        """Get pump_curve_name

        Returns:
            str: the value of `pump_curve_name` or None if not set
        """
        return self._data["Pump Curve Name"]

    @pump_curve_name.setter
    def pump_curve_name(self, value=None):
        """  Corresponds to IDD Field `pump_curve_name`
        This references any single independent variable polynomial curve in order to
        do pressure vs. flow calculations for this pump.  The available types are then:
        Linear, Quadratic, Cubic, and Quartic
        The non-dimensional pump pressure relationship is of the following form:
        (psi = C4*phi^4 + C3*phi^3 + C2*phi^2 + C1*phi + C0)
        Where the nondimensional variables are defined as:
        delP = rho * ((N/60)^2) * (D^2) * psi
        mdot = rho * (N/60) * (D^3) * phi
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `pump_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_curve_name`')

        self._data["Pump Curve Name"] = value

    @property
    def impeller_diameter(self):
        """Get impeller_diameter

        Returns:
            float: the value of `impeller_diameter` or None if not set
        """
        return self._data["Impeller Diameter"]

    @impeller_diameter.setter
    def impeller_diameter(self, value=None):
        """  Corresponds to IDD Field `impeller_diameter`
        "D" in above expression in field A6

        Args:
            value (float): value for IDD Field `impeller_diameter`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `impeller_diameter`'.format(value))

        self._data["Impeller Diameter"] = value

    @property
    def rotational_speed(self):
        """Get rotational_speed

        Returns:
            float: the value of `rotational_speed` or None if not set
        """
        return self._data["Rotational Speed"]

    @rotational_speed.setter
    def rotational_speed(self, value=None):
        """  Corresponds to IDD Field `rotational_speed`
        "N" in above expression in field A6

        Args:
            value (float): value for IDD Field `rotational_speed`
                Units: rev/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rotational_speed`'.format(value))

        self._data["Rotational Speed"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        optional, if used pump losses transfered to zone as internal gains

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def skin_loss_radiative_fraction(self):
        """Get skin_loss_radiative_fraction

        Returns:
            float: the value of `skin_loss_radiative_fraction` or None if not set
        """
        return self._data["Skin Loss Radiative Fraction"]

    @skin_loss_radiative_fraction.setter
    def skin_loss_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `skin_loss_radiative_fraction`
        optional. If zone identified in previous field then this determines
        the split between convection and radiation for the skin losses

        Args:
            value (float): value for IDD Field `skin_loss_radiative_fraction`
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
                                 'for field `skin_loss_radiative_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `skin_loss_radiative_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `skin_loss_radiative_fraction`')

        self._data["Skin Loss Radiative Fraction"] = value

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

class PumpVariableSpeedCondensate(object):
    """ Corresponds to IDD object `Pump:VariableSpeed:Condensate`
        This pump model is described in the ASHRAE secondary HVAC toolkit.
        Variable Speed Condensate pump for Steam Systems
    
    """
    internal_name = "Pump:VariableSpeed:Condensate"
    field_count = 15
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Pump:VariableSpeed:Condensate`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Rated Flow Rate"] = None
        self._data["Rated Pump Head"] = None
        self._data["Rated Power Consumption"] = None
        self._data["Motor Efficiency"] = None
        self._data["Fraction of Motor Inefficiencies to Fluid Stream"] = None
        self._data["Coefficient 1 of the Part Load Performance Curve"] = None
        self._data["Coefficient 2 of the Part Load Performance Curve"] = None
        self._data["Coefficient 3 of the Part Load Performance Curve"] = None
        self._data["Coefficient 4 of the Part Load Performance Curve"] = None
        self._data["Pump Flow Rate Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Skin Loss Radiative Fraction"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_flow_rate = None
        else:
            self.rated_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_pump_head = None
        else:
            self.rated_pump_head = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_power_consumption = None
        else:
            self.rated_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = None
        else:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_1_of_the_part_load_performance_curve = None
        else:
            self.coefficient_1_of_the_part_load_performance_curve = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_2_of_the_part_load_performance_curve = None
        else:
            self.coefficient_2_of_the_part_load_performance_curve = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_3_of_the_part_load_performance_curve = None
        else:
            self.coefficient_3_of_the_part_load_performance_curve = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_4_of_the_part_load_performance_curve = None
        else:
            self.coefficient_4_of_the_part_load_performance_curve = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_flow_rate_schedule_name = None
        else:
            self.pump_flow_rate_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.skin_loss_radiative_fraction = None
        else:
            self.skin_loss_radiative_fraction = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

    @property
    def rated_flow_rate(self):
        """Get rated_flow_rate

        Returns:
            float: the value of `rated_flow_rate` or None if not set
        """
        return self._data["Rated Flow Rate"]

    @rated_flow_rate.setter
    def rated_flow_rate(self, value=None):
        """  Corresponds to IDD Field `rated_flow_rate`

        Args:
            value (float): value for IDD Field `rated_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `rated_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_flow_rate`')

        self._data["Rated Flow Rate"] = value

    @property
    def rated_pump_head(self):
        """Get rated_pump_head

        Returns:
            float: the value of `rated_pump_head` or None if not set
        """
        return self._data["Rated Pump Head"]

    @rated_pump_head.setter
    def rated_pump_head(self, value=179352.0 ):
        """  Corresponds to IDD Field `rated_pump_head`
        default head is 60 feet

        Args:
            value (float): value for IDD Field `rated_pump_head`
                Units: Pa
                IP-Units: ftH2O
                Default value: 179352.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_pump_head`'.format(value))

        self._data["Rated Pump Head"] = value

    @property
    def rated_power_consumption(self):
        """Get rated_power_consumption

        Returns:
            float: the value of `rated_power_consumption` or None if not set
        """
        return self._data["Rated Power Consumption"]

    @rated_power_consumption.setter
    def rated_power_consumption(self, value=None):
        """  Corresponds to IDD Field `rated_power_consumption`
        If this field is autosized, an impeller efficiency of 0.78 is assumed.
        autosized Rated Power Consumption = Rated Flow Rate * Rated Pump Head / (0.78 * Motor Efficiency)

        Args:
            value (float): value for IDD Field `rated_power_consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_power_consumption`'.format(value))

        self._data["Rated Power Consumption"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency

        Returns:
            float: the value of `motor_efficiency` or None if not set
        """
        return self._data["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=0.9 ):
        """  Corresponds to IDD Field `motor_efficiency`
        This is the motor efficiency only. When the Rated Power Consumption if autosized,
        an impeller efficiency of 0.78 is assumed in addition to the motor efficiency.

        Args:
            value (float): value for IDD Field `motor_efficiency`
                Default value: 0.9
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
                                 'for field `motor_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `motor_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_efficiency`')

        self._data["Motor Efficiency"] = value

    @property
    def fraction_of_motor_inefficiencies_to_fluid_stream(self):
        """Get fraction_of_motor_inefficiencies_to_fluid_stream

        Returns:
            float: the value of `fraction_of_motor_inefficiencies_to_fluid_stream` or None if not set
        """
        return self._data["Fraction of Motor Inefficiencies to Fluid Stream"]

    @fraction_of_motor_inefficiencies_to_fluid_stream.setter
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_of_motor_inefficiencies_to_fluid_stream`

        Args:
            value (float): value for IDD Field `fraction_of_motor_inefficiencies_to_fluid_stream`
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
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`')

        self._data["Fraction of Motor Inefficiencies to Fluid Stream"] = value

    @property
    def coefficient_1_of_the_part_load_performance_curve(self):
        """Get coefficient_1_of_the_part_load_performance_curve

        Returns:
            float: the value of `coefficient_1_of_the_part_load_performance_curve` or None if not set
        """
        return self._data["Coefficient 1 of the Part Load Performance Curve"]

    @coefficient_1_of_the_part_load_performance_curve.setter
    def coefficient_1_of_the_part_load_performance_curve(self, value=0.0 ):
        """  Corresponds to IDD Field `coefficient_1_of_the_part_load_performance_curve`

        Args:
            value (float): value for IDD Field `coefficient_1_of_the_part_load_performance_curve`
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
                                 'for field `coefficient_1_of_the_part_load_performance_curve`'.format(value))

        self._data["Coefficient 1 of the Part Load Performance Curve"] = value

    @property
    def coefficient_2_of_the_part_load_performance_curve(self):
        """Get coefficient_2_of_the_part_load_performance_curve

        Returns:
            float: the value of `coefficient_2_of_the_part_load_performance_curve` or None if not set
        """
        return self._data["Coefficient 2 of the Part Load Performance Curve"]

    @coefficient_2_of_the_part_load_performance_curve.setter
    def coefficient_2_of_the_part_load_performance_curve(self, value=1.0 ):
        """  Corresponds to IDD Field `coefficient_2_of_the_part_load_performance_curve`

        Args:
            value (float): value for IDD Field `coefficient_2_of_the_part_load_performance_curve`
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_2_of_the_part_load_performance_curve`'.format(value))

        self._data["Coefficient 2 of the Part Load Performance Curve"] = value

    @property
    def coefficient_3_of_the_part_load_performance_curve(self):
        """Get coefficient_3_of_the_part_load_performance_curve

        Returns:
            float: the value of `coefficient_3_of_the_part_load_performance_curve` or None if not set
        """
        return self._data["Coefficient 3 of the Part Load Performance Curve"]

    @coefficient_3_of_the_part_load_performance_curve.setter
    def coefficient_3_of_the_part_load_performance_curve(self, value=0.0 ):
        """  Corresponds to IDD Field `coefficient_3_of_the_part_load_performance_curve`

        Args:
            value (float): value for IDD Field `coefficient_3_of_the_part_load_performance_curve`
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
                                 'for field `coefficient_3_of_the_part_load_performance_curve`'.format(value))

        self._data["Coefficient 3 of the Part Load Performance Curve"] = value

    @property
    def coefficient_4_of_the_part_load_performance_curve(self):
        """Get coefficient_4_of_the_part_load_performance_curve

        Returns:
            float: the value of `coefficient_4_of_the_part_load_performance_curve` or None if not set
        """
        return self._data["Coefficient 4 of the Part Load Performance Curve"]

    @coefficient_4_of_the_part_load_performance_curve.setter
    def coefficient_4_of_the_part_load_performance_curve(self, value=0.0 ):
        """  Corresponds to IDD Field `coefficient_4_of_the_part_load_performance_curve`

        Args:
            value (float): value for IDD Field `coefficient_4_of_the_part_load_performance_curve`
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
                                 'for field `coefficient_4_of_the_part_load_performance_curve`'.format(value))

        self._data["Coefficient 4 of the Part Load Performance Curve"] = value

    @property
    def pump_flow_rate_schedule_name(self):
        """Get pump_flow_rate_schedule_name

        Returns:
            str: the value of `pump_flow_rate_schedule_name` or None if not set
        """
        return self._data["Pump Flow Rate Schedule Name"]

    @pump_flow_rate_schedule_name.setter
    def pump_flow_rate_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pump_flow_rate_schedule_name`
        Modifies the rated flow rate of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `pump_flow_rate_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_flow_rate_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_flow_rate_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_flow_rate_schedule_name`')

        self._data["Pump Flow Rate Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        optional, if used pump losses transfered to zone as internal gains

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def skin_loss_radiative_fraction(self):
        """Get skin_loss_radiative_fraction

        Returns:
            float: the value of `skin_loss_radiative_fraction` or None if not set
        """
        return self._data["Skin Loss Radiative Fraction"]

    @skin_loss_radiative_fraction.setter
    def skin_loss_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `skin_loss_radiative_fraction`
        optional. If zone identified in previous field then this determines
        the split between convection and radiation for the skin losses

        Args:
            value (float): value for IDD Field `skin_loss_radiative_fraction`
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
                                 'for field `skin_loss_radiative_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `skin_loss_radiative_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `skin_loss_radiative_fraction`')

        self._data["Skin Loss Radiative Fraction"] = value

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

class HeaderedPumpsConstantSpeed(object):
    """ Corresponds to IDD object `HeaderedPumps:ConstantSpeed`
        This Headered pump object describes a pump bank with more than 1 pump in parallel
    
    """
    internal_name = "HeaderedPumps:ConstantSpeed"
    field_count = 14
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `HeaderedPumps:ConstantSpeed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Total Rated Flow Rate"] = None
        self._data["Number of Pumps in Bank"] = None
        self._data["Flow Sequencing Control Scheme"] = None
        self._data["Rated Pump Head"] = None
        self._data["Rated Power Consumption"] = None
        self._data["Motor Efficiency"] = None
        self._data["Fraction of Motor Inefficiencies to Fluid Stream"] = None
        self._data["Pump Control Type"] = None
        self._data["Pump Flow Rate Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Skin Loss Radiative Fraction"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_rated_flow_rate = None
        else:
            self.total_rated_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_pumps_in_bank = None
        else:
            self.number_of_pumps_in_bank = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.flow_sequencing_control_scheme = None
        else:
            self.flow_sequencing_control_scheme = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_pump_head = None
        else:
            self.rated_pump_head = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_power_consumption = None
        else:
            self.rated_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = None
        else:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_control_type = None
        else:
            self.pump_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_flow_rate_schedule_name = None
        else:
            self.pump_flow_rate_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.skin_loss_radiative_fraction = None
        else:
            self.skin_loss_radiative_fraction = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

    @property
    def total_rated_flow_rate(self):
        """Get total_rated_flow_rate

        Returns:
            float: the value of `total_rated_flow_rate` or None if not set
        """
        return self._data["Total Rated Flow Rate"]

    @total_rated_flow_rate.setter
    def total_rated_flow_rate(self, value=None):
        """  Corresponds to IDD Field `total_rated_flow_rate`
        If the field is not autosized set to the flow rate to
        the total flow when all pumps are running at full load

        Args:
            value (float): value for IDD Field `total_rated_flow_rate`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `total_rated_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `total_rated_flow_rate`')

        self._data["Total Rated Flow Rate"] = value

    @property
    def number_of_pumps_in_bank(self):
        """Get number_of_pumps_in_bank

        Returns:
            int: the value of `number_of_pumps_in_bank` or None if not set
        """
        return self._data["Number of Pumps in Bank"]

    @number_of_pumps_in_bank.setter
    def number_of_pumps_in_bank(self, value=None):
        """  Corresponds to IDD Field `number_of_pumps_in_bank`

        Args:
            value (int): value for IDD Field `number_of_pumps_in_bank`
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
                                 'for field `number_of_pumps_in_bank`'.format(value))

        self._data["Number of Pumps in Bank"] = value

    @property
    def flow_sequencing_control_scheme(self):
        """Get flow_sequencing_control_scheme

        Returns:
            str: the value of `flow_sequencing_control_scheme` or None if not set
        """
        return self._data["Flow Sequencing Control Scheme"]

    @flow_sequencing_control_scheme.setter
    def flow_sequencing_control_scheme(self, value="Sequential"):
        """  Corresponds to IDD Field `flow_sequencing_control_scheme`

        Args:
            value (str): value for IDD Field `flow_sequencing_control_scheme`
                Accepted values are:
                      - Sequential
                Default value: Sequential
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `flow_sequencing_control_scheme`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `flow_sequencing_control_scheme`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `flow_sequencing_control_scheme`')
            vals = {}
            vals["sequential"] = "Sequential"
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
                                     'field `flow_sequencing_control_scheme`'.format(value))
            value = vals[value_lower]

        self._data["Flow Sequencing Control Scheme"] = value

    @property
    def rated_pump_head(self):
        """Get rated_pump_head

        Returns:
            float: the value of `rated_pump_head` or None if not set
        """
        return self._data["Rated Pump Head"]

    @rated_pump_head.setter
    def rated_pump_head(self, value=179352.0 ):
        """  Corresponds to IDD Field `rated_pump_head`
        default head is 60 feet

        Args:
            value (float): value for IDD Field `rated_pump_head`
                Units: Pa
                IP-Units: ftH2O
                Default value: 179352.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_pump_head`'.format(value))

        self._data["Rated Pump Head"] = value

    @property
    def rated_power_consumption(self):
        """Get rated_power_consumption

        Returns:
            float: the value of `rated_power_consumption` or None if not set
        """
        return self._data["Rated Power Consumption"]

    @rated_power_consumption.setter
    def rated_power_consumption(self, value=None):
        """  Corresponds to IDD Field `rated_power_consumption`
        If the field is not autosized set to the power consumed by the pump bank
        when all the pumps are running at nominal flow
        If this field is autosized, an impeller efficiency of 0.78 is assumed.
        autosized Rated Power Consumption = Total Rated Flow Rate * Rated Pump Head / (0.78 * Motor Efficiency)

        Args:
            value (float): value for IDD Field `rated_power_consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_power_consumption`'.format(value))

        self._data["Rated Power Consumption"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency

        Returns:
            float: the value of `motor_efficiency` or None if not set
        """
        return self._data["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=0.9 ):
        """  Corresponds to IDD Field `motor_efficiency`
        This is the motor efficiency only. When the Rated Power Consumption if autosized,
        an impeller efficiency of 0.78 is assumed in addition to the motor efficiency.

        Args:
            value (float): value for IDD Field `motor_efficiency`
                Default value: 0.9
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
                                 'for field `motor_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `motor_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `motor_efficiency`')

        self._data["Motor Efficiency"] = value

    @property
    def fraction_of_motor_inefficiencies_to_fluid_stream(self):
        """Get fraction_of_motor_inefficiencies_to_fluid_stream

        Returns:
            float: the value of `fraction_of_motor_inefficiencies_to_fluid_stream` or None if not set
        """
        return self._data["Fraction of Motor Inefficiencies to Fluid Stream"]

    @fraction_of_motor_inefficiencies_to_fluid_stream.setter
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_of_motor_inefficiencies_to_fluid_stream`

        Args:
            value (float): value for IDD Field `fraction_of_motor_inefficiencies_to_fluid_stream`
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
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_motor_inefficiencies_to_fluid_stream`')

        self._data["Fraction of Motor Inefficiencies to Fluid Stream"] = value

    @property
    def pump_control_type(self):
        """Get pump_control_type

        Returns:
            str: the value of `pump_control_type` or None if not set
        """
        return self._data["Pump Control Type"]

    @pump_control_type.setter
    def pump_control_type(self, value="Continuous"):
        """  Corresponds to IDD Field `pump_control_type`

        Args:
            value (str): value for IDD Field `pump_control_type`
                Accepted values are:
                      - Continuous
                      - Intermittent
                Default value: Continuous
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_control_type`')
            vals = {}
            vals["continuous"] = "Continuous"
            vals["intermittent"] = "Intermittent"
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
                                     'field `pump_control_type`'.format(value))
            value = vals[value_lower]

        self._data["Pump Control Type"] = value

    @property
    def pump_flow_rate_schedule_name(self):
        """Get pump_flow_rate_schedule_name

        Returns:
            str: the value of `pump_flow_rate_schedule_name` or None if not set
        """
        return self._data["Pump Flow Rate Schedule Name"]

    @pump_flow_rate_schedule_name.setter
    def pump_flow_rate_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pump_flow_rate_schedule_name`
        Modifies the rated flow rate of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `pump_flow_rate_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pump_flow_rate_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_flow_rate_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_flow_rate_schedule_name`')

        self._data["Pump Flow Rate Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        optional, if used pump losses transfered to zone as internal gains

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def skin_loss_radiative_fraction(self):
        """Get skin_loss_radiative_fraction

        Returns:
            float: the value of `skin_loss_radiative_fraction` or None if not set
        """
        return self._data["Skin Loss Radiative Fraction"]

    @skin_loss_radiative_fraction.setter
    def skin_loss_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `skin_loss_radiative_fraction`
        optional. If zone identified in previous field then this determines
        the split between convection and radiation for the skin losses

        Args:
            value (float): value for IDD Field `skin_loss_radiative_fraction`
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
                                 'for field `skin_loss_radiative_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `skin_loss_radiative_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `skin_loss_radiative_fraction`')

        self._data["Skin Loss Radiative Fraction"] = value

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