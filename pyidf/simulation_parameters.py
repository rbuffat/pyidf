from collections import OrderedDict

class Version(object):
    """ Corresponds to IDD object `Version`
        Specifies the EnergyPlus version of the IDF file.
    
    """
    internal_name = "Version"
    field_count = 1
    required_fields = ["Version Identifier"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Version`
        """
        self._data = OrderedDict()
        self._data["Version Identifier"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.version_identifier = None
        else:
            self.version_identifier = vals[i]
        i += 1

    @property
    def version_identifier(self):
        """Get version_identifier

        Returns:
            str: the value of `version_identifier` or None if not set
        """
        return self._data["Version Identifier"]

    @version_identifier.setter
    def version_identifier(self, value="7.0"):
        """  Corresponds to IDD Field `version_identifier`

        Args:
            value (str): value for IDD Field `version_identifier`
                Default value: 7.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `version_identifier`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `version_identifier`')

        self._data["Version Identifier"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.version_identifier))
        return ",".join(out)

class SimulationControl(object):
    """ Corresponds to IDD object `SimulationControl`
        Note that the following 3 fields are related to the Sizing:Zone, Sizing:System,
        and Sizing:Plant objects.  Having these fields set to Yes but no corresponding
        Sizing object will not cause the sizing to be done. However, having any of these
        fields set to No, the corresponding Sizing object is ignored.
        Note also, if you want to do system sizing, you must also do zone sizing in the same
        run or an error will result.
    
    """
    internal_name = "SimulationControl"
    field_count = 5
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SimulationControl`
        """
        self._data = OrderedDict()
        self._data["Do Zone Sizing Calculation"] = None
        self._data["Do System Sizing Calculation"] = None
        self._data["Do Plant Sizing Calculation"] = None
        self._data["Run Simulation for Sizing Periods"] = None
        self._data["Run Simulation for Weather File Run Periods"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.do_zone_sizing_calculation = None
        else:
            self.do_zone_sizing_calculation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.do_system_sizing_calculation = None
        else:
            self.do_system_sizing_calculation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.do_plant_sizing_calculation = None
        else:
            self.do_plant_sizing_calculation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.run_simulation_for_sizing_periods = None
        else:
            self.run_simulation_for_sizing_periods = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.run_simulation_for_weather_file_run_periods = None
        else:
            self.run_simulation_for_weather_file_run_periods = vals[i]
        i += 1

    @property
    def do_zone_sizing_calculation(self):
        """Get do_zone_sizing_calculation

        Returns:
            str: the value of `do_zone_sizing_calculation` or None if not set
        """
        return self._data["Do Zone Sizing Calculation"]

    @do_zone_sizing_calculation.setter
    def do_zone_sizing_calculation(self, value="No"):
        """  Corresponds to IDD Field `do_zone_sizing_calculation`
        If Yes, Zone sizing is accomplished from corresponding Sizing:Zone objects
        and autosize fields.

        Args:
            value (str): value for IDD Field `do_zone_sizing_calculation`
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
                                 'for field `do_zone_sizing_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `do_zone_sizing_calculation`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `do_zone_sizing_calculation`'.format(value))

        self._data["Do Zone Sizing Calculation"] = value

    @property
    def do_system_sizing_calculation(self):
        """Get do_system_sizing_calculation

        Returns:
            str: the value of `do_system_sizing_calculation` or None if not set
        """
        return self._data["Do System Sizing Calculation"]

    @do_system_sizing_calculation.setter
    def do_system_sizing_calculation(self, value="No"):
        """  Corresponds to IDD Field `do_system_sizing_calculation`
        If Yes, System sizing is accomplished from corresponding Sizing:System objects
        and autosize fields.
        If Yes, Zone sizing (previous field) must also be Yes.

        Args:
            value (str): value for IDD Field `do_system_sizing_calculation`
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
                                 'for field `do_system_sizing_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `do_system_sizing_calculation`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `do_system_sizing_calculation`'.format(value))

        self._data["Do System Sizing Calculation"] = value

    @property
    def do_plant_sizing_calculation(self):
        """Get do_plant_sizing_calculation

        Returns:
            str: the value of `do_plant_sizing_calculation` or None if not set
        """
        return self._data["Do Plant Sizing Calculation"]

    @do_plant_sizing_calculation.setter
    def do_plant_sizing_calculation(self, value="No"):
        """  Corresponds to IDD Field `do_plant_sizing_calculation`
        If Yes, Plant sizing is accomplished from corresponding Sizing:Plant objects
        and autosize fields.

        Args:
            value (str): value for IDD Field `do_plant_sizing_calculation`
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
                                 'for field `do_plant_sizing_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `do_plant_sizing_calculation`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `do_plant_sizing_calculation`'.format(value))

        self._data["Do Plant Sizing Calculation"] = value

    @property
    def run_simulation_for_sizing_periods(self):
        """Get run_simulation_for_sizing_periods

        Returns:
            str: the value of `run_simulation_for_sizing_periods` or None if not set
        """
        return self._data["Run Simulation for Sizing Periods"]

    @run_simulation_for_sizing_periods.setter
    def run_simulation_for_sizing_periods(self, value="Yes"):
        """  Corresponds to IDD Field `run_simulation_for_sizing_periods`
        If Yes, SizingPeriod:* objects are executed and results from those may be displayed..

        Args:
            value (str): value for IDD Field `run_simulation_for_sizing_periods`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `run_simulation_for_sizing_periods`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `run_simulation_for_sizing_periods`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `run_simulation_for_sizing_periods`'.format(value))

        self._data["Run Simulation for Sizing Periods"] = value

    @property
    def run_simulation_for_weather_file_run_periods(self):
        """Get run_simulation_for_weather_file_run_periods

        Returns:
            str: the value of `run_simulation_for_weather_file_run_periods` or None if not set
        """
        return self._data["Run Simulation for Weather File Run Periods"]

    @run_simulation_for_weather_file_run_periods.setter
    def run_simulation_for_weather_file_run_periods(self, value="Yes"):
        """  Corresponds to IDD Field `run_simulation_for_weather_file_run_periods`
        If Yes, RunPeriod:* objects are executed and results from those may be displayed..

        Args:
            value (str): value for IDD Field `run_simulation_for_weather_file_run_periods`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `run_simulation_for_weather_file_run_periods`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `run_simulation_for_weather_file_run_periods`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `run_simulation_for_weather_file_run_periods`'.format(value))

        self._data["Run Simulation for Weather File Run Periods"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.do_zone_sizing_calculation))
        out.append(self._to_str(self.do_system_sizing_calculation))
        out.append(self._to_str(self.do_plant_sizing_calculation))
        out.append(self._to_str(self.run_simulation_for_sizing_periods))
        out.append(self._to_str(self.run_simulation_for_weather_file_run_periods))
        return ",".join(out)

class Building(object):
    """ Corresponds to IDD object `Building`
        Describes parameters that are used during the simulation
        of the building. There are necessary correlations between the entries for
        this object and some entries in the Site:WeatherStation and
        Site:HeightVariation objects, specifically the Terrain field.
    
    """
    internal_name = "Building"
    field_count = 8
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Building`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["North Axis"] = None
        self._data["Terrain"] = None
        self._data["Loads Convergence Tolerance Value"] = None
        self._data["Temperature Convergence Tolerance Value"] = None
        self._data["Solar Distribution"] = None
        self._data["Maximum Number of Warmup Days"] = None
        self._data["Minimum Number of Warmup Days"] = None

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
            self.north_axis = None
        else:
            self.north_axis = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.terrain = None
        else:
            self.terrain = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.loads_convergence_tolerance_value = None
        else:
            self.loads_convergence_tolerance_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_convergence_tolerance_value = None
        else:
            self.temperature_convergence_tolerance_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_distribution = None
        else:
            self.solar_distribution = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_number_of_warmup_days = None
        else:
            self.maximum_number_of_warmup_days = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_number_of_warmup_days = None
        else:
            self.minimum_number_of_warmup_days = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value="NONE"):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                Default value: NONE
                if `value` is None it will not be checked against the
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
    def north_axis(self):
        """Get north_axis

        Returns:
            float: the value of `north_axis` or None if not set
        """
        return self._data["North Axis"]

    @north_axis.setter
    def north_axis(self, value=0.0 ):
        """  Corresponds to IDD Field `north_axis`
        degrees from true North

        Args:
            value (float): value for IDD Field `north_axis`
                Units: deg
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
                                 'for field `north_axis`'.format(value))

        self._data["North Axis"] = value

    @property
    def terrain(self):
        """Get terrain

        Returns:
            str: the value of `terrain` or None if not set
        """
        return self._data["Terrain"]

    @terrain.setter
    def terrain(self, value="Suburbs"):
        """  Corresponds to IDD Field `terrain`
        Country=FlatOpenCountry | Suburbs=CountryTownsSuburbs | City=CityCenter | Ocean=body of water (5km) | Urban=Urban-Industrial-Forest

        Args:
            value (str): value for IDD Field `terrain`
                Accepted values are:
                      - Country
                      - Suburbs
                      - City
                      - Ocean
                      - Urban
                Default value: Suburbs
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terrain`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terrain`')
            vals = set()
            vals.add("Country")
            vals.add("Suburbs")
            vals.add("City")
            vals.add("Ocean")
            vals.add("Urban")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `terrain`'.format(value))

        self._data["Terrain"] = value

    @property
    def loads_convergence_tolerance_value(self):
        """Get loads_convergence_tolerance_value

        Returns:
            float: the value of `loads_convergence_tolerance_value` or None if not set
        """
        return self._data["Loads Convergence Tolerance Value"]

    @loads_convergence_tolerance_value.setter
    def loads_convergence_tolerance_value(self, value=0.04 ):
        """  Corresponds to IDD Field `loads_convergence_tolerance_value`
        Loads Convergence Tolerance Value is a fraction of load

        Args:
            value (float): value for IDD Field `loads_convergence_tolerance_value`
                Default value: 0.04
                value > 0.0
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
                                 'for field `loads_convergence_tolerance_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `loads_convergence_tolerance_value`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `loads_convergence_tolerance_value`')

        self._data["Loads Convergence Tolerance Value"] = value

    @property
    def temperature_convergence_tolerance_value(self):
        """Get temperature_convergence_tolerance_value

        Returns:
            float: the value of `temperature_convergence_tolerance_value` or None if not set
        """
        return self._data["Temperature Convergence Tolerance Value"]

    @temperature_convergence_tolerance_value.setter
    def temperature_convergence_tolerance_value(self, value=0.4 ):
        """  Corresponds to IDD Field `temperature_convergence_tolerance_value`

        Args:
            value (float): value for IDD Field `temperature_convergence_tolerance_value`
                Units: deltaC
                Default value: 0.4
                value > 0.0
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
                                 'for field `temperature_convergence_tolerance_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `temperature_convergence_tolerance_value`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `temperature_convergence_tolerance_value`')

        self._data["Temperature Convergence Tolerance Value"] = value

    @property
    def solar_distribution(self):
        """Get solar_distribution

        Returns:
            str: the value of `solar_distribution` or None if not set
        """
        return self._data["Solar Distribution"]

    @solar_distribution.setter
    def solar_distribution(self, value="FullExterior"):
        """  Corresponds to IDD Field `solar_distribution`
        MinimalShadowing | FullExterior | FullInteriorAndExterior | FullExteriorWithReflections | FullInteriorAndExteriorWithReflections

        Args:
            value (str): value for IDD Field `solar_distribution`
                Accepted values are:
                      - MinimalShadowing
                      - FullExterior
                      - FullInteriorAndExterior
                      - FullExteriorWithReflections
                      - FullInteriorAndExteriorWithReflections
                Default value: FullExterior
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `solar_distribution`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `solar_distribution`')
            vals = set()
            vals.add("MinimalShadowing")
            vals.add("FullExterior")
            vals.add("FullInteriorAndExterior")
            vals.add("FullExteriorWithReflections")
            vals.add("FullInteriorAndExteriorWithReflections")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `solar_distribution`'.format(value))

        self._data["Solar Distribution"] = value

    @property
    def maximum_number_of_warmup_days(self):
        """Get maximum_number_of_warmup_days

        Returns:
            int: the value of `maximum_number_of_warmup_days` or None if not set
        """
        return self._data["Maximum Number of Warmup Days"]

    @maximum_number_of_warmup_days.setter
    def maximum_number_of_warmup_days(self, value=25 ):
        """  Corresponds to IDD Field `maximum_number_of_warmup_days`
        EnergyPlus will only use as many warmup days as needed to reach convergence tolerance.
        This field's value should NOT be set less than 25.

        Args:
            value (int): value for IDD Field `maximum_number_of_warmup_days`
                Default value: 25
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
                                 'for field `maximum_number_of_warmup_days`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `maximum_number_of_warmup_days`')

        self._data["Maximum Number of Warmup Days"] = value

    @property
    def minimum_number_of_warmup_days(self):
        """Get minimum_number_of_warmup_days

        Returns:
            int: the value of `minimum_number_of_warmup_days` or None if not set
        """
        return self._data["Minimum Number of Warmup Days"]

    @minimum_number_of_warmup_days.setter
    def minimum_number_of_warmup_days(self, value=6 ):
        """  Corresponds to IDD Field `minimum_number_of_warmup_days`
        The minimum number of warmup days that produce enough temperature and flux history
        to start EnergyPlus simulation for all reference buildings was suggested to be 6.
        When this field is greater than the maximum warmup days defined previous field
        the maximum number of warmup days will be reset to the minimum value entered here.
        Warmup days will be set to be the value you entered when it is less than the default 6.

        Args:
            value (int): value for IDD Field `minimum_number_of_warmup_days`
                Default value: 6
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
                                 'for field `minimum_number_of_warmup_days`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `minimum_number_of_warmup_days`')

        self._data["Minimum Number of Warmup Days"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.north_axis))
        out.append(self._to_str(self.terrain))
        out.append(self._to_str(self.loads_convergence_tolerance_value))
        out.append(self._to_str(self.temperature_convergence_tolerance_value))
        out.append(self._to_str(self.solar_distribution))
        out.append(self._to_str(self.maximum_number_of_warmup_days))
        out.append(self._to_str(self.minimum_number_of_warmup_days))
        return ",".join(out)

class ShadowCalculation(object):
    """ Corresponds to IDD object `ShadowCalculation`
        This object is used to control details of the solar, shading, and daylighting models
    
    """
    internal_name = "ShadowCalculation"
    field_count = 5
    required_fields = ["Calculation Frequency"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ShadowCalculation`
        """
        self._data = OrderedDict()
        self._data["Calculation Method"] = None
        self._data["Calculation Frequency"] = None
        self._data["Maximum Figures in Shadow Overlap Calculations"] = None
        self._data["Polygon Clipping Algorithm"] = None
        self._data["Sky Diffuse Modeling Algorithm"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.calculation_method = None
        else:
            self.calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.calculation_frequency = None
        else:
            self.calculation_frequency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_figures_in_shadow_overlap_calculations = None
        else:
            self.maximum_figures_in_shadow_overlap_calculations = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.polygon_clipping_algorithm = None
        else:
            self.polygon_clipping_algorithm = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sky_diffuse_modeling_algorithm = None
        else:
            self.sky_diffuse_modeling_algorithm = vals[i]
        i += 1

    @property
    def calculation_method(self):
        """Get calculation_method

        Returns:
            str: the value of `calculation_method` or None if not set
        """
        return self._data["Calculation Method"]

    @calculation_method.setter
    def calculation_method(self, value="AverageOverDaysInFrequency"):
        """  Corresponds to IDD Field `calculation_method`
        choose calculation method. note that TimestepFrequency is only needed for certain cases
        and can increase execution time significantly.

        Args:
            value (str): value for IDD Field `calculation_method`
                Accepted values are:
                      - AverageOverDaysInFrequency
                      - TimestepFrequency
                Default value: AverageOverDaysInFrequency
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `calculation_method`')
            vals = set()
            vals.add("AverageOverDaysInFrequency")
            vals.add("TimestepFrequency")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `calculation_method`'.format(value))

        self._data["Calculation Method"] = value

    @property
    def calculation_frequency(self):
        """Get calculation_frequency

        Returns:
            int: the value of `calculation_frequency` or None if not set
        """
        return self._data["Calculation Frequency"]

    @calculation_frequency.setter
    def calculation_frequency(self, value=20 ):
        """  Corresponds to IDD Field `calculation_frequency`
        enter number of days
        this field is only used if the previous field is set to AverageOverDaysInFrequency
        0=Use Default Periodic Calculation|<else> calculate every <value> day
        only really applicable to RunPeriods
        warning issued if >31

        Args:
            value (int): value for IDD Field `calculation_frequency`
                Default value: 20
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
                                 'for field `calculation_frequency`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `calculation_frequency`')

        self._data["Calculation Frequency"] = value

    @property
    def maximum_figures_in_shadow_overlap_calculations(self):
        """Get maximum_figures_in_shadow_overlap_calculations

        Returns:
            int: the value of `maximum_figures_in_shadow_overlap_calculations` or None if not set
        """
        return self._data["Maximum Figures in Shadow Overlap Calculations"]

    @maximum_figures_in_shadow_overlap_calculations.setter
    def maximum_figures_in_shadow_overlap_calculations(self, value=15000 ):
        """  Corresponds to IDD Field `maximum_figures_in_shadow_overlap_calculations`
        Number of allowable figures in shadow overlap calculations

        Args:
            value (int): value for IDD Field `maximum_figures_in_shadow_overlap_calculations`
                Default value: 15000
                value >= 200
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
                                 'for field `maximum_figures_in_shadow_overlap_calculations`'.format(value))
            if value < 200:
                raise ValueError('value need to be greater or equal 200 '
                                 'for field `maximum_figures_in_shadow_overlap_calculations`')

        self._data["Maximum Figures in Shadow Overlap Calculations"] = value

    @property
    def polygon_clipping_algorithm(self):
        """Get polygon_clipping_algorithm

        Returns:
            str: the value of `polygon_clipping_algorithm` or None if not set
        """
        return self._data["Polygon Clipping Algorithm"]

    @polygon_clipping_algorithm.setter
    def polygon_clipping_algorithm(self, value=None):
        """  Corresponds to IDD Field `polygon_clipping_algorithm`
        Advanced Feature.  Internal default is SutherlandHodgman
        Refer to InputOutput Reference and Engineering Reference for more information

        Args:
            value (str): value for IDD Field `polygon_clipping_algorithm`
                Accepted values are:
                      - ConvexWeilerAtherton
                      - SutherlandHodgman
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `polygon_clipping_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `polygon_clipping_algorithm`')
            vals = set()
            vals.add("ConvexWeilerAtherton")
            vals.add("SutherlandHodgman")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `polygon_clipping_algorithm`'.format(value))

        self._data["Polygon Clipping Algorithm"] = value

    @property
    def sky_diffuse_modeling_algorithm(self):
        """Get sky_diffuse_modeling_algorithm

        Returns:
            str: the value of `sky_diffuse_modeling_algorithm` or None if not set
        """
        return self._data["Sky Diffuse Modeling Algorithm"]

    @sky_diffuse_modeling_algorithm.setter
    def sky_diffuse_modeling_algorithm(self, value=None):
        """  Corresponds to IDD Field `sky_diffuse_modeling_algorithm`
        Advanced Feature.  Internal default is SimpleSkyDiffuseModeling
        If you have shading elements that change transmittance over the
        year, you may wish to choose the detailed method.
        Refer to InputOutput Reference and Engineering Reference for more information

        Args:
            value (str): value for IDD Field `sky_diffuse_modeling_algorithm`
                Accepted values are:
                      - SimpleSkyDiffuseModeling
                      - DetailedSkyDiffuseModeling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `sky_diffuse_modeling_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sky_diffuse_modeling_algorithm`')
            vals = set()
            vals.add("SimpleSkyDiffuseModeling")
            vals.add("DetailedSkyDiffuseModeling")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `sky_diffuse_modeling_algorithm`'.format(value))

        self._data["Sky Diffuse Modeling Algorithm"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.calculation_method))
        out.append(self._to_str(self.calculation_frequency))
        out.append(self._to_str(self.maximum_figures_in_shadow_overlap_calculations))
        out.append(self._to_str(self.polygon_clipping_algorithm))
        out.append(self._to_str(self.sky_diffuse_modeling_algorithm))
        return ",".join(out)

class SurfaceConvectionAlgorithmInside(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside`
        Default indoor surface heat transfer convection algorithm to be used for all zones
    
    """
    internal_name = "SurfaceConvectionAlgorithm:Inside"
    field_count = 1
    required_fields = ["Algorithm"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceConvectionAlgorithm:Inside`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="TARP"):
        """  Corresponds to IDD Field `algorithm`
        Simple = constant value natural convection (ASHRAE)
        TARP = variable natural convection based on temperature difference (ASHRAE, Walton)
        CeilingDiffuser = ACH-based forced and mixed convection correlations
        for ceiling diffuser configuration with simple natural convection limit
        AdaptiveConvectionAlgorithm = dynamic selection of convection models based on conditions

        Args:
            value (str): value for IDD Field `algorithm`
                Accepted values are:
                      - Simple
                      - TARP
                      - CeilingDiffuser
                      - AdaptiveConvectionAlgorithm
                Default value: TARP
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("Simple")
            vals.add("TARP")
            vals.add("CeilingDiffuser")
            vals.add("AdaptiveConvectionAlgorithm")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.algorithm))
        return ",".join(out)

class SurfaceConvectionAlgorithmOutside(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside`
        Default outside surface heat transfer convection algorithm to be used for all zones
    
    """
    internal_name = "SurfaceConvectionAlgorithm:Outside"
    field_count = 1
    required_fields = ["Algorithm"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceConvectionAlgorithm:Outside`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="DOE-2"):
        """  Corresponds to IDD Field `algorithm`
        SimpleCombined = Combined radiation and convection coefficient using simple ASHRAE model
        TARP = correlation from models developed by ASHRAE, Walton, and Sparrow et. al.
        MoWiTT = correlation from measurements by Klems and Yazdanian for smooth surfaces
        DOE-2 = correlation from measurements by Klems and Yazdanian for rough surfaces
        AdaptiveConvectionAlgorithm = dynamic selection of correlations based on conditions

        Args:
            value (str): value for IDD Field `algorithm`
                Accepted values are:
                      - SimpleCombined
                      - TARP
                      - MoWiTT
                      - DOE-2
                      - AdaptiveConvectionAlgorithm
                Default value: DOE-2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("SimpleCombined")
            vals.add("TARP")
            vals.add("MoWiTT")
            vals.add("DOE-2")
            vals.add("AdaptiveConvectionAlgorithm")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.algorithm))
        return ",".join(out)

class HeatBalanceAlgorithm(object):
    """ Corresponds to IDD object `HeatBalanceAlgorithm`
        Determines which Heat Balance Algorithm will be used ie.
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: ConductionFiniteDifferenceSimplified
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    
    """
    internal_name = "HeatBalanceAlgorithm"
    field_count = 4
    required_fields = ["Algorithm"]

    def __init__(self):
        """ Init data dictionary object for IDD  `HeatBalanceAlgorithm`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None
        self._data["Surface Temperature Upper Limit"] = None
        self._data["Minimum Surface Convection Heat Transfer Coefficient Value"] = None
        self._data["Maximum Surface Convection Heat Transfer Coefficient Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_temperature_upper_limit = None
        else:
            self.surface_temperature_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_surface_convection_heat_transfer_coefficient_value = None
        else:
            self.minimum_surface_convection_heat_transfer_coefficient_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_surface_convection_heat_transfer_coefficient_value = None
        else:
            self.maximum_surface_convection_heat_transfer_coefficient_value = vals[i]
        i += 1

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """  Corresponds to IDD Field `algorithm`

        Args:
            value (str): value for IDD Field `algorithm`
                Accepted values are:
                      - ConductionTransferFunction
                      - MoisturePenetrationDepthConductionTransferFunction
                      - ConductionFiniteDifference
                      - CombinedHeatAndMoistureFiniteElement
                Default value: ConductionTransferFunction
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("ConductionTransferFunction")
            vals.add("MoisturePenetrationDepthConductionTransferFunction")
            vals.add("ConductionFiniteDifference")
            vals.add("CombinedHeatAndMoistureFiniteElement")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

    @property
    def surface_temperature_upper_limit(self):
        """Get surface_temperature_upper_limit

        Returns:
            float: the value of `surface_temperature_upper_limit` or None if not set
        """
        return self._data["Surface Temperature Upper Limit"]

    @surface_temperature_upper_limit.setter
    def surface_temperature_upper_limit(self, value=200.0 ):
        """  Corresponds to IDD Field `surface_temperature_upper_limit`

        Args:
            value (float): value for IDD Field `surface_temperature_upper_limit`
                Units: C
                Default value: 200.0
                value >= 200.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `surface_temperature_upper_limit`'.format(value))
            if value < 200.0:
                raise ValueError('value need to be greater or equal 200.0 '
                                 'for field `surface_temperature_upper_limit`')

        self._data["Surface Temperature Upper Limit"] = value

    @property
    def minimum_surface_convection_heat_transfer_coefficient_value(self):
        """Get minimum_surface_convection_heat_transfer_coefficient_value

        Returns:
            float: the value of `minimum_surface_convection_heat_transfer_coefficient_value` or None if not set
        """
        return self._data["Minimum Surface Convection Heat Transfer Coefficient Value"]

    @minimum_surface_convection_heat_transfer_coefficient_value.setter
    def minimum_surface_convection_heat_transfer_coefficient_value(self, value=0.1 ):
        """  Corresponds to IDD Field `minimum_surface_convection_heat_transfer_coefficient_value`

        Args:
            value (float): value for IDD Field `minimum_surface_convection_heat_transfer_coefficient_value`
                Units: W/m2-K
                Default value: 0.1
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
                                 'for field `minimum_surface_convection_heat_transfer_coefficient_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_surface_convection_heat_transfer_coefficient_value`')

        self._data["Minimum Surface Convection Heat Transfer Coefficient Value"] = value

    @property
    def maximum_surface_convection_heat_transfer_coefficient_value(self):
        """Get maximum_surface_convection_heat_transfer_coefficient_value

        Returns:
            float: the value of `maximum_surface_convection_heat_transfer_coefficient_value` or None if not set
        """
        return self._data["Maximum Surface Convection Heat Transfer Coefficient Value"]

    @maximum_surface_convection_heat_transfer_coefficient_value.setter
    def maximum_surface_convection_heat_transfer_coefficient_value(self, value=1000.0 ):
        """  Corresponds to IDD Field `maximum_surface_convection_heat_transfer_coefficient_value`

        Args:
            value (float): value for IDD Field `maximum_surface_convection_heat_transfer_coefficient_value`
                Units: W/m2-K
                Default value: 1000.0
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_surface_convection_heat_transfer_coefficient_value`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `maximum_surface_convection_heat_transfer_coefficient_value`')

        self._data["Maximum Surface Convection Heat Transfer Coefficient Value"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.algorithm))
        out.append(self._to_str(self.surface_temperature_upper_limit))
        out.append(self._to_str(self.minimum_surface_convection_heat_transfer_coefficient_value))
        out.append(self._to_str(self.maximum_surface_convection_heat_transfer_coefficient_value))
        return ",".join(out)

class HeatBalanceSettingsConductionFiniteDifference(object):
    """ Corresponds to IDD object `HeatBalanceSettings:ConductionFiniteDifference`
        Determines settings for the Conduction Finite Difference
        algorithm for surface heat transfer modeling.
    
    """
    internal_name = "HeatBalanceSettings:ConductionFiniteDifference"
    field_count = 4
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `HeatBalanceSettings:ConductionFiniteDifference`
        """
        self._data = OrderedDict()
        self._data["Difference Scheme"] = None
        self._data["Space Discretization Constant"] = None
        self._data["Relaxation Factor"] = None
        self._data["Inside Face Surface Temperature Convergence Criteria"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.difference_scheme = None
        else:
            self.difference_scheme = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.space_discretization_constant = None
        else:
            self.space_discretization_constant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relaxation_factor = None
        else:
            self.relaxation_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inside_face_surface_temperature_convergence_criteria = None
        else:
            self.inside_face_surface_temperature_convergence_criteria = vals[i]
        i += 1

    @property
    def difference_scheme(self):
        """Get difference_scheme

        Returns:
            str: the value of `difference_scheme` or None if not set
        """
        return self._data["Difference Scheme"]

    @difference_scheme.setter
    def difference_scheme(self, value="FullyImplicitFirstOrder"):
        """  Corresponds to IDD Field `difference_scheme`

        Args:
            value (str): value for IDD Field `difference_scheme`
                Accepted values are:
                      - CrankNicholsonSecondOrder
                      - FullyImplicitFirstOrder
                Default value: FullyImplicitFirstOrder
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `difference_scheme`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `difference_scheme`')
            vals = set()
            vals.add("CrankNicholsonSecondOrder")
            vals.add("FullyImplicitFirstOrder")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `difference_scheme`'.format(value))

        self._data["Difference Scheme"] = value

    @property
    def space_discretization_constant(self):
        """Get space_discretization_constant

        Returns:
            float: the value of `space_discretization_constant` or None if not set
        """
        return self._data["Space Discretization Constant"]

    @space_discretization_constant.setter
    def space_discretization_constant(self, value=3.0 ):
        """  Corresponds to IDD Field `space_discretization_constant`
        increase or decrease number of nodes

        Args:
            value (float): value for IDD Field `space_discretization_constant`
                Default value: 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `space_discretization_constant`'.format(value))

        self._data["Space Discretization Constant"] = value

    @property
    def relaxation_factor(self):
        """Get relaxation_factor

        Returns:
            float: the value of `relaxation_factor` or None if not set
        """
        return self._data["Relaxation Factor"]

    @relaxation_factor.setter
    def relaxation_factor(self, value=1.0 ):
        """  Corresponds to IDD Field `relaxation_factor`

        Args:
            value (float): value for IDD Field `relaxation_factor`
                Default value: 1.0
                value >= 0.01
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
                                 'for field `relaxation_factor`'.format(value))
            if value < 0.01:
                raise ValueError('value need to be greater or equal 0.01 '
                                 'for field `relaxation_factor`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relaxation_factor`')

        self._data["Relaxation Factor"] = value

    @property
    def inside_face_surface_temperature_convergence_criteria(self):
        """Get inside_face_surface_temperature_convergence_criteria

        Returns:
            float: the value of `inside_face_surface_temperature_convergence_criteria` or None if not set
        """
        return self._data["Inside Face Surface Temperature Convergence Criteria"]

    @inside_face_surface_temperature_convergence_criteria.setter
    def inside_face_surface_temperature_convergence_criteria(self, value=0.002 ):
        """  Corresponds to IDD Field `inside_face_surface_temperature_convergence_criteria`

        Args:
            value (float): value for IDD Field `inside_face_surface_temperature_convergence_criteria`
                Default value: 0.002
                value >= 1e-07
                value <= 0.01
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `inside_face_surface_temperature_convergence_criteria`'.format(value))
            if value < 1e-07:
                raise ValueError('value need to be greater or equal 1e-07 '
                                 'for field `inside_face_surface_temperature_convergence_criteria`')
            if value > 0.01:
                raise ValueError('value need to be smaller 0.01 '
                                 'for field `inside_face_surface_temperature_convergence_criteria`')

        self._data["Inside Face Surface Temperature Convergence Criteria"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.difference_scheme))
        out.append(self._to_str(self.space_discretization_constant))
        out.append(self._to_str(self.relaxation_factor))
        out.append(self._to_str(self.inside_face_surface_temperature_convergence_criteria))
        return ",".join(out)

class ZoneAirHeatBalanceAlgorithm(object):
    """ Corresponds to IDD object `ZoneAirHeatBalanceAlgorithm`
        Determines which algorithm will be used to solve the zone air heat balance.
    
    """
    internal_name = "ZoneAirHeatBalanceAlgorithm"
    field_count = 1
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneAirHeatBalanceAlgorithm`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ThirdOrderBackwardDifference"):
        """  Corresponds to IDD Field `algorithm`

        Args:
            value (str): value for IDD Field `algorithm`
                Accepted values are:
                      - ThirdOrderBackwardDifference
                      - AnalyticalSolution
                      - EulerMethod
                Default value: ThirdOrderBackwardDifference
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("ThirdOrderBackwardDifference")
            vals.add("AnalyticalSolution")
            vals.add("EulerMethod")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.algorithm))
        return ",".join(out)

class ZoneAirContaminantBalance(object):
    """ Corresponds to IDD object `ZoneAirContaminantBalance`
        Determines which contaminant concentration will be simulates.
    
    """
    internal_name = "ZoneAirContaminantBalance"
    field_count = 4
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneAirContaminantBalance`
        """
        self._data = OrderedDict()
        self._data["Carbon Dioxide Concentration"] = None
        self._data["Outdoor Carbon Dioxide Schedule Name"] = None
        self._data["Generic Contaminant Concentration"] = None
        self._data["Outdoor Generic Contaminant Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.carbon_dioxide_concentration = None
        else:
            self.carbon_dioxide_concentration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_carbon_dioxide_schedule_name = None
        else:
            self.outdoor_carbon_dioxide_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generic_contaminant_concentration = None
        else:
            self.generic_contaminant_concentration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_generic_contaminant_schedule_name = None
        else:
            self.outdoor_generic_contaminant_schedule_name = vals[i]
        i += 1

    @property
    def carbon_dioxide_concentration(self):
        """Get carbon_dioxide_concentration

        Returns:
            str: the value of `carbon_dioxide_concentration` or None if not set
        """
        return self._data["Carbon Dioxide Concentration"]

    @carbon_dioxide_concentration.setter
    def carbon_dioxide_concentration(self, value="No"):
        """  Corresponds to IDD Field `carbon_dioxide_concentration`
        If Yes, CO2 simulation will be performed.

        Args:
            value (str): value for IDD Field `carbon_dioxide_concentration`
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
                                 'for field `carbon_dioxide_concentration`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `carbon_dioxide_concentration`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `carbon_dioxide_concentration`'.format(value))

        self._data["Carbon Dioxide Concentration"] = value

    @property
    def outdoor_carbon_dioxide_schedule_name(self):
        """Get outdoor_carbon_dioxide_schedule_name

        Returns:
            str: the value of `outdoor_carbon_dioxide_schedule_name` or None if not set
        """
        return self._data["Outdoor Carbon Dioxide Schedule Name"]

    @outdoor_carbon_dioxide_schedule_name.setter
    def outdoor_carbon_dioxide_schedule_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_carbon_dioxide_schedule_name`
        Schedule values should be in parts per million (ppm)

        Args:
            value (str): value for IDD Field `outdoor_carbon_dioxide_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_carbon_dioxide_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_carbon_dioxide_schedule_name`')

        self._data["Outdoor Carbon Dioxide Schedule Name"] = value

    @property
    def generic_contaminant_concentration(self):
        """Get generic_contaminant_concentration

        Returns:
            str: the value of `generic_contaminant_concentration` or None if not set
        """
        return self._data["Generic Contaminant Concentration"]

    @generic_contaminant_concentration.setter
    def generic_contaminant_concentration(self, value="No"):
        """  Corresponds to IDD Field `generic_contaminant_concentration`
        If Yes, generic contaminant simulation will be performed.

        Args:
            value (str): value for IDD Field `generic_contaminant_concentration`
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
                                 'for field `generic_contaminant_concentration`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generic_contaminant_concentration`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generic_contaminant_concentration`'.format(value))

        self._data["Generic Contaminant Concentration"] = value

    @property
    def outdoor_generic_contaminant_schedule_name(self):
        """Get outdoor_generic_contaminant_schedule_name

        Returns:
            str: the value of `outdoor_generic_contaminant_schedule_name` or None if not set
        """
        return self._data["Outdoor Generic Contaminant Schedule Name"]

    @outdoor_generic_contaminant_schedule_name.setter
    def outdoor_generic_contaminant_schedule_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_generic_contaminant_schedule_name`
        Schedule values should be generic contaminant concentration in parts per
        million (ppm)

        Args:
            value (str): value for IDD Field `outdoor_generic_contaminant_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_generic_contaminant_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_generic_contaminant_schedule_name`')

        self._data["Outdoor Generic Contaminant Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.carbon_dioxide_concentration))
        out.append(self._to_str(self.outdoor_carbon_dioxide_schedule_name))
        out.append(self._to_str(self.generic_contaminant_concentration))
        out.append(self._to_str(self.outdoor_generic_contaminant_schedule_name))
        return ",".join(out)

class ZoneAirMassFlowConservation(object):
    """ Corresponds to IDD object `ZoneAirMassFlowConservation`
        Enforces the zone air mass flow balance by adjusting zone mixing object flow rates.
        The infiltration object mass flow rate may also be adjusted or may add infiltration
        air flow to the base infiltration air flow for source zones only.
    
    """
    internal_name = "ZoneAirMassFlowConservation"
    field_count = 2
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneAirMassFlowConservation`
        """
        self._data = OrderedDict()
        self._data["Adjust Zone Mixing For Zone Air Mass Flow Balance"] = None
        self._data["Source Zone Infiltration Treatment"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.adjust_zone_mixing_for_zone_air_mass_flow_balance = None
        else:
            self.adjust_zone_mixing_for_zone_air_mass_flow_balance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_zone_infiltration_treatment = None
        else:
            self.source_zone_infiltration_treatment = vals[i]
        i += 1

    @property
    def adjust_zone_mixing_for_zone_air_mass_flow_balance(self):
        """Get adjust_zone_mixing_for_zone_air_mass_flow_balance

        Returns:
            str: the value of `adjust_zone_mixing_for_zone_air_mass_flow_balance` or None if not set
        """
        return self._data["Adjust Zone Mixing For Zone Air Mass Flow Balance"]

    @adjust_zone_mixing_for_zone_air_mass_flow_balance.setter
    def adjust_zone_mixing_for_zone_air_mass_flow_balance(self, value="No"):
        """  Corresponds to IDD Field `adjust_zone_mixing_for_zone_air_mass_flow_balance`
        If Yes, Zone mixing object flow rates are adjusted to balance the zone air mass flow
        and additional infiltration air flow may be added if required in order to balance the
        zone air mass flow.
        This optional choice input field allows users triggering the zone air mass flow
        balance calculation when desired. This global object has two choice KEYs: Yes and
        No. If this input field is specified as Yes, then EnergyPlus attempts to enforce
        the zone air mass flow conservation, or else if it is specified as No, then EnergyPlus
        calculation defaults to zone air mass flow balance that does not include zone mixing
        objects and that assumes self-balanced simple flow objects per the default procedure,
        which may not necessarily enforce zone mass conservation unless the user specified
        a balanced flow to begin with. Mass conservation is enforced both for the receiving
        and source zones if there is at least one mixing object defined. The default input
        is No. (Note that No input may also results in balanced flow depending on the
        system specified).

        Args:
            value (str): value for IDD Field `adjust_zone_mixing_for_zone_air_mass_flow_balance`
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
                                 'for field `adjust_zone_mixing_for_zone_air_mass_flow_balance`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `adjust_zone_mixing_for_zone_air_mass_flow_balance`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `adjust_zone_mixing_for_zone_air_mass_flow_balance`'.format(value))

        self._data["Adjust Zone Mixing For Zone Air Mass Flow Balance"] = value

    @property
    def source_zone_infiltration_treatment(self):
        """Get source_zone_infiltration_treatment

        Returns:
            str: the value of `source_zone_infiltration_treatment` or None if not set
        """
        return self._data["Source Zone Infiltration Treatment"]

    @source_zone_infiltration_treatment.setter
    def source_zone_infiltration_treatment(self, value="AddInfiltrationFlow"):
        """  Corresponds to IDD Field `source_zone_infiltration_treatment`
        This input field allows user to choose how zone infiltration flow is treated during
        the zone air mass flow balance calculation.
        It has two choice KEYs: AddInfiltrationFlow and AdjustInfiltrationFlow.  If this
        input is specified as AddInfiltrationFlow, then energy plus adds infiltration air
        mass flow on top of the base flow, which is calculated using the infiltration object
        user inputs, in order to balance the zone air mass flow.  The additional infiltration
        air mass flow is not self-balanced.  If this input is specified as
        AdjustInfiltrationFlow, then energy plus may adjust the base flow calculated using
        the infiltration object user inputs in order to balance the zone air mass flow. If it
        is not required to adjust the base infiltration air flow calculated from the user
        specified infiltration object inputs, then the base infiltration air mass flow
        is assumed self-balanced. If the above input field specified as "No", then this input
        field has no impact on the simulation.

        Args:
            value (str): value for IDD Field `source_zone_infiltration_treatment`
                Accepted values are:
                      - AddInfiltrationFlow
                      - AdjustInfiltrationFlow
                Default value: AddInfiltrationFlow
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_zone_infiltration_treatment`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_zone_infiltration_treatment`')
            vals = set()
            vals.add("AddInfiltrationFlow")
            vals.add("AdjustInfiltrationFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `source_zone_infiltration_treatment`'.format(value))

        self._data["Source Zone Infiltration Treatment"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.adjust_zone_mixing_for_zone_air_mass_flow_balance))
        out.append(self._to_str(self.source_zone_infiltration_treatment))
        return ",".join(out)

class ZoneCapacitanceMultiplierResearchSpecial(object):
    """ Corresponds to IDD object `ZoneCapacitanceMultiplier:ResearchSpecial`
        Multiplier altering the relative capacitance of the air compared to an empty zone
    
    """
    internal_name = "ZoneCapacitanceMultiplier:ResearchSpecial"
    field_count = 4
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneCapacitanceMultiplier:ResearchSpecial`
        """
        self._data = OrderedDict()
        self._data["Temperature Capacity Multiplier"] = None
        self._data["Humidity Capacity Multiplier"] = None
        self._data["Carbon Dioxide Capacity Multiplier"] = None
        self._data["Generic Contaminant Capacity Multiplier"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.temperature_capacity_multiplier = None
        else:
            self.temperature_capacity_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_capacity_multiplier = None
        else:
            self.humidity_capacity_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.carbon_dioxide_capacity_multiplier = None
        else:
            self.carbon_dioxide_capacity_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generic_contaminant_capacity_multiplier = None
        else:
            self.generic_contaminant_capacity_multiplier = vals[i]
        i += 1

    @property
    def temperature_capacity_multiplier(self):
        """Get temperature_capacity_multiplier

        Returns:
            float: the value of `temperature_capacity_multiplier` or None if not set
        """
        return self._data["Temperature Capacity Multiplier"]

    @temperature_capacity_multiplier.setter
    def temperature_capacity_multiplier(self, value=1.0 ):
        """  Corresponds to IDD Field `temperature_capacity_multiplier`
        Used to alter the capacitance of zone air with respect to heat or temperature

        Args:
            value (float): value for IDD Field `temperature_capacity_multiplier`
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
                                 'for field `temperature_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `temperature_capacity_multiplier`')

        self._data["Temperature Capacity Multiplier"] = value

    @property
    def humidity_capacity_multiplier(self):
        """Get humidity_capacity_multiplier

        Returns:
            float: the value of `humidity_capacity_multiplier` or None if not set
        """
        return self._data["Humidity Capacity Multiplier"]

    @humidity_capacity_multiplier.setter
    def humidity_capacity_multiplier(self, value=1.0 ):
        """  Corresponds to IDD Field `humidity_capacity_multiplier`
        Used to alter the capacitance of zone air with respect to moisture or humidity ratio

        Args:
            value (float): value for IDD Field `humidity_capacity_multiplier`
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
                                 'for field `humidity_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `humidity_capacity_multiplier`')

        self._data["Humidity Capacity Multiplier"] = value

    @property
    def carbon_dioxide_capacity_multiplier(self):
        """Get carbon_dioxide_capacity_multiplier

        Returns:
            float: the value of `carbon_dioxide_capacity_multiplier` or None if not set
        """
        return self._data["Carbon Dioxide Capacity Multiplier"]

    @carbon_dioxide_capacity_multiplier.setter
    def carbon_dioxide_capacity_multiplier(self, value=1.0 ):
        """  Corresponds to IDD Field `carbon_dioxide_capacity_multiplier`
        Used to alter the capacitance of zone air with respect to zone air carbob dioxide concentration

        Args:
            value (float): value for IDD Field `carbon_dioxide_capacity_multiplier`
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
                                 'for field `carbon_dioxide_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `carbon_dioxide_capacity_multiplier`')

        self._data["Carbon Dioxide Capacity Multiplier"] = value

    @property
    def generic_contaminant_capacity_multiplier(self):
        """Get generic_contaminant_capacity_multiplier

        Returns:
            float: the value of `generic_contaminant_capacity_multiplier` or None if not set
        """
        return self._data["Generic Contaminant Capacity Multiplier"]

    @generic_contaminant_capacity_multiplier.setter
    def generic_contaminant_capacity_multiplier(self, value=1.0 ):
        """  Corresponds to IDD Field `generic_contaminant_capacity_multiplier`
        Used to alter the capacitance of zone air with respect to zone air generic contaminant concentration

        Args:
            value (float): value for IDD Field `generic_contaminant_capacity_multiplier`
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
                                 'for field `generic_contaminant_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `generic_contaminant_capacity_multiplier`')

        self._data["Generic Contaminant Capacity Multiplier"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.temperature_capacity_multiplier))
        out.append(self._to_str(self.humidity_capacity_multiplier))
        out.append(self._to_str(self.carbon_dioxide_capacity_multiplier))
        out.append(self._to_str(self.generic_contaminant_capacity_multiplier))
        return ",".join(out)

class Timestep(object):
    """ Corresponds to IDD object `Timestep`
        Specifies the "basic" timestep for the simulation. The
        value entered here is also known as the Zone Timestep.  This is used in
        the Zone Heat Balance Model calculation as the driving timestep for heat
        transfer and load calculations.
    
    """
    internal_name = "Timestep"
    field_count = 1
    required_fields = ["Number of Timesteps per Hour"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Timestep`
        """
        self._data = OrderedDict()
        self._data["Number of Timesteps per Hour"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.number_of_timesteps_per_hour = None
        else:
            self.number_of_timesteps_per_hour = vals[i]
        i += 1

    @property
    def number_of_timesteps_per_hour(self):
        """Get number_of_timesteps_per_hour

        Returns:
            int: the value of `number_of_timesteps_per_hour` or None if not set
        """
        return self._data["Number of Timesteps per Hour"]

    @number_of_timesteps_per_hour.setter
    def number_of_timesteps_per_hour(self, value=6 ):
        """  Corresponds to IDD Field `number_of_timesteps_per_hour`
        Number in hour: normal validity 4 to 60: 6 suggested
        Must be evenly divisible into 60
        Allowable values include 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60
        Normal 6 is mimimum as lower values may cause inaccuracies
        A minimum value of 20 is suggested for both ConductionFiniteDifference
        and CombinedHeatAndMoistureFiniteElement surface heat balance alogorithms
        A minimum of 12 is suggested for simulations involving a Vegetated Roof (Material:RoofVegetation).

        Args:
            value (int): value for IDD Field `number_of_timesteps_per_hour`
                Default value: 6
                value >= 1
                value <= 60
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
                                 'for field `number_of_timesteps_per_hour`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_timesteps_per_hour`')
            if value > 60:
                raise ValueError('value need to be smaller 60 '
                                 'for field `number_of_timesteps_per_hour`')

        self._data["Number of Timesteps per Hour"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.number_of_timesteps_per_hour))
        return ",".join(out)

class ConvergenceLimits(object):
    """ Corresponds to IDD object `ConvergenceLimits`
        Specifies limits on HVAC system simulation timesteps and iterations.
        This item is an advanced feature that should be used only with caution.
    
    """
    internal_name = "ConvergenceLimits"
    field_count = 4
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ConvergenceLimits`
        """
        self._data = OrderedDict()
        self._data["Minimum System Timestep"] = None
        self._data["Maximum HVAC Iterations"] = None
        self._data["Minimum Plant Iterations"] = None
        self._data["Maximum Plant Iterations"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.minimum_system_timestep = None
        else:
            self.minimum_system_timestep = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_hvac_iterations = None
        else:
            self.maximum_hvac_iterations = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_plant_iterations = None
        else:
            self.minimum_plant_iterations = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_plant_iterations = None
        else:
            self.maximum_plant_iterations = vals[i]
        i += 1

    @property
    def minimum_system_timestep(self):
        """Get minimum_system_timestep

        Returns:
            int: the value of `minimum_system_timestep` or None if not set
        """
        return self._data["Minimum System Timestep"]

    @minimum_system_timestep.setter
    def minimum_system_timestep(self, value=None):
        """  Corresponds to IDD Field `minimum_system_timestep`
        0 sets the minimum to the zone timestep (ref: Timestep)
        1 is normal (ratchet down to 1 minute)
        setting greater than zone timestep (in minutes) will effectively set to zone timestep

        Args:
            value (int): value for IDD Field `minimum_system_timestep`
                Units: minutes
                value >= 0
                value <= 60
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
                                 'for field `minimum_system_timestep`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `minimum_system_timestep`')
            if value > 60:
                raise ValueError('value need to be smaller 60 '
                                 'for field `minimum_system_timestep`')

        self._data["Minimum System Timestep"] = value

    @property
    def maximum_hvac_iterations(self):
        """Get maximum_hvac_iterations

        Returns:
            int: the value of `maximum_hvac_iterations` or None if not set
        """
        return self._data["Maximum HVAC Iterations"]

    @maximum_hvac_iterations.setter
    def maximum_hvac_iterations(self, value=20 ):
        """  Corresponds to IDD Field `maximum_hvac_iterations`

        Args:
            value (int): value for IDD Field `maximum_hvac_iterations`
                Default value: 20
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
                                 'for field `maximum_hvac_iterations`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `maximum_hvac_iterations`')

        self._data["Maximum HVAC Iterations"] = value

    @property
    def minimum_plant_iterations(self):
        """Get minimum_plant_iterations

        Returns:
            int: the value of `minimum_plant_iterations` or None if not set
        """
        return self._data["Minimum Plant Iterations"]

    @minimum_plant_iterations.setter
    def minimum_plant_iterations(self, value=2 ):
        """  Corresponds to IDD Field `minimum_plant_iterations`
        Controls the minimum number of plant system solver iterations within a single HVAC iteration
        Larger values will increase runtime but might improve solution accuracy for complicated plant systems
        Complex plants include: several interconnected loops, heat recovery, thermal load following generators, etc.

        Args:
            value (int): value for IDD Field `minimum_plant_iterations`
                Default value: 2
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
                                 'for field `minimum_plant_iterations`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `minimum_plant_iterations`')

        self._data["Minimum Plant Iterations"] = value

    @property
    def maximum_plant_iterations(self):
        """Get maximum_plant_iterations

        Returns:
            int: the value of `maximum_plant_iterations` or None if not set
        """
        return self._data["Maximum Plant Iterations"]

    @maximum_plant_iterations.setter
    def maximum_plant_iterations(self, value=8 ):
        """  Corresponds to IDD Field `maximum_plant_iterations`
        Controls the maximum number of plant system solver iterations within a single HVAC iteration
        Smaller values might decrease runtime but could decrease solution accuracy for complicated plant systems

        Args:
            value (int): value for IDD Field `maximum_plant_iterations`
                Default value: 8
                value >= 2
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
                                 'for field `maximum_plant_iterations`'.format(value))
            if value < 2:
                raise ValueError('value need to be greater or equal 2 '
                                 'for field `maximum_plant_iterations`')

        self._data["Maximum Plant Iterations"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.minimum_system_timestep))
        out.append(self._to_str(self.maximum_hvac_iterations))
        out.append(self._to_str(self.minimum_plant_iterations))
        out.append(self._to_str(self.maximum_plant_iterations))
        return ",".join(out)

class ProgramControl(object):
    """ Corresponds to IDD object `ProgramControl`
        used to support various efforts in time reduction for simulation including threading
    
    """
    internal_name = "ProgramControl"
    field_count = 1
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ProgramControl`
        """
        self._data = OrderedDict()
        self._data["Number of Threads Allowed"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.number_of_threads_allowed = None
        else:
            self.number_of_threads_allowed = vals[i]
        i += 1

    @property
    def number_of_threads_allowed(self):
        """Get number_of_threads_allowed

        Returns:
            int: the value of `number_of_threads_allowed` or None if not set
        """
        return self._data["Number of Threads Allowed"]

    @number_of_threads_allowed.setter
    def number_of_threads_allowed(self, value=None):
        """  Corresponds to IDD Field `number_of_threads_allowed`
        This is currently used only in the Interior Radiant Exchange module -- view factors on # surfaces
        if value is 0, then maximum number allowed will be used.

        Args:
            value (int): value for IDD Field `number_of_threads_allowed`
                value >= 0
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
                                 'for field `number_of_threads_allowed`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `number_of_threads_allowed`')

        self._data["Number of Threads Allowed"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.number_of_threads_allowed))
        return ",".join(out)