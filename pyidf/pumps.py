from collections import OrderedDict

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
        """  Corresponds to IDD Field `Name`

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
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
        """  Corresponds to IDD Field `Rated Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Flow Rate`
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
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Rated Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
    def rated_pump_head(self, value=179352.0):
        """  Corresponds to IDD Field `Rated Pump Head`
        default head is 60 feet

        Args:
            value (float): value for IDD Field `Rated Pump Head`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Rated Power Consumption`
        If this field is autosized, an impeller efficiency of 0.78 is assumed.
        autosized Rated Power Consumption = Rated Flow Rate * Rated Pump Head / (0.78 * Motor Efficiency)

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Power Consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Rated Power Consumption"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
    def motor_efficiency(self, value=0.9):
        """  Corresponds to IDD Field `Motor Efficiency`
        This is the motor efficiency only. When the Rated Power Consumption if autosized,
        an impeller efficiency of 0.78 is assumed in addition to the motor efficiency.

        Args:
            value (float): value for IDD Field `Motor Efficiency`
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
            except ValueError:
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
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=0.0):
        """  Corresponds to IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`

        Args:
            value (float): value for IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`
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
    def coefficient_1_of_the_part_load_performance_curve(self, value=0.0):
        """  Corresponds to IDD Field `Coefficient 1 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 1 of the Part Load Performance Curve`
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
    def coefficient_2_of_the_part_load_performance_curve(self, value=1.0):
        """  Corresponds to IDD Field `Coefficient 2 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 2 of the Part Load Performance Curve`
                Default value: 1.0
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
    def coefficient_3_of_the_part_load_performance_curve(self, value=0.0):
        """  Corresponds to IDD Field `Coefficient 3 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 3 of the Part Load Performance Curve`
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
    def coefficient_4_of_the_part_load_performance_curve(self, value=0.0):
        """  Corresponds to IDD Field `Coefficient 4 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 4 of the Part Load Performance Curve`
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
    def minimum_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Flow Rate`
        This value can be zero and will be defaulted to that if not specified.

        Args:
            value (float): value for IDD Field `Minimum Flow Rate`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Pump Control Type`

        Args:
            value (str): value for IDD Field `Pump Control Type`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Pump Flow Rate Schedule Name`
        Modifies the rated flow rate of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `Pump Flow Rate Schedule Name`
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
        """  Corresponds to IDD Field `Pump Curve Name`
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
            value (str): value for IDD Field `Pump Curve Name`
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
        """  Corresponds to IDD Field `Impeller Diameter`
        "D" in above expression in field A6

        Args:
            value (float): value for IDD Field `Impeller Diameter`
                Units: m
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
        """  Corresponds to IDD Field `VFD Control Type`

        Args:
            value (str): value for IDD Field `VFD Control Type`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Pump rpm Schedule Name`
        Modifies the rpm of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `Pump rpm Schedule Name`
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
        """  Corresponds to IDD Field `Minimum Pressure Schedule`

        Args:
            value (str): value for IDD Field `Minimum Pressure Schedule`
                Units: Pa
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
        """  Corresponds to IDD Field `Maximum Pressure Schedule`

        Args:
            value (str): value for IDD Field `Maximum Pressure Schedule`
                Units: Pa
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
        """  Corresponds to IDD Field `Minimum RPM Schedule`

        Args:
            value (str): value for IDD Field `Minimum RPM Schedule`
                Units: Rotations Per Minute
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
        """  Corresponds to IDD Field `Maximum RPM Schedule`

        Args:
            value (str): value for IDD Field `Maximum RPM Schedule`
                Units: Rotations Per Minute
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
        """  Corresponds to IDD Field `Zone Name`
        optional, if used pump losses transfered to zone as internal gains

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
    def skin_loss_radiative_fraction(self):
        """Get skin_loss_radiative_fraction

        Returns:
            float: the value of `skin_loss_radiative_fraction` or None if not set
        """
        return self._data["Skin Loss Radiative Fraction"]

    @skin_loss_radiative_fraction.setter
    def skin_loss_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `Skin Loss Radiative Fraction`
        optional. If zone identified in previous field then this determines
        the split between convection and radiation for the skin losses

        Args:
            value (float): value for IDD Field `Skin Loss Radiative Fraction`
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
        """  Corresponds to IDD Field `Name`

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
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
        """  Corresponds to IDD Field `Rated Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Flow Rate`
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
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Rated Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
    def rated_pump_head(self, value=179352.0):
        """  Corresponds to IDD Field `Rated Pump Head`
        default head is 60 feet

        Args:
            value (float): value for IDD Field `Rated Pump Head`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Rated Power Consumption`
        If this field is autosized, an impeller efficiency of 0.78 is assumed.
        autosized Rated Power Consumption = Rated Flow Rate * Rated Pump Head / (0.78 * Motor Efficiency)

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Power Consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Rated Power Consumption"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
    def motor_efficiency(self, value=0.9):
        """  Corresponds to IDD Field `Motor Efficiency`
        This is the motor efficiency only. When the Rated Power Consumption if autosized,
        an impeller efficiency of 0.78 is assumed in addition to the motor efficiency.

        Args:
            value (float): value for IDD Field `Motor Efficiency`
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
            except ValueError:
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
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=0.0):
        """  Corresponds to IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`

        Args:
            value (float): value for IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`
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
        """  Corresponds to IDD Field `Pump Control Type`

        Args:
            value (str): value for IDD Field `Pump Control Type`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Pump Flow Rate Schedule Name`
        Modifies the rated flow rate of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `Pump Flow Rate Schedule Name`
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
        """  Corresponds to IDD Field `Pump Curve Name`
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
            value (str): value for IDD Field `Pump Curve Name`
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
        """  Corresponds to IDD Field `Impeller Diameter`
        "D" in above expression in field A6

        Args:
            value (float): value for IDD Field `Impeller Diameter`
                Units: m
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
        """  Corresponds to IDD Field `Rotational Speed`
        "N" in above expression in field A6

        Args:
            value (float): value for IDD Field `Rotational Speed`
                Units: rev/min
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
        """  Corresponds to IDD Field `Zone Name`
        optional, if used pump losses transfered to zone as internal gains

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
    def skin_loss_radiative_fraction(self):
        """Get skin_loss_radiative_fraction

        Returns:
            float: the value of `skin_loss_radiative_fraction` or None if not set
        """
        return self._data["Skin Loss Radiative Fraction"]

    @skin_loss_radiative_fraction.setter
    def skin_loss_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `Skin Loss Radiative Fraction`
        optional. If zone identified in previous field then this determines
        the split between convection and radiation for the skin losses

        Args:
            value (float): value for IDD Field `Skin Loss Radiative Fraction`
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
        """  Corresponds to IDD Field `Name`

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
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
        """  Corresponds to IDD Field `Rated Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Flow Rate`
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
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Rated Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
    def rated_pump_head(self, value=179352.0):
        """  Corresponds to IDD Field `Rated Pump Head`
        default head is 60 feet

        Args:
            value (float): value for IDD Field `Rated Pump Head`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Rated Power Consumption`
        If this field is autosized, an impeller efficiency of 0.78 is assumed.
        autosized Rated Power Consumption = Rated Flow Rate * Rated Pump Head / (0.78 * Motor Efficiency)

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Power Consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Rated Power Consumption"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
    def motor_efficiency(self, value=0.9):
        """  Corresponds to IDD Field `Motor Efficiency`
        This is the motor efficiency only. When the Rated Power Consumption if autosized,
        an impeller efficiency of 0.78 is assumed in addition to the motor efficiency.

        Args:
            value (float): value for IDD Field `Motor Efficiency`
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
            except ValueError:
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
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=0.0):
        """  Corresponds to IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`

        Args:
            value (float): value for IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`
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
    def coefficient_1_of_the_part_load_performance_curve(self, value=0.0):
        """  Corresponds to IDD Field `Coefficient 1 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 1 of the Part Load Performance Curve`
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
    def coefficient_2_of_the_part_load_performance_curve(self, value=1.0):
        """  Corresponds to IDD Field `Coefficient 2 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 2 of the Part Load Performance Curve`
                Default value: 1.0
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
    def coefficient_3_of_the_part_load_performance_curve(self, value=0.0):
        """  Corresponds to IDD Field `Coefficient 3 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 3 of the Part Load Performance Curve`
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
    def coefficient_4_of_the_part_load_performance_curve(self, value=0.0):
        """  Corresponds to IDD Field `Coefficient 4 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 4 of the Part Load Performance Curve`
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
        """  Corresponds to IDD Field `Pump Flow Rate Schedule Name`
        Modifies the rated flow rate of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `Pump Flow Rate Schedule Name`
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
        """  Corresponds to IDD Field `Zone Name`
        optional, if used pump losses transfered to zone as internal gains

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
    def skin_loss_radiative_fraction(self):
        """Get skin_loss_radiative_fraction

        Returns:
            float: the value of `skin_loss_radiative_fraction` or None if not set
        """
        return self._data["Skin Loss Radiative Fraction"]

    @skin_loss_radiative_fraction.setter
    def skin_loss_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `Skin Loss Radiative Fraction`
        optional. If zone identified in previous field then this determines
        the split between convection and radiation for the skin losses

        Args:
            value (float): value for IDD Field `Skin Loss Radiative Fraction`
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
        """  Corresponds to IDD Field `Name`

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
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
        """  Corresponds to IDD Field `Total Rated Flow Rate`
        If the field is not autosized set to the flow rate to
        the total flow when all pumps are running at full load

        Args:
            value (float or "Autosize"): value for IDD Field `Total Rated Flow Rate`
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
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Total Rated Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Number of Pumps in Bank`

        Args:
            value (int): value for IDD Field `Number of Pumps in Bank`
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
        """  Corresponds to IDD Field `Flow Sequencing Control Scheme`

        Args:
            value (str): value for IDD Field `Flow Sequencing Control Scheme`
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
            except ValueError:
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
    def rated_pump_head(self, value=179352.0):
        """  Corresponds to IDD Field `Rated Pump Head`
        default head is 60 feet

        Args:
            value (float): value for IDD Field `Rated Pump Head`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Rated Power Consumption`
        If the field is not autosized set to the power consumed by the pump bank
        when all the pumps are running at nominal flow
        If this field is autosized, an impeller efficiency of 0.78 is assumed.
        autosized Rated Power Consumption = Total Rated Flow Rate * Rated Pump Head / (0.78 * Motor Efficiency)

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Power Consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Rated Power Consumption"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
    def motor_efficiency(self, value=0.9):
        """  Corresponds to IDD Field `Motor Efficiency`
        This is the motor efficiency only. When the Rated Power Consumption if autosized,
        an impeller efficiency of 0.78 is assumed in addition to the motor efficiency.

        Args:
            value (float): value for IDD Field `Motor Efficiency`
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
            except ValueError:
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
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=0.0):
        """  Corresponds to IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`

        Args:
            value (float): value for IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`
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
        """  Corresponds to IDD Field `Pump Control Type`

        Args:
            value (str): value for IDD Field `Pump Control Type`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Pump Flow Rate Schedule Name`
        Modifies the rated flow rate of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `Pump Flow Rate Schedule Name`
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
        """  Corresponds to IDD Field `Zone Name`
        optional, if used pump losses transfered to zone as internal gains

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
    def skin_loss_radiative_fraction(self):
        """Get skin_loss_radiative_fraction

        Returns:
            float: the value of `skin_loss_radiative_fraction` or None if not set
        """
        return self._data["Skin Loss Radiative Fraction"]

    @skin_loss_radiative_fraction.setter
    def skin_loss_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `Skin Loss Radiative Fraction`
        optional. If zone identified in previous field then this determines
        the split between convection and radiation for the skin losses

        Args:
            value (float): value for IDD Field `Skin Loss Radiative Fraction`
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

class HeaderedPumpsVariableSpeed(object):
    """ Corresponds to IDD object `HeaderedPumps:VariableSpeed`
        This Headered pump object describes a pump bank with more than 1 pump in parallel
    
    """
    internal_name = "HeaderedPumps:VariableSpeed"
    field_count = 19
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `HeaderedPumps:VariableSpeed`
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
        self._data["Coefficient 1 of the Part Load Performance Curve"] = None
        self._data["Coefficient 2 of the Part Load Performance Curve"] = None
        self._data["Coefficient 3 of the Part Load Performance Curve"] = None
        self._data["Coefficient 4 of the Part Load Performance Curve"] = None
        self._data["Minimum Flow Rate Fraction"] = None
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
            self.minimum_flow_rate_fraction = None
        else:
            self.minimum_flow_rate_fraction = vals[i]
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
        """  Corresponds to IDD Field `Name`

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
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
        """  Corresponds to IDD Field `Total Rated Flow Rate`
        If the field is not autosized set to the flow rate to
        the total flow when all pumps are running at full load

        Args:
            value (float or "Autosize"): value for IDD Field `Total Rated Flow Rate`
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
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Total Rated Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Number of Pumps in Bank`

        Args:
            value (int): value for IDD Field `Number of Pumps in Bank`
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
        """  Corresponds to IDD Field `Flow Sequencing Control Scheme`

        Args:
            value (str): value for IDD Field `Flow Sequencing Control Scheme`
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
            except ValueError:
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
    def rated_pump_head(self, value=179352.0):
        """  Corresponds to IDD Field `Rated Pump Head`
        default head is 60 feet

        Args:
            value (float): value for IDD Field `Rated Pump Head`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Rated Power Consumption`
        If the field is not autosized set to the power consumed by the pump bank
        when all the pumps are running at nominal flow
        If this field is autosized, an impeller efficiency of 0.78 is assumed.
        autosized Rated Power Consumption = Total Rated Flow Rate * Rated Pump Head / (0.78 * Motor Efficiency)

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Power Consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Rated Power Consumption"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
    def motor_efficiency(self, value=0.9):
        """  Corresponds to IDD Field `Motor Efficiency`
        This is the motor efficiency only. When the Rated Power Consumption if autosized,
        an impeller efficiency of 0.78 is assumed in addition to the motor efficiency.

        Args:
            value (float): value for IDD Field `Motor Efficiency`
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
            except ValueError:
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
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=0.0):
        """  Corresponds to IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`

        Args:
            value (float): value for IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`
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
    def coefficient_1_of_the_part_load_performance_curve(self, value=0.0):
        """  Corresponds to IDD Field `Coefficient 1 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 1 of the Part Load Performance Curve`
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
    def coefficient_2_of_the_part_load_performance_curve(self, value=1.0):
        """  Corresponds to IDD Field `Coefficient 2 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 2 of the Part Load Performance Curve`
                Default value: 1.0
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
    def coefficient_3_of_the_part_load_performance_curve(self, value=0.0):
        """  Corresponds to IDD Field `Coefficient 3 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 3 of the Part Load Performance Curve`
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
    def coefficient_4_of_the_part_load_performance_curve(self, value=0.0):
        """  Corresponds to IDD Field `Coefficient 4 of the Part Load Performance Curve`

        Args:
            value (float): value for IDD Field `Coefficient 4 of the Part Load Performance Curve`
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
                                 'for field `coefficient_4_of_the_part_load_performance_curve`'.format(value))
        self._data["Coefficient 4 of the Part Load Performance Curve"] = value

    @property
    def minimum_flow_rate_fraction(self):
        """Get minimum_flow_rate_fraction

        Returns:
            float: the value of `minimum_flow_rate_fraction` or None if not set
        """
        return self._data["Minimum Flow Rate Fraction"]

    @minimum_flow_rate_fraction.setter
    def minimum_flow_rate_fraction(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Flow Rate Fraction`
        This value can be zero and will be defaulted to that if not specified.

        Args:
            value (float): value for IDD Field `Minimum Flow Rate Fraction`
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
                                 'for field `minimum_flow_rate_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_flow_rate_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_flow_rate_fraction`')
        self._data["Minimum Flow Rate Fraction"] = value

    @property
    def pump_control_type(self):
        """Get pump_control_type

        Returns:
            str: the value of `pump_control_type` or None if not set
        """
        return self._data["Pump Control Type"]

    @pump_control_type.setter
    def pump_control_type(self, value="Continuous"):
        """  Corresponds to IDD Field `Pump Control Type`

        Args:
            value (str): value for IDD Field `Pump Control Type`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Pump Flow Rate Schedule Name`
        Modifies the rated flow rate of the pump on a time basis. Default is
        that the pump is on and runs according to its other operational requirements
        specified above.  The schedule is for special pump operations.

        Args:
            value (str): value for IDD Field `Pump Flow Rate Schedule Name`
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
        """  Corresponds to IDD Field `Zone Name`
        optional, if used pump losses transfered to zone as internal gains

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
    def skin_loss_radiative_fraction(self):
        """Get skin_loss_radiative_fraction

        Returns:
            float: the value of `skin_loss_radiative_fraction` or None if not set
        """
        return self._data["Skin Loss Radiative Fraction"]

    @skin_loss_radiative_fraction.setter
    def skin_loss_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `Skin Loss Radiative Fraction`
        optional. If zone identified in previous field then this determines
        the split between convection and radiation for the skin losses

        Args:
            value (float): value for IDD Field `Skin Loss Radiative Fraction`
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