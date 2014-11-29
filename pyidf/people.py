from collections import OrderedDict

class People(object):
    """ Corresponds to IDD object `People`
        Sets internal gains and contaminant rates for occupants in the zone.
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    """
    internal_name = "People"
    field_count = 24

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `People`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Number of People Schedule Name"] = None
        self._data["Number of People Calculation Method"] = None
        self._data["Number of People"] = None
        self._data["People per Zone Floor Area"] = None
        self._data["Zone Floor Area per Person"] = None
        self._data["Fraction Radiant"] = None
        self._data["Sensible Heat Fraction"] = None
        self._data["Activity Level Schedule Name"] = None
        self._data["Carbon Dioxide Generation Rate"] = None
        self._data["Enable ASHRAE 55 Comfort Warnings"] = None
        self._data["Mean Radiant Temperature Calculation Type"] = None
        self._data["Surface Name/Angle Factor List Name"] = None
        self._data["Work Efficiency Schedule Name"] = None
        self._data["Clothing Insulation Calculation Method"] = None
        self._data["Clothing Insulation Calculation Method Schedule Name"] = None
        self._data["Clothing Insulation Schedule Name"] = None
        self._data["Air Velocity Schedule Name"] = None
        self._data["Thermal Comfort Model 1 Type"] = None
        self._data["Thermal Comfort Model 2 Type"] = None
        self._data["Thermal Comfort Model 3 Type"] = None
        self._data["Thermal Comfort Model 4 Type"] = None
        self._data["Thermal Comfort Model 5 Type"] = None

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
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_people_schedule_name = None
        else:
            self.number_of_people_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_people_calculation_method = None
        else:
            self.number_of_people_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_people = None
        else:
            self.number_of_people = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.people_per_zone_floor_area = None
        else:
            self.people_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_floor_area_per_person = None
        else:
            self.zone_floor_area_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sensible_heat_fraction = None
        else:
            self.sensible_heat_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.activity_level_schedule_name = None
        else:
            self.activity_level_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.carbon_dioxide_generation_rate = None
        else:
            self.carbon_dioxide_generation_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enable_ashrae_55_comfort_warnings = None
        else:
            self.enable_ashrae_55_comfort_warnings = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mean_radiant_temperature_calculation_type = None
        else:
            self.mean_radiant_temperature_calculation_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_or_angle_factor_list_name = None
        else:
            self.surface_name_or_angle_factor_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.work_efficiency_schedule_name = None
        else:
            self.work_efficiency_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.clothing_insulation_calculation_method = None
        else:
            self.clothing_insulation_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.clothing_insulation_calculation_method_schedule_name = None
        else:
            self.clothing_insulation_calculation_method_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.clothing_insulation_schedule_name = None
        else:
            self.clothing_insulation_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_velocity_schedule_name = None
        else:
            self.air_velocity_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_comfort_model_1_type = None
        else:
            self.thermal_comfort_model_1_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_comfort_model_2_type = None
        else:
            self.thermal_comfort_model_2_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_comfort_model_3_type = None
        else:
            self.thermal_comfort_model_3_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_comfort_model_4_type = None
        else:
            self.thermal_comfort_model_4_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_comfort_model_5_type = None
        else:
            self.thermal_comfort_model_5_type = vals[i]
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
    def zone_or_zonelist_name(self):
        """Get zone_or_zonelist_name

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set
        """
        return self._data["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """  Corresponds to IDD Field `zone_or_zonelist_name`

        Args:
            value (str): value for IDD Field `zone_or_zonelist_name`
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
                                 'for field `zone_or_zonelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_or_zonelist_name`')

        self._data["Zone or ZoneList Name"] = value

    @property
    def number_of_people_schedule_name(self):
        """Get number_of_people_schedule_name

        Returns:
            str: the value of `number_of_people_schedule_name` or None if not set
        """
        return self._data["Number of People Schedule Name"]

    @number_of_people_schedule_name.setter
    def number_of_people_schedule_name(self, value=None):
        """  Corresponds to IDD Field `number_of_people_schedule_name`
        units in schedule should be fraction applied to number of people (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `number_of_people_schedule_name`
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
                                 'for field `number_of_people_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `number_of_people_schedule_name`')

        self._data["Number of People Schedule Name"] = value

    @property
    def number_of_people_calculation_method(self):
        """Get number_of_people_calculation_method

        Returns:
            str: the value of `number_of_people_calculation_method` or None if not set
        """
        return self._data["Number of People Calculation Method"]

    @number_of_people_calculation_method.setter
    def number_of_people_calculation_method(self, value="People"):
        """  Corresponds to IDD Field `number_of_people_calculation_method`
        The entered calculation method is used to create the maximum number of people
        for this set of attributes (i.e. sensible fraction, schedule, etc)
        Choices: People -- simply enter number of occupants.
        People per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Number of people
        Zone Floor Area per Person -- enter the number to apply.  Floor Area / Value = Number of people

        Args:
            value (str): value for IDD Field `number_of_people_calculation_method`
                Accepted values are:
                      - People
                      - People/Area
                      - Area/Person
                Default value: People
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
                                 'for field `number_of_people_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `number_of_people_calculation_method`')
            vals = set()
            vals.add("People")
            vals.add("People/Area")
            vals.add("Area/Person")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `number_of_people_calculation_method`'.format(value))

        self._data["Number of People Calculation Method"] = value

    @property
    def number_of_people(self):
        """Get number_of_people

        Returns:
            float: the value of `number_of_people` or None if not set
        """
        return self._data["Number of People"]

    @number_of_people.setter
    def number_of_people(self, value=None):
        """  Corresponds to IDD Field `number_of_people`

        Args:
            value (float): value for IDD Field `number_of_people`
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
                                 'for field `number_of_people`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `number_of_people`')

        self._data["Number of People"] = value

    @property
    def people_per_zone_floor_area(self):
        """Get people_per_zone_floor_area

        Returns:
            float: the value of `people_per_zone_floor_area` or None if not set
        """
        return self._data["People per Zone Floor Area"]

    @people_per_zone_floor_area.setter
    def people_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `people_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `people_per_zone_floor_area`
                Unit: person/m2
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
                                 'for field `people_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `people_per_zone_floor_area`')

        self._data["People per Zone Floor Area"] = value

    @property
    def zone_floor_area_per_person(self):
        """Get zone_floor_area_per_person

        Returns:
            float: the value of `zone_floor_area_per_person` or None if not set
        """
        return self._data["Zone Floor Area per Person"]

    @zone_floor_area_per_person.setter
    def zone_floor_area_per_person(self, value=None):
        """  Corresponds to IDD Field `zone_floor_area_per_person`

        Args:
            value (float): value for IDD Field `zone_floor_area_per_person`
                Unit: m2/person
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
                                 'for field `zone_floor_area_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_floor_area_per_person`')

        self._data["Zone Floor Area per Person"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """  Corresponds to IDD Field `fraction_radiant`

        Args:
            value (float): value for IDD Field `fraction_radiant`
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
                                 'for field `fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_radiant`')

        self._data["Fraction Radiant"] = value

    @property
    def sensible_heat_fraction(self):
        """Get sensible_heat_fraction

        Returns:
            float: the value of `sensible_heat_fraction` or None if not set
        """
        return self._data["Sensible Heat Fraction"]

    @sensible_heat_fraction.setter
    def sensible_heat_fraction(self, value=None):
        """  Corresponds to IDD Field `sensible_heat_fraction`
        if input, overrides program calculated sensible/latent split

        Args:
            value (float): value for IDD Field `sensible_heat_fraction`
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
                                 'for field `sensible_heat_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `sensible_heat_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `sensible_heat_fraction`')

        self._data["Sensible Heat Fraction"] = value

    @property
    def activity_level_schedule_name(self):
        """Get activity_level_schedule_name

        Returns:
            str: the value of `activity_level_schedule_name` or None if not set
        """
        return self._data["Activity Level Schedule Name"]

    @activity_level_schedule_name.setter
    def activity_level_schedule_name(self, value=None):
        """  Corresponds to IDD Field `activity_level_schedule_name`
        Note that W has to be converted to mets in TC routine
        units in schedule are W/person

        Args:
            value (str): value for IDD Field `activity_level_schedule_name`
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
                                 'for field `activity_level_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `activity_level_schedule_name`')

        self._data["Activity Level Schedule Name"] = value

    @property
    def carbon_dioxide_generation_rate(self):
        """Get carbon_dioxide_generation_rate

        Returns:
            float: the value of `carbon_dioxide_generation_rate` or None if not set
        """
        return self._data["Carbon Dioxide Generation Rate"]

    @carbon_dioxide_generation_rate.setter
    def carbon_dioxide_generation_rate(self, value=3.82e-08 ):
        """  Corresponds to IDD Field `carbon_dioxide_generation_rate`
        CO2 generation rate per unit of activity level.
        The default value is obtained from ASHRAE Std 62.1 at 0.0084 cfm/met/person over
        the general adult population.

        Args:
            value (float): value for IDD Field `carbon_dioxide_generation_rate`
                Unit: m3/s-W
                Default value: 3.82e-08
                value >= 0.0
                value <= 3.82e-07
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `carbon_dioxide_generation_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `carbon_dioxide_generation_rate`')
            if value > 3.82e-07:
                raise ValueError('value need to be smaller 3.82e-07 '
                                 'for field `carbon_dioxide_generation_rate`')

        self._data["Carbon Dioxide Generation Rate"] = value

    @property
    def enable_ashrae_55_comfort_warnings(self):
        """Get enable_ashrae_55_comfort_warnings

        Returns:
            str: the value of `enable_ashrae_55_comfort_warnings` or None if not set
        """
        return self._data["Enable ASHRAE 55 Comfort Warnings"]

    @enable_ashrae_55_comfort_warnings.setter
    def enable_ashrae_55_comfort_warnings(self, value="No"):
        """  Corresponds to IDD Field `enable_ashrae_55_comfort_warnings`

        Args:
            value (str): value for IDD Field `enable_ashrae_55_comfort_warnings`
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
                                 'for field `enable_ashrae_55_comfort_warnings`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enable_ashrae_55_comfort_warnings`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `enable_ashrae_55_comfort_warnings`'.format(value))

        self._data["Enable ASHRAE 55 Comfort Warnings"] = value

    @property
    def mean_radiant_temperature_calculation_type(self):
        """Get mean_radiant_temperature_calculation_type

        Returns:
            str: the value of `mean_radiant_temperature_calculation_type` or None if not set
        """
        return self._data["Mean Radiant Temperature Calculation Type"]

    @mean_radiant_temperature_calculation_type.setter
    def mean_radiant_temperature_calculation_type(self, value="ZoneAveraged"):
        """  Corresponds to IDD Field `mean_radiant_temperature_calculation_type`
        optional (only required for thermal comfort runs)

        Args:
            value (str): value for IDD Field `mean_radiant_temperature_calculation_type`
                Accepted values are:
                      - ZoneAveraged
                      - SurfaceWeighted
                      - AngleFactor
                Default value: ZoneAveraged
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
                                 'for field `mean_radiant_temperature_calculation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mean_radiant_temperature_calculation_type`')
            vals = set()
            vals.add("ZoneAveraged")
            vals.add("SurfaceWeighted")
            vals.add("AngleFactor")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mean_radiant_temperature_calculation_type`'.format(value))

        self._data["Mean Radiant Temperature Calculation Type"] = value

    @property
    def surface_name_or_angle_factor_list_name(self):
        """Get surface_name_or_angle_factor_list_name

        Returns:
            str: the value of `surface_name_or_angle_factor_list_name` or None if not set
        """
        return self._data["Surface Name/Angle Factor List Name"]

    @surface_name_or_angle_factor_list_name.setter
    def surface_name_or_angle_factor_list_name(self, value=None):
        """  Corresponds to IDD Field `surface_name_or_angle_factor_list_name`
        optional (only required for thermal comfort runs)

        Args:
            value (str): value for IDD Field `surface_name_or_angle_factor_list_name`
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
                                 'for field `surface_name_or_angle_factor_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_or_angle_factor_list_name`')

        self._data["Surface Name/Angle Factor List Name"] = value

    @property
    def work_efficiency_schedule_name(self):
        """Get work_efficiency_schedule_name

        Returns:
            str: the value of `work_efficiency_schedule_name` or None if not set
        """
        return self._data["Work Efficiency Schedule Name"]

    @work_efficiency_schedule_name.setter
    def work_efficiency_schedule_name(self, value=None):
        """  Corresponds to IDD Field `work_efficiency_schedule_name`
        units in schedule are 0.0 to 1.0
        optional (only required for thermal comfort runs)

        Args:
            value (str): value for IDD Field `work_efficiency_schedule_name`
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
                                 'for field `work_efficiency_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `work_efficiency_schedule_name`')

        self._data["Work Efficiency Schedule Name"] = value

    @property
    def clothing_insulation_calculation_method(self):
        """Get clothing_insulation_calculation_method

        Returns:
            str: the value of `clothing_insulation_calculation_method` or None if not set
        """
        return self._data["Clothing Insulation Calculation Method"]

    @clothing_insulation_calculation_method.setter
    def clothing_insulation_calculation_method(self, value="ClothingInsulationSchedule"):
        """  Corresponds to IDD Field `clothing_insulation_calculation_method`

        Args:
            value (str): value for IDD Field `clothing_insulation_calculation_method`
                Accepted values are:
                      - ClothingInsulationSchedule
                      - DynamicClothingModelASHRAE55
                      - CalculationMethodSchedule
                Default value: ClothingInsulationSchedule
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
                                 'for field `clothing_insulation_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `clothing_insulation_calculation_method`')
            vals = set()
            vals.add("ClothingInsulationSchedule")
            vals.add("DynamicClothingModelASHRAE55")
            vals.add("CalculationMethodSchedule")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `clothing_insulation_calculation_method`'.format(value))

        self._data["Clothing Insulation Calculation Method"] = value

    @property
    def clothing_insulation_calculation_method_schedule_name(self):
        """Get clothing_insulation_calculation_method_schedule_name

        Returns:
            str: the value of `clothing_insulation_calculation_method_schedule_name` or None if not set
        """
        return self._data["Clothing Insulation Calculation Method Schedule Name"]

    @clothing_insulation_calculation_method_schedule_name.setter
    def clothing_insulation_calculation_method_schedule_name(self, value=None):
        """  Corresponds to IDD Field `clothing_insulation_calculation_method_schedule_name`
        a schedule value of 1 for the Scheduled method, and 2 for the DynamicClothingModelASHRAE55 method

        Args:
            value (str): value for IDD Field `clothing_insulation_calculation_method_schedule_name`
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
                                 'for field `clothing_insulation_calculation_method_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `clothing_insulation_calculation_method_schedule_name`')

        self._data["Clothing Insulation Calculation Method Schedule Name"] = value

    @property
    def clothing_insulation_schedule_name(self):
        """Get clothing_insulation_schedule_name

        Returns:
            str: the value of `clothing_insulation_schedule_name` or None if not set
        """
        return self._data["Clothing Insulation Schedule Name"]

    @clothing_insulation_schedule_name.setter
    def clothing_insulation_schedule_name(self, value=None):
        """  Corresponds to IDD Field `clothing_insulation_schedule_name`
        use "Clo" from ASHRAE or Thermal Comfort guides
        optional (only required for thermal comfort runs)

        Args:
            value (str): value for IDD Field `clothing_insulation_schedule_name`
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
                                 'for field `clothing_insulation_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `clothing_insulation_schedule_name`')

        self._data["Clothing Insulation Schedule Name"] = value

    @property
    def air_velocity_schedule_name(self):
        """Get air_velocity_schedule_name

        Returns:
            str: the value of `air_velocity_schedule_name` or None if not set
        """
        return self._data["Air Velocity Schedule Name"]

    @air_velocity_schedule_name.setter
    def air_velocity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `air_velocity_schedule_name`
        units in the schedule are m/s
        optional (only required for thermal comfort runs)

        Args:
            value (str): value for IDD Field `air_velocity_schedule_name`
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
                                 'for field `air_velocity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_velocity_schedule_name`')

        self._data["Air Velocity Schedule Name"] = value

    @property
    def thermal_comfort_model_1_type(self):
        """Get thermal_comfort_model_1_type

        Returns:
            str: the value of `thermal_comfort_model_1_type` or None if not set
        """
        return self._data["Thermal Comfort Model 1 Type"]

    @thermal_comfort_model_1_type.setter
    def thermal_comfort_model_1_type(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_model_1_type`
        optional (only needed for people thermal comfort results reporting)

        Args:
            value (str): value for IDD Field `thermal_comfort_model_1_type`
                Accepted values are:
                      - Fanger
                      - Pierce
                      - KSU
                      - AdaptiveASH55
                      - AdaptiveCEN15251
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
                                 'for field `thermal_comfort_model_1_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_model_1_type`')
            vals = set()
            vals.add("Fanger")
            vals.add("Pierce")
            vals.add("KSU")
            vals.add("AdaptiveASH55")
            vals.add("AdaptiveCEN15251")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `thermal_comfort_model_1_type`'.format(value))

        self._data["Thermal Comfort Model 1 Type"] = value

    @property
    def thermal_comfort_model_2_type(self):
        """Get thermal_comfort_model_2_type

        Returns:
            str: the value of `thermal_comfort_model_2_type` or None if not set
        """
        return self._data["Thermal Comfort Model 2 Type"]

    @thermal_comfort_model_2_type.setter
    def thermal_comfort_model_2_type(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_model_2_type`
        optional (second type of thermal comfort model and results reporting)

        Args:
            value (str): value for IDD Field `thermal_comfort_model_2_type`
                Accepted values are:
                      - Fanger
                      - Pierce
                      - KSU
                      - AdaptiveASH55
                      - AdaptiveCEN15251
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
                                 'for field `thermal_comfort_model_2_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_model_2_type`')
            vals = set()
            vals.add("Fanger")
            vals.add("Pierce")
            vals.add("KSU")
            vals.add("AdaptiveASH55")
            vals.add("AdaptiveCEN15251")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `thermal_comfort_model_2_type`'.format(value))

        self._data["Thermal Comfort Model 2 Type"] = value

    @property
    def thermal_comfort_model_3_type(self):
        """Get thermal_comfort_model_3_type

        Returns:
            str: the value of `thermal_comfort_model_3_type` or None if not set
        """
        return self._data["Thermal Comfort Model 3 Type"]

    @thermal_comfort_model_3_type.setter
    def thermal_comfort_model_3_type(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_model_3_type`
        optional (third thermal comfort model and report type)

        Args:
            value (str): value for IDD Field `thermal_comfort_model_3_type`
                Accepted values are:
                      - Fanger
                      - Pierce
                      - KSU
                      - AdaptiveASH55
                      - AdaptiveCEN15251
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
                                 'for field `thermal_comfort_model_3_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_model_3_type`')
            vals = set()
            vals.add("Fanger")
            vals.add("Pierce")
            vals.add("KSU")
            vals.add("AdaptiveASH55")
            vals.add("AdaptiveCEN15251")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `thermal_comfort_model_3_type`'.format(value))

        self._data["Thermal Comfort Model 3 Type"] = value

    @property
    def thermal_comfort_model_4_type(self):
        """Get thermal_comfort_model_4_type

        Returns:
            str: the value of `thermal_comfort_model_4_type` or None if not set
        """
        return self._data["Thermal Comfort Model 4 Type"]

    @thermal_comfort_model_4_type.setter
    def thermal_comfort_model_4_type(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_model_4_type`
        optional (fourth thermal comfort model and report type)

        Args:
            value (str): value for IDD Field `thermal_comfort_model_4_type`
                Accepted values are:
                      - Fanger
                      - Pierce
                      - KSU
                      - AdaptiveASH55
                      - AdaptiveCEN15251
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
                                 'for field `thermal_comfort_model_4_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_model_4_type`')
            vals = set()
            vals.add("Fanger")
            vals.add("Pierce")
            vals.add("KSU")
            vals.add("AdaptiveASH55")
            vals.add("AdaptiveCEN15251")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `thermal_comfort_model_4_type`'.format(value))

        self._data["Thermal Comfort Model 4 Type"] = value

    @property
    def thermal_comfort_model_5_type(self):
        """Get thermal_comfort_model_5_type

        Returns:
            str: the value of `thermal_comfort_model_5_type` or None if not set
        """
        return self._data["Thermal Comfort Model 5 Type"]

    @thermal_comfort_model_5_type.setter
    def thermal_comfort_model_5_type(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_model_5_type`
        optional (fifth thermal comfort model and report type)

        Args:
            value (str): value for IDD Field `thermal_comfort_model_5_type`
                Accepted values are:
                      - Fanger
                      - Pierce
                      - KSU
                      - AdaptiveASH55
                      - AdaptiveCEN15251
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
                                 'for field `thermal_comfort_model_5_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_model_5_type`')
            vals = set()
            vals.add("Fanger")
            vals.add("Pierce")
            vals.add("KSU")
            vals.add("AdaptiveASH55")
            vals.add("AdaptiveCEN15251")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `thermal_comfort_model_5_type`'.format(value))

        self._data["Thermal Comfort Model 5 Type"] = value

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
        out.append(self._to_str(self.zone_or_zonelist_name))
        out.append(self._to_str(self.number_of_people_schedule_name))
        out.append(self._to_str(self.number_of_people_calculation_method))
        out.append(self._to_str(self.number_of_people))
        out.append(self._to_str(self.people_per_zone_floor_area))
        out.append(self._to_str(self.zone_floor_area_per_person))
        out.append(self._to_str(self.fraction_radiant))
        out.append(self._to_str(self.sensible_heat_fraction))
        out.append(self._to_str(self.activity_level_schedule_name))
        out.append(self._to_str(self.carbon_dioxide_generation_rate))
        out.append(self._to_str(self.enable_ashrae_55_comfort_warnings))
        out.append(self._to_str(self.mean_radiant_temperature_calculation_type))
        out.append(self._to_str(self.surface_name_or_angle_factor_list_name))
        out.append(self._to_str(self.work_efficiency_schedule_name))
        out.append(self._to_str(self.clothing_insulation_calculation_method))
        out.append(self._to_str(self.clothing_insulation_calculation_method_schedule_name))
        out.append(self._to_str(self.clothing_insulation_schedule_name))
        out.append(self._to_str(self.air_velocity_schedule_name))
        out.append(self._to_str(self.thermal_comfort_model_1_type))
        out.append(self._to_str(self.thermal_comfort_model_2_type))
        out.append(self._to_str(self.thermal_comfort_model_3_type))
        out.append(self._to_str(self.thermal_comfort_model_4_type))
        out.append(self._to_str(self.thermal_comfort_model_5_type))
        return ",".join(out)