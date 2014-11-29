from collections import OrderedDict

class WindowMaterialSimpleGlazingSystem(object):
    """ Corresponds to IDD object `WindowMaterial:SimpleGlazingSystem`
        Alternate method of describing windows
        This window material object is used to define an entire glazing system
        using simple performance parameters.
    """
    internal_name = "WindowMaterial:SimpleGlazingSystem"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:SimpleGlazingSystem`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["U-Factor"] = None
        self._data["Solar Heat Gain Coefficient"] = None
        self._data["Visible Transmittance"] = None

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
            self.ufactor = None
        else:
            self.ufactor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_heat_gain_coefficient = None
        else:
            self.solar_heat_gain_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_transmittance = None
        else:
            self.visible_transmittance = vals[i]
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
    def ufactor(self):
        """Get ufactor

        Returns:
            float: the value of `ufactor` or None if not set
        """
        return self._data["U-Factor"]

    @ufactor.setter
    def ufactor(self, value=None):
        """  Corresponds to IDD Field `ufactor`
        Enter U-Factor including film coefficients
        Note that the effective upper limit for U-factor is 5.8 W/m2-K

        Args:
            value (float): value for IDD Field `ufactor`
                Unit: W/m2-K
                value > 0.0
                value <= 7.0
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
                                 'for field `ufactor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ufactor`')
            if value > 7.0:
                raise ValueError('value need to be smaller 7.0 '
                                 'for field `ufactor`')

        self._data["U-Factor"] = value

    @property
    def solar_heat_gain_coefficient(self):
        """Get solar_heat_gain_coefficient

        Returns:
            float: the value of `solar_heat_gain_coefficient` or None if not set
        """
        return self._data["Solar Heat Gain Coefficient"]

    @solar_heat_gain_coefficient.setter
    def solar_heat_gain_coefficient(self, value=None):
        """  Corresponds to IDD Field `solar_heat_gain_coefficient`
        SHGC at Normal Incidence

        Args:
            value (float): value for IDD Field `solar_heat_gain_coefficient`
                value > 0.0
                value < 1.0
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
                                 'for field `solar_heat_gain_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `solar_heat_gain_coefficient`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `solar_heat_gain_coefficient`')

        self._data["Solar Heat Gain Coefficient"] = value

    @property
    def visible_transmittance(self):
        """Get visible_transmittance

        Returns:
            float: the value of `visible_transmittance` or None if not set
        """
        return self._data["Visible Transmittance"]

    @visible_transmittance.setter
    def visible_transmittance(self, value=None):
        """  Corresponds to IDD Field `visible_transmittance`
        VT at Normal Incidence
        optional

        Args:
            value (float): value for IDD Field `visible_transmittance`
                value > 0.0
                value < 1.0
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
                                 'for field `visible_transmittance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `visible_transmittance`')

        self._data["Visible Transmittance"] = value

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
        out.append(self._to_str(self.ufactor))
        out.append(self._to_str(self.solar_heat_gain_coefficient))
        out.append(self._to_str(self.visible_transmittance))
        return ",".join(out)

class WindowMaterialGlazing(object):
    """ Corresponds to IDD object `WindowMaterial:Glazing`
        Glass material properties for Windows or Glass Doors
        Transmittance/Reflectance input method.
    """
    internal_name = "WindowMaterial:Glazing"
    field_count = 18

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Glazing`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Optical Data Type"] = None
        self._data["Window Glass Spectral Data Set Name"] = None
        self._data["Thickness"] = None
        self._data["Solar Transmittance at Normal Incidence"] = None
        self._data["Front Side Solar Reflectance at Normal Incidence"] = None
        self._data["Back Side Solar Reflectance at Normal Incidence"] = None
        self._data["Visible Transmittance at Normal Incidence"] = None
        self._data["Front Side Visible Reflectance at Normal Incidence"] = None
        self._data["Back Side Visible Reflectance at Normal Incidence"] = None
        self._data["Infrared Transmittance at Normal Incidence"] = None
        self._data["Front Side Infrared Hemispherical Emissivity"] = None
        self._data["Back Side Infrared Hemispherical Emissivity"] = None
        self._data["Conductivity"] = None
        self._data["Dirt Correction Factor for Solar and Visible Transmittance"] = None
        self._data["Solar Diffusing"] = None
        self._data["Youngs modulus"] = None
        self._data["Poissons ratio"] = None

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
            self.optical_data_type = None
        else:
            self.optical_data_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_glass_spectral_data_set_name = None
        else:
            self.window_glass_spectral_data_set_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thickness = None
        else:
            self.thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_transmittance_at_normal_incidence = None
        else:
            self.solar_transmittance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_solar_reflectance_at_normal_incidence = None
        else:
            self.front_side_solar_reflectance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_solar_reflectance_at_normal_incidence = None
        else:
            self.back_side_solar_reflectance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_transmittance_at_normal_incidence = None
        else:
            self.visible_transmittance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_visible_reflectance_at_normal_incidence = None
        else:
            self.front_side_visible_reflectance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_visible_reflectance_at_normal_incidence = None
        else:
            self.back_side_visible_reflectance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.infrared_transmittance_at_normal_incidence = None
        else:
            self.infrared_transmittance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_infrared_hemispherical_emissivity = None
        else:
            self.front_side_infrared_hemispherical_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_infrared_hemispherical_emissivity = None
        else:
            self.back_side_infrared_hemispherical_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity = None
        else:
            self.conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dirt_correction_factor_for_solar_and_visible_transmittance = None
        else:
            self.dirt_correction_factor_for_solar_and_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_diffusing = None
        else:
            self.solar_diffusing = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.youngs_modulus = None
        else:
            self.youngs_modulus = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.poissons_ratio = None
        else:
            self.poissons_ratio = vals[i]
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
    def optical_data_type(self):
        """Get optical_data_type

        Returns:
            str: the value of `optical_data_type` or None if not set
        """
        return self._data["Optical Data Type"]

    @optical_data_type.setter
    def optical_data_type(self, value=None):
        """  Corresponds to IDD Field `optical_data_type`

        Args:
            value (str): value for IDD Field `optical_data_type`
                Accepted values are:
                      - SpectralAverage
                      - Spectral
                      - BSDF
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
                                 'for field `optical_data_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `optical_data_type`')
            vals = set()
            vals.add("SpectralAverage")
            vals.add("Spectral")
            vals.add("BSDF")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `optical_data_type`'.format(value))

        self._data["Optical Data Type"] = value

    @property
    def window_glass_spectral_data_set_name(self):
        """Get window_glass_spectral_data_set_name

        Returns:
            str: the value of `window_glass_spectral_data_set_name` or None if not set
        """
        return self._data["Window Glass Spectral Data Set Name"]

    @window_glass_spectral_data_set_name.setter
    def window_glass_spectral_data_set_name(self, value=None):
        """  Corresponds to IDD Field `window_glass_spectral_data_set_name`
        Used only when Optical Data Type = Spectral

        Args:
            value (str): value for IDD Field `window_glass_spectral_data_set_name`
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
                                 'for field `window_glass_spectral_data_set_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_glass_spectral_data_set_name`')

        self._data["Window Glass Spectral Data Set Name"] = value

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

        self._data["Thickness"] = value

    @property
    def solar_transmittance_at_normal_incidence(self):
        """Get solar_transmittance_at_normal_incidence

        Returns:
            float: the value of `solar_transmittance_at_normal_incidence` or None if not set
        """
        return self._data["Solar Transmittance at Normal Incidence"]

    @solar_transmittance_at_normal_incidence.setter
    def solar_transmittance_at_normal_incidence(self, value=None):
        """  Corresponds to IDD Field `solar_transmittance_at_normal_incidence`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `solar_transmittance_at_normal_incidence`
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
                                 'for field `solar_transmittance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `solar_transmittance_at_normal_incidence`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `solar_transmittance_at_normal_incidence`')

        self._data["Solar Transmittance at Normal Incidence"] = value

    @property
    def front_side_solar_reflectance_at_normal_incidence(self):
        """Get front_side_solar_reflectance_at_normal_incidence

        Returns:
            float: the value of `front_side_solar_reflectance_at_normal_incidence` or None if not set
        """
        return self._data["Front Side Solar Reflectance at Normal Incidence"]

    @front_side_solar_reflectance_at_normal_incidence.setter
    def front_side_solar_reflectance_at_normal_incidence(self, value=None):
        """  Corresponds to IDD Field `front_side_solar_reflectance_at_normal_incidence`
        Used only when Optical Data Type = SpectralAverage
        Front Side is side closest to outdoor air

        Args:
            value (float): value for IDD Field `front_side_solar_reflectance_at_normal_incidence`
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
                                 'for field `front_side_solar_reflectance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_solar_reflectance_at_normal_incidence`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_solar_reflectance_at_normal_incidence`')

        self._data["Front Side Solar Reflectance at Normal Incidence"] = value

    @property
    def back_side_solar_reflectance_at_normal_incidence(self):
        """Get back_side_solar_reflectance_at_normal_incidence

        Returns:
            float: the value of `back_side_solar_reflectance_at_normal_incidence` or None if not set
        """
        return self._data["Back Side Solar Reflectance at Normal Incidence"]

    @back_side_solar_reflectance_at_normal_incidence.setter
    def back_side_solar_reflectance_at_normal_incidence(self, value=None):
        """  Corresponds to IDD Field `back_side_solar_reflectance_at_normal_incidence`
        Used only when Optical Data Type = SpectralAverage
        Back Side is side closest to zone air

        Args:
            value (float): value for IDD Field `back_side_solar_reflectance_at_normal_incidence`
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
                                 'for field `back_side_solar_reflectance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_solar_reflectance_at_normal_incidence`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_solar_reflectance_at_normal_incidence`')

        self._data["Back Side Solar Reflectance at Normal Incidence"] = value

    @property
    def visible_transmittance_at_normal_incidence(self):
        """Get visible_transmittance_at_normal_incidence

        Returns:
            float: the value of `visible_transmittance_at_normal_incidence` or None if not set
        """
        return self._data["Visible Transmittance at Normal Incidence"]

    @visible_transmittance_at_normal_incidence.setter
    def visible_transmittance_at_normal_incidence(self, value=None):
        """  Corresponds to IDD Field `visible_transmittance_at_normal_incidence`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `visible_transmittance_at_normal_incidence`
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
                                 'for field `visible_transmittance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `visible_transmittance_at_normal_incidence`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `visible_transmittance_at_normal_incidence`')

        self._data["Visible Transmittance at Normal Incidence"] = value

    @property
    def front_side_visible_reflectance_at_normal_incidence(self):
        """Get front_side_visible_reflectance_at_normal_incidence

        Returns:
            float: the value of `front_side_visible_reflectance_at_normal_incidence` or None if not set
        """
        return self._data["Front Side Visible Reflectance at Normal Incidence"]

    @front_side_visible_reflectance_at_normal_incidence.setter
    def front_side_visible_reflectance_at_normal_incidence(self, value=None):
        """  Corresponds to IDD Field `front_side_visible_reflectance_at_normal_incidence`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `front_side_visible_reflectance_at_normal_incidence`
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
                                 'for field `front_side_visible_reflectance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_visible_reflectance_at_normal_incidence`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_visible_reflectance_at_normal_incidence`')

        self._data["Front Side Visible Reflectance at Normal Incidence"] = value

    @property
    def back_side_visible_reflectance_at_normal_incidence(self):
        """Get back_side_visible_reflectance_at_normal_incidence

        Returns:
            float: the value of `back_side_visible_reflectance_at_normal_incidence` or None if not set
        """
        return self._data["Back Side Visible Reflectance at Normal Incidence"]

    @back_side_visible_reflectance_at_normal_incidence.setter
    def back_side_visible_reflectance_at_normal_incidence(self, value=None):
        """  Corresponds to IDD Field `back_side_visible_reflectance_at_normal_incidence`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `back_side_visible_reflectance_at_normal_incidence`
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
                                 'for field `back_side_visible_reflectance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_visible_reflectance_at_normal_incidence`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_visible_reflectance_at_normal_incidence`')

        self._data["Back Side Visible Reflectance at Normal Incidence"] = value

    @property
    def infrared_transmittance_at_normal_incidence(self):
        """Get infrared_transmittance_at_normal_incidence

        Returns:
            float: the value of `infrared_transmittance_at_normal_incidence` or None if not set
        """
        return self._data["Infrared Transmittance at Normal Incidence"]

    @infrared_transmittance_at_normal_incidence.setter
    def infrared_transmittance_at_normal_incidence(self, value=0.0 ):
        """  Corresponds to IDD Field `infrared_transmittance_at_normal_incidence`

        Args:
            value (float): value for IDD Field `infrared_transmittance_at_normal_incidence`
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
                                 'for field `infrared_transmittance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `infrared_transmittance_at_normal_incidence`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `infrared_transmittance_at_normal_incidence`')

        self._data["Infrared Transmittance at Normal Incidence"] = value

    @property
    def front_side_infrared_hemispherical_emissivity(self):
        """Get front_side_infrared_hemispherical_emissivity

        Returns:
            float: the value of `front_side_infrared_hemispherical_emissivity` or None if not set
        """
        return self._data["Front Side Infrared Hemispherical Emissivity"]

    @front_side_infrared_hemispherical_emissivity.setter
    def front_side_infrared_hemispherical_emissivity(self, value=0.84 ):
        """  Corresponds to IDD Field `front_side_infrared_hemispherical_emissivity`

        Args:
            value (float): value for IDD Field `front_side_infrared_hemispherical_emissivity`
                Default value: 0.84
                value > 0.0
                value < 1.0
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
                                 'for field `front_side_infrared_hemispherical_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `front_side_infrared_hemispherical_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_infrared_hemispherical_emissivity`')

        self._data["Front Side Infrared Hemispherical Emissivity"] = value

    @property
    def back_side_infrared_hemispherical_emissivity(self):
        """Get back_side_infrared_hemispherical_emissivity

        Returns:
            float: the value of `back_side_infrared_hemispherical_emissivity` or None if not set
        """
        return self._data["Back Side Infrared Hemispherical Emissivity"]

    @back_side_infrared_hemispherical_emissivity.setter
    def back_side_infrared_hemispherical_emissivity(self, value=0.84 ):
        """  Corresponds to IDD Field `back_side_infrared_hemispherical_emissivity`

        Args:
            value (float): value for IDD Field `back_side_infrared_hemispherical_emissivity`
                Default value: 0.84
                value > 0.0
                value < 1.0
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
                                 'for field `back_side_infrared_hemispherical_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `back_side_infrared_hemispherical_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_infrared_hemispherical_emissivity`')

        self._data["Back Side Infrared Hemispherical Emissivity"] = value

    @property
    def conductivity(self):
        """Get conductivity

        Returns:
            float: the value of `conductivity` or None if not set
        """
        return self._data["Conductivity"]

    @conductivity.setter
    def conductivity(self, value=0.9 ):
        """  Corresponds to IDD Field `conductivity`

        Args:
            value (float): value for IDD Field `conductivity`
                Unit: W/m-K
                Default value: 0.9
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
    def dirt_correction_factor_for_solar_and_visible_transmittance(self):
        """Get dirt_correction_factor_for_solar_and_visible_transmittance

        Returns:
            float: the value of `dirt_correction_factor_for_solar_and_visible_transmittance` or None if not set
        """
        return self._data["Dirt Correction Factor for Solar and Visible Transmittance"]

    @dirt_correction_factor_for_solar_and_visible_transmittance.setter
    def dirt_correction_factor_for_solar_and_visible_transmittance(self, value=1.0 ):
        """  Corresponds to IDD Field `dirt_correction_factor_for_solar_and_visible_transmittance`

        Args:
            value (float): value for IDD Field `dirt_correction_factor_for_solar_and_visible_transmittance`
                Default value: 1.0
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
                                 'for field `dirt_correction_factor_for_solar_and_visible_transmittance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `dirt_correction_factor_for_solar_and_visible_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `dirt_correction_factor_for_solar_and_visible_transmittance`')

        self._data["Dirt Correction Factor for Solar and Visible Transmittance"] = value

    @property
    def solar_diffusing(self):
        """Get solar_diffusing

        Returns:
            str: the value of `solar_diffusing` or None if not set
        """
        return self._data["Solar Diffusing"]

    @solar_diffusing.setter
    def solar_diffusing(self, value="No"):
        """  Corresponds to IDD Field `solar_diffusing`

        Args:
            value (str): value for IDD Field `solar_diffusing`
                Accepted values are:
                      - No
                      - Yes
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
                                 'for field `solar_diffusing`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `solar_diffusing`')
            vals = set()
            vals.add("No")
            vals.add("Yes")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `solar_diffusing`'.format(value))

        self._data["Solar Diffusing"] = value

    @property
    def youngs_modulus(self):
        """Get youngs_modulus

        Returns:
            float: the value of `youngs_modulus` or None if not set
        """
        return self._data["Youngs modulus"]

    @youngs_modulus.setter
    def youngs_modulus(self, value=72000000000.0 ):
        """  Corresponds to IDD Field `youngs_modulus`
        coefficient used for deflection calculations. Used only with complex
        fenestration when deflection model is set to TemperatureAndPressureInput

        Args:
            value (float): value for IDD Field `youngs_modulus`
                Unit: Pa
                Default value: 72000000000.0
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
                                 'for field `youngs_modulus`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `youngs_modulus`')

        self._data["Youngs modulus"] = value

    @property
    def poissons_ratio(self):
        """Get poissons_ratio

        Returns:
            float: the value of `poissons_ratio` or None if not set
        """
        return self._data["Poissons ratio"]

    @poissons_ratio.setter
    def poissons_ratio(self, value=0.22 ):
        """  Corresponds to IDD Field `poissons_ratio`
        coefficient used for deflection calculations. Used only with complex
        fenestration when deflection model is set to TemperatureAndPressureInput

        Args:
            value (float): value for IDD Field `poissons_ratio`
                Default value: 0.22
                value > 0.0
                value < 1.0
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
                                 'for field `poissons_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `poissons_ratio`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `poissons_ratio`')

        self._data["Poissons ratio"] = value

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
        out.append(self._to_str(self.optical_data_type))
        out.append(self._to_str(self.window_glass_spectral_data_set_name))
        out.append(self._to_str(self.thickness))
        out.append(self._to_str(self.solar_transmittance_at_normal_incidence))
        out.append(self._to_str(self.front_side_solar_reflectance_at_normal_incidence))
        out.append(self._to_str(self.back_side_solar_reflectance_at_normal_incidence))
        out.append(self._to_str(self.visible_transmittance_at_normal_incidence))
        out.append(self._to_str(self.front_side_visible_reflectance_at_normal_incidence))
        out.append(self._to_str(self.back_side_visible_reflectance_at_normal_incidence))
        out.append(self._to_str(self.infrared_transmittance_at_normal_incidence))
        out.append(self._to_str(self.front_side_infrared_hemispherical_emissivity))
        out.append(self._to_str(self.back_side_infrared_hemispherical_emissivity))
        out.append(self._to_str(self.conductivity))
        out.append(self._to_str(self.dirt_correction_factor_for_solar_and_visible_transmittance))
        out.append(self._to_str(self.solar_diffusing))
        out.append(self._to_str(self.youngs_modulus))
        out.append(self._to_str(self.poissons_ratio))
        return ",".join(out)

class WindowMaterialGlazingGroupThermochromic(object):
    """ Corresponds to IDD object `WindowMaterial:GlazingGroup:Thermochromic`
        thermochromic glass at different temperatures
    """
    internal_name = "WindowMaterial:GlazingGroup:Thermochromic"
    field_count = 91

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:GlazingGroup:Thermochromic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Optical Data Temperature 1"] = None
        self._data["Window Material Glazing Name 1"] = None
        self._data["Optical Data Temperature 2"] = None
        self._data["Window Material Glazing Name 2"] = None
        self._data["Optical Data Temperature 3"] = None
        self._data["Window Material Glazing Name 3"] = None
        self._data["Optical Data Temperature 4"] = None
        self._data["Window Material Glazing Name 4"] = None
        self._data["Optical Data Temperature 5"] = None
        self._data["Window Material Glazing Name 5"] = None
        self._data["Optical Data Temperature 6"] = None
        self._data["Window Material Glazing Name 6"] = None
        self._data["Optical Data Temperature 7"] = None
        self._data["Window Material Glazing Name 7"] = None
        self._data["Optical Data Temperature 8"] = None
        self._data["Window Material Glazing Name 8"] = None
        self._data["Optical Data Temperature 9"] = None
        self._data["Window Material Glazing Name 9"] = None
        self._data["Optical Data Temperature 10"] = None
        self._data["Window Material Glazing Name 10"] = None
        self._data["Optical Data Temperature 11"] = None
        self._data["Window Material Glazing Name 11"] = None
        self._data["Optical Data Temperature 12"] = None
        self._data["Window Material Glazing Name 12"] = None
        self._data["Optical Data Temperature 13"] = None
        self._data["Window Material Glazing Name 13"] = None
        self._data["Optical Data Temperature 14"] = None
        self._data["Window Material Glazing Name 14"] = None
        self._data["Optical Data Temperature 15"] = None
        self._data["Window Material Glazing Name 15"] = None
        self._data["Optical Data Temperature 16"] = None
        self._data["Window Material Glazing Name 16"] = None
        self._data["Optical Data Temperature 17"] = None
        self._data["Window Material Glazing Name 17"] = None
        self._data["Optical Data Temperature 18"] = None
        self._data["Window Material Glazing Name 18"] = None
        self._data["Optical Data Temperature 19"] = None
        self._data["Window Material Glazing Name 19"] = None
        self._data["Optical Data Temperature 20"] = None
        self._data["Window Material Glazing Name 20"] = None
        self._data["Optical Data Temperature 21"] = None
        self._data["Window Material Glazing Name 21"] = None
        self._data["Optical Data Temperature 22"] = None
        self._data["Window Material Glazing Name 22"] = None
        self._data["Optical Data Temperature 23"] = None
        self._data["Window Material Glazing Name 23"] = None
        self._data["Optical Data Temperature 24"] = None
        self._data["Window Material Glazing Name 24"] = None
        self._data["Optical Data Temperature 25"] = None
        self._data["Window Material Glazing Name 25"] = None
        self._data["Optical Data Temperature 26"] = None
        self._data["Window Material Glazing Name 26"] = None
        self._data["Optical Data Temperature 27"] = None
        self._data["Window Material Glazing Name 27"] = None
        self._data["Optical Data Temperature 28"] = None
        self._data["Window Material Glazing Name 28"] = None
        self._data["Optical Data Temperature 29"] = None
        self._data["Window Material Glazing Name 29"] = None
        self._data["Optical Data Temperature 30"] = None
        self._data["Window Material Glazing Name 30"] = None
        self._data["Optical Data Temperature 31"] = None
        self._data["Window Material Glazing Name 31"] = None
        self._data["Optical Data Temperature 32"] = None
        self._data["Window Material Glazing Name 32"] = None
        self._data["Optical Data Temperature 33"] = None
        self._data["Window Material Glazing Name 33"] = None
        self._data["Optical Data Temperature 34"] = None
        self._data["Window Material Glazing Name 34"] = None
        self._data["Optical Data Temperature 35"] = None
        self._data["Window Material Glazing Name 35"] = None
        self._data["Optical Data Temperature 36"] = None
        self._data["Window Material Glazing Name 36"] = None
        self._data["Optical Data Temperature 37"] = None
        self._data["Window Material Glazing Name 37"] = None
        self._data["Optical Data Temperature 38"] = None
        self._data["Window Material Glazing Name 38"] = None
        self._data["Optical Data Temperature 39"] = None
        self._data["Window Material Glazing Name 39"] = None
        self._data["Optical Data Temperature 40"] = None
        self._data["Window Material Glazing Name 40"] = None
        self._data["Optical Data Temperature 41"] = None
        self._data["Window Material Glazing Name 41"] = None
        self._data["Optical Data Temperature 42"] = None
        self._data["Window Material Glazing Name 42"] = None
        self._data["Optical Data Temperature 43"] = None
        self._data["Window Material Glazing Name 43"] = None
        self._data["Optical Data Temperature 44"] = None
        self._data["Window Material Glazing Name 44"] = None
        self._data["Optical Data Temperature 45"] = None
        self._data["Window Material Glazing Name 45"] = None

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
            self.optical_data_temperature_1 = None
        else:
            self.optical_data_temperature_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_1 = None
        else:
            self.window_material_glazing_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_2 = None
        else:
            self.optical_data_temperature_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_2 = None
        else:
            self.window_material_glazing_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_3 = None
        else:
            self.optical_data_temperature_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_3 = None
        else:
            self.window_material_glazing_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_4 = None
        else:
            self.optical_data_temperature_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_4 = None
        else:
            self.window_material_glazing_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_5 = None
        else:
            self.optical_data_temperature_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_5 = None
        else:
            self.window_material_glazing_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_6 = None
        else:
            self.optical_data_temperature_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_6 = None
        else:
            self.window_material_glazing_name_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_7 = None
        else:
            self.optical_data_temperature_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_7 = None
        else:
            self.window_material_glazing_name_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_8 = None
        else:
            self.optical_data_temperature_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_8 = None
        else:
            self.window_material_glazing_name_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_9 = None
        else:
            self.optical_data_temperature_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_9 = None
        else:
            self.window_material_glazing_name_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_10 = None
        else:
            self.optical_data_temperature_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_10 = None
        else:
            self.window_material_glazing_name_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_11 = None
        else:
            self.optical_data_temperature_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_11 = None
        else:
            self.window_material_glazing_name_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_12 = None
        else:
            self.optical_data_temperature_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_12 = None
        else:
            self.window_material_glazing_name_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_13 = None
        else:
            self.optical_data_temperature_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_13 = None
        else:
            self.window_material_glazing_name_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_14 = None
        else:
            self.optical_data_temperature_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_14 = None
        else:
            self.window_material_glazing_name_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_15 = None
        else:
            self.optical_data_temperature_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_15 = None
        else:
            self.window_material_glazing_name_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_16 = None
        else:
            self.optical_data_temperature_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_16 = None
        else:
            self.window_material_glazing_name_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_17 = None
        else:
            self.optical_data_temperature_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_17 = None
        else:
            self.window_material_glazing_name_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_18 = None
        else:
            self.optical_data_temperature_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_18 = None
        else:
            self.window_material_glazing_name_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_19 = None
        else:
            self.optical_data_temperature_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_19 = None
        else:
            self.window_material_glazing_name_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_20 = None
        else:
            self.optical_data_temperature_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_20 = None
        else:
            self.window_material_glazing_name_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_21 = None
        else:
            self.optical_data_temperature_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_21 = None
        else:
            self.window_material_glazing_name_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_22 = None
        else:
            self.optical_data_temperature_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_22 = None
        else:
            self.window_material_glazing_name_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_23 = None
        else:
            self.optical_data_temperature_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_23 = None
        else:
            self.window_material_glazing_name_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_24 = None
        else:
            self.optical_data_temperature_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_24 = None
        else:
            self.window_material_glazing_name_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_25 = None
        else:
            self.optical_data_temperature_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_25 = None
        else:
            self.window_material_glazing_name_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_26 = None
        else:
            self.optical_data_temperature_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_26 = None
        else:
            self.window_material_glazing_name_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_27 = None
        else:
            self.optical_data_temperature_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_27 = None
        else:
            self.window_material_glazing_name_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_28 = None
        else:
            self.optical_data_temperature_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_28 = None
        else:
            self.window_material_glazing_name_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_29 = None
        else:
            self.optical_data_temperature_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_29 = None
        else:
            self.window_material_glazing_name_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_30 = None
        else:
            self.optical_data_temperature_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_30 = None
        else:
            self.window_material_glazing_name_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_31 = None
        else:
            self.optical_data_temperature_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_31 = None
        else:
            self.window_material_glazing_name_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_32 = None
        else:
            self.optical_data_temperature_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_32 = None
        else:
            self.window_material_glazing_name_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_33 = None
        else:
            self.optical_data_temperature_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_33 = None
        else:
            self.window_material_glazing_name_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_34 = None
        else:
            self.optical_data_temperature_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_34 = None
        else:
            self.window_material_glazing_name_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_35 = None
        else:
            self.optical_data_temperature_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_35 = None
        else:
            self.window_material_glazing_name_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_36 = None
        else:
            self.optical_data_temperature_36 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_36 = None
        else:
            self.window_material_glazing_name_36 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_37 = None
        else:
            self.optical_data_temperature_37 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_37 = None
        else:
            self.window_material_glazing_name_37 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_38 = None
        else:
            self.optical_data_temperature_38 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_38 = None
        else:
            self.window_material_glazing_name_38 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_39 = None
        else:
            self.optical_data_temperature_39 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_39 = None
        else:
            self.window_material_glazing_name_39 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_40 = None
        else:
            self.optical_data_temperature_40 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_40 = None
        else:
            self.window_material_glazing_name_40 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_41 = None
        else:
            self.optical_data_temperature_41 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_41 = None
        else:
            self.window_material_glazing_name_41 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_42 = None
        else:
            self.optical_data_temperature_42 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_42 = None
        else:
            self.window_material_glazing_name_42 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_43 = None
        else:
            self.optical_data_temperature_43 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_43 = None
        else:
            self.window_material_glazing_name_43 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_44 = None
        else:
            self.optical_data_temperature_44 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_44 = None
        else:
            self.window_material_glazing_name_44 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.optical_data_temperature_45 = None
        else:
            self.optical_data_temperature_45 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_material_glazing_name_45 = None
        else:
            self.window_material_glazing_name_45 = vals[i]
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
    def optical_data_temperature_1(self):
        """Get optical_data_temperature_1

        Returns:
            float: the value of `optical_data_temperature_1` or None if not set
        """
        return self._data["Optical Data Temperature 1"]

    @optical_data_temperature_1.setter
    def optical_data_temperature_1(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_1`

        Args:
            value (float): value for IDD Field `optical_data_temperature_1`
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
                                 'for field `optical_data_temperature_1`'.format(value))

        self._data["Optical Data Temperature 1"] = value

    @property
    def window_material_glazing_name_1(self):
        """Get window_material_glazing_name_1

        Returns:
            str: the value of `window_material_glazing_name_1` or None if not set
        """
        return self._data["Window Material Glazing Name 1"]

    @window_material_glazing_name_1.setter
    def window_material_glazing_name_1(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_1`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_1`
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
                                 'for field `window_material_glazing_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_1`')

        self._data["Window Material Glazing Name 1"] = value

    @property
    def optical_data_temperature_2(self):
        """Get optical_data_temperature_2

        Returns:
            float: the value of `optical_data_temperature_2` or None if not set
        """
        return self._data["Optical Data Temperature 2"]

    @optical_data_temperature_2.setter
    def optical_data_temperature_2(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_2`

        Args:
            value (float): value for IDD Field `optical_data_temperature_2`
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
                                 'for field `optical_data_temperature_2`'.format(value))

        self._data["Optical Data Temperature 2"] = value

    @property
    def window_material_glazing_name_2(self):
        """Get window_material_glazing_name_2

        Returns:
            str: the value of `window_material_glazing_name_2` or None if not set
        """
        return self._data["Window Material Glazing Name 2"]

    @window_material_glazing_name_2.setter
    def window_material_glazing_name_2(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_2`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_2`
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
                                 'for field `window_material_glazing_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_2`')

        self._data["Window Material Glazing Name 2"] = value

    @property
    def optical_data_temperature_3(self):
        """Get optical_data_temperature_3

        Returns:
            float: the value of `optical_data_temperature_3` or None if not set
        """
        return self._data["Optical Data Temperature 3"]

    @optical_data_temperature_3.setter
    def optical_data_temperature_3(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_3`

        Args:
            value (float): value for IDD Field `optical_data_temperature_3`
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
                                 'for field `optical_data_temperature_3`'.format(value))

        self._data["Optical Data Temperature 3"] = value

    @property
    def window_material_glazing_name_3(self):
        """Get window_material_glazing_name_3

        Returns:
            str: the value of `window_material_glazing_name_3` or None if not set
        """
        return self._data["Window Material Glazing Name 3"]

    @window_material_glazing_name_3.setter
    def window_material_glazing_name_3(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_3`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_3`
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
                                 'for field `window_material_glazing_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_3`')

        self._data["Window Material Glazing Name 3"] = value

    @property
    def optical_data_temperature_4(self):
        """Get optical_data_temperature_4

        Returns:
            float: the value of `optical_data_temperature_4` or None if not set
        """
        return self._data["Optical Data Temperature 4"]

    @optical_data_temperature_4.setter
    def optical_data_temperature_4(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_4`

        Args:
            value (float): value for IDD Field `optical_data_temperature_4`
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
                                 'for field `optical_data_temperature_4`'.format(value))

        self._data["Optical Data Temperature 4"] = value

    @property
    def window_material_glazing_name_4(self):
        """Get window_material_glazing_name_4

        Returns:
            str: the value of `window_material_glazing_name_4` or None if not set
        """
        return self._data["Window Material Glazing Name 4"]

    @window_material_glazing_name_4.setter
    def window_material_glazing_name_4(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_4`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_4`
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
                                 'for field `window_material_glazing_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_4`')

        self._data["Window Material Glazing Name 4"] = value

    @property
    def optical_data_temperature_5(self):
        """Get optical_data_temperature_5

        Returns:
            float: the value of `optical_data_temperature_5` or None if not set
        """
        return self._data["Optical Data Temperature 5"]

    @optical_data_temperature_5.setter
    def optical_data_temperature_5(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_5`

        Args:
            value (float): value for IDD Field `optical_data_temperature_5`
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
                                 'for field `optical_data_temperature_5`'.format(value))

        self._data["Optical Data Temperature 5"] = value

    @property
    def window_material_glazing_name_5(self):
        """Get window_material_glazing_name_5

        Returns:
            str: the value of `window_material_glazing_name_5` or None if not set
        """
        return self._data["Window Material Glazing Name 5"]

    @window_material_glazing_name_5.setter
    def window_material_glazing_name_5(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_5`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_5`
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
                                 'for field `window_material_glazing_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_5`')

        self._data["Window Material Glazing Name 5"] = value

    @property
    def optical_data_temperature_6(self):
        """Get optical_data_temperature_6

        Returns:
            float: the value of `optical_data_temperature_6` or None if not set
        """
        return self._data["Optical Data Temperature 6"]

    @optical_data_temperature_6.setter
    def optical_data_temperature_6(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_6`

        Args:
            value (float): value for IDD Field `optical_data_temperature_6`
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
                                 'for field `optical_data_temperature_6`'.format(value))

        self._data["Optical Data Temperature 6"] = value

    @property
    def window_material_glazing_name_6(self):
        """Get window_material_glazing_name_6

        Returns:
            str: the value of `window_material_glazing_name_6` or None if not set
        """
        return self._data["Window Material Glazing Name 6"]

    @window_material_glazing_name_6.setter
    def window_material_glazing_name_6(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_6`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_6`
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
                                 'for field `window_material_glazing_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_6`')

        self._data["Window Material Glazing Name 6"] = value

    @property
    def optical_data_temperature_7(self):
        """Get optical_data_temperature_7

        Returns:
            float: the value of `optical_data_temperature_7` or None if not set
        """
        return self._data["Optical Data Temperature 7"]

    @optical_data_temperature_7.setter
    def optical_data_temperature_7(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_7`

        Args:
            value (float): value for IDD Field `optical_data_temperature_7`
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
                                 'for field `optical_data_temperature_7`'.format(value))

        self._data["Optical Data Temperature 7"] = value

    @property
    def window_material_glazing_name_7(self):
        """Get window_material_glazing_name_7

        Returns:
            str: the value of `window_material_glazing_name_7` or None if not set
        """
        return self._data["Window Material Glazing Name 7"]

    @window_material_glazing_name_7.setter
    def window_material_glazing_name_7(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_7`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_7`
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
                                 'for field `window_material_glazing_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_7`')

        self._data["Window Material Glazing Name 7"] = value

    @property
    def optical_data_temperature_8(self):
        """Get optical_data_temperature_8

        Returns:
            float: the value of `optical_data_temperature_8` or None if not set
        """
        return self._data["Optical Data Temperature 8"]

    @optical_data_temperature_8.setter
    def optical_data_temperature_8(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_8`

        Args:
            value (float): value for IDD Field `optical_data_temperature_8`
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
                                 'for field `optical_data_temperature_8`'.format(value))

        self._data["Optical Data Temperature 8"] = value

    @property
    def window_material_glazing_name_8(self):
        """Get window_material_glazing_name_8

        Returns:
            str: the value of `window_material_glazing_name_8` or None if not set
        """
        return self._data["Window Material Glazing Name 8"]

    @window_material_glazing_name_8.setter
    def window_material_glazing_name_8(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_8`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_8`
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
                                 'for field `window_material_glazing_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_8`')

        self._data["Window Material Glazing Name 8"] = value

    @property
    def optical_data_temperature_9(self):
        """Get optical_data_temperature_9

        Returns:
            float: the value of `optical_data_temperature_9` or None if not set
        """
        return self._data["Optical Data Temperature 9"]

    @optical_data_temperature_9.setter
    def optical_data_temperature_9(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_9`

        Args:
            value (float): value for IDD Field `optical_data_temperature_9`
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
                                 'for field `optical_data_temperature_9`'.format(value))

        self._data["Optical Data Temperature 9"] = value

    @property
    def window_material_glazing_name_9(self):
        """Get window_material_glazing_name_9

        Returns:
            str: the value of `window_material_glazing_name_9` or None if not set
        """
        return self._data["Window Material Glazing Name 9"]

    @window_material_glazing_name_9.setter
    def window_material_glazing_name_9(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_9`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_9`
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
                                 'for field `window_material_glazing_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_9`')

        self._data["Window Material Glazing Name 9"] = value

    @property
    def optical_data_temperature_10(self):
        """Get optical_data_temperature_10

        Returns:
            float: the value of `optical_data_temperature_10` or None if not set
        """
        return self._data["Optical Data Temperature 10"]

    @optical_data_temperature_10.setter
    def optical_data_temperature_10(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_10`

        Args:
            value (float): value for IDD Field `optical_data_temperature_10`
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
                                 'for field `optical_data_temperature_10`'.format(value))

        self._data["Optical Data Temperature 10"] = value

    @property
    def window_material_glazing_name_10(self):
        """Get window_material_glazing_name_10

        Returns:
            str: the value of `window_material_glazing_name_10` or None if not set
        """
        return self._data["Window Material Glazing Name 10"]

    @window_material_glazing_name_10.setter
    def window_material_glazing_name_10(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_10`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_10`
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
                                 'for field `window_material_glazing_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_10`')

        self._data["Window Material Glazing Name 10"] = value

    @property
    def optical_data_temperature_11(self):
        """Get optical_data_temperature_11

        Returns:
            float: the value of `optical_data_temperature_11` or None if not set
        """
        return self._data["Optical Data Temperature 11"]

    @optical_data_temperature_11.setter
    def optical_data_temperature_11(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_11`

        Args:
            value (float): value for IDD Field `optical_data_temperature_11`
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
                                 'for field `optical_data_temperature_11`'.format(value))

        self._data["Optical Data Temperature 11"] = value

    @property
    def window_material_glazing_name_11(self):
        """Get window_material_glazing_name_11

        Returns:
            str: the value of `window_material_glazing_name_11` or None if not set
        """
        return self._data["Window Material Glazing Name 11"]

    @window_material_glazing_name_11.setter
    def window_material_glazing_name_11(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_11`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_11`
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
                                 'for field `window_material_glazing_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_11`')

        self._data["Window Material Glazing Name 11"] = value

    @property
    def optical_data_temperature_12(self):
        """Get optical_data_temperature_12

        Returns:
            float: the value of `optical_data_temperature_12` or None if not set
        """
        return self._data["Optical Data Temperature 12"]

    @optical_data_temperature_12.setter
    def optical_data_temperature_12(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_12`

        Args:
            value (float): value for IDD Field `optical_data_temperature_12`
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
                                 'for field `optical_data_temperature_12`'.format(value))

        self._data["Optical Data Temperature 12"] = value

    @property
    def window_material_glazing_name_12(self):
        """Get window_material_glazing_name_12

        Returns:
            str: the value of `window_material_glazing_name_12` or None if not set
        """
        return self._data["Window Material Glazing Name 12"]

    @window_material_glazing_name_12.setter
    def window_material_glazing_name_12(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_12`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_12`
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
                                 'for field `window_material_glazing_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_12`')

        self._data["Window Material Glazing Name 12"] = value

    @property
    def optical_data_temperature_13(self):
        """Get optical_data_temperature_13

        Returns:
            float: the value of `optical_data_temperature_13` or None if not set
        """
        return self._data["Optical Data Temperature 13"]

    @optical_data_temperature_13.setter
    def optical_data_temperature_13(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_13`

        Args:
            value (float): value for IDD Field `optical_data_temperature_13`
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
                                 'for field `optical_data_temperature_13`'.format(value))

        self._data["Optical Data Temperature 13"] = value

    @property
    def window_material_glazing_name_13(self):
        """Get window_material_glazing_name_13

        Returns:
            str: the value of `window_material_glazing_name_13` or None if not set
        """
        return self._data["Window Material Glazing Name 13"]

    @window_material_glazing_name_13.setter
    def window_material_glazing_name_13(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_13`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_13`
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
                                 'for field `window_material_glazing_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_13`')

        self._data["Window Material Glazing Name 13"] = value

    @property
    def optical_data_temperature_14(self):
        """Get optical_data_temperature_14

        Returns:
            float: the value of `optical_data_temperature_14` or None if not set
        """
        return self._data["Optical Data Temperature 14"]

    @optical_data_temperature_14.setter
    def optical_data_temperature_14(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_14`

        Args:
            value (float): value for IDD Field `optical_data_temperature_14`
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
                                 'for field `optical_data_temperature_14`'.format(value))

        self._data["Optical Data Temperature 14"] = value

    @property
    def window_material_glazing_name_14(self):
        """Get window_material_glazing_name_14

        Returns:
            str: the value of `window_material_glazing_name_14` or None if not set
        """
        return self._data["Window Material Glazing Name 14"]

    @window_material_glazing_name_14.setter
    def window_material_glazing_name_14(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_14`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_14`
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
                                 'for field `window_material_glazing_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_14`')

        self._data["Window Material Glazing Name 14"] = value

    @property
    def optical_data_temperature_15(self):
        """Get optical_data_temperature_15

        Returns:
            float: the value of `optical_data_temperature_15` or None if not set
        """
        return self._data["Optical Data Temperature 15"]

    @optical_data_temperature_15.setter
    def optical_data_temperature_15(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_15`

        Args:
            value (float): value for IDD Field `optical_data_temperature_15`
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
                                 'for field `optical_data_temperature_15`'.format(value))

        self._data["Optical Data Temperature 15"] = value

    @property
    def window_material_glazing_name_15(self):
        """Get window_material_glazing_name_15

        Returns:
            str: the value of `window_material_glazing_name_15` or None if not set
        """
        return self._data["Window Material Glazing Name 15"]

    @window_material_glazing_name_15.setter
    def window_material_glazing_name_15(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_15`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_15`
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
                                 'for field `window_material_glazing_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_15`')

        self._data["Window Material Glazing Name 15"] = value

    @property
    def optical_data_temperature_16(self):
        """Get optical_data_temperature_16

        Returns:
            float: the value of `optical_data_temperature_16` or None if not set
        """
        return self._data["Optical Data Temperature 16"]

    @optical_data_temperature_16.setter
    def optical_data_temperature_16(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_16`

        Args:
            value (float): value for IDD Field `optical_data_temperature_16`
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
                                 'for field `optical_data_temperature_16`'.format(value))

        self._data["Optical Data Temperature 16"] = value

    @property
    def window_material_glazing_name_16(self):
        """Get window_material_glazing_name_16

        Returns:
            str: the value of `window_material_glazing_name_16` or None if not set
        """
        return self._data["Window Material Glazing Name 16"]

    @window_material_glazing_name_16.setter
    def window_material_glazing_name_16(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_16`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_16`
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
                                 'for field `window_material_glazing_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_16`')

        self._data["Window Material Glazing Name 16"] = value

    @property
    def optical_data_temperature_17(self):
        """Get optical_data_temperature_17

        Returns:
            float: the value of `optical_data_temperature_17` or None if not set
        """
        return self._data["Optical Data Temperature 17"]

    @optical_data_temperature_17.setter
    def optical_data_temperature_17(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_17`

        Args:
            value (float): value for IDD Field `optical_data_temperature_17`
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
                                 'for field `optical_data_temperature_17`'.format(value))

        self._data["Optical Data Temperature 17"] = value

    @property
    def window_material_glazing_name_17(self):
        """Get window_material_glazing_name_17

        Returns:
            str: the value of `window_material_glazing_name_17` or None if not set
        """
        return self._data["Window Material Glazing Name 17"]

    @window_material_glazing_name_17.setter
    def window_material_glazing_name_17(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_17`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_17`
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
                                 'for field `window_material_glazing_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_17`')

        self._data["Window Material Glazing Name 17"] = value

    @property
    def optical_data_temperature_18(self):
        """Get optical_data_temperature_18

        Returns:
            float: the value of `optical_data_temperature_18` or None if not set
        """
        return self._data["Optical Data Temperature 18"]

    @optical_data_temperature_18.setter
    def optical_data_temperature_18(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_18`

        Args:
            value (float): value for IDD Field `optical_data_temperature_18`
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
                                 'for field `optical_data_temperature_18`'.format(value))

        self._data["Optical Data Temperature 18"] = value

    @property
    def window_material_glazing_name_18(self):
        """Get window_material_glazing_name_18

        Returns:
            str: the value of `window_material_glazing_name_18` or None if not set
        """
        return self._data["Window Material Glazing Name 18"]

    @window_material_glazing_name_18.setter
    def window_material_glazing_name_18(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_18`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_18`
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
                                 'for field `window_material_glazing_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_18`')

        self._data["Window Material Glazing Name 18"] = value

    @property
    def optical_data_temperature_19(self):
        """Get optical_data_temperature_19

        Returns:
            float: the value of `optical_data_temperature_19` or None if not set
        """
        return self._data["Optical Data Temperature 19"]

    @optical_data_temperature_19.setter
    def optical_data_temperature_19(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_19`

        Args:
            value (float): value for IDD Field `optical_data_temperature_19`
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
                                 'for field `optical_data_temperature_19`'.format(value))

        self._data["Optical Data Temperature 19"] = value

    @property
    def window_material_glazing_name_19(self):
        """Get window_material_glazing_name_19

        Returns:
            str: the value of `window_material_glazing_name_19` or None if not set
        """
        return self._data["Window Material Glazing Name 19"]

    @window_material_glazing_name_19.setter
    def window_material_glazing_name_19(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_19`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_19`
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
                                 'for field `window_material_glazing_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_19`')

        self._data["Window Material Glazing Name 19"] = value

    @property
    def optical_data_temperature_20(self):
        """Get optical_data_temperature_20

        Returns:
            float: the value of `optical_data_temperature_20` or None if not set
        """
        return self._data["Optical Data Temperature 20"]

    @optical_data_temperature_20.setter
    def optical_data_temperature_20(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_20`

        Args:
            value (float): value for IDD Field `optical_data_temperature_20`
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
                                 'for field `optical_data_temperature_20`'.format(value))

        self._data["Optical Data Temperature 20"] = value

    @property
    def window_material_glazing_name_20(self):
        """Get window_material_glazing_name_20

        Returns:
            str: the value of `window_material_glazing_name_20` or None if not set
        """
        return self._data["Window Material Glazing Name 20"]

    @window_material_glazing_name_20.setter
    def window_material_glazing_name_20(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_20`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_20`
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
                                 'for field `window_material_glazing_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_20`')

        self._data["Window Material Glazing Name 20"] = value

    @property
    def optical_data_temperature_21(self):
        """Get optical_data_temperature_21

        Returns:
            float: the value of `optical_data_temperature_21` or None if not set
        """
        return self._data["Optical Data Temperature 21"]

    @optical_data_temperature_21.setter
    def optical_data_temperature_21(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_21`

        Args:
            value (float): value for IDD Field `optical_data_temperature_21`
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
                                 'for field `optical_data_temperature_21`'.format(value))

        self._data["Optical Data Temperature 21"] = value

    @property
    def window_material_glazing_name_21(self):
        """Get window_material_glazing_name_21

        Returns:
            str: the value of `window_material_glazing_name_21` or None if not set
        """
        return self._data["Window Material Glazing Name 21"]

    @window_material_glazing_name_21.setter
    def window_material_glazing_name_21(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_21`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_21`
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
                                 'for field `window_material_glazing_name_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_21`')

        self._data["Window Material Glazing Name 21"] = value

    @property
    def optical_data_temperature_22(self):
        """Get optical_data_temperature_22

        Returns:
            float: the value of `optical_data_temperature_22` or None if not set
        """
        return self._data["Optical Data Temperature 22"]

    @optical_data_temperature_22.setter
    def optical_data_temperature_22(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_22`

        Args:
            value (float): value for IDD Field `optical_data_temperature_22`
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
                                 'for field `optical_data_temperature_22`'.format(value))

        self._data["Optical Data Temperature 22"] = value

    @property
    def window_material_glazing_name_22(self):
        """Get window_material_glazing_name_22

        Returns:
            str: the value of `window_material_glazing_name_22` or None if not set
        """
        return self._data["Window Material Glazing Name 22"]

    @window_material_glazing_name_22.setter
    def window_material_glazing_name_22(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_22`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_22`
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
                                 'for field `window_material_glazing_name_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_22`')

        self._data["Window Material Glazing Name 22"] = value

    @property
    def optical_data_temperature_23(self):
        """Get optical_data_temperature_23

        Returns:
            float: the value of `optical_data_temperature_23` or None if not set
        """
        return self._data["Optical Data Temperature 23"]

    @optical_data_temperature_23.setter
    def optical_data_temperature_23(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_23`

        Args:
            value (float): value for IDD Field `optical_data_temperature_23`
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
                                 'for field `optical_data_temperature_23`'.format(value))

        self._data["Optical Data Temperature 23"] = value

    @property
    def window_material_glazing_name_23(self):
        """Get window_material_glazing_name_23

        Returns:
            str: the value of `window_material_glazing_name_23` or None if not set
        """
        return self._data["Window Material Glazing Name 23"]

    @window_material_glazing_name_23.setter
    def window_material_glazing_name_23(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_23`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_23`
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
                                 'for field `window_material_glazing_name_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_23`')

        self._data["Window Material Glazing Name 23"] = value

    @property
    def optical_data_temperature_24(self):
        """Get optical_data_temperature_24

        Returns:
            float: the value of `optical_data_temperature_24` or None if not set
        """
        return self._data["Optical Data Temperature 24"]

    @optical_data_temperature_24.setter
    def optical_data_temperature_24(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_24`

        Args:
            value (float): value for IDD Field `optical_data_temperature_24`
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
                                 'for field `optical_data_temperature_24`'.format(value))

        self._data["Optical Data Temperature 24"] = value

    @property
    def window_material_glazing_name_24(self):
        """Get window_material_glazing_name_24

        Returns:
            str: the value of `window_material_glazing_name_24` or None if not set
        """
        return self._data["Window Material Glazing Name 24"]

    @window_material_glazing_name_24.setter
    def window_material_glazing_name_24(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_24`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_24`
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
                                 'for field `window_material_glazing_name_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_24`')

        self._data["Window Material Glazing Name 24"] = value

    @property
    def optical_data_temperature_25(self):
        """Get optical_data_temperature_25

        Returns:
            float: the value of `optical_data_temperature_25` or None if not set
        """
        return self._data["Optical Data Temperature 25"]

    @optical_data_temperature_25.setter
    def optical_data_temperature_25(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_25`

        Args:
            value (float): value for IDD Field `optical_data_temperature_25`
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
                                 'for field `optical_data_temperature_25`'.format(value))

        self._data["Optical Data Temperature 25"] = value

    @property
    def window_material_glazing_name_25(self):
        """Get window_material_glazing_name_25

        Returns:
            str: the value of `window_material_glazing_name_25` or None if not set
        """
        return self._data["Window Material Glazing Name 25"]

    @window_material_glazing_name_25.setter
    def window_material_glazing_name_25(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_25`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_25`
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
                                 'for field `window_material_glazing_name_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_25`')

        self._data["Window Material Glazing Name 25"] = value

    @property
    def optical_data_temperature_26(self):
        """Get optical_data_temperature_26

        Returns:
            float: the value of `optical_data_temperature_26` or None if not set
        """
        return self._data["Optical Data Temperature 26"]

    @optical_data_temperature_26.setter
    def optical_data_temperature_26(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_26`

        Args:
            value (float): value for IDD Field `optical_data_temperature_26`
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
                                 'for field `optical_data_temperature_26`'.format(value))

        self._data["Optical Data Temperature 26"] = value

    @property
    def window_material_glazing_name_26(self):
        """Get window_material_glazing_name_26

        Returns:
            str: the value of `window_material_glazing_name_26` or None if not set
        """
        return self._data["Window Material Glazing Name 26"]

    @window_material_glazing_name_26.setter
    def window_material_glazing_name_26(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_26`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_26`
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
                                 'for field `window_material_glazing_name_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_26`')

        self._data["Window Material Glazing Name 26"] = value

    @property
    def optical_data_temperature_27(self):
        """Get optical_data_temperature_27

        Returns:
            float: the value of `optical_data_temperature_27` or None if not set
        """
        return self._data["Optical Data Temperature 27"]

    @optical_data_temperature_27.setter
    def optical_data_temperature_27(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_27`

        Args:
            value (float): value for IDD Field `optical_data_temperature_27`
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
                                 'for field `optical_data_temperature_27`'.format(value))

        self._data["Optical Data Temperature 27"] = value

    @property
    def window_material_glazing_name_27(self):
        """Get window_material_glazing_name_27

        Returns:
            str: the value of `window_material_glazing_name_27` or None if not set
        """
        return self._data["Window Material Glazing Name 27"]

    @window_material_glazing_name_27.setter
    def window_material_glazing_name_27(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_27`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_27`
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
                                 'for field `window_material_glazing_name_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_27`')

        self._data["Window Material Glazing Name 27"] = value

    @property
    def optical_data_temperature_28(self):
        """Get optical_data_temperature_28

        Returns:
            float: the value of `optical_data_temperature_28` or None if not set
        """
        return self._data["Optical Data Temperature 28"]

    @optical_data_temperature_28.setter
    def optical_data_temperature_28(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_28`

        Args:
            value (float): value for IDD Field `optical_data_temperature_28`
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
                                 'for field `optical_data_temperature_28`'.format(value))

        self._data["Optical Data Temperature 28"] = value

    @property
    def window_material_glazing_name_28(self):
        """Get window_material_glazing_name_28

        Returns:
            str: the value of `window_material_glazing_name_28` or None if not set
        """
        return self._data["Window Material Glazing Name 28"]

    @window_material_glazing_name_28.setter
    def window_material_glazing_name_28(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_28`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_28`
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
                                 'for field `window_material_glazing_name_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_28`')

        self._data["Window Material Glazing Name 28"] = value

    @property
    def optical_data_temperature_29(self):
        """Get optical_data_temperature_29

        Returns:
            float: the value of `optical_data_temperature_29` or None if not set
        """
        return self._data["Optical Data Temperature 29"]

    @optical_data_temperature_29.setter
    def optical_data_temperature_29(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_29`

        Args:
            value (float): value for IDD Field `optical_data_temperature_29`
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
                                 'for field `optical_data_temperature_29`'.format(value))

        self._data["Optical Data Temperature 29"] = value

    @property
    def window_material_glazing_name_29(self):
        """Get window_material_glazing_name_29

        Returns:
            str: the value of `window_material_glazing_name_29` or None if not set
        """
        return self._data["Window Material Glazing Name 29"]

    @window_material_glazing_name_29.setter
    def window_material_glazing_name_29(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_29`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_29`
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
                                 'for field `window_material_glazing_name_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_29`')

        self._data["Window Material Glazing Name 29"] = value

    @property
    def optical_data_temperature_30(self):
        """Get optical_data_temperature_30

        Returns:
            float: the value of `optical_data_temperature_30` or None if not set
        """
        return self._data["Optical Data Temperature 30"]

    @optical_data_temperature_30.setter
    def optical_data_temperature_30(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_30`

        Args:
            value (float): value for IDD Field `optical_data_temperature_30`
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
                                 'for field `optical_data_temperature_30`'.format(value))

        self._data["Optical Data Temperature 30"] = value

    @property
    def window_material_glazing_name_30(self):
        """Get window_material_glazing_name_30

        Returns:
            str: the value of `window_material_glazing_name_30` or None if not set
        """
        return self._data["Window Material Glazing Name 30"]

    @window_material_glazing_name_30.setter
    def window_material_glazing_name_30(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_30`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_30`
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
                                 'for field `window_material_glazing_name_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_30`')

        self._data["Window Material Glazing Name 30"] = value

    @property
    def optical_data_temperature_31(self):
        """Get optical_data_temperature_31

        Returns:
            float: the value of `optical_data_temperature_31` or None if not set
        """
        return self._data["Optical Data Temperature 31"]

    @optical_data_temperature_31.setter
    def optical_data_temperature_31(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_31`

        Args:
            value (float): value for IDD Field `optical_data_temperature_31`
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
                                 'for field `optical_data_temperature_31`'.format(value))

        self._data["Optical Data Temperature 31"] = value

    @property
    def window_material_glazing_name_31(self):
        """Get window_material_glazing_name_31

        Returns:
            str: the value of `window_material_glazing_name_31` or None if not set
        """
        return self._data["Window Material Glazing Name 31"]

    @window_material_glazing_name_31.setter
    def window_material_glazing_name_31(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_31`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_31`
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
                                 'for field `window_material_glazing_name_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_31`')

        self._data["Window Material Glazing Name 31"] = value

    @property
    def optical_data_temperature_32(self):
        """Get optical_data_temperature_32

        Returns:
            float: the value of `optical_data_temperature_32` or None if not set
        """
        return self._data["Optical Data Temperature 32"]

    @optical_data_temperature_32.setter
    def optical_data_temperature_32(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_32`

        Args:
            value (float): value for IDD Field `optical_data_temperature_32`
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
                                 'for field `optical_data_temperature_32`'.format(value))

        self._data["Optical Data Temperature 32"] = value

    @property
    def window_material_glazing_name_32(self):
        """Get window_material_glazing_name_32

        Returns:
            str: the value of `window_material_glazing_name_32` or None if not set
        """
        return self._data["Window Material Glazing Name 32"]

    @window_material_glazing_name_32.setter
    def window_material_glazing_name_32(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_32`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_32`
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
                                 'for field `window_material_glazing_name_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_32`')

        self._data["Window Material Glazing Name 32"] = value

    @property
    def optical_data_temperature_33(self):
        """Get optical_data_temperature_33

        Returns:
            float: the value of `optical_data_temperature_33` or None if not set
        """
        return self._data["Optical Data Temperature 33"]

    @optical_data_temperature_33.setter
    def optical_data_temperature_33(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_33`

        Args:
            value (float): value for IDD Field `optical_data_temperature_33`
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
                                 'for field `optical_data_temperature_33`'.format(value))

        self._data["Optical Data Temperature 33"] = value

    @property
    def window_material_glazing_name_33(self):
        """Get window_material_glazing_name_33

        Returns:
            str: the value of `window_material_glazing_name_33` or None if not set
        """
        return self._data["Window Material Glazing Name 33"]

    @window_material_glazing_name_33.setter
    def window_material_glazing_name_33(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_33`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_33`
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
                                 'for field `window_material_glazing_name_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_33`')

        self._data["Window Material Glazing Name 33"] = value

    @property
    def optical_data_temperature_34(self):
        """Get optical_data_temperature_34

        Returns:
            float: the value of `optical_data_temperature_34` or None if not set
        """
        return self._data["Optical Data Temperature 34"]

    @optical_data_temperature_34.setter
    def optical_data_temperature_34(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_34`

        Args:
            value (float): value for IDD Field `optical_data_temperature_34`
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
                                 'for field `optical_data_temperature_34`'.format(value))

        self._data["Optical Data Temperature 34"] = value

    @property
    def window_material_glazing_name_34(self):
        """Get window_material_glazing_name_34

        Returns:
            str: the value of `window_material_glazing_name_34` or None if not set
        """
        return self._data["Window Material Glazing Name 34"]

    @window_material_glazing_name_34.setter
    def window_material_glazing_name_34(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_34`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_34`
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
                                 'for field `window_material_glazing_name_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_34`')

        self._data["Window Material Glazing Name 34"] = value

    @property
    def optical_data_temperature_35(self):
        """Get optical_data_temperature_35

        Returns:
            float: the value of `optical_data_temperature_35` or None if not set
        """
        return self._data["Optical Data Temperature 35"]

    @optical_data_temperature_35.setter
    def optical_data_temperature_35(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_35`

        Args:
            value (float): value for IDD Field `optical_data_temperature_35`
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
                                 'for field `optical_data_temperature_35`'.format(value))

        self._data["Optical Data Temperature 35"] = value

    @property
    def window_material_glazing_name_35(self):
        """Get window_material_glazing_name_35

        Returns:
            str: the value of `window_material_glazing_name_35` or None if not set
        """
        return self._data["Window Material Glazing Name 35"]

    @window_material_glazing_name_35.setter
    def window_material_glazing_name_35(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_35`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_35`
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
                                 'for field `window_material_glazing_name_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_35`')

        self._data["Window Material Glazing Name 35"] = value

    @property
    def optical_data_temperature_36(self):
        """Get optical_data_temperature_36

        Returns:
            float: the value of `optical_data_temperature_36` or None if not set
        """
        return self._data["Optical Data Temperature 36"]

    @optical_data_temperature_36.setter
    def optical_data_temperature_36(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_36`

        Args:
            value (float): value for IDD Field `optical_data_temperature_36`
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
                                 'for field `optical_data_temperature_36`'.format(value))

        self._data["Optical Data Temperature 36"] = value

    @property
    def window_material_glazing_name_36(self):
        """Get window_material_glazing_name_36

        Returns:
            str: the value of `window_material_glazing_name_36` or None if not set
        """
        return self._data["Window Material Glazing Name 36"]

    @window_material_glazing_name_36.setter
    def window_material_glazing_name_36(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_36`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_36`
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
                                 'for field `window_material_glazing_name_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_36`')

        self._data["Window Material Glazing Name 36"] = value

    @property
    def optical_data_temperature_37(self):
        """Get optical_data_temperature_37

        Returns:
            float: the value of `optical_data_temperature_37` or None if not set
        """
        return self._data["Optical Data Temperature 37"]

    @optical_data_temperature_37.setter
    def optical_data_temperature_37(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_37`

        Args:
            value (float): value for IDD Field `optical_data_temperature_37`
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
                                 'for field `optical_data_temperature_37`'.format(value))

        self._data["Optical Data Temperature 37"] = value

    @property
    def window_material_glazing_name_37(self):
        """Get window_material_glazing_name_37

        Returns:
            str: the value of `window_material_glazing_name_37` or None if not set
        """
        return self._data["Window Material Glazing Name 37"]

    @window_material_glazing_name_37.setter
    def window_material_glazing_name_37(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_37`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_37`
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
                                 'for field `window_material_glazing_name_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_37`')

        self._data["Window Material Glazing Name 37"] = value

    @property
    def optical_data_temperature_38(self):
        """Get optical_data_temperature_38

        Returns:
            float: the value of `optical_data_temperature_38` or None if not set
        """
        return self._data["Optical Data Temperature 38"]

    @optical_data_temperature_38.setter
    def optical_data_temperature_38(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_38`

        Args:
            value (float): value for IDD Field `optical_data_temperature_38`
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
                                 'for field `optical_data_temperature_38`'.format(value))

        self._data["Optical Data Temperature 38"] = value

    @property
    def window_material_glazing_name_38(self):
        """Get window_material_glazing_name_38

        Returns:
            str: the value of `window_material_glazing_name_38` or None if not set
        """
        return self._data["Window Material Glazing Name 38"]

    @window_material_glazing_name_38.setter
    def window_material_glazing_name_38(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_38`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_38`
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
                                 'for field `window_material_glazing_name_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_38`')

        self._data["Window Material Glazing Name 38"] = value

    @property
    def optical_data_temperature_39(self):
        """Get optical_data_temperature_39

        Returns:
            float: the value of `optical_data_temperature_39` or None if not set
        """
        return self._data["Optical Data Temperature 39"]

    @optical_data_temperature_39.setter
    def optical_data_temperature_39(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_39`

        Args:
            value (float): value for IDD Field `optical_data_temperature_39`
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
                                 'for field `optical_data_temperature_39`'.format(value))

        self._data["Optical Data Temperature 39"] = value

    @property
    def window_material_glazing_name_39(self):
        """Get window_material_glazing_name_39

        Returns:
            str: the value of `window_material_glazing_name_39` or None if not set
        """
        return self._data["Window Material Glazing Name 39"]

    @window_material_glazing_name_39.setter
    def window_material_glazing_name_39(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_39`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_39`
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
                                 'for field `window_material_glazing_name_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_39`')

        self._data["Window Material Glazing Name 39"] = value

    @property
    def optical_data_temperature_40(self):
        """Get optical_data_temperature_40

        Returns:
            float: the value of `optical_data_temperature_40` or None if not set
        """
        return self._data["Optical Data Temperature 40"]

    @optical_data_temperature_40.setter
    def optical_data_temperature_40(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_40`

        Args:
            value (float): value for IDD Field `optical_data_temperature_40`
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
                                 'for field `optical_data_temperature_40`'.format(value))

        self._data["Optical Data Temperature 40"] = value

    @property
    def window_material_glazing_name_40(self):
        """Get window_material_glazing_name_40

        Returns:
            str: the value of `window_material_glazing_name_40` or None if not set
        """
        return self._data["Window Material Glazing Name 40"]

    @window_material_glazing_name_40.setter
    def window_material_glazing_name_40(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_40`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_40`
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
                                 'for field `window_material_glazing_name_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_40`')

        self._data["Window Material Glazing Name 40"] = value

    @property
    def optical_data_temperature_41(self):
        """Get optical_data_temperature_41

        Returns:
            float: the value of `optical_data_temperature_41` or None if not set
        """
        return self._data["Optical Data Temperature 41"]

    @optical_data_temperature_41.setter
    def optical_data_temperature_41(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_41`

        Args:
            value (float): value for IDD Field `optical_data_temperature_41`
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
                                 'for field `optical_data_temperature_41`'.format(value))

        self._data["Optical Data Temperature 41"] = value

    @property
    def window_material_glazing_name_41(self):
        """Get window_material_glazing_name_41

        Returns:
            str: the value of `window_material_glazing_name_41` or None if not set
        """
        return self._data["Window Material Glazing Name 41"]

    @window_material_glazing_name_41.setter
    def window_material_glazing_name_41(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_41`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_41`
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
                                 'for field `window_material_glazing_name_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_41`')

        self._data["Window Material Glazing Name 41"] = value

    @property
    def optical_data_temperature_42(self):
        """Get optical_data_temperature_42

        Returns:
            float: the value of `optical_data_temperature_42` or None if not set
        """
        return self._data["Optical Data Temperature 42"]

    @optical_data_temperature_42.setter
    def optical_data_temperature_42(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_42`

        Args:
            value (float): value for IDD Field `optical_data_temperature_42`
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
                                 'for field `optical_data_temperature_42`'.format(value))

        self._data["Optical Data Temperature 42"] = value

    @property
    def window_material_glazing_name_42(self):
        """Get window_material_glazing_name_42

        Returns:
            str: the value of `window_material_glazing_name_42` or None if not set
        """
        return self._data["Window Material Glazing Name 42"]

    @window_material_glazing_name_42.setter
    def window_material_glazing_name_42(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_42`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_42`
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
                                 'for field `window_material_glazing_name_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_42`')

        self._data["Window Material Glazing Name 42"] = value

    @property
    def optical_data_temperature_43(self):
        """Get optical_data_temperature_43

        Returns:
            float: the value of `optical_data_temperature_43` or None if not set
        """
        return self._data["Optical Data Temperature 43"]

    @optical_data_temperature_43.setter
    def optical_data_temperature_43(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_43`

        Args:
            value (float): value for IDD Field `optical_data_temperature_43`
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
                                 'for field `optical_data_temperature_43`'.format(value))

        self._data["Optical Data Temperature 43"] = value

    @property
    def window_material_glazing_name_43(self):
        """Get window_material_glazing_name_43

        Returns:
            str: the value of `window_material_glazing_name_43` or None if not set
        """
        return self._data["Window Material Glazing Name 43"]

    @window_material_glazing_name_43.setter
    def window_material_glazing_name_43(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_43`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_43`
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
                                 'for field `window_material_glazing_name_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_43`')

        self._data["Window Material Glazing Name 43"] = value

    @property
    def optical_data_temperature_44(self):
        """Get optical_data_temperature_44

        Returns:
            float: the value of `optical_data_temperature_44` or None if not set
        """
        return self._data["Optical Data Temperature 44"]

    @optical_data_temperature_44.setter
    def optical_data_temperature_44(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_44`

        Args:
            value (float): value for IDD Field `optical_data_temperature_44`
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
                                 'for field `optical_data_temperature_44`'.format(value))

        self._data["Optical Data Temperature 44"] = value

    @property
    def window_material_glazing_name_44(self):
        """Get window_material_glazing_name_44

        Returns:
            str: the value of `window_material_glazing_name_44` or None if not set
        """
        return self._data["Window Material Glazing Name 44"]

    @window_material_glazing_name_44.setter
    def window_material_glazing_name_44(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_44`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_44`
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
                                 'for field `window_material_glazing_name_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_44`')

        self._data["Window Material Glazing Name 44"] = value

    @property
    def optical_data_temperature_45(self):
        """Get optical_data_temperature_45

        Returns:
            float: the value of `optical_data_temperature_45` or None if not set
        """
        return self._data["Optical Data Temperature 45"]

    @optical_data_temperature_45.setter
    def optical_data_temperature_45(self, value=None):
        """  Corresponds to IDD Field `optical_data_temperature_45`

        Args:
            value (float): value for IDD Field `optical_data_temperature_45`
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
                                 'for field `optical_data_temperature_45`'.format(value))

        self._data["Optical Data Temperature 45"] = value

    @property
    def window_material_glazing_name_45(self):
        """Get window_material_glazing_name_45

        Returns:
            str: the value of `window_material_glazing_name_45` or None if not set
        """
        return self._data["Window Material Glazing Name 45"]

    @window_material_glazing_name_45.setter
    def window_material_glazing_name_45(self, value=None):
        """  Corresponds to IDD Field `window_material_glazing_name_45`

        Args:
            value (str): value for IDD Field `window_material_glazing_name_45`
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
                                 'for field `window_material_glazing_name_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_material_glazing_name_45`')

        self._data["Window Material Glazing Name 45"] = value

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
        out.append(self._to_str(self.optical_data_temperature_1))
        out.append(self._to_str(self.window_material_glazing_name_1))
        out.append(self._to_str(self.optical_data_temperature_2))
        out.append(self._to_str(self.window_material_glazing_name_2))
        out.append(self._to_str(self.optical_data_temperature_3))
        out.append(self._to_str(self.window_material_glazing_name_3))
        out.append(self._to_str(self.optical_data_temperature_4))
        out.append(self._to_str(self.window_material_glazing_name_4))
        out.append(self._to_str(self.optical_data_temperature_5))
        out.append(self._to_str(self.window_material_glazing_name_5))
        out.append(self._to_str(self.optical_data_temperature_6))
        out.append(self._to_str(self.window_material_glazing_name_6))
        out.append(self._to_str(self.optical_data_temperature_7))
        out.append(self._to_str(self.window_material_glazing_name_7))
        out.append(self._to_str(self.optical_data_temperature_8))
        out.append(self._to_str(self.window_material_glazing_name_8))
        out.append(self._to_str(self.optical_data_temperature_9))
        out.append(self._to_str(self.window_material_glazing_name_9))
        out.append(self._to_str(self.optical_data_temperature_10))
        out.append(self._to_str(self.window_material_glazing_name_10))
        out.append(self._to_str(self.optical_data_temperature_11))
        out.append(self._to_str(self.window_material_glazing_name_11))
        out.append(self._to_str(self.optical_data_temperature_12))
        out.append(self._to_str(self.window_material_glazing_name_12))
        out.append(self._to_str(self.optical_data_temperature_13))
        out.append(self._to_str(self.window_material_glazing_name_13))
        out.append(self._to_str(self.optical_data_temperature_14))
        out.append(self._to_str(self.window_material_glazing_name_14))
        out.append(self._to_str(self.optical_data_temperature_15))
        out.append(self._to_str(self.window_material_glazing_name_15))
        out.append(self._to_str(self.optical_data_temperature_16))
        out.append(self._to_str(self.window_material_glazing_name_16))
        out.append(self._to_str(self.optical_data_temperature_17))
        out.append(self._to_str(self.window_material_glazing_name_17))
        out.append(self._to_str(self.optical_data_temperature_18))
        out.append(self._to_str(self.window_material_glazing_name_18))
        out.append(self._to_str(self.optical_data_temperature_19))
        out.append(self._to_str(self.window_material_glazing_name_19))
        out.append(self._to_str(self.optical_data_temperature_20))
        out.append(self._to_str(self.window_material_glazing_name_20))
        out.append(self._to_str(self.optical_data_temperature_21))
        out.append(self._to_str(self.window_material_glazing_name_21))
        out.append(self._to_str(self.optical_data_temperature_22))
        out.append(self._to_str(self.window_material_glazing_name_22))
        out.append(self._to_str(self.optical_data_temperature_23))
        out.append(self._to_str(self.window_material_glazing_name_23))
        out.append(self._to_str(self.optical_data_temperature_24))
        out.append(self._to_str(self.window_material_glazing_name_24))
        out.append(self._to_str(self.optical_data_temperature_25))
        out.append(self._to_str(self.window_material_glazing_name_25))
        out.append(self._to_str(self.optical_data_temperature_26))
        out.append(self._to_str(self.window_material_glazing_name_26))
        out.append(self._to_str(self.optical_data_temperature_27))
        out.append(self._to_str(self.window_material_glazing_name_27))
        out.append(self._to_str(self.optical_data_temperature_28))
        out.append(self._to_str(self.window_material_glazing_name_28))
        out.append(self._to_str(self.optical_data_temperature_29))
        out.append(self._to_str(self.window_material_glazing_name_29))
        out.append(self._to_str(self.optical_data_temperature_30))
        out.append(self._to_str(self.window_material_glazing_name_30))
        out.append(self._to_str(self.optical_data_temperature_31))
        out.append(self._to_str(self.window_material_glazing_name_31))
        out.append(self._to_str(self.optical_data_temperature_32))
        out.append(self._to_str(self.window_material_glazing_name_32))
        out.append(self._to_str(self.optical_data_temperature_33))
        out.append(self._to_str(self.window_material_glazing_name_33))
        out.append(self._to_str(self.optical_data_temperature_34))
        out.append(self._to_str(self.window_material_glazing_name_34))
        out.append(self._to_str(self.optical_data_temperature_35))
        out.append(self._to_str(self.window_material_glazing_name_35))
        out.append(self._to_str(self.optical_data_temperature_36))
        out.append(self._to_str(self.window_material_glazing_name_36))
        out.append(self._to_str(self.optical_data_temperature_37))
        out.append(self._to_str(self.window_material_glazing_name_37))
        out.append(self._to_str(self.optical_data_temperature_38))
        out.append(self._to_str(self.window_material_glazing_name_38))
        out.append(self._to_str(self.optical_data_temperature_39))
        out.append(self._to_str(self.window_material_glazing_name_39))
        out.append(self._to_str(self.optical_data_temperature_40))
        out.append(self._to_str(self.window_material_glazing_name_40))
        out.append(self._to_str(self.optical_data_temperature_41))
        out.append(self._to_str(self.window_material_glazing_name_41))
        out.append(self._to_str(self.optical_data_temperature_42))
        out.append(self._to_str(self.window_material_glazing_name_42))
        out.append(self._to_str(self.optical_data_temperature_43))
        out.append(self._to_str(self.window_material_glazing_name_43))
        out.append(self._to_str(self.optical_data_temperature_44))
        out.append(self._to_str(self.window_material_glazing_name_44))
        out.append(self._to_str(self.optical_data_temperature_45))
        out.append(self._to_str(self.window_material_glazing_name_45))
        return ",".join(out)

class WindowMaterialGlazingRefractionExtinctionMethod(object):
    """ Corresponds to IDD object `WindowMaterial:Glazing:RefractionExtinctionMethod`
        Glass material properties for Windows or Glass Doors
        Index of Refraction/Extinction Coefficient input method
        Not to be used for coated glass
    """
    internal_name = "WindowMaterial:Glazing:RefractionExtinctionMethod"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Glazing:RefractionExtinctionMethod`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Thickness"] = None
        self._data["Solar Index of Refraction"] = None
        self._data["Solar Extinction Coefficient"] = None
        self._data["Visible Index of Refraction"] = None
        self._data["Visible Extinction Coefficient"] = None
        self._data["Infrared Transmittance at Normal Incidence"] = None
        self._data["Infrared Hemispherical Emissivity"] = None
        self._data["Conductivity"] = None
        self._data["Dirt Correction Factor for Solar and Visible Transmittance"] = None
        self._data["Solar Diffusing"] = None

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
            self.thickness = None
        else:
            self.thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_index_of_refraction = None
        else:
            self.solar_index_of_refraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_extinction_coefficient = None
        else:
            self.solar_extinction_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_index_of_refraction = None
        else:
            self.visible_index_of_refraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_extinction_coefficient = None
        else:
            self.visible_extinction_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.infrared_transmittance_at_normal_incidence = None
        else:
            self.infrared_transmittance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.infrared_hemispherical_emissivity = None
        else:
            self.infrared_hemispherical_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity = None
        else:
            self.conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dirt_correction_factor_for_solar_and_visible_transmittance = None
        else:
            self.dirt_correction_factor_for_solar_and_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_diffusing = None
        else:
            self.solar_diffusing = vals[i]
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

        self._data["Thickness"] = value

    @property
    def solar_index_of_refraction(self):
        """Get solar_index_of_refraction

        Returns:
            float: the value of `solar_index_of_refraction` or None if not set
        """
        return self._data["Solar Index of Refraction"]

    @solar_index_of_refraction.setter
    def solar_index_of_refraction(self, value=None):
        """  Corresponds to IDD Field `solar_index_of_refraction`

        Args:
            value (float): value for IDD Field `solar_index_of_refraction`
                value > 1.0
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
                                 'for field `solar_index_of_refraction`'.format(value))
            if value <= 1.0:
                raise ValueError('value need to be greater 1.0 '
                                 'for field `solar_index_of_refraction`')

        self._data["Solar Index of Refraction"] = value

    @property
    def solar_extinction_coefficient(self):
        """Get solar_extinction_coefficient

        Returns:
            float: the value of `solar_extinction_coefficient` or None if not set
        """
        return self._data["Solar Extinction Coefficient"]

    @solar_extinction_coefficient.setter
    def solar_extinction_coefficient(self, value=None):
        """  Corresponds to IDD Field `solar_extinction_coefficient`

        Args:
            value (float): value for IDD Field `solar_extinction_coefficient`
                Unit: 1/m
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
                                 'for field `solar_extinction_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `solar_extinction_coefficient`')

        self._data["Solar Extinction Coefficient"] = value

    @property
    def visible_index_of_refraction(self):
        """Get visible_index_of_refraction

        Returns:
            float: the value of `visible_index_of_refraction` or None if not set
        """
        return self._data["Visible Index of Refraction"]

    @visible_index_of_refraction.setter
    def visible_index_of_refraction(self, value=None):
        """  Corresponds to IDD Field `visible_index_of_refraction`

        Args:
            value (float): value for IDD Field `visible_index_of_refraction`
                value > 1.0
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
                                 'for field `visible_index_of_refraction`'.format(value))
            if value <= 1.0:
                raise ValueError('value need to be greater 1.0 '
                                 'for field `visible_index_of_refraction`')

        self._data["Visible Index of Refraction"] = value

    @property
    def visible_extinction_coefficient(self):
        """Get visible_extinction_coefficient

        Returns:
            float: the value of `visible_extinction_coefficient` or None if not set
        """
        return self._data["Visible Extinction Coefficient"]

    @visible_extinction_coefficient.setter
    def visible_extinction_coefficient(self, value=None):
        """  Corresponds to IDD Field `visible_extinction_coefficient`

        Args:
            value (float): value for IDD Field `visible_extinction_coefficient`
                Unit: 1/m
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
                                 'for field `visible_extinction_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `visible_extinction_coefficient`')

        self._data["Visible Extinction Coefficient"] = value

    @property
    def infrared_transmittance_at_normal_incidence(self):
        """Get infrared_transmittance_at_normal_incidence

        Returns:
            float: the value of `infrared_transmittance_at_normal_incidence` or None if not set
        """
        return self._data["Infrared Transmittance at Normal Incidence"]

    @infrared_transmittance_at_normal_incidence.setter
    def infrared_transmittance_at_normal_incidence(self, value=0.0 ):
        """  Corresponds to IDD Field `infrared_transmittance_at_normal_incidence`

        Args:
            value (float): value for IDD Field `infrared_transmittance_at_normal_incidence`
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `infrared_transmittance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `infrared_transmittance_at_normal_incidence`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `infrared_transmittance_at_normal_incidence`')

        self._data["Infrared Transmittance at Normal Incidence"] = value

    @property
    def infrared_hemispherical_emissivity(self):
        """Get infrared_hemispherical_emissivity

        Returns:
            float: the value of `infrared_hemispherical_emissivity` or None if not set
        """
        return self._data["Infrared Hemispherical Emissivity"]

    @infrared_hemispherical_emissivity.setter
    def infrared_hemispherical_emissivity(self, value=0.84 ):
        """  Corresponds to IDD Field `infrared_hemispherical_emissivity`
        Emissivity of front and back side assumed equal

        Args:
            value (float): value for IDD Field `infrared_hemispherical_emissivity`
                Default value: 0.84
                value > 0.0
                value < 1.0
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
                                 'for field `infrared_hemispherical_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `infrared_hemispherical_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `infrared_hemispherical_emissivity`')

        self._data["Infrared Hemispherical Emissivity"] = value

    @property
    def conductivity(self):
        """Get conductivity

        Returns:
            float: the value of `conductivity` or None if not set
        """
        return self._data["Conductivity"]

    @conductivity.setter
    def conductivity(self, value=0.9 ):
        """  Corresponds to IDD Field `conductivity`

        Args:
            value (float): value for IDD Field `conductivity`
                Unit: W/m-K
                Default value: 0.9
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
    def dirt_correction_factor_for_solar_and_visible_transmittance(self):
        """Get dirt_correction_factor_for_solar_and_visible_transmittance

        Returns:
            float: the value of `dirt_correction_factor_for_solar_and_visible_transmittance` or None if not set
        """
        return self._data["Dirt Correction Factor for Solar and Visible Transmittance"]

    @dirt_correction_factor_for_solar_and_visible_transmittance.setter
    def dirt_correction_factor_for_solar_and_visible_transmittance(self, value=1.0 ):
        """  Corresponds to IDD Field `dirt_correction_factor_for_solar_and_visible_transmittance`

        Args:
            value (float): value for IDD Field `dirt_correction_factor_for_solar_and_visible_transmittance`
                Default value: 1.0
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
                                 'for field `dirt_correction_factor_for_solar_and_visible_transmittance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `dirt_correction_factor_for_solar_and_visible_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `dirt_correction_factor_for_solar_and_visible_transmittance`')

        self._data["Dirt Correction Factor for Solar and Visible Transmittance"] = value

    @property
    def solar_diffusing(self):
        """Get solar_diffusing

        Returns:
            str: the value of `solar_diffusing` or None if not set
        """
        return self._data["Solar Diffusing"]

    @solar_diffusing.setter
    def solar_diffusing(self, value="No"):
        """  Corresponds to IDD Field `solar_diffusing`

        Args:
            value (str): value for IDD Field `solar_diffusing`
                Accepted values are:
                      - No
                      - Yes
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
                                 'for field `solar_diffusing`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `solar_diffusing`')
            vals = set()
            vals.add("No")
            vals.add("Yes")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `solar_diffusing`'.format(value))

        self._data["Solar Diffusing"] = value

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
        out.append(self._to_str(self.thickness))
        out.append(self._to_str(self.solar_index_of_refraction))
        out.append(self._to_str(self.solar_extinction_coefficient))
        out.append(self._to_str(self.visible_index_of_refraction))
        out.append(self._to_str(self.visible_extinction_coefficient))
        out.append(self._to_str(self.infrared_transmittance_at_normal_incidence))
        out.append(self._to_str(self.infrared_hemispherical_emissivity))
        out.append(self._to_str(self.conductivity))
        out.append(self._to_str(self.dirt_correction_factor_for_solar_and_visible_transmittance))
        out.append(self._to_str(self.solar_diffusing))
        return ",".join(out)

class WindowMaterialGas(object):
    """ Corresponds to IDD object `WindowMaterial:Gas`
        Gas material properties that are used in Windows or Glass Doors
    """
    internal_name = "WindowMaterial:Gas"
    field_count = 14

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Gas`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Gas Type"] = None
        self._data["Thickness"] = None
        self._data["Conductivity Coefficient A"] = None
        self._data["Conductivity Coefficient B"] = None
        self._data["Conductivity Coefficient C"] = None
        self._data["Viscosity Coefficient A"] = None
        self._data["Viscosity Coefficient B"] = None
        self._data["Viscosity Coefficient C"] = None
        self._data["Specific Heat Coefficient A"] = None
        self._data["Specific Heat Coefficient B"] = None
        self._data["Specific Heat Coefficient C"] = None
        self._data["Molecular Weight"] = None
        self._data["Specific Heat Ratio"] = None

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
            self.gas_type = None
        else:
            self.gas_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thickness = None
        else:
            self.thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity_coefficient_a = None
        else:
            self.conductivity_coefficient_a = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity_coefficient_b = None
        else:
            self.conductivity_coefficient_b = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity_coefficient_c = None
        else:
            self.conductivity_coefficient_c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.viscosity_coefficient_a = None
        else:
            self.viscosity_coefficient_a = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.viscosity_coefficient_b = None
        else:
            self.viscosity_coefficient_b = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.viscosity_coefficient_c = None
        else:
            self.viscosity_coefficient_c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.specific_heat_coefficient_a = None
        else:
            self.specific_heat_coefficient_a = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.specific_heat_coefficient_b = None
        else:
            self.specific_heat_coefficient_b = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.specific_heat_coefficient_c = None
        else:
            self.specific_heat_coefficient_c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.molecular_weight = None
        else:
            self.molecular_weight = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.specific_heat_ratio = None
        else:
            self.specific_heat_ratio = vals[i]
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
    def gas_type(self):
        """Get gas_type

        Returns:
            str: the value of `gas_type` or None if not set
        """
        return self._data["Gas Type"]

    @gas_type.setter
    def gas_type(self, value=None):
        """  Corresponds to IDD Field `gas_type`

        Args:
            value (str): value for IDD Field `gas_type`
                Accepted values are:
                      - Air
                      - Argon
                      - Krypton
                      - Xenon
                      - Custom
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
                                 'for field `gas_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gas_type`')
            vals = set()
            vals.add("Air")
            vals.add("Argon")
            vals.add("Krypton")
            vals.add("Xenon")
            vals.add("Custom")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `gas_type`'.format(value))

        self._data["Gas Type"] = value

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

        self._data["Thickness"] = value

    @property
    def conductivity_coefficient_a(self):
        """Get conductivity_coefficient_a

        Returns:
            float: the value of `conductivity_coefficient_a` or None if not set
        """
        return self._data["Conductivity Coefficient A"]

    @conductivity_coefficient_a.setter
    def conductivity_coefficient_a(self, value=None):
        """  Corresponds to IDD Field `conductivity_coefficient_a`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `conductivity_coefficient_a`
                Unit: W/m-K
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
                                 'for field `conductivity_coefficient_a`'.format(value))

        self._data["Conductivity Coefficient A"] = value

    @property
    def conductivity_coefficient_b(self):
        """Get conductivity_coefficient_b

        Returns:
            float: the value of `conductivity_coefficient_b` or None if not set
        """
        return self._data["Conductivity Coefficient B"]

    @conductivity_coefficient_b.setter
    def conductivity_coefficient_b(self, value=None):
        """  Corresponds to IDD Field `conductivity_coefficient_b`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `conductivity_coefficient_b`
                Unit: W/m-K2
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
                                 'for field `conductivity_coefficient_b`'.format(value))

        self._data["Conductivity Coefficient B"] = value

    @property
    def conductivity_coefficient_c(self):
        """Get conductivity_coefficient_c

        Returns:
            float: the value of `conductivity_coefficient_c` or None if not set
        """
        return self._data["Conductivity Coefficient C"]

    @conductivity_coefficient_c.setter
    def conductivity_coefficient_c(self, value=None):
        """  Corresponds to IDD Field `conductivity_coefficient_c`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `conductivity_coefficient_c`
                Unit: W/m-K3
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
                                 'for field `conductivity_coefficient_c`'.format(value))

        self._data["Conductivity Coefficient C"] = value

    @property
    def viscosity_coefficient_a(self):
        """Get viscosity_coefficient_a

        Returns:
            float: the value of `viscosity_coefficient_a` or None if not set
        """
        return self._data["Viscosity Coefficient A"]

    @viscosity_coefficient_a.setter
    def viscosity_coefficient_a(self, value=None):
        """  Corresponds to IDD Field `viscosity_coefficient_a`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `viscosity_coefficient_a`
                Unit: kg/m-s
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
                                 'for field `viscosity_coefficient_a`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `viscosity_coefficient_a`')

        self._data["Viscosity Coefficient A"] = value

    @property
    def viscosity_coefficient_b(self):
        """Get viscosity_coefficient_b

        Returns:
            float: the value of `viscosity_coefficient_b` or None if not set
        """
        return self._data["Viscosity Coefficient B"]

    @viscosity_coefficient_b.setter
    def viscosity_coefficient_b(self, value=None):
        """  Corresponds to IDD Field `viscosity_coefficient_b`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `viscosity_coefficient_b`
                Unit: kg/m-s-K
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
                                 'for field `viscosity_coefficient_b`'.format(value))

        self._data["Viscosity Coefficient B"] = value

    @property
    def viscosity_coefficient_c(self):
        """Get viscosity_coefficient_c

        Returns:
            float: the value of `viscosity_coefficient_c` or None if not set
        """
        return self._data["Viscosity Coefficient C"]

    @viscosity_coefficient_c.setter
    def viscosity_coefficient_c(self, value=None):
        """  Corresponds to IDD Field `viscosity_coefficient_c`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `viscosity_coefficient_c`
                Unit: kg/m-s-K2
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
                                 'for field `viscosity_coefficient_c`'.format(value))

        self._data["Viscosity Coefficient C"] = value

    @property
    def specific_heat_coefficient_a(self):
        """Get specific_heat_coefficient_a

        Returns:
            float: the value of `specific_heat_coefficient_a` or None if not set
        """
        return self._data["Specific Heat Coefficient A"]

    @specific_heat_coefficient_a.setter
    def specific_heat_coefficient_a(self, value=None):
        """  Corresponds to IDD Field `specific_heat_coefficient_a`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `specific_heat_coefficient_a`
                Unit: J/kg-K
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
                                 'for field `specific_heat_coefficient_a`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `specific_heat_coefficient_a`')

        self._data["Specific Heat Coefficient A"] = value

    @property
    def specific_heat_coefficient_b(self):
        """Get specific_heat_coefficient_b

        Returns:
            float: the value of `specific_heat_coefficient_b` or None if not set
        """
        return self._data["Specific Heat Coefficient B"]

    @specific_heat_coefficient_b.setter
    def specific_heat_coefficient_b(self, value=None):
        """  Corresponds to IDD Field `specific_heat_coefficient_b`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `specific_heat_coefficient_b`
                Unit: J/kg-K2
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
                                 'for field `specific_heat_coefficient_b`'.format(value))

        self._data["Specific Heat Coefficient B"] = value

    @property
    def specific_heat_coefficient_c(self):
        """Get specific_heat_coefficient_c

        Returns:
            float: the value of `specific_heat_coefficient_c` or None if not set
        """
        return self._data["Specific Heat Coefficient C"]

    @specific_heat_coefficient_c.setter
    def specific_heat_coefficient_c(self, value=None):
        """  Corresponds to IDD Field `specific_heat_coefficient_c`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `specific_heat_coefficient_c`
                Unit: J/kg-K3
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
                                 'for field `specific_heat_coefficient_c`'.format(value))

        self._data["Specific Heat Coefficient C"] = value

    @property
    def molecular_weight(self):
        """Get molecular_weight

        Returns:
            float: the value of `molecular_weight` or None if not set
        """
        return self._data["Molecular Weight"]

    @molecular_weight.setter
    def molecular_weight(self, value=None):
        """  Corresponds to IDD Field `molecular_weight`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `molecular_weight`
                Unit: g/mol
                value >= 20.0
                value <= 200.0
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
                                 'for field `molecular_weight`'.format(value))
            if value < 20.0:
                raise ValueError('value need to be greater or equal 20.0 '
                                 'for field `molecular_weight`')
            if value > 200.0:
                raise ValueError('value need to be smaller 200.0 '
                                 'for field `molecular_weight`')

        self._data["Molecular Weight"] = value

    @property
    def specific_heat_ratio(self):
        """Get specific_heat_ratio

        Returns:
            float: the value of `specific_heat_ratio` or None if not set
        """
        return self._data["Specific Heat Ratio"]

    @specific_heat_ratio.setter
    def specific_heat_ratio(self, value=None):
        """  Corresponds to IDD Field `specific_heat_ratio`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `specific_heat_ratio`
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
                                 'for field `specific_heat_ratio`'.format(value))

        self._data["Specific Heat Ratio"] = value

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
        out.append(self._to_str(self.gas_type))
        out.append(self._to_str(self.thickness))
        out.append(self._to_str(self.conductivity_coefficient_a))
        out.append(self._to_str(self.conductivity_coefficient_b))
        out.append(self._to_str(self.conductivity_coefficient_c))
        out.append(self._to_str(self.viscosity_coefficient_a))
        out.append(self._to_str(self.viscosity_coefficient_b))
        out.append(self._to_str(self.viscosity_coefficient_c))
        out.append(self._to_str(self.specific_heat_coefficient_a))
        out.append(self._to_str(self.specific_heat_coefficient_b))
        out.append(self._to_str(self.specific_heat_coefficient_c))
        out.append(self._to_str(self.molecular_weight))
        out.append(self._to_str(self.specific_heat_ratio))
        return ",".join(out)

class WindowMaterialGasMixture(object):
    """ Corresponds to IDD object `WindowMaterial:GasMixture`
        Gas mixtures that are used in Windows or Glass Doors
    """
    internal_name = "WindowMaterial:GasMixture"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:GasMixture`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Thickness"] = None
        self._data["Number of Gases in Mixture"] = None
        self._data["Gas 1 Type"] = None
        self._data["Gas 1 Fraction"] = None
        self._data["Gas 2 Type"] = None
        self._data["Gas 2 Fraction"] = None
        self._data["Gas 3 Type"] = None
        self._data["Gas 3 Fraction"] = None
        self._data["Gas 4 Type"] = None
        self._data["Gas 4 Fraction"] = None

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
            self.thickness = None
        else:
            self.thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_gases_in_mixture = None
        else:
            self.number_of_gases_in_mixture = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gas_1_type = None
        else:
            self.gas_1_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gas_1_fraction = None
        else:
            self.gas_1_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gas_2_type = None
        else:
            self.gas_2_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gas_2_fraction = None
        else:
            self.gas_2_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gas_3_type = None
        else:
            self.gas_3_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gas_3_fraction = None
        else:
            self.gas_3_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gas_4_type = None
        else:
            self.gas_4_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gas_4_fraction = None
        else:
            self.gas_4_fraction = vals[i]
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

        self._data["Thickness"] = value

    @property
    def number_of_gases_in_mixture(self):
        """Get number_of_gases_in_mixture

        Returns:
            int: the value of `number_of_gases_in_mixture` or None if not set
        """
        return self._data["Number of Gases in Mixture"]

    @number_of_gases_in_mixture.setter
    def number_of_gases_in_mixture(self, value=None):
        """  Corresponds to IDD Field `number_of_gases_in_mixture`

        Args:
            value (int): value for IDD Field `number_of_gases_in_mixture`
                value >= 1
                value <= 4
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_gases_in_mixture`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_gases_in_mixture`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `number_of_gases_in_mixture`')

        self._data["Number of Gases in Mixture"] = value

    @property
    def gas_1_type(self):
        """Get gas_1_type

        Returns:
            str: the value of `gas_1_type` or None if not set
        """
        return self._data["Gas 1 Type"]

    @gas_1_type.setter
    def gas_1_type(self, value=None):
        """  Corresponds to IDD Field `gas_1_type`

        Args:
            value (str): value for IDD Field `gas_1_type`
                Accepted values are:
                      - Air
                      - Argon
                      - Krypton
                      - Xenon
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
                                 'for field `gas_1_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gas_1_type`')
            vals = set()
            vals.add("Air")
            vals.add("Argon")
            vals.add("Krypton")
            vals.add("Xenon")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `gas_1_type`'.format(value))

        self._data["Gas 1 Type"] = value

    @property
    def gas_1_fraction(self):
        """Get gas_1_fraction

        Returns:
            float: the value of `gas_1_fraction` or None if not set
        """
        return self._data["Gas 1 Fraction"]

    @gas_1_fraction.setter
    def gas_1_fraction(self, value=None):
        """  Corresponds to IDD Field `gas_1_fraction`

        Args:
            value (float): value for IDD Field `gas_1_fraction`
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
                                 'for field `gas_1_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gas_1_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `gas_1_fraction`')

        self._data["Gas 1 Fraction"] = value

    @property
    def gas_2_type(self):
        """Get gas_2_type

        Returns:
            str: the value of `gas_2_type` or None if not set
        """
        return self._data["Gas 2 Type"]

    @gas_2_type.setter
    def gas_2_type(self, value=None):
        """  Corresponds to IDD Field `gas_2_type`

        Args:
            value (str): value for IDD Field `gas_2_type`
                Accepted values are:
                      - Air
                      - Argon
                      - Krypton
                      - Xenon
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
                                 'for field `gas_2_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gas_2_type`')
            vals = set()
            vals.add("Air")
            vals.add("Argon")
            vals.add("Krypton")
            vals.add("Xenon")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `gas_2_type`'.format(value))

        self._data["Gas 2 Type"] = value

    @property
    def gas_2_fraction(self):
        """Get gas_2_fraction

        Returns:
            float: the value of `gas_2_fraction` or None if not set
        """
        return self._data["Gas 2 Fraction"]

    @gas_2_fraction.setter
    def gas_2_fraction(self, value=None):
        """  Corresponds to IDD Field `gas_2_fraction`

        Args:
            value (float): value for IDD Field `gas_2_fraction`
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
                                 'for field `gas_2_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gas_2_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `gas_2_fraction`')

        self._data["Gas 2 Fraction"] = value

    @property
    def gas_3_type(self):
        """Get gas_3_type

        Returns:
            str: the value of `gas_3_type` or None if not set
        """
        return self._data["Gas 3 Type"]

    @gas_3_type.setter
    def gas_3_type(self, value=None):
        """  Corresponds to IDD Field `gas_3_type`

        Args:
            value (str): value for IDD Field `gas_3_type`
                Accepted values are:
                      - Air
                      - Argon
                      - Krypton
                      - Xenon
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
                                 'for field `gas_3_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gas_3_type`')
            vals = set()
            vals.add("Air")
            vals.add("Argon")
            vals.add("Krypton")
            vals.add("Xenon")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `gas_3_type`'.format(value))

        self._data["Gas 3 Type"] = value

    @property
    def gas_3_fraction(self):
        """Get gas_3_fraction

        Returns:
            float: the value of `gas_3_fraction` or None if not set
        """
        return self._data["Gas 3 Fraction"]

    @gas_3_fraction.setter
    def gas_3_fraction(self, value=None):
        """  Corresponds to IDD Field `gas_3_fraction`

        Args:
            value (float): value for IDD Field `gas_3_fraction`
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
                                 'for field `gas_3_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gas_3_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `gas_3_fraction`')

        self._data["Gas 3 Fraction"] = value

    @property
    def gas_4_type(self):
        """Get gas_4_type

        Returns:
            str: the value of `gas_4_type` or None if not set
        """
        return self._data["Gas 4 Type"]

    @gas_4_type.setter
    def gas_4_type(self, value=None):
        """  Corresponds to IDD Field `gas_4_type`

        Args:
            value (str): value for IDD Field `gas_4_type`
                Accepted values are:
                      - Air
                      - Argon
                      - Krypton
                      - Xenon
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
                                 'for field `gas_4_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gas_4_type`')
            vals = set()
            vals.add("Air")
            vals.add("Argon")
            vals.add("Krypton")
            vals.add("Xenon")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `gas_4_type`'.format(value))

        self._data["Gas 4 Type"] = value

    @property
    def gas_4_fraction(self):
        """Get gas_4_fraction

        Returns:
            float: the value of `gas_4_fraction` or None if not set
        """
        return self._data["Gas 4 Fraction"]

    @gas_4_fraction.setter
    def gas_4_fraction(self, value=None):
        """  Corresponds to IDD Field `gas_4_fraction`

        Args:
            value (float): value for IDD Field `gas_4_fraction`
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
                                 'for field `gas_4_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gas_4_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `gas_4_fraction`')

        self._data["Gas 4 Fraction"] = value

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
        out.append(self._to_str(self.thickness))
        out.append(self._to_str(self.number_of_gases_in_mixture))
        out.append(self._to_str(self.gas_1_type))
        out.append(self._to_str(self.gas_1_fraction))
        out.append(self._to_str(self.gas_2_type))
        out.append(self._to_str(self.gas_2_fraction))
        out.append(self._to_str(self.gas_3_type))
        out.append(self._to_str(self.gas_3_fraction))
        out.append(self._to_str(self.gas_4_type))
        out.append(self._to_str(self.gas_4_fraction))
        return ",".join(out)

class WindowMaterialGap(object):
    """ Corresponds to IDD object `WindowMaterial:Gap`
        Used to define the gap between two layers in a complex fenestration system, where the
        Construction:ComplexFenestrationState object is used. It is referenced as a layer in the
        Construction:ComplexFenestrationState object. It cannot be referenced as a layer from the
        Construction object.
    """
    internal_name = "WindowMaterial:Gap"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Gap`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Thickness"] = None
        self._data["Gas (or Gas Mixture)"] = None
        self._data["Pressure"] = None
        self._data["Deflection State"] = None
        self._data["Support Pillar"] = None

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
            self.thickness = None
        else:
            self.thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gas_or_gas_mixture = None
        else:
            self.gas_or_gas_mixture = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pressure = None
        else:
            self.pressure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.deflection_state = None
        else:
            self.deflection_state = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.support_pillar = None
        else:
            self.support_pillar = vals[i]
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

        self._data["Thickness"] = value

    @property
    def gas_or_gas_mixture(self):
        """Get gas_or_gas_mixture

        Returns:
            str: the value of `gas_or_gas_mixture` or None if not set
        """
        return self._data["Gas (or Gas Mixture)"]

    @gas_or_gas_mixture.setter
    def gas_or_gas_mixture(self, value=None):
        """  Corresponds to IDD Field `gas_or_gas_mixture`
        This field should reference only WindowMaterial:Gas
        or WindowMaterial:GasMixture objects

        Args:
            value (str): value for IDD Field `gas_or_gas_mixture`
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
                                 'for field `gas_or_gas_mixture`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gas_or_gas_mixture`')

        self._data["Gas (or Gas Mixture)"] = value

    @property
    def pressure(self):
        """Get pressure

        Returns:
            float: the value of `pressure` or None if not set
        """
        return self._data["Pressure"]

    @pressure.setter
    def pressure(self, value=101325.0 ):
        """  Corresponds to IDD Field `pressure`

        Args:
            value (float): value for IDD Field `pressure`
                Unit: Pa
                Default value: 101325.0
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
                                 'for field `pressure`'.format(value))

        self._data["Pressure"] = value

    @property
    def deflection_state(self):
        """Get deflection_state

        Returns:
            str: the value of `deflection_state` or None if not set
        """
        return self._data["Deflection State"]

    @deflection_state.setter
    def deflection_state(self, value=None):
        """  Corresponds to IDD Field `deflection_state`
        If left blank, it will be considered that gap is not deflected

        Args:
            value (str): value for IDD Field `deflection_state`
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
                                 'for field `deflection_state`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `deflection_state`')

        self._data["Deflection State"] = value

    @property
    def support_pillar(self):
        """Get support_pillar

        Returns:
            str: the value of `support_pillar` or None if not set
        """
        return self._data["Support Pillar"]

    @support_pillar.setter
    def support_pillar(self, value=None):
        """  Corresponds to IDD Field `support_pillar`
        If left blank, it will be considered that gap does not have
        support pillars

        Args:
            value (str): value for IDD Field `support_pillar`
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
                                 'for field `support_pillar`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `support_pillar`')

        self._data["Support Pillar"] = value

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
        out.append(self._to_str(self.thickness))
        out.append(self._to_str(self.gas_or_gas_mixture))
        out.append(self._to_str(self.pressure))
        out.append(self._to_str(self.deflection_state))
        out.append(self._to_str(self.support_pillar))
        return ",".join(out)

class WindowMaterialShade(object):
    """ Corresponds to IDD object `WindowMaterial:Shade`
        Specifies the properties of window shade materials. Reflectance and emissivity
        properties are assumed to be the same on both sides of the shade. Shades are considered
        to be perfect diffusers (all transmitted and reflected radiation is
        hemispherically-diffuse) independent of angle of incidence.
    """
    internal_name = "WindowMaterial:Shade"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Shade`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Solar Transmittance"] = None
        self._data["Solar Reflectance"] = None
        self._data["Visible Transmittance"] = None
        self._data["Visible Reflectance"] = None
        self._data["Infrared Hemispherical Emissivity"] = None
        self._data["Infrared Transmittance"] = None
        self._data["Thickness"] = None
        self._data["Conductivity"] = None
        self._data["Shade to Glass Distance"] = None
        self._data["Top Opening Multiplier"] = None
        self._data["Bottom Opening Multiplier"] = None
        self._data["Left-Side Opening Multiplier"] = None
        self._data["Right-Side Opening Multiplier"] = None
        self._data["Airflow Permeability"] = None

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
            self.solar_transmittance = None
        else:
            self.solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_reflectance = None
        else:
            self.solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_transmittance = None
        else:
            self.visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_reflectance = None
        else:
            self.visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.infrared_hemispherical_emissivity = None
        else:
            self.infrared_hemispherical_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.infrared_transmittance = None
        else:
            self.infrared_transmittance = vals[i]
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
            self.shade_to_glass_distance = None
        else:
            self.shade_to_glass_distance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.top_opening_multiplier = None
        else:
            self.top_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.bottom_opening_multiplier = None
        else:
            self.bottom_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.leftside_opening_multiplier = None
        else:
            self.leftside_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rightside_opening_multiplier = None
        else:
            self.rightside_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airflow_permeability = None
        else:
            self.airflow_permeability = vals[i]
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
    def solar_transmittance(self):
        """Get solar_transmittance

        Returns:
            float: the value of `solar_transmittance` or None if not set
        """
        return self._data["Solar Transmittance"]

    @solar_transmittance.setter
    def solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `solar_transmittance`
        Assumed independent of incidence angle

        Args:
            value (float): value for IDD Field `solar_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `solar_transmittance`')

        self._data["Solar Transmittance"] = value

    @property
    def solar_reflectance(self):
        """Get solar_reflectance

        Returns:
            float: the value of `solar_reflectance` or None if not set
        """
        return self._data["Solar Reflectance"]

    @solar_reflectance.setter
    def solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `solar_reflectance`
        Assumed same for both sides
        Assumed independent of incidence angle

        Args:
            value (float): value for IDD Field `solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `solar_reflectance`')

        self._data["Solar Reflectance"] = value

    @property
    def visible_transmittance(self):
        """Get visible_transmittance

        Returns:
            float: the value of `visible_transmittance` or None if not set
        """
        return self._data["Visible Transmittance"]

    @visible_transmittance.setter
    def visible_transmittance(self, value=None):
        """  Corresponds to IDD Field `visible_transmittance`
        Assumed independent of incidence angle

        Args:
            value (float): value for IDD Field `visible_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `visible_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `visible_transmittance`')

        self._data["Visible Transmittance"] = value

    @property
    def visible_reflectance(self):
        """Get visible_reflectance

        Returns:
            float: the value of `visible_reflectance` or None if not set
        """
        return self._data["Visible Reflectance"]

    @visible_reflectance.setter
    def visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `visible_reflectance`
        Assumed same for both sides
        Assumed independent of incidence angle

        Args:
            value (float): value for IDD Field `visible_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `visible_reflectance`')

        self._data["Visible Reflectance"] = value

    @property
    def infrared_hemispherical_emissivity(self):
        """Get infrared_hemispherical_emissivity

        Returns:
            float: the value of `infrared_hemispherical_emissivity` or None if not set
        """
        return self._data["Infrared Hemispherical Emissivity"]

    @infrared_hemispherical_emissivity.setter
    def infrared_hemispherical_emissivity(self, value=None):
        """  Corresponds to IDD Field `infrared_hemispherical_emissivity`

        Args:
            value (float): value for IDD Field `infrared_hemispherical_emissivity`
                Unit: dimensionless
                value > 0.0
                value < 1.0
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
                                 'for field `infrared_hemispherical_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `infrared_hemispherical_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `infrared_hemispherical_emissivity`')

        self._data["Infrared Hemispherical Emissivity"] = value

    @property
    def infrared_transmittance(self):
        """Get infrared_transmittance

        Returns:
            float: the value of `infrared_transmittance` or None if not set
        """
        return self._data["Infrared Transmittance"]

    @infrared_transmittance.setter
    def infrared_transmittance(self, value=None):
        """  Corresponds to IDD Field `infrared_transmittance`

        Args:
            value (float): value for IDD Field `infrared_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `infrared_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `infrared_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `infrared_transmittance`')

        self._data["Infrared Transmittance"] = value

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
    def shade_to_glass_distance(self):
        """Get shade_to_glass_distance

        Returns:
            float: the value of `shade_to_glass_distance` or None if not set
        """
        return self._data["Shade to Glass Distance"]

    @shade_to_glass_distance.setter
    def shade_to_glass_distance(self, value=0.05 ):
        """  Corresponds to IDD Field `shade_to_glass_distance`

        Args:
            value (float): value for IDD Field `shade_to_glass_distance`
                Unit: m
                Default value: 0.05
                value >= 0.001
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
                                 'for field `shade_to_glass_distance`'.format(value))
            if value < 0.001:
                raise ValueError('value need to be greater or equal 0.001 '
                                 'for field `shade_to_glass_distance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `shade_to_glass_distance`')

        self._data["Shade to Glass Distance"] = value

    @property
    def top_opening_multiplier(self):
        """Get top_opening_multiplier

        Returns:
            float: the value of `top_opening_multiplier` or None if not set
        """
        return self._data["Top Opening Multiplier"]

    @top_opening_multiplier.setter
    def top_opening_multiplier(self, value=0.5 ):
        """  Corresponds to IDD Field `top_opening_multiplier`

        Args:
            value (float): value for IDD Field `top_opening_multiplier`
                Default value: 0.5
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
                                 'for field `top_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `top_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `top_opening_multiplier`')

        self._data["Top Opening Multiplier"] = value

    @property
    def bottom_opening_multiplier(self):
        """Get bottom_opening_multiplier

        Returns:
            float: the value of `bottom_opening_multiplier` or None if not set
        """
        return self._data["Bottom Opening Multiplier"]

    @bottom_opening_multiplier.setter
    def bottom_opening_multiplier(self, value=0.5 ):
        """  Corresponds to IDD Field `bottom_opening_multiplier`

        Args:
            value (float): value for IDD Field `bottom_opening_multiplier`
                Default value: 0.5
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
                                 'for field `bottom_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `bottom_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `bottom_opening_multiplier`')

        self._data["Bottom Opening Multiplier"] = value

    @property
    def leftside_opening_multiplier(self):
        """Get leftside_opening_multiplier

        Returns:
            float: the value of `leftside_opening_multiplier` or None if not set
        """
        return self._data["Left-Side Opening Multiplier"]

    @leftside_opening_multiplier.setter
    def leftside_opening_multiplier(self, value=0.5 ):
        """  Corresponds to IDD Field `leftside_opening_multiplier`

        Args:
            value (float): value for IDD Field `leftside_opening_multiplier`
                Default value: 0.5
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
                                 'for field `leftside_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `leftside_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `leftside_opening_multiplier`')

        self._data["Left-Side Opening Multiplier"] = value

    @property
    def rightside_opening_multiplier(self):
        """Get rightside_opening_multiplier

        Returns:
            float: the value of `rightside_opening_multiplier` or None if not set
        """
        return self._data["Right-Side Opening Multiplier"]

    @rightside_opening_multiplier.setter
    def rightside_opening_multiplier(self, value=0.5 ):
        """  Corresponds to IDD Field `rightside_opening_multiplier`

        Args:
            value (float): value for IDD Field `rightside_opening_multiplier`
                Default value: 0.5
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
                                 'for field `rightside_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rightside_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `rightside_opening_multiplier`')

        self._data["Right-Side Opening Multiplier"] = value

    @property
    def airflow_permeability(self):
        """Get airflow_permeability

        Returns:
            float: the value of `airflow_permeability` or None if not set
        """
        return self._data["Airflow Permeability"]

    @airflow_permeability.setter
    def airflow_permeability(self, value=0.0 ):
        """  Corresponds to IDD Field `airflow_permeability`

        Args:
            value (float): value for IDD Field `airflow_permeability`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 0.8
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
                                 'for field `airflow_permeability`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `airflow_permeability`')
            if value > 0.8:
                raise ValueError('value need to be smaller 0.8 '
                                 'for field `airflow_permeability`')

        self._data["Airflow Permeability"] = value

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
        out.append(self._to_str(self.solar_transmittance))
        out.append(self._to_str(self.solar_reflectance))
        out.append(self._to_str(self.visible_transmittance))
        out.append(self._to_str(self.visible_reflectance))
        out.append(self._to_str(self.infrared_hemispherical_emissivity))
        out.append(self._to_str(self.infrared_transmittance))
        out.append(self._to_str(self.thickness))
        out.append(self._to_str(self.conductivity))
        out.append(self._to_str(self.shade_to_glass_distance))
        out.append(self._to_str(self.top_opening_multiplier))
        out.append(self._to_str(self.bottom_opening_multiplier))
        out.append(self._to_str(self.leftside_opening_multiplier))
        out.append(self._to_str(self.rightside_opening_multiplier))
        out.append(self._to_str(self.airflow_permeability))
        return ",".join(out)

class WindowMaterialComplexShade(object):
    """ Corresponds to IDD object `WindowMaterial:ComplexShade`
        Complex window shading layer thermal properties
    """
    internal_name = "WindowMaterial:ComplexShade"
    field_count = 18

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:ComplexShade`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Layer Type"] = None
        self._data["Thickness"] = None
        self._data["Conductivity"] = None
        self._data["IR Transmittance"] = None
        self._data["Front Emissivity"] = None
        self._data["Back Emissivity"] = None
        self._data["Top Opening Multiplier"] = None
        self._data["Bottom Opening Multiplier"] = None
        self._data["Left Side Opening Multiplier"] = None
        self._data["Right Side Opening Multiplier"] = None
        self._data["Front Opening Multiplier"] = None
        self._data["Slat Width"] = None
        self._data["Slat Spacing"] = None
        self._data["Slat Thickness"] = None
        self._data["Slat Angle"] = None
        self._data["Slat Conductivity"] = None
        self._data["Slat Curve"] = None

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
            self.layer_type = None
        else:
            self.layer_type = vals[i]
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
            self.ir_transmittance = None
        else:
            self.ir_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_emissivity = None
        else:
            self.front_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_emissivity = None
        else:
            self.back_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.top_opening_multiplier = None
        else:
            self.top_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.bottom_opening_multiplier = None
        else:
            self.bottom_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.left_side_opening_multiplier = None
        else:
            self.left_side_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.right_side_opening_multiplier = None
        else:
            self.right_side_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_opening_multiplier = None
        else:
            self.front_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_width = None
        else:
            self.slat_width = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_spacing = None
        else:
            self.slat_spacing = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_thickness = None
        else:
            self.slat_thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_angle = None
        else:
            self.slat_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_conductivity = None
        else:
            self.slat_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_curve = None
        else:
            self.slat_curve = vals[i]
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
    def layer_type(self):
        """Get layer_type

        Returns:
            str: the value of `layer_type` or None if not set
        """
        return self._data["Layer Type"]

    @layer_type.setter
    def layer_type(self, value="OtherShadingType"):
        """  Corresponds to IDD Field `layer_type`

        Args:
            value (str): value for IDD Field `layer_type`
                Accepted values are:
                      - Venetian
                      - Woven
                      - Perforated
                      - BSDF
                      - OtherShadingType
                Default value: OtherShadingType
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
                                 'for field `layer_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_type`')
            vals = set()
            vals.add("Venetian")
            vals.add("Woven")
            vals.add("Perforated")
            vals.add("BSDF")
            vals.add("OtherShadingType")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `layer_type`'.format(value))

        self._data["Layer Type"] = value

    @property
    def thickness(self):
        """Get thickness

        Returns:
            float: the value of `thickness` or None if not set
        """
        return self._data["Thickness"]

    @thickness.setter
    def thickness(self, value=0.002 ):
        """  Corresponds to IDD Field `thickness`

        Args:
            value (float): value for IDD Field `thickness`
                Unit: m
                Default value: 0.002
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
                                 'for field `thickness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
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
    def conductivity(self, value=1.0 ):
        """  Corresponds to IDD Field `conductivity`

        Args:
            value (float): value for IDD Field `conductivity`
                Unit: W/m-K
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
                                 'for field `conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `conductivity`')

        self._data["Conductivity"] = value

    @property
    def ir_transmittance(self):
        """Get ir_transmittance

        Returns:
            float: the value of `ir_transmittance` or None if not set
        """
        return self._data["IR Transmittance"]

    @ir_transmittance.setter
    def ir_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `ir_transmittance`

        Args:
            value (float): value for IDD Field `ir_transmittance`
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
                                 'for field `ir_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ir_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ir_transmittance`')

        self._data["IR Transmittance"] = value

    @property
    def front_emissivity(self):
        """Get front_emissivity

        Returns:
            float: the value of `front_emissivity` or None if not set
        """
        return self._data["Front Emissivity"]

    @front_emissivity.setter
    def front_emissivity(self, value=0.84 ):
        """  Corresponds to IDD Field `front_emissivity`

        Args:
            value (float): value for IDD Field `front_emissivity`
                Default value: 0.84
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
                                 'for field `front_emissivity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_emissivity`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_emissivity`')

        self._data["Front Emissivity"] = value

    @property
    def back_emissivity(self):
        """Get back_emissivity

        Returns:
            float: the value of `back_emissivity` or None if not set
        """
        return self._data["Back Emissivity"]

    @back_emissivity.setter
    def back_emissivity(self, value=0.84 ):
        """  Corresponds to IDD Field `back_emissivity`

        Args:
            value (float): value for IDD Field `back_emissivity`
                Default value: 0.84
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
                                 'for field `back_emissivity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_emissivity`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_emissivity`')

        self._data["Back Emissivity"] = value

    @property
    def top_opening_multiplier(self):
        """Get top_opening_multiplier

        Returns:
            float: the value of `top_opening_multiplier` or None if not set
        """
        return self._data["Top Opening Multiplier"]

    @top_opening_multiplier.setter
    def top_opening_multiplier(self, value=0.0 ):
        """  Corresponds to IDD Field `top_opening_multiplier`

        Args:
            value (float): value for IDD Field `top_opening_multiplier`
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
                                 'for field `top_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `top_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `top_opening_multiplier`')

        self._data["Top Opening Multiplier"] = value

    @property
    def bottom_opening_multiplier(self):
        """Get bottom_opening_multiplier

        Returns:
            float: the value of `bottom_opening_multiplier` or None if not set
        """
        return self._data["Bottom Opening Multiplier"]

    @bottom_opening_multiplier.setter
    def bottom_opening_multiplier(self, value=0.0 ):
        """  Corresponds to IDD Field `bottom_opening_multiplier`

        Args:
            value (float): value for IDD Field `bottom_opening_multiplier`
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
                                 'for field `bottom_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `bottom_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `bottom_opening_multiplier`')

        self._data["Bottom Opening Multiplier"] = value

    @property
    def left_side_opening_multiplier(self):
        """Get left_side_opening_multiplier

        Returns:
            float: the value of `left_side_opening_multiplier` or None if not set
        """
        return self._data["Left Side Opening Multiplier"]

    @left_side_opening_multiplier.setter
    def left_side_opening_multiplier(self, value=0.0 ):
        """  Corresponds to IDD Field `left_side_opening_multiplier`

        Args:
            value (float): value for IDD Field `left_side_opening_multiplier`
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
                                 'for field `left_side_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `left_side_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `left_side_opening_multiplier`')

        self._data["Left Side Opening Multiplier"] = value

    @property
    def right_side_opening_multiplier(self):
        """Get right_side_opening_multiplier

        Returns:
            float: the value of `right_side_opening_multiplier` or None if not set
        """
        return self._data["Right Side Opening Multiplier"]

    @right_side_opening_multiplier.setter
    def right_side_opening_multiplier(self, value=0.0 ):
        """  Corresponds to IDD Field `right_side_opening_multiplier`

        Args:
            value (float): value for IDD Field `right_side_opening_multiplier`
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
                                 'for field `right_side_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `right_side_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `right_side_opening_multiplier`')

        self._data["Right Side Opening Multiplier"] = value

    @property
    def front_opening_multiplier(self):
        """Get front_opening_multiplier

        Returns:
            float: the value of `front_opening_multiplier` or None if not set
        """
        return self._data["Front Opening Multiplier"]

    @front_opening_multiplier.setter
    def front_opening_multiplier(self, value=0.05 ):
        """  Corresponds to IDD Field `front_opening_multiplier`

        Args:
            value (float): value for IDD Field `front_opening_multiplier`
                Default value: 0.05
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
                                 'for field `front_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_opening_multiplier`')

        self._data["Front Opening Multiplier"] = value

    @property
    def slat_width(self):
        """Get slat_width

        Returns:
            float: the value of `slat_width` or None if not set
        """
        return self._data["Slat Width"]

    @slat_width.setter
    def slat_width(self, value=0.016 ):
        """  Corresponds to IDD Field `slat_width`

        Args:
            value (float): value for IDD Field `slat_width`
                Unit: m
                Default value: 0.016
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
                                 'for field `slat_width`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `slat_width`')

        self._data["Slat Width"] = value

    @property
    def slat_spacing(self):
        """Get slat_spacing

        Returns:
            float: the value of `slat_spacing` or None if not set
        """
        return self._data["Slat Spacing"]

    @slat_spacing.setter
    def slat_spacing(self, value=0.012 ):
        """  Corresponds to IDD Field `slat_spacing`
        Distance between adjacent slat faces

        Args:
            value (float): value for IDD Field `slat_spacing`
                Unit: m
                Default value: 0.012
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
                                 'for field `slat_spacing`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `slat_spacing`')

        self._data["Slat Spacing"] = value

    @property
    def slat_thickness(self):
        """Get slat_thickness

        Returns:
            float: the value of `slat_thickness` or None if not set
        """
        return self._data["Slat Thickness"]

    @slat_thickness.setter
    def slat_thickness(self, value=0.0006 ):
        """  Corresponds to IDD Field `slat_thickness`
        Distance between top and bottom surfaces of slat
        Slat is assumed to be rectangular in cross section and flat

        Args:
            value (float): value for IDD Field `slat_thickness`
                Unit: m
                Default value: 0.0006
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
                                 'for field `slat_thickness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `slat_thickness`')

        self._data["Slat Thickness"] = value

    @property
    def slat_angle(self):
        """Get slat_angle

        Returns:
            float: the value of `slat_angle` or None if not set
        """
        return self._data["Slat Angle"]

    @slat_angle.setter
    def slat_angle(self, value=90.0 ):
        """  Corresponds to IDD Field `slat_angle`

        Args:
            value (float): value for IDD Field `slat_angle`
                Unit: deg
                Default value: 90.0
                value >= -90.0
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
                                 'for field `slat_angle`'.format(value))
            if value < -90.0:
                raise ValueError('value need to be greater or equal -90.0 '
                                 'for field `slat_angle`')
            if value > 90.0:
                raise ValueError('value need to be smaller 90.0 '
                                 'for field `slat_angle`')

        self._data["Slat Angle"] = value

    @property
    def slat_conductivity(self):
        """Get slat_conductivity

        Returns:
            float: the value of `slat_conductivity` or None if not set
        """
        return self._data["Slat Conductivity"]

    @slat_conductivity.setter
    def slat_conductivity(self, value=160.0 ):
        """  Corresponds to IDD Field `slat_conductivity`

        Args:
            value (float): value for IDD Field `slat_conductivity`
                Unit: W/m-K
                Default value: 160.0
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
                                 'for field `slat_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `slat_conductivity`')

        self._data["Slat Conductivity"] = value

    @property
    def slat_curve(self):
        """Get slat_curve

        Returns:
            float: the value of `slat_curve` or None if not set
        """
        return self._data["Slat Curve"]

    @slat_curve.setter
    def slat_curve(self, value=0.0 ):
        """  Corresponds to IDD Field `slat_curve`
        this value represents curvature radius of the slat.
        if the slat is flat use zero.
        if this value is not zero, then it must be > SlatWidth/2.

        Args:
            value (float): value for IDD Field `slat_curve`
                Unit: m
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
                                 'for field `slat_curve`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_curve`')

        self._data["Slat Curve"] = value

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
        out.append(self._to_str(self.layer_type))
        out.append(self._to_str(self.thickness))
        out.append(self._to_str(self.conductivity))
        out.append(self._to_str(self.ir_transmittance))
        out.append(self._to_str(self.front_emissivity))
        out.append(self._to_str(self.back_emissivity))
        out.append(self._to_str(self.top_opening_multiplier))
        out.append(self._to_str(self.bottom_opening_multiplier))
        out.append(self._to_str(self.left_side_opening_multiplier))
        out.append(self._to_str(self.right_side_opening_multiplier))
        out.append(self._to_str(self.front_opening_multiplier))
        out.append(self._to_str(self.slat_width))
        out.append(self._to_str(self.slat_spacing))
        out.append(self._to_str(self.slat_thickness))
        out.append(self._to_str(self.slat_angle))
        out.append(self._to_str(self.slat_conductivity))
        out.append(self._to_str(self.slat_curve))
        return ",".join(out)

class WindowMaterialBlind(object):
    """ Corresponds to IDD object `WindowMaterial:Blind`
        Window blind thermal properties
    """
    internal_name = "WindowMaterial:Blind"
    field_count = 29

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Blind`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Slat Orientation"] = None
        self._data["Slat Width"] = None
        self._data["Slat Separation"] = None
        self._data["Slat Thickness"] = None
        self._data["Slat Angle"] = None
        self._data["Slat Conductivity"] = None
        self._data["Slat Beam Solar Transmittance"] = None
        self._data["Front Side Slat Beam Solar Reflectance"] = None
        self._data["Back Side Slat Beam Solar Reflectance"] = None
        self._data["Slat Diffuse Solar Transmittance"] = None
        self._data["Front Side Slat Diffuse Solar Reflectance"] = None
        self._data["Back Side Slat Diffuse Solar Reflectance"] = None
        self._data["Slat Beam Visible Transmittance"] = None
        self._data["Front Side Slat Beam Visible Reflectance"] = None
        self._data["Back Side Slat Beam Visible Reflectance"] = None
        self._data["Slat Diffuse Visible Transmittance"] = None
        self._data["Front Side Slat Diffuse Visible Reflectance"] = None
        self._data["Back Side Slat Diffuse Visible Reflectance"] = None
        self._data["Slat Infrared Hemispherical Transmittance"] = None
        self._data["Front Side Slat Infrared Hemispherical Emissivity"] = None
        self._data["Back Side Slat Infrared Hemispherical Emissivity"] = None
        self._data["Blind to Glass Distance"] = None
        self._data["Blind Top Opening Multiplier"] = None
        self._data["Blind Bottom Opening Multiplier"] = None
        self._data["Blind Left Side Opening Multiplier"] = None
        self._data["Blind Right Side Opening Multiplier"] = None
        self._data["Minimum Slat Angle"] = None
        self._data["Maximum Slat Angle"] = None

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
            self.slat_orientation = None
        else:
            self.slat_orientation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_width = None
        else:
            self.slat_width = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_separation = None
        else:
            self.slat_separation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_thickness = None
        else:
            self.slat_thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_angle = None
        else:
            self.slat_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_conductivity = None
        else:
            self.slat_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_beam_solar_transmittance = None
        else:
            self.slat_beam_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_beam_solar_reflectance = None
        else:
            self.front_side_slat_beam_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_beam_solar_reflectance = None
        else:
            self.back_side_slat_beam_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_diffuse_solar_transmittance = None
        else:
            self.slat_diffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_diffuse_solar_reflectance = None
        else:
            self.front_side_slat_diffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_diffuse_solar_reflectance = None
        else:
            self.back_side_slat_diffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_beam_visible_transmittance = None
        else:
            self.slat_beam_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_beam_visible_reflectance = None
        else:
            self.front_side_slat_beam_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_beam_visible_reflectance = None
        else:
            self.back_side_slat_beam_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_diffuse_visible_transmittance = None
        else:
            self.slat_diffuse_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_diffuse_visible_reflectance = None
        else:
            self.front_side_slat_diffuse_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_diffuse_visible_reflectance = None
        else:
            self.back_side_slat_diffuse_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_infrared_hemispherical_transmittance = None
        else:
            self.slat_infrared_hemispherical_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_infrared_hemispherical_emissivity = None
        else:
            self.front_side_slat_infrared_hemispherical_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_infrared_hemispherical_emissivity = None
        else:
            self.back_side_slat_infrared_hemispherical_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blind_to_glass_distance = None
        else:
            self.blind_to_glass_distance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blind_top_opening_multiplier = None
        else:
            self.blind_top_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blind_bottom_opening_multiplier = None
        else:
            self.blind_bottom_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blind_left_side_opening_multiplier = None
        else:
            self.blind_left_side_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.blind_right_side_opening_multiplier = None
        else:
            self.blind_right_side_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_slat_angle = None
        else:
            self.minimum_slat_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_slat_angle = None
        else:
            self.maximum_slat_angle = vals[i]
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
    def slat_orientation(self):
        """Get slat_orientation

        Returns:
            str: the value of `slat_orientation` or None if not set
        """
        return self._data["Slat Orientation"]

    @slat_orientation.setter
    def slat_orientation(self, value="Horizontal"):
        """  Corresponds to IDD Field `slat_orientation`

        Args:
            value (str): value for IDD Field `slat_orientation`
                Accepted values are:
                      - Horizontal
                      - Vertical
                Default value: Horizontal
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
                                 'for field `slat_orientation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `slat_orientation`')
            vals = set()
            vals.add("Horizontal")
            vals.add("Vertical")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `slat_orientation`'.format(value))

        self._data["Slat Orientation"] = value

    @property
    def slat_width(self):
        """Get slat_width

        Returns:
            float: the value of `slat_width` or None if not set
        """
        return self._data["Slat Width"]

    @slat_width.setter
    def slat_width(self, value=None):
        """  Corresponds to IDD Field `slat_width`

        Args:
            value (float): value for IDD Field `slat_width`
                Unit: m
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
                                 'for field `slat_width`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `slat_width`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `slat_width`')

        self._data["Slat Width"] = value

    @property
    def slat_separation(self):
        """Get slat_separation

        Returns:
            float: the value of `slat_separation` or None if not set
        """
        return self._data["Slat Separation"]

    @slat_separation.setter
    def slat_separation(self, value=None):
        """  Corresponds to IDD Field `slat_separation`
        Distance between adjacent slat faces

        Args:
            value (float): value for IDD Field `slat_separation`
                Unit: m
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
                                 'for field `slat_separation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `slat_separation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `slat_separation`')

        self._data["Slat Separation"] = value

    @property
    def slat_thickness(self):
        """Get slat_thickness

        Returns:
            float: the value of `slat_thickness` or None if not set
        """
        return self._data["Slat Thickness"]

    @slat_thickness.setter
    def slat_thickness(self, value=0.00025 ):
        """  Corresponds to IDD Field `slat_thickness`
        Distance between top and bottom surfaces of slat
        Slat is assumed to be rectangular in cross section and flat

        Args:
            value (float): value for IDD Field `slat_thickness`
                Unit: m
                Default value: 0.00025
                value > 0.0
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
                                 'for field `slat_thickness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `slat_thickness`')
            if value > 0.1:
                raise ValueError('value need to be smaller 0.1 '
                                 'for field `slat_thickness`')

        self._data["Slat Thickness"] = value

    @property
    def slat_angle(self):
        """Get slat_angle

        Returns:
            float: the value of `slat_angle` or None if not set
        """
        return self._data["Slat Angle"]

    @slat_angle.setter
    def slat_angle(self, value=45.0 ):
        """  Corresponds to IDD Field `slat_angle`
        If WindowProperty:ShadingControl for the window that incorporates this blind
        has Type of Slat Angle Control for Blinds = FixedSlatAngle,
        then this is the fixed value of the slat angle;
        If WindowProperty:ShadingControl for the window that incorporates this blind
        has Type of Slat Angle Control for Blinds = BlockBeamSolar,
        then this is the slat angle when slat angle control
        is not in effect (e.g., when there is no beam solar on the blind);
        Not used if WindowProperty:ShadingControl for the window that incorporates this blind
        has Type of Slat Angle Control for Blinds = ScheduledSlatAngle.

        Args:
            value (float): value for IDD Field `slat_angle`
                Unit: deg
                Default value: 45.0
                value >= 0.0
                value <= 180.0
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
                                 'for field `slat_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `slat_angle`')

        self._data["Slat Angle"] = value

    @property
    def slat_conductivity(self):
        """Get slat_conductivity

        Returns:
            float: the value of `slat_conductivity` or None if not set
        """
        return self._data["Slat Conductivity"]

    @slat_conductivity.setter
    def slat_conductivity(self, value=221.0 ):
        """  Corresponds to IDD Field `slat_conductivity`
        default is for aluminum

        Args:
            value (float): value for IDD Field `slat_conductivity`
                Unit: W/m-K
                Default value: 221.0
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
                                 'for field `slat_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `slat_conductivity`')

        self._data["Slat Conductivity"] = value

    @property
    def slat_beam_solar_transmittance(self):
        """Get slat_beam_solar_transmittance

        Returns:
            float: the value of `slat_beam_solar_transmittance` or None if not set
        """
        return self._data["Slat Beam Solar Transmittance"]

    @slat_beam_solar_transmittance.setter
    def slat_beam_solar_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `slat_beam_solar_transmittance`

        Args:
            value (float): value for IDD Field `slat_beam_solar_transmittance`
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `slat_beam_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_beam_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `slat_beam_solar_transmittance`')

        self._data["Slat Beam Solar Transmittance"] = value

    @property
    def front_side_slat_beam_solar_reflectance(self):
        """Get front_side_slat_beam_solar_reflectance

        Returns:
            float: the value of `front_side_slat_beam_solar_reflectance` or None if not set
        """
        return self._data["Front Side Slat Beam Solar Reflectance"]

    @front_side_slat_beam_solar_reflectance.setter
    def front_side_slat_beam_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_slat_beam_solar_reflectance`

        Args:
            value (float): value for IDD Field `front_side_slat_beam_solar_reflectance`
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_beam_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_beam_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_beam_solar_reflectance`')

        self._data["Front Side Slat Beam Solar Reflectance"] = value

    @property
    def back_side_slat_beam_solar_reflectance(self):
        """Get back_side_slat_beam_solar_reflectance

        Returns:
            float: the value of `back_side_slat_beam_solar_reflectance` or None if not set
        """
        return self._data["Back Side Slat Beam Solar Reflectance"]

    @back_side_slat_beam_solar_reflectance.setter
    def back_side_slat_beam_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_slat_beam_solar_reflectance`

        Args:
            value (float): value for IDD Field `back_side_slat_beam_solar_reflectance`
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_beam_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_beam_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_beam_solar_reflectance`')

        self._data["Back Side Slat Beam Solar Reflectance"] = value

    @property
    def slat_diffuse_solar_transmittance(self):
        """Get slat_diffuse_solar_transmittance

        Returns:
            float: the value of `slat_diffuse_solar_transmittance` or None if not set
        """
        return self._data["Slat Diffuse Solar Transmittance"]

    @slat_diffuse_solar_transmittance.setter
    def slat_diffuse_solar_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `slat_diffuse_solar_transmittance`
        Must equal "Slat beam solar transmittance"

        Args:
            value (float): value for IDD Field `slat_diffuse_solar_transmittance`
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `slat_diffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_diffuse_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `slat_diffuse_solar_transmittance`')

        self._data["Slat Diffuse Solar Transmittance"] = value

    @property
    def front_side_slat_diffuse_solar_reflectance(self):
        """Get front_side_slat_diffuse_solar_reflectance

        Returns:
            float: the value of `front_side_slat_diffuse_solar_reflectance` or None if not set
        """
        return self._data["Front Side Slat Diffuse Solar Reflectance"]

    @front_side_slat_diffuse_solar_reflectance.setter
    def front_side_slat_diffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_slat_diffuse_solar_reflectance`
        Must equal "Front Side Slat Beam Solar Reflectance"

        Args:
            value (float): value for IDD Field `front_side_slat_diffuse_solar_reflectance`
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_diffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_diffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_diffuse_solar_reflectance`')

        self._data["Front Side Slat Diffuse Solar Reflectance"] = value

    @property
    def back_side_slat_diffuse_solar_reflectance(self):
        """Get back_side_slat_diffuse_solar_reflectance

        Returns:
            float: the value of `back_side_slat_diffuse_solar_reflectance` or None if not set
        """
        return self._data["Back Side Slat Diffuse Solar Reflectance"]

    @back_side_slat_diffuse_solar_reflectance.setter
    def back_side_slat_diffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_slat_diffuse_solar_reflectance`
        Must equal "Back Side Slat Beam Solar Reflectance"

        Args:
            value (float): value for IDD Field `back_side_slat_diffuse_solar_reflectance`
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_diffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_diffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_diffuse_solar_reflectance`')

        self._data["Back Side Slat Diffuse Solar Reflectance"] = value

    @property
    def slat_beam_visible_transmittance(self):
        """Get slat_beam_visible_transmittance

        Returns:
            float: the value of `slat_beam_visible_transmittance` or None if not set
        """
        return self._data["Slat Beam Visible Transmittance"]

    @slat_beam_visible_transmittance.setter
    def slat_beam_visible_transmittance(self, value=None):
        """  Corresponds to IDD Field `slat_beam_visible_transmittance`
        Required for detailed daylighting calculation

        Args:
            value (float): value for IDD Field `slat_beam_visible_transmittance`
                value >= 0.0
                value < 1.0
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
                                 'for field `slat_beam_visible_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_beam_visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `slat_beam_visible_transmittance`')

        self._data["Slat Beam Visible Transmittance"] = value

    @property
    def front_side_slat_beam_visible_reflectance(self):
        """Get front_side_slat_beam_visible_reflectance

        Returns:
            float: the value of `front_side_slat_beam_visible_reflectance` or None if not set
        """
        return self._data["Front Side Slat Beam Visible Reflectance"]

    @front_side_slat_beam_visible_reflectance.setter
    def front_side_slat_beam_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_slat_beam_visible_reflectance`
        Required for detailed daylighting calculation

        Args:
            value (float): value for IDD Field `front_side_slat_beam_visible_reflectance`
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_beam_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_beam_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_beam_visible_reflectance`')

        self._data["Front Side Slat Beam Visible Reflectance"] = value

    @property
    def back_side_slat_beam_visible_reflectance(self):
        """Get back_side_slat_beam_visible_reflectance

        Returns:
            float: the value of `back_side_slat_beam_visible_reflectance` or None if not set
        """
        return self._data["Back Side Slat Beam Visible Reflectance"]

    @back_side_slat_beam_visible_reflectance.setter
    def back_side_slat_beam_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_slat_beam_visible_reflectance`
        Required for detailed daylighting calculation

        Args:
            value (float): value for IDD Field `back_side_slat_beam_visible_reflectance`
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_beam_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_beam_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_beam_visible_reflectance`')

        self._data["Back Side Slat Beam Visible Reflectance"] = value

    @property
    def slat_diffuse_visible_transmittance(self):
        """Get slat_diffuse_visible_transmittance

        Returns:
            float: the value of `slat_diffuse_visible_transmittance` or None if not set
        """
        return self._data["Slat Diffuse Visible Transmittance"]

    @slat_diffuse_visible_transmittance.setter
    def slat_diffuse_visible_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `slat_diffuse_visible_transmittance`
        Used only for detailed daylighting calculation
        Must equal "Slat Beam Visible Transmittance"

        Args:
            value (float): value for IDD Field `slat_diffuse_visible_transmittance`
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `slat_diffuse_visible_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_diffuse_visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `slat_diffuse_visible_transmittance`')

        self._data["Slat Diffuse Visible Transmittance"] = value

    @property
    def front_side_slat_diffuse_visible_reflectance(self):
        """Get front_side_slat_diffuse_visible_reflectance

        Returns:
            float: the value of `front_side_slat_diffuse_visible_reflectance` or None if not set
        """
        return self._data["Front Side Slat Diffuse Visible Reflectance"]

    @front_side_slat_diffuse_visible_reflectance.setter
    def front_side_slat_diffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_slat_diffuse_visible_reflectance`
        Required for detailed daylighting calculation
        Must equal "Front Side Slat Beam Visible Reflectance"

        Args:
            value (float): value for IDD Field `front_side_slat_diffuse_visible_reflectance`
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_diffuse_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_diffuse_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_diffuse_visible_reflectance`')

        self._data["Front Side Slat Diffuse Visible Reflectance"] = value

    @property
    def back_side_slat_diffuse_visible_reflectance(self):
        """Get back_side_slat_diffuse_visible_reflectance

        Returns:
            float: the value of `back_side_slat_diffuse_visible_reflectance` or None if not set
        """
        return self._data["Back Side Slat Diffuse Visible Reflectance"]

    @back_side_slat_diffuse_visible_reflectance.setter
    def back_side_slat_diffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_slat_diffuse_visible_reflectance`
        Required for detailed daylighting calculation
        Must equal "Back Side Slat Beam Visible Reflectance"

        Args:
            value (float): value for IDD Field `back_side_slat_diffuse_visible_reflectance`
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_diffuse_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_diffuse_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_diffuse_visible_reflectance`')

        self._data["Back Side Slat Diffuse Visible Reflectance"] = value

    @property
    def slat_infrared_hemispherical_transmittance(self):
        """Get slat_infrared_hemispherical_transmittance

        Returns:
            float: the value of `slat_infrared_hemispherical_transmittance` or None if not set
        """
        return self._data["Slat Infrared Hemispherical Transmittance"]

    @slat_infrared_hemispherical_transmittance.setter
    def slat_infrared_hemispherical_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `slat_infrared_hemispherical_transmittance`

        Args:
            value (float): value for IDD Field `slat_infrared_hemispherical_transmittance`
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `slat_infrared_hemispherical_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_infrared_hemispherical_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `slat_infrared_hemispherical_transmittance`')

        self._data["Slat Infrared Hemispherical Transmittance"] = value

    @property
    def front_side_slat_infrared_hemispherical_emissivity(self):
        """Get front_side_slat_infrared_hemispherical_emissivity

        Returns:
            float: the value of `front_side_slat_infrared_hemispherical_emissivity` or None if not set
        """
        return self._data["Front Side Slat Infrared Hemispherical Emissivity"]

    @front_side_slat_infrared_hemispherical_emissivity.setter
    def front_side_slat_infrared_hemispherical_emissivity(self, value=0.9 ):
        """  Corresponds to IDD Field `front_side_slat_infrared_hemispherical_emissivity`

        Args:
            value (float): value for IDD Field `front_side_slat_infrared_hemispherical_emissivity`
                Default value: 0.9
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_infrared_hemispherical_emissivity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_infrared_hemispherical_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_infrared_hemispherical_emissivity`')

        self._data["Front Side Slat Infrared Hemispherical Emissivity"] = value

    @property
    def back_side_slat_infrared_hemispherical_emissivity(self):
        """Get back_side_slat_infrared_hemispherical_emissivity

        Returns:
            float: the value of `back_side_slat_infrared_hemispherical_emissivity` or None if not set
        """
        return self._data["Back Side Slat Infrared Hemispherical Emissivity"]

    @back_side_slat_infrared_hemispherical_emissivity.setter
    def back_side_slat_infrared_hemispherical_emissivity(self, value=0.9 ):
        """  Corresponds to IDD Field `back_side_slat_infrared_hemispherical_emissivity`

        Args:
            value (float): value for IDD Field `back_side_slat_infrared_hemispherical_emissivity`
                Default value: 0.9
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_infrared_hemispherical_emissivity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_infrared_hemispherical_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_infrared_hemispherical_emissivity`')

        self._data["Back Side Slat Infrared Hemispherical Emissivity"] = value

    @property
    def blind_to_glass_distance(self):
        """Get blind_to_glass_distance

        Returns:
            float: the value of `blind_to_glass_distance` or None if not set
        """
        return self._data["Blind to Glass Distance"]

    @blind_to_glass_distance.setter
    def blind_to_glass_distance(self, value=0.05 ):
        """  Corresponds to IDD Field `blind_to_glass_distance`

        Args:
            value (float): value for IDD Field `blind_to_glass_distance`
                Unit: m
                Default value: 0.05
                value >= 0.01
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
                                 'for field `blind_to_glass_distance`'.format(value))
            if value < 0.01:
                raise ValueError('value need to be greater or equal 0.01 '
                                 'for field `blind_to_glass_distance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `blind_to_glass_distance`')

        self._data["Blind to Glass Distance"] = value

    @property
    def blind_top_opening_multiplier(self):
        """Get blind_top_opening_multiplier

        Returns:
            float: the value of `blind_top_opening_multiplier` or None if not set
        """
        return self._data["Blind Top Opening Multiplier"]

    @blind_top_opening_multiplier.setter
    def blind_top_opening_multiplier(self, value=0.5 ):
        """  Corresponds to IDD Field `blind_top_opening_multiplier`

        Args:
            value (float): value for IDD Field `blind_top_opening_multiplier`
                Default value: 0.5
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
                                 'for field `blind_top_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `blind_top_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `blind_top_opening_multiplier`')

        self._data["Blind Top Opening Multiplier"] = value

    @property
    def blind_bottom_opening_multiplier(self):
        """Get blind_bottom_opening_multiplier

        Returns:
            float: the value of `blind_bottom_opening_multiplier` or None if not set
        """
        return self._data["Blind Bottom Opening Multiplier"]

    @blind_bottom_opening_multiplier.setter
    def blind_bottom_opening_multiplier(self, value=0.0 ):
        """  Corresponds to IDD Field `blind_bottom_opening_multiplier`

        Args:
            value (float): value for IDD Field `blind_bottom_opening_multiplier`
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
                                 'for field `blind_bottom_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `blind_bottom_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `blind_bottom_opening_multiplier`')

        self._data["Blind Bottom Opening Multiplier"] = value

    @property
    def blind_left_side_opening_multiplier(self):
        """Get blind_left_side_opening_multiplier

        Returns:
            float: the value of `blind_left_side_opening_multiplier` or None if not set
        """
        return self._data["Blind Left Side Opening Multiplier"]

    @blind_left_side_opening_multiplier.setter
    def blind_left_side_opening_multiplier(self, value=0.5 ):
        """  Corresponds to IDD Field `blind_left_side_opening_multiplier`

        Args:
            value (float): value for IDD Field `blind_left_side_opening_multiplier`
                Default value: 0.5
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
                                 'for field `blind_left_side_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `blind_left_side_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `blind_left_side_opening_multiplier`')

        self._data["Blind Left Side Opening Multiplier"] = value

    @property
    def blind_right_side_opening_multiplier(self):
        """Get blind_right_side_opening_multiplier

        Returns:
            float: the value of `blind_right_side_opening_multiplier` or None if not set
        """
        return self._data["Blind Right Side Opening Multiplier"]

    @blind_right_side_opening_multiplier.setter
    def blind_right_side_opening_multiplier(self, value=0.5 ):
        """  Corresponds to IDD Field `blind_right_side_opening_multiplier`

        Args:
            value (float): value for IDD Field `blind_right_side_opening_multiplier`
                Default value: 0.5
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
                                 'for field `blind_right_side_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `blind_right_side_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `blind_right_side_opening_multiplier`')

        self._data["Blind Right Side Opening Multiplier"] = value

    @property
    def minimum_slat_angle(self):
        """Get minimum_slat_angle

        Returns:
            float: the value of `minimum_slat_angle` or None if not set
        """
        return self._data["Minimum Slat Angle"]

    @minimum_slat_angle.setter
    def minimum_slat_angle(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_slat_angle`
        Used only if WindowProperty:ShadingControl for the window that incorporates
        this blind varies the slat angle (i.e., WindowProperty:ShadingControl with
        Type of Slat Angle Control for Blinds = ScheduledSlatAngle
        or BlockBeamSolar)

        Args:
            value (float): value for IDD Field `minimum_slat_angle`
                Unit: deg
                Default value: 0.0
                value >= 0.0
                value <= 180.0
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
                                 'for field `minimum_slat_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_slat_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `minimum_slat_angle`')

        self._data["Minimum Slat Angle"] = value

    @property
    def maximum_slat_angle(self):
        """Get maximum_slat_angle

        Returns:
            float: the value of `maximum_slat_angle` or None if not set
        """
        return self._data["Maximum Slat Angle"]

    @maximum_slat_angle.setter
    def maximum_slat_angle(self, value=180.0 ):
        """  Corresponds to IDD Field `maximum_slat_angle`
        Used only if WindowProperty:ShadingControl for the window that incorporates
        this blind varies the slat angle (i.e., WindowProperty:ShadingControl with
        Type of Slat Angle Control for Blinds = ScheduledSlatAngle
        or BlockBeamSolar)

        Args:
            value (float): value for IDD Field `maximum_slat_angle`
                Unit: deg
                Default value: 180.0
                value >= 0.0
                value <= 180.0
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
                                 'for field `maximum_slat_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_slat_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `maximum_slat_angle`')

        self._data["Maximum Slat Angle"] = value

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
        out.append(self._to_str(self.slat_orientation))
        out.append(self._to_str(self.slat_width))
        out.append(self._to_str(self.slat_separation))
        out.append(self._to_str(self.slat_thickness))
        out.append(self._to_str(self.slat_angle))
        out.append(self._to_str(self.slat_conductivity))
        out.append(self._to_str(self.slat_beam_solar_transmittance))
        out.append(self._to_str(self.front_side_slat_beam_solar_reflectance))
        out.append(self._to_str(self.back_side_slat_beam_solar_reflectance))
        out.append(self._to_str(self.slat_diffuse_solar_transmittance))
        out.append(self._to_str(self.front_side_slat_diffuse_solar_reflectance))
        out.append(self._to_str(self.back_side_slat_diffuse_solar_reflectance))
        out.append(self._to_str(self.slat_beam_visible_transmittance))
        out.append(self._to_str(self.front_side_slat_beam_visible_reflectance))
        out.append(self._to_str(self.back_side_slat_beam_visible_reflectance))
        out.append(self._to_str(self.slat_diffuse_visible_transmittance))
        out.append(self._to_str(self.front_side_slat_diffuse_visible_reflectance))
        out.append(self._to_str(self.back_side_slat_diffuse_visible_reflectance))
        out.append(self._to_str(self.slat_infrared_hemispherical_transmittance))
        out.append(self._to_str(self.front_side_slat_infrared_hemispherical_emissivity))
        out.append(self._to_str(self.back_side_slat_infrared_hemispherical_emissivity))
        out.append(self._to_str(self.blind_to_glass_distance))
        out.append(self._to_str(self.blind_top_opening_multiplier))
        out.append(self._to_str(self.blind_bottom_opening_multiplier))
        out.append(self._to_str(self.blind_left_side_opening_multiplier))
        out.append(self._to_str(self.blind_right_side_opening_multiplier))
        out.append(self._to_str(self.minimum_slat_angle))
        out.append(self._to_str(self.maximum_slat_angle))
        return ",".join(out)

class WindowMaterialScreen(object):
    """ Corresponds to IDD object `WindowMaterial:Screen`
        Window screen physical properties. Can only be located on the exterior side of a window construction.
    """
    internal_name = "WindowMaterial:Screen"
    field_count = 14

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Screen`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reflected Beam Transmittance Accounting Method"] = None
        self._data["Diffuse Solar Reflectance"] = None
        self._data["Diffuse Visible Reflectance"] = None
        self._data["Thermal Hemispherical Emissivity"] = None
        self._data["Conductivity"] = None
        self._data["Screen Material Spacing"] = None
        self._data["Screen Material Diameter"] = None
        self._data["Screen to Glass Distance"] = None
        self._data["Top Opening Multiplier"] = None
        self._data["Bottom Opening Multiplier"] = None
        self._data["Left Side Opening Multiplier"] = None
        self._data["Right Side Opening Multiplier"] = None
        self._data["Angle of Resolution for Screen Transmittance Output Map"] = None

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
            self.reflected_beam_transmittance_accounting_method = None
        else:
            self.reflected_beam_transmittance_accounting_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffuse_solar_reflectance = None
        else:
            self.diffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffuse_visible_reflectance = None
        else:
            self.diffuse_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_hemispherical_emissivity = None
        else:
            self.thermal_hemispherical_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity = None
        else:
            self.conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_material_spacing = None
        else:
            self.screen_material_spacing = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_material_diameter = None
        else:
            self.screen_material_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_to_glass_distance = None
        else:
            self.screen_to_glass_distance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.top_opening_multiplier = None
        else:
            self.top_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.bottom_opening_multiplier = None
        else:
            self.bottom_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.left_side_opening_multiplier = None
        else:
            self.left_side_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.right_side_opening_multiplier = None
        else:
            self.right_side_opening_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.angle_of_resolution_for_screen_transmittance_output_map = None
        else:
            self.angle_of_resolution_for_screen_transmittance_output_map = vals[i]
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
        Enter a unique name for this window screen material.

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
    def reflected_beam_transmittance_accounting_method(self):
        """Get reflected_beam_transmittance_accounting_method

        Returns:
            str: the value of `reflected_beam_transmittance_accounting_method` or None if not set
        """
        return self._data["Reflected Beam Transmittance Accounting Method"]

    @reflected_beam_transmittance_accounting_method.setter
    def reflected_beam_transmittance_accounting_method(self, value="ModelAsDiffuse"):
        """  Corresponds to IDD Field `reflected_beam_transmittance_accounting_method`
        Select the method used to account for the beam solar reflected off the material surface.

        Args:
            value (str): value for IDD Field `reflected_beam_transmittance_accounting_method`
                Accepted values are:
                      - DoNotModel
                      - ModelAsDirectBeam
                      - ModelAsDiffuse
                Default value: ModelAsDiffuse
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
                                 'for field `reflected_beam_transmittance_accounting_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reflected_beam_transmittance_accounting_method`')
            vals = set()
            vals.add("DoNotModel")
            vals.add("ModelAsDirectBeam")
            vals.add("ModelAsDiffuse")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `reflected_beam_transmittance_accounting_method`'.format(value))

        self._data["Reflected Beam Transmittance Accounting Method"] = value

    @property
    def diffuse_solar_reflectance(self):
        """Get diffuse_solar_reflectance

        Returns:
            float: the value of `diffuse_solar_reflectance` or None if not set
        """
        return self._data["Diffuse Solar Reflectance"]

    @diffuse_solar_reflectance.setter
    def diffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `diffuse_solar_reflectance`
        Diffuse reflectance of the screen material over the entire solar radiation spectrum.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `diffuse_solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `diffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `diffuse_solar_reflectance`')

        self._data["Diffuse Solar Reflectance"] = value

    @property
    def diffuse_visible_reflectance(self):
        """Get diffuse_visible_reflectance

        Returns:
            float: the value of `diffuse_visible_reflectance` or None if not set
        """
        return self._data["Diffuse Visible Reflectance"]

    @diffuse_visible_reflectance.setter
    def diffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `diffuse_visible_reflectance`
        Diffuse visible reflectance of the screen material averaged over the solar spectrum
        and weighted by the response of the human eye.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `diffuse_visible_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `diffuse_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffuse_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `diffuse_visible_reflectance`')

        self._data["Diffuse Visible Reflectance"] = value

    @property
    def thermal_hemispherical_emissivity(self):
        """Get thermal_hemispherical_emissivity

        Returns:
            float: the value of `thermal_hemispherical_emissivity` or None if not set
        """
        return self._data["Thermal Hemispherical Emissivity"]

    @thermal_hemispherical_emissivity.setter
    def thermal_hemispherical_emissivity(self, value=0.9 ):
        """  Corresponds to IDD Field `thermal_hemispherical_emissivity`
        Long-wave emissivity of the screen material.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `thermal_hemispherical_emissivity`
                Unit: dimensionless
                Default value: 0.9
                value > 0.0
                value < 1.0
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
                                 'for field `thermal_hemispherical_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_hemispherical_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `thermal_hemispherical_emissivity`')

        self._data["Thermal Hemispherical Emissivity"] = value

    @property
    def conductivity(self):
        """Get conductivity

        Returns:
            float: the value of `conductivity` or None if not set
        """
        return self._data["Conductivity"]

    @conductivity.setter
    def conductivity(self, value=221.0 ):
        """  Corresponds to IDD Field `conductivity`
        Thermal conductivity of the screen material.
        Default is for aluminum.

        Args:
            value (float): value for IDD Field `conductivity`
                Unit: W/m-K
                Default value: 221.0
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
    def screen_material_spacing(self):
        """Get screen_material_spacing

        Returns:
            float: the value of `screen_material_spacing` or None if not set
        """
        return self._data["Screen Material Spacing"]

    @screen_material_spacing.setter
    def screen_material_spacing(self, value=None):
        """  Corresponds to IDD Field `screen_material_spacing`
        Spacing assumed to be the same in both directions.

        Args:
            value (float): value for IDD Field `screen_material_spacing`
                Unit: m
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
                                 'for field `screen_material_spacing`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `screen_material_spacing`')

        self._data["Screen Material Spacing"] = value

    @property
    def screen_material_diameter(self):
        """Get screen_material_diameter

        Returns:
            float: the value of `screen_material_diameter` or None if not set
        """
        return self._data["Screen Material Diameter"]

    @screen_material_diameter.setter
    def screen_material_diameter(self, value=None):
        """  Corresponds to IDD Field `screen_material_diameter`
        Diameter assumed to be the same in both directions.

        Args:
            value (float): value for IDD Field `screen_material_diameter`
                Unit: m
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
                                 'for field `screen_material_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `screen_material_diameter`')

        self._data["Screen Material Diameter"] = value

    @property
    def screen_to_glass_distance(self):
        """Get screen_to_glass_distance

        Returns:
            float: the value of `screen_to_glass_distance` or None if not set
        """
        return self._data["Screen to Glass Distance"]

    @screen_to_glass_distance.setter
    def screen_to_glass_distance(self, value=0.025 ):
        """  Corresponds to IDD Field `screen_to_glass_distance`
        Distance from the window screen to the adjacent glass surface.

        Args:
            value (float): value for IDD Field `screen_to_glass_distance`
                Unit: m
                Default value: 0.025
                value >= 0.001
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
                                 'for field `screen_to_glass_distance`'.format(value))
            if value < 0.001:
                raise ValueError('value need to be greater or equal 0.001 '
                                 'for field `screen_to_glass_distance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `screen_to_glass_distance`')

        self._data["Screen to Glass Distance"] = value

    @property
    def top_opening_multiplier(self):
        """Get top_opening_multiplier

        Returns:
            float: the value of `top_opening_multiplier` or None if not set
        """
        return self._data["Top Opening Multiplier"]

    @top_opening_multiplier.setter
    def top_opening_multiplier(self, value=0.0 ):
        """  Corresponds to IDD Field `top_opening_multiplier`
        Effective area for air flow at the top of the screen divided by the perpendicular
        area between the glass and the top of the screen.

        Args:
            value (float): value for IDD Field `top_opening_multiplier`
                Unit: dimensionless
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
                                 'for field `top_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `top_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `top_opening_multiplier`')

        self._data["Top Opening Multiplier"] = value

    @property
    def bottom_opening_multiplier(self):
        """Get bottom_opening_multiplier

        Returns:
            float: the value of `bottom_opening_multiplier` or None if not set
        """
        return self._data["Bottom Opening Multiplier"]

    @bottom_opening_multiplier.setter
    def bottom_opening_multiplier(self, value=0.0 ):
        """  Corresponds to IDD Field `bottom_opening_multiplier`
        Effective area for air flow at the bottom of the screen divided by the perpendicular
        area between the glass and the bottom of the screen.

        Args:
            value (float): value for IDD Field `bottom_opening_multiplier`
                Unit: dimensionless
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
                                 'for field `bottom_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `bottom_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `bottom_opening_multiplier`')

        self._data["Bottom Opening Multiplier"] = value

    @property
    def left_side_opening_multiplier(self):
        """Get left_side_opening_multiplier

        Returns:
            float: the value of `left_side_opening_multiplier` or None if not set
        """
        return self._data["Left Side Opening Multiplier"]

    @left_side_opening_multiplier.setter
    def left_side_opening_multiplier(self, value=0.0 ):
        """  Corresponds to IDD Field `left_side_opening_multiplier`
        Effective area for air flow at the left side of the screen divided by the perpendicular
        area between the glass and the left side of the screen.

        Args:
            value (float): value for IDD Field `left_side_opening_multiplier`
                Unit: dimensionless
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
                                 'for field `left_side_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `left_side_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `left_side_opening_multiplier`')

        self._data["Left Side Opening Multiplier"] = value

    @property
    def right_side_opening_multiplier(self):
        """Get right_side_opening_multiplier

        Returns:
            float: the value of `right_side_opening_multiplier` or None if not set
        """
        return self._data["Right Side Opening Multiplier"]

    @right_side_opening_multiplier.setter
    def right_side_opening_multiplier(self, value=0.0 ):
        """  Corresponds to IDD Field `right_side_opening_multiplier`
        Effective area for air flow at the right side of the screen divided by the perpendicular
        area between the glass and the right side of the screen.

        Args:
            value (float): value for IDD Field `right_side_opening_multiplier`
                Unit: dimensionless
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
                                 'for field `right_side_opening_multiplier`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `right_side_opening_multiplier`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `right_side_opening_multiplier`')

        self._data["Right Side Opening Multiplier"] = value

    @property
    def angle_of_resolution_for_screen_transmittance_output_map(self):
        """Get angle_of_resolution_for_screen_transmittance_output_map

        Returns:
            str: the value of `angle_of_resolution_for_screen_transmittance_output_map` or None if not set
        """
        return self._data["Angle of Resolution for Screen Transmittance Output Map"]

    @angle_of_resolution_for_screen_transmittance_output_map.setter
    def angle_of_resolution_for_screen_transmittance_output_map(self, value="0"):
        """  Corresponds to IDD Field `angle_of_resolution_for_screen_transmittance_output_map`
        Select the resolution of azimuth and altitude angles for the screen transmittance map.
        A value of 0 means no transmittance map will be generated.
        Valid values for this field are 0, 1, 2, 3 and 5.

        Args:
            value (str): value for IDD Field `angle_of_resolution_for_screen_transmittance_output_map`
                Accepted values are:
                      - 0
                      - 1
                      - 2
                      - 3
                      - 5
                Unit: deg
                Default value: 0
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
                                 'for field `angle_of_resolution_for_screen_transmittance_output_map`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `angle_of_resolution_for_screen_transmittance_output_map`')
            vals = set()
            vals.add("0")
            vals.add("1")
            vals.add("2")
            vals.add("3")
            vals.add("5")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `angle_of_resolution_for_screen_transmittance_output_map`'.format(value))

        self._data["Angle of Resolution for Screen Transmittance Output Map"] = value

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
        out.append(self._to_str(self.reflected_beam_transmittance_accounting_method))
        out.append(self._to_str(self.diffuse_solar_reflectance))
        out.append(self._to_str(self.diffuse_visible_reflectance))
        out.append(self._to_str(self.thermal_hemispherical_emissivity))
        out.append(self._to_str(self.conductivity))
        out.append(self._to_str(self.screen_material_spacing))
        out.append(self._to_str(self.screen_material_diameter))
        out.append(self._to_str(self.screen_to_glass_distance))
        out.append(self._to_str(self.top_opening_multiplier))
        out.append(self._to_str(self.bottom_opening_multiplier))
        out.append(self._to_str(self.left_side_opening_multiplier))
        out.append(self._to_str(self.right_side_opening_multiplier))
        out.append(self._to_str(self.angle_of_resolution_for_screen_transmittance_output_map))
        return ",".join(out)

class WindowMaterialShadeEquivalentLayer(object):
    """ Corresponds to IDD object `WindowMaterial:Shade:EquivalentLayer`
        Specifies the properties of equivalent layer window shade material
        Shades are considered to be perfect diffusers (all transmitted and
        reflected radiation is hemispherically-diffuse) independent of angle
        of incidence.  Shade represents roller blinds.
    """
    internal_name = "WindowMaterial:Shade:EquivalentLayer"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Shade:EquivalentLayer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Shade Beam-Beam Solar Transmittance"] = None
        self._data["Front Side Shade Beam-Diffuse Solar Transmittance"] = None
        self._data["Back Side Shade Beam-Diffuse Solar Transmittance"] = None
        self._data["Front Side Shade Beam-Diffuse Solar Reflectance"] = None
        self._data["Back Side Shade Beam-Diffuse Solar Reflectance"] = None
        self._data["Shade Beam-Beam Visible Transmittance at Normal Incidence"] = None
        self._data["Shade Beam-Diffuse Visible Transmittance at Normal Incidence"] = None
        self._data["Shade Beam-Diffuse Visible Reflectance at Normal Incidence"] = None
        self._data["Shade Material Infrared Transmittance"] = None
        self._data["Front Side Shade Material Infrared Emissivity"] = None
        self._data["Back Side Shade Material Infrared Emissivity"] = None

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
            self.shade_beambeam_solar_transmittance = None
        else:
            self.shade_beambeam_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_shade_beamdiffuse_solar_transmittance = None
        else:
            self.front_side_shade_beamdiffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_shade_beamdiffuse_solar_transmittance = None
        else:
            self.back_side_shade_beamdiffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_shade_beamdiffuse_solar_reflectance = None
        else:
            self.front_side_shade_beamdiffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_shade_beamdiffuse_solar_reflectance = None
        else:
            self.back_side_shade_beamdiffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shade_beambeam_visible_transmittance_at_normal_incidence = None
        else:
            self.shade_beambeam_visible_transmittance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shade_beamdiffuse_visible_transmittance_at_normal_incidence = None
        else:
            self.shade_beamdiffuse_visible_transmittance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shade_beamdiffuse_visible_reflectance_at_normal_incidence = None
        else:
            self.shade_beamdiffuse_visible_reflectance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shade_material_infrared_transmittance = None
        else:
            self.shade_material_infrared_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_shade_material_infrared_emissivity = None
        else:
            self.front_side_shade_material_infrared_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_shade_material_infrared_emissivity = None
        else:
            self.back_side_shade_material_infrared_emissivity = vals[i]
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
    def shade_beambeam_solar_transmittance(self):
        """Get shade_beambeam_solar_transmittance

        Returns:
            float: the value of `shade_beambeam_solar_transmittance` or None if not set
        """
        return self._data["Shade Beam-Beam Solar Transmittance"]

    @shade_beambeam_solar_transmittance.setter
    def shade_beambeam_solar_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `shade_beambeam_solar_transmittance`
        The beam-beam solar transmittance at normal incidence.  This value is
        the same as the openness area fraction of the shade material. Assumed
        to be the same for front and back sides.

        Args:
            value (float): value for IDD Field `shade_beambeam_solar_transmittance`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 0.8
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
                                 'for field `shade_beambeam_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `shade_beambeam_solar_transmittance`')
            if value > 0.8:
                raise ValueError('value need to be smaller 0.8 '
                                 'for field `shade_beambeam_solar_transmittance`')

        self._data["Shade Beam-Beam Solar Transmittance"] = value

    @property
    def front_side_shade_beamdiffuse_solar_transmittance(self):
        """Get front_side_shade_beamdiffuse_solar_transmittance

        Returns:
            float: the value of `front_side_shade_beamdiffuse_solar_transmittance` or None if not set
        """
        return self._data["Front Side Shade Beam-Diffuse Solar Transmittance"]

    @front_side_shade_beamdiffuse_solar_transmittance.setter
    def front_side_shade_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `front_side_shade_beamdiffuse_solar_transmittance`
        The front side beam-diffuse solar transmittance at normal incidence averaged
        over the entire spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `front_side_shade_beamdiffuse_solar_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_shade_beamdiffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_shade_beamdiffuse_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_shade_beamdiffuse_solar_transmittance`')

        self._data["Front Side Shade Beam-Diffuse Solar Transmittance"] = value

    @property
    def back_side_shade_beamdiffuse_solar_transmittance(self):
        """Get back_side_shade_beamdiffuse_solar_transmittance

        Returns:
            float: the value of `back_side_shade_beamdiffuse_solar_transmittance` or None if not set
        """
        return self._data["Back Side Shade Beam-Diffuse Solar Transmittance"]

    @back_side_shade_beamdiffuse_solar_transmittance.setter
    def back_side_shade_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `back_side_shade_beamdiffuse_solar_transmittance`
        The back side beam-diffuse solar transmittance at normal incidence averaged
        over the entire spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `back_side_shade_beamdiffuse_solar_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_shade_beamdiffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_shade_beamdiffuse_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_shade_beamdiffuse_solar_transmittance`')

        self._data["Back Side Shade Beam-Diffuse Solar Transmittance"] = value

    @property
    def front_side_shade_beamdiffuse_solar_reflectance(self):
        """Get front_side_shade_beamdiffuse_solar_reflectance

        Returns:
            float: the value of `front_side_shade_beamdiffuse_solar_reflectance` or None if not set
        """
        return self._data["Front Side Shade Beam-Diffuse Solar Reflectance"]

    @front_side_shade_beamdiffuse_solar_reflectance.setter
    def front_side_shade_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_shade_beamdiffuse_solar_reflectance`
        The front side beam-diffuse solar reflectance at normal incidence averaged
        over the entire spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `front_side_shade_beamdiffuse_solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_shade_beamdiffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_shade_beamdiffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_shade_beamdiffuse_solar_reflectance`')

        self._data["Front Side Shade Beam-Diffuse Solar Reflectance"] = value

    @property
    def back_side_shade_beamdiffuse_solar_reflectance(self):
        """Get back_side_shade_beamdiffuse_solar_reflectance

        Returns:
            float: the value of `back_side_shade_beamdiffuse_solar_reflectance` or None if not set
        """
        return self._data["Back Side Shade Beam-Diffuse Solar Reflectance"]

    @back_side_shade_beamdiffuse_solar_reflectance.setter
    def back_side_shade_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_shade_beamdiffuse_solar_reflectance`
        The back side beam-diffuse solar reflectance at normal incidence averaged
        over the entire spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `back_side_shade_beamdiffuse_solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_shade_beamdiffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_shade_beamdiffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_shade_beamdiffuse_solar_reflectance`')

        self._data["Back Side Shade Beam-Diffuse Solar Reflectance"] = value

    @property
    def shade_beambeam_visible_transmittance_at_normal_incidence(self):
        """Get shade_beambeam_visible_transmittance_at_normal_incidence

        Returns:
            float: the value of `shade_beambeam_visible_transmittance_at_normal_incidence` or None if not set
        """
        return self._data["Shade Beam-Beam Visible Transmittance at Normal Incidence"]

    @shade_beambeam_visible_transmittance_at_normal_incidence.setter
    def shade_beambeam_visible_transmittance_at_normal_incidence(self, value=None):
        """  Corresponds to IDD Field `shade_beambeam_visible_transmittance_at_normal_incidence`
        The beam-beam visible transmittance at nromal incidence averaged over the
        visible spectrum range of solar radiation. Assumed to be the same for
        front and back sides of the shade.

        Args:
            value (float): value for IDD Field `shade_beambeam_visible_transmittance_at_normal_incidence`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `shade_beambeam_visible_transmittance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `shade_beambeam_visible_transmittance_at_normal_incidence`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `shade_beambeam_visible_transmittance_at_normal_incidence`')

        self._data["Shade Beam-Beam Visible Transmittance at Normal Incidence"] = value

    @property
    def shade_beamdiffuse_visible_transmittance_at_normal_incidence(self):
        """Get shade_beamdiffuse_visible_transmittance_at_normal_incidence

        Returns:
            float: the value of `shade_beamdiffuse_visible_transmittance_at_normal_incidence` or None if not set
        """
        return self._data["Shade Beam-Diffuse Visible Transmittance at Normal Incidence"]

    @shade_beamdiffuse_visible_transmittance_at_normal_incidence.setter
    def shade_beamdiffuse_visible_transmittance_at_normal_incidence(self, value=None):
        """  Corresponds to IDD Field `shade_beamdiffuse_visible_transmittance_at_normal_incidence`
        The beam-diffuse visible transmittance at nromal incidence averaged over the
        visible spectrum range of solar radiation. Assumed to be the same for
        front and back sides of the shade.

        Args:
            value (float): value for IDD Field `shade_beamdiffuse_visible_transmittance_at_normal_incidence`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `shade_beamdiffuse_visible_transmittance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `shade_beamdiffuse_visible_transmittance_at_normal_incidence`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `shade_beamdiffuse_visible_transmittance_at_normal_incidence`')

        self._data["Shade Beam-Diffuse Visible Transmittance at Normal Incidence"] = value

    @property
    def shade_beamdiffuse_visible_reflectance_at_normal_incidence(self):
        """Get shade_beamdiffuse_visible_reflectance_at_normal_incidence

        Returns:
            float: the value of `shade_beamdiffuse_visible_reflectance_at_normal_incidence` or None if not set
        """
        return self._data["Shade Beam-Diffuse Visible Reflectance at Normal Incidence"]

    @shade_beamdiffuse_visible_reflectance_at_normal_incidence.setter
    def shade_beamdiffuse_visible_reflectance_at_normal_incidence(self, value=None):
        """  Corresponds to IDD Field `shade_beamdiffuse_visible_reflectance_at_normal_incidence`
        The beam-diffuse visible reflectance at nromal incidence averaged over the
        visible spectrum range of solar radiation. Assumed to be the same for
        front and back sides of the shade.

        Args:
            value (float): value for IDD Field `shade_beamdiffuse_visible_reflectance_at_normal_incidence`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `shade_beamdiffuse_visible_reflectance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `shade_beamdiffuse_visible_reflectance_at_normal_incidence`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `shade_beamdiffuse_visible_reflectance_at_normal_incidence`')

        self._data["Shade Beam-Diffuse Visible Reflectance at Normal Incidence"] = value

    @property
    def shade_material_infrared_transmittance(self):
        """Get shade_material_infrared_transmittance

        Returns:
            float: the value of `shade_material_infrared_transmittance` or None if not set
        """
        return self._data["Shade Material Infrared Transmittance"]

    @shade_material_infrared_transmittance.setter
    def shade_material_infrared_transmittance(self, value=0.05 ):
        """  Corresponds to IDD Field `shade_material_infrared_transmittance`
        The long-wave transmittance of the shade material at zero shade openness.
        Assumed to be the same for front and back sides of the shade.

        Args:
            value (float): value for IDD Field `shade_material_infrared_transmittance`
                Unit: dimensionless
                Default value: 0.05
                value >= 0.0
                value < 1.0
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
                                 'for field `shade_material_infrared_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `shade_material_infrared_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `shade_material_infrared_transmittance`')

        self._data["Shade Material Infrared Transmittance"] = value

    @property
    def front_side_shade_material_infrared_emissivity(self):
        """Get front_side_shade_material_infrared_emissivity

        Returns:
            float: the value of `front_side_shade_material_infrared_emissivity` or None if not set
        """
        return self._data["Front Side Shade Material Infrared Emissivity"]

    @front_side_shade_material_infrared_emissivity.setter
    def front_side_shade_material_infrared_emissivity(self, value=0.91 ):
        """  Corresponds to IDD Field `front_side_shade_material_infrared_emissivity`
        The front side long-wave emissivity of the shade material at zero shade
        openness. Openness fraction is used to calculate the effective emissivity
        value.

        Args:
            value (float): value for IDD Field `front_side_shade_material_infrared_emissivity`
                Unit: dimensionless
                Default value: 0.91
                value > 0.0
                value < 1.0
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
                                 'for field `front_side_shade_material_infrared_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `front_side_shade_material_infrared_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_shade_material_infrared_emissivity`')

        self._data["Front Side Shade Material Infrared Emissivity"] = value

    @property
    def back_side_shade_material_infrared_emissivity(self):
        """Get back_side_shade_material_infrared_emissivity

        Returns:
            float: the value of `back_side_shade_material_infrared_emissivity` or None if not set
        """
        return self._data["Back Side Shade Material Infrared Emissivity"]

    @back_side_shade_material_infrared_emissivity.setter
    def back_side_shade_material_infrared_emissivity(self, value=0.91 ):
        """  Corresponds to IDD Field `back_side_shade_material_infrared_emissivity`
        The back side long-wave emissivity of the shade material at zero shade
        openness. Openness fraction is used to calculate the effective emissivity
        value.

        Args:
            value (float): value for IDD Field `back_side_shade_material_infrared_emissivity`
                Unit: dimensionless
                Default value: 0.91
                value > 0.0
                value < 1.0
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
                                 'for field `back_side_shade_material_infrared_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `back_side_shade_material_infrared_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_shade_material_infrared_emissivity`')

        self._data["Back Side Shade Material Infrared Emissivity"] = value

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
        out.append(self._to_str(self.shade_beambeam_solar_transmittance))
        out.append(self._to_str(self.front_side_shade_beamdiffuse_solar_transmittance))
        out.append(self._to_str(self.back_side_shade_beamdiffuse_solar_transmittance))
        out.append(self._to_str(self.front_side_shade_beamdiffuse_solar_reflectance))
        out.append(self._to_str(self.back_side_shade_beamdiffuse_solar_reflectance))
        out.append(self._to_str(self.shade_beambeam_visible_transmittance_at_normal_incidence))
        out.append(self._to_str(self.shade_beamdiffuse_visible_transmittance_at_normal_incidence))
        out.append(self._to_str(self.shade_beamdiffuse_visible_reflectance_at_normal_incidence))
        out.append(self._to_str(self.shade_material_infrared_transmittance))
        out.append(self._to_str(self.front_side_shade_material_infrared_emissivity))
        out.append(self._to_str(self.back_side_shade_material_infrared_emissivity))
        return ",".join(out)

class WindowMaterialDrapeEquivalentLayer(object):
    """ Corresponds to IDD object `WindowMaterial:Drape:EquivalentLayer`
        Specifies the properties of equivalent layer drape fabirc materials.
        Shades are considered to be perfect diffusers (all transmitted and reflected
        radiation is hemispherically-diffuse) independent of angle of incidence.
        unpleated drape fabric is treated as thin and flat layer.
    """
    internal_name = "WindowMaterial:Drape:EquivalentLayer"
    field_count = 14

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Drape:EquivalentLayer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Drape Beam-Beam Solar Transmittance at Normal Incidence"] = None
        self._data["Front Side Drape Beam-Diffuse Solar Transmittance"] = None
        self._data["Back Side Drape Beam-Diffuse Solar Transmittance"] = None
        self._data["Front Side Drape Beam-Diffuse Solar Reflectance"] = None
        self._data["Back Side Drape Beam-Diffuse Solar Reflectance"] = None
        self._data["Drape Beam-Beam Visible Transmittance"] = None
        self._data["Drape Beam-Diffuse Visible Transmittance"] = None
        self._data["Drape Beam-Diffuse Visible Reflectance"] = None
        self._data["Drape Material Infrared Transmittance"] = None
        self._data["Front Side Drape Material Infrared Emissivity"] = None
        self._data["Back Side Drape Material Infrared Emissivity"] = None
        self._data["Width of Pleated Fabric"] = None
        self._data["Length of Pleated Fabric"] = None

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
            self.drape_beambeam_solar_transmittance_at_normal_incidence = None
        else:
            self.drape_beambeam_solar_transmittance_at_normal_incidence = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_drape_beamdiffuse_solar_transmittance = None
        else:
            self.front_side_drape_beamdiffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_drape_beamdiffuse_solar_transmittance = None
        else:
            self.back_side_drape_beamdiffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_drape_beamdiffuse_solar_reflectance = None
        else:
            self.front_side_drape_beamdiffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_drape_beamdiffuse_solar_reflectance = None
        else:
            self.back_side_drape_beamdiffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drape_beambeam_visible_transmittance = None
        else:
            self.drape_beambeam_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drape_beamdiffuse_visible_transmittance = None
        else:
            self.drape_beamdiffuse_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drape_beamdiffuse_visible_reflectance = None
        else:
            self.drape_beamdiffuse_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drape_material_infrared_transmittance = None
        else:
            self.drape_material_infrared_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_drape_material_infrared_emissivity = None
        else:
            self.front_side_drape_material_infrared_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_drape_material_infrared_emissivity = None
        else:
            self.back_side_drape_material_infrared_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.width_of_pleated_fabric = None
        else:
            self.width_of_pleated_fabric = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.length_of_pleated_fabric = None
        else:
            self.length_of_pleated_fabric = vals[i]
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
    def drape_beambeam_solar_transmittance_at_normal_incidence(self):
        """Get drape_beambeam_solar_transmittance_at_normal_incidence

        Returns:
            float: the value of `drape_beambeam_solar_transmittance_at_normal_incidence` or None if not set
        """
        return self._data["Drape Beam-Beam Solar Transmittance at Normal Incidence"]

    @drape_beambeam_solar_transmittance_at_normal_incidence.setter
    def drape_beambeam_solar_transmittance_at_normal_incidence(self, value=0.0 ):
        """  Corresponds to IDD Field `drape_beambeam_solar_transmittance_at_normal_incidence`
        The beam-beam solar transmittance at normal incidence. This value is the
        same as the openness area fraction of the drape fabric. Assumed to be
        same for front and back sides.

        Args:
            value (float): value for IDD Field `drape_beambeam_solar_transmittance_at_normal_incidence`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value <= 0.2
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
                                 'for field `drape_beambeam_solar_transmittance_at_normal_incidence`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `drape_beambeam_solar_transmittance_at_normal_incidence`')
            if value > 0.2:
                raise ValueError('value need to be smaller 0.2 '
                                 'for field `drape_beambeam_solar_transmittance_at_normal_incidence`')

        self._data["Drape Beam-Beam Solar Transmittance at Normal Incidence"] = value

    @property
    def front_side_drape_beamdiffuse_solar_transmittance(self):
        """Get front_side_drape_beamdiffuse_solar_transmittance

        Returns:
            float: the value of `front_side_drape_beamdiffuse_solar_transmittance` or None if not set
        """
        return self._data["Front Side Drape Beam-Diffuse Solar Transmittance"]

    @front_side_drape_beamdiffuse_solar_transmittance.setter
    def front_side_drape_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `front_side_drape_beamdiffuse_solar_transmittance`
        The front side beam-diffuse solar transmittance at normal incidence averaged
        over the entire spectrum of solar radiation. Assumed to be the same for front
        and back sides.

        Args:
            value (float): value for IDD Field `front_side_drape_beamdiffuse_solar_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_drape_beamdiffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_drape_beamdiffuse_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_drape_beamdiffuse_solar_transmittance`')

        self._data["Front Side Drape Beam-Diffuse Solar Transmittance"] = value

    @property
    def back_side_drape_beamdiffuse_solar_transmittance(self):
        """Get back_side_drape_beamdiffuse_solar_transmittance

        Returns:
            float: the value of `back_side_drape_beamdiffuse_solar_transmittance` or None if not set
        """
        return self._data["Back Side Drape Beam-Diffuse Solar Transmittance"]

    @back_side_drape_beamdiffuse_solar_transmittance.setter
    def back_side_drape_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `back_side_drape_beamdiffuse_solar_transmittance`
        The back side beam-diffuse solar transmittance at normal incidence averaged
        over the entire spectrum of solar radiation. Assumed to be the same for front
        and back sides.

        Args:
            value (float): value for IDD Field `back_side_drape_beamdiffuse_solar_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_drape_beamdiffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_drape_beamdiffuse_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_drape_beamdiffuse_solar_transmittance`')

        self._data["Back Side Drape Beam-Diffuse Solar Transmittance"] = value

    @property
    def front_side_drape_beamdiffuse_solar_reflectance(self):
        """Get front_side_drape_beamdiffuse_solar_reflectance

        Returns:
            float: the value of `front_side_drape_beamdiffuse_solar_reflectance` or None if not set
        """
        return self._data["Front Side Drape Beam-Diffuse Solar Reflectance"]

    @front_side_drape_beamdiffuse_solar_reflectance.setter
    def front_side_drape_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_drape_beamdiffuse_solar_reflectance`
        The front side beam-diffuse solar reflectance at normal incidence averaged
        over the entire spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `front_side_drape_beamdiffuse_solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_drape_beamdiffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_drape_beamdiffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_drape_beamdiffuse_solar_reflectance`')

        self._data["Front Side Drape Beam-Diffuse Solar Reflectance"] = value

    @property
    def back_side_drape_beamdiffuse_solar_reflectance(self):
        """Get back_side_drape_beamdiffuse_solar_reflectance

        Returns:
            float: the value of `back_side_drape_beamdiffuse_solar_reflectance` or None if not set
        """
        return self._data["Back Side Drape Beam-Diffuse Solar Reflectance"]

    @back_side_drape_beamdiffuse_solar_reflectance.setter
    def back_side_drape_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_drape_beamdiffuse_solar_reflectance`
        The back side beam-diffuse solar reflectance at normal incidence averaged
        over the entire spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `back_side_drape_beamdiffuse_solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_drape_beamdiffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_drape_beamdiffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_drape_beamdiffuse_solar_reflectance`')

        self._data["Back Side Drape Beam-Diffuse Solar Reflectance"] = value

    @property
    def drape_beambeam_visible_transmittance(self):
        """Get drape_beambeam_visible_transmittance

        Returns:
            float: the value of `drape_beambeam_visible_transmittance` or None if not set
        """
        return self._data["Drape Beam-Beam Visible Transmittance"]

    @drape_beambeam_visible_transmittance.setter
    def drape_beambeam_visible_transmittance(self, value=None):
        """  Corresponds to IDD Field `drape_beambeam_visible_transmittance`
        The beam-beam visible transmittance at normal incidence averaged over the
        visible spectrum of solar radiation. Assumed same for front and back sides.

        Args:
            value (float): value for IDD Field `drape_beambeam_visible_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `drape_beambeam_visible_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `drape_beambeam_visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `drape_beambeam_visible_transmittance`')

        self._data["Drape Beam-Beam Visible Transmittance"] = value

    @property
    def drape_beamdiffuse_visible_transmittance(self):
        """Get drape_beamdiffuse_visible_transmittance

        Returns:
            float: the value of `drape_beamdiffuse_visible_transmittance` or None if not set
        """
        return self._data["Drape Beam-Diffuse Visible Transmittance"]

    @drape_beamdiffuse_visible_transmittance.setter
    def drape_beamdiffuse_visible_transmittance(self, value=None):
        """  Corresponds to IDD Field `drape_beamdiffuse_visible_transmittance`
        The beam-diffuse visible transmittance at normal incidence averaged over the
        visible spectrum range of solar radiation. Assumed to be the same for front
        and back sides.

        Args:
            value (float): value for IDD Field `drape_beamdiffuse_visible_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `drape_beamdiffuse_visible_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `drape_beamdiffuse_visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `drape_beamdiffuse_visible_transmittance`')

        self._data["Drape Beam-Diffuse Visible Transmittance"] = value

    @property
    def drape_beamdiffuse_visible_reflectance(self):
        """Get drape_beamdiffuse_visible_reflectance

        Returns:
            float: the value of `drape_beamdiffuse_visible_reflectance` or None if not set
        """
        return self._data["Drape Beam-Diffuse Visible Reflectance"]

    @drape_beamdiffuse_visible_reflectance.setter
    def drape_beamdiffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `drape_beamdiffuse_visible_reflectance`
        The beam-diffuse visible reflectance at normal incidence average over the
        visible spectrum range of solar radiation. Assumed to be the same for front
        and back sides.

        Args:
            value (float): value for IDD Field `drape_beamdiffuse_visible_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `drape_beamdiffuse_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `drape_beamdiffuse_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `drape_beamdiffuse_visible_reflectance`')

        self._data["Drape Beam-Diffuse Visible Reflectance"] = value

    @property
    def drape_material_infrared_transmittance(self):
        """Get drape_material_infrared_transmittance

        Returns:
            float: the value of `drape_material_infrared_transmittance` or None if not set
        """
        return self._data["Drape Material Infrared Transmittance"]

    @drape_material_infrared_transmittance.setter
    def drape_material_infrared_transmittance(self, value=0.05 ):
        """  Corresponds to IDD Field `drape_material_infrared_transmittance`
        Long-wave transmittance of the drape fabric at zero openness fraction.
        Assumed same for front and back sides.

        Args:
            value (float): value for IDD Field `drape_material_infrared_transmittance`
                Unit: dimensionless
                Default value: 0.05
                value >= 0.0
                value < 1.0
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
                                 'for field `drape_material_infrared_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `drape_material_infrared_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `drape_material_infrared_transmittance`')

        self._data["Drape Material Infrared Transmittance"] = value

    @property
    def front_side_drape_material_infrared_emissivity(self):
        """Get front_side_drape_material_infrared_emissivity

        Returns:
            float: the value of `front_side_drape_material_infrared_emissivity` or None if not set
        """
        return self._data["Front Side Drape Material Infrared Emissivity"]

    @front_side_drape_material_infrared_emissivity.setter
    def front_side_drape_material_infrared_emissivity(self, value=0.87 ):
        """  Corresponds to IDD Field `front_side_drape_material_infrared_emissivity`
        Front side long-wave emissivity of the drape fabric at zero shade openness.
        Openness fraction specified above is used to calculate the effective
        emissivity value.

        Args:
            value (float): value for IDD Field `front_side_drape_material_infrared_emissivity`
                Unit: dimensionless
                Default value: 0.87
                value > 0.0
                value < 1.0
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
                                 'for field `front_side_drape_material_infrared_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `front_side_drape_material_infrared_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_drape_material_infrared_emissivity`')

        self._data["Front Side Drape Material Infrared Emissivity"] = value

    @property
    def back_side_drape_material_infrared_emissivity(self):
        """Get back_side_drape_material_infrared_emissivity

        Returns:
            float: the value of `back_side_drape_material_infrared_emissivity` or None if not set
        """
        return self._data["Back Side Drape Material Infrared Emissivity"]

    @back_side_drape_material_infrared_emissivity.setter
    def back_side_drape_material_infrared_emissivity(self, value=0.87 ):
        """  Corresponds to IDD Field `back_side_drape_material_infrared_emissivity`
        Back side long-wave emissivity of the drape fabric at zero shade openness.
        Openness fraction specified above is used to calculate the effective
        emissivity value.

        Args:
            value (float): value for IDD Field `back_side_drape_material_infrared_emissivity`
                Unit: dimensionless
                Default value: 0.87
                value > 0.0
                value < 1.0
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
                                 'for field `back_side_drape_material_infrared_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `back_side_drape_material_infrared_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_drape_material_infrared_emissivity`')

        self._data["Back Side Drape Material Infrared Emissivity"] = value

    @property
    def width_of_pleated_fabric(self):
        """Get width_of_pleated_fabric

        Returns:
            float: the value of `width_of_pleated_fabric` or None if not set
        """
        return self._data["Width of Pleated Fabric"]

    @width_of_pleated_fabric.setter
    def width_of_pleated_fabric(self, value=0.0 ):
        """  Corresponds to IDD Field `width_of_pleated_fabric`
        Width of the pleasted section of the draped fabric. If the drape fabric is
        unpleated or is flat, then the pleated section width is set to zero.

        Args:
            value (float): value for IDD Field `width_of_pleated_fabric`
                Unit: m
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
                                 'for field `width_of_pleated_fabric`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `width_of_pleated_fabric`')

        self._data["Width of Pleated Fabric"] = value

    @property
    def length_of_pleated_fabric(self):
        """Get length_of_pleated_fabric

        Returns:
            float: the value of `length_of_pleated_fabric` or None if not set
        """
        return self._data["Length of Pleated Fabric"]

    @length_of_pleated_fabric.setter
    def length_of_pleated_fabric(self, value=0.0 ):
        """  Corresponds to IDD Field `length_of_pleated_fabric`
        Length of the pleasted section of the draped fabric. If the drape fabric is
        unpleated or is flat, then the pleated section length is set to zero.

        Args:
            value (float): value for IDD Field `length_of_pleated_fabric`
                Unit: m
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
                                 'for field `length_of_pleated_fabric`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `length_of_pleated_fabric`')

        self._data["Length of Pleated Fabric"] = value

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
        out.append(self._to_str(self.drape_beambeam_solar_transmittance_at_normal_incidence))
        out.append(self._to_str(self.front_side_drape_beamdiffuse_solar_transmittance))
        out.append(self._to_str(self.back_side_drape_beamdiffuse_solar_transmittance))
        out.append(self._to_str(self.front_side_drape_beamdiffuse_solar_reflectance))
        out.append(self._to_str(self.back_side_drape_beamdiffuse_solar_reflectance))
        out.append(self._to_str(self.drape_beambeam_visible_transmittance))
        out.append(self._to_str(self.drape_beamdiffuse_visible_transmittance))
        out.append(self._to_str(self.drape_beamdiffuse_visible_reflectance))
        out.append(self._to_str(self.drape_material_infrared_transmittance))
        out.append(self._to_str(self.front_side_drape_material_infrared_emissivity))
        out.append(self._to_str(self.back_side_drape_material_infrared_emissivity))
        out.append(self._to_str(self.width_of_pleated_fabric))
        out.append(self._to_str(self.length_of_pleated_fabric))
        return ",".join(out)

class WindowMaterialBlindEquivalentLayer(object):
    """ Corresponds to IDD object `WindowMaterial:Blind:EquivalentLayer`
        Window equivalent layer blind slat optical and thermal properties.
        The model assumes that slats are thin and flat, applies correction
        imperical correlation to accout for curvature effect. Slats are
        assumed to transmit and reflect diffusely.
    """
    internal_name = "WindowMaterial:Blind:EquivalentLayer"
    field_count = 24

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Blind:EquivalentLayer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Slat Orientation"] = None
        self._data["Slat Width"] = None
        self._data["Slat Separation"] = None
        self._data["Slat Crown"] = None
        self._data["Slat Angle"] = None
        self._data["Front Side Slat Beam-Diffuse Solar Transmittance"] = None
        self._data["Back Side Slat Beam-Diffuse Solar Transmittance"] = None
        self._data["Front Side Slat Beam-Diffuse Solar Reflectance"] = None
        self._data["Back Side Slat Beam-Diffuse Solar Reflectance"] = None
        self._data["Front Side Slat Beam-Diffuse Visible Transmittance"] = None
        self._data["Back Side Slat Beam-Diffuse Visible Transmittance"] = None
        self._data["Front Side Slat Beam-Diffuse Visible Reflectance"] = None
        self._data["Back Side Slat Beam-Diffuse Visible Reflectance"] = None
        self._data["Slat Diffuse-Diffuse Solar Transmittance"] = None
        self._data["Front Side Slat Diffuse-Diffuse Solar Reflectance"] = None
        self._data["Back Side Slat Diffuse-Diffuse Solar Reflectance"] = None
        self._data["Slat Diffuse-Diffuse Visible Transmittance"] = None
        self._data["Front Side Slat Diffuse-Diffuse Visible Reflectance"] = None
        self._data["Back Side Slat Diffuse-Diffuse Visible Reflectance"] = None
        self._data["Slat Infrared Transmittance"] = None
        self._data["Front Side Slat Infrared Emissivity"] = None
        self._data["Back Side Slat Infrared Emissivity"] = None
        self._data["Slat Angle Control"] = None

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
            self.slat_orientation = None
        else:
            self.slat_orientation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_width = None
        else:
            self.slat_width = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_separation = None
        else:
            self.slat_separation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_crown = None
        else:
            self.slat_crown = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_angle = None
        else:
            self.slat_angle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_beamdiffuse_solar_transmittance = None
        else:
            self.front_side_slat_beamdiffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_beamdiffuse_solar_transmittance = None
        else:
            self.back_side_slat_beamdiffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_beamdiffuse_solar_reflectance = None
        else:
            self.front_side_slat_beamdiffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_beamdiffuse_solar_reflectance = None
        else:
            self.back_side_slat_beamdiffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_beamdiffuse_visible_transmittance = None
        else:
            self.front_side_slat_beamdiffuse_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_beamdiffuse_visible_transmittance = None
        else:
            self.back_side_slat_beamdiffuse_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_beamdiffuse_visible_reflectance = None
        else:
            self.front_side_slat_beamdiffuse_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_beamdiffuse_visible_reflectance = None
        else:
            self.back_side_slat_beamdiffuse_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_diffusediffuse_solar_transmittance = None
        else:
            self.slat_diffusediffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_diffusediffuse_solar_reflectance = None
        else:
            self.front_side_slat_diffusediffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_diffusediffuse_solar_reflectance = None
        else:
            self.back_side_slat_diffusediffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_diffusediffuse_visible_transmittance = None
        else:
            self.slat_diffusediffuse_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_diffusediffuse_visible_reflectance = None
        else:
            self.front_side_slat_diffusediffuse_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_diffusediffuse_visible_reflectance = None
        else:
            self.back_side_slat_diffusediffuse_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_infrared_transmittance = None
        else:
            self.slat_infrared_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_slat_infrared_emissivity = None
        else:
            self.front_side_slat_infrared_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_slat_infrared_emissivity = None
        else:
            self.back_side_slat_infrared_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_angle_control = None
        else:
            self.slat_angle_control = vals[i]
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
    def slat_orientation(self):
        """Get slat_orientation

        Returns:
            str: the value of `slat_orientation` or None if not set
        """
        return self._data["Slat Orientation"]

    @slat_orientation.setter
    def slat_orientation(self, value="Horizontal"):
        """  Corresponds to IDD Field `slat_orientation`

        Args:
            value (str): value for IDD Field `slat_orientation`
                Accepted values are:
                      - Horizontal
                      - Vertical
                Default value: Horizontal
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
                                 'for field `slat_orientation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `slat_orientation`')
            vals = set()
            vals.add("Horizontal")
            vals.add("Vertical")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `slat_orientation`'.format(value))

        self._data["Slat Orientation"] = value

    @property
    def slat_width(self):
        """Get slat_width

        Returns:
            float: the value of `slat_width` or None if not set
        """
        return self._data["Slat Width"]

    @slat_width.setter
    def slat_width(self, value=None):
        """  Corresponds to IDD Field `slat_width`

        Args:
            value (float): value for IDD Field `slat_width`
                Unit: m
                value > 0.0
                value <= 0.025
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
                                 'for field `slat_width`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `slat_width`')
            if value > 0.025:
                raise ValueError('value need to be smaller 0.025 '
                                 'for field `slat_width`')

        self._data["Slat Width"] = value

    @property
    def slat_separation(self):
        """Get slat_separation

        Returns:
            float: the value of `slat_separation` or None if not set
        """
        return self._data["Slat Separation"]

    @slat_separation.setter
    def slat_separation(self, value=None):
        """  Corresponds to IDD Field `slat_separation`
        Distance between adjacent slat faces

        Args:
            value (float): value for IDD Field `slat_separation`
                Unit: m
                value > 0.0
                value <= 0.025
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
                                 'for field `slat_separation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `slat_separation`')
            if value > 0.025:
                raise ValueError('value need to be smaller 0.025 '
                                 'for field `slat_separation`')

        self._data["Slat Separation"] = value

    @property
    def slat_crown(self):
        """Get slat_crown

        Returns:
            float: the value of `slat_crown` or None if not set
        """
        return self._data["Slat Crown"]

    @slat_crown.setter
    def slat_crown(self, value=0.0015 ):
        """  Corresponds to IDD Field `slat_crown`
        Perpendicular length between the cord and the curve.
        Slat is assumed to be rectangular in cross section
        and flat. Crown=0.0625xSlat width

        Args:
            value (float): value for IDD Field `slat_crown`
                Unit: m
                Default value: 0.0015
                value >= 0.0
                value <= 0.00156
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
                                 'for field `slat_crown`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_crown`')
            if value > 0.00156:
                raise ValueError('value need to be smaller 0.00156 '
                                 'for field `slat_crown`')

        self._data["Slat Crown"] = value

    @property
    def slat_angle(self):
        """Get slat_angle

        Returns:
            float: the value of `slat_angle` or None if not set
        """
        return self._data["Slat Angle"]

    @slat_angle.setter
    def slat_angle(self, value=45.0 ):
        """  Corresponds to IDD Field `slat_angle`

        Args:
            value (float): value for IDD Field `slat_angle`
                Unit: deg
                Default value: 45.0
                value >= 0.0
                value <= 180.0
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
                                 'for field `slat_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `slat_angle`')

        self._data["Slat Angle"] = value

    @property
    def front_side_slat_beamdiffuse_solar_transmittance(self):
        """Get front_side_slat_beamdiffuse_solar_transmittance

        Returns:
            float: the value of `front_side_slat_beamdiffuse_solar_transmittance` or None if not set
        """
        return self._data["Front Side Slat Beam-Diffuse Solar Transmittance"]

    @front_side_slat_beamdiffuse_solar_transmittance.setter
    def front_side_slat_beamdiffuse_solar_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `front_side_slat_beamdiffuse_solar_transmittance`
        The front side beam-diffuse solar transmittance of the slat at normal
        incidence averaged over the entire spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `front_side_slat_beamdiffuse_solar_transmittance`
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_beamdiffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_beamdiffuse_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_beamdiffuse_solar_transmittance`')

        self._data["Front Side Slat Beam-Diffuse Solar Transmittance"] = value

    @property
    def back_side_slat_beamdiffuse_solar_transmittance(self):
        """Get back_side_slat_beamdiffuse_solar_transmittance

        Returns:
            float: the value of `back_side_slat_beamdiffuse_solar_transmittance` or None if not set
        """
        return self._data["Back Side Slat Beam-Diffuse Solar Transmittance"]

    @back_side_slat_beamdiffuse_solar_transmittance.setter
    def back_side_slat_beamdiffuse_solar_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `back_side_slat_beamdiffuse_solar_transmittance`
        The back side beam-diffuse solar transmittance of the slat at normal
        incidence averaged over the entire spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `back_side_slat_beamdiffuse_solar_transmittance`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_beamdiffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_beamdiffuse_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_beamdiffuse_solar_transmittance`')

        self._data["Back Side Slat Beam-Diffuse Solar Transmittance"] = value

    @property
    def front_side_slat_beamdiffuse_solar_reflectance(self):
        """Get front_side_slat_beamdiffuse_solar_reflectance

        Returns:
            float: the value of `front_side_slat_beamdiffuse_solar_reflectance` or None if not set
        """
        return self._data["Front Side Slat Beam-Diffuse Solar Reflectance"]

    @front_side_slat_beamdiffuse_solar_reflectance.setter
    def front_side_slat_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_slat_beamdiffuse_solar_reflectance`
        The front side beam-diffuse solar reflectance of the slat at normal
        incidence averaged over the entire spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `front_side_slat_beamdiffuse_solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_beamdiffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_beamdiffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_beamdiffuse_solar_reflectance`')

        self._data["Front Side Slat Beam-Diffuse Solar Reflectance"] = value

    @property
    def back_side_slat_beamdiffuse_solar_reflectance(self):
        """Get back_side_slat_beamdiffuse_solar_reflectance

        Returns:
            float: the value of `back_side_slat_beamdiffuse_solar_reflectance` or None if not set
        """
        return self._data["Back Side Slat Beam-Diffuse Solar Reflectance"]

    @back_side_slat_beamdiffuse_solar_reflectance.setter
    def back_side_slat_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_slat_beamdiffuse_solar_reflectance`
        The back side beam-diffuse solar reflectance of the slat at normal
        incidence averaged over the entire spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `back_side_slat_beamdiffuse_solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_beamdiffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_beamdiffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_beamdiffuse_solar_reflectance`')

        self._data["Back Side Slat Beam-Diffuse Solar Reflectance"] = value

    @property
    def front_side_slat_beamdiffuse_visible_transmittance(self):
        """Get front_side_slat_beamdiffuse_visible_transmittance

        Returns:
            float: the value of `front_side_slat_beamdiffuse_visible_transmittance` or None if not set
        """
        return self._data["Front Side Slat Beam-Diffuse Visible Transmittance"]

    @front_side_slat_beamdiffuse_visible_transmittance.setter
    def front_side_slat_beamdiffuse_visible_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `front_side_slat_beamdiffuse_visible_transmittance`
        The front side beam-diffuse visible transmittance of the slat
        at normal incidence averaged over the visible spectrum range
        of solar radiation.

        Args:
            value (float): value for IDD Field `front_side_slat_beamdiffuse_visible_transmittance`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_beamdiffuse_visible_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_beamdiffuse_visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_beamdiffuse_visible_transmittance`')

        self._data["Front Side Slat Beam-Diffuse Visible Transmittance"] = value

    @property
    def back_side_slat_beamdiffuse_visible_transmittance(self):
        """Get back_side_slat_beamdiffuse_visible_transmittance

        Returns:
            float: the value of `back_side_slat_beamdiffuse_visible_transmittance` or None if not set
        """
        return self._data["Back Side Slat Beam-Diffuse Visible Transmittance"]

    @back_side_slat_beamdiffuse_visible_transmittance.setter
    def back_side_slat_beamdiffuse_visible_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `back_side_slat_beamdiffuse_visible_transmittance`
        The back side beam-diffuse visible transmittance of the slat
        at normal incidence averaged over the visible spectrum range
        of solar radiation.

        Args:
            value (float): value for IDD Field `back_side_slat_beamdiffuse_visible_transmittance`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_beamdiffuse_visible_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_beamdiffuse_visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_beamdiffuse_visible_transmittance`')

        self._data["Back Side Slat Beam-Diffuse Visible Transmittance"] = value

    @property
    def front_side_slat_beamdiffuse_visible_reflectance(self):
        """Get front_side_slat_beamdiffuse_visible_reflectance

        Returns:
            float: the value of `front_side_slat_beamdiffuse_visible_reflectance` or None if not set
        """
        return self._data["Front Side Slat Beam-Diffuse Visible Reflectance"]

    @front_side_slat_beamdiffuse_visible_reflectance.setter
    def front_side_slat_beamdiffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_slat_beamdiffuse_visible_reflectance`
        The front side beam-diffuse visible reflectance of the slat
        at normal incidence averaged over the visible spectrum range
        of solar radiation.

        Args:
            value (float): value for IDD Field `front_side_slat_beamdiffuse_visible_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_beamdiffuse_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_beamdiffuse_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_beamdiffuse_visible_reflectance`')

        self._data["Front Side Slat Beam-Diffuse Visible Reflectance"] = value

    @property
    def back_side_slat_beamdiffuse_visible_reflectance(self):
        """Get back_side_slat_beamdiffuse_visible_reflectance

        Returns:
            float: the value of `back_side_slat_beamdiffuse_visible_reflectance` or None if not set
        """
        return self._data["Back Side Slat Beam-Diffuse Visible Reflectance"]

    @back_side_slat_beamdiffuse_visible_reflectance.setter
    def back_side_slat_beamdiffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_slat_beamdiffuse_visible_reflectance`
        The back side beam-diffuse visible reflectance of the slat
        at normal incidence averaged over the visible spectrum range
        of solar radiation.

        Args:
            value (float): value for IDD Field `back_side_slat_beamdiffuse_visible_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_beamdiffuse_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_beamdiffuse_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_beamdiffuse_visible_reflectance`')

        self._data["Back Side Slat Beam-Diffuse Visible Reflectance"] = value

    @property
    def slat_diffusediffuse_solar_transmittance(self):
        """Get slat_diffusediffuse_solar_transmittance

        Returns:
            float: the value of `slat_diffusediffuse_solar_transmittance` or None if not set
        """
        return self._data["Slat Diffuse-Diffuse Solar Transmittance"]

    @slat_diffusediffuse_solar_transmittance.setter
    def slat_diffusediffuse_solar_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `slat_diffusediffuse_solar_transmittance`
        The beam-diffuse solar transmittance of the slat averaged
        over the entire solar spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `slat_diffusediffuse_solar_transmittance`
                Unit: dimensionless
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `slat_diffusediffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_diffusediffuse_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `slat_diffusediffuse_solar_transmittance`')

        self._data["Slat Diffuse-Diffuse Solar Transmittance"] = value

    @property
    def front_side_slat_diffusediffuse_solar_reflectance(self):
        """Get front_side_slat_diffusediffuse_solar_reflectance

        Returns:
            float: the value of `front_side_slat_diffusediffuse_solar_reflectance` or None if not set
        """
        return self._data["Front Side Slat Diffuse-Diffuse Solar Reflectance"]

    @front_side_slat_diffusediffuse_solar_reflectance.setter
    def front_side_slat_diffusediffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_slat_diffusediffuse_solar_reflectance`
        The front side beam-diffuse solar reflectance of the slat
        averaged over the entire solar spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `front_side_slat_diffusediffuse_solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_diffusediffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_diffusediffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_diffusediffuse_solar_reflectance`')

        self._data["Front Side Slat Diffuse-Diffuse Solar Reflectance"] = value

    @property
    def back_side_slat_diffusediffuse_solar_reflectance(self):
        """Get back_side_slat_diffusediffuse_solar_reflectance

        Returns:
            float: the value of `back_side_slat_diffusediffuse_solar_reflectance` or None if not set
        """
        return self._data["Back Side Slat Diffuse-Diffuse Solar Reflectance"]

    @back_side_slat_diffusediffuse_solar_reflectance.setter
    def back_side_slat_diffusediffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_slat_diffusediffuse_solar_reflectance`
        The back side beam-diffuse solar reflectance of the slat
        averaged over the entire solar spectrum of solar radiation.

        Args:
            value (float): value for IDD Field `back_side_slat_diffusediffuse_solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_diffusediffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_diffusediffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_diffusediffuse_solar_reflectance`')

        self._data["Back Side Slat Diffuse-Diffuse Solar Reflectance"] = value

    @property
    def slat_diffusediffuse_visible_transmittance(self):
        """Get slat_diffusediffuse_visible_transmittance

        Returns:
            float: the value of `slat_diffusediffuse_visible_transmittance` or None if not set
        """
        return self._data["Slat Diffuse-Diffuse Visible Transmittance"]

    @slat_diffusediffuse_visible_transmittance.setter
    def slat_diffusediffuse_visible_transmittance(self, value=None):
        """  Corresponds to IDD Field `slat_diffusediffuse_visible_transmittance`
        The beam-diffuse visible transmittance of the slat averaged
        over the visible spectrum range of solar radiation.

        Args:
            value (float): value for IDD Field `slat_diffusediffuse_visible_transmittance`
                value >= 0.0
                value < 1.0
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
                                 'for field `slat_diffusediffuse_visible_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_diffusediffuse_visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `slat_diffusediffuse_visible_transmittance`')

        self._data["Slat Diffuse-Diffuse Visible Transmittance"] = value

    @property
    def front_side_slat_diffusediffuse_visible_reflectance(self):
        """Get front_side_slat_diffusediffuse_visible_reflectance

        Returns:
            float: the value of `front_side_slat_diffusediffuse_visible_reflectance` or None if not set
        """
        return self._data["Front Side Slat Diffuse-Diffuse Visible Reflectance"]

    @front_side_slat_diffusediffuse_visible_reflectance.setter
    def front_side_slat_diffusediffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_slat_diffusediffuse_visible_reflectance`
        The front side beam-diffuse visible reflectance of the slat
        averaged over the visible spectrum range of solar radiation.

        Args:
            value (float): value for IDD Field `front_side_slat_diffusediffuse_visible_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_diffusediffuse_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_diffusediffuse_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_diffusediffuse_visible_reflectance`')

        self._data["Front Side Slat Diffuse-Diffuse Visible Reflectance"] = value

    @property
    def back_side_slat_diffusediffuse_visible_reflectance(self):
        """Get back_side_slat_diffusediffuse_visible_reflectance

        Returns:
            float: the value of `back_side_slat_diffusediffuse_visible_reflectance` or None if not set
        """
        return self._data["Back Side Slat Diffuse-Diffuse Visible Reflectance"]

    @back_side_slat_diffusediffuse_visible_reflectance.setter
    def back_side_slat_diffusediffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_slat_diffusediffuse_visible_reflectance`
        The back side beam-diffuse visible reflectance of the slat
        averaged over the visible spectrum range of solar radiation.

        Args:
            value (float): value for IDD Field `back_side_slat_diffusediffuse_visible_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_diffusediffuse_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_diffusediffuse_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_diffusediffuse_visible_reflectance`')

        self._data["Back Side Slat Diffuse-Diffuse Visible Reflectance"] = value

    @property
    def slat_infrared_transmittance(self):
        """Get slat_infrared_transmittance

        Returns:
            float: the value of `slat_infrared_transmittance` or None if not set
        """
        return self._data["Slat Infrared Transmittance"]

    @slat_infrared_transmittance.setter
    def slat_infrared_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `slat_infrared_transmittance`
        Long-wave hemispherical transmittance of the slat material.
        Assumed to be the same for both sides of the slat.

        Args:
            value (float): value for IDD Field `slat_infrared_transmittance`
                Default value: 0.0
                value >= 0.0
                value < 1.0
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
                                 'for field `slat_infrared_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slat_infrared_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `slat_infrared_transmittance`')

        self._data["Slat Infrared Transmittance"] = value

    @property
    def front_side_slat_infrared_emissivity(self):
        """Get front_side_slat_infrared_emissivity

        Returns:
            float: the value of `front_side_slat_infrared_emissivity` or None if not set
        """
        return self._data["Front Side Slat Infrared Emissivity"]

    @front_side_slat_infrared_emissivity.setter
    def front_side_slat_infrared_emissivity(self, value=0.9 ):
        """  Corresponds to IDD Field `front_side_slat_infrared_emissivity`
        Front side long-wave hemispherical emissivity of the slat material.

        Args:
            value (float): value for IDD Field `front_side_slat_infrared_emissivity`
                Unit: dimensionless
                Default value: 0.9
                value >= 0.0
                value < 1.0
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
                                 'for field `front_side_slat_infrared_emissivity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_slat_infrared_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_slat_infrared_emissivity`')

        self._data["Front Side Slat Infrared Emissivity"] = value

    @property
    def back_side_slat_infrared_emissivity(self):
        """Get back_side_slat_infrared_emissivity

        Returns:
            float: the value of `back_side_slat_infrared_emissivity` or None if not set
        """
        return self._data["Back Side Slat Infrared Emissivity"]

    @back_side_slat_infrared_emissivity.setter
    def back_side_slat_infrared_emissivity(self, value=0.9 ):
        """  Corresponds to IDD Field `back_side_slat_infrared_emissivity`
        Back side long-wave hemispherical emissivity of the slat material.

        Args:
            value (float): value for IDD Field `back_side_slat_infrared_emissivity`
                Unit: dimensionless
                Default value: 0.9
                value >= 0.0
                value < 1.0
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
                                 'for field `back_side_slat_infrared_emissivity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_slat_infrared_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_slat_infrared_emissivity`')

        self._data["Back Side Slat Infrared Emissivity"] = value

    @property
    def slat_angle_control(self):
        """Get slat_angle_control

        Returns:
            str: the value of `slat_angle_control` or None if not set
        """
        return self._data["Slat Angle Control"]

    @slat_angle_control.setter
    def slat_angle_control(self, value="FixedSlatAngle"):
        """  Corresponds to IDD Field `slat_angle_control`
        Used only if slat angle control is deired to either maximize solar
        gain (MaximizeSolar), maximize visibiity while eliminating beam solar
        radiation (BlockBeamSolar), or fixed slate angle (FixedSlatAngle).
        If FixedSlatAngle is selected, the slat angle entered above is used.

        Args:
            value (str): value for IDD Field `slat_angle_control`
                Accepted values are:
                      - FixedSlatAngle
                      - MaximizeSolar
                      - BlockBeamSolar
                Default value: FixedSlatAngle
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
                                 'for field `slat_angle_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `slat_angle_control`')
            vals = set()
            vals.add("FixedSlatAngle")
            vals.add("MaximizeSolar")
            vals.add("BlockBeamSolar")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `slat_angle_control`'.format(value))

        self._data["Slat Angle Control"] = value

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
        out.append(self._to_str(self.slat_orientation))
        out.append(self._to_str(self.slat_width))
        out.append(self._to_str(self.slat_separation))
        out.append(self._to_str(self.slat_crown))
        out.append(self._to_str(self.slat_angle))
        out.append(self._to_str(self.front_side_slat_beamdiffuse_solar_transmittance))
        out.append(self._to_str(self.back_side_slat_beamdiffuse_solar_transmittance))
        out.append(self._to_str(self.front_side_slat_beamdiffuse_solar_reflectance))
        out.append(self._to_str(self.back_side_slat_beamdiffuse_solar_reflectance))
        out.append(self._to_str(self.front_side_slat_beamdiffuse_visible_transmittance))
        out.append(self._to_str(self.back_side_slat_beamdiffuse_visible_transmittance))
        out.append(self._to_str(self.front_side_slat_beamdiffuse_visible_reflectance))
        out.append(self._to_str(self.back_side_slat_beamdiffuse_visible_reflectance))
        out.append(self._to_str(self.slat_diffusediffuse_solar_transmittance))
        out.append(self._to_str(self.front_side_slat_diffusediffuse_solar_reflectance))
        out.append(self._to_str(self.back_side_slat_diffusediffuse_solar_reflectance))
        out.append(self._to_str(self.slat_diffusediffuse_visible_transmittance))
        out.append(self._to_str(self.front_side_slat_diffusediffuse_visible_reflectance))
        out.append(self._to_str(self.back_side_slat_diffusediffuse_visible_reflectance))
        out.append(self._to_str(self.slat_infrared_transmittance))
        out.append(self._to_str(self.front_side_slat_infrared_emissivity))
        out.append(self._to_str(self.back_side_slat_infrared_emissivity))
        out.append(self._to_str(self.slat_angle_control))
        return ",".join(out)

class WindowMaterialScreenEquivalentLayer(object):
    """ Corresponds to IDD object `WindowMaterial:Screen:EquivalentLayer`
        Equivalent layer window screen physical properties. Can only be
        located on the exterior side of a window construction.
    """
    internal_name = "WindowMaterial:Screen:EquivalentLayer"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Screen:EquivalentLayer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Screen Beam-Beam Solar Transmittance"] = None
        self._data["Screen Beam-Diffuse Solar Transmittance"] = None
        self._data["Screen Beam-Diffuse Solar Reflectance"] = None
        self._data["Screen Beam-Beam Visible Transmittance"] = None
        self._data["Screen Beam-Diffuse Visible Transmittance"] = None
        self._data["Screen Beam-Diffuse Visible Reflectance"] = None
        self._data["Screen Infrared Transmittance"] = None
        self._data["Screen Infrared Emissivity"] = None
        self._data["Screen Wire Spacing"] = None
        self._data["Screen Wire Diameter"] = None

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
            self.screen_beambeam_solar_transmittance = None
        else:
            self.screen_beambeam_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_beamdiffuse_solar_transmittance = None
        else:
            self.screen_beamdiffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_beamdiffuse_solar_reflectance = None
        else:
            self.screen_beamdiffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_beambeam_visible_transmittance = None
        else:
            self.screen_beambeam_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_beamdiffuse_visible_transmittance = None
        else:
            self.screen_beamdiffuse_visible_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_beamdiffuse_visible_reflectance = None
        else:
            self.screen_beamdiffuse_visible_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_infrared_transmittance = None
        else:
            self.screen_infrared_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_infrared_emissivity = None
        else:
            self.screen_infrared_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_wire_spacing = None
        else:
            self.screen_wire_spacing = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.screen_wire_diameter = None
        else:
            self.screen_wire_diameter = vals[i]
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
        Enter a unique name for this window screen material.

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
    def screen_beambeam_solar_transmittance(self):
        """Get screen_beambeam_solar_transmittance

        Returns:
            float: the value of `screen_beambeam_solar_transmittance` or None if not set
        """
        return self._data["Screen Beam-Beam Solar Transmittance"]

    @screen_beambeam_solar_transmittance.setter
    def screen_beambeam_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `screen_beambeam_solar_transmittance`
        The beam-beam transmittance of the screen material at normal incidence.
        This input field is the same as the material oppenness area fraction
        and can be autocalculated from the wire spacing and wire and diameter.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `screen_beambeam_solar_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `screen_beambeam_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `screen_beambeam_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `screen_beambeam_solar_transmittance`')

        self._data["Screen Beam-Beam Solar Transmittance"] = value

    @property
    def screen_beamdiffuse_solar_transmittance(self):
        """Get screen_beamdiffuse_solar_transmittance

        Returns:
            float: the value of `screen_beamdiffuse_solar_transmittance` or None if not set
        """
        return self._data["Screen Beam-Diffuse Solar Transmittance"]

    @screen_beamdiffuse_solar_transmittance.setter
    def screen_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `screen_beamdiffuse_solar_transmittance`
        The beam-diffuse solar transmittance of the screen material at normal
        incidence averaged over the entire spectrum of solar radiation.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `screen_beamdiffuse_solar_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `screen_beamdiffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `screen_beamdiffuse_solar_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `screen_beamdiffuse_solar_transmittance`')

        self._data["Screen Beam-Diffuse Solar Transmittance"] = value

    @property
    def screen_beamdiffuse_solar_reflectance(self):
        """Get screen_beamdiffuse_solar_reflectance

        Returns:
            float: the value of `screen_beamdiffuse_solar_reflectance` or None if not set
        """
        return self._data["Screen Beam-Diffuse Solar Reflectance"]

    @screen_beamdiffuse_solar_reflectance.setter
    def screen_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `screen_beamdiffuse_solar_reflectance`
        The beam-diffuse solar reflectance of the screen material at normal
        incidence averaged over the entire spectrum of solar radiation.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `screen_beamdiffuse_solar_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `screen_beamdiffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `screen_beamdiffuse_solar_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `screen_beamdiffuse_solar_reflectance`')

        self._data["Screen Beam-Diffuse Solar Reflectance"] = value

    @property
    def screen_beambeam_visible_transmittance(self):
        """Get screen_beambeam_visible_transmittance

        Returns:
            float: the value of `screen_beambeam_visible_transmittance` or None if not set
        """
        return self._data["Screen Beam-Beam Visible Transmittance"]

    @screen_beambeam_visible_transmittance.setter
    def screen_beambeam_visible_transmittance(self, value=None):
        """  Corresponds to IDD Field `screen_beambeam_visible_transmittance`
        The beam-beam visible transmittance of the screen material at normal
        incidence averaged over the visible spectrum range of solar radiation.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `screen_beambeam_visible_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `screen_beambeam_visible_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `screen_beambeam_visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `screen_beambeam_visible_transmittance`')

        self._data["Screen Beam-Beam Visible Transmittance"] = value

    @property
    def screen_beamdiffuse_visible_transmittance(self):
        """Get screen_beamdiffuse_visible_transmittance

        Returns:
            float: the value of `screen_beamdiffuse_visible_transmittance` or None if not set
        """
        return self._data["Screen Beam-Diffuse Visible Transmittance"]

    @screen_beamdiffuse_visible_transmittance.setter
    def screen_beamdiffuse_visible_transmittance(self, value=None):
        """  Corresponds to IDD Field `screen_beamdiffuse_visible_transmittance`
        The beam-diffuse visible transmittance of the screen material at normal
        incidence averaged over the visible spectrum range of solar radiation.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `screen_beamdiffuse_visible_transmittance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `screen_beamdiffuse_visible_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `screen_beamdiffuse_visible_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `screen_beamdiffuse_visible_transmittance`')

        self._data["Screen Beam-Diffuse Visible Transmittance"] = value

    @property
    def screen_beamdiffuse_visible_reflectance(self):
        """Get screen_beamdiffuse_visible_reflectance

        Returns:
            float: the value of `screen_beamdiffuse_visible_reflectance` or None if not set
        """
        return self._data["Screen Beam-Diffuse Visible Reflectance"]

    @screen_beamdiffuse_visible_reflectance.setter
    def screen_beamdiffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD Field `screen_beamdiffuse_visible_reflectance`
        Beam-diffuse visible reflectance of the screen material at normal
        incidence averaged over the visible spectrum range of solar radiation.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `screen_beamdiffuse_visible_reflectance`
                Unit: dimensionless
                value >= 0.0
                value < 1.0
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
                                 'for field `screen_beamdiffuse_visible_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `screen_beamdiffuse_visible_reflectance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `screen_beamdiffuse_visible_reflectance`')

        self._data["Screen Beam-Diffuse Visible Reflectance"] = value

    @property
    def screen_infrared_transmittance(self):
        """Get screen_infrared_transmittance

        Returns:
            float: the value of `screen_infrared_transmittance` or None if not set
        """
        return self._data["Screen Infrared Transmittance"]

    @screen_infrared_transmittance.setter
    def screen_infrared_transmittance(self, value=0.02 ):
        """  Corresponds to IDD Field `screen_infrared_transmittance`
        The long-wave hemispherical transmittance of the screen material.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `screen_infrared_transmittance`
                Unit: dimensionless
                Default value: 0.02
                value >= 0.0
                value < 1.0
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
                                 'for field `screen_infrared_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `screen_infrared_transmittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `screen_infrared_transmittance`')

        self._data["Screen Infrared Transmittance"] = value

    @property
    def screen_infrared_emissivity(self):
        """Get screen_infrared_emissivity

        Returns:
            float: the value of `screen_infrared_emissivity` or None if not set
        """
        return self._data["Screen Infrared Emissivity"]

    @screen_infrared_emissivity.setter
    def screen_infrared_emissivity(self, value=0.93 ):
        """  Corresponds to IDD Field `screen_infrared_emissivity`
        The long-wave hemispherical emissivity of the screen material.
        Assumed to be the same for both sides of the screen.

        Args:
            value (float): value for IDD Field `screen_infrared_emissivity`
                Unit: dimensionless
                Default value: 0.93
                value > 0.0
                value < 1.0
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
                                 'for field `screen_infrared_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `screen_infrared_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `screen_infrared_emissivity`')

        self._data["Screen Infrared Emissivity"] = value

    @property
    def screen_wire_spacing(self):
        """Get screen_wire_spacing

        Returns:
            float: the value of `screen_wire_spacing` or None if not set
        """
        return self._data["Screen Wire Spacing"]

    @screen_wire_spacing.setter
    def screen_wire_spacing(self, value=0.025 ):
        """  Corresponds to IDD Field `screen_wire_spacing`
        Spacing assumed to be the same in both directions.

        Args:
            value (float): value for IDD Field `screen_wire_spacing`
                Unit: m
                Default value: 0.025
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
                                 'for field `screen_wire_spacing`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `screen_wire_spacing`')

        self._data["Screen Wire Spacing"] = value

    @property
    def screen_wire_diameter(self):
        """Get screen_wire_diameter

        Returns:
            float: the value of `screen_wire_diameter` or None if not set
        """
        return self._data["Screen Wire Diameter"]

    @screen_wire_diameter.setter
    def screen_wire_diameter(self, value=0.005 ):
        """  Corresponds to IDD Field `screen_wire_diameter`
        Diameter assumed to be the same in both directions.

        Args:
            value (float): value for IDD Field `screen_wire_diameter`
                Unit: m
                Default value: 0.005
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
                                 'for field `screen_wire_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `screen_wire_diameter`')

        self._data["Screen Wire Diameter"] = value

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
        out.append(self._to_str(self.screen_beambeam_solar_transmittance))
        out.append(self._to_str(self.screen_beamdiffuse_solar_transmittance))
        out.append(self._to_str(self.screen_beamdiffuse_solar_reflectance))
        out.append(self._to_str(self.screen_beambeam_visible_transmittance))
        out.append(self._to_str(self.screen_beamdiffuse_visible_transmittance))
        out.append(self._to_str(self.screen_beamdiffuse_visible_reflectance))
        out.append(self._to_str(self.screen_infrared_transmittance))
        out.append(self._to_str(self.screen_infrared_emissivity))
        out.append(self._to_str(self.screen_wire_spacing))
        out.append(self._to_str(self.screen_wire_diameter))
        return ",".join(out)

class WindowMaterialGlazingEquivalentLayer(object):
    """ Corresponds to IDD object `WindowMaterial:Glazing:EquivalentLayer`
        Glass material properties for Windows or Glass Doors
        Transmittance/Reflectance input method.
    """
    internal_name = "WindowMaterial:Glazing:EquivalentLayer"
    field_count = 28

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Glazing:EquivalentLayer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Optical Data Type"] = None
        self._data["Window Glass Spectral Data Set Name"] = None
        self._data["Front Side Beam-Beam Solar Transmittance"] = None
        self._data["Back Side Beam-Beam Solar Transmittance"] = None
        self._data["Front Side Beam-Beam Solar Reflectance"] = None
        self._data["Back Side Beam-Beam Solar Reflectance"] = None
        self._data["Front Side Beam-Beam Visible Solar Transmittance"] = None
        self._data["Back Side Beam-Beam Visible Solar Transmittance"] = None
        self._data["Front Side Beam-Beam Visible Solar Reflectance"] = None
        self._data["Back Side Beam-Beam Visible Solar Reflectance"] = None
        self._data["Front Side Beam-Diffuse Solar Transmittance"] = None
        self._data["Back Side Beam-Diffuse Solar Transmittance"] = None
        self._data["Front Side Beam-Diffuse Solar Reflectance"] = None
        self._data["Back Side Beam-Diffuse Solar Reflectance"] = None
        self._data["Front Side Beam-Diffuse Visible Solar Transmittance"] = None
        self._data["Back Side Beam-Diffuse Visible Solar Transmittance"] = None
        self._data["Front Side Beam-Diffuse Visible Solar Reflectance"] = None
        self._data["Back Side Beam-Diffuse Visible Solar Reflectance"] = None
        self._data["Diffuse-Diffuse Solar Transmittance"] = None
        self._data["Front Side Diffuse-Diffuse Solar Reflectance"] = None
        self._data["Back Side Diffuse-Diffuse Solar Reflectance"] = None
        self._data["Diffuse-Diffuse Visible Solar Transmittance"] = None
        self._data["Front Side Diffuse-Diffuse Visible Solar Reflectance"] = None
        self._data["Back Side Diffuse-Diffuse Visible Solar Reflectance"] = None
        self._data["Infrared Transmittance (applies to front and back)"] = None
        self._data["Front Side Infrared Emissivity"] = None
        self._data["Back Side Infrared Emissivity"] = None

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
            self.optical_data_type = None
        else:
            self.optical_data_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_glass_spectral_data_set_name = None
        else:
            self.window_glass_spectral_data_set_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_beambeam_solar_transmittance = None
        else:
            self.front_side_beambeam_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_beambeam_solar_transmittance = None
        else:
            self.back_side_beambeam_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_beambeam_solar_reflectance = None
        else:
            self.front_side_beambeam_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_beambeam_solar_reflectance = None
        else:
            self.back_side_beambeam_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_beambeam_visible_solar_transmittance = None
        else:
            self.front_side_beambeam_visible_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_beambeam_visible_solar_transmittance = None
        else:
            self.back_side_beambeam_visible_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_beambeam_visible_solar_reflectance = None
        else:
            self.front_side_beambeam_visible_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_beambeam_visible_solar_reflectance = None
        else:
            self.back_side_beambeam_visible_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_beamdiffuse_solar_transmittance = None
        else:
            self.front_side_beamdiffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_beamdiffuse_solar_transmittance = None
        else:
            self.back_side_beamdiffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_beamdiffuse_solar_reflectance = None
        else:
            self.front_side_beamdiffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_beamdiffuse_solar_reflectance = None
        else:
            self.back_side_beamdiffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_beamdiffuse_visible_solar_transmittance = None
        else:
            self.front_side_beamdiffuse_visible_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_beamdiffuse_visible_solar_transmittance = None
        else:
            self.back_side_beamdiffuse_visible_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_beamdiffuse_visible_solar_reflectance = None
        else:
            self.front_side_beamdiffuse_visible_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_beamdiffuse_visible_solar_reflectance = None
        else:
            self.back_side_beamdiffuse_visible_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffusediffuse_solar_transmittance = None
        else:
            self.diffusediffuse_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_diffusediffuse_solar_reflectance = None
        else:
            self.front_side_diffusediffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_diffusediffuse_solar_reflectance = None
        else:
            self.back_side_diffusediffuse_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffusediffuse_visible_solar_transmittance = None
        else:
            self.diffusediffuse_visible_solar_transmittance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_diffusediffuse_visible_solar_reflectance = None
        else:
            self.front_side_diffusediffuse_visible_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_diffusediffuse_visible_solar_reflectance = None
        else:
            self.back_side_diffusediffuse_visible_solar_reflectance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.infrared_transmittance_applies_to_front_and_back = None
        else:
            self.infrared_transmittance_applies_to_front_and_back = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_side_infrared_emissivity = None
        else:
            self.front_side_infrared_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_side_infrared_emissivity = None
        else:
            self.back_side_infrared_emissivity = vals[i]
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
    def optical_data_type(self):
        """Get optical_data_type

        Returns:
            str: the value of `optical_data_type` or None if not set
        """
        return self._data["Optical Data Type"]

    @optical_data_type.setter
    def optical_data_type(self, value=None):
        """  Corresponds to IDD Field `optical_data_type`

        Args:
            value (str): value for IDD Field `optical_data_type`
                Accepted values are:
                      - SpectralAverage
                      - Spectral (not supported now)
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
                                 'for field `optical_data_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `optical_data_type`')
            vals = set()
            vals.add("SpectralAverage")
            vals.add("Spectral (not supported now)")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `optical_data_type`'.format(value))

        self._data["Optical Data Type"] = value

    @property
    def window_glass_spectral_data_set_name(self):
        """Get window_glass_spectral_data_set_name

        Returns:
            str: the value of `window_glass_spectral_data_set_name` or None if not set
        """
        return self._data["Window Glass Spectral Data Set Name"]

    @window_glass_spectral_data_set_name.setter
    def window_glass_spectral_data_set_name(self, value=None):
        """  Corresponds to IDD Field `window_glass_spectral_data_set_name`
        Used only when Optical Data Type = Spectral

        Args:
            value (str): value for IDD Field `window_glass_spectral_data_set_name`
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
                                 'for field `window_glass_spectral_data_set_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_glass_spectral_data_set_name`')

        self._data["Window Glass Spectral Data Set Name"] = value

    @property
    def front_side_beambeam_solar_transmittance(self):
        """Get front_side_beambeam_solar_transmittance

        Returns:
            float: the value of `front_side_beambeam_solar_transmittance` or None if not set
        """
        return self._data["Front Side Beam-Beam Solar Transmittance"]

    @front_side_beambeam_solar_transmittance.setter
    def front_side_beambeam_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `front_side_beambeam_solar_transmittance`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `front_side_beambeam_solar_transmittance`
                Unit: dimensionless
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
                                 'for field `front_side_beambeam_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_beambeam_solar_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_beambeam_solar_transmittance`')

        self._data["Front Side Beam-Beam Solar Transmittance"] = value

    @property
    def back_side_beambeam_solar_transmittance(self):
        """Get back_side_beambeam_solar_transmittance

        Returns:
            float: the value of `back_side_beambeam_solar_transmittance` or None if not set
        """
        return self._data["Back Side Beam-Beam Solar Transmittance"]

    @back_side_beambeam_solar_transmittance.setter
    def back_side_beambeam_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `back_side_beambeam_solar_transmittance`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `back_side_beambeam_solar_transmittance`
                Unit: dimensionless
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
                                 'for field `back_side_beambeam_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_beambeam_solar_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_beambeam_solar_transmittance`')

        self._data["Back Side Beam-Beam Solar Transmittance"] = value

    @property
    def front_side_beambeam_solar_reflectance(self):
        """Get front_side_beambeam_solar_reflectance

        Returns:
            float: the value of `front_side_beambeam_solar_reflectance` or None if not set
        """
        return self._data["Front Side Beam-Beam Solar Reflectance"]

    @front_side_beambeam_solar_reflectance.setter
    def front_side_beambeam_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_beambeam_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        Front Side is side closest to outdoor air

        Args:
            value (float): value for IDD Field `front_side_beambeam_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `front_side_beambeam_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_beambeam_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_beambeam_solar_reflectance`')

        self._data["Front Side Beam-Beam Solar Reflectance"] = value

    @property
    def back_side_beambeam_solar_reflectance(self):
        """Get back_side_beambeam_solar_reflectance

        Returns:
            float: the value of `back_side_beambeam_solar_reflectance` or None if not set
        """
        return self._data["Back Side Beam-Beam Solar Reflectance"]

    @back_side_beambeam_solar_reflectance.setter
    def back_side_beambeam_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_beambeam_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        Back Side is side closest to zone air

        Args:
            value (float): value for IDD Field `back_side_beambeam_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `back_side_beambeam_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_beambeam_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_beambeam_solar_reflectance`')

        self._data["Back Side Beam-Beam Solar Reflectance"] = value

    @property
    def front_side_beambeam_visible_solar_transmittance(self):
        """Get front_side_beambeam_visible_solar_transmittance

        Returns:
            float: the value of `front_side_beambeam_visible_solar_transmittance` or None if not set
        """
        return self._data["Front Side Beam-Beam Visible Solar Transmittance"]

    @front_side_beambeam_visible_solar_transmittance.setter
    def front_side_beambeam_visible_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `front_side_beambeam_visible_solar_transmittance`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `front_side_beambeam_visible_solar_transmittance`
                Unit: dimensionless
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
                                 'for field `front_side_beambeam_visible_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_beambeam_visible_solar_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_beambeam_visible_solar_transmittance`')

        self._data["Front Side Beam-Beam Visible Solar Transmittance"] = value

    @property
    def back_side_beambeam_visible_solar_transmittance(self):
        """Get back_side_beambeam_visible_solar_transmittance

        Returns:
            float: the value of `back_side_beambeam_visible_solar_transmittance` or None if not set
        """
        return self._data["Back Side Beam-Beam Visible Solar Transmittance"]

    @back_side_beambeam_visible_solar_transmittance.setter
    def back_side_beambeam_visible_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `back_side_beambeam_visible_solar_transmittance`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `back_side_beambeam_visible_solar_transmittance`
                Unit: dimensionless
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
                                 'for field `back_side_beambeam_visible_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_beambeam_visible_solar_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_beambeam_visible_solar_transmittance`')

        self._data["Back Side Beam-Beam Visible Solar Transmittance"] = value

    @property
    def front_side_beambeam_visible_solar_reflectance(self):
        """Get front_side_beambeam_visible_solar_reflectance

        Returns:
            float: the value of `front_side_beambeam_visible_solar_reflectance` or None if not set
        """
        return self._data["Front Side Beam-Beam Visible Solar Reflectance"]

    @front_side_beambeam_visible_solar_reflectance.setter
    def front_side_beambeam_visible_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_beambeam_visible_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        Front Side is side closest to outdoor air

        Args:
            value (float): value for IDD Field `front_side_beambeam_visible_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `front_side_beambeam_visible_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_beambeam_visible_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_beambeam_visible_solar_reflectance`')

        self._data["Front Side Beam-Beam Visible Solar Reflectance"] = value

    @property
    def back_side_beambeam_visible_solar_reflectance(self):
        """Get back_side_beambeam_visible_solar_reflectance

        Returns:
            float: the value of `back_side_beambeam_visible_solar_reflectance` or None if not set
        """
        return self._data["Back Side Beam-Beam Visible Solar Reflectance"]

    @back_side_beambeam_visible_solar_reflectance.setter
    def back_side_beambeam_visible_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_beambeam_visible_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        Back Side is side closest to zone air

        Args:
            value (float): value for IDD Field `back_side_beambeam_visible_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `back_side_beambeam_visible_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_beambeam_visible_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_beambeam_visible_solar_reflectance`')

        self._data["Back Side Beam-Beam Visible Solar Reflectance"] = value

    @property
    def front_side_beamdiffuse_solar_transmittance(self):
        """Get front_side_beamdiffuse_solar_transmittance

        Returns:
            float: the value of `front_side_beamdiffuse_solar_transmittance` or None if not set
        """
        return self._data["Front Side Beam-Diffuse Solar Transmittance"]

    @front_side_beamdiffuse_solar_transmittance.setter
    def front_side_beamdiffuse_solar_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `front_side_beamdiffuse_solar_transmittance`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `front_side_beamdiffuse_solar_transmittance`
                Unit: dimensionless
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
                                 'for field `front_side_beamdiffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_beamdiffuse_solar_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_beamdiffuse_solar_transmittance`')

        self._data["Front Side Beam-Diffuse Solar Transmittance"] = value

    @property
    def back_side_beamdiffuse_solar_transmittance(self):
        """Get back_side_beamdiffuse_solar_transmittance

        Returns:
            float: the value of `back_side_beamdiffuse_solar_transmittance` or None if not set
        """
        return self._data["Back Side Beam-Diffuse Solar Transmittance"]

    @back_side_beamdiffuse_solar_transmittance.setter
    def back_side_beamdiffuse_solar_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `back_side_beamdiffuse_solar_transmittance`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `back_side_beamdiffuse_solar_transmittance`
                Unit: dimensionless
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
                                 'for field `back_side_beamdiffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_beamdiffuse_solar_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_beamdiffuse_solar_transmittance`')

        self._data["Back Side Beam-Diffuse Solar Transmittance"] = value

    @property
    def front_side_beamdiffuse_solar_reflectance(self):
        """Get front_side_beamdiffuse_solar_reflectance

        Returns:
            float: the value of `front_side_beamdiffuse_solar_reflectance` or None if not set
        """
        return self._data["Front Side Beam-Diffuse Solar Reflectance"]

    @front_side_beamdiffuse_solar_reflectance.setter
    def front_side_beamdiffuse_solar_reflectance(self, value=0.0 ):
        """  Corresponds to IDD Field `front_side_beamdiffuse_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        Front Side is side closest to outdoor air

        Args:
            value (float): value for IDD Field `front_side_beamdiffuse_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `front_side_beamdiffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_beamdiffuse_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_beamdiffuse_solar_reflectance`')

        self._data["Front Side Beam-Diffuse Solar Reflectance"] = value

    @property
    def back_side_beamdiffuse_solar_reflectance(self):
        """Get back_side_beamdiffuse_solar_reflectance

        Returns:
            float: the value of `back_side_beamdiffuse_solar_reflectance` or None if not set
        """
        return self._data["Back Side Beam-Diffuse Solar Reflectance"]

    @back_side_beamdiffuse_solar_reflectance.setter
    def back_side_beamdiffuse_solar_reflectance(self, value=0.0 ):
        """  Corresponds to IDD Field `back_side_beamdiffuse_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        Back Side is side closest to zone air

        Args:
            value (float): value for IDD Field `back_side_beamdiffuse_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `back_side_beamdiffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_beamdiffuse_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_beamdiffuse_solar_reflectance`')

        self._data["Back Side Beam-Diffuse Solar Reflectance"] = value

    @property
    def front_side_beamdiffuse_visible_solar_transmittance(self):
        """Get front_side_beamdiffuse_visible_solar_transmittance

        Returns:
            float: the value of `front_side_beamdiffuse_visible_solar_transmittance` or None if not set
        """
        return self._data["Front Side Beam-Diffuse Visible Solar Transmittance"]

    @front_side_beamdiffuse_visible_solar_transmittance.setter
    def front_side_beamdiffuse_visible_solar_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `front_side_beamdiffuse_visible_solar_transmittance`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `front_side_beamdiffuse_visible_solar_transmittance`
                Unit: dimensionless
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
                                 'for field `front_side_beamdiffuse_visible_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_beamdiffuse_visible_solar_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_beamdiffuse_visible_solar_transmittance`')

        self._data["Front Side Beam-Diffuse Visible Solar Transmittance"] = value

    @property
    def back_side_beamdiffuse_visible_solar_transmittance(self):
        """Get back_side_beamdiffuse_visible_solar_transmittance

        Returns:
            float: the value of `back_side_beamdiffuse_visible_solar_transmittance` or None if not set
        """
        return self._data["Back Side Beam-Diffuse Visible Solar Transmittance"]

    @back_side_beamdiffuse_visible_solar_transmittance.setter
    def back_side_beamdiffuse_visible_solar_transmittance(self, value=0.0 ):
        """  Corresponds to IDD Field `back_side_beamdiffuse_visible_solar_transmittance`
        Used only when Optical Data Type = SpectralAverage

        Args:
            value (float): value for IDD Field `back_side_beamdiffuse_visible_solar_transmittance`
                Unit: dimensionless
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
                                 'for field `back_side_beamdiffuse_visible_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_beamdiffuse_visible_solar_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_beamdiffuse_visible_solar_transmittance`')

        self._data["Back Side Beam-Diffuse Visible Solar Transmittance"] = value

    @property
    def front_side_beamdiffuse_visible_solar_reflectance(self):
        """Get front_side_beamdiffuse_visible_solar_reflectance

        Returns:
            float: the value of `front_side_beamdiffuse_visible_solar_reflectance` or None if not set
        """
        return self._data["Front Side Beam-Diffuse Visible Solar Reflectance"]

    @front_side_beamdiffuse_visible_solar_reflectance.setter
    def front_side_beamdiffuse_visible_solar_reflectance(self, value=0.0 ):
        """  Corresponds to IDD Field `front_side_beamdiffuse_visible_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        Front Side is side closest to outdoor air

        Args:
            value (float): value for IDD Field `front_side_beamdiffuse_visible_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `front_side_beamdiffuse_visible_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_beamdiffuse_visible_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_beamdiffuse_visible_solar_reflectance`')

        self._data["Front Side Beam-Diffuse Visible Solar Reflectance"] = value

    @property
    def back_side_beamdiffuse_visible_solar_reflectance(self):
        """Get back_side_beamdiffuse_visible_solar_reflectance

        Returns:
            float: the value of `back_side_beamdiffuse_visible_solar_reflectance` or None if not set
        """
        return self._data["Back Side Beam-Diffuse Visible Solar Reflectance"]

    @back_side_beamdiffuse_visible_solar_reflectance.setter
    def back_side_beamdiffuse_visible_solar_reflectance(self, value=0.0 ):
        """  Corresponds to IDD Field `back_side_beamdiffuse_visible_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        Back Side is side closest to zone air

        Args:
            value (float): value for IDD Field `back_side_beamdiffuse_visible_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `back_side_beamdiffuse_visible_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_beamdiffuse_visible_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_beamdiffuse_visible_solar_reflectance`')

        self._data["Back Side Beam-Diffuse Visible Solar Reflectance"] = value

    @property
    def diffusediffuse_solar_transmittance(self):
        """Get diffusediffuse_solar_transmittance

        Returns:
            float: the value of `diffusediffuse_solar_transmittance` or None if not set
        """
        return self._data["Diffuse-Diffuse Solar Transmittance"]

    @diffusediffuse_solar_transmittance.setter
    def diffusediffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `diffusediffuse_solar_transmittance`
        Used only when Optical Data Type = SpectralAverage
        If this field is autocalculate, then the diffuse-diffuse solar
        transmittance is automatically estimated from other inputs and used
        in subsequent calculations. If this field is zero or positive, then
        the value entered here will be used.

        Args:
            value (float): value for IDD Field `diffusediffuse_solar_transmittance`
                Unit: dimensionless
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
                                 'for field `diffusediffuse_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffusediffuse_solar_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `diffusediffuse_solar_transmittance`')

        self._data["Diffuse-Diffuse Solar Transmittance"] = value

    @property
    def front_side_diffusediffuse_solar_reflectance(self):
        """Get front_side_diffusediffuse_solar_reflectance

        Returns:
            float: the value of `front_side_diffusediffuse_solar_reflectance` or None if not set
        """
        return self._data["Front Side Diffuse-Diffuse Solar Reflectance"]

    @front_side_diffusediffuse_solar_reflectance.setter
    def front_side_diffusediffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_diffusediffuse_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        If this field is autocalculate, then the front diffuse-diffuse solar
        reflectance is automatically estimated from other inputs and used in
        subsequent calculations. If this field is zero or positive, then the value
        entered here will be used.  Front Side is side closest to outdoor air.

        Args:
            value (float): value for IDD Field `front_side_diffusediffuse_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `front_side_diffusediffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_diffusediffuse_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_diffusediffuse_solar_reflectance`')

        self._data["Front Side Diffuse-Diffuse Solar Reflectance"] = value

    @property
    def back_side_diffusediffuse_solar_reflectance(self):
        """Get back_side_diffusediffuse_solar_reflectance

        Returns:
            float: the value of `back_side_diffusediffuse_solar_reflectance` or None if not set
        """
        return self._data["Back Side Diffuse-Diffuse Solar Reflectance"]

    @back_side_diffusediffuse_solar_reflectance.setter
    def back_side_diffusediffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_diffusediffuse_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        If this field is autocalculate, then the back diffuse-diffuse solar
        reflectance is automatically estimated from other inputs and used in
        subsequent calculations. If this field is zero or positive, then the value
        entered here will be used.  Back side is side closest to indoor air.

        Args:
            value (float): value for IDD Field `back_side_diffusediffuse_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `back_side_diffusediffuse_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_diffusediffuse_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_diffusediffuse_solar_reflectance`')

        self._data["Back Side Diffuse-Diffuse Solar Reflectance"] = value

    @property
    def diffusediffuse_visible_solar_transmittance(self):
        """Get diffusediffuse_visible_solar_transmittance

        Returns:
            float: the value of `diffusediffuse_visible_solar_transmittance` or None if not set
        """
        return self._data["Diffuse-Diffuse Visible Solar Transmittance"]

    @diffusediffuse_visible_solar_transmittance.setter
    def diffusediffuse_visible_solar_transmittance(self, value=None):
        """  Corresponds to IDD Field `diffusediffuse_visible_solar_transmittance`
        Used only when Optical Data Type = SpectralAverage
        This input field is not used currently.

        Args:
            value (float): value for IDD Field `diffusediffuse_visible_solar_transmittance`
                Unit: dimensionless
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
                                 'for field `diffusediffuse_visible_solar_transmittance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffusediffuse_visible_solar_transmittance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `diffusediffuse_visible_solar_transmittance`')

        self._data["Diffuse-Diffuse Visible Solar Transmittance"] = value

    @property
    def front_side_diffusediffuse_visible_solar_reflectance(self):
        """Get front_side_diffusediffuse_visible_solar_reflectance

        Returns:
            float: the value of `front_side_diffusediffuse_visible_solar_reflectance` or None if not set
        """
        return self._data["Front Side Diffuse-Diffuse Visible Solar Reflectance"]

    @front_side_diffusediffuse_visible_solar_reflectance.setter
    def front_side_diffusediffuse_visible_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `front_side_diffusediffuse_visible_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        This input field is not used currently.

        Args:
            value (float): value for IDD Field `front_side_diffusediffuse_visible_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `front_side_diffusediffuse_visible_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `front_side_diffusediffuse_visible_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_diffusediffuse_visible_solar_reflectance`')

        self._data["Front Side Diffuse-Diffuse Visible Solar Reflectance"] = value

    @property
    def back_side_diffusediffuse_visible_solar_reflectance(self):
        """Get back_side_diffusediffuse_visible_solar_reflectance

        Returns:
            float: the value of `back_side_diffusediffuse_visible_solar_reflectance` or None if not set
        """
        return self._data["Back Side Diffuse-Diffuse Visible Solar Reflectance"]

    @back_side_diffusediffuse_visible_solar_reflectance.setter
    def back_side_diffusediffuse_visible_solar_reflectance(self, value=None):
        """  Corresponds to IDD Field `back_side_diffusediffuse_visible_solar_reflectance`
        Used only when Optical Data Type = SpectralAverage
        This input field is not used currently.

        Args:
            value (float): value for IDD Field `back_side_diffusediffuse_visible_solar_reflectance`
                Unit: dimensionless
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
                                 'for field `back_side_diffusediffuse_visible_solar_reflectance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `back_side_diffusediffuse_visible_solar_reflectance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_diffusediffuse_visible_solar_reflectance`')

        self._data["Back Side Diffuse-Diffuse Visible Solar Reflectance"] = value

    @property
    def infrared_transmittance_applies_to_front_and_back(self):
        """Get infrared_transmittance_applies_to_front_and_back

        Returns:
            float: the value of `infrared_transmittance_applies_to_front_and_back` or None if not set
        """
        return self._data["Infrared Transmittance (applies to front and back)"]

    @infrared_transmittance_applies_to_front_and_back.setter
    def infrared_transmittance_applies_to_front_and_back(self, value=0.0 ):
        """  Corresponds to IDD Field `infrared_transmittance_applies_to_front_and_back`
        The long-wave hemispherical transmittance of the glazing.
        Assumed to be the same for both sides of the glazing.

        Args:
            value (float): value for IDD Field `infrared_transmittance_applies_to_front_and_back`
                Unit: dimensionless
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
                                 'for field `infrared_transmittance_applies_to_front_and_back`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `infrared_transmittance_applies_to_front_and_back`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `infrared_transmittance_applies_to_front_and_back`')

        self._data["Infrared Transmittance (applies to front and back)"] = value

    @property
    def front_side_infrared_emissivity(self):
        """Get front_side_infrared_emissivity

        Returns:
            float: the value of `front_side_infrared_emissivity` or None if not set
        """
        return self._data["Front Side Infrared Emissivity"]

    @front_side_infrared_emissivity.setter
    def front_side_infrared_emissivity(self, value=0.84 ):
        """  Corresponds to IDD Field `front_side_infrared_emissivity`
        The front side long-wave hemispherical emissivity of the glazing.

        Args:
            value (float): value for IDD Field `front_side_infrared_emissivity`
                Unit: dimensionless
                Default value: 0.84
                value > 0.0
                value < 1.0
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
                                 'for field `front_side_infrared_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `front_side_infrared_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `front_side_infrared_emissivity`')

        self._data["Front Side Infrared Emissivity"] = value

    @property
    def back_side_infrared_emissivity(self):
        """Get back_side_infrared_emissivity

        Returns:
            float: the value of `back_side_infrared_emissivity` or None if not set
        """
        return self._data["Back Side Infrared Emissivity"]

    @back_side_infrared_emissivity.setter
    def back_side_infrared_emissivity(self, value=0.84 ):
        """  Corresponds to IDD Field `back_side_infrared_emissivity`
        The back side long-wave hemispherical emissivity of the glazing.

        Args:
            value (float): value for IDD Field `back_side_infrared_emissivity`
                Unit: dimensionless
                Default value: 0.84
                value > 0.0
                value < 1.0
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
                                 'for field `back_side_infrared_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `back_side_infrared_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `back_side_infrared_emissivity`')

        self._data["Back Side Infrared Emissivity"] = value

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
        out.append(self._to_str(self.optical_data_type))
        out.append(self._to_str(self.window_glass_spectral_data_set_name))
        out.append(self._to_str(self.front_side_beambeam_solar_transmittance))
        out.append(self._to_str(self.back_side_beambeam_solar_transmittance))
        out.append(self._to_str(self.front_side_beambeam_solar_reflectance))
        out.append(self._to_str(self.back_side_beambeam_solar_reflectance))
        out.append(self._to_str(self.front_side_beambeam_visible_solar_transmittance))
        out.append(self._to_str(self.back_side_beambeam_visible_solar_transmittance))
        out.append(self._to_str(self.front_side_beambeam_visible_solar_reflectance))
        out.append(self._to_str(self.back_side_beambeam_visible_solar_reflectance))
        out.append(self._to_str(self.front_side_beamdiffuse_solar_transmittance))
        out.append(self._to_str(self.back_side_beamdiffuse_solar_transmittance))
        out.append(self._to_str(self.front_side_beamdiffuse_solar_reflectance))
        out.append(self._to_str(self.back_side_beamdiffuse_solar_reflectance))
        out.append(self._to_str(self.front_side_beamdiffuse_visible_solar_transmittance))
        out.append(self._to_str(self.back_side_beamdiffuse_visible_solar_transmittance))
        out.append(self._to_str(self.front_side_beamdiffuse_visible_solar_reflectance))
        out.append(self._to_str(self.back_side_beamdiffuse_visible_solar_reflectance))
        out.append(self._to_str(self.diffusediffuse_solar_transmittance))
        out.append(self._to_str(self.front_side_diffusediffuse_solar_reflectance))
        out.append(self._to_str(self.back_side_diffusediffuse_solar_reflectance))
        out.append(self._to_str(self.diffusediffuse_visible_solar_transmittance))
        out.append(self._to_str(self.front_side_diffusediffuse_visible_solar_reflectance))
        out.append(self._to_str(self.back_side_diffusediffuse_visible_solar_reflectance))
        out.append(self._to_str(self.infrared_transmittance_applies_to_front_and_back))
        out.append(self._to_str(self.front_side_infrared_emissivity))
        out.append(self._to_str(self.back_side_infrared_emissivity))
        return ",".join(out)

class WindowMaterialGapEquivalentLayer(object):
    """ Corresponds to IDD object `WindowMaterial:Gap:EquivalentLayer`
        Gas material properties that are used in Windows Equivalent Layer
        References only WindowMaterial:Gas properties
    """
    internal_name = "WindowMaterial:Gap:EquivalentLayer"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowMaterial:Gap:EquivalentLayer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Gas Type"] = None
        self._data["Thickness"] = None
        self._data["Gap Vent Type"] = None
        self._data["Conductivity Coefficient A"] = None
        self._data["Conductivity Coefficient B"] = None
        self._data["Conductivity Coefficient C"] = None
        self._data["Viscosity Coefficient A"] = None
        self._data["Viscosity Coefficient B"] = None
        self._data["Viscosity Coefficient C"] = None
        self._data["Specific Heat Coefficient A"] = None
        self._data["Specific Heat Coefficient B"] = None
        self._data["Specific Heat Coefficient C"] = None
        self._data["Molecular Weight"] = None
        self._data["Specific Heat Ratio"] = None

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
            self.gas_type = None
        else:
            self.gas_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thickness = None
        else:
            self.thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_vent_type = None
        else:
            self.gap_vent_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity_coefficient_a = None
        else:
            self.conductivity_coefficient_a = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity_coefficient_b = None
        else:
            self.conductivity_coefficient_b = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductivity_coefficient_c = None
        else:
            self.conductivity_coefficient_c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.viscosity_coefficient_a = None
        else:
            self.viscosity_coefficient_a = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.viscosity_coefficient_b = None
        else:
            self.viscosity_coefficient_b = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.viscosity_coefficient_c = None
        else:
            self.viscosity_coefficient_c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.specific_heat_coefficient_a = None
        else:
            self.specific_heat_coefficient_a = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.specific_heat_coefficient_b = None
        else:
            self.specific_heat_coefficient_b = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.specific_heat_coefficient_c = None
        else:
            self.specific_heat_coefficient_c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.molecular_weight = None
        else:
            self.molecular_weight = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.specific_heat_ratio = None
        else:
            self.specific_heat_ratio = vals[i]
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
    def gas_type(self):
        """Get gas_type

        Returns:
            str: the value of `gas_type` or None if not set
        """
        return self._data["Gas Type"]

    @gas_type.setter
    def gas_type(self, value=None):
        """  Corresponds to IDD Field `gas_type`

        Args:
            value (str): value for IDD Field `gas_type`
                Accepted values are:
                      - AIR
                      - ARGON
                      - KRYPTON
                      - XENON
                      - CUSTOM
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
                                 'for field `gas_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gas_type`')
            vals = set()
            vals.add("AIR")
            vals.add("ARGON")
            vals.add("KRYPTON")
            vals.add("XENON")
            vals.add("CUSTOM")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `gas_type`'.format(value))

        self._data["Gas Type"] = value

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

        self._data["Thickness"] = value

    @property
    def gap_vent_type(self):
        """Get gap_vent_type

        Returns:
            str: the value of `gap_vent_type` or None if not set
        """
        return self._data["Gap Vent Type"]

    @gap_vent_type.setter
    def gap_vent_type(self, value=None):
        """  Corresponds to IDD Field `gap_vent_type`
        Sealed means the gap is enclosed and gas tight, i.e., no venting to indoor or
        outdoor environment.  VentedIndoor means the gap is vented to indoor environment, and
        VentedOutdoor means the gap is vented to the outdoor environment. The gap types
        VentedIndoor and VentedOutdoor are used with gas type Air only.

        Args:
            value (str): value for IDD Field `gap_vent_type`
                Accepted values are:
                      - Sealed
                      - VentedIndoor
                      - VentedOutdoor
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
                                 'for field `gap_vent_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_vent_type`')
            vals = set()
            vals.add("Sealed")
            vals.add("VentedIndoor")
            vals.add("VentedOutdoor")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `gap_vent_type`'.format(value))

        self._data["Gap Vent Type"] = value

    @property
    def conductivity_coefficient_a(self):
        """Get conductivity_coefficient_a

        Returns:
            float: the value of `conductivity_coefficient_a` or None if not set
        """
        return self._data["Conductivity Coefficient A"]

    @conductivity_coefficient_a.setter
    def conductivity_coefficient_a(self, value=None):
        """  Corresponds to IDD Field `conductivity_coefficient_a`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `conductivity_coefficient_a`
                Unit: W/m-K
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
                                 'for field `conductivity_coefficient_a`'.format(value))

        self._data["Conductivity Coefficient A"] = value

    @property
    def conductivity_coefficient_b(self):
        """Get conductivity_coefficient_b

        Returns:
            float: the value of `conductivity_coefficient_b` or None if not set
        """
        return self._data["Conductivity Coefficient B"]

    @conductivity_coefficient_b.setter
    def conductivity_coefficient_b(self, value=None):
        """  Corresponds to IDD Field `conductivity_coefficient_b`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `conductivity_coefficient_b`
                Unit: W/m-K2
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
                                 'for field `conductivity_coefficient_b`'.format(value))

        self._data["Conductivity Coefficient B"] = value

    @property
    def conductivity_coefficient_c(self):
        """Get conductivity_coefficient_c

        Returns:
            float: the value of `conductivity_coefficient_c` or None if not set
        """
        return self._data["Conductivity Coefficient C"]

    @conductivity_coefficient_c.setter
    def conductivity_coefficient_c(self, value=None):
        """  Corresponds to IDD Field `conductivity_coefficient_c`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `conductivity_coefficient_c`
                Unit: W/m-K3
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
                                 'for field `conductivity_coefficient_c`'.format(value))

        self._data["Conductivity Coefficient C"] = value

    @property
    def viscosity_coefficient_a(self):
        """Get viscosity_coefficient_a

        Returns:
            float: the value of `viscosity_coefficient_a` or None if not set
        """
        return self._data["Viscosity Coefficient A"]

    @viscosity_coefficient_a.setter
    def viscosity_coefficient_a(self, value=None):
        """  Corresponds to IDD Field `viscosity_coefficient_a`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `viscosity_coefficient_a`
                Unit: kg/m-s
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
                                 'for field `viscosity_coefficient_a`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `viscosity_coefficient_a`')

        self._data["Viscosity Coefficient A"] = value

    @property
    def viscosity_coefficient_b(self):
        """Get viscosity_coefficient_b

        Returns:
            float: the value of `viscosity_coefficient_b` or None if not set
        """
        return self._data["Viscosity Coefficient B"]

    @viscosity_coefficient_b.setter
    def viscosity_coefficient_b(self, value=None):
        """  Corresponds to IDD Field `viscosity_coefficient_b`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `viscosity_coefficient_b`
                Unit: kg/m-s-K
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
                                 'for field `viscosity_coefficient_b`'.format(value))

        self._data["Viscosity Coefficient B"] = value

    @property
    def viscosity_coefficient_c(self):
        """Get viscosity_coefficient_c

        Returns:
            float: the value of `viscosity_coefficient_c` or None if not set
        """
        return self._data["Viscosity Coefficient C"]

    @viscosity_coefficient_c.setter
    def viscosity_coefficient_c(self, value=None):
        """  Corresponds to IDD Field `viscosity_coefficient_c`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `viscosity_coefficient_c`
                Unit: kg/m-s-K2
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
                                 'for field `viscosity_coefficient_c`'.format(value))

        self._data["Viscosity Coefficient C"] = value

    @property
    def specific_heat_coefficient_a(self):
        """Get specific_heat_coefficient_a

        Returns:
            float: the value of `specific_heat_coefficient_a` or None if not set
        """
        return self._data["Specific Heat Coefficient A"]

    @specific_heat_coefficient_a.setter
    def specific_heat_coefficient_a(self, value=None):
        """  Corresponds to IDD Field `specific_heat_coefficient_a`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `specific_heat_coefficient_a`
                Unit: J/kg-K
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
                                 'for field `specific_heat_coefficient_a`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `specific_heat_coefficient_a`')

        self._data["Specific Heat Coefficient A"] = value

    @property
    def specific_heat_coefficient_b(self):
        """Get specific_heat_coefficient_b

        Returns:
            float: the value of `specific_heat_coefficient_b` or None if not set
        """
        return self._data["Specific Heat Coefficient B"]

    @specific_heat_coefficient_b.setter
    def specific_heat_coefficient_b(self, value=None):
        """  Corresponds to IDD Field `specific_heat_coefficient_b`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `specific_heat_coefficient_b`
                Unit: J/kg-K2
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
                                 'for field `specific_heat_coefficient_b`'.format(value))

        self._data["Specific Heat Coefficient B"] = value

    @property
    def specific_heat_coefficient_c(self):
        """Get specific_heat_coefficient_c

        Returns:
            float: the value of `specific_heat_coefficient_c` or None if not set
        """
        return self._data["Specific Heat Coefficient C"]

    @specific_heat_coefficient_c.setter
    def specific_heat_coefficient_c(self, value=None):
        """  Corresponds to IDD Field `specific_heat_coefficient_c`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `specific_heat_coefficient_c`
                Unit: J/kg-K3
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
                                 'for field `specific_heat_coefficient_c`'.format(value))

        self._data["Specific Heat Coefficient C"] = value

    @property
    def molecular_weight(self):
        """Get molecular_weight

        Returns:
            float: the value of `molecular_weight` or None if not set
        """
        return self._data["Molecular Weight"]

    @molecular_weight.setter
    def molecular_weight(self, value=None):
        """  Corresponds to IDD Field `molecular_weight`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `molecular_weight`
                Unit: g/mol
                value >= 20.0
                value <= 200.0
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
                                 'for field `molecular_weight`'.format(value))
            if value < 20.0:
                raise ValueError('value need to be greater or equal 20.0 '
                                 'for field `molecular_weight`')
            if value > 200.0:
                raise ValueError('value need to be smaller 200.0 '
                                 'for field `molecular_weight`')

        self._data["Molecular Weight"] = value

    @property
    def specific_heat_ratio(self):
        """Get specific_heat_ratio

        Returns:
            float: the value of `specific_heat_ratio` or None if not set
        """
        return self._data["Specific Heat Ratio"]

    @specific_heat_ratio.setter
    def specific_heat_ratio(self, value=None):
        """  Corresponds to IDD Field `specific_heat_ratio`
        Used only if Gas Type = Custom

        Args:
            value (float): value for IDD Field `specific_heat_ratio`
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
                                 'for field `specific_heat_ratio`'.format(value))

        self._data["Specific Heat Ratio"] = value

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
        out.append(self._to_str(self.gas_type))
        out.append(self._to_str(self.thickness))
        out.append(self._to_str(self.gap_vent_type))
        out.append(self._to_str(self.conductivity_coefficient_a))
        out.append(self._to_str(self.conductivity_coefficient_b))
        out.append(self._to_str(self.conductivity_coefficient_c))
        out.append(self._to_str(self.viscosity_coefficient_a))
        out.append(self._to_str(self.viscosity_coefficient_b))
        out.append(self._to_str(self.viscosity_coefficient_c))
        out.append(self._to_str(self.specific_heat_coefficient_a))
        out.append(self._to_str(self.specific_heat_coefficient_b))
        out.append(self._to_str(self.specific_heat_coefficient_c))
        out.append(self._to_str(self.molecular_weight))
        out.append(self._to_str(self.specific_heat_ratio))
        return ",".join(out)