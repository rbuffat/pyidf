from collections import OrderedDict

class EnvironmentalImpactFactors(object):
    """ Corresponds to IDD object `EnvironmentalImpactFactors`
        Used to help convert district and ideal energy use to a fuel type and provide total carbon equivalent with coefficients
        Also used in Source=>Site conversions.
    """
    internal_name = "EnvironmentalImpactFactors"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `EnvironmentalImpactFactors`
        """
        self._data = OrderedDict()
        self._data["District Heating Efficiency"] = None
        self._data["District Cooling COP"] = None
        self._data["Steam Conversion Efficiency"] = None
        self._data["Total Carbon Equivalent Emission Factor From N2O"] = None
        self._data["Total Carbon Equivalent Emission Factor From CH4"] = None
        self._data["Total Carbon Equivalent Emission Factor From CO2"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.district_heating_efficiency = None
        else:
            self.district_heating_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.district_cooling_cop = None
        else:
            self.district_cooling_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.steam_conversion_efficiency = None
        else:
            self.steam_conversion_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.total_carbon_equivalent_emission_factor_from_n2o = None
        else:
            self.total_carbon_equivalent_emission_factor_from_n2o = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.total_carbon_equivalent_emission_factor_from_ch4 = None
        else:
            self.total_carbon_equivalent_emission_factor_from_ch4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.total_carbon_equivalent_emission_factor_from_co2 = None
        else:
            self.total_carbon_equivalent_emission_factor_from_co2 = vals[i]
        i += 1

    @property
    def district_heating_efficiency(self):
        """Get district_heating_efficiency

        Returns:
            float: the value of `district_heating_efficiency` or None if not set
        """
        return self._data["District Heating Efficiency"]

    @district_heating_efficiency.setter
    def district_heating_efficiency(self, value=0.3 ):
        """  Corresponds to IDD Field `district_heating_efficiency`
        District heating efficiency used when converted to natural gas

        Args:
            value (float): value for IDD Field `district_heating_efficiency`
                Default value: 0.3
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
                                 'for field `district_heating_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `district_heating_efficiency`')

        self._data["District Heating Efficiency"] = value

    @property
    def district_cooling_cop(self):
        """Get district_cooling_cop

        Returns:
            float: the value of `district_cooling_cop` or None if not set
        """
        return self._data["District Cooling COP"]

    @district_cooling_cop.setter
    def district_cooling_cop(self, value=3.0 ):
        """  Corresponds to IDD Field `district_cooling_cop`
        District cooling COP used when converted to electricity

        Args:
            value (float): value for IDD Field `district_cooling_cop`
                Unit: W/W
                Default value: 3.0
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
                                 'for field `district_cooling_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `district_cooling_cop`')

        self._data["District Cooling COP"] = value

    @property
    def steam_conversion_efficiency(self):
        """Get steam_conversion_efficiency

        Returns:
            float: the value of `steam_conversion_efficiency` or None if not set
        """
        return self._data["Steam Conversion Efficiency"]

    @steam_conversion_efficiency.setter
    def steam_conversion_efficiency(self, value=0.25 ):
        """  Corresponds to IDD Field `steam_conversion_efficiency`
        Steam conversion efficiency used to convert steam usage to natural gas

        Args:
            value (float): value for IDD Field `steam_conversion_efficiency`
                Default value: 0.25
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
                                 'for field `steam_conversion_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `steam_conversion_efficiency`')

        self._data["Steam Conversion Efficiency"] = value

    @property
    def total_carbon_equivalent_emission_factor_from_n2o(self):
        """Get total_carbon_equivalent_emission_factor_from_n2o

        Returns:
            float: the value of `total_carbon_equivalent_emission_factor_from_n2o` or None if not set
        """
        return self._data["Total Carbon Equivalent Emission Factor From N2O"]

    @total_carbon_equivalent_emission_factor_from_n2o.setter
    def total_carbon_equivalent_emission_factor_from_n2o(self, value=80.7272 ):
        """  Corresponds to IDD Field `total_carbon_equivalent_emission_factor_from_n2o`

        Args:
            value (float): value for IDD Field `total_carbon_equivalent_emission_factor_from_n2o`
                Unit: kg/kg
                Default value: 80.7272
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `total_carbon_equivalent_emission_factor_from_n2o`'.format(value))

        self._data["Total Carbon Equivalent Emission Factor From N2O"] = value

    @property
    def total_carbon_equivalent_emission_factor_from_ch4(self):
        """Get total_carbon_equivalent_emission_factor_from_ch4

        Returns:
            float: the value of `total_carbon_equivalent_emission_factor_from_ch4` or None if not set
        """
        return self._data["Total Carbon Equivalent Emission Factor From CH4"]

    @total_carbon_equivalent_emission_factor_from_ch4.setter
    def total_carbon_equivalent_emission_factor_from_ch4(self, value=6.2727 ):
        """  Corresponds to IDD Field `total_carbon_equivalent_emission_factor_from_ch4`

        Args:
            value (float): value for IDD Field `total_carbon_equivalent_emission_factor_from_ch4`
                Unit: kg/kg
                Default value: 6.2727
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `total_carbon_equivalent_emission_factor_from_ch4`'.format(value))

        self._data["Total Carbon Equivalent Emission Factor From CH4"] = value

    @property
    def total_carbon_equivalent_emission_factor_from_co2(self):
        """Get total_carbon_equivalent_emission_factor_from_co2

        Returns:
            float: the value of `total_carbon_equivalent_emission_factor_from_co2` or None if not set
        """
        return self._data["Total Carbon Equivalent Emission Factor From CO2"]

    @total_carbon_equivalent_emission_factor_from_co2.setter
    def total_carbon_equivalent_emission_factor_from_co2(self, value=0.2727 ):
        """  Corresponds to IDD Field `total_carbon_equivalent_emission_factor_from_co2`

        Args:
            value (float): value for IDD Field `total_carbon_equivalent_emission_factor_from_co2`
                Unit: kg/kg
                Default value: 0.2727
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `total_carbon_equivalent_emission_factor_from_co2`'.format(value))

        self._data["Total Carbon Equivalent Emission Factor From CO2"] = value

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
        out.append(self._to_str(self.district_heating_efficiency))
        out.append(self._to_str(self.district_cooling_cop))
        out.append(self._to_str(self.steam_conversion_efficiency))
        out.append(self._to_str(self.total_carbon_equivalent_emission_factor_from_n2o))
        out.append(self._to_str(self.total_carbon_equivalent_emission_factor_from_ch4))
        out.append(self._to_str(self.total_carbon_equivalent_emission_factor_from_co2))
        return ",".join(out)