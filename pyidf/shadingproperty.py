from collections import OrderedDict

class ShadingPropertyReflectance(object):
    """ Corresponds to IDD object `ShadingProperty:Reflectance`
        If this object is not defined for a shading surface the default values
        listed in following fields will be used in the solar reflection calculation.
    """
    internal_name = "ShadingProperty:Reflectance"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ShadingProperty:Reflectance`
        """
        self._data = OrderedDict()
        self._data["Shading Surface Name"] = None
        self._data["Diffuse Solar Reflectance of Unglazed Part of Shading Surface"] = None
        self._data["Diffuse Visible Reflectance of Unglazed Part of Shading Surface"] = None
        self._data["Fraction of Shading Surface That Is Glazed"] = None
        self._data["Glazing Construction Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.shading_surface_name = None
        else:
            self.shading_surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffuse_solar_reflectance_of_unglazed_part_of_shading_surface = None
        else:
            self.diffuse_solar_reflectance_of_unglazed_part_of_shading_surface = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffuse_visible_reflectance_of_unglazed_part_of_shading_surface = None
        else:
            self.diffuse_visible_reflectance_of_unglazed_part_of_shading_surface = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_shading_surface_that_is_glazed = None
        else:
            self.fraction_of_shading_surface_that_is_glazed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.glazing_construction_name = None
        else:
            self.glazing_construction_name = vals[i]
        i += 1

    @property
    def shading_surface_name(self):
        """Get shading_surface_name

        Returns:
            str: the value of `shading_surface_name` or None if not set
        """
        return self._data["Shading Surface Name"]

    @shading_surface_name.setter
    def shading_surface_name(self, value=None):
        """  Corresponds to IDD Field `shading_surface_name`

        Args:
            value (str): value for IDD Field `shading_surface_name`
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
                                 'for field `shading_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `shading_surface_name`')

        self._data["Shading Surface Name"] = value

    @property
    def diffuse_solar_reflectance_of_unglazed_part_of_shading_surface(self):
        """Get diffuse_solar_reflectance_of_unglazed_part_of_shading_surface

        Returns:
            float: the value of `diffuse_solar_reflectance_of_unglazed_part_of_shading_surface` or None if not set
        """
        return self._data["Diffuse Solar Reflectance of Unglazed Part of Shading Surface"]

    @diffuse_solar_reflectance_of_unglazed_part_of_shading_surface.setter
    def diffuse_solar_reflectance_of_unglazed_part_of_shading_surface(self, value=0.2 ):
        """  Corresponds to IDD Field `diffuse_solar_reflectance_of_unglazed_part_of_shading_surface`

        Args:
            value (float): value for IDD Field `diffuse_solar_reflectance_of_unglazed_part_of_shading_surface`
                Default value: 0.2
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
                                 'for field `diffuse_solar_reflectance_of_unglazed_part_of_shading_surface`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffuse_solar_reflectance_of_unglazed_part_of_shading_surface`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `diffuse_solar_reflectance_of_unglazed_part_of_shading_surface`')

        self._data["Diffuse Solar Reflectance of Unglazed Part of Shading Surface"] = value

    @property
    def diffuse_visible_reflectance_of_unglazed_part_of_shading_surface(self):
        """Get diffuse_visible_reflectance_of_unglazed_part_of_shading_surface

        Returns:
            float: the value of `diffuse_visible_reflectance_of_unglazed_part_of_shading_surface` or None if not set
        """
        return self._data["Diffuse Visible Reflectance of Unglazed Part of Shading Surface"]

    @diffuse_visible_reflectance_of_unglazed_part_of_shading_surface.setter
    def diffuse_visible_reflectance_of_unglazed_part_of_shading_surface(self, value=0.2 ):
        """  Corresponds to IDD Field `diffuse_visible_reflectance_of_unglazed_part_of_shading_surface`

        Args:
            value (float): value for IDD Field `diffuse_visible_reflectance_of_unglazed_part_of_shading_surface`
                Default value: 0.2
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
                                 'for field `diffuse_visible_reflectance_of_unglazed_part_of_shading_surface`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffuse_visible_reflectance_of_unglazed_part_of_shading_surface`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `diffuse_visible_reflectance_of_unglazed_part_of_shading_surface`')

        self._data["Diffuse Visible Reflectance of Unglazed Part of Shading Surface"] = value

    @property
    def fraction_of_shading_surface_that_is_glazed(self):
        """Get fraction_of_shading_surface_that_is_glazed

        Returns:
            float: the value of `fraction_of_shading_surface_that_is_glazed` or None if not set
        """
        return self._data["Fraction of Shading Surface That Is Glazed"]

    @fraction_of_shading_surface_that_is_glazed.setter
    def fraction_of_shading_surface_that_is_glazed(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_of_shading_surface_that_is_glazed`

        Args:
            value (float): value for IDD Field `fraction_of_shading_surface_that_is_glazed`
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
                                 'for field `fraction_of_shading_surface_that_is_glazed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_shading_surface_that_is_glazed`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_shading_surface_that_is_glazed`')

        self._data["Fraction of Shading Surface That Is Glazed"] = value

    @property
    def glazing_construction_name(self):
        """Get glazing_construction_name

        Returns:
            str: the value of `glazing_construction_name` or None if not set
        """
        return self._data["Glazing Construction Name"]

    @glazing_construction_name.setter
    def glazing_construction_name(self, value=None):
        """  Corresponds to IDD Field `glazing_construction_name`
        Required if Fraction of Shading Surface That Is Glazed > 0.0

        Args:
            value (str): value for IDD Field `glazing_construction_name`
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
                                 'for field `glazing_construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `glazing_construction_name`')

        self._data["Glazing Construction Name"] = value

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
        out.append(self._to_str(self.shading_surface_name))
        out.append(self._to_str(self.diffuse_solar_reflectance_of_unglazed_part_of_shading_surface))
        out.append(self._to_str(self.diffuse_visible_reflectance_of_unglazed_part_of_shading_surface))
        out.append(self._to_str(self.fraction_of_shading_surface_that_is_glazed))
        out.append(self._to_str(self.glazing_construction_name))
        return ",".join(out)