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
        """ Init data dictionary object for IDD  `People`
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

class ComfortViewFactorAngles(object):
    """ Corresponds to IDD object `ComfortViewFactorAngles`
        Used to specify radiant view factors for thermal comfort calculations.
    """
    internal_name = "ComfortViewFactorAngles"
    field_count = 42

    def __init__(self):
        """ Init data dictionary object for IDD  `ComfortViewFactorAngles`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Surface 1 Name"] = None
        self._data["Angle Factor 1"] = None
        self._data["Surface 2 Name"] = None
        self._data["Angle Factor 2"] = None
        self._data["Surface 3 Name"] = None
        self._data["Angle Factor 3"] = None
        self._data["Surface 4 Name"] = None
        self._data["Angle Factor 4"] = None
        self._data["Surface 5 Name"] = None
        self._data["Angle Factor 5"] = None
        self._data["Surface 6 Name"] = None
        self._data["Angle Factor 6"] = None
        self._data["Surface 7 Name"] = None
        self._data["Angle Factor 7"] = None
        self._data["Surface 8 Name"] = None
        self._data["Angle Factor 8"] = None
        self._data["Surface 9 Name"] = None
        self._data["Angle Factor 9"] = None
        self._data["Surface 10 Name"] = None
        self._data["Angle Factor 10"] = None
        self._data["Surface 11 Name"] = None
        self._data["Angle Factor 11"] = None
        self._data["Surface 12 Name"] = None
        self._data["Angle Factor 12"] = None
        self._data["Surface 13 Name"] = None
        self._data["Angle Factor 13"] = None
        self._data["Surface 14 Name"] = None
        self._data["Angle Factor 14"] = None
        self._data["Surface 15 Name"] = None
        self._data["Angle Factor 15"] = None
        self._data["Surface 16 Name"] = None
        self._data["Angle Factor 16"] = None
        self._data["Surface 17 Name"] = None
        self._data["Angle Factor 17"] = None
        self._data["Surface 18 Name"] = None
        self._data["Angle Factor 18"] = None
        self._data["Surface 19 Name"] = None
        self._data["Angle Factor 19"] = None
        self._data["Surface 20 Name"] = None
        self._data["Angle Factor 20"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_1_name = None
        else:
            self.surface_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_1 = None
        else:
            self.angle_factor_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_2_name = None
        else:
            self.surface_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_2 = None
        else:
            self.angle_factor_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_3_name = None
        else:
            self.surface_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_3 = None
        else:
            self.angle_factor_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_4_name = None
        else:
            self.surface_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_4 = None
        else:
            self.angle_factor_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_5_name = None
        else:
            self.surface_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_5 = None
        else:
            self.angle_factor_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_6_name = None
        else:
            self.surface_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_6 = None
        else:
            self.angle_factor_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_7_name = None
        else:
            self.surface_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_7 = None
        else:
            self.angle_factor_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_8_name = None
        else:
            self.surface_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_8 = None
        else:
            self.angle_factor_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_9_name = None
        else:
            self.surface_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_9 = None
        else:
            self.angle_factor_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_10_name = None
        else:
            self.surface_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_10 = None
        else:
            self.angle_factor_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_11_name = None
        else:
            self.surface_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_11 = None
        else:
            self.angle_factor_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_12_name = None
        else:
            self.surface_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_12 = None
        else:
            self.angle_factor_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_13_name = None
        else:
            self.surface_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_13 = None
        else:
            self.angle_factor_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_14_name = None
        else:
            self.surface_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_14 = None
        else:
            self.angle_factor_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_15_name = None
        else:
            self.surface_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_15 = None
        else:
            self.angle_factor_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_16_name = None
        else:
            self.surface_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_16 = None
        else:
            self.angle_factor_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_17_name = None
        else:
            self.surface_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_17 = None
        else:
            self.angle_factor_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_18_name = None
        else:
            self.surface_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_18 = None
        else:
            self.angle_factor_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_19_name = None
        else:
            self.surface_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_19 = None
        else:
            self.angle_factor_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_20_name = None
        else:
            self.surface_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_factor_20 = None
        else:
            self.angle_factor_20 = vals[i]
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
    def surface_1_name(self):
        """Get surface_1_name

        Returns:
            str: the value of `surface_1_name` or None if not set
        """
        return self._data["Surface 1 Name"]

    @surface_1_name.setter
    def surface_1_name(self, value=None):
        """  Corresponds to IDD Field `surface_1_name`

        Args:
            value (str): value for IDD Field `surface_1_name`
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
                                 'for field `surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_1_name`')

        self._data["Surface 1 Name"] = value

    @property
    def angle_factor_1(self):
        """Get angle_factor_1

        Returns:
            float: the value of `angle_factor_1` or None if not set
        """
        return self._data["Angle Factor 1"]

    @angle_factor_1.setter
    def angle_factor_1(self, value=None):
        """  Corresponds to IDD Field `angle_factor_1`

        Args:
            value (float): value for IDD Field `angle_factor_1`
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
                                 'for field `angle_factor_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_1`')

        self._data["Angle Factor 1"] = value

    @property
    def surface_2_name(self):
        """Get surface_2_name

        Returns:
            str: the value of `surface_2_name` or None if not set
        """
        return self._data["Surface 2 Name"]

    @surface_2_name.setter
    def surface_2_name(self, value=None):
        """  Corresponds to IDD Field `surface_2_name`

        Args:
            value (str): value for IDD Field `surface_2_name`
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
                                 'for field `surface_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_2_name`')

        self._data["Surface 2 Name"] = value

    @property
    def angle_factor_2(self):
        """Get angle_factor_2

        Returns:
            float: the value of `angle_factor_2` or None if not set
        """
        return self._data["Angle Factor 2"]

    @angle_factor_2.setter
    def angle_factor_2(self, value=None):
        """  Corresponds to IDD Field `angle_factor_2`

        Args:
            value (float): value for IDD Field `angle_factor_2`
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
                                 'for field `angle_factor_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_2`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_2`')

        self._data["Angle Factor 2"] = value

    @property
    def surface_3_name(self):
        """Get surface_3_name

        Returns:
            str: the value of `surface_3_name` or None if not set
        """
        return self._data["Surface 3 Name"]

    @surface_3_name.setter
    def surface_3_name(self, value=None):
        """  Corresponds to IDD Field `surface_3_name`

        Args:
            value (str): value for IDD Field `surface_3_name`
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
                                 'for field `surface_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_3_name`')

        self._data["Surface 3 Name"] = value

    @property
    def angle_factor_3(self):
        """Get angle_factor_3

        Returns:
            float: the value of `angle_factor_3` or None if not set
        """
        return self._data["Angle Factor 3"]

    @angle_factor_3.setter
    def angle_factor_3(self, value=None):
        """  Corresponds to IDD Field `angle_factor_3`

        Args:
            value (float): value for IDD Field `angle_factor_3`
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
                                 'for field `angle_factor_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_3`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_3`')

        self._data["Angle Factor 3"] = value

    @property
    def surface_4_name(self):
        """Get surface_4_name

        Returns:
            str: the value of `surface_4_name` or None if not set
        """
        return self._data["Surface 4 Name"]

    @surface_4_name.setter
    def surface_4_name(self, value=None):
        """  Corresponds to IDD Field `surface_4_name`

        Args:
            value (str): value for IDD Field `surface_4_name`
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
                                 'for field `surface_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_4_name`')

        self._data["Surface 4 Name"] = value

    @property
    def angle_factor_4(self):
        """Get angle_factor_4

        Returns:
            float: the value of `angle_factor_4` or None if not set
        """
        return self._data["Angle Factor 4"]

    @angle_factor_4.setter
    def angle_factor_4(self, value=None):
        """  Corresponds to IDD Field `angle_factor_4`

        Args:
            value (float): value for IDD Field `angle_factor_4`
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
                                 'for field `angle_factor_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_4`')

        self._data["Angle Factor 4"] = value

    @property
    def surface_5_name(self):
        """Get surface_5_name

        Returns:
            str: the value of `surface_5_name` or None if not set
        """
        return self._data["Surface 5 Name"]

    @surface_5_name.setter
    def surface_5_name(self, value=None):
        """  Corresponds to IDD Field `surface_5_name`

        Args:
            value (str): value for IDD Field `surface_5_name`
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
                                 'for field `surface_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_5_name`')

        self._data["Surface 5 Name"] = value

    @property
    def angle_factor_5(self):
        """Get angle_factor_5

        Returns:
            float: the value of `angle_factor_5` or None if not set
        """
        return self._data["Angle Factor 5"]

    @angle_factor_5.setter
    def angle_factor_5(self, value=None):
        """  Corresponds to IDD Field `angle_factor_5`

        Args:
            value (float): value for IDD Field `angle_factor_5`
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
                                 'for field `angle_factor_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_5`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_5`')

        self._data["Angle Factor 5"] = value

    @property
    def surface_6_name(self):
        """Get surface_6_name

        Returns:
            str: the value of `surface_6_name` or None if not set
        """
        return self._data["Surface 6 Name"]

    @surface_6_name.setter
    def surface_6_name(self, value=None):
        """  Corresponds to IDD Field `surface_6_name`

        Args:
            value (str): value for IDD Field `surface_6_name`
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
                                 'for field `surface_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_6_name`')

        self._data["Surface 6 Name"] = value

    @property
    def angle_factor_6(self):
        """Get angle_factor_6

        Returns:
            float: the value of `angle_factor_6` or None if not set
        """
        return self._data["Angle Factor 6"]

    @angle_factor_6.setter
    def angle_factor_6(self, value=None):
        """  Corresponds to IDD Field `angle_factor_6`

        Args:
            value (float): value for IDD Field `angle_factor_6`
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
                                 'for field `angle_factor_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_6`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_6`')

        self._data["Angle Factor 6"] = value

    @property
    def surface_7_name(self):
        """Get surface_7_name

        Returns:
            str: the value of `surface_7_name` or None if not set
        """
        return self._data["Surface 7 Name"]

    @surface_7_name.setter
    def surface_7_name(self, value=None):
        """  Corresponds to IDD Field `surface_7_name`

        Args:
            value (str): value for IDD Field `surface_7_name`
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
                                 'for field `surface_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_7_name`')

        self._data["Surface 7 Name"] = value

    @property
    def angle_factor_7(self):
        """Get angle_factor_7

        Returns:
            float: the value of `angle_factor_7` or None if not set
        """
        return self._data["Angle Factor 7"]

    @angle_factor_7.setter
    def angle_factor_7(self, value=None):
        """  Corresponds to IDD Field `angle_factor_7`

        Args:
            value (float): value for IDD Field `angle_factor_7`
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
                                 'for field `angle_factor_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_7`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_7`')

        self._data["Angle Factor 7"] = value

    @property
    def surface_8_name(self):
        """Get surface_8_name

        Returns:
            str: the value of `surface_8_name` or None if not set
        """
        return self._data["Surface 8 Name"]

    @surface_8_name.setter
    def surface_8_name(self, value=None):
        """  Corresponds to IDD Field `surface_8_name`

        Args:
            value (str): value for IDD Field `surface_8_name`
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
                                 'for field `surface_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_8_name`')

        self._data["Surface 8 Name"] = value

    @property
    def angle_factor_8(self):
        """Get angle_factor_8

        Returns:
            float: the value of `angle_factor_8` or None if not set
        """
        return self._data["Angle Factor 8"]

    @angle_factor_8.setter
    def angle_factor_8(self, value=None):
        """  Corresponds to IDD Field `angle_factor_8`

        Args:
            value (float): value for IDD Field `angle_factor_8`
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
                                 'for field `angle_factor_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_8`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_8`')

        self._data["Angle Factor 8"] = value

    @property
    def surface_9_name(self):
        """Get surface_9_name

        Returns:
            str: the value of `surface_9_name` or None if not set
        """
        return self._data["Surface 9 Name"]

    @surface_9_name.setter
    def surface_9_name(self, value=None):
        """  Corresponds to IDD Field `surface_9_name`

        Args:
            value (str): value for IDD Field `surface_9_name`
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
                                 'for field `surface_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_9_name`')

        self._data["Surface 9 Name"] = value

    @property
    def angle_factor_9(self):
        """Get angle_factor_9

        Returns:
            float: the value of `angle_factor_9` or None if not set
        """
        return self._data["Angle Factor 9"]

    @angle_factor_9.setter
    def angle_factor_9(self, value=None):
        """  Corresponds to IDD Field `angle_factor_9`

        Args:
            value (float): value for IDD Field `angle_factor_9`
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
                                 'for field `angle_factor_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_9`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_9`')

        self._data["Angle Factor 9"] = value

    @property
    def surface_10_name(self):
        """Get surface_10_name

        Returns:
            str: the value of `surface_10_name` or None if not set
        """
        return self._data["Surface 10 Name"]

    @surface_10_name.setter
    def surface_10_name(self, value=None):
        """  Corresponds to IDD Field `surface_10_name`

        Args:
            value (str): value for IDD Field `surface_10_name`
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
                                 'for field `surface_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_10_name`')

        self._data["Surface 10 Name"] = value

    @property
    def angle_factor_10(self):
        """Get angle_factor_10

        Returns:
            float: the value of `angle_factor_10` or None if not set
        """
        return self._data["Angle Factor 10"]

    @angle_factor_10.setter
    def angle_factor_10(self, value=None):
        """  Corresponds to IDD Field `angle_factor_10`

        Args:
            value (float): value for IDD Field `angle_factor_10`
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
                                 'for field `angle_factor_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_10`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_10`')

        self._data["Angle Factor 10"] = value

    @property
    def surface_11_name(self):
        """Get surface_11_name

        Returns:
            str: the value of `surface_11_name` or None if not set
        """
        return self._data["Surface 11 Name"]

    @surface_11_name.setter
    def surface_11_name(self, value=None):
        """  Corresponds to IDD Field `surface_11_name`

        Args:
            value (str): value for IDD Field `surface_11_name`
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
                                 'for field `surface_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_11_name`')

        self._data["Surface 11 Name"] = value

    @property
    def angle_factor_11(self):
        """Get angle_factor_11

        Returns:
            float: the value of `angle_factor_11` or None if not set
        """
        return self._data["Angle Factor 11"]

    @angle_factor_11.setter
    def angle_factor_11(self, value=None):
        """  Corresponds to IDD Field `angle_factor_11`

        Args:
            value (float): value for IDD Field `angle_factor_11`
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
                                 'for field `angle_factor_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_11`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_11`')

        self._data["Angle Factor 11"] = value

    @property
    def surface_12_name(self):
        """Get surface_12_name

        Returns:
            str: the value of `surface_12_name` or None if not set
        """
        return self._data["Surface 12 Name"]

    @surface_12_name.setter
    def surface_12_name(self, value=None):
        """  Corresponds to IDD Field `surface_12_name`

        Args:
            value (str): value for IDD Field `surface_12_name`
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
                                 'for field `surface_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_12_name`')

        self._data["Surface 12 Name"] = value

    @property
    def angle_factor_12(self):
        """Get angle_factor_12

        Returns:
            float: the value of `angle_factor_12` or None if not set
        """
        return self._data["Angle Factor 12"]

    @angle_factor_12.setter
    def angle_factor_12(self, value=None):
        """  Corresponds to IDD Field `angle_factor_12`

        Args:
            value (float): value for IDD Field `angle_factor_12`
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
                                 'for field `angle_factor_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_12`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_12`')

        self._data["Angle Factor 12"] = value

    @property
    def surface_13_name(self):
        """Get surface_13_name

        Returns:
            str: the value of `surface_13_name` or None if not set
        """
        return self._data["Surface 13 Name"]

    @surface_13_name.setter
    def surface_13_name(self, value=None):
        """  Corresponds to IDD Field `surface_13_name`

        Args:
            value (str): value for IDD Field `surface_13_name`
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
                                 'for field `surface_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_13_name`')

        self._data["Surface 13 Name"] = value

    @property
    def angle_factor_13(self):
        """Get angle_factor_13

        Returns:
            float: the value of `angle_factor_13` or None if not set
        """
        return self._data["Angle Factor 13"]

    @angle_factor_13.setter
    def angle_factor_13(self, value=None):
        """  Corresponds to IDD Field `angle_factor_13`

        Args:
            value (float): value for IDD Field `angle_factor_13`
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
                                 'for field `angle_factor_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_13`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_13`')

        self._data["Angle Factor 13"] = value

    @property
    def surface_14_name(self):
        """Get surface_14_name

        Returns:
            str: the value of `surface_14_name` or None if not set
        """
        return self._data["Surface 14 Name"]

    @surface_14_name.setter
    def surface_14_name(self, value=None):
        """  Corresponds to IDD Field `surface_14_name`

        Args:
            value (str): value for IDD Field `surface_14_name`
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
                                 'for field `surface_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_14_name`')

        self._data["Surface 14 Name"] = value

    @property
    def angle_factor_14(self):
        """Get angle_factor_14

        Returns:
            float: the value of `angle_factor_14` or None if not set
        """
        return self._data["Angle Factor 14"]

    @angle_factor_14.setter
    def angle_factor_14(self, value=None):
        """  Corresponds to IDD Field `angle_factor_14`

        Args:
            value (float): value for IDD Field `angle_factor_14`
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
                                 'for field `angle_factor_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_14`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_14`')

        self._data["Angle Factor 14"] = value

    @property
    def surface_15_name(self):
        """Get surface_15_name

        Returns:
            str: the value of `surface_15_name` or None if not set
        """
        return self._data["Surface 15 Name"]

    @surface_15_name.setter
    def surface_15_name(self, value=None):
        """  Corresponds to IDD Field `surface_15_name`

        Args:
            value (str): value for IDD Field `surface_15_name`
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
                                 'for field `surface_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_15_name`')

        self._data["Surface 15 Name"] = value

    @property
    def angle_factor_15(self):
        """Get angle_factor_15

        Returns:
            float: the value of `angle_factor_15` or None if not set
        """
        return self._data["Angle Factor 15"]

    @angle_factor_15.setter
    def angle_factor_15(self, value=None):
        """  Corresponds to IDD Field `angle_factor_15`

        Args:
            value (float): value for IDD Field `angle_factor_15`
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
                                 'for field `angle_factor_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_15`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_15`')

        self._data["Angle Factor 15"] = value

    @property
    def surface_16_name(self):
        """Get surface_16_name

        Returns:
            str: the value of `surface_16_name` or None if not set
        """
        return self._data["Surface 16 Name"]

    @surface_16_name.setter
    def surface_16_name(self, value=None):
        """  Corresponds to IDD Field `surface_16_name`

        Args:
            value (str): value for IDD Field `surface_16_name`
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
                                 'for field `surface_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_16_name`')

        self._data["Surface 16 Name"] = value

    @property
    def angle_factor_16(self):
        """Get angle_factor_16

        Returns:
            float: the value of `angle_factor_16` or None if not set
        """
        return self._data["Angle Factor 16"]

    @angle_factor_16.setter
    def angle_factor_16(self, value=None):
        """  Corresponds to IDD Field `angle_factor_16`

        Args:
            value (float): value for IDD Field `angle_factor_16`
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
                                 'for field `angle_factor_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_16`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_16`')

        self._data["Angle Factor 16"] = value

    @property
    def surface_17_name(self):
        """Get surface_17_name

        Returns:
            str: the value of `surface_17_name` or None if not set
        """
        return self._data["Surface 17 Name"]

    @surface_17_name.setter
    def surface_17_name(self, value=None):
        """  Corresponds to IDD Field `surface_17_name`

        Args:
            value (str): value for IDD Field `surface_17_name`
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
                                 'for field `surface_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_17_name`')

        self._data["Surface 17 Name"] = value

    @property
    def angle_factor_17(self):
        """Get angle_factor_17

        Returns:
            float: the value of `angle_factor_17` or None if not set
        """
        return self._data["Angle Factor 17"]

    @angle_factor_17.setter
    def angle_factor_17(self, value=None):
        """  Corresponds to IDD Field `angle_factor_17`

        Args:
            value (float): value for IDD Field `angle_factor_17`
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
                                 'for field `angle_factor_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_17`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_17`')

        self._data["Angle Factor 17"] = value

    @property
    def surface_18_name(self):
        """Get surface_18_name

        Returns:
            str: the value of `surface_18_name` or None if not set
        """
        return self._data["Surface 18 Name"]

    @surface_18_name.setter
    def surface_18_name(self, value=None):
        """  Corresponds to IDD Field `surface_18_name`

        Args:
            value (str): value for IDD Field `surface_18_name`
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
                                 'for field `surface_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_18_name`')

        self._data["Surface 18 Name"] = value

    @property
    def angle_factor_18(self):
        """Get angle_factor_18

        Returns:
            float: the value of `angle_factor_18` or None if not set
        """
        return self._data["Angle Factor 18"]

    @angle_factor_18.setter
    def angle_factor_18(self, value=None):
        """  Corresponds to IDD Field `angle_factor_18`

        Args:
            value (float): value for IDD Field `angle_factor_18`
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
                                 'for field `angle_factor_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_18`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_18`')

        self._data["Angle Factor 18"] = value

    @property
    def surface_19_name(self):
        """Get surface_19_name

        Returns:
            str: the value of `surface_19_name` or None if not set
        """
        return self._data["Surface 19 Name"]

    @surface_19_name.setter
    def surface_19_name(self, value=None):
        """  Corresponds to IDD Field `surface_19_name`

        Args:
            value (str): value for IDD Field `surface_19_name`
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
                                 'for field `surface_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_19_name`')

        self._data["Surface 19 Name"] = value

    @property
    def angle_factor_19(self):
        """Get angle_factor_19

        Returns:
            float: the value of `angle_factor_19` or None if not set
        """
        return self._data["Angle Factor 19"]

    @angle_factor_19.setter
    def angle_factor_19(self, value=None):
        """  Corresponds to IDD Field `angle_factor_19`

        Args:
            value (float): value for IDD Field `angle_factor_19`
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
                                 'for field `angle_factor_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_19`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_19`')

        self._data["Angle Factor 19"] = value

    @property
    def surface_20_name(self):
        """Get surface_20_name

        Returns:
            str: the value of `surface_20_name` or None if not set
        """
        return self._data["Surface 20 Name"]

    @surface_20_name.setter
    def surface_20_name(self, value=None):
        """  Corresponds to IDD Field `surface_20_name`

        Args:
            value (str): value for IDD Field `surface_20_name`
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
                                 'for field `surface_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_20_name`')

        self._data["Surface 20 Name"] = value

    @property
    def angle_factor_20(self):
        """Get angle_factor_20

        Returns:
            float: the value of `angle_factor_20` or None if not set
        """
        return self._data["Angle Factor 20"]

    @angle_factor_20.setter
    def angle_factor_20(self, value=None):
        """  Corresponds to IDD Field `angle_factor_20`

        Args:
            value (float): value for IDD Field `angle_factor_20`
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
                                 'for field `angle_factor_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `angle_factor_20`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `angle_factor_20`')

        self._data["Angle Factor 20"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.surface_1_name))
        out.append(self._to_str(self.angle_factor_1))
        out.append(self._to_str(self.surface_2_name))
        out.append(self._to_str(self.angle_factor_2))
        out.append(self._to_str(self.surface_3_name))
        out.append(self._to_str(self.angle_factor_3))
        out.append(self._to_str(self.surface_4_name))
        out.append(self._to_str(self.angle_factor_4))
        out.append(self._to_str(self.surface_5_name))
        out.append(self._to_str(self.angle_factor_5))
        out.append(self._to_str(self.surface_6_name))
        out.append(self._to_str(self.angle_factor_6))
        out.append(self._to_str(self.surface_7_name))
        out.append(self._to_str(self.angle_factor_7))
        out.append(self._to_str(self.surface_8_name))
        out.append(self._to_str(self.angle_factor_8))
        out.append(self._to_str(self.surface_9_name))
        out.append(self._to_str(self.angle_factor_9))
        out.append(self._to_str(self.surface_10_name))
        out.append(self._to_str(self.angle_factor_10))
        out.append(self._to_str(self.surface_11_name))
        out.append(self._to_str(self.angle_factor_11))
        out.append(self._to_str(self.surface_12_name))
        out.append(self._to_str(self.angle_factor_12))
        out.append(self._to_str(self.surface_13_name))
        out.append(self._to_str(self.angle_factor_13))
        out.append(self._to_str(self.surface_14_name))
        out.append(self._to_str(self.angle_factor_14))
        out.append(self._to_str(self.surface_15_name))
        out.append(self._to_str(self.angle_factor_15))
        out.append(self._to_str(self.surface_16_name))
        out.append(self._to_str(self.angle_factor_16))
        out.append(self._to_str(self.surface_17_name))
        out.append(self._to_str(self.angle_factor_17))
        out.append(self._to_str(self.surface_18_name))
        out.append(self._to_str(self.angle_factor_18))
        out.append(self._to_str(self.surface_19_name))
        out.append(self._to_str(self.angle_factor_19))
        out.append(self._to_str(self.surface_20_name))
        out.append(self._to_str(self.angle_factor_20))
        return ",".join(out)

class Lights(object):
    """ Corresponds to IDD object `Lights`
        Sets internal gains for lights in the zone.
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    """
    internal_name = "Lights"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for IDD  `Lights`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Level Calculation Method"] = None
        self._data["Lighting Level"] = None
        self._data["Watts per Zone Floor Area"] = None
        self._data["Watts per Person"] = None
        self._data["Return Air Fraction"] = None
        self._data["Fraction Radiant"] = None
        self._data["Fraction Visible"] = None
        self._data["Fraction Replaceable"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Return Air Fraction Calculated from Plenum Temperature"] = None
        self._data["Return Air Fraction Function of Plenum Temperature Coefficient 1"] = None
        self._data["Return Air Fraction Function of Plenum Temperature Coefficient 2"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level_calculation_method = None
        else:
            self.design_level_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lighting_level = None
        else:
            self.lighting_level = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.watts_per_zone_floor_area = None
        else:
            self.watts_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.watts_per_person = None
        else:
            self.watts_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.return_air_fraction = None
        else:
            self.return_air_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_visible = None
        else:
            self.fraction_visible = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_replaceable = None
        else:
            self.fraction_replaceable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.return_air_fraction_calculated_from_plenum_temperature = None
        else:
            self.return_air_fraction_calculated_from_plenum_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.return_air_fraction_function_of_plenum_temperature_coefficient_1 = None
        else:
            self.return_air_fraction_function_of_plenum_temperature_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.return_air_fraction_function_of_plenum_temperature_coefficient_2 = None
        else:
            self.return_air_fraction_function_of_plenum_temperature_coefficient_2 = vals[i]
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
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        units in schedule should be fraction applied to design level of lights, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """Get design_level_calculation_method

        Returns:
            str: the value of `design_level_calculation_method` or None if not set
        """
        return self._data["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="LightingLevel"):
        """  Corresponds to IDD Field `design_level_calculation_method`
        The entered calculation method is used to create the maximum amount of lights
        for this set of attributes
        Choices: LightingLevel => Lighting Level -- simply enter watts of lights
        Watts/Area => Watts per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Lights
        Watts/Person => Watts per Person -- enter the number to apply.  Value * Occupants = Lights

        Args:
            value (str): value for IDD Field `design_level_calculation_method`
                Accepted values are:
                      - LightingLevel
                      - Watts/Area
                      - Watts/Person
                Default value: LightingLevel
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
                                 'for field `design_level_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_level_calculation_method`')
            vals = set()
            vals.add("LightingLevel")
            vals.add("Watts/Area")
            vals.add("Watts/Person")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_level_calculation_method`'.format(value))

        self._data["Design Level Calculation Method"] = value

    @property
    def lighting_level(self):
        """Get lighting_level

        Returns:
            float: the value of `lighting_level` or None if not set
        """
        return self._data["Lighting Level"]

    @lighting_level.setter
    def lighting_level(self, value=None):
        """  Corresponds to IDD Field `lighting_level`

        Args:
            value (float): value for IDD Field `lighting_level`
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
                                 'for field `lighting_level`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `lighting_level`')

        self._data["Lighting Level"] = value

    @property
    def watts_per_zone_floor_area(self):
        """Get watts_per_zone_floor_area

        Returns:
            float: the value of `watts_per_zone_floor_area` or None if not set
        """
        return self._data["Watts per Zone Floor Area"]

    @watts_per_zone_floor_area.setter
    def watts_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `watts_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `watts_per_zone_floor_area`
                Unit: W/m2
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
                                 'for field `watts_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `watts_per_zone_floor_area`')

        self._data["Watts per Zone Floor Area"] = value

    @property
    def watts_per_person(self):
        """Get watts_per_person

        Returns:
            float: the value of `watts_per_person` or None if not set
        """
        return self._data["Watts per Person"]

    @watts_per_person.setter
    def watts_per_person(self, value=None):
        """  Corresponds to IDD Field `watts_per_person`

        Args:
            value (float): value for IDD Field `watts_per_person`
                Unit: W/person
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
                                 'for field `watts_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `watts_per_person`')

        self._data["Watts per Person"] = value

    @property
    def return_air_fraction(self):
        """Get return_air_fraction

        Returns:
            float: the value of `return_air_fraction` or None if not set
        """
        return self._data["Return Air Fraction"]

    @return_air_fraction.setter
    def return_air_fraction(self, value=0.0 ):
        """  Corresponds to IDD Field `return_air_fraction`
        Used only for sizing calculation if return-air-fraction
        coefficients are specified.

        Args:
            value (float): value for IDD Field `return_air_fraction`
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
                                 'for field `return_air_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `return_air_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `return_air_fraction`')

        self._data["Return Air Fraction"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_radiant`

        Args:
            value (float): value for IDD Field `fraction_radiant`
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
                                 'for field `fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_radiant`')

        self._data["Fraction Radiant"] = value

    @property
    def fraction_visible(self):
        """Get fraction_visible

        Returns:
            float: the value of `fraction_visible` or None if not set
        """
        return self._data["Fraction Visible"]

    @fraction_visible.setter
    def fraction_visible(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_visible`

        Args:
            value (float): value for IDD Field `fraction_visible`
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
                                 'for field `fraction_visible`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_visible`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_visible`')

        self._data["Fraction Visible"] = value

    @property
    def fraction_replaceable(self):
        """Get fraction_replaceable

        Returns:
            float: the value of `fraction_replaceable` or None if not set
        """
        return self._data["Fraction Replaceable"]

    @fraction_replaceable.setter
    def fraction_replaceable(self, value=1.0 ):
        """  Corresponds to IDD Field `fraction_replaceable`
        For Daylighting:Controls and Daylighting:DElight:Controls,
        must be 0 or 1:  0 = no dimming control, 1 = full dimming control

        Args:
            value (float): value for IDD Field `fraction_replaceable`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_replaceable`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_replaceable`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_replaceable`')

        self._data["Fraction Replaceable"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `enduse_subcategory`

        Args:
            value (str): value for IDD Field `enduse_subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')

        self._data["End-Use Subcategory"] = value

    @property
    def return_air_fraction_calculated_from_plenum_temperature(self):
        """Get return_air_fraction_calculated_from_plenum_temperature

        Returns:
            str: the value of `return_air_fraction_calculated_from_plenum_temperature` or None if not set
        """
        return self._data["Return Air Fraction Calculated from Plenum Temperature"]

    @return_air_fraction_calculated_from_plenum_temperature.setter
    def return_air_fraction_calculated_from_plenum_temperature(self, value="No"):
        """  Corresponds to IDD Field `return_air_fraction_calculated_from_plenum_temperature`

        Args:
            value (str): value for IDD Field `return_air_fraction_calculated_from_plenum_temperature`
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
                                 'for field `return_air_fraction_calculated_from_plenum_temperature`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `return_air_fraction_calculated_from_plenum_temperature`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `return_air_fraction_calculated_from_plenum_temperature`'.format(value))

        self._data["Return Air Fraction Calculated from Plenum Temperature"] = value

    @property
    def return_air_fraction_function_of_plenum_temperature_coefficient_1(self):
        """Get return_air_fraction_function_of_plenum_temperature_coefficient_1

        Returns:
            float: the value of `return_air_fraction_function_of_plenum_temperature_coefficient_1` or None if not set
        """
        return self._data["Return Air Fraction Function of Plenum Temperature Coefficient 1"]

    @return_air_fraction_function_of_plenum_temperature_coefficient_1.setter
    def return_air_fraction_function_of_plenum_temperature_coefficient_1(self, value=0.0 ):
        """  Corresponds to IDD Field `return_air_fraction_function_of_plenum_temperature_coefficient_1`
        Used only if Return Air Fraction Is Calculated from Plenum Temperature = Yes
        Equation is Return Air Fraction = Coefficient#1 - Coefficient#2 X PlenumTemp(degC)

        Args:
            value (float): value for IDD Field `return_air_fraction_function_of_plenum_temperature_coefficient_1`
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
                                 'for field `return_air_fraction_function_of_plenum_temperature_coefficient_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `return_air_fraction_function_of_plenum_temperature_coefficient_1`')

        self._data["Return Air Fraction Function of Plenum Temperature Coefficient 1"] = value

    @property
    def return_air_fraction_function_of_plenum_temperature_coefficient_2(self):
        """Get return_air_fraction_function_of_plenum_temperature_coefficient_2

        Returns:
            float: the value of `return_air_fraction_function_of_plenum_temperature_coefficient_2` or None if not set
        """
        return self._data["Return Air Fraction Function of Plenum Temperature Coefficient 2"]

    @return_air_fraction_function_of_plenum_temperature_coefficient_2.setter
    def return_air_fraction_function_of_plenum_temperature_coefficient_2(self, value=0.0 ):
        """  Corresponds to IDD Field `return_air_fraction_function_of_plenum_temperature_coefficient_2`
        Used only if Return Air Fraction Is Calculated from Plenum Temperature = Yes
        Equation is Return Air Fraction = Coefficient#1 - Coefficient#2 X PlenumTemp(degC)

        Args:
            value (float): value for IDD Field `return_air_fraction_function_of_plenum_temperature_coefficient_2`
                Unit: 1/K
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
                                 'for field `return_air_fraction_function_of_plenum_temperature_coefficient_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `return_air_fraction_function_of_plenum_temperature_coefficient_2`')

        self._data["Return Air Fraction Function of Plenum Temperature Coefficient 2"] = value

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
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.design_level_calculation_method))
        out.append(self._to_str(self.lighting_level))
        out.append(self._to_str(self.watts_per_zone_floor_area))
        out.append(self._to_str(self.watts_per_person))
        out.append(self._to_str(self.return_air_fraction))
        out.append(self._to_str(self.fraction_radiant))
        out.append(self._to_str(self.fraction_visible))
        out.append(self._to_str(self.fraction_replaceable))
        out.append(self._to_str(self.enduse_subcategory))
        out.append(self._to_str(self.return_air_fraction_calculated_from_plenum_temperature))
        out.append(self._to_str(self.return_air_fraction_function_of_plenum_temperature_coefficient_1))
        out.append(self._to_str(self.return_air_fraction_function_of_plenum_temperature_coefficient_2))
        return ",".join(out)

class ElectricEquipment(object):
    """ Corresponds to IDD object `ElectricEquipment`
        Sets internal gains for electric equipment in the zone.
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    """
    internal_name = "ElectricEquipment"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for IDD  `ElectricEquipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Level Calculation Method"] = None
        self._data["Design Level"] = None
        self._data["Watts per Zone Floor Area"] = None
        self._data["Watts per Person"] = None
        self._data["Fraction Latent"] = None
        self._data["Fraction Radiant"] = None
        self._data["Fraction Lost"] = None
        self._data["End-Use Subcategory"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level_calculation_method = None
        else:
            self.design_level_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level = None
        else:
            self.design_level = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.watts_per_zone_floor_area = None
        else:
            self.watts_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.watts_per_person = None
        else:
            self.watts_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_latent = None
        else:
            self.fraction_latent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_lost = None
        else:
            self.fraction_lost = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
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
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        units in schedule should be fraction applied to design level of electric equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """Get design_level_calculation_method

        Returns:
            str: the value of `design_level_calculation_method` or None if not set
        """
        return self._data["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """  Corresponds to IDD Field `design_level_calculation_method`
        The entered calculation method is used to create the maximum amount of electric equipment
        for this set of attributes
        Choices: EquipmentLevel => Equipment Level -- simply enter watts of equipment
        Watts/Area => Watts per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        Watts/Person => Watts per Person -- enter the number to apply.  Value * Occupants = Equipment Level

        Args:
            value (str): value for IDD Field `design_level_calculation_method`
                Accepted values are:
                      - EquipmentLevel
                      - Watts/Area
                      - Watts/Person
                Default value: EquipmentLevel
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
                                 'for field `design_level_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_level_calculation_method`')
            vals = set()
            vals.add("EquipmentLevel")
            vals.add("Watts/Area")
            vals.add("Watts/Person")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_level_calculation_method`'.format(value))

        self._data["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """Get design_level

        Returns:
            float: the value of `design_level` or None if not set
        """
        return self._data["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """  Corresponds to IDD Field `design_level`

        Args:
            value (float): value for IDD Field `design_level`
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
                                 'for field `design_level`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_level`')

        self._data["Design Level"] = value

    @property
    def watts_per_zone_floor_area(self):
        """Get watts_per_zone_floor_area

        Returns:
            float: the value of `watts_per_zone_floor_area` or None if not set
        """
        return self._data["Watts per Zone Floor Area"]

    @watts_per_zone_floor_area.setter
    def watts_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `watts_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `watts_per_zone_floor_area`
                Unit: W/m2
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
                                 'for field `watts_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `watts_per_zone_floor_area`')

        self._data["Watts per Zone Floor Area"] = value

    @property
    def watts_per_person(self):
        """Get watts_per_person

        Returns:
            float: the value of `watts_per_person` or None if not set
        """
        return self._data["Watts per Person"]

    @watts_per_person.setter
    def watts_per_person(self, value=None):
        """  Corresponds to IDD Field `watts_per_person`

        Args:
            value (float): value for IDD Field `watts_per_person`
                Unit: W/person
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
                                 'for field `watts_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `watts_per_person`')

        self._data["Watts per Person"] = value

    @property
    def fraction_latent(self):
        """Get fraction_latent

        Returns:
            float: the value of `fraction_latent` or None if not set
        """
        return self._data["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_latent`

        Args:
            value (float): value for IDD Field `fraction_latent`
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
                                 'for field `fraction_latent`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_latent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_latent`')

        self._data["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_radiant`

        Args:
            value (float): value for IDD Field `fraction_radiant`
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
                                 'for field `fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_radiant`')

        self._data["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """Get fraction_lost

        Returns:
            float: the value of `fraction_lost` or None if not set
        """
        return self._data["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_lost`

        Args:
            value (float): value for IDD Field `fraction_lost`
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
                                 'for field `fraction_lost`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_lost`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_lost`')

        self._data["Fraction Lost"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `enduse_subcategory`

        Args:
            value (str): value for IDD Field `enduse_subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')

        self._data["End-Use Subcategory"] = value

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
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.design_level_calculation_method))
        out.append(self._to_str(self.design_level))
        out.append(self._to_str(self.watts_per_zone_floor_area))
        out.append(self._to_str(self.watts_per_person))
        out.append(self._to_str(self.fraction_latent))
        out.append(self._to_str(self.fraction_radiant))
        out.append(self._to_str(self.fraction_lost))
        out.append(self._to_str(self.enduse_subcategory))
        return ",".join(out)

class GasEquipment(object):
    """ Corresponds to IDD object `GasEquipment`
        Sets internal gains and contaminant rates for gas equipment in the zone.
        If you use a ZoneList in the Zone name field then this definition applies to all those zones.
    """
    internal_name = "GasEquipment"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for IDD  `GasEquipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Level Calculation Method"] = None
        self._data["Design Level"] = None
        self._data["Power per Zone Floor Area"] = None
        self._data["Power per Person"] = None
        self._data["Fraction Latent"] = None
        self._data["Fraction Radiant"] = None
        self._data["Fraction Lost"] = None
        self._data["Carbon Dioxide Generation Rate"] = None
        self._data["End-Use Subcategory"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level_calculation_method = None
        else:
            self.design_level_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level = None
        else:
            self.design_level = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_zone_floor_area = None
        else:
            self.power_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_person = None
        else:
            self.power_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_latent = None
        else:
            self.fraction_latent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_lost = None
        else:
            self.fraction_lost = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.carbon_dioxide_generation_rate = None
        else:
            self.carbon_dioxide_generation_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
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
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        units in Schedule should be fraction applied to design level of gas equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """Get design_level_calculation_method

        Returns:
            str: the value of `design_level_calculation_method` or None if not set
        """
        return self._data["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """  Corresponds to IDD Field `design_level_calculation_method`
        The entered calculation method is used to create the maximum amount of gas equipment
        for this set of attributes
        Choices: EquipmentLevel => Design Level -- simply enter power input of equipment
        Watts/Area or Power/Area => Power per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        Watts/Person or Power/Person => Power per Person -- enter the number to apply.  Value * Occupants = Equipment Level

        Args:
            value (str): value for IDD Field `design_level_calculation_method`
                Accepted values are:
                      - EquipmentLevel
                      - Watts/Area
                      - Watts/Person
                      - Power/Area
                      - Power/Person
                Default value: EquipmentLevel
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
                                 'for field `design_level_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_level_calculation_method`')
            vals = set()
            vals.add("EquipmentLevel")
            vals.add("Watts/Area")
            vals.add("Watts/Person")
            vals.add("Power/Area")
            vals.add("Power/Person")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_level_calculation_method`'.format(value))

        self._data["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """Get design_level

        Returns:
            float: the value of `design_level` or None if not set
        """
        return self._data["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """  Corresponds to IDD Field `design_level`

        Args:
            value (float): value for IDD Field `design_level`
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
                                 'for field `design_level`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_level`')

        self._data["Design Level"] = value

    @property
    def power_per_zone_floor_area(self):
        """Get power_per_zone_floor_area

        Returns:
            float: the value of `power_per_zone_floor_area` or None if not set
        """
        return self._data["Power per Zone Floor Area"]

    @power_per_zone_floor_area.setter
    def power_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `power_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `power_per_zone_floor_area`
                Unit: W/m2
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
                                 'for field `power_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `power_per_zone_floor_area`')

        self._data["Power per Zone Floor Area"] = value

    @property
    def power_per_person(self):
        """Get power_per_person

        Returns:
            float: the value of `power_per_person` or None if not set
        """
        return self._data["Power per Person"]

    @power_per_person.setter
    def power_per_person(self, value=None):
        """  Corresponds to IDD Field `power_per_person`

        Args:
            value (float): value for IDD Field `power_per_person`
                Unit: W/Person
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
                                 'for field `power_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `power_per_person`')

        self._data["Power per Person"] = value

    @property
    def fraction_latent(self):
        """Get fraction_latent

        Returns:
            float: the value of `fraction_latent` or None if not set
        """
        return self._data["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_latent`

        Args:
            value (float): value for IDD Field `fraction_latent`
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
                                 'for field `fraction_latent`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_latent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_latent`')

        self._data["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_radiant`

        Args:
            value (float): value for IDD Field `fraction_radiant`
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
                                 'for field `fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_radiant`')

        self._data["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """Get fraction_lost

        Returns:
            float: the value of `fraction_lost` or None if not set
        """
        return self._data["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_lost`

        Args:
            value (float): value for IDD Field `fraction_lost`
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
                                 'for field `fraction_lost`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_lost`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_lost`')

        self._data["Fraction Lost"] = value

    @property
    def carbon_dioxide_generation_rate(self):
        """Get carbon_dioxide_generation_rate

        Returns:
            float: the value of `carbon_dioxide_generation_rate` or None if not set
        """
        return self._data["Carbon Dioxide Generation Rate"]

    @carbon_dioxide_generation_rate.setter
    def carbon_dioxide_generation_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `carbon_dioxide_generation_rate`
        CO2 generation rate per unit of power input
        The default value assumes the equipment is fully vented.
        For unvented equipment, a suggested value is 3.45E-8 m3/s-W. This value is
        converted from a natural gas CO2 emission rate of 117 lbs CO2 per million Btu.
        The maximum value assumes to be 10 times of the recommended value.

        Args:
            value (float): value for IDD Field `carbon_dioxide_generation_rate`
                Unit: m3/s-W
                Default value: 0.0
                value >= 0.0
                value <= 4e-07
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
            if value > 4e-07:
                raise ValueError('value need to be smaller 4e-07 '
                                 'for field `carbon_dioxide_generation_rate`')

        self._data["Carbon Dioxide Generation Rate"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `enduse_subcategory`

        Args:
            value (str): value for IDD Field `enduse_subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')

        self._data["End-Use Subcategory"] = value

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
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.design_level_calculation_method))
        out.append(self._to_str(self.design_level))
        out.append(self._to_str(self.power_per_zone_floor_area))
        out.append(self._to_str(self.power_per_person))
        out.append(self._to_str(self.fraction_latent))
        out.append(self._to_str(self.fraction_radiant))
        out.append(self._to_str(self.fraction_lost))
        out.append(self._to_str(self.carbon_dioxide_generation_rate))
        out.append(self._to_str(self.enduse_subcategory))
        return ",".join(out)

class HotWaterEquipment(object):
    """ Corresponds to IDD object `HotWaterEquipment`
        Sets internal gains for hot water equipment in the zone.
        If you use a ZoneList in the Zone name field then this definition applies to all those zones.
    """
    internal_name = "HotWaterEquipment"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for IDD  `HotWaterEquipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Level Calculation Method"] = None
        self._data["Design Level"] = None
        self._data["Power per Zone Floor Area"] = None
        self._data["Power per Person"] = None
        self._data["Fraction Latent"] = None
        self._data["Fraction Radiant"] = None
        self._data["Fraction Lost"] = None
        self._data["End-Use Subcategory"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level_calculation_method = None
        else:
            self.design_level_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level = None
        else:
            self.design_level = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_zone_floor_area = None
        else:
            self.power_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_person = None
        else:
            self.power_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_latent = None
        else:
            self.fraction_latent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_lost = None
        else:
            self.fraction_lost = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
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
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        units in Schedule should be fraction applied to design level of hot water equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """Get design_level_calculation_method

        Returns:
            str: the value of `design_level_calculation_method` or None if not set
        """
        return self._data["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """  Corresponds to IDD Field `design_level_calculation_method`
        The entered calculation method is used to create the maximum amount of hot water equipment
        for this set of attributes
        Choices: EquipmentLevel => Design Level -- simply enter power input of equipment
        Watts/Area or Power/Area => Power per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        Watts/Person or Power/Person => Power per Person -- enter the number to apply.  Value * Occupants = Equipment Level

        Args:
            value (str): value for IDD Field `design_level_calculation_method`
                Accepted values are:
                      - EquipmentLevel
                      - Watts/Area
                      - Watts/Person
                      - Power/Area
                      - Power/Person
                Default value: EquipmentLevel
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
                                 'for field `design_level_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_level_calculation_method`')
            vals = set()
            vals.add("EquipmentLevel")
            vals.add("Watts/Area")
            vals.add("Watts/Person")
            vals.add("Power/Area")
            vals.add("Power/Person")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_level_calculation_method`'.format(value))

        self._data["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """Get design_level

        Returns:
            float: the value of `design_level` or None if not set
        """
        return self._data["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """  Corresponds to IDD Field `design_level`

        Args:
            value (float): value for IDD Field `design_level`
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
                                 'for field `design_level`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_level`')

        self._data["Design Level"] = value

    @property
    def power_per_zone_floor_area(self):
        """Get power_per_zone_floor_area

        Returns:
            float: the value of `power_per_zone_floor_area` or None if not set
        """
        return self._data["Power per Zone Floor Area"]

    @power_per_zone_floor_area.setter
    def power_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `power_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `power_per_zone_floor_area`
                Unit: W/m2
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
                                 'for field `power_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `power_per_zone_floor_area`')

        self._data["Power per Zone Floor Area"] = value

    @property
    def power_per_person(self):
        """Get power_per_person

        Returns:
            float: the value of `power_per_person` or None if not set
        """
        return self._data["Power per Person"]

    @power_per_person.setter
    def power_per_person(self, value=None):
        """  Corresponds to IDD Field `power_per_person`

        Args:
            value (float): value for IDD Field `power_per_person`
                Unit: W/Person
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
                                 'for field `power_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `power_per_person`')

        self._data["Power per Person"] = value

    @property
    def fraction_latent(self):
        """Get fraction_latent

        Returns:
            float: the value of `fraction_latent` or None if not set
        """
        return self._data["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_latent`

        Args:
            value (float): value for IDD Field `fraction_latent`
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
                                 'for field `fraction_latent`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_latent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_latent`')

        self._data["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_radiant`

        Args:
            value (float): value for IDD Field `fraction_radiant`
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
                                 'for field `fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_radiant`')

        self._data["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """Get fraction_lost

        Returns:
            float: the value of `fraction_lost` or None if not set
        """
        return self._data["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_lost`

        Args:
            value (float): value for IDD Field `fraction_lost`
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
                                 'for field `fraction_lost`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_lost`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_lost`')

        self._data["Fraction Lost"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `enduse_subcategory`

        Args:
            value (str): value for IDD Field `enduse_subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')

        self._data["End-Use Subcategory"] = value

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
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.design_level_calculation_method))
        out.append(self._to_str(self.design_level))
        out.append(self._to_str(self.power_per_zone_floor_area))
        out.append(self._to_str(self.power_per_person))
        out.append(self._to_str(self.fraction_latent))
        out.append(self._to_str(self.fraction_radiant))
        out.append(self._to_str(self.fraction_lost))
        out.append(self._to_str(self.enduse_subcategory))
        return ",".join(out)

class SteamEquipment(object):
    """ Corresponds to IDD object `SteamEquipment`
        Sets internal gains for steam equipment in the zone.
    """
    internal_name = "SteamEquipment"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for IDD  `SteamEquipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Level Calculation Method"] = None
        self._data["Design Level"] = None
        self._data["Power per Zone Floor Area"] = None
        self._data["Power per Person"] = None
        self._data["Fraction Latent"] = None
        self._data["Fraction Radiant"] = None
        self._data["Fraction Lost"] = None
        self._data["End-Use Subcategory"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level_calculation_method = None
        else:
            self.design_level_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level = None
        else:
            self.design_level = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_zone_floor_area = None
        else:
            self.power_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_person = None
        else:
            self.power_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_latent = None
        else:
            self.fraction_latent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_lost = None
        else:
            self.fraction_lost = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
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
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        units in Schedule should be fraction applied to design level of steam equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """Get design_level_calculation_method

        Returns:
            str: the value of `design_level_calculation_method` or None if not set
        """
        return self._data["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """  Corresponds to IDD Field `design_level_calculation_method`
        The entered calculation method is used to create the maximum amount of steam equipment
        for this set of attributes
        Choices: EquipmentLevel => Design Level -- simply enter power input of equipment
        Watts/Area or Power/Area => Power per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        Watts/Person or Power/Person => Power per Person -- enter the number to apply.  Value * Occupants = Equipment Level

        Args:
            value (str): value for IDD Field `design_level_calculation_method`
                Accepted values are:
                      - EquipmentLevel
                      - Watts/Area
                      - Watts/Person
                      - Power/Area
                      - Power/Person
                Default value: EquipmentLevel
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
                                 'for field `design_level_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_level_calculation_method`')
            vals = set()
            vals.add("EquipmentLevel")
            vals.add("Watts/Area")
            vals.add("Watts/Person")
            vals.add("Power/Area")
            vals.add("Power/Person")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_level_calculation_method`'.format(value))

        self._data["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """Get design_level

        Returns:
            float: the value of `design_level` or None if not set
        """
        return self._data["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """  Corresponds to IDD Field `design_level`

        Args:
            value (float): value for IDD Field `design_level`
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
                                 'for field `design_level`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_level`')

        self._data["Design Level"] = value

    @property
    def power_per_zone_floor_area(self):
        """Get power_per_zone_floor_area

        Returns:
            float: the value of `power_per_zone_floor_area` or None if not set
        """
        return self._data["Power per Zone Floor Area"]

    @power_per_zone_floor_area.setter
    def power_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `power_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `power_per_zone_floor_area`
                Unit: W/m2
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
                                 'for field `power_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `power_per_zone_floor_area`')

        self._data["Power per Zone Floor Area"] = value

    @property
    def power_per_person(self):
        """Get power_per_person

        Returns:
            float: the value of `power_per_person` or None if not set
        """
        return self._data["Power per Person"]

    @power_per_person.setter
    def power_per_person(self, value=None):
        """  Corresponds to IDD Field `power_per_person`

        Args:
            value (float): value for IDD Field `power_per_person`
                Unit: W/Person
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
                                 'for field `power_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `power_per_person`')

        self._data["Power per Person"] = value

    @property
    def fraction_latent(self):
        """Get fraction_latent

        Returns:
            float: the value of `fraction_latent` or None if not set
        """
        return self._data["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_latent`

        Args:
            value (float): value for IDD Field `fraction_latent`
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
                                 'for field `fraction_latent`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_latent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_latent`')

        self._data["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_radiant`

        Args:
            value (float): value for IDD Field `fraction_radiant`
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
                                 'for field `fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_radiant`')

        self._data["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """Get fraction_lost

        Returns:
            float: the value of `fraction_lost` or None if not set
        """
        return self._data["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_lost`

        Args:
            value (float): value for IDD Field `fraction_lost`
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
                                 'for field `fraction_lost`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_lost`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_lost`')

        self._data["Fraction Lost"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `enduse_subcategory`

        Args:
            value (str): value for IDD Field `enduse_subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')

        self._data["End-Use Subcategory"] = value

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
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.design_level_calculation_method))
        out.append(self._to_str(self.design_level))
        out.append(self._to_str(self.power_per_zone_floor_area))
        out.append(self._to_str(self.power_per_person))
        out.append(self._to_str(self.fraction_latent))
        out.append(self._to_str(self.fraction_radiant))
        out.append(self._to_str(self.fraction_lost))
        out.append(self._to_str(self.enduse_subcategory))
        return ",".join(out)

class OtherEquipment(object):
    """ Corresponds to IDD object `OtherEquipment`
        Sets internal gains or losses for "other" equipment in the zone.
    """
    internal_name = "OtherEquipment"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for IDD  `OtherEquipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Level Calculation Method"] = None
        self._data["Design Level"] = None
        self._data["Power per Zone Floor Area"] = None
        self._data["Power per Person"] = None
        self._data["Fraction Latent"] = None
        self._data["Fraction Radiant"] = None
        self._data["Fraction Lost"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level_calculation_method = None
        else:
            self.design_level_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_level = None
        else:
            self.design_level = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_zone_floor_area = None
        else:
            self.power_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.power_per_person = None
        else:
            self.power_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_latent = None
        else:
            self.fraction_latent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_lost = None
        else:
            self.fraction_lost = vals[i]
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
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        units in Schedule should be fraction applied to design level of other equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """Get design_level_calculation_method

        Returns:
            str: the value of `design_level_calculation_method` or None if not set
        """
        return self._data["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """  Corresponds to IDD Field `design_level_calculation_method`
        The entered calculation method is used to create the maximum amount of other equipment.
        to set a loss, use a negative value in the following fields.
        for this set of attributes
        Choices: EquipmentLevel => Design Level -- simply enter power input of equipment
        Watts/Area or Power/Area => Power per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        Watts/Person or Power/Person => Power per Person -- enter the number to apply.  Value * Occupants = Equipment Level

        Args:
            value (str): value for IDD Field `design_level_calculation_method`
                Accepted values are:
                      - EquipmentLevel
                      - Watts/Area
                      - Watts/Person
                      - Power/Area
                      - Power/Person
                Default value: EquipmentLevel
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
                                 'for field `design_level_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_level_calculation_method`')
            vals = set()
            vals.add("EquipmentLevel")
            vals.add("Watts/Area")
            vals.add("Watts/Person")
            vals.add("Power/Area")
            vals.add("Power/Person")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_level_calculation_method`'.format(value))

        self._data["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """Get design_level

        Returns:
            float: the value of `design_level` or None if not set
        """
        return self._data["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """  Corresponds to IDD Field `design_level`

        Args:
            value (float): value for IDD Field `design_level`
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
                                 'for field `design_level`'.format(value))

        self._data["Design Level"] = value

    @property
    def power_per_zone_floor_area(self):
        """Get power_per_zone_floor_area

        Returns:
            float: the value of `power_per_zone_floor_area` or None if not set
        """
        return self._data["Power per Zone Floor Area"]

    @power_per_zone_floor_area.setter
    def power_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `power_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `power_per_zone_floor_area`
                Unit: W/m2
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
                                 'for field `power_per_zone_floor_area`'.format(value))

        self._data["Power per Zone Floor Area"] = value

    @property
    def power_per_person(self):
        """Get power_per_person

        Returns:
            float: the value of `power_per_person` or None if not set
        """
        return self._data["Power per Person"]

    @power_per_person.setter
    def power_per_person(self, value=None):
        """  Corresponds to IDD Field `power_per_person`

        Args:
            value (float): value for IDD Field `power_per_person`
                Unit: W/Person
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
                                 'for field `power_per_person`'.format(value))

        self._data["Power per Person"] = value

    @property
    def fraction_latent(self):
        """Get fraction_latent

        Returns:
            float: the value of `fraction_latent` or None if not set
        """
        return self._data["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_latent`

        Args:
            value (float): value for IDD Field `fraction_latent`
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
                                 'for field `fraction_latent`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_latent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_latent`')

        self._data["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_radiant`

        Args:
            value (float): value for IDD Field `fraction_radiant`
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
                                 'for field `fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_radiant`')

        self._data["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """Get fraction_lost

        Returns:
            float: the value of `fraction_lost` or None if not set
        """
        return self._data["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_lost`

        Args:
            value (float): value for IDD Field `fraction_lost`
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
                                 'for field `fraction_lost`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_lost`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_lost`')

        self._data["Fraction Lost"] = value

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
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.design_level_calculation_method))
        out.append(self._to_str(self.design_level))
        out.append(self._to_str(self.power_per_zone_floor_area))
        out.append(self._to_str(self.power_per_person))
        out.append(self._to_str(self.fraction_latent))
        out.append(self._to_str(self.fraction_radiant))
        out.append(self._to_str(self.fraction_lost))
        return ",".join(out)

class ZoneBaseboardOutdoorTemperatureControlled(object):
    """ Corresponds to IDD object `ZoneBaseboard:OutdoorTemperatureControlled`
        Specifies outside temperature-controlled electric baseboard heating.
    """
    internal_name = "ZoneBaseboard:OutdoorTemperatureControlled"
    field_count = 9

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneBaseboard:OutdoorTemperatureControlled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Schedule Name"] = None
        self._data["Capacity at Low Temperature"] = None
        self._data["Low Temperature"] = None
        self._data["Capacity at High Temperature"] = None
        self._data["High Temperature"] = None
        self._data["Fraction Radiant"] = None
        self._data["End-Use Subcategory"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity_at_low_temperature = None
        else:
            self.capacity_at_low_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.low_temperature = None
        else:
            self.low_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity_at_high_temperature = None
        else:
            self.capacity_at_high_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.high_temperature = None
        else:
            self.high_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
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
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        units in Schedule should be fraction applied to capacity of the baseboard heat equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def capacity_at_low_temperature(self):
        """Get capacity_at_low_temperature

        Returns:
            float: the value of `capacity_at_low_temperature` or None if not set
        """
        return self._data["Capacity at Low Temperature"]

    @capacity_at_low_temperature.setter
    def capacity_at_low_temperature(self, value=None):
        """  Corresponds to IDD Field `capacity_at_low_temperature`

        Args:
            value (float): value for IDD Field `capacity_at_low_temperature`
                Unit: W
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
                                 'for field `capacity_at_low_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `capacity_at_low_temperature`')

        self._data["Capacity at Low Temperature"] = value

    @property
    def low_temperature(self):
        """Get low_temperature

        Returns:
            float: the value of `low_temperature` or None if not set
        """
        return self._data["Low Temperature"]

    @low_temperature.setter
    def low_temperature(self, value=None):
        """  Corresponds to IDD Field `low_temperature`

        Args:
            value (float): value for IDD Field `low_temperature`
                Unit: C
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
                                 'for field `low_temperature`'.format(value))

        self._data["Low Temperature"] = value

    @property
    def capacity_at_high_temperature(self):
        """Get capacity_at_high_temperature

        Returns:
            float: the value of `capacity_at_high_temperature` or None if not set
        """
        return self._data["Capacity at High Temperature"]

    @capacity_at_high_temperature.setter
    def capacity_at_high_temperature(self, value=None):
        """  Corresponds to IDD Field `capacity_at_high_temperature`

        Args:
            value (float): value for IDD Field `capacity_at_high_temperature`
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
                                 'for field `capacity_at_high_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `capacity_at_high_temperature`')

        self._data["Capacity at High Temperature"] = value

    @property
    def high_temperature(self):
        """Get high_temperature

        Returns:
            float: the value of `high_temperature` or None if not set
        """
        return self._data["High Temperature"]

    @high_temperature.setter
    def high_temperature(self, value=None):
        """  Corresponds to IDD Field `high_temperature`

        Args:
            value (float): value for IDD Field `high_temperature`
                Unit: C
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
                                 'for field `high_temperature`'.format(value))

        self._data["High Temperature"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_radiant`

        Args:
            value (float): value for IDD Field `fraction_radiant`
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
                                 'for field `fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_radiant`')

        self._data["Fraction Radiant"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `enduse_subcategory`

        Args:
            value (str): value for IDD Field `enduse_subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')

        self._data["End-Use Subcategory"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.capacity_at_low_temperature))
        out.append(self._to_str(self.low_temperature))
        out.append(self._to_str(self.capacity_at_high_temperature))
        out.append(self._to_str(self.high_temperature))
        out.append(self._to_str(self.fraction_radiant))
        out.append(self._to_str(self.enduse_subcategory))
        return ",".join(out)

class ZoneContaminantSourceAndSinkCarbonDioxide(object):
    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:CarbonDioxide`
        Represents internal CO2 gains and sinks in the zone.
    """
    internal_name = "ZoneContaminantSourceAndSink:CarbonDioxide"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneContaminantSourceAndSink:CarbonDioxide`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Design Generation Rate"] = None
        self._data["Schedule Name"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_generation_rate = None
        else:
            self.design_generation_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
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
    def design_generation_rate(self):
        """Get design_generation_rate

        Returns:
            float: the value of `design_generation_rate` or None if not set
        """
        return self._data["Design Generation Rate"]

    @design_generation_rate.setter
    def design_generation_rate(self, value=None):
        """  Corresponds to IDD Field `design_generation_rate`

        Args:
            value (float): value for IDD Field `design_generation_rate`
                Unit: m3/s
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
                                 'for field `design_generation_rate`'.format(value))

        self._data["Design Generation Rate"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.design_generation_rate))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)

class ZoneContaminantSourceAndSinkGenericConstant(object):
    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:Constant`
        Sets internal generic contaminant gains and sinks in a zone with constant values.
    """
    internal_name = "ZoneContaminantSourceAndSink:Generic:Constant"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneContaminantSourceAndSink:Generic:Constant`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Design Generation Rate"] = None
        self._data["Generation Schedule Name"] = None
        self._data["Design Removal Coefficient"] = None
        self._data["Removal Schedule Name"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_generation_rate = None
        else:
            self.design_generation_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generation_schedule_name = None
        else:
            self.generation_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_removal_coefficient = None
        else:
            self.design_removal_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.removal_schedule_name = None
        else:
            self.removal_schedule_name = vals[i]
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
    def design_generation_rate(self):
        """Get design_generation_rate

        Returns:
            float: the value of `design_generation_rate` or None if not set
        """
        return self._data["Design Generation Rate"]

    @design_generation_rate.setter
    def design_generation_rate(self, value=None):
        """  Corresponds to IDD Field `design_generation_rate`

        Args:
            value (float): value for IDD Field `design_generation_rate`
                Unit: m3/s
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
                                 'for field `design_generation_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_generation_rate`')

        self._data["Design Generation Rate"] = value

    @property
    def generation_schedule_name(self):
        """Get generation_schedule_name

        Returns:
            str: the value of `generation_schedule_name` or None if not set
        """
        return self._data["Generation Schedule Name"]

    @generation_schedule_name.setter
    def generation_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generation_schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate

        Args:
            value (str): value for IDD Field `generation_schedule_name`
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
                                 'for field `generation_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generation_schedule_name`')

        self._data["Generation Schedule Name"] = value

    @property
    def design_removal_coefficient(self):
        """Get design_removal_coefficient

        Returns:
            float: the value of `design_removal_coefficient` or None if not set
        """
        return self._data["Design Removal Coefficient"]

    @design_removal_coefficient.setter
    def design_removal_coefficient(self, value=None):
        """  Corresponds to IDD Field `design_removal_coefficient`

        Args:
            value (float): value for IDD Field `design_removal_coefficient`
                Unit: m3/s
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
                                 'for field `design_removal_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_removal_coefficient`')

        self._data["Design Removal Coefficient"] = value

    @property
    def removal_schedule_name(self):
        """Get removal_schedule_name

        Returns:
            str: the value of `removal_schedule_name` or None if not set
        """
        return self._data["Removal Schedule Name"]

    @removal_schedule_name.setter
    def removal_schedule_name(self, value=None):
        """  Corresponds to IDD Field `removal_schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Design removal Coefficient

        Args:
            value (str): value for IDD Field `removal_schedule_name`
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
                                 'for field `removal_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `removal_schedule_name`')

        self._data["Removal Schedule Name"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.design_generation_rate))
        out.append(self._to_str(self.generation_schedule_name))
        out.append(self._to_str(self.design_removal_coefficient))
        out.append(self._to_str(self.removal_schedule_name))
        return ",".join(out)

class SurfaceContaminantSourceAndSinkGenericPressureDriven(object):
    """ Corresponds to IDD object `SurfaceContaminantSourceAndSink:Generic:PressureDriven`
        Simulate generic contaminant source driven by the pressure difference across a surface.
    """
    internal_name = "SurfaceContaminantSourceAndSink:Generic:PressureDriven"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceContaminantSourceAndSink:Generic:PressureDriven`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Name"] = None
        self._data["Design Generation Rate Coefficient"] = None
        self._data["Generation Schedule Name"] = None
        self._data["Generation Exponent"] = None

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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_generation_rate_coefficient = None
        else:
            self.design_generation_rate_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generation_schedule_name = None
        else:
            self.generation_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generation_exponent = None
        else:
            self.generation_exponent = vals[i]
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
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `surface_name`

        Args:
            value (str): value for IDD Field `surface_name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')

        self._data["Surface Name"] = value

    @property
    def design_generation_rate_coefficient(self):
        """Get design_generation_rate_coefficient

        Returns:
            float: the value of `design_generation_rate_coefficient` or None if not set
        """
        return self._data["Design Generation Rate Coefficient"]

    @design_generation_rate_coefficient.setter
    def design_generation_rate_coefficient(self, value=None):
        """  Corresponds to IDD Field `design_generation_rate_coefficient`

        Args:
            value (float): value for IDD Field `design_generation_rate_coefficient`
                Unit: m3/s
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
                                 'for field `design_generation_rate_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_generation_rate_coefficient`')

        self._data["Design Generation Rate Coefficient"] = value

    @property
    def generation_schedule_name(self):
        """Get generation_schedule_name

        Returns:
            str: the value of `generation_schedule_name` or None if not set
        """
        return self._data["Generation Schedule Name"]

    @generation_schedule_name.setter
    def generation_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generation_schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Design Generation Rate Coefficient

        Args:
            value (str): value for IDD Field `generation_schedule_name`
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
                                 'for field `generation_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generation_schedule_name`')

        self._data["Generation Schedule Name"] = value

    @property
    def generation_exponent(self):
        """Get generation_exponent

        Returns:
            float: the value of `generation_exponent` or None if not set
        """
        return self._data["Generation Exponent"]

    @generation_exponent.setter
    def generation_exponent(self, value=None):
        """  Corresponds to IDD Field `generation_exponent`

        Args:
            value (float): value for IDD Field `generation_exponent`
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
                                 'for field `generation_exponent`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `generation_exponent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `generation_exponent`')

        self._data["Generation Exponent"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.design_generation_rate_coefficient))
        out.append(self._to_str(self.generation_schedule_name))
        out.append(self._to_str(self.generation_exponent))
        return ",".join(out)

class ZoneContaminantSourceAndSinkGenericCutoffModel(object):
    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:CutoffModel`
        Simulate generic contaminant source driven by the cutoff concentration model.
    """
    internal_name = "ZoneContaminantSourceAndSink:Generic:CutoffModel"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneContaminantSourceAndSink:Generic:CutoffModel`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Design Generation Rate Coefficient"] = None
        self._data["Schedule Name"] = None
        self._data["Cutoff Generic Contaminant at which Emission Ceases"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_generation_rate_coefficient = None
        else:
            self.design_generation_rate_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cutoff_generic_contaminant_at_which_emission_ceases = None
        else:
            self.cutoff_generic_contaminant_at_which_emission_ceases = vals[i]
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
    def design_generation_rate_coefficient(self):
        """Get design_generation_rate_coefficient

        Returns:
            float: the value of `design_generation_rate_coefficient` or None if not set
        """
        return self._data["Design Generation Rate Coefficient"]

    @design_generation_rate_coefficient.setter
    def design_generation_rate_coefficient(self, value=None):
        """  Corresponds to IDD Field `design_generation_rate_coefficient`

        Args:
            value (float): value for IDD Field `design_generation_rate_coefficient`
                Unit: m3/s
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
                                 'for field `design_generation_rate_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_generation_rate_coefficient`')

        self._data["Design Generation Rate Coefficient"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Design Generation Rate Coefficient

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def cutoff_generic_contaminant_at_which_emission_ceases(self):
        """Get cutoff_generic_contaminant_at_which_emission_ceases

        Returns:
            float: the value of `cutoff_generic_contaminant_at_which_emission_ceases` or None if not set
        """
        return self._data["Cutoff Generic Contaminant at which Emission Ceases"]

    @cutoff_generic_contaminant_at_which_emission_ceases.setter
    def cutoff_generic_contaminant_at_which_emission_ceases(self, value=None):
        """  Corresponds to IDD Field `cutoff_generic_contaminant_at_which_emission_ceases`
        When the zone concentration level is greater than the cutoff level, emission stops,
        and the source level is zero.

        Args:
            value (float): value for IDD Field `cutoff_generic_contaminant_at_which_emission_ceases`
                Unit: ppm
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
                                 'for field `cutoff_generic_contaminant_at_which_emission_ceases`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cutoff_generic_contaminant_at_which_emission_ceases`')

        self._data["Cutoff Generic Contaminant at which Emission Ceases"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.design_generation_rate_coefficient))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.cutoff_generic_contaminant_at_which_emission_ceases))
        return ",".join(out)

class ZoneContaminantSourceAndSinkGenericDecaySource(object):
    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:DecaySource`
        Simulate generic contaminant source driven by the cutoff concentration model.
    """
    internal_name = "ZoneContaminantSourceAndSink:Generic:DecaySource"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneContaminantSourceAndSink:Generic:DecaySource`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Initial Emission Rate"] = None
        self._data["Schedule Name"] = None
        self._data["Delay Time Constant"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_emission_rate = None
        else:
            self.initial_emission_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delay_time_constant = None
        else:
            self.delay_time_constant = vals[i]
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
    def initial_emission_rate(self):
        """Get initial_emission_rate

        Returns:
            float: the value of `initial_emission_rate` or None if not set
        """
        return self._data["Initial Emission Rate"]

    @initial_emission_rate.setter
    def initial_emission_rate(self, value=None):
        """  Corresponds to IDD Field `initial_emission_rate`

        Args:
            value (float): value for IDD Field `initial_emission_rate`
                Unit: m3/s
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
                                 'for field `initial_emission_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `initial_emission_rate`')

        self._data["Initial Emission Rate"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Initial Emission Rate. When the value is equal to 1.0, the time will be reset to
        zero.

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def delay_time_constant(self):
        """Get delay_time_constant

        Returns:
            float: the value of `delay_time_constant` or None if not set
        """
        return self._data["Delay Time Constant"]

    @delay_time_constant.setter
    def delay_time_constant(self, value=None):
        """  Corresponds to IDD Field `delay_time_constant`

        Args:
            value (float): value for IDD Field `delay_time_constant`
                Unit: s
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
                                 'for field `delay_time_constant`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `delay_time_constant`')

        self._data["Delay Time Constant"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.initial_emission_rate))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.delay_time_constant))
        return ",".join(out)

class SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion(object):
    """ Corresponds to IDD object `SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion`
        Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    """
    internal_name = "SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Name"] = None
        self._data["Mass Transfer Coefficient"] = None
        self._data["Schedule Name"] = None
        self._data["Henry adsorption constant or partition coefficient"] = None

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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mass_transfer_coefficient = None
        else:
            self.mass_transfer_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.henry_adsorption_constant_or_partition_coefficient = None
        else:
            self.henry_adsorption_constant_or_partition_coefficient = vals[i]
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
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `surface_name`

        Args:
            value (str): value for IDD Field `surface_name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')

        self._data["Surface Name"] = value

    @property
    def mass_transfer_coefficient(self):
        """Get mass_transfer_coefficient

        Returns:
            float: the value of `mass_transfer_coefficient` or None if not set
        """
        return self._data["Mass Transfer Coefficient"]

    @mass_transfer_coefficient.setter
    def mass_transfer_coefficient(self, value=None):
        """  Corresponds to IDD Field `mass_transfer_coefficient`

        Args:
            value (float): value for IDD Field `mass_transfer_coefficient`
                Unit: m/s
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
                                 'for field `mass_transfer_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `mass_transfer_coefficient`')

        self._data["Mass Transfer Coefficient"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Initial Emission Rate. When the value is equal to 1.0, the time will be reset to
        zero.

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def henry_adsorption_constant_or_partition_coefficient(self):
        """Get henry_adsorption_constant_or_partition_coefficient

        Returns:
            float: the value of `henry_adsorption_constant_or_partition_coefficient` or None if not set
        """
        return self._data["Henry adsorption constant or partition coefficient"]

    @henry_adsorption_constant_or_partition_coefficient.setter
    def henry_adsorption_constant_or_partition_coefficient(self, value=None):
        """  Corresponds to IDD Field `henry_adsorption_constant_or_partition_coefficient`

        Args:
            value (float): value for IDD Field `henry_adsorption_constant_or_partition_coefficient`
                Unit: dimensionless
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
                                 'for field `henry_adsorption_constant_or_partition_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `henry_adsorption_constant_or_partition_coefficient`')

        self._data["Henry adsorption constant or partition coefficient"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.mass_transfer_coefficient))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.henry_adsorption_constant_or_partition_coefficient))
        return ",".join(out)

class SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink(object):
    """ Corresponds to IDD object `SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink`
        Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    """
    internal_name = "SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Name"] = None
        self._data["Deposition Velocity"] = None
        self._data["Schedule Name"] = None

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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.deposition_velocity = None
        else:
            self.deposition_velocity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
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
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `surface_name`

        Args:
            value (str): value for IDD Field `surface_name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')

        self._data["Surface Name"] = value

    @property
    def deposition_velocity(self):
        """Get deposition_velocity

        Returns:
            float: the value of `deposition_velocity` or None if not set
        """
        return self._data["Deposition Velocity"]

    @deposition_velocity.setter
    def deposition_velocity(self, value=None):
        """  Corresponds to IDD Field `deposition_velocity`

        Args:
            value (float): value for IDD Field `deposition_velocity`
                Unit: m/s
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
                                 'for field `deposition_velocity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `deposition_velocity`')

        self._data["Deposition Velocity"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Initial Emission Rate. When the value is equal to 1.0, the time will be reset to
        zero.

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.deposition_velocity))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)

class ZoneContaminantSourceAndSinkGenericDepositionRateSink(object):
    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:DepositionRateSink`
        Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    """
    internal_name = "ZoneContaminantSourceAndSink:Generic:DepositionRateSink"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneContaminantSourceAndSink:Generic:DepositionRateSink`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Deposition Rate"] = None
        self._data["Schedule Name"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.deposition_rate = None
        else:
            self.deposition_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
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
    def deposition_rate(self):
        """Get deposition_rate

        Returns:
            float: the value of `deposition_rate` or None if not set
        """
        return self._data["Deposition Rate"]

    @deposition_rate.setter
    def deposition_rate(self, value=None):
        """  Corresponds to IDD Field `deposition_rate`

        Args:
            value (float): value for IDD Field `deposition_rate`
                Unit: m/s
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
                                 'for field `deposition_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `deposition_rate`')

        self._data["Deposition Rate"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Initial Emission Rate. When the value is equal to 1.0, the time will be reset to
        zero.

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.deposition_rate))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)