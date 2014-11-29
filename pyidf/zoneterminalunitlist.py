from collections import OrderedDict

class ZoneTerminalUnitList(object):
    """ Corresponds to IDD object `ZoneTerminalUnitList`
        List of variable refrigerant flow (VRF) terminal units served by a given VRF condensing
        unit. See ZoneHVAC:TerminalUnit:VariableRefrigerantFlow and
        AirConditioner:VariableRefrigerantFlow.
    """
    internal_name = "ZoneTerminalUnitList"
    field_count = 21

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneTerminalUnitList`
        """
        self._data = OrderedDict()
        self._data["Zone Terminal Unit List Name"] = None
        self._data["Zone Terminal Unit Name 1"] = None
        self._data["Zone Terminal Unit Name 2"] = None
        self._data["Zone Terminal Unit Name 3"] = None
        self._data["Zone Terminal Unit Name 4"] = None
        self._data["Zone Terminal Unit Name 5"] = None
        self._data["Zone Terminal Unit Name 6"] = None
        self._data["Zone Terminal Unit Name 7"] = None
        self._data["Zone Terminal Unit Name 8"] = None
        self._data["Zone Terminal Unit Name 9"] = None
        self._data["Zone Terminal Unit Name 10"] = None
        self._data["Zone Terminal Unit Name 11"] = None
        self._data["Zone Terminal Unit Name 12"] = None
        self._data["Zone Terminal Unit Name 13"] = None
        self._data["Zone Terminal Unit Name 14"] = None
        self._data["Zone Terminal Unit Name 15"] = None
        self._data["Zone Terminal Unit Name 16"] = None
        self._data["Zone Terminal Unit Name 17"] = None
        self._data["Zone Terminal Unit Name 18"] = None
        self._data["Zone Terminal Unit Name 19"] = None
        self._data["Zone Terminal Unit Name 20"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.zone_terminal_unit_list_name = None
        else:
            self.zone_terminal_unit_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_1 = None
        else:
            self.zone_terminal_unit_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_2 = None
        else:
            self.zone_terminal_unit_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_3 = None
        else:
            self.zone_terminal_unit_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_4 = None
        else:
            self.zone_terminal_unit_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_5 = None
        else:
            self.zone_terminal_unit_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_6 = None
        else:
            self.zone_terminal_unit_name_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_7 = None
        else:
            self.zone_terminal_unit_name_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_8 = None
        else:
            self.zone_terminal_unit_name_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_9 = None
        else:
            self.zone_terminal_unit_name_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_10 = None
        else:
            self.zone_terminal_unit_name_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_11 = None
        else:
            self.zone_terminal_unit_name_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_12 = None
        else:
            self.zone_terminal_unit_name_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_13 = None
        else:
            self.zone_terminal_unit_name_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_14 = None
        else:
            self.zone_terminal_unit_name_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_15 = None
        else:
            self.zone_terminal_unit_name_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_16 = None
        else:
            self.zone_terminal_unit_name_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_17 = None
        else:
            self.zone_terminal_unit_name_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_18 = None
        else:
            self.zone_terminal_unit_name_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_19 = None
        else:
            self.zone_terminal_unit_name_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_20 = None
        else:
            self.zone_terminal_unit_name_20 = vals[i]
        i += 1

    @property
    def zone_terminal_unit_list_name(self):
        """Get zone_terminal_unit_list_name

        Returns:
            str: the value of `zone_terminal_unit_list_name` or None if not set
        """
        return self._data["Zone Terminal Unit List Name"]

    @zone_terminal_unit_list_name.setter
    def zone_terminal_unit_list_name(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_list_name`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_list_name`
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
                                 'for field `zone_terminal_unit_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_list_name`')

        self._data["Zone Terminal Unit List Name"] = value

    @property
    def zone_terminal_unit_name_1(self):
        """Get zone_terminal_unit_name_1

        Returns:
            str: the value of `zone_terminal_unit_name_1` or None if not set
        """
        return self._data["Zone Terminal Unit Name 1"]

    @zone_terminal_unit_name_1.setter
    def zone_terminal_unit_name_1(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_1`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_1`
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
                                 'for field `zone_terminal_unit_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_1`')

        self._data["Zone Terminal Unit Name 1"] = value

    @property
    def zone_terminal_unit_name_2(self):
        """Get zone_terminal_unit_name_2

        Returns:
            str: the value of `zone_terminal_unit_name_2` or None if not set
        """
        return self._data["Zone Terminal Unit Name 2"]

    @zone_terminal_unit_name_2.setter
    def zone_terminal_unit_name_2(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_2`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_2`
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
                                 'for field `zone_terminal_unit_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_2`')

        self._data["Zone Terminal Unit Name 2"] = value

    @property
    def zone_terminal_unit_name_3(self):
        """Get zone_terminal_unit_name_3

        Returns:
            str: the value of `zone_terminal_unit_name_3` or None if not set
        """
        return self._data["Zone Terminal Unit Name 3"]

    @zone_terminal_unit_name_3.setter
    def zone_terminal_unit_name_3(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_3`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_3`
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
                                 'for field `zone_terminal_unit_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_3`')

        self._data["Zone Terminal Unit Name 3"] = value

    @property
    def zone_terminal_unit_name_4(self):
        """Get zone_terminal_unit_name_4

        Returns:
            str: the value of `zone_terminal_unit_name_4` or None if not set
        """
        return self._data["Zone Terminal Unit Name 4"]

    @zone_terminal_unit_name_4.setter
    def zone_terminal_unit_name_4(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_4`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_4`
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
                                 'for field `zone_terminal_unit_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_4`')

        self._data["Zone Terminal Unit Name 4"] = value

    @property
    def zone_terminal_unit_name_5(self):
        """Get zone_terminal_unit_name_5

        Returns:
            str: the value of `zone_terminal_unit_name_5` or None if not set
        """
        return self._data["Zone Terminal Unit Name 5"]

    @zone_terminal_unit_name_5.setter
    def zone_terminal_unit_name_5(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_5`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_5`
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
                                 'for field `zone_terminal_unit_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_5`')

        self._data["Zone Terminal Unit Name 5"] = value

    @property
    def zone_terminal_unit_name_6(self):
        """Get zone_terminal_unit_name_6

        Returns:
            str: the value of `zone_terminal_unit_name_6` or None if not set
        """
        return self._data["Zone Terminal Unit Name 6"]

    @zone_terminal_unit_name_6.setter
    def zone_terminal_unit_name_6(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_6`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_6`
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
                                 'for field `zone_terminal_unit_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_6`')

        self._data["Zone Terminal Unit Name 6"] = value

    @property
    def zone_terminal_unit_name_7(self):
        """Get zone_terminal_unit_name_7

        Returns:
            str: the value of `zone_terminal_unit_name_7` or None if not set
        """
        return self._data["Zone Terminal Unit Name 7"]

    @zone_terminal_unit_name_7.setter
    def zone_terminal_unit_name_7(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_7`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_7`
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
                                 'for field `zone_terminal_unit_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_7`')

        self._data["Zone Terminal Unit Name 7"] = value

    @property
    def zone_terminal_unit_name_8(self):
        """Get zone_terminal_unit_name_8

        Returns:
            str: the value of `zone_terminal_unit_name_8` or None if not set
        """
        return self._data["Zone Terminal Unit Name 8"]

    @zone_terminal_unit_name_8.setter
    def zone_terminal_unit_name_8(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_8`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_8`
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
                                 'for field `zone_terminal_unit_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_8`')

        self._data["Zone Terminal Unit Name 8"] = value

    @property
    def zone_terminal_unit_name_9(self):
        """Get zone_terminal_unit_name_9

        Returns:
            str: the value of `zone_terminal_unit_name_9` or None if not set
        """
        return self._data["Zone Terminal Unit Name 9"]

    @zone_terminal_unit_name_9.setter
    def zone_terminal_unit_name_9(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_9`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_9`
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
                                 'for field `zone_terminal_unit_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_9`')

        self._data["Zone Terminal Unit Name 9"] = value

    @property
    def zone_terminal_unit_name_10(self):
        """Get zone_terminal_unit_name_10

        Returns:
            str: the value of `zone_terminal_unit_name_10` or None if not set
        """
        return self._data["Zone Terminal Unit Name 10"]

    @zone_terminal_unit_name_10.setter
    def zone_terminal_unit_name_10(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_10`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_10`
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
                                 'for field `zone_terminal_unit_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_10`')

        self._data["Zone Terminal Unit Name 10"] = value

    @property
    def zone_terminal_unit_name_11(self):
        """Get zone_terminal_unit_name_11

        Returns:
            str: the value of `zone_terminal_unit_name_11` or None if not set
        """
        return self._data["Zone Terminal Unit Name 11"]

    @zone_terminal_unit_name_11.setter
    def zone_terminal_unit_name_11(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_11`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_11`
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
                                 'for field `zone_terminal_unit_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_11`')

        self._data["Zone Terminal Unit Name 11"] = value

    @property
    def zone_terminal_unit_name_12(self):
        """Get zone_terminal_unit_name_12

        Returns:
            str: the value of `zone_terminal_unit_name_12` or None if not set
        """
        return self._data["Zone Terminal Unit Name 12"]

    @zone_terminal_unit_name_12.setter
    def zone_terminal_unit_name_12(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_12`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_12`
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
                                 'for field `zone_terminal_unit_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_12`')

        self._data["Zone Terminal Unit Name 12"] = value

    @property
    def zone_terminal_unit_name_13(self):
        """Get zone_terminal_unit_name_13

        Returns:
            str: the value of `zone_terminal_unit_name_13` or None if not set
        """
        return self._data["Zone Terminal Unit Name 13"]

    @zone_terminal_unit_name_13.setter
    def zone_terminal_unit_name_13(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_13`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_13`
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
                                 'for field `zone_terminal_unit_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_13`')

        self._data["Zone Terminal Unit Name 13"] = value

    @property
    def zone_terminal_unit_name_14(self):
        """Get zone_terminal_unit_name_14

        Returns:
            str: the value of `zone_terminal_unit_name_14` or None if not set
        """
        return self._data["Zone Terminal Unit Name 14"]

    @zone_terminal_unit_name_14.setter
    def zone_terminal_unit_name_14(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_14`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_14`
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
                                 'for field `zone_terminal_unit_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_14`')

        self._data["Zone Terminal Unit Name 14"] = value

    @property
    def zone_terminal_unit_name_15(self):
        """Get zone_terminal_unit_name_15

        Returns:
            str: the value of `zone_terminal_unit_name_15` or None if not set
        """
        return self._data["Zone Terminal Unit Name 15"]

    @zone_terminal_unit_name_15.setter
    def zone_terminal_unit_name_15(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_15`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_15`
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
                                 'for field `zone_terminal_unit_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_15`')

        self._data["Zone Terminal Unit Name 15"] = value

    @property
    def zone_terminal_unit_name_16(self):
        """Get zone_terminal_unit_name_16

        Returns:
            str: the value of `zone_terminal_unit_name_16` or None if not set
        """
        return self._data["Zone Terminal Unit Name 16"]

    @zone_terminal_unit_name_16.setter
    def zone_terminal_unit_name_16(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_16`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_16`
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
                                 'for field `zone_terminal_unit_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_16`')

        self._data["Zone Terminal Unit Name 16"] = value

    @property
    def zone_terminal_unit_name_17(self):
        """Get zone_terminal_unit_name_17

        Returns:
            str: the value of `zone_terminal_unit_name_17` or None if not set
        """
        return self._data["Zone Terminal Unit Name 17"]

    @zone_terminal_unit_name_17.setter
    def zone_terminal_unit_name_17(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_17`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_17`
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
                                 'for field `zone_terminal_unit_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_17`')

        self._data["Zone Terminal Unit Name 17"] = value

    @property
    def zone_terminal_unit_name_18(self):
        """Get zone_terminal_unit_name_18

        Returns:
            str: the value of `zone_terminal_unit_name_18` or None if not set
        """
        return self._data["Zone Terminal Unit Name 18"]

    @zone_terminal_unit_name_18.setter
    def zone_terminal_unit_name_18(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_18`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_18`
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
                                 'for field `zone_terminal_unit_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_18`')

        self._data["Zone Terminal Unit Name 18"] = value

    @property
    def zone_terminal_unit_name_19(self):
        """Get zone_terminal_unit_name_19

        Returns:
            str: the value of `zone_terminal_unit_name_19` or None if not set
        """
        return self._data["Zone Terminal Unit Name 19"]

    @zone_terminal_unit_name_19.setter
    def zone_terminal_unit_name_19(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_19`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_19`
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
                                 'for field `zone_terminal_unit_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_19`')

        self._data["Zone Terminal Unit Name 19"] = value

    @property
    def zone_terminal_unit_name_20(self):
        """Get zone_terminal_unit_name_20

        Returns:
            str: the value of `zone_terminal_unit_name_20` or None if not set
        """
        return self._data["Zone Terminal Unit Name 20"]

    @zone_terminal_unit_name_20.setter
    def zone_terminal_unit_name_20(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_20`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_20`
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
                                 'for field `zone_terminal_unit_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_20`')

        self._data["Zone Terminal Unit Name 20"] = value

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
        out.append(self._to_str(self.zone_terminal_unit_list_name))
        out.append(self._to_str(self.zone_terminal_unit_name_1))
        out.append(self._to_str(self.zone_terminal_unit_name_2))
        out.append(self._to_str(self.zone_terminal_unit_name_3))
        out.append(self._to_str(self.zone_terminal_unit_name_4))
        out.append(self._to_str(self.zone_terminal_unit_name_5))
        out.append(self._to_str(self.zone_terminal_unit_name_6))
        out.append(self._to_str(self.zone_terminal_unit_name_7))
        out.append(self._to_str(self.zone_terminal_unit_name_8))
        out.append(self._to_str(self.zone_terminal_unit_name_9))
        out.append(self._to_str(self.zone_terminal_unit_name_10))
        out.append(self._to_str(self.zone_terminal_unit_name_11))
        out.append(self._to_str(self.zone_terminal_unit_name_12))
        out.append(self._to_str(self.zone_terminal_unit_name_13))
        out.append(self._to_str(self.zone_terminal_unit_name_14))
        out.append(self._to_str(self.zone_terminal_unit_name_15))
        out.append(self._to_str(self.zone_terminal_unit_name_16))
        out.append(self._to_str(self.zone_terminal_unit_name_17))
        out.append(self._to_str(self.zone_terminal_unit_name_18))
        out.append(self._to_str(self.zone_terminal_unit_name_19))
        out.append(self._to_str(self.zone_terminal_unit_name_20))
        return ",".join(out)