from collections import OrderedDict

class WindowThermalModelParams(object):
    """ Corresponds to IDD object `WindowThermalModel:Params`
        object is used to select which thermal model should be used in tarcog simulations
    """
    internal_name = "WindowThermalModel:Params"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowThermalModel:Params`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["standard"] = None
        self._data["Thermal Model"] = None
        self._data["SDScalar"] = None
        self._data["Deflection Model"] = None
        self._data["Vacuum Pressure Limit"] = None
        self._data["Initial temperature"] = None
        self._data["Initial pressure"] = None

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
            self.standard = None
        else:
            self.standard = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_model = None
        else:
            self.thermal_model = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sdscalar = None
        else:
            self.sdscalar = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.deflection_model = None
        else:
            self.deflection_model = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vacuum_pressure_limit = None
        else:
            self.vacuum_pressure_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_temperature = None
        else:
            self.initial_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_pressure = None
        else:
            self.initial_pressure = vals[i]
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
    def standard(self):
        """Get standard

        Returns:
            str: the value of `standard` or None if not set
        """
        return self._data["standard"]

    @standard.setter
    def standard(self, value="ISO15099"):
        """  Corresponds to IDD Field `standard`

        Args:
            value (str): value for IDD Field `standard`
                Accepted values are:
                      - ISO15099
                      - EN673Declared
                      - EN673Design
                Default value: ISO15099
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
                                 'for field `standard`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `standard`')
            vals = set()
            vals.add("ISO15099")
            vals.add("EN673Declared")
            vals.add("EN673Design")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `standard`'.format(value))

        self._data["standard"] = value

    @property
    def thermal_model(self):
        """Get thermal_model

        Returns:
            str: the value of `thermal_model` or None if not set
        """
        return self._data["Thermal Model"]

    @thermal_model.setter
    def thermal_model(self, value="ISO15099"):
        """  Corresponds to IDD Field `thermal_model`

        Args:
            value (str): value for IDD Field `thermal_model`
                Accepted values are:
                      - ISO15099
                      - ScaledCavityWidth
                      - ConvectiveScalarModel_NoSDThickness
                      - ConvectiveScalarModel_withSDThickness
                Default value: ISO15099
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
                                 'for field `thermal_model`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_model`')
            vals = set()
            vals.add("ISO15099")
            vals.add("ScaledCavityWidth")
            vals.add("ConvectiveScalarModel_NoSDThickness")
            vals.add("ConvectiveScalarModel_withSDThickness")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `thermal_model`'.format(value))

        self._data["Thermal Model"] = value

    @property
    def sdscalar(self):
        """Get sdscalar

        Returns:
            float: the value of `sdscalar` or None if not set
        """
        return self._data["SDScalar"]

    @sdscalar.setter
    def sdscalar(self, value=1.0 ):
        """  Corresponds to IDD Field `sdscalar`

        Args:
            value (float): value for IDD Field `sdscalar`
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
                                 'for field `sdscalar`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `sdscalar`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `sdscalar`')

        self._data["SDScalar"] = value

    @property
    def deflection_model(self):
        """Get deflection_model

        Returns:
            str: the value of `deflection_model` or None if not set
        """
        return self._data["Deflection Model"]

    @deflection_model.setter
    def deflection_model(self, value="NoDeflection"):
        """  Corresponds to IDD Field `deflection_model`

        Args:
            value (str): value for IDD Field `deflection_model`
                Accepted values are:
                      - NoDeflection
                      - TemperatureAndPressureInput
                      - MeasuredDeflection
                Default value: NoDeflection
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
                                 'for field `deflection_model`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `deflection_model`')
            vals = set()
            vals.add("NoDeflection")
            vals.add("TemperatureAndPressureInput")
            vals.add("MeasuredDeflection")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `deflection_model`'.format(value))

        self._data["Deflection Model"] = value

    @property
    def vacuum_pressure_limit(self):
        """Get vacuum_pressure_limit

        Returns:
            float: the value of `vacuum_pressure_limit` or None if not set
        """
        return self._data["Vacuum Pressure Limit"]

    @vacuum_pressure_limit.setter
    def vacuum_pressure_limit(self, value=13.238 ):
        """  Corresponds to IDD Field `vacuum_pressure_limit`

        Args:
            value (float): value for IDD Field `vacuum_pressure_limit`
                Unit: Pa
                Default value: 13.238
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vacuum_pressure_limit`'.format(value))

        self._data["Vacuum Pressure Limit"] = value

    @property
    def initial_temperature(self):
        """Get initial_temperature

        Returns:
            float: the value of `initial_temperature` or None if not set
        """
        return self._data["Initial temperature"]

    @initial_temperature.setter
    def initial_temperature(self, value=25.0 ):
        """  Corresponds to IDD Field `initial_temperature`
        This is temperature in time of window fabrication

        Args:
            value (float): value for IDD Field `initial_temperature`
                Unit: C
                Default value: 25.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `initial_temperature`'.format(value))

        self._data["Initial temperature"] = value

    @property
    def initial_pressure(self):
        """Get initial_pressure

        Returns:
            float: the value of `initial_pressure` or None if not set
        """
        return self._data["Initial pressure"]

    @initial_pressure.setter
    def initial_pressure(self, value=101325.0 ):
        """  Corresponds to IDD Field `initial_pressure`
        This is pressure in time of window fabrication

        Args:
            value (float): value for IDD Field `initial_pressure`
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
                                 'for field `initial_pressure`'.format(value))

        self._data["Initial pressure"] = value

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
        out.append(self._to_str(self.standard))
        out.append(self._to_str(self.thermal_model))
        out.append(self._to_str(self.sdscalar))
        out.append(self._to_str(self.deflection_model))
        out.append(self._to_str(self.vacuum_pressure_limit))
        out.append(self._to_str(self.initial_temperature))
        out.append(self._to_str(self.initial_pressure))
        return ",".join(out)