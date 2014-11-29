from collections import OrderedDict

class Lights(object):
    """ Corresponds to IDD object `Lights`
        Sets internal gains for lights in the zone.
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    """
    internal_name = "Lights"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Lights`
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