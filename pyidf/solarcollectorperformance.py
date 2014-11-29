from collections import OrderedDict

class SolarCollectorPerformanceFlatPlate(object):
    """ Corresponds to IDD object `SolarCollectorPerformance:FlatPlate`
        Thermal and optical performance parameters for a single flat plate solar collector
        module. These parameters are based on the testing methodologies described in ASHRAE
        Standards 93 and 96 which are used Solar Rating and Certification Corporation (SRCC)
        Directory of SRCC Certified Solar Collector Ratings. See EnergyPlus DataSets file
        SolarCollectors.idf.
    """
    internal_name = "SolarCollectorPerformance:FlatPlate"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SolarCollectorPerformance:FlatPlate`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Gross Area"] = None
        self._data["Test Fluid"] = None
        self._data["Test Flow Rate"] = None
        self._data["Test Correlation Type"] = None
        self._data["Coefficient 1 of Efficiency Equation"] = None
        self._data["Coefficient 2 of Efficiency Equation"] = None
        self._data["Coefficient 3 of Efficiency Equation"] = None
        self._data["Coefficient 2 of Incident Angle Modifier"] = None
        self._data["Coefficient 3 of Incident Angle Modifier"] = None

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
            self.gross_area = None
        else:
            self.gross_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.test_fluid = None
        else:
            self.test_fluid = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.test_flow_rate = None
        else:
            self.test_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.test_correlation_type = None
        else:
            self.test_correlation_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_1_of_efficiency_equation = None
        else:
            self.coefficient_1_of_efficiency_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_efficiency_equation = None
        else:
            self.coefficient_2_of_efficiency_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_efficiency_equation = None
        else:
            self.coefficient_3_of_efficiency_equation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_2_of_incident_angle_modifier = None
        else:
            self.coefficient_2_of_incident_angle_modifier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_3_of_incident_angle_modifier = None
        else:
            self.coefficient_3_of_incident_angle_modifier = vals[i]
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
    def gross_area(self):
        """Get gross_area

        Returns:
            float: the value of `gross_area` or None if not set
        """
        return self._data["Gross Area"]

    @gross_area.setter
    def gross_area(self, value=None):
        """  Corresponds to IDD Field `gross_area`

        Args:
            value (float): value for IDD Field `gross_area`
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
                                 'for field `gross_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gross_area`')

        self._data["Gross Area"] = value

    @property
    def test_fluid(self):
        """Get test_fluid

        Returns:
            str: the value of `test_fluid` or None if not set
        """
        return self._data["Test Fluid"]

    @test_fluid.setter
    def test_fluid(self, value="Water"):
        """  Corresponds to IDD Field `test_fluid`

        Args:
            value (str): value for IDD Field `test_fluid`
                Accepted values are:
                      - Water
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
                                 'for field `test_fluid`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `test_fluid`')
            vals = set()
            vals.add("Water")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `test_fluid`'.format(value))

        self._data["Test Fluid"] = value

    @property
    def test_flow_rate(self):
        """Get test_flow_rate

        Returns:
            float: the value of `test_flow_rate` or None if not set
        """
        return self._data["Test Flow Rate"]

    @test_flow_rate.setter
    def test_flow_rate(self, value=None):
        """  Corresponds to IDD Field `test_flow_rate`

        Args:
            value (float): value for IDD Field `test_flow_rate`
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
                                 'for field `test_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `test_flow_rate`')

        self._data["Test Flow Rate"] = value

    @property
    def test_correlation_type(self):
        """Get test_correlation_type

        Returns:
            str: the value of `test_correlation_type` or None if not set
        """
        return self._data["Test Correlation Type"]

    @test_correlation_type.setter
    def test_correlation_type(self, value=None):
        """  Corresponds to IDD Field `test_correlation_type`

        Args:
            value (str): value for IDD Field `test_correlation_type`
                Accepted values are:
                      - Inlet
                      - Average
                      - Outlet
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `test_correlation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `test_correlation_type`')
            vals = set()
            vals.add("Inlet")
            vals.add("Average")
            vals.add("Outlet")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `test_correlation_type`'.format(value))

        self._data["Test Correlation Type"] = value

    @property
    def coefficient_1_of_efficiency_equation(self):
        """Get coefficient_1_of_efficiency_equation

        Returns:
            float: the value of `coefficient_1_of_efficiency_equation` or None if not set
        """
        return self._data["Coefficient 1 of Efficiency Equation"]

    @coefficient_1_of_efficiency_equation.setter
    def coefficient_1_of_efficiency_equation(self, value=None):
        """  Corresponds to IDD Field `coefficient_1_of_efficiency_equation`
        Y-intercept term

        Args:
            value (float): value for IDD Field `coefficient_1_of_efficiency_equation`
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
                                 'for field `coefficient_1_of_efficiency_equation`'.format(value))

        self._data["Coefficient 1 of Efficiency Equation"] = value

    @property
    def coefficient_2_of_efficiency_equation(self):
        """Get coefficient_2_of_efficiency_equation

        Returns:
            float: the value of `coefficient_2_of_efficiency_equation` or None if not set
        """
        return self._data["Coefficient 2 of Efficiency Equation"]

    @coefficient_2_of_efficiency_equation.setter
    def coefficient_2_of_efficiency_equation(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_efficiency_equation`
        1st Order term

        Args:
            value (float): value for IDD Field `coefficient_2_of_efficiency_equation`
                Unit: W/m2-K
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_2_of_efficiency_equation`'.format(value))

        self._data["Coefficient 2 of Efficiency Equation"] = value

    @property
    def coefficient_3_of_efficiency_equation(self):
        """Get coefficient_3_of_efficiency_equation

        Returns:
            float: the value of `coefficient_3_of_efficiency_equation` or None if not set
        """
        return self._data["Coefficient 3 of Efficiency Equation"]

    @coefficient_3_of_efficiency_equation.setter
    def coefficient_3_of_efficiency_equation(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_efficiency_equation`
        2nd order term

        Args:
            value (float): value for IDD Field `coefficient_3_of_efficiency_equation`
                Unit: W/m2-K2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_3_of_efficiency_equation`'.format(value))

        self._data["Coefficient 3 of Efficiency Equation"] = value

    @property
    def coefficient_2_of_incident_angle_modifier(self):
        """Get coefficient_2_of_incident_angle_modifier

        Returns:
            float: the value of `coefficient_2_of_incident_angle_modifier` or None if not set
        """
        return self._data["Coefficient 2 of Incident Angle Modifier"]

    @coefficient_2_of_incident_angle_modifier.setter
    def coefficient_2_of_incident_angle_modifier(self, value=None):
        """  Corresponds to IDD Field `coefficient_2_of_incident_angle_modifier`
        1st order term

        Args:
            value (float): value for IDD Field `coefficient_2_of_incident_angle_modifier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_2_of_incident_angle_modifier`'.format(value))

        self._data["Coefficient 2 of Incident Angle Modifier"] = value

    @property
    def coefficient_3_of_incident_angle_modifier(self):
        """Get coefficient_3_of_incident_angle_modifier

        Returns:
            float: the value of `coefficient_3_of_incident_angle_modifier` or None if not set
        """
        return self._data["Coefficient 3 of Incident Angle Modifier"]

    @coefficient_3_of_incident_angle_modifier.setter
    def coefficient_3_of_incident_angle_modifier(self, value=None):
        """  Corresponds to IDD Field `coefficient_3_of_incident_angle_modifier`
        2nd order term

        Args:
            value (float): value for IDD Field `coefficient_3_of_incident_angle_modifier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_3_of_incident_angle_modifier`'.format(value))

        self._data["Coefficient 3 of Incident Angle Modifier"] = value

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
        out.append(self._to_str(self.gross_area))
        out.append(self._to_str(self.test_fluid))
        out.append(self._to_str(self.test_flow_rate))
        out.append(self._to_str(self.test_correlation_type))
        out.append(self._to_str(self.coefficient_1_of_efficiency_equation))
        out.append(self._to_str(self.coefficient_2_of_efficiency_equation))
        out.append(self._to_str(self.coefficient_3_of_efficiency_equation))
        out.append(self._to_str(self.coefficient_2_of_incident_angle_modifier))
        out.append(self._to_str(self.coefficient_3_of_incident_angle_modifier))
        return ",".join(out)

class SolarCollectorPerformancePhotovoltaicThermalSimple(object):
    """ Corresponds to IDD object `SolarCollectorPerformance:PhotovoltaicThermal:Simple`
        Thermal performance parameters for a hybrid photovoltaic-thermal (PVT) solar collector.
    """
    internal_name = "SolarCollectorPerformance:PhotovoltaicThermal:Simple"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SolarCollectorPerformance:PhotovoltaicThermal:Simple`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fraction of Surface Area with Active Thermal Collector"] = None
        self._data["Thermal Conversion Efficiency Input Mode Type"] = None
        self._data["Value for Thermal Conversion Efficiency if Fixed"] = None
        self._data["Thermal Conversion Efficiency Schedule Name"] = None
        self._data["Front Surface Emittance"] = None

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
            self.fraction_of_surface_area_with_active_thermal_collector = None
        else:
            self.fraction_of_surface_area_with_active_thermal_collector = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conversion_efficiency_input_mode_type = None
        else:
            self.thermal_conversion_efficiency_input_mode_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_for_thermal_conversion_efficiency_if_fixed = None
        else:
            self.value_for_thermal_conversion_efficiency_if_fixed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conversion_efficiency_schedule_name = None
        else:
            self.thermal_conversion_efficiency_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_surface_emittance = None
        else:
            self.front_surface_emittance = vals[i]
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
    def fraction_of_surface_area_with_active_thermal_collector(self):
        """Get fraction_of_surface_area_with_active_thermal_collector

        Returns:
            float: the value of `fraction_of_surface_area_with_active_thermal_collector` or None if not set
        """
        return self._data["Fraction of Surface Area with Active Thermal Collector"]

    @fraction_of_surface_area_with_active_thermal_collector.setter
    def fraction_of_surface_area_with_active_thermal_collector(self, value=None):
        """  Corresponds to IDD Field `fraction_of_surface_area_with_active_thermal_collector`

        Args:
            value (float): value for IDD Field `fraction_of_surface_area_with_active_thermal_collector`
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
                                 'for field `fraction_of_surface_area_with_active_thermal_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `fraction_of_surface_area_with_active_thermal_collector`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_surface_area_with_active_thermal_collector`')

        self._data["Fraction of Surface Area with Active Thermal Collector"] = value

    @property
    def thermal_conversion_efficiency_input_mode_type(self):
        """Get thermal_conversion_efficiency_input_mode_type

        Returns:
            str: the value of `thermal_conversion_efficiency_input_mode_type` or None if not set
        """
        return self._data["Thermal Conversion Efficiency Input Mode Type"]

    @thermal_conversion_efficiency_input_mode_type.setter
    def thermal_conversion_efficiency_input_mode_type(self, value=None):
        """  Corresponds to IDD Field `thermal_conversion_efficiency_input_mode_type`

        Args:
            value (str): value for IDD Field `thermal_conversion_efficiency_input_mode_type`
                Accepted values are:
                      - Fixed
                      - Scheduled
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_conversion_efficiency_input_mode_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_conversion_efficiency_input_mode_type`')
            vals = set()
            vals.add("Fixed")
            vals.add("Scheduled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `thermal_conversion_efficiency_input_mode_type`'.format(value))

        self._data["Thermal Conversion Efficiency Input Mode Type"] = value

    @property
    def value_for_thermal_conversion_efficiency_if_fixed(self):
        """Get value_for_thermal_conversion_efficiency_if_fixed

        Returns:
            float: the value of `value_for_thermal_conversion_efficiency_if_fixed` or None if not set
        """
        return self._data["Value for Thermal Conversion Efficiency if Fixed"]

    @value_for_thermal_conversion_efficiency_if_fixed.setter
    def value_for_thermal_conversion_efficiency_if_fixed(self, value=None):
        """  Corresponds to IDD Field `value_for_thermal_conversion_efficiency_if_fixed`
        Efficiency = (thermal power generated [W])/(incident solar[W])

        Args:
            value (float): value for IDD Field `value_for_thermal_conversion_efficiency_if_fixed`
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
                                 'for field `value_for_thermal_conversion_efficiency_if_fixed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `value_for_thermal_conversion_efficiency_if_fixed`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `value_for_thermal_conversion_efficiency_if_fixed`')

        self._data["Value for Thermal Conversion Efficiency if Fixed"] = value

    @property
    def thermal_conversion_efficiency_schedule_name(self):
        """Get thermal_conversion_efficiency_schedule_name

        Returns:
            str: the value of `thermal_conversion_efficiency_schedule_name` or None if not set
        """
        return self._data["Thermal Conversion Efficiency Schedule Name"]

    @thermal_conversion_efficiency_schedule_name.setter
    def thermal_conversion_efficiency_schedule_name(self, value=None):
        """  Corresponds to IDD Field `thermal_conversion_efficiency_schedule_name`

        Args:
            value (str): value for IDD Field `thermal_conversion_efficiency_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_conversion_efficiency_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_conversion_efficiency_schedule_name`')

        self._data["Thermal Conversion Efficiency Schedule Name"] = value

    @property
    def front_surface_emittance(self):
        """Get front_surface_emittance

        Returns:
            float: the value of `front_surface_emittance` or None if not set
        """
        return self._data["Front Surface Emittance"]

    @front_surface_emittance.setter
    def front_surface_emittance(self, value=0.84 ):
        """  Corresponds to IDD Field `front_surface_emittance`

        Args:
            value (float): value for IDD Field `front_surface_emittance`
                Default value: 0.84
                value > 0.0
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
                                 'for field `front_surface_emittance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `front_surface_emittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_surface_emittance`')

        self._data["Front Surface Emittance"] = value

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
        out.append(self._to_str(self.fraction_of_surface_area_with_active_thermal_collector))
        out.append(self._to_str(self.thermal_conversion_efficiency_input_mode_type))
        out.append(self._to_str(self.value_for_thermal_conversion_efficiency_if_fixed))
        out.append(self._to_str(self.thermal_conversion_efficiency_schedule_name))
        out.append(self._to_str(self.front_surface_emittance))
        return ",".join(out)

class SolarCollectorPerformanceIntegralCollectorStorage(object):
    """ Corresponds to IDD object `SolarCollectorPerformance:IntegralCollectorStorage`
        Thermal and optical performance parameters for a single glazed solar collector with
        integral storage unit.
    """
    internal_name = "SolarCollectorPerformance:IntegralCollectorStorage"
    field_count = 19

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SolarCollectorPerformance:IntegralCollectorStorage`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["ICS Collector Type"] = None
        self._data["Gross Area"] = None
        self._data["Collector Water Volume"] = None
        self._data["Bottom Heat Loss Conductance"] = None
        self._data["Side Heat Loss Conductance"] = None
        self._data["Aspect Ratio"] = None
        self._data["Collector Side Height"] = None
        self._data["Thermal Mass of Absorber Plate"] = None
        self._data["Number of Covers"] = None
        self._data["Cover Spacing"] = None
        self._data["Refractive Index of Outer Cover"] = None
        self._data["Extinction Coefficient Times Thickness of Outer Cover"] = None
        self._data["Emissivity of Outer Cover"] = None
        self._data["Refractive Index of Inner Cover"] = None
        self._data["Extinction Coefficient Times Thickness of the inner Cover"] = None
        self._data["Emmissivity of Inner Cover"] = None
        self._data["Absorptance of Absorber Plate"] = None
        self._data["Emissivity of Absorber Plate"] = None

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
            self.ics_collector_type = None
        else:
            self.ics_collector_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gross_area = None
        else:
            self.gross_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.collector_water_volume = None
        else:
            self.collector_water_volume = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.bottom_heat_loss_conductance = None
        else:
            self.bottom_heat_loss_conductance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.side_heat_loss_conductance = None
        else:
            self.side_heat_loss_conductance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.aspect_ratio = None
        else:
            self.aspect_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.collector_side_height = None
        else:
            self.collector_side_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_mass_of_absorber_plate = None
        else:
            self.thermal_mass_of_absorber_plate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_covers = None
        else:
            self.number_of_covers = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cover_spacing = None
        else:
            self.cover_spacing = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.refractive_index_of_outer_cover = None
        else:
            self.refractive_index_of_outer_cover = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.extinction_coefficient_times_thickness_of_outer_cover = None
        else:
            self.extinction_coefficient_times_thickness_of_outer_cover = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.emissivity_of_outer_cover = None
        else:
            self.emissivity_of_outer_cover = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.refractive_index_of_inner_cover = None
        else:
            self.refractive_index_of_inner_cover = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.extinction_coefficient_times_thickness_of_the_inner_cover = None
        else:
            self.extinction_coefficient_times_thickness_of_the_inner_cover = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.emmissivity_of_inner_cover = None
        else:
            self.emmissivity_of_inner_cover = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.absorptance_of_absorber_plate = None
        else:
            self.absorptance_of_absorber_plate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.emissivity_of_absorber_plate = None
        else:
            self.emissivity_of_absorber_plate = vals[i]
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
    def ics_collector_type(self):
        """Get ics_collector_type

        Returns:
            str: the value of `ics_collector_type` or None if not set
        """
        return self._data["ICS Collector Type"]

    @ics_collector_type.setter
    def ics_collector_type(self, value=None):
        """  Corresponds to IDD Field `ics_collector_type`
        Currently only RectangularTank ICS collector type is available.

        Args:
            value (str): value for IDD Field `ics_collector_type`
                Accepted values are:
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ics_collector_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ics_collector_type`')
            vals = set()
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `ics_collector_type`'.format(value))

        self._data["ICS Collector Type"] = value

    @property
    def gross_area(self):
        """Get gross_area

        Returns:
            float: the value of `gross_area` or None if not set
        """
        return self._data["Gross Area"]

    @gross_area.setter
    def gross_area(self, value=None):
        """  Corresponds to IDD Field `gross_area`

        Args:
            value (float): value for IDD Field `gross_area`
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
                                 'for field `gross_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gross_area`')

        self._data["Gross Area"] = value

    @property
    def collector_water_volume(self):
        """Get collector_water_volume

        Returns:
            float: the value of `collector_water_volume` or None if not set
        """
        return self._data["Collector Water Volume"]

    @collector_water_volume.setter
    def collector_water_volume(self, value=None):
        """  Corresponds to IDD Field `collector_water_volume`

        Args:
            value (float): value for IDD Field `collector_water_volume`
                Unit: m3
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
                                 'for field `collector_water_volume`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `collector_water_volume`')

        self._data["Collector Water Volume"] = value

    @property
    def bottom_heat_loss_conductance(self):
        """Get bottom_heat_loss_conductance

        Returns:
            float: the value of `bottom_heat_loss_conductance` or None if not set
        """
        return self._data["Bottom Heat Loss Conductance"]

    @bottom_heat_loss_conductance.setter
    def bottom_heat_loss_conductance(self, value=0.4 ):
        """  Corresponds to IDD Field `bottom_heat_loss_conductance`
        Heat loss conductance of the collector bottom insulation

        Args:
            value (float): value for IDD Field `bottom_heat_loss_conductance`
                Unit: W/m2-K
                Default value: 0.4
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
                                 'for field `bottom_heat_loss_conductance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `bottom_heat_loss_conductance`')

        self._data["Bottom Heat Loss Conductance"] = value

    @property
    def side_heat_loss_conductance(self):
        """Get side_heat_loss_conductance

        Returns:
            float: the value of `side_heat_loss_conductance` or None if not set
        """
        return self._data["Side Heat Loss Conductance"]

    @side_heat_loss_conductance.setter
    def side_heat_loss_conductance(self, value=0.6 ):
        """  Corresponds to IDD Field `side_heat_loss_conductance`
        heat loss conductance of the collector side insulation

        Args:
            value (float): value for IDD Field `side_heat_loss_conductance`
                Unit: W/m2-K
                Default value: 0.6
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
                                 'for field `side_heat_loss_conductance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `side_heat_loss_conductance`')

        self._data["Side Heat Loss Conductance"] = value

    @property
    def aspect_ratio(self):
        """Get aspect_ratio

        Returns:
            float: the value of `aspect_ratio` or None if not set
        """
        return self._data["Aspect Ratio"]

    @aspect_ratio.setter
    def aspect_ratio(self, value=0.8 ):
        """  Corresponds to IDD Field `aspect_ratio`
        This value is ratio of the width (short side) to length
        (long side of) of the collector.  Used to calculate the
        perimeter of the collector

        Args:
            value (float): value for IDD Field `aspect_ratio`
                Unit: m
                Default value: 0.8
                value > 0.5
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
                                 'for field `aspect_ratio`'.format(value))
            if value <= 0.5:
                raise ValueError('value need to be greater 0.5 '
                                 'for field `aspect_ratio`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `aspect_ratio`')

        self._data["Aspect Ratio"] = value

    @property
    def collector_side_height(self):
        """Get collector_side_height

        Returns:
            float: the value of `collector_side_height` or None if not set
        """
        return self._data["Collector Side Height"]

    @collector_side_height.setter
    def collector_side_height(self, value=0.2 ):
        """  Corresponds to IDD Field `collector_side_height`
        This value is used to estimate collector side area for the heat
        loss calculation through the collector side

        Args:
            value (float): value for IDD Field `collector_side_height`
                Unit: m
                Default value: 0.2
                value > 0.0
                value < 0.3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `collector_side_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `collector_side_height`')
            if value >= 0.3:
                raise ValueError('value need to be smaller 0.3 '
                                 'for field `collector_side_height`')

        self._data["Collector Side Height"] = value

    @property
    def thermal_mass_of_absorber_plate(self):
        """Get thermal_mass_of_absorber_plate

        Returns:
            float: the value of `thermal_mass_of_absorber_plate` or None if not set
        """
        return self._data["Thermal Mass of Absorber Plate"]

    @thermal_mass_of_absorber_plate.setter
    def thermal_mass_of_absorber_plate(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_mass_of_absorber_plate`
        Calculated from the specific heat, density and thickness
        of the absorber plate.

        Args:
            value (float): value for IDD Field `thermal_mass_of_absorber_plate`
                Unit: J/m2-K
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
                                 'for field `thermal_mass_of_absorber_plate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `thermal_mass_of_absorber_plate`')

        self._data["Thermal Mass of Absorber Plate"] = value

    @property
    def number_of_covers(self):
        """Get number_of_covers

        Returns:
            int: the value of `number_of_covers` or None if not set
        """
        return self._data["Number of Covers"]

    @number_of_covers.setter
    def number_of_covers(self, value=2 ):
        """  Corresponds to IDD Field `number_of_covers`
        Number of transparent covers. Common practice is to use low-iron
        glass as the outer cover and very thin transparent sheet such as
        Teflon as the inner cover.

        Args:
            value (int): value for IDD Field `number_of_covers`
                Default value: 2
                value >= 1
                value <= 2
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
                                 'for field `number_of_covers`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_covers`')
            if value > 2:
                raise ValueError('value need to be smaller 2 '
                                 'for field `number_of_covers`')

        self._data["Number of Covers"] = value

    @property
    def cover_spacing(self):
        """Get cover_spacing

        Returns:
            float: the value of `cover_spacing` or None if not set
        """
        return self._data["Cover Spacing"]

    @cover_spacing.setter
    def cover_spacing(self, value=0.05 ):
        """  Corresponds to IDD Field `cover_spacing`
        The gap between the transparent covers and between the inner cover
        and the absorber plate

        Args:
            value (float): value for IDD Field `cover_spacing`
                Unit: m
                Default value: 0.05
                value > 0.0
                value <= 0.2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cover_spacing`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cover_spacing`')
            if value > 0.2:
                raise ValueError('value need to be smaller 0.2 '
                                 'for field `cover_spacing`')

        self._data["Cover Spacing"] = value

    @property
    def refractive_index_of_outer_cover(self):
        """Get refractive_index_of_outer_cover

        Returns:
            float: the value of `refractive_index_of_outer_cover` or None if not set
        """
        return self._data["Refractive Index of Outer Cover"]

    @refractive_index_of_outer_cover.setter
    def refractive_index_of_outer_cover(self, value=1.526 ):
        """  Corresponds to IDD Field `refractive_index_of_outer_cover`
        Refractive index of outer cover. Typically low-iron glass is used
        as the outer cover material, and used as the default outer cover
        with a vallue of 1.526.

        Args:
            value (float): value for IDD Field `refractive_index_of_outer_cover`
                Unit: dimensionless
                Default value: 1.526
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
                                 'for field `refractive_index_of_outer_cover`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `refractive_index_of_outer_cover`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `refractive_index_of_outer_cover`')

        self._data["Refractive Index of Outer Cover"] = value

    @property
    def extinction_coefficient_times_thickness_of_outer_cover(self):
        """Get extinction_coefficient_times_thickness_of_outer_cover

        Returns:
            float: the value of `extinction_coefficient_times_thickness_of_outer_cover` or None if not set
        """
        return self._data["Extinction Coefficient Times Thickness of Outer Cover"]

    @extinction_coefficient_times_thickness_of_outer_cover.setter
    def extinction_coefficient_times_thickness_of_outer_cover(self, value=0.045 ):
        """  Corresponds to IDD Field `extinction_coefficient_times_thickness_of_outer_cover`
        Clear glass has extinction coefficient of about 15 [1/m]
        and with thickness of 3.0mm, the product of the extinction
        coefficient and thickness becomes 0.045 (=15 * 0.003)

        Args:
            value (float): value for IDD Field `extinction_coefficient_times_thickness_of_outer_cover`
                Unit: dimensionless
                Default value: 0.045
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
                                 'for field `extinction_coefficient_times_thickness_of_outer_cover`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `extinction_coefficient_times_thickness_of_outer_cover`')

        self._data["Extinction Coefficient Times Thickness of Outer Cover"] = value

    @property
    def emissivity_of_outer_cover(self):
        """Get emissivity_of_outer_cover

        Returns:
            float: the value of `emissivity_of_outer_cover` or None if not set
        """
        return self._data["Emissivity of Outer Cover"]

    @emissivity_of_outer_cover.setter
    def emissivity_of_outer_cover(self, value=0.88 ):
        """  Corresponds to IDD Field `emissivity_of_outer_cover`
        Thermal emissivity of the outer cover, commonly glass is used as
        the out collector cover material.

        Args:
            value (float): value for IDD Field `emissivity_of_outer_cover`
                Unit: dimensionless
                Default value: 0.88
                value > 0.0
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
                                 'for field `emissivity_of_outer_cover`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `emissivity_of_outer_cover`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `emissivity_of_outer_cover`')

        self._data["Emissivity of Outer Cover"] = value

    @property
    def refractive_index_of_inner_cover(self):
        """Get refractive_index_of_inner_cover

        Returns:
            float: the value of `refractive_index_of_inner_cover` or None if not set
        """
        return self._data["Refractive Index of Inner Cover"]

    @refractive_index_of_inner_cover.setter
    def refractive_index_of_inner_cover(self, value=1.37 ):
        """  Corresponds to IDD Field `refractive_index_of_inner_cover`
        Typical material is very thin sheet of Teflon (PTFE). The default
        value is refractive index of Teflon.

        Args:
            value (float): value for IDD Field `refractive_index_of_inner_cover`
                Unit: dimensionless
                Default value: 1.37
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
                                 'for field `refractive_index_of_inner_cover`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `refractive_index_of_inner_cover`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `refractive_index_of_inner_cover`')

        self._data["Refractive Index of Inner Cover"] = value

    @property
    def extinction_coefficient_times_thickness_of_the_inner_cover(self):
        """Get extinction_coefficient_times_thickness_of_the_inner_cover

        Returns:
            float: the value of `extinction_coefficient_times_thickness_of_the_inner_cover` or None if not set
        """
        return self._data["Extinction Coefficient Times Thickness of the inner Cover"]

    @extinction_coefficient_times_thickness_of_the_inner_cover.setter
    def extinction_coefficient_times_thickness_of_the_inner_cover(self, value=0.008 ):
        """  Corresponds to IDD Field `extinction_coefficient_times_thickness_of_the_inner_cover`
        Default inner cover is very thin sheet of Teflon with
        extinction coefficient of approximately 40.0 and a thickness
        0.2mm yields a default value of 0.008.

        Args:
            value (float): value for IDD Field `extinction_coefficient_times_thickness_of_the_inner_cover`
                Unit: dimensionless
                Default value: 0.008
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
                                 'for field `extinction_coefficient_times_thickness_of_the_inner_cover`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `extinction_coefficient_times_thickness_of_the_inner_cover`')

        self._data["Extinction Coefficient Times Thickness of the inner Cover"] = value

    @property
    def emmissivity_of_inner_cover(self):
        """Get emmissivity_of_inner_cover

        Returns:
            float: the value of `emmissivity_of_inner_cover` or None if not set
        """
        return self._data["Emmissivity of Inner Cover"]

    @emmissivity_of_inner_cover.setter
    def emmissivity_of_inner_cover(self, value=0.88 ):
        """  Corresponds to IDD Field `emmissivity_of_inner_cover`
        Thermal emissivity of the inner cover matrial

        Args:
            value (float): value for IDD Field `emmissivity_of_inner_cover`
                Unit: dimensionless
                Default value: 0.88
                value > 0.0
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
                                 'for field `emmissivity_of_inner_cover`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `emmissivity_of_inner_cover`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `emmissivity_of_inner_cover`')

        self._data["Emmissivity of Inner Cover"] = value

    @property
    def absorptance_of_absorber_plate(self):
        """Get absorptance_of_absorber_plate

        Returns:
            float: the value of `absorptance_of_absorber_plate` or None if not set
        """
        return self._data["Absorptance of Absorber Plate"]

    @absorptance_of_absorber_plate.setter
    def absorptance_of_absorber_plate(self, value=0.96 ):
        """  Corresponds to IDD Field `absorptance_of_absorber_plate`
        The absober plate solar absorptance.  Copper is assumed as
        the default absorber plate.

        Args:
            value (float): value for IDD Field `absorptance_of_absorber_plate`
                Unit: dimensionless
                Default value: 0.96
                value > 0.0
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
                                 'for field `absorptance_of_absorber_plate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `absorptance_of_absorber_plate`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `absorptance_of_absorber_plate`')

        self._data["Absorptance of Absorber Plate"] = value

    @property
    def emissivity_of_absorber_plate(self):
        """Get emissivity_of_absorber_plate

        Returns:
            float: the value of `emissivity_of_absorber_plate` or None if not set
        """
        return self._data["Emissivity of Absorber Plate"]

    @emissivity_of_absorber_plate.setter
    def emissivity_of_absorber_plate(self, value=0.3 ):
        """  Corresponds to IDD Field `emissivity_of_absorber_plate`
        Thermal emissivity of the absorber plate

        Args:
            value (float): value for IDD Field `emissivity_of_absorber_plate`
                Unit: dimensionless
                Default value: 0.3
                value > 0.0
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
                                 'for field `emissivity_of_absorber_plate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `emissivity_of_absorber_plate`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `emissivity_of_absorber_plate`')

        self._data["Emissivity of Absorber Plate"] = value

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
        out.append(self._to_str(self.ics_collector_type))
        out.append(self._to_str(self.gross_area))
        out.append(self._to_str(self.collector_water_volume))
        out.append(self._to_str(self.bottom_heat_loss_conductance))
        out.append(self._to_str(self.side_heat_loss_conductance))
        out.append(self._to_str(self.aspect_ratio))
        out.append(self._to_str(self.collector_side_height))
        out.append(self._to_str(self.thermal_mass_of_absorber_plate))
        out.append(self._to_str(self.number_of_covers))
        out.append(self._to_str(self.cover_spacing))
        out.append(self._to_str(self.refractive_index_of_outer_cover))
        out.append(self._to_str(self.extinction_coefficient_times_thickness_of_outer_cover))
        out.append(self._to_str(self.emissivity_of_outer_cover))
        out.append(self._to_str(self.refractive_index_of_inner_cover))
        out.append(self._to_str(self.extinction_coefficient_times_thickness_of_the_inner_cover))
        out.append(self._to_str(self.emmissivity_of_inner_cover))
        out.append(self._to_str(self.absorptance_of_absorber_plate))
        out.append(self._to_str(self.emissivity_of_absorber_plate))
        return ",".join(out)