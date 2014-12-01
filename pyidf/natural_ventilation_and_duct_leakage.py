from collections import OrderedDict

class AirflowNetworkSimulationControl(object):
    """ Corresponds to IDD object `AirflowNetwork:SimulationControl`
        This object defines the global parameters used in an Airflow Network simulation.
    
    """
    internal_name = "AirflowNetwork:SimulationControl"
    field_count = 14
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:SimulationControl`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["AirflowNetwork Control"] = None
        self._data["Wind Pressure Coefficient Type"] = None
        self._data["AirflowNetwork Wind Pressure Coefficient Array Name"] = None
        self._data["Height Selection for Local Wind Pressure Calculation"] = None
        self._data["Building Type"] = None
        self._data["Maximum Number of Iterations"] = None
        self._data["Initialization Type"] = None
        self._data["Relative Airflow Convergence Tolerance"] = None
        self._data["Absolute Airflow Convergence Tolerance"] = None
        self._data["Convergence Acceleration Limit"] = None
        self._data["Azimuth Angle of Long Axis of Building"] = None
        self._data["Ratio of Building Width Along Short Axis to Width Along Long Axis"] = None
        self._data["Height Dependence of External Node Temperature"] = None
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
            self.airflownetwork_control = None
        else:
            self.airflownetwork_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_type = None
        else:
            self.wind_pressure_coefficient_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.airflownetwork_wind_pressure_coefficient_array_name = None
        else:
            self.airflownetwork_wind_pressure_coefficient_array_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_selection_for_local_wind_pressure_calculation = None
        else:
            self.height_selection_for_local_wind_pressure_calculation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.building_type = None
        else:
            self.building_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_number_of_iterations = None
        else:
            self.maximum_number_of_iterations = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initialization_type = None
        else:
            self.initialization_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relative_airflow_convergence_tolerance = None
        else:
            self.relative_airflow_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.absolute_airflow_convergence_tolerance = None
        else:
            self.absolute_airflow_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_acceleration_limit = None
        else:
            self.convergence_acceleration_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle_of_long_axis_of_building = None
        else:
            self.azimuth_angle_of_long_axis_of_building = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ratio_of_building_width_along_short_axis_to_width_along_long_axis = None
        else:
            self.ratio_of_building_width_along_short_axis_to_width_along_long_axis = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_dependence_of_external_node_temperature = None
        else:
            self.height_dependence_of_external_node_temperature = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], 'type': 'alpha', u'required-field': True, 'pytype': 'str'}

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
    def airflownetwork_control(self):
        """Get airflownetwork_control

        Returns:
            str: the value of `airflownetwork_control` or None if not set
        """
        return self._data["AirflowNetwork Control"]

    @airflownetwork_control.setter
    def airflownetwork_control(self, value="NoMultizoneOrDistribution"):
        """  Corresponds to IDD Field `AirflowNetwork Control`
        NoMultizoneOrDistribution: Only perform Simple calculations (objects ZoneInfiltration:*,
        ZoneVentilation:*, ZoneMixing, ZoneCrossMixing, ZoneRefrigerationDoorMixing,
        ZoneAirBalance:OutdoorAir, ZoneEarthtube, ZoneThermalChimney, and ZoneCoolTower:Shower);
        MultizoneWithoutDistribution: Use AirflowNetwork objects to simulate multizone
        Airflows driven by wind during simulation time,
        and objects of ZoneInfiltration:*, ZoneVentilation:*, ZoneMixing, ZoneCrossMixing
        ZoneRefrigerationDoorMixing, ZoneAirBalance:OutdoorAir, ZoneEarthtube,
        ZoneThermalChimney, and ZoneCoolTower:Shower are ignored;
        MultizoneWithDistributionOnlyDuringFanOperation: Perform distribution system
        calculations during system fan on time
        and Simple calculations during system Fan off time;
        MultizoneWithDistribution: Perform distribution system calculations during system
        fan on time and multizone Airflow driven by wind during system fan off time.
        
        {u'default': u'NoMultizoneOrDistribution', u'note': [u'NoMultizoneOrDistribution: Only perform Simple calculations (objects ZoneInfiltration:*,', u'ZoneVentilation:*, ZoneMixing, ZoneCrossMixing, ZoneRefrigerationDoorMixing,', u'ZoneAirBalance:OutdoorAir, ZoneEarthtube, ZoneThermalChimney, and ZoneCoolTower:Shower);', u'MultizoneWithoutDistribution: Use AirflowNetwork objects to simulate multizone', u'Airflows driven by wind during simulation time,', u'and objects of ZoneInfiltration:*, ZoneVentilation:*, ZoneMixing, ZoneCrossMixing', u'ZoneRefrigerationDoorMixing, ZoneAirBalance:OutdoorAir, ZoneEarthtube,', u'ZoneThermalChimney, and ZoneCoolTower:Shower are ignored;', u'MultizoneWithDistributionOnlyDuringFanOperation: Perform distribution system', u'calculations during system fan on time', u'and Simple calculations during system Fan off time;', u'MultizoneWithDistribution: Perform distribution system calculations during system', u'fan on time and multizone Airflow driven by wind during system fan off time.'], u'type': u'choice', u'key': [u'MultizoneWithDistribution', u'MultizoneWithoutDistribution', u'MultizoneWithDistributionOnlyDuringFanOperation', u'NoMultizoneOrDistribution'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `AirflowNetwork Control`
                Accepted values are:
                      - MultizoneWithDistribution
                      - MultizoneWithoutDistribution
                      - MultizoneWithDistributionOnlyDuringFanOperation
                      - NoMultizoneOrDistribution
                Default value: NoMultizoneOrDistribution
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
                                 'for field `airflownetwork_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflownetwork_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `airflownetwork_control`')
            vals = {}
            vals["multizonewithdistribution"] = "MultizoneWithDistribution"
            vals["multizonewithoutdistribution"] = "MultizoneWithoutDistribution"
            vals["multizonewithdistributiononlyduringfanoperation"] = "MultizoneWithDistributionOnlyDuringFanOperation"
            vals["nomultizoneordistribution"] = "NoMultizoneOrDistribution"
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
                                     'field `airflownetwork_control`'.format(value))
            value = vals[value_lower]
        self._data["AirflowNetwork Control"] = value

    @property
    def wind_pressure_coefficient_type(self):
        """Get wind_pressure_coefficient_type

        Returns:
            str: the value of `wind_pressure_coefficient_type` or None if not set
        """
        return self._data["Wind Pressure Coefficient Type"]

    @wind_pressure_coefficient_type.setter
    def wind_pressure_coefficient_type(self, value="SurfaceAverageCalculation"):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Type`
        Input: User must enter AirflowNetwork:MultiZone:WindPressureCoefficientArray,
        AirflowNetwork:MultiZone:ExternalNode, and
        AirflowNetwork:MultiZone:WindPressureCoefficientValues objects.
        SurfaceAverageCalculation: used only for rectangular buildings.
        If SurfaceAverageCalculation is selected,
        AirflowNetwork:MultiZone:WindPressureCoefficientArray, AirflowNetwork:MultiZone:ExternalNode,
        and AirflowNetwork:MultiZone:WindPressureCoefficientValues objects are not used.
        
        {u'default': u'SurfaceAverageCalculation', u'note': [u'Input: User must enter AirflowNetwork:MultiZone:WindPressureCoefficientArray,', u'AirflowNetwork:MultiZone:ExternalNode, and', u'AirflowNetwork:MultiZone:WindPressureCoefficientValues objects.', u'SurfaceAverageCalculation: used only for rectangular buildings.', u'If SurfaceAverageCalculation is selected,', u'AirflowNetwork:MultiZone:WindPressureCoefficientArray, AirflowNetwork:MultiZone:ExternalNode,', u'and AirflowNetwork:MultiZone:WindPressureCoefficientValues objects are not used.'], u'type': u'choice', u'key': [u'Input', u'SurfaceAverageCalculation'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Wind Pressure Coefficient Type`
                Accepted values are:
                      - Input
                      - SurfaceAverageCalculation
                Default value: SurfaceAverageCalculation
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
                                 'for field `wind_pressure_coefficient_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_pressure_coefficient_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `wind_pressure_coefficient_type`')
            vals = {}
            vals["input"] = "Input"
            vals["surfaceaveragecalculation"] = "SurfaceAverageCalculation"
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
                                     'field `wind_pressure_coefficient_type`'.format(value))
            value = vals[value_lower]
        self._data["Wind Pressure Coefficient Type"] = value

    @property
    def airflownetwork_wind_pressure_coefficient_array_name(self):
        """Get airflownetwork_wind_pressure_coefficient_array_name

        Returns:
            str: the value of `airflownetwork_wind_pressure_coefficient_array_name` or None if not set
        """
        return self._data["AirflowNetwork Wind Pressure Coefficient Array Name"]

    @airflownetwork_wind_pressure_coefficient_array_name.setter
    def airflownetwork_wind_pressure_coefficient_array_name(self, value=None):
        """  Corresponds to IDD Field `AirflowNetwork Wind Pressure Coefficient Array Name`
        Used only if Wind Pressure Coefficient Type = Input, otherwise this field may be left blank.
        
        {u'note': [u'Used only if Wind Pressure Coefficient Type = Input, otherwise this field may be left blank.'], u'type': u'object-list', u'object-list': u'WPCSetNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `AirflowNetwork Wind Pressure Coefficient Array Name`
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
                                 'for field `airflownetwork_wind_pressure_coefficient_array_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflownetwork_wind_pressure_coefficient_array_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `airflownetwork_wind_pressure_coefficient_array_name`')
        self._data["AirflowNetwork Wind Pressure Coefficient Array Name"] = value

    @property
    def height_selection_for_local_wind_pressure_calculation(self):
        """Get height_selection_for_local_wind_pressure_calculation

        Returns:
            str: the value of `height_selection_for_local_wind_pressure_calculation` or None if not set
        """
        return self._data["Height Selection for Local Wind Pressure Calculation"]

    @height_selection_for_local_wind_pressure_calculation.setter
    def height_selection_for_local_wind_pressure_calculation(self, value="OpeningHeight"):
        """  Corresponds to IDD Field `Height Selection for Local Wind Pressure Calculation`
        If ExternalNode is selected, the height given in the
        AirflowNetwork:MultiZone:ExternalNode object will be used.
        If OpeningHeight is selected, the surface opening height (centroid) will be used to
        calculate local wind pressure
        This field is ignored when the choice of the Wind Pressure Coefficient Type field is
        SurfaceAverageCalculation.
        
        {u'default': u'OpeningHeight', u'note': [u'If ExternalNode is selected, the height given in the', u'AirflowNetwork:MultiZone:ExternalNode object will be used.', u'If OpeningHeight is selected, the surface opening height (centroid) will be used to', u'calculate local wind pressure', u'This field is ignored when the choice of the Wind Pressure Coefficient Type field is', u'SurfaceAverageCalculation.'], u'type': u'choice', u'key': [u'ExternalNode', u'OpeningHeight'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Height Selection for Local Wind Pressure Calculation`
                Accepted values are:
                      - ExternalNode
                      - OpeningHeight
                Default value: OpeningHeight
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
                                 'for field `height_selection_for_local_wind_pressure_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `height_selection_for_local_wind_pressure_calculation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `height_selection_for_local_wind_pressure_calculation`')
            vals = {}
            vals["externalnode"] = "ExternalNode"
            vals["openingheight"] = "OpeningHeight"
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
                                     'field `height_selection_for_local_wind_pressure_calculation`'.format(value))
            value = vals[value_lower]
        self._data["Height Selection for Local Wind Pressure Calculation"] = value

    @property
    def building_type(self):
        """Get building_type

        Returns:
            str: the value of `building_type` or None if not set
        """
        return self._data["Building Type"]

    @building_type.setter
    def building_type(self, value="LowRise"):
        """  Corresponds to IDD Field `Building Type`
        Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation,
        otherwise this field may be left blank.
        
        {u'note': [u'Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation,', u'otherwise this field may be left blank.'], u'default': u'LowRise', u'type': u'choice', u'key': [u'LowRise', u'HighRise'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Building Type`
                Accepted values are:
                      - LowRise
                      - HighRise
                Default value: LowRise
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
                                 'for field `building_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `building_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `building_type`')
            vals = {}
            vals["lowrise"] = "LowRise"
            vals["highrise"] = "HighRise"
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
                                     'field `building_type`'.format(value))
            value = vals[value_lower]
        self._data["Building Type"] = value

    @property
    def maximum_number_of_iterations(self):
        """Get maximum_number_of_iterations

        Returns:
            int: the value of `maximum_number_of_iterations` or None if not set
        """
        return self._data["Maximum Number of Iterations"]

    @maximum_number_of_iterations.setter
    def maximum_number_of_iterations(self, value=500 ):
        """  Corresponds to IDD Field `Maximum Number of Iterations`
        Determines the maximum number of iterations used to converge on a solution. If this limit
        is exceeded, the program terminates.
        
        {'pytype': 'int', u'default': '500', u'minimum>': '10', u'maximum': '30000', u'note': [u'Determines the maximum number of iterations used to converge on a solution. If this limit', u'is exceeded, the program terminates.'], u'units': u'dimensionless', u'type': u'integer'}

        Args:
            value (int): value for IDD Field `Maximum Number of Iterations`
                Units: dimensionless
                Default value: 500
                value > 10
                value <= 30000
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `maximum_number_of_iterations`'.format(value))
            if value <= 10:
                raise ValueError('value need to be greater 10 '
                                 'for field `maximum_number_of_iterations`')
            if value > 30000:
                raise ValueError('value need to be smaller 30000 '
                                 'for field `maximum_number_of_iterations`')
        self._data["Maximum Number of Iterations"] = value

    @property
    def initialization_type(self):
        """Get initialization_type

        Returns:
            str: the value of `initialization_type` or None if not set
        """
        return self._data["Initialization Type"]

    @initialization_type.setter
    def initialization_type(self, value="ZeroNodePressures"):
        """  Corresponds to IDD Field `Initialization Type`
        
        {u'default': u'ZeroNodePressures', u'type': u'choice', u'key': [u'LinearInitializationMethod', u'ZeroNodePressures'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Initialization Type`
                Accepted values are:
                      - LinearInitializationMethod
                      - ZeroNodePressures
                Default value: ZeroNodePressures
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
                                 'for field `initialization_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `initialization_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `initialization_type`')
            vals = {}
            vals["linearinitializationmethod"] = "LinearInitializationMethod"
            vals["zeronodepressures"] = "ZeroNodePressures"
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
                                     'field `initialization_type`'.format(value))
            value = vals[value_lower]
        self._data["Initialization Type"] = value

    @property
    def relative_airflow_convergence_tolerance(self):
        """Get relative_airflow_convergence_tolerance

        Returns:
            float: the value of `relative_airflow_convergence_tolerance` or None if not set
        """
        return self._data["Relative Airflow Convergence Tolerance"]

    @relative_airflow_convergence_tolerance.setter
    def relative_airflow_convergence_tolerance(self, value=0.0001 ):
        """  Corresponds to IDD Field `Relative Airflow Convergence Tolerance`
        This tolerance is defined as the absolute value of the sum of the mass Flow Rates
        divided by the sum of the absolute value of the mass Flow Rates. The mass Flow Rates
        described here refer to the mass Flow Rates at all Nodes in the AirflowNetwork model.
        The solution converges when both this tolerance and the tolerance in the next field
        (Absolute Airflow Convergence Tolerance) are satisfied.
        
        {'pytype': 'float', u'default': '0.0001', u'minimum>': '0.0', u'note': [u'This tolerance is defined as the absolute value of the sum of the mass Flow Rates', u'divided by the sum of the absolute value of the mass Flow Rates. The mass Flow Rates', u'described here refer to the mass Flow Rates at all Nodes in the AirflowNetwork model.', u'The solution converges when both this tolerance and the tolerance in the next field', u'(Absolute Airflow Convergence Tolerance) are satisfied.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Relative Airflow Convergence Tolerance`
                Units: dimensionless
                Default value: 0.0001
                value > 0.0
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
                                 'for field `relative_airflow_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `relative_airflow_convergence_tolerance`')
        self._data["Relative Airflow Convergence Tolerance"] = value

    @property
    def absolute_airflow_convergence_tolerance(self):
        """Get absolute_airflow_convergence_tolerance

        Returns:
            float: the value of `absolute_airflow_convergence_tolerance` or None if not set
        """
        return self._data["Absolute Airflow Convergence Tolerance"]

    @absolute_airflow_convergence_tolerance.setter
    def absolute_airflow_convergence_tolerance(self, value=1e-06 ):
        """  Corresponds to IDD Field `Absolute Airflow Convergence Tolerance`
        This tolerance is defined as the absolute value of the sum of the mass flow rates. The mass
        flow rates described here refer to the mass flow rates at all nodes in the AirflowNetwork
        model. The solution converges when both this tolerance and the tolerance in the previous
        field (Relative Airflow Convergence Tolerance) are satisfied.
        
        {'pytype': 'float', u'default': '1e-06', u'minimum>': '0.0', u'note': [u'This tolerance is defined as the absolute value of the sum of the mass flow rates. The mass', u'flow rates described here refer to the mass flow rates at all nodes in the AirflowNetwork', u'model. The solution converges when both this tolerance and the tolerance in the previous', u'field (Relative Airflow Convergence Tolerance) are satisfied.'], u'units': u'kg/s', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Absolute Airflow Convergence Tolerance`
                Units: kg/s
                Default value: 1e-06
                value > 0.0
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
                                 'for field `absolute_airflow_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `absolute_airflow_convergence_tolerance`')
        self._data["Absolute Airflow Convergence Tolerance"] = value

    @property
    def convergence_acceleration_limit(self):
        """Get convergence_acceleration_limit

        Returns:
            float: the value of `convergence_acceleration_limit` or None if not set
        """
        return self._data["Convergence Acceleration Limit"]

    @convergence_acceleration_limit.setter
    def convergence_acceleration_limit(self, value=-0.5 ):
        """  Corresponds to IDD Field `Convergence Acceleration Limit`
        Used only for AirflowNetwork:SimulationControl
        
        {'pytype': 'float', u'default': '-0.5', u'maximum': '1.0', u'note': [u'Used only for AirflowNetwork:SimulationControl'], u'minimum': '-1.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Convergence Acceleration Limit`
                Units: dimensionless
                Default value: -0.5
                value >= -1.0
                value <= 1.0
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
                                 'for field `convergence_acceleration_limit`'.format(value))
            if value < -1.0:
                raise ValueError('value need to be greater or equal -1.0 '
                                 'for field `convergence_acceleration_limit`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `convergence_acceleration_limit`')
        self._data["Convergence Acceleration Limit"] = value

    @property
    def azimuth_angle_of_long_axis_of_building(self):
        """Get azimuth_angle_of_long_axis_of_building

        Returns:
            float: the value of `azimuth_angle_of_long_axis_of_building` or None if not set
        """
        return self._data["Azimuth Angle of Long Axis of Building"]

    @azimuth_angle_of_long_axis_of_building.setter
    def azimuth_angle_of_long_axis_of_building(self, value=0.0 ):
        """  Corresponds to IDD Field `Azimuth Angle of Long Axis of Building`
        Degrees clockwise from true North.
        Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '180.0', u'note': [u'Degrees clockwise from true North.', u'Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Azimuth Angle of Long Axis of Building`
                Units: deg
                Default value: 0.0
                value >= 0.0
                value <= 180.0
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
                                 'for field `azimuth_angle_of_long_axis_of_building`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `azimuth_angle_of_long_axis_of_building`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `azimuth_angle_of_long_axis_of_building`')
        self._data["Azimuth Angle of Long Axis of Building"] = value

    @property
    def ratio_of_building_width_along_short_axis_to_width_along_long_axis(self):
        """Get ratio_of_building_width_along_short_axis_to_width_along_long_axis

        Returns:
            float: the value of `ratio_of_building_width_along_short_axis_to_width_along_long_axis` or None if not set
        """
        return self._data["Ratio of Building Width Along Short Axis to Width Along Long Axis"]

    @ratio_of_building_width_along_short_axis_to_width_along_long_axis.setter
    def ratio_of_building_width_along_short_axis_to_width_along_long_axis(self, value=1.0 ):
        """  Corresponds to IDD Field `Ratio of Building Width Along Short Axis to Width Along Long Axis`
        Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation.
        
        {'pytype': 'float', u'default': '1.0', u'minimum>': '0.0', u'maximum': '1.0', u'note': [u'Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation.'], u'type': u'real'}

        Args:
            value (float): value for IDD Field `Ratio of Building Width Along Short Axis to Width Along Long Axis`
                Default value: 1.0
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `ratio_of_building_width_along_short_axis_to_width_along_long_axis`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ratio_of_building_width_along_short_axis_to_width_along_long_axis`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ratio_of_building_width_along_short_axis_to_width_along_long_axis`')
        self._data["Ratio of Building Width Along Short Axis to Width Along Long Axis"] = value

    @property
    def height_dependence_of_external_node_temperature(self):
        """Get height_dependence_of_external_node_temperature

        Returns:
            str: the value of `height_dependence_of_external_node_temperature` or None if not set
        """
        return self._data["Height Dependence of External Node Temperature"]

    @height_dependence_of_external_node_temperature.setter
    def height_dependence_of_external_node_temperature(self, value="No"):
        """  Corresponds to IDD Field `Height Dependence of External Node Temperature`
        If Yes, external node temperature is height dependent.
        If No, external node temperature is based on zero height.
        
        {u'note': [u'If Yes, external node temperature is height dependent.', u'If No, external node temperature is based on zero height.'], u'default': u'No', u'type': u'choice', u'key': [u'Yes', u'No'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Height Dependence of External Node Temperature`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `height_dependence_of_external_node_temperature`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `height_dependence_of_external_node_temperature`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `height_dependence_of_external_node_temperature`')
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
                                     'field `height_dependence_of_external_node_temperature`'.format(value))
            value = vals[value_lower]
        self._data["Height Dependence of External Node Temperature"] = value

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

class AirflowNetworkMultiZoneZone(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Zone`
        This object is used to simultaneously control a thermal zone's window and door openings,
        both exterior and interior.
    
    """
    internal_name = "AirflowNetwork:MultiZone:Zone"
    field_count = 11
    required_fields = ["Zone Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:Zone`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Ventilation Control Mode"] = None
        self._data["Ventilation Control Zone Temperature Setpoint Schedule Name"] = None
        self._data["Minimum Venting Open Factor"] = None
        self._data["Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor"] = None
        self._data["Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor"] = None
        self._data["Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor"] = None
        self._data["Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor"] = None
        self._data["Venting Availability Schedule Name"] = None
        self._data["Single Sided Wind Pressure Coefficient Algorithm"] = None
        self._data["Facade Width"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ventilation_control_mode = None
        else:
            self.ventilation_control_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ventilation_control_zone_temperature_setpoint_schedule_name = None
        else:
            self.ventilation_control_zone_temperature_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_venting_open_factor = None
        else:
            self.minimum_venting_open_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor = None
        else:
            self.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor = None
        else:
            self.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = None
        else:
            self.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor = None
        else:
            self.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.venting_availability_schedule_name = None
        else:
            self.venting_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.single_sided_wind_pressure_coefficient_algorithm = None
        else:
            self.single_sided_wind_pressure_coefficient_algorithm = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.facade_width = None
        else:
            self.facade_width = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Enter the zone name where ventilation control is required.
        
        {u'note': [u'Enter the zone name where ventilation control is required.'], u'type': u'object-list', u'object-list': u'ZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def ventilation_control_mode(self):
        """Get ventilation_control_mode

        Returns:
            str: the value of `ventilation_control_mode` or None if not set
        """
        return self._data["Ventilation Control Mode"]

    @ventilation_control_mode.setter
    def ventilation_control_mode(self, value="NoVent"):
        """  Corresponds to IDD Field `Ventilation Control Mode`
        When Ventilation Control Mode = Temperature or Enthalpy, the following
        fields are used to modulate the Ventilation Open Factor for all
        window and door openings in the zone according to the zone's
        indoor-outdoor temperature or enthalpy difference.
        Constant: controlled by field Venting Schedule Name.
        NoVent: control will not open window or door during simulation (Ventilation Open Factor = 0).
        
        {u'default': u'NoVent', u'note': [u'When Ventilation Control Mode = Temperature or Enthalpy, the following', u'fields are used to modulate the Ventilation Open Factor for all', u"window and door openings in the zone according to the zone's", u'indoor-outdoor temperature or enthalpy difference.', u'Constant: controlled by field Venting Schedule Name.', u'NoVent: control will not open window or door during simulation (Ventilation Open Factor = 0).'], u'type': u'choice', u'key': [u'Temperature', u'Enthalpy', u'Constant', u'ASHRAE55Adaptive', u'CEN15251Adaptive', u'NoVent'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Ventilation Control Mode`
                Accepted values are:
                      - Temperature
                      - Enthalpy
                      - Constant
                      - ASHRAE55Adaptive
                      - CEN15251Adaptive
                      - NoVent
                Default value: NoVent
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
                                 'for field `ventilation_control_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ventilation_control_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ventilation_control_mode`')
            vals = {}
            vals["temperature"] = "Temperature"
            vals["enthalpy"] = "Enthalpy"
            vals["constant"] = "Constant"
            vals["ashrae55adaptive"] = "ASHRAE55Adaptive"
            vals["cen15251adaptive"] = "CEN15251Adaptive"
            vals["novent"] = "NoVent"
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
                                     'field `ventilation_control_mode`'.format(value))
            value = vals[value_lower]
        self._data["Ventilation Control Mode"] = value

    @property
    def ventilation_control_zone_temperature_setpoint_schedule_name(self):
        """Get ventilation_control_zone_temperature_setpoint_schedule_name

        Returns:
            str: the value of `ventilation_control_zone_temperature_setpoint_schedule_name` or None if not set
        """
        return self._data["Ventilation Control Zone Temperature Setpoint Schedule Name"]

    @ventilation_control_zone_temperature_setpoint_schedule_name.setter
    def ventilation_control_zone_temperature_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Ventilation Control Zone Temperature Setpoint Schedule Name`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.
        
        {u'note': [u'Used only if Ventilation Control Mode = Temperature or Enthalpy.'], u'type': u'object-list', u'object-list': u'ScheduleNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Ventilation Control Zone Temperature Setpoint Schedule Name`
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
                                 'for field `ventilation_control_zone_temperature_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ventilation_control_zone_temperature_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ventilation_control_zone_temperature_setpoint_schedule_name`')
        self._data["Ventilation Control Zone Temperature Setpoint Schedule Name"] = value

    @property
    def minimum_venting_open_factor(self):
        """Get minimum_venting_open_factor

        Returns:
            float: the value of `minimum_venting_open_factor` or None if not set
        """
        return self._data["Minimum Venting Open Factor"]

    @minimum_venting_open_factor.setter
    def minimum_venting_open_factor(self, value=0.0 ):
        """  Corresponds to IDD Field `Minimum Venting Open Factor`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'Used only if Ventilation Control Mode = Temperature or Enthalpy.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Minimum Venting Open Factor`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_venting_open_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_venting_open_factor`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_venting_open_factor`')
        self._data["Minimum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor(self):
        """Get indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor

        Returns:
            float: the value of `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor` or None if not set
        """
        return self._data["Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor"]

    @indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor.setter
    def indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor(self, value=0.0 ):
        """  Corresponds to IDD Field `Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor`
        Applicable only if Ventilation Control Mode = Temperature.
        This value must be less than the corresponding upper value (next field).
        
        {'pytype': 'float', u'default': '0.0', u'maximum<': '100.0', u'note': [u'Applicable only if Ventilation Control Mode = Temperature.', u'This value must be less than the corresponding upper value (next field).'], u'minimum': '0.0', u'units': u'deltaC', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor`
                Units: deltaC
                Default value: 0.0
                value >= 0.0
                value < 100.0
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
                                 'for field `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor`')
            if value >= 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor`')
        self._data["Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor(self):
        """Get indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor

        Returns:
            float: the value of `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor` or None if not set
        """
        return self._data["Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor"]

    @indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor.setter
    def indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor(self, value=100.0 ):
        """  Corresponds to IDD Field `Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor`
        Applicable only if Ventilation Control Mode = Temperature.
        This value must be greater than the corresponding lower value (previous field).
        
        {'pytype': 'float', u'default': '100.0', u'minimum>': '0.0', u'note': [u'Applicable only if Ventilation Control Mode = Temperature.', u'This value must be greater than the corresponding lower value (previous field).'], u'units': u'deltaC', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor`
                Units: deltaC
                Default value: 100.0
                value > 0.0
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
                                 'for field `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor`')
        self._data["Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor(self):
        """Get indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor

        Returns:
            float: the value of `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor` or None if not set
        """
        return self._data["Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor"]

    @indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor.setter
    def indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor(self, value=0.0 ):
        """  Corresponds to IDD Field `Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be less than the corresponding upper value (next field).
        
        {'pytype': 'float', u'default': '0.0', u'maximum<': '300000.0', u'note': [u'Applicable only if Ventilation Control Mode = Enthalpy.', u'This value must be less than the corresponding upper value (next field).'], u'minimum': '0.0', u'units': u'deltaJ/kg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor`
                Units: deltaJ/kg
                Default value: 0.0
                value >= 0.0
                value < 300000.0
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
                                 'for field `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor`')
            if value >= 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor`')
        self._data["Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor(self):
        """Get indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor

        Returns:
            float: the value of `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor` or None if not set
        """
        return self._data["Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor"]

    @indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor.setter
    def indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor(self, value=300000.0 ):
        """  Corresponds to IDD Field `Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be greater than the corresponding lower value (previous field).
        
        {'pytype': 'float', u'default': '300000.0', u'minimum>': '0.0', u'note': [u'Applicable only if Ventilation Control Mode = Enthalpy.', u'This value must be greater than the corresponding lower value (previous field).'], u'units': u'deltaJ/kg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor`
                Units: deltaJ/kg
                Default value: 300000.0
                value > 0.0
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
                                 'for field `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor`')
        self._data["Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor"] = value

    @property
    def venting_availability_schedule_name(self):
        """Get venting_availability_schedule_name

        Returns:
            str: the value of `venting_availability_schedule_name` or None if not set
        """
        return self._data["Venting Availability Schedule Name"]

    @venting_availability_schedule_name.setter
    def venting_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Venting Availability Schedule Name`
        Non-zero Schedule value means venting is allowed if other venting control conditions are
        satisfied. A zero (or negative) Schedule value means venting is not allowed under any
        The Schedule values should be greater than or equal to 0 and less than or equal to 1.
        circumstances. If this Schedule is not specified then venting is allowed if
        other venting control conditions are satisfied.
        Not used if Ventilation Control Mode = NoVent.
        
        {u'note': [u'Non-zero Schedule value means venting is allowed if other venting control conditions are', u'satisfied. A zero (or negative) Schedule value means venting is not allowed under any', u'The Schedule values should be greater than or equal to 0 and less than or equal to 1.', u'circumstances. If this Schedule is not specified then venting is allowed if', u'other venting control conditions are satisfied.', u'Not used if Ventilation Control Mode = NoVent.'], u'type': u'object-list', u'object-list': u'ScheduleNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Venting Availability Schedule Name`
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
                                 'for field `venting_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `venting_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `venting_availability_schedule_name`')
        self._data["Venting Availability Schedule Name"] = value

    @property
    def single_sided_wind_pressure_coefficient_algorithm(self):
        """Get single_sided_wind_pressure_coefficient_algorithm

        Returns:
            str: the value of `single_sided_wind_pressure_coefficient_algorithm` or None if not set
        """
        return self._data["Single Sided Wind Pressure Coefficient Algorithm"]

    @single_sided_wind_pressure_coefficient_algorithm.setter
    def single_sided_wind_pressure_coefficient_algorithm(self, value="Standard"):
        """  Corresponds to IDD Field `Single Sided Wind Pressure Coefficient Algorithm`
        Selecting Advanced results in EnergyPlus calculating modified Wind Pressure Coefficients
        to account for wind direction and turbulence effects on single sided ventilation rates.
        Model is only valid for zones with 2 openings, both of which are on a single facade.
        
        {u'default': u'Standard', u'note': [u'Selecting Advanced results in EnergyPlus calculating modified Wind Pressure Coefficients', u'to account for wind direction and turbulence effects on single sided ventilation rates.', u'Model is only valid for zones with 2 openings, both of which are on a single facade.'], u'type': u'choice', u'key': [u'Advanced', u'Standard'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Single Sided Wind Pressure Coefficient Algorithm`
                Accepted values are:
                      - Advanced
                      - Standard
                Default value: Standard
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
                                 'for field `single_sided_wind_pressure_coefficient_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `single_sided_wind_pressure_coefficient_algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `single_sided_wind_pressure_coefficient_algorithm`')
            vals = {}
            vals["advanced"] = "Advanced"
            vals["standard"] = "Standard"
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
                                     'field `single_sided_wind_pressure_coefficient_algorithm`'.format(value))
            value = vals[value_lower]
        self._data["Single Sided Wind Pressure Coefficient Algorithm"] = value

    @property
    def facade_width(self):
        """Get facade_width

        Returns:
            float: the value of `facade_width` or None if not set
        """
        return self._data["Facade Width"]

    @facade_width.setter
    def facade_width(self, value=10.0 ):
        """  Corresponds to IDD Field `Facade Width`
        This is the whole building width along the direction of the facade of this zone.
        
        {'pytype': 'float', u'default': '10.0', u'note': [u'This is the whole building width along the direction of the facade of this zone.'], u'minimum': '0.0', u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Facade Width`
                Units: m
                Default value: 10.0
                value >= 0.0
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
                                 'for field `facade_width`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `facade_width`')
        self._data["Facade Width"] = value

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

class AirflowNetworkMultiZoneSurface(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Surface`
        This object specifies the properties of a surface linkage through which air flows.
        Airflow Report: Node 1 as an inside face zone;
        Node 2 as an outside face zone or external node.
    
    """
    internal_name = "AirflowNetwork:MultiZone:Surface"
    field_count = 12
    required_fields = ["Surface Name", "Leakage Component Name", "Window/Door Opening Factor, or Crack Factor"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:Surface`
        """
        self._data = OrderedDict()
        self._data["Surface Name"] = None
        self._data["Leakage Component Name"] = None
        self._data["External Node Name"] = None
        self._data["Window/Door Opening Factor, or Crack Factor"] = None
        self._data["Ventilation Control Mode"] = None
        self._data["Ventilation Control Zone Temperature Setpoint Schedule Name"] = None
        self._data["Minimum Venting Open Factor"] = None
        self._data["Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor"] = None
        self._data["Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor"] = None
        self._data["Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor"] = None
        self._data["Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor"] = None
        self._data["Venting Availability Schedule Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.leakage_component_name = None
        else:
            self.leakage_component_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.external_node_name = None
        else:
            self.external_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.window_or_door_opening_factor_or_crack_factor = None
        else:
            self.window_or_door_opening_factor_or_crack_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ventilation_control_mode = None
        else:
            self.ventilation_control_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ventilation_control_zone_temperature_setpoint_schedule_name = None
        else:
            self.ventilation_control_zone_temperature_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_venting_open_factor = None
        else:
            self.minimum_venting_open_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor = None
        else:
            self.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor = None
        else:
            self.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = None
        else:
            self.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor = None
        else:
            self.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.venting_availability_schedule_name = None
        else:
            self.venting_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name`
        Enter the name of a heat transfer surface.
        
        {u'note': [u'Enter the name of a heat transfer surface.'], u'type': u'object-list', u'object-list': u'SurfAndSubSurfNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name`')
        self._data["Surface Name"] = value

    @property
    def leakage_component_name(self):
        """Get leakage_component_name

        Returns:
            str: the value of `leakage_component_name` or None if not set
        """
        return self._data["Leakage Component Name"]

    @leakage_component_name.setter
    def leakage_component_name(self, value=None):
        """  Corresponds to IDD Field `Leakage Component Name`
        Enter the name of an Airflow Network leakage component. A leakage component is
        one of the following AirflowNetwork:Multizone objects:
        AirflowNetwork:MultiZone:Component:DetailedOpening,
        AirflowNetwork:MultiZone:Component:SimpleOpening,
        AirflowNetwork:MultiZone:Surface:Crack,
        AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea,
        AirflowNetwork:MultiZone:Component:HorizontalOpening, or
        AirflowNetwork:MultiZone:Component:ZoneExhaustFan.
        When the zone exhaust fan name is entered, any surface control fields below A3 are
        ignored when the zone exhaust fan turns on.
        
        {u'note': [u'Enter the name of an Airflow Network leakage component. A leakage component is', u'one of the following AirflowNetwork:Multizone objects:', u'AirflowNetwork:MultiZone:Component:DetailedOpening,', u'AirflowNetwork:MultiZone:Component:SimpleOpening,', u'AirflowNetwork:MultiZone:Surface:Crack,', u'AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea,', u'AirflowNetwork:MultiZone:Component:HorizontalOpening, or', u'AirflowNetwork:MultiZone:Component:ZoneExhaustFan.', u'When the zone exhaust fan name is entered, any surface control fields below A3 are', u'ignored when the zone exhaust fan turns on.'], u'type': u'object-list', u'object-list': u'SurfaceAirflowLeakageNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Leakage Component Name`
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
                                 'for field `leakage_component_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `leakage_component_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `leakage_component_name`')
        self._data["Leakage Component Name"] = value

    @property
    def external_node_name(self):
        """Get external_node_name

        Returns:
            str: the value of `external_node_name` or None if not set
        """
        return self._data["External Node Name"]

    @external_node_name.setter
    def external_node_name(self, value=None):
        """  Corresponds to IDD Field `External Node Name`
        Used if Wind Pressure Coefficient Type = Input in the AirflowNetwork:SimulationControl object,
        otherwise this field may be left blank.
        
        {u'note': [u'Used if Wind Pressure Coefficient Type = Input in the AirflowNetwork:SimulationControl object,', u'otherwise this field may be left blank.'], u'type': u'object-list', u'object-list': u'ExternalNodeNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `External Node Name`
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
                                 'for field `external_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `external_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `external_node_name`')
        self._data["External Node Name"] = value

    @property
    def window_or_door_opening_factor_or_crack_factor(self):
        """Get window_or_door_opening_factor_or_crack_factor

        Returns:
            float: the value of `window_or_door_opening_factor_or_crack_factor` or None if not set
        """
        return self._data["Window/Door Opening Factor, or Crack Factor"]

    @window_or_door_opening_factor_or_crack_factor.setter
    def window_or_door_opening_factor_or_crack_factor(self, value=1.0 ):
        """  Corresponds to IDD Field `Window/Door Opening Factor, or Crack Factor`
        This field specifies a multiplier for a crack, window, or door.
        
        {'pytype': 'float', u'default': '1.0', u'minimum>': '0.0', u'maximum': '1.0', u'required-field': True, u'note': [u'This field specifies a multiplier for a crack, window, or door.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Window/Door Opening Factor, or Crack Factor`
                Units: dimensionless
                Default value: 1.0
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `window_or_door_opening_factor_or_crack_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `window_or_door_opening_factor_or_crack_factor`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `window_or_door_opening_factor_or_crack_factor`')
        self._data["Window/Door Opening Factor, or Crack Factor"] = value

    @property
    def ventilation_control_mode(self):
        """Get ventilation_control_mode

        Returns:
            str: the value of `ventilation_control_mode` or None if not set
        """
        return self._data["Ventilation Control Mode"]

    @ventilation_control_mode.setter
    def ventilation_control_mode(self, value="ZoneLevel"):
        """  Corresponds to IDD Field `Ventilation Control Mode`
        When Ventilation Control Mode = Temperature or Enthalpy, the following
        fields are used to modulate the Ventilation Open Factor for a
        window or door opening according to the parent zone's
        indoor-outdoor temperature or enthalpy difference.
        When Ventilation Control Mode = AdjacentTemperature or AdjacentEnthalpy, the following
        fields are used to modulate the Ventilation Open Factor for an interior
        window or door opening according to temperature or enthalpy difference
        between the parent zone and the adjacent zone.
        Constant: controlled by field Venting Schedule Name.
        NoVent: control will not open window or door during simulation (Ventilation Open Factor = 0).
        ZoneLevel: control will be controlled by AirflowNetwork:MultiZone:Zone
        Mode.
        
        {u'default': u'ZoneLevel', u'note': [u'When Ventilation Control Mode = Temperature or Enthalpy, the following', u'fields are used to modulate the Ventilation Open Factor for a', u"window or door opening according to the parent zone's", u'indoor-outdoor temperature or enthalpy difference.', u'When Ventilation Control Mode = AdjacentTemperature or AdjacentEnthalpy, the following', u'fields are used to modulate the Ventilation Open Factor for an interior', u'window or door opening according to temperature or enthalpy difference', u'between the parent zone and the adjacent zone.', u'Constant: controlled by field Venting Schedule Name.', u'NoVent: control will not open window or door during simulation (Ventilation Open Factor = 0).', u'ZoneLevel: control will be controlled by AirflowNetwork:MultiZone:Zone', u'Mode.'], u'type': u'choice', u'key': [u'Temperature', u'Enthalpy', u'Constant', u'ASHRAE55Adaptive', u'CEN15251Adaptive', u'NoVent', u'ZoneLevel', u'AdjacentTemperature', u'AdjacentEnthalpy'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Ventilation Control Mode`
                Accepted values are:
                      - Temperature
                      - Enthalpy
                      - Constant
                      - ASHRAE55Adaptive
                      - CEN15251Adaptive
                      - NoVent
                      - ZoneLevel
                      - AdjacentTemperature
                      - AdjacentEnthalpy
                Default value: ZoneLevel
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
                                 'for field `ventilation_control_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ventilation_control_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ventilation_control_mode`')
            vals = {}
            vals["temperature"] = "Temperature"
            vals["enthalpy"] = "Enthalpy"
            vals["constant"] = "Constant"
            vals["ashrae55adaptive"] = "ASHRAE55Adaptive"
            vals["cen15251adaptive"] = "CEN15251Adaptive"
            vals["novent"] = "NoVent"
            vals["zonelevel"] = "ZoneLevel"
            vals["adjacenttemperature"] = "AdjacentTemperature"
            vals["adjacententhalpy"] = "AdjacentEnthalpy"
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
                                     'field `ventilation_control_mode`'.format(value))
            value = vals[value_lower]
        self._data["Ventilation Control Mode"] = value

    @property
    def ventilation_control_zone_temperature_setpoint_schedule_name(self):
        """Get ventilation_control_zone_temperature_setpoint_schedule_name

        Returns:
            str: the value of `ventilation_control_zone_temperature_setpoint_schedule_name` or None if not set
        """
        return self._data["Ventilation Control Zone Temperature Setpoint Schedule Name"]

    @ventilation_control_zone_temperature_setpoint_schedule_name.setter
    def ventilation_control_zone_temperature_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Ventilation Control Zone Temperature Setpoint Schedule Name`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.
        
        {u'note': [u'Used only if Ventilation Control Mode = Temperature or Enthalpy.'], u'type': u'object-list', u'object-list': u'ScheduleNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Ventilation Control Zone Temperature Setpoint Schedule Name`
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
                                 'for field `ventilation_control_zone_temperature_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ventilation_control_zone_temperature_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ventilation_control_zone_temperature_setpoint_schedule_name`')
        self._data["Ventilation Control Zone Temperature Setpoint Schedule Name"] = value

    @property
    def minimum_venting_open_factor(self):
        """Get minimum_venting_open_factor

        Returns:
            float: the value of `minimum_venting_open_factor` or None if not set
        """
        return self._data["Minimum Venting Open Factor"]

    @minimum_venting_open_factor.setter
    def minimum_venting_open_factor(self, value=0.0 ):
        """  Corresponds to IDD Field `Minimum Venting Open Factor`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'Used only if Ventilation Control Mode = Temperature or Enthalpy.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Minimum Venting Open Factor`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_venting_open_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_venting_open_factor`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_venting_open_factor`')
        self._data["Minimum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor(self):
        """Get indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor

        Returns:
            float: the value of `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor` or None if not set
        """
        return self._data["Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor"]

    @indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor.setter
    def indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor(self, value=0.0 ):
        """  Corresponds to IDD Field `Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor`
        Applicable only if Ventilation Control Mode = Temperature
        
        {'pytype': 'float', u'default': '0.0', u'maximum<': '100.0', u'note': [u'Applicable only if Ventilation Control Mode = Temperature'], u'minimum': '0.0', u'units': u'deltaC', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor`
                Units: deltaC
                Default value: 0.0
                value >= 0.0
                value < 100.0
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
                                 'for field `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor`')
            if value >= 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor`')
        self._data["Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor(self):
        """Get indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor

        Returns:
            float: the value of `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor` or None if not set
        """
        return self._data["Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor"]

    @indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor.setter
    def indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor(self, value=100.0 ):
        """  Corresponds to IDD Field `Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor`
        Applicable only if Ventilation Control Mode = Temperature.
        This value must be greater than the corresponding lower value (previous field).
        
        {'pytype': 'float', u'default': '100.0', u'minimum>': '0.0', u'note': [u'Applicable only if Ventilation Control Mode = Temperature.', u'This value must be greater than the corresponding lower value (previous field).'], u'units': u'deltaC', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor`
                Units: deltaC
                Default value: 100.0
                value > 0.0
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
                                 'for field `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor`')
        self._data["Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor(self):
        """Get indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor

        Returns:
            float: the value of `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor` or None if not set
        """
        return self._data["Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor"]

    @indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor.setter
    def indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor(self, value=0.0 ):
        """  Corresponds to IDD Field `Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be less than the corresponding upper value (next field).
        
        {'pytype': 'float', u'default': '0.0', u'maximum<': '300000.0', u'note': [u'Applicable only if Ventilation Control Mode = Enthalpy.', u'This value must be less than the corresponding upper value (next field).'], u'minimum': '0.0', u'units': u'deltaJ/kg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor`
                Units: deltaJ/kg
                Default value: 0.0
                value >= 0.0
                value < 300000.0
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
                                 'for field `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor`')
            if value >= 300000.0:
                raise ValueError('value need to be smaller 300000.0 '
                                 'for field `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor`')
        self._data["Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor(self):
        """Get indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor

        Returns:
            float: the value of `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor` or None if not set
        """
        return self._data["Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor"]

    @indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor.setter
    def indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor(self, value=300000.0 ):
        """  Corresponds to IDD Field `Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be greater than the corresponding lower value (previous field).
        
        {'pytype': 'float', u'default': '300000.0', u'minimum>': '0.0', u'note': [u'Applicable only if Ventilation Control Mode = Enthalpy.', u'This value must be greater than the corresponding lower value (previous field).'], u'units': u'deltaJ/kg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor`
                Units: deltaJ/kg
                Default value: 300000.0
                value > 0.0
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
                                 'for field `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor`')
        self._data["Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor"] = value

    @property
    def venting_availability_schedule_name(self):
        """Get venting_availability_schedule_name

        Returns:
            str: the value of `venting_availability_schedule_name` or None if not set
        """
        return self._data["Venting Availability Schedule Name"]

    @venting_availability_schedule_name.setter
    def venting_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Venting Availability Schedule Name`
        Non-zero schedule value means venting is allowed if other venting control conditions are
        satisfied. A zero (or negative) schedule value means venting is not allowed under any
        circumstances. The schedule values should be greater than or equal to 0 and less than or
        equal to 1. If this schedule is not specified then venting is allowed if
        other venting control conditions are satisfied.
        Not used if Ventilation Control Mode = NoVent or ZoneLevel.
        
        {u'note': [u'Non-zero schedule value means venting is allowed if other venting control conditions are', u'satisfied. A zero (or negative) schedule value means venting is not allowed under any', u'circumstances. The schedule values should be greater than or equal to 0 and less than or', u'equal to 1. If this schedule is not specified then venting is allowed if', u'other venting control conditions are satisfied.', u'Not used if Ventilation Control Mode = NoVent or ZoneLevel.'], u'type': u'object-list', u'object-list': u'ScheduleNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Venting Availability Schedule Name`
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
                                 'for field `venting_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `venting_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `venting_availability_schedule_name`')
        self._data["Venting Availability Schedule Name"] = value

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

class AirflowNetworkMultiZoneReferenceCrackConditions(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:ReferenceCrackConditions`
        This object specifies the conditions under which the air mass flow coefficient was measured.
    
    """
    internal_name = "AirflowNetwork:MultiZone:ReferenceCrackConditions"
    field_count = 4
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:ReferenceCrackConditions`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Temperature"] = None
        self._data["Reference Barometric Pressure"] = None
        self._data["Reference Humidity Ratio"] = None
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
            self.reference_temperature = None
        else:
            self.reference_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_barometric_pressure = None
        else:
            self.reference_barometric_pressure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_humidity_ratio = None
        else:
            self.reference_humidity_ratio = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'ReferenceCrackConditions', u'required-field': True, 'pytype': 'str'}

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
    def reference_temperature(self):
        """Get reference_temperature

        Returns:
            float: the value of `reference_temperature` or None if not set
        """
        return self._data["Reference Temperature"]

    @reference_temperature.setter
    def reference_temperature(self, value=20.0 ):
        """  Corresponds to IDD Field `Reference Temperature`
        Enter the reference temperature under which the surface crack data were obtained.
        
        {u'units': u'C', u'default': '20.0', u'note': [u'Enter the reference temperature under which the surface crack data were obtained.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Reference Temperature`
                Units: C
                Default value: 20.0
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
                                 'for field `reference_temperature`'.format(value))
        self._data["Reference Temperature"] = value

    @property
    def reference_barometric_pressure(self):
        """Get reference_barometric_pressure

        Returns:
            float: the value of `reference_barometric_pressure` or None if not set
        """
        return self._data["Reference Barometric Pressure"]

    @reference_barometric_pressure.setter
    def reference_barometric_pressure(self, value=101325.0 ):
        """  Corresponds to IDD Field `Reference Barometric Pressure`
        Enter the reference barometric pressure under which the surface crack data were obtained.
        
        {'pytype': 'float', u'default': '101325.0', u'maximum': '120000.0', u'note': [u'Enter the reference barometric pressure under which the surface crack data were obtained.'], u'ip-units': u'inHg', u'minimum': '31000.0', u'units': u'Pa', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Reference Barometric Pressure`
                Units: Pa
                IP-Units: inHg
                Default value: 101325.0
                value >= 31000.0
                value <= 120000.0
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
                                 'for field `reference_barometric_pressure`'.format(value))
            if value < 31000.0:
                raise ValueError('value need to be greater or equal 31000.0 '
                                 'for field `reference_barometric_pressure`')
            if value > 120000.0:
                raise ValueError('value need to be smaller 120000.0 '
                                 'for field `reference_barometric_pressure`')
        self._data["Reference Barometric Pressure"] = value

    @property
    def reference_humidity_ratio(self):
        """Get reference_humidity_ratio

        Returns:
            float: the value of `reference_humidity_ratio` or None if not set
        """
        return self._data["Reference Humidity Ratio"]

    @reference_humidity_ratio.setter
    def reference_humidity_ratio(self, value=0.0 ):
        """  Corresponds to IDD Field `Reference Humidity Ratio`
        Enter the reference humidity ratio under which the surface crack data were obtained.
        
        {u'units': u'kgWater/kgDryAir', u'default': '0.0', u'note': [u'Enter the reference humidity ratio under which the surface crack data were obtained.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Reference Humidity Ratio`
                Units: kgWater/kgDryAir
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
                                 'for field `reference_humidity_ratio`'.format(value))
        self._data["Reference Humidity Ratio"] = value

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

class AirflowNetworkMultiZoneSurfaceCrack(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Surface:Crack`
        This object specifies the properties of airflow through a crack.
    
    """
    internal_name = "AirflowNetwork:MultiZone:Surface:Crack"
    field_count = 4
    required_fields = ["Name", "Air Mass Flow Coefficient at Reference Conditions"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:Surface:Crack`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient at Reference Conditions"] = None
        self._data["Air Mass Flow Exponent"] = None
        self._data["Reference Crack Conditions"] = None
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
            self.air_mass_flow_coefficient_at_reference_conditions = None
        else:
            self.air_mass_flow_coefficient_at_reference_conditions = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent = None
        else:
            self.air_mass_flow_exponent = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_crack_conditions = None
        else:
            self.reference_crack_conditions = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'SurfaceAirflowLeakageNames', u'required-field': True, 'pytype': 'str'}

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
    def air_mass_flow_coefficient_at_reference_conditions(self):
        """Get air_mass_flow_coefficient_at_reference_conditions

        Returns:
            float: the value of `air_mass_flow_coefficient_at_reference_conditions` or None if not set
        """
        return self._data["Air Mass Flow Coefficient at Reference Conditions"]

    @air_mass_flow_coefficient_at_reference_conditions.setter
    def air_mass_flow_coefficient_at_reference_conditions(self, value=None):
        """  Corresponds to IDD Field `Air Mass Flow Coefficient at Reference Conditions`
        Enter the air mass flow coefficient at the conditions defined
        in the Reference Crack Conditions object.
        Defined at 1 Pa pressure difference across this crack.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the air mass flow coefficient at the conditions defined', u'in the Reference Crack Conditions object.', u'Defined at 1 Pa pressure difference across this crack.'], u'units': u'kg/s', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient at Reference Conditions`
                Units: kg/s
                value > 0.0
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
                                 'for field `air_mass_flow_coefficient_at_reference_conditions`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_mass_flow_coefficient_at_reference_conditions`')
        self._data["Air Mass Flow Coefficient at Reference Conditions"] = value

    @property
    def air_mass_flow_exponent(self):
        """Get air_mass_flow_exponent

        Returns:
            float: the value of `air_mass_flow_exponent` or None if not set
        """
        return self._data["Air Mass Flow Exponent"]

    @air_mass_flow_exponent.setter
    def air_mass_flow_exponent(self, value=0.65 ):
        """  Corresponds to IDD Field `Air Mass Flow Exponent`
        Enter the air mass flow exponent for the surface crack.
        
        {'pytype': 'float', u'default': '0.65', u'maximum': '1.0', u'note': [u'Enter the air mass flow exponent for the surface crack.'], u'minimum': '0.5', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
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
                                 'for field `air_mass_flow_exponent`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent`')
        self._data["Air Mass Flow Exponent"] = value

    @property
    def reference_crack_conditions(self):
        """Get reference_crack_conditions

        Returns:
            str: the value of `reference_crack_conditions` or None if not set
        """
        return self._data["Reference Crack Conditions"]

    @reference_crack_conditions.setter
    def reference_crack_conditions(self, value=None):
        """  Corresponds to IDD Field `Reference Crack Conditions`
        Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with
        the air mass flow coefficient entered above.
        
        {u'note': [u'Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with', u'the air mass flow coefficient entered above.'], u'type': u'object-list', u'object-list': u'ReferenceCrackConditions', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Reference Crack Conditions`
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
                                 'for field `reference_crack_conditions`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_crack_conditions`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_crack_conditions`')
        self._data["Reference Crack Conditions"] = value

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

class AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea`
        This object is used to define surface air leakage.
    
    """
    internal_name = "AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea"
    field_count = 5
    required_fields = ["Name", "Effective Leakage Area"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Effective Leakage Area"] = None
        self._data["Discharge Coefficient"] = None
        self._data["Reference Pressure Difference"] = None
        self._data["Air Mass Flow Exponent"] = None
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
            self.effective_leakage_area = None
        else:
            self.effective_leakage_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharge_coefficient = None
        else:
            self.discharge_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_pressure_difference = None
        else:
            self.reference_pressure_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent = None
        else:
            self.air_mass_flow_exponent = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'SurfaceAirflowLeakageNames', u'required-field': True, 'pytype': 'str'}

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
    def effective_leakage_area(self):
        """Get effective_leakage_area

        Returns:
            float: the value of `effective_leakage_area` or None if not set
        """
        return self._data["Effective Leakage Area"]

    @effective_leakage_area.setter
    def effective_leakage_area(self, value=None):
        """  Corresponds to IDD Field `Effective Leakage Area`
        Enter the effective leakage area.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the effective leakage area.'], u'units': u'm2', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Effective Leakage Area`
                Units: m2
                value > 0.0
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
                                 'for field `effective_leakage_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `effective_leakage_area`')
        self._data["Effective Leakage Area"] = value

    @property
    def discharge_coefficient(self):
        """Get discharge_coefficient

        Returns:
            float: the value of `discharge_coefficient` or None if not set
        """
        return self._data["Discharge Coefficient"]

    @discharge_coefficient.setter
    def discharge_coefficient(self, value=1.0 ):
        """  Corresponds to IDD Field `Discharge Coefficient`
        Enter the coefficient used in the air mass flow equation.
        
        {'pytype': 'float', u'default': '1.0', u'minimum>': '0.0', u'note': [u'Enter the coefficient used in the air mass flow equation.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Discharge Coefficient`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `discharge_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `discharge_coefficient`')
        self._data["Discharge Coefficient"] = value

    @property
    def reference_pressure_difference(self):
        """Get reference_pressure_difference

        Returns:
            float: the value of `reference_pressure_difference` or None if not set
        """
        return self._data["Reference Pressure Difference"]

    @reference_pressure_difference.setter
    def reference_pressure_difference(self, value=4.0 ):
        """  Corresponds to IDD Field `Reference Pressure Difference`
        Enter the pressure difference used to define the air mass flow coefficient and exponent.
        
        {'pytype': 'float', u'default': '4.0', u'minimum>': '0.0', u'note': [u'Enter the pressure difference used to define the air mass flow coefficient and exponent.'], u'units': u'Pa', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Reference Pressure Difference`
                Units: Pa
                Default value: 4.0
                value > 0.0
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
                                 'for field `reference_pressure_difference`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_pressure_difference`')
        self._data["Reference Pressure Difference"] = value

    @property
    def air_mass_flow_exponent(self):
        """Get air_mass_flow_exponent

        Returns:
            float: the value of `air_mass_flow_exponent` or None if not set
        """
        return self._data["Air Mass Flow Exponent"]

    @air_mass_flow_exponent.setter
    def air_mass_flow_exponent(self, value=0.65 ):
        """  Corresponds to IDD Field `Air Mass Flow Exponent`
        Enter the exponent used in the air mass flow equation.
        
        {'pytype': 'float', u'default': '0.65', u'maximum': '1.0', u'note': [u'Enter the exponent used in the air mass flow equation.'], u'minimum': '0.5', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
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
                                 'for field `air_mass_flow_exponent`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent`')
        self._data["Air Mass Flow Exponent"] = value

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

class AirflowNetworkMultiZoneComponentDetailedOpening(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:DetailedOpening`
        This object specifies the properties of airflow through windows and doors (window, door and
        glass door heat transfer subsurfaces) when they are closed or open.
    
    """
    internal_name = "AirflowNetwork:MultiZone:Component:DetailedOpening"
    field_count = 26
    required_fields = ["Name", "Air Mass Flow Coefficient When Opening is Closed", "Number of Sets of Opening Factor Data", "Opening Factor 2"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:Component:DetailedOpening`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient When Opening is Closed"] = None
        self._data["Air Mass Flow Exponent When Opening is Closed"] = None
        self._data["Type of Rectanguler Large Vertical Opening (LVO)"] = None
        self._data["Extra Crack Length or Height of Pivoting Axis"] = None
        self._data["Number of Sets of Opening Factor Data"] = None
        self._data["Opening Factor 1"] = None
        self._data["Discharge Coefficient for Opening Factor 1"] = None
        self._data["Width Factor for Opening Factor 1"] = None
        self._data["Height Factor for Opening Factor 1"] = None
        self._data["Start Height Factor for Opening Factor 1"] = None
        self._data["Opening Factor 2"] = None
        self._data["Discharge Coefficient for Opening Factor 2"] = None
        self._data["Width Factor for Opening Factor 2"] = None
        self._data["Height Factor for Opening Factor 2"] = None
        self._data["Start Height Factor for Opening Factor 2"] = None
        self._data["Opening Factor 3"] = None
        self._data["Discharge Coefficient for Opening Factor 3"] = None
        self._data["Width Factor for Opening Factor 3"] = None
        self._data["Height Factor for Opening Factor 3"] = None
        self._data["Start Height Factor for Opening Factor 3"] = None
        self._data["Opening Factor 4"] = None
        self._data["Discharge Coefficient for Opening Factor 4"] = None
        self._data["Width Factor for Opening Factor 4"] = None
        self._data["Height Factor for Opening Factor 4"] = None
        self._data["Start Height Factor for Opening Factor 4"] = None
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
            self.air_mass_flow_coefficient_when_opening_is_closed = None
        else:
            self.air_mass_flow_coefficient_when_opening_is_closed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent_when_opening_is_closed = None
        else:
            self.air_mass_flow_exponent_when_opening_is_closed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.type_of_rectanguler_large_vertical_opening_lvo = None
        else:
            self.type_of_rectanguler_large_vertical_opening_lvo = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.extra_crack_length_or_height_of_pivoting_axis = None
        else:
            self.extra_crack_length_or_height_of_pivoting_axis = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_sets_of_opening_factor_data = None
        else:
            self.number_of_sets_of_opening_factor_data = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.opening_factor_1 = None
        else:
            self.opening_factor_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_opening_factor_1 = None
        else:
            self.discharge_coefficient_for_opening_factor_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width_factor_for_opening_factor_1 = None
        else:
            self.width_factor_for_opening_factor_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_factor_for_opening_factor_1 = None
        else:
            self.height_factor_for_opening_factor_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.start_height_factor_for_opening_factor_1 = None
        else:
            self.start_height_factor_for_opening_factor_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.opening_factor_2 = None
        else:
            self.opening_factor_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_opening_factor_2 = None
        else:
            self.discharge_coefficient_for_opening_factor_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width_factor_for_opening_factor_2 = None
        else:
            self.width_factor_for_opening_factor_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_factor_for_opening_factor_2 = None
        else:
            self.height_factor_for_opening_factor_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.start_height_factor_for_opening_factor_2 = None
        else:
            self.start_height_factor_for_opening_factor_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.opening_factor_3 = None
        else:
            self.opening_factor_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_opening_factor_3 = None
        else:
            self.discharge_coefficient_for_opening_factor_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width_factor_for_opening_factor_3 = None
        else:
            self.width_factor_for_opening_factor_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_factor_for_opening_factor_3 = None
        else:
            self.height_factor_for_opening_factor_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.start_height_factor_for_opening_factor_3 = None
        else:
            self.start_height_factor_for_opening_factor_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.opening_factor_4 = None
        else:
            self.opening_factor_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_opening_factor_4 = None
        else:
            self.discharge_coefficient_for_opening_factor_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width_factor_for_opening_factor_4 = None
        else:
            self.width_factor_for_opening_factor_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_factor_for_opening_factor_4 = None
        else:
            self.height_factor_for_opening_factor_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.start_height_factor_for_opening_factor_4 = None
        else:
            self.start_height_factor_for_opening_factor_4 = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'SurfaceAirflowLeakageNames', u'required-field': True, 'pytype': 'str'}

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
    def air_mass_flow_coefficient_when_opening_is_closed(self):
        """Get air_mass_flow_coefficient_when_opening_is_closed

        Returns:
            float: the value of `air_mass_flow_coefficient_when_opening_is_closed` or None if not set
        """
        return self._data["Air Mass Flow Coefficient When Opening is Closed"]

    @air_mass_flow_coefficient_when_opening_is_closed.setter
    def air_mass_flow_coefficient_when_opening_is_closed(self, value=None):
        """  Corresponds to IDD Field `Air Mass Flow Coefficient When Opening is Closed`
        Defined at 1 Pa per meter of crack length. Enter the coefficient used in the following
        equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Defined at 1 Pa per meter of crack length. Enter the coefficient used in the following', u'equation:', u'Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.', u'Used only when opening (window or door) is closed.'], u'units': u'kg/s-m', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient When Opening is Closed`
                Units: kg/s-m
                value > 0.0
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
                                 'for field `air_mass_flow_coefficient_when_opening_is_closed`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_mass_flow_coefficient_when_opening_is_closed`')
        self._data["Air Mass Flow Coefficient When Opening is Closed"] = value

    @property
    def air_mass_flow_exponent_when_opening_is_closed(self):
        """Get air_mass_flow_exponent_when_opening_is_closed

        Returns:
            float: the value of `air_mass_flow_exponent_when_opening_is_closed` or None if not set
        """
        return self._data["Air Mass Flow Exponent When Opening is Closed"]

    @air_mass_flow_exponent_when_opening_is_closed.setter
    def air_mass_flow_exponent_when_opening_is_closed(self, value=0.65 ):
        """  Corresponds to IDD Field `Air Mass Flow Exponent When Opening is Closed`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.
        
        {'pytype': 'float', u'default': '0.65', u'maximum': '1.0', u'note': [u'Enter the exponent used in the following equation:', u'Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.', u'Used only when opening (window or door) is closed.'], u'minimum': '0.5', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent When Opening is Closed`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
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
                                 'for field `air_mass_flow_exponent_when_opening_is_closed`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent_when_opening_is_closed`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent_when_opening_is_closed`')
        self._data["Air Mass Flow Exponent When Opening is Closed"] = value

    @property
    def type_of_rectanguler_large_vertical_opening_lvo(self):
        """Get type_of_rectanguler_large_vertical_opening_lvo

        Returns:
            str: the value of `type_of_rectanguler_large_vertical_opening_lvo` or None if not set
        """
        return self._data["Type of Rectanguler Large Vertical Opening (LVO)"]

    @type_of_rectanguler_large_vertical_opening_lvo.setter
    def type_of_rectanguler_large_vertical_opening_lvo(self, value="NonPivoted"):
        """  Corresponds to IDD Field `Type of Rectanguler Large Vertical Opening (LVO)`
        Select the type of vertical opening: Non-pivoted opening or Horizontally pivoted opening.
        
        {u'note': [u'Select the type of vertical opening: Non-pivoted opening or Horizontally pivoted opening.'], u'default': u'NonPivoted', u'type': u'choice', u'key': [u'NonPivoted', u'HorizontallyPivoted'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Type of Rectanguler Large Vertical Opening (LVO)`
                Accepted values are:
                      - NonPivoted
                      - HorizontallyPivoted
                Default value: NonPivoted
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
                                 'for field `type_of_rectanguler_large_vertical_opening_lvo`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type_of_rectanguler_large_vertical_opening_lvo`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `type_of_rectanguler_large_vertical_opening_lvo`')
            vals = {}
            vals["nonpivoted"] = "NonPivoted"
            vals["horizontallypivoted"] = "HorizontallyPivoted"
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
                                     'field `type_of_rectanguler_large_vertical_opening_lvo`'.format(value))
            value = vals[value_lower]
        self._data["Type of Rectanguler Large Vertical Opening (LVO)"] = value

    @property
    def extra_crack_length_or_height_of_pivoting_axis(self):
        """Get extra_crack_length_or_height_of_pivoting_axis

        Returns:
            float: the value of `extra_crack_length_or_height_of_pivoting_axis` or None if not set
        """
        return self._data["Extra Crack Length or Height of Pivoting Axis"]

    @extra_crack_length_or_height_of_pivoting_axis.setter
    def extra_crack_length_or_height_of_pivoting_axis(self, value=0.0 ):
        """  Corresponds to IDD Field `Extra Crack Length or Height of Pivoting Axis`
        Extra crack length is used for LVO Non-pivoted type with multiple openable parts.
        Height of pivoting axis is used for LVO Horizontally pivoted type.
        Specifies window or door characteristics that depend on the LVO type.
        For Non-pivoted Type (rectangular windows and doors), this field is the extra crack length
        in meters due to multiple openable parts, if present.  Extra here means in addition
        to the length of the cracks on the top, bottom and sides of the window/door.
        For Horizontally pivoted Type, this field gives the height of the
        pivoting axis measured from the bottom of the glazed part of the window (m).
        
        {'pytype': 'float', u'default': '0.0', u'note': [u'Extra crack length is used for LVO Non-pivoted type with multiple openable parts.', u'Height of pivoting axis is used for LVO Horizontally pivoted type.', u'Specifies window or door characteristics that depend on the LVO type.', u'For Non-pivoted Type (rectangular windows and doors), this field is the extra crack length', u'in meters due to multiple openable parts, if present.  Extra here means in addition', u'to the length of the cracks on the top, bottom and sides of the window/door.', u'For Horizontally pivoted Type, this field gives the height of the', u'pivoting axis measured from the bottom of the glazed part of the window (m).'], u'minimum': '0.0', u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Extra Crack Length or Height of Pivoting Axis`
                Units: m
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `extra_crack_length_or_height_of_pivoting_axis`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `extra_crack_length_or_height_of_pivoting_axis`')
        self._data["Extra Crack Length or Height of Pivoting Axis"] = value

    @property
    def number_of_sets_of_opening_factor_data(self):
        """Get number_of_sets_of_opening_factor_data

        Returns:
            int: the value of `number_of_sets_of_opening_factor_data` or None if not set
        """
        return self._data["Number of Sets of Opening Factor Data"]

    @number_of_sets_of_opening_factor_data.setter
    def number_of_sets_of_opening_factor_data(self, value=None):
        """  Corresponds to IDD Field `Number of Sets of Opening Factor Data`
        Enter the number of the following sets of data for opening factor,
        discharge coefficient, width factor, height factor, and start height factor.
        
        {'pytype': 'int', u'maximum': '4', u'required-field': True, u'note': [u'Enter the number of the following sets of data for opening factor,', u'discharge coefficient, width factor, height factor, and start height factor.'], u'minimum': '2', u'type': u'integer'}

        Args:
            value (int): value for IDD Field `Number of Sets of Opening Factor Data`
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
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_sets_of_opening_factor_data`'.format(value))
            if value < 2:
                raise ValueError('value need to be greater or equal 2 '
                                 'for field `number_of_sets_of_opening_factor_data`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `number_of_sets_of_opening_factor_data`')
        self._data["Number of Sets of Opening Factor Data"] = value

    @property
    def opening_factor_1(self):
        """Get opening_factor_1

        Returns:
            float: the value of `opening_factor_1` or None if not set
        """
        return self._data["Opening Factor 1"]

    @opening_factor_1.setter
    def opening_factor_1(self, value=0.0 ):
        """  Corresponds to IDD Field `Opening Factor 1`
        This value must be specified as 0.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '0.0', u'note': [u'This value must be specified as 0.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Opening Factor 1`
                Units: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 0.0
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
                                 'for field `opening_factor_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `opening_factor_1`')
            if value > 0.0:
                raise ValueError('value need to be smaller 0.0 '
                                 'for field `opening_factor_1`')
        self._data["Opening Factor 1"] = value

    @property
    def discharge_coefficient_for_opening_factor_1(self):
        """Get discharge_coefficient_for_opening_factor_1

        Returns:
            float: the value of `discharge_coefficient_for_opening_factor_1` or None if not set
        """
        return self._data["Discharge Coefficient for Opening Factor 1"]

    @discharge_coefficient_for_opening_factor_1.setter
    def discharge_coefficient_for_opening_factor_1(self, value=0.001 ):
        """  Corresponds to IDD Field `Discharge Coefficient for Opening Factor 1`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through a window or door at that Opening Factor.
        
        {'pytype': 'float', u'default': '0.001', u'minimum>': '0.0', u'maximum': '1.0', u'note': [u'The Discharge Coefficient indicates the fractional effectiveness', u'for air flow through a window or door at that Opening Factor.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Opening Factor 1`
                Units: dimensionless
                Default value: 0.001
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `discharge_coefficient_for_opening_factor_1`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `discharge_coefficient_for_opening_factor_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `discharge_coefficient_for_opening_factor_1`')
        self._data["Discharge Coefficient for Opening Factor 1"] = value

    @property
    def width_factor_for_opening_factor_1(self):
        """Get width_factor_for_opening_factor_1

        Returns:
            float: the value of `width_factor_for_opening_factor_1` or None if not set
        """
        return self._data["Width Factor for Opening Factor 1"]

    @width_factor_for_opening_factor_1.setter
    def width_factor_for_opening_factor_1(self, value=0.0 ):
        """  Corresponds to IDD Field `Width Factor for Opening Factor 1`
        The Width Factor is the opening width divided by the window or door width.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Width Factor is the opening width divided by the window or door width.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Width Factor for Opening Factor 1`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `width_factor_for_opening_factor_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `width_factor_for_opening_factor_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `width_factor_for_opening_factor_1`')
        self._data["Width Factor for Opening Factor 1"] = value

    @property
    def height_factor_for_opening_factor_1(self):
        """Get height_factor_for_opening_factor_1

        Returns:
            float: the value of `height_factor_for_opening_factor_1` or None if not set
        """
        return self._data["Height Factor for Opening Factor 1"]

    @height_factor_for_opening_factor_1.setter
    def height_factor_for_opening_factor_1(self, value=0.0 ):
        """  Corresponds to IDD Field `Height Factor for Opening Factor 1`
        The Height Factor is the opening height divided by the window or door height.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Height Factor is the opening height divided by the window or door height.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Height Factor for Opening Factor 1`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `height_factor_for_opening_factor_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `height_factor_for_opening_factor_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `height_factor_for_opening_factor_1`')
        self._data["Height Factor for Opening Factor 1"] = value

    @property
    def start_height_factor_for_opening_factor_1(self):
        """Get start_height_factor_for_opening_factor_1

        Returns:
            float: the value of `start_height_factor_for_opening_factor_1` or None if not set
        """
        return self._data["Start Height Factor for Opening Factor 1"]

    @start_height_factor_for_opening_factor_1.setter
    def start_height_factor_for_opening_factor_1(self, value=0.0 ):
        """  Corresponds to IDD Field `Start Height Factor for Opening Factor 1`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Start Height Factor is the Start Height divided by the window or door height.', u'Start Height is the distance between the bottom of the window or door and the', u'bottom of the window or door opening. The sum of the Height Factor and the Start Height', u'Factor must be less than 1.0 in order to have the opening within the window or door', u'dimensions.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Start Height Factor for Opening Factor 1`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `start_height_factor_for_opening_factor_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `start_height_factor_for_opening_factor_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `start_height_factor_for_opening_factor_1`')
        self._data["Start Height Factor for Opening Factor 1"] = value

    @property
    def opening_factor_2(self):
        """Get opening_factor_2

        Returns:
            float: the value of `opening_factor_2` or None if not set
        """
        return self._data["Opening Factor 2"]

    @opening_factor_2.setter
    def opening_factor_2(self, value=None):
        """  Corresponds to IDD Field `Opening Factor 2`
        If Number of Sets of Opening Factor Data = 2, this value must be 1.0.
        If Number of Sets of Opening Factor Data = 3, this value must be less than 1.0.
        If Number of Sets of Opening Factor Data = 4, this value must be less than the
        value entered for Opening factor 3 and greater than the value entered
        for Opening factor 1.
        
        {'pytype': 'float', u'minimum>': '0.0', u'maximum': '1.0', u'required-field': True, u'note': [u'If Number of Sets of Opening Factor Data = 2, this value must be 1.0.', u'If Number of Sets of Opening Factor Data = 3, this value must be less than 1.0.', u'If Number of Sets of Opening Factor Data = 4, this value must be less than the', u'value entered for Opening factor 3 and greater than the value entered', u'for Opening factor 1.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Opening Factor 2`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `opening_factor_2`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `opening_factor_2`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `opening_factor_2`')
        self._data["Opening Factor 2"] = value

    @property
    def discharge_coefficient_for_opening_factor_2(self):
        """Get discharge_coefficient_for_opening_factor_2

        Returns:
            float: the value of `discharge_coefficient_for_opening_factor_2` or None if not set
        """
        return self._data["Discharge Coefficient for Opening Factor 2"]

    @discharge_coefficient_for_opening_factor_2.setter
    def discharge_coefficient_for_opening_factor_2(self, value=1.0 ):
        """  Corresponds to IDD Field `Discharge Coefficient for Opening Factor 2`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through a window or door at that Opening Factor.
        
        {'pytype': 'float', u'default': '1.0', u'minimum>': '0.0', u'maximum': '1.0', u'note': [u'The Discharge Coefficient indicates the fractional effectiveness', u'for air flow through a window or door at that Opening Factor.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Opening Factor 2`
                Units: dimensionless
                Default value: 1.0
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `discharge_coefficient_for_opening_factor_2`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `discharge_coefficient_for_opening_factor_2`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `discharge_coefficient_for_opening_factor_2`')
        self._data["Discharge Coefficient for Opening Factor 2"] = value

    @property
    def width_factor_for_opening_factor_2(self):
        """Get width_factor_for_opening_factor_2

        Returns:
            float: the value of `width_factor_for_opening_factor_2` or None if not set
        """
        return self._data["Width Factor for Opening Factor 2"]

    @width_factor_for_opening_factor_2.setter
    def width_factor_for_opening_factor_2(self, value=1.0 ):
        """  Corresponds to IDD Field `Width Factor for Opening Factor 2`
        The Width Factor is the opening width divided by the window or door width.
        
        {'pytype': 'float', u'default': '1.0', u'minimum>': '0.0', u'maximum': '1.0', u'note': [u'The Width Factor is the opening width divided by the window or door width.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Width Factor for Opening Factor 2`
                Units: dimensionless
                Default value: 1.0
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `width_factor_for_opening_factor_2`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `width_factor_for_opening_factor_2`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `width_factor_for_opening_factor_2`')
        self._data["Width Factor for Opening Factor 2"] = value

    @property
    def height_factor_for_opening_factor_2(self):
        """Get height_factor_for_opening_factor_2

        Returns:
            float: the value of `height_factor_for_opening_factor_2` or None if not set
        """
        return self._data["Height Factor for Opening Factor 2"]

    @height_factor_for_opening_factor_2.setter
    def height_factor_for_opening_factor_2(self, value=1.0 ):
        """  Corresponds to IDD Field `Height Factor for Opening Factor 2`
        The Height Factor is the opening height divided by the window or door height.
        
        {'pytype': 'float', u'default': '1.0', u'minimum>': '0.0', u'maximum': '1.0', u'note': [u'The Height Factor is the opening height divided by the window or door height.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Height Factor for Opening Factor 2`
                Units: dimensionless
                Default value: 1.0
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `height_factor_for_opening_factor_2`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `height_factor_for_opening_factor_2`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `height_factor_for_opening_factor_2`')
        self._data["Height Factor for Opening Factor 2"] = value

    @property
    def start_height_factor_for_opening_factor_2(self):
        """Get start_height_factor_for_opening_factor_2

        Returns:
            float: the value of `start_height_factor_for_opening_factor_2` or None if not set
        """
        return self._data["Start Height Factor for Opening Factor 2"]

    @start_height_factor_for_opening_factor_2.setter
    def start_height_factor_for_opening_factor_2(self, value=0.0 ):
        """  Corresponds to IDD Field `Start Height Factor for Opening Factor 2`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.
        
        {'pytype': 'float', u'default': '0.0', u'maximum<': '1.0', u'note': [u'The Start Height Factor is the Start Height divided by the window or door height.', u'Start Height is the distance between the bottom of the window or door and the', u'bottom of the window or door opening. The sum of the Height Factor and the Start Height', u'Factor must be less than 1.0 in order to have the opening within the window or door', u'dimensions.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Start Height Factor for Opening Factor 2`
                Units: dimensionless
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `start_height_factor_for_opening_factor_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `start_height_factor_for_opening_factor_2`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `start_height_factor_for_opening_factor_2`')
        self._data["Start Height Factor for Opening Factor 2"] = value

    @property
    def opening_factor_3(self):
        """Get opening_factor_3

        Returns:
            float: the value of `opening_factor_3` or None if not set
        """
        return self._data["Opening Factor 3"]

    @opening_factor_3.setter
    def opening_factor_3(self, value=None):
        """  Corresponds to IDD Field `Opening Factor 3`
        If Number of Sets of Opening Factor Data = 3, this value must be 1.0.
        If Number of Sets of Opening Factor Data = 4, this value must be less than 1.0,
        and greater than value entered for Opening factor 2.
        
        {'pytype': 'float', u'maximum': '1.0', u'note': [u'If Number of Sets of Opening Factor Data = 3, this value must be 1.0.', u'If Number of Sets of Opening Factor Data = 4, this value must be less than 1.0,', u'and greater than value entered for Opening factor 2.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Opening Factor 3`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `opening_factor_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `opening_factor_3`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `opening_factor_3`')
        self._data["Opening Factor 3"] = value

    @property
    def discharge_coefficient_for_opening_factor_3(self):
        """Get discharge_coefficient_for_opening_factor_3

        Returns:
            float: the value of `discharge_coefficient_for_opening_factor_3` or None if not set
        """
        return self._data["Discharge Coefficient for Opening Factor 3"]

    @discharge_coefficient_for_opening_factor_3.setter
    def discharge_coefficient_for_opening_factor_3(self, value=0.0 ):
        """  Corresponds to IDD Field `Discharge Coefficient for Opening Factor 3`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through a window or door at that Opening Factor.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Discharge Coefficient indicates the fractional effectiveness', u'for air flow through a window or door at that Opening Factor.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Opening Factor 3`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `discharge_coefficient_for_opening_factor_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `discharge_coefficient_for_opening_factor_3`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `discharge_coefficient_for_opening_factor_3`')
        self._data["Discharge Coefficient for Opening Factor 3"] = value

    @property
    def width_factor_for_opening_factor_3(self):
        """Get width_factor_for_opening_factor_3

        Returns:
            float: the value of `width_factor_for_opening_factor_3` or None if not set
        """
        return self._data["Width Factor for Opening Factor 3"]

    @width_factor_for_opening_factor_3.setter
    def width_factor_for_opening_factor_3(self, value=0.0 ):
        """  Corresponds to IDD Field `Width Factor for Opening Factor 3`
        The Width Factor is the opening width divided by the window or door width.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Width Factor is the opening width divided by the window or door width.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Width Factor for Opening Factor 3`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `width_factor_for_opening_factor_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `width_factor_for_opening_factor_3`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `width_factor_for_opening_factor_3`')
        self._data["Width Factor for Opening Factor 3"] = value

    @property
    def height_factor_for_opening_factor_3(self):
        """Get height_factor_for_opening_factor_3

        Returns:
            float: the value of `height_factor_for_opening_factor_3` or None if not set
        """
        return self._data["Height Factor for Opening Factor 3"]

    @height_factor_for_opening_factor_3.setter
    def height_factor_for_opening_factor_3(self, value=0.0 ):
        """  Corresponds to IDD Field `Height Factor for Opening Factor 3`
        The Height Factor is the opening height divided by the window or door height.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Height Factor is the opening height divided by the window or door height.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Height Factor for Opening Factor 3`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `height_factor_for_opening_factor_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `height_factor_for_opening_factor_3`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `height_factor_for_opening_factor_3`')
        self._data["Height Factor for Opening Factor 3"] = value

    @property
    def start_height_factor_for_opening_factor_3(self):
        """Get start_height_factor_for_opening_factor_3

        Returns:
            float: the value of `start_height_factor_for_opening_factor_3` or None if not set
        """
        return self._data["Start Height Factor for Opening Factor 3"]

    @start_height_factor_for_opening_factor_3.setter
    def start_height_factor_for_opening_factor_3(self, value=0.0 ):
        """  Corresponds to IDD Field `Start Height Factor for Opening Factor 3`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Start Height Factor is the Start Height divided by the window or door height.', u'Start Height is the distance between the bottom of the window or door and the', u'bottom of the window or door opening. The sum of the Height Factor and the Start Height', u'Factor must be less than 1.0 in order to have the opening within the window or door', u'dimensions.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Start Height Factor for Opening Factor 3`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `start_height_factor_for_opening_factor_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `start_height_factor_for_opening_factor_3`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `start_height_factor_for_opening_factor_3`')
        self._data["Start Height Factor for Opening Factor 3"] = value

    @property
    def opening_factor_4(self):
        """Get opening_factor_4

        Returns:
            float: the value of `opening_factor_4` or None if not set
        """
        return self._data["Opening Factor 4"]

    @opening_factor_4.setter
    def opening_factor_4(self, value=None):
        """  Corresponds to IDD Field `Opening Factor 4`
        If Number of Sets of Opening Factor Data = 4, this value must be 1.0
        
        {'pytype': 'float', u'maximum': '1.0', u'note': [u'If Number of Sets of Opening Factor Data = 4, this value must be 1.0'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Opening Factor 4`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `opening_factor_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `opening_factor_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `opening_factor_4`')
        self._data["Opening Factor 4"] = value

    @property
    def discharge_coefficient_for_opening_factor_4(self):
        """Get discharge_coefficient_for_opening_factor_4

        Returns:
            float: the value of `discharge_coefficient_for_opening_factor_4` or None if not set
        """
        return self._data["Discharge Coefficient for Opening Factor 4"]

    @discharge_coefficient_for_opening_factor_4.setter
    def discharge_coefficient_for_opening_factor_4(self, value=0.0 ):
        """  Corresponds to IDD Field `Discharge Coefficient for Opening Factor 4`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through a window or door at that Opening Factor.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Discharge Coefficient indicates the fractional effectiveness', u'for air flow through a window or door at that Opening Factor.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Opening Factor 4`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `discharge_coefficient_for_opening_factor_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `discharge_coefficient_for_opening_factor_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `discharge_coefficient_for_opening_factor_4`')
        self._data["Discharge Coefficient for Opening Factor 4"] = value

    @property
    def width_factor_for_opening_factor_4(self):
        """Get width_factor_for_opening_factor_4

        Returns:
            float: the value of `width_factor_for_opening_factor_4` or None if not set
        """
        return self._data["Width Factor for Opening Factor 4"]

    @width_factor_for_opening_factor_4.setter
    def width_factor_for_opening_factor_4(self, value=0.0 ):
        """  Corresponds to IDD Field `Width Factor for Opening Factor 4`
        The Width Factor is the opening width divided by the window or door width.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Width Factor is the opening width divided by the window or door width.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Width Factor for Opening Factor 4`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `width_factor_for_opening_factor_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `width_factor_for_opening_factor_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `width_factor_for_opening_factor_4`')
        self._data["Width Factor for Opening Factor 4"] = value

    @property
    def height_factor_for_opening_factor_4(self):
        """Get height_factor_for_opening_factor_4

        Returns:
            float: the value of `height_factor_for_opening_factor_4` or None if not set
        """
        return self._data["Height Factor for Opening Factor 4"]

    @height_factor_for_opening_factor_4.setter
    def height_factor_for_opening_factor_4(self, value=0.0 ):
        """  Corresponds to IDD Field `Height Factor for Opening Factor 4`
        The Height Factor is the opening height divided by the window or door height.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Height Factor is the opening height divided by the window or door height.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Height Factor for Opening Factor 4`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `height_factor_for_opening_factor_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `height_factor_for_opening_factor_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `height_factor_for_opening_factor_4`')
        self._data["Height Factor for Opening Factor 4"] = value

    @property
    def start_height_factor_for_opening_factor_4(self):
        """Get start_height_factor_for_opening_factor_4

        Returns:
            float: the value of `start_height_factor_for_opening_factor_4` or None if not set
        """
        return self._data["Start Height Factor for Opening Factor 4"]

    @start_height_factor_for_opening_factor_4.setter
    def start_height_factor_for_opening_factor_4(self, value=0.0 ):
        """  Corresponds to IDD Field `Start Height Factor for Opening Factor 4`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.
        
        {'pytype': 'float', u'default': '0.0', u'maximum': '1.0', u'note': [u'The Start Height Factor is the Start Height divided by the window or door height.', u'Start Height is the distance between the bottom of the window or door and the', u'bottom of the window or door opening. The sum of the Height Factor and the Start Height', u'Factor must be less than 1.0 in order to have the opening within the window or door', u'dimensions.'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Start Height Factor for Opening Factor 4`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `start_height_factor_for_opening_factor_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `start_height_factor_for_opening_factor_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `start_height_factor_for_opening_factor_4`')
        self._data["Start Height Factor for Opening Factor 4"] = value

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

class AirflowNetworkMultiZoneComponentSimpleOpening(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:SimpleOpening`
        This object specifies the properties of air flow through windows and doors (window, door and
        glass door heat transfer subsurfaces) when they are closed or open.
    
    """
    internal_name = "AirflowNetwork:MultiZone:Component:SimpleOpening"
    field_count = 5
    required_fields = ["Name", "Air Mass Flow Coefficient When Opening is Closed", "Minimum Density Difference for Two-Way Flow", "Discharge Coefficient"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:Component:SimpleOpening`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient When Opening is Closed"] = None
        self._data["Air Mass Flow Exponent When Opening is Closed"] = None
        self._data["Minimum Density Difference for Two-Way Flow"] = None
        self._data["Discharge Coefficient"] = None
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
            self.air_mass_flow_coefficient_when_opening_is_closed = None
        else:
            self.air_mass_flow_coefficient_when_opening_is_closed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent_when_opening_is_closed = None
        else:
            self.air_mass_flow_exponent_when_opening_is_closed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_density_difference_for_twoway_flow = None
        else:
            self.minimum_density_difference_for_twoway_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharge_coefficient = None
        else:
            self.discharge_coefficient = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'SurfaceAirflowLeakageNames', u'required-field': True, 'pytype': 'str'}

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
    def air_mass_flow_coefficient_when_opening_is_closed(self):
        """Get air_mass_flow_coefficient_when_opening_is_closed

        Returns:
            float: the value of `air_mass_flow_coefficient_when_opening_is_closed` or None if not set
        """
        return self._data["Air Mass Flow Coefficient When Opening is Closed"]

    @air_mass_flow_coefficient_when_opening_is_closed.setter
    def air_mass_flow_coefficient_when_opening_is_closed(self, value=None):
        """  Corresponds to IDD Field `Air Mass Flow Coefficient When Opening is Closed`
        Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation:', u'Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.', u'Used only when opening (window or door) is closed.'], u'units': u'kg/s-m', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient When Opening is Closed`
                Units: kg/s-m
                value > 0.0
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
                                 'for field `air_mass_flow_coefficient_when_opening_is_closed`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_mass_flow_coefficient_when_opening_is_closed`')
        self._data["Air Mass Flow Coefficient When Opening is Closed"] = value

    @property
    def air_mass_flow_exponent_when_opening_is_closed(self):
        """Get air_mass_flow_exponent_when_opening_is_closed

        Returns:
            float: the value of `air_mass_flow_exponent_when_opening_is_closed` or None if not set
        """
        return self._data["Air Mass Flow Exponent When Opening is Closed"]

    @air_mass_flow_exponent_when_opening_is_closed.setter
    def air_mass_flow_exponent_when_opening_is_closed(self, value=0.65 ):
        """  Corresponds to IDD Field `Air Mass Flow Exponent When Opening is Closed`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.
        
        {'pytype': 'float', u'default': '0.65', u'maximum': '1.0', u'note': [u'Enter the exponent used in the following equation:', u'Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.', u'Used only when opening (window or door) is closed.'], u'minimum': '0.5', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent When Opening is Closed`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
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
                                 'for field `air_mass_flow_exponent_when_opening_is_closed`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent_when_opening_is_closed`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent_when_opening_is_closed`')
        self._data["Air Mass Flow Exponent When Opening is Closed"] = value

    @property
    def minimum_density_difference_for_twoway_flow(self):
        """Get minimum_density_difference_for_twoway_flow

        Returns:
            float: the value of `minimum_density_difference_for_twoway_flow` or None if not set
        """
        return self._data["Minimum Density Difference for Two-Way Flow"]

    @minimum_density_difference_for_twoway_flow.setter
    def minimum_density_difference_for_twoway_flow(self, value=None):
        """  Corresponds to IDD Field `Minimum Density Difference for Two-Way Flow`
        Enter the minimum density difference above which two-way flow may occur due to stack effect.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the minimum density difference above which two-way flow may occur due to stack effect.'], u'units': u'kg/m3', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Minimum Density Difference for Two-Way Flow`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_density_difference_for_twoway_flow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_density_difference_for_twoway_flow`')
        self._data["Minimum Density Difference for Two-Way Flow"] = value

    @property
    def discharge_coefficient(self):
        """Get discharge_coefficient

        Returns:
            float: the value of `discharge_coefficient` or None if not set
        """
        return self._data["Discharge Coefficient"]

    @discharge_coefficient.setter
    def discharge_coefficient(self, value=None):
        """  Corresponds to IDD Field `Discharge Coefficient`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through a window or door at that Opening Factor.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'The Discharge Coefficient indicates the fractional effectiveness', u'for air flow through a window or door at that Opening Factor.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Discharge Coefficient`
                Units: dimensionless
                value > 0.0
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
                                 'for field `discharge_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `discharge_coefficient`')
        self._data["Discharge Coefficient"] = value

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

class AirflowNetworkMultiZoneComponentHorizontalOpening(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:HorizontalOpening`
        This object specifies the properties of air flow through a horizontal opening
    
    """
    internal_name = "AirflowNetwork:MultiZone:Component:HorizontalOpening"
    field_count = 5
    required_fields = ["Name", "Air Mass Flow Coefficient When Opening is Closed", "Discharge Coefficient"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:Component:HorizontalOpening`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient When Opening is Closed"] = None
        self._data["Air Mass Flow Exponent When Opening is Closed"] = None
        self._data["Sloping Plane Angle"] = None
        self._data["Discharge Coefficient"] = None
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
            self.air_mass_flow_coefficient_when_opening_is_closed = None
        else:
            self.air_mass_flow_coefficient_when_opening_is_closed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent_when_opening_is_closed = None
        else:
            self.air_mass_flow_exponent_when_opening_is_closed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sloping_plane_angle = None
        else:
            self.sloping_plane_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharge_coefficient = None
        else:
            self.discharge_coefficient = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'SurfaceAirflowLeakageNames', u'required-field': True, 'pytype': 'str'}

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
    def air_mass_flow_coefficient_when_opening_is_closed(self):
        """Get air_mass_flow_coefficient_when_opening_is_closed

        Returns:
            float: the value of `air_mass_flow_coefficient_when_opening_is_closed` or None if not set
        """
        return self._data["Air Mass Flow Coefficient When Opening is Closed"]

    @air_mass_flow_coefficient_when_opening_is_closed.setter
    def air_mass_flow_coefficient_when_opening_is_closed(self, value=None):
        """  Corresponds to IDD Field `Air Mass Flow Coefficient When Opening is Closed`
        Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation:
        Mass flow rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening is closed.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation:', u'Mass flow rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.', u'Used only when opening is closed.'], u'units': u'kg/s-m', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient When Opening is Closed`
                Units: kg/s-m
                value > 0.0
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
                                 'for field `air_mass_flow_coefficient_when_opening_is_closed`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_mass_flow_coefficient_when_opening_is_closed`')
        self._data["Air Mass Flow Coefficient When Opening is Closed"] = value

    @property
    def air_mass_flow_exponent_when_opening_is_closed(self):
        """Get air_mass_flow_exponent_when_opening_is_closed

        Returns:
            float: the value of `air_mass_flow_exponent_when_opening_is_closed` or None if not set
        """
        return self._data["Air Mass Flow Exponent When Opening is Closed"]

    @air_mass_flow_exponent_when_opening_is_closed.setter
    def air_mass_flow_exponent_when_opening_is_closed(self, value=0.65 ):
        """  Corresponds to IDD Field `Air Mass Flow Exponent When Opening is Closed`
        Enter the exponent used in the following equation:
        Mass flow rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening is closed.
        
        {'pytype': 'float', u'default': '0.65', u'maximum': '1.0', u'note': [u'Enter the exponent used in the following equation:', u'Mass flow rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.', u'Used only when opening is closed.'], u'minimum': '0.5', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent When Opening is Closed`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
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
                                 'for field `air_mass_flow_exponent_when_opening_is_closed`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent_when_opening_is_closed`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent_when_opening_is_closed`')
        self._data["Air Mass Flow Exponent When Opening is Closed"] = value

    @property
    def sloping_plane_angle(self):
        """Get sloping_plane_angle

        Returns:
            float: the value of `sloping_plane_angle` or None if not set
        """
        return self._data["Sloping Plane Angle"]

    @sloping_plane_angle.setter
    def sloping_plane_angle(self, value=90.0 ):
        """  Corresponds to IDD Field `Sloping Plane Angle`
        Sloping plane angle = 90 is equivalent to fully open.
        
        {'pytype': 'float', u'default': '90.0', u'minimum>': '0.0', u'maximum': '90.0', u'note': [u'Sloping plane angle = 90 is equivalent to fully open.'], u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Sloping Plane Angle`
                Units: deg
                Default value: 90.0
                value > 0.0
                value <= 90.0
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
                                 'for field `sloping_plane_angle`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `sloping_plane_angle`')
            if value > 90.0:
                raise ValueError('value need to be smaller 90.0 '
                                 'for field `sloping_plane_angle`')
        self._data["Sloping Plane Angle"] = value

    @property
    def discharge_coefficient(self):
        """Get discharge_coefficient

        Returns:
            float: the value of `discharge_coefficient` or None if not set
        """
        return self._data["Discharge Coefficient"]

    @discharge_coefficient.setter
    def discharge_coefficient(self, value=None):
        """  Corresponds to IDD Field `Discharge Coefficient`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through the opening at that Opening Factor.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'The Discharge Coefficient indicates the fractional effectiveness', u'for air flow through the opening at that Opening Factor.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Discharge Coefficient`
                Units: dimensionless
                value > 0.0
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
                                 'for field `discharge_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `discharge_coefficient`')
        self._data["Discharge Coefficient"] = value

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

class AirflowNetworkMultiZoneComponentZoneExhaustFan(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:ZoneExhaustFan`
        This object specifies the additional properties for a zone exhaust fan
        to perform multizone airflow calculations.
    
    """
    internal_name = "AirflowNetwork:MultiZone:Component:ZoneExhaustFan"
    field_count = 4
    required_fields = ["Name", "Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:Component:ZoneExhaustFan`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions"] = None
        self._data["Air Mass Flow Exponent When the Zone Exhaust Fan is Off"] = None
        self._data["Reference Crack Conditions"] = None
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
            self.air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions = None
        else:
            self.air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off = None
        else:
            self.air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_crack_conditions = None
        else:
            self.reference_crack_conditions = vals[i]
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
        Enter the name of a Fan:ZoneExhaust object.
        
        {u'note': [u'Enter the name of a Fan:ZoneExhaust object.'], u'type': u'object-list', u'object-list': u'FansZoneExhaust', u'required-field': True, 'pytype': 'str'}

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
    def air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions(self):
        """Get air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions

        Returns:
            float: the value of `air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions` or None if not set
        """
        return self._data["Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions"]

    @air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions.setter
    def air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions(self, value=None):
        """  Corresponds to IDD Field `Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions`
        Enter the air mass flow coefficient at the conditions defined
        in the Reference Crack Conditions object.
        Defined at 1 Pa pressure difference. Enter the coefficient used in the following
        equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when the fan is off.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the air mass flow coefficient at the conditions defined', u'in the Reference Crack Conditions object.', u'Defined at 1 Pa pressure difference. Enter the coefficient used in the following', u'equation:', u'Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.', u'Used only when the fan is off.'], u'units': u'kg/s', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions`
                Units: kg/s
                value > 0.0
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
                                 'for field `air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions`')
        self._data["Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions"] = value

    @property
    def air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off(self):
        """Get air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off

        Returns:
            float: the value of `air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off` or None if not set
        """
        return self._data["Air Mass Flow Exponent When the Zone Exhaust Fan is Off"]

    @air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off.setter
    def air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off(self, value=0.65 ):
        """  Corresponds to IDD Field `Air Mass Flow Exponent When the Zone Exhaust Fan is Off`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when the fan is off.
        
        {'pytype': 'float', u'default': '0.65', u'maximum': '1.0', u'note': [u'Enter the exponent used in the following equation:', u'Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.', u'Used only when the fan is off.'], u'minimum': '0.5', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent When the Zone Exhaust Fan is Off`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
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
                                 'for field `air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off`')
        self._data["Air Mass Flow Exponent When the Zone Exhaust Fan is Off"] = value

    @property
    def reference_crack_conditions(self):
        """Get reference_crack_conditions

        Returns:
            str: the value of `reference_crack_conditions` or None if not set
        """
        return self._data["Reference Crack Conditions"]

    @reference_crack_conditions.setter
    def reference_crack_conditions(self, value=None):
        """  Corresponds to IDD Field `Reference Crack Conditions`
        Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with
        the air mass flow coefficient entered above.
        
        {u'note': [u'Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with', u'the air mass flow coefficient entered above.'], u'type': u'object-list', u'object-list': u'ReferenceCrackConditions', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Reference Crack Conditions`
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
                                 'for field `reference_crack_conditions`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_crack_conditions`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reference_crack_conditions`')
        self._data["Reference Crack Conditions"] = value

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

class AirflowNetworkMultiZoneExternalNode(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:ExternalNode`
        This object defines outdoor environmental conditions outside of the building.
    
    """
    internal_name = "AirflowNetwork:MultiZone:ExternalNode"
    field_count = 3
    required_fields = ["Name", "Wind Pressure Coefficient Values Object Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:ExternalNode`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["External Node Height"] = None
        self._data["Wind Pressure Coefficient Values Object Name"] = None
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
            self.external_node_height = None
        else:
            self.external_node_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_values_object_name = None
        else:
            self.wind_pressure_coefficient_values_object_name = vals[i]
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
        Enter a unique name for this object.
        This node name will be referenced by a particular building facade.
        
        {u'note': [u'Enter a unique name for this object.', u'This node name will be referenced by a particular building facade.'], u'type': u'alpha', u'reference': u'ExternalNodeNames', u'required-field': True, 'pytype': 'str'}

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
    def external_node_height(self):
        """Get external_node_height

        Returns:
            float: the value of `external_node_height` or None if not set
        """
        return self._data["External Node Height"]

    @external_node_height.setter
    def external_node_height(self, value=0.0 ):
        """  Corresponds to IDD Field `External Node Height`
        Designates the reference height used to calculate relative pressure.
        
        {u'units': u'm', u'default': '0.0', u'note': [u'Designates the reference height used to calculate relative pressure.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `External Node Height`
                Units: m
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
                                 'for field `external_node_height`'.format(value))
        self._data["External Node Height"] = value

    @property
    def wind_pressure_coefficient_values_object_name(self):
        """Get wind_pressure_coefficient_values_object_name

        Returns:
            str: the value of `wind_pressure_coefficient_values_object_name` or None if not set
        """
        return self._data["Wind Pressure Coefficient Values Object Name"]

    @wind_pressure_coefficient_values_object_name.setter
    def wind_pressure_coefficient_values_object_name(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Values Object Name`
        Enter the name of the AirflowNetwork:MultiZone:WindPressureCoefficientValues object.
        
        {u'note': [u'Enter the name of the AirflowNetwork:MultiZone:WindPressureCoefficientValues object.'], u'type': u'object-list', u'object-list': u'WPCValueNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Wind Pressure Coefficient Values Object Name`
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
                                 'for field `wind_pressure_coefficient_values_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_pressure_coefficient_values_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `wind_pressure_coefficient_values_object_name`')
        self._data["Wind Pressure Coefficient Values Object Name"] = value

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

class AirflowNetworkMultiZoneWindPressureCoefficientArray(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:WindPressureCoefficientArray`
        Used only if Wind Pressure Coefficient (WPC) Type = Input in the AirflowNetwork:SimulationControl
        object. Number of WPC Values in the corresponding AirflowNetwork:MultiZone:WindPressureCoefficientValues
        object must be the same as the number of wind directions specified for
        this AirflowNetwork:MultiZone:WindPressureCoefficientArray object.
    
    """
    internal_name = "AirflowNetwork:MultiZone:WindPressureCoefficientArray"
    field_count = 37
    required_fields = ["Name", "Wind Direction 1", "Wind Direction 2"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:WindPressureCoefficientArray`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Wind Direction 1"] = None
        self._data["Wind Direction 2"] = None
        self._data["Wind Direction 3"] = None
        self._data["Wind Direction 4"] = None
        self._data["Wind Direction 5"] = None
        self._data["Wind Direction 6"] = None
        self._data["Wind Direction 7"] = None
        self._data["Wind Direction 8"] = None
        self._data["Wind Direction 9"] = None
        self._data["Wind Direction 10"] = None
        self._data["Wind Direction 11"] = None
        self._data["Wind Direction 12"] = None
        self._data["Wind Direction 13"] = None
        self._data["Wind Direction 14"] = None
        self._data["Wind Direction 15"] = None
        self._data["Wind Direction 16"] = None
        self._data["Wind Direction 17"] = None
        self._data["Wind Direction 18"] = None
        self._data["Wind Direction 19"] = None
        self._data["Wind Direction 20"] = None
        self._data["Wind Direction 21"] = None
        self._data["Wind Direction 22"] = None
        self._data["Wind Direction 23"] = None
        self._data["Wind Direction 24"] = None
        self._data["Wind Direction 25"] = None
        self._data["Wind Direction 26"] = None
        self._data["Wind Direction 27"] = None
        self._data["Wind Direction 28"] = None
        self._data["Wind Direction 29"] = None
        self._data["Wind Direction 30"] = None
        self._data["Wind Direction 31"] = None
        self._data["Wind Direction 32"] = None
        self._data["Wind Direction 33"] = None
        self._data["Wind Direction 34"] = None
        self._data["Wind Direction 35"] = None
        self._data["Wind Direction 36"] = None
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
            self.wind_direction_1 = None
        else:
            self.wind_direction_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_2 = None
        else:
            self.wind_direction_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_3 = None
        else:
            self.wind_direction_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_4 = None
        else:
            self.wind_direction_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_5 = None
        else:
            self.wind_direction_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_6 = None
        else:
            self.wind_direction_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_7 = None
        else:
            self.wind_direction_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_8 = None
        else:
            self.wind_direction_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_9 = None
        else:
            self.wind_direction_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_10 = None
        else:
            self.wind_direction_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_11 = None
        else:
            self.wind_direction_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_12 = None
        else:
            self.wind_direction_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_13 = None
        else:
            self.wind_direction_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_14 = None
        else:
            self.wind_direction_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_15 = None
        else:
            self.wind_direction_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_16 = None
        else:
            self.wind_direction_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_17 = None
        else:
            self.wind_direction_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_18 = None
        else:
            self.wind_direction_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_19 = None
        else:
            self.wind_direction_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_20 = None
        else:
            self.wind_direction_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_21 = None
        else:
            self.wind_direction_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_22 = None
        else:
            self.wind_direction_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_23 = None
        else:
            self.wind_direction_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_24 = None
        else:
            self.wind_direction_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_25 = None
        else:
            self.wind_direction_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_26 = None
        else:
            self.wind_direction_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_27 = None
        else:
            self.wind_direction_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_28 = None
        else:
            self.wind_direction_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_29 = None
        else:
            self.wind_direction_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_30 = None
        else:
            self.wind_direction_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_31 = None
        else:
            self.wind_direction_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_32 = None
        else:
            self.wind_direction_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_33 = None
        else:
            self.wind_direction_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_34 = None
        else:
            self.wind_direction_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_35 = None
        else:
            self.wind_direction_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_direction_36 = None
        else:
            self.wind_direction_36 = vals[i]
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
        Enter a unique name for the object.
        
        {u'note': [u'Enter a unique name for the object.'], u'type': u'alpha', u'reference': u'WPCSetNames', u'required-field': True, 'pytype': 'str'}

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
    def wind_direction_1(self):
        """Get wind_direction_1

        Returns:
            float: the value of `wind_direction_1` or None if not set
        """
        return self._data["Wind Direction 1"]

    @wind_direction_1.setter
    def wind_direction_1(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 1`
        Enter the wind direction corresponding to the 1st WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'required-field': True, u'note': [u'Enter the wind direction corresponding to the 1st WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 1`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_1`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_1`')
        self._data["Wind Direction 1"] = value

    @property
    def wind_direction_2(self):
        """Get wind_direction_2

        Returns:
            float: the value of `wind_direction_2` or None if not set
        """
        return self._data["Wind Direction 2"]

    @wind_direction_2.setter
    def wind_direction_2(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 2`
        Enter the wind direction corresponding to the 2nd WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'required-field': True, u'note': [u'Enter the wind direction corresponding to the 2nd WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 2`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_2`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_2`')
        self._data["Wind Direction 2"] = value

    @property
    def wind_direction_3(self):
        """Get wind_direction_3

        Returns:
            float: the value of `wind_direction_3` or None if not set
        """
        return self._data["Wind Direction 3"]

    @wind_direction_3.setter
    def wind_direction_3(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 3`
        Enter the wind direction corresponding to the 3rd WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 3rd WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 3`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_3`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_3`')
        self._data["Wind Direction 3"] = value

    @property
    def wind_direction_4(self):
        """Get wind_direction_4

        Returns:
            float: the value of `wind_direction_4` or None if not set
        """
        return self._data["Wind Direction 4"]

    @wind_direction_4.setter
    def wind_direction_4(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 4`
        Enter the wind direction corresponding to the 4th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 4th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 4`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_4`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_4`')
        self._data["Wind Direction 4"] = value

    @property
    def wind_direction_5(self):
        """Get wind_direction_5

        Returns:
            float: the value of `wind_direction_5` or None if not set
        """
        return self._data["Wind Direction 5"]

    @wind_direction_5.setter
    def wind_direction_5(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 5`
        Enter the wind direction corresponding to the 5th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 5th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 5`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_5`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_5`')
        self._data["Wind Direction 5"] = value

    @property
    def wind_direction_6(self):
        """Get wind_direction_6

        Returns:
            float: the value of `wind_direction_6` or None if not set
        """
        return self._data["Wind Direction 6"]

    @wind_direction_6.setter
    def wind_direction_6(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 6`
        Enter the wind direction corresponding to the 6th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 6th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 6`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_6`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_6`')
        self._data["Wind Direction 6"] = value

    @property
    def wind_direction_7(self):
        """Get wind_direction_7

        Returns:
            float: the value of `wind_direction_7` or None if not set
        """
        return self._data["Wind Direction 7"]

    @wind_direction_7.setter
    def wind_direction_7(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 7`
        Enter the wind direction corresponding to the 7th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 7th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 7`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_7`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_7`')
        self._data["Wind Direction 7"] = value

    @property
    def wind_direction_8(self):
        """Get wind_direction_8

        Returns:
            float: the value of `wind_direction_8` or None if not set
        """
        return self._data["Wind Direction 8"]

    @wind_direction_8.setter
    def wind_direction_8(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 8`
        Enter the wind direction corresponding to the 8th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 8th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 8`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_8`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_8`')
        self._data["Wind Direction 8"] = value

    @property
    def wind_direction_9(self):
        """Get wind_direction_9

        Returns:
            float: the value of `wind_direction_9` or None if not set
        """
        return self._data["Wind Direction 9"]

    @wind_direction_9.setter
    def wind_direction_9(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 9`
        Enter the wind direction corresponding to the 9th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 9th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 9`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_9`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_9`')
        self._data["Wind Direction 9"] = value

    @property
    def wind_direction_10(self):
        """Get wind_direction_10

        Returns:
            float: the value of `wind_direction_10` or None if not set
        """
        return self._data["Wind Direction 10"]

    @wind_direction_10.setter
    def wind_direction_10(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 10`
        Enter the wind direction corresponding to the 10th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 10th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 10`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_10`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_10`')
        self._data["Wind Direction 10"] = value

    @property
    def wind_direction_11(self):
        """Get wind_direction_11

        Returns:
            float: the value of `wind_direction_11` or None if not set
        """
        return self._data["Wind Direction 11"]

    @wind_direction_11.setter
    def wind_direction_11(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 11`
        Enter the wind direction corresponding to the 11th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 11th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 11`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_11`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_11`')
        self._data["Wind Direction 11"] = value

    @property
    def wind_direction_12(self):
        """Get wind_direction_12

        Returns:
            float: the value of `wind_direction_12` or None if not set
        """
        return self._data["Wind Direction 12"]

    @wind_direction_12.setter
    def wind_direction_12(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 12`
        Enter the wind direction corresponding to the 12th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 12th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 12`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_12`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_12`')
        self._data["Wind Direction 12"] = value

    @property
    def wind_direction_13(self):
        """Get wind_direction_13

        Returns:
            float: the value of `wind_direction_13` or None if not set
        """
        return self._data["Wind Direction 13"]

    @wind_direction_13.setter
    def wind_direction_13(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 13`
        Enter the wind direction corresponding to the 13th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 13th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 13`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_13`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_13`')
        self._data["Wind Direction 13"] = value

    @property
    def wind_direction_14(self):
        """Get wind_direction_14

        Returns:
            float: the value of `wind_direction_14` or None if not set
        """
        return self._data["Wind Direction 14"]

    @wind_direction_14.setter
    def wind_direction_14(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 14`
        Enter the wind direction corresponding to the 14th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 14th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 14`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_14`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_14`')
        self._data["Wind Direction 14"] = value

    @property
    def wind_direction_15(self):
        """Get wind_direction_15

        Returns:
            float: the value of `wind_direction_15` or None if not set
        """
        return self._data["Wind Direction 15"]

    @wind_direction_15.setter
    def wind_direction_15(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 15`
        Enter the wind direction corresponding to the 15th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 15th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 15`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_15`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_15`')
        self._data["Wind Direction 15"] = value

    @property
    def wind_direction_16(self):
        """Get wind_direction_16

        Returns:
            float: the value of `wind_direction_16` or None if not set
        """
        return self._data["Wind Direction 16"]

    @wind_direction_16.setter
    def wind_direction_16(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 16`
        Enter the wind direction corresponding to the 16th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 16th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 16`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_16`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_16`')
        self._data["Wind Direction 16"] = value

    @property
    def wind_direction_17(self):
        """Get wind_direction_17

        Returns:
            float: the value of `wind_direction_17` or None if not set
        """
        return self._data["Wind Direction 17"]

    @wind_direction_17.setter
    def wind_direction_17(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 17`
        Enter the wind direction corresponding to the 17th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 17th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 17`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_17`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_17`')
        self._data["Wind Direction 17"] = value

    @property
    def wind_direction_18(self):
        """Get wind_direction_18

        Returns:
            float: the value of `wind_direction_18` or None if not set
        """
        return self._data["Wind Direction 18"]

    @wind_direction_18.setter
    def wind_direction_18(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 18`
        Enter the wind direction corresponding to the 18th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 18th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 18`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_18`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_18`')
        self._data["Wind Direction 18"] = value

    @property
    def wind_direction_19(self):
        """Get wind_direction_19

        Returns:
            float: the value of `wind_direction_19` or None if not set
        """
        return self._data["Wind Direction 19"]

    @wind_direction_19.setter
    def wind_direction_19(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 19`
        Enter the wind direction corresponding to the 19th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 19th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 19`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_19`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_19`')
        self._data["Wind Direction 19"] = value

    @property
    def wind_direction_20(self):
        """Get wind_direction_20

        Returns:
            float: the value of `wind_direction_20` or None if not set
        """
        return self._data["Wind Direction 20"]

    @wind_direction_20.setter
    def wind_direction_20(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 20`
        Enter the wind direction corresponding to the 20th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 20th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 20`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_20`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_20`')
        self._data["Wind Direction 20"] = value

    @property
    def wind_direction_21(self):
        """Get wind_direction_21

        Returns:
            float: the value of `wind_direction_21` or None if not set
        """
        return self._data["Wind Direction 21"]

    @wind_direction_21.setter
    def wind_direction_21(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 21`
        Enter the wind direction corresponding to the 21st WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 21st WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 21`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_21`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_21`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_21`')
        self._data["Wind Direction 21"] = value

    @property
    def wind_direction_22(self):
        """Get wind_direction_22

        Returns:
            float: the value of `wind_direction_22` or None if not set
        """
        return self._data["Wind Direction 22"]

    @wind_direction_22.setter
    def wind_direction_22(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 22`
        Enter the wind direction corresponding to the 22nd WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 22nd WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 22`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_22`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_22`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_22`')
        self._data["Wind Direction 22"] = value

    @property
    def wind_direction_23(self):
        """Get wind_direction_23

        Returns:
            float: the value of `wind_direction_23` or None if not set
        """
        return self._data["Wind Direction 23"]

    @wind_direction_23.setter
    def wind_direction_23(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 23`
        Enter the wind direction corresponding to the 23rd WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 23rd WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 23`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_23`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_23`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_23`')
        self._data["Wind Direction 23"] = value

    @property
    def wind_direction_24(self):
        """Get wind_direction_24

        Returns:
            float: the value of `wind_direction_24` or None if not set
        """
        return self._data["Wind Direction 24"]

    @wind_direction_24.setter
    def wind_direction_24(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 24`
        Enter the wind direction corresponding to the 24th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 24th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 24`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_24`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_24`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_24`')
        self._data["Wind Direction 24"] = value

    @property
    def wind_direction_25(self):
        """Get wind_direction_25

        Returns:
            float: the value of `wind_direction_25` or None if not set
        """
        return self._data["Wind Direction 25"]

    @wind_direction_25.setter
    def wind_direction_25(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 25`
        Enter the wind direction corresponding to the 25th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 25th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 25`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_25`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_25`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_25`')
        self._data["Wind Direction 25"] = value

    @property
    def wind_direction_26(self):
        """Get wind_direction_26

        Returns:
            float: the value of `wind_direction_26` or None if not set
        """
        return self._data["Wind Direction 26"]

    @wind_direction_26.setter
    def wind_direction_26(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 26`
        Enter the wind direction corresponding to the 26th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 26th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 26`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_26`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_26`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_26`')
        self._data["Wind Direction 26"] = value

    @property
    def wind_direction_27(self):
        """Get wind_direction_27

        Returns:
            float: the value of `wind_direction_27` or None if not set
        """
        return self._data["Wind Direction 27"]

    @wind_direction_27.setter
    def wind_direction_27(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 27`
        Enter the wind direction corresponding to the 27th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 27th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 27`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_27`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_27`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_27`')
        self._data["Wind Direction 27"] = value

    @property
    def wind_direction_28(self):
        """Get wind_direction_28

        Returns:
            float: the value of `wind_direction_28` or None if not set
        """
        return self._data["Wind Direction 28"]

    @wind_direction_28.setter
    def wind_direction_28(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 28`
        Enter the wind direction corresponding to the 28th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 28th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 28`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_28`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_28`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_28`')
        self._data["Wind Direction 28"] = value

    @property
    def wind_direction_29(self):
        """Get wind_direction_29

        Returns:
            float: the value of `wind_direction_29` or None if not set
        """
        return self._data["Wind Direction 29"]

    @wind_direction_29.setter
    def wind_direction_29(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 29`
        Enter the wind direction corresponding to the 29th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 29th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 29`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_29`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_29`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_29`')
        self._data["Wind Direction 29"] = value

    @property
    def wind_direction_30(self):
        """Get wind_direction_30

        Returns:
            float: the value of `wind_direction_30` or None if not set
        """
        return self._data["Wind Direction 30"]

    @wind_direction_30.setter
    def wind_direction_30(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 30`
        Enter the wind direction corresponding to the 30th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 30th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 30`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_30`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_30`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_30`')
        self._data["Wind Direction 30"] = value

    @property
    def wind_direction_31(self):
        """Get wind_direction_31

        Returns:
            float: the value of `wind_direction_31` or None if not set
        """
        return self._data["Wind Direction 31"]

    @wind_direction_31.setter
    def wind_direction_31(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 31`
        Enter the wind direction corresponding to the 31st WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 31st WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 31`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_31`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_31`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_31`')
        self._data["Wind Direction 31"] = value

    @property
    def wind_direction_32(self):
        """Get wind_direction_32

        Returns:
            float: the value of `wind_direction_32` or None if not set
        """
        return self._data["Wind Direction 32"]

    @wind_direction_32.setter
    def wind_direction_32(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 32`
        Enter the wind direction corresponding to the 32nd WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 32nd WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 32`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_32`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_32`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_32`')
        self._data["Wind Direction 32"] = value

    @property
    def wind_direction_33(self):
        """Get wind_direction_33

        Returns:
            float: the value of `wind_direction_33` or None if not set
        """
        return self._data["Wind Direction 33"]

    @wind_direction_33.setter
    def wind_direction_33(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 33`
        Enter the wind direction corresponding to the 33rd WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 33rd WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 33`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_33`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_33`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_33`')
        self._data["Wind Direction 33"] = value

    @property
    def wind_direction_34(self):
        """Get wind_direction_34

        Returns:
            float: the value of `wind_direction_34` or None if not set
        """
        return self._data["Wind Direction 34"]

    @wind_direction_34.setter
    def wind_direction_34(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 34`
        Enter the wind direction corresponding to the 34th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 34th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 34`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_34`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_34`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_34`')
        self._data["Wind Direction 34"] = value

    @property
    def wind_direction_35(self):
        """Get wind_direction_35

        Returns:
            float: the value of `wind_direction_35` or None if not set
        """
        return self._data["Wind Direction 35"]

    @wind_direction_35.setter
    def wind_direction_35(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 35`
        Enter the wind direction corresponding to the 35th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 35th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 35`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_35`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_35`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_35`')
        self._data["Wind Direction 35"] = value

    @property
    def wind_direction_36(self):
        """Get wind_direction_36

        Returns:
            float: the value of `wind_direction_36` or None if not set
        """
        return self._data["Wind Direction 36"]

    @wind_direction_36.setter
    def wind_direction_36(self, value=None):
        """  Corresponds to IDD Field `Wind Direction 36`
        Enter the wind direction corresponding to the 36th WPC Array value.
        
        {'pytype': 'float', u'maximum': '360.0', u'note': [u'Enter the wind direction corresponding to the 36th WPC Array value.'], u'minimum': '0.0', u'units': u'deg', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Wind Direction 36`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 'for field `wind_direction_36`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_36`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_36`')
        self._data["Wind Direction 36"] = value

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

class AirflowNetworkMultiZoneWindPressureCoefficientValues(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:WindPressureCoefficientValues`
        Used only if Wind Pressure Coefficient (WPC) Type = INPUT in the AirflowNetwork:SimulationControl
        object. The number of WPC numeric inputs must correspond to the number of wind direction
        inputs in the AirflowNetwork:Multizone:WindPressureCoefficientArray object.
    
    """
    internal_name = "AirflowNetwork:MultiZone:WindPressureCoefficientValues"
    field_count = 38
    required_fields = ["Name", "AirflowNetwork:MultiZone:WindPressureCoefficientArray Name", "Wind Pressure Coefficient Value 1", "Wind Pressure Coefficient Value 2"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:MultiZone:WindPressureCoefficientValues`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["AirflowNetwork:MultiZone:WindPressureCoefficientArray Name"] = None
        self._data["Wind Pressure Coefficient Value 1"] = None
        self._data["Wind Pressure Coefficient Value 2"] = None
        self._data["Wind Pressure Coefficient Value 3"] = None
        self._data["Wind Pressure Coefficient Value 4"] = None
        self._data["Wind Pressure Coefficient Value 5"] = None
        self._data["Wind Pressure Coefficient Value 6"] = None
        self._data["Wind Pressure Coefficient Value 7"] = None
        self._data["Wind Pressure Coefficient Value 8"] = None
        self._data["Wind Pressure Coefficient Value 9"] = None
        self._data["Wind Pressure Coefficient Value 10"] = None
        self._data["Wind Pressure Coefficient Value 11"] = None
        self._data["Wind Pressure Coefficient Value 12"] = None
        self._data["Wind Pressure Coefficient Value 13"] = None
        self._data["Wind Pressure Coefficient Value 14"] = None
        self._data["Wind Pressure Coefficient Value 15"] = None
        self._data["Wind Pressure Coefficient Value 16"] = None
        self._data["Wind Pressure Coefficient Value 17"] = None
        self._data["Wind Pressure Coefficient Value 18"] = None
        self._data["Wind Pressure Coefficient Value 19"] = None
        self._data["Wind Pressure Coefficient Value 20"] = None
        self._data["Wind Pressure Coefficient Value 21"] = None
        self._data["Wind Pressure Coefficient Value 22"] = None
        self._data["Wind Pressure Coefficient Value 23"] = None
        self._data["Wind Pressure Coefficient Value 24"] = None
        self._data["Wind Pressure Coefficient Value 25"] = None
        self._data["Wind Pressure Coefficient Value 26"] = None
        self._data["Wind Pressure Coefficient Value 27"] = None
        self._data["Wind Pressure Coefficient Value 28"] = None
        self._data["Wind Pressure Coefficient Value 29"] = None
        self._data["Wind Pressure Coefficient Value 30"] = None
        self._data["Wind Pressure Coefficient Value 31"] = None
        self._data["Wind Pressure Coefficient Value 32"] = None
        self._data["Wind Pressure Coefficient Value 33"] = None
        self._data["Wind Pressure Coefficient Value 34"] = None
        self._data["Wind Pressure Coefficient Value 35"] = None
        self._data["Wind Pressure Coefficient Value 36"] = None
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
            self.airflownetworkmultizonewindpressurecoefficientarray_name = None
        else:
            self.airflownetworkmultizonewindpressurecoefficientarray_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_1 = None
        else:
            self.wind_pressure_coefficient_value_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_2 = None
        else:
            self.wind_pressure_coefficient_value_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_3 = None
        else:
            self.wind_pressure_coefficient_value_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_4 = None
        else:
            self.wind_pressure_coefficient_value_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_5 = None
        else:
            self.wind_pressure_coefficient_value_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_6 = None
        else:
            self.wind_pressure_coefficient_value_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_7 = None
        else:
            self.wind_pressure_coefficient_value_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_8 = None
        else:
            self.wind_pressure_coefficient_value_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_9 = None
        else:
            self.wind_pressure_coefficient_value_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_10 = None
        else:
            self.wind_pressure_coefficient_value_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_11 = None
        else:
            self.wind_pressure_coefficient_value_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_12 = None
        else:
            self.wind_pressure_coefficient_value_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_13 = None
        else:
            self.wind_pressure_coefficient_value_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_14 = None
        else:
            self.wind_pressure_coefficient_value_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_15 = None
        else:
            self.wind_pressure_coefficient_value_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_16 = None
        else:
            self.wind_pressure_coefficient_value_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_17 = None
        else:
            self.wind_pressure_coefficient_value_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_18 = None
        else:
            self.wind_pressure_coefficient_value_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_19 = None
        else:
            self.wind_pressure_coefficient_value_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_20 = None
        else:
            self.wind_pressure_coefficient_value_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_21 = None
        else:
            self.wind_pressure_coefficient_value_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_22 = None
        else:
            self.wind_pressure_coefficient_value_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_23 = None
        else:
            self.wind_pressure_coefficient_value_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_24 = None
        else:
            self.wind_pressure_coefficient_value_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_25 = None
        else:
            self.wind_pressure_coefficient_value_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_26 = None
        else:
            self.wind_pressure_coefficient_value_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_27 = None
        else:
            self.wind_pressure_coefficient_value_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_28 = None
        else:
            self.wind_pressure_coefficient_value_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_29 = None
        else:
            self.wind_pressure_coefficient_value_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_30 = None
        else:
            self.wind_pressure_coefficient_value_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_31 = None
        else:
            self.wind_pressure_coefficient_value_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_32 = None
        else:
            self.wind_pressure_coefficient_value_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_33 = None
        else:
            self.wind_pressure_coefficient_value_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_34 = None
        else:
            self.wind_pressure_coefficient_value_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_35 = None
        else:
            self.wind_pressure_coefficient_value_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_36 = None
        else:
            self.wind_pressure_coefficient_value_36 = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'WPCValueNames', u'required-field': True, 'pytype': 'str'}

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
    def airflownetworkmultizonewindpressurecoefficientarray_name(self):
        """Get airflownetworkmultizonewindpressurecoefficientarray_name

        Returns:
            str: the value of `airflownetworkmultizonewindpressurecoefficientarray_name` or None if not set
        """
        return self._data["AirflowNetwork:MultiZone:WindPressureCoefficientArray Name"]

    @airflownetworkmultizonewindpressurecoefficientarray_name.setter
    def airflownetworkmultizonewindpressurecoefficientarray_name(self, value=None):
        """  Corresponds to IDD Field `AirflowNetwork:MultiZone:WindPressureCoefficientArray Name`
        Enter the name of the AirflowNetwork:Multizone:WindPressureCoefficientArray object.
        
        {u'note': [u'Enter the name of the AirflowNetwork:Multizone:WindPressureCoefficientArray object.'], u'type': u'object-list', u'object-list': u'WPCSetNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `AirflowNetwork:MultiZone:WindPressureCoefficientArray Name`
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
                                 'for field `airflownetworkmultizonewindpressurecoefficientarray_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflownetworkmultizonewindpressurecoefficientarray_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `airflownetworkmultizonewindpressurecoefficientarray_name`')
        self._data["AirflowNetwork:MultiZone:WindPressureCoefficientArray Name"] = value

    @property
    def wind_pressure_coefficient_value_1(self):
        """Get wind_pressure_coefficient_value_1

        Returns:
            float: the value of `wind_pressure_coefficient_value_1` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 1"]

    @wind_pressure_coefficient_value_1.setter
    def wind_pressure_coefficient_value_1(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 1`
        Enter the WPC Value corresponding to the 1st wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 1st wind direction.'], u'type': u'real', u'required-field': True, 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 1`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_1`'.format(value))
        self._data["Wind Pressure Coefficient Value 1"] = value

    @property
    def wind_pressure_coefficient_value_2(self):
        """Get wind_pressure_coefficient_value_2

        Returns:
            float: the value of `wind_pressure_coefficient_value_2` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 2"]

    @wind_pressure_coefficient_value_2.setter
    def wind_pressure_coefficient_value_2(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 2`
        Enter the WPC Value corresponding to the 2nd wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 2nd wind direction.'], u'type': u'real', u'required-field': True, 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 2`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_2`'.format(value))
        self._data["Wind Pressure Coefficient Value 2"] = value

    @property
    def wind_pressure_coefficient_value_3(self):
        """Get wind_pressure_coefficient_value_3

        Returns:
            float: the value of `wind_pressure_coefficient_value_3` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 3"]

    @wind_pressure_coefficient_value_3.setter
    def wind_pressure_coefficient_value_3(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 3`
        Enter the WPC Value corresponding to the 3rd wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 3rd wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 3`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_3`'.format(value))
        self._data["Wind Pressure Coefficient Value 3"] = value

    @property
    def wind_pressure_coefficient_value_4(self):
        """Get wind_pressure_coefficient_value_4

        Returns:
            float: the value of `wind_pressure_coefficient_value_4` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 4"]

    @wind_pressure_coefficient_value_4.setter
    def wind_pressure_coefficient_value_4(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 4`
        Enter the WPC Value corresponding to the 4th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 4th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 4`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_4`'.format(value))
        self._data["Wind Pressure Coefficient Value 4"] = value

    @property
    def wind_pressure_coefficient_value_5(self):
        """Get wind_pressure_coefficient_value_5

        Returns:
            float: the value of `wind_pressure_coefficient_value_5` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 5"]

    @wind_pressure_coefficient_value_5.setter
    def wind_pressure_coefficient_value_5(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 5`
        Enter the WPC Value corresponding to the 5th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 5th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 5`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_5`'.format(value))
        self._data["Wind Pressure Coefficient Value 5"] = value

    @property
    def wind_pressure_coefficient_value_6(self):
        """Get wind_pressure_coefficient_value_6

        Returns:
            float: the value of `wind_pressure_coefficient_value_6` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 6"]

    @wind_pressure_coefficient_value_6.setter
    def wind_pressure_coefficient_value_6(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 6`
        Enter the WPC Value corresponding to the 6th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 6th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 6`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_6`'.format(value))
        self._data["Wind Pressure Coefficient Value 6"] = value

    @property
    def wind_pressure_coefficient_value_7(self):
        """Get wind_pressure_coefficient_value_7

        Returns:
            float: the value of `wind_pressure_coefficient_value_7` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 7"]

    @wind_pressure_coefficient_value_7.setter
    def wind_pressure_coefficient_value_7(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 7`
        Enter the WPC Value corresponding to the 7th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 7th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 7`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_7`'.format(value))
        self._data["Wind Pressure Coefficient Value 7"] = value

    @property
    def wind_pressure_coefficient_value_8(self):
        """Get wind_pressure_coefficient_value_8

        Returns:
            float: the value of `wind_pressure_coefficient_value_8` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 8"]

    @wind_pressure_coefficient_value_8.setter
    def wind_pressure_coefficient_value_8(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 8`
        Enter the WPC Value corresponding to the 8th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 8th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 8`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_8`'.format(value))
        self._data["Wind Pressure Coefficient Value 8"] = value

    @property
    def wind_pressure_coefficient_value_9(self):
        """Get wind_pressure_coefficient_value_9

        Returns:
            float: the value of `wind_pressure_coefficient_value_9` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 9"]

    @wind_pressure_coefficient_value_9.setter
    def wind_pressure_coefficient_value_9(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 9`
        Enter the WPC Value corresponding to the 9th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 9th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 9`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_9`'.format(value))
        self._data["Wind Pressure Coefficient Value 9"] = value

    @property
    def wind_pressure_coefficient_value_10(self):
        """Get wind_pressure_coefficient_value_10

        Returns:
            float: the value of `wind_pressure_coefficient_value_10` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 10"]

    @wind_pressure_coefficient_value_10.setter
    def wind_pressure_coefficient_value_10(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 10`
        Enter the WPC Value corresponding to the 10th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 10th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 10`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_10`'.format(value))
        self._data["Wind Pressure Coefficient Value 10"] = value

    @property
    def wind_pressure_coefficient_value_11(self):
        """Get wind_pressure_coefficient_value_11

        Returns:
            float: the value of `wind_pressure_coefficient_value_11` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 11"]

    @wind_pressure_coefficient_value_11.setter
    def wind_pressure_coefficient_value_11(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 11`
        Enter the WPC Value corresponding to the 11th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 11th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 11`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_11`'.format(value))
        self._data["Wind Pressure Coefficient Value 11"] = value

    @property
    def wind_pressure_coefficient_value_12(self):
        """Get wind_pressure_coefficient_value_12

        Returns:
            float: the value of `wind_pressure_coefficient_value_12` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 12"]

    @wind_pressure_coefficient_value_12.setter
    def wind_pressure_coefficient_value_12(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 12`
        Enter the WPC Value corresponding to the 12th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 12th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 12`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_12`'.format(value))
        self._data["Wind Pressure Coefficient Value 12"] = value

    @property
    def wind_pressure_coefficient_value_13(self):
        """Get wind_pressure_coefficient_value_13

        Returns:
            float: the value of `wind_pressure_coefficient_value_13` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 13"]

    @wind_pressure_coefficient_value_13.setter
    def wind_pressure_coefficient_value_13(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 13`
        Enter the WPC Value corresponding to the 13th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 13th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 13`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_13`'.format(value))
        self._data["Wind Pressure Coefficient Value 13"] = value

    @property
    def wind_pressure_coefficient_value_14(self):
        """Get wind_pressure_coefficient_value_14

        Returns:
            float: the value of `wind_pressure_coefficient_value_14` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 14"]

    @wind_pressure_coefficient_value_14.setter
    def wind_pressure_coefficient_value_14(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 14`
        Enter the WPC Value corresponding to the 14th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 14th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 14`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_14`'.format(value))
        self._data["Wind Pressure Coefficient Value 14"] = value

    @property
    def wind_pressure_coefficient_value_15(self):
        """Get wind_pressure_coefficient_value_15

        Returns:
            float: the value of `wind_pressure_coefficient_value_15` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 15"]

    @wind_pressure_coefficient_value_15.setter
    def wind_pressure_coefficient_value_15(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 15`
        Enter the WPC Value corresponding to the 15th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 15th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 15`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_15`'.format(value))
        self._data["Wind Pressure Coefficient Value 15"] = value

    @property
    def wind_pressure_coefficient_value_16(self):
        """Get wind_pressure_coefficient_value_16

        Returns:
            float: the value of `wind_pressure_coefficient_value_16` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 16"]

    @wind_pressure_coefficient_value_16.setter
    def wind_pressure_coefficient_value_16(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 16`
        Enter the WPC Value corresponding to the 16th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 16th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 16`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_16`'.format(value))
        self._data["Wind Pressure Coefficient Value 16"] = value

    @property
    def wind_pressure_coefficient_value_17(self):
        """Get wind_pressure_coefficient_value_17

        Returns:
            float: the value of `wind_pressure_coefficient_value_17` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 17"]

    @wind_pressure_coefficient_value_17.setter
    def wind_pressure_coefficient_value_17(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 17`
        Enter the WPC Value corresponding to the 17th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 17th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 17`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_17`'.format(value))
        self._data["Wind Pressure Coefficient Value 17"] = value

    @property
    def wind_pressure_coefficient_value_18(self):
        """Get wind_pressure_coefficient_value_18

        Returns:
            float: the value of `wind_pressure_coefficient_value_18` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 18"]

    @wind_pressure_coefficient_value_18.setter
    def wind_pressure_coefficient_value_18(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 18`
        Enter the WPC Value corresponding to the 18th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 18th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 18`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_18`'.format(value))
        self._data["Wind Pressure Coefficient Value 18"] = value

    @property
    def wind_pressure_coefficient_value_19(self):
        """Get wind_pressure_coefficient_value_19

        Returns:
            float: the value of `wind_pressure_coefficient_value_19` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 19"]

    @wind_pressure_coefficient_value_19.setter
    def wind_pressure_coefficient_value_19(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 19`
        Enter the WPC Value corresponding to the 19th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 19th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 19`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_19`'.format(value))
        self._data["Wind Pressure Coefficient Value 19"] = value

    @property
    def wind_pressure_coefficient_value_20(self):
        """Get wind_pressure_coefficient_value_20

        Returns:
            float: the value of `wind_pressure_coefficient_value_20` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 20"]

    @wind_pressure_coefficient_value_20.setter
    def wind_pressure_coefficient_value_20(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 20`
        Enter the WPC Value corresponding to the 20th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 20th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 20`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_20`'.format(value))
        self._data["Wind Pressure Coefficient Value 20"] = value

    @property
    def wind_pressure_coefficient_value_21(self):
        """Get wind_pressure_coefficient_value_21

        Returns:
            float: the value of `wind_pressure_coefficient_value_21` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 21"]

    @wind_pressure_coefficient_value_21.setter
    def wind_pressure_coefficient_value_21(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 21`
        Enter the WPC Value corresponding to the 21st wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 21st wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 21`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_21`'.format(value))
        self._data["Wind Pressure Coefficient Value 21"] = value

    @property
    def wind_pressure_coefficient_value_22(self):
        """Get wind_pressure_coefficient_value_22

        Returns:
            float: the value of `wind_pressure_coefficient_value_22` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 22"]

    @wind_pressure_coefficient_value_22.setter
    def wind_pressure_coefficient_value_22(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 22`
        Enter the WPC Value corresponding to the 22nd wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 22nd wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 22`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_22`'.format(value))
        self._data["Wind Pressure Coefficient Value 22"] = value

    @property
    def wind_pressure_coefficient_value_23(self):
        """Get wind_pressure_coefficient_value_23

        Returns:
            float: the value of `wind_pressure_coefficient_value_23` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 23"]

    @wind_pressure_coefficient_value_23.setter
    def wind_pressure_coefficient_value_23(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 23`
        Enter the WPC Value corresponding to the 23rd wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 23rd wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 23`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_23`'.format(value))
        self._data["Wind Pressure Coefficient Value 23"] = value

    @property
    def wind_pressure_coefficient_value_24(self):
        """Get wind_pressure_coefficient_value_24

        Returns:
            float: the value of `wind_pressure_coefficient_value_24` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 24"]

    @wind_pressure_coefficient_value_24.setter
    def wind_pressure_coefficient_value_24(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 24`
        Enter the WPC Value corresponding to the 24th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 24th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 24`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_24`'.format(value))
        self._data["Wind Pressure Coefficient Value 24"] = value

    @property
    def wind_pressure_coefficient_value_25(self):
        """Get wind_pressure_coefficient_value_25

        Returns:
            float: the value of `wind_pressure_coefficient_value_25` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 25"]

    @wind_pressure_coefficient_value_25.setter
    def wind_pressure_coefficient_value_25(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 25`
        Enter the WPC Value corresponding to the 25th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 25th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 25`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_25`'.format(value))
        self._data["Wind Pressure Coefficient Value 25"] = value

    @property
    def wind_pressure_coefficient_value_26(self):
        """Get wind_pressure_coefficient_value_26

        Returns:
            float: the value of `wind_pressure_coefficient_value_26` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 26"]

    @wind_pressure_coefficient_value_26.setter
    def wind_pressure_coefficient_value_26(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 26`
        Enter the WPC Value corresponding to the 26th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 26th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 26`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_26`'.format(value))
        self._data["Wind Pressure Coefficient Value 26"] = value

    @property
    def wind_pressure_coefficient_value_27(self):
        """Get wind_pressure_coefficient_value_27

        Returns:
            float: the value of `wind_pressure_coefficient_value_27` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 27"]

    @wind_pressure_coefficient_value_27.setter
    def wind_pressure_coefficient_value_27(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 27`
        Enter the WPC Value corresponding to the 27th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 27th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 27`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_27`'.format(value))
        self._data["Wind Pressure Coefficient Value 27"] = value

    @property
    def wind_pressure_coefficient_value_28(self):
        """Get wind_pressure_coefficient_value_28

        Returns:
            float: the value of `wind_pressure_coefficient_value_28` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 28"]

    @wind_pressure_coefficient_value_28.setter
    def wind_pressure_coefficient_value_28(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 28`
        Enter the WPC Value corresponding to the 28th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 28th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 28`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_28`'.format(value))
        self._data["Wind Pressure Coefficient Value 28"] = value

    @property
    def wind_pressure_coefficient_value_29(self):
        """Get wind_pressure_coefficient_value_29

        Returns:
            float: the value of `wind_pressure_coefficient_value_29` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 29"]

    @wind_pressure_coefficient_value_29.setter
    def wind_pressure_coefficient_value_29(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 29`
        Enter the WPC Value corresponding to the 29th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 29th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 29`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_29`'.format(value))
        self._data["Wind Pressure Coefficient Value 29"] = value

    @property
    def wind_pressure_coefficient_value_30(self):
        """Get wind_pressure_coefficient_value_30

        Returns:
            float: the value of `wind_pressure_coefficient_value_30` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 30"]

    @wind_pressure_coefficient_value_30.setter
    def wind_pressure_coefficient_value_30(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 30`
        Enter the WPC Value corresponding to the 30th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 30th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 30`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_30`'.format(value))
        self._data["Wind Pressure Coefficient Value 30"] = value

    @property
    def wind_pressure_coefficient_value_31(self):
        """Get wind_pressure_coefficient_value_31

        Returns:
            float: the value of `wind_pressure_coefficient_value_31` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 31"]

    @wind_pressure_coefficient_value_31.setter
    def wind_pressure_coefficient_value_31(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 31`
        Enter the WPC Value corresponding to the 31st wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 31st wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 31`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_31`'.format(value))
        self._data["Wind Pressure Coefficient Value 31"] = value

    @property
    def wind_pressure_coefficient_value_32(self):
        """Get wind_pressure_coefficient_value_32

        Returns:
            float: the value of `wind_pressure_coefficient_value_32` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 32"]

    @wind_pressure_coefficient_value_32.setter
    def wind_pressure_coefficient_value_32(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 32`
        Enter the WPC Value corresponding to the 32nd wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 32nd wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 32`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_32`'.format(value))
        self._data["Wind Pressure Coefficient Value 32"] = value

    @property
    def wind_pressure_coefficient_value_33(self):
        """Get wind_pressure_coefficient_value_33

        Returns:
            float: the value of `wind_pressure_coefficient_value_33` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 33"]

    @wind_pressure_coefficient_value_33.setter
    def wind_pressure_coefficient_value_33(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 33`
        Enter the WPC Value corresponding to the 33rd wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 33rd wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 33`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_33`'.format(value))
        self._data["Wind Pressure Coefficient Value 33"] = value

    @property
    def wind_pressure_coefficient_value_34(self):
        """Get wind_pressure_coefficient_value_34

        Returns:
            float: the value of `wind_pressure_coefficient_value_34` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 34"]

    @wind_pressure_coefficient_value_34.setter
    def wind_pressure_coefficient_value_34(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 34`
        Enter the WPC Value corresponding to the 34th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 34th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 34`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_34`'.format(value))
        self._data["Wind Pressure Coefficient Value 34"] = value

    @property
    def wind_pressure_coefficient_value_35(self):
        """Get wind_pressure_coefficient_value_35

        Returns:
            float: the value of `wind_pressure_coefficient_value_35` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 35"]

    @wind_pressure_coefficient_value_35.setter
    def wind_pressure_coefficient_value_35(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 35`
        Enter the WPC Value corresponding to the 35th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 35th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 35`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_35`'.format(value))
        self._data["Wind Pressure Coefficient Value 35"] = value

    @property
    def wind_pressure_coefficient_value_36(self):
        """Get wind_pressure_coefficient_value_36

        Returns:
            float: the value of `wind_pressure_coefficient_value_36` or None if not set
        """
        return self._data["Wind Pressure Coefficient Value 36"]

    @wind_pressure_coefficient_value_36.setter
    def wind_pressure_coefficient_value_36(self, value=None):
        """  Corresponds to IDD Field `Wind Pressure Coefficient Value 36`
        Enter the WPC Value corresponding to the 36th wind direction.
        
        {u'units': u'dimensionless', u'note': [u'Enter the WPC Value corresponding to the 36th wind direction.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 36`
                Units: dimensionless
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
                                 'for field `wind_pressure_coefficient_value_36`'.format(value))
        self._data["Wind Pressure Coefficient Value 36"] = value

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

class AirflowNetworkDistributionNode(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Node`
        This object represents an air distribution node in the AirflowNetwork model.
    
    """
    internal_name = "AirflowNetwork:Distribution:Node"
    field_count = 4
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:Distribution:Node`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Component Name or Node Name"] = None
        self._data["Component Object Type or Node Type"] = None
        self._data["Node Height"] = None
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
            self.component_name_or_node_name = None
        else:
            self.component_name_or_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_object_type_or_node_type = None
        else:
            self.component_object_type_or_node_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_height = None
        else:
            self.node_height = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'AirflowNetworkNodeAndZoneNames', u'required-field': True, 'pytype': 'str'}

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
    def component_name_or_node_name(self):
        """Get component_name_or_node_name

        Returns:
            str: the value of `component_name_or_node_name` or None if not set
        """
        return self._data["Component Name or Node Name"]

    @component_name_or_node_name.setter
    def component_name_or_node_name(self, value=None):
        """  Corresponds to IDD Field `Component Name or Node Name`
        Designates node names defined in another object. The node name may occur in air branches.
        Enter a node name to represent a node already defined in an air loop.
        Leave this field blank if the Node or Object Type field below is entered as
        AirLoopHVAC:ZoneMixer, AirLoopHVAC:ZoneSplitter, AirLoopHVAC:OutdoorAirSystem, or Other.
        
        {u'note': [u'Designates node names defined in another object. The node name may occur in air branches.', u'Enter a node name to represent a node already defined in an air loop.', u'Leave this field blank if the Node or Object Type field below is entered as', u'AirLoopHVAC:ZoneMixer, AirLoopHVAC:ZoneSplitter, AirLoopHVAC:OutdoorAirSystem, or Other.'], u'type': u'alpha', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component Name or Node Name`
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
                                 'for field `component_name_or_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_name_or_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_name_or_node_name`')
        self._data["Component Name or Node Name"] = value

    @property
    def component_object_type_or_node_type(self):
        """Get component_object_type_or_node_type

        Returns:
            str: the value of `component_object_type_or_node_type` or None if not set
        """
        return self._data["Component Object Type or Node Type"]

    @component_object_type_or_node_type.setter
    def component_object_type_or_node_type(self, value="Other"):
        """  Corresponds to IDD Field `Component Object Type or Node Type`
        Designates Node type for the Node or Component Name defined in the field above.
        AirLoopHVAC:ZoneMixer -- Represents a AirLoopHVAC:ZoneMixer object.
        AirLoopHVAC:ZoneSplitter -- Represents a AirLoopHVAC:ZoneSplitter object.
        AirLoopHVAC:OutdoorAirSystem -- Represents an AirLoopHVAC:OutdoorAirSystem object.
        OAMixerOutdoorAirStreamNode -- Represents an external node used in the OutdoorAir:Mixer
        OutdoorAir:NodeList -- Represents an external node when a heat exchanger is used before
        the OutdoorAir:Mixer
        OutdoorAir:Node -- Represents an external node when a heat exchanger is used before
        the OutdoorAir:Mixer
        Other -- none of the above, the Node name already defined in the previous field is part
        of an air loop.
        
        {u'default': u'Other', u'note': [u'Designates Node type for the Node or Component Name defined in the field above.', u'AirLoopHVAC:ZoneMixer -- Represents a AirLoopHVAC:ZoneMixer object.', u'AirLoopHVAC:ZoneSplitter -- Represents a AirLoopHVAC:ZoneSplitter object.', u'AirLoopHVAC:OutdoorAirSystem -- Represents an AirLoopHVAC:OutdoorAirSystem object.', u'OAMixerOutdoorAirStreamNode -- Represents an external node used in the OutdoorAir:Mixer', u'OutdoorAir:NodeList -- Represents an external node when a heat exchanger is used before', u'the OutdoorAir:Mixer', u'OutdoorAir:Node -- Represents an external node when a heat exchanger is used before', u'the OutdoorAir:Mixer', u'Other -- none of the above, the Node name already defined in the previous field is part', u'of an air loop.'], u'type': u'choice', u'key': [u'AirLoopHVAC:ZoneMixer', u'AirLoopHVAC:ZoneSplitter', u'AirLoopHVAC:OutdoorAirSystem', u'OAMixerOutdoorAirStreamNode', u'OutdoorAir:NodeList', u'OutdoorAir:Node', u'Other'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component Object Type or Node Type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:OutdoorAirSystem
                      - OAMixerOutdoorAirStreamNode
                      - OutdoorAir:NodeList
                      - OutdoorAir:Node
                      - Other
                Default value: Other
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
                                 'for field `component_object_type_or_node_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_object_type_or_node_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_object_type_or_node_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:outdoorairsystem"] = "AirLoopHVAC:OutdoorAirSystem"
            vals["oamixeroutdoorairstreamnode"] = "OAMixerOutdoorAirStreamNode"
            vals["outdoorair:nodelist"] = "OutdoorAir:NodeList"
            vals["outdoorair:node"] = "OutdoorAir:Node"
            vals["other"] = "Other"
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
                                     'field `component_object_type_or_node_type`'.format(value))
            value = vals[value_lower]
        self._data["Component Object Type or Node Type"] = value

    @property
    def node_height(self):
        """Get node_height

        Returns:
            float: the value of `node_height` or None if not set
        """
        return self._data["Node Height"]

    @node_height.setter
    def node_height(self, value=0.0 ):
        """  Corresponds to IDD Field `Node Height`
        Enter the reference height used to calculate the relative pressure.
        
        {u'units': u'm', u'default': '0.0', u'note': [u'Enter the reference height used to calculate the relative pressure.'], u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Node Height`
                Units: m
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
                                 'for field `node_height`'.format(value))
        self._data["Node Height"] = value

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

class AirflowNetworkDistributionComponentLeak(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Leak`
        This object defines the characteristics of a supply or return air leak.
    
    """
    internal_name = "AirflowNetwork:Distribution:Component:Leak"
    field_count = 3
    required_fields = ["Name", "Air Mass Flow Coefficient"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:Distribution:Component:Leak`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient"] = None
        self._data["Air Mass Flow Exponent"] = None
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
            self.air_mass_flow_coefficient = None
        else:
            self.air_mass_flow_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent = None
        else:
            self.air_mass_flow_exponent = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'AirflowNetworkComponentNames', u'required-field': True, 'pytype': 'str'}

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
    def air_mass_flow_coefficient(self):
        """Get air_mass_flow_coefficient

        Returns:
            float: the value of `air_mass_flow_coefficient` or None if not set
        """
        return self._data["Air Mass Flow Coefficient"]

    @air_mass_flow_coefficient.setter
    def air_mass_flow_coefficient(self, value=None):
        """  Corresponds to IDD Field `Air Mass Flow Coefficient`
        Defined at 1 Pa pressure difference across this component.
        Enter the coefficient used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Defined at 1 Pa pressure difference across this component.', u'Enter the coefficient used in the following equation:', u'Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent'], u'units': u'kg/s', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient`
                Units: kg/s
                value > 0.0
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
                                 'for field `air_mass_flow_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_mass_flow_coefficient`')
        self._data["Air Mass Flow Coefficient"] = value

    @property
    def air_mass_flow_exponent(self):
        """Get air_mass_flow_exponent

        Returns:
            float: the value of `air_mass_flow_exponent` or None if not set
        """
        return self._data["Air Mass Flow Exponent"]

    @air_mass_flow_exponent.setter
    def air_mass_flow_exponent(self, value=0.65 ):
        """  Corresponds to IDD Field `Air Mass Flow Exponent`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent
        
        {'pytype': 'float', u'default': '0.65', u'maximum': '1.0', u'note': [u'Enter the exponent used in the following equation:', u'Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent'], u'minimum': '0.5', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
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
                                 'for field `air_mass_flow_exponent`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent`')
        self._data["Air Mass Flow Exponent"] = value

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

class AirflowNetworkDistributionComponentLeakageRatio(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:LeakageRatio`
        This object is used to define supply and return air leaks with respect to the fan's maximum
        air flow rate.
    
    """
    internal_name = "AirflowNetwork:Distribution:Component:LeakageRatio"
    field_count = 5
    required_fields = ["Name", "Maximum Flow Rate", "Reference Pressure Difference"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:Distribution:Component:LeakageRatio`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Effective Leakage Ratio"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Reference Pressure Difference"] = None
        self._data["Air Mass Flow Exponent"] = None
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
            self.effective_leakage_ratio = None
        else:
            self.effective_leakage_ratio = vals[i]
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
            self.reference_pressure_difference = None
        else:
            self.reference_pressure_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent = None
        else:
            self.air_mass_flow_exponent = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'AirflowNetworkComponentNames', u'required-field': True, 'pytype': 'str'}

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
    def effective_leakage_ratio(self):
        """Get effective_leakage_ratio

        Returns:
            float: the value of `effective_leakage_ratio` or None if not set
        """
        return self._data["Effective Leakage Ratio"]

    @effective_leakage_ratio.setter
    def effective_leakage_ratio(self, value=None):
        """  Corresponds to IDD Field `Effective Leakage Ratio`
        Defined as a ratio of leak flow rate to the maximum flow rate.
        
        {'pytype': 'float', u'minimum>': '0.0', u'maximum': '1.0', u'note': [u'Defined as a ratio of leak flow rate to the maximum flow rate.'], u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Effective Leakage Ratio`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `effective_leakage_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `effective_leakage_ratio`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `effective_leakage_ratio`')
        self._data["Effective Leakage Ratio"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Flow Rate`
        Enter the maximum air flow rate in this air loop.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the maximum air flow rate in this air loop.'], u'units': u'm3/s', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Maximum Flow Rate`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_flow_rate`')
        self._data["Maximum Flow Rate"] = value

    @property
    def reference_pressure_difference(self):
        """Get reference_pressure_difference

        Returns:
            float: the value of `reference_pressure_difference` or None if not set
        """
        return self._data["Reference Pressure Difference"]

    @reference_pressure_difference.setter
    def reference_pressure_difference(self, value=None):
        """  Corresponds to IDD Field `Reference Pressure Difference`
        Enter the pressure corresponding to the Effective leakage ratio entered above.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the pressure corresponding to the Effective leakage ratio entered above.'], u'units': u'Pa', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Reference Pressure Difference`
                Units: Pa
                value > 0.0
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
                                 'for field `reference_pressure_difference`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `reference_pressure_difference`')
        self._data["Reference Pressure Difference"] = value

    @property
    def air_mass_flow_exponent(self):
        """Get air_mass_flow_exponent

        Returns:
            float: the value of `air_mass_flow_exponent` or None if not set
        """
        return self._data["Air Mass Flow Exponent"]

    @air_mass_flow_exponent.setter
    def air_mass_flow_exponent(self, value=0.65 ):
        """  Corresponds to IDD Field `Air Mass Flow Exponent`
        Enter the exponent used in the air mass flow equation.
        
        {'pytype': 'float', u'default': '0.65', u'maximum': '1.0', u'note': [u'Enter the exponent used in the air mass flow equation.'], u'minimum': '0.5', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
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
                                 'for field `air_mass_flow_exponent`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent`')
        self._data["Air Mass Flow Exponent"] = value

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

class AirflowNetworkDistributionComponentDuct(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Duct`
        This object defines the relationship between pressure and air flow through the duct.
    
    """
    internal_name = "AirflowNetwork:Distribution:Component:Duct"
    field_count = 8
    required_fields = ["Name", "Duct Length", "Hydraulic Diameter", "Cross Section Area"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:Distribution:Component:Duct`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Duct Length"] = None
        self._data["Hydraulic Diameter"] = None
        self._data["Cross Section Area"] = None
        self._data["Surface Roughness"] = None
        self._data["Coefficient for Local Dynamic Loss Due to Fitting"] = None
        self._data["Overall Heat Transmittance Coefficient (U-Factor) from Air to Air"] = None
        self._data["Overall Moisture Transmittance Coefficient from Air to Air"] = None
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
            self.duct_length = None
        else:
            self.duct_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hydraulic_diameter = None
        else:
            self.hydraulic_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cross_section_area = None
        else:
            self.cross_section_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_roughness = None
        else:
            self.surface_roughness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_for_local_dynamic_loss_due_to_fitting = None
        else:
            self.coefficient_for_local_dynamic_loss_due_to_fitting = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overall_heat_transmittance_coefficient_ufactor_from_air_to_air = None
        else:
            self.overall_heat_transmittance_coefficient_ufactor_from_air_to_air = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overall_moisture_transmittance_coefficient_from_air_to_air = None
        else:
            self.overall_moisture_transmittance_coefficient_from_air_to_air = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'AirflowNetworkComponentNames', u'required-field': True, 'pytype': 'str'}

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
    def duct_length(self):
        """Get duct_length

        Returns:
            float: the value of `duct_length` or None if not set
        """
        return self._data["Duct Length"]

    @duct_length.setter
    def duct_length(self, value=None):
        """  Corresponds to IDD Field `Duct Length`
        Enter the length of the duct.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the length of the duct.'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Duct Length`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `duct_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `duct_length`')
        self._data["Duct Length"] = value

    @property
    def hydraulic_diameter(self):
        """Get hydraulic_diameter

        Returns:
            float: the value of `hydraulic_diameter` or None if not set
        """
        return self._data["Hydraulic Diameter"]

    @hydraulic_diameter.setter
    def hydraulic_diameter(self, value=None):
        """  Corresponds to IDD Field `Hydraulic Diameter`
        Enter the hydraulic diameter of the duct.
        Hydraulic diameter is defined as 4 multiplied by cross section area divided by perimeter
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the hydraulic diameter of the duct.', u'Hydraulic diameter is defined as 4 multiplied by cross section area divided by perimeter'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Hydraulic Diameter`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydraulic_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydraulic_diameter`')
        self._data["Hydraulic Diameter"] = value

    @property
    def cross_section_area(self):
        """Get cross_section_area

        Returns:
            float: the value of `cross_section_area` or None if not set
        """
        return self._data["Cross Section Area"]

    @cross_section_area.setter
    def cross_section_area(self, value=None):
        """  Corresponds to IDD Field `Cross Section Area`
        Enter the cross section area of the duct.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the cross section area of the duct.'], u'units': u'm2', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Cross Section Area`
                Units: m2
                value > 0.0
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
                                 'for field `cross_section_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cross_section_area`')
        self._data["Cross Section Area"] = value

    @property
    def surface_roughness(self):
        """Get surface_roughness

        Returns:
            float: the value of `surface_roughness` or None if not set
        """
        return self._data["Surface Roughness"]

    @surface_roughness.setter
    def surface_roughness(self, value=0.0009 ):
        """  Corresponds to IDD Field `Surface Roughness`
        Enter the inside surface roughness of the duct.
        
        {'pytype': 'float', u'default': '0.0009', u'minimum>': '0.0', u'note': [u'Enter the inside surface roughness of the duct.'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Surface Roughness`
                Units: m
                Default value: 0.0009
                value > 0.0
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
                                 'for field `surface_roughness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `surface_roughness`')
        self._data["Surface Roughness"] = value

    @property
    def coefficient_for_local_dynamic_loss_due_to_fitting(self):
        """Get coefficient_for_local_dynamic_loss_due_to_fitting

        Returns:
            float: the value of `coefficient_for_local_dynamic_loss_due_to_fitting` or None if not set
        """
        return self._data["Coefficient for Local Dynamic Loss Due to Fitting"]

    @coefficient_for_local_dynamic_loss_due_to_fitting.setter
    def coefficient_for_local_dynamic_loss_due_to_fitting(self, value=0.0 ):
        """  Corresponds to IDD Field `Coefficient for Local Dynamic Loss Due to Fitting`
        Enter the coefficient used to calculate dynamic losses of fittings (e.g. elbows).
        
        {'pytype': 'float', u'default': '0.0', u'note': [u'Enter the coefficient used to calculate dynamic losses of fittings (e.g. elbows).'], u'minimum': '0.0', u'units': u'dimensionless', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Coefficient for Local Dynamic Loss Due to Fitting`
                Units: dimensionless
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_for_local_dynamic_loss_due_to_fitting`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `coefficient_for_local_dynamic_loss_due_to_fitting`')
        self._data["Coefficient for Local Dynamic Loss Due to Fitting"] = value

    @property
    def overall_heat_transmittance_coefficient_ufactor_from_air_to_air(self):
        """Get overall_heat_transmittance_coefficient_ufactor_from_air_to_air

        Returns:
            float: the value of `overall_heat_transmittance_coefficient_ufactor_from_air_to_air` or None if not set
        """
        return self._data["Overall Heat Transmittance Coefficient (U-Factor) from Air to Air"]

    @overall_heat_transmittance_coefficient_ufactor_from_air_to_air.setter
    def overall_heat_transmittance_coefficient_ufactor_from_air_to_air(self, value=0.772 ):
        """  Corresponds to IDD Field `Overall Heat Transmittance Coefficient (U-Factor) from Air to Air`
        including film coefficients at both surfaces
        Enter the overall U-value for this duct.
        Default value of 0.772 is equivalent to 1.06 m2-K/W (R6) duct insulation with
        film coefficients for outside and inside equal to 5 and 25 W/m2-K, respectively.
        
        {'pytype': 'float', u'default': '0.772', u'minimum>': '0.0', u'note': [u'including film coefficients at both surfaces', u'Enter the overall U-value for this duct.', u'Default value of 0.772 is equivalent to 1.06 m2-K/W (R6) duct insulation with', u'film coefficients for outside and inside equal to 5 and 25 W/m2-K, respectively.'], u'units': u'W/m2-K', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Overall Heat Transmittance Coefficient (U-Factor) from Air to Air`
                Units: W/m2-K
                Default value: 0.772
                value > 0.0
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
                                 'for field `overall_heat_transmittance_coefficient_ufactor_from_air_to_air`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `overall_heat_transmittance_coefficient_ufactor_from_air_to_air`')
        self._data["Overall Heat Transmittance Coefficient (U-Factor) from Air to Air"] = value

    @property
    def overall_moisture_transmittance_coefficient_from_air_to_air(self):
        """Get overall_moisture_transmittance_coefficient_from_air_to_air

        Returns:
            float: the value of `overall_moisture_transmittance_coefficient_from_air_to_air` or None if not set
        """
        return self._data["Overall Moisture Transmittance Coefficient from Air to Air"]

    @overall_moisture_transmittance_coefficient_from_air_to_air.setter
    def overall_moisture_transmittance_coefficient_from_air_to_air(self, value=0.001 ):
        """  Corresponds to IDD Field `Overall Moisture Transmittance Coefficient from Air to Air`
        Enter the overall moisture transmittance coefficient
        including moisture film coefficients at both surfaces.
        
        {'pytype': 'float', u'default': '0.001', u'minimum>': '0.0', u'note': [u'Enter the overall moisture transmittance coefficient', u'including moisture film coefficients at both surfaces.'], u'units': u'kg/m2', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Overall Moisture Transmittance Coefficient from Air to Air`
                Units: kg/m2
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `overall_moisture_transmittance_coefficient_from_air_to_air`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `overall_moisture_transmittance_coefficient_from_air_to_air`')
        self._data["Overall Moisture Transmittance Coefficient from Air to Air"] = value

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

class AirflowNetworkDistributionComponentFan(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Fan`
        This object defines the name of the constant volume supply Air Fan used in an Air loop.
    
    """
    internal_name = "AirflowNetwork:Distribution:Component:Fan"
    field_count = 2
    required_fields = ["Fan Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:Distribution:Component:Fan`
        """
        self._data = OrderedDict()
        self._data["Fan Name"] = None
        self._data["Supply Fan Object Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.fan_name = None
        else:
            self.fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_fan_object_type = None
        else:
            self.supply_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def fan_name(self):
        """Get fan_name

        Returns:
            str: the value of `fan_name` or None if not set
        """
        return self._data["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """  Corresponds to IDD Field `Fan Name`
        Enter the name of the constant volume fan in the primary air loop.
        
        {u'reference': u'AirflowNetworkComponentNames', 'pytype': 'str', u'required-field': True, u'note': [u'Enter the name of the constant volume fan in the primary air loop.'], u'object-list': u'FansCVandOnOff', u'type': u'object-list'}

        Args:
            value (str): value for IDD Field `Fan Name`
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
                                 'for field `fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_name`')
        self._data["Fan Name"] = value

    @property
    def supply_fan_object_type(self):
        """Get supply_fan_object_type

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self._data["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value="Fan:ConstantVolume"):
        """  Corresponds to IDD Field `Supply Fan Object Type`
        
        {u'default': u'Fan:ConstantVolume', u'type': u'choice', u'key': [u'Fan:OnOff', u'Fan:ConstantVolume', u'Fan:VariableVolume'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Supply Fan Object Type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
                      - Fan:VariableVolume
                Default value: Fan:ConstantVolume
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
                                 'for field `supply_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_fan_object_type`')
            vals = {}
            vals["fan:onoff"] = "Fan:OnOff"
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
            vals["fan:variablevolume"] = "Fan:VariableVolume"
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
                                     'field `supply_fan_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Supply Fan Object Type"] = value

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

class AirflowNetworkDistributionComponentCoil(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Coil`
        This object defines the name of a coil used in an air loop.
    
    """
    internal_name = "AirflowNetwork:Distribution:Component:Coil"
    field_count = 4
    required_fields = ["Coil Name", "Coil Object Type", "Air Path Length", "Air Path Hydraulic Diameter"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:Distribution:Component:Coil`
        """
        self._data = OrderedDict()
        self._data["Coil Name"] = None
        self._data["Coil Object Type"] = None
        self._data["Air Path Length"] = None
        self._data["Air Path Hydraulic Diameter"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.coil_name = None
        else:
            self.coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coil_object_type = None
        else:
            self.coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_path_length = None
        else:
            self.air_path_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_path_hydraulic_diameter = None
        else:
            self.air_path_hydraulic_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def coil_name(self):
        """Get coil_name

        Returns:
            str: the value of `coil_name` or None if not set
        """
        return self._data["Coil Name"]

    @coil_name.setter
    def coil_name(self, value=None):
        """  Corresponds to IDD Field `Coil Name`
        Enter the name of a cooling or heating coil in the primary Air loop.
        
        {u'reference': u'AirflowNetworkComponentNames', 'pytype': 'str', u'required-field': True, u'note': [u'Enter the name of a cooling or heating coil in the primary Air loop.'], u'object-list': u'AFNCoilNames', u'type': u'object-list'}

        Args:
            value (str): value for IDD Field `Coil Name`
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
                                 'for field `coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `coil_name`')
        self._data["Coil Name"] = value

    @property
    def coil_object_type(self):
        """Get coil_object_type

        Returns:
            str: the value of `coil_object_type` or None if not set
        """
        return self._data["Coil Object Type"]

    @coil_object_type.setter
    def coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Coil Object Type`
        Select the type of coil corresponding to the name entered in the field above.
        
        {u'note': [u'Select the type of coil corresponding to the name entered in the field above.'], u'type': u'choice', u'key': [u'Coil:Cooling:DX:SingleSpeed', u'Coil:Heating:Gas', u'Coil:Heating:Electric', u'Coil:Heating:DX:SingleSpeed', u'Coil:Cooling:Water', u'Coil:Heating:Water', u'Coil:Cooling:Water:DetailedGeometry', u'Coil:Cooling:DX:TwoStageWithHumidityControlMode', u'Coil:Cooling:DX:MultiSpeed', u'Coil:Heating:DX:MultiSpeed', u'Coil:Heating:Desuperheater'], u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - Coil:Heating:Gas
                      - Coil:Heating:Electric
                      - Coil:Heating:DX:SingleSpeed
                      - Coil:Cooling:Water
                      - Coil:Heating:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - Coil:Cooling:DX:TwoStageWithHumidityControlMode
                      - Coil:Cooling:DX:MultiSpeed
                      - Coil:Heating:DX:MultiSpeed
                      - Coil:Heating:Desuperheater
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
                                 'for field `coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `coil_object_type`')
            vals = {}
            vals["coil:cooling:dx:singlespeed"] = "Coil:Cooling:DX:SingleSpeed"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:dx:singlespeed"] = "Coil:Heating:DX:SingleSpeed"
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coil:cooling:dx:twostagewithhumiditycontrolmode"] = "Coil:Cooling:DX:TwoStageWithHumidityControlMode"
            vals["coil:cooling:dx:multispeed"] = "Coil:Cooling:DX:MultiSpeed"
            vals["coil:heating:dx:multispeed"] = "Coil:Heating:DX:MultiSpeed"
            vals["coil:heating:desuperheater"] = "Coil:Heating:Desuperheater"
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
                                     'field `coil_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Coil Object Type"] = value

    @property
    def air_path_length(self):
        """Get air_path_length

        Returns:
            float: the value of `air_path_length` or None if not set
        """
        return self._data["Air Path Length"]

    @air_path_length.setter
    def air_path_length(self, value=None):
        """  Corresponds to IDD Field `Air Path Length`
        Enter the air path length (depth) for the coil.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the air path length (depth) for the coil.'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Path Length`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `air_path_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_path_length`')
        self._data["Air Path Length"] = value

    @property
    def air_path_hydraulic_diameter(self):
        """Get air_path_hydraulic_diameter

        Returns:
            float: the value of `air_path_hydraulic_diameter` or None if not set
        """
        return self._data["Air Path Hydraulic Diameter"]

    @air_path_hydraulic_diameter.setter
    def air_path_hydraulic_diameter(self, value=None):
        """  Corresponds to IDD Field `Air Path Hydraulic Diameter`
        Enter the hydraulic diameter of this coil. The hydraulic diameter is
        defined as 4 multiplied by the cross section area divided by perimeter.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the hydraulic diameter of this coil. The hydraulic diameter is', u'defined as 4 multiplied by the cross section area divided by perimeter.'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Path Hydraulic Diameter`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `air_path_hydraulic_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_path_hydraulic_diameter`')
        self._data["Air Path Hydraulic Diameter"] = value

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

class AirflowNetworkDistributionComponentHeatExchanger(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:HeatExchanger`
        This object defines the name of an air-to-air heat exchanger used in an air loop.
    
    """
    internal_name = "AirflowNetwork:Distribution:Component:HeatExchanger"
    field_count = 4
    required_fields = ["HeatExchanger Name", "HeatExchanger Object Type", "Air Path Length", "Air Path Hydraulic Diameter"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:Distribution:Component:HeatExchanger`
        """
        self._data = OrderedDict()
        self._data["HeatExchanger Name"] = None
        self._data["HeatExchanger Object Type"] = None
        self._data["Air Path Length"] = None
        self._data["Air Path Hydraulic Diameter"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.heatexchanger_name = None
        else:
            self.heatexchanger_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heatexchanger_object_type = None
        else:
            self.heatexchanger_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_path_length = None
        else:
            self.air_path_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_path_hydraulic_diameter = None
        else:
            self.air_path_hydraulic_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def heatexchanger_name(self):
        """Get heatexchanger_name

        Returns:
            str: the value of `heatexchanger_name` or None if not set
        """
        return self._data["HeatExchanger Name"]

    @heatexchanger_name.setter
    def heatexchanger_name(self, value=None):
        """  Corresponds to IDD Field `HeatExchanger Name`
        Enter the name of an air-to-air heat exchanger in the primary Air loop.
        
        {u'reference': u'AirflowNetworkComponentNames', 'pytype': 'str', u'required-field': True, u'note': [u'Enter the name of an air-to-air heat exchanger in the primary Air loop.'], u'object-list': u'AFNHeatExchangerNames', u'type': u'object-list'}

        Args:
            value (str): value for IDD Field `HeatExchanger Name`
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
                                 'for field `heatexchanger_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heatexchanger_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heatexchanger_name`')
        self._data["HeatExchanger Name"] = value

    @property
    def heatexchanger_object_type(self):
        """Get heatexchanger_object_type

        Returns:
            str: the value of `heatexchanger_object_type` or None if not set
        """
        return self._data["HeatExchanger Object Type"]

    @heatexchanger_object_type.setter
    def heatexchanger_object_type(self, value=None):
        """  Corresponds to IDD Field `HeatExchanger Object Type`
        Select the type of heat exchanger corresponding to the name entered in the field above.
        
        {u'note': [u'Select the type of heat exchanger corresponding to the name entered in the field above.'], u'type': u'choice', u'key': [u'HeatExchanger:AirToAir:FlatPlate', u'HeatExchanger:AirToAir:SensibleAndLatent', u'HeatExchanger:Desiccant:BalancedFlow'], u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `HeatExchanger Object Type`
                Accepted values are:
                      - HeatExchanger:AirToAir:FlatPlate
                      - HeatExchanger:AirToAir:SensibleAndLatent
                      - HeatExchanger:Desiccant:BalancedFlow
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
                                 'for field `heatexchanger_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heatexchanger_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heatexchanger_object_type`')
            vals = {}
            vals["heatexchanger:airtoair:flatplate"] = "HeatExchanger:AirToAir:FlatPlate"
            vals["heatexchanger:airtoair:sensibleandlatent"] = "HeatExchanger:AirToAir:SensibleAndLatent"
            vals["heatexchanger:desiccant:balancedflow"] = "HeatExchanger:Desiccant:BalancedFlow"
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
                                     'field `heatexchanger_object_type`'.format(value))
            value = vals[value_lower]
        self._data["HeatExchanger Object Type"] = value

    @property
    def air_path_length(self):
        """Get air_path_length

        Returns:
            float: the value of `air_path_length` or None if not set
        """
        return self._data["Air Path Length"]

    @air_path_length.setter
    def air_path_length(self, value=None):
        """  Corresponds to IDD Field `Air Path Length`
        Enter the air path length (depth) for the heat exchanger.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the air path length (depth) for the heat exchanger.'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Path Length`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `air_path_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_path_length`')
        self._data["Air Path Length"] = value

    @property
    def air_path_hydraulic_diameter(self):
        """Get air_path_hydraulic_diameter

        Returns:
            float: the value of `air_path_hydraulic_diameter` or None if not set
        """
        return self._data["Air Path Hydraulic Diameter"]

    @air_path_hydraulic_diameter.setter
    def air_path_hydraulic_diameter(self, value=None):
        """  Corresponds to IDD Field `Air Path Hydraulic Diameter`
        Enter the hydraulic diameter of this heat exchanger. The hydraulic diameter is
        defined as 4 multiplied by the cross section area divided by perimeter.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the hydraulic diameter of this heat exchanger. The hydraulic diameter is', u'defined as 4 multiplied by the cross section area divided by perimeter.'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Path Hydraulic Diameter`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `air_path_hydraulic_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_path_hydraulic_diameter`')
        self._data["Air Path Hydraulic Diameter"] = value

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

class AirflowNetworkDistributionComponentTerminalUnit(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:TerminalUnit`
        This object defines the name of a terminal unit in an air loop.
    
    """
    internal_name = "AirflowNetwork:Distribution:Component:TerminalUnit"
    field_count = 4
    required_fields = ["Terminal Unit Name", "Terminal Unit Object Type", "Air Path Length", "Air Path Hydraulic Diameter"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:Distribution:Component:TerminalUnit`
        """
        self._data = OrderedDict()
        self._data["Terminal Unit Name"] = None
        self._data["Terminal Unit Object Type"] = None
        self._data["Air Path Length"] = None
        self._data["Air Path Hydraulic Diameter"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.terminal_unit_name = None
        else:
            self.terminal_unit_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terminal_unit_object_type = None
        else:
            self.terminal_unit_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_path_length = None
        else:
            self.air_path_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_path_hydraulic_diameter = None
        else:
            self.air_path_hydraulic_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def terminal_unit_name(self):
        """Get terminal_unit_name

        Returns:
            str: the value of `terminal_unit_name` or None if not set
        """
        return self._data["Terminal Unit Name"]

    @terminal_unit_name.setter
    def terminal_unit_name(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Name`
        Enter the name of a terminal unit in the AirLoopHVAC.
        
        {u'reference': u'AirflowNetworkComponentNames', 'pytype': 'str', u'required-field': True, u'note': [u'Enter the name of a terminal unit in the AirLoopHVAC.'], u'object-list': u'AFNTerminalUnitNames', u'type': u'object-list'}

        Args:
            value (str): value for IDD Field `Terminal Unit Name`
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
                                 'for field `terminal_unit_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_name`')
        self._data["Terminal Unit Name"] = value

    @property
    def terminal_unit_object_type(self):
        """Get terminal_unit_object_type

        Returns:
            str: the value of `terminal_unit_object_type` or None if not set
        """
        return self._data["Terminal Unit Object Type"]

    @terminal_unit_object_type.setter
    def terminal_unit_object_type(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Object Type`
        Select the type of terminal unit corresponding to the name entered in the field above.
        
        {u'note': [u'Select the type of terminal unit corresponding to the name entered in the field above.'], u'type': u'choice', u'key': [u'AirTerminal:SingleDuct:ConstantVolume:Reheat', u'AirTerminal:SingleDuct:VAV:Reheat'], u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Terminal Unit Object Type`
                Accepted values are:
                      - AirTerminal:SingleDuct:ConstantVolume:Reheat
                      - AirTerminal:SingleDuct:VAV:Reheat
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
                                 'for field `terminal_unit_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_object_type`')
            vals = {}
            vals["airterminal:singleduct:constantvolume:reheat"] = "AirTerminal:SingleDuct:ConstantVolume:Reheat"
            vals["airterminal:singleduct:vav:reheat"] = "AirTerminal:SingleDuct:VAV:Reheat"
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
                                     'field `terminal_unit_object_type`'.format(value))
            value = vals[value_lower]
        self._data["Terminal Unit Object Type"] = value

    @property
    def air_path_length(self):
        """Get air_path_length

        Returns:
            float: the value of `air_path_length` or None if not set
        """
        return self._data["Air Path Length"]

    @air_path_length.setter
    def air_path_length(self, value=None):
        """  Corresponds to IDD Field `Air Path Length`
        Enter the air path length (depth) for the terminal unit.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the air path length (depth) for the terminal unit.'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Path Length`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `air_path_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_path_length`')
        self._data["Air Path Length"] = value

    @property
    def air_path_hydraulic_diameter(self):
        """Get air_path_hydraulic_diameter

        Returns:
            float: the value of `air_path_hydraulic_diameter` or None if not set
        """
        return self._data["Air Path Hydraulic Diameter"]

    @air_path_hydraulic_diameter.setter
    def air_path_hydraulic_diameter(self, value=None):
        """  Corresponds to IDD Field `Air Path Hydraulic Diameter`
        Enter the hydraulic diameter of this terminal unit. The hydraulic diameter is
        defined as 4 multiplied by the cross section area divided by perimeter.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the hydraulic diameter of this terminal unit. The hydraulic diameter is', u'defined as 4 multiplied by the cross section area divided by perimeter.'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Air Path Hydraulic Diameter`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `air_path_hydraulic_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_path_hydraulic_diameter`')
        self._data["Air Path Hydraulic Diameter"] = value

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

class AirflowNetworkDistributionComponentConstantPressureDrop(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:ConstantPressureDrop`
        This object defines the characteristics of a constant pressure drop component (e.g. filter).
        Each node connected to this object can not be a node of mixer, splitter, a node of air primary
        loop, or zone equipment loop. It is recommended to connect to a duct component at both ends.
    
    """
    internal_name = "AirflowNetwork:Distribution:Component:ConstantPressureDrop"
    field_count = 2
    required_fields = ["Name", "Pressure Difference Across the Component"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:Distribution:Component:ConstantPressureDrop`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Pressure Difference Across the Component"] = None
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
            self.pressure_difference_across_the_component = None
        else:
            self.pressure_difference_across_the_component = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'AirflowNetworkComponentNames', u'required-field': True, 'pytype': 'str'}

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
    def pressure_difference_across_the_component(self):
        """Get pressure_difference_across_the_component

        Returns:
            float: the value of `pressure_difference_across_the_component` or None if not set
        """
        return self._data["Pressure Difference Across the Component"]

    @pressure_difference_across_the_component.setter
    def pressure_difference_across_the_component(self, value=None):
        """  Corresponds to IDD Field `Pressure Difference Across the Component`
        Enter the pressure drop across this component.
        
        {'pytype': 'float', u'minimum>': '0.0', u'required-field': True, u'note': [u'Enter the pressure drop across this component.'], u'units': u'Pa', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Pressure Difference Across the Component`
                Units: Pa
                value > 0.0
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
                                 'for field `pressure_difference_across_the_component`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pressure_difference_across_the_component`')
        self._data["Pressure Difference Across the Component"] = value

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

class AirflowNetworkDistributionLinkage(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Linkage`
        This object defines the connection between two nodes and a component.
    
    """
    internal_name = "AirflowNetwork:Distribution:Linkage"
    field_count = 5
    required_fields = ["Name", "Node 1 Name", "Node 2 Name", "Component Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirflowNetwork:Distribution:Linkage`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Node 1 Name"] = None
        self._data["Node 2 Name"] = None
        self._data["Component Name"] = None
        self._data["Thermal Zone Name"] = None
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
            self.node_1_name = None
        else:
            self.node_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.node_2_name = None
        else:
            self.node_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_name = None
        else:
            self.component_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_zone_name = None
        else:
            self.thermal_zone_name = vals[i]
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
        Enter a unique name for this object.
        
        {u'note': [u'Enter a unique name for this object.'], u'type': u'alpha', u'reference': u'AirflowNetwork LinkageNames', u'required-field': True, 'pytype': 'str'}

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
    def node_1_name(self):
        """Get node_1_name

        Returns:
            str: the value of `node_1_name` or None if not set
        """
        return self._data["Node 1 Name"]

    @node_1_name.setter
    def node_1_name(self, value=None):
        """  Corresponds to IDD Field `Node 1 Name`
        Enter the name of zone or AirflowNetwork Node.
        
        {u'note': [u'Enter the name of zone or AirflowNetwork Node.'], u'type': u'alpha', u'object-list': u'AirflowNetworkNodeAndZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Node 1 Name`
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
                                 'for field `node_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `node_1_name`')
        self._data["Node 1 Name"] = value

    @property
    def node_2_name(self):
        """Get node_2_name

        Returns:
            str: the value of `node_2_name` or None if not set
        """
        return self._data["Node 2 Name"]

    @node_2_name.setter
    def node_2_name(self, value=None):
        """  Corresponds to IDD Field `Node 2 Name`
        Enter the name of zone or AirflowNetwork Node.
        
        {u'note': [u'Enter the name of zone or AirflowNetwork Node.'], u'type': u'alpha', u'object-list': u'AirflowNetworkNodeAndZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Node 2 Name`
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
                                 'for field `node_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `node_2_name`')
        self._data["Node 2 Name"] = value

    @property
    def component_name(self):
        """Get component_name

        Returns:
            str: the value of `component_name` or None if not set
        """
        return self._data["Component Name"]

    @component_name.setter
    def component_name(self, value=None):
        """  Corresponds to IDD Field `Component Name`
        Enter the name of an AirflowNetwork component. A component is one of the
        following AirflowNetwork:Distribution:Component objects: Leak, LeakageRatio,
        Duct, ConstantVolumeFan, Coil, TerminalUnit, ConstantPressureDrop, or HeatExchanger.
        
        {u'note': [u'Enter the name of an AirflowNetwork component. A component is one of the', u'following AirflowNetwork:Distribution:Component objects: Leak, LeakageRatio,', u'Duct, ConstantVolumeFan, Coil, TerminalUnit, ConstantPressureDrop, or HeatExchanger.'], u'type': u'object-list', u'object-list': u'AirflowNetworkComponentNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Component Name`
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
                                 'for field `component_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `component_name`')
        self._data["Component Name"] = value

    @property
    def thermal_zone_name(self):
        """Get thermal_zone_name

        Returns:
            str: the value of `thermal_zone_name` or None if not set
        """
        return self._data["Thermal Zone Name"]

    @thermal_zone_name.setter
    def thermal_zone_name(self, value=None):
        """  Corresponds to IDD Field `Thermal Zone Name`
        Only used if component = AirflowNetwork:Distribution:Component:Duct
        The zone name is where AirflowNetwork:Distribution:Component:Duct is exposed. Leave this field blank if the duct
        conduction loss is ignored.
        
        {u'note': [u'Only used if component = AirflowNetwork:Distribution:Component:Duct', u'The zone name is where AirflowNetwork:Distribution:Component:Duct is exposed. Leave this field blank if the duct', u'conduction loss is ignored.'], u'type': u'object-list', u'object-list': u'ZoneNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Thermal Zone Name`
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
                                 'for field `thermal_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermal_zone_name`')
        self._data["Thermal Zone Name"] = value

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