from collections import OrderedDict

class RoomAirSettingsOneNodeDisplacementVentilation(object):
    """ Corresponds to IDD object `RoomAirSettings:OneNodeDisplacementVentilation`
        The Mundt model for displacement ventilation
    """
    internal_name = "RoomAirSettings:OneNodeDisplacementVentilation"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAirSettings:OneNodeDisplacementVentilation`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Fraction of Convective Internal Loads Added to Floor Air"] = None
        self._data["Fraction of Infiltration Internal Loads Added to Floor Air"] = None

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
            self.fraction_of_convective_internal_loads_added_to_floor_air = None
        else:
            self.fraction_of_convective_internal_loads_added_to_floor_air = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_infiltration_internal_loads_added_to_floor_air = None
        else:
            self.fraction_of_infiltration_internal_loads_added_to_floor_air = vals[i]
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
    def fraction_of_convective_internal_loads_added_to_floor_air(self):
        """Get fraction_of_convective_internal_loads_added_to_floor_air

        Returns:
            float: the value of `fraction_of_convective_internal_loads_added_to_floor_air` or None if not set
        """
        return self._data["Fraction of Convective Internal Loads Added to Floor Air"]

    @fraction_of_convective_internal_loads_added_to_floor_air.setter
    def fraction_of_convective_internal_loads_added_to_floor_air(self, value=None):
        """  Corresponds to IDD Field `fraction_of_convective_internal_loads_added_to_floor_air`

        Args:
            value (float): value for IDD Field `fraction_of_convective_internal_loads_added_to_floor_air`
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
                                 'for field `fraction_of_convective_internal_loads_added_to_floor_air`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_convective_internal_loads_added_to_floor_air`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_convective_internal_loads_added_to_floor_air`')

        self._data["Fraction of Convective Internal Loads Added to Floor Air"] = value

    @property
    def fraction_of_infiltration_internal_loads_added_to_floor_air(self):
        """Get fraction_of_infiltration_internal_loads_added_to_floor_air

        Returns:
            float: the value of `fraction_of_infiltration_internal_loads_added_to_floor_air` or None if not set
        """
        return self._data["Fraction of Infiltration Internal Loads Added to Floor Air"]

    @fraction_of_infiltration_internal_loads_added_to_floor_air.setter
    def fraction_of_infiltration_internal_loads_added_to_floor_air(self, value=None):
        """  Corresponds to IDD Field `fraction_of_infiltration_internal_loads_added_to_floor_air`

        Args:
            value (float): value for IDD Field `fraction_of_infiltration_internal_loads_added_to_floor_air`
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
                                 'for field `fraction_of_infiltration_internal_loads_added_to_floor_air`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_infiltration_internal_loads_added_to_floor_air`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_infiltration_internal_loads_added_to_floor_air`')

        self._data["Fraction of Infiltration Internal Loads Added to Floor Air"] = value

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
        out.append(self._to_str(self.fraction_of_convective_internal_loads_added_to_floor_air))
        out.append(self._to_str(self.fraction_of_infiltration_internal_loads_added_to_floor_air))
        return ",".join(out)

class RoomAirSettingsThreeNodeDisplacementVentilation(object):
    """ Corresponds to IDD object `RoomAirSettings:ThreeNodeDisplacementVentilation`
        The UCSD model for Displacement Ventilation
    """
    internal_name = "RoomAirSettings:ThreeNodeDisplacementVentilation"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAirSettings:ThreeNodeDisplacementVentilation`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Gain Distribution Schedule Name"] = None
        self._data["Number of Plumes per Occupant"] = None
        self._data["Thermostat Height"] = None
        self._data["Comfort Height"] = None
        self._data["Temperature Difference Threshold for Reporting"] = None

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
            self.gain_distribution_schedule_name = None
        else:
            self.gain_distribution_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_plumes_per_occupant = None
        else:
            self.number_of_plumes_per_occupant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_height = None
        else:
            self.thermostat_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.comfort_height = None
        else:
            self.comfort_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_difference_threshold_for_reporting = None
        else:
            self.temperature_difference_threshold_for_reporting = vals[i]
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
        Name of Zone being described. Any existing zone name

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
    def gain_distribution_schedule_name(self):
        """Get gain_distribution_schedule_name

        Returns:
            str: the value of `gain_distribution_schedule_name` or None if not set
        """
        return self._data["Gain Distribution Schedule Name"]

    @gain_distribution_schedule_name.setter
    def gain_distribution_schedule_name(self, value=None):
        """  Corresponds to IDD Field `gain_distribution_schedule_name`
        Distribution of the convective heat gains between the occupied and mixed zones.
        0<= Accepted Value <= 1.
        In the DV model 1 means all convective gains in the lower layer.

        Args:
            value (str): value for IDD Field `gain_distribution_schedule_name`
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
                                 'for field `gain_distribution_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gain_distribution_schedule_name`')

        self._data["Gain Distribution Schedule Name"] = value

    @property
    def number_of_plumes_per_occupant(self):
        """Get number_of_plumes_per_occupant

        Returns:
            float: the value of `number_of_plumes_per_occupant` or None if not set
        """
        return self._data["Number of Plumes per Occupant"]

    @number_of_plumes_per_occupant.setter
    def number_of_plumes_per_occupant(self, value=1.0 ):
        """  Corresponds to IDD Field `number_of_plumes_per_occupant`
        Used only in the UCSD displacement ventilation model.
        Effective number of separate plumes per occupant in the occupied zone.
        Plumes that merge together in the occupied zone count as one.

        Args:
            value (float): value for IDD Field `number_of_plumes_per_occupant`
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
                                 'for field `number_of_plumes_per_occupant`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `number_of_plumes_per_occupant`')

        self._data["Number of Plumes per Occupant"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self._data["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=1.1 ):
        """  Corresponds to IDD Field `thermostat_height`
        Height of thermostat/temperature control sensor above floor

        Args:
            value (float): value for IDD Field `thermostat_height`
                Unit: m
                Default value: 1.1
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
                                 'for field `thermostat_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermostat_height`')

        self._data["Thermostat Height"] = value

    @property
    def comfort_height(self):
        """Get comfort_height

        Returns:
            float: the value of `comfort_height` or None if not set
        """
        return self._data["Comfort Height"]

    @comfort_height.setter
    def comfort_height(self, value=1.1 ):
        """  Corresponds to IDD Field `comfort_height`
        Height at which air temperature is calculated for comfort purposes

        Args:
            value (float): value for IDD Field `comfort_height`
                Unit: m
                Default value: 1.1
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
                                 'for field `comfort_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `comfort_height`')

        self._data["Comfort Height"] = value

    @property
    def temperature_difference_threshold_for_reporting(self):
        """Get temperature_difference_threshold_for_reporting

        Returns:
            float: the value of `temperature_difference_threshold_for_reporting` or None if not set
        """
        return self._data["Temperature Difference Threshold for Reporting"]

    @temperature_difference_threshold_for_reporting.setter
    def temperature_difference_threshold_for_reporting(self, value=0.4 ):
        """  Corresponds to IDD Field `temperature_difference_threshold_for_reporting`
        Minimum temperature difference between predicted upper and lower layer
        temperatures above which DV auxilliary outputs are calculated.
        These outputs are 'DV Transition Height', 'DV Fraction Min Recommended Flow Rate'
        'DV Average Temp Gradient' and 'DV Maximum Temp Gradient'.  They
        are set to negative values when the temperature difference is less than the
        threshold and the output 'DV Zone Is Mixed' is set to 1

        Args:
            value (float): value for IDD Field `temperature_difference_threshold_for_reporting`
                Unit: deltaC
                Default value: 0.4
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
                                 'for field `temperature_difference_threshold_for_reporting`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `temperature_difference_threshold_for_reporting`')

        self._data["Temperature Difference Threshold for Reporting"] = value

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
        out.append(self._to_str(self.gain_distribution_schedule_name))
        out.append(self._to_str(self.number_of_plumes_per_occupant))
        out.append(self._to_str(self.thermostat_height))
        out.append(self._to_str(self.comfort_height))
        out.append(self._to_str(self.temperature_difference_threshold_for_reporting))
        return ",".join(out)

class RoomAirSettingsCrossVentilation(object):
    """ Corresponds to IDD object `RoomAirSettings:CrossVentilation`
        This UCSD Cross Ventilation Room Air Model provides a simple model for heat transfer
        and vertical temperature profile prediction in cross ventilated rooms. The model
        distinguishes two regions in the room, the main jet region and the recirculations,
        and predicts characteristic airflow velocities and average air temperatures.
        Used with RoomAirModelType = CrossVentilation.
    """
    internal_name = "RoomAirSettings:CrossVentilation"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAirSettings:CrossVentilation`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Gain Distribution Schedule Name"] = None
        self._data["Airflow Region Used for Thermal Comfort Evaluation"] = None

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
            self.gain_distribution_schedule_name = None
        else:
            self.gain_distribution_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airflow_region_used_for_thermal_comfort_evaluation = None
        else:
            self.airflow_region_used_for_thermal_comfort_evaluation = vals[i]
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
        Name of Zone being described. Any existing zone name

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
    def gain_distribution_schedule_name(self):
        """Get gain_distribution_schedule_name

        Returns:
            str: the value of `gain_distribution_schedule_name` or None if not set
        """
        return self._data["Gain Distribution Schedule Name"]

    @gain_distribution_schedule_name.setter
    def gain_distribution_schedule_name(self, value=None):
        """  Corresponds to IDD Field `gain_distribution_schedule_name`
        Distribution of the convective heat gains between the jet and recirculation zones.
        0<= Accepted Value <= 1.
        In the CV model 1 means all convective gains in the jet region.

        Args:
            value (str): value for IDD Field `gain_distribution_schedule_name`
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
                                 'for field `gain_distribution_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gain_distribution_schedule_name`')

        self._data["Gain Distribution Schedule Name"] = value

    @property
    def airflow_region_used_for_thermal_comfort_evaluation(self):
        """Get airflow_region_used_for_thermal_comfort_evaluation

        Returns:
            str: the value of `airflow_region_used_for_thermal_comfort_evaluation` or None if not set
        """
        return self._data["Airflow Region Used for Thermal Comfort Evaluation"]

    @airflow_region_used_for_thermal_comfort_evaluation.setter
    def airflow_region_used_for_thermal_comfort_evaluation(self, value=None):
        """  Corresponds to IDD Field `airflow_region_used_for_thermal_comfort_evaluation`
        Required field whenever thermal comfort is predicted
        defines Air temperature and Airflow velocity that will be used in the Fanger model
        conditions must refer to one of the two regions: jet or recirculation

        Args:
            value (str): value for IDD Field `airflow_region_used_for_thermal_comfort_evaluation`
                Accepted values are:
                      - Jet
                      - Recirculation
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
                                 'for field `airflow_region_used_for_thermal_comfort_evaluation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflow_region_used_for_thermal_comfort_evaluation`')
            vals = set()
            vals.add("Jet")
            vals.add("Recirculation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `airflow_region_used_for_thermal_comfort_evaluation`'.format(value))

        self._data["Airflow Region Used for Thermal Comfort Evaluation"] = value

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
        out.append(self._to_str(self.gain_distribution_schedule_name))
        out.append(self._to_str(self.airflow_region_used_for_thermal_comfort_evaluation))
        return ",".join(out)

class RoomAirSettingsUnderFloorAirDistributionInterior(object):
    """ Corresponds to IDD object `RoomAirSettings:UnderFloorAirDistributionInterior`
        This Room Air Model is applicable to interior spaces that are served by an underfloor
        air distribution system. The dominant sources of heat gain should be from people,
        equipment, and other localized sources located in the occupied part of the room.
        The model should be used with caution in zones which have large heat gains or losses
        through exterior walls or windows or which have considerable direct solar gain.
        Used with RoomAirModelType = UnderFloorAirDistributionInterior.
    """
    internal_name = "RoomAirSettings:UnderFloorAirDistributionInterior"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAirSettings:UnderFloorAirDistributionInterior`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Number of Diffusers"] = None
        self._data["Power per Plume"] = None
        self._data["Design Effective Area of Diffuser"] = None
        self._data["Diffuser Slot Angle from Vertical"] = None
        self._data["Thermostat Height"] = None
        self._data["Comfort Height"] = None
        self._data["Temperature Difference Threshold for Reporting"] = None
        self._data["Floor Diffuser Type"] = None
        self._data["Transition Height"] = None
        self._data["Coefficient A"] = None
        self._data["Coefficient B"] = None
        self._data["Coefficient C"] = None
        self._data["Coefficient D"] = None
        self._data["Coefficient E"] = None

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
            self.number_of_diffusers = None
        else:
            self.number_of_diffusers = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_plume = None
        else:
            self.power_per_plume = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_effective_area_of_diffuser = None
        else:
            self.design_effective_area_of_diffuser = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffuser_slot_angle_from_vertical = None
        else:
            self.diffuser_slot_angle_from_vertical = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_height = None
        else:
            self.thermostat_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.comfort_height = None
        else:
            self.comfort_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_difference_threshold_for_reporting = None
        else:
            self.temperature_difference_threshold_for_reporting = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_diffuser_type = None
        else:
            self.floor_diffuser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transition_height = None
        else:
            self.transition_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_a = None
        else:
            self.coefficient_a = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_b = None
        else:
            self.coefficient_b = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_c = None
        else:
            self.coefficient_c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_d = None
        else:
            self.coefficient_d = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_e = None
        else:
            self.coefficient_e = vals[i]
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
        Name of Zone with underfloor air distribution

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
    def number_of_diffusers(self):
        """Get number_of_diffusers

        Returns:
            float: the value of `number_of_diffusers` or None if not set
        """
        return self._data["Number of Diffusers"]

    @number_of_diffusers.setter
    def number_of_diffusers(self, value=None):
        """  Corresponds to IDD Field `number_of_diffusers`
        Total number of diffusers in this zone

        Args:
            value (float): value for IDD Field `number_of_diffusers`
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
                                 'for field `number_of_diffusers`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `number_of_diffusers`')

        self._data["Number of Diffusers"] = value

    @property
    def power_per_plume(self):
        """Get power_per_plume

        Returns:
            float: the value of `power_per_plume` or None if not set
        """
        return self._data["Power per Plume"]

    @power_per_plume.setter
    def power_per_plume(self, value=None):
        """  Corresponds to IDD Field `power_per_plume`

        Args:
            value (float): value for IDD Field `power_per_plume`
                Unit: W
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
                                 'for field `power_per_plume`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `power_per_plume`')

        self._data["Power per Plume"] = value

    @property
    def design_effective_area_of_diffuser(self):
        """Get design_effective_area_of_diffuser

        Returns:
            float: the value of `design_effective_area_of_diffuser` or None if not set
        """
        return self._data["Design Effective Area of Diffuser"]

    @design_effective_area_of_diffuser.setter
    def design_effective_area_of_diffuser(self, value=None):
        """  Corresponds to IDD Field `design_effective_area_of_diffuser`

        Args:
            value (float): value for IDD Field `design_effective_area_of_diffuser`
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
                                 'for field `design_effective_area_of_diffuser`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_effective_area_of_diffuser`')

        self._data["Design Effective Area of Diffuser"] = value

    @property
    def diffuser_slot_angle_from_vertical(self):
        """Get diffuser_slot_angle_from_vertical

        Returns:
            float: the value of `diffuser_slot_angle_from_vertical` or None if not set
        """
        return self._data["Diffuser Slot Angle from Vertical"]

    @diffuser_slot_angle_from_vertical.setter
    def diffuser_slot_angle_from_vertical(self, value=None):
        """  Corresponds to IDD Field `diffuser_slot_angle_from_vertical`

        Args:
            value (float): value for IDD Field `diffuser_slot_angle_from_vertical`
                Unit: deg
                value >= 0.0
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
                                 'for field `diffuser_slot_angle_from_vertical`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffuser_slot_angle_from_vertical`')
            if value > 90.0:
                raise ValueError('value need to be smaller 90.0 '
                                 'for field `diffuser_slot_angle_from_vertical`')

        self._data["Diffuser Slot Angle from Vertical"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self._data["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=1.2 ):
        """  Corresponds to IDD Field `thermostat_height`
        Height of thermostat/temperature control sensor above floor

        Args:
            value (float): value for IDD Field `thermostat_height`
                Unit: m
                Default value: 1.2
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
                                 'for field `thermostat_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermostat_height`')

        self._data["Thermostat Height"] = value

    @property
    def comfort_height(self):
        """Get comfort_height

        Returns:
            float: the value of `comfort_height` or None if not set
        """
        return self._data["Comfort Height"]

    @comfort_height.setter
    def comfort_height(self, value=1.1 ):
        """  Corresponds to IDD Field `comfort_height`
        Height at which air temperature is calculated for comfort purposes

        Args:
            value (float): value for IDD Field `comfort_height`
                Unit: m
                Default value: 1.1
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
                                 'for field `comfort_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `comfort_height`')

        self._data["Comfort Height"] = value

    @property
    def temperature_difference_threshold_for_reporting(self):
        """Get temperature_difference_threshold_for_reporting

        Returns:
            float: the value of `temperature_difference_threshold_for_reporting` or None if not set
        """
        return self._data["Temperature Difference Threshold for Reporting"]

    @temperature_difference_threshold_for_reporting.setter
    def temperature_difference_threshold_for_reporting(self, value=0.4 ):
        """  Corresponds to IDD Field `temperature_difference_threshold_for_reporting`
        Minimum temperature difference between predicted upper and lower layer
        temperatures above which UFAD auxilliary outputs are calculated.
        These outputs are 'UF Transition Height'and 'UF Average Temp Gradient'.  They
        are set to zero values when the temperature difference is less than the
        threshold and the output 'UF Zone Is Mixed' is set to 1

        Args:
            value (float): value for IDD Field `temperature_difference_threshold_for_reporting`
                Unit: deltaC
                Default value: 0.4
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
                                 'for field `temperature_difference_threshold_for_reporting`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `temperature_difference_threshold_for_reporting`')

        self._data["Temperature Difference Threshold for Reporting"] = value

    @property
    def floor_diffuser_type(self):
        """Get floor_diffuser_type

        Returns:
            str: the value of `floor_diffuser_type` or None if not set
        """
        return self._data["Floor Diffuser Type"]

    @floor_diffuser_type.setter
    def floor_diffuser_type(self, value="Swirl"):
        """  Corresponds to IDD Field `floor_diffuser_type`

        Args:
            value (str): value for IDD Field `floor_diffuser_type`
                Accepted values are:
                      - Custom
                      - Swirl
                      - VariableArea
                      - HorizontalSwirl
                      - LinearBarGrille
                Default value: Swirl
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
                                 'for field `floor_diffuser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_diffuser_type`')
            vals = set()
            vals.add("Custom")
            vals.add("Swirl")
            vals.add("VariableArea")
            vals.add("HorizontalSwirl")
            vals.add("LinearBarGrille")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_diffuser_type`'.format(value))

        self._data["Floor Diffuser Type"] = value

    @property
    def transition_height(self):
        """Get transition_height

        Returns:
            float: the value of `transition_height` or None if not set
        """
        return self._data["Transition Height"]

    @transition_height.setter
    def transition_height(self, value=1.7 ):
        """  Corresponds to IDD Field `transition_height`
        user-specified height above floor of boundary between occupied and upper subzones

        Args:
            value (float): value for IDD Field `transition_height`
                Unit: m
                Default value: 1.7
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
                                 'for field `transition_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `transition_height`')

        self._data["Transition Height"] = value

    @property
    def coefficient_a(self):
        """Get coefficient_a

        Returns:
            float: the value of `coefficient_a` or None if not set
        """
        return self._data["Coefficient A"]

    @coefficient_a.setter
    def coefficient_a(self, value=None):
        """  Corresponds to IDD Field `coefficient_a`
        Coefficient A in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float): value for IDD Field `coefficient_a`
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
                                 'for field `coefficient_a`'.format(value))

        self._data["Coefficient A"] = value

    @property
    def coefficient_b(self):
        """Get coefficient_b

        Returns:
            float: the value of `coefficient_b` or None if not set
        """
        return self._data["Coefficient B"]

    @coefficient_b.setter
    def coefficient_b(self, value=None):
        """  Corresponds to IDD Field `coefficient_b`
        Coefficient B in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float): value for IDD Field `coefficient_b`
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
                                 'for field `coefficient_b`'.format(value))

        self._data["Coefficient B"] = value

    @property
    def coefficient_c(self):
        """Get coefficient_c

        Returns:
            float: the value of `coefficient_c` or None if not set
        """
        return self._data["Coefficient C"]

    @coefficient_c.setter
    def coefficient_c(self, value=None):
        """  Corresponds to IDD Field `coefficient_c`
        Coefficient C in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float): value for IDD Field `coefficient_c`
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
                                 'for field `coefficient_c`'.format(value))

        self._data["Coefficient C"] = value

    @property
    def coefficient_d(self):
        """Get coefficient_d

        Returns:
            float: the value of `coefficient_d` or None if not set
        """
        return self._data["Coefficient D"]

    @coefficient_d.setter
    def coefficient_d(self, value=None):
        """  Corresponds to IDD Field `coefficient_d`
        Coefficient D in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float): value for IDD Field `coefficient_d`
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
                                 'for field `coefficient_d`'.format(value))

        self._data["Coefficient D"] = value

    @property
    def coefficient_e(self):
        """Get coefficient_e

        Returns:
            float: the value of `coefficient_e` or None if not set
        """
        return self._data["Coefficient E"]

    @coefficient_e.setter
    def coefficient_e(self, value=None):
        """  Corresponds to IDD Field `coefficient_e`
        Coefficient E in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float): value for IDD Field `coefficient_e`
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
                                 'for field `coefficient_e`'.format(value))

        self._data["Coefficient E"] = value

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
        out.append(self._to_str(self.number_of_diffusers))
        out.append(self._to_str(self.power_per_plume))
        out.append(self._to_str(self.design_effective_area_of_diffuser))
        out.append(self._to_str(self.diffuser_slot_angle_from_vertical))
        out.append(self._to_str(self.thermostat_height))
        out.append(self._to_str(self.comfort_height))
        out.append(self._to_str(self.temperature_difference_threshold_for_reporting))
        out.append(self._to_str(self.floor_diffuser_type))
        out.append(self._to_str(self.transition_height))
        out.append(self._to_str(self.coefficient_a))
        out.append(self._to_str(self.coefficient_b))
        out.append(self._to_str(self.coefficient_c))
        out.append(self._to_str(self.coefficient_d))
        out.append(self._to_str(self.coefficient_e))
        return ",".join(out)

class RoomAirSettingsUnderFloorAirDistributionExterior(object):
    """ Corresponds to IDD object `RoomAirSettings:UnderFloorAirDistributionExterior`
        Applicable to exterior spaces that are served by an underfloor air distribution system.
        The dominant sources of heat gain should be from people, equipment, and other
        localized sources located in the occupied part of the room, as well as convective gain
        coming from a warm window. Used with RoomAirModelType = CrossVentilation.
    """
    internal_name = "RoomAirSettings:UnderFloorAirDistributionExterior"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAirSettings:UnderFloorAirDistributionExterior`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Number of Diffusers per Zone"] = None
        self._data["Power per Plume"] = None
        self._data["Design Effective Area of Diffuser"] = None
        self._data["Diffuser Slot Angle from Vertical"] = None
        self._data["Thermostat Height"] = None
        self._data["Comfort Height"] = None
        self._data["Temperature Difference Threshold for Reporting"] = None
        self._data["Floor Diffuser Type"] = None
        self._data["Transition Height"] = None
        self._data["Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = None
        self._data["Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = None
        self._data["Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = None
        self._data["Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = None
        self._data["Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = None

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
            self.number_of_diffusers_per_zone = None
        else:
            self.number_of_diffusers_per_zone = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_plume = None
        else:
            self.power_per_plume = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_effective_area_of_diffuser = None
        else:
            self.design_effective_area_of_diffuser = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffuser_slot_angle_from_vertical = None
        else:
            self.diffuser_slot_angle_from_vertical = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_height = None
        else:
            self.thermostat_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.comfort_height = None
        else:
            self.comfort_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_difference_threshold_for_reporting = None
        else:
            self.temperature_difference_threshold_for_reporting = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_diffuser_type = None
        else:
            self.floor_diffuser_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transition_height = None
        else:
            self.transition_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2 = None
        else:
            self.coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2 = None
        else:
            self.coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2 = None
        else:
            self.coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2 = None
        else:
            self.coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2 = None
        else:
            self.coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2 = vals[i]
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
        Name of Zone being described. Any existing zone name

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
    def number_of_diffusers_per_zone(self):
        """Get number_of_diffusers_per_zone

        Returns:
            float: the value of `number_of_diffusers_per_zone` or None if not set
        """
        return self._data["Number of Diffusers per Zone"]

    @number_of_diffusers_per_zone.setter
    def number_of_diffusers_per_zone(self, value=None):
        """  Corresponds to IDD Field `number_of_diffusers_per_zone`

        Args:
            value (float): value for IDD Field `number_of_diffusers_per_zone`
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
                                 'for field `number_of_diffusers_per_zone`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `number_of_diffusers_per_zone`')

        self._data["Number of Diffusers per Zone"] = value

    @property
    def power_per_plume(self):
        """Get power_per_plume

        Returns:
            float: the value of `power_per_plume` or None if not set
        """
        return self._data["Power per Plume"]

    @power_per_plume.setter
    def power_per_plume(self, value=None):
        """  Corresponds to IDD Field `power_per_plume`

        Args:
            value (float): value for IDD Field `power_per_plume`
                Unit: W
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
                                 'for field `power_per_plume`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `power_per_plume`')

        self._data["Power per Plume"] = value

    @property
    def design_effective_area_of_diffuser(self):
        """Get design_effective_area_of_diffuser

        Returns:
            float: the value of `design_effective_area_of_diffuser` or None if not set
        """
        return self._data["Design Effective Area of Diffuser"]

    @design_effective_area_of_diffuser.setter
    def design_effective_area_of_diffuser(self, value=None):
        """  Corresponds to IDD Field `design_effective_area_of_diffuser`

        Args:
            value (float): value for IDD Field `design_effective_area_of_diffuser`
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
                                 'for field `design_effective_area_of_diffuser`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_effective_area_of_diffuser`')

        self._data["Design Effective Area of Diffuser"] = value

    @property
    def diffuser_slot_angle_from_vertical(self):
        """Get diffuser_slot_angle_from_vertical

        Returns:
            float: the value of `diffuser_slot_angle_from_vertical` or None if not set
        """
        return self._data["Diffuser Slot Angle from Vertical"]

    @diffuser_slot_angle_from_vertical.setter
    def diffuser_slot_angle_from_vertical(self, value=None):
        """  Corresponds to IDD Field `diffuser_slot_angle_from_vertical`

        Args:
            value (float): value for IDD Field `diffuser_slot_angle_from_vertical`
                Unit: deg
                value >= 0.0
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
                                 'for field `diffuser_slot_angle_from_vertical`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffuser_slot_angle_from_vertical`')
            if value > 90.0:
                raise ValueError('value need to be smaller 90.0 '
                                 'for field `diffuser_slot_angle_from_vertical`')

        self._data["Diffuser Slot Angle from Vertical"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self._data["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=1.2 ):
        """  Corresponds to IDD Field `thermostat_height`
        Height of thermostat/temperature control sensor above floor

        Args:
            value (float): value for IDD Field `thermostat_height`
                Unit: m
                Default value: 1.2
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
                                 'for field `thermostat_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermostat_height`')

        self._data["Thermostat Height"] = value

    @property
    def comfort_height(self):
        """Get comfort_height

        Returns:
            float: the value of `comfort_height` or None if not set
        """
        return self._data["Comfort Height"]

    @comfort_height.setter
    def comfort_height(self, value=1.1 ):
        """  Corresponds to IDD Field `comfort_height`
        Height at which Air temperature is calculated for comfort purposes

        Args:
            value (float): value for IDD Field `comfort_height`
                Unit: m
                Default value: 1.1
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
                                 'for field `comfort_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `comfort_height`')

        self._data["Comfort Height"] = value

    @property
    def temperature_difference_threshold_for_reporting(self):
        """Get temperature_difference_threshold_for_reporting

        Returns:
            float: the value of `temperature_difference_threshold_for_reporting` or None if not set
        """
        return self._data["Temperature Difference Threshold for Reporting"]

    @temperature_difference_threshold_for_reporting.setter
    def temperature_difference_threshold_for_reporting(self, value=0.4 ):
        """  Corresponds to IDD Field `temperature_difference_threshold_for_reporting`
        Minimum temperature difference between upper and lower layer
        temperatures above which UFAD auxilliary outputs are calculated.
        These outputs are 'UF Transition Height'and 'UF Average Temp Gradient'.  They
        are set to zero values when the temperature difference is less than the
        threshold and the output 'UF Zone Is Mixed' is set to 1

        Args:
            value (float): value for IDD Field `temperature_difference_threshold_for_reporting`
                Unit: deltaC
                Default value: 0.4
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
                                 'for field `temperature_difference_threshold_for_reporting`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `temperature_difference_threshold_for_reporting`')

        self._data["Temperature Difference Threshold for Reporting"] = value

    @property
    def floor_diffuser_type(self):
        """Get floor_diffuser_type

        Returns:
            str: the value of `floor_diffuser_type` or None if not set
        """
        return self._data["Floor Diffuser Type"]

    @floor_diffuser_type.setter
    def floor_diffuser_type(self, value="Swirl"):
        """  Corresponds to IDD Field `floor_diffuser_type`

        Args:
            value (str): value for IDD Field `floor_diffuser_type`
                Accepted values are:
                      - Custom
                      - Swirl
                      - VariableArea
                      - HorizontalSwirl
                      - LinearBarGrille
                Default value: Swirl
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
                                 'for field `floor_diffuser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_diffuser_type`')
            vals = set()
            vals.add("Custom")
            vals.add("Swirl")
            vals.add("VariableArea")
            vals.add("HorizontalSwirl")
            vals.add("LinearBarGrille")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_diffuser_type`'.format(value))

        self._data["Floor Diffuser Type"] = value

    @property
    def transition_height(self):
        """Get transition_height

        Returns:
            float: the value of `transition_height` or None if not set
        """
        return self._data["Transition Height"]

    @transition_height.setter
    def transition_height(self, value=1.7 ):
        """  Corresponds to IDD Field `transition_height`
        User-specified height above floor of boundary between occupied and upper subzones

        Args:
            value (float): value for IDD Field `transition_height`
                Unit: m
                Default value: 1.7
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
                                 'for field `transition_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `transition_height`')

        self._data["Transition Height"] = value

    @property
    def coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self._data["Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2(self, value=None):
        """  Corresponds to IDD Field `coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2`
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float): value for IDD Field `coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2`
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
                                 'for field `coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2`'.format(value))

        self._data["Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self._data["Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2(self, value=None):
        """  Corresponds to IDD Field `coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2`
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float): value for IDD Field `coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2`
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
                                 'for field `coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2`'.format(value))

        self._data["Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self._data["Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2(self, value=None):
        """  Corresponds to IDD Field `coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2`
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float): value for IDD Field `coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2`
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
                                 'for field `coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2`'.format(value))

        self._data["Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self._data["Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2(self, value=None):
        """  Corresponds to IDD Field `coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2`
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float): value for IDD Field `coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2`
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
                                 'for field `coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2`'.format(value))

        self._data["Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self._data["Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2(self, value=None):
        """  Corresponds to IDD Field `coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2`
        Kc is the fraction of the total zone load attributable to the lower subzone

        Args:
            value (float): value for IDD Field `coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2`
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
                                 'for field `coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2`'.format(value))

        self._data["Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

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
        out.append(self._to_str(self.number_of_diffusers_per_zone))
        out.append(self._to_str(self.power_per_plume))
        out.append(self._to_str(self.design_effective_area_of_diffuser))
        out.append(self._to_str(self.diffuser_slot_angle_from_vertical))
        out.append(self._to_str(self.thermostat_height))
        out.append(self._to_str(self.comfort_height))
        out.append(self._to_str(self.temperature_difference_threshold_for_reporting))
        out.append(self._to_str(self.floor_diffuser_type))
        out.append(self._to_str(self.transition_height))
        out.append(self._to_str(self.coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2))
        out.append(self._to_str(self.coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2))
        out.append(self._to_str(self.coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2))
        out.append(self._to_str(self.coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2))
        out.append(self._to_str(self.coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2))
        return ",".join(out)