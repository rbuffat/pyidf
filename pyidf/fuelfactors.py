from collections import OrderedDict

class FuelFactors(object):
    """ Corresponds to IDD object `FuelFactors`
        Provides Fuel Factors for Emissions as well as Source=>Site conversions.
        OtherFuel1, OtherFuel2 provide options for users who want to create and use
        fuels that may not be mainstream (biomass, wood, pellets).
    """
    internal_name = "FuelFactors"
    field_count = 37

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `FuelFactors`
        """
        self._data = OrderedDict()
        self._data["Existing Fuel Resource Name"] = None
        self._data["Units of Measure"] = None
        self._data["Energy per Unit Factor"] = None
        self._data["Source Energy Factor"] = None
        self._data["Source Energy Schedule Name"] = None
        self._data["CO2 Emission Factor"] = None
        self._data["CO2 Emission Factor Schedule Name"] = None
        self._data["CO Emission Factor"] = None
        self._data["CO Emission Factor Schedule Name"] = None
        self._data["CH4 Emission Factor"] = None
        self._data["CH4 Emission Factor Schedule Name"] = None
        self._data["NOx Emission Factor"] = None
        self._data["NOx Emission Factor Schedule Name"] = None
        self._data["N2O Emission Factor"] = None
        self._data["N2O Emission Factor Schedule Name"] = None
        self._data["SO2 Emission Factor"] = None
        self._data["SO2 Emission Factor Schedule Name"] = None
        self._data["PM Emission Factor"] = None
        self._data["PM Emission Factor Schedule Name"] = None
        self._data["PM10 Emission Factor"] = None
        self._data["PM10 Emission Factor Schedule Name"] = None
        self._data["PM2.5 Emission Factor"] = None
        self._data["PM2.5 Emission Factor Schedule Name"] = None
        self._data["NH3 Emission Factor"] = None
        self._data["NH3 Emission Factor Schedule Name"] = None
        self._data["NMVOC Emission Factor"] = None
        self._data["NMVOC Emission Factor Schedule Name"] = None
        self._data["Hg Emission Factor"] = None
        self._data["Hg Emission Factor Schedule Name"] = None
        self._data["Pb Emission Factor"] = None
        self._data["Pb Emission Factor Schedule Name"] = None
        self._data["Water Emission Factor"] = None
        self._data["Water Emission Factor Schedule Name"] = None
        self._data["Nuclear High Level Emission Factor"] = None
        self._data["Nuclear High Level Emission Factor Schedule Name"] = None
        self._data["Nuclear Low Level Emission Factor"] = None
        self._data["Nuclear Low Level Emission Factor Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.existing_fuel_resource_name = None
        else:
            self.existing_fuel_resource_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.units_of_measure = None
        else:
            self.units_of_measure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.energy_per_unit_factor = None
        else:
            self.energy_per_unit_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_energy_factor = None
        else:
            self.source_energy_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_energy_schedule_name = None
        else:
            self.source_energy_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.co2_emission_factor = None
        else:
            self.co2_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.co2_emission_factor_schedule_name = None
        else:
            self.co2_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.co_emission_factor = None
        else:
            self.co_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.co_emission_factor_schedule_name = None
        else:
            self.co_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ch4_emission_factor = None
        else:
            self.ch4_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ch4_emission_factor_schedule_name = None
        else:
            self.ch4_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nox_emission_factor = None
        else:
            self.nox_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nox_emission_factor_schedule_name = None
        else:
            self.nox_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.n2o_emission_factor = None
        else:
            self.n2o_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.n2o_emission_factor_schedule_name = None
        else:
            self.n2o_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.so2_emission_factor = None
        else:
            self.so2_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.so2_emission_factor_schedule_name = None
        else:
            self.so2_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pm_emission_factor = None
        else:
            self.pm_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pm_emission_factor_schedule_name = None
        else:
            self.pm_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pm10_emission_factor = None
        else:
            self.pm10_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pm10_emission_factor_schedule_name = None
        else:
            self.pm10_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pm2_5_emission_factor = None
        else:
            self.pm2_5_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pm2_5_emission_factor_schedule_name = None
        else:
            self.pm2_5_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nh3_emission_factor = None
        else:
            self.nh3_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nh3_emission_factor_schedule_name = None
        else:
            self.nh3_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nmvoc_emission_factor = None
        else:
            self.nmvoc_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nmvoc_emission_factor_schedule_name = None
        else:
            self.nmvoc_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hg_emission_factor = None
        else:
            self.hg_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hg_emission_factor_schedule_name = None
        else:
            self.hg_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pb_emission_factor = None
        else:
            self.pb_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pb_emission_factor_schedule_name = None
        else:
            self.pb_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_emission_factor = None
        else:
            self.water_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_emission_factor_schedule_name = None
        else:
            self.water_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nuclear_high_level_emission_factor = None
        else:
            self.nuclear_high_level_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nuclear_high_level_emission_factor_schedule_name = None
        else:
            self.nuclear_high_level_emission_factor_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nuclear_low_level_emission_factor = None
        else:
            self.nuclear_low_level_emission_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nuclear_low_level_emission_factor_schedule_name = None
        else:
            self.nuclear_low_level_emission_factor_schedule_name = vals[i]
        i += 1

    @property
    def existing_fuel_resource_name(self):
        """Get existing_fuel_resource_name

        Returns:
            str: the value of `existing_fuel_resource_name` or None if not set
        """
        return self._data["Existing Fuel Resource Name"]

    @existing_fuel_resource_name.setter
    def existing_fuel_resource_name(self, value=None):
        """  Corresponds to IDD Field `existing_fuel_resource_name`

        Args:
            value (str): value for IDD Field `existing_fuel_resource_name`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Gasoline
                      - Propane
                      - Diesel
                      - OtherFuel1
                      - OtherFuel2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `existing_fuel_resource_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `existing_fuel_resource_name`')
            vals = set()
            vals.add("Electricity")
            vals.add("NaturalGas")
            vals.add("FuelOil#1")
            vals.add("FuelOil#2")
            vals.add("Coal")
            vals.add("Gasoline")
            vals.add("Propane")
            vals.add("Diesel")
            vals.add("OtherFuel1")
            vals.add("OtherFuel2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `existing_fuel_resource_name`'.format(value))

        self._data["Existing Fuel Resource Name"] = value

    @property
    def units_of_measure(self):
        """Get units_of_measure

        Returns:
            str: the value of `units_of_measure` or None if not set
        """
        return self._data["Units of Measure"]

    @units_of_measure.setter
    def units_of_measure(self, value=None):
        """  Corresponds to IDD Field `units_of_measure`

        Args:
            value (str): value for IDD Field `units_of_measure`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `units_of_measure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `units_of_measure`')

        self._data["Units of Measure"] = value

    @property
    def energy_per_unit_factor(self):
        """Get energy_per_unit_factor

        Returns:
            float: the value of `energy_per_unit_factor` or None if not set
        """
        return self._data["Energy per Unit Factor"]

    @energy_per_unit_factor.setter
    def energy_per_unit_factor(self, value=None):
        """  Corresponds to IDD Field `energy_per_unit_factor`

        Args:
            value (float): value for IDD Field `energy_per_unit_factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `energy_per_unit_factor`'.format(value))

        self._data["Energy per Unit Factor"] = value

    @property
    def source_energy_factor(self):
        """Get source_energy_factor

        Returns:
            float: the value of `source_energy_factor` or None if not set
        """
        return self._data["Source Energy Factor"]

    @source_energy_factor.setter
    def source_energy_factor(self, value=None):
        """  Corresponds to IDD Field `source_energy_factor`

        Args:
            value (float): value for IDD Field `source_energy_factor`
                Unit: J/J
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `source_energy_factor`'.format(value))

        self._data["Source Energy Factor"] = value

    @property
    def source_energy_schedule_name(self):
        """Get source_energy_schedule_name

        Returns:
            str: the value of `source_energy_schedule_name` or None if not set
        """
        return self._data["Source Energy Schedule Name"]

    @source_energy_schedule_name.setter
    def source_energy_schedule_name(self, value=None):
        """  Corresponds to IDD Field `source_energy_schedule_name`

        Args:
            value (str): value for IDD Field `source_energy_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_energy_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_energy_schedule_name`')

        self._data["Source Energy Schedule Name"] = value

    @property
    def co2_emission_factor(self):
        """Get co2_emission_factor

        Returns:
            float: the value of `co2_emission_factor` or None if not set
        """
        return self._data["CO2 Emission Factor"]

    @co2_emission_factor.setter
    def co2_emission_factor(self, value=None):
        """  Corresponds to IDD Field `co2_emission_factor`

        Args:
            value (float): value for IDD Field `co2_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `co2_emission_factor`'.format(value))

        self._data["CO2 Emission Factor"] = value

    @property
    def co2_emission_factor_schedule_name(self):
        """Get co2_emission_factor_schedule_name

        Returns:
            str: the value of `co2_emission_factor_schedule_name` or None if not set
        """
        return self._data["CO2 Emission Factor Schedule Name"]

    @co2_emission_factor_schedule_name.setter
    def co2_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `co2_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `co2_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `co2_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `co2_emission_factor_schedule_name`')

        self._data["CO2 Emission Factor Schedule Name"] = value

    @property
    def co_emission_factor(self):
        """Get co_emission_factor

        Returns:
            float: the value of `co_emission_factor` or None if not set
        """
        return self._data["CO Emission Factor"]

    @co_emission_factor.setter
    def co_emission_factor(self, value=None):
        """  Corresponds to IDD Field `co_emission_factor`

        Args:
            value (float): value for IDD Field `co_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `co_emission_factor`'.format(value))

        self._data["CO Emission Factor"] = value

    @property
    def co_emission_factor_schedule_name(self):
        """Get co_emission_factor_schedule_name

        Returns:
            str: the value of `co_emission_factor_schedule_name` or None if not set
        """
        return self._data["CO Emission Factor Schedule Name"]

    @co_emission_factor_schedule_name.setter
    def co_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `co_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `co_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `co_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `co_emission_factor_schedule_name`')

        self._data["CO Emission Factor Schedule Name"] = value

    @property
    def ch4_emission_factor(self):
        """Get ch4_emission_factor

        Returns:
            float: the value of `ch4_emission_factor` or None if not set
        """
        return self._data["CH4 Emission Factor"]

    @ch4_emission_factor.setter
    def ch4_emission_factor(self, value=None):
        """  Corresponds to IDD Field `ch4_emission_factor`

        Args:
            value (float): value for IDD Field `ch4_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ch4_emission_factor`'.format(value))

        self._data["CH4 Emission Factor"] = value

    @property
    def ch4_emission_factor_schedule_name(self):
        """Get ch4_emission_factor_schedule_name

        Returns:
            str: the value of `ch4_emission_factor_schedule_name` or None if not set
        """
        return self._data["CH4 Emission Factor Schedule Name"]

    @ch4_emission_factor_schedule_name.setter
    def ch4_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ch4_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `ch4_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ch4_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ch4_emission_factor_schedule_name`')

        self._data["CH4 Emission Factor Schedule Name"] = value

    @property
    def nox_emission_factor(self):
        """Get nox_emission_factor

        Returns:
            float: the value of `nox_emission_factor` or None if not set
        """
        return self._data["NOx Emission Factor"]

    @nox_emission_factor.setter
    def nox_emission_factor(self, value=None):
        """  Corresponds to IDD Field `nox_emission_factor`

        Args:
            value (float): value for IDD Field `nox_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `nox_emission_factor`'.format(value))

        self._data["NOx Emission Factor"] = value

    @property
    def nox_emission_factor_schedule_name(self):
        """Get nox_emission_factor_schedule_name

        Returns:
            str: the value of `nox_emission_factor_schedule_name` or None if not set
        """
        return self._data["NOx Emission Factor Schedule Name"]

    @nox_emission_factor_schedule_name.setter
    def nox_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `nox_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `nox_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `nox_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `nox_emission_factor_schedule_name`')

        self._data["NOx Emission Factor Schedule Name"] = value

    @property
    def n2o_emission_factor(self):
        """Get n2o_emission_factor

        Returns:
            float: the value of `n2o_emission_factor` or None if not set
        """
        return self._data["N2O Emission Factor"]

    @n2o_emission_factor.setter
    def n2o_emission_factor(self, value=None):
        """  Corresponds to IDD Field `n2o_emission_factor`

        Args:
            value (float): value for IDD Field `n2o_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `n2o_emission_factor`'.format(value))

        self._data["N2O Emission Factor"] = value

    @property
    def n2o_emission_factor_schedule_name(self):
        """Get n2o_emission_factor_schedule_name

        Returns:
            str: the value of `n2o_emission_factor_schedule_name` or None if not set
        """
        return self._data["N2O Emission Factor Schedule Name"]

    @n2o_emission_factor_schedule_name.setter
    def n2o_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `n2o_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `n2o_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `n2o_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `n2o_emission_factor_schedule_name`')

        self._data["N2O Emission Factor Schedule Name"] = value

    @property
    def so2_emission_factor(self):
        """Get so2_emission_factor

        Returns:
            float: the value of `so2_emission_factor` or None if not set
        """
        return self._data["SO2 Emission Factor"]

    @so2_emission_factor.setter
    def so2_emission_factor(self, value=None):
        """  Corresponds to IDD Field `so2_emission_factor`

        Args:
            value (float): value for IDD Field `so2_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `so2_emission_factor`'.format(value))

        self._data["SO2 Emission Factor"] = value

    @property
    def so2_emission_factor_schedule_name(self):
        """Get so2_emission_factor_schedule_name

        Returns:
            str: the value of `so2_emission_factor_schedule_name` or None if not set
        """
        return self._data["SO2 Emission Factor Schedule Name"]

    @so2_emission_factor_schedule_name.setter
    def so2_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `so2_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `so2_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `so2_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `so2_emission_factor_schedule_name`')

        self._data["SO2 Emission Factor Schedule Name"] = value

    @property
    def pm_emission_factor(self):
        """Get pm_emission_factor

        Returns:
            float: the value of `pm_emission_factor` or None if not set
        """
        return self._data["PM Emission Factor"]

    @pm_emission_factor.setter
    def pm_emission_factor(self, value=None):
        """  Corresponds to IDD Field `pm_emission_factor`

        Args:
            value (float): value for IDD Field `pm_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pm_emission_factor`'.format(value))

        self._data["PM Emission Factor"] = value

    @property
    def pm_emission_factor_schedule_name(self):
        """Get pm_emission_factor_schedule_name

        Returns:
            str: the value of `pm_emission_factor_schedule_name` or None if not set
        """
        return self._data["PM Emission Factor Schedule Name"]

    @pm_emission_factor_schedule_name.setter
    def pm_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pm_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `pm_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pm_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pm_emission_factor_schedule_name`')

        self._data["PM Emission Factor Schedule Name"] = value

    @property
    def pm10_emission_factor(self):
        """Get pm10_emission_factor

        Returns:
            float: the value of `pm10_emission_factor` or None if not set
        """
        return self._data["PM10 Emission Factor"]

    @pm10_emission_factor.setter
    def pm10_emission_factor(self, value=None):
        """  Corresponds to IDD Field `pm10_emission_factor`

        Args:
            value (float): value for IDD Field `pm10_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pm10_emission_factor`'.format(value))

        self._data["PM10 Emission Factor"] = value

    @property
    def pm10_emission_factor_schedule_name(self):
        """Get pm10_emission_factor_schedule_name

        Returns:
            str: the value of `pm10_emission_factor_schedule_name` or None if not set
        """
        return self._data["PM10 Emission Factor Schedule Name"]

    @pm10_emission_factor_schedule_name.setter
    def pm10_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pm10_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `pm10_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pm10_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pm10_emission_factor_schedule_name`')

        self._data["PM10 Emission Factor Schedule Name"] = value

    @property
    def pm2_5_emission_factor(self):
        """Get pm2_5_emission_factor

        Returns:
            float: the value of `pm2_5_emission_factor` or None if not set
        """
        return self._data["PM2.5 Emission Factor"]

    @pm2_5_emission_factor.setter
    def pm2_5_emission_factor(self, value=None):
        """  Corresponds to IDD Field `pm2_5_emission_factor`

        Args:
            value (float): value for IDD Field `pm2_5_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pm2_5_emission_factor`'.format(value))

        self._data["PM2.5 Emission Factor"] = value

    @property
    def pm2_5_emission_factor_schedule_name(self):
        """Get pm2_5_emission_factor_schedule_name

        Returns:
            str: the value of `pm2_5_emission_factor_schedule_name` or None if not set
        """
        return self._data["PM2.5 Emission Factor Schedule Name"]

    @pm2_5_emission_factor_schedule_name.setter
    def pm2_5_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pm2_5_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `pm2_5_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pm2_5_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pm2_5_emission_factor_schedule_name`')

        self._data["PM2.5 Emission Factor Schedule Name"] = value

    @property
    def nh3_emission_factor(self):
        """Get nh3_emission_factor

        Returns:
            float: the value of `nh3_emission_factor` or None if not set
        """
        return self._data["NH3 Emission Factor"]

    @nh3_emission_factor.setter
    def nh3_emission_factor(self, value=None):
        """  Corresponds to IDD Field `nh3_emission_factor`

        Args:
            value (float): value for IDD Field `nh3_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `nh3_emission_factor`'.format(value))

        self._data["NH3 Emission Factor"] = value

    @property
    def nh3_emission_factor_schedule_name(self):
        """Get nh3_emission_factor_schedule_name

        Returns:
            str: the value of `nh3_emission_factor_schedule_name` or None if not set
        """
        return self._data["NH3 Emission Factor Schedule Name"]

    @nh3_emission_factor_schedule_name.setter
    def nh3_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `nh3_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `nh3_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `nh3_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `nh3_emission_factor_schedule_name`')

        self._data["NH3 Emission Factor Schedule Name"] = value

    @property
    def nmvoc_emission_factor(self):
        """Get nmvoc_emission_factor

        Returns:
            float: the value of `nmvoc_emission_factor` or None if not set
        """
        return self._data["NMVOC Emission Factor"]

    @nmvoc_emission_factor.setter
    def nmvoc_emission_factor(self, value=None):
        """  Corresponds to IDD Field `nmvoc_emission_factor`

        Args:
            value (float): value for IDD Field `nmvoc_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `nmvoc_emission_factor`'.format(value))

        self._data["NMVOC Emission Factor"] = value

    @property
    def nmvoc_emission_factor_schedule_name(self):
        """Get nmvoc_emission_factor_schedule_name

        Returns:
            str: the value of `nmvoc_emission_factor_schedule_name` or None if not set
        """
        return self._data["NMVOC Emission Factor Schedule Name"]

    @nmvoc_emission_factor_schedule_name.setter
    def nmvoc_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `nmvoc_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `nmvoc_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `nmvoc_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `nmvoc_emission_factor_schedule_name`')

        self._data["NMVOC Emission Factor Schedule Name"] = value

    @property
    def hg_emission_factor(self):
        """Get hg_emission_factor

        Returns:
            float: the value of `hg_emission_factor` or None if not set
        """
        return self._data["Hg Emission Factor"]

    @hg_emission_factor.setter
    def hg_emission_factor(self, value=None):
        """  Corresponds to IDD Field `hg_emission_factor`

        Args:
            value (float): value for IDD Field `hg_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hg_emission_factor`'.format(value))

        self._data["Hg Emission Factor"] = value

    @property
    def hg_emission_factor_schedule_name(self):
        """Get hg_emission_factor_schedule_name

        Returns:
            str: the value of `hg_emission_factor_schedule_name` or None if not set
        """
        return self._data["Hg Emission Factor Schedule Name"]

    @hg_emission_factor_schedule_name.setter
    def hg_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `hg_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `hg_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hg_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hg_emission_factor_schedule_name`')

        self._data["Hg Emission Factor Schedule Name"] = value

    @property
    def pb_emission_factor(self):
        """Get pb_emission_factor

        Returns:
            float: the value of `pb_emission_factor` or None if not set
        """
        return self._data["Pb Emission Factor"]

    @pb_emission_factor.setter
    def pb_emission_factor(self, value=None):
        """  Corresponds to IDD Field `pb_emission_factor`

        Args:
            value (float): value for IDD Field `pb_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pb_emission_factor`'.format(value))

        self._data["Pb Emission Factor"] = value

    @property
    def pb_emission_factor_schedule_name(self):
        """Get pb_emission_factor_schedule_name

        Returns:
            str: the value of `pb_emission_factor_schedule_name` or None if not set
        """
        return self._data["Pb Emission Factor Schedule Name"]

    @pb_emission_factor_schedule_name.setter
    def pb_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pb_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `pb_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pb_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pb_emission_factor_schedule_name`')

        self._data["Pb Emission Factor Schedule Name"] = value

    @property
    def water_emission_factor(self):
        """Get water_emission_factor

        Returns:
            float: the value of `water_emission_factor` or None if not set
        """
        return self._data["Water Emission Factor"]

    @water_emission_factor.setter
    def water_emission_factor(self, value=None):
        """  Corresponds to IDD Field `water_emission_factor`

        Args:
            value (float): value for IDD Field `water_emission_factor`
                Unit: L/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `water_emission_factor`'.format(value))

        self._data["Water Emission Factor"] = value

    @property
    def water_emission_factor_schedule_name(self):
        """Get water_emission_factor_schedule_name

        Returns:
            str: the value of `water_emission_factor_schedule_name` or None if not set
        """
        return self._data["Water Emission Factor Schedule Name"]

    @water_emission_factor_schedule_name.setter
    def water_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `water_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `water_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `water_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_emission_factor_schedule_name`')

        self._data["Water Emission Factor Schedule Name"] = value

    @property
    def nuclear_high_level_emission_factor(self):
        """Get nuclear_high_level_emission_factor

        Returns:
            float: the value of `nuclear_high_level_emission_factor` or None if not set
        """
        return self._data["Nuclear High Level Emission Factor"]

    @nuclear_high_level_emission_factor.setter
    def nuclear_high_level_emission_factor(self, value=None):
        """  Corresponds to IDD Field `nuclear_high_level_emission_factor`

        Args:
            value (float): value for IDD Field `nuclear_high_level_emission_factor`
                Unit: g/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `nuclear_high_level_emission_factor`'.format(value))

        self._data["Nuclear High Level Emission Factor"] = value

    @property
    def nuclear_high_level_emission_factor_schedule_name(self):
        """Get nuclear_high_level_emission_factor_schedule_name

        Returns:
            str: the value of `nuclear_high_level_emission_factor_schedule_name` or None if not set
        """
        return self._data["Nuclear High Level Emission Factor Schedule Name"]

    @nuclear_high_level_emission_factor_schedule_name.setter
    def nuclear_high_level_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `nuclear_high_level_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `nuclear_high_level_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `nuclear_high_level_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `nuclear_high_level_emission_factor_schedule_name`')

        self._data["Nuclear High Level Emission Factor Schedule Name"] = value

    @property
    def nuclear_low_level_emission_factor(self):
        """Get nuclear_low_level_emission_factor

        Returns:
            float: the value of `nuclear_low_level_emission_factor` or None if not set
        """
        return self._data["Nuclear Low Level Emission Factor"]

    @nuclear_low_level_emission_factor.setter
    def nuclear_low_level_emission_factor(self, value=None):
        """  Corresponds to IDD Field `nuclear_low_level_emission_factor`

        Args:
            value (float): value for IDD Field `nuclear_low_level_emission_factor`
                Unit: m3/MJ
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `nuclear_low_level_emission_factor`'.format(value))

        self._data["Nuclear Low Level Emission Factor"] = value

    @property
    def nuclear_low_level_emission_factor_schedule_name(self):
        """Get nuclear_low_level_emission_factor_schedule_name

        Returns:
            str: the value of `nuclear_low_level_emission_factor_schedule_name` or None if not set
        """
        return self._data["Nuclear Low Level Emission Factor Schedule Name"]

    @nuclear_low_level_emission_factor_schedule_name.setter
    def nuclear_low_level_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `nuclear_low_level_emission_factor_schedule_name`

        Args:
            value (str): value for IDD Field `nuclear_low_level_emission_factor_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `nuclear_low_level_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `nuclear_low_level_emission_factor_schedule_name`')

        self._data["Nuclear Low Level Emission Factor Schedule Name"] = value

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
        out.append(self._to_str(self.existing_fuel_resource_name))
        out.append(self._to_str(self.units_of_measure))
        out.append(self._to_str(self.energy_per_unit_factor))
        out.append(self._to_str(self.source_energy_factor))
        out.append(self._to_str(self.source_energy_schedule_name))
        out.append(self._to_str(self.co2_emission_factor))
        out.append(self._to_str(self.co2_emission_factor_schedule_name))
        out.append(self._to_str(self.co_emission_factor))
        out.append(self._to_str(self.co_emission_factor_schedule_name))
        out.append(self._to_str(self.ch4_emission_factor))
        out.append(self._to_str(self.ch4_emission_factor_schedule_name))
        out.append(self._to_str(self.nox_emission_factor))
        out.append(self._to_str(self.nox_emission_factor_schedule_name))
        out.append(self._to_str(self.n2o_emission_factor))
        out.append(self._to_str(self.n2o_emission_factor_schedule_name))
        out.append(self._to_str(self.so2_emission_factor))
        out.append(self._to_str(self.so2_emission_factor_schedule_name))
        out.append(self._to_str(self.pm_emission_factor))
        out.append(self._to_str(self.pm_emission_factor_schedule_name))
        out.append(self._to_str(self.pm10_emission_factor))
        out.append(self._to_str(self.pm10_emission_factor_schedule_name))
        out.append(self._to_str(self.pm2_5_emission_factor))
        out.append(self._to_str(self.pm2_5_emission_factor_schedule_name))
        out.append(self._to_str(self.nh3_emission_factor))
        out.append(self._to_str(self.nh3_emission_factor_schedule_name))
        out.append(self._to_str(self.nmvoc_emission_factor))
        out.append(self._to_str(self.nmvoc_emission_factor_schedule_name))
        out.append(self._to_str(self.hg_emission_factor))
        out.append(self._to_str(self.hg_emission_factor_schedule_name))
        out.append(self._to_str(self.pb_emission_factor))
        out.append(self._to_str(self.pb_emission_factor_schedule_name))
        out.append(self._to_str(self.water_emission_factor))
        out.append(self._to_str(self.water_emission_factor_schedule_name))
        out.append(self._to_str(self.nuclear_high_level_emission_factor))
        out.append(self._to_str(self.nuclear_high_level_emission_factor_schedule_name))
        out.append(self._to_str(self.nuclear_low_level_emission_factor))
        out.append(self._to_str(self.nuclear_low_level_emission_factor_schedule_name))
        return ",".join(out)