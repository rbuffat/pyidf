from collections import OrderedDict

class RefrigerationCase(object):
    """ Corresponds to IDD object `Refrigeration:Case`
        The Refrigeration Case object works in conjunction with a compressor rack, a
        refrigeration system, or a secondary loop to simulate the performance of a
        refrigerated case system. The object calculates the energy use for lights, fans and
        anti-sweat heaters and accounts for the sensible and latent heat exchange with the
        surrounding environment (termed "case credits") which impacts the temperature
        and humidity in the zone where the case is located.
    
    """
    internal_name = "Refrigeration:Case"
    field_count = 35
    required_fields = ["Name", "Zone Name", "Latent Case Credit Curve Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:Case`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Rated Ambient Temperature"] = None
        self._data["Rated Ambient Relative Humidity"] = None
        self._data["Rated Total Cooling Capacity per Unit Length"] = None
        self._data["Rated Latent Heat Ratio"] = None
        self._data["Rated Runtime Fraction"] = None
        self._data["Case Length"] = None
        self._data["Case Operating Temperature"] = None
        self._data["Latent Case Credit Curve Type"] = None
        self._data["Latent Case Credit Curve Name"] = None
        self._data["Standard Case Fan Power per Unit Length"] = None
        self._data["Operating Case Fan Power per Unit Length"] = None
        self._data["Standard Case Lighting Power per Unit Length"] = None
        self._data["Installed Case Lighting Power per Unit Length"] = None
        self._data["Case Lighting Schedule Name"] = None
        self._data["Fraction of Lighting Energy to Case"] = None
        self._data["Case Anti-Sweat Heater Power per Unit Length"] = None
        self._data["Minimum Anti-Sweat Heater Power per Unit Length"] = None
        self._data["Anti-Sweat Heater Control Type"] = None
        self._data["Humidity at Zero Anti-Sweat Heater Energy"] = None
        self._data["Case Height"] = None
        self._data["Fraction of Anti-Sweat Heater Energy to Case"] = None
        self._data["Case Defrost Power per Unit Length"] = None
        self._data["Case Defrost Type"] = None
        self._data["Case Defrost Schedule Name"] = None
        self._data["Case Defrost Drip-Down Schedule Name"] = None
        self._data["Defrost Energy Correction Curve Type"] = None
        self._data["Defrost Energy Correction Curve Name"] = None
        self._data["Under Case HVAC Return Air Fraction"] = None
        self._data["Refrigerated Case Restocking Schedule Name"] = None
        self._data["Case Credit Fraction Schedule Name"] = None
        self._data["Design Evaporator Temperature or Brine Inlet Temperature"] = None
        self._data["Average Refrigerant Charge Inventory"] = None
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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
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
            self.rated_ambient_temperature = None
        else:
            self.rated_ambient_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_ambient_relative_humidity = None
        else:
            self.rated_ambient_relative_humidity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_total_cooling_capacity_per_unit_length = None
        else:
            self.rated_total_cooling_capacity_per_unit_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_latent_heat_ratio = None
        else:
            self.rated_latent_heat_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_runtime_fraction = None
        else:
            self.rated_runtime_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_length = None
        else:
            self.case_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_operating_temperature = None
        else:
            self.case_operating_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.latent_case_credit_curve_type = None
        else:
            self.latent_case_credit_curve_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.latent_case_credit_curve_name = None
        else:
            self.latent_case_credit_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.standard_case_fan_power_per_unit_length = None
        else:
            self.standard_case_fan_power_per_unit_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operating_case_fan_power_per_unit_length = None
        else:
            self.operating_case_fan_power_per_unit_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.standard_case_lighting_power_per_unit_length = None
        else:
            self.standard_case_lighting_power_per_unit_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.installed_case_lighting_power_per_unit_length = None
        else:
            self.installed_case_lighting_power_per_unit_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_lighting_schedule_name = None
        else:
            self.case_lighting_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_lighting_energy_to_case = None
        else:
            self.fraction_of_lighting_energy_to_case = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_antisweat_heater_power_per_unit_length = None
        else:
            self.case_antisweat_heater_power_per_unit_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_antisweat_heater_power_per_unit_length = None
        else:
            self.minimum_antisweat_heater_power_per_unit_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.antisweat_heater_control_type = None
        else:
            self.antisweat_heater_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_at_zero_antisweat_heater_energy = None
        else:
            self.humidity_at_zero_antisweat_heater_energy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_height = None
        else:
            self.case_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_antisweat_heater_energy_to_case = None
        else:
            self.fraction_of_antisweat_heater_energy_to_case = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_defrost_power_per_unit_length = None
        else:
            self.case_defrost_power_per_unit_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_defrost_type = None
        else:
            self.case_defrost_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_defrost_schedule_name = None
        else:
            self.case_defrost_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_defrost_dripdown_schedule_name = None
        else:
            self.case_defrost_dripdown_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_energy_correction_curve_type = None
        else:
            self.defrost_energy_correction_curve_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_energy_correction_curve_name = None
        else:
            self.defrost_energy_correction_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.under_case_hvac_return_air_fraction = None
        else:
            self.under_case_hvac_return_air_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigerated_case_restocking_schedule_name = None
        else:
            self.refrigerated_case_restocking_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_credit_fraction_schedule_name = None
        else:
            self.case_credit_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_evaporator_temperature_or_brine_inlet_temperature = None
        else:
            self.design_evaporator_temperature_or_brine_inlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.average_refrigerant_charge_inventory = None
        else:
            self.average_refrigerant_charge_inventory = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
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
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

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
        This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object.

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
    def rated_ambient_temperature(self):
        """Get rated_ambient_temperature

        Returns:
            float: the value of `rated_ambient_temperature` or None if not set
        """
        return self._data["Rated Ambient Temperature"]

    @rated_ambient_temperature.setter
    def rated_ambient_temperature(self, value=23.9):
        """  Corresponds to IDD Field `Rated Ambient Temperature`

        Args:
            value (float): value for IDD Field `Rated Ambient Temperature`
                Units: C
                Default value: 23.9
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
                                 'for field `rated_ambient_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_ambient_temperature`')
        self._data["Rated Ambient Temperature"] = value

    @property
    def rated_ambient_relative_humidity(self):
        """Get rated_ambient_relative_humidity

        Returns:
            float: the value of `rated_ambient_relative_humidity` or None if not set
        """
        return self._data["Rated Ambient Relative Humidity"]

    @rated_ambient_relative_humidity.setter
    def rated_ambient_relative_humidity(self, value=55.0):
        """  Corresponds to IDD Field `Rated Ambient Relative Humidity`

        Args:
            value (float): value for IDD Field `Rated Ambient Relative Humidity`
                Units: percent
                Default value: 55.0
                value > 0.0
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
                                 'for field `rated_ambient_relative_humidity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_ambient_relative_humidity`')
            if value >= 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `rated_ambient_relative_humidity`')
        self._data["Rated Ambient Relative Humidity"] = value

    @property
    def rated_total_cooling_capacity_per_unit_length(self):
        """Get rated_total_cooling_capacity_per_unit_length

        Returns:
            float: the value of `rated_total_cooling_capacity_per_unit_length` or None if not set
        """
        return self._data["Rated Total Cooling Capacity per Unit Length"]

    @rated_total_cooling_capacity_per_unit_length.setter
    def rated_total_cooling_capacity_per_unit_length(self, value=1900.0):
        """  Corresponds to IDD Field `Rated Total Cooling Capacity per Unit Length`

        Args:
            value (float): value for IDD Field `Rated Total Cooling Capacity per Unit Length`
                Units: W/m
                Default value: 1900.0
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
                                 'for field `rated_total_cooling_capacity_per_unit_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_total_cooling_capacity_per_unit_length`')
        self._data["Rated Total Cooling Capacity per Unit Length"] = value

    @property
    def rated_latent_heat_ratio(self):
        """Get rated_latent_heat_ratio

        Returns:
            float: the value of `rated_latent_heat_ratio` or None if not set
        """
        return self._data["Rated Latent Heat Ratio"]

    @rated_latent_heat_ratio.setter
    def rated_latent_heat_ratio(self, value=0.3):
        """  Corresponds to IDD Field `Rated Latent Heat Ratio`

        Args:
            value (float): value for IDD Field `Rated Latent Heat Ratio`
                Default value: 0.3
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
                                 'for field `rated_latent_heat_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_latent_heat_ratio`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `rated_latent_heat_ratio`')
        self._data["Rated Latent Heat Ratio"] = value

    @property
    def rated_runtime_fraction(self):
        """Get rated_runtime_fraction

        Returns:
            float: the value of `rated_runtime_fraction` or None if not set
        """
        return self._data["Rated Runtime Fraction"]

    @rated_runtime_fraction.setter
    def rated_runtime_fraction(self, value=0.85):
        """  Corresponds to IDD Field `Rated Runtime Fraction`

        Args:
            value (float): value for IDD Field `Rated Runtime Fraction`
                Default value: 0.85
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
                                 'for field `rated_runtime_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_runtime_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `rated_runtime_fraction`')
        self._data["Rated Runtime Fraction"] = value

    @property
    def case_length(self):
        """Get case_length

        Returns:
            float: the value of `case_length` or None if not set
        """
        return self._data["Case Length"]

    @case_length.setter
    def case_length(self, value=3.0):
        """  Corresponds to IDD Field `Case Length`

        Args:
            value (float): value for IDD Field `Case Length`
                Units: m
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `case_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `case_length`')
        self._data["Case Length"] = value

    @property
    def case_operating_temperature(self):
        """Get case_operating_temperature

        Returns:
            float: the value of `case_operating_temperature` or None if not set
        """
        return self._data["Case Operating Temperature"]

    @case_operating_temperature.setter
    def case_operating_temperature(self, value=1.1):
        """  Corresponds to IDD Field `Case Operating Temperature`

        Args:
            value (float): value for IDD Field `Case Operating Temperature`
                Units: C
                Default value: 1.1
                value < 20.0
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
                                 'for field `case_operating_temperature`'.format(value))
            if value >= 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `case_operating_temperature`')
        self._data["Case Operating Temperature"] = value

    @property
    def latent_case_credit_curve_type(self):
        """Get latent_case_credit_curve_type

        Returns:
            str: the value of `latent_case_credit_curve_type` or None if not set
        """
        return self._data["Latent Case Credit Curve Type"]

    @latent_case_credit_curve_type.setter
    def latent_case_credit_curve_type(self, value="CaseTemperatureMethod"):
        """  Corresponds to IDD Field `Latent Case Credit Curve Type`

        Args:
            value (str): value for IDD Field `Latent Case Credit Curve Type`
                Accepted values are:
                      - CaseTemperatureMethod
                      - RelativeHumidityMethod
                      - DewpointMethod
                Default value: CaseTemperatureMethod
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
                                 'for field `latent_case_credit_curve_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `latent_case_credit_curve_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `latent_case_credit_curve_type`')
            vals = {}
            vals["casetemperaturemethod"] = "CaseTemperatureMethod"
            vals["relativehumiditymethod"] = "RelativeHumidityMethod"
            vals["dewpointmethod"] = "DewpointMethod"
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
                                     'field `latent_case_credit_curve_type`'.format(value))
            value = vals[value_lower]
        self._data["Latent Case Credit Curve Type"] = value

    @property
    def latent_case_credit_curve_name(self):
        """Get latent_case_credit_curve_name

        Returns:
            str: the value of `latent_case_credit_curve_name` or None if not set
        """
        return self._data["Latent Case Credit Curve Name"]

    @latent_case_credit_curve_name.setter
    def latent_case_credit_curve_name(self, value=None):
        """  Corresponds to IDD Field `Latent Case Credit Curve Name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `Latent Case Credit Curve Name`
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
                                 'for field `latent_case_credit_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `latent_case_credit_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `latent_case_credit_curve_name`')
        self._data["Latent Case Credit Curve Name"] = value

    @property
    def standard_case_fan_power_per_unit_length(self):
        """Get standard_case_fan_power_per_unit_length

        Returns:
            float: the value of `standard_case_fan_power_per_unit_length` or None if not set
        """
        return self._data["Standard Case Fan Power per Unit Length"]

    @standard_case_fan_power_per_unit_length.setter
    def standard_case_fan_power_per_unit_length(self, value=75.0):
        """  Corresponds to IDD Field `Standard Case Fan Power per Unit Length`

        Args:
            value (float): value for IDD Field `Standard Case Fan Power per Unit Length`
                Units: W/m
                Default value: 75.0
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
                                 'for field `standard_case_fan_power_per_unit_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `standard_case_fan_power_per_unit_length`')
        self._data["Standard Case Fan Power per Unit Length"] = value

    @property
    def operating_case_fan_power_per_unit_length(self):
        """Get operating_case_fan_power_per_unit_length

        Returns:
            float: the value of `operating_case_fan_power_per_unit_length` or None if not set
        """
        return self._data["Operating Case Fan Power per Unit Length"]

    @operating_case_fan_power_per_unit_length.setter
    def operating_case_fan_power_per_unit_length(self, value=75.0):
        """  Corresponds to IDD Field `Operating Case Fan Power per Unit Length`

        Args:
            value (float): value for IDD Field `Operating Case Fan Power per Unit Length`
                Units: W/m
                Default value: 75.0
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
                                 'for field `operating_case_fan_power_per_unit_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `operating_case_fan_power_per_unit_length`')
        self._data["Operating Case Fan Power per Unit Length"] = value

    @property
    def standard_case_lighting_power_per_unit_length(self):
        """Get standard_case_lighting_power_per_unit_length

        Returns:
            float: the value of `standard_case_lighting_power_per_unit_length` or None if not set
        """
        return self._data["Standard Case Lighting Power per Unit Length"]

    @standard_case_lighting_power_per_unit_length.setter
    def standard_case_lighting_power_per_unit_length(self, value=90.0):
        """  Corresponds to IDD Field `Standard Case Lighting Power per Unit Length`

        Args:
            value (float): value for IDD Field `Standard Case Lighting Power per Unit Length`
                Units: W/m
                Default value: 90.0
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
                                 'for field `standard_case_lighting_power_per_unit_length`'.format(value))
        self._data["Standard Case Lighting Power per Unit Length"] = value

    @property
    def installed_case_lighting_power_per_unit_length(self):
        """Get installed_case_lighting_power_per_unit_length

        Returns:
            float: the value of `installed_case_lighting_power_per_unit_length` or None if not set
        """
        return self._data["Installed Case Lighting Power per Unit Length"]

    @installed_case_lighting_power_per_unit_length.setter
    def installed_case_lighting_power_per_unit_length(self, value=None):
        """  Corresponds to IDD Field `Installed Case Lighting Power per Unit Length`
        default set equal to Standard Case Lighting Power per Unit Length

        Args:
            value (float): value for IDD Field `Installed Case Lighting Power per Unit Length`
                Units: W/m
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
                                 'for field `installed_case_lighting_power_per_unit_length`'.format(value))
        self._data["Installed Case Lighting Power per Unit Length"] = value

    @property
    def case_lighting_schedule_name(self):
        """Get case_lighting_schedule_name

        Returns:
            str: the value of `case_lighting_schedule_name` or None if not set
        """
        return self._data["Case Lighting Schedule Name"]

    @case_lighting_schedule_name.setter
    def case_lighting_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Case Lighting Schedule Name`

        Args:
            value (str): value for IDD Field `Case Lighting Schedule Name`
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
                                 'for field `case_lighting_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_lighting_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_lighting_schedule_name`')
        self._data["Case Lighting Schedule Name"] = value

    @property
    def fraction_of_lighting_energy_to_case(self):
        """Get fraction_of_lighting_energy_to_case

        Returns:
            float: the value of `fraction_of_lighting_energy_to_case` or None if not set
        """
        return self._data["Fraction of Lighting Energy to Case"]

    @fraction_of_lighting_energy_to_case.setter
    def fraction_of_lighting_energy_to_case(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Lighting Energy to Case`

        Args:
            value (float): value for IDD Field `Fraction of Lighting Energy to Case`
                Default value: 1.0
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
                                 'for field `fraction_of_lighting_energy_to_case`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_lighting_energy_to_case`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_lighting_energy_to_case`')
        self._data["Fraction of Lighting Energy to Case"] = value

    @property
    def case_antisweat_heater_power_per_unit_length(self):
        """Get case_antisweat_heater_power_per_unit_length

        Returns:
            float: the value of `case_antisweat_heater_power_per_unit_length` or None if not set
        """
        return self._data["Case Anti-Sweat Heater Power per Unit Length"]

    @case_antisweat_heater_power_per_unit_length.setter
    def case_antisweat_heater_power_per_unit_length(self, value=0.0):
        """  Corresponds to IDD Field `Case Anti-Sweat Heater Power per Unit Length`

        Args:
            value (float): value for IDD Field `Case Anti-Sweat Heater Power per Unit Length`
                Units: W/m
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
                                 'for field `case_antisweat_heater_power_per_unit_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `case_antisweat_heater_power_per_unit_length`')
        self._data["Case Anti-Sweat Heater Power per Unit Length"] = value

    @property
    def minimum_antisweat_heater_power_per_unit_length(self):
        """Get minimum_antisweat_heater_power_per_unit_length

        Returns:
            float: the value of `minimum_antisweat_heater_power_per_unit_length` or None if not set
        """
        return self._data["Minimum Anti-Sweat Heater Power per Unit Length"]

    @minimum_antisweat_heater_power_per_unit_length.setter
    def minimum_antisweat_heater_power_per_unit_length(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Anti-Sweat Heater Power per Unit Length`
        This field is only applicable to the Linear, Dewpoint Method, and
        Heat Balance Method anti-sweat heater control types

        Args:
            value (float): value for IDD Field `Minimum Anti-Sweat Heater Power per Unit Length`
                Units: W/m
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
                                 'for field `minimum_antisweat_heater_power_per_unit_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_antisweat_heater_power_per_unit_length`')
        self._data["Minimum Anti-Sweat Heater Power per Unit Length"] = value

    @property
    def antisweat_heater_control_type(self):
        """Get antisweat_heater_control_type

        Returns:
            str: the value of `antisweat_heater_control_type` or None if not set
        """
        return self._data["Anti-Sweat Heater Control Type"]

    @antisweat_heater_control_type.setter
    def antisweat_heater_control_type(self, value="None"):
        """  Corresponds to IDD Field `Anti-Sweat Heater Control Type`

        Args:
            value (str): value for IDD Field `Anti-Sweat Heater Control Type`
                Accepted values are:
                      - None
                      - Constant
                      - Linear
                      - DewpointMethod
                      - HeatBalanceMethod
                Default value: None
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
                                 'for field `antisweat_heater_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `antisweat_heater_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `antisweat_heater_control_type`')
            vals = {}
            vals["none"] = "None"
            vals["constant"] = "Constant"
            vals["linear"] = "Linear"
            vals["dewpointmethod"] = "DewpointMethod"
            vals["heatbalancemethod"] = "HeatBalanceMethod"
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
                                     'field `antisweat_heater_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Anti-Sweat Heater Control Type"] = value

    @property
    def humidity_at_zero_antisweat_heater_energy(self):
        """Get humidity_at_zero_antisweat_heater_energy

        Returns:
            float: the value of `humidity_at_zero_antisweat_heater_energy` or None if not set
        """
        return self._data["Humidity at Zero Anti-Sweat Heater Energy"]

    @humidity_at_zero_antisweat_heater_energy.setter
    def humidity_at_zero_antisweat_heater_energy(self, value=-10.0):
        """  Corresponds to IDD Field `Humidity at Zero Anti-Sweat Heater Energy`
        This field is only applicable to Linear AS heater control type
        Zone relative humidity (%) where anti-sweat heater energy is zero

        Args:
            value (float): value for IDD Field `Humidity at Zero Anti-Sweat Heater Energy`
                Units: percent
                Default value: -10.0
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
                                 'for field `humidity_at_zero_antisweat_heater_energy`'.format(value))
        self._data["Humidity at Zero Anti-Sweat Heater Energy"] = value

    @property
    def case_height(self):
        """Get case_height

        Returns:
            float: the value of `case_height` or None if not set
        """
        return self._data["Case Height"]

    @case_height.setter
    def case_height(self, value=1.5):
        """  Corresponds to IDD Field `Case Height`
        This field only applicable to Heat Balance Method AS heater control type
        Height must be greater than zero if Heat Balance Method AS heater control is selected

        Args:
            value (float): value for IDD Field `Case Height`
                Units: m
                Default value: 1.5
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
                                 'for field `case_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `case_height`')
        self._data["Case Height"] = value

    @property
    def fraction_of_antisweat_heater_energy_to_case(self):
        """Get fraction_of_antisweat_heater_energy_to_case

        Returns:
            float: the value of `fraction_of_antisweat_heater_energy_to_case` or None if not set
        """
        return self._data["Fraction of Anti-Sweat Heater Energy to Case"]

    @fraction_of_antisweat_heater_energy_to_case.setter
    def fraction_of_antisweat_heater_energy_to_case(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Anti-Sweat Heater Energy to Case`

        Args:
            value (float): value for IDD Field `Fraction of Anti-Sweat Heater Energy to Case`
                Default value: 1.0
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
                                 'for field `fraction_of_antisweat_heater_energy_to_case`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_antisweat_heater_energy_to_case`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_antisweat_heater_energy_to_case`')
        self._data["Fraction of Anti-Sweat Heater Energy to Case"] = value

    @property
    def case_defrost_power_per_unit_length(self):
        """Get case_defrost_power_per_unit_length

        Returns:
            float: the value of `case_defrost_power_per_unit_length` or None if not set
        """
        return self._data["Case Defrost Power per Unit Length"]

    @case_defrost_power_per_unit_length.setter
    def case_defrost_power_per_unit_length(self, value=0.0):
        """  Corresponds to IDD Field `Case Defrost Power per Unit Length`
        Used to evaluate load on case as well as power or heat consumption

        Args:
            value (float): value for IDD Field `Case Defrost Power per Unit Length`
                Units: W/m
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
                                 'for field `case_defrost_power_per_unit_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `case_defrost_power_per_unit_length`')
        self._data["Case Defrost Power per Unit Length"] = value

    @property
    def case_defrost_type(self):
        """Get case_defrost_type

        Returns:
            str: the value of `case_defrost_type` or None if not set
        """
        return self._data["Case Defrost Type"]

    @case_defrost_type.setter
    def case_defrost_type(self, value="OffCycle"):
        """  Corresponds to IDD Field `Case Defrost Type`

        Args:
            value (str): value for IDD Field `Case Defrost Type`
                Accepted values are:
                      - None
                      - OffCycle
                      - HotGas
                      - Electric
                      - HotFluid
                      - HotGasWithTemperatureTermination
                      - ElectricWithTemperatureTermination
                      - HotFluidWithTemperatureTermination
                Default value: OffCycle
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
                                 'for field `case_defrost_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_defrost_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_defrost_type`')
            vals = {}
            vals["none"] = "None"
            vals["offcycle"] = "OffCycle"
            vals["hotgas"] = "HotGas"
            vals["electric"] = "Electric"
            vals["hotfluid"] = "HotFluid"
            vals["hotgaswithtemperaturetermination"] = "HotGasWithTemperatureTermination"
            vals["electricwithtemperaturetermination"] = "ElectricWithTemperatureTermination"
            vals["hotfluidwithtemperaturetermination"] = "HotFluidWithTemperatureTermination"
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
                                     'field `case_defrost_type`'.format(value))
            value = vals[value_lower]
        self._data["Case Defrost Type"] = value

    @property
    def case_defrost_schedule_name(self):
        """Get case_defrost_schedule_name

        Returns:
            str: the value of `case_defrost_schedule_name` or None if not set
        """
        return self._data["Case Defrost Schedule Name"]

    @case_defrost_schedule_name.setter
    def case_defrost_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Case Defrost Schedule Name`
        A case defrost schedule name is required unless case defrost type = None

        Args:
            value (str): value for IDD Field `Case Defrost Schedule Name`
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
                                 'for field `case_defrost_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_defrost_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_defrost_schedule_name`')
        self._data["Case Defrost Schedule Name"] = value

    @property
    def case_defrost_dripdown_schedule_name(self):
        """Get case_defrost_dripdown_schedule_name

        Returns:
            str: the value of `case_defrost_dripdown_schedule_name` or None if not set
        """
        return self._data["Case Defrost Drip-Down Schedule Name"]

    @case_defrost_dripdown_schedule_name.setter
    def case_defrost_dripdown_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Case Defrost Drip-Down Schedule Name`
        If left blank, the defrost schedule will be used
        The start time for each defrost period in this drip-down schedule should coincide with
        the start time for each defrost period in the case defrost schedule (previous input
        field).The length of each defrost drip-down period must be greater than or equal to the
        corresponding defrost period specified in the case defrost schedule. This extra time
        allows the melted frost to drip from the coil before refrigeration is restarted.

        Args:
            value (str): value for IDD Field `Case Defrost Drip-Down Schedule Name`
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
                                 'for field `case_defrost_dripdown_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_defrost_dripdown_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_defrost_dripdown_schedule_name`')
        self._data["Case Defrost Drip-Down Schedule Name"] = value

    @property
    def defrost_energy_correction_curve_type(self):
        """Get defrost_energy_correction_curve_type

        Returns:
            str: the value of `defrost_energy_correction_curve_type` or None if not set
        """
        return self._data["Defrost Energy Correction Curve Type"]

    @defrost_energy_correction_curve_type.setter
    def defrost_energy_correction_curve_type(self, value="None"):
        """  Corresponds to IDD Field `Defrost Energy Correction Curve Type`
        Case Temperature, Relative Humidity, and Dewpoint Method are applicable to case defrost
        types with temperature termination only.

        Args:
            value (str): value for IDD Field `Defrost Energy Correction Curve Type`
                Accepted values are:
                      - None
                      - CaseTemperatureMethod
                      - RelativeHumidityMethod
                      - DewpointMethod
                Default value: None
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
                                 'for field `defrost_energy_correction_curve_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_energy_correction_curve_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_energy_correction_curve_type`')
            vals = {}
            vals["none"] = "None"
            vals["casetemperaturemethod"] = "CaseTemperatureMethod"
            vals["relativehumiditymethod"] = "RelativeHumidityMethod"
            vals["dewpointmethod"] = "DewpointMethod"
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
                                     'field `defrost_energy_correction_curve_type`'.format(value))
            value = vals[value_lower]
        self._data["Defrost Energy Correction Curve Type"] = value

    @property
    def defrost_energy_correction_curve_name(self):
        """Get defrost_energy_correction_curve_name

        Returns:
            str: the value of `defrost_energy_correction_curve_name` or None if not set
        """
        return self._data["Defrost Energy Correction Curve Name"]

    @defrost_energy_correction_curve_name.setter
    def defrost_energy_correction_curve_name(self, value=None):
        """  Corresponds to IDD Field `Defrost Energy Correction Curve Name`
        Table:OneIndependentVariable object can also be used
        Defrost Energy Correction Curve Name is applicable to case defrost types
        with temperature termination only.

        Args:
            value (str): value for IDD Field `Defrost Energy Correction Curve Name`
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
                                 'for field `defrost_energy_correction_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_energy_correction_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_energy_correction_curve_name`')
        self._data["Defrost Energy Correction Curve Name"] = value

    @property
    def under_case_hvac_return_air_fraction(self):
        """Get under_case_hvac_return_air_fraction

        Returns:
            float: the value of `under_case_hvac_return_air_fraction` or None if not set
        """
        return self._data["Under Case HVAC Return Air Fraction"]

    @under_case_hvac_return_air_fraction.setter
    def under_case_hvac_return_air_fraction(self, value=0.0):
        """  Corresponds to IDD Field `Under Case HVAC Return Air Fraction`

        Args:
            value (float): value for IDD Field `Under Case HVAC Return Air Fraction`
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
                                 'for field `under_case_hvac_return_air_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `under_case_hvac_return_air_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `under_case_hvac_return_air_fraction`')
        self._data["Under Case HVAC Return Air Fraction"] = value

    @property
    def refrigerated_case_restocking_schedule_name(self):
        """Get refrigerated_case_restocking_schedule_name

        Returns:
            str: the value of `refrigerated_case_restocking_schedule_name` or None if not set
        """
        return self._data["Refrigerated Case Restocking Schedule Name"]

    @refrigerated_case_restocking_schedule_name.setter
    def refrigerated_case_restocking_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Refrigerated Case Restocking Schedule Name`
        Schedule values should be in units of Watts per unit case length (W/m)
        Leave this field blank if no restocking is to be modeled

        Args:
            value (str): value for IDD Field `Refrigerated Case Restocking Schedule Name`
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
                                 'for field `refrigerated_case_restocking_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigerated_case_restocking_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigerated_case_restocking_schedule_name`')
        self._data["Refrigerated Case Restocking Schedule Name"] = value

    @property
    def case_credit_fraction_schedule_name(self):
        """Get case_credit_fraction_schedule_name

        Returns:
            str: the value of `case_credit_fraction_schedule_name` or None if not set
        """
        return self._data["Case Credit Fraction Schedule Name"]

    @case_credit_fraction_schedule_name.setter
    def case_credit_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Case Credit Fraction Schedule Name`
        Schedule values should be from 0 to 1
        Leave this field blank if no case credit fraction is to be applied

        Args:
            value (str): value for IDD Field `Case Credit Fraction Schedule Name`
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
                                 'for field `case_credit_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_credit_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_credit_fraction_schedule_name`')
        self._data["Case Credit Fraction Schedule Name"] = value

    @property
    def design_evaporator_temperature_or_brine_inlet_temperature(self):
        """Get design_evaporator_temperature_or_brine_inlet_temperature

        Returns:
            float: the value of `design_evaporator_temperature_or_brine_inlet_temperature` or None if not set
        """
        return self._data["Design Evaporator Temperature or Brine Inlet Temperature"]

    @design_evaporator_temperature_or_brine_inlet_temperature.setter
    def design_evaporator_temperature_or_brine_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Evaporator Temperature or Brine Inlet Temperature`
        Required for detailed refrigeration system, not for compressor rack
        For a DX system, enter the saturated temperature for refrigerant pressure leaving case
        For a brine-cooled cooled (secondary system) case, enter the brine inlet temperature
        Default is 5 C less than case operating temperature

        Args:
            value (float): value for IDD Field `Design Evaporator Temperature or Brine Inlet Temperature`
                Units: C
                value >= -70.0
                value <= 40.0
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
                                 'for field `design_evaporator_temperature_or_brine_inlet_temperature`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `design_evaporator_temperature_or_brine_inlet_temperature`')
            if value > 40.0:
                raise ValueError('value need to be smaller 40.0 '
                                 'for field `design_evaporator_temperature_or_brine_inlet_temperature`')
        self._data["Design Evaporator Temperature or Brine Inlet Temperature"] = value

    @property
    def average_refrigerant_charge_inventory(self):
        """Get average_refrigerant_charge_inventory

        Returns:
            float: the value of `average_refrigerant_charge_inventory` or None if not set
        """
        return self._data["Average Refrigerant Charge Inventory"]

    @average_refrigerant_charge_inventory.setter
    def average_refrigerant_charge_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Average Refrigerant Charge Inventory`

        Args:
            value (float): value for IDD Field `Average Refrigerant Charge Inventory`
                Units: kg/m
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
                                 'for field `average_refrigerant_charge_inventory`'.format(value))
        self._data["Average Refrigerant Charge Inventory"] = value

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

class RefrigerationCompressorRack(object):
    """ Corresponds to IDD object `Refrigeration:CompressorRack`
        Works in conjunction with the refrigeration case and walkin objects to simulate the
        performance of a refrigerated case system. This object models the electric
        consumption of the rack compressors and the condenser fans. Heat can be rejected
        eitheroutdoors or to a zone. Compressor rack waste heat can also be reclaimed for
        use by an optional air- or water-heating coil (Coil:Heating:Desuperheater and
        Coil:WaterHeating:Desuperheater).
    
    """
    internal_name = "Refrigeration:CompressorRack"
    field_count = 26
    required_fields = ["Name", "Compressor Rack COP Function of Temperature Curve Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:CompressorRack`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Heat Rejection Location"] = None
        self._data["Design Compressor Rack COP"] = None
        self._data["Compressor Rack COP Function of Temperature Curve Name"] = None
        self._data["Design Condenser Fan Power"] = None
        self._data["Condenser Fan Power Function of Temperature Curve Name"] = None
        self._data["Condenser Type"] = None
        self._data["Water-Cooled Condenser Inlet Node Name"] = None
        self._data["Water-Cooled Condenser Outlet Node Name"] = None
        self._data["Water-Cooled Loop Flow Type"] = None
        self._data["Water-Cooled Condenser Outlet Temperature Schedule Name"] = None
        self._data["Water-Cooled Condenser Design Flow Rate"] = None
        self._data["Water-Cooled Condenser Maximum Flow Rate"] = None
        self._data["Water-Cooled Condenser Maximum Water Outlet Temperature"] = None
        self._data["Water-Cooled Condenser Minimum Water Inlet Temperature"] = None
        self._data["Evaporative Condenser Availability Schedule Name"] = None
        self._data["Evaporative Condenser Effectiveness"] = None
        self._data["Evaporative Condenser Air Flow Rate"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Design Evaporative Condenser Water Pump Power"] = None
        self._data["Evaporative Water Supply Tank Name"] = None
        self._data["Condenser Air Inlet Node Name"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Refrigeration Case Name or WalkIn Name or CaseAndWalkInList Name"] = None
        self._data["Heat Rejection Zone Name"] = None
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
            self.heat_rejection_location = None
        else:
            self.heat_rejection_location = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_compressor_rack_cop = None
        else:
            self.design_compressor_rack_cop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compressor_rack_cop_function_of_temperature_curve_name = None
        else:
            self.compressor_rack_cop_function_of_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_condenser_fan_power = None
        else:
            self.design_condenser_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_fan_power_function_of_temperature_curve_name = None
        else:
            self.condenser_fan_power_function_of_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.watercooled_condenser_inlet_node_name = None
        else:
            self.watercooled_condenser_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.watercooled_condenser_outlet_node_name = None
        else:
            self.watercooled_condenser_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.watercooled_loop_flow_type = None
        else:
            self.watercooled_loop_flow_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.watercooled_condenser_outlet_temperature_schedule_name = None
        else:
            self.watercooled_condenser_outlet_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.watercooled_condenser_design_flow_rate = None
        else:
            self.watercooled_condenser_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.watercooled_condenser_maximum_flow_rate = None
        else:
            self.watercooled_condenser_maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.watercooled_condenser_maximum_water_outlet_temperature = None
        else:
            self.watercooled_condenser_maximum_water_outlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.watercooled_condenser_minimum_water_inlet_temperature = None
        else:
            self.watercooled_condenser_minimum_water_inlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporative_condenser_availability_schedule_name = None
        else:
            self.evaporative_condenser_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporative_condenser_effectiveness = None
        else:
            self.evaporative_condenser_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporative_condenser_air_flow_rate = None
        else:
            self.evaporative_condenser_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_evaporative_condenser_water_pump_power = None
        else:
            self.design_evaporative_condenser_water_pump_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporative_water_supply_tank_name = None
        else:
            self.evaporative_water_supply_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_air_inlet_node_name = None
        else:
            self.condenser_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name = None
        else:
            self.refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_rejection_zone_name = None
        else:
            self.heat_rejection_zone_name = vals[i]
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
    def heat_rejection_location(self):
        """Get heat_rejection_location

        Returns:
            str: the value of `heat_rejection_location` or None if not set
        """
        return self._data["Heat Rejection Location"]

    @heat_rejection_location.setter
    def heat_rejection_location(self, value="Outdoors"):
        """  Corresponds to IDD Field `Heat Rejection Location`

        Args:
            value (str): value for IDD Field `Heat Rejection Location`
                Accepted values are:
                      - Outdoors
                      - Zone
                Default value: Outdoors
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
                                 'for field `heat_rejection_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_rejection_location`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_rejection_location`')
            vals = {}
            vals["outdoors"] = "Outdoors"
            vals["zone"] = "Zone"
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
                                     'field `heat_rejection_location`'.format(value))
            value = vals[value_lower]
        self._data["Heat Rejection Location"] = value

    @property
    def design_compressor_rack_cop(self):
        """Get design_compressor_rack_cop

        Returns:
            float: the value of `design_compressor_rack_cop` or None if not set
        """
        return self._data["Design Compressor Rack COP"]

    @design_compressor_rack_cop.setter
    def design_compressor_rack_cop(self, value=2.0):
        """  Corresponds to IDD Field `Design Compressor Rack COP`
        It is important that this COP correspond to the lowest saturated suction
        temperature needed to serve all refrigeration loads

        Args:
            value (float): value for IDD Field `Design Compressor Rack COP`
                Units: W/W
                Default value: 2.0
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
                                 'for field `design_compressor_rack_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_compressor_rack_cop`')
        self._data["Design Compressor Rack COP"] = value

    @property
    def compressor_rack_cop_function_of_temperature_curve_name(self):
        """Get compressor_rack_cop_function_of_temperature_curve_name

        Returns:
            str: the value of `compressor_rack_cop_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Compressor Rack COP Function of Temperature Curve Name"]

    @compressor_rack_cop_function_of_temperature_curve_name.setter
    def compressor_rack_cop_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `Compressor Rack COP Function of Temperature Curve Name`
        Table:OneIndependentVariable object can also be used
        It is important that this COP curve correspond to the lowest saturated suction
        temperature needed to serve all refrigeration loads

        Args:
            value (str): value for IDD Field `Compressor Rack COP Function of Temperature Curve Name`
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
                                 'for field `compressor_rack_cop_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compressor_rack_cop_function_of_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `compressor_rack_cop_function_of_temperature_curve_name`')
        self._data["Compressor Rack COP Function of Temperature Curve Name"] = value

    @property
    def design_condenser_fan_power(self):
        """Get design_condenser_fan_power

        Returns:
            float: the value of `design_condenser_fan_power` or None if not set
        """
        return self._data["Design Condenser Fan Power"]

    @design_condenser_fan_power.setter
    def design_condenser_fan_power(self, value=250.0):
        """  Corresponds to IDD Field `Design Condenser Fan Power`
        Design power for condenser fan(s).

        Args:
            value (float): value for IDD Field `Design Condenser Fan Power`
                Units: W
                Default value: 250.0
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
                                 'for field `design_condenser_fan_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_condenser_fan_power`')
        self._data["Design Condenser Fan Power"] = value

    @property
    def condenser_fan_power_function_of_temperature_curve_name(self):
        """Get condenser_fan_power_function_of_temperature_curve_name

        Returns:
            str: the value of `condenser_fan_power_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Condenser Fan Power Function of Temperature Curve Name"]

    @condenser_fan_power_function_of_temperature_curve_name.setter
    def condenser_fan_power_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `Condenser Fan Power Function of Temperature Curve Name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `Condenser Fan Power Function of Temperature Curve Name`
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
                                 'for field `condenser_fan_power_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_fan_power_function_of_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_fan_power_function_of_temperature_curve_name`')
        self._data["Condenser Fan Power Function of Temperature Curve Name"] = value

    @property
    def condenser_type(self):
        """Get condenser_type

        Returns:
            str: the value of `condenser_type` or None if not set
        """
        return self._data["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="AirCooled"):
        """  Corresponds to IDD Field `Condenser Type`
        Applicable only when Heat Rejection Location is Outdoors.

        Args:
            value (str): value for IDD Field `Condenser Type`
                Accepted values are:
                      - AirCooled
                      - EvaporativelyCooled
                      - WaterCooled
                Default value: AirCooled
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
                                 'for field `condenser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_type`')
            vals = {}
            vals["aircooled"] = "AirCooled"
            vals["evaporativelycooled"] = "EvaporativelyCooled"
            vals["watercooled"] = "WaterCooled"
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
                                     'field `condenser_type`'.format(value))
            value = vals[value_lower]
        self._data["Condenser Type"] = value

    @property
    def watercooled_condenser_inlet_node_name(self):
        """Get watercooled_condenser_inlet_node_name

        Returns:
            str: the value of `watercooled_condenser_inlet_node_name` or None if not set
        """
        return self._data["Water-Cooled Condenser Inlet Node Name"]

    @watercooled_condenser_inlet_node_name.setter
    def watercooled_condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water-Cooled Condenser Inlet Node Name`

        Args:
            value (str): value for IDD Field `Water-Cooled Condenser Inlet Node Name`
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
                                 'for field `watercooled_condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `watercooled_condenser_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `watercooled_condenser_inlet_node_name`')
        self._data["Water-Cooled Condenser Inlet Node Name"] = value

    @property
    def watercooled_condenser_outlet_node_name(self):
        """Get watercooled_condenser_outlet_node_name

        Returns:
            str: the value of `watercooled_condenser_outlet_node_name` or None if not set
        """
        return self._data["Water-Cooled Condenser Outlet Node Name"]

    @watercooled_condenser_outlet_node_name.setter
    def watercooled_condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water-Cooled Condenser Outlet Node Name`

        Args:
            value (str): value for IDD Field `Water-Cooled Condenser Outlet Node Name`
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
                                 'for field `watercooled_condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `watercooled_condenser_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `watercooled_condenser_outlet_node_name`')
        self._data["Water-Cooled Condenser Outlet Node Name"] = value

    @property
    def watercooled_loop_flow_type(self):
        """Get watercooled_loop_flow_type

        Returns:
            str: the value of `watercooled_loop_flow_type` or None if not set
        """
        return self._data["Water-Cooled Loop Flow Type"]

    @watercooled_loop_flow_type.setter
    def watercooled_loop_flow_type(self, value="VariableFlow"):
        """  Corresponds to IDD Field `Water-Cooled Loop Flow Type`
        Applicable only when Condenser Type is WaterCooled.

        Args:
            value (str): value for IDD Field `Water-Cooled Loop Flow Type`
                Accepted values are:
                      - VariableFlow
                      - ConstantFlow
                Default value: VariableFlow
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
                                 'for field `watercooled_loop_flow_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `watercooled_loop_flow_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `watercooled_loop_flow_type`')
            vals = {}
            vals["variableflow"] = "VariableFlow"
            vals["constantflow"] = "ConstantFlow"
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
                                     'field `watercooled_loop_flow_type`'.format(value))
            value = vals[value_lower]
        self._data["Water-Cooled Loop Flow Type"] = value

    @property
    def watercooled_condenser_outlet_temperature_schedule_name(self):
        """Get watercooled_condenser_outlet_temperature_schedule_name

        Returns:
            str: the value of `watercooled_condenser_outlet_temperature_schedule_name` or None if not set
        """
        return self._data["Water-Cooled Condenser Outlet Temperature Schedule Name"]

    @watercooled_condenser_outlet_temperature_schedule_name.setter
    def watercooled_condenser_outlet_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Water-Cooled Condenser Outlet Temperature Schedule Name`
        Applicable only when loop Flow type is VariableFlow.

        Args:
            value (str): value for IDD Field `Water-Cooled Condenser Outlet Temperature Schedule Name`
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
                                 'for field `watercooled_condenser_outlet_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `watercooled_condenser_outlet_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `watercooled_condenser_outlet_temperature_schedule_name`')
        self._data["Water-Cooled Condenser Outlet Temperature Schedule Name"] = value

    @property
    def watercooled_condenser_design_flow_rate(self):
        """Get watercooled_condenser_design_flow_rate

        Returns:
            float: the value of `watercooled_condenser_design_flow_rate` or None if not set
        """
        return self._data["Water-Cooled Condenser Design Flow Rate"]

    @watercooled_condenser_design_flow_rate.setter
    def watercooled_condenser_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Water-Cooled Condenser Design Flow Rate`
        Applicable only when loop flow type is ConstantFlow.

        Args:
            value (float): value for IDD Field `Water-Cooled Condenser Design Flow Rate`
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
                                 'for field `watercooled_condenser_design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `watercooled_condenser_design_flow_rate`')
        self._data["Water-Cooled Condenser Design Flow Rate"] = value

    @property
    def watercooled_condenser_maximum_flow_rate(self):
        """Get watercooled_condenser_maximum_flow_rate

        Returns:
            float: the value of `watercooled_condenser_maximum_flow_rate` or None if not set
        """
        return self._data["Water-Cooled Condenser Maximum Flow Rate"]

    @watercooled_condenser_maximum_flow_rate.setter
    def watercooled_condenser_maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Water-Cooled Condenser Maximum Flow Rate`

        Args:
            value (float): value for IDD Field `Water-Cooled Condenser Maximum Flow Rate`
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
                                 'for field `watercooled_condenser_maximum_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `watercooled_condenser_maximum_flow_rate`')
        self._data["Water-Cooled Condenser Maximum Flow Rate"] = value

    @property
    def watercooled_condenser_maximum_water_outlet_temperature(self):
        """Get watercooled_condenser_maximum_water_outlet_temperature

        Returns:
            float: the value of `watercooled_condenser_maximum_water_outlet_temperature` or None if not set
        """
        return self._data["Water-Cooled Condenser Maximum Water Outlet Temperature"]

    @watercooled_condenser_maximum_water_outlet_temperature.setter
    def watercooled_condenser_maximum_water_outlet_temperature(self, value=55.0):
        """  Corresponds to IDD Field `Water-Cooled Condenser Maximum Water Outlet Temperature`

        Args:
            value (float): value for IDD Field `Water-Cooled Condenser Maximum Water Outlet Temperature`
                Units: C
                Default value: 55.0
                value >= 10.0
                value <= 60.0
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
                                 'for field `watercooled_condenser_maximum_water_outlet_temperature`'.format(value))
            if value < 10.0:
                raise ValueError('value need to be greater or equal 10.0 '
                                 'for field `watercooled_condenser_maximum_water_outlet_temperature`')
            if value > 60.0:
                raise ValueError('value need to be smaller 60.0 '
                                 'for field `watercooled_condenser_maximum_water_outlet_temperature`')
        self._data["Water-Cooled Condenser Maximum Water Outlet Temperature"] = value

    @property
    def watercooled_condenser_minimum_water_inlet_temperature(self):
        """Get watercooled_condenser_minimum_water_inlet_temperature

        Returns:
            float: the value of `watercooled_condenser_minimum_water_inlet_temperature` or None if not set
        """
        return self._data["Water-Cooled Condenser Minimum Water Inlet Temperature"]

    @watercooled_condenser_minimum_water_inlet_temperature.setter
    def watercooled_condenser_minimum_water_inlet_temperature(self, value=10.0):
        """  Corresponds to IDD Field `Water-Cooled Condenser Minimum Water Inlet Temperature`

        Args:
            value (float): value for IDD Field `Water-Cooled Condenser Minimum Water Inlet Temperature`
                Units: C
                Default value: 10.0
                value >= 10.0
                value <= 30.0
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
                                 'for field `watercooled_condenser_minimum_water_inlet_temperature`'.format(value))
            if value < 10.0:
                raise ValueError('value need to be greater or equal 10.0 '
                                 'for field `watercooled_condenser_minimum_water_inlet_temperature`')
            if value > 30.0:
                raise ValueError('value need to be smaller 30.0 '
                                 'for field `watercooled_condenser_minimum_water_inlet_temperature`')
        self._data["Water-Cooled Condenser Minimum Water Inlet Temperature"] = value

    @property
    def evaporative_condenser_availability_schedule_name(self):
        """Get evaporative_condenser_availability_schedule_name

        Returns:
            str: the value of `evaporative_condenser_availability_schedule_name` or None if not set
        """
        return self._data["Evaporative Condenser Availability Schedule Name"]

    @evaporative_condenser_availability_schedule_name.setter
    def evaporative_condenser_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Evaporative Condenser Availability Schedule Name`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Schedule values greater than 0 indicate that evaporative cooling of the
        condenser is available. This schedule allows the user to define seasonal
        shutdown/draining of the water cooling system in cold climate applications.
        For periods with schedule values of 0, the condenser operates as AirCooled.

        Args:
            value (str): value for IDD Field `Evaporative Condenser Availability Schedule Name`
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
                                 'for field `evaporative_condenser_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporative_condenser_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evaporative_condenser_availability_schedule_name`')
        self._data["Evaporative Condenser Availability Schedule Name"] = value

    @property
    def evaporative_condenser_effectiveness(self):
        """Get evaporative_condenser_effectiveness

        Returns:
            float: the value of `evaporative_condenser_effectiveness` or None if not set
        """
        return self._data["Evaporative Condenser Effectiveness"]

    @evaporative_condenser_effectiveness.setter
    def evaporative_condenser_effectiveness(self, value=0.9):
        """  Corresponds to IDD Field `Evaporative Condenser Effectiveness`
        Applicable only for Condenser Type = EvaporativlyCooled.

        Args:
            value (float): value for IDD Field `Evaporative Condenser Effectiveness`
                Units: dimensionless
                Default value: 0.9
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
                                 'for field `evaporative_condenser_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evaporative_condenser_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `evaporative_condenser_effectiveness`')
        self._data["Evaporative Condenser Effectiveness"] = value

    @property
    def evaporative_condenser_air_flow_rate(self):
        """Get evaporative_condenser_air_flow_rate

        Returns:
            float: the value of `evaporative_condenser_air_flow_rate` or None if not set
        """
        return self._data["Evaporative Condenser Air Flow Rate"]

    @evaporative_condenser_air_flow_rate.setter
    def evaporative_condenser_air_flow_rate(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Evaporative Condenser Air Flow Rate`
        Applicable only for Condenser Type = EvaporativelyCooled.
        Used to calculate evaporative condenser water use.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Evaporative Condenser Air Flow Rate`
                Units: m3/s
                Default value: "Autocalculate"
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Evaporative Condenser Air Flow Rate"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `evaporative_condenser_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `evaporative_condenser_air_flow_rate`')
        self._data["Evaporative Condenser Air Flow Rate"] = value

    @property
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=200.0):
        """  Corresponds to IDD Field `Basin Heater Capacity`
        This field is only used for Condenser Type = EvaporativelyCooled and for periods
        when the evaporatively cooled condenser is available (field Evaporative Condenser Availability
        Schedule Name). For this situation, the heater heats the basin water when the
        outdoor air dry-bulb temperature falls below the setpoint temperature, but
        only when the condenser fans are off (i.e., no refrigerated case load).

        Args:
            value (float): value for IDD Field `Basin Heater Capacity`
                Units: W/K
                Default value: 200.0
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
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')
        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0):
        """  Corresponds to IDD Field `Basin Heater Setpoint Temperature`
        Enter the outdoor dry-bulb temperature at which the basin heater turns on.

        Args:
            value (float): value for IDD Field `Basin Heater Setpoint Temperature`
                Units: C
                Default value: 2.0
                value >= 2.0
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
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')
        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def design_evaporative_condenser_water_pump_power(self):
        """Get design_evaporative_condenser_water_pump_power

        Returns:
            float: the value of `design_evaporative_condenser_water_pump_power` or None if not set
        """
        return self._data["Design Evaporative Condenser Water Pump Power"]

    @design_evaporative_condenser_water_pump_power.setter
    def design_evaporative_condenser_water_pump_power(self, value=1000.0):
        """  Corresponds to IDD Field `Design Evaporative Condenser Water Pump Power`
        Design recirc water pump power for Condenser Type = EvaporativelyCooled.
        Applicable only for Condenser Type = EvaporativelyCooled.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Design Evaporative Condenser Water Pump Power`
                Units: W
                Default value: 1000.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Design Evaporative Condenser Water Pump Power"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_evaporative_condenser_water_pump_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_evaporative_condenser_water_pump_power`')
        self._data["Design Evaporative Condenser Water Pump Power"] = value

    @property
    def evaporative_water_supply_tank_name(self):
        """Get evaporative_water_supply_tank_name

        Returns:
            str: the value of `evaporative_water_supply_tank_name` or None if not set
        """
        return self._data["Evaporative Water Supply Tank Name"]

    @evaporative_water_supply_tank_name.setter
    def evaporative_water_supply_tank_name(self, value=None):
        """  Corresponds to IDD Field `Evaporative Water Supply Tank Name`
        If blank, water supply is from Mains.
        Applicable only for Condenser Type = EvaporativelyCooled.

        Args:
            value (str): value for IDD Field `Evaporative Water Supply Tank Name`
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
                                 'for field `evaporative_water_supply_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporative_water_supply_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evaporative_water_supply_tank_name`')
        self._data["Evaporative Water Supply Tank Name"] = value

    @property
    def condenser_air_inlet_node_name(self):
        """Get condenser_air_inlet_node_name

        Returns:
            str: the value of `condenser_air_inlet_node_name` or None if not set
        """
        return self._data["Condenser Air Inlet Node Name"]

    @condenser_air_inlet_node_name.setter
    def condenser_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Condenser Air Inlet Node Name`
        Applicable only when Heat Rejection Location is Outdoors and Condenser Type is
        not WaterCooled; otherwise, leave field blank. If field is left blank with
        Heat Rejection Location = Outdoors, then the model assumes that the Inlet Air
        conditions are the outdoor air conditions for the current timestep
        (e.g., no adjustment for height above ground).

        Args:
            value (str): value for IDD Field `Condenser Air Inlet Node Name`
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
                                 'for field `condenser_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_air_inlet_node_name`')
        self._data["Condenser Air Inlet Node Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    @property
    def refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name(self):
        """Get refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name

        Returns:
            str: the value of `refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name` or None if not set
        """
        return self._data["Refrigeration Case Name or WalkIn Name or CaseAndWalkInList Name"]

    @refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name.setter
    def refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Case Name or WalkIn Name or CaseAndWalkInList Name`
        Enter the name of a Refrigeration:Case or Refrigeration:Walkin or
        Refrigeration:CaseAndWalkinList object.

        Args:
            value (str): value for IDD Field `Refrigeration Case Name or WalkIn Name or CaseAndWalkInList Name`
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
                                 'for field `refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name`')
        self._data["Refrigeration Case Name or WalkIn Name or CaseAndWalkInList Name"] = value

    @property
    def heat_rejection_zone_name(self):
        """Get heat_rejection_zone_name

        Returns:
            str: the value of `heat_rejection_zone_name` or None if not set
        """
        return self._data["Heat Rejection Zone Name"]

    @heat_rejection_zone_name.setter
    def heat_rejection_zone_name(self, value=None):
        """  Corresponds to IDD Field `Heat Rejection Zone Name`
        This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object.
        Required only if walk-in[s] are connected to this rack
        AND the heat rejection location is "Zone"

        Args:
            value (str): value for IDD Field `Heat Rejection Zone Name`
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
                                 'for field `heat_rejection_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_rejection_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_rejection_zone_name`')
        self._data["Heat Rejection Zone Name"] = value

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

class RefrigerationCaseAndWalkInList(object):
    """ Corresponds to IDD object `Refrigeration:CaseAndWalkInList`
        Provides a list of all the refrigerated cases, walk in coolers, or air chillers
        cooled by a single refrigeration system.  Note that the names of all cases,
        walk-ins ,air chillers, and CaseAndWalkInLists must be unique.  That is, you cannot
        give a list the same name as one of list items. This list may contain a combination
        of case and walk-in names OR a list of air chiller names.  Air chillers
        may not be included in any list that also includes cases or walk-ins.
    
    """
    internal_name = "Refrigeration:CaseAndWalkInList"
    field_count = 41
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:CaseAndWalkInList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Case or WalkIn 1 Name"] = None
        self._data["Case or WalkIn 2 Name"] = None
        self._data["Case or WalkIn 3 Name"] = None
        self._data["Case or WalkIn 4 Name"] = None
        self._data["Case or WalkIn 5 Name"] = None
        self._data["Case or WalkIn 6 Name"] = None
        self._data["Case or WalkIn 7 Name"] = None
        self._data["Case or WalkIn 8 Name"] = None
        self._data["Case or WalkIn 9 Name"] = None
        self._data["Case or WalkIn 10 Name"] = None
        self._data["Case or WalkIn 11 Name"] = None
        self._data["Case or WalkIn 12 Name"] = None
        self._data["Case or WalkIn 13 Name"] = None
        self._data["Case or WalkIn 14 Name"] = None
        self._data["Case or WalkIn 15 Name"] = None
        self._data["Case or WalkIn 16 Name"] = None
        self._data["Case or WalkIn 17 Name"] = None
        self._data["Case or WalkIn 18 Name"] = None
        self._data["Case or WalkIn 19 Name"] = None
        self._data["Case or WalkIn 20 Name"] = None
        self._data["Case or WalkIn 21 Name"] = None
        self._data["Case or WalkIn 22 Name"] = None
        self._data["Case or WalkIn 23 Name"] = None
        self._data["Case or WalkIn 24 Name"] = None
        self._data["Case or WalkIn 25 Name"] = None
        self._data["Case or WalkIn 26 Name"] = None
        self._data["Case or WalkIn 27 Name"] = None
        self._data["Case or WalkIn 28 Name"] = None
        self._data["Case or WalkIn 29 Name"] = None
        self._data["Case or WalkIn 30 Name"] = None
        self._data["Case or WalkIn 31 Name"] = None
        self._data["Case or WalkIn 32 Name"] = None
        self._data["Case or WalkIn 33 Name"] = None
        self._data["Case or WalkIn 34 Name"] = None
        self._data["Case or WalkIn 35 Name"] = None
        self._data["Case or WalkIn 36 Name"] = None
        self._data["Case or WalkIn 37 Name"] = None
        self._data["Case or WalkIn 38 Name"] = None
        self._data["Case or WalkIn 39 Name"] = None
        self._data["Case or WalkIn 40 Name"] = None
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
            self.case_or_walkin_1_name = None
        else:
            self.case_or_walkin_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_2_name = None
        else:
            self.case_or_walkin_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_3_name = None
        else:
            self.case_or_walkin_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_4_name = None
        else:
            self.case_or_walkin_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_5_name = None
        else:
            self.case_or_walkin_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_6_name = None
        else:
            self.case_or_walkin_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_7_name = None
        else:
            self.case_or_walkin_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_8_name = None
        else:
            self.case_or_walkin_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_9_name = None
        else:
            self.case_or_walkin_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_10_name = None
        else:
            self.case_or_walkin_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_11_name = None
        else:
            self.case_or_walkin_11_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_12_name = None
        else:
            self.case_or_walkin_12_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_13_name = None
        else:
            self.case_or_walkin_13_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_14_name = None
        else:
            self.case_or_walkin_14_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_15_name = None
        else:
            self.case_or_walkin_15_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_16_name = None
        else:
            self.case_or_walkin_16_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_17_name = None
        else:
            self.case_or_walkin_17_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_18_name = None
        else:
            self.case_or_walkin_18_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_19_name = None
        else:
            self.case_or_walkin_19_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_20_name = None
        else:
            self.case_or_walkin_20_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_21_name = None
        else:
            self.case_or_walkin_21_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_22_name = None
        else:
            self.case_or_walkin_22_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_23_name = None
        else:
            self.case_or_walkin_23_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_24_name = None
        else:
            self.case_or_walkin_24_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_25_name = None
        else:
            self.case_or_walkin_25_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_26_name = None
        else:
            self.case_or_walkin_26_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_27_name = None
        else:
            self.case_or_walkin_27_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_28_name = None
        else:
            self.case_or_walkin_28_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_29_name = None
        else:
            self.case_or_walkin_29_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_30_name = None
        else:
            self.case_or_walkin_30_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_31_name = None
        else:
            self.case_or_walkin_31_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_32_name = None
        else:
            self.case_or_walkin_32_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_33_name = None
        else:
            self.case_or_walkin_33_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_34_name = None
        else:
            self.case_or_walkin_34_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_35_name = None
        else:
            self.case_or_walkin_35_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_36_name = None
        else:
            self.case_or_walkin_36_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_37_name = None
        else:
            self.case_or_walkin_37_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_38_name = None
        else:
            self.case_or_walkin_38_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_39_name = None
        else:
            self.case_or_walkin_39_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.case_or_walkin_40_name = None
        else:
            self.case_or_walkin_40_name = vals[i]
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
    def case_or_walkin_1_name(self):
        """Get case_or_walkin_1_name

        Returns:
            str: the value of `case_or_walkin_1_name` or None if not set
        """
        return self._data["Case or WalkIn 1 Name"]

    @case_or_walkin_1_name.setter
    def case_or_walkin_1_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 1 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 1 Name`
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
                                 'for field `case_or_walkin_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_1_name`')
        self._data["Case or WalkIn 1 Name"] = value

    @property
    def case_or_walkin_2_name(self):
        """Get case_or_walkin_2_name

        Returns:
            str: the value of `case_or_walkin_2_name` or None if not set
        """
        return self._data["Case or WalkIn 2 Name"]

    @case_or_walkin_2_name.setter
    def case_or_walkin_2_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 2 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 2 Name`
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
                                 'for field `case_or_walkin_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_2_name`')
        self._data["Case or WalkIn 2 Name"] = value

    @property
    def case_or_walkin_3_name(self):
        """Get case_or_walkin_3_name

        Returns:
            str: the value of `case_or_walkin_3_name` or None if not set
        """
        return self._data["Case or WalkIn 3 Name"]

    @case_or_walkin_3_name.setter
    def case_or_walkin_3_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 3 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 3 Name`
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
                                 'for field `case_or_walkin_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_3_name`')
        self._data["Case or WalkIn 3 Name"] = value

    @property
    def case_or_walkin_4_name(self):
        """Get case_or_walkin_4_name

        Returns:
            str: the value of `case_or_walkin_4_name` or None if not set
        """
        return self._data["Case or WalkIn 4 Name"]

    @case_or_walkin_4_name.setter
    def case_or_walkin_4_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 4 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 4 Name`
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
                                 'for field `case_or_walkin_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_4_name`')
        self._data["Case or WalkIn 4 Name"] = value

    @property
    def case_or_walkin_5_name(self):
        """Get case_or_walkin_5_name

        Returns:
            str: the value of `case_or_walkin_5_name` or None if not set
        """
        return self._data["Case or WalkIn 5 Name"]

    @case_or_walkin_5_name.setter
    def case_or_walkin_5_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 5 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 5 Name`
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
                                 'for field `case_or_walkin_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_5_name`')
        self._data["Case or WalkIn 5 Name"] = value

    @property
    def case_or_walkin_6_name(self):
        """Get case_or_walkin_6_name

        Returns:
            str: the value of `case_or_walkin_6_name` or None if not set
        """
        return self._data["Case or WalkIn 6 Name"]

    @case_or_walkin_6_name.setter
    def case_or_walkin_6_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 6 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 6 Name`
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
                                 'for field `case_or_walkin_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_6_name`')
        self._data["Case or WalkIn 6 Name"] = value

    @property
    def case_or_walkin_7_name(self):
        """Get case_or_walkin_7_name

        Returns:
            str: the value of `case_or_walkin_7_name` or None if not set
        """
        return self._data["Case or WalkIn 7 Name"]

    @case_or_walkin_7_name.setter
    def case_or_walkin_7_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 7 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 7 Name`
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
                                 'for field `case_or_walkin_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_7_name`')
        self._data["Case or WalkIn 7 Name"] = value

    @property
    def case_or_walkin_8_name(self):
        """Get case_or_walkin_8_name

        Returns:
            str: the value of `case_or_walkin_8_name` or None if not set
        """
        return self._data["Case or WalkIn 8 Name"]

    @case_or_walkin_8_name.setter
    def case_or_walkin_8_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 8 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 8 Name`
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
                                 'for field `case_or_walkin_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_8_name`')
        self._data["Case or WalkIn 8 Name"] = value

    @property
    def case_or_walkin_9_name(self):
        """Get case_or_walkin_9_name

        Returns:
            str: the value of `case_or_walkin_9_name` or None if not set
        """
        return self._data["Case or WalkIn 9 Name"]

    @case_or_walkin_9_name.setter
    def case_or_walkin_9_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 9 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 9 Name`
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
                                 'for field `case_or_walkin_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_9_name`')
        self._data["Case or WalkIn 9 Name"] = value

    @property
    def case_or_walkin_10_name(self):
        """Get case_or_walkin_10_name

        Returns:
            str: the value of `case_or_walkin_10_name` or None if not set
        """
        return self._data["Case or WalkIn 10 Name"]

    @case_or_walkin_10_name.setter
    def case_or_walkin_10_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 10 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 10 Name`
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
                                 'for field `case_or_walkin_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_10_name`')
        self._data["Case or WalkIn 10 Name"] = value

    @property
    def case_or_walkin_11_name(self):
        """Get case_or_walkin_11_name

        Returns:
            str: the value of `case_or_walkin_11_name` or None if not set
        """
        return self._data["Case or WalkIn 11 Name"]

    @case_or_walkin_11_name.setter
    def case_or_walkin_11_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 11 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 11 Name`
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
                                 'for field `case_or_walkin_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_11_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_11_name`')
        self._data["Case or WalkIn 11 Name"] = value

    @property
    def case_or_walkin_12_name(self):
        """Get case_or_walkin_12_name

        Returns:
            str: the value of `case_or_walkin_12_name` or None if not set
        """
        return self._data["Case or WalkIn 12 Name"]

    @case_or_walkin_12_name.setter
    def case_or_walkin_12_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 12 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 12 Name`
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
                                 'for field `case_or_walkin_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_12_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_12_name`')
        self._data["Case or WalkIn 12 Name"] = value

    @property
    def case_or_walkin_13_name(self):
        """Get case_or_walkin_13_name

        Returns:
            str: the value of `case_or_walkin_13_name` or None if not set
        """
        return self._data["Case or WalkIn 13 Name"]

    @case_or_walkin_13_name.setter
    def case_or_walkin_13_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 13 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 13 Name`
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
                                 'for field `case_or_walkin_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_13_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_13_name`')
        self._data["Case or WalkIn 13 Name"] = value

    @property
    def case_or_walkin_14_name(self):
        """Get case_or_walkin_14_name

        Returns:
            str: the value of `case_or_walkin_14_name` or None if not set
        """
        return self._data["Case or WalkIn 14 Name"]

    @case_or_walkin_14_name.setter
    def case_or_walkin_14_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 14 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 14 Name`
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
                                 'for field `case_or_walkin_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_14_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_14_name`')
        self._data["Case or WalkIn 14 Name"] = value

    @property
    def case_or_walkin_15_name(self):
        """Get case_or_walkin_15_name

        Returns:
            str: the value of `case_or_walkin_15_name` or None if not set
        """
        return self._data["Case or WalkIn 15 Name"]

    @case_or_walkin_15_name.setter
    def case_or_walkin_15_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 15 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 15 Name`
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
                                 'for field `case_or_walkin_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_15_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_15_name`')
        self._data["Case or WalkIn 15 Name"] = value

    @property
    def case_or_walkin_16_name(self):
        """Get case_or_walkin_16_name

        Returns:
            str: the value of `case_or_walkin_16_name` or None if not set
        """
        return self._data["Case or WalkIn 16 Name"]

    @case_or_walkin_16_name.setter
    def case_or_walkin_16_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 16 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 16 Name`
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
                                 'for field `case_or_walkin_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_16_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_16_name`')
        self._data["Case or WalkIn 16 Name"] = value

    @property
    def case_or_walkin_17_name(self):
        """Get case_or_walkin_17_name

        Returns:
            str: the value of `case_or_walkin_17_name` or None if not set
        """
        return self._data["Case or WalkIn 17 Name"]

    @case_or_walkin_17_name.setter
    def case_or_walkin_17_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 17 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 17 Name`
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
                                 'for field `case_or_walkin_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_17_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_17_name`')
        self._data["Case or WalkIn 17 Name"] = value

    @property
    def case_or_walkin_18_name(self):
        """Get case_or_walkin_18_name

        Returns:
            str: the value of `case_or_walkin_18_name` or None if not set
        """
        return self._data["Case or WalkIn 18 Name"]

    @case_or_walkin_18_name.setter
    def case_or_walkin_18_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 18 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 18 Name`
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
                                 'for field `case_or_walkin_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_18_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_18_name`')
        self._data["Case or WalkIn 18 Name"] = value

    @property
    def case_or_walkin_19_name(self):
        """Get case_or_walkin_19_name

        Returns:
            str: the value of `case_or_walkin_19_name` or None if not set
        """
        return self._data["Case or WalkIn 19 Name"]

    @case_or_walkin_19_name.setter
    def case_or_walkin_19_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 19 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 19 Name`
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
                                 'for field `case_or_walkin_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_19_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_19_name`')
        self._data["Case or WalkIn 19 Name"] = value

    @property
    def case_or_walkin_20_name(self):
        """Get case_or_walkin_20_name

        Returns:
            str: the value of `case_or_walkin_20_name` or None if not set
        """
        return self._data["Case or WalkIn 20 Name"]

    @case_or_walkin_20_name.setter
    def case_or_walkin_20_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 20 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 20 Name`
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
                                 'for field `case_or_walkin_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_20_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_20_name`')
        self._data["Case or WalkIn 20 Name"] = value

    @property
    def case_or_walkin_21_name(self):
        """Get case_or_walkin_21_name

        Returns:
            str: the value of `case_or_walkin_21_name` or None if not set
        """
        return self._data["Case or WalkIn 21 Name"]

    @case_or_walkin_21_name.setter
    def case_or_walkin_21_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 21 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 21 Name`
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
                                 'for field `case_or_walkin_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_21_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_21_name`')
        self._data["Case or WalkIn 21 Name"] = value

    @property
    def case_or_walkin_22_name(self):
        """Get case_or_walkin_22_name

        Returns:
            str: the value of `case_or_walkin_22_name` or None if not set
        """
        return self._data["Case or WalkIn 22 Name"]

    @case_or_walkin_22_name.setter
    def case_or_walkin_22_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 22 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 22 Name`
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
                                 'for field `case_or_walkin_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_22_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_22_name`')
        self._data["Case or WalkIn 22 Name"] = value

    @property
    def case_or_walkin_23_name(self):
        """Get case_or_walkin_23_name

        Returns:
            str: the value of `case_or_walkin_23_name` or None if not set
        """
        return self._data["Case or WalkIn 23 Name"]

    @case_or_walkin_23_name.setter
    def case_or_walkin_23_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 23 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 23 Name`
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
                                 'for field `case_or_walkin_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_23_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_23_name`')
        self._data["Case or WalkIn 23 Name"] = value

    @property
    def case_or_walkin_24_name(self):
        """Get case_or_walkin_24_name

        Returns:
            str: the value of `case_or_walkin_24_name` or None if not set
        """
        return self._data["Case or WalkIn 24 Name"]

    @case_or_walkin_24_name.setter
    def case_or_walkin_24_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 24 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 24 Name`
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
                                 'for field `case_or_walkin_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_24_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_24_name`')
        self._data["Case or WalkIn 24 Name"] = value

    @property
    def case_or_walkin_25_name(self):
        """Get case_or_walkin_25_name

        Returns:
            str: the value of `case_or_walkin_25_name` or None if not set
        """
        return self._data["Case or WalkIn 25 Name"]

    @case_or_walkin_25_name.setter
    def case_or_walkin_25_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 25 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 25 Name`
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
                                 'for field `case_or_walkin_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_25_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_25_name`')
        self._data["Case or WalkIn 25 Name"] = value

    @property
    def case_or_walkin_26_name(self):
        """Get case_or_walkin_26_name

        Returns:
            str: the value of `case_or_walkin_26_name` or None if not set
        """
        return self._data["Case or WalkIn 26 Name"]

    @case_or_walkin_26_name.setter
    def case_or_walkin_26_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 26 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 26 Name`
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
                                 'for field `case_or_walkin_26_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_26_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_26_name`')
        self._data["Case or WalkIn 26 Name"] = value

    @property
    def case_or_walkin_27_name(self):
        """Get case_or_walkin_27_name

        Returns:
            str: the value of `case_or_walkin_27_name` or None if not set
        """
        return self._data["Case or WalkIn 27 Name"]

    @case_or_walkin_27_name.setter
    def case_or_walkin_27_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 27 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 27 Name`
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
                                 'for field `case_or_walkin_27_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_27_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_27_name`')
        self._data["Case or WalkIn 27 Name"] = value

    @property
    def case_or_walkin_28_name(self):
        """Get case_or_walkin_28_name

        Returns:
            str: the value of `case_or_walkin_28_name` or None if not set
        """
        return self._data["Case or WalkIn 28 Name"]

    @case_or_walkin_28_name.setter
    def case_or_walkin_28_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 28 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 28 Name`
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
                                 'for field `case_or_walkin_28_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_28_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_28_name`')
        self._data["Case or WalkIn 28 Name"] = value

    @property
    def case_or_walkin_29_name(self):
        """Get case_or_walkin_29_name

        Returns:
            str: the value of `case_or_walkin_29_name` or None if not set
        """
        return self._data["Case or WalkIn 29 Name"]

    @case_or_walkin_29_name.setter
    def case_or_walkin_29_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 29 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 29 Name`
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
                                 'for field `case_or_walkin_29_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_29_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_29_name`')
        self._data["Case or WalkIn 29 Name"] = value

    @property
    def case_or_walkin_30_name(self):
        """Get case_or_walkin_30_name

        Returns:
            str: the value of `case_or_walkin_30_name` or None if not set
        """
        return self._data["Case or WalkIn 30 Name"]

    @case_or_walkin_30_name.setter
    def case_or_walkin_30_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 30 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 30 Name`
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
                                 'for field `case_or_walkin_30_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_30_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_30_name`')
        self._data["Case or WalkIn 30 Name"] = value

    @property
    def case_or_walkin_31_name(self):
        """Get case_or_walkin_31_name

        Returns:
            str: the value of `case_or_walkin_31_name` or None if not set
        """
        return self._data["Case or WalkIn 31 Name"]

    @case_or_walkin_31_name.setter
    def case_or_walkin_31_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 31 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 31 Name`
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
                                 'for field `case_or_walkin_31_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_31_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_31_name`')
        self._data["Case or WalkIn 31 Name"] = value

    @property
    def case_or_walkin_32_name(self):
        """Get case_or_walkin_32_name

        Returns:
            str: the value of `case_or_walkin_32_name` or None if not set
        """
        return self._data["Case or WalkIn 32 Name"]

    @case_or_walkin_32_name.setter
    def case_or_walkin_32_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 32 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 32 Name`
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
                                 'for field `case_or_walkin_32_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_32_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_32_name`')
        self._data["Case or WalkIn 32 Name"] = value

    @property
    def case_or_walkin_33_name(self):
        """Get case_or_walkin_33_name

        Returns:
            str: the value of `case_or_walkin_33_name` or None if not set
        """
        return self._data["Case or WalkIn 33 Name"]

    @case_or_walkin_33_name.setter
    def case_or_walkin_33_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 33 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 33 Name`
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
                                 'for field `case_or_walkin_33_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_33_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_33_name`')
        self._data["Case or WalkIn 33 Name"] = value

    @property
    def case_or_walkin_34_name(self):
        """Get case_or_walkin_34_name

        Returns:
            str: the value of `case_or_walkin_34_name` or None if not set
        """
        return self._data["Case or WalkIn 34 Name"]

    @case_or_walkin_34_name.setter
    def case_or_walkin_34_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 34 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 34 Name`
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
                                 'for field `case_or_walkin_34_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_34_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_34_name`')
        self._data["Case or WalkIn 34 Name"] = value

    @property
    def case_or_walkin_35_name(self):
        """Get case_or_walkin_35_name

        Returns:
            str: the value of `case_or_walkin_35_name` or None if not set
        """
        return self._data["Case or WalkIn 35 Name"]

    @case_or_walkin_35_name.setter
    def case_or_walkin_35_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 35 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 35 Name`
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
                                 'for field `case_or_walkin_35_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_35_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_35_name`')
        self._data["Case or WalkIn 35 Name"] = value

    @property
    def case_or_walkin_36_name(self):
        """Get case_or_walkin_36_name

        Returns:
            str: the value of `case_or_walkin_36_name` or None if not set
        """
        return self._data["Case or WalkIn 36 Name"]

    @case_or_walkin_36_name.setter
    def case_or_walkin_36_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 36 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 36 Name`
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
                                 'for field `case_or_walkin_36_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_36_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_36_name`')
        self._data["Case or WalkIn 36 Name"] = value

    @property
    def case_or_walkin_37_name(self):
        """Get case_or_walkin_37_name

        Returns:
            str: the value of `case_or_walkin_37_name` or None if not set
        """
        return self._data["Case or WalkIn 37 Name"]

    @case_or_walkin_37_name.setter
    def case_or_walkin_37_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 37 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 37 Name`
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
                                 'for field `case_or_walkin_37_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_37_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_37_name`')
        self._data["Case or WalkIn 37 Name"] = value

    @property
    def case_or_walkin_38_name(self):
        """Get case_or_walkin_38_name

        Returns:
            str: the value of `case_or_walkin_38_name` or None if not set
        """
        return self._data["Case or WalkIn 38 Name"]

    @case_or_walkin_38_name.setter
    def case_or_walkin_38_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 38 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 38 Name`
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
                                 'for field `case_or_walkin_38_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_38_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_38_name`')
        self._data["Case or WalkIn 38 Name"] = value

    @property
    def case_or_walkin_39_name(self):
        """Get case_or_walkin_39_name

        Returns:
            str: the value of `case_or_walkin_39_name` or None if not set
        """
        return self._data["Case or WalkIn 39 Name"]

    @case_or_walkin_39_name.setter
    def case_or_walkin_39_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 39 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 39 Name`
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
                                 'for field `case_or_walkin_39_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_39_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_39_name`')
        self._data["Case or WalkIn 39 Name"] = value

    @property
    def case_or_walkin_40_name(self):
        """Get case_or_walkin_40_name

        Returns:
            str: the value of `case_or_walkin_40_name` or None if not set
        """
        return self._data["Case or WalkIn 40 Name"]

    @case_or_walkin_40_name.setter
    def case_or_walkin_40_name(self, value=None):
        """  Corresponds to IDD Field `Case or WalkIn 40 Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.

        Args:
            value (str): value for IDD Field `Case or WalkIn 40 Name`
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
                                 'for field `case_or_walkin_40_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `case_or_walkin_40_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `case_or_walkin_40_name`')
        self._data["Case or WalkIn 40 Name"] = value

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

class RefrigerationCondenserAirCooled(object):
    """ Corresponds to IDD object `Refrigeration:Condenser:AirCooled`
        Air cooled condenser for a refrigeration system (Refrigeration:System).
    
    """
    internal_name = "Refrigeration:Condenser:AirCooled"
    field_count = 11
    required_fields = ["Name", "Rated Fan Power"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:Condenser:AirCooled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Rated Effective Total Heat Rejection Rate Curve Name"] = None
        self._data["Rated Subcooling Temperature Difference"] = None
        self._data["Condenser Fan Speed Control Type"] = None
        self._data["Rated Fan Power"] = None
        self._data["Minimum Fan Air Flow Ratio"] = None
        self._data["Air Inlet Node Name or Zone Name"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Condenser Refrigerant Operating Charge Inventory"] = None
        self._data["Condensate Receiver Refrigerant Inventory"] = None
        self._data["Condensate Piping Refrigerant Inventory"] = None
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
            self.rated_effective_total_heat_rejection_rate_curve_name = None
        else:
            self.rated_effective_total_heat_rejection_rate_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_subcooling_temperature_difference = None
        else:
            self.rated_subcooling_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_fan_speed_control_type = None
        else:
            self.condenser_fan_speed_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_fan_power = None
        else:
            self.rated_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_fan_air_flow_ratio = None
        else:
            self.minimum_fan_air_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name_or_zone_name = None
        else:
            self.air_inlet_node_name_or_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_refrigerant_operating_charge_inventory = None
        else:
            self.condenser_refrigerant_operating_charge_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensate_receiver_refrigerant_inventory = None
        else:
            self.condensate_receiver_refrigerant_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensate_piping_refrigerant_inventory = None
        else:
            self.condensate_piping_refrigerant_inventory = vals[i]
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
    def rated_effective_total_heat_rejection_rate_curve_name(self):
        """Get rated_effective_total_heat_rejection_rate_curve_name

        Returns:
            str: the value of `rated_effective_total_heat_rejection_rate_curve_name` or None if not set
        """
        return self._data["Rated Effective Total Heat Rejection Rate Curve Name"]

    @rated_effective_total_heat_rejection_rate_curve_name.setter
    def rated_effective_total_heat_rejection_rate_curve_name(self, value=None):
        """  Corresponds to IDD Field `Rated Effective Total Heat Rejection Rate Curve Name`
        Rating as per ARI 460
        Be sure the rating corresponds to the correct refrigerant
        Table:OneIndependentVariable object can also be used
        HeatRejection(W)=C1 +C2(Condensing Temp - Entering Air Temp, deg C)
        Will be adjusted for elevation automatically

        Args:
            value (str): value for IDD Field `Rated Effective Total Heat Rejection Rate Curve Name`
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
                                 'for field `rated_effective_total_heat_rejection_rate_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `rated_effective_total_heat_rejection_rate_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `rated_effective_total_heat_rejection_rate_curve_name`')
        self._data["Rated Effective Total Heat Rejection Rate Curve Name"] = value

    @property
    def rated_subcooling_temperature_difference(self):
        """Get rated_subcooling_temperature_difference

        Returns:
            float: the value of `rated_subcooling_temperature_difference` or None if not set
        """
        return self._data["Rated Subcooling Temperature Difference"]

    @rated_subcooling_temperature_difference.setter
    def rated_subcooling_temperature_difference(self, value=0.0):
        """  Corresponds to IDD Field `Rated Subcooling Temperature Difference`
        must correspond to rating given for total heat rejection effect

        Args:
            value (float): value for IDD Field `Rated Subcooling Temperature Difference`
                Units: DeltaC
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
                                 'for field `rated_subcooling_temperature_difference`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_subcooling_temperature_difference`')
        self._data["Rated Subcooling Temperature Difference"] = value

    @property
    def condenser_fan_speed_control_type(self):
        """Get condenser_fan_speed_control_type

        Returns:
            str: the value of `condenser_fan_speed_control_type` or None if not set
        """
        return self._data["Condenser Fan Speed Control Type"]

    @condenser_fan_speed_control_type.setter
    def condenser_fan_speed_control_type(self, value="Fixed"):
        """  Corresponds to IDD Field `Condenser Fan Speed Control Type`

        Args:
            value (str): value for IDD Field `Condenser Fan Speed Control Type`
                Accepted values are:
                      - Fixed
                      - FixedLinear
                      - VariableSpeed
                      - TwoSpeed
                Default value: Fixed
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
                                 'for field `condenser_fan_speed_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_fan_speed_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_fan_speed_control_type`')
            vals = {}
            vals["fixed"] = "Fixed"
            vals["fixedlinear"] = "FixedLinear"
            vals["variablespeed"] = "VariableSpeed"
            vals["twospeed"] = "TwoSpeed"
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
                                     'field `condenser_fan_speed_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Condenser Fan Speed Control Type"] = value

    @property
    def rated_fan_power(self):
        """Get rated_fan_power

        Returns:
            float: the value of `rated_fan_power` or None if not set
        """
        return self._data["Rated Fan Power"]

    @rated_fan_power.setter
    def rated_fan_power(self, value=250.0):
        """  Corresponds to IDD Field `Rated Fan Power`
        Power for condenser fan(s) corresponding to rated total heat rejection effect.

        Args:
            value (float): value for IDD Field `Rated Fan Power`
                Units: W
                Default value: 250.0
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
                                 'for field `rated_fan_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_fan_power`')
        self._data["Rated Fan Power"] = value

    @property
    def minimum_fan_air_flow_ratio(self):
        """Get minimum_fan_air_flow_ratio

        Returns:
            float: the value of `minimum_fan_air_flow_ratio` or None if not set
        """
        return self._data["Minimum Fan Air Flow Ratio"]

    @minimum_fan_air_flow_ratio.setter
    def minimum_fan_air_flow_ratio(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Fan Air Flow Ratio`
        Minimum air flow fraction through condenser fan

        Args:
            value (float): value for IDD Field `Minimum Fan Air Flow Ratio`
                Units: dimensionless
                Default value: 0.2
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
                                 'for field `minimum_fan_air_flow_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_fan_air_flow_ratio`')
        self._data["Minimum Fan Air Flow Ratio"] = value

    @property
    def air_inlet_node_name_or_zone_name(self):
        """Get air_inlet_node_name_or_zone_name

        Returns:
            str: the value of `air_inlet_node_name_or_zone_name` or None if not set
        """
        return self._data["Air Inlet Node Name or Zone Name"]

    @air_inlet_node_name_or_zone_name.setter
    def air_inlet_node_name_or_zone_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name or Zone Name`
        If field is left blank,
        then the model assumes that the inlet air
        conditions are the outdoor air conditions for the current timestep
        (e.g., no adjustment for height above ground).
        If the condenser rejects heat to a conditioned zone, enter the zone name here.

        Args:
            value (str): value for IDD Field `Air Inlet Node Name or Zone Name`
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
                                 'for field `air_inlet_node_name_or_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name_or_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name_or_zone_name`')
        self._data["Air Inlet Node Name or Zone Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    @property
    def condenser_refrigerant_operating_charge_inventory(self):
        """Get condenser_refrigerant_operating_charge_inventory

        Returns:
            float: the value of `condenser_refrigerant_operating_charge_inventory` or None if not set
        """
        return self._data["Condenser Refrigerant Operating Charge Inventory"]

    @condenser_refrigerant_operating_charge_inventory.setter
    def condenser_refrigerant_operating_charge_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Condenser Refrigerant Operating Charge Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condenser Refrigerant Operating Charge Inventory`
                Units: kg
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
                                 'for field `condenser_refrigerant_operating_charge_inventory`'.format(value))
        self._data["Condenser Refrigerant Operating Charge Inventory"] = value

    @property
    def condensate_receiver_refrigerant_inventory(self):
        """Get condensate_receiver_refrigerant_inventory

        Returns:
            float: the value of `condensate_receiver_refrigerant_inventory` or None if not set
        """
        return self._data["Condensate Receiver Refrigerant Inventory"]

    @condensate_receiver_refrigerant_inventory.setter
    def condensate_receiver_refrigerant_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Condensate Receiver Refrigerant Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condensate Receiver Refrigerant Inventory`
                Units: kg
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
                                 'for field `condensate_receiver_refrigerant_inventory`'.format(value))
        self._data["Condensate Receiver Refrigerant Inventory"] = value

    @property
    def condensate_piping_refrigerant_inventory(self):
        """Get condensate_piping_refrigerant_inventory

        Returns:
            float: the value of `condensate_piping_refrigerant_inventory` or None if not set
        """
        return self._data["Condensate Piping Refrigerant Inventory"]

    @condensate_piping_refrigerant_inventory.setter
    def condensate_piping_refrigerant_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Condensate Piping Refrigerant Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condensate Piping Refrigerant Inventory`
                Units: kg
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
                                 'for field `condensate_piping_refrigerant_inventory`'.format(value))
        self._data["Condensate Piping Refrigerant Inventory"] = value

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

class RefrigerationCondenserEvaporativeCooled(object):
    """ Corresponds to IDD object `Refrigeration:Condenser:EvaporativeCooled`
        Evaporative-cooled condenser for a refrigeration system (Refrigeration:System).
    
    """
    internal_name = "Refrigeration:Condenser:EvaporativeCooled"
    field_count = 23
    required_fields = ["Name", "Rated Effective Total Heat Rejection Rate", "Rated Fan Power"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:Condenser:EvaporativeCooled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Rated Effective Total Heat Rejection Rate"] = None
        self._data["Rated Subcooling Temperature Difference"] = None
        self._data["Fan Speed Control Type"] = None
        self._data["Rated Fan Power"] = None
        self._data["Minimum Fan Air Flow Ratio"] = None
        self._data["Approach Temperature Constant Term"] = None
        self._data["Approach Temperature Coefficient 2"] = None
        self._data["Approach Temperature Coefficient 3"] = None
        self._data["Approach Temperature Coefficient 4"] = None
        self._data["Minimum Capacity Factor"] = None
        self._data["Maximum Capacity Factor"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Rated Air Flow Rate"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Rated Water Pump Power"] = None
        self._data["Evaporative Water Supply Tank Name"] = None
        self._data["Evaporative Condenser Availability Schedule Name"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Condenser Refrigerant Operating Charge Inventory"] = None
        self._data["Condensate Receiver Refrigerant Inventory"] = None
        self._data["Condensate Piping Refrigerant Inventory"] = None
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
            self.rated_effective_total_heat_rejection_rate = None
        else:
            self.rated_effective_total_heat_rejection_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_subcooling_temperature_difference = None
        else:
            self.rated_subcooling_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_speed_control_type = None
        else:
            self.fan_speed_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_fan_power = None
        else:
            self.rated_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_fan_air_flow_ratio = None
        else:
            self.minimum_fan_air_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.approach_temperature_constant_term = None
        else:
            self.approach_temperature_constant_term = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.approach_temperature_coefficient_2 = None
        else:
            self.approach_temperature_coefficient_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.approach_temperature_coefficient_3 = None
        else:
            self.approach_temperature_coefficient_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.approach_temperature_coefficient_4 = None
        else:
            self.approach_temperature_coefficient_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_capacity_factor = None
        else:
            self.minimum_capacity_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_capacity_factor = None
        else:
            self.maximum_capacity_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_air_flow_rate = None
        else:
            self.rated_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_water_pump_power = None
        else:
            self.rated_water_pump_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporative_water_supply_tank_name = None
        else:
            self.evaporative_water_supply_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporative_condenser_availability_schedule_name = None
        else:
            self.evaporative_condenser_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_refrigerant_operating_charge_inventory = None
        else:
            self.condenser_refrigerant_operating_charge_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensate_receiver_refrigerant_inventory = None
        else:
            self.condensate_receiver_refrigerant_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensate_piping_refrigerant_inventory = None
        else:
            self.condensate_piping_refrigerant_inventory = vals[i]
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
    def rated_effective_total_heat_rejection_rate(self):
        """Get rated_effective_total_heat_rejection_rate

        Returns:
            float: the value of `rated_effective_total_heat_rejection_rate` or None if not set
        """
        return self._data["Rated Effective Total Heat Rejection Rate"]

    @rated_effective_total_heat_rejection_rate.setter
    def rated_effective_total_heat_rejection_rate(self, value=None):
        """  Corresponds to IDD Field `Rated Effective Total Heat Rejection Rate`
        Rating as per ARI 490
        Be sure the rating corresponds to the correct refrigerant

        Args:
            value (float): value for IDD Field `Rated Effective Total Heat Rejection Rate`
                Units: W
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
                                 'for field `rated_effective_total_heat_rejection_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_effective_total_heat_rejection_rate`')
        self._data["Rated Effective Total Heat Rejection Rate"] = value

    @property
    def rated_subcooling_temperature_difference(self):
        """Get rated_subcooling_temperature_difference

        Returns:
            float: the value of `rated_subcooling_temperature_difference` or None if not set
        """
        return self._data["Rated Subcooling Temperature Difference"]

    @rated_subcooling_temperature_difference.setter
    def rated_subcooling_temperature_difference(self, value=0.0):
        """  Corresponds to IDD Field `Rated Subcooling Temperature Difference`
        must correspond to rating given for total heat rejection effect

        Args:
            value (float): value for IDD Field `Rated Subcooling Temperature Difference`
                Units: DeltaC
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
                                 'for field `rated_subcooling_temperature_difference`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_subcooling_temperature_difference`')
        self._data["Rated Subcooling Temperature Difference"] = value

    @property
    def fan_speed_control_type(self):
        """Get fan_speed_control_type

        Returns:
            str: the value of `fan_speed_control_type` or None if not set
        """
        return self._data["Fan Speed Control Type"]

    @fan_speed_control_type.setter
    def fan_speed_control_type(self, value="Fixed"):
        """  Corresponds to IDD Field `Fan Speed Control Type`

        Args:
            value (str): value for IDD Field `Fan Speed Control Type`
                Accepted values are:
                      - Fixed
                      - FixedLinear
                      - VariableSpeed
                      - TwoSpeed
                Default value: Fixed
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
                                 'for field `fan_speed_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_speed_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_speed_control_type`')
            vals = {}
            vals["fixed"] = "Fixed"
            vals["fixedlinear"] = "FixedLinear"
            vals["variablespeed"] = "VariableSpeed"
            vals["twospeed"] = "TwoSpeed"
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
                                     'field `fan_speed_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Fan Speed Control Type"] = value

    @property
    def rated_fan_power(self):
        """Get rated_fan_power

        Returns:
            float: the value of `rated_fan_power` or None if not set
        """
        return self._data["Rated Fan Power"]

    @rated_fan_power.setter
    def rated_fan_power(self, value=None):
        """  Corresponds to IDD Field `Rated Fan Power`
        Power for condenser fan(s) corresponding to rated total heat rejection effect.

        Args:
            value (float): value for IDD Field `Rated Fan Power`
                Units: W
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
                                 'for field `rated_fan_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_fan_power`')
        self._data["Rated Fan Power"] = value

    @property
    def minimum_fan_air_flow_ratio(self):
        """Get minimum_fan_air_flow_ratio

        Returns:
            float: the value of `minimum_fan_air_flow_ratio` or None if not set
        """
        return self._data["Minimum Fan Air Flow Ratio"]

    @minimum_fan_air_flow_ratio.setter
    def minimum_fan_air_flow_ratio(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Fan Air Flow Ratio`
        Minimum air flow fraction through condenser fan

        Args:
            value (float): value for IDD Field `Minimum Fan Air Flow Ratio`
                Units: dimensionless
                Default value: 0.2
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
                                 'for field `minimum_fan_air_flow_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_fan_air_flow_ratio`')
        self._data["Minimum Fan Air Flow Ratio"] = value

    @property
    def approach_temperature_constant_term(self):
        """Get approach_temperature_constant_term

        Returns:
            float: the value of `approach_temperature_constant_term` or None if not set
        """
        return self._data["Approach Temperature Constant Term"]

    @approach_temperature_constant_term.setter
    def approach_temperature_constant_term(self, value=6.63):
        """  Corresponds to IDD Field `Approach Temperature Constant Term`
        A1 in delta T = A1 + A2(hrcf) + A3/(hrcf) + A4(Twb)

        Args:
            value (float): value for IDD Field `Approach Temperature Constant Term`
                Units: C
                Default value: 6.63
                value >= 0.0
                value <= 20.0
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
                                 'for field `approach_temperature_constant_term`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `approach_temperature_constant_term`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `approach_temperature_constant_term`')
        self._data["Approach Temperature Constant Term"] = value

    @property
    def approach_temperature_coefficient_2(self):
        """Get approach_temperature_coefficient_2

        Returns:
            float: the value of `approach_temperature_coefficient_2` or None if not set
        """
        return self._data["Approach Temperature Coefficient 2"]

    @approach_temperature_coefficient_2.setter
    def approach_temperature_coefficient_2(self, value=0.468):
        """  Corresponds to IDD Field `Approach Temperature Coefficient 2`
        A2 in delta T = A1 + A2(hrcf) +A3/(hrcf) +A4(Twb)

        Args:
            value (float): value for IDD Field `Approach Temperature Coefficient 2`
                Units: C
                Default value: 0.468
                value >= 0.0
                value <= 20.0
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
                                 'for field `approach_temperature_coefficient_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `approach_temperature_coefficient_2`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `approach_temperature_coefficient_2`')
        self._data["Approach Temperature Coefficient 2"] = value

    @property
    def approach_temperature_coefficient_3(self):
        """Get approach_temperature_coefficient_3

        Returns:
            float: the value of `approach_temperature_coefficient_3` or None if not set
        """
        return self._data["Approach Temperature Coefficient 3"]

    @approach_temperature_coefficient_3.setter
    def approach_temperature_coefficient_3(self, value=17.93):
        """  Corresponds to IDD Field `Approach Temperature Coefficient 3`
        A3 in delta T = A1 + A2(hrcf) +A3/(hrcf) +A4(Twb)

        Args:
            value (float): value for IDD Field `Approach Temperature Coefficient 3`
                Units: C
                Default value: 17.93
                value >= 0.0
                value <= 30.0
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
                                 'for field `approach_temperature_coefficient_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `approach_temperature_coefficient_3`')
            if value > 30.0:
                raise ValueError('value need to be smaller 30.0 '
                                 'for field `approach_temperature_coefficient_3`')
        self._data["Approach Temperature Coefficient 3"] = value

    @property
    def approach_temperature_coefficient_4(self):
        """Get approach_temperature_coefficient_4

        Returns:
            float: the value of `approach_temperature_coefficient_4` or None if not set
        """
        return self._data["Approach Temperature Coefficient 4"]

    @approach_temperature_coefficient_4.setter
    def approach_temperature_coefficient_4(self, value=-0.322):
        """  Corresponds to IDD Field `Approach Temperature Coefficient 4`
        A4 in deltaT=A1 + A2(hrcf) +A3/(hrcf) +A4(Twb)

        Args:
            value (float): value for IDD Field `Approach Temperature Coefficient 4`
                Units: dimensionless
                Default value: -0.322
                value >= -20.0
                value <= 20.0
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
                                 'for field `approach_temperature_coefficient_4`'.format(value))
            if value < -20.0:
                raise ValueError('value need to be greater or equal -20.0 '
                                 'for field `approach_temperature_coefficient_4`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `approach_temperature_coefficient_4`')
        self._data["Approach Temperature Coefficient 4"] = value

    @property
    def minimum_capacity_factor(self):
        """Get minimum_capacity_factor

        Returns:
            float: the value of `minimum_capacity_factor` or None if not set
        """
        return self._data["Minimum Capacity Factor"]

    @minimum_capacity_factor.setter
    def minimum_capacity_factor(self, value=0.5):
        """  Corresponds to IDD Field `Minimum Capacity Factor`
        taken from manufacturer's Heat Rejection Capacity Factor Table

        Args:
            value (float): value for IDD Field `Minimum Capacity Factor`
                Units: dimensionless
                Default value: 0.5
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
                                 'for field `minimum_capacity_factor`'.format(value))
        self._data["Minimum Capacity Factor"] = value

    @property
    def maximum_capacity_factor(self):
        """Get maximum_capacity_factor

        Returns:
            float: the value of `maximum_capacity_factor` or None if not set
        """
        return self._data["Maximum Capacity Factor"]

    @maximum_capacity_factor.setter
    def maximum_capacity_factor(self, value=5.0):
        """  Corresponds to IDD Field `Maximum Capacity Factor`
        taken from manufacturer's Heat Rejection Capacity Factor Table

        Args:
            value (float): value for IDD Field `Maximum Capacity Factor`
                Units: dimensionless
                Default value: 5.0
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
                                 'for field `maximum_capacity_factor`'.format(value))
        self._data["Maximum Capacity Factor"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`
        If field is left blank,
        then the model assumes that the inlet air
        conditions are the outdoor air conditions for the current timestep
        (e.g., no adjustment for height above ground).

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
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
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def rated_air_flow_rate(self):
        """Get rated_air_flow_rate

        Returns:
            float: the value of `rated_air_flow_rate` or None if not set
        """
        return self._data["Rated Air Flow Rate"]

    @rated_air_flow_rate.setter
    def rated_air_flow_rate(self, value="autocalculate"):
        """  Corresponds to IDD Field `Rated Air Flow Rate`
        Used to calculate evaporative condenser water use and fan energy use.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Rated Air Flow Rate`
                Units: m3/s
                Default value: "autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Rated Air Flow Rate"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_air_flow_rate`'.format(value))
        self._data["Rated Air Flow Rate"] = value

    @property
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=200.0):
        """  Corresponds to IDD Field `Basin Heater Capacity`
        This field is only used for periods
        when the evap condenser is available (field Evaporative Condenser Availability
        Schedule). For this situation, the heater heats the basin water when the
        outdoor air dry-bulb temperature falls below the set point temperature, but
        only when the condenser fans are off (i.e., no refrigerated case load).

        Args:
            value (float): value for IDD Field `Basin Heater Capacity`
                Units: W/K
                Default value: 200.0
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
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')
        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0):
        """  Corresponds to IDD Field `Basin Heater Setpoint Temperature`
        Enter the outdoor dry-bulb temperature at which the basin heater turns on.

        Args:
            value (float): value for IDD Field `Basin Heater Setpoint Temperature`
                Units: C
                Default value: 2.0
                value >= 2.0
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
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')
        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def rated_water_pump_power(self):
        """Get rated_water_pump_power

        Returns:
            float: the value of `rated_water_pump_power` or None if not set
        """
        return self._data["Rated Water Pump Power"]

    @rated_water_pump_power.setter
    def rated_water_pump_power(self, value=1000.0):
        """  Corresponds to IDD Field `Rated Water Pump Power`
        Design recirculating water pump power.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Rated Water Pump Power`
                Units: W
                Default value: 1000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Rated Water Pump Power"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_water_pump_power`'.format(value))
        self._data["Rated Water Pump Power"] = value

    @property
    def evaporative_water_supply_tank_name(self):
        """Get evaporative_water_supply_tank_name

        Returns:
            str: the value of `evaporative_water_supply_tank_name` or None if not set
        """
        return self._data["Evaporative Water Supply Tank Name"]

    @evaporative_water_supply_tank_name.setter
    def evaporative_water_supply_tank_name(self, value=None):
        """  Corresponds to IDD Field `Evaporative Water Supply Tank Name`
        If blank, water supply is from Mains.

        Args:
            value (str): value for IDD Field `Evaporative Water Supply Tank Name`
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
                                 'for field `evaporative_water_supply_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporative_water_supply_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evaporative_water_supply_tank_name`')
        self._data["Evaporative Water Supply Tank Name"] = value

    @property
    def evaporative_condenser_availability_schedule_name(self):
        """Get evaporative_condenser_availability_schedule_name

        Returns:
            str: the value of `evaporative_condenser_availability_schedule_name` or None if not set
        """
        return self._data["Evaporative Condenser Availability Schedule Name"]

    @evaporative_condenser_availability_schedule_name.setter
    def evaporative_condenser_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Evaporative Condenser Availability Schedule Name`
        Schedule values greater than 0 indicate that evaporative cooling of the
        condenser is available. This schedule allows the user to define seasonal
        shutdown/draining of the water cooling system in cold climate applications.
        For periods with schedule values of 0, the condenser operates as Air Cooled.

        Args:
            value (str): value for IDD Field `Evaporative Condenser Availability Schedule Name`
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
                                 'for field `evaporative_condenser_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evaporative_condenser_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evaporative_condenser_availability_schedule_name`')
        self._data["Evaporative Condenser Availability Schedule Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    @property
    def condenser_refrigerant_operating_charge_inventory(self):
        """Get condenser_refrigerant_operating_charge_inventory

        Returns:
            float: the value of `condenser_refrigerant_operating_charge_inventory` or None if not set
        """
        return self._data["Condenser Refrigerant Operating Charge Inventory"]

    @condenser_refrigerant_operating_charge_inventory.setter
    def condenser_refrigerant_operating_charge_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Condenser Refrigerant Operating Charge Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condenser Refrigerant Operating Charge Inventory`
                Units: kg
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
                                 'for field `condenser_refrigerant_operating_charge_inventory`'.format(value))
        self._data["Condenser Refrigerant Operating Charge Inventory"] = value

    @property
    def condensate_receiver_refrigerant_inventory(self):
        """Get condensate_receiver_refrigerant_inventory

        Returns:
            float: the value of `condensate_receiver_refrigerant_inventory` or None if not set
        """
        return self._data["Condensate Receiver Refrigerant Inventory"]

    @condensate_receiver_refrigerant_inventory.setter
    def condensate_receiver_refrigerant_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Condensate Receiver Refrigerant Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condensate Receiver Refrigerant Inventory`
                Units: kg
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
                                 'for field `condensate_receiver_refrigerant_inventory`'.format(value))
        self._data["Condensate Receiver Refrigerant Inventory"] = value

    @property
    def condensate_piping_refrigerant_inventory(self):
        """Get condensate_piping_refrigerant_inventory

        Returns:
            float: the value of `condensate_piping_refrigerant_inventory` or None if not set
        """
        return self._data["Condensate Piping Refrigerant Inventory"]

    @condensate_piping_refrigerant_inventory.setter
    def condensate_piping_refrigerant_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Condensate Piping Refrigerant Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condensate Piping Refrigerant Inventory`
                Units: kg
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
                                 'for field `condensate_piping_refrigerant_inventory`'.format(value))
        self._data["Condensate Piping Refrigerant Inventory"] = value

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

class RefrigerationCondenserWaterCooled(object):
    """ Corresponds to IDD object `Refrigeration:Condenser:WaterCooled`
        Water cooled condenser for a refrigeration system (Refrigeration:System).
    
    """
    internal_name = "Refrigeration:Condenser:WaterCooled"
    field_count = 17
    required_fields = ["Name", "Rated Condensing Temperature", "Rated Water Inlet Temperature"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:Condenser:WaterCooled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Rated Effective Total Heat Rejection Rate"] = None
        self._data["Rated Condensing Temperature"] = None
        self._data["Rated Subcooling Temperature Difference"] = None
        self._data["Rated Water Inlet Temperature"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Water-Cooled Loop Flow Type"] = None
        self._data["Water Outlet Temperature Schedule Name"] = None
        self._data["Water Design Flow Rate"] = None
        self._data["Water Maximum Flow Rate"] = None
        self._data["Water Maximum Water Outlet Temperature"] = None
        self._data["Water Minimum Water Inlet Temperature"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Condenser Refrigerant Operating Charge Inventory"] = None
        self._data["Condensate Receiver Refrigerant Inventory"] = None
        self._data["Condensate Piping Refrigerant Inventory"] = None
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
            self.rated_effective_total_heat_rejection_rate = None
        else:
            self.rated_effective_total_heat_rejection_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_condensing_temperature = None
        else:
            self.rated_condensing_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_subcooling_temperature_difference = None
        else:
            self.rated_subcooling_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_water_inlet_temperature = None
        else:
            self.rated_water_inlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.watercooled_loop_flow_type = None
        else:
            self.watercooled_loop_flow_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_temperature_schedule_name = None
        else:
            self.water_outlet_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_design_flow_rate = None
        else:
            self.water_design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_maximum_flow_rate = None
        else:
            self.water_maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_maximum_water_outlet_temperature = None
        else:
            self.water_maximum_water_outlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_minimum_water_inlet_temperature = None
        else:
            self.water_minimum_water_inlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_refrigerant_operating_charge_inventory = None
        else:
            self.condenser_refrigerant_operating_charge_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensate_receiver_refrigerant_inventory = None
        else:
            self.condensate_receiver_refrigerant_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensate_piping_refrigerant_inventory = None
        else:
            self.condensate_piping_refrigerant_inventory = vals[i]
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
    def rated_effective_total_heat_rejection_rate(self):
        """Get rated_effective_total_heat_rejection_rate

        Returns:
            float: the value of `rated_effective_total_heat_rejection_rate` or None if not set
        """
        return self._data["Rated Effective Total Heat Rejection Rate"]

    @rated_effective_total_heat_rejection_rate.setter
    def rated_effective_total_heat_rejection_rate(self, value=None):
        """  Corresponds to IDD Field `Rated Effective Total Heat Rejection Rate`
        Rating as per ARI 450
        Be sure the rating corresponds to the correct refrigerant
        not used in calculations, only for identification and output

        Args:
            value (float): value for IDD Field `Rated Effective Total Heat Rejection Rate`
                Units: W
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
                                 'for field `rated_effective_total_heat_rejection_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_effective_total_heat_rejection_rate`')
        self._data["Rated Effective Total Heat Rejection Rate"] = value

    @property
    def rated_condensing_temperature(self):
        """Get rated_condensing_temperature

        Returns:
            float: the value of `rated_condensing_temperature` or None if not set
        """
        return self._data["Rated Condensing Temperature"]

    @rated_condensing_temperature.setter
    def rated_condensing_temperature(self, value=None):
        """  Corresponds to IDD Field `Rated Condensing Temperature`
        must correspond to rating given for total heat rejection effect

        Args:
            value (float): value for IDD Field `Rated Condensing Temperature`
                Units: C
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
                                 'for field `rated_condensing_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_condensing_temperature`')
        self._data["Rated Condensing Temperature"] = value

    @property
    def rated_subcooling_temperature_difference(self):
        """Get rated_subcooling_temperature_difference

        Returns:
            float: the value of `rated_subcooling_temperature_difference` or None if not set
        """
        return self._data["Rated Subcooling Temperature Difference"]

    @rated_subcooling_temperature_difference.setter
    def rated_subcooling_temperature_difference(self, value=0.0):
        """  Corresponds to IDD Field `Rated Subcooling Temperature Difference`
        must correspond to rating given for total heat rejection effect

        Args:
            value (float): value for IDD Field `Rated Subcooling Temperature Difference`
                Units: DeltaC
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
                                 'for field `rated_subcooling_temperature_difference`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_subcooling_temperature_difference`')
        self._data["Rated Subcooling Temperature Difference"] = value

    @property
    def rated_water_inlet_temperature(self):
        """Get rated_water_inlet_temperature

        Returns:
            float: the value of `rated_water_inlet_temperature` or None if not set
        """
        return self._data["Rated Water Inlet Temperature"]

    @rated_water_inlet_temperature.setter
    def rated_water_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `Rated Water Inlet Temperature`
        must correspond to rating given for total heat rejection effect

        Args:
            value (float): value for IDD Field `Rated Water Inlet Temperature`
                Units: C
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
                                 'for field `rated_water_inlet_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_water_inlet_temperature`')
        self._data["Rated Water Inlet Temperature"] = value

    @property
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`
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
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_inlet_node_name`')
        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`
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
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_outlet_node_name`')
        self._data["Water Outlet Node Name"] = value

    @property
    def watercooled_loop_flow_type(self):
        """Get watercooled_loop_flow_type

        Returns:
            str: the value of `watercooled_loop_flow_type` or None if not set
        """
        return self._data["Water-Cooled Loop Flow Type"]

    @watercooled_loop_flow_type.setter
    def watercooled_loop_flow_type(self, value="VariableFlow"):
        """  Corresponds to IDD Field `Water-Cooled Loop Flow Type`

        Args:
            value (str): value for IDD Field `Water-Cooled Loop Flow Type`
                Accepted values are:
                      - VariableFlow
                      - ConstantFlow
                Default value: VariableFlow
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
                                 'for field `watercooled_loop_flow_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `watercooled_loop_flow_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `watercooled_loop_flow_type`')
            vals = {}
            vals["variableflow"] = "VariableFlow"
            vals["constantflow"] = "ConstantFlow"
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
                                     'field `watercooled_loop_flow_type`'.format(value))
            value = vals[value_lower]
        self._data["Water-Cooled Loop Flow Type"] = value

    @property
    def water_outlet_temperature_schedule_name(self):
        """Get water_outlet_temperature_schedule_name

        Returns:
            str: the value of `water_outlet_temperature_schedule_name` or None if not set
        """
        return self._data["Water Outlet Temperature Schedule Name"]

    @water_outlet_temperature_schedule_name.setter
    def water_outlet_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Temperature Schedule Name`
        Applicable only when loop flow type is Variable Flow.

        Args:
            value (str): value for IDD Field `Water Outlet Temperature Schedule Name`
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
                                 'for field `water_outlet_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_outlet_temperature_schedule_name`')
        self._data["Water Outlet Temperature Schedule Name"] = value

    @property
    def water_design_flow_rate(self):
        """Get water_design_flow_rate

        Returns:
            float: the value of `water_design_flow_rate` or None if not set
        """
        return self._data["Water Design Flow Rate"]

    @water_design_flow_rate.setter
    def water_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Water Design Flow Rate`
        note required units must be converted from L/s as specified in ARI 450-2007
        Applicable only when loop flow type is Constant Flow.

        Args:
            value (float): value for IDD Field `Water Design Flow Rate`
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
                                 'for field `water_design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `water_design_flow_rate`')
        self._data["Water Design Flow Rate"] = value

    @property
    def water_maximum_flow_rate(self):
        """Get water_maximum_flow_rate

        Returns:
            float: the value of `water_maximum_flow_rate` or None if not set
        """
        return self._data["Water Maximum Flow Rate"]

    @water_maximum_flow_rate.setter
    def water_maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Water Maximum Flow Rate`

        Args:
            value (float): value for IDD Field `Water Maximum Flow Rate`
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
                                 'for field `water_maximum_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `water_maximum_flow_rate`')
        self._data["Water Maximum Flow Rate"] = value

    @property
    def water_maximum_water_outlet_temperature(self):
        """Get water_maximum_water_outlet_temperature

        Returns:
            float: the value of `water_maximum_water_outlet_temperature` or None if not set
        """
        return self._data["Water Maximum Water Outlet Temperature"]

    @water_maximum_water_outlet_temperature.setter
    def water_maximum_water_outlet_temperature(self, value=55.0):
        """  Corresponds to IDD Field `Water Maximum Water Outlet Temperature`

        Args:
            value (float): value for IDD Field `Water Maximum Water Outlet Temperature`
                Units: C
                Default value: 55.0
                value >= 10.0
                value <= 60.0
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
                                 'for field `water_maximum_water_outlet_temperature`'.format(value))
            if value < 10.0:
                raise ValueError('value need to be greater or equal 10.0 '
                                 'for field `water_maximum_water_outlet_temperature`')
            if value > 60.0:
                raise ValueError('value need to be smaller 60.0 '
                                 'for field `water_maximum_water_outlet_temperature`')
        self._data["Water Maximum Water Outlet Temperature"] = value

    @property
    def water_minimum_water_inlet_temperature(self):
        """Get water_minimum_water_inlet_temperature

        Returns:
            float: the value of `water_minimum_water_inlet_temperature` or None if not set
        """
        return self._data["Water Minimum Water Inlet Temperature"]

    @water_minimum_water_inlet_temperature.setter
    def water_minimum_water_inlet_temperature(self, value=10.0):
        """  Corresponds to IDD Field `Water Minimum Water Inlet Temperature`
        related to the minimum allowed refrigeration system condensing temperature

        Args:
            value (float): value for IDD Field `Water Minimum Water Inlet Temperature`
                Units: C
                Default value: 10.0
                value >= 10.0
                value <= 30.0
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
                                 'for field `water_minimum_water_inlet_temperature`'.format(value))
            if value < 10.0:
                raise ValueError('value need to be greater or equal 10.0 '
                                 'for field `water_minimum_water_inlet_temperature`')
            if value > 30.0:
                raise ValueError('value need to be smaller 30.0 '
                                 'for field `water_minimum_water_inlet_temperature`')
        self._data["Water Minimum Water Inlet Temperature"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    @property
    def condenser_refrigerant_operating_charge_inventory(self):
        """Get condenser_refrigerant_operating_charge_inventory

        Returns:
            float: the value of `condenser_refrigerant_operating_charge_inventory` or None if not set
        """
        return self._data["Condenser Refrigerant Operating Charge Inventory"]

    @condenser_refrigerant_operating_charge_inventory.setter
    def condenser_refrigerant_operating_charge_inventory(self, value=None):
        """  Corresponds to IDD Field `Condenser Refrigerant Operating Charge Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condenser Refrigerant Operating Charge Inventory`
                Units: kg
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
                                 'for field `condenser_refrigerant_operating_charge_inventory`'.format(value))
        self._data["Condenser Refrigerant Operating Charge Inventory"] = value

    @property
    def condensate_receiver_refrigerant_inventory(self):
        """Get condensate_receiver_refrigerant_inventory

        Returns:
            float: the value of `condensate_receiver_refrigerant_inventory` or None if not set
        """
        return self._data["Condensate Receiver Refrigerant Inventory"]

    @condensate_receiver_refrigerant_inventory.setter
    def condensate_receiver_refrigerant_inventory(self, value=None):
        """  Corresponds to IDD Field `Condensate Receiver Refrigerant Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condensate Receiver Refrigerant Inventory`
                Units: kg
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
                                 'for field `condensate_receiver_refrigerant_inventory`'.format(value))
        self._data["Condensate Receiver Refrigerant Inventory"] = value

    @property
    def condensate_piping_refrigerant_inventory(self):
        """Get condensate_piping_refrigerant_inventory

        Returns:
            float: the value of `condensate_piping_refrigerant_inventory` or None if not set
        """
        return self._data["Condensate Piping Refrigerant Inventory"]

    @condensate_piping_refrigerant_inventory.setter
    def condensate_piping_refrigerant_inventory(self, value=None):
        """  Corresponds to IDD Field `Condensate Piping Refrigerant Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condensate Piping Refrigerant Inventory`
                Units: kg
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
                                 'for field `condensate_piping_refrigerant_inventory`'.format(value))
        self._data["Condensate Piping Refrigerant Inventory"] = value

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

class RefrigerationCondenserCascade(object):
    """ Corresponds to IDD object `Refrigeration:Condenser:Cascade`
        Cascade condenser for a refrigeration system (Refrigeration:System). The cascade
        condenser is unlike the other condenser options because it rejects heat to another,
        higher-temperature, refrigeration system. That is, the cascade condenser acts as a
        heat rejection object for one system, but acts as a refrigeration load for another
        system.
    
    """
    internal_name = "Refrigeration:Condenser:Cascade"
    field_count = 8
    required_fields = ["Name", "Rated Condensing Temperature", "Rated Effective Total Heat Rejection Rate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:Condenser:Cascade`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Rated Condensing Temperature"] = None
        self._data["Rated Approach Temperature Difference"] = None
        self._data["Rated Effective Total Heat Rejection Rate"] = None
        self._data["Condensing Temperature Control Type"] = None
        self._data["Condenser Refrigerant Operating Charge Inventory"] = None
        self._data["Condensate Receiver Refrigerant Inventory"] = None
        self._data["Condensate Piping Refrigerant Inventory"] = None
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
            self.rated_condensing_temperature = None
        else:
            self.rated_condensing_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_approach_temperature_difference = None
        else:
            self.rated_approach_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_effective_total_heat_rejection_rate = None
        else:
            self.rated_effective_total_heat_rejection_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensing_temperature_control_type = None
        else:
            self.condensing_temperature_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_refrigerant_operating_charge_inventory = None
        else:
            self.condenser_refrigerant_operating_charge_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensate_receiver_refrigerant_inventory = None
        else:
            self.condensate_receiver_refrigerant_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensate_piping_refrigerant_inventory = None
        else:
            self.condensate_piping_refrigerant_inventory = vals[i]
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
    def rated_condensing_temperature(self):
        """Get rated_condensing_temperature

        Returns:
            float: the value of `rated_condensing_temperature` or None if not set
        """
        return self._data["Rated Condensing Temperature"]

    @rated_condensing_temperature.setter
    def rated_condensing_temperature(self, value=None):
        """  Corresponds to IDD Field `Rated Condensing Temperature`
        This is the condensing temperature for the lower temperature secondary loop

        Args:
            value (float): value for IDD Field `Rated Condensing Temperature`
                Units: C
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
                                 'for field `rated_condensing_temperature`'.format(value))
        self._data["Rated Condensing Temperature"] = value

    @property
    def rated_approach_temperature_difference(self):
        """Get rated_approach_temperature_difference

        Returns:
            float: the value of `rated_approach_temperature_difference` or None if not set
        """
        return self._data["Rated Approach Temperature Difference"]

    @rated_approach_temperature_difference.setter
    def rated_approach_temperature_difference(self, value=3.0):
        """  Corresponds to IDD Field `Rated Approach Temperature Difference`
        This is the difference between the condensing and evaporating temperatures

        Args:
            value (float): value for IDD Field `Rated Approach Temperature Difference`
                Units: DeltaC
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_approach_temperature_difference`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_approach_temperature_difference`')
        self._data["Rated Approach Temperature Difference"] = value

    @property
    def rated_effective_total_heat_rejection_rate(self):
        """Get rated_effective_total_heat_rejection_rate

        Returns:
            float: the value of `rated_effective_total_heat_rejection_rate` or None if not set
        """
        return self._data["Rated Effective Total Heat Rejection Rate"]

    @rated_effective_total_heat_rejection_rate.setter
    def rated_effective_total_heat_rejection_rate(self, value=None):
        """  Corresponds to IDD Field `Rated Effective Total Heat Rejection Rate`
        used for identification and rough system size error checking

        Args:
            value (float): value for IDD Field `Rated Effective Total Heat Rejection Rate`
                Units: W
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
                                 'for field `rated_effective_total_heat_rejection_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_effective_total_heat_rejection_rate`')
        self._data["Rated Effective Total Heat Rejection Rate"] = value

    @property
    def condensing_temperature_control_type(self):
        """Get condensing_temperature_control_type

        Returns:
            str: the value of `condensing_temperature_control_type` or None if not set
        """
        return self._data["Condensing Temperature Control Type"]

    @condensing_temperature_control_type.setter
    def condensing_temperature_control_type(self, value="Fixed"):
        """  Corresponds to IDD Field `Condensing Temperature Control Type`
        Fixed keeps condensing temperature constant
        Float sets the condensing temperature according to
        the other loads on the higher temperature system

        Args:
            value (str): value for IDD Field `Condensing Temperature Control Type`
                Accepted values are:
                      - Fixed
                      - Float
                Default value: Fixed
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
                                 'for field `condensing_temperature_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condensing_temperature_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condensing_temperature_control_type`')
            vals = {}
            vals["fixed"] = "Fixed"
            vals["float"] = "Float"
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
                                     'field `condensing_temperature_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Condensing Temperature Control Type"] = value

    @property
    def condenser_refrigerant_operating_charge_inventory(self):
        """Get condenser_refrigerant_operating_charge_inventory

        Returns:
            float: the value of `condenser_refrigerant_operating_charge_inventory` or None if not set
        """
        return self._data["Condenser Refrigerant Operating Charge Inventory"]

    @condenser_refrigerant_operating_charge_inventory.setter
    def condenser_refrigerant_operating_charge_inventory(self, value=None):
        """  Corresponds to IDD Field `Condenser Refrigerant Operating Charge Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condenser Refrigerant Operating Charge Inventory`
                Units: kg
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
                                 'for field `condenser_refrigerant_operating_charge_inventory`'.format(value))
        self._data["Condenser Refrigerant Operating Charge Inventory"] = value

    @property
    def condensate_receiver_refrigerant_inventory(self):
        """Get condensate_receiver_refrigerant_inventory

        Returns:
            float: the value of `condensate_receiver_refrigerant_inventory` or None if not set
        """
        return self._data["Condensate Receiver Refrigerant Inventory"]

    @condensate_receiver_refrigerant_inventory.setter
    def condensate_receiver_refrigerant_inventory(self, value=None):
        """  Corresponds to IDD Field `Condensate Receiver Refrigerant Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condensate Receiver Refrigerant Inventory`
                Units: kg
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
                                 'for field `condensate_receiver_refrigerant_inventory`'.format(value))
        self._data["Condensate Receiver Refrigerant Inventory"] = value

    @property
    def condensate_piping_refrigerant_inventory(self):
        """Get condensate_piping_refrigerant_inventory

        Returns:
            float: the value of `condensate_piping_refrigerant_inventory` or None if not set
        """
        return self._data["Condensate Piping Refrigerant Inventory"]

    @condensate_piping_refrigerant_inventory.setter
    def condensate_piping_refrigerant_inventory(self, value=None):
        """  Corresponds to IDD Field `Condensate Piping Refrigerant Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Condensate Piping Refrigerant Inventory`
                Units: kg
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
                                 'for field `condensate_piping_refrigerant_inventory`'.format(value))
        self._data["Condensate Piping Refrigerant Inventory"] = value

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

class RefrigerationGasCoolerAirCooled(object):
    """ Corresponds to IDD object `Refrigeration:GasCooler:AirCooled`
        The transcritical refrigeration system requires a single gas cooler to reject the
        system heat.
    
    """
    internal_name = "Refrigeration:GasCooler:AirCooled"
    field_count = 14
    required_fields = ["Name", "Rated Total Heat Rejection Rate Curve Name", "Rated Fan Power"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:GasCooler:AirCooled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Rated Total Heat Rejection Rate Curve Name"] = None
        self._data["Gas Cooler Fan Speed Control Type"] = None
        self._data["Rated Fan Power"] = None
        self._data["Minimum Fan Air Flow Ratio"] = None
        self._data["Transition Temperature"] = None
        self._data["Transcritical Approach Temperature"] = None
        self._data["Subcritical Temperature Difference"] = None
        self._data["Minimum Condensing Temperature"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Gas Cooler Refrigerant Operating Charge Inventory"] = None
        self._data["Gas Cooler Receiver Refrigerant Inventory"] = None
        self._data["Gas Cooler Outlet Piping Refrigerant Inventory"] = None
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
            self.rated_total_heat_rejection_rate_curve_name = None
        else:
            self.rated_total_heat_rejection_rate_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gas_cooler_fan_speed_control_type = None
        else:
            self.gas_cooler_fan_speed_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_fan_power = None
        else:
            self.rated_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_fan_air_flow_ratio = None
        else:
            self.minimum_fan_air_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transition_temperature = None
        else:
            self.transition_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transcritical_approach_temperature = None
        else:
            self.transcritical_approach_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.subcritical_temperature_difference = None
        else:
            self.subcritical_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_condensing_temperature = None
        else:
            self.minimum_condensing_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gas_cooler_refrigerant_operating_charge_inventory = None
        else:
            self.gas_cooler_refrigerant_operating_charge_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gas_cooler_receiver_refrigerant_inventory = None
        else:
            self.gas_cooler_receiver_refrigerant_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gas_cooler_outlet_piping_refrigerant_inventory = None
        else:
            self.gas_cooler_outlet_piping_refrigerant_inventory = vals[i]
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
    def rated_total_heat_rejection_rate_curve_name(self):
        """Get rated_total_heat_rejection_rate_curve_name

        Returns:
            str: the value of `rated_total_heat_rejection_rate_curve_name` or None if not set
        """
        return self._data["Rated Total Heat Rejection Rate Curve Name"]

    @rated_total_heat_rejection_rate_curve_name.setter
    def rated_total_heat_rejection_rate_curve_name(self, value=None):
        """  Corresponds to IDD Field `Rated Total Heat Rejection Rate Curve Name`
        Table:OneIndependentVariable object can also be used
        Be sure the rating corresponds to the correct refrigerant (R744)
        HeatRejection(W)=C1 +C2(Gas Cooler Outlet Temp - Entering Air Temp, deg C)
        Will be adjusted for elevation automatically

        Args:
            value (str): value for IDD Field `Rated Total Heat Rejection Rate Curve Name`
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
                                 'for field `rated_total_heat_rejection_rate_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `rated_total_heat_rejection_rate_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `rated_total_heat_rejection_rate_curve_name`')
        self._data["Rated Total Heat Rejection Rate Curve Name"] = value

    @property
    def gas_cooler_fan_speed_control_type(self):
        """Get gas_cooler_fan_speed_control_type

        Returns:
            str: the value of `gas_cooler_fan_speed_control_type` or None if not set
        """
        return self._data["Gas Cooler Fan Speed Control Type"]

    @gas_cooler_fan_speed_control_type.setter
    def gas_cooler_fan_speed_control_type(self, value="Fixed"):
        """  Corresponds to IDD Field `Gas Cooler Fan Speed Control Type`

        Args:
            value (str): value for IDD Field `Gas Cooler Fan Speed Control Type`
                Accepted values are:
                      - Fixed
                      - FixedLinear
                      - VariableSpeed
                      - TwoSpeed
                Default value: Fixed
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
                                 'for field `gas_cooler_fan_speed_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gas_cooler_fan_speed_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `gas_cooler_fan_speed_control_type`')
            vals = {}
            vals["fixed"] = "Fixed"
            vals["fixedlinear"] = "FixedLinear"
            vals["variablespeed"] = "VariableSpeed"
            vals["twospeed"] = "TwoSpeed"
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
                                     'field `gas_cooler_fan_speed_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Gas Cooler Fan Speed Control Type"] = value

    @property
    def rated_fan_power(self):
        """Get rated_fan_power

        Returns:
            float: the value of `rated_fan_power` or None if not set
        """
        return self._data["Rated Fan Power"]

    @rated_fan_power.setter
    def rated_fan_power(self, value=5000.0):
        """  Corresponds to IDD Field `Rated Fan Power`
        Power for gas cooler fan(s) corresponding to rated total heat rejection effect.

        Args:
            value (float): value for IDD Field `Rated Fan Power`
                Units: W
                Default value: 5000.0
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
                                 'for field `rated_fan_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_fan_power`')
        self._data["Rated Fan Power"] = value

    @property
    def minimum_fan_air_flow_ratio(self):
        """Get minimum_fan_air_flow_ratio

        Returns:
            float: the value of `minimum_fan_air_flow_ratio` or None if not set
        """
        return self._data["Minimum Fan Air Flow Ratio"]

    @minimum_fan_air_flow_ratio.setter
    def minimum_fan_air_flow_ratio(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Fan Air Flow Ratio`
        Minimum air flow fraction through gas cooler fan

        Args:
            value (float): value for IDD Field `Minimum Fan Air Flow Ratio`
                Units: dimensionless
                Default value: 0.2
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
                                 'for field `minimum_fan_air_flow_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_fan_air_flow_ratio`')
        self._data["Minimum Fan Air Flow Ratio"] = value

    @property
    def transition_temperature(self):
        """Get transition_temperature

        Returns:
            float: the value of `transition_temperature` or None if not set
        """
        return self._data["Transition Temperature"]

    @transition_temperature.setter
    def transition_temperature(self, value=27.0):
        """  Corresponds to IDD Field `Transition Temperature`
        Temperature at which system transitions between subcritical and transcritical operation.

        Args:
            value (float): value for IDD Field `Transition Temperature`
                Units: C
                Default value: 27.0
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
                                 'for field `transition_temperature`'.format(value))
        self._data["Transition Temperature"] = value

    @property
    def transcritical_approach_temperature(self):
        """Get transcritical_approach_temperature

        Returns:
            float: the value of `transcritical_approach_temperature` or None if not set
        """
        return self._data["Transcritical Approach Temperature"]

    @transcritical_approach_temperature.setter
    def transcritical_approach_temperature(self, value=3.0):
        """  Corresponds to IDD Field `Transcritical Approach Temperature`
        Temperature difference between the CO2 exiting the gas cooler and the air entering the
        gas cooler during transcritical operation.

        Args:
            value (float): value for IDD Field `Transcritical Approach Temperature`
                Units: DeltaC
                Default value: 3.0
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
                                 'for field `transcritical_approach_temperature`'.format(value))
        self._data["Transcritical Approach Temperature"] = value

    @property
    def subcritical_temperature_difference(self):
        """Get subcritical_temperature_difference

        Returns:
            float: the value of `subcritical_temperature_difference` or None if not set
        """
        return self._data["Subcritical Temperature Difference"]

    @subcritical_temperature_difference.setter
    def subcritical_temperature_difference(self, value=10.0):
        """  Corresponds to IDD Field `Subcritical Temperature Difference`
        Temperature difference between the saturated condensing temperature and the air
        temperature during subcritical operation.

        Args:
            value (float): value for IDD Field `Subcritical Temperature Difference`
                Units: DeltaC
                Default value: 10.0
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
                                 'for field `subcritical_temperature_difference`'.format(value))
        self._data["Subcritical Temperature Difference"] = value

    @property
    def minimum_condensing_temperature(self):
        """Get minimum_condensing_temperature

        Returns:
            float: the value of `minimum_condensing_temperature` or None if not set
        """
        return self._data["Minimum Condensing Temperature"]

    @minimum_condensing_temperature.setter
    def minimum_condensing_temperature(self, value=10.0):
        """  Corresponds to IDD Field `Minimum Condensing Temperature`
        Minimum saturated condensing temperature during subcritical operation.

        Args:
            value (float): value for IDD Field `Minimum Condensing Temperature`
                Units: C
                Default value: 10.0
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
                                 'for field `minimum_condensing_temperature`'.format(value))
        self._data["Minimum Condensing Temperature"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`
        If field is left blank,
        then the model assumes that the inlet air
        conditions are the outdoor air conditions for the current timestep
        (e.g., no adjustment for height above ground).

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
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
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    @property
    def gas_cooler_refrigerant_operating_charge_inventory(self):
        """Get gas_cooler_refrigerant_operating_charge_inventory

        Returns:
            float: the value of `gas_cooler_refrigerant_operating_charge_inventory` or None if not set
        """
        return self._data["Gas Cooler Refrigerant Operating Charge Inventory"]

    @gas_cooler_refrigerant_operating_charge_inventory.setter
    def gas_cooler_refrigerant_operating_charge_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Gas Cooler Refrigerant Operating Charge Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Gas Cooler Refrigerant Operating Charge Inventory`
                Units: kg
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
                                 'for field `gas_cooler_refrigerant_operating_charge_inventory`'.format(value))
        self._data["Gas Cooler Refrigerant Operating Charge Inventory"] = value

    @property
    def gas_cooler_receiver_refrigerant_inventory(self):
        """Get gas_cooler_receiver_refrigerant_inventory

        Returns:
            float: the value of `gas_cooler_receiver_refrigerant_inventory` or None if not set
        """
        return self._data["Gas Cooler Receiver Refrigerant Inventory"]

    @gas_cooler_receiver_refrigerant_inventory.setter
    def gas_cooler_receiver_refrigerant_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Gas Cooler Receiver Refrigerant Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Gas Cooler Receiver Refrigerant Inventory`
                Units: kg
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
                                 'for field `gas_cooler_receiver_refrigerant_inventory`'.format(value))
        self._data["Gas Cooler Receiver Refrigerant Inventory"] = value

    @property
    def gas_cooler_outlet_piping_refrigerant_inventory(self):
        """Get gas_cooler_outlet_piping_refrigerant_inventory

        Returns:
            float: the value of `gas_cooler_outlet_piping_refrigerant_inventory` or None if not set
        """
        return self._data["Gas Cooler Outlet Piping Refrigerant Inventory"]

    @gas_cooler_outlet_piping_refrigerant_inventory.setter
    def gas_cooler_outlet_piping_refrigerant_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Gas Cooler Outlet Piping Refrigerant Inventory`
        optional input

        Args:
            value (float): value for IDD Field `Gas Cooler Outlet Piping Refrigerant Inventory`
                Units: kg
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
                                 'for field `gas_cooler_outlet_piping_refrigerant_inventory`'.format(value))
        self._data["Gas Cooler Outlet Piping Refrigerant Inventory"] = value

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

class RefrigerationTransferLoadList(object):
    """ Corresponds to IDD object `Refrigeration:TransferLoadList`
        A refrigeration system may provide cooling to other, secondary, systems through
        either a secondary loop or a cascade condenser. If multiple transfer loads are served
        by a single primary system, use this list to group them together for reference by the
        primary system (see the field "Refrigeration Transfer Load or TransferLoad List Name"
        in the Refrigeration:System object).
    
    """
    internal_name = "Refrigeration:TransferLoadList"
    field_count = 10
    required_fields = ["Name", "Cascade Condenser Name or Secondary System 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:TransferLoadList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Cascade Condenser Name or Secondary System 1 Name"] = None
        self._data["Cascade Condenser Name or Secondary System 2 Name"] = None
        self._data["Cascade Condenser Name or Secondary System 3 Name"] = None
        self._data["Cascade Condenser Name or Secondary System 4 Name"] = None
        self._data["Cascade Condenser Name or Secondary System 5 Name"] = None
        self._data["Cascade Condenser Name or Secondary System 6 Name"] = None
        self._data["Cascade Condenser Name or Secondary System 7 Name"] = None
        self._data["Cascade Condenser Name or Secondary System 8 Name"] = None
        self._data["Cascade Condenser Name or Secondary System 9 Name"] = None
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
            self.cascade_condenser_name_or_secondary_system_1_name = None
        else:
            self.cascade_condenser_name_or_secondary_system_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cascade_condenser_name_or_secondary_system_2_name = None
        else:
            self.cascade_condenser_name_or_secondary_system_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cascade_condenser_name_or_secondary_system_3_name = None
        else:
            self.cascade_condenser_name_or_secondary_system_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cascade_condenser_name_or_secondary_system_4_name = None
        else:
            self.cascade_condenser_name_or_secondary_system_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cascade_condenser_name_or_secondary_system_5_name = None
        else:
            self.cascade_condenser_name_or_secondary_system_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cascade_condenser_name_or_secondary_system_6_name = None
        else:
            self.cascade_condenser_name_or_secondary_system_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cascade_condenser_name_or_secondary_system_7_name = None
        else:
            self.cascade_condenser_name_or_secondary_system_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cascade_condenser_name_or_secondary_system_8_name = None
        else:
            self.cascade_condenser_name_or_secondary_system_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cascade_condenser_name_or_secondary_system_9_name = None
        else:
            self.cascade_condenser_name_or_secondary_system_9_name = vals[i]
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
    def cascade_condenser_name_or_secondary_system_1_name(self):
        """Get cascade_condenser_name_or_secondary_system_1_name

        Returns:
            str: the value of `cascade_condenser_name_or_secondary_system_1_name` or None if not set
        """
        return self._data["Cascade Condenser Name or Secondary System 1 Name"]

    @cascade_condenser_name_or_secondary_system_1_name.setter
    def cascade_condenser_name_or_secondary_system_1_name(self, value=None):
        """  Corresponds to IDD Field `Cascade Condenser Name or Secondary System 1 Name`
        Enter the name of a Refrigeration:Condenser:Cascade object OR
        the name of a Refrigeration:SecondarySystem object.

        Args:
            value (str): value for IDD Field `Cascade Condenser Name or Secondary System 1 Name`
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
                                 'for field `cascade_condenser_name_or_secondary_system_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cascade_condenser_name_or_secondary_system_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cascade_condenser_name_or_secondary_system_1_name`')
        self._data["Cascade Condenser Name or Secondary System 1 Name"] = value

    @property
    def cascade_condenser_name_or_secondary_system_2_name(self):
        """Get cascade_condenser_name_or_secondary_system_2_name

        Returns:
            str: the value of `cascade_condenser_name_or_secondary_system_2_name` or None if not set
        """
        return self._data["Cascade Condenser Name or Secondary System 2 Name"]

    @cascade_condenser_name_or_secondary_system_2_name.setter
    def cascade_condenser_name_or_secondary_system_2_name(self, value=None):
        """  Corresponds to IDD Field `Cascade Condenser Name or Secondary System 2 Name`
        Enter the name of a Refrigeration:Condenser:Cascade object OR
        the name of a Refrigeration:SecondarySystem object.

        Args:
            value (str): value for IDD Field `Cascade Condenser Name or Secondary System 2 Name`
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
                                 'for field `cascade_condenser_name_or_secondary_system_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cascade_condenser_name_or_secondary_system_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cascade_condenser_name_or_secondary_system_2_name`')
        self._data["Cascade Condenser Name or Secondary System 2 Name"] = value

    @property
    def cascade_condenser_name_or_secondary_system_3_name(self):
        """Get cascade_condenser_name_or_secondary_system_3_name

        Returns:
            str: the value of `cascade_condenser_name_or_secondary_system_3_name` or None if not set
        """
        return self._data["Cascade Condenser Name or Secondary System 3 Name"]

    @cascade_condenser_name_or_secondary_system_3_name.setter
    def cascade_condenser_name_or_secondary_system_3_name(self, value=None):
        """  Corresponds to IDD Field `Cascade Condenser Name or Secondary System 3 Name`
        Enter the name of a Refrigeration:Condenser:Cascade object OR
        the name of a Refrigeration:SecondarySystem object.

        Args:
            value (str): value for IDD Field `Cascade Condenser Name or Secondary System 3 Name`
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
                                 'for field `cascade_condenser_name_or_secondary_system_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cascade_condenser_name_or_secondary_system_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cascade_condenser_name_or_secondary_system_3_name`')
        self._data["Cascade Condenser Name or Secondary System 3 Name"] = value

    @property
    def cascade_condenser_name_or_secondary_system_4_name(self):
        """Get cascade_condenser_name_or_secondary_system_4_name

        Returns:
            str: the value of `cascade_condenser_name_or_secondary_system_4_name` or None if not set
        """
        return self._data["Cascade Condenser Name or Secondary System 4 Name"]

    @cascade_condenser_name_or_secondary_system_4_name.setter
    def cascade_condenser_name_or_secondary_system_4_name(self, value=None):
        """  Corresponds to IDD Field `Cascade Condenser Name or Secondary System 4 Name`
        Enter the name of a Refrigeration:Condenser:Cascade object OR
        the name of a Refrigeration:SecondarySystem object.

        Args:
            value (str): value for IDD Field `Cascade Condenser Name or Secondary System 4 Name`
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
                                 'for field `cascade_condenser_name_or_secondary_system_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cascade_condenser_name_or_secondary_system_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cascade_condenser_name_or_secondary_system_4_name`')
        self._data["Cascade Condenser Name or Secondary System 4 Name"] = value

    @property
    def cascade_condenser_name_or_secondary_system_5_name(self):
        """Get cascade_condenser_name_or_secondary_system_5_name

        Returns:
            str: the value of `cascade_condenser_name_or_secondary_system_5_name` or None if not set
        """
        return self._data["Cascade Condenser Name or Secondary System 5 Name"]

    @cascade_condenser_name_or_secondary_system_5_name.setter
    def cascade_condenser_name_or_secondary_system_5_name(self, value=None):
        """  Corresponds to IDD Field `Cascade Condenser Name or Secondary System 5 Name`
        Enter the name of a Refrigeration:Condenser:Cascade object OR
        the name of a Refrigeration:SecondarySystem object.

        Args:
            value (str): value for IDD Field `Cascade Condenser Name or Secondary System 5 Name`
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
                                 'for field `cascade_condenser_name_or_secondary_system_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cascade_condenser_name_or_secondary_system_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cascade_condenser_name_or_secondary_system_5_name`')
        self._data["Cascade Condenser Name or Secondary System 5 Name"] = value

    @property
    def cascade_condenser_name_or_secondary_system_6_name(self):
        """Get cascade_condenser_name_or_secondary_system_6_name

        Returns:
            str: the value of `cascade_condenser_name_or_secondary_system_6_name` or None if not set
        """
        return self._data["Cascade Condenser Name or Secondary System 6 Name"]

    @cascade_condenser_name_or_secondary_system_6_name.setter
    def cascade_condenser_name_or_secondary_system_6_name(self, value=None):
        """  Corresponds to IDD Field `Cascade Condenser Name or Secondary System 6 Name`
        Enter the name of a Refrigeration:Condenser:Cascade object OR
        the name of a Refrigeration:SecondarySystem object.

        Args:
            value (str): value for IDD Field `Cascade Condenser Name or Secondary System 6 Name`
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
                                 'for field `cascade_condenser_name_or_secondary_system_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cascade_condenser_name_or_secondary_system_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cascade_condenser_name_or_secondary_system_6_name`')
        self._data["Cascade Condenser Name or Secondary System 6 Name"] = value

    @property
    def cascade_condenser_name_or_secondary_system_7_name(self):
        """Get cascade_condenser_name_or_secondary_system_7_name

        Returns:
            str: the value of `cascade_condenser_name_or_secondary_system_7_name` or None if not set
        """
        return self._data["Cascade Condenser Name or Secondary System 7 Name"]

    @cascade_condenser_name_or_secondary_system_7_name.setter
    def cascade_condenser_name_or_secondary_system_7_name(self, value=None):
        """  Corresponds to IDD Field `Cascade Condenser Name or Secondary System 7 Name`
        Enter the name of a Refrigeration:Condenser:Cascade object OR
        the name of a Refrigeration:SecondarySystem object.

        Args:
            value (str): value for IDD Field `Cascade Condenser Name or Secondary System 7 Name`
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
                                 'for field `cascade_condenser_name_or_secondary_system_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cascade_condenser_name_or_secondary_system_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cascade_condenser_name_or_secondary_system_7_name`')
        self._data["Cascade Condenser Name or Secondary System 7 Name"] = value

    @property
    def cascade_condenser_name_or_secondary_system_8_name(self):
        """Get cascade_condenser_name_or_secondary_system_8_name

        Returns:
            str: the value of `cascade_condenser_name_or_secondary_system_8_name` or None if not set
        """
        return self._data["Cascade Condenser Name or Secondary System 8 Name"]

    @cascade_condenser_name_or_secondary_system_8_name.setter
    def cascade_condenser_name_or_secondary_system_8_name(self, value=None):
        """  Corresponds to IDD Field `Cascade Condenser Name or Secondary System 8 Name`
        Enter the name of a Refrigeration:Condenser:Cascade object OR
        the name of a Refrigeration:SecondarySystem object.

        Args:
            value (str): value for IDD Field `Cascade Condenser Name or Secondary System 8 Name`
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
                                 'for field `cascade_condenser_name_or_secondary_system_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cascade_condenser_name_or_secondary_system_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cascade_condenser_name_or_secondary_system_8_name`')
        self._data["Cascade Condenser Name or Secondary System 8 Name"] = value

    @property
    def cascade_condenser_name_or_secondary_system_9_name(self):
        """Get cascade_condenser_name_or_secondary_system_9_name

        Returns:
            str: the value of `cascade_condenser_name_or_secondary_system_9_name` or None if not set
        """
        return self._data["Cascade Condenser Name or Secondary System 9 Name"]

    @cascade_condenser_name_or_secondary_system_9_name.setter
    def cascade_condenser_name_or_secondary_system_9_name(self, value=None):
        """  Corresponds to IDD Field `Cascade Condenser Name or Secondary System 9 Name`
        Enter the name of a Refrigeration:Condenser:Cascade object OR
        the name of a Refrigeration:SecondarySystem object.

        Args:
            value (str): value for IDD Field `Cascade Condenser Name or Secondary System 9 Name`
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
                                 'for field `cascade_condenser_name_or_secondary_system_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cascade_condenser_name_or_secondary_system_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cascade_condenser_name_or_secondary_system_9_name`')
        self._data["Cascade Condenser Name or Secondary System 9 Name"] = value

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

class RefrigerationSubcooler(object):
    """ Corresponds to IDD object `Refrigeration:Subcooler`
        Two types of subcoolers are modeled by the detailed refrigeration system.  The
        liquid suction heat exchanger uses cool suction gas to subcool the hot condensate
        after it leaves the condenser and before it reaches the thermal expansion valve.
        A mechanical subcooler is used to transfer cooling capacity from one refrigeration
        system to another.
    
    """
    internal_name = "Refrigeration:Subcooler"
    field_count = 7
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:Subcooler`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Subcooler Type"] = None
        self._data["Liquid Suction Design Subcooling Temperature Difference"] = None
        self._data["Design Liquid Inlet Temperature"] = None
        self._data["Design Vapor Inlet Temperature"] = None
        self._data["Capacity-Providing System"] = None
        self._data["Outlet Control Temperature"] = None
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
            self.subcooler_type = None
        else:
            self.subcooler_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.liquid_suction_design_subcooling_temperature_difference = None
        else:
            self.liquid_suction_design_subcooling_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_liquid_inlet_temperature = None
        else:
            self.design_liquid_inlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_vapor_inlet_temperature = None
        else:
            self.design_vapor_inlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.capacityproviding_system = None
        else:
            self.capacityproviding_system = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_control_temperature = None
        else:
            self.outlet_control_temperature = vals[i]
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
    def subcooler_type(self):
        """Get subcooler_type

        Returns:
            str: the value of `subcooler_type` or None if not set
        """
        return self._data["Subcooler Type"]

    @subcooler_type.setter
    def subcooler_type(self, value="LiquidSuction"):
        """  Corresponds to IDD Field `Subcooler Type`
        plan to add ambient subcoolers at future time

        Args:
            value (str): value for IDD Field `Subcooler Type`
                Accepted values are:
                      - Mechanical
                      - LiquidSuction
                Default value: LiquidSuction
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
                                 'for field `subcooler_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `subcooler_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `subcooler_type`')
            vals = {}
            vals["mechanical"] = "Mechanical"
            vals["liquidsuction"] = "LiquidSuction"
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
                                     'field `subcooler_type`'.format(value))
            value = vals[value_lower]
        self._data["Subcooler Type"] = value

    @property
    def liquid_suction_design_subcooling_temperature_difference(self):
        """Get liquid_suction_design_subcooling_temperature_difference

        Returns:
            float: the value of `liquid_suction_design_subcooling_temperature_difference` or None if not set
        """
        return self._data["Liquid Suction Design Subcooling Temperature Difference"]

    @liquid_suction_design_subcooling_temperature_difference.setter
    def liquid_suction_design_subcooling_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `Liquid Suction Design Subcooling Temperature Difference`
        Applicable only and required for liquid suction heat exchangers
        design liquid suction subcooling

        Args:
            value (float): value for IDD Field `Liquid Suction Design Subcooling Temperature Difference`
                Units: DeltaC
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
                                 'for field `liquid_suction_design_subcooling_temperature_difference`'.format(value))
        self._data["Liquid Suction Design Subcooling Temperature Difference"] = value

    @property
    def design_liquid_inlet_temperature(self):
        """Get design_liquid_inlet_temperature

        Returns:
            float: the value of `design_liquid_inlet_temperature` or None if not set
        """
        return self._data["Design Liquid Inlet Temperature"]

    @design_liquid_inlet_temperature.setter
    def design_liquid_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Liquid Inlet Temperature`
        design inlet temperature on liquid side
        Applicable only and required for liquid suction heat exchangers (LSHX)

        Args:
            value (float): value for IDD Field `Design Liquid Inlet Temperature`
                Units: C
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
                                 'for field `design_liquid_inlet_temperature`'.format(value))
        self._data["Design Liquid Inlet Temperature"] = value

    @property
    def design_vapor_inlet_temperature(self):
        """Get design_vapor_inlet_temperature

        Returns:
            float: the value of `design_vapor_inlet_temperature` or None if not set
        """
        return self._data["Design Vapor Inlet Temperature"]

    @design_vapor_inlet_temperature.setter
    def design_vapor_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `Design Vapor Inlet Temperature`
        design inlet temperature on vapor side
        Applicable only and required for liquid suction heat exchangers (LSHX)
        Design vapor inlet temperature must be less than or equal to
        the Liquid inlet design temp

        Args:
            value (float): value for IDD Field `Design Vapor Inlet Temperature`
                Units: C
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
                                 'for field `design_vapor_inlet_temperature`'.format(value))
        self._data["Design Vapor Inlet Temperature"] = value

    @property
    def capacityproviding_system(self):
        """Get capacityproviding_system

        Returns:
            str: the value of `capacityproviding_system` or None if not set
        """
        return self._data["Capacity-Providing System"]

    @capacityproviding_system.setter
    def capacityproviding_system(self, value=None):
        """  Corresponds to IDD Field `Capacity-Providing System`
        Name of the Detailed Refrigeration System providing cooling capacity
        Applicable only and required for mechanical subcoolers

        Args:
            value (str): value for IDD Field `Capacity-Providing System`
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
                                 'for field `capacityproviding_system`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacityproviding_system`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `capacityproviding_system`')
        self._data["Capacity-Providing System"] = value

    @property
    def outlet_control_temperature(self):
        """Get outlet_control_temperature

        Returns:
            float: the value of `outlet_control_temperature` or None if not set
        """
        return self._data["Outlet Control Temperature"]

    @outlet_control_temperature.setter
    def outlet_control_temperature(self, value=None):
        """  Corresponds to IDD Field `Outlet Control Temperature`
        Control Temperature Out for subcooled liquid
        Applicable only and required for mechanical subcoolers

        Args:
            value (float): value for IDD Field `Outlet Control Temperature`
                Units: C
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
                                 'for field `outlet_control_temperature`'.format(value))
        self._data["Outlet Control Temperature"] = value

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

class RefrigerationCompressor(object):
    """ Corresponds to IDD object `Refrigeration:Compressor`
        Refrigeration system compressor. Data is available for many compressors
        in the RefrigerationCompressor.idf dataset
    
    """
    internal_name = "Refrigeration:Compressor"
    field_count = 11
    required_fields = ["Name", "Refrigeration Compressor Power Curve Name", "Refrigeration Compressor Capacity Curve Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:Compressor`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Refrigeration Compressor Power Curve Name"] = None
        self._data["Refrigeration Compressor Capacity Curve Name"] = None
        self._data["Rated Superheat"] = None
        self._data["Rated Return Gas Temperature"] = None
        self._data["Rated Liquid Temperature"] = None
        self._data["Rated Subcooling"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Mode of Operation"] = None
        self._data["Transcritical Compressor Power Curve Name"] = None
        self._data["Transcritical Compressor Capacity Curve Name"] = None
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
            self.refrigeration_compressor_power_curve_name = None
        else:
            self.refrigeration_compressor_power_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_capacity_curve_name = None
        else:
            self.refrigeration_compressor_capacity_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_superheat = None
        else:
            self.rated_superheat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_return_gas_temperature = None
        else:
            self.rated_return_gas_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_liquid_temperature = None
        else:
            self.rated_liquid_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_subcooling = None
        else:
            self.rated_subcooling = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mode_of_operation = None
        else:
            self.mode_of_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transcritical_compressor_power_curve_name = None
        else:
            self.transcritical_compressor_power_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transcritical_compressor_capacity_curve_name = None
        else:
            self.transcritical_compressor_capacity_curve_name = vals[i]
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
    def refrigeration_compressor_power_curve_name(self):
        """Get refrigeration_compressor_power_curve_name

        Returns:
            str: the value of `refrigeration_compressor_power_curve_name` or None if not set
        """
        return self._data["Refrigeration Compressor Power Curve Name"]

    @refrigeration_compressor_power_curve_name.setter
    def refrigeration_compressor_power_curve_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor Power Curve Name`
        Table:TwoIndependentVariable object can also be used
        the input order for the Curve:Bicubic does not
        match the ARI 540-2004 Eq. 1 coefficient order
        N1 is ARI_C1, N2 is ARI_C2, N3 is ARI_C4, N4 is ARI_C3,
        N5 is ARI_C6, N6 is ARI_C5, N7 is ARI_C7, N8 is ARI_C10,
        N9 is ARI_C8, N10 is ARI_C9,
        N11 is Minimum Suction dewpoint temperature,
        N12 is Maximum Suction dewpoint temperature,
        N13 is Minimum Discharge dewpoint temperature,
        N14 is Maximum Discharge dewpoint temperature

        Args:
            value (str): value for IDD Field `Refrigeration Compressor Power Curve Name`
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
                                 'for field `refrigeration_compressor_power_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_power_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_power_curve_name`')
        self._data["Refrigeration Compressor Power Curve Name"] = value

    @property
    def refrigeration_compressor_capacity_curve_name(self):
        """Get refrigeration_compressor_capacity_curve_name

        Returns:
            str: the value of `refrigeration_compressor_capacity_curve_name` or None if not set
        """
        return self._data["Refrigeration Compressor Capacity Curve Name"]

    @refrigeration_compressor_capacity_curve_name.setter
    def refrigeration_compressor_capacity_curve_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor Capacity Curve Name`
        Table:TwoIndependentVariable object can also be used
        the input order for the Curve:Bicubic does not
        match the ARI 540-2004 Eq. 1 coefficient order
        N1 is ARI_C1, N2 is ARI_C2, N3 is ARI_C4, N4 is ARI_C3,
        N5 is ARI_C6, N6 is ARI_C5, N7 is ARI_C7, N8 is ARI_C10,
        N9 is ARI_C8, N10 is ARI_C9,
        N11 is Minimum Suction dewpoint temperature,
        N12 is Maximum Suction dewpoint temperature,
        N13 is Minimum Discharge dewpoint temperature,
        N14 is Maximum Discharge dewpoint temperature

        Args:
            value (str): value for IDD Field `Refrigeration Compressor Capacity Curve Name`
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
                                 'for field `refrigeration_compressor_capacity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_capacity_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_capacity_curve_name`')
        self._data["Refrigeration Compressor Capacity Curve Name"] = value

    @property
    def rated_superheat(self):
        """Get rated_superheat

        Returns:
            float: the value of `rated_superheat` or None if not set
        """
        return self._data["Rated Superheat"]

    @rated_superheat.setter
    def rated_superheat(self, value=None):
        """  Corresponds to IDD Field `Rated Superheat`
        Use this input field OR the next, not both
        This is used if the compressor rating is based upon
        degrees of superheat

        Args:
            value (float): value for IDD Field `Rated Superheat`
                Units: deltaC
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
                                 'for field `rated_superheat`'.format(value))
        self._data["Rated Superheat"] = value

    @property
    def rated_return_gas_temperature(self):
        """Get rated_return_gas_temperature

        Returns:
            float: the value of `rated_return_gas_temperature` or None if not set
        """
        return self._data["Rated Return Gas Temperature"]

    @rated_return_gas_temperature.setter
    def rated_return_gas_temperature(self, value=None):
        """  Corresponds to IDD Field `Rated Return Gas Temperature`
        Use this input field OR the previous, not both
        This is used if the compressor rating is based upon
        rated return gas temperature (Rated Suction Temperature)

        Args:
            value (float): value for IDD Field `Rated Return Gas Temperature`
                Units: C
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
                                 'for field `rated_return_gas_temperature`'.format(value))
        self._data["Rated Return Gas Temperature"] = value

    @property
    def rated_liquid_temperature(self):
        """Get rated_liquid_temperature

        Returns:
            float: the value of `rated_liquid_temperature` or None if not set
        """
        return self._data["Rated Liquid Temperature"]

    @rated_liquid_temperature.setter
    def rated_liquid_temperature(self, value=None):
        """  Corresponds to IDD Field `Rated Liquid Temperature`
        Use this input field OR the next, not both
        This is used if the compressor rating is based upon
        rated liquid temperature at the expansion valve

        Args:
            value (float): value for IDD Field `Rated Liquid Temperature`
                Units: C
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
                                 'for field `rated_liquid_temperature`'.format(value))
        self._data["Rated Liquid Temperature"] = value

    @property
    def rated_subcooling(self):
        """Get rated_subcooling

        Returns:
            float: the value of `rated_subcooling` or None if not set
        """
        return self._data["Rated Subcooling"]

    @rated_subcooling.setter
    def rated_subcooling(self, value=None):
        """  Corresponds to IDD Field `Rated Subcooling`
        Use this input field OR the previous, not both
        This is used if the compressor rating is based upon
        degrees of subcooling

        Args:
            value (float): value for IDD Field `Rated Subcooling`
                Units: deltaC
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
                                 'for field `rated_subcooling`'.format(value))
        self._data["Rated Subcooling"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    @property
    def mode_of_operation(self):
        """Get mode_of_operation

        Returns:
            str: the value of `mode_of_operation` or None if not set
        """
        return self._data["Mode of Operation"]

    @mode_of_operation.setter
    def mode_of_operation(self, value="Subcritical"):
        """  Corresponds to IDD Field `Mode of Operation`

        Args:
            value (str): value for IDD Field `Mode of Operation`
                Accepted values are:
                      - Subcritical
                      - Transcritical
                Default value: Subcritical
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
                                 'for field `mode_of_operation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mode_of_operation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `mode_of_operation`')
            vals = {}
            vals["subcritical"] = "Subcritical"
            vals["transcritical"] = "Transcritical"
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
                                     'field `mode_of_operation`'.format(value))
            value = vals[value_lower]
        self._data["Mode of Operation"] = value

    @property
    def transcritical_compressor_power_curve_name(self):
        """Get transcritical_compressor_power_curve_name

        Returns:
            str: the value of `transcritical_compressor_power_curve_name` or None if not set
        """
        return self._data["Transcritical Compressor Power Curve Name"]

    @transcritical_compressor_power_curve_name.setter
    def transcritical_compressor_power_curve_name(self, value=None):
        """  Corresponds to IDD Field `Transcritical Compressor Power Curve Name`

        Args:
            value (str): value for IDD Field `Transcritical Compressor Power Curve Name`
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
                                 'for field `transcritical_compressor_power_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `transcritical_compressor_power_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `transcritical_compressor_power_curve_name`')
        self._data["Transcritical Compressor Power Curve Name"] = value

    @property
    def transcritical_compressor_capacity_curve_name(self):
        """Get transcritical_compressor_capacity_curve_name

        Returns:
            str: the value of `transcritical_compressor_capacity_curve_name` or None if not set
        """
        return self._data["Transcritical Compressor Capacity Curve Name"]

    @transcritical_compressor_capacity_curve_name.setter
    def transcritical_compressor_capacity_curve_name(self, value=None):
        """  Corresponds to IDD Field `Transcritical Compressor Capacity Curve Name`

        Args:
            value (str): value for IDD Field `Transcritical Compressor Capacity Curve Name`
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
                                 'for field `transcritical_compressor_capacity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `transcritical_compressor_capacity_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `transcritical_compressor_capacity_curve_name`')
        self._data["Transcritical Compressor Capacity Curve Name"] = value

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

class RefrigerationCompressorList(object):
    """ Corresponds to IDD object `Refrigeration:CompressorList`
        List of all the compressors included within a single refrigeration system
        (Refrigeration:System). Each list must contain at least one compressor.
        The order in which the individual compressors are listed here will be the
        order in which the compressors are dispatched to meet the system load.
        IMPORTANT: List compressor names in the order in which the compressors will be loaded
        Data is available for many compressors in the RefrigerationCompressor.idf dataset
    
    """
    internal_name = "Refrigeration:CompressorList"
    field_count = 41
    required_fields = ["Name", "Refrigeration Compressor 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:CompressorList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Refrigeration Compressor 1 Name"] = None
        self._data["Refrigeration Compressor 2 Name"] = None
        self._data["Refrigeration Compressor 3 Name"] = None
        self._data["Refrigeration Compressor 4 Name"] = None
        self._data["Refrigeration Compressor 5 Name"] = None
        self._data["Refrigeration Compressor 6 Name"] = None
        self._data["Refrigeration Compressor 7 Name"] = None
        self._data["Refrigeration Compressor 8 Name"] = None
        self._data["Refrigeration Compressor 9 Name"] = None
        self._data["Refrigeration Compressor 10 Name"] = None
        self._data["Refrigeration Compressor 11 Name"] = None
        self._data["Refrigeration Compressor 12  Name"] = None
        self._data["Refrigeration Compressor 13 Name"] = None
        self._data["Refrigeration Compressor 14 Name"] = None
        self._data["Refrigeration Compressor 15 Name"] = None
        self._data["Refrigeration Compressor 16 Name"] = None
        self._data["Refrigeration Compressor 17 Name"] = None
        self._data["Refrigeration Compressor 18 Name"] = None
        self._data["Refrigeration Compressor 19 Name"] = None
        self._data["Refrigeration Compressor 20 Name"] = None
        self._data["Refrigeration Compressor 21 Name"] = None
        self._data["Refrigeration Compressor 22 Name"] = None
        self._data["Refrigeration Compressor 23 Name"] = None
        self._data["Refrigeration Compressor 24 Name"] = None
        self._data["Refrigeration Compressor 25 Name"] = None
        self._data["Refrigeration Compressor 26 Name"] = None
        self._data["Refrigeration Compressor 27 Name"] = None
        self._data["Refrigeration Compressor 28 Name"] = None
        self._data["Refrigeration Compressor 29 Name"] = None
        self._data["Refrigeration Compressor 30 Name"] = None
        self._data["Refrigeration Compressor 31 Name"] = None
        self._data["Refrigeration Compressor 32 Name"] = None
        self._data["Refrigeration Compressor 33 Name"] = None
        self._data["Refrigeration Compressor 34 Name"] = None
        self._data["Refrigeration Compressor 35 Name"] = None
        self._data["Refrigeration Compressor 36 Name"] = None
        self._data["Refrigeration Compressor 37 Name"] = None
        self._data["Refrigeration Compressor 38 Name"] = None
        self._data["Refrigeration Compressor 39 Name"] = None
        self._data["Refrigeration Compressor 40 Name"] = None
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
            self.refrigeration_compressor_1_name = None
        else:
            self.refrigeration_compressor_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_2_name = None
        else:
            self.refrigeration_compressor_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_3_name = None
        else:
            self.refrigeration_compressor_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_4_name = None
        else:
            self.refrigeration_compressor_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_5_name = None
        else:
            self.refrigeration_compressor_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_6_name = None
        else:
            self.refrigeration_compressor_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_7_name = None
        else:
            self.refrigeration_compressor_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_8_name = None
        else:
            self.refrigeration_compressor_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_9_name = None
        else:
            self.refrigeration_compressor_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_10_name = None
        else:
            self.refrigeration_compressor_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_11_name = None
        else:
            self.refrigeration_compressor_11_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_12_name = None
        else:
            self.refrigeration_compressor_12_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_13_name = None
        else:
            self.refrigeration_compressor_13_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_14_name = None
        else:
            self.refrigeration_compressor_14_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_15_name = None
        else:
            self.refrigeration_compressor_15_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_16_name = None
        else:
            self.refrigeration_compressor_16_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_17_name = None
        else:
            self.refrigeration_compressor_17_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_18_name = None
        else:
            self.refrigeration_compressor_18_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_19_name = None
        else:
            self.refrigeration_compressor_19_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_20_name = None
        else:
            self.refrigeration_compressor_20_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_21_name = None
        else:
            self.refrigeration_compressor_21_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_22_name = None
        else:
            self.refrigeration_compressor_22_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_23_name = None
        else:
            self.refrigeration_compressor_23_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_24_name = None
        else:
            self.refrigeration_compressor_24_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_25_name = None
        else:
            self.refrigeration_compressor_25_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_26_name = None
        else:
            self.refrigeration_compressor_26_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_27_name = None
        else:
            self.refrigeration_compressor_27_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_28_name = None
        else:
            self.refrigeration_compressor_28_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_29_name = None
        else:
            self.refrigeration_compressor_29_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_30_name = None
        else:
            self.refrigeration_compressor_30_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_31_name = None
        else:
            self.refrigeration_compressor_31_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_32_name = None
        else:
            self.refrigeration_compressor_32_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_33_name = None
        else:
            self.refrigeration_compressor_33_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_34_name = None
        else:
            self.refrigeration_compressor_34_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_35_name = None
        else:
            self.refrigeration_compressor_35_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_36_name = None
        else:
            self.refrigeration_compressor_36_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_37_name = None
        else:
            self.refrigeration_compressor_37_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_38_name = None
        else:
            self.refrigeration_compressor_38_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_39_name = None
        else:
            self.refrigeration_compressor_39_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_compressor_40_name = None
        else:
            self.refrigeration_compressor_40_name = vals[i]
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
    def refrigeration_compressor_1_name(self):
        """Get refrigeration_compressor_1_name

        Returns:
            str: the value of `refrigeration_compressor_1_name` or None if not set
        """
        return self._data["Refrigeration Compressor 1 Name"]

    @refrigeration_compressor_1_name.setter
    def refrigeration_compressor_1_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 1 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 1 Name`
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
                                 'for field `refrigeration_compressor_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_1_name`')
        self._data["Refrigeration Compressor 1 Name"] = value

    @property
    def refrigeration_compressor_2_name(self):
        """Get refrigeration_compressor_2_name

        Returns:
            str: the value of `refrigeration_compressor_2_name` or None if not set
        """
        return self._data["Refrigeration Compressor 2 Name"]

    @refrigeration_compressor_2_name.setter
    def refrigeration_compressor_2_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 2 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 2 Name`
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
                                 'for field `refrigeration_compressor_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_2_name`')
        self._data["Refrigeration Compressor 2 Name"] = value

    @property
    def refrigeration_compressor_3_name(self):
        """Get refrigeration_compressor_3_name

        Returns:
            str: the value of `refrigeration_compressor_3_name` or None if not set
        """
        return self._data["Refrigeration Compressor 3 Name"]

    @refrigeration_compressor_3_name.setter
    def refrigeration_compressor_3_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 3 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 3 Name`
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
                                 'for field `refrigeration_compressor_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_3_name`')
        self._data["Refrigeration Compressor 3 Name"] = value

    @property
    def refrigeration_compressor_4_name(self):
        """Get refrigeration_compressor_4_name

        Returns:
            str: the value of `refrigeration_compressor_4_name` or None if not set
        """
        return self._data["Refrigeration Compressor 4 Name"]

    @refrigeration_compressor_4_name.setter
    def refrigeration_compressor_4_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 4 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 4 Name`
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
                                 'for field `refrigeration_compressor_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_4_name`')
        self._data["Refrigeration Compressor 4 Name"] = value

    @property
    def refrigeration_compressor_5_name(self):
        """Get refrigeration_compressor_5_name

        Returns:
            str: the value of `refrigeration_compressor_5_name` or None if not set
        """
        return self._data["Refrigeration Compressor 5 Name"]

    @refrigeration_compressor_5_name.setter
    def refrigeration_compressor_5_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 5 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 5 Name`
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
                                 'for field `refrigeration_compressor_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_5_name`')
        self._data["Refrigeration Compressor 5 Name"] = value

    @property
    def refrigeration_compressor_6_name(self):
        """Get refrigeration_compressor_6_name

        Returns:
            str: the value of `refrigeration_compressor_6_name` or None if not set
        """
        return self._data["Refrigeration Compressor 6 Name"]

    @refrigeration_compressor_6_name.setter
    def refrigeration_compressor_6_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 6 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 6 Name`
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
                                 'for field `refrigeration_compressor_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_6_name`')
        self._data["Refrigeration Compressor 6 Name"] = value

    @property
    def refrigeration_compressor_7_name(self):
        """Get refrigeration_compressor_7_name

        Returns:
            str: the value of `refrigeration_compressor_7_name` or None if not set
        """
        return self._data["Refrigeration Compressor 7 Name"]

    @refrigeration_compressor_7_name.setter
    def refrigeration_compressor_7_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 7 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 7 Name`
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
                                 'for field `refrigeration_compressor_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_7_name`')
        self._data["Refrigeration Compressor 7 Name"] = value

    @property
    def refrigeration_compressor_8_name(self):
        """Get refrigeration_compressor_8_name

        Returns:
            str: the value of `refrigeration_compressor_8_name` or None if not set
        """
        return self._data["Refrigeration Compressor 8 Name"]

    @refrigeration_compressor_8_name.setter
    def refrigeration_compressor_8_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 8 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 8 Name`
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
                                 'for field `refrigeration_compressor_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_8_name`')
        self._data["Refrigeration Compressor 8 Name"] = value

    @property
    def refrigeration_compressor_9_name(self):
        """Get refrigeration_compressor_9_name

        Returns:
            str: the value of `refrigeration_compressor_9_name` or None if not set
        """
        return self._data["Refrigeration Compressor 9 Name"]

    @refrigeration_compressor_9_name.setter
    def refrigeration_compressor_9_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 9 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 9 Name`
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
                                 'for field `refrigeration_compressor_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_9_name`')
        self._data["Refrigeration Compressor 9 Name"] = value

    @property
    def refrigeration_compressor_10_name(self):
        """Get refrigeration_compressor_10_name

        Returns:
            str: the value of `refrigeration_compressor_10_name` or None if not set
        """
        return self._data["Refrigeration Compressor 10 Name"]

    @refrigeration_compressor_10_name.setter
    def refrigeration_compressor_10_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 10 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 10 Name`
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
                                 'for field `refrigeration_compressor_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_10_name`')
        self._data["Refrigeration Compressor 10 Name"] = value

    @property
    def refrigeration_compressor_11_name(self):
        """Get refrigeration_compressor_11_name

        Returns:
            str: the value of `refrigeration_compressor_11_name` or None if not set
        """
        return self._data["Refrigeration Compressor 11 Name"]

    @refrigeration_compressor_11_name.setter
    def refrigeration_compressor_11_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 11 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 11 Name`
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
                                 'for field `refrigeration_compressor_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_11_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_11_name`')
        self._data["Refrigeration Compressor 11 Name"] = value

    @property
    def refrigeration_compressor_12_name(self):
        """Get refrigeration_compressor_12_name

        Returns:
            str: the value of `refrigeration_compressor_12_name` or None if not set
        """
        return self._data["Refrigeration Compressor 12  Name"]

    @refrigeration_compressor_12_name.setter
    def refrigeration_compressor_12_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 12  Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 12  Name`
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
                                 'for field `refrigeration_compressor_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_12_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_12_name`')
        self._data["Refrigeration Compressor 12  Name"] = value

    @property
    def refrigeration_compressor_13_name(self):
        """Get refrigeration_compressor_13_name

        Returns:
            str: the value of `refrigeration_compressor_13_name` or None if not set
        """
        return self._data["Refrigeration Compressor 13 Name"]

    @refrigeration_compressor_13_name.setter
    def refrigeration_compressor_13_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 13 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 13 Name`
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
                                 'for field `refrigeration_compressor_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_13_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_13_name`')
        self._data["Refrigeration Compressor 13 Name"] = value

    @property
    def refrigeration_compressor_14_name(self):
        """Get refrigeration_compressor_14_name

        Returns:
            str: the value of `refrigeration_compressor_14_name` or None if not set
        """
        return self._data["Refrigeration Compressor 14 Name"]

    @refrigeration_compressor_14_name.setter
    def refrigeration_compressor_14_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 14 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 14 Name`
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
                                 'for field `refrigeration_compressor_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_14_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_14_name`')
        self._data["Refrigeration Compressor 14 Name"] = value

    @property
    def refrigeration_compressor_15_name(self):
        """Get refrigeration_compressor_15_name

        Returns:
            str: the value of `refrigeration_compressor_15_name` or None if not set
        """
        return self._data["Refrigeration Compressor 15 Name"]

    @refrigeration_compressor_15_name.setter
    def refrigeration_compressor_15_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 15 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 15 Name`
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
                                 'for field `refrigeration_compressor_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_15_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_15_name`')
        self._data["Refrigeration Compressor 15 Name"] = value

    @property
    def refrigeration_compressor_16_name(self):
        """Get refrigeration_compressor_16_name

        Returns:
            str: the value of `refrigeration_compressor_16_name` or None if not set
        """
        return self._data["Refrigeration Compressor 16 Name"]

    @refrigeration_compressor_16_name.setter
    def refrigeration_compressor_16_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 16 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 16 Name`
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
                                 'for field `refrigeration_compressor_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_16_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_16_name`')
        self._data["Refrigeration Compressor 16 Name"] = value

    @property
    def refrigeration_compressor_17_name(self):
        """Get refrigeration_compressor_17_name

        Returns:
            str: the value of `refrigeration_compressor_17_name` or None if not set
        """
        return self._data["Refrigeration Compressor 17 Name"]

    @refrigeration_compressor_17_name.setter
    def refrigeration_compressor_17_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 17 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 17 Name`
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
                                 'for field `refrigeration_compressor_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_17_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_17_name`')
        self._data["Refrigeration Compressor 17 Name"] = value

    @property
    def refrigeration_compressor_18_name(self):
        """Get refrigeration_compressor_18_name

        Returns:
            str: the value of `refrigeration_compressor_18_name` or None if not set
        """
        return self._data["Refrigeration Compressor 18 Name"]

    @refrigeration_compressor_18_name.setter
    def refrigeration_compressor_18_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 18 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 18 Name`
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
                                 'for field `refrigeration_compressor_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_18_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_18_name`')
        self._data["Refrigeration Compressor 18 Name"] = value

    @property
    def refrigeration_compressor_19_name(self):
        """Get refrigeration_compressor_19_name

        Returns:
            str: the value of `refrigeration_compressor_19_name` or None if not set
        """
        return self._data["Refrigeration Compressor 19 Name"]

    @refrigeration_compressor_19_name.setter
    def refrigeration_compressor_19_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 19 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 19 Name`
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
                                 'for field `refrigeration_compressor_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_19_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_19_name`')
        self._data["Refrigeration Compressor 19 Name"] = value

    @property
    def refrigeration_compressor_20_name(self):
        """Get refrigeration_compressor_20_name

        Returns:
            str: the value of `refrigeration_compressor_20_name` or None if not set
        """
        return self._data["Refrigeration Compressor 20 Name"]

    @refrigeration_compressor_20_name.setter
    def refrigeration_compressor_20_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 20 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 20 Name`
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
                                 'for field `refrigeration_compressor_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_20_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_20_name`')
        self._data["Refrigeration Compressor 20 Name"] = value

    @property
    def refrigeration_compressor_21_name(self):
        """Get refrigeration_compressor_21_name

        Returns:
            str: the value of `refrigeration_compressor_21_name` or None if not set
        """
        return self._data["Refrigeration Compressor 21 Name"]

    @refrigeration_compressor_21_name.setter
    def refrigeration_compressor_21_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 21 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 21 Name`
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
                                 'for field `refrigeration_compressor_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_21_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_21_name`')
        self._data["Refrigeration Compressor 21 Name"] = value

    @property
    def refrigeration_compressor_22_name(self):
        """Get refrigeration_compressor_22_name

        Returns:
            str: the value of `refrigeration_compressor_22_name` or None if not set
        """
        return self._data["Refrigeration Compressor 22 Name"]

    @refrigeration_compressor_22_name.setter
    def refrigeration_compressor_22_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 22 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 22 Name`
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
                                 'for field `refrigeration_compressor_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_22_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_22_name`')
        self._data["Refrigeration Compressor 22 Name"] = value

    @property
    def refrigeration_compressor_23_name(self):
        """Get refrigeration_compressor_23_name

        Returns:
            str: the value of `refrigeration_compressor_23_name` or None if not set
        """
        return self._data["Refrigeration Compressor 23 Name"]

    @refrigeration_compressor_23_name.setter
    def refrigeration_compressor_23_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 23 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 23 Name`
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
                                 'for field `refrigeration_compressor_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_23_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_23_name`')
        self._data["Refrigeration Compressor 23 Name"] = value

    @property
    def refrigeration_compressor_24_name(self):
        """Get refrigeration_compressor_24_name

        Returns:
            str: the value of `refrigeration_compressor_24_name` or None if not set
        """
        return self._data["Refrigeration Compressor 24 Name"]

    @refrigeration_compressor_24_name.setter
    def refrigeration_compressor_24_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 24 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 24 Name`
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
                                 'for field `refrigeration_compressor_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_24_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_24_name`')
        self._data["Refrigeration Compressor 24 Name"] = value

    @property
    def refrigeration_compressor_25_name(self):
        """Get refrigeration_compressor_25_name

        Returns:
            str: the value of `refrigeration_compressor_25_name` or None if not set
        """
        return self._data["Refrigeration Compressor 25 Name"]

    @refrigeration_compressor_25_name.setter
    def refrigeration_compressor_25_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 25 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 25 Name`
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
                                 'for field `refrigeration_compressor_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_25_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_25_name`')
        self._data["Refrigeration Compressor 25 Name"] = value

    @property
    def refrigeration_compressor_26_name(self):
        """Get refrigeration_compressor_26_name

        Returns:
            str: the value of `refrigeration_compressor_26_name` or None if not set
        """
        return self._data["Refrigeration Compressor 26 Name"]

    @refrigeration_compressor_26_name.setter
    def refrigeration_compressor_26_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 26 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 26 Name`
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
                                 'for field `refrigeration_compressor_26_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_26_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_26_name`')
        self._data["Refrigeration Compressor 26 Name"] = value

    @property
    def refrigeration_compressor_27_name(self):
        """Get refrigeration_compressor_27_name

        Returns:
            str: the value of `refrigeration_compressor_27_name` or None if not set
        """
        return self._data["Refrigeration Compressor 27 Name"]

    @refrigeration_compressor_27_name.setter
    def refrigeration_compressor_27_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 27 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 27 Name`
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
                                 'for field `refrigeration_compressor_27_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_27_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_27_name`')
        self._data["Refrigeration Compressor 27 Name"] = value

    @property
    def refrigeration_compressor_28_name(self):
        """Get refrigeration_compressor_28_name

        Returns:
            str: the value of `refrigeration_compressor_28_name` or None if not set
        """
        return self._data["Refrigeration Compressor 28 Name"]

    @refrigeration_compressor_28_name.setter
    def refrigeration_compressor_28_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 28 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 28 Name`
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
                                 'for field `refrigeration_compressor_28_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_28_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_28_name`')
        self._data["Refrigeration Compressor 28 Name"] = value

    @property
    def refrigeration_compressor_29_name(self):
        """Get refrigeration_compressor_29_name

        Returns:
            str: the value of `refrigeration_compressor_29_name` or None if not set
        """
        return self._data["Refrigeration Compressor 29 Name"]

    @refrigeration_compressor_29_name.setter
    def refrigeration_compressor_29_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 29 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 29 Name`
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
                                 'for field `refrigeration_compressor_29_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_29_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_29_name`')
        self._data["Refrigeration Compressor 29 Name"] = value

    @property
    def refrigeration_compressor_30_name(self):
        """Get refrigeration_compressor_30_name

        Returns:
            str: the value of `refrigeration_compressor_30_name` or None if not set
        """
        return self._data["Refrigeration Compressor 30 Name"]

    @refrigeration_compressor_30_name.setter
    def refrigeration_compressor_30_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 30 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 30 Name`
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
                                 'for field `refrigeration_compressor_30_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_30_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_30_name`')
        self._data["Refrigeration Compressor 30 Name"] = value

    @property
    def refrigeration_compressor_31_name(self):
        """Get refrigeration_compressor_31_name

        Returns:
            str: the value of `refrigeration_compressor_31_name` or None if not set
        """
        return self._data["Refrigeration Compressor 31 Name"]

    @refrigeration_compressor_31_name.setter
    def refrigeration_compressor_31_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 31 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 31 Name`
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
                                 'for field `refrigeration_compressor_31_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_31_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_31_name`')
        self._data["Refrigeration Compressor 31 Name"] = value

    @property
    def refrigeration_compressor_32_name(self):
        """Get refrigeration_compressor_32_name

        Returns:
            str: the value of `refrigeration_compressor_32_name` or None if not set
        """
        return self._data["Refrigeration Compressor 32 Name"]

    @refrigeration_compressor_32_name.setter
    def refrigeration_compressor_32_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 32 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 32 Name`
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
                                 'for field `refrigeration_compressor_32_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_32_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_32_name`')
        self._data["Refrigeration Compressor 32 Name"] = value

    @property
    def refrigeration_compressor_33_name(self):
        """Get refrigeration_compressor_33_name

        Returns:
            str: the value of `refrigeration_compressor_33_name` or None if not set
        """
        return self._data["Refrigeration Compressor 33 Name"]

    @refrigeration_compressor_33_name.setter
    def refrigeration_compressor_33_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 33 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 33 Name`
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
                                 'for field `refrigeration_compressor_33_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_33_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_33_name`')
        self._data["Refrigeration Compressor 33 Name"] = value

    @property
    def refrigeration_compressor_34_name(self):
        """Get refrigeration_compressor_34_name

        Returns:
            str: the value of `refrigeration_compressor_34_name` or None if not set
        """
        return self._data["Refrigeration Compressor 34 Name"]

    @refrigeration_compressor_34_name.setter
    def refrigeration_compressor_34_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 34 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 34 Name`
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
                                 'for field `refrigeration_compressor_34_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_34_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_34_name`')
        self._data["Refrigeration Compressor 34 Name"] = value

    @property
    def refrigeration_compressor_35_name(self):
        """Get refrigeration_compressor_35_name

        Returns:
            str: the value of `refrigeration_compressor_35_name` or None if not set
        """
        return self._data["Refrigeration Compressor 35 Name"]

    @refrigeration_compressor_35_name.setter
    def refrigeration_compressor_35_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 35 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 35 Name`
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
                                 'for field `refrigeration_compressor_35_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_35_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_35_name`')
        self._data["Refrigeration Compressor 35 Name"] = value

    @property
    def refrigeration_compressor_36_name(self):
        """Get refrigeration_compressor_36_name

        Returns:
            str: the value of `refrigeration_compressor_36_name` or None if not set
        """
        return self._data["Refrigeration Compressor 36 Name"]

    @refrigeration_compressor_36_name.setter
    def refrigeration_compressor_36_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 36 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 36 Name`
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
                                 'for field `refrigeration_compressor_36_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_36_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_36_name`')
        self._data["Refrigeration Compressor 36 Name"] = value

    @property
    def refrigeration_compressor_37_name(self):
        """Get refrigeration_compressor_37_name

        Returns:
            str: the value of `refrigeration_compressor_37_name` or None if not set
        """
        return self._data["Refrigeration Compressor 37 Name"]

    @refrigeration_compressor_37_name.setter
    def refrigeration_compressor_37_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 37 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 37 Name`
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
                                 'for field `refrigeration_compressor_37_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_37_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_37_name`')
        self._data["Refrigeration Compressor 37 Name"] = value

    @property
    def refrigeration_compressor_38_name(self):
        """Get refrigeration_compressor_38_name

        Returns:
            str: the value of `refrigeration_compressor_38_name` or None if not set
        """
        return self._data["Refrigeration Compressor 38 Name"]

    @refrigeration_compressor_38_name.setter
    def refrigeration_compressor_38_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 38 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 38 Name`
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
                                 'for field `refrigeration_compressor_38_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_38_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_38_name`')
        self._data["Refrigeration Compressor 38 Name"] = value

    @property
    def refrigeration_compressor_39_name(self):
        """Get refrigeration_compressor_39_name

        Returns:
            str: the value of `refrigeration_compressor_39_name` or None if not set
        """
        return self._data["Refrigeration Compressor 39 Name"]

    @refrigeration_compressor_39_name.setter
    def refrigeration_compressor_39_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 39 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 39 Name`
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
                                 'for field `refrigeration_compressor_39_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_39_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_39_name`')
        self._data["Refrigeration Compressor 39 Name"] = value

    @property
    def refrigeration_compressor_40_name(self):
        """Get refrigeration_compressor_40_name

        Returns:
            str: the value of `refrigeration_compressor_40_name` or None if not set
        """
        return self._data["Refrigeration Compressor 40 Name"]

    @refrigeration_compressor_40_name.setter
    def refrigeration_compressor_40_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Compressor 40 Name`
        Enter the name of a Refrigeration:Compressor object.

        Args:
            value (str): value for IDD Field `Refrigeration Compressor 40 Name`
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
                                 'for field `refrigeration_compressor_40_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_compressor_40_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_compressor_40_name`')
        self._data["Refrigeration Compressor 40 Name"] = value

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

class RefrigerationSystem(object):
    """ Corresponds to IDD object `Refrigeration:System`
        Simulates the performance of a supermarket refrigeration system when used along with
        other objects to define the refrigeration load(s), the compressor(s), and the
        condenser.
    
    """
    internal_name = "Refrigeration:System"
    field_count = 17
    required_fields = ["Name", "Refrigeration Condenser Name", "Compressor or CompressorList Name", "Minimum Condensing Temperature", "Refrigeration System Working Fluid Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:System`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Refrigerated Case or Walkin or CaseAndWalkInList Name"] = None
        self._data["Refrigeration Transfer Load or TransferLoad List Name"] = None
        self._data["Refrigeration Condenser Name"] = None
        self._data["Compressor or CompressorList Name"] = None
        self._data["Minimum Condensing Temperature"] = None
        self._data["Refrigeration System Working Fluid Type"] = None
        self._data["Suction Temperature Control Type"] = None
        self._data["Mechanical Subcooler Name"] = None
        self._data["Liquid Suction Heat Exchanger Subcooler Name"] = None
        self._data["Sum UA Suction Piping"] = None
        self._data["Suction Piping Zone Name"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Number of Compressor Stages"] = None
        self._data["Intercooler Type"] = None
        self._data["Shell-and-Coil Intercooler Effectiveness"] = None
        self._data["High-Stage Compressor or CompressorList Name"] = None
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
            self.refrigerated_case_or_walkin_or_caseandwalkinlist_name = None
        else:
            self.refrigerated_case_or_walkin_or_caseandwalkinlist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_transfer_load_or_transferload_list_name = None
        else:
            self.refrigeration_transfer_load_or_transferload_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_condenser_name = None
        else:
            self.refrigeration_condenser_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compressor_or_compressorlist_name = None
        else:
            self.compressor_or_compressorlist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_condensing_temperature = None
        else:
            self.minimum_condensing_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_system_working_fluid_type = None
        else:
            self.refrigeration_system_working_fluid_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suction_temperature_control_type = None
        else:
            self.suction_temperature_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_subcooler_name = None
        else:
            self.mechanical_subcooler_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.liquid_suction_heat_exchanger_subcooler_name = None
        else:
            self.liquid_suction_heat_exchanger_subcooler_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sum_ua_suction_piping = None
        else:
            self.sum_ua_suction_piping = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suction_piping_zone_name = None
        else:
            self.suction_piping_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_compressor_stages = None
        else:
            self.number_of_compressor_stages = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.intercooler_type = None
        else:
            self.intercooler_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shellandcoil_intercooler_effectiveness = None
        else:
            self.shellandcoil_intercooler_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.highstage_compressor_or_compressorlist_name = None
        else:
            self.highstage_compressor_or_compressorlist_name = vals[i]
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
    def refrigerated_case_or_walkin_or_caseandwalkinlist_name(self):
        """Get refrigerated_case_or_walkin_or_caseandwalkinlist_name

        Returns:
            str: the value of `refrigerated_case_or_walkin_or_caseandwalkinlist_name` or None if not set
        """
        return self._data["Refrigerated Case or Walkin or CaseAndWalkInList Name"]

    @refrigerated_case_or_walkin_or_caseandwalkinlist_name.setter
    def refrigerated_case_or_walkin_or_caseandwalkinlist_name(self, value=None):
        """  Corresponds to IDD Field `Refrigerated Case or Walkin or CaseAndWalkInList Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.
        If there is more than one refrigerated case or walkin served by this system,
        enter the name of a Refrigeration:CaseAndWalkInList object.
        Only cases and walkins served directly by the system should be included in this list.
        Any cases served indirectly via a secondary chiller should NOT be included in this list

        Args:
            value (str): value for IDD Field `Refrigerated Case or Walkin or CaseAndWalkInList Name`
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
                                 'for field `refrigerated_case_or_walkin_or_caseandwalkinlist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigerated_case_or_walkin_or_caseandwalkinlist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigerated_case_or_walkin_or_caseandwalkinlist_name`')
        self._data["Refrigerated Case or Walkin or CaseAndWalkInList Name"] = value

    @property
    def refrigeration_transfer_load_or_transferload_list_name(self):
        """Get refrigeration_transfer_load_or_transferload_list_name

        Returns:
            str: the value of `refrigeration_transfer_load_or_transferload_list_name` or None if not set
        """
        return self._data["Refrigeration Transfer Load or TransferLoad List Name"]

    @refrigeration_transfer_load_or_transferload_list_name.setter
    def refrigeration_transfer_load_or_transferload_list_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Transfer Load or TransferLoad List Name`
        Enter the name of a Refrigeration:SecondarySystem object OR
        a Refrigeration:Condenser:Cascade object OR,
        a Refrigeration:TransferLoadList object.
        A transfer load is identified as one which moves the load from one system to another.
        So if you have more than one such load (including cascade condensers and secondary
        loops) served by the same system, use a TransferLoadList object.

        Args:
            value (str): value for IDD Field `Refrigeration Transfer Load or TransferLoad List Name`
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
                                 'for field `refrigeration_transfer_load_or_transferload_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_transfer_load_or_transferload_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_transfer_load_or_transferload_list_name`')
        self._data["Refrigeration Transfer Load or TransferLoad List Name"] = value

    @property
    def refrigeration_condenser_name(self):
        """Get refrigeration_condenser_name

        Returns:
            str: the value of `refrigeration_condenser_name` or None if not set
        """
        return self._data["Refrigeration Condenser Name"]

    @refrigeration_condenser_name.setter
    def refrigeration_condenser_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Condenser Name`

        Args:
            value (str): value for IDD Field `Refrigeration Condenser Name`
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
                                 'for field `refrigeration_condenser_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_condenser_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_condenser_name`')
        self._data["Refrigeration Condenser Name"] = value

    @property
    def compressor_or_compressorlist_name(self):
        """Get compressor_or_compressorlist_name

        Returns:
            str: the value of `compressor_or_compressorlist_name` or None if not set
        """
        return self._data["Compressor or CompressorList Name"]

    @compressor_or_compressorlist_name.setter
    def compressor_or_compressorlist_name(self, value=None):
        """  Corresponds to IDD Field `Compressor or CompressorList Name`

        Args:
            value (str): value for IDD Field `Compressor or CompressorList Name`
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
                                 'for field `compressor_or_compressorlist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compressor_or_compressorlist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `compressor_or_compressorlist_name`')
        self._data["Compressor or CompressorList Name"] = value

    @property
    def minimum_condensing_temperature(self):
        """Get minimum_condensing_temperature

        Returns:
            float: the value of `minimum_condensing_temperature` or None if not set
        """
        return self._data["Minimum Condensing Temperature"]

    @minimum_condensing_temperature.setter
    def minimum_condensing_temperature(self, value=None):
        """  Corresponds to IDD Field `Minimum Condensing Temperature`
        related to the proper operation of the thermal expansion
        valves and compressors

        Args:
            value (float): value for IDD Field `Minimum Condensing Temperature`
                Units: C
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
                                 'for field `minimum_condensing_temperature`'.format(value))
        self._data["Minimum Condensing Temperature"] = value

    @property
    def refrigeration_system_working_fluid_type(self):
        """Get refrigeration_system_working_fluid_type

        Returns:
            str: the value of `refrigeration_system_working_fluid_type` or None if not set
        """
        return self._data["Refrigeration System Working Fluid Type"]

    @refrigeration_system_working_fluid_type.setter
    def refrigeration_system_working_fluid_type(self, value=None):
        """  Corresponds to IDD Field `Refrigeration System Working Fluid Type`
        Fluid property data for the refrigerant must be entered.
        The fluid property data, including the objects:
        FluidProperties:Name, FluidProperties:Temperatures,
        FluidProperties:Saturated and FluidProperties:Superheated
        can be copied from the FluidPropertiesRefData.idf dataset

        Args:
            value (str): value for IDD Field `Refrigeration System Working Fluid Type`
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
                                 'for field `refrigeration_system_working_fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_system_working_fluid_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_system_working_fluid_type`')
        self._data["Refrigeration System Working Fluid Type"] = value

    @property
    def suction_temperature_control_type(self):
        """Get suction_temperature_control_type

        Returns:
            str: the value of `suction_temperature_control_type` or None if not set
        """
        return self._data["Suction Temperature Control Type"]

    @suction_temperature_control_type.setter
    def suction_temperature_control_type(self, value="ConstantSuctionTemperature"):
        """  Corresponds to IDD Field `Suction Temperature Control Type`

        Args:
            value (str): value for IDD Field `Suction Temperature Control Type`
                Accepted values are:
                      - FloatSuctionTemperature
                      - ConstantSuctionTemperature
                Default value: ConstantSuctionTemperature
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
                                 'for field `suction_temperature_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suction_temperature_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suction_temperature_control_type`')
            vals = {}
            vals["floatsuctiontemperature"] = "FloatSuctionTemperature"
            vals["constantsuctiontemperature"] = "ConstantSuctionTemperature"
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
                                     'field `suction_temperature_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Suction Temperature Control Type"] = value

    @property
    def mechanical_subcooler_name(self):
        """Get mechanical_subcooler_name

        Returns:
            str: the value of `mechanical_subcooler_name` or None if not set
        """
        return self._data["Mechanical Subcooler Name"]

    @mechanical_subcooler_name.setter
    def mechanical_subcooler_name(self, value=None):
        """  Corresponds to IDD Field `Mechanical Subcooler Name`
        Optional Field
        Recipient of refrigeration capacity, that is receives cool liquid
        from another refrigeraiton system to help meet aggregate case loads

        Args:
            value (str): value for IDD Field `Mechanical Subcooler Name`
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
                                 'for field `mechanical_subcooler_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_subcooler_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `mechanical_subcooler_name`')
        self._data["Mechanical Subcooler Name"] = value

    @property
    def liquid_suction_heat_exchanger_subcooler_name(self):
        """Get liquid_suction_heat_exchanger_subcooler_name

        Returns:
            str: the value of `liquid_suction_heat_exchanger_subcooler_name` or None if not set
        """
        return self._data["Liquid Suction Heat Exchanger Subcooler Name"]

    @liquid_suction_heat_exchanger_subcooler_name.setter
    def liquid_suction_heat_exchanger_subcooler_name(self, value=None):
        """  Corresponds to IDD Field `Liquid Suction Heat Exchanger Subcooler Name`
        Optional Field
        Liquid Suction Heat Exchanger Name, or leave blank

        Args:
            value (str): value for IDD Field `Liquid Suction Heat Exchanger Subcooler Name`
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
                                 'for field `liquid_suction_heat_exchanger_subcooler_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `liquid_suction_heat_exchanger_subcooler_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `liquid_suction_heat_exchanger_subcooler_name`')
        self._data["Liquid Suction Heat Exchanger Subcooler Name"] = value

    @property
    def sum_ua_suction_piping(self):
        """Get sum_ua_suction_piping

        Returns:
            float: the value of `sum_ua_suction_piping` or None if not set
        """
        return self._data["Sum UA Suction Piping"]

    @sum_ua_suction_piping.setter
    def sum_ua_suction_piping(self, value=0.0):
        """  Corresponds to IDD Field `Sum UA Suction Piping`
        Use only if you want to include suction piping heat gain in refrigeration load

        Args:
            value (float): value for IDD Field `Sum UA Suction Piping`
                Units: W/K
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
                                 'for field `sum_ua_suction_piping`'.format(value))
        self._data["Sum UA Suction Piping"] = value

    @property
    def suction_piping_zone_name(self):
        """Get suction_piping_zone_name

        Returns:
            str: the value of `suction_piping_zone_name` or None if not set
        """
        return self._data["Suction Piping Zone Name"]

    @suction_piping_zone_name.setter
    def suction_piping_zone_name(self, value=None):
        """  Corresponds to IDD Field `Suction Piping Zone Name`
        This will be used to determine the temperature used for distribution piping heat gain
        and the pipe heat gains  as cooling credit for the zone.
        Required only if Sum UA Distribution Piping >0.0

        Args:
            value (str): value for IDD Field `Suction Piping Zone Name`
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
                                 'for field `suction_piping_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suction_piping_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suction_piping_zone_name`')
        self._data["Suction Piping Zone Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    @property
    def number_of_compressor_stages(self):
        """Get number_of_compressor_stages

        Returns:
            str: the value of `number_of_compressor_stages` or None if not set
        """
        return self._data["Number of Compressor Stages"]

    @number_of_compressor_stages.setter
    def number_of_compressor_stages(self, value="1"):
        """  Corresponds to IDD Field `Number of Compressor Stages`

        Args:
            value (str): value for IDD Field `Number of Compressor Stages`
                Accepted values are:
                      - 1
                      - 2
                Default value: 1
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
                                 'for field `number_of_compressor_stages`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `number_of_compressor_stages`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `number_of_compressor_stages`')
            vals = {}
            vals["1"] = "1"
            vals["2"] = "2"
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
                                     'field `number_of_compressor_stages`'.format(value))
            value = vals[value_lower]
        self._data["Number of Compressor Stages"] = value

    @property
    def intercooler_type(self):
        """Get intercooler_type

        Returns:
            str: the value of `intercooler_type` or None if not set
        """
        return self._data["Intercooler Type"]

    @intercooler_type.setter
    def intercooler_type(self, value="None"):
        """  Corresponds to IDD Field `Intercooler Type`

        Args:
            value (str): value for IDD Field `Intercooler Type`
                Accepted values are:
                      - None
                      - Flash Intercooler
                      - Shell-and-Coil Intercooler
                Default value: None
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
                                 'for field `intercooler_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `intercooler_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `intercooler_type`')
            vals = {}
            vals["none"] = "None"
            vals["flash intercooler"] = "Flash Intercooler"
            vals["shell-and-coil intercooler"] = "Shell-and-Coil Intercooler"
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
                                     'field `intercooler_type`'.format(value))
            value = vals[value_lower]
        self._data["Intercooler Type"] = value

    @property
    def shellandcoil_intercooler_effectiveness(self):
        """Get shellandcoil_intercooler_effectiveness

        Returns:
            float: the value of `shellandcoil_intercooler_effectiveness` or None if not set
        """
        return self._data["Shell-and-Coil Intercooler Effectiveness"]

    @shellandcoil_intercooler_effectiveness.setter
    def shellandcoil_intercooler_effectiveness(self, value=0.8):
        """  Corresponds to IDD Field `Shell-and-Coil Intercooler Effectiveness`

        Args:
            value (float): value for IDD Field `Shell-and-Coil Intercooler Effectiveness`
                Default value: 0.8
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
                                 'for field `shellandcoil_intercooler_effectiveness`'.format(value))
        self._data["Shell-and-Coil Intercooler Effectiveness"] = value

    @property
    def highstage_compressor_or_compressorlist_name(self):
        """Get highstage_compressor_or_compressorlist_name

        Returns:
            str: the value of `highstage_compressor_or_compressorlist_name` or None if not set
        """
        return self._data["High-Stage Compressor or CompressorList Name"]

    @highstage_compressor_or_compressorlist_name.setter
    def highstage_compressor_or_compressorlist_name(self, value=None):
        """  Corresponds to IDD Field `High-Stage Compressor or CompressorList Name`

        Args:
            value (str): value for IDD Field `High-Stage Compressor or CompressorList Name`
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
                                 'for field `highstage_compressor_or_compressorlist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `highstage_compressor_or_compressorlist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `highstage_compressor_or_compressorlist_name`')
        self._data["High-Stage Compressor or CompressorList Name"] = value

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

class RefrigerationTranscriticalSystem(object):
    """ Corresponds to IDD object `Refrigeration:TranscriticalSystem`
        Detailed transcritical carbon dioxide (CO2) booster refrigeration systems used in
        supermarkets.  The object allows for modeling either a single stage system with
        medium-temperature loads or a two stage system with both medium- and low-temperature
        loads.
    
    """
    internal_name = "Refrigeration:TranscriticalSystem"
    field_count = 15
    required_fields = ["Name", "System Type", "Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name", "Refrigeration Gas Cooler Name", "High Pressure Compressor or CompressorList Name", "Refrigeration System Working Fluid Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:TranscriticalSystem`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["System Type"] = None
        self._data["Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"] = None
        self._data["Low Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"] = None
        self._data["Refrigeration Gas Cooler Name"] = None
        self._data["High Pressure Compressor or CompressorList Name"] = None
        self._data["Low Pressure Compressor or CompressorList Name"] = None
        self._data["Receiver Pressure"] = None
        self._data["Subcooler Effectiveness"] = None
        self._data["Refrigeration System Working Fluid Type"] = None
        self._data["Sum UA Suction Piping for Medium Temperature Loads"] = None
        self._data["Medium Temperature Suction Piping Zone Name"] = None
        self._data["Sum UA Suction Piping for Low Temperature Loads"] = None
        self._data["Low Temperature Suction Piping Zone Name"] = None
        self._data["End-Use Subcategory"] = None
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
            self.system_type = None
        else:
            self.system_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name = None
        else:
            self.medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name = None
        else:
            self.low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_gas_cooler_name = None
        else:
            self.refrigeration_gas_cooler_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.high_pressure_compressor_or_compressorlist_name = None
        else:
            self.high_pressure_compressor_or_compressorlist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_pressure_compressor_or_compressorlist_name = None
        else:
            self.low_pressure_compressor_or_compressorlist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.receiver_pressure = None
        else:
            self.receiver_pressure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.subcooler_effectiveness = None
        else:
            self.subcooler_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigeration_system_working_fluid_type = None
        else:
            self.refrigeration_system_working_fluid_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sum_ua_suction_piping_for_medium_temperature_loads = None
        else:
            self.sum_ua_suction_piping_for_medium_temperature_loads = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.medium_temperature_suction_piping_zone_name = None
        else:
            self.medium_temperature_suction_piping_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sum_ua_suction_piping_for_low_temperature_loads = None
        else:
            self.sum_ua_suction_piping_for_low_temperature_loads = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.low_temperature_suction_piping_zone_name = None
        else:
            self.low_temperature_suction_piping_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
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
    def system_type(self):
        """Get system_type

        Returns:
            str: the value of `system_type` or None if not set
        """
        return self._data["System Type"]

    @system_type.setter
    def system_type(self, value=None):
        """  Corresponds to IDD Field `System Type`

        Args:
            value (str): value for IDD Field `System Type`
                Accepted values are:
                      - SingleStage
                      - TwoStage
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
                                 'for field `system_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `system_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `system_type`')
            vals = {}
            vals["singlestage"] = "SingleStage"
            vals["twostage"] = "TwoStage"
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
                                     'field `system_type`'.format(value))
            value = vals[value_lower]
        self._data["System Type"] = value

    @property
    def medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name(self):
        """Get medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name

        Returns:
            str: the value of `medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name` or None if not set
        """
        return self._data["Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"]

    @medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name.setter
    def medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name(self, value=None):
        """  Corresponds to IDD Field `Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.
        If there is more than one refrigerated case or walkin served by this system,
        enter the name of a Refrigeration:CaseAndWalkInList object.
        Only medium temperature cases and walkins served directly by the system should
        be included in this list.

        Args:
            value (str): value for IDD Field `Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name`
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
                                 'for field `medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name`')
        self._data["Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"] = value

    @property
    def low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name(self):
        """Get low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name

        Returns:
            str: the value of `low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name` or None if not set
        """
        return self._data["Low Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"]

    @low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name.setter
    def low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name(self, value=None):
        """  Corresponds to IDD Field `Low Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.
        If there is more than one refrigerated case or walkin served by this system,
        enter the name of a Refrigeration:CaseAndWalkInList object.
        Only low temperature cases and walkins served directly by the system should be
        included in this list.

        Args:
            value (str): value for IDD Field `Low Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name`
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
                                 'for field `low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name`')
        self._data["Low Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"] = value

    @property
    def refrigeration_gas_cooler_name(self):
        """Get refrigeration_gas_cooler_name

        Returns:
            str: the value of `refrigeration_gas_cooler_name` or None if not set
        """
        return self._data["Refrigeration Gas Cooler Name"]

    @refrigeration_gas_cooler_name.setter
    def refrigeration_gas_cooler_name(self, value=None):
        """  Corresponds to IDD Field `Refrigeration Gas Cooler Name`

        Args:
            value (str): value for IDD Field `Refrigeration Gas Cooler Name`
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
                                 'for field `refrigeration_gas_cooler_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_gas_cooler_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_gas_cooler_name`')
        self._data["Refrigeration Gas Cooler Name"] = value

    @property
    def high_pressure_compressor_or_compressorlist_name(self):
        """Get high_pressure_compressor_or_compressorlist_name

        Returns:
            str: the value of `high_pressure_compressor_or_compressorlist_name` or None if not set
        """
        return self._data["High Pressure Compressor or CompressorList Name"]

    @high_pressure_compressor_or_compressorlist_name.setter
    def high_pressure_compressor_or_compressorlist_name(self, value=None):
        """  Corresponds to IDD Field `High Pressure Compressor or CompressorList Name`

        Args:
            value (str): value for IDD Field `High Pressure Compressor or CompressorList Name`
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
                                 'for field `high_pressure_compressor_or_compressorlist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `high_pressure_compressor_or_compressorlist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `high_pressure_compressor_or_compressorlist_name`')
        self._data["High Pressure Compressor or CompressorList Name"] = value

    @property
    def low_pressure_compressor_or_compressorlist_name(self):
        """Get low_pressure_compressor_or_compressorlist_name

        Returns:
            str: the value of `low_pressure_compressor_or_compressorlist_name` or None if not set
        """
        return self._data["Low Pressure Compressor or CompressorList Name"]

    @low_pressure_compressor_or_compressorlist_name.setter
    def low_pressure_compressor_or_compressorlist_name(self, value=None):
        """  Corresponds to IDD Field `Low Pressure Compressor or CompressorList Name`

        Args:
            value (str): value for IDD Field `Low Pressure Compressor or CompressorList Name`
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
                                 'for field `low_pressure_compressor_or_compressorlist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `low_pressure_compressor_or_compressorlist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `low_pressure_compressor_or_compressorlist_name`')
        self._data["Low Pressure Compressor or CompressorList Name"] = value

    @property
    def receiver_pressure(self):
        """Get receiver_pressure

        Returns:
            float: the value of `receiver_pressure` or None if not set
        """
        return self._data["Receiver Pressure"]

    @receiver_pressure.setter
    def receiver_pressure(self, value=4000000.0):
        """  Corresponds to IDD Field `Receiver Pressure`

        Args:
            value (float): value for IDD Field `Receiver Pressure`
                Units: Pa
                Default value: 4000000.0
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
                                 'for field `receiver_pressure`'.format(value))
        self._data["Receiver Pressure"] = value

    @property
    def subcooler_effectiveness(self):
        """Get subcooler_effectiveness

        Returns:
            float: the value of `subcooler_effectiveness` or None if not set
        """
        return self._data["Subcooler Effectiveness"]

    @subcooler_effectiveness.setter
    def subcooler_effectiveness(self, value=0.4):
        """  Corresponds to IDD Field `Subcooler Effectiveness`

        Args:
            value (float): value for IDD Field `Subcooler Effectiveness`
                Default value: 0.4
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
                                 'for field `subcooler_effectiveness`'.format(value))
        self._data["Subcooler Effectiveness"] = value

    @property
    def refrigeration_system_working_fluid_type(self):
        """Get refrigeration_system_working_fluid_type

        Returns:
            str: the value of `refrigeration_system_working_fluid_type` or None if not set
        """
        return self._data["Refrigeration System Working Fluid Type"]

    @refrigeration_system_working_fluid_type.setter
    def refrigeration_system_working_fluid_type(self, value=None):
        """  Corresponds to IDD Field `Refrigeration System Working Fluid Type`
        Fluid property data for the refrigerant must be entered.
        The fluid property data, including the objects:
        FluidProperties:Name, FluidProperties:Temperatures,
        FluidProperties:Saturated and FluidProperties:Superheated
        can be copied from the FluidPropertiesRefData.idf dataset

        Args:
            value (str): value for IDD Field `Refrigeration System Working Fluid Type`
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
                                 'for field `refrigeration_system_working_fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigeration_system_working_fluid_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigeration_system_working_fluid_type`')
        self._data["Refrigeration System Working Fluid Type"] = value

    @property
    def sum_ua_suction_piping_for_medium_temperature_loads(self):
        """Get sum_ua_suction_piping_for_medium_temperature_loads

        Returns:
            float: the value of `sum_ua_suction_piping_for_medium_temperature_loads` or None if not set
        """
        return self._data["Sum UA Suction Piping for Medium Temperature Loads"]

    @sum_ua_suction_piping_for_medium_temperature_loads.setter
    def sum_ua_suction_piping_for_medium_temperature_loads(self, value=0.0):
        """  Corresponds to IDD Field `Sum UA Suction Piping for Medium Temperature Loads`
        Use only if you want to include suction piping heat gain in refrigeration load

        Args:
            value (float): value for IDD Field `Sum UA Suction Piping for Medium Temperature Loads`
                Units: W/K
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
                                 'for field `sum_ua_suction_piping_for_medium_temperature_loads`'.format(value))
        self._data["Sum UA Suction Piping for Medium Temperature Loads"] = value

    @property
    def medium_temperature_suction_piping_zone_name(self):
        """Get medium_temperature_suction_piping_zone_name

        Returns:
            str: the value of `medium_temperature_suction_piping_zone_name` or None if not set
        """
        return self._data["Medium Temperature Suction Piping Zone Name"]

    @medium_temperature_suction_piping_zone_name.setter
    def medium_temperature_suction_piping_zone_name(self, value=None):
        """  Corresponds to IDD Field `Medium Temperature Suction Piping Zone Name`
        This will be used to determine the temperature used for distribution piping heat
        gain and the pipe heat gains as cooling credit for the zone.
        Required only if Sum UA Distribution Piping for Medium Temperature Loads > 0.0

        Args:
            value (str): value for IDD Field `Medium Temperature Suction Piping Zone Name`
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
                                 'for field `medium_temperature_suction_piping_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `medium_temperature_suction_piping_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `medium_temperature_suction_piping_zone_name`')
        self._data["Medium Temperature Suction Piping Zone Name"] = value

    @property
    def sum_ua_suction_piping_for_low_temperature_loads(self):
        """Get sum_ua_suction_piping_for_low_temperature_loads

        Returns:
            float: the value of `sum_ua_suction_piping_for_low_temperature_loads` or None if not set
        """
        return self._data["Sum UA Suction Piping for Low Temperature Loads"]

    @sum_ua_suction_piping_for_low_temperature_loads.setter
    def sum_ua_suction_piping_for_low_temperature_loads(self, value=0.0):
        """  Corresponds to IDD Field `Sum UA Suction Piping for Low Temperature Loads`
        Use only if you want to include suction piping heat gain in refrigeration load

        Args:
            value (float): value for IDD Field `Sum UA Suction Piping for Low Temperature Loads`
                Units: W/K
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
                                 'for field `sum_ua_suction_piping_for_low_temperature_loads`'.format(value))
        self._data["Sum UA Suction Piping for Low Temperature Loads"] = value

    @property
    def low_temperature_suction_piping_zone_name(self):
        """Get low_temperature_suction_piping_zone_name

        Returns:
            str: the value of `low_temperature_suction_piping_zone_name` or None if not set
        """
        return self._data["Low Temperature Suction Piping Zone Name"]

    @low_temperature_suction_piping_zone_name.setter
    def low_temperature_suction_piping_zone_name(self, value=None):
        """  Corresponds to IDD Field `Low Temperature Suction Piping Zone Name`
        This will be used to determine the temperature used for distribution piping heat
        gain and the pipe heat gains as cooling credit for the zone.
        Required only if Sum UA Distribution Piping for Low Temperature Loads > 0.0

        Args:
            value (str): value for IDD Field `Low Temperature Suction Piping Zone Name`
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
                                 'for field `low_temperature_suction_piping_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `low_temperature_suction_piping_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `low_temperature_suction_piping_zone_name`')
        self._data["Low Temperature Suction Piping Zone Name"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

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

class RefrigerationSecondarySystem(object):
    """ Corresponds to IDD object `Refrigeration:SecondarySystem`
        Works in conjunction with refrigerated cases and walkins to simulate the performance
        of a secondary loop supermarket refrigeration system. Heat from the refrigeration
        loads served by the secondary loop is absorbed by a primary refrigeration system
        (Refrigeration:System). The SecondarySystem object simulates a heat exchanger that
        is an evaporator, or refrigeration load, on the primary refrigeration system.
    
    """
    internal_name = "Refrigeration:SecondarySystem"
    field_count = 23
    required_fields = ["Name", "Refrigerated Case or Walkin or CaseAndWalkInList Name", "Circulating Fluid Type", "Circulating Fluid Name", "Evaporator Evaporating Temperature", "Evaporator Approach Temperature Difference"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:SecondarySystem`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Refrigerated Case or Walkin or CaseAndWalkInList Name"] = None
        self._data["Circulating Fluid Type"] = None
        self._data["Circulating Fluid Name"] = None
        self._data["Evaporator Capacity"] = None
        self._data["Evaporator Flow Rate for Secondary Fluid"] = None
        self._data["Evaporator Evaporating Temperature"] = None
        self._data["Evaporator Approach Temperature Difference"] = None
        self._data["Evaporator Range Temperature Difference"] = None
        self._data["Number of Pumps in Loop"] = None
        self._data["Total Pump Flow Rate"] = None
        self._data["Total Pump Power"] = None
        self._data["Total Pump Head"] = None
        self._data["PhaseChange Circulating Rate"] = None
        self._data["Pump Drive Type"] = None
        self._data["Variable Speed Pump Cubic Curve Name"] = None
        self._data["Pump Motor Heat to Fluid"] = None
        self._data["Sum UA Distribution Piping"] = None
        self._data["Distribution Piping Zone Name"] = None
        self._data["Sum UA Receiver/Separator Shell"] = None
        self._data["Receiver/Separator Zone Name"] = None
        self._data["Evaporator Refrigerant Inventory"] = None
        self._data["End-Use Subcategory"] = None
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
            self.refrigerated_case_or_walkin_or_caseandwalkinlist_name = None
        else:
            self.refrigerated_case_or_walkin_or_caseandwalkinlist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.circulating_fluid_type = None
        else:
            self.circulating_fluid_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.circulating_fluid_name = None
        else:
            self.circulating_fluid_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporator_capacity = None
        else:
            self.evaporator_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporator_flow_rate_for_secondary_fluid = None
        else:
            self.evaporator_flow_rate_for_secondary_fluid = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporator_evaporating_temperature = None
        else:
            self.evaporator_evaporating_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporator_approach_temperature_difference = None
        else:
            self.evaporator_approach_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporator_range_temperature_difference = None
        else:
            self.evaporator_range_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_pumps_in_loop = None
        else:
            self.number_of_pumps_in_loop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_pump_flow_rate = None
        else:
            self.total_pump_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_pump_power = None
        else:
            self.total_pump_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_pump_head = None
        else:
            self.total_pump_head = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.phasechange_circulating_rate = None
        else:
            self.phasechange_circulating_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_drive_type = None
        else:
            self.pump_drive_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.variable_speed_pump_cubic_curve_name = None
        else:
            self.variable_speed_pump_cubic_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_motor_heat_to_fluid = None
        else:
            self.pump_motor_heat_to_fluid = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sum_ua_distribution_piping = None
        else:
            self.sum_ua_distribution_piping = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.distribution_piping_zone_name = None
        else:
            self.distribution_piping_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sum_ua_receiver_or_separator_shell = None
        else:
            self.sum_ua_receiver_or_separator_shell = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.receiver_or_separator_zone_name = None
        else:
            self.receiver_or_separator_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporator_refrigerant_inventory = None
        else:
            self.evaporator_refrigerant_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
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
    def refrigerated_case_or_walkin_or_caseandwalkinlist_name(self):
        """Get refrigerated_case_or_walkin_or_caseandwalkinlist_name

        Returns:
            str: the value of `refrigerated_case_or_walkin_or_caseandwalkinlist_name` or None if not set
        """
        return self._data["Refrigerated Case or Walkin or CaseAndWalkInList Name"]

    @refrigerated_case_or_walkin_or_caseandwalkinlist_name.setter
    def refrigerated_case_or_walkin_or_caseandwalkinlist_name(self, value=None):
        """  Corresponds to IDD Field `Refrigerated Case or Walkin or CaseAndWalkInList Name`
        Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.
        If there is more than one refrigerated case or walkin served by this secondary system,
        enter the name of a Refrigeration:CaseAndWalkInList object.

        Args:
            value (str): value for IDD Field `Refrigerated Case or Walkin or CaseAndWalkInList Name`
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
                                 'for field `refrigerated_case_or_walkin_or_caseandwalkinlist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `refrigerated_case_or_walkin_or_caseandwalkinlist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `refrigerated_case_or_walkin_or_caseandwalkinlist_name`')
        self._data["Refrigerated Case or Walkin or CaseAndWalkInList Name"] = value

    @property
    def circulating_fluid_type(self):
        """Get circulating_fluid_type

        Returns:
            str: the value of `circulating_fluid_type` or None if not set
        """
        return self._data["Circulating Fluid Type"]

    @circulating_fluid_type.setter
    def circulating_fluid_type(self, value=None):
        """  Corresponds to IDD Field `Circulating Fluid Type`
        If "FluidAlwaysLiquid" is selected, the fluid properties
        must be input using the objects: FluidProperties:Name,
        FluidProperties:GlycolConcentration, and, if user defined fluid type,
        FluidProperties:Temperatures and FluidProperties:Concentration.
        Many sets of fluid properties can be found in GlycolPropertiesRefData.idf.
        If "FluidPhaseChange" is selected, the refrigerant properties
        must be input using the objects: (if user defined fluid type): FluidProperties:Name,
        FluidProperties:Temperatures, FluidProperties:Saturated, and
        FluidProperties:Superheated.
        Many sets of refrigerant data can be found in FluidPropertiesRefData.idf.

        Args:
            value (str): value for IDD Field `Circulating Fluid Type`
                Accepted values are:
                      - FluidAlwaysLiquid
                      - FluidPhaseChange
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
                                 'for field `circulating_fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `circulating_fluid_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `circulating_fluid_type`')
            vals = {}
            vals["fluidalwaysliquid"] = "FluidAlwaysLiquid"
            vals["fluidphasechange"] = "FluidPhaseChange"
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
                                     'field `circulating_fluid_type`'.format(value))
            value = vals[value_lower]
        self._data["Circulating Fluid Type"] = value

    @property
    def circulating_fluid_name(self):
        """Get circulating_fluid_name

        Returns:
            str: the value of `circulating_fluid_name` or None if not set
        """
        return self._data["Circulating Fluid Name"]

    @circulating_fluid_name.setter
    def circulating_fluid_name(self, value=None):
        """  Corresponds to IDD Field `Circulating Fluid Name`
        This must correspond to a name in the FluidProperties:Name object.

        Args:
            value (str): value for IDD Field `Circulating Fluid Name`
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
                                 'for field `circulating_fluid_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `circulating_fluid_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `circulating_fluid_name`')
        self._data["Circulating Fluid Name"] = value

    @property
    def evaporator_capacity(self):
        """Get evaporator_capacity

        Returns:
            float: the value of `evaporator_capacity` or None if not set
        """
        return self._data["Evaporator Capacity"]

    @evaporator_capacity.setter
    def evaporator_capacity(self, value=None):
        """  Corresponds to IDD Field `Evaporator Capacity`
        For "FluidAlwaysLiquid", at least one of the two, Evaporator Capacity OR
        Evaporator Flow Rate for Secondary Fluid, is required.
        For "FluidPhaseChange", the default capacity is the sum of the rated capacities of the
        Cases and Walk-ins served by the secondary loop.

        Args:
            value (float): value for IDD Field `Evaporator Capacity`
                Units: W
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
                                 'for field `evaporator_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evaporator_capacity`')
        self._data["Evaporator Capacity"] = value

    @property
    def evaporator_flow_rate_for_secondary_fluid(self):
        """Get evaporator_flow_rate_for_secondary_fluid

        Returns:
            float: the value of `evaporator_flow_rate_for_secondary_fluid` or None if not set
        """
        return self._data["Evaporator Flow Rate for Secondary Fluid"]

    @evaporator_flow_rate_for_secondary_fluid.setter
    def evaporator_flow_rate_for_secondary_fluid(self, value=None):
        """  Corresponds to IDD Field `Evaporator Flow Rate for Secondary Fluid`
        For "FluidAlwaysLiquid", at least one of the two, Evaporator Capacity OR
        Evaporator Flow Rate for Secondary Fluid, is required.
        For "FluidPhaseChange" loops, this input is not used. (see PhaseChange Circulating
        Rate)

        Args:
            value (float): value for IDD Field `Evaporator Flow Rate for Secondary Fluid`
                Units: M3/s
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
                                 'for field `evaporator_flow_rate_for_secondary_fluid`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evaporator_flow_rate_for_secondary_fluid`')
        self._data["Evaporator Flow Rate for Secondary Fluid"] = value

    @property
    def evaporator_evaporating_temperature(self):
        """Get evaporator_evaporating_temperature

        Returns:
            float: the value of `evaporator_evaporating_temperature` or None if not set
        """
        return self._data["Evaporator Evaporating Temperature"]

    @evaporator_evaporating_temperature.setter
    def evaporator_evaporating_temperature(self, value=None):
        """  Corresponds to IDD Field `Evaporator Evaporating Temperature`
        This is the evaporating temperature in the heat exchanger
        used to chill or condense the secondary loop circulating fluid.
        It is NOT the temperature in any cases or walk-ins served by the
        secondary loop.

        Args:
            value (float): value for IDD Field `Evaporator Evaporating Temperature`
                Units: C
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
                                 'for field `evaporator_evaporating_temperature`'.format(value))
        self._data["Evaporator Evaporating Temperature"] = value

    @property
    def evaporator_approach_temperature_difference(self):
        """Get evaporator_approach_temperature_difference

        Returns:
            float: the value of `evaporator_approach_temperature_difference` or None if not set
        """
        return self._data["Evaporator Approach Temperature Difference"]

    @evaporator_approach_temperature_difference.setter
    def evaporator_approach_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `Evaporator Approach Temperature Difference`
        For "FluidAlwaysLiquid", this is the rated difference between the temperature of the
        circulating fluid leaving the heat exchanger
        and the heat exchanger's rated evaporating temperature.
        For "FluidPhaseChange", this is the difference between the temperature of the
        evaporating and condensing temperatures in the heat exchanger.

        Args:
            value (float): value for IDD Field `Evaporator Approach Temperature Difference`
                Units: DeltaC
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
                                 'for field `evaporator_approach_temperature_difference`'.format(value))
        self._data["Evaporator Approach Temperature Difference"] = value

    @property
    def evaporator_range_temperature_difference(self):
        """Get evaporator_range_temperature_difference

        Returns:
            float: the value of `evaporator_range_temperature_difference` or None if not set
        """
        return self._data["Evaporator Range Temperature Difference"]

    @evaporator_range_temperature_difference.setter
    def evaporator_range_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `Evaporator Range Temperature Difference`
        For "FluidAlwaysLiquid", this is the rated difference between the temperature of the
        circulating fluid entering the heat exchanger and the temperature of the
        circulating fluid leaving the heat exchanger, and is Required.
        For "FluidPhaseChange", this input is not used.

        Args:
            value (float): value for IDD Field `Evaporator Range Temperature Difference`
                Units: DeltaC
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
                                 'for field `evaporator_range_temperature_difference`'.format(value))
        self._data["Evaporator Range Temperature Difference"] = value

    @property
    def number_of_pumps_in_loop(self):
        """Get number_of_pumps_in_loop

        Returns:
            int: the value of `number_of_pumps_in_loop` or None if not set
        """
        return self._data["Number of Pumps in Loop"]

    @number_of_pumps_in_loop.setter
    def number_of_pumps_in_loop(self, value=1):
        """  Corresponds to IDD Field `Number of Pumps in Loop`

        Args:
            value (int): value for IDD Field `Number of Pumps in Loop`
                Default value: 1
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
                                 'for field `number_of_pumps_in_loop`'.format(value))
        self._data["Number of Pumps in Loop"] = value

    @property
    def total_pump_flow_rate(self):
        """Get total_pump_flow_rate

        Returns:
            float: the value of `total_pump_flow_rate` or None if not set
        """
        return self._data["Total Pump Flow Rate"]

    @total_pump_flow_rate.setter
    def total_pump_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Total Pump Flow Rate`
        For "FluidAlwaysLiquid",if not input, Evaporator Flow Rate for Secondary Fluid
        will be used.
        For "FluidPhaseChange", if not input, this will be calculated using the
        PhaseChange Circulating Rate.

        Args:
            value (float): value for IDD Field `Total Pump Flow Rate`
                Units: M3/s
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
                                 'for field `total_pump_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `total_pump_flow_rate`')
        self._data["Total Pump Flow Rate"] = value

    @property
    def total_pump_power(self):
        """Get total_pump_power

        Returns:
            float: the value of `total_pump_power` or None if not set
        """
        return self._data["Total Pump Power"]

    @total_pump_power.setter
    def total_pump_power(self, value=None):
        """  Corresponds to IDD Field `Total Pump Power`
        Either the Total Pump Power or the Total Pump Head is required.

        Args:
            value (float): value for IDD Field `Total Pump Power`
                Units: W
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
                                 'for field `total_pump_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `total_pump_power`')
        self._data["Total Pump Power"] = value

    @property
    def total_pump_head(self):
        """Get total_pump_head

        Returns:
            float: the value of `total_pump_head` or None if not set
        """
        return self._data["Total Pump Head"]

    @total_pump_head.setter
    def total_pump_head(self, value=None):
        """  Corresponds to IDD Field `Total Pump Head`
        Either the Total Pump Power or the Total Pump Head is required.

        Args:
            value (float): value for IDD Field `Total Pump Head`
                Units: Pa
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
                                 'for field `total_pump_head`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `total_pump_head`')
        self._data["Total Pump Head"] = value

    @property
    def phasechange_circulating_rate(self):
        """Get phasechange_circulating_rate

        Returns:
            float: the value of `phasechange_circulating_rate` or None if not set
        """
        return self._data["PhaseChange Circulating Rate"]

    @phasechange_circulating_rate.setter
    def phasechange_circulating_rate(self, value=2.5):
        """  Corresponds to IDD Field `PhaseChange Circulating Rate`
        This is the total mass flow at the pump divided by the gaseous mass flow
        leaving the refrigeration load.

        Args:
            value (float): value for IDD Field `PhaseChange Circulating Rate`
                Units: dimensionless
                Default value: 2.5
                value >= 1.0
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
                                 'for field `phasechange_circulating_rate`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `phasechange_circulating_rate`')
        self._data["PhaseChange Circulating Rate"] = value

    @property
    def pump_drive_type(self):
        """Get pump_drive_type

        Returns:
            str: the value of `pump_drive_type` or None if not set
        """
        return self._data["Pump Drive Type"]

    @pump_drive_type.setter
    def pump_drive_type(self, value="Constant"):
        """  Corresponds to IDD Field `Pump Drive Type`

        Args:
            value (str): value for IDD Field `Pump Drive Type`
                Accepted values are:
                      - Constant
                      - Variable
                Default value: Constant
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
                                 'for field `pump_drive_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_drive_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pump_drive_type`')
            vals = {}
            vals["constant"] = "Constant"
            vals["variable"] = "Variable"
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
                                     'field `pump_drive_type`'.format(value))
            value = vals[value_lower]
        self._data["Pump Drive Type"] = value

    @property
    def variable_speed_pump_cubic_curve_name(self):
        """Get variable_speed_pump_cubic_curve_name

        Returns:
            str: the value of `variable_speed_pump_cubic_curve_name` or None if not set
        """
        return self._data["Variable Speed Pump Cubic Curve Name"]

    @variable_speed_pump_cubic_curve_name.setter
    def variable_speed_pump_cubic_curve_name(self, value=None):
        """  Corresponds to IDD Field `Variable Speed Pump Cubic Curve Name`
        Variable Speed Pump Curve Name is applicable to variable speed pumps
        only.

        Args:
            value (str): value for IDD Field `Variable Speed Pump Cubic Curve Name`
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
                                 'for field `variable_speed_pump_cubic_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `variable_speed_pump_cubic_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `variable_speed_pump_cubic_curve_name`')
        self._data["Variable Speed Pump Cubic Curve Name"] = value

    @property
    def pump_motor_heat_to_fluid(self):
        """Get pump_motor_heat_to_fluid

        Returns:
            float: the value of `pump_motor_heat_to_fluid` or None if not set
        """
        return self._data["Pump Motor Heat to Fluid"]

    @pump_motor_heat_to_fluid.setter
    def pump_motor_heat_to_fluid(self, value=0.85):
        """  Corresponds to IDD Field `Pump Motor Heat to Fluid`
        This is the portion of the pump motor heat added to secondary circulating fluid
        and is equal to the motor efficiency for non-hermetic motor.
        Enter 1.0 for a semi-hermetic motor.

        Args:
            value (float): value for IDD Field `Pump Motor Heat to Fluid`
                Units: dimensionless
                Default value: 0.85
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
                                 'for field `pump_motor_heat_to_fluid`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `pump_motor_heat_to_fluid`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `pump_motor_heat_to_fluid`')
        self._data["Pump Motor Heat to Fluid"] = value

    @property
    def sum_ua_distribution_piping(self):
        """Get sum_ua_distribution_piping

        Returns:
            float: the value of `sum_ua_distribution_piping` or None if not set
        """
        return self._data["Sum UA Distribution Piping"]

    @sum_ua_distribution_piping.setter
    def sum_ua_distribution_piping(self, value=0.0):
        """  Corresponds to IDD Field `Sum UA Distribution Piping`
        Use only if you want to include distribution piping heat gain in refrigeration load.

        Args:
            value (float): value for IDD Field `Sum UA Distribution Piping`
                Units: W/K
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
                                 'for field `sum_ua_distribution_piping`'.format(value))
        self._data["Sum UA Distribution Piping"] = value

    @property
    def distribution_piping_zone_name(self):
        """Get distribution_piping_zone_name

        Returns:
            str: the value of `distribution_piping_zone_name` or None if not set
        """
        return self._data["Distribution Piping Zone Name"]

    @distribution_piping_zone_name.setter
    def distribution_piping_zone_name(self, value=None):
        """  Corresponds to IDD Field `Distribution Piping Zone Name`
        This will be used to determine the temperature used for distribution piping heat gain.
        The pipe heat gains are also counted as cooling credit for the zone.
        Required only if Sum UA Distribution Piping >0.0

        Args:
            value (str): value for IDD Field `Distribution Piping Zone Name`
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
                                 'for field `distribution_piping_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `distribution_piping_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `distribution_piping_zone_name`')
        self._data["Distribution Piping Zone Name"] = value

    @property
    def sum_ua_receiver_or_separator_shell(self):
        """Get sum_ua_receiver_or_separator_shell

        Returns:
            float: the value of `sum_ua_receiver_or_separator_shell` or None if not set
        """
        return self._data["Sum UA Receiver/Separator Shell"]

    @sum_ua_receiver_or_separator_shell.setter
    def sum_ua_receiver_or_separator_shell(self, value=0.0):
        """  Corresponds to IDD Field `Sum UA Receiver/Separator Shell`
        Use only if you want to include Receiver/Separator Shell heat gain in refrigeration load.

        Args:
            value (float): value for IDD Field `Sum UA Receiver/Separator Shell`
                Units: W/K
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
                                 'for field `sum_ua_receiver_or_separator_shell`'.format(value))
        self._data["Sum UA Receiver/Separator Shell"] = value

    @property
    def receiver_or_separator_zone_name(self):
        """Get receiver_or_separator_zone_name

        Returns:
            str: the value of `receiver_or_separator_zone_name` or None if not set
        """
        return self._data["Receiver/Separator Zone Name"]

    @receiver_or_separator_zone_name.setter
    def receiver_or_separator_zone_name(self, value=None):
        """  Corresponds to IDD Field `Receiver/Separator Zone Name`
        This will be used to determine the temperature used for Receiver/Separator Shell heat gain.
        The shell heat gains are also counted as cooling credit for the zone.
        Required only if Sum UA Receiver/Separator Shell >0.0

        Args:
            value (str): value for IDD Field `Receiver/Separator Zone Name`
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
                                 'for field `receiver_or_separator_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `receiver_or_separator_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `receiver_or_separator_zone_name`')
        self._data["Receiver/Separator Zone Name"] = value

    @property
    def evaporator_refrigerant_inventory(self):
        """Get evaporator_refrigerant_inventory

        Returns:
            float: the value of `evaporator_refrigerant_inventory` or None if not set
        """
        return self._data["Evaporator Refrigerant Inventory"]

    @evaporator_refrigerant_inventory.setter
    def evaporator_refrigerant_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Evaporator Refrigerant Inventory`
        This value refers to the refrigerant circulating within the primary system providing
        cooling to the chiller for the secondary loop, not to the fluid circulating
        within the secondary loop itself.

        Args:
            value (float): value for IDD Field `Evaporator Refrigerant Inventory`
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
                                 'for field `evaporator_refrigerant_inventory`'.format(value))
        self._data["Evaporator Refrigerant Inventory"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

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

class RefrigerationWalkIn(object):
    """ Corresponds to IDD object `Refrigeration:WalkIn`
        Works in conjunction with a compressor rack, a refrigeration system, or a
        refrigeration secondary system to simulate the performance of a walk-in cooler.
        The walk-in cooler model uses information at rated conditions along with input
        descriptions for heat transfer surfaces facing multiple zones to determine
        performance.
    
    """
    internal_name = "Refrigeration:WalkIn"
    field_count = 57
    required_fields = ["Name", "Rated Coil Cooling Capacity", "Operating Temperature", "Rated Cooling Source Temperature", "Rated Total Heating Power", "Rated Total Lighting Power", "Defrost Schedule Name", "Insulated Floor Surface Area", "Zone 1 Name", "Total Insulated Surface Area Facing Zone 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:WalkIn`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Rated Coil Cooling Capacity"] = None
        self._data["Operating Temperature"] = None
        self._data["Rated Cooling Source Temperature"] = None
        self._data["Rated Total Heating Power"] = None
        self._data["Heating Power Schedule Name"] = None
        self._data["Rated Cooling Coil Fan Power"] = None
        self._data["Rated Circulation Fan Power"] = None
        self._data["Rated Total Lighting Power"] = None
        self._data["Lighting Schedule Name"] = None
        self._data["Defrost Type"] = None
        self._data["Defrost Control Type"] = None
        self._data["Defrost Schedule Name"] = None
        self._data["Defrost Drip-Down Schedule Name"] = None
        self._data["Defrost Power"] = None
        self._data["Temperature Termination Defrost Fraction to Ice"] = None
        self._data["Restocking Schedule Name"] = None
        self._data["Average Refrigerant Charge Inventory"] = None
        self._data["Insulated Floor Surface Area"] = None
        self._data["Insulated Floor U-Value"] = None
        self._data["Zone 1 Name"] = None
        self._data["Total Insulated Surface Area Facing Zone 1"] = None
        self._data["Insulated Surface U-Value Facing Zone 1"] = None
        self._data["Area of Glass Reach In Doors Facing Zone 1"] = None
        self._data["Height of Glass Reach In Doors Facing Zone 1"] = None
        self._data["Glass Reach In Door U Value Facing Zone 1"] = None
        self._data["Glass Reach In Door Opening Schedule Name Facing Zone 1"] = None
        self._data["Area of Stocking Doors Facing Zone 1"] = None
        self._data["Height of Stocking Doors Facing Zone 1"] = None
        self._data["Stocking Door U Value Facing Zone 1"] = None
        self._data["Stocking Door Opening Schedule Name Facing Zone 1"] = None
        self._data["Stocking Door Opening Protection Type Facing Zone 1"] = None
        self._data["Zone 2 Name"] = None
        self._data["Total Insulated Surface Area Facing Zone 2"] = None
        self._data["Insulated Surface U-Value Facing Zone 2"] = None
        self._data["Area of Glass Reach In Doors Facing Zone 2"] = None
        self._data["Height of Glass Reach In Doors Facing Zone 2"] = None
        self._data["Glass Reach In Door U Value Facing Zone 2"] = None
        self._data["Glass Reach In Door Opening Schedule Name Facing Zone 2"] = None
        self._data["Area of Stocking Doors Facing Zone 2"] = None
        self._data["Height of Stocking Doors Facing Zone 2"] = None
        self._data["Stocking Door U Value Facing Zone 2"] = None
        self._data["Stocking Door Opening Schedule Name Facing Zone 2"] = None
        self._data["Stocking Door Opening Protection Type Facing Zone 2"] = None
        self._data["Zone 3 Name"] = None
        self._data["Total Insulated Surface Area Facing Zone 3"] = None
        self._data["Insulated Surface U-Value Facing Zone 3"] = None
        self._data["Area of Glass Reach In Doors Facing Zone 3"] = None
        self._data["Height of Glass Reach In Doors Facing Zone 3"] = None
        self._data["Glass Reach In Door U Value Facing Zone 3"] = None
        self._data["Glass Reach In Door Opening Schedule Name Facing Zone 3"] = None
        self._data["Area of Stocking Doors Facing Zone 3"] = None
        self._data["Height of Stocking Doors Facing Zone 3"] = None
        self._data["Stocking Door U Value Facing Zone 3"] = None
        self._data["Stocking Door Opening Schedule Name Facing Zone 3"] = None
        self._data["Stocking Door Opening Protection Type Facing Zone 3"] = None
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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_coil_cooling_capacity = None
        else:
            self.rated_coil_cooling_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.operating_temperature = None
        else:
            self.operating_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_cooling_source_temperature = None
        else:
            self.rated_cooling_source_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_total_heating_power = None
        else:
            self.rated_total_heating_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_power_schedule_name = None
        else:
            self.heating_power_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_cooling_coil_fan_power = None
        else:
            self.rated_cooling_coil_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_circulation_fan_power = None
        else:
            self.rated_circulation_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_total_lighting_power = None
        else:
            self.rated_total_lighting_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lighting_schedule_name = None
        else:
            self.lighting_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_type = None
        else:
            self.defrost_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_control_type = None
        else:
            self.defrost_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_schedule_name = None
        else:
            self.defrost_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_dripdown_schedule_name = None
        else:
            self.defrost_dripdown_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_power = None
        else:
            self.defrost_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_termination_defrost_fraction_to_ice = None
        else:
            self.temperature_termination_defrost_fraction_to_ice = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.restocking_schedule_name = None
        else:
            self.restocking_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.average_refrigerant_charge_inventory = None
        else:
            self.average_refrigerant_charge_inventory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.insulated_floor_surface_area = None
        else:
            self.insulated_floor_surface_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.insulated_floor_uvalue = None
        else:
            self.insulated_floor_uvalue = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_1_name = None
        else:
            self.zone_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_insulated_surface_area_facing_zone_1 = None
        else:
            self.total_insulated_surface_area_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.insulated_surface_uvalue_facing_zone_1 = None
        else:
            self.insulated_surface_uvalue_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.area_of_glass_reach_in_doors_facing_zone_1 = None
        else:
            self.area_of_glass_reach_in_doors_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_of_glass_reach_in_doors_facing_zone_1 = None
        else:
            self.height_of_glass_reach_in_doors_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.glass_reach_in_door_u_value_facing_zone_1 = None
        else:
            self.glass_reach_in_door_u_value_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.glass_reach_in_door_opening_schedule_name_facing_zone_1 = None
        else:
            self.glass_reach_in_door_opening_schedule_name_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.area_of_stocking_doors_facing_zone_1 = None
        else:
            self.area_of_stocking_doors_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_of_stocking_doors_facing_zone_1 = None
        else:
            self.height_of_stocking_doors_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stocking_door_u_value_facing_zone_1 = None
        else:
            self.stocking_door_u_value_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stocking_door_opening_schedule_name_facing_zone_1 = None
        else:
            self.stocking_door_opening_schedule_name_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stocking_door_opening_protection_type_facing_zone_1 = None
        else:
            self.stocking_door_opening_protection_type_facing_zone_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_2_name = None
        else:
            self.zone_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_insulated_surface_area_facing_zone_2 = None
        else:
            self.total_insulated_surface_area_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.insulated_surface_uvalue_facing_zone_2 = None
        else:
            self.insulated_surface_uvalue_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.area_of_glass_reach_in_doors_facing_zone_2 = None
        else:
            self.area_of_glass_reach_in_doors_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_of_glass_reach_in_doors_facing_zone_2 = None
        else:
            self.height_of_glass_reach_in_doors_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.glass_reach_in_door_u_value_facing_zone_2 = None
        else:
            self.glass_reach_in_door_u_value_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.glass_reach_in_door_opening_schedule_name_facing_zone_2 = None
        else:
            self.glass_reach_in_door_opening_schedule_name_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.area_of_stocking_doors_facing_zone_2 = None
        else:
            self.area_of_stocking_doors_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_of_stocking_doors_facing_zone_2 = None
        else:
            self.height_of_stocking_doors_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stocking_door_u_value_facing_zone_2 = None
        else:
            self.stocking_door_u_value_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stocking_door_opening_schedule_name_facing_zone_2 = None
        else:
            self.stocking_door_opening_schedule_name_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stocking_door_opening_protection_type_facing_zone_2 = None
        else:
            self.stocking_door_opening_protection_type_facing_zone_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_3_name = None
        else:
            self.zone_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_insulated_surface_area_facing_zone_3 = None
        else:
            self.total_insulated_surface_area_facing_zone_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.insulated_surface_uvalue_facing_zone_3 = None
        else:
            self.insulated_surface_uvalue_facing_zone_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.area_of_glass_reach_in_doors_facing_zone_3 = None
        else:
            self.area_of_glass_reach_in_doors_facing_zone_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_of_glass_reach_in_doors_facing_zone_3 = None
        else:
            self.height_of_glass_reach_in_doors_facing_zone_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.glass_reach_in_door_u_value_facing_zone_3 = None
        else:
            self.glass_reach_in_door_u_value_facing_zone_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.glass_reach_in_door_opening_schedule_name_facing_zone_3 = None
        else:
            self.glass_reach_in_door_opening_schedule_name_facing_zone_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.area_of_stocking_doors_facing_zone_3 = None
        else:
            self.area_of_stocking_doors_facing_zone_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_of_stocking_doors_facing_zone_3 = None
        else:
            self.height_of_stocking_doors_facing_zone_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stocking_door_u_value_facing_zone_3 = None
        else:
            self.stocking_door_u_value_facing_zone_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stocking_door_opening_schedule_name_facing_zone_3 = None
        else:
            self.stocking_door_opening_schedule_name_facing_zone_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stocking_door_opening_protection_type_facing_zone_3 = None
        else:
            self.stocking_door_opening_protection_type_facing_zone_3 = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
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
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def rated_coil_cooling_capacity(self):
        """Get rated_coil_cooling_capacity

        Returns:
            float: the value of `rated_coil_cooling_capacity` or None if not set
        """
        return self._data["Rated Coil Cooling Capacity"]

    @rated_coil_cooling_capacity.setter
    def rated_coil_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `Rated Coil Cooling Capacity`

        Args:
            value (float): value for IDD Field `Rated Coil Cooling Capacity`
                Units: W
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
                                 'for field `rated_coil_cooling_capacity`'.format(value))
        self._data["Rated Coil Cooling Capacity"] = value

    @property
    def operating_temperature(self):
        """Get operating_temperature

        Returns:
            float: the value of `operating_temperature` or None if not set
        """
        return self._data["Operating Temperature"]

    @operating_temperature.setter
    def operating_temperature(self, value=None):
        """  Corresponds to IDD Field `Operating Temperature`

        Args:
            value (float): value for IDD Field `Operating Temperature`
                Units: C
                value < 20.0
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
                                 'for field `operating_temperature`'.format(value))
            if value >= 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `operating_temperature`')
        self._data["Operating Temperature"] = value

    @property
    def rated_cooling_source_temperature(self):
        """Get rated_cooling_source_temperature

        Returns:
            float: the value of `rated_cooling_source_temperature` or None if not set
        """
        return self._data["Rated Cooling Source Temperature"]

    @rated_cooling_source_temperature.setter
    def rated_cooling_source_temperature(self, value=None):
        """  Corresponds to IDD Field `Rated Cooling Source Temperature`
        If DXEvaporator, use evaporating temperature (saturated suction temperature)
        If BrineCoil, use Brine entering temperature
        used to set minimum suction pressure for DX systems and
        minimum brine temp for secondary systems

        Args:
            value (float): value for IDD Field `Rated Cooling Source Temperature`
                Units: C
                value >= -70.0
                value <= 40.0
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
                                 'for field `rated_cooling_source_temperature`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `rated_cooling_source_temperature`')
            if value > 40.0:
                raise ValueError('value need to be smaller 40.0 '
                                 'for field `rated_cooling_source_temperature`')
        self._data["Rated Cooling Source Temperature"] = value

    @property
    def rated_total_heating_power(self):
        """Get rated_total_heating_power

        Returns:
            float: the value of `rated_total_heating_power` or None if not set
        """
        return self._data["Rated Total Heating Power"]

    @rated_total_heating_power.setter
    def rated_total_heating_power(self, value=None):
        """  Corresponds to IDD Field `Rated Total Heating Power`
        Include total for all anti-sweat, door, drip-pan, and floor heater power
        Do not include defrost heater power

        Args:
            value (float): value for IDD Field `Rated Total Heating Power`
                Units: W
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
                                 'for field `rated_total_heating_power`'.format(value))
        self._data["Rated Total Heating Power"] = value

    @property
    def heating_power_schedule_name(self):
        """Get heating_power_schedule_name

        Returns:
            str: the value of `heating_power_schedule_name` or None if not set
        """
        return self._data["Heating Power Schedule Name"]

    @heating_power_schedule_name.setter
    def heating_power_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Power Schedule Name`
        Values will be used to multiply the total heating power
        Values in the schedule should be between 0.0 and 1.0
        For example, this could be used if display door antisweat heaters
        are turned off at night
        Defaults to always on if schedule name left blank.

        Args:
            value (str): value for IDD Field `Heating Power Schedule Name`
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
                                 'for field `heating_power_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_power_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_power_schedule_name`')
        self._data["Heating Power Schedule Name"] = value

    @property
    def rated_cooling_coil_fan_power(self):
        """Get rated_cooling_coil_fan_power

        Returns:
            float: the value of `rated_cooling_coil_fan_power` or None if not set
        """
        return self._data["Rated Cooling Coil Fan Power"]

    @rated_cooling_coil_fan_power.setter
    def rated_cooling_coil_fan_power(self, value=375.0):
        """  Corresponds to IDD Field `Rated Cooling Coil Fan Power`

        Args:
            value (float): value for IDD Field `Rated Cooling Coil Fan Power`
                Units: W
                Default value: 375.0
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
                                 'for field `rated_cooling_coil_fan_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_cooling_coil_fan_power`')
        self._data["Rated Cooling Coil Fan Power"] = value

    @property
    def rated_circulation_fan_power(self):
        """Get rated_circulation_fan_power

        Returns:
            float: the value of `rated_circulation_fan_power` or None if not set
        """
        return self._data["Rated Circulation Fan Power"]

    @rated_circulation_fan_power.setter
    def rated_circulation_fan_power(self, value=0.0):
        """  Corresponds to IDD Field `Rated Circulation Fan Power`

        Args:
            value (float): value for IDD Field `Rated Circulation Fan Power`
                Units: W
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
                                 'for field `rated_circulation_fan_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_circulation_fan_power`')
        self._data["Rated Circulation Fan Power"] = value

    @property
    def rated_total_lighting_power(self):
        """Get rated_total_lighting_power

        Returns:
            float: the value of `rated_total_lighting_power` or None if not set
        """
        return self._data["Rated Total Lighting Power"]

    @rated_total_lighting_power.setter
    def rated_total_lighting_power(self, value=None):
        """  Corresponds to IDD Field `Rated Total Lighting Power`
        Enter the total (display + task) installed lighting power.

        Args:
            value (float): value for IDD Field `Rated Total Lighting Power`
                Units: W
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
                                 'for field `rated_total_lighting_power`'.format(value))
        self._data["Rated Total Lighting Power"] = value

    @property
    def lighting_schedule_name(self):
        """Get lighting_schedule_name

        Returns:
            str: the value of `lighting_schedule_name` or None if not set
        """
        return self._data["Lighting Schedule Name"]

    @lighting_schedule_name.setter
    def lighting_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Lighting Schedule Name`
        The schedule should contain values between 0 and 1
        Defaults to always on if schedule name left blank.

        Args:
            value (str): value for IDD Field `Lighting Schedule Name`
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
                                 'for field `lighting_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lighting_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lighting_schedule_name`')
        self._data["Lighting Schedule Name"] = value

    @property
    def defrost_type(self):
        """Get defrost_type

        Returns:
            str: the value of `defrost_type` or None if not set
        """
        return self._data["Defrost Type"]

    @defrost_type.setter
    def defrost_type(self, value="Electric"):
        """  Corresponds to IDD Field `Defrost Type`
        HotFluid includes either hot gas defrost for a DX system or
        Hot Brine defrost if this walk in is cooled by brine from a secondary chiller

        Args:
            value (str): value for IDD Field `Defrost Type`
                Accepted values are:
                      - HotFluid
                      - Electric
                      - None
                      - OffCycle
                Default value: Electric
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
                                 'for field `defrost_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_type`')
            vals = {}
            vals["hotfluid"] = "HotFluid"
            vals["electric"] = "Electric"
            vals["none"] = "None"
            vals["offcycle"] = "OffCycle"
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
                                     'field `defrost_type`'.format(value))
            value = vals[value_lower]
        self._data["Defrost Type"] = value

    @property
    def defrost_control_type(self):
        """Get defrost_control_type

        Returns:
            str: the value of `defrost_control_type` or None if not set
        """
        return self._data["Defrost Control Type"]

    @defrost_control_type.setter
    def defrost_control_type(self, value="TimeSchedule"):
        """  Corresponds to IDD Field `Defrost Control Type`

        Args:
            value (str): value for IDD Field `Defrost Control Type`
                Accepted values are:
                      - TimeSchedule
                      - TemperatureTermination
                Default value: TimeSchedule
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
                                 'for field `defrost_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_control_type`')
            vals = {}
            vals["timeschedule"] = "TimeSchedule"
            vals["temperaturetermination"] = "TemperatureTermination"
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
                                     'field `defrost_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Defrost Control Type"] = value

    @property
    def defrost_schedule_name(self):
        """Get defrost_schedule_name

        Returns:
            str: the value of `defrost_schedule_name` or None if not set
        """
        return self._data["Defrost Schedule Name"]

    @defrost_schedule_name.setter
    def defrost_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Defrost Schedule Name`
        The schedule values should be 0 (off) or 1 (on)

        Args:
            value (str): value for IDD Field `Defrost Schedule Name`
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
                                 'for field `defrost_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_schedule_name`')
        self._data["Defrost Schedule Name"] = value

    @property
    def defrost_dripdown_schedule_name(self):
        """Get defrost_dripdown_schedule_name

        Returns:
            str: the value of `defrost_dripdown_schedule_name` or None if not set
        """
        return self._data["Defrost Drip-Down Schedule Name"]

    @defrost_dripdown_schedule_name.setter
    def defrost_dripdown_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Defrost Drip-Down Schedule Name`
        The schedule values should be 0 (off) or 1 (on)
        The start time for each defrost period in this drip-down schedule should coincide with
        the start time for each defrost period in the defrost schedule (previous input
        field).The length of each defrost drip-down period must be greater than or equal to the
        corresponding defrost period specified in the defrost schedule. This extra time
        allows the melted frost to drip from the coil before refrigeration is restarted.

        Args:
            value (str): value for IDD Field `Defrost Drip-Down Schedule Name`
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
                                 'for field `defrost_dripdown_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_dripdown_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_dripdown_schedule_name`')
        self._data["Defrost Drip-Down Schedule Name"] = value

    @property
    def defrost_power(self):
        """Get defrost_power

        Returns:
            float: the value of `defrost_power` or None if not set
        """
        return self._data["Defrost Power"]

    @defrost_power.setter
    def defrost_power(self, value=None):
        """  Corresponds to IDD Field `Defrost Power`
        needed for all defrost types except none and offcycle

        Args:
            value (float): value for IDD Field `Defrost Power`
                Units: W
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
                                 'for field `defrost_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `defrost_power`')
        self._data["Defrost Power"] = value

    @property
    def temperature_termination_defrost_fraction_to_ice(self):
        """Get temperature_termination_defrost_fraction_to_ice

        Returns:
            float: the value of `temperature_termination_defrost_fraction_to_ice` or None if not set
        """
        return self._data["Temperature Termination Defrost Fraction to Ice"]

    @temperature_termination_defrost_fraction_to_ice.setter
    def temperature_termination_defrost_fraction_to_ice(self, value=None):
        """  Corresponds to IDD Field `Temperature Termination Defrost Fraction to Ice`
        This is the portion of the defrost energy that is available to melt frost
        Needed only for defrost control type TemperatureTermination
        defaults to 0.7 for electric defrost and to 0.3 for hot fluid defrost

        Args:
            value (float): value for IDD Field `Temperature Termination Defrost Fraction to Ice`
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
                                 'for field `temperature_termination_defrost_fraction_to_ice`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `temperature_termination_defrost_fraction_to_ice`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `temperature_termination_defrost_fraction_to_ice`')
        self._data["Temperature Termination Defrost Fraction to Ice"] = value

    @property
    def restocking_schedule_name(self):
        """Get restocking_schedule_name

        Returns:
            str: the value of `restocking_schedule_name` or None if not set
        """
        return self._data["Restocking Schedule Name"]

    @restocking_schedule_name.setter
    def restocking_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Restocking Schedule Name`
        Schedule values should be in units of Watts
        Leave this field blank if no restocking is to be modeled

        Args:
            value (str): value for IDD Field `Restocking Schedule Name`
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
                                 'for field `restocking_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `restocking_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `restocking_schedule_name`')
        self._data["Restocking Schedule Name"] = value

    @property
    def average_refrigerant_charge_inventory(self):
        """Get average_refrigerant_charge_inventory

        Returns:
            float: the value of `average_refrigerant_charge_inventory` or None if not set
        """
        return self._data["Average Refrigerant Charge Inventory"]

    @average_refrigerant_charge_inventory.setter
    def average_refrigerant_charge_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Average Refrigerant Charge Inventory`
        This value is only used if the Cooling Source Type is DXEvaporator

        Args:
            value (float): value for IDD Field `Average Refrigerant Charge Inventory`
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
                                 'for field `average_refrigerant_charge_inventory`'.format(value))
        self._data["Average Refrigerant Charge Inventory"] = value

    @property
    def insulated_floor_surface_area(self):
        """Get insulated_floor_surface_area

        Returns:
            float: the value of `insulated_floor_surface_area` or None if not set
        """
        return self._data["Insulated Floor Surface Area"]

    @insulated_floor_surface_area.setter
    def insulated_floor_surface_area(self, value=None):
        """  Corresponds to IDD Field `Insulated Floor Surface Area`
        floor area of walk-in cooler

        Args:
            value (float): value for IDD Field `Insulated Floor Surface Area`
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
                                 'for field `insulated_floor_surface_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `insulated_floor_surface_area`')
        self._data["Insulated Floor Surface Area"] = value

    @property
    def insulated_floor_uvalue(self):
        """Get insulated_floor_uvalue

        Returns:
            float: the value of `insulated_floor_uvalue` or None if not set
        """
        return self._data["Insulated Floor U-Value"]

    @insulated_floor_uvalue.setter
    def insulated_floor_uvalue(self, value=0.3154):
        """  Corresponds to IDD Field `Insulated Floor U-Value`
        The default value corresponds to R18
        To convert other Archaic American R-values to U, divide 5.678 by the R-value
        Some examples:
        R15 is U 0.3785 W/m2-K
        R5 is U 1.136 W/m2-K

        Args:
            value (float): value for IDD Field `Insulated Floor U-Value`
                Units: W/m2-K
                Default value: 0.3154
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
                                 'for field `insulated_floor_uvalue`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `insulated_floor_uvalue`')
        self._data["Insulated Floor U-Value"] = value

    @property
    def zone_1_name(self):
        """Get zone_1_name

        Returns:
            str: the value of `zone_1_name` or None if not set
        """
        return self._data["Zone 1 Name"]

    @zone_1_name.setter
    def zone_1_name(self, value=None):
        """  Corresponds to IDD Field `Zone 1 Name`
        This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object.
        The walkin cooler can face multiple zones.  The heat exchange with each zone
        must be input separately

        Args:
            value (str): value for IDD Field `Zone 1 Name`
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
                                 'for field `zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_1_name`')
        self._data["Zone 1 Name"] = value

    @property
    def total_insulated_surface_area_facing_zone_1(self):
        """Get total_insulated_surface_area_facing_zone_1

        Returns:
            float: the value of `total_insulated_surface_area_facing_zone_1` or None if not set
        """
        return self._data["Total Insulated Surface Area Facing Zone 1"]

    @total_insulated_surface_area_facing_zone_1.setter
    def total_insulated_surface_area_facing_zone_1(self, value=None):
        """  Corresponds to IDD Field `Total Insulated Surface Area Facing Zone 1`
        Area should include walls and ceilings, but not doors

        Args:
            value (float): value for IDD Field `Total Insulated Surface Area Facing Zone 1`
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
                                 'for field `total_insulated_surface_area_facing_zone_1`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `total_insulated_surface_area_facing_zone_1`')
        self._data["Total Insulated Surface Area Facing Zone 1"] = value

    @property
    def insulated_surface_uvalue_facing_zone_1(self):
        """Get insulated_surface_uvalue_facing_zone_1

        Returns:
            float: the value of `insulated_surface_uvalue_facing_zone_1` or None if not set
        """
        return self._data["Insulated Surface U-Value Facing Zone 1"]

    @insulated_surface_uvalue_facing_zone_1.setter
    def insulated_surface_uvalue_facing_zone_1(self, value=0.3154):
        """  Corresponds to IDD Field `Insulated Surface U-Value Facing Zone 1`
        The default value corresponds to R18
        To convert other Archaic American R-values to U, divide 5.678 by the R-value
        Some examples:
        R15 is U 0.3785 W/m2-K
        R5 is U 1.136 W/m2-K

        Args:
            value (float): value for IDD Field `Insulated Surface U-Value Facing Zone 1`
                Units: W/m2-K
                Default value: 0.3154
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
                                 'for field `insulated_surface_uvalue_facing_zone_1`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `insulated_surface_uvalue_facing_zone_1`')
        self._data["Insulated Surface U-Value Facing Zone 1"] = value

    @property
    def area_of_glass_reach_in_doors_facing_zone_1(self):
        """Get area_of_glass_reach_in_doors_facing_zone_1

        Returns:
            float: the value of `area_of_glass_reach_in_doors_facing_zone_1` or None if not set
        """
        return self._data["Area of Glass Reach In Doors Facing Zone 1"]

    @area_of_glass_reach_in_doors_facing_zone_1.setter
    def area_of_glass_reach_in_doors_facing_zone_1(self, value=0.0):
        """  Corresponds to IDD Field `Area of Glass Reach In Doors Facing Zone 1`

        Args:
            value (float): value for IDD Field `Area of Glass Reach In Doors Facing Zone 1`
                Units: m2
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
                                 'for field `area_of_glass_reach_in_doors_facing_zone_1`'.format(value))
        self._data["Area of Glass Reach In Doors Facing Zone 1"] = value

    @property
    def height_of_glass_reach_in_doors_facing_zone_1(self):
        """Get height_of_glass_reach_in_doors_facing_zone_1

        Returns:
            float: the value of `height_of_glass_reach_in_doors_facing_zone_1` or None if not set
        """
        return self._data["Height of Glass Reach In Doors Facing Zone 1"]

    @height_of_glass_reach_in_doors_facing_zone_1.setter
    def height_of_glass_reach_in_doors_facing_zone_1(self, value=1.5):
        """  Corresponds to IDD Field `Height of Glass Reach In Doors Facing Zone 1`

        Args:
            value (float): value for IDD Field `Height of Glass Reach In Doors Facing Zone 1`
                Units: m
                Default value: 1.5
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
                                 'for field `height_of_glass_reach_in_doors_facing_zone_1`'.format(value))
        self._data["Height of Glass Reach In Doors Facing Zone 1"] = value

    @property
    def glass_reach_in_door_u_value_facing_zone_1(self):
        """Get glass_reach_in_door_u_value_facing_zone_1

        Returns:
            float: the value of `glass_reach_in_door_u_value_facing_zone_1` or None if not set
        """
        return self._data["Glass Reach In Door U Value Facing Zone 1"]

    @glass_reach_in_door_u_value_facing_zone_1.setter
    def glass_reach_in_door_u_value_facing_zone_1(self, value=1.136):
        """  Corresponds to IDD Field `Glass Reach In Door U Value Facing Zone 1`
        The default value corresponds to R5
        To convert other Archaic American R-values to U, divide 5.678 by the R-value

        Args:
            value (float): value for IDD Field `Glass Reach In Door U Value Facing Zone 1`
                Units: W/m2-K
                Default value: 1.136
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
                                 'for field `glass_reach_in_door_u_value_facing_zone_1`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `glass_reach_in_door_u_value_facing_zone_1`')
        self._data["Glass Reach In Door U Value Facing Zone 1"] = value

    @property
    def glass_reach_in_door_opening_schedule_name_facing_zone_1(self):
        """Get glass_reach_in_door_opening_schedule_name_facing_zone_1

        Returns:
            str: the value of `glass_reach_in_door_opening_schedule_name_facing_zone_1` or None if not set
        """
        return self._data["Glass Reach In Door Opening Schedule Name Facing Zone 1"]

    @glass_reach_in_door_opening_schedule_name_facing_zone_1.setter
    def glass_reach_in_door_opening_schedule_name_facing_zone_1(self, value=None):
        """  Corresponds to IDD Field `Glass Reach In Door Opening Schedule Name Facing Zone 1`
        Schedule values should all be between 0.0 and 1.0.
        For example, if the door is open 30% of the time during working hours,
        then the schedule would hold the value 0.3 during working hours
        and 0 during other hours
        If no schedule name is entered, default is 5% open time during all hours

        Args:
            value (str): value for IDD Field `Glass Reach In Door Opening Schedule Name Facing Zone 1`
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
                                 'for field `glass_reach_in_door_opening_schedule_name_facing_zone_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `glass_reach_in_door_opening_schedule_name_facing_zone_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `glass_reach_in_door_opening_schedule_name_facing_zone_1`')
        self._data["Glass Reach In Door Opening Schedule Name Facing Zone 1"] = value

    @property
    def area_of_stocking_doors_facing_zone_1(self):
        """Get area_of_stocking_doors_facing_zone_1

        Returns:
            float: the value of `area_of_stocking_doors_facing_zone_1` or None if not set
        """
        return self._data["Area of Stocking Doors Facing Zone 1"]

    @area_of_stocking_doors_facing_zone_1.setter
    def area_of_stocking_doors_facing_zone_1(self, value=0.0):
        """  Corresponds to IDD Field `Area of Stocking Doors Facing Zone 1`

        Args:
            value (float): value for IDD Field `Area of Stocking Doors Facing Zone 1`
                Units: m2
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
                                 'for field `area_of_stocking_doors_facing_zone_1`'.format(value))
        self._data["Area of Stocking Doors Facing Zone 1"] = value

    @property
    def height_of_stocking_doors_facing_zone_1(self):
        """Get height_of_stocking_doors_facing_zone_1

        Returns:
            float: the value of `height_of_stocking_doors_facing_zone_1` or None if not set
        """
        return self._data["Height of Stocking Doors Facing Zone 1"]

    @height_of_stocking_doors_facing_zone_1.setter
    def height_of_stocking_doors_facing_zone_1(self, value=3.0):
        """  Corresponds to IDD Field `Height of Stocking Doors Facing Zone 1`

        Args:
            value (float): value for IDD Field `Height of Stocking Doors Facing Zone 1`
                Units: m
                Default value: 3.0
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
                                 'for field `height_of_stocking_doors_facing_zone_1`'.format(value))
        self._data["Height of Stocking Doors Facing Zone 1"] = value

    @property
    def stocking_door_u_value_facing_zone_1(self):
        """Get stocking_door_u_value_facing_zone_1

        Returns:
            float: the value of `stocking_door_u_value_facing_zone_1` or None if not set
        """
        return self._data["Stocking Door U Value Facing Zone 1"]

    @stocking_door_u_value_facing_zone_1.setter
    def stocking_door_u_value_facing_zone_1(self, value=0.3785):
        """  Corresponds to IDD Field `Stocking Door U Value Facing Zone 1`
        The default value corresponds to R15
        To convert other Archaic American R-values to U, divide 5.678 by the R-value
        Some examples:
        R5 is U 1.136 W/m2-K
        R18 is U 0.3154 W/m2-K

        Args:
            value (float): value for IDD Field `Stocking Door U Value Facing Zone 1`
                Units: W/m2-K
                Default value: 0.3785
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
                                 'for field `stocking_door_u_value_facing_zone_1`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `stocking_door_u_value_facing_zone_1`')
        self._data["Stocking Door U Value Facing Zone 1"] = value

    @property
    def stocking_door_opening_schedule_name_facing_zone_1(self):
        """Get stocking_door_opening_schedule_name_facing_zone_1

        Returns:
            str: the value of `stocking_door_opening_schedule_name_facing_zone_1` or None if not set
        """
        return self._data["Stocking Door Opening Schedule Name Facing Zone 1"]

    @stocking_door_opening_schedule_name_facing_zone_1.setter
    def stocking_door_opening_schedule_name_facing_zone_1(self, value=None):
        """  Corresponds to IDD Field `Stocking Door Opening Schedule Name Facing Zone 1`
        Schedule values should all be between 0.0 and 1.0.
        For example, if the door is open 30% of the time during working hours,
        then the schedule would hold the value 0.3 during working hours
        and 0 during other hours
        If no schedule name is entered, default is 5% open time during all hours

        Args:
            value (str): value for IDD Field `Stocking Door Opening Schedule Name Facing Zone 1`
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
                                 'for field `stocking_door_opening_schedule_name_facing_zone_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `stocking_door_opening_schedule_name_facing_zone_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `stocking_door_opening_schedule_name_facing_zone_1`')
        self._data["Stocking Door Opening Schedule Name Facing Zone 1"] = value

    @property
    def stocking_door_opening_protection_type_facing_zone_1(self):
        """Get stocking_door_opening_protection_type_facing_zone_1

        Returns:
            str: the value of `stocking_door_opening_protection_type_facing_zone_1` or None if not set
        """
        return self._data["Stocking Door Opening Protection Type Facing Zone 1"]

    @stocking_door_opening_protection_type_facing_zone_1.setter
    def stocking_door_opening_protection_type_facing_zone_1(self, value="AirCurtain"):
        """  Corresponds to IDD Field `Stocking Door Opening Protection Type Facing Zone 1`
        Use StripCurtain for hanging strips or airlock vestibules

        Args:
            value (str): value for IDD Field `Stocking Door Opening Protection Type Facing Zone 1`
                Accepted values are:
                      - None
                      - AirCurtain
                      - StripCurtain
                Default value: AirCurtain
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
                                 'for field `stocking_door_opening_protection_type_facing_zone_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `stocking_door_opening_protection_type_facing_zone_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `stocking_door_opening_protection_type_facing_zone_1`')
            vals = {}
            vals["none"] = "None"
            vals["aircurtain"] = "AirCurtain"
            vals["stripcurtain"] = "StripCurtain"
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
                                     'field `stocking_door_opening_protection_type_facing_zone_1`'.format(value))
            value = vals[value_lower]
        self._data["Stocking Door Opening Protection Type Facing Zone 1"] = value

    @property
    def zone_2_name(self):
        """Get zone_2_name

        Returns:
            str: the value of `zone_2_name` or None if not set
        """
        return self._data["Zone 2 Name"]

    @zone_2_name.setter
    def zone_2_name(self, value=None):
        """  Corresponds to IDD Field `Zone 2 Name`
        required if more than one zone
        This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object.

        Args:
            value (str): value for IDD Field `Zone 2 Name`
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
                                 'for field `zone_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_2_name`')
        self._data["Zone 2 Name"] = value

    @property
    def total_insulated_surface_area_facing_zone_2(self):
        """Get total_insulated_surface_area_facing_zone_2

        Returns:
            float: the value of `total_insulated_surface_area_facing_zone_2` or None if not set
        """
        return self._data["Total Insulated Surface Area Facing Zone 2"]

    @total_insulated_surface_area_facing_zone_2.setter
    def total_insulated_surface_area_facing_zone_2(self, value=None):
        """  Corresponds to IDD Field `Total Insulated Surface Area Facing Zone 2`
        Area should include walls and ceilings, but not doors
        required if more than one zone

        Args:
            value (float): value for IDD Field `Total Insulated Surface Area Facing Zone 2`
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
                                 'for field `total_insulated_surface_area_facing_zone_2`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `total_insulated_surface_area_facing_zone_2`')
        self._data["Total Insulated Surface Area Facing Zone 2"] = value

    @property
    def insulated_surface_uvalue_facing_zone_2(self):
        """Get insulated_surface_uvalue_facing_zone_2

        Returns:
            float: the value of `insulated_surface_uvalue_facing_zone_2` or None if not set
        """
        return self._data["Insulated Surface U-Value Facing Zone 2"]

    @insulated_surface_uvalue_facing_zone_2.setter
    def insulated_surface_uvalue_facing_zone_2(self, value=0.3154):
        """  Corresponds to IDD Field `Insulated Surface U-Value Facing Zone 2`
        The default value corresponds to R18
        To convert other Archaic American R-values to U, divide 5.678 by the R-value
        Some examples:
        R15 is U 0.3785 W/m2-K
        R5 is U 1.136 W/m2-K

        Args:
            value (float): value for IDD Field `Insulated Surface U-Value Facing Zone 2`
                Units: W/m2-K
                Default value: 0.3154
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
                                 'for field `insulated_surface_uvalue_facing_zone_2`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `insulated_surface_uvalue_facing_zone_2`')
        self._data["Insulated Surface U-Value Facing Zone 2"] = value

    @property
    def area_of_glass_reach_in_doors_facing_zone_2(self):
        """Get area_of_glass_reach_in_doors_facing_zone_2

        Returns:
            float: the value of `area_of_glass_reach_in_doors_facing_zone_2` or None if not set
        """
        return self._data["Area of Glass Reach In Doors Facing Zone 2"]

    @area_of_glass_reach_in_doors_facing_zone_2.setter
    def area_of_glass_reach_in_doors_facing_zone_2(self, value=0.0):
        """  Corresponds to IDD Field `Area of Glass Reach In Doors Facing Zone 2`

        Args:
            value (float): value for IDD Field `Area of Glass Reach In Doors Facing Zone 2`
                Units: m2
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
                                 'for field `area_of_glass_reach_in_doors_facing_zone_2`'.format(value))
        self._data["Area of Glass Reach In Doors Facing Zone 2"] = value

    @property
    def height_of_glass_reach_in_doors_facing_zone_2(self):
        """Get height_of_glass_reach_in_doors_facing_zone_2

        Returns:
            float: the value of `height_of_glass_reach_in_doors_facing_zone_2` or None if not set
        """
        return self._data["Height of Glass Reach In Doors Facing Zone 2"]

    @height_of_glass_reach_in_doors_facing_zone_2.setter
    def height_of_glass_reach_in_doors_facing_zone_2(self, value=1.5):
        """  Corresponds to IDD Field `Height of Glass Reach In Doors Facing Zone 2`

        Args:
            value (float): value for IDD Field `Height of Glass Reach In Doors Facing Zone 2`
                Units: m
                Default value: 1.5
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
                                 'for field `height_of_glass_reach_in_doors_facing_zone_2`'.format(value))
        self._data["Height of Glass Reach In Doors Facing Zone 2"] = value

    @property
    def glass_reach_in_door_u_value_facing_zone_2(self):
        """Get glass_reach_in_door_u_value_facing_zone_2

        Returns:
            float: the value of `glass_reach_in_door_u_value_facing_zone_2` or None if not set
        """
        return self._data["Glass Reach In Door U Value Facing Zone 2"]

    @glass_reach_in_door_u_value_facing_zone_2.setter
    def glass_reach_in_door_u_value_facing_zone_2(self, value=1.136):
        """  Corresponds to IDD Field `Glass Reach In Door U Value Facing Zone 2`
        The default value corresponds to R5
        To convert other Archaic American R-values to U, divide 5.678 by the R-value

        Args:
            value (float): value for IDD Field `Glass Reach In Door U Value Facing Zone 2`
                Units: W/m2-K
                Default value: 1.136
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
                                 'for field `glass_reach_in_door_u_value_facing_zone_2`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `glass_reach_in_door_u_value_facing_zone_2`')
        self._data["Glass Reach In Door U Value Facing Zone 2"] = value

    @property
    def glass_reach_in_door_opening_schedule_name_facing_zone_2(self):
        """Get glass_reach_in_door_opening_schedule_name_facing_zone_2

        Returns:
            str: the value of `glass_reach_in_door_opening_schedule_name_facing_zone_2` or None if not set
        """
        return self._data["Glass Reach In Door Opening Schedule Name Facing Zone 2"]

    @glass_reach_in_door_opening_schedule_name_facing_zone_2.setter
    def glass_reach_in_door_opening_schedule_name_facing_zone_2(self, value=None):
        """  Corresponds to IDD Field `Glass Reach In Door Opening Schedule Name Facing Zone 2`
        Schedule values should all be between 0.0 and 1.0.
        For example, if the door is open 30% of the time during working hours,
        then the schedule would hold the value 0.3 during working hours
        and 0 during other hours
        If no schedule name is entered, default is 5% open time during all hours

        Args:
            value (str): value for IDD Field `Glass Reach In Door Opening Schedule Name Facing Zone 2`
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
                                 'for field `glass_reach_in_door_opening_schedule_name_facing_zone_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `glass_reach_in_door_opening_schedule_name_facing_zone_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `glass_reach_in_door_opening_schedule_name_facing_zone_2`')
        self._data["Glass Reach In Door Opening Schedule Name Facing Zone 2"] = value

    @property
    def area_of_stocking_doors_facing_zone_2(self):
        """Get area_of_stocking_doors_facing_zone_2

        Returns:
            float: the value of `area_of_stocking_doors_facing_zone_2` or None if not set
        """
        return self._data["Area of Stocking Doors Facing Zone 2"]

    @area_of_stocking_doors_facing_zone_2.setter
    def area_of_stocking_doors_facing_zone_2(self, value=0.0):
        """  Corresponds to IDD Field `Area of Stocking Doors Facing Zone 2`

        Args:
            value (float): value for IDD Field `Area of Stocking Doors Facing Zone 2`
                Units: m2
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
                                 'for field `area_of_stocking_doors_facing_zone_2`'.format(value))
        self._data["Area of Stocking Doors Facing Zone 2"] = value

    @property
    def height_of_stocking_doors_facing_zone_2(self):
        """Get height_of_stocking_doors_facing_zone_2

        Returns:
            float: the value of `height_of_stocking_doors_facing_zone_2` or None if not set
        """
        return self._data["Height of Stocking Doors Facing Zone 2"]

    @height_of_stocking_doors_facing_zone_2.setter
    def height_of_stocking_doors_facing_zone_2(self, value=3.0):
        """  Corresponds to IDD Field `Height of Stocking Doors Facing Zone 2`

        Args:
            value (float): value for IDD Field `Height of Stocking Doors Facing Zone 2`
                Units: m
                Default value: 3.0
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
                                 'for field `height_of_stocking_doors_facing_zone_2`'.format(value))
        self._data["Height of Stocking Doors Facing Zone 2"] = value

    @property
    def stocking_door_u_value_facing_zone_2(self):
        """Get stocking_door_u_value_facing_zone_2

        Returns:
            float: the value of `stocking_door_u_value_facing_zone_2` or None if not set
        """
        return self._data["Stocking Door U Value Facing Zone 2"]

    @stocking_door_u_value_facing_zone_2.setter
    def stocking_door_u_value_facing_zone_2(self, value=0.3785):
        """  Corresponds to IDD Field `Stocking Door U Value Facing Zone 2`
        The default value corresponds to R15
        To convert other Archaic American R-values to U, divide 5.678 by the R-value
        Some examples:
        R5 is U 1.136 W/m2-K
        R18 is U 0.3154 W/m2-K

        Args:
            value (float): value for IDD Field `Stocking Door U Value Facing Zone 2`
                Units: W/m2-K
                Default value: 0.3785
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
                                 'for field `stocking_door_u_value_facing_zone_2`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `stocking_door_u_value_facing_zone_2`')
        self._data["Stocking Door U Value Facing Zone 2"] = value

    @property
    def stocking_door_opening_schedule_name_facing_zone_2(self):
        """Get stocking_door_opening_schedule_name_facing_zone_2

        Returns:
            str: the value of `stocking_door_opening_schedule_name_facing_zone_2` or None if not set
        """
        return self._data["Stocking Door Opening Schedule Name Facing Zone 2"]

    @stocking_door_opening_schedule_name_facing_zone_2.setter
    def stocking_door_opening_schedule_name_facing_zone_2(self, value=None):
        """  Corresponds to IDD Field `Stocking Door Opening Schedule Name Facing Zone 2`
        Schedule values should all be between 0.0 and 1.0.
        For example, if the door is open 30% of the time during working hours,
        then the schedule would hold the value 0.3 during working hours
        and 0 during other hours
        If no schedule name is entered, default is 5% open time during all hours

        Args:
            value (str): value for IDD Field `Stocking Door Opening Schedule Name Facing Zone 2`
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
                                 'for field `stocking_door_opening_schedule_name_facing_zone_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `stocking_door_opening_schedule_name_facing_zone_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `stocking_door_opening_schedule_name_facing_zone_2`')
        self._data["Stocking Door Opening Schedule Name Facing Zone 2"] = value

    @property
    def stocking_door_opening_protection_type_facing_zone_2(self):
        """Get stocking_door_opening_protection_type_facing_zone_2

        Returns:
            str: the value of `stocking_door_opening_protection_type_facing_zone_2` or None if not set
        """
        return self._data["Stocking Door Opening Protection Type Facing Zone 2"]

    @stocking_door_opening_protection_type_facing_zone_2.setter
    def stocking_door_opening_protection_type_facing_zone_2(self, value="AirCurtain"):
        """  Corresponds to IDD Field `Stocking Door Opening Protection Type Facing Zone 2`
        Use StripCurtain for hanging strips or airlock vestibules
        last extensible set begins here
        dup remaining 12 lines as many times as there are zones exchanging heat with walkin
        Move the ending semicolon and increment the field numbers.

        Args:
            value (str): value for IDD Field `Stocking Door Opening Protection Type Facing Zone 2`
                Accepted values are:
                      - None
                      - AirCurtain
                      - StripCurtain
                Default value: AirCurtain
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
                                 'for field `stocking_door_opening_protection_type_facing_zone_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `stocking_door_opening_protection_type_facing_zone_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `stocking_door_opening_protection_type_facing_zone_2`')
            vals = {}
            vals["none"] = "None"
            vals["aircurtain"] = "AirCurtain"
            vals["stripcurtain"] = "StripCurtain"
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
                                     'field `stocking_door_opening_protection_type_facing_zone_2`'.format(value))
            value = vals[value_lower]
        self._data["Stocking Door Opening Protection Type Facing Zone 2"] = value

    @property
    def zone_3_name(self):
        """Get zone_3_name

        Returns:
            str: the value of `zone_3_name` or None if not set
        """
        return self._data["Zone 3 Name"]

    @zone_3_name.setter
    def zone_3_name(self, value=None):
        """  Corresponds to IDD Field `Zone 3 Name`
        This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object.
        required if more than two zones

        Args:
            value (str): value for IDD Field `Zone 3 Name`
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
                                 'for field `zone_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_3_name`')
        self._data["Zone 3 Name"] = value

    @property
    def total_insulated_surface_area_facing_zone_3(self):
        """Get total_insulated_surface_area_facing_zone_3

        Returns:
            float: the value of `total_insulated_surface_area_facing_zone_3` or None if not set
        """
        return self._data["Total Insulated Surface Area Facing Zone 3"]

    @total_insulated_surface_area_facing_zone_3.setter
    def total_insulated_surface_area_facing_zone_3(self, value=None):
        """  Corresponds to IDD Field `Total Insulated Surface Area Facing Zone 3`
        required if more than two zones
        Area should include walls and ceilings, but not doors

        Args:
            value (float): value for IDD Field `Total Insulated Surface Area Facing Zone 3`
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
                                 'for field `total_insulated_surface_area_facing_zone_3`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `total_insulated_surface_area_facing_zone_3`')
        self._data["Total Insulated Surface Area Facing Zone 3"] = value

    @property
    def insulated_surface_uvalue_facing_zone_3(self):
        """Get insulated_surface_uvalue_facing_zone_3

        Returns:
            float: the value of `insulated_surface_uvalue_facing_zone_3` or None if not set
        """
        return self._data["Insulated Surface U-Value Facing Zone 3"]

    @insulated_surface_uvalue_facing_zone_3.setter
    def insulated_surface_uvalue_facing_zone_3(self, value=0.3154):
        """  Corresponds to IDD Field `Insulated Surface U-Value Facing Zone 3`
        The default value corresponds to R18
        To convert other Archaic American R-values to U, divide 5.678 by the R-value
        Some examples:
        R15 is U 0.3785 W/m2-K
        R5 is U 1.136 W/m2-K

        Args:
            value (float): value for IDD Field `Insulated Surface U-Value Facing Zone 3`
                Units: W/m2-K
                Default value: 0.3154
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
                                 'for field `insulated_surface_uvalue_facing_zone_3`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `insulated_surface_uvalue_facing_zone_3`')
        self._data["Insulated Surface U-Value Facing Zone 3"] = value

    @property
    def area_of_glass_reach_in_doors_facing_zone_3(self):
        """Get area_of_glass_reach_in_doors_facing_zone_3

        Returns:
            float: the value of `area_of_glass_reach_in_doors_facing_zone_3` or None if not set
        """
        return self._data["Area of Glass Reach In Doors Facing Zone 3"]

    @area_of_glass_reach_in_doors_facing_zone_3.setter
    def area_of_glass_reach_in_doors_facing_zone_3(self, value=0.0):
        """  Corresponds to IDD Field `Area of Glass Reach In Doors Facing Zone 3`

        Args:
            value (float): value for IDD Field `Area of Glass Reach In Doors Facing Zone 3`
                Units: m2
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
                                 'for field `area_of_glass_reach_in_doors_facing_zone_3`'.format(value))
        self._data["Area of Glass Reach In Doors Facing Zone 3"] = value

    @property
    def height_of_glass_reach_in_doors_facing_zone_3(self):
        """Get height_of_glass_reach_in_doors_facing_zone_3

        Returns:
            float: the value of `height_of_glass_reach_in_doors_facing_zone_3` or None if not set
        """
        return self._data["Height of Glass Reach In Doors Facing Zone 3"]

    @height_of_glass_reach_in_doors_facing_zone_3.setter
    def height_of_glass_reach_in_doors_facing_zone_3(self, value=1.5):
        """  Corresponds to IDD Field `Height of Glass Reach In Doors Facing Zone 3`

        Args:
            value (float): value for IDD Field `Height of Glass Reach In Doors Facing Zone 3`
                Units: m
                Default value: 1.5
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
                                 'for field `height_of_glass_reach_in_doors_facing_zone_3`'.format(value))
        self._data["Height of Glass Reach In Doors Facing Zone 3"] = value

    @property
    def glass_reach_in_door_u_value_facing_zone_3(self):
        """Get glass_reach_in_door_u_value_facing_zone_3

        Returns:
            float: the value of `glass_reach_in_door_u_value_facing_zone_3` or None if not set
        """
        return self._data["Glass Reach In Door U Value Facing Zone 3"]

    @glass_reach_in_door_u_value_facing_zone_3.setter
    def glass_reach_in_door_u_value_facing_zone_3(self, value=1.136):
        """  Corresponds to IDD Field `Glass Reach In Door U Value Facing Zone 3`
        The default value corresponds to R5
        To convert other Archaic American R-values to U, divide 5.678 by the R-value

        Args:
            value (float): value for IDD Field `Glass Reach In Door U Value Facing Zone 3`
                Units: W/m2-K
                Default value: 1.136
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
                                 'for field `glass_reach_in_door_u_value_facing_zone_3`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `glass_reach_in_door_u_value_facing_zone_3`')
        self._data["Glass Reach In Door U Value Facing Zone 3"] = value

    @property
    def glass_reach_in_door_opening_schedule_name_facing_zone_3(self):
        """Get glass_reach_in_door_opening_schedule_name_facing_zone_3

        Returns:
            str: the value of `glass_reach_in_door_opening_schedule_name_facing_zone_3` or None if not set
        """
        return self._data["Glass Reach In Door Opening Schedule Name Facing Zone 3"]

    @glass_reach_in_door_opening_schedule_name_facing_zone_3.setter
    def glass_reach_in_door_opening_schedule_name_facing_zone_3(self, value=None):
        """  Corresponds to IDD Field `Glass Reach In Door Opening Schedule Name Facing Zone 3`
        Schedule values should all be between 0.0 and 1.0.
        For example, if the door is open 30% of the time during working hours,
        then the schedule would hold the value 0.3 during working hours
        and 0 during other hours
        If no schedule name is entered, default is 5% open time during all hours

        Args:
            value (str): value for IDD Field `Glass Reach In Door Opening Schedule Name Facing Zone 3`
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
                                 'for field `glass_reach_in_door_opening_schedule_name_facing_zone_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `glass_reach_in_door_opening_schedule_name_facing_zone_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `glass_reach_in_door_opening_schedule_name_facing_zone_3`')
        self._data["Glass Reach In Door Opening Schedule Name Facing Zone 3"] = value

    @property
    def area_of_stocking_doors_facing_zone_3(self):
        """Get area_of_stocking_doors_facing_zone_3

        Returns:
            float: the value of `area_of_stocking_doors_facing_zone_3` or None if not set
        """
        return self._data["Area of Stocking Doors Facing Zone 3"]

    @area_of_stocking_doors_facing_zone_3.setter
    def area_of_stocking_doors_facing_zone_3(self, value=0.0):
        """  Corresponds to IDD Field `Area of Stocking Doors Facing Zone 3`

        Args:
            value (float): value for IDD Field `Area of Stocking Doors Facing Zone 3`
                Units: m2
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
                                 'for field `area_of_stocking_doors_facing_zone_3`'.format(value))
        self._data["Area of Stocking Doors Facing Zone 3"] = value

    @property
    def height_of_stocking_doors_facing_zone_3(self):
        """Get height_of_stocking_doors_facing_zone_3

        Returns:
            float: the value of `height_of_stocking_doors_facing_zone_3` or None if not set
        """
        return self._data["Height of Stocking Doors Facing Zone 3"]

    @height_of_stocking_doors_facing_zone_3.setter
    def height_of_stocking_doors_facing_zone_3(self, value=3.0):
        """  Corresponds to IDD Field `Height of Stocking Doors Facing Zone 3`

        Args:
            value (float): value for IDD Field `Height of Stocking Doors Facing Zone 3`
                Units: m
                Default value: 3.0
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
                                 'for field `height_of_stocking_doors_facing_zone_3`'.format(value))
        self._data["Height of Stocking Doors Facing Zone 3"] = value

    @property
    def stocking_door_u_value_facing_zone_3(self):
        """Get stocking_door_u_value_facing_zone_3

        Returns:
            float: the value of `stocking_door_u_value_facing_zone_3` or None if not set
        """
        return self._data["Stocking Door U Value Facing Zone 3"]

    @stocking_door_u_value_facing_zone_3.setter
    def stocking_door_u_value_facing_zone_3(self, value=0.3785):
        """  Corresponds to IDD Field `Stocking Door U Value Facing Zone 3`
        The default value corresponds to R15
        To convert other Archaic American R-values to U, divide 5.678 by the R-value
        Some examples:
        R5 is U 1.136 W/m2-K
        R18 is U 0.3154 W/m2-K

        Args:
            value (float): value for IDD Field `Stocking Door U Value Facing Zone 3`
                Units: W/m2-K
                Default value: 0.3785
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
                                 'for field `stocking_door_u_value_facing_zone_3`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `stocking_door_u_value_facing_zone_3`')
        self._data["Stocking Door U Value Facing Zone 3"] = value

    @property
    def stocking_door_opening_schedule_name_facing_zone_3(self):
        """Get stocking_door_opening_schedule_name_facing_zone_3

        Returns:
            str: the value of `stocking_door_opening_schedule_name_facing_zone_3` or None if not set
        """
        return self._data["Stocking Door Opening Schedule Name Facing Zone 3"]

    @stocking_door_opening_schedule_name_facing_zone_3.setter
    def stocking_door_opening_schedule_name_facing_zone_3(self, value=None):
        """  Corresponds to IDD Field `Stocking Door Opening Schedule Name Facing Zone 3`
        Schedule values should all be between 0.0 and 1.0.
        For example, if the door is open 30% of the time during working hours,
        then the schedule would hold the value 0.3 during working hours
        and 0 during other hours
        If no schedule name is entered, default is 5% open time during all hours

        Args:
            value (str): value for IDD Field `Stocking Door Opening Schedule Name Facing Zone 3`
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
                                 'for field `stocking_door_opening_schedule_name_facing_zone_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `stocking_door_opening_schedule_name_facing_zone_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `stocking_door_opening_schedule_name_facing_zone_3`')
        self._data["Stocking Door Opening Schedule Name Facing Zone 3"] = value

    @property
    def stocking_door_opening_protection_type_facing_zone_3(self):
        """Get stocking_door_opening_protection_type_facing_zone_3

        Returns:
            str: the value of `stocking_door_opening_protection_type_facing_zone_3` or None if not set
        """
        return self._data["Stocking Door Opening Protection Type Facing Zone 3"]

    @stocking_door_opening_protection_type_facing_zone_3.setter
    def stocking_door_opening_protection_type_facing_zone_3(self, value="AirCurtain"):
        """  Corresponds to IDD Field `Stocking Door Opening Protection Type Facing Zone 3`
        Use StripCurtain for hanging strips or airlock vestibules

        Args:
            value (str): value for IDD Field `Stocking Door Opening Protection Type Facing Zone 3`
                Accepted values are:
                      - None
                      - AirCurtain
                      - StripCurtain
                Default value: AirCurtain
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
                                 'for field `stocking_door_opening_protection_type_facing_zone_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `stocking_door_opening_protection_type_facing_zone_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `stocking_door_opening_protection_type_facing_zone_3`')
            vals = {}
            vals["none"] = "None"
            vals["aircurtain"] = "AirCurtain"
            vals["stripcurtain"] = "StripCurtain"
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
                                     'field `stocking_door_opening_protection_type_facing_zone_3`'.format(value))
            value = vals[value_lower]
        self._data["Stocking Door Opening Protection Type Facing Zone 3"] = value

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

class RefrigerationAirChiller(object):
    """ Corresponds to IDD object `Refrigeration:AirChiller`
        Works in conjunction with a refrigeration chiller set, compressor rack, a
        refrigeration system, or a refrigeration secondary system to simulate the performance
        of an air chiller, similar to one found in a refrigerated warehouse. Energy use for
        fans and heaters is modeled based on inputs for nominal power, schedules, and control
        type. The air chiller model accounts for the sensible and latent heat exchange
        with the surrounding environment.
    
    """
    internal_name = "Refrigeration:AirChiller"
    field_count = 28
    required_fields = ["Name", "Capacity Rating Type", "Rated Cooling Source Temperature", "Rated Temperature Difference DT1", "Rated Total Heating Power", "Rated Air Flow", "Defrost Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Refrigeration:AirChiller`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Capacity Rating Type"] = None
        self._data["Rated Unit Load Factor"] = None
        self._data["Rated Capacity"] = None
        self._data["Rated Relative Humidity"] = None
        self._data["Rated Cooling Source Temperature"] = None
        self._data["Rated Temperature Difference DT1"] = None
        self._data["Maximum Temperature Difference Between Inlet Air and Evaporating Temperature"] = None
        self._data["Coil Material Correction Factor"] = None
        self._data["Refrigerant Correction Factor"] = None
        self._data["Capacity Correction Curve Type"] = None
        self._data["Capacity Correction Curve Name"] = None
        self._data["SHR60 Correction Factor"] = None
        self._data["Rated Total Heating Power"] = None
        self._data["Heating Power Schedule Name"] = None
        self._data["Fan Speed Control Type"] = None
        self._data["Rated Fan Power"] = None
        self._data["Rated Air Flow"] = None
        self._data["Minimum Fan Air Flow Ratio"] = None
        self._data["Defrost Type"] = None
        self._data["Defrost Control Type"] = None
        self._data["Defrost Schedule Name"] = None
        self._data["Defrost Drip-Down Schedule Name"] = None
        self._data["Defrost Power"] = None
        self._data["Temperature Termination Defrost Fraction to Ice"] = None
        self._data["Vertical Location"] = None
        self._data["Average Refrigerant Charge Inventory"] = None
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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.capacity_rating_type = None
        else:
            self.capacity_rating_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_unit_load_factor = None
        else:
            self.rated_unit_load_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_capacity = None
        else:
            self.rated_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_relative_humidity = None
        else:
            self.rated_relative_humidity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_cooling_source_temperature = None
        else:
            self.rated_cooling_source_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_temperature_difference_dt1 = None
        else:
            self.rated_temperature_difference_dt1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_temperature_difference_between_inlet_air_and_evaporating_temperature = None
        else:
            self.maximum_temperature_difference_between_inlet_air_and_evaporating_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coil_material_correction_factor = None
        else:
            self.coil_material_correction_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refrigerant_correction_factor = None
        else:
            self.refrigerant_correction_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.capacity_correction_curve_type = None
        else:
            self.capacity_correction_curve_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.capacity_correction_curve_name = None
        else:
            self.capacity_correction_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shr60_correction_factor = None
        else:
            self.shr60_correction_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_total_heating_power = None
        else:
            self.rated_total_heating_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_power_schedule_name = None
        else:
            self.heating_power_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_speed_control_type = None
        else:
            self.fan_speed_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_fan_power = None
        else:
            self.rated_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_air_flow = None
        else:
            self.rated_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_fan_air_flow_ratio = None
        else:
            self.minimum_fan_air_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_type = None
        else:
            self.defrost_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_control_type = None
        else:
            self.defrost_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_schedule_name = None
        else:
            self.defrost_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_dripdown_schedule_name = None
        else:
            self.defrost_dripdown_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_power = None
        else:
            self.defrost_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_termination_defrost_fraction_to_ice = None
        else:
            self.temperature_termination_defrost_fraction_to_ice = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertical_location = None
        else:
            self.vertical_location = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.average_refrigerant_charge_inventory = None
        else:
            self.average_refrigerant_charge_inventory = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
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
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def capacity_rating_type(self):
        """Get capacity_rating_type

        Returns:
            str: the value of `capacity_rating_type` or None if not set
        """
        return self._data["Capacity Rating Type"]

    @capacity_rating_type.setter
    def capacity_rating_type(self, value=None):
        """  Corresponds to IDD Field `Capacity Rating Type`
        In each case, select the rating option that corresponds to the expected service conditions.
        For example, U.S. manufacturers quote a separate Unit Load Factor for wet or frosted coils.
        If the evaporating temperature is less than 0C, input the frosted coil value.
        Within the European convention, select SC1, 2, 3, 4, or 5 depending upon the expected evaporating temperature.        \type choice

        Args:
            value (str): value for IDD Field `Capacity Rating Type`
                Accepted values are:
                      - UnitLoadFactorSensibleOnly
                      - CapacityTotalSpecificConditions
                      - EuropeanSC1Standard
                      - EuropeanSC1NominalWet
                      - EuropeanSC2Standard
                      - EuropeanSC2NominalWet
                      - EuropeanSC3Standard
                      - FixedLinear
                      - EuropeanSC3NominalWet
                      - EuropeanSC4Standard
                      - EuropeanSC4NominalWet
                      - EuropeanSC5Standard
                      - EuropeanSC5NominalWet
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
                                 'for field `capacity_rating_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_rating_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `capacity_rating_type`')
            vals = {}
            vals["unitloadfactorsensibleonly"] = "UnitLoadFactorSensibleOnly"
            vals["capacitytotalspecificconditions"] = "CapacityTotalSpecificConditions"
            vals["europeansc1standard"] = "EuropeanSC1Standard"
            vals["europeansc1nominalwet"] = "EuropeanSC1NominalWet"
            vals["europeansc2standard"] = "EuropeanSC2Standard"
            vals["europeansc2nominalwet"] = "EuropeanSC2NominalWet"
            vals["europeansc3standard"] = "EuropeanSC3Standard"
            vals["fixedlinear"] = "FixedLinear"
            vals["europeansc3nominalwet"] = "EuropeanSC3NominalWet"
            vals["europeansc4standard"] = "EuropeanSC4Standard"
            vals["europeansc4nominalwet"] = "EuropeanSC4NominalWet"
            vals["europeansc5standard"] = "EuropeanSC5Standard"
            vals["europeansc5nominalwet"] = "EuropeanSC5NominalWet"
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
                                     'field `capacity_rating_type`'.format(value))
            value = vals[value_lower]
        self._data["Capacity Rating Type"] = value

    @property
    def rated_unit_load_factor(self):
        """Get rated_unit_load_factor

        Returns:
            float: the value of `rated_unit_load_factor` or None if not set
        """
        return self._data["Rated Unit Load Factor"]

    @rated_unit_load_factor.setter
    def rated_unit_load_factor(self, value=None):
        """  Corresponds to IDD Field `Rated Unit Load Factor`
        The sensible cooling capacity in watts (W/C) at rated conditions.
        The value entered for this field must be greater than zero, with no default value.
        This value is only used if the Capacity Rating Type is UnitLoadFactorSensibleOnly.
        The value given must be based upon the difference between the chiller inlet and
        outlet air temperatures, not on the difference between the zone mean temperature
        and the outlet air temperature

        Args:
            value (float): value for IDD Field `Rated Unit Load Factor`
                Units: W/K
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
                                 'for field `rated_unit_load_factor`'.format(value))
        self._data["Rated Unit Load Factor"] = value

    @property
    def rated_capacity(self):
        """Get rated_capacity

        Returns:
            float: the value of `rated_capacity` or None if not set
        """
        return self._data["Rated Capacity"]

    @rated_capacity.setter
    def rated_capacity(self, value=None):
        """  Corresponds to IDD Field `Rated Capacity`
        This value is only used if the Capacity Rating Type is NOT UnitLoadFactorSensibleOnly.
        For CapacityTotalSpecificConditions, this capacity includes both sensible and latent
        at the conditions given in the next two fields.
        Note that the European Standard ratings are sensible only and
        the European Nominal ratings include latent capacity as well.
        The value given here must correspond to the capacity rating type given previously

        Args:
            value (float): value for IDD Field `Rated Capacity`
                Units: W
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
                                 'for field `rated_capacity`'.format(value))
        self._data["Rated Capacity"] = value

    @property
    def rated_relative_humidity(self):
        """Get rated_relative_humidity

        Returns:
            float: the value of `rated_relative_humidity` or None if not set
        """
        return self._data["Rated Relative Humidity"]

    @rated_relative_humidity.setter
    def rated_relative_humidity(self, value=85.0):
        """  Corresponds to IDD Field `Rated Relative Humidity`
        This field is ONLY used if the Capacity Rating Type is CapacityTotalSpecificConditions and
        represents the relative humidity at rated conditions. The default is 85.

        Args:
            value (float): value for IDD Field `Rated Relative Humidity`
                Units: percent
                Default value: 85.0
                value <= 100.0
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
                                 'for field `rated_relative_humidity`'.format(value))
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `rated_relative_humidity`')
        self._data["Rated Relative Humidity"] = value

    @property
    def rated_cooling_source_temperature(self):
        """Get rated_cooling_source_temperature

        Returns:
            float: the value of `rated_cooling_source_temperature` or None if not set
        """
        return self._data["Rated Cooling Source Temperature"]

    @rated_cooling_source_temperature.setter
    def rated_cooling_source_temperature(self, value=None):
        """  Corresponds to IDD Field `Rated Cooling Source Temperature`
        If DXEvaporator, use evaporating temperature (saturated suction temperature)
        If BrineCoil, use Brine entering temperature
        used to set minimum suction pressure for DX systems and
        minimum brine temp for secondary systems

        Args:
            value (float): value for IDD Field `Rated Cooling Source Temperature`
                Units: C
                value >= -70.0
                value <= 40.0
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
                                 'for field `rated_cooling_source_temperature`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `rated_cooling_source_temperature`')
            if value > 40.0:
                raise ValueError('value need to be smaller 40.0 '
                                 'for field `rated_cooling_source_temperature`')
        self._data["Rated Cooling Source Temperature"] = value

    @property
    def rated_temperature_difference_dt1(self):
        """Get rated_temperature_difference_dt1

        Returns:
            float: the value of `rated_temperature_difference_dt1` or None if not set
        """
        return self._data["Rated Temperature Difference DT1"]

    @rated_temperature_difference_dt1.setter
    def rated_temperature_difference_dt1(self, value=None):
        """  Corresponds to IDD Field `Rated Temperature Difference DT1`
        The rated difference between the air entering the refrigeration chiller and the
        cooling source temperature in C.

        Args:
            value (float): value for IDD Field `Rated Temperature Difference DT1`
                Units: deltaC
                value >= 0.0
                value <= 20.0
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
                                 'for field `rated_temperature_difference_dt1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_temperature_difference_dt1`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `rated_temperature_difference_dt1`')
        self._data["Rated Temperature Difference DT1"] = value

    @property
    def maximum_temperature_difference_between_inlet_air_and_evaporating_temperature(self):
        """Get maximum_temperature_difference_between_inlet_air_and_evaporating_temperature

        Returns:
            float: the value of `maximum_temperature_difference_between_inlet_air_and_evaporating_temperature` or None if not set
        """
        return self._data["Maximum Temperature Difference Between Inlet Air and Evaporating Temperature"]

    @maximum_temperature_difference_between_inlet_air_and_evaporating_temperature.setter
    def maximum_temperature_difference_between_inlet_air_and_evaporating_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Temperature Difference Between Inlet Air and Evaporating Temperature`
        The maximum difference between the air entering the refrigeration chiller and the
        cooling source temperature in C used to limit capacity during pull-down.
        defaults to 1.3 times the Rated Temperature Difference DT1

        Args:
            value (float): value for IDD Field `Maximum Temperature Difference Between Inlet Air and Evaporating Temperature`
                Units: deltaC
                value >= 0.0
                value <= 25.0
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
                                 'for field `maximum_temperature_difference_between_inlet_air_and_evaporating_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_temperature_difference_between_inlet_air_and_evaporating_temperature`')
            if value > 25.0:
                raise ValueError('value need to be smaller 25.0 '
                                 'for field `maximum_temperature_difference_between_inlet_air_and_evaporating_temperature`')
        self._data["Maximum Temperature Difference Between Inlet Air and Evaporating Temperature"] = value

    @property
    def coil_material_correction_factor(self):
        """Get coil_material_correction_factor

        Returns:
            float: the value of `coil_material_correction_factor` or None if not set
        """
        return self._data["Coil Material Correction Factor"]

    @coil_material_correction_factor.setter
    def coil_material_correction_factor(self, value=1.0):
        """  Corresponds to IDD Field `Coil Material Correction Factor`
        This is the manufacturer's correction factor for coil material corresponding to rating

        Args:
            value (float): value for IDD Field `Coil Material Correction Factor`
                Units: dimensionless
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
                                 'for field `coil_material_correction_factor`'.format(value))
        self._data["Coil Material Correction Factor"] = value

    @property
    def refrigerant_correction_factor(self):
        """Get refrigerant_correction_factor

        Returns:
            float: the value of `refrigerant_correction_factor` or None if not set
        """
        return self._data["Refrigerant Correction Factor"]

    @refrigerant_correction_factor.setter
    def refrigerant_correction_factor(self, value=1.0):
        """  Corresponds to IDD Field `Refrigerant Correction Factor`
        This is the manufacturer's correction factor for refrigerant corresponding to rating

        Args:
            value (float): value for IDD Field `Refrigerant Correction Factor`
                Units: dimensionless
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
                                 'for field `refrigerant_correction_factor`'.format(value))
        self._data["Refrigerant Correction Factor"] = value

    @property
    def capacity_correction_curve_type(self):
        """Get capacity_correction_curve_type

        Returns:
            str: the value of `capacity_correction_curve_type` or None if not set
        """
        return self._data["Capacity Correction Curve Type"]

    @capacity_correction_curve_type.setter
    def capacity_correction_curve_type(self, value=None):
        """  Corresponds to IDD Field `Capacity Correction Curve Type`
        In each case, select the correction curve type that corresponds to the rating type.
        default LinearSHR60 unless Capcity Rating Type = CapacityTotalSpecificConditions

        Args:
            value (str): value for IDD Field `Capacity Correction Curve Type`
                Accepted values are:
                      - LinearSHR60
                      - QuadraticSHR
                      - European
                      - TabularRHxDT1xTRoom
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
                                 'for field `capacity_correction_curve_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_correction_curve_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `capacity_correction_curve_type`')
            vals = {}
            vals["linearshr60"] = "LinearSHR60"
            vals["quadraticshr"] = "QuadraticSHR"
            vals["european"] = "European"
            vals["tabularrhxdt1xtroom"] = "TabularRHxDT1xTRoom"
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
                                     'field `capacity_correction_curve_type`'.format(value))
            value = vals[value_lower]
        self._data["Capacity Correction Curve Type"] = value

    @property
    def capacity_correction_curve_name(self):
        """Get capacity_correction_curve_name

        Returns:
            str: the value of `capacity_correction_curve_name` or None if not set
        """
        return self._data["Capacity Correction Curve Name"]

    @capacity_correction_curve_name.setter
    def capacity_correction_curve_name(self, value=None):
        """  Corresponds to IDD Field `Capacity Correction Curve Name`
        Table:OneIndependentVariable object can also be used
        Can also be the name of a "Table:OneIndependentVariable" or a "Table:MultiVariableLookup"
        Should be blank for LinearSHR60 correction curve type

        Args:
            value (str): value for IDD Field `Capacity Correction Curve Name`
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
                                 'for field `capacity_correction_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_correction_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `capacity_correction_curve_name`')
        self._data["Capacity Correction Curve Name"] = value

    @property
    def shr60_correction_factor(self):
        """Get shr60_correction_factor

        Returns:
            float: the value of `shr60_correction_factor` or None if not set
        """
        return self._data["SHR60 Correction Factor"]

    @shr60_correction_factor.setter
    def shr60_correction_factor(self, value=1.48):
        """  Corresponds to IDD Field `SHR60 Correction Factor`
        only used when the capacity correction curve type is LinearSHR60

        Args:
            value (float): value for IDD Field `SHR60 Correction Factor`
                Units: dimensionless
                Default value: 1.48
                value <= 1.67
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
                                 'for field `shr60_correction_factor`'.format(value))
            if value > 1.67:
                raise ValueError('value need to be smaller 1.67 '
                                 'for field `shr60_correction_factor`')
        self._data["SHR60 Correction Factor"] = value

    @property
    def rated_total_heating_power(self):
        """Get rated_total_heating_power

        Returns:
            float: the value of `rated_total_heating_power` or None if not set
        """
        return self._data["Rated Total Heating Power"]

    @rated_total_heating_power.setter
    def rated_total_heating_power(self, value=None):
        """  Corresponds to IDD Field `Rated Total Heating Power`
        Include total for all heater power
        Do not include defrost heater power

        Args:
            value (float): value for IDD Field `Rated Total Heating Power`
                Units: W
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
                                 'for field `rated_total_heating_power`'.format(value))
        self._data["Rated Total Heating Power"] = value

    @property
    def heating_power_schedule_name(self):
        """Get heating_power_schedule_name

        Returns:
            str: the value of `heating_power_schedule_name` or None if not set
        """
        return self._data["Heating Power Schedule Name"]

    @heating_power_schedule_name.setter
    def heating_power_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Power Schedule Name`
        Values will be used to multiply the total heating power
        Values in the schedule should be between 0.0 and 1.0
        Defaults to always on if schedule name left blank.

        Args:
            value (str): value for IDD Field `Heating Power Schedule Name`
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
                                 'for field `heating_power_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_power_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_power_schedule_name`')
        self._data["Heating Power Schedule Name"] = value

    @property
    def fan_speed_control_type(self):
        """Get fan_speed_control_type

        Returns:
            str: the value of `fan_speed_control_type` or None if not set
        """
        return self._data["Fan Speed Control Type"]

    @fan_speed_control_type.setter
    def fan_speed_control_type(self, value="Fixed"):
        """  Corresponds to IDD Field `Fan Speed Control Type`

        Args:
            value (str): value for IDD Field `Fan Speed Control Type`
                Accepted values are:
                      - Fixed
                      - FixedLinear
                      - VariableSpeed
                      - TwoSpeed
                Default value: Fixed
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
                                 'for field `fan_speed_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_speed_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_speed_control_type`')
            vals = {}
            vals["fixed"] = "Fixed"
            vals["fixedlinear"] = "FixedLinear"
            vals["variablespeed"] = "VariableSpeed"
            vals["twospeed"] = "TwoSpeed"
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
                                     'field `fan_speed_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Fan Speed Control Type"] = value

    @property
    def rated_fan_power(self):
        """Get rated_fan_power

        Returns:
            float: the value of `rated_fan_power` or None if not set
        """
        return self._data["Rated Fan Power"]

    @rated_fan_power.setter
    def rated_fan_power(self, value=375.0):
        """  Corresponds to IDD Field `Rated Fan Power`

        Args:
            value (float): value for IDD Field `Rated Fan Power`
                Units: W
                Default value: 375.0
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
                                 'for field `rated_fan_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_fan_power`')
        self._data["Rated Fan Power"] = value

    @property
    def rated_air_flow(self):
        """Get rated_air_flow

        Returns:
            float: the value of `rated_air_flow` or None if not set
        """
        return self._data["Rated Air Flow"]

    @rated_air_flow.setter
    def rated_air_flow(self, value=None):
        """  Corresponds to IDD Field `Rated Air Flow`

        Args:
            value (float): value for IDD Field `Rated Air Flow`
                Units: m3/s
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
                                 'for field `rated_air_flow`'.format(value))
        self._data["Rated Air Flow"] = value

    @property
    def minimum_fan_air_flow_ratio(self):
        """Get minimum_fan_air_flow_ratio

        Returns:
            float: the value of `minimum_fan_air_flow_ratio` or None if not set
        """
        return self._data["Minimum Fan Air Flow Ratio"]

    @minimum_fan_air_flow_ratio.setter
    def minimum_fan_air_flow_ratio(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Fan Air Flow Ratio`
        Minimum air flow fraction through fan

        Args:
            value (float): value for IDD Field `Minimum Fan Air Flow Ratio`
                Units: dimensionless
                Default value: 0.2
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
                                 'for field `minimum_fan_air_flow_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_fan_air_flow_ratio`')
        self._data["Minimum Fan Air Flow Ratio"] = value

    @property
    def defrost_type(self):
        """Get defrost_type

        Returns:
            str: the value of `defrost_type` or None if not set
        """
        return self._data["Defrost Type"]

    @defrost_type.setter
    def defrost_type(self, value="Electric"):
        """  Corresponds to IDD Field `Defrost Type`
        HotFluid includes either hot gas defrost for a DX system or
        Hot Brine defrost if this walk in is cooled by brine from a secondary chiller

        Args:
            value (str): value for IDD Field `Defrost Type`
                Accepted values are:
                      - HotFluid
                      - Electric
                      - None
                      - OffCycle
                Default value: Electric
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
                                 'for field `defrost_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_type`')
            vals = {}
            vals["hotfluid"] = "HotFluid"
            vals["electric"] = "Electric"
            vals["none"] = "None"
            vals["offcycle"] = "OffCycle"
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
                                     'field `defrost_type`'.format(value))
            value = vals[value_lower]
        self._data["Defrost Type"] = value

    @property
    def defrost_control_type(self):
        """Get defrost_control_type

        Returns:
            str: the value of `defrost_control_type` or None if not set
        """
        return self._data["Defrost Control Type"]

    @defrost_control_type.setter
    def defrost_control_type(self, value="TimeSchedule"):
        """  Corresponds to IDD Field `Defrost Control Type`

        Args:
            value (str): value for IDD Field `Defrost Control Type`
                Accepted values are:
                      - TimeSchedule
                      - TemperatureTermination
                Default value: TimeSchedule
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
                                 'for field `defrost_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_control_type`')
            vals = {}
            vals["timeschedule"] = "TimeSchedule"
            vals["temperaturetermination"] = "TemperatureTermination"
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
                                     'field `defrost_control_type`'.format(value))
            value = vals[value_lower]
        self._data["Defrost Control Type"] = value

    @property
    def defrost_schedule_name(self):
        """Get defrost_schedule_name

        Returns:
            str: the value of `defrost_schedule_name` or None if not set
        """
        return self._data["Defrost Schedule Name"]

    @defrost_schedule_name.setter
    def defrost_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Defrost Schedule Name`
        The schedule values should be 0 (off) or 1 (on)

        Args:
            value (str): value for IDD Field `Defrost Schedule Name`
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
                                 'for field `defrost_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_schedule_name`')
        self._data["Defrost Schedule Name"] = value

    @property
    def defrost_dripdown_schedule_name(self):
        """Get defrost_dripdown_schedule_name

        Returns:
            str: the value of `defrost_dripdown_schedule_name` or None if not set
        """
        return self._data["Defrost Drip-Down Schedule Name"]

    @defrost_dripdown_schedule_name.setter
    def defrost_dripdown_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Defrost Drip-Down Schedule Name`
        The schedule values should be 0 (off) or 1 (on)
        The start time for each defrost period in this drip-down schedule should coincide with
        the start time for each defrost period in the defrost schedule (previous input
        field).The length of each defrost drip-down period must be greater than or equal to the
        corresponding defrost period specified in the defrost schedule. This extra time
        allows the melted frost to drip from the coil before refrigeration is restarted.

        Args:
            value (str): value for IDD Field `Defrost Drip-Down Schedule Name`
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
                                 'for field `defrost_dripdown_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_dripdown_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_dripdown_schedule_name`')
        self._data["Defrost Drip-Down Schedule Name"] = value

    @property
    def defrost_power(self):
        """Get defrost_power

        Returns:
            float: the value of `defrost_power` or None if not set
        """
        return self._data["Defrost Power"]

    @defrost_power.setter
    def defrost_power(self, value=None):
        """  Corresponds to IDD Field `Defrost Power`
        needed for all defrost types except none and offcycle

        Args:
            value (float): value for IDD Field `Defrost Power`
                Units: W
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
                                 'for field `defrost_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `defrost_power`')
        self._data["Defrost Power"] = value

    @property
    def temperature_termination_defrost_fraction_to_ice(self):
        """Get temperature_termination_defrost_fraction_to_ice

        Returns:
            float: the value of `temperature_termination_defrost_fraction_to_ice` or None if not set
        """
        return self._data["Temperature Termination Defrost Fraction to Ice"]

    @temperature_termination_defrost_fraction_to_ice.setter
    def temperature_termination_defrost_fraction_to_ice(self, value=None):
        """  Corresponds to IDD Field `Temperature Termination Defrost Fraction to Ice`
        This is the portion of the defrost energy that is available to melt frost
        Needed only for defrost control type TemperatureTermination
        defaults to 0.7 for electric defrost and to 0.3 for hot fluid defrost

        Args:
            value (float): value for IDD Field `Temperature Termination Defrost Fraction to Ice`
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
                                 'for field `temperature_termination_defrost_fraction_to_ice`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `temperature_termination_defrost_fraction_to_ice`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `temperature_termination_defrost_fraction_to_ice`')
        self._data["Temperature Termination Defrost Fraction to Ice"] = value

    @property
    def vertical_location(self):
        """Get vertical_location

        Returns:
            str: the value of `vertical_location` or None if not set
        """
        return self._data["Vertical Location"]

    @vertical_location.setter
    def vertical_location(self, value="Middle"):
        """  Corresponds to IDD Field `Vertical Location`

        Args:
            value (str): value for IDD Field `Vertical Location`
                Accepted values are:
                      - Ceiling
                      - Middle
                      - Floor
                Default value: Middle
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
                                 'for field `vertical_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `vertical_location`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `vertical_location`')
            vals = {}
            vals["ceiling"] = "Ceiling"
            vals["middle"] = "Middle"
            vals["floor"] = "Floor"
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
                                     'field `vertical_location`'.format(value))
            value = vals[value_lower]
        self._data["Vertical Location"] = value

    @property
    def average_refrigerant_charge_inventory(self):
        """Get average_refrigerant_charge_inventory

        Returns:
            float: the value of `average_refrigerant_charge_inventory` or None if not set
        """
        return self._data["Average Refrigerant Charge Inventory"]

    @average_refrigerant_charge_inventory.setter
    def average_refrigerant_charge_inventory(self, value=0.0):
        """  Corresponds to IDD Field `Average Refrigerant Charge Inventory`
        This value is only used if the Cooling Source Type is DXEvaporator

        Args:
            value (float): value for IDD Field `Average Refrigerant Charge Inventory`
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
                                 'for field `average_refrigerant_charge_inventory`'.format(value))
        self._data["Average Refrigerant Charge Inventory"] = value

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