from collections import OrderedDict

class Branch(object):
    """ Corresponds to IDD object `Branch`
        List components on the branch in simulation and connection order
        Note: this should NOT include splitters or mixers which define
        endpoints of branches
    """
    internal_name = "Branch"
    field_count = 58

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Branch`
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
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pressure_drop_curve_name = None
        else:
            self.pressure_drop_curve_name = vals[i]
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
            self.component_1_inlet_node_name = None
        else:
            self.component_1_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_1_outlet_node_name = None
        else:
            self.component_1_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_1_branch_control_type = None
        else:
            self.component_1_branch_control_type = vals[i]
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
            self.component_2_inlet_node_name = None
        else:
            self.component_2_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_outlet_node_name = None
        else:
            self.component_2_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_branch_control_type = None
        else:
            self.component_2_branch_control_type = vals[i]
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
            self.component_3_inlet_node_name = None
        else:
            self.component_3_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_outlet_node_name = None
        else:
            self.component_3_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_branch_control_type = None
        else:
            self.component_3_branch_control_type = vals[i]
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
            self.component_4_inlet_node_name = None
        else:
            self.component_4_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_outlet_node_name = None
        else:
            self.component_4_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_branch_control_type = None
        else:
            self.component_4_branch_control_type = vals[i]
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
            self.component_5_inlet_node_name = None
        else:
            self.component_5_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_outlet_node_name = None
        else:
            self.component_5_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_branch_control_type = None
        else:
            self.component_5_branch_control_type = vals[i]
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
            self.component_6_inlet_node_name = None
        else:
            self.component_6_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_outlet_node_name = None
        else:
            self.component_6_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_branch_control_type = None
        else:
            self.component_6_branch_control_type = vals[i]
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
            self.component_7_inlet_node_name = None
        else:
            self.component_7_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_outlet_node_name = None
        else:
            self.component_7_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_branch_control_type = None
        else:
            self.component_7_branch_control_type = vals[i]
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
            self.component_8_inlet_node_name = None
        else:
            self.component_8_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_outlet_node_name = None
        else:
            self.component_8_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_branch_control_type = None
        else:
            self.component_8_branch_control_type = vals[i]
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
            self.component_9_inlet_node_name = None
        else:
            self.component_9_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_9_outlet_node_name = None
        else:
            self.component_9_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_9_branch_control_type = None
        else:
            self.component_9_branch_control_type = vals[i]
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
            self.component_10_inlet_node_name = None
        else:
            self.component_10_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_10_outlet_node_name = None
        else:
            self.component_10_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_10_branch_control_type = None
        else:
            self.component_10_branch_control_type = vals[i]
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
            self.component_11_inlet_node_name = None
        else:
            self.component_11_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_11_outlet_node_name = None
        else:
            self.component_11_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_11_branch_control_type = None
        else:
            self.component_11_branch_control_type = vals[i]
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

        self._data["Component 11 Branch Control Type"] = value

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
        out.append(self._to_str(self.maximum_flow_rate))
        out.append(self._to_str(self.pressure_drop_curve_name))
        out.append(self._to_str(self.component_1_object_type))
        out.append(self._to_str(self.component_1_name))
        out.append(self._to_str(self.component_1_inlet_node_name))
        out.append(self._to_str(self.component_1_outlet_node_name))
        out.append(self._to_str(self.component_1_branch_control_type))
        out.append(self._to_str(self.component_2_object_type))
        out.append(self._to_str(self.component_2_name))
        out.append(self._to_str(self.component_2_inlet_node_name))
        out.append(self._to_str(self.component_2_outlet_node_name))
        out.append(self._to_str(self.component_2_branch_control_type))
        out.append(self._to_str(self.component_3_object_type))
        out.append(self._to_str(self.component_3_name))
        out.append(self._to_str(self.component_3_inlet_node_name))
        out.append(self._to_str(self.component_3_outlet_node_name))
        out.append(self._to_str(self.component_3_branch_control_type))
        out.append(self._to_str(self.component_4_object_type))
        out.append(self._to_str(self.component_4_name))
        out.append(self._to_str(self.component_4_inlet_node_name))
        out.append(self._to_str(self.component_4_outlet_node_name))
        out.append(self._to_str(self.component_4_branch_control_type))
        out.append(self._to_str(self.component_5_object_type))
        out.append(self._to_str(self.component_5_name))
        out.append(self._to_str(self.component_5_inlet_node_name))
        out.append(self._to_str(self.component_5_outlet_node_name))
        out.append(self._to_str(self.component_5_branch_control_type))
        out.append(self._to_str(self.component_6_object_type))
        out.append(self._to_str(self.component_6_name))
        out.append(self._to_str(self.component_6_inlet_node_name))
        out.append(self._to_str(self.component_6_outlet_node_name))
        out.append(self._to_str(self.component_6_branch_control_type))
        out.append(self._to_str(self.component_7_object_type))
        out.append(self._to_str(self.component_7_name))
        out.append(self._to_str(self.component_7_inlet_node_name))
        out.append(self._to_str(self.component_7_outlet_node_name))
        out.append(self._to_str(self.component_7_branch_control_type))
        out.append(self._to_str(self.component_8_object_type))
        out.append(self._to_str(self.component_8_name))
        out.append(self._to_str(self.component_8_inlet_node_name))
        out.append(self._to_str(self.component_8_outlet_node_name))
        out.append(self._to_str(self.component_8_branch_control_type))
        out.append(self._to_str(self.component_9_object_type))
        out.append(self._to_str(self.component_9_name))
        out.append(self._to_str(self.component_9_inlet_node_name))
        out.append(self._to_str(self.component_9_outlet_node_name))
        out.append(self._to_str(self.component_9_branch_control_type))
        out.append(self._to_str(self.component_10_object_type))
        out.append(self._to_str(self.component_10_name))
        out.append(self._to_str(self.component_10_inlet_node_name))
        out.append(self._to_str(self.component_10_outlet_node_name))
        out.append(self._to_str(self.component_10_branch_control_type))
        out.append(self._to_str(self.component_11_object_type))
        out.append(self._to_str(self.component_11_name))
        out.append(self._to_str(self.component_11_inlet_node_name))
        out.append(self._to_str(self.component_11_outlet_node_name))
        out.append(self._to_str(self.component_11_branch_control_type))
        return ",".join(out)