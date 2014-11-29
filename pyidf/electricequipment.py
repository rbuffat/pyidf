from collections import OrderedDict

class ElectricEquipment(object):
    """ Corresponds to IDD object `ElectricEquipment`
        Sets internal gains for electric equipment in the zone.
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    """
    internal_name = "ElectricEquipment"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ElectricEquipment`
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