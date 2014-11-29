from collections import OrderedDict

class CondenserEquipmentList(object):
    """ Corresponds to IDD object `CondenserEquipmentList`
        List condenser equipment in order of operating priority, 1st in list will be used 1st, etc
        Use only condenser equipment in this list.
        If no equipment object types and equipment names are specified, then the corresponding
        PlantEquipmentOperation:* object will assume all available condenser equipment for the loop
        should be OFF (not operate) within the specified lower/upper limit.
    """
    internal_name = "CondenserEquipmentList"
    field_count = 21

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CondenserEquipmentList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Equipment 1 Object Type"] = None
        self._data["Equipment 1 Name"] = None
        self._data["Equipment 2 Object Type"] = None
        self._data["Equipment 2 Name"] = None
        self._data["Equipment 3 Object Type"] = None
        self._data["Equipment 3 Name"] = None
        self._data["Equipment 4 Object Type"] = None
        self._data["Equipment 4 Name"] = None
        self._data["Equipment 5 Object Type"] = None
        self._data["Equipment 5 Name"] = None
        self._data["Equipment 6 Object Type"] = None
        self._data["Equipment 6 Name"] = None
        self._data["Equipment 7 Object Type"] = None
        self._data["Equipment 7 Name"] = None
        self._data["Equipment 8 Object Type"] = None
        self._data["Equipment 8 Name"] = None
        self._data["Equipment 9 Object Type"] = None
        self._data["Equipment 9 Name"] = None
        self._data["Equipment 10 Object Type"] = None
        self._data["Equipment 10 Name"] = None

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
            self.equipment_1_object_type = None
        else:
            self.equipment_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_1_name = None
        else:
            self.equipment_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_2_object_type = None
        else:
            self.equipment_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_2_name = None
        else:
            self.equipment_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_3_object_type = None
        else:
            self.equipment_3_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_3_name = None
        else:
            self.equipment_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_4_object_type = None
        else:
            self.equipment_4_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_4_name = None
        else:
            self.equipment_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_5_object_type = None
        else:
            self.equipment_5_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_5_name = None
        else:
            self.equipment_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_6_object_type = None
        else:
            self.equipment_6_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_6_name = None
        else:
            self.equipment_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_7_object_type = None
        else:
            self.equipment_7_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_7_name = None
        else:
            self.equipment_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_8_object_type = None
        else:
            self.equipment_8_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_8_name = None
        else:
            self.equipment_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_9_object_type = None
        else:
            self.equipment_9_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_9_name = None
        else:
            self.equipment_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_10_object_type = None
        else:
            self.equipment_10_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_10_name = None
        else:
            self.equipment_10_name = vals[i]
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
    def equipment_1_object_type(self):
        """Get equipment_1_object_type

        Returns:
            str: the value of `equipment_1_object_type` or None if not set
        """
        return self._data["Equipment 1 Object Type"]

    @equipment_1_object_type.setter
    def equipment_1_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_1_object_type`

        Args:
            value (str): value for IDD Field `equipment_1_object_type`
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
                                 'for field `equipment_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_1_object_type`')

        self._data["Equipment 1 Object Type"] = value

    @property
    def equipment_1_name(self):
        """Get equipment_1_name

        Returns:
            str: the value of `equipment_1_name` or None if not set
        """
        return self._data["Equipment 1 Name"]

    @equipment_1_name.setter
    def equipment_1_name(self, value=None):
        """  Corresponds to IDD Field `equipment_1_name`

        Args:
            value (str): value for IDD Field `equipment_1_name`
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
                                 'for field `equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_1_name`')

        self._data["Equipment 1 Name"] = value

    @property
    def equipment_2_object_type(self):
        """Get equipment_2_object_type

        Returns:
            str: the value of `equipment_2_object_type` or None if not set
        """
        return self._data["Equipment 2 Object Type"]

    @equipment_2_object_type.setter
    def equipment_2_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_2_object_type`

        Args:
            value (str): value for IDD Field `equipment_2_object_type`
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
                                 'for field `equipment_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_2_object_type`')

        self._data["Equipment 2 Object Type"] = value

    @property
    def equipment_2_name(self):
        """Get equipment_2_name

        Returns:
            str: the value of `equipment_2_name` or None if not set
        """
        return self._data["Equipment 2 Name"]

    @equipment_2_name.setter
    def equipment_2_name(self, value=None):
        """  Corresponds to IDD Field `equipment_2_name`

        Args:
            value (str): value for IDD Field `equipment_2_name`
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
                                 'for field `equipment_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_2_name`')

        self._data["Equipment 2 Name"] = value

    @property
    def equipment_3_object_type(self):
        """Get equipment_3_object_type

        Returns:
            str: the value of `equipment_3_object_type` or None if not set
        """
        return self._data["Equipment 3 Object Type"]

    @equipment_3_object_type.setter
    def equipment_3_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_3_object_type`

        Args:
            value (str): value for IDD Field `equipment_3_object_type`
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
                                 'for field `equipment_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_3_object_type`')

        self._data["Equipment 3 Object Type"] = value

    @property
    def equipment_3_name(self):
        """Get equipment_3_name

        Returns:
            str: the value of `equipment_3_name` or None if not set
        """
        return self._data["Equipment 3 Name"]

    @equipment_3_name.setter
    def equipment_3_name(self, value=None):
        """  Corresponds to IDD Field `equipment_3_name`

        Args:
            value (str): value for IDD Field `equipment_3_name`
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
                                 'for field `equipment_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_3_name`')

        self._data["Equipment 3 Name"] = value

    @property
    def equipment_4_object_type(self):
        """Get equipment_4_object_type

        Returns:
            str: the value of `equipment_4_object_type` or None if not set
        """
        return self._data["Equipment 4 Object Type"]

    @equipment_4_object_type.setter
    def equipment_4_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_4_object_type`

        Args:
            value (str): value for IDD Field `equipment_4_object_type`
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
                                 'for field `equipment_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_4_object_type`')

        self._data["Equipment 4 Object Type"] = value

    @property
    def equipment_4_name(self):
        """Get equipment_4_name

        Returns:
            str: the value of `equipment_4_name` or None if not set
        """
        return self._data["Equipment 4 Name"]

    @equipment_4_name.setter
    def equipment_4_name(self, value=None):
        """  Corresponds to IDD Field `equipment_4_name`

        Args:
            value (str): value for IDD Field `equipment_4_name`
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
                                 'for field `equipment_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_4_name`')

        self._data["Equipment 4 Name"] = value

    @property
    def equipment_5_object_type(self):
        """Get equipment_5_object_type

        Returns:
            str: the value of `equipment_5_object_type` or None if not set
        """
        return self._data["Equipment 5 Object Type"]

    @equipment_5_object_type.setter
    def equipment_5_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_5_object_type`

        Args:
            value (str): value for IDD Field `equipment_5_object_type`
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
                                 'for field `equipment_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_5_object_type`')

        self._data["Equipment 5 Object Type"] = value

    @property
    def equipment_5_name(self):
        """Get equipment_5_name

        Returns:
            str: the value of `equipment_5_name` or None if not set
        """
        return self._data["Equipment 5 Name"]

    @equipment_5_name.setter
    def equipment_5_name(self, value=None):
        """  Corresponds to IDD Field `equipment_5_name`

        Args:
            value (str): value for IDD Field `equipment_5_name`
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
                                 'for field `equipment_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_5_name`')

        self._data["Equipment 5 Name"] = value

    @property
    def equipment_6_object_type(self):
        """Get equipment_6_object_type

        Returns:
            str: the value of `equipment_6_object_type` or None if not set
        """
        return self._data["Equipment 6 Object Type"]

    @equipment_6_object_type.setter
    def equipment_6_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_6_object_type`

        Args:
            value (str): value for IDD Field `equipment_6_object_type`
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
                                 'for field `equipment_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_6_object_type`')

        self._data["Equipment 6 Object Type"] = value

    @property
    def equipment_6_name(self):
        """Get equipment_6_name

        Returns:
            str: the value of `equipment_6_name` or None if not set
        """
        return self._data["Equipment 6 Name"]

    @equipment_6_name.setter
    def equipment_6_name(self, value=None):
        """  Corresponds to IDD Field `equipment_6_name`

        Args:
            value (str): value for IDD Field `equipment_6_name`
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
                                 'for field `equipment_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_6_name`')

        self._data["Equipment 6 Name"] = value

    @property
    def equipment_7_object_type(self):
        """Get equipment_7_object_type

        Returns:
            str: the value of `equipment_7_object_type` or None if not set
        """
        return self._data["Equipment 7 Object Type"]

    @equipment_7_object_type.setter
    def equipment_7_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_7_object_type`

        Args:
            value (str): value for IDD Field `equipment_7_object_type`
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
                                 'for field `equipment_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_7_object_type`')

        self._data["Equipment 7 Object Type"] = value

    @property
    def equipment_7_name(self):
        """Get equipment_7_name

        Returns:
            str: the value of `equipment_7_name` or None if not set
        """
        return self._data["Equipment 7 Name"]

    @equipment_7_name.setter
    def equipment_7_name(self, value=None):
        """  Corresponds to IDD Field `equipment_7_name`

        Args:
            value (str): value for IDD Field `equipment_7_name`
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
                                 'for field `equipment_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_7_name`')

        self._data["Equipment 7 Name"] = value

    @property
    def equipment_8_object_type(self):
        """Get equipment_8_object_type

        Returns:
            str: the value of `equipment_8_object_type` or None if not set
        """
        return self._data["Equipment 8 Object Type"]

    @equipment_8_object_type.setter
    def equipment_8_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_8_object_type`

        Args:
            value (str): value for IDD Field `equipment_8_object_type`
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
                                 'for field `equipment_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_8_object_type`')

        self._data["Equipment 8 Object Type"] = value

    @property
    def equipment_8_name(self):
        """Get equipment_8_name

        Returns:
            str: the value of `equipment_8_name` or None if not set
        """
        return self._data["Equipment 8 Name"]

    @equipment_8_name.setter
    def equipment_8_name(self, value=None):
        """  Corresponds to IDD Field `equipment_8_name`

        Args:
            value (str): value for IDD Field `equipment_8_name`
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
                                 'for field `equipment_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_8_name`')

        self._data["Equipment 8 Name"] = value

    @property
    def equipment_9_object_type(self):
        """Get equipment_9_object_type

        Returns:
            str: the value of `equipment_9_object_type` or None if not set
        """
        return self._data["Equipment 9 Object Type"]

    @equipment_9_object_type.setter
    def equipment_9_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_9_object_type`

        Args:
            value (str): value for IDD Field `equipment_9_object_type`
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
                                 'for field `equipment_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_9_object_type`')

        self._data["Equipment 9 Object Type"] = value

    @property
    def equipment_9_name(self):
        """Get equipment_9_name

        Returns:
            str: the value of `equipment_9_name` or None if not set
        """
        return self._data["Equipment 9 Name"]

    @equipment_9_name.setter
    def equipment_9_name(self, value=None):
        """  Corresponds to IDD Field `equipment_9_name`

        Args:
            value (str): value for IDD Field `equipment_9_name`
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
                                 'for field `equipment_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_9_name`')

        self._data["Equipment 9 Name"] = value

    @property
    def equipment_10_object_type(self):
        """Get equipment_10_object_type

        Returns:
            str: the value of `equipment_10_object_type` or None if not set
        """
        return self._data["Equipment 10 Object Type"]

    @equipment_10_object_type.setter
    def equipment_10_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_10_object_type`

        Args:
            value (str): value for IDD Field `equipment_10_object_type`
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
                                 'for field `equipment_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_10_object_type`')

        self._data["Equipment 10 Object Type"] = value

    @property
    def equipment_10_name(self):
        """Get equipment_10_name

        Returns:
            str: the value of `equipment_10_name` or None if not set
        """
        return self._data["Equipment 10 Name"]

    @equipment_10_name.setter
    def equipment_10_name(self, value=None):
        """  Corresponds to IDD Field `equipment_10_name`

        Args:
            value (str): value for IDD Field `equipment_10_name`
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
                                 'for field `equipment_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_10_name`')

        self._data["Equipment 10 Name"] = value

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
        out.append(self._to_str(self.equipment_1_object_type))
        out.append(self._to_str(self.equipment_1_name))
        out.append(self._to_str(self.equipment_2_object_type))
        out.append(self._to_str(self.equipment_2_name))
        out.append(self._to_str(self.equipment_3_object_type))
        out.append(self._to_str(self.equipment_3_name))
        out.append(self._to_str(self.equipment_4_object_type))
        out.append(self._to_str(self.equipment_4_name))
        out.append(self._to_str(self.equipment_5_object_type))
        out.append(self._to_str(self.equipment_5_name))
        out.append(self._to_str(self.equipment_6_object_type))
        out.append(self._to_str(self.equipment_6_name))
        out.append(self._to_str(self.equipment_7_object_type))
        out.append(self._to_str(self.equipment_7_name))
        out.append(self._to_str(self.equipment_8_object_type))
        out.append(self._to_str(self.equipment_8_name))
        out.append(self._to_str(self.equipment_9_object_type))
        out.append(self._to_str(self.equipment_9_name))
        out.append(self._to_str(self.equipment_10_object_type))
        out.append(self._to_str(self.equipment_10_name))
        return ",".join(out)