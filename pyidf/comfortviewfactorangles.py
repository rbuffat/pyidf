from collections import OrderedDict

class ComfortViewFactorAngles(object):
    """ Corresponds to IDD object `ComfortViewFactorAngles`
        Used to specify radiant view factors for thermal comfort calculations.
    """
    internal_name = "ComfortViewFactorAngles"
    field_count = 42

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ComfortViewFactorAngles`
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