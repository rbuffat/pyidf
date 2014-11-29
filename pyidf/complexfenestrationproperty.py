from collections import OrderedDict

class ComplexFenestrationPropertySolarAbsorbedLayers(object):
    """ Corresponds to IDD object `ComplexFenestrationProperty:SolarAbsorbedLayers`
        Used to provide solar radiation absorbed in fenestration layers. References surface-construction pair
        and if that pair is used in a simulation, then program will use value provided in schedules instead of calculating it.
    """
    internal_name = "ComplexFenestrationProperty:SolarAbsorbedLayers"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ComplexFenestrationProperty:SolarAbsorbedLayers`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fenestration Surface"] = None
        self._data["Construction Name"] = None
        self._data["Layer 1 Solar Radiation Absorbed Schedule Name"] = None
        self._data["Layer 2 Solar Radiation Absorbed Schedule Name"] = None
        self._data["Layer 3 Solar Radiation Absorbed Schedule Name"] = None
        self._data["Layer 4 Solar Radiation Absorbed Schedule Name"] = None
        self._data["Layer 5 Solar Radiation Absorbed Schedule Name"] = None

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
            self.fenestration_surface = None
        else:
            self.fenestration_surface = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_1_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_1_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_2_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_2_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_3_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_3_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_4_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_4_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_5_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_5_solar_radiation_absorbed_schedule_name = vals[i]
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
    def fenestration_surface(self):
        """Get fenestration_surface

        Returns:
            str: the value of `fenestration_surface` or None if not set
        """
        return self._data["Fenestration Surface"]

    @fenestration_surface.setter
    def fenestration_surface(self, value=None):
        """  Corresponds to IDD Field `fenestration_surface`

        Args:
            value (str): value for IDD Field `fenestration_surface`
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
                                 'for field `fenestration_surface`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fenestration_surface`')

        self._data["Fenestration Surface"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`

        Args:
            value (str): value for IDD Field `construction_name`
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
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def layer_1_solar_radiation_absorbed_schedule_name(self):
        """Get layer_1_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_1_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 1 Solar Radiation Absorbed Schedule Name"]

    @layer_1_solar_radiation_absorbed_schedule_name.setter
    def layer_1_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `layer_1_solar_radiation_absorbed_schedule_name`

        Args:
            value (str): value for IDD Field `layer_1_solar_radiation_absorbed_schedule_name`
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
                                 'for field `layer_1_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_1_solar_radiation_absorbed_schedule_name`')

        self._data["Layer 1 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_2_solar_radiation_absorbed_schedule_name(self):
        """Get layer_2_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_2_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 2 Solar Radiation Absorbed Schedule Name"]

    @layer_2_solar_radiation_absorbed_schedule_name.setter
    def layer_2_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `layer_2_solar_radiation_absorbed_schedule_name`

        Args:
            value (str): value for IDD Field `layer_2_solar_radiation_absorbed_schedule_name`
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
                                 'for field `layer_2_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_2_solar_radiation_absorbed_schedule_name`')

        self._data["Layer 2 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_3_solar_radiation_absorbed_schedule_name(self):
        """Get layer_3_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_3_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 3 Solar Radiation Absorbed Schedule Name"]

    @layer_3_solar_radiation_absorbed_schedule_name.setter
    def layer_3_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `layer_3_solar_radiation_absorbed_schedule_name`

        Args:
            value (str): value for IDD Field `layer_3_solar_radiation_absorbed_schedule_name`
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
                                 'for field `layer_3_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_3_solar_radiation_absorbed_schedule_name`')

        self._data["Layer 3 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_4_solar_radiation_absorbed_schedule_name(self):
        """Get layer_4_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_4_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 4 Solar Radiation Absorbed Schedule Name"]

    @layer_4_solar_radiation_absorbed_schedule_name.setter
    def layer_4_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `layer_4_solar_radiation_absorbed_schedule_name`

        Args:
            value (str): value for IDD Field `layer_4_solar_radiation_absorbed_schedule_name`
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
                                 'for field `layer_4_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_4_solar_radiation_absorbed_schedule_name`')

        self._data["Layer 4 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_5_solar_radiation_absorbed_schedule_name(self):
        """Get layer_5_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_5_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 5 Solar Radiation Absorbed Schedule Name"]

    @layer_5_solar_radiation_absorbed_schedule_name.setter
    def layer_5_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `layer_5_solar_radiation_absorbed_schedule_name`

        Args:
            value (str): value for IDD Field `layer_5_solar_radiation_absorbed_schedule_name`
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
                                 'for field `layer_5_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_5_solar_radiation_absorbed_schedule_name`')

        self._data["Layer 5 Solar Radiation Absorbed Schedule Name"] = value

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
        out.append(self._to_str(self.fenestration_surface))
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.layer_1_solar_radiation_absorbed_schedule_name))
        out.append(self._to_str(self.layer_2_solar_radiation_absorbed_schedule_name))
        out.append(self._to_str(self.layer_3_solar_radiation_absorbed_schedule_name))
        out.append(self._to_str(self.layer_4_solar_radiation_absorbed_schedule_name))
        out.append(self._to_str(self.layer_5_solar_radiation_absorbed_schedule_name))
        return ",".join(out)