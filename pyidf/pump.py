from collections import OrderedDict

class PumpVariableSpeed(object):
    """ Corresponds to IDD object `Pump:VariableSpeed`
        This pump model is described in the ASHRAE secondary HVAC toolkit.
    """
    internal_name = "Pump:VariableSpeed"
    field_count = 25

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Pump:VariableSpeed`
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_flow_rate = None
        else:
            self.rated_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_pump_head = None
        else:
            self.rated_pump_head = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_power_consumption = None
        else:
            self.rated_power_consumption = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = None
        else:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_the_part_load_performance_curve = None
        else:
            self.coefficient_1_of_the_part_load_performance_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_the_part_load_performance_curve = None
        else:
            self.coefficient_2_of_the_part_load_performance_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_the_part_load_performance_curve = None
        else:
            self.coefficient_3_of_the_part_load_performance_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_4_of_the_part_load_performance_curve = None
        else:
            self.coefficient_4_of_the_part_load_performance_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_flow_rate = None
        else:
            self.minimum_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_control_type = None
        else:
            self.pump_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_flow_rate_schedule_name = None
        else:
            self.pump_flow_rate_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_curve_name = None
        else:
            self.pump_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.impeller_diameter = None
        else:
            self.impeller_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vfd_control_type = None
        else:
            self.vfd_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_rpm_schedule_name = None
        else:
            self.pump_rpm_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_pressure_schedule = None
        else:
            self.minimum_pressure_schedule = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_pressure_schedule = None
        else:
            self.maximum_pressure_schedule = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_rpm_schedule = None
        else:
            self.minimum_rpm_schedule = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_rpm_schedule = None
        else:
            self.maximum_rpm_schedule = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.skin_loss_radiative_fraction = None
        else:
            self.skin_loss_radiative_fraction = vals[i]
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
                Unit: Pa
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
            vals = set()
            vals.add("Continuous")
            vals.add("Intermittent")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `pump_control_type`'.format(value))

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
                Unit: m
                if `value` is None it will not be checked against the
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
            vals = set()
            vals.add("ManualControl")
            vals.add("PressureSetpointControl")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `vfd_control_type`'.format(value))

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
                Unit: Pa
                if `value` is None it will not be checked against the
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
                Unit: Pa
                if `value` is None it will not be checked against the
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
                Unit: Rotations Per Minute
                if `value` is None it will not be checked against the
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
                Unit: Rotations Per Minute
                if `value` is None it will not be checked against the
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
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        out.append(self._to_str(self.rated_flow_rate))
        out.append(self._to_str(self.rated_pump_head))
        out.append(self._to_str(self.rated_power_consumption))
        out.append(self._to_str(self.motor_efficiency))
        out.append(self._to_str(self.fraction_of_motor_inefficiencies_to_fluid_stream))
        out.append(self._to_str(self.coefficient_1_of_the_part_load_performance_curve))
        out.append(self._to_str(self.coefficient_2_of_the_part_load_performance_curve))
        out.append(self._to_str(self.coefficient_3_of_the_part_load_performance_curve))
        out.append(self._to_str(self.coefficient_4_of_the_part_load_performance_curve))
        out.append(self._to_str(self.minimum_flow_rate))
        out.append(self._to_str(self.pump_control_type))
        out.append(self._to_str(self.pump_flow_rate_schedule_name))
        out.append(self._to_str(self.pump_curve_name))
        out.append(self._to_str(self.impeller_diameter))
        out.append(self._to_str(self.vfd_control_type))
        out.append(self._to_str(self.pump_rpm_schedule_name))
        out.append(self._to_str(self.minimum_pressure_schedule))
        out.append(self._to_str(self.maximum_pressure_schedule))
        out.append(self._to_str(self.minimum_rpm_schedule))
        out.append(self._to_str(self.maximum_rpm_schedule))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.skin_loss_radiative_fraction))
        return ",".join(out)

class PumpConstantSpeed(object):
    """ Corresponds to IDD object `Pump:ConstantSpeed`
        This pump model is described in the ASHRAE secondary HVAC toolkit.
    """
    internal_name = "Pump:ConstantSpeed"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Pump:ConstantSpeed`
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_flow_rate = None
        else:
            self.rated_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_pump_head = None
        else:
            self.rated_pump_head = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_power_consumption = None
        else:
            self.rated_power_consumption = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = None
        else:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_control_type = None
        else:
            self.pump_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_flow_rate_schedule_name = None
        else:
            self.pump_flow_rate_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_curve_name = None
        else:
            self.pump_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.impeller_diameter = None
        else:
            self.impeller_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rotational_speed = None
        else:
            self.rotational_speed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.skin_loss_radiative_fraction = None
        else:
            self.skin_loss_radiative_fraction = vals[i]
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
                Unit: Pa
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
            vals = set()
            vals.add("Continuous")
            vals.add("Intermittent")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `pump_control_type`'.format(value))

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
                Unit: m
                if `value` is None it will not be checked against the
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
                Unit: rev/min
                if `value` is None it will not be checked against the
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
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        out.append(self._to_str(self.rated_flow_rate))
        out.append(self._to_str(self.rated_pump_head))
        out.append(self._to_str(self.rated_power_consumption))
        out.append(self._to_str(self.motor_efficiency))
        out.append(self._to_str(self.fraction_of_motor_inefficiencies_to_fluid_stream))
        out.append(self._to_str(self.pump_control_type))
        out.append(self._to_str(self.pump_flow_rate_schedule_name))
        out.append(self._to_str(self.pump_curve_name))
        out.append(self._to_str(self.impeller_diameter))
        out.append(self._to_str(self.rotational_speed))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.skin_loss_radiative_fraction))
        return ",".join(out)

class PumpVariableSpeedCondensate(object):
    """ Corresponds to IDD object `Pump:VariableSpeed:Condensate`
        This pump model is described in the ASHRAE secondary HVAC toolkit.
        Variable Speed Condensate pump for Steam Systems
    """
    internal_name = "Pump:VariableSpeed:Condensate"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Pump:VariableSpeed:Condensate`
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_flow_rate = None
        else:
            self.rated_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_pump_head = None
        else:
            self.rated_pump_head = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_power_consumption = None
        else:
            self.rated_power_consumption = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = None
        else:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_the_part_load_performance_curve = None
        else:
            self.coefficient_1_of_the_part_load_performance_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_the_part_load_performance_curve = None
        else:
            self.coefficient_2_of_the_part_load_performance_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_the_part_load_performance_curve = None
        else:
            self.coefficient_3_of_the_part_load_performance_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_4_of_the_part_load_performance_curve = None
        else:
            self.coefficient_4_of_the_part_load_performance_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_flow_rate_schedule_name = None
        else:
            self.pump_flow_rate_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.skin_loss_radiative_fraction = None
        else:
            self.skin_loss_radiative_fraction = vals[i]
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
                Unit: Pa
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
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        out.append(self._to_str(self.rated_flow_rate))
        out.append(self._to_str(self.rated_pump_head))
        out.append(self._to_str(self.rated_power_consumption))
        out.append(self._to_str(self.motor_efficiency))
        out.append(self._to_str(self.fraction_of_motor_inefficiencies_to_fluid_stream))
        out.append(self._to_str(self.coefficient_1_of_the_part_load_performance_curve))
        out.append(self._to_str(self.coefficient_2_of_the_part_load_performance_curve))
        out.append(self._to_str(self.coefficient_3_of_the_part_load_performance_curve))
        out.append(self._to_str(self.coefficient_4_of_the_part_load_performance_curve))
        out.append(self._to_str(self.pump_flow_rate_schedule_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.skin_loss_radiative_fraction))
        return ",".join(out)