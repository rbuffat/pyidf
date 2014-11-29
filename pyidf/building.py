from collections import OrderedDict

class Building(object):
    """ Corresponds to IDD object `Building`
        Describes parameters that are used during the simulation
        of the building. There are necessary correlations between the entries for
        this object and some entries in the Site:WeatherStation and
        Site:HeightVariation objects, specifically the Terrain field.
    """
    internal_name = "Building"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Building`
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
                Unit: deg
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
                Unit: deltaC
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