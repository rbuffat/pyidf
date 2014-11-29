from collections import OrderedDict

class Material(object):
    """ Corresponds to IDD object `Material`
        Regular materials described with full set of thermal properties
    """
    internal_name = "Material"
    field_count = 9

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Material`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Roughness"] = None
        self._data["Thickness"] = None
        self._data["Conductivity"] = None
        self._data["Density"] = None
        self._data["Specific Heat"] = None
        self._data["Thermal Absorptance"] = None
        self._data["Solar Absorptance"] = None
        self._data["Visible Absorptance"] = None

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
            self.roughness = None
        else:
            self.roughness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thickness = None
        else:
            self.thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity = None
        else:
            self.conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.density = None
        else:
            self.density = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.specific_heat = None
        else:
            self.specific_heat = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_absorptance = None
        else:
            self.thermal_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_absorptance = None
        else:
            self.solar_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_absorptance = None
        else:
            self.visible_absorptance = vals[i]
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
    def roughness(self):
        """Get roughness

        Returns:
            str: the value of `roughness` or None if not set
        """
        return self._data["Roughness"]

    @roughness.setter
    def roughness(self, value=None):
        """  Corresponds to IDD Field `roughness`

        Args:
            value (str): value for IDD Field `roughness`
                Accepted values are:
                      - VeryRough
                      - Rough
                      - MediumRough
                      - MediumSmooth
                      - Smooth
                      - VerySmooth
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
                                 'for field `roughness`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `roughness`')
            vals = set()
            vals.add("VeryRough")
            vals.add("Rough")
            vals.add("MediumRough")
            vals.add("MediumSmooth")
            vals.add("Smooth")
            vals.add("VerySmooth")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `roughness`'.format(value))

        self._data["Roughness"] = value

    @property
    def thickness(self):
        """Get thickness

        Returns:
            float: the value of `thickness` or None if not set
        """
        return self._data["Thickness"]

    @thickness.setter
    def thickness(self, value=None):
        """  Corresponds to IDD Field `thickness`

        Args:
            value (float): value for IDD Field `thickness`
                Unit: m
                value > 0.0
                value <= 3.0
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
                                 'for field `thickness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thickness`')
            if value > 3.0:
                raise ValueError('value need to be smaller 3.0 '
                                 'for field `thickness`')

        self._data["Thickness"] = value

    @property
    def conductivity(self):
        """Get conductivity

        Returns:
            float: the value of `conductivity` or None if not set
        """
        return self._data["Conductivity"]

    @conductivity.setter
    def conductivity(self, value=None):
        """  Corresponds to IDD Field `conductivity`

        Args:
            value (float): value for IDD Field `conductivity`
                Unit: W/m-K
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
                                 'for field `conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `conductivity`')

        self._data["Conductivity"] = value

    @property
    def density(self):
        """Get density

        Returns:
            float: the value of `density` or None if not set
        """
        return self._data["Density"]

    @density.setter
    def density(self, value=None):
        """  Corresponds to IDD Field `density`

        Args:
            value (float): value for IDD Field `density`
                Unit: kg/m3
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
                                 'for field `density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `density`')

        self._data["Density"] = value

    @property
    def specific_heat(self):
        """Get specific_heat

        Returns:
            float: the value of `specific_heat` or None if not set
        """
        return self._data["Specific Heat"]

    @specific_heat.setter
    def specific_heat(self, value=None):
        """  Corresponds to IDD Field `specific_heat`

        Args:
            value (float): value for IDD Field `specific_heat`
                Unit: J/kg-K
                value >= 100.0
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
                                 'for field `specific_heat`'.format(value))
            if value < 100.0:
                raise ValueError('value need to be greater or equal 100.0 '
                                 'for field `specific_heat`')

        self._data["Specific Heat"] = value

    @property
    def thermal_absorptance(self):
        """Get thermal_absorptance

        Returns:
            float: the value of `thermal_absorptance` or None if not set
        """
        return self._data["Thermal Absorptance"]

    @thermal_absorptance.setter
    def thermal_absorptance(self, value=0.9 ):
        """  Corresponds to IDD Field `thermal_absorptance`

        Args:
            value (float): value for IDD Field `thermal_absorptance`
                Default value: 0.9
                value > 0.0
                value <= 0.99999
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
                                 'for field `thermal_absorptance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_absorptance`')
            if value > 0.99999:
                raise ValueError('value need to be smaller 0.99999 '
                                 'for field `thermal_absorptance`')

        self._data["Thermal Absorptance"] = value

    @property
    def solar_absorptance(self):
        """Get solar_absorptance

        Returns:
            float: the value of `solar_absorptance` or None if not set
        """
        return self._data["Solar Absorptance"]

    @solar_absorptance.setter
    def solar_absorptance(self, value=0.7 ):
        """  Corresponds to IDD Field `solar_absorptance`

        Args:
            value (float): value for IDD Field `solar_absorptance`
                Default value: 0.7
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
                                 'for field `solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `solar_absorptance`')

        self._data["Solar Absorptance"] = value

    @property
    def visible_absorptance(self):
        """Get visible_absorptance

        Returns:
            float: the value of `visible_absorptance` or None if not set
        """
        return self._data["Visible Absorptance"]

    @visible_absorptance.setter
    def visible_absorptance(self, value=0.7 ):
        """  Corresponds to IDD Field `visible_absorptance`

        Args:
            value (float): value for IDD Field `visible_absorptance`
                Default value: 0.7
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
                                 'for field `visible_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `visible_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `visible_absorptance`')

        self._data["Visible Absorptance"] = value

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
        out.append(self._to_str(self.roughness))
        out.append(self._to_str(self.thickness))
        out.append(self._to_str(self.conductivity))
        out.append(self._to_str(self.density))
        out.append(self._to_str(self.specific_heat))
        out.append(self._to_str(self.thermal_absorptance))
        out.append(self._to_str(self.solar_absorptance))
        out.append(self._to_str(self.visible_absorptance))
        return ",".join(out)

class MaterialNoMass(object):
    """ Corresponds to IDD object `Material:NoMass`
        Regular materials properties described whose principal description is R (Thermal Resistance)
    """
    internal_name = "Material:NoMass"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Material:NoMass`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Roughness"] = None
        self._data["Thermal Resistance"] = None
        self._data["Thermal Absorptance"] = None
        self._data["Solar Absorptance"] = None
        self._data["Visible Absorptance"] = None

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
            self.roughness = None
        else:
            self.roughness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_resistance = None
        else:
            self.thermal_resistance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_absorptance = None
        else:
            self.thermal_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_absorptance = None
        else:
            self.solar_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_absorptance = None
        else:
            self.visible_absorptance = vals[i]
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
    def roughness(self):
        """Get roughness

        Returns:
            str: the value of `roughness` or None if not set
        """
        return self._data["Roughness"]

    @roughness.setter
    def roughness(self, value=None):
        """  Corresponds to IDD Field `roughness`

        Args:
            value (str): value for IDD Field `roughness`
                Accepted values are:
                      - VeryRough
                      - Rough
                      - MediumRough
                      - MediumSmooth
                      - Smooth
                      - VerySmooth
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
                                 'for field `roughness`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `roughness`')
            vals = set()
            vals.add("VeryRough")
            vals.add("Rough")
            vals.add("MediumRough")
            vals.add("MediumSmooth")
            vals.add("Smooth")
            vals.add("VerySmooth")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `roughness`'.format(value))

        self._data["Roughness"] = value

    @property
    def thermal_resistance(self):
        """Get thermal_resistance

        Returns:
            float: the value of `thermal_resistance` or None if not set
        """
        return self._data["Thermal Resistance"]

    @thermal_resistance.setter
    def thermal_resistance(self, value=None):
        """  Corresponds to IDD Field `thermal_resistance`

        Args:
            value (float): value for IDD Field `thermal_resistance`
                Unit: m2-K/W
                value >= 0.001
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
                                 'for field `thermal_resistance`'.format(value))
            if value < 0.001:
                raise ValueError('value need to be greater or equal 0.001 '
                                 'for field `thermal_resistance`')

        self._data["Thermal Resistance"] = value

    @property
    def thermal_absorptance(self):
        """Get thermal_absorptance

        Returns:
            float: the value of `thermal_absorptance` or None if not set
        """
        return self._data["Thermal Absorptance"]

    @thermal_absorptance.setter
    def thermal_absorptance(self, value=0.9 ):
        """  Corresponds to IDD Field `thermal_absorptance`

        Args:
            value (float): value for IDD Field `thermal_absorptance`
                Default value: 0.9
                value > 0.0
                value <= 0.99999
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
                                 'for field `thermal_absorptance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_absorptance`')
            if value > 0.99999:
                raise ValueError('value need to be smaller 0.99999 '
                                 'for field `thermal_absorptance`')

        self._data["Thermal Absorptance"] = value

    @property
    def solar_absorptance(self):
        """Get solar_absorptance

        Returns:
            float: the value of `solar_absorptance` or None if not set
        """
        return self._data["Solar Absorptance"]

    @solar_absorptance.setter
    def solar_absorptance(self, value=0.7 ):
        """  Corresponds to IDD Field `solar_absorptance`

        Args:
            value (float): value for IDD Field `solar_absorptance`
                Default value: 0.7
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
                                 'for field `solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `solar_absorptance`')

        self._data["Solar Absorptance"] = value

    @property
    def visible_absorptance(self):
        """Get visible_absorptance

        Returns:
            float: the value of `visible_absorptance` or None if not set
        """
        return self._data["Visible Absorptance"]

    @visible_absorptance.setter
    def visible_absorptance(self, value=0.7 ):
        """  Corresponds to IDD Field `visible_absorptance`

        Args:
            value (float): value for IDD Field `visible_absorptance`
                Default value: 0.7
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
                                 'for field `visible_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `visible_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `visible_absorptance`')

        self._data["Visible Absorptance"] = value

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
        out.append(self._to_str(self.roughness))
        out.append(self._to_str(self.thermal_resistance))
        out.append(self._to_str(self.thermal_absorptance))
        out.append(self._to_str(self.solar_absorptance))
        out.append(self._to_str(self.visible_absorptance))
        return ",".join(out)

class MaterialInfraredTransparent(object):
    """ Corresponds to IDD object `Material:InfraredTransparent`
        Special infrared transparent material.  Similar to a Material:Nomass with low thermal resistance.
        High absorptance in both wavelengths.
        Area will be doubled internally to make internal radiant exchange accurate.
        Should be only material in single layer surface construction.
        All thermal properties are set internally. User needs only to supply name.
        Cannot be used with ConductionFiniteDifference solution algorithms
    """
    internal_name = "Material:InfraredTransparent"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Material:InfraredTransparent`
        """
        self._data = OrderedDict()
        self._data["Name"] = None

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
        return ",".join(out)

class MaterialAirGap(object):
    """ Corresponds to IDD object `Material:AirGap`
        Air Space in Opaque Construction
    """
    internal_name = "Material:AirGap"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Material:AirGap`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Thermal Resistance"] = None

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
            self.thermal_resistance = None
        else:
            self.thermal_resistance = vals[i]
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
    def thermal_resistance(self):
        """Get thermal_resistance

        Returns:
            float: the value of `thermal_resistance` or None if not set
        """
        return self._data["Thermal Resistance"]

    @thermal_resistance.setter
    def thermal_resistance(self, value=None):
        """  Corresponds to IDD Field `thermal_resistance`

        Args:
            value (float): value for IDD Field `thermal_resistance`
                Unit: m2-K/W
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
                                 'for field `thermal_resistance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_resistance`')

        self._data["Thermal Resistance"] = value

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
        out.append(self._to_str(self.thermal_resistance))
        return ",".join(out)

class MaterialRoofVegetation(object):
    """ Corresponds to IDD object `Material:RoofVegetation`
        EcoRoof model, plant layer plus soil layer
        Implemented by Portland State University
        (Sailor et al., January, 2007)
        only one material must be referenced per simulation though the same EcoRoof material could be
        used in multiple constructions. New moisture redistribution scheme (2010) requires higher
        number of timesteps per hour (minimum 12 recommended).
    """
    internal_name = "Material:RoofVegetation"
    field_count = 19

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Material:RoofVegetation`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Height of Plants"] = None
        self._data["Leaf Area Index"] = None
        self._data["Leaf Reflectivity"] = None
        self._data["Leaf Emissivity"] = None
        self._data["Minimum Stomatal Resistance"] = None
        self._data["Soil Layer Name"] = None
        self._data["Roughness"] = None
        self._data["Thickness"] = None
        self._data["Conductivity of Dry Soil"] = None
        self._data["Density of Dry Soil"] = None
        self._data["Specific Heat of Dry Soil"] = None
        self._data["Thermal Absorptance"] = None
        self._data["Solar Absorptance"] = None
        self._data["Visible Absorptance"] = None
        self._data["Saturation Volumetric Moisture Content of the Soil Layer"] = None
        self._data["Residual Volumetric Moisture Content of the Soil Layer"] = None
        self._data["Initial Volumetric Moisture Content of the Soil Layer"] = None
        self._data["Moisture Diffusion Calculation Method"] = None

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
            self.height_of_plants = None
        else:
            self.height_of_plants = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leaf_area_index = None
        else:
            self.leaf_area_index = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leaf_reflectivity = None
        else:
            self.leaf_reflectivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leaf_emissivity = None
        else:
            self.leaf_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_stomatal_resistance = None
        else:
            self.minimum_stomatal_resistance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_layer_name = None
        else:
            self.soil_layer_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.roughness = None
        else:
            self.roughness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thickness = None
        else:
            self.thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity_of_dry_soil = None
        else:
            self.conductivity_of_dry_soil = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.density_of_dry_soil = None
        else:
            self.density_of_dry_soil = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.specific_heat_of_dry_soil = None
        else:
            self.specific_heat_of_dry_soil = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_absorptance = None
        else:
            self.thermal_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_absorptance = None
        else:
            self.solar_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_absorptance = None
        else:
            self.visible_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.saturation_volumetric_moisture_content_of_the_soil_layer = None
        else:
            self.saturation_volumetric_moisture_content_of_the_soil_layer = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.residual_volumetric_moisture_content_of_the_soil_layer = None
        else:
            self.residual_volumetric_moisture_content_of_the_soil_layer = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_volumetric_moisture_content_of_the_soil_layer = None
        else:
            self.initial_volumetric_moisture_content_of_the_soil_layer = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_diffusion_calculation_method = None
        else:
            self.moisture_diffusion_calculation_method = vals[i]
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
    def height_of_plants(self):
        """Get height_of_plants

        Returns:
            float: the value of `height_of_plants` or None if not set
        """
        return self._data["Height of Plants"]

    @height_of_plants.setter
    def height_of_plants(self, value=0.2 ):
        """  Corresponds to IDD Field `height_of_plants`
        The ecoroof module is designed for short plants and shrubs.

        Args:
            value (float): value for IDD Field `height_of_plants`
                Unit: m
                Default value: 0.2
                value > 0.005
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
                                 'for field `height_of_plants`'.format(value))
            if value <= 0.005:
                raise ValueError('value need to be greater 0.005 '
                                 'for field `height_of_plants`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `height_of_plants`')

        self._data["Height of Plants"] = value

    @property
    def leaf_area_index(self):
        """Get leaf_area_index

        Returns:
            float: the value of `leaf_area_index` or None if not set
        """
        return self._data["Leaf Area Index"]

    @leaf_area_index.setter
    def leaf_area_index(self, value=1.0 ):
        """  Corresponds to IDD Field `leaf_area_index`
        Entire surface is assumed covered, so decrease LAI accordingly.

        Args:
            value (float): value for IDD Field `leaf_area_index`
                Unit: dimensionless
                Default value: 1.0
                value > 0.001
                value <= 5.0
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
                                 'for field `leaf_area_index`'.format(value))
            if value <= 0.001:
                raise ValueError('value need to be greater 0.001 '
                                 'for field `leaf_area_index`')
            if value > 5.0:
                raise ValueError('value need to be smaller 5.0 '
                                 'for field `leaf_area_index`')

        self._data["Leaf Area Index"] = value

    @property
    def leaf_reflectivity(self):
        """Get leaf_reflectivity

        Returns:
            float: the value of `leaf_reflectivity` or None if not set
        """
        return self._data["Leaf Reflectivity"]

    @leaf_reflectivity.setter
    def leaf_reflectivity(self, value=0.22 ):
        """  Corresponds to IDD Field `leaf_reflectivity`
        Leaf reflectivity (albedo) is typically 0.18-0.25

        Args:
            value (float): value for IDD Field `leaf_reflectivity`
                Unit: dimensionless
                Default value: 0.22
                value >= 0.05
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
                                 'for field `leaf_reflectivity`'.format(value))
            if value < 0.05:
                raise ValueError('value need to be greater or equal 0.05 '
                                 'for field `leaf_reflectivity`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `leaf_reflectivity`')

        self._data["Leaf Reflectivity"] = value

    @property
    def leaf_emissivity(self):
        """Get leaf_emissivity

        Returns:
            float: the value of `leaf_emissivity` or None if not set
        """
        return self._data["Leaf Emissivity"]

    @leaf_emissivity.setter
    def leaf_emissivity(self, value=0.95 ):
        """  Corresponds to IDD Field `leaf_emissivity`

        Args:
            value (float): value for IDD Field `leaf_emissivity`
                Default value: 0.95
                value >= 0.8
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
                                 'for field `leaf_emissivity`'.format(value))
            if value < 0.8:
                raise ValueError('value need to be greater or equal 0.8 '
                                 'for field `leaf_emissivity`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `leaf_emissivity`')

        self._data["Leaf Emissivity"] = value

    @property
    def minimum_stomatal_resistance(self):
        """Get minimum_stomatal_resistance

        Returns:
            float: the value of `minimum_stomatal_resistance` or None if not set
        """
        return self._data["Minimum Stomatal Resistance"]

    @minimum_stomatal_resistance.setter
    def minimum_stomatal_resistance(self, value=180.0 ):
        """  Corresponds to IDD Field `minimum_stomatal_resistance`
        This depends upon plant type

        Args:
            value (float): value for IDD Field `minimum_stomatal_resistance`
                Unit: s/m
                Default value: 180.0
                value >= 50.0
                value <= 300.0
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
                                 'for field `minimum_stomatal_resistance`'.format(value))
            if value < 50.0:
                raise ValueError('value need to be greater or equal 50.0 '
                                 'for field `minimum_stomatal_resistance`')
            if value > 300.0:
                raise ValueError('value need to be smaller 300.0 '
                                 'for field `minimum_stomatal_resistance`')

        self._data["Minimum Stomatal Resistance"] = value

    @property
    def soil_layer_name(self):
        """Get soil_layer_name

        Returns:
            str: the value of `soil_layer_name` or None if not set
        """
        return self._data["Soil Layer Name"]

    @soil_layer_name.setter
    def soil_layer_name(self, value="Green Roof Soil"):
        """  Corresponds to IDD Field `soil_layer_name`

        Args:
            value (str): value for IDD Field `soil_layer_name`
                Default value: Green Roof Soil
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
                                 'for field `soil_layer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `soil_layer_name`')

        self._data["Soil Layer Name"] = value

    @property
    def roughness(self):
        """Get roughness

        Returns:
            str: the value of `roughness` or None if not set
        """
        return self._data["Roughness"]

    @roughness.setter
    def roughness(self, value="MediumRough"):
        """  Corresponds to IDD Field `roughness`

        Args:
            value (str): value for IDD Field `roughness`
                Accepted values are:
                      - VeryRough
                      - MediumRough
                      - Rough
                      - Smooth
                      - MediumSmooth
                      - VerySmooth
                Default value: MediumRough
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
                                 'for field `roughness`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `roughness`')
            vals = set()
            vals.add("VeryRough")
            vals.add("MediumRough")
            vals.add("Rough")
            vals.add("Smooth")
            vals.add("MediumSmooth")
            vals.add("VerySmooth")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `roughness`'.format(value))

        self._data["Roughness"] = value

    @property
    def thickness(self):
        """Get thickness

        Returns:
            float: the value of `thickness` or None if not set
        """
        return self._data["Thickness"]

    @thickness.setter
    def thickness(self, value=0.1 ):
        """  Corresponds to IDD Field `thickness`
        thickness of the soil layer of the EcoRoof
        Soil depths of 0.15m (6in) and 0.30m (12in) are common.

        Args:
            value (float): value for IDD Field `thickness`
                Unit: m
                Default value: 0.1
                value > 0.05
                value <= 0.7
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
                                 'for field `thickness`'.format(value))
            if value <= 0.05:
                raise ValueError('value need to be greater 0.05 '
                                 'for field `thickness`')
            if value > 0.7:
                raise ValueError('value need to be smaller 0.7 '
                                 'for field `thickness`')

        self._data["Thickness"] = value

    @property
    def conductivity_of_dry_soil(self):
        """Get conductivity_of_dry_soil

        Returns:
            float: the value of `conductivity_of_dry_soil` or None if not set
        """
        return self._data["Conductivity of Dry Soil"]

    @conductivity_of_dry_soil.setter
    def conductivity_of_dry_soil(self, value=0.35 ):
        """  Corresponds to IDD Field `conductivity_of_dry_soil`
        Thermal conductivity of dry soil.
        Typical ecoroof soils range from 0.3 to 0.5

        Args:
            value (float): value for IDD Field `conductivity_of_dry_soil`
                Unit: W/m-K
                Default value: 0.35
                value >= 0.2
                value <= 1.5
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
                                 'for field `conductivity_of_dry_soil`'.format(value))
            if value < 0.2:
                raise ValueError('value need to be greater or equal 0.2 '
                                 'for field `conductivity_of_dry_soil`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `conductivity_of_dry_soil`')

        self._data["Conductivity of Dry Soil"] = value

    @property
    def density_of_dry_soil(self):
        """Get density_of_dry_soil

        Returns:
            float: the value of `density_of_dry_soil` or None if not set
        """
        return self._data["Density of Dry Soil"]

    @density_of_dry_soil.setter
    def density_of_dry_soil(self, value=1100.0 ):
        """  Corresponds to IDD Field `density_of_dry_soil`
        Density of dry soil (the code modifies this as the soil becomes moist)
        Typical ecoroof soils range from 400 to 1000 (dry to wet)

        Args:
            value (float): value for IDD Field `density_of_dry_soil`
                Unit: kg/m3
                Default value: 1100.0
                value >= 300.0
                value <= 2000.0
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
                                 'for field `density_of_dry_soil`'.format(value))
            if value < 300.0:
                raise ValueError('value need to be greater or equal 300.0 '
                                 'for field `density_of_dry_soil`')
            if value > 2000.0:
                raise ValueError('value need to be smaller 2000.0 '
                                 'for field `density_of_dry_soil`')

        self._data["Density of Dry Soil"] = value

    @property
    def specific_heat_of_dry_soil(self):
        """Get specific_heat_of_dry_soil

        Returns:
            float: the value of `specific_heat_of_dry_soil` or None if not set
        """
        return self._data["Specific Heat of Dry Soil"]

    @specific_heat_of_dry_soil.setter
    def specific_heat_of_dry_soil(self, value=1200.0 ):
        """  Corresponds to IDD Field `specific_heat_of_dry_soil`
        Specific heat of dry soil

        Args:
            value (float): value for IDD Field `specific_heat_of_dry_soil`
                Unit: J/kg-K
                Default value: 1200.0
                value > 500.0
                value <= 2000.0
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
                                 'for field `specific_heat_of_dry_soil`'.format(value))
            if value <= 500.0:
                raise ValueError('value need to be greater 500.0 '
                                 'for field `specific_heat_of_dry_soil`')
            if value > 2000.0:
                raise ValueError('value need to be smaller 2000.0 '
                                 'for field `specific_heat_of_dry_soil`')

        self._data["Specific Heat of Dry Soil"] = value

    @property
    def thermal_absorptance(self):
        """Get thermal_absorptance

        Returns:
            float: the value of `thermal_absorptance` or None if not set
        """
        return self._data["Thermal Absorptance"]

    @thermal_absorptance.setter
    def thermal_absorptance(self, value=0.9 ):
        """  Corresponds to IDD Field `thermal_absorptance`
        Soil emissivity is typically in range of 0.90 to 0.98

        Args:
            value (float): value for IDD Field `thermal_absorptance`
                Default value: 0.9
                value > 0.8
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
                                 'for field `thermal_absorptance`'.format(value))
            if value <= 0.8:
                raise ValueError('value need to be greater 0.8 '
                                 'for field `thermal_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `thermal_absorptance`')

        self._data["Thermal Absorptance"] = value

    @property
    def solar_absorptance(self):
        """Get solar_absorptance

        Returns:
            float: the value of `solar_absorptance` or None if not set
        """
        return self._data["Solar Absorptance"]

    @solar_absorptance.setter
    def solar_absorptance(self, value=0.7 ):
        """  Corresponds to IDD Field `solar_absorptance`
        Solar absorptance of dry soil (1-albedo) is typically 0.60 to 0.85
        corresponding to a dry albedo of 0.15 to 0.40

        Args:
            value (float): value for IDD Field `solar_absorptance`
                Default value: 0.7
                value >= 0.4
                value <= 0.9
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
                                 'for field `solar_absorptance`'.format(value))
            if value < 0.4:
                raise ValueError('value need to be greater or equal 0.4 '
                                 'for field `solar_absorptance`')
            if value > 0.9:
                raise ValueError('value need to be smaller 0.9 '
                                 'for field `solar_absorptance`')

        self._data["Solar Absorptance"] = value

    @property
    def visible_absorptance(self):
        """Get visible_absorptance

        Returns:
            float: the value of `visible_absorptance` or None if not set
        """
        return self._data["Visible Absorptance"]

    @visible_absorptance.setter
    def visible_absorptance(self, value=0.75 ):
        """  Corresponds to IDD Field `visible_absorptance`

        Args:
            value (float): value for IDD Field `visible_absorptance`
                Default value: 0.75
                value > 0.5
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
                                 'for field `visible_absorptance`'.format(value))
            if value <= 0.5:
                raise ValueError('value need to be greater 0.5 '
                                 'for field `visible_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `visible_absorptance`')

        self._data["Visible Absorptance"] = value

    @property
    def saturation_volumetric_moisture_content_of_the_soil_layer(self):
        """Get saturation_volumetric_moisture_content_of_the_soil_layer

        Returns:
            float: the value of `saturation_volumetric_moisture_content_of_the_soil_layer` or None if not set
        """
        return self._data["Saturation Volumetric Moisture Content of the Soil Layer"]

    @saturation_volumetric_moisture_content_of_the_soil_layer.setter
    def saturation_volumetric_moisture_content_of_the_soil_layer(self, value=0.3 ):
        """  Corresponds to IDD Field `saturation_volumetric_moisture_content_of_the_soil_layer`
        Maximum moisture content is typically less than 0.5

        Args:
            value (float): value for IDD Field `saturation_volumetric_moisture_content_of_the_soil_layer`
                Default value: 0.3
                value > 0.1
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
                                 'for field `saturation_volumetric_moisture_content_of_the_soil_layer`'.format(value))
            if value <= 0.1:
                raise ValueError('value need to be greater 0.1 '
                                 'for field `saturation_volumetric_moisture_content_of_the_soil_layer`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `saturation_volumetric_moisture_content_of_the_soil_layer`')

        self._data["Saturation Volumetric Moisture Content of the Soil Layer"] = value

    @property
    def residual_volumetric_moisture_content_of_the_soil_layer(self):
        """Get residual_volumetric_moisture_content_of_the_soil_layer

        Returns:
            float: the value of `residual_volumetric_moisture_content_of_the_soil_layer` or None if not set
        """
        return self._data["Residual Volumetric Moisture Content of the Soil Layer"]

    @residual_volumetric_moisture_content_of_the_soil_layer.setter
    def residual_volumetric_moisture_content_of_the_soil_layer(self, value=0.01 ):
        """  Corresponds to IDD Field `residual_volumetric_moisture_content_of_the_soil_layer`

        Args:
            value (float): value for IDD Field `residual_volumetric_moisture_content_of_the_soil_layer`
                Default value: 0.01
                value >= 0.01
                value <= 0.1
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
                                 'for field `residual_volumetric_moisture_content_of_the_soil_layer`'.format(value))
            if value < 0.01:
                raise ValueError('value need to be greater or equal 0.01 '
                                 'for field `residual_volumetric_moisture_content_of_the_soil_layer`')
            if value > 0.1:
                raise ValueError('value need to be smaller 0.1 '
                                 'for field `residual_volumetric_moisture_content_of_the_soil_layer`')

        self._data["Residual Volumetric Moisture Content of the Soil Layer"] = value

    @property
    def initial_volumetric_moisture_content_of_the_soil_layer(self):
        """Get initial_volumetric_moisture_content_of_the_soil_layer

        Returns:
            float: the value of `initial_volumetric_moisture_content_of_the_soil_layer` or None if not set
        """
        return self._data["Initial Volumetric Moisture Content of the Soil Layer"]

    @initial_volumetric_moisture_content_of_the_soil_layer.setter
    def initial_volumetric_moisture_content_of_the_soil_layer(self, value=0.1 ):
        """  Corresponds to IDD Field `initial_volumetric_moisture_content_of_the_soil_layer`

        Args:
            value (float): value for IDD Field `initial_volumetric_moisture_content_of_the_soil_layer`
                Default value: 0.1
                value > 0.05
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
                                 'for field `initial_volumetric_moisture_content_of_the_soil_layer`'.format(value))
            if value <= 0.05:
                raise ValueError('value need to be greater 0.05 '
                                 'for field `initial_volumetric_moisture_content_of_the_soil_layer`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `initial_volumetric_moisture_content_of_the_soil_layer`')

        self._data["Initial Volumetric Moisture Content of the Soil Layer"] = value

    @property
    def moisture_diffusion_calculation_method(self):
        """Get moisture_diffusion_calculation_method

        Returns:
            str: the value of `moisture_diffusion_calculation_method` or None if not set
        """
        return self._data["Moisture Diffusion Calculation Method"]

    @moisture_diffusion_calculation_method.setter
    def moisture_diffusion_calculation_method(self, value="Advanced"):
        """  Corresponds to IDD Field `moisture_diffusion_calculation_method`
        Advanced calculation requires increased number of timesteps (recommended >20).

        Args:
            value (str): value for IDD Field `moisture_diffusion_calculation_method`
                Accepted values are:
                      - Simple
                      - Advanced
                Default value: Advanced
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
                                 'for field `moisture_diffusion_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `moisture_diffusion_calculation_method`')
            vals = set()
            vals.add("Simple")
            vals.add("Advanced")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `moisture_diffusion_calculation_method`'.format(value))

        self._data["Moisture Diffusion Calculation Method"] = value

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
        out.append(self._to_str(self.height_of_plants))
        out.append(self._to_str(self.leaf_area_index))
        out.append(self._to_str(self.leaf_reflectivity))
        out.append(self._to_str(self.leaf_emissivity))
        out.append(self._to_str(self.minimum_stomatal_resistance))
        out.append(self._to_str(self.soil_layer_name))
        out.append(self._to_str(self.roughness))
        out.append(self._to_str(self.thickness))
        out.append(self._to_str(self.conductivity_of_dry_soil))
        out.append(self._to_str(self.density_of_dry_soil))
        out.append(self._to_str(self.specific_heat_of_dry_soil))
        out.append(self._to_str(self.thermal_absorptance))
        out.append(self._to_str(self.solar_absorptance))
        out.append(self._to_str(self.visible_absorptance))
        out.append(self._to_str(self.saturation_volumetric_moisture_content_of_the_soil_layer))
        out.append(self._to_str(self.residual_volumetric_moisture_content_of_the_soil_layer))
        out.append(self._to_str(self.initial_volumetric_moisture_content_of_the_soil_layer))
        out.append(self._to_str(self.moisture_diffusion_calculation_method))
        return ",".join(out)