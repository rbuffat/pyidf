from collections import OrderedDict

class MaterialPropertyMoisturePenetrationDepthSettings(object):
    """ Corresponds to IDD object `MaterialProperty:MoisturePenetrationDepth:Settings`
        Additional properties for moisture using EMPD procedure
        HeatBalanceAlgorithm choice=MoisturePenetrationDepthConductionTransferFunction only
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    internal_name = "MaterialProperty:MoisturePenetrationDepth:Settings"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `MaterialProperty:MoisturePenetrationDepth:Settings`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Moisture Penetration Depth"] = None
        self._data["Moisture Equation Coefficient a"] = None
        self._data["Moisture Equation Coefficient b"] = None
        self._data["Moisture Equation Coefficient c"] = None
        self._data["Moisture Equation Coefficient d"] = None

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
            self.moisture_penetration_depth = None
        else:
            self.moisture_penetration_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_equation_coefficient_a = None
        else:
            self.moisture_equation_coefficient_a = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_equation_coefficient_b = None
        else:
            self.moisture_equation_coefficient_b = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_equation_coefficient_c = None
        else:
            self.moisture_equation_coefficient_c = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_equation_coefficient_d = None
        else:
            self.moisture_equation_coefficient_d = vals[i]
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
        Material Name that the moisture properties will be added to.
        Additional material properties required to perform the EMPD model.
        Effective Mean Penetration Depth (EMPD)

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
    def moisture_penetration_depth(self):
        """Get moisture_penetration_depth

        Returns:
            float: the value of `moisture_penetration_depth` or None if not set
        """
        return self._data["Moisture Penetration Depth"]

    @moisture_penetration_depth.setter
    def moisture_penetration_depth(self, value=None):
        """  Corresponds to IDD Field `moisture_penetration_depth`
        This is the penetration depth

        Args:
            value (float): value for IDD Field `moisture_penetration_depth`
                Unit: m
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
                                 'for field `moisture_penetration_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_penetration_depth`')

        self._data["Moisture Penetration Depth"] = value

    @property
    def moisture_equation_coefficient_a(self):
        """Get moisture_equation_coefficient_a

        Returns:
            float: the value of `moisture_equation_coefficient_a` or None if not set
        """
        return self._data["Moisture Equation Coefficient a"]

    @moisture_equation_coefficient_a.setter
    def moisture_equation_coefficient_a(self, value=None):
        """  Corresponds to IDD Field `moisture_equation_coefficient_a`

        Args:
            value (float): value for IDD Field `moisture_equation_coefficient_a`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `moisture_equation_coefficient_a`'.format(value))

        self._data["Moisture Equation Coefficient a"] = value

    @property
    def moisture_equation_coefficient_b(self):
        """Get moisture_equation_coefficient_b

        Returns:
            float: the value of `moisture_equation_coefficient_b` or None if not set
        """
        return self._data["Moisture Equation Coefficient b"]

    @moisture_equation_coefficient_b.setter
    def moisture_equation_coefficient_b(self, value=None):
        """  Corresponds to IDD Field `moisture_equation_coefficient_b`

        Args:
            value (float): value for IDD Field `moisture_equation_coefficient_b`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `moisture_equation_coefficient_b`'.format(value))

        self._data["Moisture Equation Coefficient b"] = value

    @property
    def moisture_equation_coefficient_c(self):
        """Get moisture_equation_coefficient_c

        Returns:
            float: the value of `moisture_equation_coefficient_c` or None if not set
        """
        return self._data["Moisture Equation Coefficient c"]

    @moisture_equation_coefficient_c.setter
    def moisture_equation_coefficient_c(self, value=None):
        """  Corresponds to IDD Field `moisture_equation_coefficient_c`

        Args:
            value (float): value for IDD Field `moisture_equation_coefficient_c`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `moisture_equation_coefficient_c`'.format(value))

        self._data["Moisture Equation Coefficient c"] = value

    @property
    def moisture_equation_coefficient_d(self):
        """Get moisture_equation_coefficient_d

        Returns:
            float: the value of `moisture_equation_coefficient_d` or None if not set
        """
        return self._data["Moisture Equation Coefficient d"]

    @moisture_equation_coefficient_d.setter
    def moisture_equation_coefficient_d(self, value=None):
        """  Corresponds to IDD Field `moisture_equation_coefficient_d`

        Args:
            value (float): value for IDD Field `moisture_equation_coefficient_d`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `moisture_equation_coefficient_d`'.format(value))

        self._data["Moisture Equation Coefficient d"] = value

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
        out.append(self._to_str(self.moisture_penetration_depth))
        out.append(self._to_str(self.moisture_equation_coefficient_a))
        out.append(self._to_str(self.moisture_equation_coefficient_b))
        out.append(self._to_str(self.moisture_equation_coefficient_c))
        out.append(self._to_str(self.moisture_equation_coefficient_d))
        return ",".join(out)

class MaterialPropertyPhaseChange(object):
    """ Corresponds to IDD object `MaterialProperty:PhaseChange`
        Additional properties for temperature dependent thermal conductivity
        and enthalpy for Phase Change Materials (PCM)
        HeatBalanceAlgorithm = CondFD(ConductionFiniteDifference) solution algorithm only.
        Constructions with this should use the detailed CondFD process.
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    internal_name = "MaterialProperty:PhaseChange"
    field_count = 34

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `MaterialProperty:PhaseChange`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Temperature Coefficient for Thermal Conductivity"] = None
        self._data["Temperature 1"] = None
        self._data["Enthalpy 1"] = None
        self._data["Temperature 2"] = None
        self._data["Enthalpy 2"] = None
        self._data["Temperature 3"] = None
        self._data["Enthalpy 3"] = None
        self._data["Temperature 4"] = None
        self._data["Enthalpy 4"] = None
        self._data["Temperature 5"] = None
        self._data["Enthalpy 5"] = None
        self._data["Temperature 6"] = None
        self._data["Enthalpy 6"] = None
        self._data["Temperature 7"] = None
        self._data["Enthalpy 7"] = None
        self._data["Temperature 8"] = None
        self._data["Enthalpy 8"] = None
        self._data["Temperature 9"] = None
        self._data["Enthalpy 9"] = None
        self._data["Temperature 10"] = None
        self._data["Enthalpy 10"] = None
        self._data["Temperature 11"] = None
        self._data["Enthalpy 11"] = None
        self._data["Temperature 12"] = None
        self._data["Enthalpy 12"] = None
        self._data["Temperature 13"] = None
        self._data["Enthalpy 13"] = None
        self._data["Temperature 14"] = None
        self._data["Enthalpy 14"] = None
        self._data["Temperature 15"] = None
        self._data["Enthalpy 15"] = None
        self._data["Temperature 16"] = None
        self._data["Enthalpy 16"] = None

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
            self.temperature_coefficient_for_thermal_conductivity = None
        else:
            self.temperature_coefficient_for_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_1 = None
        else:
            self.temperature_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_1 = None
        else:
            self.enthalpy_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_2 = None
        else:
            self.temperature_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_2 = None
        else:
            self.enthalpy_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_3 = None
        else:
            self.temperature_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_3 = None
        else:
            self.enthalpy_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_4 = None
        else:
            self.temperature_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_4 = None
        else:
            self.enthalpy_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_5 = None
        else:
            self.temperature_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_5 = None
        else:
            self.enthalpy_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_6 = None
        else:
            self.temperature_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_6 = None
        else:
            self.enthalpy_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_7 = None
        else:
            self.temperature_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_7 = None
        else:
            self.enthalpy_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_8 = None
        else:
            self.temperature_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_8 = None
        else:
            self.enthalpy_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_9 = None
        else:
            self.temperature_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_9 = None
        else:
            self.enthalpy_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_10 = None
        else:
            self.temperature_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_10 = None
        else:
            self.enthalpy_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_11 = None
        else:
            self.temperature_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_11 = None
        else:
            self.enthalpy_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_12 = None
        else:
            self.temperature_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_12 = None
        else:
            self.enthalpy_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_13 = None
        else:
            self.temperature_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_13 = None
        else:
            self.enthalpy_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_14 = None
        else:
            self.temperature_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_14 = None
        else:
            self.enthalpy_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_15 = None
        else:
            self.temperature_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_15 = None
        else:
            self.enthalpy_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_16 = None
        else:
            self.temperature_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.enthalpy_16 = None
        else:
            self.enthalpy_16 = vals[i]
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
        Regular Material Name to which the additional properties will be added.
        this the material name for the basic material properties.

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
    def temperature_coefficient_for_thermal_conductivity(self):
        """Get temperature_coefficient_for_thermal_conductivity

        Returns:
            float: the value of `temperature_coefficient_for_thermal_conductivity` or None if not set
        """
        return self._data["Temperature Coefficient for Thermal Conductivity"]

    @temperature_coefficient_for_thermal_conductivity.setter
    def temperature_coefficient_for_thermal_conductivity(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_coefficient_for_thermal_conductivity`
        The base temperature is 20C.
        This is the thermal conductivity change per degree excursion from 20C.
        This variable conductivity function is overridden by the VariableThermalConductivity object, if present.

        Args:
            value (float): value for IDD Field `temperature_coefficient_for_thermal_conductivity`
                Unit: W/m-K2
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_coefficient_for_thermal_conductivity`'.format(value))

        self._data["Temperature Coefficient for Thermal Conductivity"] = value

    @property
    def temperature_1(self):
        """Get temperature_1

        Returns:
            float: the value of `temperature_1` or None if not set
        """
        return self._data["Temperature 1"]

    @temperature_1.setter
    def temperature_1(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_1`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_1`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_1`'.format(value))

        self._data["Temperature 1"] = value

    @property
    def enthalpy_1(self):
        """Get enthalpy_1

        Returns:
            float: the value of `enthalpy_1` or None if not set
        """
        return self._data["Enthalpy 1"]

    @enthalpy_1.setter
    def enthalpy_1(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_1`
        for Temperature-enthalpy function corresponding to temperature 1

        Args:
            value (float): value for IDD Field `enthalpy_1`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_1`'.format(value))

        self._data["Enthalpy 1"] = value

    @property
    def temperature_2(self):
        """Get temperature_2

        Returns:
            float: the value of `temperature_2` or None if not set
        """
        return self._data["Temperature 2"]

    @temperature_2.setter
    def temperature_2(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_2`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_2`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_2`'.format(value))

        self._data["Temperature 2"] = value

    @property
    def enthalpy_2(self):
        """Get enthalpy_2

        Returns:
            float: the value of `enthalpy_2` or None if not set
        """
        return self._data["Enthalpy 2"]

    @enthalpy_2.setter
    def enthalpy_2(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_2`
        for Temperature-enthalpy function corresponding to temperature 2

        Args:
            value (float): value for IDD Field `enthalpy_2`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_2`'.format(value))

        self._data["Enthalpy 2"] = value

    @property
    def temperature_3(self):
        """Get temperature_3

        Returns:
            float: the value of `temperature_3` or None if not set
        """
        return self._data["Temperature 3"]

    @temperature_3.setter
    def temperature_3(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_3`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_3`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_3`'.format(value))

        self._data["Temperature 3"] = value

    @property
    def enthalpy_3(self):
        """Get enthalpy_3

        Returns:
            float: the value of `enthalpy_3` or None if not set
        """
        return self._data["Enthalpy 3"]

    @enthalpy_3.setter
    def enthalpy_3(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_3`
        for Temperature-enthalpy function corresponding to temperature 3

        Args:
            value (float): value for IDD Field `enthalpy_3`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_3`'.format(value))

        self._data["Enthalpy 3"] = value

    @property
    def temperature_4(self):
        """Get temperature_4

        Returns:
            float: the value of `temperature_4` or None if not set
        """
        return self._data["Temperature 4"]

    @temperature_4.setter
    def temperature_4(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_4`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_4`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_4`'.format(value))

        self._data["Temperature 4"] = value

    @property
    def enthalpy_4(self):
        """Get enthalpy_4

        Returns:
            float: the value of `enthalpy_4` or None if not set
        """
        return self._data["Enthalpy 4"]

    @enthalpy_4.setter
    def enthalpy_4(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_4`
        for Temperature-enthalpy function corresponding to temperature 4

        Args:
            value (float): value for IDD Field `enthalpy_4`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_4`'.format(value))

        self._data["Enthalpy 4"] = value

    @property
    def temperature_5(self):
        """Get temperature_5

        Returns:
            float: the value of `temperature_5` or None if not set
        """
        return self._data["Temperature 5"]

    @temperature_5.setter
    def temperature_5(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_5`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_5`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_5`'.format(value))

        self._data["Temperature 5"] = value

    @property
    def enthalpy_5(self):
        """Get enthalpy_5

        Returns:
            float: the value of `enthalpy_5` or None if not set
        """
        return self._data["Enthalpy 5"]

    @enthalpy_5.setter
    def enthalpy_5(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_5`
        for Temperature-enthalpy function corresponding to temperature 5

        Args:
            value (float): value for IDD Field `enthalpy_5`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_5`'.format(value))

        self._data["Enthalpy 5"] = value

    @property
    def temperature_6(self):
        """Get temperature_6

        Returns:
            float: the value of `temperature_6` or None if not set
        """
        return self._data["Temperature 6"]

    @temperature_6.setter
    def temperature_6(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_6`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_6`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_6`'.format(value))

        self._data["Temperature 6"] = value

    @property
    def enthalpy_6(self):
        """Get enthalpy_6

        Returns:
            float: the value of `enthalpy_6` or None if not set
        """
        return self._data["Enthalpy 6"]

    @enthalpy_6.setter
    def enthalpy_6(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_6`
        for Temperature-enthalpy function corresponding to temperature 6

        Args:
            value (float): value for IDD Field `enthalpy_6`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_6`'.format(value))

        self._data["Enthalpy 6"] = value

    @property
    def temperature_7(self):
        """Get temperature_7

        Returns:
            float: the value of `temperature_7` or None if not set
        """
        return self._data["Temperature 7"]

    @temperature_7.setter
    def temperature_7(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_7`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_7`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_7`'.format(value))

        self._data["Temperature 7"] = value

    @property
    def enthalpy_7(self):
        """Get enthalpy_7

        Returns:
            float: the value of `enthalpy_7` or None if not set
        """
        return self._data["Enthalpy 7"]

    @enthalpy_7.setter
    def enthalpy_7(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_7`
        for Temperature-enthalpy function corresponding to temperature 7

        Args:
            value (float): value for IDD Field `enthalpy_7`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_7`'.format(value))

        self._data["Enthalpy 7"] = value

    @property
    def temperature_8(self):
        """Get temperature_8

        Returns:
            float: the value of `temperature_8` or None if not set
        """
        return self._data["Temperature 8"]

    @temperature_8.setter
    def temperature_8(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_8`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_8`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_8`'.format(value))

        self._data["Temperature 8"] = value

    @property
    def enthalpy_8(self):
        """Get enthalpy_8

        Returns:
            float: the value of `enthalpy_8` or None if not set
        """
        return self._data["Enthalpy 8"]

    @enthalpy_8.setter
    def enthalpy_8(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_8`
        for Temperature-enthalpy function corresponding to temperature 8

        Args:
            value (float): value for IDD Field `enthalpy_8`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_8`'.format(value))

        self._data["Enthalpy 8"] = value

    @property
    def temperature_9(self):
        """Get temperature_9

        Returns:
            float: the value of `temperature_9` or None if not set
        """
        return self._data["Temperature 9"]

    @temperature_9.setter
    def temperature_9(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_9`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_9`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_9`'.format(value))

        self._data["Temperature 9"] = value

    @property
    def enthalpy_9(self):
        """Get enthalpy_9

        Returns:
            float: the value of `enthalpy_9` or None if not set
        """
        return self._data["Enthalpy 9"]

    @enthalpy_9.setter
    def enthalpy_9(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_9`
        for Temperature-enthalpy function corresponding to temperature 1

        Args:
            value (float): value for IDD Field `enthalpy_9`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_9`'.format(value))

        self._data["Enthalpy 9"] = value

    @property
    def temperature_10(self):
        """Get temperature_10

        Returns:
            float: the value of `temperature_10` or None if not set
        """
        return self._data["Temperature 10"]

    @temperature_10.setter
    def temperature_10(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_10`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_10`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_10`'.format(value))

        self._data["Temperature 10"] = value

    @property
    def enthalpy_10(self):
        """Get enthalpy_10

        Returns:
            float: the value of `enthalpy_10` or None if not set
        """
        return self._data["Enthalpy 10"]

    @enthalpy_10.setter
    def enthalpy_10(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_10`
        for Temperature-enthalpy function corresponding to temperature 2

        Args:
            value (float): value for IDD Field `enthalpy_10`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_10`'.format(value))

        self._data["Enthalpy 10"] = value

    @property
    def temperature_11(self):
        """Get temperature_11

        Returns:
            float: the value of `temperature_11` or None if not set
        """
        return self._data["Temperature 11"]

    @temperature_11.setter
    def temperature_11(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_11`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_11`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_11`'.format(value))

        self._data["Temperature 11"] = value

    @property
    def enthalpy_11(self):
        """Get enthalpy_11

        Returns:
            float: the value of `enthalpy_11` or None if not set
        """
        return self._data["Enthalpy 11"]

    @enthalpy_11.setter
    def enthalpy_11(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_11`
        for Temperature-enthalpy function corresponding to temperature 3

        Args:
            value (float): value for IDD Field `enthalpy_11`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_11`'.format(value))

        self._data["Enthalpy 11"] = value

    @property
    def temperature_12(self):
        """Get temperature_12

        Returns:
            float: the value of `temperature_12` or None if not set
        """
        return self._data["Temperature 12"]

    @temperature_12.setter
    def temperature_12(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_12`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_12`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_12`'.format(value))

        self._data["Temperature 12"] = value

    @property
    def enthalpy_12(self):
        """Get enthalpy_12

        Returns:
            float: the value of `enthalpy_12` or None if not set
        """
        return self._data["Enthalpy 12"]

    @enthalpy_12.setter
    def enthalpy_12(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_12`
        for Temperature-enthalpy function corresponding to temperature 14

        Args:
            value (float): value for IDD Field `enthalpy_12`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_12`'.format(value))

        self._data["Enthalpy 12"] = value

    @property
    def temperature_13(self):
        """Get temperature_13

        Returns:
            float: the value of `temperature_13` or None if not set
        """
        return self._data["Temperature 13"]

    @temperature_13.setter
    def temperature_13(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_13`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_13`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_13`'.format(value))

        self._data["Temperature 13"] = value

    @property
    def enthalpy_13(self):
        """Get enthalpy_13

        Returns:
            float: the value of `enthalpy_13` or None if not set
        """
        return self._data["Enthalpy 13"]

    @enthalpy_13.setter
    def enthalpy_13(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_13`
        for Temperature-enthalpy function corresponding to temperature 15

        Args:
            value (float): value for IDD Field `enthalpy_13`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_13`'.format(value))

        self._data["Enthalpy 13"] = value

    @property
    def temperature_14(self):
        """Get temperature_14

        Returns:
            float: the value of `temperature_14` or None if not set
        """
        return self._data["Temperature 14"]

    @temperature_14.setter
    def temperature_14(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_14`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_14`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_14`'.format(value))

        self._data["Temperature 14"] = value

    @property
    def enthalpy_14(self):
        """Get enthalpy_14

        Returns:
            float: the value of `enthalpy_14` or None if not set
        """
        return self._data["Enthalpy 14"]

    @enthalpy_14.setter
    def enthalpy_14(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_14`
        for Temperature-enthalpy function corresponding to temperature 16

        Args:
            value (float): value for IDD Field `enthalpy_14`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_14`'.format(value))

        self._data["Enthalpy 14"] = value

    @property
    def temperature_15(self):
        """Get temperature_15

        Returns:
            float: the value of `temperature_15` or None if not set
        """
        return self._data["Temperature 15"]

    @temperature_15.setter
    def temperature_15(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_15`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_15`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_15`'.format(value))

        self._data["Temperature 15"] = value

    @property
    def enthalpy_15(self):
        """Get enthalpy_15

        Returns:
            float: the value of `enthalpy_15` or None if not set
        """
        return self._data["Enthalpy 15"]

    @enthalpy_15.setter
    def enthalpy_15(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_15`
        for Temperature-enthalpy function corresponding to temperature 17

        Args:
            value (float): value for IDD Field `enthalpy_15`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_15`'.format(value))

        self._data["Enthalpy 15"] = value

    @property
    def temperature_16(self):
        """Get temperature_16

        Returns:
            float: the value of `temperature_16` or None if not set
        """
        return self._data["Temperature 16"]

    @temperature_16.setter
    def temperature_16(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_16`
        for Temperature-enthalpy function

        Args:
            value (float): value for IDD Field `temperature_16`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_16`'.format(value))

        self._data["Temperature 16"] = value

    @property
    def enthalpy_16(self):
        """Get enthalpy_16

        Returns:
            float: the value of `enthalpy_16` or None if not set
        """
        return self._data["Enthalpy 16"]

    @enthalpy_16.setter
    def enthalpy_16(self, value=0.0 ):
        """  Corresponds to IDD Field `enthalpy_16`
        for Temperature-enthalpy function corresponding to temperature 16

        Args:
            value (float): value for IDD Field `enthalpy_16`
                Unit: J/kg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `enthalpy_16`'.format(value))

        self._data["Enthalpy 16"] = value

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
        out.append(self._to_str(self.temperature_coefficient_for_thermal_conductivity))
        out.append(self._to_str(self.temperature_1))
        out.append(self._to_str(self.enthalpy_1))
        out.append(self._to_str(self.temperature_2))
        out.append(self._to_str(self.enthalpy_2))
        out.append(self._to_str(self.temperature_3))
        out.append(self._to_str(self.enthalpy_3))
        out.append(self._to_str(self.temperature_4))
        out.append(self._to_str(self.enthalpy_4))
        out.append(self._to_str(self.temperature_5))
        out.append(self._to_str(self.enthalpy_5))
        out.append(self._to_str(self.temperature_6))
        out.append(self._to_str(self.enthalpy_6))
        out.append(self._to_str(self.temperature_7))
        out.append(self._to_str(self.enthalpy_7))
        out.append(self._to_str(self.temperature_8))
        out.append(self._to_str(self.enthalpy_8))
        out.append(self._to_str(self.temperature_9))
        out.append(self._to_str(self.enthalpy_9))
        out.append(self._to_str(self.temperature_10))
        out.append(self._to_str(self.enthalpy_10))
        out.append(self._to_str(self.temperature_11))
        out.append(self._to_str(self.enthalpy_11))
        out.append(self._to_str(self.temperature_12))
        out.append(self._to_str(self.enthalpy_12))
        out.append(self._to_str(self.temperature_13))
        out.append(self._to_str(self.enthalpy_13))
        out.append(self._to_str(self.temperature_14))
        out.append(self._to_str(self.enthalpy_14))
        out.append(self._to_str(self.temperature_15))
        out.append(self._to_str(self.enthalpy_15))
        out.append(self._to_str(self.temperature_16))
        out.append(self._to_str(self.enthalpy_16))
        return ",".join(out)

class MaterialPropertyVariableThermalConductivity(object):
    """ Corresponds to IDD object `MaterialProperty:VariableThermalConductivity`
        Additional properties for temperature dependent thermal conductivity
        using piecewise linear temperature-conductivity function.
        HeatBalanceAlgorithm = CondFD(ConductionFiniteDifference) solution algorithm only.
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    internal_name = "MaterialProperty:VariableThermalConductivity"
    field_count = 21

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `MaterialProperty:VariableThermalConductivity`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Temperature 1"] = None
        self._data["Thermal Conductivity 1"] = None
        self._data["Temperature 2"] = None
        self._data["Thermal Conductivity 2"] = None
        self._data["Temperature 3"] = None
        self._data["Thermal Conductivity 3"] = None
        self._data["Temperature 4"] = None
        self._data["Thermal Conductivity 4"] = None
        self._data["Temperature 5"] = None
        self._data["Thermal Conductivity 5"] = None
        self._data["Temperature 6"] = None
        self._data["Thermal Conductivity 6"] = None
        self._data["Temperature 7"] = None
        self._data["Thermal Conductivity 7"] = None
        self._data["Temperature 8"] = None
        self._data["Thermal Conductivity 8"] = None
        self._data["Temperature 9"] = None
        self._data["Thermal Conductivity 9"] = None
        self._data["Temperature 10"] = None
        self._data["Thermal Conductivity 10"] = None

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
            self.temperature_1 = None
        else:
            self.temperature_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_1 = None
        else:
            self.thermal_conductivity_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_2 = None
        else:
            self.temperature_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_2 = None
        else:
            self.thermal_conductivity_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_3 = None
        else:
            self.temperature_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_3 = None
        else:
            self.thermal_conductivity_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_4 = None
        else:
            self.temperature_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_4 = None
        else:
            self.thermal_conductivity_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_5 = None
        else:
            self.temperature_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_5 = None
        else:
            self.thermal_conductivity_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_6 = None
        else:
            self.temperature_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_6 = None
        else:
            self.thermal_conductivity_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_7 = None
        else:
            self.temperature_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_7 = None
        else:
            self.thermal_conductivity_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_8 = None
        else:
            self.temperature_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_8 = None
        else:
            self.thermal_conductivity_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_9 = None
        else:
            self.temperature_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_9 = None
        else:
            self.thermal_conductivity_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_10 = None
        else:
            self.temperature_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_10 = None
        else:
            self.thermal_conductivity_10 = vals[i]
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
        Regular Material Name to which the additional properties will be added.
        this the material name for the basic material properties.

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
    def temperature_1(self):
        """Get temperature_1

        Returns:
            float: the value of `temperature_1` or None if not set
        """
        return self._data["Temperature 1"]

    @temperature_1.setter
    def temperature_1(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_1`
        for Temperature-Thermal Conductivity function

        Args:
            value (float): value for IDD Field `temperature_1`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_1`'.format(value))

        self._data["Temperature 1"] = value

    @property
    def thermal_conductivity_1(self):
        """Get thermal_conductivity_1

        Returns:
            float: the value of `thermal_conductivity_1` or None if not set
        """
        return self._data["Thermal Conductivity 1"]

    @thermal_conductivity_1.setter
    def thermal_conductivity_1(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_conductivity_1`
        for Temperature-Thermal Conductivity function corresponding to temperature 1

        Args:
            value (float): value for IDD Field `thermal_conductivity_1`
                Unit: W/m-K
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_conductivity_1`'.format(value))

        self._data["Thermal Conductivity 1"] = value

    @property
    def temperature_2(self):
        """Get temperature_2

        Returns:
            float: the value of `temperature_2` or None if not set
        """
        return self._data["Temperature 2"]

    @temperature_2.setter
    def temperature_2(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_2`
        for Temperature-Thermal Conductivity function

        Args:
            value (float): value for IDD Field `temperature_2`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_2`'.format(value))

        self._data["Temperature 2"] = value

    @property
    def thermal_conductivity_2(self):
        """Get thermal_conductivity_2

        Returns:
            float: the value of `thermal_conductivity_2` or None if not set
        """
        return self._data["Thermal Conductivity 2"]

    @thermal_conductivity_2.setter
    def thermal_conductivity_2(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_conductivity_2`
        for Temperature-Thermal Conductivity function corresponding to temperature 2

        Args:
            value (float): value for IDD Field `thermal_conductivity_2`
                Unit: W/m-K
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_conductivity_2`'.format(value))

        self._data["Thermal Conductivity 2"] = value

    @property
    def temperature_3(self):
        """Get temperature_3

        Returns:
            float: the value of `temperature_3` or None if not set
        """
        return self._data["Temperature 3"]

    @temperature_3.setter
    def temperature_3(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_3`
        for Temperature-Thermal Conductivity function

        Args:
            value (float): value for IDD Field `temperature_3`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_3`'.format(value))

        self._data["Temperature 3"] = value

    @property
    def thermal_conductivity_3(self):
        """Get thermal_conductivity_3

        Returns:
            float: the value of `thermal_conductivity_3` or None if not set
        """
        return self._data["Thermal Conductivity 3"]

    @thermal_conductivity_3.setter
    def thermal_conductivity_3(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_conductivity_3`
        for Temperature-Thermal Conductivity function corresponding to temperature 3

        Args:
            value (float): value for IDD Field `thermal_conductivity_3`
                Unit: W/m-K
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_conductivity_3`'.format(value))

        self._data["Thermal Conductivity 3"] = value

    @property
    def temperature_4(self):
        """Get temperature_4

        Returns:
            float: the value of `temperature_4` or None if not set
        """
        return self._data["Temperature 4"]

    @temperature_4.setter
    def temperature_4(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_4`
        for Temperature-Thermal Conductivity function

        Args:
            value (float): value for IDD Field `temperature_4`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_4`'.format(value))

        self._data["Temperature 4"] = value

    @property
    def thermal_conductivity_4(self):
        """Get thermal_conductivity_4

        Returns:
            float: the value of `thermal_conductivity_4` or None if not set
        """
        return self._data["Thermal Conductivity 4"]

    @thermal_conductivity_4.setter
    def thermal_conductivity_4(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_conductivity_4`
        for Temperature-Thermal Conductivity function corresponding to temperature 4

        Args:
            value (float): value for IDD Field `thermal_conductivity_4`
                Unit: W/m-K
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_conductivity_4`'.format(value))

        self._data["Thermal Conductivity 4"] = value

    @property
    def temperature_5(self):
        """Get temperature_5

        Returns:
            float: the value of `temperature_5` or None if not set
        """
        return self._data["Temperature 5"]

    @temperature_5.setter
    def temperature_5(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_5`
        for Temperature-Thermal Conductivity function

        Args:
            value (float): value for IDD Field `temperature_5`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_5`'.format(value))

        self._data["Temperature 5"] = value

    @property
    def thermal_conductivity_5(self):
        """Get thermal_conductivity_5

        Returns:
            float: the value of `thermal_conductivity_5` or None if not set
        """
        return self._data["Thermal Conductivity 5"]

    @thermal_conductivity_5.setter
    def thermal_conductivity_5(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_conductivity_5`
        for Temperature-Thermal Conductivity function corresponding to temperature 5

        Args:
            value (float): value for IDD Field `thermal_conductivity_5`
                Unit: W/m-K
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_conductivity_5`'.format(value))

        self._data["Thermal Conductivity 5"] = value

    @property
    def temperature_6(self):
        """Get temperature_6

        Returns:
            float: the value of `temperature_6` or None if not set
        """
        return self._data["Temperature 6"]

    @temperature_6.setter
    def temperature_6(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_6`
        for Temperature-Thermal Conductivity function

        Args:
            value (float): value for IDD Field `temperature_6`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_6`'.format(value))

        self._data["Temperature 6"] = value

    @property
    def thermal_conductivity_6(self):
        """Get thermal_conductivity_6

        Returns:
            float: the value of `thermal_conductivity_6` or None if not set
        """
        return self._data["Thermal Conductivity 6"]

    @thermal_conductivity_6.setter
    def thermal_conductivity_6(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_conductivity_6`
        for Temperature-Thermal Conductivity function corresponding to temperature 6

        Args:
            value (float): value for IDD Field `thermal_conductivity_6`
                Unit: W/m-K
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_conductivity_6`'.format(value))

        self._data["Thermal Conductivity 6"] = value

    @property
    def temperature_7(self):
        """Get temperature_7

        Returns:
            float: the value of `temperature_7` or None if not set
        """
        return self._data["Temperature 7"]

    @temperature_7.setter
    def temperature_7(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_7`
        for Temperature-Thermal Conductivity function

        Args:
            value (float): value for IDD Field `temperature_7`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_7`'.format(value))

        self._data["Temperature 7"] = value

    @property
    def thermal_conductivity_7(self):
        """Get thermal_conductivity_7

        Returns:
            float: the value of `thermal_conductivity_7` or None if not set
        """
        return self._data["Thermal Conductivity 7"]

    @thermal_conductivity_7.setter
    def thermal_conductivity_7(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_conductivity_7`
        for Temperature-Thermal Conductivity function corresponding to temperature 7

        Args:
            value (float): value for IDD Field `thermal_conductivity_7`
                Unit: W/m-K
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_conductivity_7`'.format(value))

        self._data["Thermal Conductivity 7"] = value

    @property
    def temperature_8(self):
        """Get temperature_8

        Returns:
            float: the value of `temperature_8` or None if not set
        """
        return self._data["Temperature 8"]

    @temperature_8.setter
    def temperature_8(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_8`
        for Temperature-Thermal Conductivity function

        Args:
            value (float): value for IDD Field `temperature_8`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_8`'.format(value))

        self._data["Temperature 8"] = value

    @property
    def thermal_conductivity_8(self):
        """Get thermal_conductivity_8

        Returns:
            float: the value of `thermal_conductivity_8` or None if not set
        """
        return self._data["Thermal Conductivity 8"]

    @thermal_conductivity_8.setter
    def thermal_conductivity_8(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_conductivity_8`
        for Temperature-Thermal Conductivity function corresponding to temperature 8

        Args:
            value (float): value for IDD Field `thermal_conductivity_8`
                Unit: W/m-K
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_conductivity_8`'.format(value))

        self._data["Thermal Conductivity 8"] = value

    @property
    def temperature_9(self):
        """Get temperature_9

        Returns:
            float: the value of `temperature_9` or None if not set
        """
        return self._data["Temperature 9"]

    @temperature_9.setter
    def temperature_9(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_9`
        for Temperature-Thermal Conductivity function

        Args:
            value (float): value for IDD Field `temperature_9`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_9`'.format(value))

        self._data["Temperature 9"] = value

    @property
    def thermal_conductivity_9(self):
        """Get thermal_conductivity_9

        Returns:
            float: the value of `thermal_conductivity_9` or None if not set
        """
        return self._data["Thermal Conductivity 9"]

    @thermal_conductivity_9.setter
    def thermal_conductivity_9(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_conductivity_9`
        for Temperature-Thermal Conductivity function corresponding to temperature 9

        Args:
            value (float): value for IDD Field `thermal_conductivity_9`
                Unit: W/m-K
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_conductivity_9`'.format(value))

        self._data["Thermal Conductivity 9"] = value

    @property
    def temperature_10(self):
        """Get temperature_10

        Returns:
            float: the value of `temperature_10` or None if not set
        """
        return self._data["Temperature 10"]

    @temperature_10.setter
    def temperature_10(self, value=0.0 ):
        """  Corresponds to IDD Field `temperature_10`
        for Temperature-Thermal Conductivity function

        Args:
            value (float): value for IDD Field `temperature_10`
                Unit: C
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_10`'.format(value))

        self._data["Temperature 10"] = value

    @property
    def thermal_conductivity_10(self):
        """Get thermal_conductivity_10

        Returns:
            float: the value of `thermal_conductivity_10` or None if not set
        """
        return self._data["Thermal Conductivity 10"]

    @thermal_conductivity_10.setter
    def thermal_conductivity_10(self, value=0.0 ):
        """  Corresponds to IDD Field `thermal_conductivity_10`
        for Temperature-Thermal Conductivity function corresponding to temperature 10

        Args:
            value (float): value for IDD Field `thermal_conductivity_10`
                Unit: W/m-K
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_conductivity_10`'.format(value))

        self._data["Thermal Conductivity 10"] = value

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
        out.append(self._to_str(self.temperature_1))
        out.append(self._to_str(self.thermal_conductivity_1))
        out.append(self._to_str(self.temperature_2))
        out.append(self._to_str(self.thermal_conductivity_2))
        out.append(self._to_str(self.temperature_3))
        out.append(self._to_str(self.thermal_conductivity_3))
        out.append(self._to_str(self.temperature_4))
        out.append(self._to_str(self.thermal_conductivity_4))
        out.append(self._to_str(self.temperature_5))
        out.append(self._to_str(self.thermal_conductivity_5))
        out.append(self._to_str(self.temperature_6))
        out.append(self._to_str(self.thermal_conductivity_6))
        out.append(self._to_str(self.temperature_7))
        out.append(self._to_str(self.thermal_conductivity_7))
        out.append(self._to_str(self.temperature_8))
        out.append(self._to_str(self.thermal_conductivity_8))
        out.append(self._to_str(self.temperature_9))
        out.append(self._to_str(self.thermal_conductivity_9))
        out.append(self._to_str(self.temperature_10))
        out.append(self._to_str(self.thermal_conductivity_10))
        return ",".join(out)

class MaterialPropertyHeatAndMoistureTransferSettings(object):
    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:Settings`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Additional material properties for surfaces.
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    internal_name = "MaterialProperty:HeatAndMoistureTransfer:Settings"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `MaterialProperty:HeatAndMoistureTransfer:Settings`
        """
        self._data = OrderedDict()
        self._data["Material Name"] = None
        self._data["Porosity"] = None
        self._data["Initial Water Content Ratio"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.material_name = None
        else:
            self.material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.porosity = None
        else:
            self.porosity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_water_content_ratio = None
        else:
            self.initial_water_content_ratio = vals[i]
        i += 1

    @property
    def material_name(self):
        """Get material_name

        Returns:
            str: the value of `material_name` or None if not set
        """
        return self._data["Material Name"]

    @material_name.setter
    def material_name(self, value=None):
        """  Corresponds to IDD Field `material_name`
        Material Name that the moisture properties will be added to.
        This augments material properties needed for combined heat and moisture transfer for surfaces.

        Args:
            value (str): value for IDD Field `material_name`
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
                                 'for field `material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `material_name`')

        self._data["Material Name"] = value

    @property
    def porosity(self):
        """Get porosity

        Returns:
            float: the value of `porosity` or None if not set
        """
        return self._data["Porosity"]

    @porosity.setter
    def porosity(self, value=None):
        """  Corresponds to IDD Field `porosity`

        Args:
            value (float): value for IDD Field `porosity`
                Unit: m3/m3
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
                                 'for field `porosity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `porosity`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `porosity`')

        self._data["Porosity"] = value

    @property
    def initial_water_content_ratio(self):
        """Get initial_water_content_ratio

        Returns:
            float: the value of `initial_water_content_ratio` or None if not set
        """
        return self._data["Initial Water Content Ratio"]

    @initial_water_content_ratio.setter
    def initial_water_content_ratio(self, value=0.2 ):
        """  Corresponds to IDD Field `initial_water_content_ratio`
        units are the water/material density ratio at the begining of each run period.

        Args:
            value (float): value for IDD Field `initial_water_content_ratio`
                Unit: kg/kg
                Default value: 0.2
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
                                 'for field `initial_water_content_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `initial_water_content_ratio`')

        self._data["Initial Water Content Ratio"] = value

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
        out.append(self._to_str(self.material_name))
        out.append(self._to_str(self.porosity))
        out.append(self._to_str(self.initial_water_content_ratio))
        return ",".join(out)

class MaterialPropertyHeatAndMoistureTransferSorptionIsotherm(object):
    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Relationship between moisture content and relative humidity fraction.
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    internal_name = "MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm"
    field_count = 52

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm`
        """
        self._data = OrderedDict()
        self._data["Material Name"] = None
        self._data["Number of Isotherm Coordinates"] = None
        self._data["Relative Humidity Fraction 1"] = None
        self._data["Moisture Content 1"] = None
        self._data["Relative Humidity Fraction 2"] = None
        self._data["Moisture Content 2"] = None
        self._data["Relative Humidity Fraction 3"] = None
        self._data["Moisture Content 3"] = None
        self._data["Relative Humidity Fraction 4"] = None
        self._data["Moisture Content 4"] = None
        self._data["Relative Humidity Fraction 5"] = None
        self._data["Moisture Content 5"] = None
        self._data["Relative Humidity Fraction 6"] = None
        self._data["Moisture Content 6"] = None
        self._data["Relative Humidity Fraction 7"] = None
        self._data["Moisture Content 7"] = None
        self._data["Relative Humidity Fraction 8"] = None
        self._data["Moisture Content 8"] = None
        self._data["Relative Humidity Fraction 9"] = None
        self._data["Moisture Content 9"] = None
        self._data["Relative Humidity Fraction 10"] = None
        self._data["Moisture Content 10"] = None
        self._data["Relative Humidity Fraction 11"] = None
        self._data["Moisture Content 11"] = None
        self._data["Relative Humidity Fraction 12"] = None
        self._data["Moisture Content 12"] = None
        self._data["Relative Humidity Fraction 13"] = None
        self._data["Moisture Content 13"] = None
        self._data["Relative Humidity Fraction 14"] = None
        self._data["Moisture Content 14"] = None
        self._data["Relative Humidity Fraction 15"] = None
        self._data["Moisture Content 15"] = None
        self._data["Relative Humidity Fraction 16"] = None
        self._data["Moisture Content 16"] = None
        self._data["Relative Humidity Fraction 17"] = None
        self._data["Moisture Content 17"] = None
        self._data["Relative Humidity Fraction 18"] = None
        self._data["Moisture Content 18"] = None
        self._data["Relative Humidity Fraction 19"] = None
        self._data["Moisture Content 19"] = None
        self._data["Relative Humidity Fraction 20"] = None
        self._data["Moisture Content 20"] = None
        self._data["Relative Humidity Fraction 21"] = None
        self._data["Moisture Content 21"] = None
        self._data["Relative Humidity Fraction 22"] = None
        self._data["Moisture Content 22"] = None
        self._data["Relative Humidity Fraction 23"] = None
        self._data["Moisture Content 23"] = None
        self._data["Relative Humidity Fraction 24"] = None
        self._data["Moisture Content 24"] = None
        self._data["Relative Humidity Fraction 25"] = None
        self._data["Moisture Content 25"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.material_name = None
        else:
            self.material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_isotherm_coordinates = None
        else:
            self.number_of_isotherm_coordinates = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_1 = None
        else:
            self.relative_humidity_fraction_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_1 = None
        else:
            self.moisture_content_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_2 = None
        else:
            self.relative_humidity_fraction_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_2 = None
        else:
            self.moisture_content_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_3 = None
        else:
            self.relative_humidity_fraction_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_3 = None
        else:
            self.moisture_content_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_4 = None
        else:
            self.relative_humidity_fraction_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_4 = None
        else:
            self.moisture_content_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_5 = None
        else:
            self.relative_humidity_fraction_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_5 = None
        else:
            self.moisture_content_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_6 = None
        else:
            self.relative_humidity_fraction_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_6 = None
        else:
            self.moisture_content_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_7 = None
        else:
            self.relative_humidity_fraction_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_7 = None
        else:
            self.moisture_content_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_8 = None
        else:
            self.relative_humidity_fraction_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_8 = None
        else:
            self.moisture_content_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_9 = None
        else:
            self.relative_humidity_fraction_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_9 = None
        else:
            self.moisture_content_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_10 = None
        else:
            self.relative_humidity_fraction_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_10 = None
        else:
            self.moisture_content_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_11 = None
        else:
            self.relative_humidity_fraction_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_11 = None
        else:
            self.moisture_content_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_12 = None
        else:
            self.relative_humidity_fraction_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_12 = None
        else:
            self.moisture_content_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_13 = None
        else:
            self.relative_humidity_fraction_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_13 = None
        else:
            self.moisture_content_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_14 = None
        else:
            self.relative_humidity_fraction_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_14 = None
        else:
            self.moisture_content_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_15 = None
        else:
            self.relative_humidity_fraction_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_15 = None
        else:
            self.moisture_content_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_16 = None
        else:
            self.relative_humidity_fraction_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_16 = None
        else:
            self.moisture_content_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_17 = None
        else:
            self.relative_humidity_fraction_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_17 = None
        else:
            self.moisture_content_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_18 = None
        else:
            self.relative_humidity_fraction_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_18 = None
        else:
            self.moisture_content_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_19 = None
        else:
            self.relative_humidity_fraction_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_19 = None
        else:
            self.moisture_content_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_20 = None
        else:
            self.relative_humidity_fraction_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_20 = None
        else:
            self.moisture_content_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_21 = None
        else:
            self.relative_humidity_fraction_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_21 = None
        else:
            self.moisture_content_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_22 = None
        else:
            self.relative_humidity_fraction_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_22 = None
        else:
            self.moisture_content_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_23 = None
        else:
            self.relative_humidity_fraction_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_23 = None
        else:
            self.moisture_content_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_24 = None
        else:
            self.relative_humidity_fraction_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_24 = None
        else:
            self.moisture_content_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_25 = None
        else:
            self.relative_humidity_fraction_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_25 = None
        else:
            self.moisture_content_25 = vals[i]
        i += 1

    @property
    def material_name(self):
        """Get material_name

        Returns:
            str: the value of `material_name` or None if not set
        """
        return self._data["Material Name"]

    @material_name.setter
    def material_name(self, value=None):
        """  Corresponds to IDD Field `material_name`
        The Material Name that the moisture sorption isotherm will be added to.

        Args:
            value (str): value for IDD Field `material_name`
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
                                 'for field `material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `material_name`')

        self._data["Material Name"] = value

    @property
    def number_of_isotherm_coordinates(self):
        """Get number_of_isotherm_coordinates

        Returns:
            int: the value of `number_of_isotherm_coordinates` or None if not set
        """
        return self._data["Number of Isotherm Coordinates"]

    @number_of_isotherm_coordinates.setter
    def number_of_isotherm_coordinates(self, value=None):
        """  Corresponds to IDD Field `number_of_isotherm_coordinates`
        Number of data Coordinates

        Args:
            value (int): value for IDD Field `number_of_isotherm_coordinates`
                value >= 1
                value <= 25
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
                                 'for field `number_of_isotherm_coordinates`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_isotherm_coordinates`')
            if value > 25:
                raise ValueError('value need to be smaller 25 '
                                 'for field `number_of_isotherm_coordinates`')

        self._data["Number of Isotherm Coordinates"] = value

    @property
    def relative_humidity_fraction_1(self):
        """Get relative_humidity_fraction_1

        Returns:
            float: the value of `relative_humidity_fraction_1` or None if not set
        """
        return self._data["Relative Humidity Fraction 1"]

    @relative_humidity_fraction_1.setter
    def relative_humidity_fraction_1(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_1`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_1`
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
                                 'for field `relative_humidity_fraction_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_1`')

        self._data["Relative Humidity Fraction 1"] = value

    @property
    def moisture_content_1(self):
        """Get moisture_content_1

        Returns:
            float: the value of `moisture_content_1` or None if not set
        """
        return self._data["Moisture Content 1"]

    @moisture_content_1.setter
    def moisture_content_1(self, value=None):
        """  Corresponds to IDD Field `moisture_content_1`

        Args:
            value (float): value for IDD Field `moisture_content_1`
                Unit: kg/m3
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
                                 'for field `moisture_content_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_1`')

        self._data["Moisture Content 1"] = value

    @property
    def relative_humidity_fraction_2(self):
        """Get relative_humidity_fraction_2

        Returns:
            float: the value of `relative_humidity_fraction_2` or None if not set
        """
        return self._data["Relative Humidity Fraction 2"]

    @relative_humidity_fraction_2.setter
    def relative_humidity_fraction_2(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_2`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_2`
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
                                 'for field `relative_humidity_fraction_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_2`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_2`')

        self._data["Relative Humidity Fraction 2"] = value

    @property
    def moisture_content_2(self):
        """Get moisture_content_2

        Returns:
            float: the value of `moisture_content_2` or None if not set
        """
        return self._data["Moisture Content 2"]

    @moisture_content_2.setter
    def moisture_content_2(self, value=None):
        """  Corresponds to IDD Field `moisture_content_2`

        Args:
            value (float): value for IDD Field `moisture_content_2`
                Unit: kg/m3
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
                                 'for field `moisture_content_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_2`')

        self._data["Moisture Content 2"] = value

    @property
    def relative_humidity_fraction_3(self):
        """Get relative_humidity_fraction_3

        Returns:
            float: the value of `relative_humidity_fraction_3` or None if not set
        """
        return self._data["Relative Humidity Fraction 3"]

    @relative_humidity_fraction_3.setter
    def relative_humidity_fraction_3(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_3`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_3`
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
                                 'for field `relative_humidity_fraction_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_3`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_3`')

        self._data["Relative Humidity Fraction 3"] = value

    @property
    def moisture_content_3(self):
        """Get moisture_content_3

        Returns:
            float: the value of `moisture_content_3` or None if not set
        """
        return self._data["Moisture Content 3"]

    @moisture_content_3.setter
    def moisture_content_3(self, value=None):
        """  Corresponds to IDD Field `moisture_content_3`

        Args:
            value (float): value for IDD Field `moisture_content_3`
                Unit: kg/m3
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
                                 'for field `moisture_content_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_3`')

        self._data["Moisture Content 3"] = value

    @property
    def relative_humidity_fraction_4(self):
        """Get relative_humidity_fraction_4

        Returns:
            float: the value of `relative_humidity_fraction_4` or None if not set
        """
        return self._data["Relative Humidity Fraction 4"]

    @relative_humidity_fraction_4.setter
    def relative_humidity_fraction_4(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_4`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_4`
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
                                 'for field `relative_humidity_fraction_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_4`')

        self._data["Relative Humidity Fraction 4"] = value

    @property
    def moisture_content_4(self):
        """Get moisture_content_4

        Returns:
            float: the value of `moisture_content_4` or None if not set
        """
        return self._data["Moisture Content 4"]

    @moisture_content_4.setter
    def moisture_content_4(self, value=None):
        """  Corresponds to IDD Field `moisture_content_4`

        Args:
            value (float): value for IDD Field `moisture_content_4`
                Unit: kg/m3
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
                                 'for field `moisture_content_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_4`')

        self._data["Moisture Content 4"] = value

    @property
    def relative_humidity_fraction_5(self):
        """Get relative_humidity_fraction_5

        Returns:
            float: the value of `relative_humidity_fraction_5` or None if not set
        """
        return self._data["Relative Humidity Fraction 5"]

    @relative_humidity_fraction_5.setter
    def relative_humidity_fraction_5(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_5`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_5`
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
                                 'for field `relative_humidity_fraction_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_5`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_5`')

        self._data["Relative Humidity Fraction 5"] = value

    @property
    def moisture_content_5(self):
        """Get moisture_content_5

        Returns:
            float: the value of `moisture_content_5` or None if not set
        """
        return self._data["Moisture Content 5"]

    @moisture_content_5.setter
    def moisture_content_5(self, value=None):
        """  Corresponds to IDD Field `moisture_content_5`

        Args:
            value (float): value for IDD Field `moisture_content_5`
                Unit: kg/m3
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
                                 'for field `moisture_content_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_5`')

        self._data["Moisture Content 5"] = value

    @property
    def relative_humidity_fraction_6(self):
        """Get relative_humidity_fraction_6

        Returns:
            float: the value of `relative_humidity_fraction_6` or None if not set
        """
        return self._data["Relative Humidity Fraction 6"]

    @relative_humidity_fraction_6.setter
    def relative_humidity_fraction_6(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_6`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_6`
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
                                 'for field `relative_humidity_fraction_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_6`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_6`')

        self._data["Relative Humidity Fraction 6"] = value

    @property
    def moisture_content_6(self):
        """Get moisture_content_6

        Returns:
            float: the value of `moisture_content_6` or None if not set
        """
        return self._data["Moisture Content 6"]

    @moisture_content_6.setter
    def moisture_content_6(self, value=None):
        """  Corresponds to IDD Field `moisture_content_6`

        Args:
            value (float): value for IDD Field `moisture_content_6`
                Unit: kg/m3
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
                                 'for field `moisture_content_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_6`')

        self._data["Moisture Content 6"] = value

    @property
    def relative_humidity_fraction_7(self):
        """Get relative_humidity_fraction_7

        Returns:
            float: the value of `relative_humidity_fraction_7` or None if not set
        """
        return self._data["Relative Humidity Fraction 7"]

    @relative_humidity_fraction_7.setter
    def relative_humidity_fraction_7(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_7`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_7`
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
                                 'for field `relative_humidity_fraction_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_7`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_7`')

        self._data["Relative Humidity Fraction 7"] = value

    @property
    def moisture_content_7(self):
        """Get moisture_content_7

        Returns:
            float: the value of `moisture_content_7` or None if not set
        """
        return self._data["Moisture Content 7"]

    @moisture_content_7.setter
    def moisture_content_7(self, value=None):
        """  Corresponds to IDD Field `moisture_content_7`

        Args:
            value (float): value for IDD Field `moisture_content_7`
                Unit: kg/m3
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
                                 'for field `moisture_content_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_7`')

        self._data["Moisture Content 7"] = value

    @property
    def relative_humidity_fraction_8(self):
        """Get relative_humidity_fraction_8

        Returns:
            float: the value of `relative_humidity_fraction_8` or None if not set
        """
        return self._data["Relative Humidity Fraction 8"]

    @relative_humidity_fraction_8.setter
    def relative_humidity_fraction_8(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_8`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_8`
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
                                 'for field `relative_humidity_fraction_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_8`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_8`')

        self._data["Relative Humidity Fraction 8"] = value

    @property
    def moisture_content_8(self):
        """Get moisture_content_8

        Returns:
            float: the value of `moisture_content_8` or None if not set
        """
        return self._data["Moisture Content 8"]

    @moisture_content_8.setter
    def moisture_content_8(self, value=None):
        """  Corresponds to IDD Field `moisture_content_8`

        Args:
            value (float): value for IDD Field `moisture_content_8`
                Unit: kg/m3
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
                                 'for field `moisture_content_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_8`')

        self._data["Moisture Content 8"] = value

    @property
    def relative_humidity_fraction_9(self):
        """Get relative_humidity_fraction_9

        Returns:
            float: the value of `relative_humidity_fraction_9` or None if not set
        """
        return self._data["Relative Humidity Fraction 9"]

    @relative_humidity_fraction_9.setter
    def relative_humidity_fraction_9(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_9`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_9`
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
                                 'for field `relative_humidity_fraction_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_9`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_9`')

        self._data["Relative Humidity Fraction 9"] = value

    @property
    def moisture_content_9(self):
        """Get moisture_content_9

        Returns:
            float: the value of `moisture_content_9` or None if not set
        """
        return self._data["Moisture Content 9"]

    @moisture_content_9.setter
    def moisture_content_9(self, value=None):
        """  Corresponds to IDD Field `moisture_content_9`

        Args:
            value (float): value for IDD Field `moisture_content_9`
                Unit: kg/m3
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
                                 'for field `moisture_content_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_9`')

        self._data["Moisture Content 9"] = value

    @property
    def relative_humidity_fraction_10(self):
        """Get relative_humidity_fraction_10

        Returns:
            float: the value of `relative_humidity_fraction_10` or None if not set
        """
        return self._data["Relative Humidity Fraction 10"]

    @relative_humidity_fraction_10.setter
    def relative_humidity_fraction_10(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_10`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_10`
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
                                 'for field `relative_humidity_fraction_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_10`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_10`')

        self._data["Relative Humidity Fraction 10"] = value

    @property
    def moisture_content_10(self):
        """Get moisture_content_10

        Returns:
            float: the value of `moisture_content_10` or None if not set
        """
        return self._data["Moisture Content 10"]

    @moisture_content_10.setter
    def moisture_content_10(self, value=None):
        """  Corresponds to IDD Field `moisture_content_10`

        Args:
            value (float): value for IDD Field `moisture_content_10`
                Unit: kg/m3
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
                                 'for field `moisture_content_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_10`')

        self._data["Moisture Content 10"] = value

    @property
    def relative_humidity_fraction_11(self):
        """Get relative_humidity_fraction_11

        Returns:
            float: the value of `relative_humidity_fraction_11` or None if not set
        """
        return self._data["Relative Humidity Fraction 11"]

    @relative_humidity_fraction_11.setter
    def relative_humidity_fraction_11(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_11`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_11`
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
                                 'for field `relative_humidity_fraction_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_11`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_11`')

        self._data["Relative Humidity Fraction 11"] = value

    @property
    def moisture_content_11(self):
        """Get moisture_content_11

        Returns:
            float: the value of `moisture_content_11` or None if not set
        """
        return self._data["Moisture Content 11"]

    @moisture_content_11.setter
    def moisture_content_11(self, value=None):
        """  Corresponds to IDD Field `moisture_content_11`

        Args:
            value (float): value for IDD Field `moisture_content_11`
                Unit: kg/m3
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
                                 'for field `moisture_content_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_11`')

        self._data["Moisture Content 11"] = value

    @property
    def relative_humidity_fraction_12(self):
        """Get relative_humidity_fraction_12

        Returns:
            float: the value of `relative_humidity_fraction_12` or None if not set
        """
        return self._data["Relative Humidity Fraction 12"]

    @relative_humidity_fraction_12.setter
    def relative_humidity_fraction_12(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_12`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_12`
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
                                 'for field `relative_humidity_fraction_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_12`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_12`')

        self._data["Relative Humidity Fraction 12"] = value

    @property
    def moisture_content_12(self):
        """Get moisture_content_12

        Returns:
            float: the value of `moisture_content_12` or None if not set
        """
        return self._data["Moisture Content 12"]

    @moisture_content_12.setter
    def moisture_content_12(self, value=None):
        """  Corresponds to IDD Field `moisture_content_12`

        Args:
            value (float): value for IDD Field `moisture_content_12`
                Unit: kg/m3
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
                                 'for field `moisture_content_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_12`')

        self._data["Moisture Content 12"] = value

    @property
    def relative_humidity_fraction_13(self):
        """Get relative_humidity_fraction_13

        Returns:
            float: the value of `relative_humidity_fraction_13` or None if not set
        """
        return self._data["Relative Humidity Fraction 13"]

    @relative_humidity_fraction_13.setter
    def relative_humidity_fraction_13(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_13`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_13`
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
                                 'for field `relative_humidity_fraction_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_13`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_13`')

        self._data["Relative Humidity Fraction 13"] = value

    @property
    def moisture_content_13(self):
        """Get moisture_content_13

        Returns:
            float: the value of `moisture_content_13` or None if not set
        """
        return self._data["Moisture Content 13"]

    @moisture_content_13.setter
    def moisture_content_13(self, value=None):
        """  Corresponds to IDD Field `moisture_content_13`

        Args:
            value (float): value for IDD Field `moisture_content_13`
                Unit: kg/m3
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
                                 'for field `moisture_content_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_13`')

        self._data["Moisture Content 13"] = value

    @property
    def relative_humidity_fraction_14(self):
        """Get relative_humidity_fraction_14

        Returns:
            float: the value of `relative_humidity_fraction_14` or None if not set
        """
        return self._data["Relative Humidity Fraction 14"]

    @relative_humidity_fraction_14.setter
    def relative_humidity_fraction_14(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_14`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_14`
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
                                 'for field `relative_humidity_fraction_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_14`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_14`')

        self._data["Relative Humidity Fraction 14"] = value

    @property
    def moisture_content_14(self):
        """Get moisture_content_14

        Returns:
            float: the value of `moisture_content_14` or None if not set
        """
        return self._data["Moisture Content 14"]

    @moisture_content_14.setter
    def moisture_content_14(self, value=None):
        """  Corresponds to IDD Field `moisture_content_14`

        Args:
            value (float): value for IDD Field `moisture_content_14`
                Unit: kg/m3
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
                                 'for field `moisture_content_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_14`')

        self._data["Moisture Content 14"] = value

    @property
    def relative_humidity_fraction_15(self):
        """Get relative_humidity_fraction_15

        Returns:
            float: the value of `relative_humidity_fraction_15` or None if not set
        """
        return self._data["Relative Humidity Fraction 15"]

    @relative_humidity_fraction_15.setter
    def relative_humidity_fraction_15(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_15`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_15`
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
                                 'for field `relative_humidity_fraction_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_15`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_15`')

        self._data["Relative Humidity Fraction 15"] = value

    @property
    def moisture_content_15(self):
        """Get moisture_content_15

        Returns:
            float: the value of `moisture_content_15` or None if not set
        """
        return self._data["Moisture Content 15"]

    @moisture_content_15.setter
    def moisture_content_15(self, value=None):
        """  Corresponds to IDD Field `moisture_content_15`

        Args:
            value (float): value for IDD Field `moisture_content_15`
                Unit: kg/m3
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
                                 'for field `moisture_content_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_15`')

        self._data["Moisture Content 15"] = value

    @property
    def relative_humidity_fraction_16(self):
        """Get relative_humidity_fraction_16

        Returns:
            float: the value of `relative_humidity_fraction_16` or None if not set
        """
        return self._data["Relative Humidity Fraction 16"]

    @relative_humidity_fraction_16.setter
    def relative_humidity_fraction_16(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_16`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_16`
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
                                 'for field `relative_humidity_fraction_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_16`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_16`')

        self._data["Relative Humidity Fraction 16"] = value

    @property
    def moisture_content_16(self):
        """Get moisture_content_16

        Returns:
            float: the value of `moisture_content_16` or None if not set
        """
        return self._data["Moisture Content 16"]

    @moisture_content_16.setter
    def moisture_content_16(self, value=None):
        """  Corresponds to IDD Field `moisture_content_16`

        Args:
            value (float): value for IDD Field `moisture_content_16`
                Unit: kg/m3
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
                                 'for field `moisture_content_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_16`')

        self._data["Moisture Content 16"] = value

    @property
    def relative_humidity_fraction_17(self):
        """Get relative_humidity_fraction_17

        Returns:
            float: the value of `relative_humidity_fraction_17` or None if not set
        """
        return self._data["Relative Humidity Fraction 17"]

    @relative_humidity_fraction_17.setter
    def relative_humidity_fraction_17(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_17`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_17`
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
                                 'for field `relative_humidity_fraction_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_17`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_17`')

        self._data["Relative Humidity Fraction 17"] = value

    @property
    def moisture_content_17(self):
        """Get moisture_content_17

        Returns:
            float: the value of `moisture_content_17` or None if not set
        """
        return self._data["Moisture Content 17"]

    @moisture_content_17.setter
    def moisture_content_17(self, value=None):
        """  Corresponds to IDD Field `moisture_content_17`

        Args:
            value (float): value for IDD Field `moisture_content_17`
                Unit: kg/m3
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
                                 'for field `moisture_content_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_17`')

        self._data["Moisture Content 17"] = value

    @property
    def relative_humidity_fraction_18(self):
        """Get relative_humidity_fraction_18

        Returns:
            float: the value of `relative_humidity_fraction_18` or None if not set
        """
        return self._data["Relative Humidity Fraction 18"]

    @relative_humidity_fraction_18.setter
    def relative_humidity_fraction_18(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_18`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_18`
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
                                 'for field `relative_humidity_fraction_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_18`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_18`')

        self._data["Relative Humidity Fraction 18"] = value

    @property
    def moisture_content_18(self):
        """Get moisture_content_18

        Returns:
            float: the value of `moisture_content_18` or None if not set
        """
        return self._data["Moisture Content 18"]

    @moisture_content_18.setter
    def moisture_content_18(self, value=None):
        """  Corresponds to IDD Field `moisture_content_18`

        Args:
            value (float): value for IDD Field `moisture_content_18`
                Unit: kg/m3
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
                                 'for field `moisture_content_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_18`')

        self._data["Moisture Content 18"] = value

    @property
    def relative_humidity_fraction_19(self):
        """Get relative_humidity_fraction_19

        Returns:
            float: the value of `relative_humidity_fraction_19` or None if not set
        """
        return self._data["Relative Humidity Fraction 19"]

    @relative_humidity_fraction_19.setter
    def relative_humidity_fraction_19(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_19`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_19`
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
                                 'for field `relative_humidity_fraction_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_19`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_19`')

        self._data["Relative Humidity Fraction 19"] = value

    @property
    def moisture_content_19(self):
        """Get moisture_content_19

        Returns:
            float: the value of `moisture_content_19` or None if not set
        """
        return self._data["Moisture Content 19"]

    @moisture_content_19.setter
    def moisture_content_19(self, value=None):
        """  Corresponds to IDD Field `moisture_content_19`

        Args:
            value (float): value for IDD Field `moisture_content_19`
                Unit: kg/m3
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
                                 'for field `moisture_content_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_19`')

        self._data["Moisture Content 19"] = value

    @property
    def relative_humidity_fraction_20(self):
        """Get relative_humidity_fraction_20

        Returns:
            float: the value of `relative_humidity_fraction_20` or None if not set
        """
        return self._data["Relative Humidity Fraction 20"]

    @relative_humidity_fraction_20.setter
    def relative_humidity_fraction_20(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_20`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_20`
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
                                 'for field `relative_humidity_fraction_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_20`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_20`')

        self._data["Relative Humidity Fraction 20"] = value

    @property
    def moisture_content_20(self):
        """Get moisture_content_20

        Returns:
            float: the value of `moisture_content_20` or None if not set
        """
        return self._data["Moisture Content 20"]

    @moisture_content_20.setter
    def moisture_content_20(self, value=None):
        """  Corresponds to IDD Field `moisture_content_20`

        Args:
            value (float): value for IDD Field `moisture_content_20`
                Unit: kg/m3
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
                                 'for field `moisture_content_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_20`')

        self._data["Moisture Content 20"] = value

    @property
    def relative_humidity_fraction_21(self):
        """Get relative_humidity_fraction_21

        Returns:
            float: the value of `relative_humidity_fraction_21` or None if not set
        """
        return self._data["Relative Humidity Fraction 21"]

    @relative_humidity_fraction_21.setter
    def relative_humidity_fraction_21(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_21`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_21`
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
                                 'for field `relative_humidity_fraction_21`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_21`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_21`')

        self._data["Relative Humidity Fraction 21"] = value

    @property
    def moisture_content_21(self):
        """Get moisture_content_21

        Returns:
            float: the value of `moisture_content_21` or None if not set
        """
        return self._data["Moisture Content 21"]

    @moisture_content_21.setter
    def moisture_content_21(self, value=None):
        """  Corresponds to IDD Field `moisture_content_21`

        Args:
            value (float): value for IDD Field `moisture_content_21`
                Unit: kg/m3
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
                                 'for field `moisture_content_21`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_21`')

        self._data["Moisture Content 21"] = value

    @property
    def relative_humidity_fraction_22(self):
        """Get relative_humidity_fraction_22

        Returns:
            float: the value of `relative_humidity_fraction_22` or None if not set
        """
        return self._data["Relative Humidity Fraction 22"]

    @relative_humidity_fraction_22.setter
    def relative_humidity_fraction_22(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_22`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_22`
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
                                 'for field `relative_humidity_fraction_22`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_22`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_22`')

        self._data["Relative Humidity Fraction 22"] = value

    @property
    def moisture_content_22(self):
        """Get moisture_content_22

        Returns:
            float: the value of `moisture_content_22` or None if not set
        """
        return self._data["Moisture Content 22"]

    @moisture_content_22.setter
    def moisture_content_22(self, value=None):
        """  Corresponds to IDD Field `moisture_content_22`

        Args:
            value (float): value for IDD Field `moisture_content_22`
                Unit: kg/m3
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
                                 'for field `moisture_content_22`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_22`')

        self._data["Moisture Content 22"] = value

    @property
    def relative_humidity_fraction_23(self):
        """Get relative_humidity_fraction_23

        Returns:
            float: the value of `relative_humidity_fraction_23` or None if not set
        """
        return self._data["Relative Humidity Fraction 23"]

    @relative_humidity_fraction_23.setter
    def relative_humidity_fraction_23(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_23`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_23`
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
                                 'for field `relative_humidity_fraction_23`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_23`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_23`')

        self._data["Relative Humidity Fraction 23"] = value

    @property
    def moisture_content_23(self):
        """Get moisture_content_23

        Returns:
            float: the value of `moisture_content_23` or None if not set
        """
        return self._data["Moisture Content 23"]

    @moisture_content_23.setter
    def moisture_content_23(self, value=None):
        """  Corresponds to IDD Field `moisture_content_23`

        Args:
            value (float): value for IDD Field `moisture_content_23`
                Unit: kg/m3
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
                                 'for field `moisture_content_23`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_23`')

        self._data["Moisture Content 23"] = value

    @property
    def relative_humidity_fraction_24(self):
        """Get relative_humidity_fraction_24

        Returns:
            float: the value of `relative_humidity_fraction_24` or None if not set
        """
        return self._data["Relative Humidity Fraction 24"]

    @relative_humidity_fraction_24.setter
    def relative_humidity_fraction_24(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_24`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_24`
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
                                 'for field `relative_humidity_fraction_24`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_24`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_24`')

        self._data["Relative Humidity Fraction 24"] = value

    @property
    def moisture_content_24(self):
        """Get moisture_content_24

        Returns:
            float: the value of `moisture_content_24` or None if not set
        """
        return self._data["Moisture Content 24"]

    @moisture_content_24.setter
    def moisture_content_24(self, value=None):
        """  Corresponds to IDD Field `moisture_content_24`

        Args:
            value (float): value for IDD Field `moisture_content_24`
                Unit: kg/m3
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
                                 'for field `moisture_content_24`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_24`')

        self._data["Moisture Content 24"] = value

    @property
    def relative_humidity_fraction_25(self):
        """Get relative_humidity_fraction_25

        Returns:
            float: the value of `relative_humidity_fraction_25` or None if not set
        """
        return self._data["Relative Humidity Fraction 25"]

    @relative_humidity_fraction_25.setter
    def relative_humidity_fraction_25(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_25`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_25`
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
                                 'for field `relative_humidity_fraction_25`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_25`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_25`')

        self._data["Relative Humidity Fraction 25"] = value

    @property
    def moisture_content_25(self):
        """Get moisture_content_25

        Returns:
            float: the value of `moisture_content_25` or None if not set
        """
        return self._data["Moisture Content 25"]

    @moisture_content_25.setter
    def moisture_content_25(self, value=None):
        """  Corresponds to IDD Field `moisture_content_25`

        Args:
            value (float): value for IDD Field `moisture_content_25`
                Unit: kg/m3
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
                                 'for field `moisture_content_25`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_25`')

        self._data["Moisture Content 25"] = value

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
        out.append(self._to_str(self.material_name))
        out.append(self._to_str(self.number_of_isotherm_coordinates))
        out.append(self._to_str(self.relative_humidity_fraction_1))
        out.append(self._to_str(self.moisture_content_1))
        out.append(self._to_str(self.relative_humidity_fraction_2))
        out.append(self._to_str(self.moisture_content_2))
        out.append(self._to_str(self.relative_humidity_fraction_3))
        out.append(self._to_str(self.moisture_content_3))
        out.append(self._to_str(self.relative_humidity_fraction_4))
        out.append(self._to_str(self.moisture_content_4))
        out.append(self._to_str(self.relative_humidity_fraction_5))
        out.append(self._to_str(self.moisture_content_5))
        out.append(self._to_str(self.relative_humidity_fraction_6))
        out.append(self._to_str(self.moisture_content_6))
        out.append(self._to_str(self.relative_humidity_fraction_7))
        out.append(self._to_str(self.moisture_content_7))
        out.append(self._to_str(self.relative_humidity_fraction_8))
        out.append(self._to_str(self.moisture_content_8))
        out.append(self._to_str(self.relative_humidity_fraction_9))
        out.append(self._to_str(self.moisture_content_9))
        out.append(self._to_str(self.relative_humidity_fraction_10))
        out.append(self._to_str(self.moisture_content_10))
        out.append(self._to_str(self.relative_humidity_fraction_11))
        out.append(self._to_str(self.moisture_content_11))
        out.append(self._to_str(self.relative_humidity_fraction_12))
        out.append(self._to_str(self.moisture_content_12))
        out.append(self._to_str(self.relative_humidity_fraction_13))
        out.append(self._to_str(self.moisture_content_13))
        out.append(self._to_str(self.relative_humidity_fraction_14))
        out.append(self._to_str(self.moisture_content_14))
        out.append(self._to_str(self.relative_humidity_fraction_15))
        out.append(self._to_str(self.moisture_content_15))
        out.append(self._to_str(self.relative_humidity_fraction_16))
        out.append(self._to_str(self.moisture_content_16))
        out.append(self._to_str(self.relative_humidity_fraction_17))
        out.append(self._to_str(self.moisture_content_17))
        out.append(self._to_str(self.relative_humidity_fraction_18))
        out.append(self._to_str(self.moisture_content_18))
        out.append(self._to_str(self.relative_humidity_fraction_19))
        out.append(self._to_str(self.moisture_content_19))
        out.append(self._to_str(self.relative_humidity_fraction_20))
        out.append(self._to_str(self.moisture_content_20))
        out.append(self._to_str(self.relative_humidity_fraction_21))
        out.append(self._to_str(self.moisture_content_21))
        out.append(self._to_str(self.relative_humidity_fraction_22))
        out.append(self._to_str(self.moisture_content_22))
        out.append(self._to_str(self.relative_humidity_fraction_23))
        out.append(self._to_str(self.moisture_content_23))
        out.append(self._to_str(self.relative_humidity_fraction_24))
        out.append(self._to_str(self.moisture_content_24))
        out.append(self._to_str(self.relative_humidity_fraction_25))
        out.append(self._to_str(self.moisture_content_25))
        return ",".join(out)

class MaterialPropertyHeatAndMoistureTransferSuction(object):
    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:Suction`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Relationship between liquid suction transport coefficient and moisture content
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    internal_name = "MaterialProperty:HeatAndMoistureTransfer:Suction"
    field_count = 52

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `MaterialProperty:HeatAndMoistureTransfer:Suction`
        """
        self._data = OrderedDict()
        self._data["Material Name"] = None
        self._data["Number of Suction points"] = None
        self._data["Moisture Content 1"] = None
        self._data["Liquid Transport Coefficient 1"] = None
        self._data["Moisture Content 2"] = None
        self._data["Liquid Transport Coefficient 2"] = None
        self._data["Moisture Content 3"] = None
        self._data["Liquid Transport Coefficient 3"] = None
        self._data["Moisture Content 4"] = None
        self._data["Liquid Transport Coefficient 4"] = None
        self._data["Moisture Content 5"] = None
        self._data["Liquid Transport Coefficient 5"] = None
        self._data["Moisture Content 6"] = None
        self._data["Liquid Transport Coefficient 6"] = None
        self._data["Moisture Content 7"] = None
        self._data["Liquid Transport Coefficient 7"] = None
        self._data["Moisture Content 8"] = None
        self._data["Liquid Transport Coefficient 8"] = None
        self._data["Moisture Content 9"] = None
        self._data["Liquid Transport Coefficient 9"] = None
        self._data["Moisture Content 10"] = None
        self._data["Liquid Transport Coefficient 10"] = None
        self._data["Moisture Content 11"] = None
        self._data["Liquid Transport Coefficient 11"] = None
        self._data["Moisture Content 12"] = None
        self._data["Liquid Transport Coefficient 12"] = None
        self._data["Moisture Content 13"] = None
        self._data["Liquid Transport Coefficient 13"] = None
        self._data["Moisture Content 14"] = None
        self._data["Liquid Transport Coefficient 14"] = None
        self._data["Moisture Content 15"] = None
        self._data["Liquid Transport Coefficient 15"] = None
        self._data["Moisture Content 16"] = None
        self._data["Liquid Transport Coefficient 16"] = None
        self._data["Moisture Content 17"] = None
        self._data["Liquid Transport Coefficient 17"] = None
        self._data["Moisture Content 18"] = None
        self._data["Liquid Transport Coefficient 18"] = None
        self._data["Moisture Content 19"] = None
        self._data["Liquid Transport Coefficient 19"] = None
        self._data["Moisture Content 20"] = None
        self._data["Liquid Transport Coefficient 20"] = None
        self._data["Moisture Content 21"] = None
        self._data["Liquid Transport Coefficient 21"] = None
        self._data["Moisture Content 22"] = None
        self._data["Liquid Transport Coefficient 22"] = None
        self._data["Moisture Content 23"] = None
        self._data["Liquid Transport Coefficient 23"] = None
        self._data["Moisture Content 24"] = None
        self._data["Liquid Transport Coefficient 24"] = None
        self._data["Moisture Content 25"] = None
        self._data["Liquid Transport Coefficient 25"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.material_name = None
        else:
            self.material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_suction_points = None
        else:
            self.number_of_suction_points = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_1 = None
        else:
            self.moisture_content_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_1 = None
        else:
            self.liquid_transport_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_2 = None
        else:
            self.moisture_content_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_2 = None
        else:
            self.liquid_transport_coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_3 = None
        else:
            self.moisture_content_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_3 = None
        else:
            self.liquid_transport_coefficient_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_4 = None
        else:
            self.moisture_content_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_4 = None
        else:
            self.liquid_transport_coefficient_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_5 = None
        else:
            self.moisture_content_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_5 = None
        else:
            self.liquid_transport_coefficient_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_6 = None
        else:
            self.moisture_content_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_6 = None
        else:
            self.liquid_transport_coefficient_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_7 = None
        else:
            self.moisture_content_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_7 = None
        else:
            self.liquid_transport_coefficient_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_8 = None
        else:
            self.moisture_content_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_8 = None
        else:
            self.liquid_transport_coefficient_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_9 = None
        else:
            self.moisture_content_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_9 = None
        else:
            self.liquid_transport_coefficient_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_10 = None
        else:
            self.moisture_content_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_10 = None
        else:
            self.liquid_transport_coefficient_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_11 = None
        else:
            self.moisture_content_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_11 = None
        else:
            self.liquid_transport_coefficient_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_12 = None
        else:
            self.moisture_content_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_12 = None
        else:
            self.liquid_transport_coefficient_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_13 = None
        else:
            self.moisture_content_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_13 = None
        else:
            self.liquid_transport_coefficient_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_14 = None
        else:
            self.moisture_content_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_14 = None
        else:
            self.liquid_transport_coefficient_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_15 = None
        else:
            self.moisture_content_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_15 = None
        else:
            self.liquid_transport_coefficient_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_16 = None
        else:
            self.moisture_content_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_16 = None
        else:
            self.liquid_transport_coefficient_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_17 = None
        else:
            self.moisture_content_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_17 = None
        else:
            self.liquid_transport_coefficient_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_18 = None
        else:
            self.moisture_content_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_18 = None
        else:
            self.liquid_transport_coefficient_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_19 = None
        else:
            self.moisture_content_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_19 = None
        else:
            self.liquid_transport_coefficient_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_20 = None
        else:
            self.moisture_content_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_20 = None
        else:
            self.liquid_transport_coefficient_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_21 = None
        else:
            self.moisture_content_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_21 = None
        else:
            self.liquid_transport_coefficient_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_22 = None
        else:
            self.moisture_content_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_22 = None
        else:
            self.liquid_transport_coefficient_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_23 = None
        else:
            self.moisture_content_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_23 = None
        else:
            self.liquid_transport_coefficient_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_24 = None
        else:
            self.moisture_content_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_24 = None
        else:
            self.liquid_transport_coefficient_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_25 = None
        else:
            self.moisture_content_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_25 = None
        else:
            self.liquid_transport_coefficient_25 = vals[i]
        i += 1

    @property
    def material_name(self):
        """Get material_name

        Returns:
            str: the value of `material_name` or None if not set
        """
        return self._data["Material Name"]

    @material_name.setter
    def material_name(self, value=None):
        """  Corresponds to IDD Field `material_name`
        Material Name that the moisture properties will be added to.

        Args:
            value (str): value for IDD Field `material_name`
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
                                 'for field `material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `material_name`')

        self._data["Material Name"] = value

    @property
    def number_of_suction_points(self):
        """Get number_of_suction_points

        Returns:
            int: the value of `number_of_suction_points` or None if not set
        """
        return self._data["Number of Suction points"]

    @number_of_suction_points.setter
    def number_of_suction_points(self, value=None):
        """  Corresponds to IDD Field `number_of_suction_points`
        Number of Suction Liquid Transport Coefficient coordinates

        Args:
            value (int): value for IDD Field `number_of_suction_points`
                value >= 1
                value <= 25
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
                                 'for field `number_of_suction_points`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_suction_points`')
            if value > 25:
                raise ValueError('value need to be smaller 25 '
                                 'for field `number_of_suction_points`')

        self._data["Number of Suction points"] = value

    @property
    def moisture_content_1(self):
        """Get moisture_content_1

        Returns:
            float: the value of `moisture_content_1` or None if not set
        """
        return self._data["Moisture Content 1"]

    @moisture_content_1.setter
    def moisture_content_1(self, value=None):
        """  Corresponds to IDD Field `moisture_content_1`

        Args:
            value (float): value for IDD Field `moisture_content_1`
                Unit: kg/m3
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
                                 'for field `moisture_content_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_1`')

        self._data["Moisture Content 1"] = value

    @property
    def liquid_transport_coefficient_1(self):
        """Get liquid_transport_coefficient_1

        Returns:
            float: the value of `liquid_transport_coefficient_1` or None if not set
        """
        return self._data["Liquid Transport Coefficient 1"]

    @liquid_transport_coefficient_1.setter
    def liquid_transport_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_1`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_1`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_1`')

        self._data["Liquid Transport Coefficient 1"] = value

    @property
    def moisture_content_2(self):
        """Get moisture_content_2

        Returns:
            float: the value of `moisture_content_2` or None if not set
        """
        return self._data["Moisture Content 2"]

    @moisture_content_2.setter
    def moisture_content_2(self, value=None):
        """  Corresponds to IDD Field `moisture_content_2`

        Args:
            value (float): value for IDD Field `moisture_content_2`
                Unit: kg/m3
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
                                 'for field `moisture_content_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_2`')

        self._data["Moisture Content 2"] = value

    @property
    def liquid_transport_coefficient_2(self):
        """Get liquid_transport_coefficient_2

        Returns:
            float: the value of `liquid_transport_coefficient_2` or None if not set
        """
        return self._data["Liquid Transport Coefficient 2"]

    @liquid_transport_coefficient_2.setter
    def liquid_transport_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_2`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_2`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_2`')

        self._data["Liquid Transport Coefficient 2"] = value

    @property
    def moisture_content_3(self):
        """Get moisture_content_3

        Returns:
            float: the value of `moisture_content_3` or None if not set
        """
        return self._data["Moisture Content 3"]

    @moisture_content_3.setter
    def moisture_content_3(self, value=None):
        """  Corresponds to IDD Field `moisture_content_3`

        Args:
            value (float): value for IDD Field `moisture_content_3`
                Unit: kg/m3
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
                                 'for field `moisture_content_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_3`')

        self._data["Moisture Content 3"] = value

    @property
    def liquid_transport_coefficient_3(self):
        """Get liquid_transport_coefficient_3

        Returns:
            float: the value of `liquid_transport_coefficient_3` or None if not set
        """
        return self._data["Liquid Transport Coefficient 3"]

    @liquid_transport_coefficient_3.setter
    def liquid_transport_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_3`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_3`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_3`')

        self._data["Liquid Transport Coefficient 3"] = value

    @property
    def moisture_content_4(self):
        """Get moisture_content_4

        Returns:
            float: the value of `moisture_content_4` or None if not set
        """
        return self._data["Moisture Content 4"]

    @moisture_content_4.setter
    def moisture_content_4(self, value=None):
        """  Corresponds to IDD Field `moisture_content_4`

        Args:
            value (float): value for IDD Field `moisture_content_4`
                Unit: kg/m3
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
                                 'for field `moisture_content_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_4`')

        self._data["Moisture Content 4"] = value

    @property
    def liquid_transport_coefficient_4(self):
        """Get liquid_transport_coefficient_4

        Returns:
            float: the value of `liquid_transport_coefficient_4` or None if not set
        """
        return self._data["Liquid Transport Coefficient 4"]

    @liquid_transport_coefficient_4.setter
    def liquid_transport_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_4`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_4`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_4`')

        self._data["Liquid Transport Coefficient 4"] = value

    @property
    def moisture_content_5(self):
        """Get moisture_content_5

        Returns:
            float: the value of `moisture_content_5` or None if not set
        """
        return self._data["Moisture Content 5"]

    @moisture_content_5.setter
    def moisture_content_5(self, value=None):
        """  Corresponds to IDD Field `moisture_content_5`

        Args:
            value (float): value for IDD Field `moisture_content_5`
                Unit: kg/m3
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
                                 'for field `moisture_content_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_5`')

        self._data["Moisture Content 5"] = value

    @property
    def liquid_transport_coefficient_5(self):
        """Get liquid_transport_coefficient_5

        Returns:
            float: the value of `liquid_transport_coefficient_5` or None if not set
        """
        return self._data["Liquid Transport Coefficient 5"]

    @liquid_transport_coefficient_5.setter
    def liquid_transport_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_5`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_5`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_5`')

        self._data["Liquid Transport Coefficient 5"] = value

    @property
    def moisture_content_6(self):
        """Get moisture_content_6

        Returns:
            float: the value of `moisture_content_6` or None if not set
        """
        return self._data["Moisture Content 6"]

    @moisture_content_6.setter
    def moisture_content_6(self, value=None):
        """  Corresponds to IDD Field `moisture_content_6`

        Args:
            value (float): value for IDD Field `moisture_content_6`
                Unit: kg/m3
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
                                 'for field `moisture_content_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_6`')

        self._data["Moisture Content 6"] = value

    @property
    def liquid_transport_coefficient_6(self):
        """Get liquid_transport_coefficient_6

        Returns:
            float: the value of `liquid_transport_coefficient_6` or None if not set
        """
        return self._data["Liquid Transport Coefficient 6"]

    @liquid_transport_coefficient_6.setter
    def liquid_transport_coefficient_6(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_6`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_6`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_6`')

        self._data["Liquid Transport Coefficient 6"] = value

    @property
    def moisture_content_7(self):
        """Get moisture_content_7

        Returns:
            float: the value of `moisture_content_7` or None if not set
        """
        return self._data["Moisture Content 7"]

    @moisture_content_7.setter
    def moisture_content_7(self, value=None):
        """  Corresponds to IDD Field `moisture_content_7`

        Args:
            value (float): value for IDD Field `moisture_content_7`
                Unit: kg/m3
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
                                 'for field `moisture_content_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_7`')

        self._data["Moisture Content 7"] = value

    @property
    def liquid_transport_coefficient_7(self):
        """Get liquid_transport_coefficient_7

        Returns:
            float: the value of `liquid_transport_coefficient_7` or None if not set
        """
        return self._data["Liquid Transport Coefficient 7"]

    @liquid_transport_coefficient_7.setter
    def liquid_transport_coefficient_7(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_7`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_7`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_7`')

        self._data["Liquid Transport Coefficient 7"] = value

    @property
    def moisture_content_8(self):
        """Get moisture_content_8

        Returns:
            float: the value of `moisture_content_8` or None if not set
        """
        return self._data["Moisture Content 8"]

    @moisture_content_8.setter
    def moisture_content_8(self, value=None):
        """  Corresponds to IDD Field `moisture_content_8`

        Args:
            value (float): value for IDD Field `moisture_content_8`
                Unit: kg/m3
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
                                 'for field `moisture_content_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_8`')

        self._data["Moisture Content 8"] = value

    @property
    def liquid_transport_coefficient_8(self):
        """Get liquid_transport_coefficient_8

        Returns:
            float: the value of `liquid_transport_coefficient_8` or None if not set
        """
        return self._data["Liquid Transport Coefficient 8"]

    @liquid_transport_coefficient_8.setter
    def liquid_transport_coefficient_8(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_8`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_8`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_8`')

        self._data["Liquid Transport Coefficient 8"] = value

    @property
    def moisture_content_9(self):
        """Get moisture_content_9

        Returns:
            float: the value of `moisture_content_9` or None if not set
        """
        return self._data["Moisture Content 9"]

    @moisture_content_9.setter
    def moisture_content_9(self, value=None):
        """  Corresponds to IDD Field `moisture_content_9`

        Args:
            value (float): value for IDD Field `moisture_content_9`
                Unit: kg/m3
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
                                 'for field `moisture_content_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_9`')

        self._data["Moisture Content 9"] = value

    @property
    def liquid_transport_coefficient_9(self):
        """Get liquid_transport_coefficient_9

        Returns:
            float: the value of `liquid_transport_coefficient_9` or None if not set
        """
        return self._data["Liquid Transport Coefficient 9"]

    @liquid_transport_coefficient_9.setter
    def liquid_transport_coefficient_9(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_9`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_9`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_9`')

        self._data["Liquid Transport Coefficient 9"] = value

    @property
    def moisture_content_10(self):
        """Get moisture_content_10

        Returns:
            float: the value of `moisture_content_10` or None if not set
        """
        return self._data["Moisture Content 10"]

    @moisture_content_10.setter
    def moisture_content_10(self, value=None):
        """  Corresponds to IDD Field `moisture_content_10`

        Args:
            value (float): value for IDD Field `moisture_content_10`
                Unit: kg/m3
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
                                 'for field `moisture_content_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_10`')

        self._data["Moisture Content 10"] = value

    @property
    def liquid_transport_coefficient_10(self):
        """Get liquid_transport_coefficient_10

        Returns:
            float: the value of `liquid_transport_coefficient_10` or None if not set
        """
        return self._data["Liquid Transport Coefficient 10"]

    @liquid_transport_coefficient_10.setter
    def liquid_transport_coefficient_10(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_10`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_10`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_10`')

        self._data["Liquid Transport Coefficient 10"] = value

    @property
    def moisture_content_11(self):
        """Get moisture_content_11

        Returns:
            float: the value of `moisture_content_11` or None if not set
        """
        return self._data["Moisture Content 11"]

    @moisture_content_11.setter
    def moisture_content_11(self, value=None):
        """  Corresponds to IDD Field `moisture_content_11`

        Args:
            value (float): value for IDD Field `moisture_content_11`
                Unit: kg/m3
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
                                 'for field `moisture_content_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_11`')

        self._data["Moisture Content 11"] = value

    @property
    def liquid_transport_coefficient_11(self):
        """Get liquid_transport_coefficient_11

        Returns:
            float: the value of `liquid_transport_coefficient_11` or None if not set
        """
        return self._data["Liquid Transport Coefficient 11"]

    @liquid_transport_coefficient_11.setter
    def liquid_transport_coefficient_11(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_11`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_11`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_11`')

        self._data["Liquid Transport Coefficient 11"] = value

    @property
    def moisture_content_12(self):
        """Get moisture_content_12

        Returns:
            float: the value of `moisture_content_12` or None if not set
        """
        return self._data["Moisture Content 12"]

    @moisture_content_12.setter
    def moisture_content_12(self, value=None):
        """  Corresponds to IDD Field `moisture_content_12`

        Args:
            value (float): value for IDD Field `moisture_content_12`
                Unit: kg/m3
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
                                 'for field `moisture_content_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_12`')

        self._data["Moisture Content 12"] = value

    @property
    def liquid_transport_coefficient_12(self):
        """Get liquid_transport_coefficient_12

        Returns:
            float: the value of `liquid_transport_coefficient_12` or None if not set
        """
        return self._data["Liquid Transport Coefficient 12"]

    @liquid_transport_coefficient_12.setter
    def liquid_transport_coefficient_12(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_12`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_12`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_12`')

        self._data["Liquid Transport Coefficient 12"] = value

    @property
    def moisture_content_13(self):
        """Get moisture_content_13

        Returns:
            float: the value of `moisture_content_13` or None if not set
        """
        return self._data["Moisture Content 13"]

    @moisture_content_13.setter
    def moisture_content_13(self, value=None):
        """  Corresponds to IDD Field `moisture_content_13`

        Args:
            value (float): value for IDD Field `moisture_content_13`
                Unit: kg/m3
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
                                 'for field `moisture_content_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_13`')

        self._data["Moisture Content 13"] = value

    @property
    def liquid_transport_coefficient_13(self):
        """Get liquid_transport_coefficient_13

        Returns:
            float: the value of `liquid_transport_coefficient_13` or None if not set
        """
        return self._data["Liquid Transport Coefficient 13"]

    @liquid_transport_coefficient_13.setter
    def liquid_transport_coefficient_13(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_13`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_13`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_13`')

        self._data["Liquid Transport Coefficient 13"] = value

    @property
    def moisture_content_14(self):
        """Get moisture_content_14

        Returns:
            float: the value of `moisture_content_14` or None if not set
        """
        return self._data["Moisture Content 14"]

    @moisture_content_14.setter
    def moisture_content_14(self, value=None):
        """  Corresponds to IDD Field `moisture_content_14`

        Args:
            value (float): value for IDD Field `moisture_content_14`
                Unit: kg/m3
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
                                 'for field `moisture_content_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_14`')

        self._data["Moisture Content 14"] = value

    @property
    def liquid_transport_coefficient_14(self):
        """Get liquid_transport_coefficient_14

        Returns:
            float: the value of `liquid_transport_coefficient_14` or None if not set
        """
        return self._data["Liquid Transport Coefficient 14"]

    @liquid_transport_coefficient_14.setter
    def liquid_transport_coefficient_14(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_14`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_14`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_14`')

        self._data["Liquid Transport Coefficient 14"] = value

    @property
    def moisture_content_15(self):
        """Get moisture_content_15

        Returns:
            float: the value of `moisture_content_15` or None if not set
        """
        return self._data["Moisture Content 15"]

    @moisture_content_15.setter
    def moisture_content_15(self, value=None):
        """  Corresponds to IDD Field `moisture_content_15`

        Args:
            value (float): value for IDD Field `moisture_content_15`
                Unit: kg/m3
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
                                 'for field `moisture_content_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_15`')

        self._data["Moisture Content 15"] = value

    @property
    def liquid_transport_coefficient_15(self):
        """Get liquid_transport_coefficient_15

        Returns:
            float: the value of `liquid_transport_coefficient_15` or None if not set
        """
        return self._data["Liquid Transport Coefficient 15"]

    @liquid_transport_coefficient_15.setter
    def liquid_transport_coefficient_15(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_15`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_15`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_15`')

        self._data["Liquid Transport Coefficient 15"] = value

    @property
    def moisture_content_16(self):
        """Get moisture_content_16

        Returns:
            float: the value of `moisture_content_16` or None if not set
        """
        return self._data["Moisture Content 16"]

    @moisture_content_16.setter
    def moisture_content_16(self, value=None):
        """  Corresponds to IDD Field `moisture_content_16`

        Args:
            value (float): value for IDD Field `moisture_content_16`
                Unit: kg/m3
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
                                 'for field `moisture_content_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_16`')

        self._data["Moisture Content 16"] = value

    @property
    def liquid_transport_coefficient_16(self):
        """Get liquid_transport_coefficient_16

        Returns:
            float: the value of `liquid_transport_coefficient_16` or None if not set
        """
        return self._data["Liquid Transport Coefficient 16"]

    @liquid_transport_coefficient_16.setter
    def liquid_transport_coefficient_16(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_16`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_16`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_16`')

        self._data["Liquid Transport Coefficient 16"] = value

    @property
    def moisture_content_17(self):
        """Get moisture_content_17

        Returns:
            float: the value of `moisture_content_17` or None if not set
        """
        return self._data["Moisture Content 17"]

    @moisture_content_17.setter
    def moisture_content_17(self, value=None):
        """  Corresponds to IDD Field `moisture_content_17`

        Args:
            value (float): value for IDD Field `moisture_content_17`
                Unit: kg/m3
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
                                 'for field `moisture_content_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_17`')

        self._data["Moisture Content 17"] = value

    @property
    def liquid_transport_coefficient_17(self):
        """Get liquid_transport_coefficient_17

        Returns:
            float: the value of `liquid_transport_coefficient_17` or None if not set
        """
        return self._data["Liquid Transport Coefficient 17"]

    @liquid_transport_coefficient_17.setter
    def liquid_transport_coefficient_17(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_17`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_17`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_17`')

        self._data["Liquid Transport Coefficient 17"] = value

    @property
    def moisture_content_18(self):
        """Get moisture_content_18

        Returns:
            float: the value of `moisture_content_18` or None if not set
        """
        return self._data["Moisture Content 18"]

    @moisture_content_18.setter
    def moisture_content_18(self, value=None):
        """  Corresponds to IDD Field `moisture_content_18`

        Args:
            value (float): value for IDD Field `moisture_content_18`
                Unit: kg/m3
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
                                 'for field `moisture_content_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_18`')

        self._data["Moisture Content 18"] = value

    @property
    def liquid_transport_coefficient_18(self):
        """Get liquid_transport_coefficient_18

        Returns:
            float: the value of `liquid_transport_coefficient_18` or None if not set
        """
        return self._data["Liquid Transport Coefficient 18"]

    @liquid_transport_coefficient_18.setter
    def liquid_transport_coefficient_18(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_18`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_18`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_18`')

        self._data["Liquid Transport Coefficient 18"] = value

    @property
    def moisture_content_19(self):
        """Get moisture_content_19

        Returns:
            float: the value of `moisture_content_19` or None if not set
        """
        return self._data["Moisture Content 19"]

    @moisture_content_19.setter
    def moisture_content_19(self, value=None):
        """  Corresponds to IDD Field `moisture_content_19`

        Args:
            value (float): value for IDD Field `moisture_content_19`
                Unit: kg/m3
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
                                 'for field `moisture_content_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_19`')

        self._data["Moisture Content 19"] = value

    @property
    def liquid_transport_coefficient_19(self):
        """Get liquid_transport_coefficient_19

        Returns:
            float: the value of `liquid_transport_coefficient_19` or None if not set
        """
        return self._data["Liquid Transport Coefficient 19"]

    @liquid_transport_coefficient_19.setter
    def liquid_transport_coefficient_19(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_19`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_19`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_19`')

        self._data["Liquid Transport Coefficient 19"] = value

    @property
    def moisture_content_20(self):
        """Get moisture_content_20

        Returns:
            float: the value of `moisture_content_20` or None if not set
        """
        return self._data["Moisture Content 20"]

    @moisture_content_20.setter
    def moisture_content_20(self, value=None):
        """  Corresponds to IDD Field `moisture_content_20`

        Args:
            value (float): value for IDD Field `moisture_content_20`
                Unit: kg/m3
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
                                 'for field `moisture_content_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_20`')

        self._data["Moisture Content 20"] = value

    @property
    def liquid_transport_coefficient_20(self):
        """Get liquid_transport_coefficient_20

        Returns:
            float: the value of `liquid_transport_coefficient_20` or None if not set
        """
        return self._data["Liquid Transport Coefficient 20"]

    @liquid_transport_coefficient_20.setter
    def liquid_transport_coefficient_20(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_20`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_20`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_20`')

        self._data["Liquid Transport Coefficient 20"] = value

    @property
    def moisture_content_21(self):
        """Get moisture_content_21

        Returns:
            float: the value of `moisture_content_21` or None if not set
        """
        return self._data["Moisture Content 21"]

    @moisture_content_21.setter
    def moisture_content_21(self, value=None):
        """  Corresponds to IDD Field `moisture_content_21`

        Args:
            value (float): value for IDD Field `moisture_content_21`
                Unit: kg/m3
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
                                 'for field `moisture_content_21`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_21`')

        self._data["Moisture Content 21"] = value

    @property
    def liquid_transport_coefficient_21(self):
        """Get liquid_transport_coefficient_21

        Returns:
            float: the value of `liquid_transport_coefficient_21` or None if not set
        """
        return self._data["Liquid Transport Coefficient 21"]

    @liquid_transport_coefficient_21.setter
    def liquid_transport_coefficient_21(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_21`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_21`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_21`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_21`')

        self._data["Liquid Transport Coefficient 21"] = value

    @property
    def moisture_content_22(self):
        """Get moisture_content_22

        Returns:
            float: the value of `moisture_content_22` or None if not set
        """
        return self._data["Moisture Content 22"]

    @moisture_content_22.setter
    def moisture_content_22(self, value=None):
        """  Corresponds to IDD Field `moisture_content_22`

        Args:
            value (float): value for IDD Field `moisture_content_22`
                Unit: kg/m3
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
                                 'for field `moisture_content_22`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_22`')

        self._data["Moisture Content 22"] = value

    @property
    def liquid_transport_coefficient_22(self):
        """Get liquid_transport_coefficient_22

        Returns:
            float: the value of `liquid_transport_coefficient_22` or None if not set
        """
        return self._data["Liquid Transport Coefficient 22"]

    @liquid_transport_coefficient_22.setter
    def liquid_transport_coefficient_22(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_22`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_22`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_22`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_22`')

        self._data["Liquid Transport Coefficient 22"] = value

    @property
    def moisture_content_23(self):
        """Get moisture_content_23

        Returns:
            float: the value of `moisture_content_23` or None if not set
        """
        return self._data["Moisture Content 23"]

    @moisture_content_23.setter
    def moisture_content_23(self, value=None):
        """  Corresponds to IDD Field `moisture_content_23`

        Args:
            value (float): value for IDD Field `moisture_content_23`
                Unit: kg/m3
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
                                 'for field `moisture_content_23`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_23`')

        self._data["Moisture Content 23"] = value

    @property
    def liquid_transport_coefficient_23(self):
        """Get liquid_transport_coefficient_23

        Returns:
            float: the value of `liquid_transport_coefficient_23` or None if not set
        """
        return self._data["Liquid Transport Coefficient 23"]

    @liquid_transport_coefficient_23.setter
    def liquid_transport_coefficient_23(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_23`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_23`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_23`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_23`')

        self._data["Liquid Transport Coefficient 23"] = value

    @property
    def moisture_content_24(self):
        """Get moisture_content_24

        Returns:
            float: the value of `moisture_content_24` or None if not set
        """
        return self._data["Moisture Content 24"]

    @moisture_content_24.setter
    def moisture_content_24(self, value=None):
        """  Corresponds to IDD Field `moisture_content_24`

        Args:
            value (float): value for IDD Field `moisture_content_24`
                Unit: kg/m3
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
                                 'for field `moisture_content_24`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_24`')

        self._data["Moisture Content 24"] = value

    @property
    def liquid_transport_coefficient_24(self):
        """Get liquid_transport_coefficient_24

        Returns:
            float: the value of `liquid_transport_coefficient_24` or None if not set
        """
        return self._data["Liquid Transport Coefficient 24"]

    @liquid_transport_coefficient_24.setter
    def liquid_transport_coefficient_24(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_24`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_24`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_24`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_24`')

        self._data["Liquid Transport Coefficient 24"] = value

    @property
    def moisture_content_25(self):
        """Get moisture_content_25

        Returns:
            float: the value of `moisture_content_25` or None if not set
        """
        return self._data["Moisture Content 25"]

    @moisture_content_25.setter
    def moisture_content_25(self, value=None):
        """  Corresponds to IDD Field `moisture_content_25`

        Args:
            value (float): value for IDD Field `moisture_content_25`
                Unit: kg/m3
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
                                 'for field `moisture_content_25`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_25`')

        self._data["Moisture Content 25"] = value

    @property
    def liquid_transport_coefficient_25(self):
        """Get liquid_transport_coefficient_25

        Returns:
            float: the value of `liquid_transport_coefficient_25` or None if not set
        """
        return self._data["Liquid Transport Coefficient 25"]

    @liquid_transport_coefficient_25.setter
    def liquid_transport_coefficient_25(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_25`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_25`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_25`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_25`')

        self._data["Liquid Transport Coefficient 25"] = value

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
        out.append(self._to_str(self.material_name))
        out.append(self._to_str(self.number_of_suction_points))
        out.append(self._to_str(self.moisture_content_1))
        out.append(self._to_str(self.liquid_transport_coefficient_1))
        out.append(self._to_str(self.moisture_content_2))
        out.append(self._to_str(self.liquid_transport_coefficient_2))
        out.append(self._to_str(self.moisture_content_3))
        out.append(self._to_str(self.liquid_transport_coefficient_3))
        out.append(self._to_str(self.moisture_content_4))
        out.append(self._to_str(self.liquid_transport_coefficient_4))
        out.append(self._to_str(self.moisture_content_5))
        out.append(self._to_str(self.liquid_transport_coefficient_5))
        out.append(self._to_str(self.moisture_content_6))
        out.append(self._to_str(self.liquid_transport_coefficient_6))
        out.append(self._to_str(self.moisture_content_7))
        out.append(self._to_str(self.liquid_transport_coefficient_7))
        out.append(self._to_str(self.moisture_content_8))
        out.append(self._to_str(self.liquid_transport_coefficient_8))
        out.append(self._to_str(self.moisture_content_9))
        out.append(self._to_str(self.liquid_transport_coefficient_9))
        out.append(self._to_str(self.moisture_content_10))
        out.append(self._to_str(self.liquid_transport_coefficient_10))
        out.append(self._to_str(self.moisture_content_11))
        out.append(self._to_str(self.liquid_transport_coefficient_11))
        out.append(self._to_str(self.moisture_content_12))
        out.append(self._to_str(self.liquid_transport_coefficient_12))
        out.append(self._to_str(self.moisture_content_13))
        out.append(self._to_str(self.liquid_transport_coefficient_13))
        out.append(self._to_str(self.moisture_content_14))
        out.append(self._to_str(self.liquid_transport_coefficient_14))
        out.append(self._to_str(self.moisture_content_15))
        out.append(self._to_str(self.liquid_transport_coefficient_15))
        out.append(self._to_str(self.moisture_content_16))
        out.append(self._to_str(self.liquid_transport_coefficient_16))
        out.append(self._to_str(self.moisture_content_17))
        out.append(self._to_str(self.liquid_transport_coefficient_17))
        out.append(self._to_str(self.moisture_content_18))
        out.append(self._to_str(self.liquid_transport_coefficient_18))
        out.append(self._to_str(self.moisture_content_19))
        out.append(self._to_str(self.liquid_transport_coefficient_19))
        out.append(self._to_str(self.moisture_content_20))
        out.append(self._to_str(self.liquid_transport_coefficient_20))
        out.append(self._to_str(self.moisture_content_21))
        out.append(self._to_str(self.liquid_transport_coefficient_21))
        out.append(self._to_str(self.moisture_content_22))
        out.append(self._to_str(self.liquid_transport_coefficient_22))
        out.append(self._to_str(self.moisture_content_23))
        out.append(self._to_str(self.liquid_transport_coefficient_23))
        out.append(self._to_str(self.moisture_content_24))
        out.append(self._to_str(self.liquid_transport_coefficient_24))
        out.append(self._to_str(self.moisture_content_25))
        out.append(self._to_str(self.liquid_transport_coefficient_25))
        return ",".join(out)

class MaterialPropertyHeatAndMoistureTransferRedistribution(object):
    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:Redistribution`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Relationship between liquid transport coefficient and moisture content
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    internal_name = "MaterialProperty:HeatAndMoistureTransfer:Redistribution"
    field_count = 52

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `MaterialProperty:HeatAndMoistureTransfer:Redistribution`
        """
        self._data = OrderedDict()
        self._data["Material Name"] = None
        self._data["Number of Redistribution points"] = None
        self._data["Moisture Content 1"] = None
        self._data["Liquid Transport Coefficient 1"] = None
        self._data["Moisture Content 2"] = None
        self._data["Liquid Transport Coefficient 2"] = None
        self._data["Moisture Content 3"] = None
        self._data["Liquid Transport Coefficient 3"] = None
        self._data["Moisture Content 4"] = None
        self._data["Liquid Transport Coefficient 4"] = None
        self._data["Moisture Content 5"] = None
        self._data["Liquid Transport Coefficient 5"] = None
        self._data["Moisture Content 6"] = None
        self._data["Liquid Transport Coefficient 6"] = None
        self._data["Moisture Content 7"] = None
        self._data["Liquid Transport Coefficient 7"] = None
        self._data["Moisture Content 8"] = None
        self._data["Liquid Transport Coefficient 8"] = None
        self._data["Moisture Content 9"] = None
        self._data["Liquid Transport Coefficient 9"] = None
        self._data["Moisture Content 10"] = None
        self._data["Liquid Transport Coefficient 10"] = None
        self._data["Moisture Content 11"] = None
        self._data["Liquid Transport Coefficient 11"] = None
        self._data["Moisture Content 12"] = None
        self._data["Liquid Transport Coefficient 12"] = None
        self._data["Moisture Content 13"] = None
        self._data["Liquid Transport Coefficient 13"] = None
        self._data["Moisture Content 14"] = None
        self._data["Liquid Transport Coefficient 14"] = None
        self._data["Moisture Content 15"] = None
        self._data["Liquid Transport Coefficient 15"] = None
        self._data["Moisture Content 16"] = None
        self._data["Liquid Transport Coefficient 16"] = None
        self._data["Moisture Content 17"] = None
        self._data["Liquid Transport Coefficient 17"] = None
        self._data["Moisture Content 18"] = None
        self._data["Liquid Transport Coefficient 18"] = None
        self._data["Moisture Content 19"] = None
        self._data["Liquid Transport Coefficient 19"] = None
        self._data["Moisture Content 20"] = None
        self._data["Liquid Transport Coefficient 20"] = None
        self._data["Moisture Content 21"] = None
        self._data["Liquid Transport Coefficient 21"] = None
        self._data["Moisture Content 22"] = None
        self._data["Liquid Transport Coefficient 22"] = None
        self._data["Moisture Content 23"] = None
        self._data["Liquid Transport Coefficient 23"] = None
        self._data["Moisture Content 24"] = None
        self._data["Liquid Transport Coefficient 24"] = None
        self._data["Moisture Content 25"] = None
        self._data["Liquid Transport Coefficient 25"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.material_name = None
        else:
            self.material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_redistribution_points = None
        else:
            self.number_of_redistribution_points = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_1 = None
        else:
            self.moisture_content_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_1 = None
        else:
            self.liquid_transport_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_2 = None
        else:
            self.moisture_content_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_2 = None
        else:
            self.liquid_transport_coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_3 = None
        else:
            self.moisture_content_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_3 = None
        else:
            self.liquid_transport_coefficient_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_4 = None
        else:
            self.moisture_content_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_4 = None
        else:
            self.liquid_transport_coefficient_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_5 = None
        else:
            self.moisture_content_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_5 = None
        else:
            self.liquid_transport_coefficient_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_6 = None
        else:
            self.moisture_content_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_6 = None
        else:
            self.liquid_transport_coefficient_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_7 = None
        else:
            self.moisture_content_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_7 = None
        else:
            self.liquid_transport_coefficient_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_8 = None
        else:
            self.moisture_content_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_8 = None
        else:
            self.liquid_transport_coefficient_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_9 = None
        else:
            self.moisture_content_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_9 = None
        else:
            self.liquid_transport_coefficient_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_10 = None
        else:
            self.moisture_content_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_10 = None
        else:
            self.liquid_transport_coefficient_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_11 = None
        else:
            self.moisture_content_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_11 = None
        else:
            self.liquid_transport_coefficient_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_12 = None
        else:
            self.moisture_content_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_12 = None
        else:
            self.liquid_transport_coefficient_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_13 = None
        else:
            self.moisture_content_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_13 = None
        else:
            self.liquid_transport_coefficient_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_14 = None
        else:
            self.moisture_content_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_14 = None
        else:
            self.liquid_transport_coefficient_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_15 = None
        else:
            self.moisture_content_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_15 = None
        else:
            self.liquid_transport_coefficient_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_16 = None
        else:
            self.moisture_content_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_16 = None
        else:
            self.liquid_transport_coefficient_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_17 = None
        else:
            self.moisture_content_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_17 = None
        else:
            self.liquid_transport_coefficient_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_18 = None
        else:
            self.moisture_content_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_18 = None
        else:
            self.liquid_transport_coefficient_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_19 = None
        else:
            self.moisture_content_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_19 = None
        else:
            self.liquid_transport_coefficient_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_20 = None
        else:
            self.moisture_content_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_20 = None
        else:
            self.liquid_transport_coefficient_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_21 = None
        else:
            self.moisture_content_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_21 = None
        else:
            self.liquid_transport_coefficient_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_22 = None
        else:
            self.moisture_content_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_22 = None
        else:
            self.liquid_transport_coefficient_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_23 = None
        else:
            self.moisture_content_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_23 = None
        else:
            self.liquid_transport_coefficient_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_24 = None
        else:
            self.moisture_content_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_24 = None
        else:
            self.liquid_transport_coefficient_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_25 = None
        else:
            self.moisture_content_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.liquid_transport_coefficient_25 = None
        else:
            self.liquid_transport_coefficient_25 = vals[i]
        i += 1

    @property
    def material_name(self):
        """Get material_name

        Returns:
            str: the value of `material_name` or None if not set
        """
        return self._data["Material Name"]

    @material_name.setter
    def material_name(self, value=None):
        """  Corresponds to IDD Field `material_name`
        Moisture Material Name that the moisture properties will be added to.

        Args:
            value (str): value for IDD Field `material_name`
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
                                 'for field `material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `material_name`')

        self._data["Material Name"] = value

    @property
    def number_of_redistribution_points(self):
        """Get number_of_redistribution_points

        Returns:
            int: the value of `number_of_redistribution_points` or None if not set
        """
        return self._data["Number of Redistribution points"]

    @number_of_redistribution_points.setter
    def number_of_redistribution_points(self, value=None):
        """  Corresponds to IDD Field `number_of_redistribution_points`
        number of data points

        Args:
            value (int): value for IDD Field `number_of_redistribution_points`
                value >= 1
                value <= 25
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
                                 'for field `number_of_redistribution_points`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_redistribution_points`')
            if value > 25:
                raise ValueError('value need to be smaller 25 '
                                 'for field `number_of_redistribution_points`')

        self._data["Number of Redistribution points"] = value

    @property
    def moisture_content_1(self):
        """Get moisture_content_1

        Returns:
            float: the value of `moisture_content_1` or None if not set
        """
        return self._data["Moisture Content 1"]

    @moisture_content_1.setter
    def moisture_content_1(self, value=None):
        """  Corresponds to IDD Field `moisture_content_1`

        Args:
            value (float): value for IDD Field `moisture_content_1`
                Unit: kg/m3
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
                                 'for field `moisture_content_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_1`')

        self._data["Moisture Content 1"] = value

    @property
    def liquid_transport_coefficient_1(self):
        """Get liquid_transport_coefficient_1

        Returns:
            float: the value of `liquid_transport_coefficient_1` or None if not set
        """
        return self._data["Liquid Transport Coefficient 1"]

    @liquid_transport_coefficient_1.setter
    def liquid_transport_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_1`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_1`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_1`')

        self._data["Liquid Transport Coefficient 1"] = value

    @property
    def moisture_content_2(self):
        """Get moisture_content_2

        Returns:
            float: the value of `moisture_content_2` or None if not set
        """
        return self._data["Moisture Content 2"]

    @moisture_content_2.setter
    def moisture_content_2(self, value=None):
        """  Corresponds to IDD Field `moisture_content_2`

        Args:
            value (float): value for IDD Field `moisture_content_2`
                Unit: kg/m3
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
                                 'for field `moisture_content_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_2`')

        self._data["Moisture Content 2"] = value

    @property
    def liquid_transport_coefficient_2(self):
        """Get liquid_transport_coefficient_2

        Returns:
            float: the value of `liquid_transport_coefficient_2` or None if not set
        """
        return self._data["Liquid Transport Coefficient 2"]

    @liquid_transport_coefficient_2.setter
    def liquid_transport_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_2`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_2`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_2`')

        self._data["Liquid Transport Coefficient 2"] = value

    @property
    def moisture_content_3(self):
        """Get moisture_content_3

        Returns:
            float: the value of `moisture_content_3` or None if not set
        """
        return self._data["Moisture Content 3"]

    @moisture_content_3.setter
    def moisture_content_3(self, value=None):
        """  Corresponds to IDD Field `moisture_content_3`

        Args:
            value (float): value for IDD Field `moisture_content_3`
                Unit: kg/m3
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
                                 'for field `moisture_content_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_3`')

        self._data["Moisture Content 3"] = value

    @property
    def liquid_transport_coefficient_3(self):
        """Get liquid_transport_coefficient_3

        Returns:
            float: the value of `liquid_transport_coefficient_3` or None if not set
        """
        return self._data["Liquid Transport Coefficient 3"]

    @liquid_transport_coefficient_3.setter
    def liquid_transport_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_3`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_3`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_3`')

        self._data["Liquid Transport Coefficient 3"] = value

    @property
    def moisture_content_4(self):
        """Get moisture_content_4

        Returns:
            float: the value of `moisture_content_4` or None if not set
        """
        return self._data["Moisture Content 4"]

    @moisture_content_4.setter
    def moisture_content_4(self, value=None):
        """  Corresponds to IDD Field `moisture_content_4`

        Args:
            value (float): value for IDD Field `moisture_content_4`
                Unit: kg/m3
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
                                 'for field `moisture_content_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_4`')

        self._data["Moisture Content 4"] = value

    @property
    def liquid_transport_coefficient_4(self):
        """Get liquid_transport_coefficient_4

        Returns:
            float: the value of `liquid_transport_coefficient_4` or None if not set
        """
        return self._data["Liquid Transport Coefficient 4"]

    @liquid_transport_coefficient_4.setter
    def liquid_transport_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_4`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_4`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_4`')

        self._data["Liquid Transport Coefficient 4"] = value

    @property
    def moisture_content_5(self):
        """Get moisture_content_5

        Returns:
            float: the value of `moisture_content_5` or None if not set
        """
        return self._data["Moisture Content 5"]

    @moisture_content_5.setter
    def moisture_content_5(self, value=None):
        """  Corresponds to IDD Field `moisture_content_5`

        Args:
            value (float): value for IDD Field `moisture_content_5`
                Unit: kg/m3
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
                                 'for field `moisture_content_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_5`')

        self._data["Moisture Content 5"] = value

    @property
    def liquid_transport_coefficient_5(self):
        """Get liquid_transport_coefficient_5

        Returns:
            float: the value of `liquid_transport_coefficient_5` or None if not set
        """
        return self._data["Liquid Transport Coefficient 5"]

    @liquid_transport_coefficient_5.setter
    def liquid_transport_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_5`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_5`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_5`')

        self._data["Liquid Transport Coefficient 5"] = value

    @property
    def moisture_content_6(self):
        """Get moisture_content_6

        Returns:
            float: the value of `moisture_content_6` or None if not set
        """
        return self._data["Moisture Content 6"]

    @moisture_content_6.setter
    def moisture_content_6(self, value=None):
        """  Corresponds to IDD Field `moisture_content_6`

        Args:
            value (float): value for IDD Field `moisture_content_6`
                Unit: kg/m3
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
                                 'for field `moisture_content_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_6`')

        self._data["Moisture Content 6"] = value

    @property
    def liquid_transport_coefficient_6(self):
        """Get liquid_transport_coefficient_6

        Returns:
            float: the value of `liquid_transport_coefficient_6` or None if not set
        """
        return self._data["Liquid Transport Coefficient 6"]

    @liquid_transport_coefficient_6.setter
    def liquid_transport_coefficient_6(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_6`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_6`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_6`')

        self._data["Liquid Transport Coefficient 6"] = value

    @property
    def moisture_content_7(self):
        """Get moisture_content_7

        Returns:
            float: the value of `moisture_content_7` or None if not set
        """
        return self._data["Moisture Content 7"]

    @moisture_content_7.setter
    def moisture_content_7(self, value=None):
        """  Corresponds to IDD Field `moisture_content_7`

        Args:
            value (float): value for IDD Field `moisture_content_7`
                Unit: kg/m3
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
                                 'for field `moisture_content_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_7`')

        self._data["Moisture Content 7"] = value

    @property
    def liquid_transport_coefficient_7(self):
        """Get liquid_transport_coefficient_7

        Returns:
            float: the value of `liquid_transport_coefficient_7` or None if not set
        """
        return self._data["Liquid Transport Coefficient 7"]

    @liquid_transport_coefficient_7.setter
    def liquid_transport_coefficient_7(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_7`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_7`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_7`')

        self._data["Liquid Transport Coefficient 7"] = value

    @property
    def moisture_content_8(self):
        """Get moisture_content_8

        Returns:
            float: the value of `moisture_content_8` or None if not set
        """
        return self._data["Moisture Content 8"]

    @moisture_content_8.setter
    def moisture_content_8(self, value=None):
        """  Corresponds to IDD Field `moisture_content_8`

        Args:
            value (float): value for IDD Field `moisture_content_8`
                Unit: kg/m3
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
                                 'for field `moisture_content_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_8`')

        self._data["Moisture Content 8"] = value

    @property
    def liquid_transport_coefficient_8(self):
        """Get liquid_transport_coefficient_8

        Returns:
            float: the value of `liquid_transport_coefficient_8` or None if not set
        """
        return self._data["Liquid Transport Coefficient 8"]

    @liquid_transport_coefficient_8.setter
    def liquid_transport_coefficient_8(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_8`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_8`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_8`')

        self._data["Liquid Transport Coefficient 8"] = value

    @property
    def moisture_content_9(self):
        """Get moisture_content_9

        Returns:
            float: the value of `moisture_content_9` or None if not set
        """
        return self._data["Moisture Content 9"]

    @moisture_content_9.setter
    def moisture_content_9(self, value=None):
        """  Corresponds to IDD Field `moisture_content_9`

        Args:
            value (float): value for IDD Field `moisture_content_9`
                Unit: kg/m3
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
                                 'for field `moisture_content_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_9`')

        self._data["Moisture Content 9"] = value

    @property
    def liquid_transport_coefficient_9(self):
        """Get liquid_transport_coefficient_9

        Returns:
            float: the value of `liquid_transport_coefficient_9` or None if not set
        """
        return self._data["Liquid Transport Coefficient 9"]

    @liquid_transport_coefficient_9.setter
    def liquid_transport_coefficient_9(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_9`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_9`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_9`')

        self._data["Liquid Transport Coefficient 9"] = value

    @property
    def moisture_content_10(self):
        """Get moisture_content_10

        Returns:
            float: the value of `moisture_content_10` or None if not set
        """
        return self._data["Moisture Content 10"]

    @moisture_content_10.setter
    def moisture_content_10(self, value=None):
        """  Corresponds to IDD Field `moisture_content_10`

        Args:
            value (float): value for IDD Field `moisture_content_10`
                Unit: kg/m3
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
                                 'for field `moisture_content_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_10`')

        self._data["Moisture Content 10"] = value

    @property
    def liquid_transport_coefficient_10(self):
        """Get liquid_transport_coefficient_10

        Returns:
            float: the value of `liquid_transport_coefficient_10` or None if not set
        """
        return self._data["Liquid Transport Coefficient 10"]

    @liquid_transport_coefficient_10.setter
    def liquid_transport_coefficient_10(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_10`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_10`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_10`')

        self._data["Liquid Transport Coefficient 10"] = value

    @property
    def moisture_content_11(self):
        """Get moisture_content_11

        Returns:
            float: the value of `moisture_content_11` or None if not set
        """
        return self._data["Moisture Content 11"]

    @moisture_content_11.setter
    def moisture_content_11(self, value=None):
        """  Corresponds to IDD Field `moisture_content_11`

        Args:
            value (float): value for IDD Field `moisture_content_11`
                Unit: kg/m3
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
                                 'for field `moisture_content_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_11`')

        self._data["Moisture Content 11"] = value

    @property
    def liquid_transport_coefficient_11(self):
        """Get liquid_transport_coefficient_11

        Returns:
            float: the value of `liquid_transport_coefficient_11` or None if not set
        """
        return self._data["Liquid Transport Coefficient 11"]

    @liquid_transport_coefficient_11.setter
    def liquid_transport_coefficient_11(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_11`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_11`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_11`')

        self._data["Liquid Transport Coefficient 11"] = value

    @property
    def moisture_content_12(self):
        """Get moisture_content_12

        Returns:
            float: the value of `moisture_content_12` or None if not set
        """
        return self._data["Moisture Content 12"]

    @moisture_content_12.setter
    def moisture_content_12(self, value=None):
        """  Corresponds to IDD Field `moisture_content_12`

        Args:
            value (float): value for IDD Field `moisture_content_12`
                Unit: kg/m3
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
                                 'for field `moisture_content_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_12`')

        self._data["Moisture Content 12"] = value

    @property
    def liquid_transport_coefficient_12(self):
        """Get liquid_transport_coefficient_12

        Returns:
            float: the value of `liquid_transport_coefficient_12` or None if not set
        """
        return self._data["Liquid Transport Coefficient 12"]

    @liquid_transport_coefficient_12.setter
    def liquid_transport_coefficient_12(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_12`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_12`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_12`')

        self._data["Liquid Transport Coefficient 12"] = value

    @property
    def moisture_content_13(self):
        """Get moisture_content_13

        Returns:
            float: the value of `moisture_content_13` or None if not set
        """
        return self._data["Moisture Content 13"]

    @moisture_content_13.setter
    def moisture_content_13(self, value=None):
        """  Corresponds to IDD Field `moisture_content_13`

        Args:
            value (float): value for IDD Field `moisture_content_13`
                Unit: kg/m3
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
                                 'for field `moisture_content_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_13`')

        self._data["Moisture Content 13"] = value

    @property
    def liquid_transport_coefficient_13(self):
        """Get liquid_transport_coefficient_13

        Returns:
            float: the value of `liquid_transport_coefficient_13` or None if not set
        """
        return self._data["Liquid Transport Coefficient 13"]

    @liquid_transport_coefficient_13.setter
    def liquid_transport_coefficient_13(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_13`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_13`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_13`')

        self._data["Liquid Transport Coefficient 13"] = value

    @property
    def moisture_content_14(self):
        """Get moisture_content_14

        Returns:
            float: the value of `moisture_content_14` or None if not set
        """
        return self._data["Moisture Content 14"]

    @moisture_content_14.setter
    def moisture_content_14(self, value=None):
        """  Corresponds to IDD Field `moisture_content_14`

        Args:
            value (float): value for IDD Field `moisture_content_14`
                Unit: kg/m3
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
                                 'for field `moisture_content_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_14`')

        self._data["Moisture Content 14"] = value

    @property
    def liquid_transport_coefficient_14(self):
        """Get liquid_transport_coefficient_14

        Returns:
            float: the value of `liquid_transport_coefficient_14` or None if not set
        """
        return self._data["Liquid Transport Coefficient 14"]

    @liquid_transport_coefficient_14.setter
    def liquid_transport_coefficient_14(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_14`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_14`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_14`')

        self._data["Liquid Transport Coefficient 14"] = value

    @property
    def moisture_content_15(self):
        """Get moisture_content_15

        Returns:
            float: the value of `moisture_content_15` or None if not set
        """
        return self._data["Moisture Content 15"]

    @moisture_content_15.setter
    def moisture_content_15(self, value=None):
        """  Corresponds to IDD Field `moisture_content_15`

        Args:
            value (float): value for IDD Field `moisture_content_15`
                Unit: kg/m3
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
                                 'for field `moisture_content_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_15`')

        self._data["Moisture Content 15"] = value

    @property
    def liquid_transport_coefficient_15(self):
        """Get liquid_transport_coefficient_15

        Returns:
            float: the value of `liquid_transport_coefficient_15` or None if not set
        """
        return self._data["Liquid Transport Coefficient 15"]

    @liquid_transport_coefficient_15.setter
    def liquid_transport_coefficient_15(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_15`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_15`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_15`')

        self._data["Liquid Transport Coefficient 15"] = value

    @property
    def moisture_content_16(self):
        """Get moisture_content_16

        Returns:
            float: the value of `moisture_content_16` or None if not set
        """
        return self._data["Moisture Content 16"]

    @moisture_content_16.setter
    def moisture_content_16(self, value=None):
        """  Corresponds to IDD Field `moisture_content_16`

        Args:
            value (float): value for IDD Field `moisture_content_16`
                Unit: kg/m3
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
                                 'for field `moisture_content_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_16`')

        self._data["Moisture Content 16"] = value

    @property
    def liquid_transport_coefficient_16(self):
        """Get liquid_transport_coefficient_16

        Returns:
            float: the value of `liquid_transport_coefficient_16` or None if not set
        """
        return self._data["Liquid Transport Coefficient 16"]

    @liquid_transport_coefficient_16.setter
    def liquid_transport_coefficient_16(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_16`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_16`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_16`')

        self._data["Liquid Transport Coefficient 16"] = value

    @property
    def moisture_content_17(self):
        """Get moisture_content_17

        Returns:
            float: the value of `moisture_content_17` or None if not set
        """
        return self._data["Moisture Content 17"]

    @moisture_content_17.setter
    def moisture_content_17(self, value=None):
        """  Corresponds to IDD Field `moisture_content_17`

        Args:
            value (float): value for IDD Field `moisture_content_17`
                Unit: kg/m3
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
                                 'for field `moisture_content_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_17`')

        self._data["Moisture Content 17"] = value

    @property
    def liquid_transport_coefficient_17(self):
        """Get liquid_transport_coefficient_17

        Returns:
            float: the value of `liquid_transport_coefficient_17` or None if not set
        """
        return self._data["Liquid Transport Coefficient 17"]

    @liquid_transport_coefficient_17.setter
    def liquid_transport_coefficient_17(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_17`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_17`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_17`')

        self._data["Liquid Transport Coefficient 17"] = value

    @property
    def moisture_content_18(self):
        """Get moisture_content_18

        Returns:
            float: the value of `moisture_content_18` or None if not set
        """
        return self._data["Moisture Content 18"]

    @moisture_content_18.setter
    def moisture_content_18(self, value=None):
        """  Corresponds to IDD Field `moisture_content_18`

        Args:
            value (float): value for IDD Field `moisture_content_18`
                Unit: kg/m3
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
                                 'for field `moisture_content_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_18`')

        self._data["Moisture Content 18"] = value

    @property
    def liquid_transport_coefficient_18(self):
        """Get liquid_transport_coefficient_18

        Returns:
            float: the value of `liquid_transport_coefficient_18` or None if not set
        """
        return self._data["Liquid Transport Coefficient 18"]

    @liquid_transport_coefficient_18.setter
    def liquid_transport_coefficient_18(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_18`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_18`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_18`')

        self._data["Liquid Transport Coefficient 18"] = value

    @property
    def moisture_content_19(self):
        """Get moisture_content_19

        Returns:
            float: the value of `moisture_content_19` or None if not set
        """
        return self._data["Moisture Content 19"]

    @moisture_content_19.setter
    def moisture_content_19(self, value=None):
        """  Corresponds to IDD Field `moisture_content_19`

        Args:
            value (float): value for IDD Field `moisture_content_19`
                Unit: kg/m3
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
                                 'for field `moisture_content_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_19`')

        self._data["Moisture Content 19"] = value

    @property
    def liquid_transport_coefficient_19(self):
        """Get liquid_transport_coefficient_19

        Returns:
            float: the value of `liquid_transport_coefficient_19` or None if not set
        """
        return self._data["Liquid Transport Coefficient 19"]

    @liquid_transport_coefficient_19.setter
    def liquid_transport_coefficient_19(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_19`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_19`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_19`')

        self._data["Liquid Transport Coefficient 19"] = value

    @property
    def moisture_content_20(self):
        """Get moisture_content_20

        Returns:
            float: the value of `moisture_content_20` or None if not set
        """
        return self._data["Moisture Content 20"]

    @moisture_content_20.setter
    def moisture_content_20(self, value=None):
        """  Corresponds to IDD Field `moisture_content_20`

        Args:
            value (float): value for IDD Field `moisture_content_20`
                Unit: kg/m3
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
                                 'for field `moisture_content_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_20`')

        self._data["Moisture Content 20"] = value

    @property
    def liquid_transport_coefficient_20(self):
        """Get liquid_transport_coefficient_20

        Returns:
            float: the value of `liquid_transport_coefficient_20` or None if not set
        """
        return self._data["Liquid Transport Coefficient 20"]

    @liquid_transport_coefficient_20.setter
    def liquid_transport_coefficient_20(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_20`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_20`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_20`')

        self._data["Liquid Transport Coefficient 20"] = value

    @property
    def moisture_content_21(self):
        """Get moisture_content_21

        Returns:
            float: the value of `moisture_content_21` or None if not set
        """
        return self._data["Moisture Content 21"]

    @moisture_content_21.setter
    def moisture_content_21(self, value=None):
        """  Corresponds to IDD Field `moisture_content_21`

        Args:
            value (float): value for IDD Field `moisture_content_21`
                Unit: kg/m3
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
                                 'for field `moisture_content_21`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_21`')

        self._data["Moisture Content 21"] = value

    @property
    def liquid_transport_coefficient_21(self):
        """Get liquid_transport_coefficient_21

        Returns:
            float: the value of `liquid_transport_coefficient_21` or None if not set
        """
        return self._data["Liquid Transport Coefficient 21"]

    @liquid_transport_coefficient_21.setter
    def liquid_transport_coefficient_21(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_21`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_21`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_21`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_21`')

        self._data["Liquid Transport Coefficient 21"] = value

    @property
    def moisture_content_22(self):
        """Get moisture_content_22

        Returns:
            float: the value of `moisture_content_22` or None if not set
        """
        return self._data["Moisture Content 22"]

    @moisture_content_22.setter
    def moisture_content_22(self, value=None):
        """  Corresponds to IDD Field `moisture_content_22`

        Args:
            value (float): value for IDD Field `moisture_content_22`
                Unit: kg/m3
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
                                 'for field `moisture_content_22`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_22`')

        self._data["Moisture Content 22"] = value

    @property
    def liquid_transport_coefficient_22(self):
        """Get liquid_transport_coefficient_22

        Returns:
            float: the value of `liquid_transport_coefficient_22` or None if not set
        """
        return self._data["Liquid Transport Coefficient 22"]

    @liquid_transport_coefficient_22.setter
    def liquid_transport_coefficient_22(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_22`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_22`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_22`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_22`')

        self._data["Liquid Transport Coefficient 22"] = value

    @property
    def moisture_content_23(self):
        """Get moisture_content_23

        Returns:
            float: the value of `moisture_content_23` or None if not set
        """
        return self._data["Moisture Content 23"]

    @moisture_content_23.setter
    def moisture_content_23(self, value=None):
        """  Corresponds to IDD Field `moisture_content_23`

        Args:
            value (float): value for IDD Field `moisture_content_23`
                Unit: kg/m3
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
                                 'for field `moisture_content_23`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_23`')

        self._data["Moisture Content 23"] = value

    @property
    def liquid_transport_coefficient_23(self):
        """Get liquid_transport_coefficient_23

        Returns:
            float: the value of `liquid_transport_coefficient_23` or None if not set
        """
        return self._data["Liquid Transport Coefficient 23"]

    @liquid_transport_coefficient_23.setter
    def liquid_transport_coefficient_23(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_23`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_23`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_23`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_23`')

        self._data["Liquid Transport Coefficient 23"] = value

    @property
    def moisture_content_24(self):
        """Get moisture_content_24

        Returns:
            float: the value of `moisture_content_24` or None if not set
        """
        return self._data["Moisture Content 24"]

    @moisture_content_24.setter
    def moisture_content_24(self, value=None):
        """  Corresponds to IDD Field `moisture_content_24`

        Args:
            value (float): value for IDD Field `moisture_content_24`
                Unit: kg/m3
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
                                 'for field `moisture_content_24`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_24`')

        self._data["Moisture Content 24"] = value

    @property
    def liquid_transport_coefficient_24(self):
        """Get liquid_transport_coefficient_24

        Returns:
            float: the value of `liquid_transport_coefficient_24` or None if not set
        """
        return self._data["Liquid Transport Coefficient 24"]

    @liquid_transport_coefficient_24.setter
    def liquid_transport_coefficient_24(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_24`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_24`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_24`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_24`')

        self._data["Liquid Transport Coefficient 24"] = value

    @property
    def moisture_content_25(self):
        """Get moisture_content_25

        Returns:
            float: the value of `moisture_content_25` or None if not set
        """
        return self._data["Moisture Content 25"]

    @moisture_content_25.setter
    def moisture_content_25(self, value=None):
        """  Corresponds to IDD Field `moisture_content_25`

        Args:
            value (float): value for IDD Field `moisture_content_25`
                Unit: kg/m3
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
                                 'for field `moisture_content_25`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_25`')

        self._data["Moisture Content 25"] = value

    @property
    def liquid_transport_coefficient_25(self):
        """Get liquid_transport_coefficient_25

        Returns:
            float: the value of `liquid_transport_coefficient_25` or None if not set
        """
        return self._data["Liquid Transport Coefficient 25"]

    @liquid_transport_coefficient_25.setter
    def liquid_transport_coefficient_25(self, value=None):
        """  Corresponds to IDD Field `liquid_transport_coefficient_25`

        Args:
            value (float): value for IDD Field `liquid_transport_coefficient_25`
                Unit: m2/s
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
                                 'for field `liquid_transport_coefficient_25`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `liquid_transport_coefficient_25`')

        self._data["Liquid Transport Coefficient 25"] = value

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
        out.append(self._to_str(self.material_name))
        out.append(self._to_str(self.number_of_redistribution_points))
        out.append(self._to_str(self.moisture_content_1))
        out.append(self._to_str(self.liquid_transport_coefficient_1))
        out.append(self._to_str(self.moisture_content_2))
        out.append(self._to_str(self.liquid_transport_coefficient_2))
        out.append(self._to_str(self.moisture_content_3))
        out.append(self._to_str(self.liquid_transport_coefficient_3))
        out.append(self._to_str(self.moisture_content_4))
        out.append(self._to_str(self.liquid_transport_coefficient_4))
        out.append(self._to_str(self.moisture_content_5))
        out.append(self._to_str(self.liquid_transport_coefficient_5))
        out.append(self._to_str(self.moisture_content_6))
        out.append(self._to_str(self.liquid_transport_coefficient_6))
        out.append(self._to_str(self.moisture_content_7))
        out.append(self._to_str(self.liquid_transport_coefficient_7))
        out.append(self._to_str(self.moisture_content_8))
        out.append(self._to_str(self.liquid_transport_coefficient_8))
        out.append(self._to_str(self.moisture_content_9))
        out.append(self._to_str(self.liquid_transport_coefficient_9))
        out.append(self._to_str(self.moisture_content_10))
        out.append(self._to_str(self.liquid_transport_coefficient_10))
        out.append(self._to_str(self.moisture_content_11))
        out.append(self._to_str(self.liquid_transport_coefficient_11))
        out.append(self._to_str(self.moisture_content_12))
        out.append(self._to_str(self.liquid_transport_coefficient_12))
        out.append(self._to_str(self.moisture_content_13))
        out.append(self._to_str(self.liquid_transport_coefficient_13))
        out.append(self._to_str(self.moisture_content_14))
        out.append(self._to_str(self.liquid_transport_coefficient_14))
        out.append(self._to_str(self.moisture_content_15))
        out.append(self._to_str(self.liquid_transport_coefficient_15))
        out.append(self._to_str(self.moisture_content_16))
        out.append(self._to_str(self.liquid_transport_coefficient_16))
        out.append(self._to_str(self.moisture_content_17))
        out.append(self._to_str(self.liquid_transport_coefficient_17))
        out.append(self._to_str(self.moisture_content_18))
        out.append(self._to_str(self.liquid_transport_coefficient_18))
        out.append(self._to_str(self.moisture_content_19))
        out.append(self._to_str(self.liquid_transport_coefficient_19))
        out.append(self._to_str(self.moisture_content_20))
        out.append(self._to_str(self.liquid_transport_coefficient_20))
        out.append(self._to_str(self.moisture_content_21))
        out.append(self._to_str(self.liquid_transport_coefficient_21))
        out.append(self._to_str(self.moisture_content_22))
        out.append(self._to_str(self.liquid_transport_coefficient_22))
        out.append(self._to_str(self.moisture_content_23))
        out.append(self._to_str(self.liquid_transport_coefficient_23))
        out.append(self._to_str(self.moisture_content_24))
        out.append(self._to_str(self.liquid_transport_coefficient_24))
        out.append(self._to_str(self.moisture_content_25))
        out.append(self._to_str(self.liquid_transport_coefficient_25))
        return ",".join(out)

class MaterialPropertyHeatAndMoistureTransferDiffusion(object):
    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:Diffusion`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Relationship between water vapor diffusion and relative humidity fraction
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    internal_name = "MaterialProperty:HeatAndMoistureTransfer:Diffusion"
    field_count = 52

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `MaterialProperty:HeatAndMoistureTransfer:Diffusion`
        """
        self._data = OrderedDict()
        self._data["Material Name"] = None
        self._data["Number of Data Pairs"] = None
        self._data["Relative Humidity Fraction 1"] = None
        self._data["Water Vapor Diffusion Resistance Factor 1"] = None
        self._data["Relative Humidity Fraction 2"] = None
        self._data["Water Vapor Diffusion Resistance Factor 2"] = None
        self._data["Relative Humidity Fraction 3"] = None
        self._data["Water Vapor Diffusion Resistance Factor 3"] = None
        self._data["Relative Humidity Fraction 4"] = None
        self._data["Water Vapor Diffusion Resistance Factor 4"] = None
        self._data["Relative Humidity Fraction 5"] = None
        self._data["Water Vapor Diffusion Resistance Factor 5"] = None
        self._data["Relative Humidity Fraction 6"] = None
        self._data["Water Vapor Diffusion Resistance Factor 6"] = None
        self._data["Relative Humidity Fraction 7"] = None
        self._data["Water Vapor Diffusion Resistance Factor 7"] = None
        self._data["Relative Humidity Fraction 8"] = None
        self._data["Water Vapor Diffusion Resistance Factor 8"] = None
        self._data["Relative Humidity Fraction 9"] = None
        self._data["Water Vapor Diffusion Resistance Factor 9"] = None
        self._data["Relative Humidity Fraction 10"] = None
        self._data["Water Vapor Diffusion Resistance Factor 10"] = None
        self._data["Relative Humidity Fraction 11"] = None
        self._data["Water Vapor Diffusion Resistance Factor 11"] = None
        self._data["Relative Humidity Fraction 12"] = None
        self._data["Water Vapor Diffusion Resistance Factor 12"] = None
        self._data["Relative Humidity Fraction 13"] = None
        self._data["Water Vapor Diffusion Resistance Factor 13"] = None
        self._data["Relative Humidity Fraction 14"] = None
        self._data["Water Vapor Diffusion Resistance Factor 14"] = None
        self._data["Relative Humidity Fraction 15"] = None
        self._data["Water Vapor Diffusion Resistance Factor 15"] = None
        self._data["Relative Humidity Fraction 16"] = None
        self._data["Water Vapor Diffusion Resistance Factor 16"] = None
        self._data["Relative Humidity Fraction 17"] = None
        self._data["Water Vapor Diffusion Resistance Factor 17"] = None
        self._data["Relative Humidity Fraction 18"] = None
        self._data["Water Vapor Diffusion Resistance Factor 18"] = None
        self._data["Relative Humidity Fraction 19"] = None
        self._data["Water Vapor Diffusion Resistance Factor 19"] = None
        self._data["Relative Humidity Fraction 20"] = None
        self._data["Water Vapor Diffusion Resistance Factor 20"] = None
        self._data["Relative Humidity Fraction 21"] = None
        self._data["Water Vapor Diffusion Resistance Factor 21"] = None
        self._data["Relative Humidity Fraction 22"] = None
        self._data["Water Vapor Diffusion Resistance Factor 22"] = None
        self._data["Relative Humidity Fraction 23"] = None
        self._data["Water Vapor Diffusion Resistance Factor 23"] = None
        self._data["Relative Humidity Fraction 24"] = None
        self._data["Water Vapor Diffusion Resistance Factor 24"] = None
        self._data["Relative Humidity Fraction 25"] = None
        self._data["Water Vapor Diffusion Resistance Factor 25"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.material_name = None
        else:
            self.material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_data_pairs = None
        else:
            self.number_of_data_pairs = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_1 = None
        else:
            self.relative_humidity_fraction_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_1 = None
        else:
            self.water_vapor_diffusion_resistance_factor_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_2 = None
        else:
            self.relative_humidity_fraction_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_2 = None
        else:
            self.water_vapor_diffusion_resistance_factor_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_3 = None
        else:
            self.relative_humidity_fraction_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_3 = None
        else:
            self.water_vapor_diffusion_resistance_factor_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_4 = None
        else:
            self.relative_humidity_fraction_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_4 = None
        else:
            self.water_vapor_diffusion_resistance_factor_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_5 = None
        else:
            self.relative_humidity_fraction_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_5 = None
        else:
            self.water_vapor_diffusion_resistance_factor_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_6 = None
        else:
            self.relative_humidity_fraction_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_6 = None
        else:
            self.water_vapor_diffusion_resistance_factor_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_7 = None
        else:
            self.relative_humidity_fraction_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_7 = None
        else:
            self.water_vapor_diffusion_resistance_factor_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_8 = None
        else:
            self.relative_humidity_fraction_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_8 = None
        else:
            self.water_vapor_diffusion_resistance_factor_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_9 = None
        else:
            self.relative_humidity_fraction_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_9 = None
        else:
            self.water_vapor_diffusion_resistance_factor_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_10 = None
        else:
            self.relative_humidity_fraction_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_10 = None
        else:
            self.water_vapor_diffusion_resistance_factor_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_11 = None
        else:
            self.relative_humidity_fraction_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_11 = None
        else:
            self.water_vapor_diffusion_resistance_factor_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_12 = None
        else:
            self.relative_humidity_fraction_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_12 = None
        else:
            self.water_vapor_diffusion_resistance_factor_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_13 = None
        else:
            self.relative_humidity_fraction_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_13 = None
        else:
            self.water_vapor_diffusion_resistance_factor_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_14 = None
        else:
            self.relative_humidity_fraction_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_14 = None
        else:
            self.water_vapor_diffusion_resistance_factor_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_15 = None
        else:
            self.relative_humidity_fraction_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_15 = None
        else:
            self.water_vapor_diffusion_resistance_factor_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_16 = None
        else:
            self.relative_humidity_fraction_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_16 = None
        else:
            self.water_vapor_diffusion_resistance_factor_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_17 = None
        else:
            self.relative_humidity_fraction_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_17 = None
        else:
            self.water_vapor_diffusion_resistance_factor_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_18 = None
        else:
            self.relative_humidity_fraction_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_18 = None
        else:
            self.water_vapor_diffusion_resistance_factor_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_19 = None
        else:
            self.relative_humidity_fraction_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_19 = None
        else:
            self.water_vapor_diffusion_resistance_factor_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_20 = None
        else:
            self.relative_humidity_fraction_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_20 = None
        else:
            self.water_vapor_diffusion_resistance_factor_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_21 = None
        else:
            self.relative_humidity_fraction_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_21 = None
        else:
            self.water_vapor_diffusion_resistance_factor_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_22 = None
        else:
            self.relative_humidity_fraction_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_22 = None
        else:
            self.water_vapor_diffusion_resistance_factor_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_23 = None
        else:
            self.relative_humidity_fraction_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_23 = None
        else:
            self.water_vapor_diffusion_resistance_factor_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_24 = None
        else:
            self.relative_humidity_fraction_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_24 = None
        else:
            self.water_vapor_diffusion_resistance_factor_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_fraction_25 = None
        else:
            self.relative_humidity_fraction_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_vapor_diffusion_resistance_factor_25 = None
        else:
            self.water_vapor_diffusion_resistance_factor_25 = vals[i]
        i += 1

    @property
    def material_name(self):
        """Get material_name

        Returns:
            str: the value of `material_name` or None if not set
        """
        return self._data["Material Name"]

    @material_name.setter
    def material_name(self, value=None):
        """  Corresponds to IDD Field `material_name`
        Moisture Material Name that the moisture properties will be added to.

        Args:
            value (str): value for IDD Field `material_name`
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
                                 'for field `material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `material_name`')

        self._data["Material Name"] = value

    @property
    def number_of_data_pairs(self):
        """Get number_of_data_pairs

        Returns:
            int: the value of `number_of_data_pairs` or None if not set
        """
        return self._data["Number of Data Pairs"]

    @number_of_data_pairs.setter
    def number_of_data_pairs(self, value=None):
        """  Corresponds to IDD Field `number_of_data_pairs`
        Water Vapor Diffusion Resistance Factor

        Args:
            value (int): value for IDD Field `number_of_data_pairs`
                value >= 1
                value <= 25
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
                                 'for field `number_of_data_pairs`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_data_pairs`')
            if value > 25:
                raise ValueError('value need to be smaller 25 '
                                 'for field `number_of_data_pairs`')

        self._data["Number of Data Pairs"] = value

    @property
    def relative_humidity_fraction_1(self):
        """Get relative_humidity_fraction_1

        Returns:
            float: the value of `relative_humidity_fraction_1` or None if not set
        """
        return self._data["Relative Humidity Fraction 1"]

    @relative_humidity_fraction_1.setter
    def relative_humidity_fraction_1(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_1`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_1`
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
                                 'for field `relative_humidity_fraction_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_1`')

        self._data["Relative Humidity Fraction 1"] = value

    @property
    def water_vapor_diffusion_resistance_factor_1(self):
        """Get water_vapor_diffusion_resistance_factor_1

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_1` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 1"]

    @water_vapor_diffusion_resistance_factor_1.setter
    def water_vapor_diffusion_resistance_factor_1(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_1`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_1`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_1`')

        self._data["Water Vapor Diffusion Resistance Factor 1"] = value

    @property
    def relative_humidity_fraction_2(self):
        """Get relative_humidity_fraction_2

        Returns:
            float: the value of `relative_humidity_fraction_2` or None if not set
        """
        return self._data["Relative Humidity Fraction 2"]

    @relative_humidity_fraction_2.setter
    def relative_humidity_fraction_2(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_2`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_2`
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
                                 'for field `relative_humidity_fraction_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_2`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_2`')

        self._data["Relative Humidity Fraction 2"] = value

    @property
    def water_vapor_diffusion_resistance_factor_2(self):
        """Get water_vapor_diffusion_resistance_factor_2

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_2` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 2"]

    @water_vapor_diffusion_resistance_factor_2.setter
    def water_vapor_diffusion_resistance_factor_2(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_2`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_2`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_2`')

        self._data["Water Vapor Diffusion Resistance Factor 2"] = value

    @property
    def relative_humidity_fraction_3(self):
        """Get relative_humidity_fraction_3

        Returns:
            float: the value of `relative_humidity_fraction_3` or None if not set
        """
        return self._data["Relative Humidity Fraction 3"]

    @relative_humidity_fraction_3.setter
    def relative_humidity_fraction_3(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_3`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_3`
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
                                 'for field `relative_humidity_fraction_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_3`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_3`')

        self._data["Relative Humidity Fraction 3"] = value

    @property
    def water_vapor_diffusion_resistance_factor_3(self):
        """Get water_vapor_diffusion_resistance_factor_3

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_3` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 3"]

    @water_vapor_diffusion_resistance_factor_3.setter
    def water_vapor_diffusion_resistance_factor_3(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_3`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_3`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_3`')

        self._data["Water Vapor Diffusion Resistance Factor 3"] = value

    @property
    def relative_humidity_fraction_4(self):
        """Get relative_humidity_fraction_4

        Returns:
            float: the value of `relative_humidity_fraction_4` or None if not set
        """
        return self._data["Relative Humidity Fraction 4"]

    @relative_humidity_fraction_4.setter
    def relative_humidity_fraction_4(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_4`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_4`
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
                                 'for field `relative_humidity_fraction_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_4`')

        self._data["Relative Humidity Fraction 4"] = value

    @property
    def water_vapor_diffusion_resistance_factor_4(self):
        """Get water_vapor_diffusion_resistance_factor_4

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_4` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 4"]

    @water_vapor_diffusion_resistance_factor_4.setter
    def water_vapor_diffusion_resistance_factor_4(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_4`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_4`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_4`')

        self._data["Water Vapor Diffusion Resistance Factor 4"] = value

    @property
    def relative_humidity_fraction_5(self):
        """Get relative_humidity_fraction_5

        Returns:
            float: the value of `relative_humidity_fraction_5` or None if not set
        """
        return self._data["Relative Humidity Fraction 5"]

    @relative_humidity_fraction_5.setter
    def relative_humidity_fraction_5(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_5`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_5`
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
                                 'for field `relative_humidity_fraction_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_5`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_5`')

        self._data["Relative Humidity Fraction 5"] = value

    @property
    def water_vapor_diffusion_resistance_factor_5(self):
        """Get water_vapor_diffusion_resistance_factor_5

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_5` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 5"]

    @water_vapor_diffusion_resistance_factor_5.setter
    def water_vapor_diffusion_resistance_factor_5(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_5`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_5`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_5`')

        self._data["Water Vapor Diffusion Resistance Factor 5"] = value

    @property
    def relative_humidity_fraction_6(self):
        """Get relative_humidity_fraction_6

        Returns:
            float: the value of `relative_humidity_fraction_6` or None if not set
        """
        return self._data["Relative Humidity Fraction 6"]

    @relative_humidity_fraction_6.setter
    def relative_humidity_fraction_6(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_6`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_6`
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
                                 'for field `relative_humidity_fraction_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_6`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_6`')

        self._data["Relative Humidity Fraction 6"] = value

    @property
    def water_vapor_diffusion_resistance_factor_6(self):
        """Get water_vapor_diffusion_resistance_factor_6

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_6` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 6"]

    @water_vapor_diffusion_resistance_factor_6.setter
    def water_vapor_diffusion_resistance_factor_6(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_6`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_6`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_6`')

        self._data["Water Vapor Diffusion Resistance Factor 6"] = value

    @property
    def relative_humidity_fraction_7(self):
        """Get relative_humidity_fraction_7

        Returns:
            float: the value of `relative_humidity_fraction_7` or None if not set
        """
        return self._data["Relative Humidity Fraction 7"]

    @relative_humidity_fraction_7.setter
    def relative_humidity_fraction_7(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_7`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_7`
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
                                 'for field `relative_humidity_fraction_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_7`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_7`')

        self._data["Relative Humidity Fraction 7"] = value

    @property
    def water_vapor_diffusion_resistance_factor_7(self):
        """Get water_vapor_diffusion_resistance_factor_7

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_7` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 7"]

    @water_vapor_diffusion_resistance_factor_7.setter
    def water_vapor_diffusion_resistance_factor_7(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_7`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_7`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_7`')

        self._data["Water Vapor Diffusion Resistance Factor 7"] = value

    @property
    def relative_humidity_fraction_8(self):
        """Get relative_humidity_fraction_8

        Returns:
            float: the value of `relative_humidity_fraction_8` or None if not set
        """
        return self._data["Relative Humidity Fraction 8"]

    @relative_humidity_fraction_8.setter
    def relative_humidity_fraction_8(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_8`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_8`
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
                                 'for field `relative_humidity_fraction_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_8`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_8`')

        self._data["Relative Humidity Fraction 8"] = value

    @property
    def water_vapor_diffusion_resistance_factor_8(self):
        """Get water_vapor_diffusion_resistance_factor_8

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_8` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 8"]

    @water_vapor_diffusion_resistance_factor_8.setter
    def water_vapor_diffusion_resistance_factor_8(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_8`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_8`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_8`')

        self._data["Water Vapor Diffusion Resistance Factor 8"] = value

    @property
    def relative_humidity_fraction_9(self):
        """Get relative_humidity_fraction_9

        Returns:
            float: the value of `relative_humidity_fraction_9` or None if not set
        """
        return self._data["Relative Humidity Fraction 9"]

    @relative_humidity_fraction_9.setter
    def relative_humidity_fraction_9(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_9`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_9`
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
                                 'for field `relative_humidity_fraction_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_9`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_9`')

        self._data["Relative Humidity Fraction 9"] = value

    @property
    def water_vapor_diffusion_resistance_factor_9(self):
        """Get water_vapor_diffusion_resistance_factor_9

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_9` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 9"]

    @water_vapor_diffusion_resistance_factor_9.setter
    def water_vapor_diffusion_resistance_factor_9(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_9`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_9`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_9`')

        self._data["Water Vapor Diffusion Resistance Factor 9"] = value

    @property
    def relative_humidity_fraction_10(self):
        """Get relative_humidity_fraction_10

        Returns:
            float: the value of `relative_humidity_fraction_10` or None if not set
        """
        return self._data["Relative Humidity Fraction 10"]

    @relative_humidity_fraction_10.setter
    def relative_humidity_fraction_10(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_10`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_10`
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
                                 'for field `relative_humidity_fraction_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_10`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_10`')

        self._data["Relative Humidity Fraction 10"] = value

    @property
    def water_vapor_diffusion_resistance_factor_10(self):
        """Get water_vapor_diffusion_resistance_factor_10

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_10` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 10"]

    @water_vapor_diffusion_resistance_factor_10.setter
    def water_vapor_diffusion_resistance_factor_10(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_10`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_10`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_10`')

        self._data["Water Vapor Diffusion Resistance Factor 10"] = value

    @property
    def relative_humidity_fraction_11(self):
        """Get relative_humidity_fraction_11

        Returns:
            float: the value of `relative_humidity_fraction_11` or None if not set
        """
        return self._data["Relative Humidity Fraction 11"]

    @relative_humidity_fraction_11.setter
    def relative_humidity_fraction_11(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_11`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_11`
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
                                 'for field `relative_humidity_fraction_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_11`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_11`')

        self._data["Relative Humidity Fraction 11"] = value

    @property
    def water_vapor_diffusion_resistance_factor_11(self):
        """Get water_vapor_diffusion_resistance_factor_11

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_11` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 11"]

    @water_vapor_diffusion_resistance_factor_11.setter
    def water_vapor_diffusion_resistance_factor_11(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_11`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_11`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_11`')

        self._data["Water Vapor Diffusion Resistance Factor 11"] = value

    @property
    def relative_humidity_fraction_12(self):
        """Get relative_humidity_fraction_12

        Returns:
            float: the value of `relative_humidity_fraction_12` or None if not set
        """
        return self._data["Relative Humidity Fraction 12"]

    @relative_humidity_fraction_12.setter
    def relative_humidity_fraction_12(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_12`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_12`
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
                                 'for field `relative_humidity_fraction_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_12`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_12`')

        self._data["Relative Humidity Fraction 12"] = value

    @property
    def water_vapor_diffusion_resistance_factor_12(self):
        """Get water_vapor_diffusion_resistance_factor_12

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_12` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 12"]

    @water_vapor_diffusion_resistance_factor_12.setter
    def water_vapor_diffusion_resistance_factor_12(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_12`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_12`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_12`')

        self._data["Water Vapor Diffusion Resistance Factor 12"] = value

    @property
    def relative_humidity_fraction_13(self):
        """Get relative_humidity_fraction_13

        Returns:
            float: the value of `relative_humidity_fraction_13` or None if not set
        """
        return self._data["Relative Humidity Fraction 13"]

    @relative_humidity_fraction_13.setter
    def relative_humidity_fraction_13(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_13`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_13`
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
                                 'for field `relative_humidity_fraction_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_13`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_13`')

        self._data["Relative Humidity Fraction 13"] = value

    @property
    def water_vapor_diffusion_resistance_factor_13(self):
        """Get water_vapor_diffusion_resistance_factor_13

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_13` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 13"]

    @water_vapor_diffusion_resistance_factor_13.setter
    def water_vapor_diffusion_resistance_factor_13(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_13`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_13`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_13`')

        self._data["Water Vapor Diffusion Resistance Factor 13"] = value

    @property
    def relative_humidity_fraction_14(self):
        """Get relative_humidity_fraction_14

        Returns:
            float: the value of `relative_humidity_fraction_14` or None if not set
        """
        return self._data["Relative Humidity Fraction 14"]

    @relative_humidity_fraction_14.setter
    def relative_humidity_fraction_14(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_14`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_14`
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
                                 'for field `relative_humidity_fraction_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_14`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_14`')

        self._data["Relative Humidity Fraction 14"] = value

    @property
    def water_vapor_diffusion_resistance_factor_14(self):
        """Get water_vapor_diffusion_resistance_factor_14

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_14` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 14"]

    @water_vapor_diffusion_resistance_factor_14.setter
    def water_vapor_diffusion_resistance_factor_14(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_14`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_14`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_14`')

        self._data["Water Vapor Diffusion Resistance Factor 14"] = value

    @property
    def relative_humidity_fraction_15(self):
        """Get relative_humidity_fraction_15

        Returns:
            float: the value of `relative_humidity_fraction_15` or None if not set
        """
        return self._data["Relative Humidity Fraction 15"]

    @relative_humidity_fraction_15.setter
    def relative_humidity_fraction_15(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_15`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_15`
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
                                 'for field `relative_humidity_fraction_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_15`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_15`')

        self._data["Relative Humidity Fraction 15"] = value

    @property
    def water_vapor_diffusion_resistance_factor_15(self):
        """Get water_vapor_diffusion_resistance_factor_15

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_15` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 15"]

    @water_vapor_diffusion_resistance_factor_15.setter
    def water_vapor_diffusion_resistance_factor_15(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_15`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_15`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_15`')

        self._data["Water Vapor Diffusion Resistance Factor 15"] = value

    @property
    def relative_humidity_fraction_16(self):
        """Get relative_humidity_fraction_16

        Returns:
            float: the value of `relative_humidity_fraction_16` or None if not set
        """
        return self._data["Relative Humidity Fraction 16"]

    @relative_humidity_fraction_16.setter
    def relative_humidity_fraction_16(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_16`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_16`
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
                                 'for field `relative_humidity_fraction_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_16`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_16`')

        self._data["Relative Humidity Fraction 16"] = value

    @property
    def water_vapor_diffusion_resistance_factor_16(self):
        """Get water_vapor_diffusion_resistance_factor_16

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_16` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 16"]

    @water_vapor_diffusion_resistance_factor_16.setter
    def water_vapor_diffusion_resistance_factor_16(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_16`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_16`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_16`')

        self._data["Water Vapor Diffusion Resistance Factor 16"] = value

    @property
    def relative_humidity_fraction_17(self):
        """Get relative_humidity_fraction_17

        Returns:
            float: the value of `relative_humidity_fraction_17` or None if not set
        """
        return self._data["Relative Humidity Fraction 17"]

    @relative_humidity_fraction_17.setter
    def relative_humidity_fraction_17(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_17`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_17`
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
                                 'for field `relative_humidity_fraction_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_17`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_17`')

        self._data["Relative Humidity Fraction 17"] = value

    @property
    def water_vapor_diffusion_resistance_factor_17(self):
        """Get water_vapor_diffusion_resistance_factor_17

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_17` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 17"]

    @water_vapor_diffusion_resistance_factor_17.setter
    def water_vapor_diffusion_resistance_factor_17(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_17`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_17`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_17`')

        self._data["Water Vapor Diffusion Resistance Factor 17"] = value

    @property
    def relative_humidity_fraction_18(self):
        """Get relative_humidity_fraction_18

        Returns:
            float: the value of `relative_humidity_fraction_18` or None if not set
        """
        return self._data["Relative Humidity Fraction 18"]

    @relative_humidity_fraction_18.setter
    def relative_humidity_fraction_18(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_18`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_18`
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
                                 'for field `relative_humidity_fraction_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_18`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_18`')

        self._data["Relative Humidity Fraction 18"] = value

    @property
    def water_vapor_diffusion_resistance_factor_18(self):
        """Get water_vapor_diffusion_resistance_factor_18

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_18` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 18"]

    @water_vapor_diffusion_resistance_factor_18.setter
    def water_vapor_diffusion_resistance_factor_18(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_18`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_18`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_18`')

        self._data["Water Vapor Diffusion Resistance Factor 18"] = value

    @property
    def relative_humidity_fraction_19(self):
        """Get relative_humidity_fraction_19

        Returns:
            float: the value of `relative_humidity_fraction_19` or None if not set
        """
        return self._data["Relative Humidity Fraction 19"]

    @relative_humidity_fraction_19.setter
    def relative_humidity_fraction_19(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_19`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_19`
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
                                 'for field `relative_humidity_fraction_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_19`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_19`')

        self._data["Relative Humidity Fraction 19"] = value

    @property
    def water_vapor_diffusion_resistance_factor_19(self):
        """Get water_vapor_diffusion_resistance_factor_19

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_19` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 19"]

    @water_vapor_diffusion_resistance_factor_19.setter
    def water_vapor_diffusion_resistance_factor_19(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_19`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_19`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_19`')

        self._data["Water Vapor Diffusion Resistance Factor 19"] = value

    @property
    def relative_humidity_fraction_20(self):
        """Get relative_humidity_fraction_20

        Returns:
            float: the value of `relative_humidity_fraction_20` or None if not set
        """
        return self._data["Relative Humidity Fraction 20"]

    @relative_humidity_fraction_20.setter
    def relative_humidity_fraction_20(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_20`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_20`
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
                                 'for field `relative_humidity_fraction_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_20`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_20`')

        self._data["Relative Humidity Fraction 20"] = value

    @property
    def water_vapor_diffusion_resistance_factor_20(self):
        """Get water_vapor_diffusion_resistance_factor_20

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_20` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 20"]

    @water_vapor_diffusion_resistance_factor_20.setter
    def water_vapor_diffusion_resistance_factor_20(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_20`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_20`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_20`')

        self._data["Water Vapor Diffusion Resistance Factor 20"] = value

    @property
    def relative_humidity_fraction_21(self):
        """Get relative_humidity_fraction_21

        Returns:
            float: the value of `relative_humidity_fraction_21` or None if not set
        """
        return self._data["Relative Humidity Fraction 21"]

    @relative_humidity_fraction_21.setter
    def relative_humidity_fraction_21(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_21`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_21`
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
                                 'for field `relative_humidity_fraction_21`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_21`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_21`')

        self._data["Relative Humidity Fraction 21"] = value

    @property
    def water_vapor_diffusion_resistance_factor_21(self):
        """Get water_vapor_diffusion_resistance_factor_21

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_21` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 21"]

    @water_vapor_diffusion_resistance_factor_21.setter
    def water_vapor_diffusion_resistance_factor_21(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_21`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_21`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_21`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_21`')

        self._data["Water Vapor Diffusion Resistance Factor 21"] = value

    @property
    def relative_humidity_fraction_22(self):
        """Get relative_humidity_fraction_22

        Returns:
            float: the value of `relative_humidity_fraction_22` or None if not set
        """
        return self._data["Relative Humidity Fraction 22"]

    @relative_humidity_fraction_22.setter
    def relative_humidity_fraction_22(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_22`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_22`
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
                                 'for field `relative_humidity_fraction_22`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_22`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_22`')

        self._data["Relative Humidity Fraction 22"] = value

    @property
    def water_vapor_diffusion_resistance_factor_22(self):
        """Get water_vapor_diffusion_resistance_factor_22

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_22` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 22"]

    @water_vapor_diffusion_resistance_factor_22.setter
    def water_vapor_diffusion_resistance_factor_22(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_22`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_22`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_22`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_22`')

        self._data["Water Vapor Diffusion Resistance Factor 22"] = value

    @property
    def relative_humidity_fraction_23(self):
        """Get relative_humidity_fraction_23

        Returns:
            float: the value of `relative_humidity_fraction_23` or None if not set
        """
        return self._data["Relative Humidity Fraction 23"]

    @relative_humidity_fraction_23.setter
    def relative_humidity_fraction_23(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_23`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_23`
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
                                 'for field `relative_humidity_fraction_23`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_23`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_23`')

        self._data["Relative Humidity Fraction 23"] = value

    @property
    def water_vapor_diffusion_resistance_factor_23(self):
        """Get water_vapor_diffusion_resistance_factor_23

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_23` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 23"]

    @water_vapor_diffusion_resistance_factor_23.setter
    def water_vapor_diffusion_resistance_factor_23(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_23`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_23`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_23`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_23`')

        self._data["Water Vapor Diffusion Resistance Factor 23"] = value

    @property
    def relative_humidity_fraction_24(self):
        """Get relative_humidity_fraction_24

        Returns:
            float: the value of `relative_humidity_fraction_24` or None if not set
        """
        return self._data["Relative Humidity Fraction 24"]

    @relative_humidity_fraction_24.setter
    def relative_humidity_fraction_24(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_24`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_24`
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
                                 'for field `relative_humidity_fraction_24`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_24`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_24`')

        self._data["Relative Humidity Fraction 24"] = value

    @property
    def water_vapor_diffusion_resistance_factor_24(self):
        """Get water_vapor_diffusion_resistance_factor_24

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_24` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 24"]

    @water_vapor_diffusion_resistance_factor_24.setter
    def water_vapor_diffusion_resistance_factor_24(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_24`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_24`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_24`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_24`')

        self._data["Water Vapor Diffusion Resistance Factor 24"] = value

    @property
    def relative_humidity_fraction_25(self):
        """Get relative_humidity_fraction_25

        Returns:
            float: the value of `relative_humidity_fraction_25` or None if not set
        """
        return self._data["Relative Humidity Fraction 25"]

    @relative_humidity_fraction_25.setter
    def relative_humidity_fraction_25(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_fraction_25`
        The relative humidity is entered as a fraction.

        Args:
            value (float): value for IDD Field `relative_humidity_fraction_25`
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
                                 'for field `relative_humidity_fraction_25`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_fraction_25`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_humidity_fraction_25`')

        self._data["Relative Humidity Fraction 25"] = value

    @property
    def water_vapor_diffusion_resistance_factor_25(self):
        """Get water_vapor_diffusion_resistance_factor_25

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_25` or None if not set
        """
        return self._data["Water Vapor Diffusion Resistance Factor 25"]

    @water_vapor_diffusion_resistance_factor_25.setter
    def water_vapor_diffusion_resistance_factor_25(self, value=None):
        """  Corresponds to IDD Field `water_vapor_diffusion_resistance_factor_25`

        Args:
            value (float): value for IDD Field `water_vapor_diffusion_resistance_factor_25`
                Unit: dimensionless
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
                                 'for field `water_vapor_diffusion_resistance_factor_25`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `water_vapor_diffusion_resistance_factor_25`')

        self._data["Water Vapor Diffusion Resistance Factor 25"] = value

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
        out.append(self._to_str(self.material_name))
        out.append(self._to_str(self.number_of_data_pairs))
        out.append(self._to_str(self.relative_humidity_fraction_1))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_1))
        out.append(self._to_str(self.relative_humidity_fraction_2))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_2))
        out.append(self._to_str(self.relative_humidity_fraction_3))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_3))
        out.append(self._to_str(self.relative_humidity_fraction_4))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_4))
        out.append(self._to_str(self.relative_humidity_fraction_5))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_5))
        out.append(self._to_str(self.relative_humidity_fraction_6))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_6))
        out.append(self._to_str(self.relative_humidity_fraction_7))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_7))
        out.append(self._to_str(self.relative_humidity_fraction_8))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_8))
        out.append(self._to_str(self.relative_humidity_fraction_9))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_9))
        out.append(self._to_str(self.relative_humidity_fraction_10))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_10))
        out.append(self._to_str(self.relative_humidity_fraction_11))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_11))
        out.append(self._to_str(self.relative_humidity_fraction_12))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_12))
        out.append(self._to_str(self.relative_humidity_fraction_13))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_13))
        out.append(self._to_str(self.relative_humidity_fraction_14))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_14))
        out.append(self._to_str(self.relative_humidity_fraction_15))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_15))
        out.append(self._to_str(self.relative_humidity_fraction_16))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_16))
        out.append(self._to_str(self.relative_humidity_fraction_17))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_17))
        out.append(self._to_str(self.relative_humidity_fraction_18))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_18))
        out.append(self._to_str(self.relative_humidity_fraction_19))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_19))
        out.append(self._to_str(self.relative_humidity_fraction_20))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_20))
        out.append(self._to_str(self.relative_humidity_fraction_21))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_21))
        out.append(self._to_str(self.relative_humidity_fraction_22))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_22))
        out.append(self._to_str(self.relative_humidity_fraction_23))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_23))
        out.append(self._to_str(self.relative_humidity_fraction_24))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_24))
        out.append(self._to_str(self.relative_humidity_fraction_25))
        out.append(self._to_str(self.water_vapor_diffusion_resistance_factor_25))
        return ",".join(out)

class MaterialPropertyHeatAndMoistureTransferThermalConductivity(object):
    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Relationship between thermal conductivity and moisture content
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    internal_name = "MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity"
    field_count = 52

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity`
        """
        self._data = OrderedDict()
        self._data["Material Name"] = None
        self._data["Number of Thermal Coordinates"] = None
        self._data["Moisture Content 1"] = None
        self._data["Thermal Conductivity 1"] = None
        self._data["Moisture Content 2"] = None
        self._data["Thermal Conductivity 2"] = None
        self._data["Moisture Content 3"] = None
        self._data["Thermal Conductivity 3"] = None
        self._data["Moisture Content 4"] = None
        self._data["Thermal Conductivity 4"] = None
        self._data["Moisture Content 5"] = None
        self._data["Thermal Conductivity 5"] = None
        self._data["Moisture Content 6"] = None
        self._data["Thermal Conductivity 6"] = None
        self._data["Moisture Content 7"] = None
        self._data["Thermal Conductivity 7"] = None
        self._data["Moisture Content 8"] = None
        self._data["Thermal Conductivity 8"] = None
        self._data["Moisture Content 9"] = None
        self._data["Thermal Conductivity 9"] = None
        self._data["Moisture Content 10"] = None
        self._data["Thermal Conductivity 10"] = None
        self._data["Moisture Content 11"] = None
        self._data["Thermal Conductivity 11"] = None
        self._data["Moisture Content 12"] = None
        self._data["Thermal Conductivity 12"] = None
        self._data["Moisture Content 13"] = None
        self._data["Thermal Conductivity 13"] = None
        self._data["Moisture Content 14"] = None
        self._data["Thermal Conductivity 14"] = None
        self._data["Moisture Content 15"] = None
        self._data["Thermal Conductivity 15"] = None
        self._data["Moisture Content 16"] = None
        self._data["Thermal Conductivity 16"] = None
        self._data["Moisture Content 17"] = None
        self._data["Thermal Conductivity 17"] = None
        self._data["Moisture Content 18"] = None
        self._data["Thermal Conductivity 18"] = None
        self._data["Moisture Content 19"] = None
        self._data["Thermal Conductivity 19"] = None
        self._data["Moisture Content 20"] = None
        self._data["Thermal Conductivity 20"] = None
        self._data["Moisture Content 21"] = None
        self._data["Thermal Conductivity 21"] = None
        self._data["Moisture Content 22"] = None
        self._data["Thermal Conductivity 22"] = None
        self._data["Moisture Content 23"] = None
        self._data["Thermal Conductivity 23"] = None
        self._data["Moisture Content 24"] = None
        self._data["Thermal Conductivity 24"] = None
        self._data["Moisture Content 25"] = None
        self._data["Thermal Conductivity 25"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.material_name = None
        else:
            self.material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_thermal_coordinates = None
        else:
            self.number_of_thermal_coordinates = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_1 = None
        else:
            self.moisture_content_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_1 = None
        else:
            self.thermal_conductivity_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_2 = None
        else:
            self.moisture_content_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_2 = None
        else:
            self.thermal_conductivity_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_3 = None
        else:
            self.moisture_content_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_3 = None
        else:
            self.thermal_conductivity_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_4 = None
        else:
            self.moisture_content_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_4 = None
        else:
            self.thermal_conductivity_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_5 = None
        else:
            self.moisture_content_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_5 = None
        else:
            self.thermal_conductivity_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_6 = None
        else:
            self.moisture_content_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_6 = None
        else:
            self.thermal_conductivity_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_7 = None
        else:
            self.moisture_content_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_7 = None
        else:
            self.thermal_conductivity_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_8 = None
        else:
            self.moisture_content_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_8 = None
        else:
            self.thermal_conductivity_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_9 = None
        else:
            self.moisture_content_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_9 = None
        else:
            self.thermal_conductivity_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_10 = None
        else:
            self.moisture_content_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_10 = None
        else:
            self.thermal_conductivity_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_11 = None
        else:
            self.moisture_content_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_11 = None
        else:
            self.thermal_conductivity_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_12 = None
        else:
            self.moisture_content_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_12 = None
        else:
            self.thermal_conductivity_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_13 = None
        else:
            self.moisture_content_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_13 = None
        else:
            self.thermal_conductivity_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_14 = None
        else:
            self.moisture_content_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_14 = None
        else:
            self.thermal_conductivity_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_15 = None
        else:
            self.moisture_content_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_15 = None
        else:
            self.thermal_conductivity_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_16 = None
        else:
            self.moisture_content_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_16 = None
        else:
            self.thermal_conductivity_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_17 = None
        else:
            self.moisture_content_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_17 = None
        else:
            self.thermal_conductivity_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_18 = None
        else:
            self.moisture_content_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_18 = None
        else:
            self.thermal_conductivity_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_19 = None
        else:
            self.moisture_content_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_19 = None
        else:
            self.thermal_conductivity_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_20 = None
        else:
            self.moisture_content_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_20 = None
        else:
            self.thermal_conductivity_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_21 = None
        else:
            self.moisture_content_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_21 = None
        else:
            self.thermal_conductivity_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_22 = None
        else:
            self.moisture_content_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_22 = None
        else:
            self.thermal_conductivity_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_23 = None
        else:
            self.moisture_content_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_23 = None
        else:
            self.thermal_conductivity_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_24 = None
        else:
            self.moisture_content_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_24 = None
        else:
            self.thermal_conductivity_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.moisture_content_25 = None
        else:
            self.moisture_content_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_conductivity_25 = None
        else:
            self.thermal_conductivity_25 = vals[i]
        i += 1

    @property
    def material_name(self):
        """Get material_name

        Returns:
            str: the value of `material_name` or None if not set
        """
        return self._data["Material Name"]

    @material_name.setter
    def material_name(self, value=None):
        """  Corresponds to IDD Field `material_name`
        Moisture Material Name that the Thermal Conductivity will be added to.

        Args:
            value (str): value for IDD Field `material_name`
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
                                 'for field `material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `material_name`')

        self._data["Material Name"] = value

    @property
    def number_of_thermal_coordinates(self):
        """Get number_of_thermal_coordinates

        Returns:
            int: the value of `number_of_thermal_coordinates` or None if not set
        """
        return self._data["Number of Thermal Coordinates"]

    @number_of_thermal_coordinates.setter
    def number_of_thermal_coordinates(self, value=None):
        """  Corresponds to IDD Field `number_of_thermal_coordinates`
        number of data coordinates

        Args:
            value (int): value for IDD Field `number_of_thermal_coordinates`
                value >= 1
                value <= 25
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
                                 'for field `number_of_thermal_coordinates`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_thermal_coordinates`')
            if value > 25:
                raise ValueError('value need to be smaller 25 '
                                 'for field `number_of_thermal_coordinates`')

        self._data["Number of Thermal Coordinates"] = value

    @property
    def moisture_content_1(self):
        """Get moisture_content_1

        Returns:
            float: the value of `moisture_content_1` or None if not set
        """
        return self._data["Moisture Content 1"]

    @moisture_content_1.setter
    def moisture_content_1(self, value=None):
        """  Corresponds to IDD Field `moisture_content_1`

        Args:
            value (float): value for IDD Field `moisture_content_1`
                Unit: kg/m3
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
                                 'for field `moisture_content_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_1`')

        self._data["Moisture Content 1"] = value

    @property
    def thermal_conductivity_1(self):
        """Get thermal_conductivity_1

        Returns:
            float: the value of `thermal_conductivity_1` or None if not set
        """
        return self._data["Thermal Conductivity 1"]

    @thermal_conductivity_1.setter
    def thermal_conductivity_1(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_1`

        Args:
            value (float): value for IDD Field `thermal_conductivity_1`
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
                                 'for field `thermal_conductivity_1`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_1`')

        self._data["Thermal Conductivity 1"] = value

    @property
    def moisture_content_2(self):
        """Get moisture_content_2

        Returns:
            float: the value of `moisture_content_2` or None if not set
        """
        return self._data["Moisture Content 2"]

    @moisture_content_2.setter
    def moisture_content_2(self, value=None):
        """  Corresponds to IDD Field `moisture_content_2`

        Args:
            value (float): value for IDD Field `moisture_content_2`
                Unit: kg/m3
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
                                 'for field `moisture_content_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_2`')

        self._data["Moisture Content 2"] = value

    @property
    def thermal_conductivity_2(self):
        """Get thermal_conductivity_2

        Returns:
            float: the value of `thermal_conductivity_2` or None if not set
        """
        return self._data["Thermal Conductivity 2"]

    @thermal_conductivity_2.setter
    def thermal_conductivity_2(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_2`

        Args:
            value (float): value for IDD Field `thermal_conductivity_2`
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
                                 'for field `thermal_conductivity_2`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_2`')

        self._data["Thermal Conductivity 2"] = value

    @property
    def moisture_content_3(self):
        """Get moisture_content_3

        Returns:
            float: the value of `moisture_content_3` or None if not set
        """
        return self._data["Moisture Content 3"]

    @moisture_content_3.setter
    def moisture_content_3(self, value=None):
        """  Corresponds to IDD Field `moisture_content_3`

        Args:
            value (float): value for IDD Field `moisture_content_3`
                Unit: kg/m3
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
                                 'for field `moisture_content_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_3`')

        self._data["Moisture Content 3"] = value

    @property
    def thermal_conductivity_3(self):
        """Get thermal_conductivity_3

        Returns:
            float: the value of `thermal_conductivity_3` or None if not set
        """
        return self._data["Thermal Conductivity 3"]

    @thermal_conductivity_3.setter
    def thermal_conductivity_3(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_3`

        Args:
            value (float): value for IDD Field `thermal_conductivity_3`
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
                                 'for field `thermal_conductivity_3`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_3`')

        self._data["Thermal Conductivity 3"] = value

    @property
    def moisture_content_4(self):
        """Get moisture_content_4

        Returns:
            float: the value of `moisture_content_4` or None if not set
        """
        return self._data["Moisture Content 4"]

    @moisture_content_4.setter
    def moisture_content_4(self, value=None):
        """  Corresponds to IDD Field `moisture_content_4`

        Args:
            value (float): value for IDD Field `moisture_content_4`
                Unit: kg/m3
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
                                 'for field `moisture_content_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_4`')

        self._data["Moisture Content 4"] = value

    @property
    def thermal_conductivity_4(self):
        """Get thermal_conductivity_4

        Returns:
            float: the value of `thermal_conductivity_4` or None if not set
        """
        return self._data["Thermal Conductivity 4"]

    @thermal_conductivity_4.setter
    def thermal_conductivity_4(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_4`

        Args:
            value (float): value for IDD Field `thermal_conductivity_4`
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
                                 'for field `thermal_conductivity_4`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_4`')

        self._data["Thermal Conductivity 4"] = value

    @property
    def moisture_content_5(self):
        """Get moisture_content_5

        Returns:
            float: the value of `moisture_content_5` or None if not set
        """
        return self._data["Moisture Content 5"]

    @moisture_content_5.setter
    def moisture_content_5(self, value=None):
        """  Corresponds to IDD Field `moisture_content_5`

        Args:
            value (float): value for IDD Field `moisture_content_5`
                Unit: kg/m3
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
                                 'for field `moisture_content_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_5`')

        self._data["Moisture Content 5"] = value

    @property
    def thermal_conductivity_5(self):
        """Get thermal_conductivity_5

        Returns:
            float: the value of `thermal_conductivity_5` or None if not set
        """
        return self._data["Thermal Conductivity 5"]

    @thermal_conductivity_5.setter
    def thermal_conductivity_5(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_5`

        Args:
            value (float): value for IDD Field `thermal_conductivity_5`
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
                                 'for field `thermal_conductivity_5`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_5`')

        self._data["Thermal Conductivity 5"] = value

    @property
    def moisture_content_6(self):
        """Get moisture_content_6

        Returns:
            float: the value of `moisture_content_6` or None if not set
        """
        return self._data["Moisture Content 6"]

    @moisture_content_6.setter
    def moisture_content_6(self, value=None):
        """  Corresponds to IDD Field `moisture_content_6`

        Args:
            value (float): value for IDD Field `moisture_content_6`
                Unit: kg/m3
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
                                 'for field `moisture_content_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_6`')

        self._data["Moisture Content 6"] = value

    @property
    def thermal_conductivity_6(self):
        """Get thermal_conductivity_6

        Returns:
            float: the value of `thermal_conductivity_6` or None if not set
        """
        return self._data["Thermal Conductivity 6"]

    @thermal_conductivity_6.setter
    def thermal_conductivity_6(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_6`

        Args:
            value (float): value for IDD Field `thermal_conductivity_6`
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
                                 'for field `thermal_conductivity_6`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_6`')

        self._data["Thermal Conductivity 6"] = value

    @property
    def moisture_content_7(self):
        """Get moisture_content_7

        Returns:
            float: the value of `moisture_content_7` or None if not set
        """
        return self._data["Moisture Content 7"]

    @moisture_content_7.setter
    def moisture_content_7(self, value=None):
        """  Corresponds to IDD Field `moisture_content_7`

        Args:
            value (float): value for IDD Field `moisture_content_7`
                Unit: kg/m3
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
                                 'for field `moisture_content_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_7`')

        self._data["Moisture Content 7"] = value

    @property
    def thermal_conductivity_7(self):
        """Get thermal_conductivity_7

        Returns:
            float: the value of `thermal_conductivity_7` or None if not set
        """
        return self._data["Thermal Conductivity 7"]

    @thermal_conductivity_7.setter
    def thermal_conductivity_7(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_7`

        Args:
            value (float): value for IDD Field `thermal_conductivity_7`
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
                                 'for field `thermal_conductivity_7`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_7`')

        self._data["Thermal Conductivity 7"] = value

    @property
    def moisture_content_8(self):
        """Get moisture_content_8

        Returns:
            float: the value of `moisture_content_8` or None if not set
        """
        return self._data["Moisture Content 8"]

    @moisture_content_8.setter
    def moisture_content_8(self, value=None):
        """  Corresponds to IDD Field `moisture_content_8`

        Args:
            value (float): value for IDD Field `moisture_content_8`
                Unit: kg/m3
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
                                 'for field `moisture_content_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_8`')

        self._data["Moisture Content 8"] = value

    @property
    def thermal_conductivity_8(self):
        """Get thermal_conductivity_8

        Returns:
            float: the value of `thermal_conductivity_8` or None if not set
        """
        return self._data["Thermal Conductivity 8"]

    @thermal_conductivity_8.setter
    def thermal_conductivity_8(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_8`

        Args:
            value (float): value for IDD Field `thermal_conductivity_8`
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
                                 'for field `thermal_conductivity_8`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_8`')

        self._data["Thermal Conductivity 8"] = value

    @property
    def moisture_content_9(self):
        """Get moisture_content_9

        Returns:
            float: the value of `moisture_content_9` or None if not set
        """
        return self._data["Moisture Content 9"]

    @moisture_content_9.setter
    def moisture_content_9(self, value=None):
        """  Corresponds to IDD Field `moisture_content_9`

        Args:
            value (float): value for IDD Field `moisture_content_9`
                Unit: kg/m3
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
                                 'for field `moisture_content_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_9`')

        self._data["Moisture Content 9"] = value

    @property
    def thermal_conductivity_9(self):
        """Get thermal_conductivity_9

        Returns:
            float: the value of `thermal_conductivity_9` or None if not set
        """
        return self._data["Thermal Conductivity 9"]

    @thermal_conductivity_9.setter
    def thermal_conductivity_9(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_9`

        Args:
            value (float): value for IDD Field `thermal_conductivity_9`
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
                                 'for field `thermal_conductivity_9`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_9`')

        self._data["Thermal Conductivity 9"] = value

    @property
    def moisture_content_10(self):
        """Get moisture_content_10

        Returns:
            float: the value of `moisture_content_10` or None if not set
        """
        return self._data["Moisture Content 10"]

    @moisture_content_10.setter
    def moisture_content_10(self, value=None):
        """  Corresponds to IDD Field `moisture_content_10`

        Args:
            value (float): value for IDD Field `moisture_content_10`
                Unit: kg/m3
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
                                 'for field `moisture_content_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_10`')

        self._data["Moisture Content 10"] = value

    @property
    def thermal_conductivity_10(self):
        """Get thermal_conductivity_10

        Returns:
            float: the value of `thermal_conductivity_10` or None if not set
        """
        return self._data["Thermal Conductivity 10"]

    @thermal_conductivity_10.setter
    def thermal_conductivity_10(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_10`

        Args:
            value (float): value for IDD Field `thermal_conductivity_10`
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
                                 'for field `thermal_conductivity_10`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_10`')

        self._data["Thermal Conductivity 10"] = value

    @property
    def moisture_content_11(self):
        """Get moisture_content_11

        Returns:
            float: the value of `moisture_content_11` or None if not set
        """
        return self._data["Moisture Content 11"]

    @moisture_content_11.setter
    def moisture_content_11(self, value=None):
        """  Corresponds to IDD Field `moisture_content_11`

        Args:
            value (float): value for IDD Field `moisture_content_11`
                Unit: kg/m3
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
                                 'for field `moisture_content_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_11`')

        self._data["Moisture Content 11"] = value

    @property
    def thermal_conductivity_11(self):
        """Get thermal_conductivity_11

        Returns:
            float: the value of `thermal_conductivity_11` or None if not set
        """
        return self._data["Thermal Conductivity 11"]

    @thermal_conductivity_11.setter
    def thermal_conductivity_11(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_11`

        Args:
            value (float): value for IDD Field `thermal_conductivity_11`
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
                                 'for field `thermal_conductivity_11`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_11`')

        self._data["Thermal Conductivity 11"] = value

    @property
    def moisture_content_12(self):
        """Get moisture_content_12

        Returns:
            float: the value of `moisture_content_12` or None if not set
        """
        return self._data["Moisture Content 12"]

    @moisture_content_12.setter
    def moisture_content_12(self, value=None):
        """  Corresponds to IDD Field `moisture_content_12`

        Args:
            value (float): value for IDD Field `moisture_content_12`
                Unit: kg/m3
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
                                 'for field `moisture_content_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_12`')

        self._data["Moisture Content 12"] = value

    @property
    def thermal_conductivity_12(self):
        """Get thermal_conductivity_12

        Returns:
            float: the value of `thermal_conductivity_12` or None if not set
        """
        return self._data["Thermal Conductivity 12"]

    @thermal_conductivity_12.setter
    def thermal_conductivity_12(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_12`

        Args:
            value (float): value for IDD Field `thermal_conductivity_12`
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
                                 'for field `thermal_conductivity_12`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_12`')

        self._data["Thermal Conductivity 12"] = value

    @property
    def moisture_content_13(self):
        """Get moisture_content_13

        Returns:
            float: the value of `moisture_content_13` or None if not set
        """
        return self._data["Moisture Content 13"]

    @moisture_content_13.setter
    def moisture_content_13(self, value=None):
        """  Corresponds to IDD Field `moisture_content_13`

        Args:
            value (float): value for IDD Field `moisture_content_13`
                Unit: kg/m3
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
                                 'for field `moisture_content_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_13`')

        self._data["Moisture Content 13"] = value

    @property
    def thermal_conductivity_13(self):
        """Get thermal_conductivity_13

        Returns:
            float: the value of `thermal_conductivity_13` or None if not set
        """
        return self._data["Thermal Conductivity 13"]

    @thermal_conductivity_13.setter
    def thermal_conductivity_13(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_13`

        Args:
            value (float): value for IDD Field `thermal_conductivity_13`
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
                                 'for field `thermal_conductivity_13`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_13`')

        self._data["Thermal Conductivity 13"] = value

    @property
    def moisture_content_14(self):
        """Get moisture_content_14

        Returns:
            float: the value of `moisture_content_14` or None if not set
        """
        return self._data["Moisture Content 14"]

    @moisture_content_14.setter
    def moisture_content_14(self, value=None):
        """  Corresponds to IDD Field `moisture_content_14`

        Args:
            value (float): value for IDD Field `moisture_content_14`
                Unit: kg/m3
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
                                 'for field `moisture_content_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_14`')

        self._data["Moisture Content 14"] = value

    @property
    def thermal_conductivity_14(self):
        """Get thermal_conductivity_14

        Returns:
            float: the value of `thermal_conductivity_14` or None if not set
        """
        return self._data["Thermal Conductivity 14"]

    @thermal_conductivity_14.setter
    def thermal_conductivity_14(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_14`

        Args:
            value (float): value for IDD Field `thermal_conductivity_14`
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
                                 'for field `thermal_conductivity_14`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_14`')

        self._data["Thermal Conductivity 14"] = value

    @property
    def moisture_content_15(self):
        """Get moisture_content_15

        Returns:
            float: the value of `moisture_content_15` or None if not set
        """
        return self._data["Moisture Content 15"]

    @moisture_content_15.setter
    def moisture_content_15(self, value=None):
        """  Corresponds to IDD Field `moisture_content_15`

        Args:
            value (float): value for IDD Field `moisture_content_15`
                Unit: kg/m3
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
                                 'for field `moisture_content_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_15`')

        self._data["Moisture Content 15"] = value

    @property
    def thermal_conductivity_15(self):
        """Get thermal_conductivity_15

        Returns:
            float: the value of `thermal_conductivity_15` or None if not set
        """
        return self._data["Thermal Conductivity 15"]

    @thermal_conductivity_15.setter
    def thermal_conductivity_15(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_15`

        Args:
            value (float): value for IDD Field `thermal_conductivity_15`
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
                                 'for field `thermal_conductivity_15`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_15`')

        self._data["Thermal Conductivity 15"] = value

    @property
    def moisture_content_16(self):
        """Get moisture_content_16

        Returns:
            float: the value of `moisture_content_16` or None if not set
        """
        return self._data["Moisture Content 16"]

    @moisture_content_16.setter
    def moisture_content_16(self, value=None):
        """  Corresponds to IDD Field `moisture_content_16`

        Args:
            value (float): value for IDD Field `moisture_content_16`
                Unit: kg/m3
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
                                 'for field `moisture_content_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_16`')

        self._data["Moisture Content 16"] = value

    @property
    def thermal_conductivity_16(self):
        """Get thermal_conductivity_16

        Returns:
            float: the value of `thermal_conductivity_16` or None if not set
        """
        return self._data["Thermal Conductivity 16"]

    @thermal_conductivity_16.setter
    def thermal_conductivity_16(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_16`

        Args:
            value (float): value for IDD Field `thermal_conductivity_16`
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
                                 'for field `thermal_conductivity_16`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_16`')

        self._data["Thermal Conductivity 16"] = value

    @property
    def moisture_content_17(self):
        """Get moisture_content_17

        Returns:
            float: the value of `moisture_content_17` or None if not set
        """
        return self._data["Moisture Content 17"]

    @moisture_content_17.setter
    def moisture_content_17(self, value=None):
        """  Corresponds to IDD Field `moisture_content_17`

        Args:
            value (float): value for IDD Field `moisture_content_17`
                Unit: kg/m3
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
                                 'for field `moisture_content_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_17`')

        self._data["Moisture Content 17"] = value

    @property
    def thermal_conductivity_17(self):
        """Get thermal_conductivity_17

        Returns:
            float: the value of `thermal_conductivity_17` or None if not set
        """
        return self._data["Thermal Conductivity 17"]

    @thermal_conductivity_17.setter
    def thermal_conductivity_17(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_17`

        Args:
            value (float): value for IDD Field `thermal_conductivity_17`
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
                                 'for field `thermal_conductivity_17`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_17`')

        self._data["Thermal Conductivity 17"] = value

    @property
    def moisture_content_18(self):
        """Get moisture_content_18

        Returns:
            float: the value of `moisture_content_18` or None if not set
        """
        return self._data["Moisture Content 18"]

    @moisture_content_18.setter
    def moisture_content_18(self, value=None):
        """  Corresponds to IDD Field `moisture_content_18`

        Args:
            value (float): value for IDD Field `moisture_content_18`
                Unit: kg/m3
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
                                 'for field `moisture_content_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_18`')

        self._data["Moisture Content 18"] = value

    @property
    def thermal_conductivity_18(self):
        """Get thermal_conductivity_18

        Returns:
            float: the value of `thermal_conductivity_18` or None if not set
        """
        return self._data["Thermal Conductivity 18"]

    @thermal_conductivity_18.setter
    def thermal_conductivity_18(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_18`

        Args:
            value (float): value for IDD Field `thermal_conductivity_18`
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
                                 'for field `thermal_conductivity_18`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_18`')

        self._data["Thermal Conductivity 18"] = value

    @property
    def moisture_content_19(self):
        """Get moisture_content_19

        Returns:
            float: the value of `moisture_content_19` or None if not set
        """
        return self._data["Moisture Content 19"]

    @moisture_content_19.setter
    def moisture_content_19(self, value=None):
        """  Corresponds to IDD Field `moisture_content_19`

        Args:
            value (float): value for IDD Field `moisture_content_19`
                Unit: kg/m3
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
                                 'for field `moisture_content_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_19`')

        self._data["Moisture Content 19"] = value

    @property
    def thermal_conductivity_19(self):
        """Get thermal_conductivity_19

        Returns:
            float: the value of `thermal_conductivity_19` or None if not set
        """
        return self._data["Thermal Conductivity 19"]

    @thermal_conductivity_19.setter
    def thermal_conductivity_19(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_19`

        Args:
            value (float): value for IDD Field `thermal_conductivity_19`
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
                                 'for field `thermal_conductivity_19`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_19`')

        self._data["Thermal Conductivity 19"] = value

    @property
    def moisture_content_20(self):
        """Get moisture_content_20

        Returns:
            float: the value of `moisture_content_20` or None if not set
        """
        return self._data["Moisture Content 20"]

    @moisture_content_20.setter
    def moisture_content_20(self, value=None):
        """  Corresponds to IDD Field `moisture_content_20`

        Args:
            value (float): value for IDD Field `moisture_content_20`
                Unit: kg/m3
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
                                 'for field `moisture_content_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_20`')

        self._data["Moisture Content 20"] = value

    @property
    def thermal_conductivity_20(self):
        """Get thermal_conductivity_20

        Returns:
            float: the value of `thermal_conductivity_20` or None if not set
        """
        return self._data["Thermal Conductivity 20"]

    @thermal_conductivity_20.setter
    def thermal_conductivity_20(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_20`

        Args:
            value (float): value for IDD Field `thermal_conductivity_20`
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
                                 'for field `thermal_conductivity_20`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_20`')

        self._data["Thermal Conductivity 20"] = value

    @property
    def moisture_content_21(self):
        """Get moisture_content_21

        Returns:
            float: the value of `moisture_content_21` or None if not set
        """
        return self._data["Moisture Content 21"]

    @moisture_content_21.setter
    def moisture_content_21(self, value=None):
        """  Corresponds to IDD Field `moisture_content_21`

        Args:
            value (float): value for IDD Field `moisture_content_21`
                Unit: kg/m3
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
                                 'for field `moisture_content_21`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_21`')

        self._data["Moisture Content 21"] = value

    @property
    def thermal_conductivity_21(self):
        """Get thermal_conductivity_21

        Returns:
            float: the value of `thermal_conductivity_21` or None if not set
        """
        return self._data["Thermal Conductivity 21"]

    @thermal_conductivity_21.setter
    def thermal_conductivity_21(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_21`

        Args:
            value (float): value for IDD Field `thermal_conductivity_21`
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
                                 'for field `thermal_conductivity_21`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_21`')

        self._data["Thermal Conductivity 21"] = value

    @property
    def moisture_content_22(self):
        """Get moisture_content_22

        Returns:
            float: the value of `moisture_content_22` or None if not set
        """
        return self._data["Moisture Content 22"]

    @moisture_content_22.setter
    def moisture_content_22(self, value=None):
        """  Corresponds to IDD Field `moisture_content_22`

        Args:
            value (float): value for IDD Field `moisture_content_22`
                Unit: kg/m3
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
                                 'for field `moisture_content_22`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_22`')

        self._data["Moisture Content 22"] = value

    @property
    def thermal_conductivity_22(self):
        """Get thermal_conductivity_22

        Returns:
            float: the value of `thermal_conductivity_22` or None if not set
        """
        return self._data["Thermal Conductivity 22"]

    @thermal_conductivity_22.setter
    def thermal_conductivity_22(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_22`

        Args:
            value (float): value for IDD Field `thermal_conductivity_22`
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
                                 'for field `thermal_conductivity_22`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_22`')

        self._data["Thermal Conductivity 22"] = value

    @property
    def moisture_content_23(self):
        """Get moisture_content_23

        Returns:
            float: the value of `moisture_content_23` or None if not set
        """
        return self._data["Moisture Content 23"]

    @moisture_content_23.setter
    def moisture_content_23(self, value=None):
        """  Corresponds to IDD Field `moisture_content_23`

        Args:
            value (float): value for IDD Field `moisture_content_23`
                Unit: kg/m3
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
                                 'for field `moisture_content_23`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_23`')

        self._data["Moisture Content 23"] = value

    @property
    def thermal_conductivity_23(self):
        """Get thermal_conductivity_23

        Returns:
            float: the value of `thermal_conductivity_23` or None if not set
        """
        return self._data["Thermal Conductivity 23"]

    @thermal_conductivity_23.setter
    def thermal_conductivity_23(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_23`

        Args:
            value (float): value for IDD Field `thermal_conductivity_23`
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
                                 'for field `thermal_conductivity_23`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_23`')

        self._data["Thermal Conductivity 23"] = value

    @property
    def moisture_content_24(self):
        """Get moisture_content_24

        Returns:
            float: the value of `moisture_content_24` or None if not set
        """
        return self._data["Moisture Content 24"]

    @moisture_content_24.setter
    def moisture_content_24(self, value=None):
        """  Corresponds to IDD Field `moisture_content_24`

        Args:
            value (float): value for IDD Field `moisture_content_24`
                Unit: kg/m3
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
                                 'for field `moisture_content_24`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_24`')

        self._data["Moisture Content 24"] = value

    @property
    def thermal_conductivity_24(self):
        """Get thermal_conductivity_24

        Returns:
            float: the value of `thermal_conductivity_24` or None if not set
        """
        return self._data["Thermal Conductivity 24"]

    @thermal_conductivity_24.setter
    def thermal_conductivity_24(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_24`

        Args:
            value (float): value for IDD Field `thermal_conductivity_24`
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
                                 'for field `thermal_conductivity_24`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_24`')

        self._data["Thermal Conductivity 24"] = value

    @property
    def moisture_content_25(self):
        """Get moisture_content_25

        Returns:
            float: the value of `moisture_content_25` or None if not set
        """
        return self._data["Moisture Content 25"]

    @moisture_content_25.setter
    def moisture_content_25(self, value=None):
        """  Corresponds to IDD Field `moisture_content_25`

        Args:
            value (float): value for IDD Field `moisture_content_25`
                Unit: kg/m3
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
                                 'for field `moisture_content_25`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `moisture_content_25`')

        self._data["Moisture Content 25"] = value

    @property
    def thermal_conductivity_25(self):
        """Get thermal_conductivity_25

        Returns:
            float: the value of `thermal_conductivity_25` or None if not set
        """
        return self._data["Thermal Conductivity 25"]

    @thermal_conductivity_25.setter
    def thermal_conductivity_25(self, value=None):
        """  Corresponds to IDD Field `thermal_conductivity_25`

        Args:
            value (float): value for IDD Field `thermal_conductivity_25`
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
                                 'for field `thermal_conductivity_25`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_25`')

        self._data["Thermal Conductivity 25"] = value

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
        out.append(self._to_str(self.material_name))
        out.append(self._to_str(self.number_of_thermal_coordinates))
        out.append(self._to_str(self.moisture_content_1))
        out.append(self._to_str(self.thermal_conductivity_1))
        out.append(self._to_str(self.moisture_content_2))
        out.append(self._to_str(self.thermal_conductivity_2))
        out.append(self._to_str(self.moisture_content_3))
        out.append(self._to_str(self.thermal_conductivity_3))
        out.append(self._to_str(self.moisture_content_4))
        out.append(self._to_str(self.thermal_conductivity_4))
        out.append(self._to_str(self.moisture_content_5))
        out.append(self._to_str(self.thermal_conductivity_5))
        out.append(self._to_str(self.moisture_content_6))
        out.append(self._to_str(self.thermal_conductivity_6))
        out.append(self._to_str(self.moisture_content_7))
        out.append(self._to_str(self.thermal_conductivity_7))
        out.append(self._to_str(self.moisture_content_8))
        out.append(self._to_str(self.thermal_conductivity_8))
        out.append(self._to_str(self.moisture_content_9))
        out.append(self._to_str(self.thermal_conductivity_9))
        out.append(self._to_str(self.moisture_content_10))
        out.append(self._to_str(self.thermal_conductivity_10))
        out.append(self._to_str(self.moisture_content_11))
        out.append(self._to_str(self.thermal_conductivity_11))
        out.append(self._to_str(self.moisture_content_12))
        out.append(self._to_str(self.thermal_conductivity_12))
        out.append(self._to_str(self.moisture_content_13))
        out.append(self._to_str(self.thermal_conductivity_13))
        out.append(self._to_str(self.moisture_content_14))
        out.append(self._to_str(self.thermal_conductivity_14))
        out.append(self._to_str(self.moisture_content_15))
        out.append(self._to_str(self.thermal_conductivity_15))
        out.append(self._to_str(self.moisture_content_16))
        out.append(self._to_str(self.thermal_conductivity_16))
        out.append(self._to_str(self.moisture_content_17))
        out.append(self._to_str(self.thermal_conductivity_17))
        out.append(self._to_str(self.moisture_content_18))
        out.append(self._to_str(self.thermal_conductivity_18))
        out.append(self._to_str(self.moisture_content_19))
        out.append(self._to_str(self.thermal_conductivity_19))
        out.append(self._to_str(self.moisture_content_20))
        out.append(self._to_str(self.thermal_conductivity_20))
        out.append(self._to_str(self.moisture_content_21))
        out.append(self._to_str(self.thermal_conductivity_21))
        out.append(self._to_str(self.moisture_content_22))
        out.append(self._to_str(self.thermal_conductivity_22))
        out.append(self._to_str(self.moisture_content_23))
        out.append(self._to_str(self.thermal_conductivity_23))
        out.append(self._to_str(self.moisture_content_24))
        out.append(self._to_str(self.thermal_conductivity_24))
        out.append(self._to_str(self.moisture_content_25))
        out.append(self._to_str(self.thermal_conductivity_25))
        return ",".join(out)

class MaterialPropertyGlazingSpectralData(object):
    """ Corresponds to IDD object `MaterialProperty:GlazingSpectralData`
        Name is followed by up to 800 sets of normal-incidence measured values of
        [wavelength, transmittance, front reflectance, back reflectance] for wavelengths
        covering the solar spectrum (from about 0.25 to 2.5 microns)
    """
    internal_name = "MaterialProperty:GlazingSpectralData"
    field_count = 180

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `MaterialProperty:GlazingSpectralData`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Wavelength 1"] = None
        self._data["Transmittance 1"] = None
        self._data["Front Reflectance 1"] = None
        self._data["Back Reflectance 1"] = None
        self._data["Wavelength 2"] = None
        self._data["Transmittance 2"] = None
        self._data["Front Reflectance 2"] = None
        self._data["Back Reflectance 2"] = None
        self._data["Wavelength 3"] = None
        self._data["Transmittance 3"] = None
        self._data["Front Reflectance 3"] = None
        self._data["Back Reflectance 3"] = None
        self._data["Wavelength 4"] = None
        self._data["Transmittance 4"] = None
        self._data["Front Reflectance 4"] = None
        self._data["Back Reflectance 4"] = None
        self._data["Wavelength 5"] = None
        self._data["Transmittance 5"] = None
        self._data["Front Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None
        self._data["Back Reflectance 5"] = None

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
            self.wavelength_1 = None
        else:
            self.wavelength_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transmittance_1 = None
        else:
            self.transmittance_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_reflectance_1 = None
        else:
            self.front_reflectance_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_1 = None
        else:
            self.back_reflectance_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wavelength_2 = None
        else:
            self.wavelength_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transmittance_2 = None
        else:
            self.transmittance_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_reflectance_2 = None
        else:
            self.front_reflectance_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_2 = None
        else:
            self.back_reflectance_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wavelength_3 = None
        else:
            self.wavelength_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transmittance_3 = None
        else:
            self.transmittance_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_reflectance_3 = None
        else:
            self.front_reflectance_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_3 = None
        else:
            self.back_reflectance_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wavelength_4 = None
        else:
            self.wavelength_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transmittance_4 = None
        else:
            self.transmittance_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_reflectance_4 = None
        else:
            self.front_reflectance_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_4 = None
        else:
            self.back_reflectance_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wavelength_5 = None
        else:
            self.wavelength_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transmittance_5 = None
        else:
            self.transmittance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.front_reflectance_5 = None
        else:
            self.front_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.back_reflectance_5 = None
        else:
            self.back_reflectance_5 = vals[i]
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
    def wavelength_1(self):
        """Get wavelength_1

        Returns:
            float: the value of `wavelength_1` or None if not set
        """
        return self._data["Wavelength 1"]

    @wavelength_1.setter
    def wavelength_1(self, value=None):
        """  Corresponds to IDD Field `wavelength_1`

        Args:
            value (float): value for IDD Field `wavelength_1`
                Unit: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_1`'.format(value))

        self._data["Wavelength 1"] = value

    @property
    def transmittance_1(self):
        """Get transmittance_1

        Returns:
            float: the value of `transmittance_1` or None if not set
        """
        return self._data["Transmittance 1"]

    @transmittance_1.setter
    def transmittance_1(self, value=None):
        """  Corresponds to IDD Field `transmittance_1`

        Args:
            value (float): value for IDD Field `transmittance_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `transmittance_1`'.format(value))

        self._data["Transmittance 1"] = value

    @property
    def front_reflectance_1(self):
        """Get front_reflectance_1

        Returns:
            float: the value of `front_reflectance_1` or None if not set
        """
        return self._data["Front Reflectance 1"]

    @front_reflectance_1.setter
    def front_reflectance_1(self, value=None):
        """  Corresponds to IDD Field `front_reflectance_1`

        Args:
            value (float): value for IDD Field `front_reflectance_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `front_reflectance_1`'.format(value))

        self._data["Front Reflectance 1"] = value

    @property
    def back_reflectance_1(self):
        """Get back_reflectance_1

        Returns:
            float: the value of `back_reflectance_1` or None if not set
        """
        return self._data["Back Reflectance 1"]

    @back_reflectance_1.setter
    def back_reflectance_1(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_1`

        Args:
            value (float): value for IDD Field `back_reflectance_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_1`'.format(value))

        self._data["Back Reflectance 1"] = value

    @property
    def wavelength_2(self):
        """Get wavelength_2

        Returns:
            float: the value of `wavelength_2` or None if not set
        """
        return self._data["Wavelength 2"]

    @wavelength_2.setter
    def wavelength_2(self, value=None):
        """  Corresponds to IDD Field `wavelength_2`

        Args:
            value (float): value for IDD Field `wavelength_2`
                Unit: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_2`'.format(value))

        self._data["Wavelength 2"] = value

    @property
    def transmittance_2(self):
        """Get transmittance_2

        Returns:
            float: the value of `transmittance_2` or None if not set
        """
        return self._data["Transmittance 2"]

    @transmittance_2.setter
    def transmittance_2(self, value=None):
        """  Corresponds to IDD Field `transmittance_2`

        Args:
            value (float): value for IDD Field `transmittance_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `transmittance_2`'.format(value))

        self._data["Transmittance 2"] = value

    @property
    def front_reflectance_2(self):
        """Get front_reflectance_2

        Returns:
            float: the value of `front_reflectance_2` or None if not set
        """
        return self._data["Front Reflectance 2"]

    @front_reflectance_2.setter
    def front_reflectance_2(self, value=None):
        """  Corresponds to IDD Field `front_reflectance_2`

        Args:
            value (float): value for IDD Field `front_reflectance_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `front_reflectance_2`'.format(value))

        self._data["Front Reflectance 2"] = value

    @property
    def back_reflectance_2(self):
        """Get back_reflectance_2

        Returns:
            float: the value of `back_reflectance_2` or None if not set
        """
        return self._data["Back Reflectance 2"]

    @back_reflectance_2.setter
    def back_reflectance_2(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_2`

        Args:
            value (float): value for IDD Field `back_reflectance_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_2`'.format(value))

        self._data["Back Reflectance 2"] = value

    @property
    def wavelength_3(self):
        """Get wavelength_3

        Returns:
            float: the value of `wavelength_3` or None if not set
        """
        return self._data["Wavelength 3"]

    @wavelength_3.setter
    def wavelength_3(self, value=None):
        """  Corresponds to IDD Field `wavelength_3`

        Args:
            value (float): value for IDD Field `wavelength_3`
                Unit: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_3`'.format(value))

        self._data["Wavelength 3"] = value

    @property
    def transmittance_3(self):
        """Get transmittance_3

        Returns:
            float: the value of `transmittance_3` or None if not set
        """
        return self._data["Transmittance 3"]

    @transmittance_3.setter
    def transmittance_3(self, value=None):
        """  Corresponds to IDD Field `transmittance_3`

        Args:
            value (float): value for IDD Field `transmittance_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `transmittance_3`'.format(value))

        self._data["Transmittance 3"] = value

    @property
    def front_reflectance_3(self):
        """Get front_reflectance_3

        Returns:
            float: the value of `front_reflectance_3` or None if not set
        """
        return self._data["Front Reflectance 3"]

    @front_reflectance_3.setter
    def front_reflectance_3(self, value=None):
        """  Corresponds to IDD Field `front_reflectance_3`

        Args:
            value (float): value for IDD Field `front_reflectance_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `front_reflectance_3`'.format(value))

        self._data["Front Reflectance 3"] = value

    @property
    def back_reflectance_3(self):
        """Get back_reflectance_3

        Returns:
            float: the value of `back_reflectance_3` or None if not set
        """
        return self._data["Back Reflectance 3"]

    @back_reflectance_3.setter
    def back_reflectance_3(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_3`

        Args:
            value (float): value for IDD Field `back_reflectance_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_3`'.format(value))

        self._data["Back Reflectance 3"] = value

    @property
    def wavelength_4(self):
        """Get wavelength_4

        Returns:
            float: the value of `wavelength_4` or None if not set
        """
        return self._data["Wavelength 4"]

    @wavelength_4.setter
    def wavelength_4(self, value=None):
        """  Corresponds to IDD Field `wavelength_4`

        Args:
            value (float): value for IDD Field `wavelength_4`
                Unit: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_4`'.format(value))

        self._data["Wavelength 4"] = value

    @property
    def transmittance_4(self):
        """Get transmittance_4

        Returns:
            float: the value of `transmittance_4` or None if not set
        """
        return self._data["Transmittance 4"]

    @transmittance_4.setter
    def transmittance_4(self, value=None):
        """  Corresponds to IDD Field `transmittance_4`

        Args:
            value (float): value for IDD Field `transmittance_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `transmittance_4`'.format(value))

        self._data["Transmittance 4"] = value

    @property
    def front_reflectance_4(self):
        """Get front_reflectance_4

        Returns:
            float: the value of `front_reflectance_4` or None if not set
        """
        return self._data["Front Reflectance 4"]

    @front_reflectance_4.setter
    def front_reflectance_4(self, value=None):
        """  Corresponds to IDD Field `front_reflectance_4`

        Args:
            value (float): value for IDD Field `front_reflectance_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `front_reflectance_4`'.format(value))

        self._data["Front Reflectance 4"] = value

    @property
    def back_reflectance_4(self):
        """Get back_reflectance_4

        Returns:
            float: the value of `back_reflectance_4` or None if not set
        """
        return self._data["Back Reflectance 4"]

    @back_reflectance_4.setter
    def back_reflectance_4(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_4`

        Args:
            value (float): value for IDD Field `back_reflectance_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_4`'.format(value))

        self._data["Back Reflectance 4"] = value

    @property
    def wavelength_5(self):
        """Get wavelength_5

        Returns:
            float: the value of `wavelength_5` or None if not set
        """
        return self._data["Wavelength 5"]

    @wavelength_5.setter
    def wavelength_5(self, value=None):
        """  Corresponds to IDD Field `wavelength_5`

        Args:
            value (float): value for IDD Field `wavelength_5`
                Unit: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wavelength_5`'.format(value))

        self._data["Wavelength 5"] = value

    @property
    def transmittance_5(self):
        """Get transmittance_5

        Returns:
            float: the value of `transmittance_5` or None if not set
        """
        return self._data["Transmittance 5"]

    @transmittance_5.setter
    def transmittance_5(self, value=None):
        """  Corresponds to IDD Field `transmittance_5`

        Args:
            value (float): value for IDD Field `transmittance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `transmittance_5`'.format(value))

        self._data["Transmittance 5"] = value

    @property
    def front_reflectance_5(self):
        """Get front_reflectance_5

        Returns:
            float: the value of `front_reflectance_5` or None if not set
        """
        return self._data["Front Reflectance 5"]

    @front_reflectance_5.setter
    def front_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `front_reflectance_5`

        Args:
            value (float): value for IDD Field `front_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `front_reflectance_5`'.format(value))

        self._data["Front Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

    @property
    def back_reflectance_5(self):
        """Get back_reflectance_5

        Returns:
            float: the value of `back_reflectance_5` or None if not set
        """
        return self._data["Back Reflectance 5"]

    @back_reflectance_5.setter
    def back_reflectance_5(self, value=None):
        """  Corresponds to IDD Field `back_reflectance_5`

        Args:
            value (float): value for IDD Field `back_reflectance_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `back_reflectance_5`'.format(value))

        self._data["Back Reflectance 5"] = value

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
        out.append(self._to_str(self.wavelength_1))
        out.append(self._to_str(self.transmittance_1))
        out.append(self._to_str(self.front_reflectance_1))
        out.append(self._to_str(self.back_reflectance_1))
        out.append(self._to_str(self.wavelength_2))
        out.append(self._to_str(self.transmittance_2))
        out.append(self._to_str(self.front_reflectance_2))
        out.append(self._to_str(self.back_reflectance_2))
        out.append(self._to_str(self.wavelength_3))
        out.append(self._to_str(self.transmittance_3))
        out.append(self._to_str(self.front_reflectance_3))
        out.append(self._to_str(self.back_reflectance_3))
        out.append(self._to_str(self.wavelength_4))
        out.append(self._to_str(self.transmittance_4))
        out.append(self._to_str(self.front_reflectance_4))
        out.append(self._to_str(self.back_reflectance_4))
        out.append(self._to_str(self.wavelength_5))
        out.append(self._to_str(self.transmittance_5))
        out.append(self._to_str(self.front_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        out.append(self._to_str(self.back_reflectance_5))
        return ",".join(out)