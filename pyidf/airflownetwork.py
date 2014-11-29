from collections import OrderedDict

class AirflowNetworkSimulationControl(object):
    """ Corresponds to IDD object `AirflowNetwork:SimulationControl`
        This object defines the global parameters used in an Airflow Network simulation.
    """
    internal_name = "AirflowNetwork:SimulationControl"
    field_count = 14

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:SimulationControl`
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
            self.airflownetwork_control = None
        else:
            self.airflownetwork_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_type = None
        else:
            self.wind_pressure_coefficient_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airflownetwork_wind_pressure_coefficient_array_name = None
        else:
            self.airflownetwork_wind_pressure_coefficient_array_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height_selection_for_local_wind_pressure_calculation = None
        else:
            self.height_selection_for_local_wind_pressure_calculation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.building_type = None
        else:
            self.building_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_number_of_iterations = None
        else:
            self.maximum_number_of_iterations = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initialization_type = None
        else:
            self.initialization_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_airflow_convergence_tolerance = None
        else:
            self.relative_airflow_convergence_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.absolute_airflow_convergence_tolerance = None
        else:
            self.absolute_airflow_convergence_tolerance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convergence_acceleration_limit = None
        else:
            self.convergence_acceleration_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.azimuth_angle_of_long_axis_of_building = None
        else:
            self.azimuth_angle_of_long_axis_of_building = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ratio_of_building_width_along_short_axis_to_width_along_long_axis = None
        else:
            self.ratio_of_building_width_along_short_axis_to_width_along_long_axis = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height_dependence_of_external_node_temperature = None
        else:
            self.height_dependence_of_external_node_temperature = vals[i]
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
        Enter a unique name for this object.

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
    def airflownetwork_control(self):
        """Get airflownetwork_control

        Returns:
            str: the value of `airflownetwork_control` or None if not set
        """
        return self._data["AirflowNetwork Control"]

    @airflownetwork_control.setter
    def airflownetwork_control(self, value="NoMultizoneOrDistribution"):
        """  Corresponds to IDD Field `airflownetwork_control`
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

        Args:
            value (str): value for IDD Field `airflownetwork_control`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airflownetwork_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflownetwork_control`')
            vals = set()
            vals.add("MultizoneWithDistribution")
            vals.add("MultizoneWithoutDistribution")
            vals.add("MultizoneWithDistributionOnlyDuringFanOperation")
            vals.add("NoMultizoneOrDistribution")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `airflownetwork_control`'.format(value))

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
        """  Corresponds to IDD Field `wind_pressure_coefficient_type`
        Input: User must enter AirflowNetwork:MultiZone:WindPressureCoefficientArray,
        AirflowNetwork:MultiZone:ExternalNode, and
        AirflowNetwork:MultiZone:WindPressureCoefficientValues objects.
        SurfaceAverageCalculation: used only for rectangular buildings.
        If SurfaceAverageCalculation is selected,
        AirflowNetwork:MultiZone:WindPressureCoefficientArray, AirflowNetwork:MultiZone:ExternalNode,
        and AirflowNetwork:MultiZone:WindPressureCoefficientValues objects are not used.

        Args:
            value (str): value for IDD Field `wind_pressure_coefficient_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_pressure_coefficient_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_pressure_coefficient_type`')
            vals = set()
            vals.add("Input")
            vals.add("SurfaceAverageCalculation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_pressure_coefficient_type`'.format(value))

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
        """  Corresponds to IDD Field `airflownetwork_wind_pressure_coefficient_array_name`
        Used only if Wind Pressure Coefficient Type = Input, otherwise this field may be left blank.

        Args:
            value (str): value for IDD Field `airflownetwork_wind_pressure_coefficient_array_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airflownetwork_wind_pressure_coefficient_array_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `height_selection_for_local_wind_pressure_calculation`
        If ExternalNode is selected, the height given in the
        AirflowNetwork:MultiZone:ExternalNode object will be used.
        If OpeningHeight is selected, the surface opening height (centroid) will be used to
        calculate local wind pressure
        This field is ignored when the choice of the Wind Pressure Coefficient Type field is
        SurfaceAverageCalculation.

        Args:
            value (str): value for IDD Field `height_selection_for_local_wind_pressure_calculation`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `height_selection_for_local_wind_pressure_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `height_selection_for_local_wind_pressure_calculation`')
            vals = set()
            vals.add("ExternalNode")
            vals.add("OpeningHeight")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `height_selection_for_local_wind_pressure_calculation`'.format(value))

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
        """  Corresponds to IDD Field `building_type`
        Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation,
        otherwise this field may be left blank.

        Args:
            value (str): value for IDD Field `building_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `building_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `building_type`')
            vals = set()
            vals.add("LowRise")
            vals.add("HighRise")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `building_type`'.format(value))

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
        """  Corresponds to IDD Field `maximum_number_of_iterations`
        Determines the maximum number of iterations used to converge on a solution. If this limit
        is exceeded, the program terminates.

        Args:
            value (int): value for IDD Field `maximum_number_of_iterations`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `initialization_type`

        Args:
            value (str): value for IDD Field `initialization_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `initialization_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `initialization_type`')
            vals = set()
            vals.add("LinearInitializationMethod")
            vals.add("ZeroNodePressures")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `initialization_type`'.format(value))

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
        """  Corresponds to IDD Field `relative_airflow_convergence_tolerance`
        This tolerance is defined as the absolute value of the sum of the mass Flow Rates
        divided by the sum of the absolute value of the mass Flow Rates. The mass Flow Rates
        described here refer to the mass Flow Rates at all Nodes in the AirflowNetwork model.
        The solution converges when both this tolerance and the tolerance in the next field
        (Absolute Airflow Convergence Tolerance) are satisfied.

        Args:
            value (float): value for IDD Field `relative_airflow_convergence_tolerance`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `absolute_airflow_convergence_tolerance`
        This tolerance is defined as the absolute value of the sum of the mass flow rates. The mass
        flow rates described here refer to the mass flow rates at all nodes in the AirflowNetwork
        model. The solution converges when both this tolerance and the tolerance in the previous
        field (Relative Airflow Convergence Tolerance) are satisfied.

        Args:
            value (float): value for IDD Field `absolute_airflow_convergence_tolerance`
                Unit: kg/s
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
            except:
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
        """  Corresponds to IDD Field `convergence_acceleration_limit`
        Used only for AirflowNetwork:SimulationControl

        Args:
            value (float): value for IDD Field `convergence_acceleration_limit`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `azimuth_angle_of_long_axis_of_building`
        Degrees clockwise from true North.
        Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation.

        Args:
            value (float): value for IDD Field `azimuth_angle_of_long_axis_of_building`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `ratio_of_building_width_along_short_axis_to_width_along_long_axis`
        Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation.

        Args:
            value (float): value for IDD Field `ratio_of_building_width_along_short_axis_to_width_along_long_axis`
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
            except:
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
        """  Corresponds to IDD Field `height_dependence_of_external_node_temperature`
        If Yes, external node temperature is height dependent.
        If No, external node temperature is based on zero height.

        Args:
            value (str): value for IDD Field `height_dependence_of_external_node_temperature`
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
                                 'for field `height_dependence_of_external_node_temperature`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `height_dependence_of_external_node_temperature`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `height_dependence_of_external_node_temperature`'.format(value))

        self._data["Height Dependence of External Node Temperature"] = value

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
        out.append(self._to_str(self.airflownetwork_control))
        out.append(self._to_str(self.wind_pressure_coefficient_type))
        out.append(self._to_str(self.airflownetwork_wind_pressure_coefficient_array_name))
        out.append(self._to_str(self.height_selection_for_local_wind_pressure_calculation))
        out.append(self._to_str(self.building_type))
        out.append(self._to_str(self.maximum_number_of_iterations))
        out.append(self._to_str(self.initialization_type))
        out.append(self._to_str(self.relative_airflow_convergence_tolerance))
        out.append(self._to_str(self.absolute_airflow_convergence_tolerance))
        out.append(self._to_str(self.convergence_acceleration_limit))
        out.append(self._to_str(self.azimuth_angle_of_long_axis_of_building))
        out.append(self._to_str(self.ratio_of_building_width_along_short_axis_to_width_along_long_axis))
        out.append(self._to_str(self.height_dependence_of_external_node_temperature))
        return ",".join(out)

class AirflowNetworkMultiZoneZone(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Zone`
        This object is used to simultaneously control a thermal zone's window and door openings,
        both exterior and interior.
    """
    internal_name = "AirflowNetwork:MultiZone:Zone"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:Zone`
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

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_control_mode = None
        else:
            self.ventilation_control_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_control_zone_temperature_setpoint_schedule_name = None
        else:
            self.ventilation_control_zone_temperature_setpoint_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_venting_open_factor = None
        else:
            self.minimum_venting_open_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor = None
        else:
            self.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor = None
        else:
            self.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = None
        else:
            self.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor = None
        else:
            self.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.venting_availability_schedule_name = None
        else:
            self.venting_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.single_sided_wind_pressure_coefficient_algorithm = None
        else:
            self.single_sided_wind_pressure_coefficient_algorithm = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.facade_width = None
        else:
            self.facade_width = vals[i]
        i += 1

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
        Enter the zone name where ventilation control is required.

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
        """  Corresponds to IDD Field `ventilation_control_mode`
        When Ventilation Control Mode = Temperature or Enthalpy, the following
        fields are used to modulate the Ventilation Open Factor for all
        window and door openings in the zone according to the zone's
        indoor-outdoor temperature or enthalpy difference.
        Constant: controlled by field Venting Schedule Name.
        NoVent: control will not open window or door during simulation (Ventilation Open Factor = 0).

        Args:
            value (str): value for IDD Field `ventilation_control_mode`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ventilation_control_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ventilation_control_mode`')
            vals = set()
            vals.add("Temperature")
            vals.add("Enthalpy")
            vals.add("Constant")
            vals.add("ASHRAE55Adaptive")
            vals.add("CEN15251Adaptive")
            vals.add("NoVent")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `ventilation_control_mode`'.format(value))

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
        """  Corresponds to IDD Field `ventilation_control_zone_temperature_setpoint_schedule_name`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.

        Args:
            value (str): value for IDD Field `ventilation_control_zone_temperature_setpoint_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ventilation_control_zone_temperature_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `minimum_venting_open_factor`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.

        Args:
            value (float): value for IDD Field `minimum_venting_open_factor`
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
        """  Corresponds to IDD Field `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor`
        Applicable only if Ventilation Control Mode = Temperature.
        This value must be less than the corresponding upper value (next field).

        Args:
            value (float): value for IDD Field `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor`
                Unit: deltaC
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
            except:
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
        """  Corresponds to IDD Field `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor`
        Applicable only if Ventilation Control Mode = Temperature.
        This value must be greater than the corresponding lower value (previous field).

        Args:
            value (float): value for IDD Field `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor`
                Unit: deltaC
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
            except:
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
        """  Corresponds to IDD Field `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be less than the corresponding upper value (next field).

        Args:
            value (float): value for IDD Field `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor`
                Unit: deltaJ/kg
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
            except:
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
        """  Corresponds to IDD Field `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be greater than the corresponding lower value (previous field).

        Args:
            value (float): value for IDD Field `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor`
                Unit: deltaJ/kg
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
            except:
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
        """  Corresponds to IDD Field `venting_availability_schedule_name`
        Non-zero Schedule value means venting is allowed if other venting control conditions are
        satisfied. A zero (or negative) Schedule value means venting is not allowed under any
        The Schedule values should be greater than or equal to 0 and less than or equal to 1.
        circumstances. If this Schedule is not specified then venting is allowed if
        other venting control conditions are satisfied.
        Not used if Ventilation Control Mode = NoVent.

        Args:
            value (str): value for IDD Field `venting_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `venting_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `single_sided_wind_pressure_coefficient_algorithm`
        Selecting Advanced results in EnergyPlus calculating modified Wind Pressure Coefficients
        to account for wind direction and turbulence effects on single sided ventilation rates.
        Model is only valid for zones with 2 openings, both of which are on a single facade.

        Args:
            value (str): value for IDD Field `single_sided_wind_pressure_coefficient_algorithm`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `single_sided_wind_pressure_coefficient_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `single_sided_wind_pressure_coefficient_algorithm`')
            vals = set()
            vals.add("Advanced")
            vals.add("Standard")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `single_sided_wind_pressure_coefficient_algorithm`'.format(value))

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
        """  Corresponds to IDD Field `facade_width`
        This is the whole building width along the direction of the facade of this zone.

        Args:
            value (float): value for IDD Field `facade_width`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `facade_width`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `facade_width`')

        self._data["Facade Width"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.ventilation_control_mode))
        out.append(self._to_str(self.ventilation_control_zone_temperature_setpoint_schedule_name))
        out.append(self._to_str(self.minimum_venting_open_factor))
        out.append(self._to_str(self.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor))
        out.append(self._to_str(self.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor))
        out.append(self._to_str(self.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor))
        out.append(self._to_str(self.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor))
        out.append(self._to_str(self.venting_availability_schedule_name))
        out.append(self._to_str(self.single_sided_wind_pressure_coefficient_algorithm))
        out.append(self._to_str(self.facade_width))
        return ",".join(out)

class AirflowNetworkMultiZoneSurface(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Surface`
        This object specifies the properties of a surface linkage through which air flows.
        Airflow Report: Node 1 as an inside face zone;
        Node 2 as an outside face zone or external node.
    """
    internal_name = "AirflowNetwork:MultiZone:Surface"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:Surface`
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

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leakage_component_name = None
        else:
            self.leakage_component_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.external_node_name = None
        else:
            self.external_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_or_door_opening_factor_or_crack_factor = None
        else:
            self.window_or_door_opening_factor_or_crack_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_control_mode = None
        else:
            self.ventilation_control_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ventilation_control_zone_temperature_setpoint_schedule_name = None
        else:
            self.ventilation_control_zone_temperature_setpoint_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_venting_open_factor = None
        else:
            self.minimum_venting_open_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor = None
        else:
            self.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor = None
        else:
            self.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = None
        else:
            self.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor = None
        else:
            self.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.venting_availability_schedule_name = None
        else:
            self.venting_availability_schedule_name = vals[i]
        i += 1

    @property
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `surface_name`
        Enter the name of a heat transfer surface.

        Args:
            value (str): value for IDD Field `surface_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `leakage_component_name`
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

        Args:
            value (str): value for IDD Field `leakage_component_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `leakage_component_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `external_node_name`
        Used if Wind Pressure Coefficient Type = Input in the AirflowNetwork:SimulationControl object,
        otherwise this field may be left blank.

        Args:
            value (str): value for IDD Field `external_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `external_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `window_or_door_opening_factor_or_crack_factor`
        This field specifies a multiplier for a crack, window, or door.

        Args:
            value (float): value for IDD Field `window_or_door_opening_factor_or_crack_factor`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `ventilation_control_mode`
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

        Args:
            value (str): value for IDD Field `ventilation_control_mode`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ventilation_control_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ventilation_control_mode`')
            vals = set()
            vals.add("Temperature")
            vals.add("Enthalpy")
            vals.add("Constant")
            vals.add("ASHRAE55Adaptive")
            vals.add("CEN15251Adaptive")
            vals.add("NoVent")
            vals.add("ZoneLevel")
            vals.add("AdjacentTemperature")
            vals.add("AdjacentEnthalpy")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `ventilation_control_mode`'.format(value))

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
        """  Corresponds to IDD Field `ventilation_control_zone_temperature_setpoint_schedule_name`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.

        Args:
            value (str): value for IDD Field `ventilation_control_zone_temperature_setpoint_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ventilation_control_zone_temperature_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `minimum_venting_open_factor`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.

        Args:
            value (float): value for IDD Field `minimum_venting_open_factor`
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
        """  Corresponds to IDD Field `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor`
        Applicable only if Ventilation Control Mode = Temperature

        Args:
            value (float): value for IDD Field `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor`
                Unit: deltaC
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
            except:
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
        """  Corresponds to IDD Field `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor`
        Applicable only if Ventilation Control Mode = Temperature.
        This value must be greater than the corresponding lower value (previous field).

        Args:
            value (float): value for IDD Field `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor`
                Unit: deltaC
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
            except:
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
        """  Corresponds to IDD Field `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be less than the corresponding upper value (next field).

        Args:
            value (float): value for IDD Field `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor`
                Unit: deltaJ/kg
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
            except:
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
        """  Corresponds to IDD Field `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be greater than the corresponding lower value (previous field).

        Args:
            value (float): value for IDD Field `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor`
                Unit: deltaJ/kg
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
            except:
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
        """  Corresponds to IDD Field `venting_availability_schedule_name`
        Non-zero schedule value means venting is allowed if other venting control conditions are
        satisfied. A zero (or negative) schedule value means venting is not allowed under any
        circumstances. The schedule values should be greater than or equal to 0 and less than or
        equal to 1. If this schedule is not specified then venting is allowed if
        other venting control conditions are satisfied.
        Not used if Ventilation Control Mode = NoVent or ZoneLevel.

        Args:
            value (str): value for IDD Field `venting_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `venting_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `venting_availability_schedule_name`')

        self._data["Venting Availability Schedule Name"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.leakage_component_name))
        out.append(self._to_str(self.external_node_name))
        out.append(self._to_str(self.window_or_door_opening_factor_or_crack_factor))
        out.append(self._to_str(self.ventilation_control_mode))
        out.append(self._to_str(self.ventilation_control_zone_temperature_setpoint_schedule_name))
        out.append(self._to_str(self.minimum_venting_open_factor))
        out.append(self._to_str(self.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor))
        out.append(self._to_str(self.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor))
        out.append(self._to_str(self.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor))
        out.append(self._to_str(self.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor))
        out.append(self._to_str(self.venting_availability_schedule_name))
        return ",".join(out)

class AirflowNetworkMultiZoneReferenceCrackConditions(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:ReferenceCrackConditions`
        This object specifies the conditions under which the air mass flow coefficient was measured.
    """
    internal_name = "AirflowNetwork:MultiZone:ReferenceCrackConditions"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:ReferenceCrackConditions`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Temperature"] = None
        self._data["Reference Barometric Pressure"] = None
        self._data["Reference Humidity Ratio"] = None

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
            self.reference_temperature = None
        else:
            self.reference_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_barometric_pressure = None
        else:
            self.reference_barometric_pressure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_humidity_ratio = None
        else:
            self.reference_humidity_ratio = vals[i]
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
        Enter a unique name for this object.

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
    def reference_temperature(self):
        """Get reference_temperature

        Returns:
            float: the value of `reference_temperature` or None if not set
        """
        return self._data["Reference Temperature"]

    @reference_temperature.setter
    def reference_temperature(self, value=20.0 ):
        """  Corresponds to IDD Field `reference_temperature`
        Enter the reference temperature under which the surface crack data were obtained.

        Args:
            value (float): value for IDD Field `reference_temperature`
                Unit: C
                Default value: 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `reference_barometric_pressure`
        Enter the reference barometric pressure under which the surface crack data were obtained.

        Args:
            value (float): value for IDD Field `reference_barometric_pressure`
                Unit: Pa
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
            except:
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
        """  Corresponds to IDD Field `reference_humidity_ratio`
        Enter the reference humidity ratio under which the surface crack data were obtained.

        Args:
            value (float): value for IDD Field `reference_humidity_ratio`
                Unit: kgWater/kgDryAir
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
                                 'for field `reference_humidity_ratio`'.format(value))

        self._data["Reference Humidity Ratio"] = value

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
        out.append(self._to_str(self.reference_temperature))
        out.append(self._to_str(self.reference_barometric_pressure))
        out.append(self._to_str(self.reference_humidity_ratio))
        return ",".join(out)

class AirflowNetworkMultiZoneSurfaceCrack(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Surface:Crack`
        This object specifies the properties of airflow through a crack.
    """
    internal_name = "AirflowNetwork:MultiZone:Surface:Crack"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:Surface:Crack`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient at Reference Conditions"] = None
        self._data["Air Mass Flow Exponent"] = None
        self._data["Reference Crack Conditions"] = None

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
            self.air_mass_flow_coefficient_at_reference_conditions = None
        else:
            self.air_mass_flow_coefficient_at_reference_conditions = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent = None
        else:
            self.air_mass_flow_exponent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_crack_conditions = None
        else:
            self.reference_crack_conditions = vals[i]
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
        Enter a unique name for this object.

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
    def air_mass_flow_coefficient_at_reference_conditions(self):
        """Get air_mass_flow_coefficient_at_reference_conditions

        Returns:
            float: the value of `air_mass_flow_coefficient_at_reference_conditions` or None if not set
        """
        return self._data["Air Mass Flow Coefficient at Reference Conditions"]

    @air_mass_flow_coefficient_at_reference_conditions.setter
    def air_mass_flow_coefficient_at_reference_conditions(self, value=None):
        """  Corresponds to IDD Field `air_mass_flow_coefficient_at_reference_conditions`
        Enter the air mass flow coefficient at the conditions defined
        in the Reference Crack Conditions object.
        Defined at 1 Pa pressure difference across this crack.

        Args:
            value (float): value for IDD Field `air_mass_flow_coefficient_at_reference_conditions`
                Unit: kg/s
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
        """  Corresponds to IDD Field `air_mass_flow_exponent`
        Enter the air mass flow exponent for the surface crack.

        Args:
            value (float): value for IDD Field `air_mass_flow_exponent`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `reference_crack_conditions`
        Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with
        the air mass flow coefficient entered above.

        Args:
            value (str): value for IDD Field `reference_crack_conditions`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reference_crack_conditions`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_crack_conditions`')

        self._data["Reference Crack Conditions"] = value

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
        out.append(self._to_str(self.air_mass_flow_coefficient_at_reference_conditions))
        out.append(self._to_str(self.air_mass_flow_exponent))
        out.append(self._to_str(self.reference_crack_conditions))
        return ",".join(out)

class AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea`
        This object is used to define surface air leakage.
    """
    internal_name = "AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Effective Leakage Area"] = None
        self._data["Discharge Coefficient"] = None
        self._data["Reference Pressure Difference"] = None
        self._data["Air Mass Flow Exponent"] = None

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
            self.effective_leakage_area = None
        else:
            self.effective_leakage_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient = None
        else:
            self.discharge_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_pressure_difference = None
        else:
            self.reference_pressure_difference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent = None
        else:
            self.air_mass_flow_exponent = vals[i]
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
        Enter a unique name for this object.

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
    def effective_leakage_area(self):
        """Get effective_leakage_area

        Returns:
            float: the value of `effective_leakage_area` or None if not set
        """
        return self._data["Effective Leakage Area"]

    @effective_leakage_area.setter
    def effective_leakage_area(self, value=None):
        """  Corresponds to IDD Field `effective_leakage_area`
        Enter the effective leakage area.

        Args:
            value (float): value for IDD Field `effective_leakage_area`
                Unit: m2
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
        """  Corresponds to IDD Field `discharge_coefficient`
        Enter the coefficient used in the air mass flow equation.

        Args:
            value (float): value for IDD Field `discharge_coefficient`
                Unit: dimensionless
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
        """  Corresponds to IDD Field `reference_pressure_difference`
        Enter the pressure difference used to define the air mass flow coefficient and exponent.

        Args:
            value (float): value for IDD Field `reference_pressure_difference`
                Unit: Pa
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
            except:
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
        """  Corresponds to IDD Field `air_mass_flow_exponent`
        Enter the exponent used in the air mass flow equation.

        Args:
            value (float): value for IDD Field `air_mass_flow_exponent`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `air_mass_flow_exponent`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent`')

        self._data["Air Mass Flow Exponent"] = value

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
        out.append(self._to_str(self.effective_leakage_area))
        out.append(self._to_str(self.discharge_coefficient))
        out.append(self._to_str(self.reference_pressure_difference))
        out.append(self._to_str(self.air_mass_flow_exponent))
        return ",".join(out)

class AirflowNetworkMultiZoneComponentDetailedOpening(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:DetailedOpening`
        This object specifies the properties of airflow through windows and doors (window, door and
        glass door heat transfer subsurfaces) when they are closed or open.
    """
    internal_name = "AirflowNetwork:MultiZone:Component:DetailedOpening"
    field_count = 26

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:Component:DetailedOpening`
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
            self.air_mass_flow_coefficient_when_opening_is_closed = None
        else:
            self.air_mass_flow_coefficient_when_opening_is_closed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent_when_opening_is_closed = None
        else:
            self.air_mass_flow_exponent_when_opening_is_closed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.type_of_rectanguler_large_vertical_opening_lvo = None
        else:
            self.type_of_rectanguler_large_vertical_opening_lvo = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.extra_crack_length_or_height_of_pivoting_axis = None
        else:
            self.extra_crack_length_or_height_of_pivoting_axis = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_sets_of_opening_factor_data = None
        else:
            self.number_of_sets_of_opening_factor_data = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.opening_factor_1 = None
        else:
            self.opening_factor_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_opening_factor_1 = None
        else:
            self.discharge_coefficient_for_opening_factor_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.width_factor_for_opening_factor_1 = None
        else:
            self.width_factor_for_opening_factor_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height_factor_for_opening_factor_1 = None
        else:
            self.height_factor_for_opening_factor_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.start_height_factor_for_opening_factor_1 = None
        else:
            self.start_height_factor_for_opening_factor_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.opening_factor_2 = None
        else:
            self.opening_factor_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_opening_factor_2 = None
        else:
            self.discharge_coefficient_for_opening_factor_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.width_factor_for_opening_factor_2 = None
        else:
            self.width_factor_for_opening_factor_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height_factor_for_opening_factor_2 = None
        else:
            self.height_factor_for_opening_factor_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.start_height_factor_for_opening_factor_2 = None
        else:
            self.start_height_factor_for_opening_factor_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.opening_factor_3 = None
        else:
            self.opening_factor_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_opening_factor_3 = None
        else:
            self.discharge_coefficient_for_opening_factor_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.width_factor_for_opening_factor_3 = None
        else:
            self.width_factor_for_opening_factor_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height_factor_for_opening_factor_3 = None
        else:
            self.height_factor_for_opening_factor_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.start_height_factor_for_opening_factor_3 = None
        else:
            self.start_height_factor_for_opening_factor_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.opening_factor_4 = None
        else:
            self.opening_factor_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_opening_factor_4 = None
        else:
            self.discharge_coefficient_for_opening_factor_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.width_factor_for_opening_factor_4 = None
        else:
            self.width_factor_for_opening_factor_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height_factor_for_opening_factor_4 = None
        else:
            self.height_factor_for_opening_factor_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.start_height_factor_for_opening_factor_4 = None
        else:
            self.start_height_factor_for_opening_factor_4 = vals[i]
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
        Enter a unique name for this object.

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
    def air_mass_flow_coefficient_when_opening_is_closed(self):
        """Get air_mass_flow_coefficient_when_opening_is_closed

        Returns:
            float: the value of `air_mass_flow_coefficient_when_opening_is_closed` or None if not set
        """
        return self._data["Air Mass Flow Coefficient When Opening is Closed"]

    @air_mass_flow_coefficient_when_opening_is_closed.setter
    def air_mass_flow_coefficient_when_opening_is_closed(self, value=None):
        """  Corresponds to IDD Field `air_mass_flow_coefficient_when_opening_is_closed`
        Defined at 1 Pa per meter of crack length. Enter the coefficient used in the following
        equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.

        Args:
            value (float): value for IDD Field `air_mass_flow_coefficient_when_opening_is_closed`
                Unit: kg/s-m
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
        """  Corresponds to IDD Field `air_mass_flow_exponent_when_opening_is_closed`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.

        Args:
            value (float): value for IDD Field `air_mass_flow_exponent_when_opening_is_closed`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `type_of_rectanguler_large_vertical_opening_lvo`
        Select the type of vertical opening: Non-pivoted opening or Horizontally pivoted opening.

        Args:
            value (str): value for IDD Field `type_of_rectanguler_large_vertical_opening_lvo`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `type_of_rectanguler_large_vertical_opening_lvo`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type_of_rectanguler_large_vertical_opening_lvo`')
            vals = set()
            vals.add("NonPivoted")
            vals.add("HorizontallyPivoted")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `type_of_rectanguler_large_vertical_opening_lvo`'.format(value))

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
        """  Corresponds to IDD Field `extra_crack_length_or_height_of_pivoting_axis`
        Extra crack length is used for LVO Non-pivoted type with multiple openable parts.
        Height of pivoting axis is used for LVO Horizontally pivoted type.
        Specifies window or door characteristics that depend on the LVO type.
        For Non-pivoted Type (rectangular windows and doors), this field is the extra crack length
        in meters due to multiple openable parts, if present.  Extra here means in addition
        to the length of the cracks on the top, bottom and sides of the window/door.
        For Horizontally pivoted Type, this field gives the height of the
        pivoting axis measured from the bottom of the glazed part of the window (m).

        Args:
            value (float): value for IDD Field `extra_crack_length_or_height_of_pivoting_axis`
                Unit: m
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
        """  Corresponds to IDD Field `number_of_sets_of_opening_factor_data`
        Enter the number of the following sets of data for opening factor,
        discharge coefficient, width factor, height factor, and start height factor.

        Args:
            value (int): value for IDD Field `number_of_sets_of_opening_factor_data`
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
            except:
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
        """  Corresponds to IDD Field `opening_factor_1`
        This value must be specified as 0.

        Args:
            value (float): value for IDD Field `opening_factor_1`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `discharge_coefficient_for_opening_factor_1`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through a window or door at that Opening Factor.

        Args:
            value (float): value for IDD Field `discharge_coefficient_for_opening_factor_1`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `width_factor_for_opening_factor_1`
        The Width Factor is the opening width divided by the window or door width.

        Args:
            value (float): value for IDD Field `width_factor_for_opening_factor_1`
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
        """  Corresponds to IDD Field `height_factor_for_opening_factor_1`
        The Height Factor is the opening height divided by the window or door height.

        Args:
            value (float): value for IDD Field `height_factor_for_opening_factor_1`
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
        """  Corresponds to IDD Field `start_height_factor_for_opening_factor_1`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.

        Args:
            value (float): value for IDD Field `start_height_factor_for_opening_factor_1`
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
        """  Corresponds to IDD Field `opening_factor_2`
        If Number of Sets of Opening Factor Data = 2, this value must be 1.0.
        If Number of Sets of Opening Factor Data = 3, this value must be less than 1.0.
        If Number of Sets of Opening Factor Data = 4, this value must be less than the
        value entered for Opening factor 3 and greater than the value entered
        for Opening factor 1.

        Args:
            value (float): value for IDD Field `opening_factor_2`
                Unit: dimensionless
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
        """  Corresponds to IDD Field `discharge_coefficient_for_opening_factor_2`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through a window or door at that Opening Factor.

        Args:
            value (float): value for IDD Field `discharge_coefficient_for_opening_factor_2`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `width_factor_for_opening_factor_2`
        The Width Factor is the opening width divided by the window or door width.

        Args:
            value (float): value for IDD Field `width_factor_for_opening_factor_2`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `height_factor_for_opening_factor_2`
        The Height Factor is the opening height divided by the window or door height.

        Args:
            value (float): value for IDD Field `height_factor_for_opening_factor_2`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `start_height_factor_for_opening_factor_2`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.

        Args:
            value (float): value for IDD Field `start_height_factor_for_opening_factor_2`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `opening_factor_3`
        If Number of Sets of Opening Factor Data = 3, this value must be 1.0.
        If Number of Sets of Opening Factor Data = 4, this value must be less than 1.0,
        and greater than value entered for Opening factor 2.

        Args:
            value (float): value for IDD Field `opening_factor_3`
                Unit: dimensionless
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
        """  Corresponds to IDD Field `discharge_coefficient_for_opening_factor_3`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through a window or door at that Opening Factor.

        Args:
            value (float): value for IDD Field `discharge_coefficient_for_opening_factor_3`
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
        """  Corresponds to IDD Field `width_factor_for_opening_factor_3`
        The Width Factor is the opening width divided by the window or door width.

        Args:
            value (float): value for IDD Field `width_factor_for_opening_factor_3`
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
        """  Corresponds to IDD Field `height_factor_for_opening_factor_3`
        The Height Factor is the opening height divided by the window or door height.

        Args:
            value (float): value for IDD Field `height_factor_for_opening_factor_3`
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
        """  Corresponds to IDD Field `start_height_factor_for_opening_factor_3`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.

        Args:
            value (float): value for IDD Field `start_height_factor_for_opening_factor_3`
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
        """  Corresponds to IDD Field `opening_factor_4`
        If Number of Sets of Opening Factor Data = 4, this value must be 1.0

        Args:
            value (float): value for IDD Field `opening_factor_4`
                Unit: dimensionless
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
        """  Corresponds to IDD Field `discharge_coefficient_for_opening_factor_4`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through a window or door at that Opening Factor.

        Args:
            value (float): value for IDD Field `discharge_coefficient_for_opening_factor_4`
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
        """  Corresponds to IDD Field `width_factor_for_opening_factor_4`
        The Width Factor is the opening width divided by the window or door width.

        Args:
            value (float): value for IDD Field `width_factor_for_opening_factor_4`
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
        """  Corresponds to IDD Field `height_factor_for_opening_factor_4`
        The Height Factor is the opening height divided by the window or door height.

        Args:
            value (float): value for IDD Field `height_factor_for_opening_factor_4`
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
        """  Corresponds to IDD Field `start_height_factor_for_opening_factor_4`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.

        Args:
            value (float): value for IDD Field `start_height_factor_for_opening_factor_4`
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
                                 'for field `start_height_factor_for_opening_factor_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `start_height_factor_for_opening_factor_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `start_height_factor_for_opening_factor_4`')

        self._data["Start Height Factor for Opening Factor 4"] = value

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
        out.append(self._to_str(self.air_mass_flow_coefficient_when_opening_is_closed))
        out.append(self._to_str(self.air_mass_flow_exponent_when_opening_is_closed))
        out.append(self._to_str(self.type_of_rectanguler_large_vertical_opening_lvo))
        out.append(self._to_str(self.extra_crack_length_or_height_of_pivoting_axis))
        out.append(self._to_str(self.number_of_sets_of_opening_factor_data))
        out.append(self._to_str(self.opening_factor_1))
        out.append(self._to_str(self.discharge_coefficient_for_opening_factor_1))
        out.append(self._to_str(self.width_factor_for_opening_factor_1))
        out.append(self._to_str(self.height_factor_for_opening_factor_1))
        out.append(self._to_str(self.start_height_factor_for_opening_factor_1))
        out.append(self._to_str(self.opening_factor_2))
        out.append(self._to_str(self.discharge_coefficient_for_opening_factor_2))
        out.append(self._to_str(self.width_factor_for_opening_factor_2))
        out.append(self._to_str(self.height_factor_for_opening_factor_2))
        out.append(self._to_str(self.start_height_factor_for_opening_factor_2))
        out.append(self._to_str(self.opening_factor_3))
        out.append(self._to_str(self.discharge_coefficient_for_opening_factor_3))
        out.append(self._to_str(self.width_factor_for_opening_factor_3))
        out.append(self._to_str(self.height_factor_for_opening_factor_3))
        out.append(self._to_str(self.start_height_factor_for_opening_factor_3))
        out.append(self._to_str(self.opening_factor_4))
        out.append(self._to_str(self.discharge_coefficient_for_opening_factor_4))
        out.append(self._to_str(self.width_factor_for_opening_factor_4))
        out.append(self._to_str(self.height_factor_for_opening_factor_4))
        out.append(self._to_str(self.start_height_factor_for_opening_factor_4))
        return ",".join(out)

class AirflowNetworkMultiZoneComponentSimpleOpening(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:SimpleOpening`
        This object specifies the properties of air flow through windows and doors (window, door and
        glass door heat transfer subsurfaces) when they are closed or open.
    """
    internal_name = "AirflowNetwork:MultiZone:Component:SimpleOpening"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:Component:SimpleOpening`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient When Opening is Closed"] = None
        self._data["Air Mass Flow Exponent When Opening is Closed"] = None
        self._data["Minimum Density Difference for Two-Way Flow"] = None
        self._data["Discharge Coefficient"] = None

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
            self.air_mass_flow_coefficient_when_opening_is_closed = None
        else:
            self.air_mass_flow_coefficient_when_opening_is_closed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent_when_opening_is_closed = None
        else:
            self.air_mass_flow_exponent_when_opening_is_closed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_density_difference_for_twoway_flow = None
        else:
            self.minimum_density_difference_for_twoway_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient = None
        else:
            self.discharge_coefficient = vals[i]
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
        Enter a unique name for this object.

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
    def air_mass_flow_coefficient_when_opening_is_closed(self):
        """Get air_mass_flow_coefficient_when_opening_is_closed

        Returns:
            float: the value of `air_mass_flow_coefficient_when_opening_is_closed` or None if not set
        """
        return self._data["Air Mass Flow Coefficient When Opening is Closed"]

    @air_mass_flow_coefficient_when_opening_is_closed.setter
    def air_mass_flow_coefficient_when_opening_is_closed(self, value=None):
        """  Corresponds to IDD Field `air_mass_flow_coefficient_when_opening_is_closed`
        Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.

        Args:
            value (float): value for IDD Field `air_mass_flow_coefficient_when_opening_is_closed`
                Unit: kg/s-m
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
        """  Corresponds to IDD Field `air_mass_flow_exponent_when_opening_is_closed`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.

        Args:
            value (float): value for IDD Field `air_mass_flow_exponent_when_opening_is_closed`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `minimum_density_difference_for_twoway_flow`
        Enter the minimum density difference above which two-way flow may occur due to stack effect.

        Args:
            value (float): value for IDD Field `minimum_density_difference_for_twoway_flow`
                Unit: kg/m3
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
        """  Corresponds to IDD Field `discharge_coefficient`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through a window or door at that Opening Factor.

        Args:
            value (float): value for IDD Field `discharge_coefficient`
                Unit: dimensionless
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
                                 'for field `discharge_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `discharge_coefficient`')

        self._data["Discharge Coefficient"] = value

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
        out.append(self._to_str(self.air_mass_flow_coefficient_when_opening_is_closed))
        out.append(self._to_str(self.air_mass_flow_exponent_when_opening_is_closed))
        out.append(self._to_str(self.minimum_density_difference_for_twoway_flow))
        out.append(self._to_str(self.discharge_coefficient))
        return ",".join(out)

class AirflowNetworkMultiZoneComponentHorizontalOpening(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:HorizontalOpening`
        This object specifies the properties of air flow through a horizontal opening
    """
    internal_name = "AirflowNetwork:MultiZone:Component:HorizontalOpening"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:Component:HorizontalOpening`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient When Opening is Closed"] = None
        self._data["Air Mass Flow Exponent When Opening is Closed"] = None
        self._data["Sloping Plane Angle"] = None
        self._data["Discharge Coefficient"] = None

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
            self.air_mass_flow_coefficient_when_opening_is_closed = None
        else:
            self.air_mass_flow_coefficient_when_opening_is_closed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent_when_opening_is_closed = None
        else:
            self.air_mass_flow_exponent_when_opening_is_closed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sloping_plane_angle = None
        else:
            self.sloping_plane_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient = None
        else:
            self.discharge_coefficient = vals[i]
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
        Enter a unique name for this object.

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
    def air_mass_flow_coefficient_when_opening_is_closed(self):
        """Get air_mass_flow_coefficient_when_opening_is_closed

        Returns:
            float: the value of `air_mass_flow_coefficient_when_opening_is_closed` or None if not set
        """
        return self._data["Air Mass Flow Coefficient When Opening is Closed"]

    @air_mass_flow_coefficient_when_opening_is_closed.setter
    def air_mass_flow_coefficient_when_opening_is_closed(self, value=None):
        """  Corresponds to IDD Field `air_mass_flow_coefficient_when_opening_is_closed`
        Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation:
        Mass flow rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening is closed.

        Args:
            value (float): value for IDD Field `air_mass_flow_coefficient_when_opening_is_closed`
                Unit: kg/s-m
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
        """  Corresponds to IDD Field `air_mass_flow_exponent_when_opening_is_closed`
        Enter the exponent used in the following equation:
        Mass flow rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening is closed.

        Args:
            value (float): value for IDD Field `air_mass_flow_exponent_when_opening_is_closed`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `sloping_plane_angle`
        Sloping plane angle = 90 is equivalent to fully open.

        Args:
            value (float): value for IDD Field `sloping_plane_angle`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `discharge_coefficient`
        The Discharge Coefficient indicates the fractional effectiveness
        for air flow through the opening at that Opening Factor.

        Args:
            value (float): value for IDD Field `discharge_coefficient`
                Unit: dimensionless
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
                                 'for field `discharge_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `discharge_coefficient`')

        self._data["Discharge Coefficient"] = value

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
        out.append(self._to_str(self.air_mass_flow_coefficient_when_opening_is_closed))
        out.append(self._to_str(self.air_mass_flow_exponent_when_opening_is_closed))
        out.append(self._to_str(self.sloping_plane_angle))
        out.append(self._to_str(self.discharge_coefficient))
        return ",".join(out)

class AirflowNetworkMultiZoneComponentZoneExhaustFan(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:ZoneExhaustFan`
        This object specifies the additional properties for a zone exhaust fan
        to perform multizone airflow calculations.
    """
    internal_name = "AirflowNetwork:MultiZone:Component:ZoneExhaustFan"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:Component:ZoneExhaustFan`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions"] = None
        self._data["Air Mass Flow Exponent When the Zone Exhaust Fan is Off"] = None
        self._data["Reference Crack Conditions"] = None

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
            self.air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions = None
        else:
            self.air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off = None
        else:
            self.air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_crack_conditions = None
        else:
            self.reference_crack_conditions = vals[i]
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
        Enter the name of a Fan:ZoneExhaust object.

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
    def air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions(self):
        """Get air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions

        Returns:
            float: the value of `air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions` or None if not set
        """
        return self._data["Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions"]

    @air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions.setter
    def air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions(self, value=None):
        """  Corresponds to IDD Field `air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions`
        Enter the air mass flow coefficient at the conditions defined
        in the Reference Crack Conditions object.
        Defined at 1 Pa pressure difference. Enter the coefficient used in the following
        equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when the fan is off.

        Args:
            value (float): value for IDD Field `air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions`
                Unit: kg/s
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
        """  Corresponds to IDD Field `air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when the fan is off.

        Args:
            value (float): value for IDD Field `air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off`
                Unit: dimensionless
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
            except:
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
        """  Corresponds to IDD Field `reference_crack_conditions`
        Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with
        the air mass flow coefficient entered above.

        Args:
            value (str): value for IDD Field `reference_crack_conditions`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reference_crack_conditions`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_crack_conditions`')

        self._data["Reference Crack Conditions"] = value

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
        out.append(self._to_str(self.air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions))
        out.append(self._to_str(self.air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off))
        out.append(self._to_str(self.reference_crack_conditions))
        return ",".join(out)

class AirflowNetworkMultiZoneExternalNode(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:ExternalNode`
        This object defines outdoor environmental conditions outside of the building.
    """
    internal_name = "AirflowNetwork:MultiZone:ExternalNode"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:ExternalNode`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["External Node Height"] = None
        self._data["Wind Pressure Coefficient Values Object Name"] = None

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
            self.external_node_height = None
        else:
            self.external_node_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_values_object_name = None
        else:
            self.wind_pressure_coefficient_values_object_name = vals[i]
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
        Enter a unique name for this object.
        This node name will be referenced by a particular building facade.

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
    def external_node_height(self):
        """Get external_node_height

        Returns:
            float: the value of `external_node_height` or None if not set
        """
        return self._data["External Node Height"]

    @external_node_height.setter
    def external_node_height(self, value=0.0 ):
        """  Corresponds to IDD Field `external_node_height`
        Designates the reference height used to calculate relative pressure.

        Args:
            value (float): value for IDD Field `external_node_height`
                Unit: m
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_values_object_name`
        Enter the name of the AirflowNetwork:MultiZone:WindPressureCoefficientValues object.

        Args:
            value (str): value for IDD Field `wind_pressure_coefficient_values_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_pressure_coefficient_values_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_pressure_coefficient_values_object_name`')

        self._data["Wind Pressure Coefficient Values Object Name"] = value

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
        out.append(self._to_str(self.external_node_height))
        out.append(self._to_str(self.wind_pressure_coefficient_values_object_name))
        return ",".join(out)

class AirflowNetworkMultiZoneWindPressureCoefficientArray(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:WindPressureCoefficientArray`
        Used only if Wind Pressure Coefficient (WPC) Type = Input in the AirflowNetwork:SimulationControl
        object. Number of WPC Values in the corresponding AirflowNetwork:MultiZone:WindPressureCoefficientValues
        object must be the same as the number of wind directions specified for
        this AirflowNetwork:MultiZone:WindPressureCoefficientArray object.
    """
    internal_name = "AirflowNetwork:MultiZone:WindPressureCoefficientArray"
    field_count = 37

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:WindPressureCoefficientArray`
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
            self.wind_direction_1 = None
        else:
            self.wind_direction_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_2 = None
        else:
            self.wind_direction_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_3 = None
        else:
            self.wind_direction_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_4 = None
        else:
            self.wind_direction_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_5 = None
        else:
            self.wind_direction_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_6 = None
        else:
            self.wind_direction_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_7 = None
        else:
            self.wind_direction_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_8 = None
        else:
            self.wind_direction_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_9 = None
        else:
            self.wind_direction_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_10 = None
        else:
            self.wind_direction_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_11 = None
        else:
            self.wind_direction_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_12 = None
        else:
            self.wind_direction_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_13 = None
        else:
            self.wind_direction_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_14 = None
        else:
            self.wind_direction_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_15 = None
        else:
            self.wind_direction_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_16 = None
        else:
            self.wind_direction_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_17 = None
        else:
            self.wind_direction_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_18 = None
        else:
            self.wind_direction_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_19 = None
        else:
            self.wind_direction_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_20 = None
        else:
            self.wind_direction_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_21 = None
        else:
            self.wind_direction_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_22 = None
        else:
            self.wind_direction_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_23 = None
        else:
            self.wind_direction_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_24 = None
        else:
            self.wind_direction_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_25 = None
        else:
            self.wind_direction_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_26 = None
        else:
            self.wind_direction_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_27 = None
        else:
            self.wind_direction_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_28 = None
        else:
            self.wind_direction_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_29 = None
        else:
            self.wind_direction_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_30 = None
        else:
            self.wind_direction_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_31 = None
        else:
            self.wind_direction_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_32 = None
        else:
            self.wind_direction_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_33 = None
        else:
            self.wind_direction_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_34 = None
        else:
            self.wind_direction_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_35 = None
        else:
            self.wind_direction_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_direction_36 = None
        else:
            self.wind_direction_36 = vals[i]
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
        Enter a unique name for the object.

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
    def wind_direction_1(self):
        """Get wind_direction_1

        Returns:
            float: the value of `wind_direction_1` or None if not set
        """
        return self._data["Wind Direction 1"]

    @wind_direction_1.setter
    def wind_direction_1(self, value=None):
        """  Corresponds to IDD Field `wind_direction_1`
        Enter the wind direction corresponding to the 1st WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_1`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_2`
        Enter the wind direction corresponding to the 2nd WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_2`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_3`
        Enter the wind direction corresponding to the 3rd WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_3`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_4`
        Enter the wind direction corresponding to the 4th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_4`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_5`
        Enter the wind direction corresponding to the 5th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_5`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_6`
        Enter the wind direction corresponding to the 6th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_6`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_7`
        Enter the wind direction corresponding to the 7th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_7`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_8`
        Enter the wind direction corresponding to the 8th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_8`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_9`
        Enter the wind direction corresponding to the 9th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_9`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_10`
        Enter the wind direction corresponding to the 10th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_10`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_11`
        Enter the wind direction corresponding to the 11th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_11`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_12`
        Enter the wind direction corresponding to the 12th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_12`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_13`
        Enter the wind direction corresponding to the 13th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_13`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_14`
        Enter the wind direction corresponding to the 14th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_14`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_15`
        Enter the wind direction corresponding to the 15th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_15`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_16`
        Enter the wind direction corresponding to the 16th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_16`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_17`
        Enter the wind direction corresponding to the 17th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_17`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_18`
        Enter the wind direction corresponding to the 18th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_18`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_19`
        Enter the wind direction corresponding to the 19th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_19`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_20`
        Enter the wind direction corresponding to the 20th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_20`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_21`
        Enter the wind direction corresponding to the 21st WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_21`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_22`
        Enter the wind direction corresponding to the 22nd WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_22`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_23`
        Enter the wind direction corresponding to the 23rd WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_23`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_24`
        Enter the wind direction corresponding to the 24th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_24`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_25`
        Enter the wind direction corresponding to the 25th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_25`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_26`
        Enter the wind direction corresponding to the 26th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_26`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_27`
        Enter the wind direction corresponding to the 27th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_27`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_28`
        Enter the wind direction corresponding to the 28th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_28`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_29`
        Enter the wind direction corresponding to the 29th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_29`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_30`
        Enter the wind direction corresponding to the 30th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_30`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_31`
        Enter the wind direction corresponding to the 31st WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_31`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_32`
        Enter the wind direction corresponding to the 32nd WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_32`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_33`
        Enter the wind direction corresponding to the 33rd WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_33`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_34`
        Enter the wind direction corresponding to the 34th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_34`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_35`
        Enter the wind direction corresponding to the 35th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_35`
                Unit: deg
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
            except:
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
        """  Corresponds to IDD Field `wind_direction_36`
        Enter the wind direction corresponding to the 36th WPC Array value.

        Args:
            value (float): value for IDD Field `wind_direction_36`
                Unit: deg
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wind_direction_36`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `wind_direction_36`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `wind_direction_36`')

        self._data["Wind Direction 36"] = value

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
        out.append(self._to_str(self.wind_direction_1))
        out.append(self._to_str(self.wind_direction_2))
        out.append(self._to_str(self.wind_direction_3))
        out.append(self._to_str(self.wind_direction_4))
        out.append(self._to_str(self.wind_direction_5))
        out.append(self._to_str(self.wind_direction_6))
        out.append(self._to_str(self.wind_direction_7))
        out.append(self._to_str(self.wind_direction_8))
        out.append(self._to_str(self.wind_direction_9))
        out.append(self._to_str(self.wind_direction_10))
        out.append(self._to_str(self.wind_direction_11))
        out.append(self._to_str(self.wind_direction_12))
        out.append(self._to_str(self.wind_direction_13))
        out.append(self._to_str(self.wind_direction_14))
        out.append(self._to_str(self.wind_direction_15))
        out.append(self._to_str(self.wind_direction_16))
        out.append(self._to_str(self.wind_direction_17))
        out.append(self._to_str(self.wind_direction_18))
        out.append(self._to_str(self.wind_direction_19))
        out.append(self._to_str(self.wind_direction_20))
        out.append(self._to_str(self.wind_direction_21))
        out.append(self._to_str(self.wind_direction_22))
        out.append(self._to_str(self.wind_direction_23))
        out.append(self._to_str(self.wind_direction_24))
        out.append(self._to_str(self.wind_direction_25))
        out.append(self._to_str(self.wind_direction_26))
        out.append(self._to_str(self.wind_direction_27))
        out.append(self._to_str(self.wind_direction_28))
        out.append(self._to_str(self.wind_direction_29))
        out.append(self._to_str(self.wind_direction_30))
        out.append(self._to_str(self.wind_direction_31))
        out.append(self._to_str(self.wind_direction_32))
        out.append(self._to_str(self.wind_direction_33))
        out.append(self._to_str(self.wind_direction_34))
        out.append(self._to_str(self.wind_direction_35))
        out.append(self._to_str(self.wind_direction_36))
        return ",".join(out)

class AirflowNetworkMultiZoneWindPressureCoefficientValues(object):
    """ Corresponds to IDD object `AirflowNetwork:MultiZone:WindPressureCoefficientValues`
        Used only if Wind Pressure Coefficient (WPC) Type = INPUT in the AirflowNetwork:SimulationControl
        object. The number of WPC numeric inputs must correspond to the number of wind direction
        inputs in the AirflowNetwork:Multizone:WindPressureCoefficientArray object.
    """
    internal_name = "AirflowNetwork:MultiZone:WindPressureCoefficientValues"
    field_count = 38

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:MultiZone:WindPressureCoefficientValues`
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
            self.airflownetworkmultizonewindpressurecoefficientarray_name = None
        else:
            self.airflownetworkmultizonewindpressurecoefficientarray_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_1 = None
        else:
            self.wind_pressure_coefficient_value_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_2 = None
        else:
            self.wind_pressure_coefficient_value_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_3 = None
        else:
            self.wind_pressure_coefficient_value_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_4 = None
        else:
            self.wind_pressure_coefficient_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_5 = None
        else:
            self.wind_pressure_coefficient_value_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_6 = None
        else:
            self.wind_pressure_coefficient_value_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_7 = None
        else:
            self.wind_pressure_coefficient_value_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_8 = None
        else:
            self.wind_pressure_coefficient_value_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_9 = None
        else:
            self.wind_pressure_coefficient_value_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_10 = None
        else:
            self.wind_pressure_coefficient_value_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_11 = None
        else:
            self.wind_pressure_coefficient_value_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_12 = None
        else:
            self.wind_pressure_coefficient_value_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_13 = None
        else:
            self.wind_pressure_coefficient_value_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_14 = None
        else:
            self.wind_pressure_coefficient_value_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_15 = None
        else:
            self.wind_pressure_coefficient_value_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_16 = None
        else:
            self.wind_pressure_coefficient_value_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_17 = None
        else:
            self.wind_pressure_coefficient_value_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_18 = None
        else:
            self.wind_pressure_coefficient_value_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_19 = None
        else:
            self.wind_pressure_coefficient_value_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_20 = None
        else:
            self.wind_pressure_coefficient_value_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_21 = None
        else:
            self.wind_pressure_coefficient_value_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_22 = None
        else:
            self.wind_pressure_coefficient_value_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_23 = None
        else:
            self.wind_pressure_coefficient_value_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_24 = None
        else:
            self.wind_pressure_coefficient_value_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_25 = None
        else:
            self.wind_pressure_coefficient_value_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_26 = None
        else:
            self.wind_pressure_coefficient_value_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_27 = None
        else:
            self.wind_pressure_coefficient_value_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_28 = None
        else:
            self.wind_pressure_coefficient_value_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_29 = None
        else:
            self.wind_pressure_coefficient_value_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_30 = None
        else:
            self.wind_pressure_coefficient_value_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_31 = None
        else:
            self.wind_pressure_coefficient_value_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_32 = None
        else:
            self.wind_pressure_coefficient_value_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_33 = None
        else:
            self.wind_pressure_coefficient_value_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_34 = None
        else:
            self.wind_pressure_coefficient_value_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_35 = None
        else:
            self.wind_pressure_coefficient_value_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_pressure_coefficient_value_36 = None
        else:
            self.wind_pressure_coefficient_value_36 = vals[i]
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
        Enter a unique name for this object.

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
    def airflownetworkmultizonewindpressurecoefficientarray_name(self):
        """Get airflownetworkmultizonewindpressurecoefficientarray_name

        Returns:
            str: the value of `airflownetworkmultizonewindpressurecoefficientarray_name` or None if not set
        """
        return self._data["AirflowNetwork:MultiZone:WindPressureCoefficientArray Name"]

    @airflownetworkmultizonewindpressurecoefficientarray_name.setter
    def airflownetworkmultizonewindpressurecoefficientarray_name(self, value=None):
        """  Corresponds to IDD Field `airflownetworkmultizonewindpressurecoefficientarray_name`
        Enter the name of the AirflowNetwork:Multizone:WindPressureCoefficientArray object.

        Args:
            value (str): value for IDD Field `airflownetworkmultizonewindpressurecoefficientarray_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airflownetworkmultizonewindpressurecoefficientarray_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_1`
        Enter the WPC Value corresponding to the 1st wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_1`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_2`
        Enter the WPC Value corresponding to the 2nd wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_2`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_3`
        Enter the WPC Value corresponding to the 3rd wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_3`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_4`
        Enter the WPC Value corresponding to the 4th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_4`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_5`
        Enter the WPC Value corresponding to the 5th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_5`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_6`
        Enter the WPC Value corresponding to the 6th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_6`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_7`
        Enter the WPC Value corresponding to the 7th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_7`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_8`
        Enter the WPC Value corresponding to the 8th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_8`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_9`
        Enter the WPC Value corresponding to the 9th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_9`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_10`
        Enter the WPC Value corresponding to the 10th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_10`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_11`
        Enter the WPC Value corresponding to the 11th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_11`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_12`
        Enter the WPC Value corresponding to the 12th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_12`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_13`
        Enter the WPC Value corresponding to the 13th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_13`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_14`
        Enter the WPC Value corresponding to the 14th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_14`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_15`
        Enter the WPC Value corresponding to the 15th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_15`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_16`
        Enter the WPC Value corresponding to the 16th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_16`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_17`
        Enter the WPC Value corresponding to the 17th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_17`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_18`
        Enter the WPC Value corresponding to the 18th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_18`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_19`
        Enter the WPC Value corresponding to the 19th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_19`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_20`
        Enter the WPC Value corresponding to the 20th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_20`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_21`
        Enter the WPC Value corresponding to the 21st wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_21`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_22`
        Enter the WPC Value corresponding to the 22nd wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_22`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_23`
        Enter the WPC Value corresponding to the 23rd wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_23`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_24`
        Enter the WPC Value corresponding to the 24th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_24`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_25`
        Enter the WPC Value corresponding to the 25th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_25`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_26`
        Enter the WPC Value corresponding to the 26th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_26`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_27`
        Enter the WPC Value corresponding to the 27th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_27`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_28`
        Enter the WPC Value corresponding to the 28th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_28`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_29`
        Enter the WPC Value corresponding to the 29th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_29`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_30`
        Enter the WPC Value corresponding to the 30th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_30`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_31`
        Enter the WPC Value corresponding to the 31st wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_31`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_32`
        Enter the WPC Value corresponding to the 32nd wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_32`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_33`
        Enter the WPC Value corresponding to the 33rd wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_33`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_34`
        Enter the WPC Value corresponding to the 34th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_34`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_35`
        Enter the WPC Value corresponding to the 35th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_35`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
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
        """  Corresponds to IDD Field `wind_pressure_coefficient_value_36`
        Enter the WPC Value corresponding to the 36th wind direction.

        Args:
            value (float): value for IDD Field `wind_pressure_coefficient_value_36`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wind_pressure_coefficient_value_36`'.format(value))

        self._data["Wind Pressure Coefficient Value 36"] = value

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
        out.append(self._to_str(self.airflownetworkmultizonewindpressurecoefficientarray_name))
        out.append(self._to_str(self.wind_pressure_coefficient_value_1))
        out.append(self._to_str(self.wind_pressure_coefficient_value_2))
        out.append(self._to_str(self.wind_pressure_coefficient_value_3))
        out.append(self._to_str(self.wind_pressure_coefficient_value_4))
        out.append(self._to_str(self.wind_pressure_coefficient_value_5))
        out.append(self._to_str(self.wind_pressure_coefficient_value_6))
        out.append(self._to_str(self.wind_pressure_coefficient_value_7))
        out.append(self._to_str(self.wind_pressure_coefficient_value_8))
        out.append(self._to_str(self.wind_pressure_coefficient_value_9))
        out.append(self._to_str(self.wind_pressure_coefficient_value_10))
        out.append(self._to_str(self.wind_pressure_coefficient_value_11))
        out.append(self._to_str(self.wind_pressure_coefficient_value_12))
        out.append(self._to_str(self.wind_pressure_coefficient_value_13))
        out.append(self._to_str(self.wind_pressure_coefficient_value_14))
        out.append(self._to_str(self.wind_pressure_coefficient_value_15))
        out.append(self._to_str(self.wind_pressure_coefficient_value_16))
        out.append(self._to_str(self.wind_pressure_coefficient_value_17))
        out.append(self._to_str(self.wind_pressure_coefficient_value_18))
        out.append(self._to_str(self.wind_pressure_coefficient_value_19))
        out.append(self._to_str(self.wind_pressure_coefficient_value_20))
        out.append(self._to_str(self.wind_pressure_coefficient_value_21))
        out.append(self._to_str(self.wind_pressure_coefficient_value_22))
        out.append(self._to_str(self.wind_pressure_coefficient_value_23))
        out.append(self._to_str(self.wind_pressure_coefficient_value_24))
        out.append(self._to_str(self.wind_pressure_coefficient_value_25))
        out.append(self._to_str(self.wind_pressure_coefficient_value_26))
        out.append(self._to_str(self.wind_pressure_coefficient_value_27))
        out.append(self._to_str(self.wind_pressure_coefficient_value_28))
        out.append(self._to_str(self.wind_pressure_coefficient_value_29))
        out.append(self._to_str(self.wind_pressure_coefficient_value_30))
        out.append(self._to_str(self.wind_pressure_coefficient_value_31))
        out.append(self._to_str(self.wind_pressure_coefficient_value_32))
        out.append(self._to_str(self.wind_pressure_coefficient_value_33))
        out.append(self._to_str(self.wind_pressure_coefficient_value_34))
        out.append(self._to_str(self.wind_pressure_coefficient_value_35))
        out.append(self._to_str(self.wind_pressure_coefficient_value_36))
        return ",".join(out)

class AirflowNetworkDistributionNode(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Node`
        This object represents an air distribution node in the AirflowNetwork model.
    """
    internal_name = "AirflowNetwork:Distribution:Node"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:Distribution:Node`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Component Name or Node Name"] = None
        self._data["Component Object Type or Node Type"] = None
        self._data["Node Height"] = None

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
            self.component_name_or_node_name = None
        else:
            self.component_name_or_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_object_type_or_node_type = None
        else:
            self.component_object_type_or_node_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_height = None
        else:
            self.node_height = vals[i]
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
        Enter a unique name for this object.

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
    def component_name_or_node_name(self):
        """Get component_name_or_node_name

        Returns:
            str: the value of `component_name_or_node_name` or None if not set
        """
        return self._data["Component Name or Node Name"]

    @component_name_or_node_name.setter
    def component_name_or_node_name(self, value=None):
        """  Corresponds to IDD Field `component_name_or_node_name`
        Designates node names defined in another object. The node name may occur in air branches.
        Enter a node name to represent a node already defined in an air loop.
        Leave this field blank if the Node or Object Type field below is entered as
        AirLoopHVAC:ZoneMixer, AirLoopHVAC:ZoneSplitter, AirLoopHVAC:OutdoorAirSystem, or Other.

        Args:
            value (str): value for IDD Field `component_name_or_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_name_or_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `component_object_type_or_node_type`
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

        Args:
            value (str): value for IDD Field `component_object_type_or_node_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_object_type_or_node_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `component_object_type_or_node_type`')
            vals = set()
            vals.add("AirLoopHVAC:ZoneMixer")
            vals.add("AirLoopHVAC:ZoneSplitter")
            vals.add("AirLoopHVAC:OutdoorAirSystem")
            vals.add("OAMixerOutdoorAirStreamNode")
            vals.add("OutdoorAir:NodeList")
            vals.add("OutdoorAir:Node")
            vals.add("Other")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `component_object_type_or_node_type`'.format(value))

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
        """  Corresponds to IDD Field `node_height`
        Enter the reference height used to calculate the relative pressure.

        Args:
            value (float): value for IDD Field `node_height`
                Unit: m
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
                                 'for field `node_height`'.format(value))

        self._data["Node Height"] = value

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
        out.append(self._to_str(self.component_name_or_node_name))
        out.append(self._to_str(self.component_object_type_or_node_type))
        out.append(self._to_str(self.node_height))
        return ",".join(out)

class AirflowNetworkDistributionComponentLeak(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Leak`
        This object defines the characteristics of a supply or return air leak.
    """
    internal_name = "AirflowNetwork:Distribution:Component:Leak"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:Distribution:Component:Leak`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Mass Flow Coefficient"] = None
        self._data["Air Mass Flow Exponent"] = None

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
            self.air_mass_flow_coefficient = None
        else:
            self.air_mass_flow_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent = None
        else:
            self.air_mass_flow_exponent = vals[i]
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
        Enter a unique name for this object.

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
    def air_mass_flow_coefficient(self):
        """Get air_mass_flow_coefficient

        Returns:
            float: the value of `air_mass_flow_coefficient` or None if not set
        """
        return self._data["Air Mass Flow Coefficient"]

    @air_mass_flow_coefficient.setter
    def air_mass_flow_coefficient(self, value=None):
        """  Corresponds to IDD Field `air_mass_flow_coefficient`
        Defined at 1 Pa pressure difference across this component.
        Enter the coefficient used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent

        Args:
            value (float): value for IDD Field `air_mass_flow_coefficient`
                Unit: kg/s
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
        """  Corresponds to IDD Field `air_mass_flow_exponent`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent

        Args:
            value (float): value for IDD Field `air_mass_flow_exponent`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `air_mass_flow_exponent`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent`')

        self._data["Air Mass Flow Exponent"] = value

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
        out.append(self._to_str(self.air_mass_flow_coefficient))
        out.append(self._to_str(self.air_mass_flow_exponent))
        return ",".join(out)

class AirflowNetworkDistributionComponentLeakageRatio(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:LeakageRatio`
        This object is used to define supply and return air leaks with respect to the fan's maximum
        air flow rate.
    """
    internal_name = "AirflowNetwork:Distribution:Component:LeakageRatio"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:Distribution:Component:LeakageRatio`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Effective Leakage Ratio"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Reference Pressure Difference"] = None
        self._data["Air Mass Flow Exponent"] = None

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
            self.effective_leakage_ratio = None
        else:
            self.effective_leakage_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_pressure_difference = None
        else:
            self.reference_pressure_difference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_mass_flow_exponent = None
        else:
            self.air_mass_flow_exponent = vals[i]
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
        Enter a unique name for this object.

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
    def effective_leakage_ratio(self):
        """Get effective_leakage_ratio

        Returns:
            float: the value of `effective_leakage_ratio` or None if not set
        """
        return self._data["Effective Leakage Ratio"]

    @effective_leakage_ratio.setter
    def effective_leakage_ratio(self, value=None):
        """  Corresponds to IDD Field `effective_leakage_ratio`
        Defined as a ratio of leak flow rate to the maximum flow rate.

        Args:
            value (float): value for IDD Field `effective_leakage_ratio`
                Unit: dimensionless
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
        """  Corresponds to IDD Field `maximum_flow_rate`
        Enter the maximum air flow rate in this air loop.

        Args:
            value (float): value for IDD Field `maximum_flow_rate`
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
        """  Corresponds to IDD Field `reference_pressure_difference`
        Enter the pressure corresponding to the Effective leakage ratio entered above.

        Args:
            value (float): value for IDD Field `reference_pressure_difference`
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
        """  Corresponds to IDD Field `air_mass_flow_exponent`
        Enter the exponent used in the air mass flow equation.

        Args:
            value (float): value for IDD Field `air_mass_flow_exponent`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `air_mass_flow_exponent`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `air_mass_flow_exponent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `air_mass_flow_exponent`')

        self._data["Air Mass Flow Exponent"] = value

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
        out.append(self._to_str(self.effective_leakage_ratio))
        out.append(self._to_str(self.maximum_flow_rate))
        out.append(self._to_str(self.reference_pressure_difference))
        out.append(self._to_str(self.air_mass_flow_exponent))
        return ",".join(out)

class AirflowNetworkDistributionComponentDuct(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Duct`
        This object defines the relationship between pressure and air flow through the duct.
    """
    internal_name = "AirflowNetwork:Distribution:Component:Duct"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:Distribution:Component:Duct`
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
            self.duct_length = None
        else:
            self.duct_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hydraulic_diameter = None
        else:
            self.hydraulic_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_section_area = None
        else:
            self.cross_section_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_roughness = None
        else:
            self.surface_roughness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_for_local_dynamic_loss_due_to_fitting = None
        else:
            self.coefficient_for_local_dynamic_loss_due_to_fitting = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.overall_heat_transmittance_coefficient_ufactor_from_air_to_air = None
        else:
            self.overall_heat_transmittance_coefficient_ufactor_from_air_to_air = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.overall_moisture_transmittance_coefficient_from_air_to_air = None
        else:
            self.overall_moisture_transmittance_coefficient_from_air_to_air = vals[i]
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
        Enter a unique name for this object.

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
    def duct_length(self):
        """Get duct_length

        Returns:
            float: the value of `duct_length` or None if not set
        """
        return self._data["Duct Length"]

    @duct_length.setter
    def duct_length(self, value=None):
        """  Corresponds to IDD Field `duct_length`
        Enter the length of the duct.

        Args:
            value (float): value for IDD Field `duct_length`
                Unit: m
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
        """  Corresponds to IDD Field `hydraulic_diameter`
        Enter the hydraulic diameter of the duct.
        Hydraulic diameter is defined as 4 multiplied by cross section area divided by perimeter

        Args:
            value (float): value for IDD Field `hydraulic_diameter`
                Unit: m
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
        """  Corresponds to IDD Field `cross_section_area`
        Enter the cross section area of the duct.

        Args:
            value (float): value for IDD Field `cross_section_area`
                Unit: m2
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
        """  Corresponds to IDD Field `surface_roughness`
        Enter the inside surface roughness of the duct.

        Args:
            value (float): value for IDD Field `surface_roughness`
                Unit: m
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
            except:
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
        """  Corresponds to IDD Field `coefficient_for_local_dynamic_loss_due_to_fitting`
        Enter the coefficient used to calculate dynamic losses of fittings (e.g. elbows).

        Args:
            value (float): value for IDD Field `coefficient_for_local_dynamic_loss_due_to_fitting`
                Unit: dimensionless
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
        """  Corresponds to IDD Field `overall_heat_transmittance_coefficient_ufactor_from_air_to_air`
        including film coefficients at both surfaces
        Enter the overall U-value for this duct.
        Default value of 0.772 is equivalent to 1.06 m2-K/W (R6) duct insulation with
        film coefficients for outside and inside equal to 5 and 25 W/m2-K, respectively.

        Args:
            value (float): value for IDD Field `overall_heat_transmittance_coefficient_ufactor_from_air_to_air`
                Unit: W/m2-K
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
            except:
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
        """  Corresponds to IDD Field `overall_moisture_transmittance_coefficient_from_air_to_air`
        Enter the overall moisture transmittance coefficient
        including moisture film coefficients at both surfaces.

        Args:
            value (float): value for IDD Field `overall_moisture_transmittance_coefficient_from_air_to_air`
                Unit: kg/m2
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `overall_moisture_transmittance_coefficient_from_air_to_air`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `overall_moisture_transmittance_coefficient_from_air_to_air`')

        self._data["Overall Moisture Transmittance Coefficient from Air to Air"] = value

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
        out.append(self._to_str(self.duct_length))
        out.append(self._to_str(self.hydraulic_diameter))
        out.append(self._to_str(self.cross_section_area))
        out.append(self._to_str(self.surface_roughness))
        out.append(self._to_str(self.coefficient_for_local_dynamic_loss_due_to_fitting))
        out.append(self._to_str(self.overall_heat_transmittance_coefficient_ufactor_from_air_to_air))
        out.append(self._to_str(self.overall_moisture_transmittance_coefficient_from_air_to_air))
        return ",".join(out)

class AirflowNetworkDistributionComponentFan(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Fan`
        This object defines the name of the constant volume supply Air Fan used in an Air loop.
    """
    internal_name = "AirflowNetwork:Distribution:Component:Fan"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:Distribution:Component:Fan`
        """
        self._data = OrderedDict()
        self._data["Fan Name"] = None
        self._data["Supply Fan Object Type"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.fan_name = None
        else:
            self.fan_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_fan_object_type = None
        else:
            self.supply_fan_object_type = vals[i]
        i += 1

    @property
    def fan_name(self):
        """Get fan_name

        Returns:
            str: the value of `fan_name` or None if not set
        """
        return self._data["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """  Corresponds to IDD Field `fan_name`
        Enter the name of the constant volume fan in the primary air loop.

        Args:
            value (str): value for IDD Field `fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `supply_fan_object_type`

        Args:
            value (str): value for IDD Field `supply_fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_fan_object_type`')
            vals = set()
            vals.add("Fan:OnOff")
            vals.add("Fan:ConstantVolume")
            vals.add("Fan:VariableVolume")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_fan_object_type`'.format(value))

        self._data["Supply Fan Object Type"] = value

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
        out.append(self._to_str(self.fan_name))
        out.append(self._to_str(self.supply_fan_object_type))
        return ",".join(out)

class AirflowNetworkDistributionComponentCoil(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Coil`
        This object defines the name of a coil used in an air loop.
    """
    internal_name = "AirflowNetwork:Distribution:Component:Coil"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:Distribution:Component:Coil`
        """
        self._data = OrderedDict()
        self._data["Coil Name"] = None
        self._data["Coil Object Type"] = None
        self._data["Air Path Length"] = None
        self._data["Air Path Hydraulic Diameter"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.coil_name = None
        else:
            self.coil_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coil_object_type = None
        else:
            self.coil_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_path_length = None
        else:
            self.air_path_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_path_hydraulic_diameter = None
        else:
            self.air_path_hydraulic_diameter = vals[i]
        i += 1

    @property
    def coil_name(self):
        """Get coil_name

        Returns:
            str: the value of `coil_name` or None if not set
        """
        return self._data["Coil Name"]

    @coil_name.setter
    def coil_name(self, value=None):
        """  Corresponds to IDD Field `coil_name`
        Enter the name of a cooling or heating coil in the primary Air loop.

        Args:
            value (str): value for IDD Field `coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `coil_object_type`
        Select the type of coil corresponding to the name entered in the field above.

        Args:
            value (str): value for IDD Field `coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `coil_object_type`')
            vals = set()
            vals.add("Coil:Cooling:DX:SingleSpeed")
            vals.add("Coil:Heating:Gas")
            vals.add("Coil:Heating:Electric")
            vals.add("Coil:Heating:DX:SingleSpeed")
            vals.add("Coil:Cooling:Water")
            vals.add("Coil:Heating:Water")
            vals.add("Coil:Cooling:Water:DetailedGeometry")
            vals.add("Coil:Cooling:DX:TwoStageWithHumidityControlMode")
            vals.add("Coil:Cooling:DX:MultiSpeed")
            vals.add("Coil:Heating:DX:MultiSpeed")
            vals.add("Coil:Heating:Desuperheater")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `coil_object_type`'.format(value))

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
        """  Corresponds to IDD Field `air_path_length`
        Enter the air path length (depth) for the coil.

        Args:
            value (float): value for IDD Field `air_path_length`
                Unit: m
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
        """  Corresponds to IDD Field `air_path_hydraulic_diameter`
        Enter the hydraulic diameter of this coil. The hydraulic diameter is
        defined as 4 multiplied by the cross section area divided by perimeter.

        Args:
            value (float): value for IDD Field `air_path_hydraulic_diameter`
                Unit: m
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
                                 'for field `air_path_hydraulic_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_path_hydraulic_diameter`')

        self._data["Air Path Hydraulic Diameter"] = value

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
        out.append(self._to_str(self.coil_name))
        out.append(self._to_str(self.coil_object_type))
        out.append(self._to_str(self.air_path_length))
        out.append(self._to_str(self.air_path_hydraulic_diameter))
        return ",".join(out)

class AirflowNetworkDistributionComponentHeatExchanger(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:HeatExchanger`
        This object defines the name of an air-to-air heat exchanger used in an air loop.
    """
    internal_name = "AirflowNetwork:Distribution:Component:HeatExchanger"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:Distribution:Component:HeatExchanger`
        """
        self._data = OrderedDict()
        self._data["HeatExchanger Name"] = None
        self._data["HeatExchanger Object Type"] = None
        self._data["Air Path Length"] = None
        self._data["Air Path Hydraulic Diameter"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.heatexchanger_name = None
        else:
            self.heatexchanger_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heatexchanger_object_type = None
        else:
            self.heatexchanger_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_path_length = None
        else:
            self.air_path_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_path_hydraulic_diameter = None
        else:
            self.air_path_hydraulic_diameter = vals[i]
        i += 1

    @property
    def heatexchanger_name(self):
        """Get heatexchanger_name

        Returns:
            str: the value of `heatexchanger_name` or None if not set
        """
        return self._data["HeatExchanger Name"]

    @heatexchanger_name.setter
    def heatexchanger_name(self, value=None):
        """  Corresponds to IDD Field `heatexchanger_name`
        Enter the name of an air-to-air heat exchanger in the primary Air loop.

        Args:
            value (str): value for IDD Field `heatexchanger_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heatexchanger_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `heatexchanger_object_type`
        Select the type of heat exchanger corresponding to the name entered in the field above.

        Args:
            value (str): value for IDD Field `heatexchanger_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heatexchanger_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heatexchanger_object_type`')
            vals = set()
            vals.add("HeatExchanger:AirToAir:FlatPlate")
            vals.add("HeatExchanger:AirToAir:SensibleAndLatent")
            vals.add("HeatExchanger:Desiccant:BalancedFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heatexchanger_object_type`'.format(value))

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
        """  Corresponds to IDD Field `air_path_length`
        Enter the air path length (depth) for the heat exchanger.

        Args:
            value (float): value for IDD Field `air_path_length`
                Unit: m
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
        """  Corresponds to IDD Field `air_path_hydraulic_diameter`
        Enter the hydraulic diameter of this heat exchanger. The hydraulic diameter is
        defined as 4 multiplied by the cross section area divided by perimeter.

        Args:
            value (float): value for IDD Field `air_path_hydraulic_diameter`
                Unit: m
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
                                 'for field `air_path_hydraulic_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_path_hydraulic_diameter`')

        self._data["Air Path Hydraulic Diameter"] = value

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
        out.append(self._to_str(self.heatexchanger_name))
        out.append(self._to_str(self.heatexchanger_object_type))
        out.append(self._to_str(self.air_path_length))
        out.append(self._to_str(self.air_path_hydraulic_diameter))
        return ",".join(out)

class AirflowNetworkDistributionComponentTerminalUnit(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:TerminalUnit`
        This object defines the name of a terminal unit in an air loop.
    """
    internal_name = "AirflowNetwork:Distribution:Component:TerminalUnit"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:Distribution:Component:TerminalUnit`
        """
        self._data = OrderedDict()
        self._data["Terminal Unit Name"] = None
        self._data["Terminal Unit Object Type"] = None
        self._data["Air Path Length"] = None
        self._data["Air Path Hydraulic Diameter"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.terminal_unit_name = None
        else:
            self.terminal_unit_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.terminal_unit_object_type = None
        else:
            self.terminal_unit_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_path_length = None
        else:
            self.air_path_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_path_hydraulic_diameter = None
        else:
            self.air_path_hydraulic_diameter = vals[i]
        i += 1

    @property
    def terminal_unit_name(self):
        """Get terminal_unit_name

        Returns:
            str: the value of `terminal_unit_name` or None if not set
        """
        return self._data["Terminal Unit Name"]

    @terminal_unit_name.setter
    def terminal_unit_name(self, value=None):
        """  Corresponds to IDD Field `terminal_unit_name`
        Enter the name of a terminal unit in the AirLoopHVAC.

        Args:
            value (str): value for IDD Field `terminal_unit_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `terminal_unit_object_type`
        Select the type of terminal unit corresponding to the name entered in the field above.

        Args:
            value (str): value for IDD Field `terminal_unit_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_object_type`')
            vals = set()
            vals.add("AirTerminal:SingleDuct:ConstantVolume:Reheat")
            vals.add("AirTerminal:SingleDuct:VAV:Reheat")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `terminal_unit_object_type`'.format(value))

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
        """  Corresponds to IDD Field `air_path_length`
        Enter the air path length (depth) for the terminal unit.

        Args:
            value (float): value for IDD Field `air_path_length`
                Unit: m
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
        """  Corresponds to IDD Field `air_path_hydraulic_diameter`
        Enter the hydraulic diameter of this terminal unit. The hydraulic diameter is
        defined as 4 multiplied by the cross section area divided by perimeter.

        Args:
            value (float): value for IDD Field `air_path_hydraulic_diameter`
                Unit: m
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
                                 'for field `air_path_hydraulic_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `air_path_hydraulic_diameter`')

        self._data["Air Path Hydraulic Diameter"] = value

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
        out.append(self._to_str(self.terminal_unit_name))
        out.append(self._to_str(self.terminal_unit_object_type))
        out.append(self._to_str(self.air_path_length))
        out.append(self._to_str(self.air_path_hydraulic_diameter))
        return ",".join(out)

class AirflowNetworkDistributionComponentConstantPressureDrop(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:ConstantPressureDrop`
        This object defines the characteristics of a constant pressure drop component (e.g. filter).
        Each node connected to this object can not be a node of mixer, splitter, a node of air primary
        loop, or zone equipment loop. It is recommended to connect to a duct component at both ends.
    """
    internal_name = "AirflowNetwork:Distribution:Component:ConstantPressureDrop"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:Distribution:Component:ConstantPressureDrop`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Pressure Difference Across the Component"] = None

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
            self.pressure_difference_across_the_component = None
        else:
            self.pressure_difference_across_the_component = vals[i]
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
        Enter a unique name for this object.

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
    def pressure_difference_across_the_component(self):
        """Get pressure_difference_across_the_component

        Returns:
            float: the value of `pressure_difference_across_the_component` or None if not set
        """
        return self._data["Pressure Difference Across the Component"]

    @pressure_difference_across_the_component.setter
    def pressure_difference_across_the_component(self, value=None):
        """  Corresponds to IDD Field `pressure_difference_across_the_component`
        Enter the pressure drop across this component.

        Args:
            value (float): value for IDD Field `pressure_difference_across_the_component`
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
                                 'for field `pressure_difference_across_the_component`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pressure_difference_across_the_component`')

        self._data["Pressure Difference Across the Component"] = value

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
        out.append(self._to_str(self.pressure_difference_across_the_component))
        return ",".join(out)

class AirflowNetworkDistributionLinkage(object):
    """ Corresponds to IDD object `AirflowNetwork:Distribution:Linkage`
        This object defines the connection between two nodes and a component.
    """
    internal_name = "AirflowNetwork:Distribution:Linkage"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `AirflowNetwork:Distribution:Linkage`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Node 1 Name"] = None
        self._data["Node 2 Name"] = None
        self._data["Component Name"] = None
        self._data["Thermal Zone Name"] = None

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
            self.node_1_name = None
        else:
            self.node_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_2_name = None
        else:
            self.node_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_name = None
        else:
            self.component_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_zone_name = None
        else:
            self.thermal_zone_name = vals[i]
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
        Enter a unique name for this object.

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
    def node_1_name(self):
        """Get node_1_name

        Returns:
            str: the value of `node_1_name` or None if not set
        """
        return self._data["Node 1 Name"]

    @node_1_name.setter
    def node_1_name(self, value=None):
        """  Corresponds to IDD Field `node_1_name`
        Enter the name of zone or AirflowNetwork Node.

        Args:
            value (str): value for IDD Field `node_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `node_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `node_2_name`
        Enter the name of zone or AirflowNetwork Node.

        Args:
            value (str): value for IDD Field `node_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `node_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `component_name`
        Enter the name of an AirflowNetwork component. A component is one of the
        following AirflowNetwork:Distribution:Component objects: Leak, LeakageRatio,
        Duct, ConstantVolumeFan, Coil, TerminalUnit, ConstantPressureDrop, or HeatExchanger.

        Args:
            value (str): value for IDD Field `component_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `component_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `thermal_zone_name`
        Only used if component = AirflowNetwork:Distribution:Component:Duct
        The zone name is where AirflowNetwork:Distribution:Component:Duct is exposed. Leave this field blank if the duct
        conduction loss is ignored.

        Args:
            value (str): value for IDD Field `thermal_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_zone_name`')

        self._data["Thermal Zone Name"] = value

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
        out.append(self._to_str(self.node_1_name))
        out.append(self._to_str(self.node_2_name))
        out.append(self._to_str(self.component_name))
        out.append(self._to_str(self.thermal_zone_name))
        return ",".join(out)