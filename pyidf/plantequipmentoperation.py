from collections import OrderedDict

class PlantEquipmentOperationUncontrolled(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:Uncontrolled`
        Plant equipment operation scheme for uncontrolled operation. Specifies a group of
        equipment that runs if the loop is active, unless turned off by the loop flow resolver
        to maintain continuity in the fluid loop.
    """
    internal_name = "PlantEquipmentOperation:Uncontrolled"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:Uncontrolled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Equipment List Name"] = None

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
            self.equipment_list_name = None
        else:
            self.equipment_list_name = vals[i]
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
    def equipment_list_name(self):
        """Get equipment_list_name

        Returns:
            str: the value of `equipment_list_name` or None if not set
        """
        return self._data["Equipment List Name"]

    @equipment_list_name.setter
    def equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `equipment_list_name`

        Args:
            value (str): value for IDD Field `equipment_list_name`
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
                                 'for field `equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_list_name`')

        self._data["Equipment List Name"] = value

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
        out.append(self._to_str(self.equipment_list_name))
        return ",".join(out)

class PlantEquipmentOperationCoolingLoad(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:CoolingLoad`
        Plant equipment operation scheme for cooling load range operation. Specifies one or
        more groups of equipment which are available to operate for successive cooling load
        ranges.
    """
    internal_name = "PlantEquipmentOperation:CoolingLoad"
    field_count = 31

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:CoolingLoad`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Load Range 1 Lower Limit"] = None
        self._data["Load Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Load Range 2 Lower Limit"] = None
        self._data["Load Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Load Range 3 Lower Limit"] = None
        self._data["Load Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Load Range 4 Lower Limit"] = None
        self._data["Load Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Load Range 5 Lower Limit"] = None
        self._data["Load Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Load Range 6 Lower Limit"] = None
        self._data["Load Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Load Range 7 Lower Limit"] = None
        self._data["Load Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Load Range 8 Lower Limit"] = None
        self._data["Load Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Load Range 9 Lower Limit"] = None
        self._data["Load Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Load Range 10 Lower Limit"] = None
        self._data["Load Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None

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
            self.load_range_1_lower_limit = None
        else:
            self.load_range_1_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_1_upper_limit = None
        else:
            self.load_range_1_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_2_lower_limit = None
        else:
            self.load_range_2_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_2_upper_limit = None
        else:
            self.load_range_2_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_3_lower_limit = None
        else:
            self.load_range_3_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_3_upper_limit = None
        else:
            self.load_range_3_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_4_lower_limit = None
        else:
            self.load_range_4_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_4_upper_limit = None
        else:
            self.load_range_4_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_5_lower_limit = None
        else:
            self.load_range_5_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_5_upper_limit = None
        else:
            self.load_range_5_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_6_lower_limit = None
        else:
            self.load_range_6_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_6_upper_limit = None
        else:
            self.load_range_6_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_7_lower_limit = None
        else:
            self.load_range_7_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_7_upper_limit = None
        else:
            self.load_range_7_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_8_lower_limit = None
        else:
            self.load_range_8_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_8_upper_limit = None
        else:
            self.load_range_8_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_9_lower_limit = None
        else:
            self.load_range_9_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_9_upper_limit = None
        else:
            self.load_range_9_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_10_lower_limit = None
        else:
            self.load_range_10_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_10_upper_limit = None
        else:
            self.load_range_10_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def load_range_1_lower_limit(self):
        """Get load_range_1_lower_limit

        Returns:
            float: the value of `load_range_1_lower_limit` or None if not set
        """
        return self._data["Load Range 1 Lower Limit"]

    @load_range_1_lower_limit.setter
    def load_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_1_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_1_lower_limit`
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
                                 'for field `load_range_1_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_1_lower_limit`')

        self._data["Load Range 1 Lower Limit"] = value

    @property
    def load_range_1_upper_limit(self):
        """Get load_range_1_upper_limit

        Returns:
            float: the value of `load_range_1_upper_limit` or None if not set
        """
        return self._data["Load Range 1 Upper Limit"]

    @load_range_1_upper_limit.setter
    def load_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_1_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_1_upper_limit`
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
                                 'for field `load_range_1_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_1_upper_limit`')

        self._data["Load Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_1_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_1_equipment_list_name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')

        self._data["Range 1 Equipment List Name"] = value

    @property
    def load_range_2_lower_limit(self):
        """Get load_range_2_lower_limit

        Returns:
            float: the value of `load_range_2_lower_limit` or None if not set
        """
        return self._data["Load Range 2 Lower Limit"]

    @load_range_2_lower_limit.setter
    def load_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_2_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_2_lower_limit`
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
                                 'for field `load_range_2_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_2_lower_limit`')

        self._data["Load Range 2 Lower Limit"] = value

    @property
    def load_range_2_upper_limit(self):
        """Get load_range_2_upper_limit

        Returns:
            float: the value of `load_range_2_upper_limit` or None if not set
        """
        return self._data["Load Range 2 Upper Limit"]

    @load_range_2_upper_limit.setter
    def load_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_2_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_2_upper_limit`
                Unit: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `load_range_2_upper_limit`'.format(value))

        self._data["Load Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_2_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_2_equipment_list_name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')

        self._data["Range 2 Equipment List Name"] = value

    @property
    def load_range_3_lower_limit(self):
        """Get load_range_3_lower_limit

        Returns:
            float: the value of `load_range_3_lower_limit` or None if not set
        """
        return self._data["Load Range 3 Lower Limit"]

    @load_range_3_lower_limit.setter
    def load_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_3_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_3_lower_limit`
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
                                 'for field `load_range_3_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_3_lower_limit`')

        self._data["Load Range 3 Lower Limit"] = value

    @property
    def load_range_3_upper_limit(self):
        """Get load_range_3_upper_limit

        Returns:
            float: the value of `load_range_3_upper_limit` or None if not set
        """
        return self._data["Load Range 3 Upper Limit"]

    @load_range_3_upper_limit.setter
    def load_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_3_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_3_upper_limit`
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
                                 'for field `load_range_3_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_3_upper_limit`')

        self._data["Load Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_3_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_3_equipment_list_name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')

        self._data["Range 3 Equipment List Name"] = value

    @property
    def load_range_4_lower_limit(self):
        """Get load_range_4_lower_limit

        Returns:
            float: the value of `load_range_4_lower_limit` or None if not set
        """
        return self._data["Load Range 4 Lower Limit"]

    @load_range_4_lower_limit.setter
    def load_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_4_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_4_lower_limit`
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
                                 'for field `load_range_4_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_4_lower_limit`')

        self._data["Load Range 4 Lower Limit"] = value

    @property
    def load_range_4_upper_limit(self):
        """Get load_range_4_upper_limit

        Returns:
            float: the value of `load_range_4_upper_limit` or None if not set
        """
        return self._data["Load Range 4 Upper Limit"]

    @load_range_4_upper_limit.setter
    def load_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_4_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_4_upper_limit`
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
                                 'for field `load_range_4_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_4_upper_limit`')

        self._data["Load Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_4_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_4_equipment_list_name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')

        self._data["Range 4 Equipment List Name"] = value

    @property
    def load_range_5_lower_limit(self):
        """Get load_range_5_lower_limit

        Returns:
            float: the value of `load_range_5_lower_limit` or None if not set
        """
        return self._data["Load Range 5 Lower Limit"]

    @load_range_5_lower_limit.setter
    def load_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_5_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_5_lower_limit`
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
                                 'for field `load_range_5_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_5_lower_limit`')

        self._data["Load Range 5 Lower Limit"] = value

    @property
    def load_range_5_upper_limit(self):
        """Get load_range_5_upper_limit

        Returns:
            float: the value of `load_range_5_upper_limit` or None if not set
        """
        return self._data["Load Range 5 Upper Limit"]

    @load_range_5_upper_limit.setter
    def load_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_5_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_5_upper_limit`
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
                                 'for field `load_range_5_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_5_upper_limit`')

        self._data["Load Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_5_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_5_equipment_list_name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')

        self._data["Range 5 Equipment List Name"] = value

    @property
    def load_range_6_lower_limit(self):
        """Get load_range_6_lower_limit

        Returns:
            float: the value of `load_range_6_lower_limit` or None if not set
        """
        return self._data["Load Range 6 Lower Limit"]

    @load_range_6_lower_limit.setter
    def load_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_6_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_6_lower_limit`
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
                                 'for field `load_range_6_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_6_lower_limit`')

        self._data["Load Range 6 Lower Limit"] = value

    @property
    def load_range_6_upper_limit(self):
        """Get load_range_6_upper_limit

        Returns:
            float: the value of `load_range_6_upper_limit` or None if not set
        """
        return self._data["Load Range 6 Upper Limit"]

    @load_range_6_upper_limit.setter
    def load_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_6_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_6_upper_limit`
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
                                 'for field `load_range_6_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_6_upper_limit`')

        self._data["Load Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_6_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_6_equipment_list_name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')

        self._data["Range 6 Equipment List Name"] = value

    @property
    def load_range_7_lower_limit(self):
        """Get load_range_7_lower_limit

        Returns:
            float: the value of `load_range_7_lower_limit` or None if not set
        """
        return self._data["Load Range 7 Lower Limit"]

    @load_range_7_lower_limit.setter
    def load_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_7_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_7_lower_limit`
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
                                 'for field `load_range_7_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_7_lower_limit`')

        self._data["Load Range 7 Lower Limit"] = value

    @property
    def load_range_7_upper_limit(self):
        """Get load_range_7_upper_limit

        Returns:
            float: the value of `load_range_7_upper_limit` or None if not set
        """
        return self._data["Load Range 7 Upper Limit"]

    @load_range_7_upper_limit.setter
    def load_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_7_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_7_upper_limit`
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
                                 'for field `load_range_7_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_7_upper_limit`')

        self._data["Load Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_7_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_7_equipment_list_name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')

        self._data["Range 7 Equipment List Name"] = value

    @property
    def load_range_8_lower_limit(self):
        """Get load_range_8_lower_limit

        Returns:
            float: the value of `load_range_8_lower_limit` or None if not set
        """
        return self._data["Load Range 8 Lower Limit"]

    @load_range_8_lower_limit.setter
    def load_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_8_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_8_lower_limit`
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
                                 'for field `load_range_8_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_8_lower_limit`')

        self._data["Load Range 8 Lower Limit"] = value

    @property
    def load_range_8_upper_limit(self):
        """Get load_range_8_upper_limit

        Returns:
            float: the value of `load_range_8_upper_limit` or None if not set
        """
        return self._data["Load Range 8 Upper Limit"]

    @load_range_8_upper_limit.setter
    def load_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_8_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_8_upper_limit`
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
                                 'for field `load_range_8_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_8_upper_limit`')

        self._data["Load Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_8_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_8_equipment_list_name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')

        self._data["Range 8 Equipment List Name"] = value

    @property
    def load_range_9_lower_limit(self):
        """Get load_range_9_lower_limit

        Returns:
            float: the value of `load_range_9_lower_limit` or None if not set
        """
        return self._data["Load Range 9 Lower Limit"]

    @load_range_9_lower_limit.setter
    def load_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_9_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_9_lower_limit`
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
                                 'for field `load_range_9_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_9_lower_limit`')

        self._data["Load Range 9 Lower Limit"] = value

    @property
    def load_range_9_upper_limit(self):
        """Get load_range_9_upper_limit

        Returns:
            float: the value of `load_range_9_upper_limit` or None if not set
        """
        return self._data["Load Range 9 Upper Limit"]

    @load_range_9_upper_limit.setter
    def load_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_9_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_9_upper_limit`
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
                                 'for field `load_range_9_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_9_upper_limit`')

        self._data["Load Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_9_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_9_equipment_list_name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')

        self._data["Range 9 Equipment List Name"] = value

    @property
    def load_range_10_lower_limit(self):
        """Get load_range_10_lower_limit

        Returns:
            float: the value of `load_range_10_lower_limit` or None if not set
        """
        return self._data["Load Range 10 Lower Limit"]

    @load_range_10_lower_limit.setter
    def load_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_10_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_10_lower_limit`
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
                                 'for field `load_range_10_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_10_lower_limit`')

        self._data["Load Range 10 Lower Limit"] = value

    @property
    def load_range_10_upper_limit(self):
        """Get load_range_10_upper_limit

        Returns:
            float: the value of `load_range_10_upper_limit` or None if not set
        """
        return self._data["Load Range 10 Upper Limit"]

    @load_range_10_upper_limit.setter
    def load_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_10_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_10_upper_limit`
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
                                 'for field `load_range_10_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_10_upper_limit`')

        self._data["Load Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_10_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_10_equipment_list_name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')

        self._data["Range 10 Equipment List Name"] = value

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
        out.append(self._to_str(self.load_range_1_lower_limit))
        out.append(self._to_str(self.load_range_1_upper_limit))
        out.append(self._to_str(self.range_1_equipment_list_name))
        out.append(self._to_str(self.load_range_2_lower_limit))
        out.append(self._to_str(self.load_range_2_upper_limit))
        out.append(self._to_str(self.range_2_equipment_list_name))
        out.append(self._to_str(self.load_range_3_lower_limit))
        out.append(self._to_str(self.load_range_3_upper_limit))
        out.append(self._to_str(self.range_3_equipment_list_name))
        out.append(self._to_str(self.load_range_4_lower_limit))
        out.append(self._to_str(self.load_range_4_upper_limit))
        out.append(self._to_str(self.range_4_equipment_list_name))
        out.append(self._to_str(self.load_range_5_lower_limit))
        out.append(self._to_str(self.load_range_5_upper_limit))
        out.append(self._to_str(self.range_5_equipment_list_name))
        out.append(self._to_str(self.load_range_6_lower_limit))
        out.append(self._to_str(self.load_range_6_upper_limit))
        out.append(self._to_str(self.range_6_equipment_list_name))
        out.append(self._to_str(self.load_range_7_lower_limit))
        out.append(self._to_str(self.load_range_7_upper_limit))
        out.append(self._to_str(self.range_7_equipment_list_name))
        out.append(self._to_str(self.load_range_8_lower_limit))
        out.append(self._to_str(self.load_range_8_upper_limit))
        out.append(self._to_str(self.range_8_equipment_list_name))
        out.append(self._to_str(self.load_range_9_lower_limit))
        out.append(self._to_str(self.load_range_9_upper_limit))
        out.append(self._to_str(self.range_9_equipment_list_name))
        out.append(self._to_str(self.load_range_10_lower_limit))
        out.append(self._to_str(self.load_range_10_upper_limit))
        out.append(self._to_str(self.range_10_equipment_list_name))
        return ",".join(out)

class PlantEquipmentOperationHeatingLoad(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:HeatingLoad`
        Plant equipment operation scheme for heating load range operation. Specifies one or
        more groups of equipment which are available to operate for successive heating load
        ranges.
    """
    internal_name = "PlantEquipmentOperation:HeatingLoad"
    field_count = 31

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:HeatingLoad`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Load Range 1 Lower Limit"] = None
        self._data["Load Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Load Range 2 Lower Limit"] = None
        self._data["Load Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Load Range 3 Lower Limit"] = None
        self._data["Load Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Load Range 4 Lower Limit"] = None
        self._data["Load Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Load Range 5 Lower Limit"] = None
        self._data["Load Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Load Range 6 Lower Limit"] = None
        self._data["Load Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Load Range 7 Lower Limit"] = None
        self._data["Load Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Load Range 8 Lower Limit"] = None
        self._data["Load Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Load Range 9 Lower Limit"] = None
        self._data["Load Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Load Range 10 Lower Limit"] = None
        self._data["Load Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None

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
            self.load_range_1_lower_limit = None
        else:
            self.load_range_1_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_1_upper_limit = None
        else:
            self.load_range_1_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_2_lower_limit = None
        else:
            self.load_range_2_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_2_upper_limit = None
        else:
            self.load_range_2_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_3_lower_limit = None
        else:
            self.load_range_3_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_3_upper_limit = None
        else:
            self.load_range_3_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_4_lower_limit = None
        else:
            self.load_range_4_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_4_upper_limit = None
        else:
            self.load_range_4_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_5_lower_limit = None
        else:
            self.load_range_5_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_5_upper_limit = None
        else:
            self.load_range_5_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_6_lower_limit = None
        else:
            self.load_range_6_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_6_upper_limit = None
        else:
            self.load_range_6_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_7_lower_limit = None
        else:
            self.load_range_7_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_7_upper_limit = None
        else:
            self.load_range_7_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_8_lower_limit = None
        else:
            self.load_range_8_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_8_upper_limit = None
        else:
            self.load_range_8_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_9_lower_limit = None
        else:
            self.load_range_9_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_9_upper_limit = None
        else:
            self.load_range_9_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_10_lower_limit = None
        else:
            self.load_range_10_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_range_10_upper_limit = None
        else:
            self.load_range_10_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def load_range_1_lower_limit(self):
        """Get load_range_1_lower_limit

        Returns:
            float: the value of `load_range_1_lower_limit` or None if not set
        """
        return self._data["Load Range 1 Lower Limit"]

    @load_range_1_lower_limit.setter
    def load_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_1_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_1_lower_limit`
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
                                 'for field `load_range_1_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_1_lower_limit`')

        self._data["Load Range 1 Lower Limit"] = value

    @property
    def load_range_1_upper_limit(self):
        """Get load_range_1_upper_limit

        Returns:
            float: the value of `load_range_1_upper_limit` or None if not set
        """
        return self._data["Load Range 1 Upper Limit"]

    @load_range_1_upper_limit.setter
    def load_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_1_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_1_upper_limit`
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
                                 'for field `load_range_1_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_1_upper_limit`')

        self._data["Load Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_1_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_1_equipment_list_name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')

        self._data["Range 1 Equipment List Name"] = value

    @property
    def load_range_2_lower_limit(self):
        """Get load_range_2_lower_limit

        Returns:
            float: the value of `load_range_2_lower_limit` or None if not set
        """
        return self._data["Load Range 2 Lower Limit"]

    @load_range_2_lower_limit.setter
    def load_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_2_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_2_lower_limit`
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
                                 'for field `load_range_2_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_2_lower_limit`')

        self._data["Load Range 2 Lower Limit"] = value

    @property
    def load_range_2_upper_limit(self):
        """Get load_range_2_upper_limit

        Returns:
            float: the value of `load_range_2_upper_limit` or None if not set
        """
        return self._data["Load Range 2 Upper Limit"]

    @load_range_2_upper_limit.setter
    def load_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_2_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_2_upper_limit`
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
                                 'for field `load_range_2_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_2_upper_limit`')

        self._data["Load Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_2_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_2_equipment_list_name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')

        self._data["Range 2 Equipment List Name"] = value

    @property
    def load_range_3_lower_limit(self):
        """Get load_range_3_lower_limit

        Returns:
            float: the value of `load_range_3_lower_limit` or None if not set
        """
        return self._data["Load Range 3 Lower Limit"]

    @load_range_3_lower_limit.setter
    def load_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_3_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_3_lower_limit`
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
                                 'for field `load_range_3_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_3_lower_limit`')

        self._data["Load Range 3 Lower Limit"] = value

    @property
    def load_range_3_upper_limit(self):
        """Get load_range_3_upper_limit

        Returns:
            float: the value of `load_range_3_upper_limit` or None if not set
        """
        return self._data["Load Range 3 Upper Limit"]

    @load_range_3_upper_limit.setter
    def load_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_3_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_3_upper_limit`
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
                                 'for field `load_range_3_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_3_upper_limit`')

        self._data["Load Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_3_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_3_equipment_list_name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')

        self._data["Range 3 Equipment List Name"] = value

    @property
    def load_range_4_lower_limit(self):
        """Get load_range_4_lower_limit

        Returns:
            float: the value of `load_range_4_lower_limit` or None if not set
        """
        return self._data["Load Range 4 Lower Limit"]

    @load_range_4_lower_limit.setter
    def load_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_4_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_4_lower_limit`
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
                                 'for field `load_range_4_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_4_lower_limit`')

        self._data["Load Range 4 Lower Limit"] = value

    @property
    def load_range_4_upper_limit(self):
        """Get load_range_4_upper_limit

        Returns:
            float: the value of `load_range_4_upper_limit` or None if not set
        """
        return self._data["Load Range 4 Upper Limit"]

    @load_range_4_upper_limit.setter
    def load_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_4_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_4_upper_limit`
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
                                 'for field `load_range_4_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_4_upper_limit`')

        self._data["Load Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_4_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_4_equipment_list_name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')

        self._data["Range 4 Equipment List Name"] = value

    @property
    def load_range_5_lower_limit(self):
        """Get load_range_5_lower_limit

        Returns:
            float: the value of `load_range_5_lower_limit` or None if not set
        """
        return self._data["Load Range 5 Lower Limit"]

    @load_range_5_lower_limit.setter
    def load_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_5_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_5_lower_limit`
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
                                 'for field `load_range_5_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_5_lower_limit`')

        self._data["Load Range 5 Lower Limit"] = value

    @property
    def load_range_5_upper_limit(self):
        """Get load_range_5_upper_limit

        Returns:
            float: the value of `load_range_5_upper_limit` or None if not set
        """
        return self._data["Load Range 5 Upper Limit"]

    @load_range_5_upper_limit.setter
    def load_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_5_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_5_upper_limit`
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
                                 'for field `load_range_5_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_5_upper_limit`')

        self._data["Load Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_5_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_5_equipment_list_name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')

        self._data["Range 5 Equipment List Name"] = value

    @property
    def load_range_6_lower_limit(self):
        """Get load_range_6_lower_limit

        Returns:
            float: the value of `load_range_6_lower_limit` or None if not set
        """
        return self._data["Load Range 6 Lower Limit"]

    @load_range_6_lower_limit.setter
    def load_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_6_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_6_lower_limit`
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
                                 'for field `load_range_6_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_6_lower_limit`')

        self._data["Load Range 6 Lower Limit"] = value

    @property
    def load_range_6_upper_limit(self):
        """Get load_range_6_upper_limit

        Returns:
            float: the value of `load_range_6_upper_limit` or None if not set
        """
        return self._data["Load Range 6 Upper Limit"]

    @load_range_6_upper_limit.setter
    def load_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_6_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_6_upper_limit`
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
                                 'for field `load_range_6_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_6_upper_limit`')

        self._data["Load Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_6_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_6_equipment_list_name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')

        self._data["Range 6 Equipment List Name"] = value

    @property
    def load_range_7_lower_limit(self):
        """Get load_range_7_lower_limit

        Returns:
            float: the value of `load_range_7_lower_limit` or None if not set
        """
        return self._data["Load Range 7 Lower Limit"]

    @load_range_7_lower_limit.setter
    def load_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_7_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_7_lower_limit`
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
                                 'for field `load_range_7_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_7_lower_limit`')

        self._data["Load Range 7 Lower Limit"] = value

    @property
    def load_range_7_upper_limit(self):
        """Get load_range_7_upper_limit

        Returns:
            float: the value of `load_range_7_upper_limit` or None if not set
        """
        return self._data["Load Range 7 Upper Limit"]

    @load_range_7_upper_limit.setter
    def load_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_7_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_7_upper_limit`
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
                                 'for field `load_range_7_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_7_upper_limit`')

        self._data["Load Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_7_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_7_equipment_list_name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')

        self._data["Range 7 Equipment List Name"] = value

    @property
    def load_range_8_lower_limit(self):
        """Get load_range_8_lower_limit

        Returns:
            float: the value of `load_range_8_lower_limit` or None if not set
        """
        return self._data["Load Range 8 Lower Limit"]

    @load_range_8_lower_limit.setter
    def load_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_8_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_8_lower_limit`
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
                                 'for field `load_range_8_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_8_lower_limit`')

        self._data["Load Range 8 Lower Limit"] = value

    @property
    def load_range_8_upper_limit(self):
        """Get load_range_8_upper_limit

        Returns:
            float: the value of `load_range_8_upper_limit` or None if not set
        """
        return self._data["Load Range 8 Upper Limit"]

    @load_range_8_upper_limit.setter
    def load_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_8_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_8_upper_limit`
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
                                 'for field `load_range_8_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_8_upper_limit`')

        self._data["Load Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_8_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_8_equipment_list_name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')

        self._data["Range 8 Equipment List Name"] = value

    @property
    def load_range_9_lower_limit(self):
        """Get load_range_9_lower_limit

        Returns:
            float: the value of `load_range_9_lower_limit` or None if not set
        """
        return self._data["Load Range 9 Lower Limit"]

    @load_range_9_lower_limit.setter
    def load_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_9_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_9_lower_limit`
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
                                 'for field `load_range_9_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_9_lower_limit`')

        self._data["Load Range 9 Lower Limit"] = value

    @property
    def load_range_9_upper_limit(self):
        """Get load_range_9_upper_limit

        Returns:
            float: the value of `load_range_9_upper_limit` or None if not set
        """
        return self._data["Load Range 9 Upper Limit"]

    @load_range_9_upper_limit.setter
    def load_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_9_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_9_upper_limit`
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
                                 'for field `load_range_9_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_9_upper_limit`')

        self._data["Load Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_9_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_9_equipment_list_name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')

        self._data["Range 9 Equipment List Name"] = value

    @property
    def load_range_10_lower_limit(self):
        """Get load_range_10_lower_limit

        Returns:
            float: the value of `load_range_10_lower_limit` or None if not set
        """
        return self._data["Load Range 10 Lower Limit"]

    @load_range_10_lower_limit.setter
    def load_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_10_lower_limit`

        Args:
            value (float): value for IDD Field `load_range_10_lower_limit`
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
                                 'for field `load_range_10_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_10_lower_limit`')

        self._data["Load Range 10 Lower Limit"] = value

    @property
    def load_range_10_upper_limit(self):
        """Get load_range_10_upper_limit

        Returns:
            float: the value of `load_range_10_upper_limit` or None if not set
        """
        return self._data["Load Range 10 Upper Limit"]

    @load_range_10_upper_limit.setter
    def load_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `load_range_10_upper_limit`

        Args:
            value (float): value for IDD Field `load_range_10_upper_limit`
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
                                 'for field `load_range_10_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `load_range_10_upper_limit`')

        self._data["Load Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_10_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_10_equipment_list_name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')

        self._data["Range 10 Equipment List Name"] = value

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
        out.append(self._to_str(self.load_range_1_lower_limit))
        out.append(self._to_str(self.load_range_1_upper_limit))
        out.append(self._to_str(self.range_1_equipment_list_name))
        out.append(self._to_str(self.load_range_2_lower_limit))
        out.append(self._to_str(self.load_range_2_upper_limit))
        out.append(self._to_str(self.range_2_equipment_list_name))
        out.append(self._to_str(self.load_range_3_lower_limit))
        out.append(self._to_str(self.load_range_3_upper_limit))
        out.append(self._to_str(self.range_3_equipment_list_name))
        out.append(self._to_str(self.load_range_4_lower_limit))
        out.append(self._to_str(self.load_range_4_upper_limit))
        out.append(self._to_str(self.range_4_equipment_list_name))
        out.append(self._to_str(self.load_range_5_lower_limit))
        out.append(self._to_str(self.load_range_5_upper_limit))
        out.append(self._to_str(self.range_5_equipment_list_name))
        out.append(self._to_str(self.load_range_6_lower_limit))
        out.append(self._to_str(self.load_range_6_upper_limit))
        out.append(self._to_str(self.range_6_equipment_list_name))
        out.append(self._to_str(self.load_range_7_lower_limit))
        out.append(self._to_str(self.load_range_7_upper_limit))
        out.append(self._to_str(self.range_7_equipment_list_name))
        out.append(self._to_str(self.load_range_8_lower_limit))
        out.append(self._to_str(self.load_range_8_upper_limit))
        out.append(self._to_str(self.range_8_equipment_list_name))
        out.append(self._to_str(self.load_range_9_lower_limit))
        out.append(self._to_str(self.load_range_9_upper_limit))
        out.append(self._to_str(self.range_9_equipment_list_name))
        out.append(self._to_str(self.load_range_10_lower_limit))
        out.append(self._to_str(self.load_range_10_upper_limit))
        out.append(self._to_str(self.range_10_equipment_list_name))
        return ",".join(out)

class PlantEquipmentOperationOutdoorDryBulb(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDryBulb`
        Plant equipment operation scheme for outdoor dry-bulb temperature range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor dry-bulb temperature ranges.
    """
    internal_name = "PlantEquipmentOperation:OutdoorDryBulb"
    field_count = 31

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:OutdoorDryBulb`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Dry-Bulb Temperature Range 1 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 2 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 3 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 4 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 5 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 6 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 7 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 8 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 9 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Range 10 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None

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
            self.drybulb_temperature_range_1_lower_limit = None
        else:
            self.drybulb_temperature_range_1_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_1_upper_limit = None
        else:
            self.drybulb_temperature_range_1_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_2_lower_limit = None
        else:
            self.drybulb_temperature_range_2_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_2_upper_limit = None
        else:
            self.drybulb_temperature_range_2_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_3_lower_limit = None
        else:
            self.drybulb_temperature_range_3_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_3_upper_limit = None
        else:
            self.drybulb_temperature_range_3_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_4_lower_limit = None
        else:
            self.drybulb_temperature_range_4_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_4_upper_limit = None
        else:
            self.drybulb_temperature_range_4_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_5_lower_limit = None
        else:
            self.drybulb_temperature_range_5_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_5_upper_limit = None
        else:
            self.drybulb_temperature_range_5_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_6_lower_limit = None
        else:
            self.drybulb_temperature_range_6_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_6_upper_limit = None
        else:
            self.drybulb_temperature_range_6_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_7_lower_limit = None
        else:
            self.drybulb_temperature_range_7_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_7_upper_limit = None
        else:
            self.drybulb_temperature_range_7_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_8_lower_limit = None
        else:
            self.drybulb_temperature_range_8_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_8_upper_limit = None
        else:
            self.drybulb_temperature_range_8_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_9_lower_limit = None
        else:
            self.drybulb_temperature_range_9_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_9_upper_limit = None
        else:
            self.drybulb_temperature_range_9_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_10_lower_limit = None
        else:
            self.drybulb_temperature_range_10_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_range_10_upper_limit = None
        else:
            self.drybulb_temperature_range_10_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def drybulb_temperature_range_1_lower_limit(self):
        """Get drybulb_temperature_range_1_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_1_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 1 Lower Limit"]

    @drybulb_temperature_range_1_lower_limit.setter
    def drybulb_temperature_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_1_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_1_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_1_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_1_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_1_lower_limit`')

        self._data["Dry-Bulb Temperature Range 1 Lower Limit"] = value

    @property
    def drybulb_temperature_range_1_upper_limit(self):
        """Get drybulb_temperature_range_1_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_1_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 1 Upper Limit"]

    @drybulb_temperature_range_1_upper_limit.setter
    def drybulb_temperature_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_1_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_1_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_1_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_1_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_1_upper_limit`')

        self._data["Dry-Bulb Temperature Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_1_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_1_equipment_list_name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')

        self._data["Range 1 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_2_lower_limit(self):
        """Get drybulb_temperature_range_2_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_2_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 2 Lower Limit"]

    @drybulb_temperature_range_2_lower_limit.setter
    def drybulb_temperature_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_2_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_2_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_2_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_2_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_2_lower_limit`')

        self._data["Dry-Bulb Temperature Range 2 Lower Limit"] = value

    @property
    def drybulb_temperature_range_2_upper_limit(self):
        """Get drybulb_temperature_range_2_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_2_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 2 Upper Limit"]

    @drybulb_temperature_range_2_upper_limit.setter
    def drybulb_temperature_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_2_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_2_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_2_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_2_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_2_upper_limit`')

        self._data["Dry-Bulb Temperature Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_2_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_2_equipment_list_name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')

        self._data["Range 2 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_3_lower_limit(self):
        """Get drybulb_temperature_range_3_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_3_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 3 Lower Limit"]

    @drybulb_temperature_range_3_lower_limit.setter
    def drybulb_temperature_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_3_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_3_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_3_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_3_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_3_lower_limit`')

        self._data["Dry-Bulb Temperature Range 3 Lower Limit"] = value

    @property
    def drybulb_temperature_range_3_upper_limit(self):
        """Get drybulb_temperature_range_3_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_3_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 3 Upper Limit"]

    @drybulb_temperature_range_3_upper_limit.setter
    def drybulb_temperature_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_3_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_3_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_3_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_3_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_3_upper_limit`')

        self._data["Dry-Bulb Temperature Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_3_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_3_equipment_list_name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')

        self._data["Range 3 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_4_lower_limit(self):
        """Get drybulb_temperature_range_4_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_4_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 4 Lower Limit"]

    @drybulb_temperature_range_4_lower_limit.setter
    def drybulb_temperature_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_4_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_4_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_4_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_4_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_4_lower_limit`')

        self._data["Dry-Bulb Temperature Range 4 Lower Limit"] = value

    @property
    def drybulb_temperature_range_4_upper_limit(self):
        """Get drybulb_temperature_range_4_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_4_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 4 Upper Limit"]

    @drybulb_temperature_range_4_upper_limit.setter
    def drybulb_temperature_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_4_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_4_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_4_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_4_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_4_upper_limit`')

        self._data["Dry-Bulb Temperature Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_4_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_4_equipment_list_name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')

        self._data["Range 4 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_5_lower_limit(self):
        """Get drybulb_temperature_range_5_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_5_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 5 Lower Limit"]

    @drybulb_temperature_range_5_lower_limit.setter
    def drybulb_temperature_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_5_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_5_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_5_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_5_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_5_lower_limit`')

        self._data["Dry-Bulb Temperature Range 5 Lower Limit"] = value

    @property
    def drybulb_temperature_range_5_upper_limit(self):
        """Get drybulb_temperature_range_5_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_5_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 5 Upper Limit"]

    @drybulb_temperature_range_5_upper_limit.setter
    def drybulb_temperature_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_5_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_5_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_5_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_5_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_5_upper_limit`')

        self._data["Dry-Bulb Temperature Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_5_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_5_equipment_list_name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')

        self._data["Range 5 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_6_lower_limit(self):
        """Get drybulb_temperature_range_6_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_6_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 6 Lower Limit"]

    @drybulb_temperature_range_6_lower_limit.setter
    def drybulb_temperature_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_6_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_6_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_6_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_6_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_6_lower_limit`')

        self._data["Dry-Bulb Temperature Range 6 Lower Limit"] = value

    @property
    def drybulb_temperature_range_6_upper_limit(self):
        """Get drybulb_temperature_range_6_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_6_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 6 Upper Limit"]

    @drybulb_temperature_range_6_upper_limit.setter
    def drybulb_temperature_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_6_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_6_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_6_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_6_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_6_upper_limit`')

        self._data["Dry-Bulb Temperature Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_6_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_6_equipment_list_name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')

        self._data["Range 6 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_7_lower_limit(self):
        """Get drybulb_temperature_range_7_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_7_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 7 Lower Limit"]

    @drybulb_temperature_range_7_lower_limit.setter
    def drybulb_temperature_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_7_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_7_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_7_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_7_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_7_lower_limit`')

        self._data["Dry-Bulb Temperature Range 7 Lower Limit"] = value

    @property
    def drybulb_temperature_range_7_upper_limit(self):
        """Get drybulb_temperature_range_7_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_7_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 7 Upper Limit"]

    @drybulb_temperature_range_7_upper_limit.setter
    def drybulb_temperature_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_7_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_7_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_7_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_7_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_7_upper_limit`')

        self._data["Dry-Bulb Temperature Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_7_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_7_equipment_list_name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')

        self._data["Range 7 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_8_lower_limit(self):
        """Get drybulb_temperature_range_8_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_8_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 8 Lower Limit"]

    @drybulb_temperature_range_8_lower_limit.setter
    def drybulb_temperature_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_8_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_8_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_8_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_8_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_8_lower_limit`')

        self._data["Dry-Bulb Temperature Range 8 Lower Limit"] = value

    @property
    def drybulb_temperature_range_8_upper_limit(self):
        """Get drybulb_temperature_range_8_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_8_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 8 Upper Limit"]

    @drybulb_temperature_range_8_upper_limit.setter
    def drybulb_temperature_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_8_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_8_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_8_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_8_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_8_upper_limit`')

        self._data["Dry-Bulb Temperature Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_8_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_8_equipment_list_name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')

        self._data["Range 8 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_9_lower_limit(self):
        """Get drybulb_temperature_range_9_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_9_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 9 Lower Limit"]

    @drybulb_temperature_range_9_lower_limit.setter
    def drybulb_temperature_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_9_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_9_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_9_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_9_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_9_lower_limit`')

        self._data["Dry-Bulb Temperature Range 9 Lower Limit"] = value

    @property
    def drybulb_temperature_range_9_upper_limit(self):
        """Get drybulb_temperature_range_9_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_9_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 9 Upper Limit"]

    @drybulb_temperature_range_9_upper_limit.setter
    def drybulb_temperature_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_9_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_9_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_9_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_9_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_9_upper_limit`')

        self._data["Dry-Bulb Temperature Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_9_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_9_equipment_list_name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')

        self._data["Range 9 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_10_lower_limit(self):
        """Get drybulb_temperature_range_10_lower_limit

        Returns:
            float: the value of `drybulb_temperature_range_10_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 10 Lower Limit"]

    @drybulb_temperature_range_10_lower_limit.setter
    def drybulb_temperature_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_10_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_10_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_10_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_10_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_10_lower_limit`')

        self._data["Dry-Bulb Temperature Range 10 Lower Limit"] = value

    @property
    def drybulb_temperature_range_10_upper_limit(self):
        """Get drybulb_temperature_range_10_upper_limit

        Returns:
            float: the value of `drybulb_temperature_range_10_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Range 10 Upper Limit"]

    @drybulb_temperature_range_10_upper_limit.setter
    def drybulb_temperature_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_range_10_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_range_10_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_range_10_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `drybulb_temperature_range_10_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `drybulb_temperature_range_10_upper_limit`')

        self._data["Dry-Bulb Temperature Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_10_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_10_equipment_list_name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')

        self._data["Range 10 Equipment List Name"] = value

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
        out.append(self._to_str(self.drybulb_temperature_range_1_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_range_1_upper_limit))
        out.append(self._to_str(self.range_1_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_range_2_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_range_2_upper_limit))
        out.append(self._to_str(self.range_2_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_range_3_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_range_3_upper_limit))
        out.append(self._to_str(self.range_3_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_range_4_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_range_4_upper_limit))
        out.append(self._to_str(self.range_4_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_range_5_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_range_5_upper_limit))
        out.append(self._to_str(self.range_5_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_range_6_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_range_6_upper_limit))
        out.append(self._to_str(self.range_6_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_range_7_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_range_7_upper_limit))
        out.append(self._to_str(self.range_7_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_range_8_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_range_8_upper_limit))
        out.append(self._to_str(self.range_8_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_range_9_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_range_9_upper_limit))
        out.append(self._to_str(self.range_9_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_range_10_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_range_10_upper_limit))
        out.append(self._to_str(self.range_10_equipment_list_name))
        return ",".join(out)

class PlantEquipmentOperationOutdoorWetBulb(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorWetBulb`
        Plant equipment operation scheme for outdoor wet-bulb temperature range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor wet-bulb temperature ranges.
    """
    internal_name = "PlantEquipmentOperation:OutdoorWetBulb"
    field_count = 31

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:OutdoorWetBulb`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Wet-Bulb Temperature Range 1 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 2 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 3 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 4 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 5 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 6 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 7 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 8 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 9 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Range 10 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None

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
            self.wetbulb_temperature_range_1_lower_limit = None
        else:
            self.wetbulb_temperature_range_1_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_1_upper_limit = None
        else:
            self.wetbulb_temperature_range_1_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_2_lower_limit = None
        else:
            self.wetbulb_temperature_range_2_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_2_upper_limit = None
        else:
            self.wetbulb_temperature_range_2_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_3_lower_limit = None
        else:
            self.wetbulb_temperature_range_3_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_3_upper_limit = None
        else:
            self.wetbulb_temperature_range_3_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_4_lower_limit = None
        else:
            self.wetbulb_temperature_range_4_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_4_upper_limit = None
        else:
            self.wetbulb_temperature_range_4_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_5_lower_limit = None
        else:
            self.wetbulb_temperature_range_5_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_5_upper_limit = None
        else:
            self.wetbulb_temperature_range_5_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_6_lower_limit = None
        else:
            self.wetbulb_temperature_range_6_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_6_upper_limit = None
        else:
            self.wetbulb_temperature_range_6_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_7_lower_limit = None
        else:
            self.wetbulb_temperature_range_7_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_7_upper_limit = None
        else:
            self.wetbulb_temperature_range_7_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_8_lower_limit = None
        else:
            self.wetbulb_temperature_range_8_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_8_upper_limit = None
        else:
            self.wetbulb_temperature_range_8_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_9_lower_limit = None
        else:
            self.wetbulb_temperature_range_9_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_9_upper_limit = None
        else:
            self.wetbulb_temperature_range_9_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_10_lower_limit = None
        else:
            self.wetbulb_temperature_range_10_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_range_10_upper_limit = None
        else:
            self.wetbulb_temperature_range_10_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def wetbulb_temperature_range_1_lower_limit(self):
        """Get wetbulb_temperature_range_1_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_1_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 1 Lower Limit"]

    @wetbulb_temperature_range_1_lower_limit.setter
    def wetbulb_temperature_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_1_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_1_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_1_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_1_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_1_lower_limit`')

        self._data["Wet-Bulb Temperature Range 1 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_1_upper_limit(self):
        """Get wetbulb_temperature_range_1_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_1_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 1 Upper Limit"]

    @wetbulb_temperature_range_1_upper_limit.setter
    def wetbulb_temperature_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_1_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_1_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_1_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_1_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_1_upper_limit`')

        self._data["Wet-Bulb Temperature Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_1_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_1_equipment_list_name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')

        self._data["Range 1 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_2_lower_limit(self):
        """Get wetbulb_temperature_range_2_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_2_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 2 Lower Limit"]

    @wetbulb_temperature_range_2_lower_limit.setter
    def wetbulb_temperature_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_2_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_2_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_2_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_2_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_2_lower_limit`')

        self._data["Wet-Bulb Temperature Range 2 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_2_upper_limit(self):
        """Get wetbulb_temperature_range_2_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_2_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 2 Upper Limit"]

    @wetbulb_temperature_range_2_upper_limit.setter
    def wetbulb_temperature_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_2_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_2_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_2_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_2_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_2_upper_limit`')

        self._data["Wet-Bulb Temperature Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_2_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_2_equipment_list_name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')

        self._data["Range 2 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_3_lower_limit(self):
        """Get wetbulb_temperature_range_3_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_3_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 3 Lower Limit"]

    @wetbulb_temperature_range_3_lower_limit.setter
    def wetbulb_temperature_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_3_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_3_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_3_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_3_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_3_lower_limit`')

        self._data["Wet-Bulb Temperature Range 3 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_3_upper_limit(self):
        """Get wetbulb_temperature_range_3_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_3_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 3 Upper Limit"]

    @wetbulb_temperature_range_3_upper_limit.setter
    def wetbulb_temperature_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_3_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_3_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_3_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_3_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_3_upper_limit`')

        self._data["Wet-Bulb Temperature Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_3_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_3_equipment_list_name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')

        self._data["Range 3 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_4_lower_limit(self):
        """Get wetbulb_temperature_range_4_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_4_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 4 Lower Limit"]

    @wetbulb_temperature_range_4_lower_limit.setter
    def wetbulb_temperature_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_4_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_4_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_4_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_4_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_4_lower_limit`')

        self._data["Wet-Bulb Temperature Range 4 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_4_upper_limit(self):
        """Get wetbulb_temperature_range_4_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_4_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 4 Upper Limit"]

    @wetbulb_temperature_range_4_upper_limit.setter
    def wetbulb_temperature_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_4_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_4_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_4_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_4_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_4_upper_limit`')

        self._data["Wet-Bulb Temperature Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_4_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_4_equipment_list_name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')

        self._data["Range 4 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_5_lower_limit(self):
        """Get wetbulb_temperature_range_5_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_5_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 5 Lower Limit"]

    @wetbulb_temperature_range_5_lower_limit.setter
    def wetbulb_temperature_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_5_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_5_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_5_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_5_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_5_lower_limit`')

        self._data["Wet-Bulb Temperature Range 5 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_5_upper_limit(self):
        """Get wetbulb_temperature_range_5_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_5_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 5 Upper Limit"]

    @wetbulb_temperature_range_5_upper_limit.setter
    def wetbulb_temperature_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_5_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_5_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_5_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_5_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_5_upper_limit`')

        self._data["Wet-Bulb Temperature Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_5_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_5_equipment_list_name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')

        self._data["Range 5 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_6_lower_limit(self):
        """Get wetbulb_temperature_range_6_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_6_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 6 Lower Limit"]

    @wetbulb_temperature_range_6_lower_limit.setter
    def wetbulb_temperature_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_6_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_6_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_6_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_6_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_6_lower_limit`')

        self._data["Wet-Bulb Temperature Range 6 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_6_upper_limit(self):
        """Get wetbulb_temperature_range_6_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_6_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 6 Upper Limit"]

    @wetbulb_temperature_range_6_upper_limit.setter
    def wetbulb_temperature_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_6_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_6_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_6_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_6_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_6_upper_limit`')

        self._data["Wet-Bulb Temperature Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_6_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_6_equipment_list_name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')

        self._data["Range 6 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_7_lower_limit(self):
        """Get wetbulb_temperature_range_7_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_7_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 7 Lower Limit"]

    @wetbulb_temperature_range_7_lower_limit.setter
    def wetbulb_temperature_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_7_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_7_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_7_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_7_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_7_lower_limit`')

        self._data["Wet-Bulb Temperature Range 7 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_7_upper_limit(self):
        """Get wetbulb_temperature_range_7_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_7_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 7 Upper Limit"]

    @wetbulb_temperature_range_7_upper_limit.setter
    def wetbulb_temperature_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_7_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_7_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_7_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_7_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_7_upper_limit`')

        self._data["Wet-Bulb Temperature Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_7_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_7_equipment_list_name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')

        self._data["Range 7 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_8_lower_limit(self):
        """Get wetbulb_temperature_range_8_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_8_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 8 Lower Limit"]

    @wetbulb_temperature_range_8_lower_limit.setter
    def wetbulb_temperature_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_8_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_8_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_8_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_8_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_8_lower_limit`')

        self._data["Wet-Bulb Temperature Range 8 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_8_upper_limit(self):
        """Get wetbulb_temperature_range_8_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_8_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 8 Upper Limit"]

    @wetbulb_temperature_range_8_upper_limit.setter
    def wetbulb_temperature_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_8_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_8_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_8_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_8_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_8_upper_limit`')

        self._data["Wet-Bulb Temperature Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_8_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_8_equipment_list_name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')

        self._data["Range 8 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_9_lower_limit(self):
        """Get wetbulb_temperature_range_9_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_9_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 9 Lower Limit"]

    @wetbulb_temperature_range_9_lower_limit.setter
    def wetbulb_temperature_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_9_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_9_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_9_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_9_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_9_lower_limit`')

        self._data["Wet-Bulb Temperature Range 9 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_9_upper_limit(self):
        """Get wetbulb_temperature_range_9_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_9_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 9 Upper Limit"]

    @wetbulb_temperature_range_9_upper_limit.setter
    def wetbulb_temperature_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_9_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_9_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_9_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_9_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_9_upper_limit`')

        self._data["Wet-Bulb Temperature Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_9_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_9_equipment_list_name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')

        self._data["Range 9 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_10_lower_limit(self):
        """Get wetbulb_temperature_range_10_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_range_10_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 10 Lower Limit"]

    @wetbulb_temperature_range_10_lower_limit.setter
    def wetbulb_temperature_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_10_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_10_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_10_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_10_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_10_lower_limit`')

        self._data["Wet-Bulb Temperature Range 10 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_10_upper_limit(self):
        """Get wetbulb_temperature_range_10_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_range_10_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Range 10 Upper Limit"]

    @wetbulb_temperature_range_10_upper_limit.setter
    def wetbulb_temperature_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_range_10_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_range_10_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_range_10_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `wetbulb_temperature_range_10_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `wetbulb_temperature_range_10_upper_limit`')

        self._data["Wet-Bulb Temperature Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_10_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_10_equipment_list_name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')

        self._data["Range 10 Equipment List Name"] = value

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
        out.append(self._to_str(self.wetbulb_temperature_range_1_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_range_1_upper_limit))
        out.append(self._to_str(self.range_1_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_range_2_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_range_2_upper_limit))
        out.append(self._to_str(self.range_2_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_range_3_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_range_3_upper_limit))
        out.append(self._to_str(self.range_3_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_range_4_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_range_4_upper_limit))
        out.append(self._to_str(self.range_4_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_range_5_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_range_5_upper_limit))
        out.append(self._to_str(self.range_5_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_range_6_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_range_6_upper_limit))
        out.append(self._to_str(self.range_6_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_range_7_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_range_7_upper_limit))
        out.append(self._to_str(self.range_7_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_range_8_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_range_8_upper_limit))
        out.append(self._to_str(self.range_8_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_range_9_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_range_9_upper_limit))
        out.append(self._to_str(self.range_9_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_range_10_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_range_10_upper_limit))
        out.append(self._to_str(self.range_10_equipment_list_name))
        return ",".join(out)

class PlantEquipmentOperationOutdoorRelativeHumidity(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorRelativeHumidity`
        Plant equipment operation scheme for outdoor relative humidity range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor relative humidity ranges.
    """
    internal_name = "PlantEquipmentOperation:OutdoorRelativeHumidity"
    field_count = 31

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:OutdoorRelativeHumidity`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Relative Humidity Range 1 Lower Limit"] = None
        self._data["Relative Humidity Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Relative Humidity Range 2 Lower Limit"] = None
        self._data["Relative Humidity Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Relative Humidity Range 3 Lower Limit"] = None
        self._data["Relative Humidity Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Relative Humidity Range 4 Lower Limit"] = None
        self._data["Relative Humidity Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Relative Humidity Range 5 Lower Limit"] = None
        self._data["Relative Humidity Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Relative Humidity Range 6 Lower Limit"] = None
        self._data["Relative Humidity Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Relative Humidity Range 7 Lower Limit"] = None
        self._data["Relative Humidity Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Relative Humidity Range 8 Lower Limit"] = None
        self._data["Relative Humidity Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Relative Humidity Range 9 Lower Limit"] = None
        self._data["Relative Humidity Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Relative Humidity Range 10 Lower Limit"] = None
        self._data["Relative Humidity Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None

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
            self.relative_humidity_range_1_lower_limit = None
        else:
            self.relative_humidity_range_1_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_1_upper_limit = None
        else:
            self.relative_humidity_range_1_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_2_lower_limit = None
        else:
            self.relative_humidity_range_2_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_2_upper_limit = None
        else:
            self.relative_humidity_range_2_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_3_lower_limit = None
        else:
            self.relative_humidity_range_3_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_3_upper_limit = None
        else:
            self.relative_humidity_range_3_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_4_lower_limit = None
        else:
            self.relative_humidity_range_4_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_4_upper_limit = None
        else:
            self.relative_humidity_range_4_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_5_lower_limit = None
        else:
            self.relative_humidity_range_5_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_5_upper_limit = None
        else:
            self.relative_humidity_range_5_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_6_lower_limit = None
        else:
            self.relative_humidity_range_6_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_6_upper_limit = None
        else:
            self.relative_humidity_range_6_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_7_lower_limit = None
        else:
            self.relative_humidity_range_7_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_7_upper_limit = None
        else:
            self.relative_humidity_range_7_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_8_lower_limit = None
        else:
            self.relative_humidity_range_8_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_8_upper_limit = None
        else:
            self.relative_humidity_range_8_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_9_lower_limit = None
        else:
            self.relative_humidity_range_9_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_9_upper_limit = None
        else:
            self.relative_humidity_range_9_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_10_lower_limit = None
        else:
            self.relative_humidity_range_10_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_humidity_range_10_upper_limit = None
        else:
            self.relative_humidity_range_10_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def relative_humidity_range_1_lower_limit(self):
        """Get relative_humidity_range_1_lower_limit

        Returns:
            float: the value of `relative_humidity_range_1_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 1 Lower Limit"]

    @relative_humidity_range_1_lower_limit.setter
    def relative_humidity_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_1_lower_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_1_lower_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_1_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_1_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_1_lower_limit`')

        self._data["Relative Humidity Range 1 Lower Limit"] = value

    @property
    def relative_humidity_range_1_upper_limit(self):
        """Get relative_humidity_range_1_upper_limit

        Returns:
            float: the value of `relative_humidity_range_1_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 1 Upper Limit"]

    @relative_humidity_range_1_upper_limit.setter
    def relative_humidity_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_1_upper_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_1_upper_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_1_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_1_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_1_upper_limit`')

        self._data["Relative Humidity Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_1_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_1_equipment_list_name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')

        self._data["Range 1 Equipment List Name"] = value

    @property
    def relative_humidity_range_2_lower_limit(self):
        """Get relative_humidity_range_2_lower_limit

        Returns:
            float: the value of `relative_humidity_range_2_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 2 Lower Limit"]

    @relative_humidity_range_2_lower_limit.setter
    def relative_humidity_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_2_lower_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_2_lower_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_2_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_2_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_2_lower_limit`')

        self._data["Relative Humidity Range 2 Lower Limit"] = value

    @property
    def relative_humidity_range_2_upper_limit(self):
        """Get relative_humidity_range_2_upper_limit

        Returns:
            float: the value of `relative_humidity_range_2_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 2 Upper Limit"]

    @relative_humidity_range_2_upper_limit.setter
    def relative_humidity_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_2_upper_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_2_upper_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_2_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_2_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_2_upper_limit`')

        self._data["Relative Humidity Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_2_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_2_equipment_list_name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')

        self._data["Range 2 Equipment List Name"] = value

    @property
    def relative_humidity_range_3_lower_limit(self):
        """Get relative_humidity_range_3_lower_limit

        Returns:
            float: the value of `relative_humidity_range_3_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 3 Lower Limit"]

    @relative_humidity_range_3_lower_limit.setter
    def relative_humidity_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_3_lower_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_3_lower_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_3_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_3_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_3_lower_limit`')

        self._data["Relative Humidity Range 3 Lower Limit"] = value

    @property
    def relative_humidity_range_3_upper_limit(self):
        """Get relative_humidity_range_3_upper_limit

        Returns:
            float: the value of `relative_humidity_range_3_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 3 Upper Limit"]

    @relative_humidity_range_3_upper_limit.setter
    def relative_humidity_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_3_upper_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_3_upper_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_3_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_3_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_3_upper_limit`')

        self._data["Relative Humidity Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_3_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_3_equipment_list_name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')

        self._data["Range 3 Equipment List Name"] = value

    @property
    def relative_humidity_range_4_lower_limit(self):
        """Get relative_humidity_range_4_lower_limit

        Returns:
            float: the value of `relative_humidity_range_4_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 4 Lower Limit"]

    @relative_humidity_range_4_lower_limit.setter
    def relative_humidity_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_4_lower_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_4_lower_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_4_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_4_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_4_lower_limit`')

        self._data["Relative Humidity Range 4 Lower Limit"] = value

    @property
    def relative_humidity_range_4_upper_limit(self):
        """Get relative_humidity_range_4_upper_limit

        Returns:
            float: the value of `relative_humidity_range_4_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 4 Upper Limit"]

    @relative_humidity_range_4_upper_limit.setter
    def relative_humidity_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_4_upper_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_4_upper_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_4_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_4_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_4_upper_limit`')

        self._data["Relative Humidity Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_4_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_4_equipment_list_name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')

        self._data["Range 4 Equipment List Name"] = value

    @property
    def relative_humidity_range_5_lower_limit(self):
        """Get relative_humidity_range_5_lower_limit

        Returns:
            float: the value of `relative_humidity_range_5_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 5 Lower Limit"]

    @relative_humidity_range_5_lower_limit.setter
    def relative_humidity_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_5_lower_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_5_lower_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_5_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_5_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_5_lower_limit`')

        self._data["Relative Humidity Range 5 Lower Limit"] = value

    @property
    def relative_humidity_range_5_upper_limit(self):
        """Get relative_humidity_range_5_upper_limit

        Returns:
            float: the value of `relative_humidity_range_5_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 5 Upper Limit"]

    @relative_humidity_range_5_upper_limit.setter
    def relative_humidity_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_5_upper_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_5_upper_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_5_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_5_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_5_upper_limit`')

        self._data["Relative Humidity Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_5_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_5_equipment_list_name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')

        self._data["Range 5 Equipment List Name"] = value

    @property
    def relative_humidity_range_6_lower_limit(self):
        """Get relative_humidity_range_6_lower_limit

        Returns:
            float: the value of `relative_humidity_range_6_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 6 Lower Limit"]

    @relative_humidity_range_6_lower_limit.setter
    def relative_humidity_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_6_lower_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_6_lower_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_6_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_6_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_6_lower_limit`')

        self._data["Relative Humidity Range 6 Lower Limit"] = value

    @property
    def relative_humidity_range_6_upper_limit(self):
        """Get relative_humidity_range_6_upper_limit

        Returns:
            float: the value of `relative_humidity_range_6_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 6 Upper Limit"]

    @relative_humidity_range_6_upper_limit.setter
    def relative_humidity_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_6_upper_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_6_upper_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_6_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_6_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_6_upper_limit`')

        self._data["Relative Humidity Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_6_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_6_equipment_list_name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')

        self._data["Range 6 Equipment List Name"] = value

    @property
    def relative_humidity_range_7_lower_limit(self):
        """Get relative_humidity_range_7_lower_limit

        Returns:
            float: the value of `relative_humidity_range_7_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 7 Lower Limit"]

    @relative_humidity_range_7_lower_limit.setter
    def relative_humidity_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_7_lower_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_7_lower_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_7_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_7_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_7_lower_limit`')

        self._data["Relative Humidity Range 7 Lower Limit"] = value

    @property
    def relative_humidity_range_7_upper_limit(self):
        """Get relative_humidity_range_7_upper_limit

        Returns:
            float: the value of `relative_humidity_range_7_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 7 Upper Limit"]

    @relative_humidity_range_7_upper_limit.setter
    def relative_humidity_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_7_upper_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_7_upper_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_7_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_7_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_7_upper_limit`')

        self._data["Relative Humidity Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_7_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_7_equipment_list_name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')

        self._data["Range 7 Equipment List Name"] = value

    @property
    def relative_humidity_range_8_lower_limit(self):
        """Get relative_humidity_range_8_lower_limit

        Returns:
            float: the value of `relative_humidity_range_8_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 8 Lower Limit"]

    @relative_humidity_range_8_lower_limit.setter
    def relative_humidity_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_8_lower_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_8_lower_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_8_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_8_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_8_lower_limit`')

        self._data["Relative Humidity Range 8 Lower Limit"] = value

    @property
    def relative_humidity_range_8_upper_limit(self):
        """Get relative_humidity_range_8_upper_limit

        Returns:
            float: the value of `relative_humidity_range_8_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 8 Upper Limit"]

    @relative_humidity_range_8_upper_limit.setter
    def relative_humidity_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_8_upper_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_8_upper_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_8_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_8_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_8_upper_limit`')

        self._data["Relative Humidity Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_8_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_8_equipment_list_name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')

        self._data["Range 8 Equipment List Name"] = value

    @property
    def relative_humidity_range_9_lower_limit(self):
        """Get relative_humidity_range_9_lower_limit

        Returns:
            float: the value of `relative_humidity_range_9_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 9 Lower Limit"]

    @relative_humidity_range_9_lower_limit.setter
    def relative_humidity_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_9_lower_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_9_lower_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_9_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_9_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_9_lower_limit`')

        self._data["Relative Humidity Range 9 Lower Limit"] = value

    @property
    def relative_humidity_range_9_upper_limit(self):
        """Get relative_humidity_range_9_upper_limit

        Returns:
            float: the value of `relative_humidity_range_9_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 9 Upper Limit"]

    @relative_humidity_range_9_upper_limit.setter
    def relative_humidity_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_9_upper_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_9_upper_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_9_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_9_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_9_upper_limit`')

        self._data["Relative Humidity Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_9_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_9_equipment_list_name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')

        self._data["Range 9 Equipment List Name"] = value

    @property
    def relative_humidity_range_10_lower_limit(self):
        """Get relative_humidity_range_10_lower_limit

        Returns:
            float: the value of `relative_humidity_range_10_lower_limit` or None if not set
        """
        return self._data["Relative Humidity Range 10 Lower Limit"]

    @relative_humidity_range_10_lower_limit.setter
    def relative_humidity_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_10_lower_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_10_lower_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_10_lower_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_10_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_10_lower_limit`')

        self._data["Relative Humidity Range 10 Lower Limit"] = value

    @property
    def relative_humidity_range_10_upper_limit(self):
        """Get relative_humidity_range_10_upper_limit

        Returns:
            float: the value of `relative_humidity_range_10_upper_limit` or None if not set
        """
        return self._data["Relative Humidity Range 10 Upper Limit"]

    @relative_humidity_range_10_upper_limit.setter
    def relative_humidity_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `relative_humidity_range_10_upper_limit`

        Args:
            value (float): value for IDD Field `relative_humidity_range_10_upper_limit`
                Unit: percent
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `relative_humidity_range_10_upper_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_humidity_range_10_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `relative_humidity_range_10_upper_limit`')

        self._data["Relative Humidity Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_10_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_10_equipment_list_name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')

        self._data["Range 10 Equipment List Name"] = value

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
        out.append(self._to_str(self.relative_humidity_range_1_lower_limit))
        out.append(self._to_str(self.relative_humidity_range_1_upper_limit))
        out.append(self._to_str(self.range_1_equipment_list_name))
        out.append(self._to_str(self.relative_humidity_range_2_lower_limit))
        out.append(self._to_str(self.relative_humidity_range_2_upper_limit))
        out.append(self._to_str(self.range_2_equipment_list_name))
        out.append(self._to_str(self.relative_humidity_range_3_lower_limit))
        out.append(self._to_str(self.relative_humidity_range_3_upper_limit))
        out.append(self._to_str(self.range_3_equipment_list_name))
        out.append(self._to_str(self.relative_humidity_range_4_lower_limit))
        out.append(self._to_str(self.relative_humidity_range_4_upper_limit))
        out.append(self._to_str(self.range_4_equipment_list_name))
        out.append(self._to_str(self.relative_humidity_range_5_lower_limit))
        out.append(self._to_str(self.relative_humidity_range_5_upper_limit))
        out.append(self._to_str(self.range_5_equipment_list_name))
        out.append(self._to_str(self.relative_humidity_range_6_lower_limit))
        out.append(self._to_str(self.relative_humidity_range_6_upper_limit))
        out.append(self._to_str(self.range_6_equipment_list_name))
        out.append(self._to_str(self.relative_humidity_range_7_lower_limit))
        out.append(self._to_str(self.relative_humidity_range_7_upper_limit))
        out.append(self._to_str(self.range_7_equipment_list_name))
        out.append(self._to_str(self.relative_humidity_range_8_lower_limit))
        out.append(self._to_str(self.relative_humidity_range_8_upper_limit))
        out.append(self._to_str(self.range_8_equipment_list_name))
        out.append(self._to_str(self.relative_humidity_range_9_lower_limit))
        out.append(self._to_str(self.relative_humidity_range_9_upper_limit))
        out.append(self._to_str(self.range_9_equipment_list_name))
        out.append(self._to_str(self.relative_humidity_range_10_lower_limit))
        out.append(self._to_str(self.relative_humidity_range_10_upper_limit))
        out.append(self._to_str(self.range_10_equipment_list_name))
        return ",".join(out)

class PlantEquipmentOperationOutdoorDewpoint(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDewpoint`
        Plant equipment operation scheme for outdoor dewpoint temperature range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor dewpoint temperature ranges.
    """
    internal_name = "PlantEquipmentOperation:OutdoorDewpoint"
    field_count = 31

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:OutdoorDewpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Dewpoint Temperature Range 1 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 2 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 3 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 4 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 5 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 6 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 7 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 8 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 9 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Dewpoint Temperature Range 10 Lower Limit"] = None
        self._data["Dewpoint Temperature Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None

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
            self.dewpoint_temperature_range_1_lower_limit = None
        else:
            self.dewpoint_temperature_range_1_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_1_upper_limit = None
        else:
            self.dewpoint_temperature_range_1_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_2_lower_limit = None
        else:
            self.dewpoint_temperature_range_2_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_2_upper_limit = None
        else:
            self.dewpoint_temperature_range_2_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_3_lower_limit = None
        else:
            self.dewpoint_temperature_range_3_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_3_upper_limit = None
        else:
            self.dewpoint_temperature_range_3_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_4_lower_limit = None
        else:
            self.dewpoint_temperature_range_4_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_4_upper_limit = None
        else:
            self.dewpoint_temperature_range_4_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_5_lower_limit = None
        else:
            self.dewpoint_temperature_range_5_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_5_upper_limit = None
        else:
            self.dewpoint_temperature_range_5_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_6_lower_limit = None
        else:
            self.dewpoint_temperature_range_6_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_6_upper_limit = None
        else:
            self.dewpoint_temperature_range_6_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_7_lower_limit = None
        else:
            self.dewpoint_temperature_range_7_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_7_upper_limit = None
        else:
            self.dewpoint_temperature_range_7_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_8_lower_limit = None
        else:
            self.dewpoint_temperature_range_8_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_8_upper_limit = None
        else:
            self.dewpoint_temperature_range_8_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_9_lower_limit = None
        else:
            self.dewpoint_temperature_range_9_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_9_upper_limit = None
        else:
            self.dewpoint_temperature_range_9_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_10_lower_limit = None
        else:
            self.dewpoint_temperature_range_10_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_range_10_upper_limit = None
        else:
            self.dewpoint_temperature_range_10_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def dewpoint_temperature_range_1_lower_limit(self):
        """Get dewpoint_temperature_range_1_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_1_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 1 Lower Limit"]

    @dewpoint_temperature_range_1_lower_limit.setter
    def dewpoint_temperature_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_1_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_1_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_1_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_1_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_1_lower_limit`')

        self._data["Dewpoint Temperature Range 1 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_1_upper_limit(self):
        """Get dewpoint_temperature_range_1_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_1_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 1 Upper Limit"]

    @dewpoint_temperature_range_1_upper_limit.setter
    def dewpoint_temperature_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_1_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_1_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_1_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_1_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_1_upper_limit`')

        self._data["Dewpoint Temperature Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_1_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_1_equipment_list_name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')

        self._data["Range 1 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_2_lower_limit(self):
        """Get dewpoint_temperature_range_2_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_2_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 2 Lower Limit"]

    @dewpoint_temperature_range_2_lower_limit.setter
    def dewpoint_temperature_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_2_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_2_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_2_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_2_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_2_lower_limit`')

        self._data["Dewpoint Temperature Range 2 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_2_upper_limit(self):
        """Get dewpoint_temperature_range_2_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_2_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 2 Upper Limit"]

    @dewpoint_temperature_range_2_upper_limit.setter
    def dewpoint_temperature_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_2_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_2_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_2_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_2_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_2_upper_limit`')

        self._data["Dewpoint Temperature Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_2_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_2_equipment_list_name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')

        self._data["Range 2 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_3_lower_limit(self):
        """Get dewpoint_temperature_range_3_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_3_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 3 Lower Limit"]

    @dewpoint_temperature_range_3_lower_limit.setter
    def dewpoint_temperature_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_3_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_3_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_3_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_3_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_3_lower_limit`')

        self._data["Dewpoint Temperature Range 3 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_3_upper_limit(self):
        """Get dewpoint_temperature_range_3_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_3_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 3 Upper Limit"]

    @dewpoint_temperature_range_3_upper_limit.setter
    def dewpoint_temperature_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_3_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_3_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_3_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_3_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_3_upper_limit`')

        self._data["Dewpoint Temperature Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_3_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_3_equipment_list_name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')

        self._data["Range 3 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_4_lower_limit(self):
        """Get dewpoint_temperature_range_4_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_4_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 4 Lower Limit"]

    @dewpoint_temperature_range_4_lower_limit.setter
    def dewpoint_temperature_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_4_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_4_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_4_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_4_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_4_lower_limit`')

        self._data["Dewpoint Temperature Range 4 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_4_upper_limit(self):
        """Get dewpoint_temperature_range_4_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_4_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 4 Upper Limit"]

    @dewpoint_temperature_range_4_upper_limit.setter
    def dewpoint_temperature_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_4_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_4_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_4_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_4_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_4_upper_limit`')

        self._data["Dewpoint Temperature Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_4_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_4_equipment_list_name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')

        self._data["Range 4 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_5_lower_limit(self):
        """Get dewpoint_temperature_range_5_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_5_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 5 Lower Limit"]

    @dewpoint_temperature_range_5_lower_limit.setter
    def dewpoint_temperature_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_5_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_5_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_5_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_5_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_5_lower_limit`')

        self._data["Dewpoint Temperature Range 5 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_5_upper_limit(self):
        """Get dewpoint_temperature_range_5_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_5_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 5 Upper Limit"]

    @dewpoint_temperature_range_5_upper_limit.setter
    def dewpoint_temperature_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_5_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_5_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_5_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_5_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_5_upper_limit`')

        self._data["Dewpoint Temperature Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_5_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_5_equipment_list_name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')

        self._data["Range 5 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_6_lower_limit(self):
        """Get dewpoint_temperature_range_6_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_6_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 6 Lower Limit"]

    @dewpoint_temperature_range_6_lower_limit.setter
    def dewpoint_temperature_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_6_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_6_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_6_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_6_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_6_lower_limit`')

        self._data["Dewpoint Temperature Range 6 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_6_upper_limit(self):
        """Get dewpoint_temperature_range_6_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_6_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 6 Upper Limit"]

    @dewpoint_temperature_range_6_upper_limit.setter
    def dewpoint_temperature_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_6_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_6_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_6_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_6_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_6_upper_limit`')

        self._data["Dewpoint Temperature Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_6_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_6_equipment_list_name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')

        self._data["Range 6 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_7_lower_limit(self):
        """Get dewpoint_temperature_range_7_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_7_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 7 Lower Limit"]

    @dewpoint_temperature_range_7_lower_limit.setter
    def dewpoint_temperature_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_7_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_7_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_7_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_7_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_7_lower_limit`')

        self._data["Dewpoint Temperature Range 7 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_7_upper_limit(self):
        """Get dewpoint_temperature_range_7_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_7_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 7 Upper Limit"]

    @dewpoint_temperature_range_7_upper_limit.setter
    def dewpoint_temperature_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_7_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_7_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_7_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_7_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_7_upper_limit`')

        self._data["Dewpoint Temperature Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_7_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_7_equipment_list_name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')

        self._data["Range 7 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_8_lower_limit(self):
        """Get dewpoint_temperature_range_8_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_8_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 8 Lower Limit"]

    @dewpoint_temperature_range_8_lower_limit.setter
    def dewpoint_temperature_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_8_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_8_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_8_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_8_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_8_lower_limit`')

        self._data["Dewpoint Temperature Range 8 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_8_upper_limit(self):
        """Get dewpoint_temperature_range_8_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_8_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 8 Upper Limit"]

    @dewpoint_temperature_range_8_upper_limit.setter
    def dewpoint_temperature_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_8_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_8_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_8_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_8_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_8_upper_limit`')

        self._data["Dewpoint Temperature Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_8_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_8_equipment_list_name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')

        self._data["Range 8 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_9_lower_limit(self):
        """Get dewpoint_temperature_range_9_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_9_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 9 Lower Limit"]

    @dewpoint_temperature_range_9_lower_limit.setter
    def dewpoint_temperature_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_9_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_9_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_9_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_9_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_9_lower_limit`')

        self._data["Dewpoint Temperature Range 9 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_9_upper_limit(self):
        """Get dewpoint_temperature_range_9_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_9_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 9 Upper Limit"]

    @dewpoint_temperature_range_9_upper_limit.setter
    def dewpoint_temperature_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_9_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_9_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_9_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_9_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_9_upper_limit`')

        self._data["Dewpoint Temperature Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_9_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_9_equipment_list_name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')

        self._data["Range 9 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_10_lower_limit(self):
        """Get dewpoint_temperature_range_10_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_range_10_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 10 Lower Limit"]

    @dewpoint_temperature_range_10_lower_limit.setter
    def dewpoint_temperature_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_10_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_10_lower_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_10_lower_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_10_lower_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_10_lower_limit`')

        self._data["Dewpoint Temperature Range 10 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_10_upper_limit(self):
        """Get dewpoint_temperature_range_10_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_range_10_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Range 10 Upper Limit"]

    @dewpoint_temperature_range_10_upper_limit.setter
    def dewpoint_temperature_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_range_10_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_range_10_upper_limit`
                Unit: C
                value >= -70.0
                value <= 70.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_range_10_upper_limit`'.format(value))
            if value < -70.0:
                raise ValueError('value need to be greater or equal -70.0 '
                                 'for field `dewpoint_temperature_range_10_upper_limit`')
            if value > 70.0:
                raise ValueError('value need to be smaller 70.0 '
                                 'for field `dewpoint_temperature_range_10_upper_limit`')

        self._data["Dewpoint Temperature Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_10_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_10_equipment_list_name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')

        self._data["Range 10 Equipment List Name"] = value

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
        out.append(self._to_str(self.dewpoint_temperature_range_1_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_range_1_upper_limit))
        out.append(self._to_str(self.range_1_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_range_2_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_range_2_upper_limit))
        out.append(self._to_str(self.range_2_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_range_3_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_range_3_upper_limit))
        out.append(self._to_str(self.range_3_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_range_4_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_range_4_upper_limit))
        out.append(self._to_str(self.range_4_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_range_5_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_range_5_upper_limit))
        out.append(self._to_str(self.range_5_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_range_6_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_range_6_upper_limit))
        out.append(self._to_str(self.range_6_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_range_7_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_range_7_upper_limit))
        out.append(self._to_str(self.range_7_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_range_8_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_range_8_upper_limit))
        out.append(self._to_str(self.range_8_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_range_9_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_range_9_upper_limit))
        out.append(self._to_str(self.range_9_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_range_10_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_range_10_upper_limit))
        out.append(self._to_str(self.range_10_equipment_list_name))
        return ",".join(out)

class PlantEquipmentOperationComponentSetpoint(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:ComponentSetpoint`
        Plant equipment operation scheme for component setpoint operation. Specifies one or
        pieces of equipment which are controlled to meet the temperature setpoint at the
        component outlet node.
    """
    internal_name = "PlantEquipmentOperation:ComponentSetpoint"
    field_count = 61

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:ComponentSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Equipment 1 Object Type"] = None
        self._data["Equipment 1 Name"] = None
        self._data["Demand Calculation 1 Node Name"] = None
        self._data["Setpoint 1 Node Name"] = None
        self._data["Component 1 Flow Rate"] = None
        self._data["Operation 1 Type"] = None
        self._data["Equipment 2 Object Type"] = None
        self._data["Equipment 2 Name"] = None
        self._data["Demand Calculation 2 Node Name"] = None
        self._data["Setpoint 2 Node Name"] = None
        self._data["Component 2 Flow Rate"] = None
        self._data["Operation 2 Type"] = None
        self._data["Equipment 3 Object Type"] = None
        self._data["Equipment 3 Name"] = None
        self._data["Demand Calculation 3 Node Name"] = None
        self._data["Setpoint 3 Node Name"] = None
        self._data["Component 3 Flow Rate"] = None
        self._data["Operation 3 Type"] = None
        self._data["Equipment 4 Object Type"] = None
        self._data["Equipment 4 Name"] = None
        self._data["Demand Calculation 4 Node Name"] = None
        self._data["Setpoint 4 Node Name"] = None
        self._data["Component 4 Flow Rate"] = None
        self._data["Operation 4 Type"] = None
        self._data["Equipment 5 Object Type"] = None
        self._data["Equipment 5 Name"] = None
        self._data["Demand Calculation 5 Node Name"] = None
        self._data["Setpoint 5 Node Name"] = None
        self._data["Component 5 Flow Rate"] = None
        self._data["Operation 5 Type"] = None
        self._data["Equipment 6 Object Type"] = None
        self._data["Equipment 6 Name"] = None
        self._data["Demand Calculation 6 Node Name"] = None
        self._data["Setpoint 6 Node Name"] = None
        self._data["Component 6 Flow Rate"] = None
        self._data["Operation 6 Type"] = None
        self._data["Equipment 7 Object Type"] = None
        self._data["Equipment 7 Name"] = None
        self._data["Demand Calculation 7 Node Name"] = None
        self._data["Setpoint 7 Node Name"] = None
        self._data["Component 7 Flow Rate"] = None
        self._data["Operation 7 Type"] = None
        self._data["Equipment 8 Object Type"] = None
        self._data["Equipment 8 Name"] = None
        self._data["Demand Calculation 8 Node Name"] = None
        self._data["Setpoint 8 Node Name"] = None
        self._data["Component 8 Flow Rate"] = None
        self._data["Operation 8 Type"] = None
        self._data["Equipment 9 Object Type"] = None
        self._data["Equipment 9 Name"] = None
        self._data["Demand Calculation 9 Node Name"] = None
        self._data["Setpoint 9 Node Name"] = None
        self._data["Component 9 Flow Rate"] = None
        self._data["Operation 9 Type"] = None
        self._data["Equipment 10 Object Type"] = None
        self._data["Equipment 10 Name"] = None
        self._data["Demand Calculation 10 Node Name"] = None
        self._data["Setpoint 10 Node Name"] = None
        self._data["Component 10 Flow Rate"] = None
        self._data["Operation 10 Type"] = None

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
            self.demand_calculation_1_node_name = None
        else:
            self.demand_calculation_1_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_1_node_name = None
        else:
            self.setpoint_1_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_1_flow_rate = None
        else:
            self.component_1_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_1_type = None
        else:
            self.operation_1_type = vals[i]
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
            self.demand_calculation_2_node_name = None
        else:
            self.demand_calculation_2_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_2_node_name = None
        else:
            self.setpoint_2_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_2_flow_rate = None
        else:
            self.component_2_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_2_type = None
        else:
            self.operation_2_type = vals[i]
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
            self.demand_calculation_3_node_name = None
        else:
            self.demand_calculation_3_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_3_node_name = None
        else:
            self.setpoint_3_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_3_flow_rate = None
        else:
            self.component_3_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_3_type = None
        else:
            self.operation_3_type = vals[i]
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
            self.demand_calculation_4_node_name = None
        else:
            self.demand_calculation_4_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_4_node_name = None
        else:
            self.setpoint_4_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_4_flow_rate = None
        else:
            self.component_4_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_4_type = None
        else:
            self.operation_4_type = vals[i]
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
            self.demand_calculation_5_node_name = None
        else:
            self.demand_calculation_5_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_5_node_name = None
        else:
            self.setpoint_5_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_5_flow_rate = None
        else:
            self.component_5_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_5_type = None
        else:
            self.operation_5_type = vals[i]
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
            self.demand_calculation_6_node_name = None
        else:
            self.demand_calculation_6_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_6_node_name = None
        else:
            self.setpoint_6_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_6_flow_rate = None
        else:
            self.component_6_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_6_type = None
        else:
            self.operation_6_type = vals[i]
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
            self.demand_calculation_7_node_name = None
        else:
            self.demand_calculation_7_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_7_node_name = None
        else:
            self.setpoint_7_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_7_flow_rate = None
        else:
            self.component_7_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_7_type = None
        else:
            self.operation_7_type = vals[i]
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
            self.demand_calculation_8_node_name = None
        else:
            self.demand_calculation_8_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_8_node_name = None
        else:
            self.setpoint_8_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_8_flow_rate = None
        else:
            self.component_8_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_8_type = None
        else:
            self.operation_8_type = vals[i]
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
            self.demand_calculation_9_node_name = None
        else:
            self.demand_calculation_9_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_9_node_name = None
        else:
            self.setpoint_9_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_9_flow_rate = None
        else:
            self.component_9_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_9_type = None
        else:
            self.operation_9_type = vals[i]
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
        if len(vals[i]) == 0:
            self.demand_calculation_10_node_name = None
        else:
            self.demand_calculation_10_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_10_node_name = None
        else:
            self.setpoint_10_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.component_10_flow_rate = None
        else:
            self.component_10_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.operation_10_type = None
        else:
            self.operation_10_type = vals[i]
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
    def demand_calculation_1_node_name(self):
        """Get demand_calculation_1_node_name

        Returns:
            str: the value of `demand_calculation_1_node_name` or None if not set
        """
        return self._data["Demand Calculation 1 Node Name"]

    @demand_calculation_1_node_name.setter
    def demand_calculation_1_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_calculation_1_node_name`

        Args:
            value (str): value for IDD Field `demand_calculation_1_node_name`
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
                                 'for field `demand_calculation_1_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_1_node_name`')

        self._data["Demand Calculation 1 Node Name"] = value

    @property
    def setpoint_1_node_name(self):
        """Get setpoint_1_node_name

        Returns:
            str: the value of `setpoint_1_node_name` or None if not set
        """
        return self._data["Setpoint 1 Node Name"]

    @setpoint_1_node_name.setter
    def setpoint_1_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_1_node_name`

        Args:
            value (str): value for IDD Field `setpoint_1_node_name`
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
                                 'for field `setpoint_1_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_1_node_name`')

        self._data["Setpoint 1 Node Name"] = value

    @property
    def component_1_flow_rate(self):
        """Get component_1_flow_rate

        Returns:
            float: the value of `component_1_flow_rate` or None if not set
        """
        return self._data["Component 1 Flow Rate"]

    @component_1_flow_rate.setter
    def component_1_flow_rate(self, value=None):
        """  Corresponds to IDD Field `component_1_flow_rate`

        Args:
            value (float): value for IDD Field `component_1_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_1_flow_rate`'.format(value))

        self._data["Component 1 Flow Rate"] = value

    @property
    def operation_1_type(self):
        """Get operation_1_type

        Returns:
            str: the value of `operation_1_type` or None if not set
        """
        return self._data["Operation 1 Type"]

    @operation_1_type.setter
    def operation_1_type(self, value=None):
        """  Corresponds to IDD Field `operation_1_type`

        Args:
            value (str): value for IDD Field `operation_1_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_1_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_1_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Dual")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `operation_1_type`'.format(value))

        self._data["Operation 1 Type"] = value

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
    def demand_calculation_2_node_name(self):
        """Get demand_calculation_2_node_name

        Returns:
            str: the value of `demand_calculation_2_node_name` or None if not set
        """
        return self._data["Demand Calculation 2 Node Name"]

    @demand_calculation_2_node_name.setter
    def demand_calculation_2_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_calculation_2_node_name`

        Args:
            value (str): value for IDD Field `demand_calculation_2_node_name`
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
                                 'for field `demand_calculation_2_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_2_node_name`')

        self._data["Demand Calculation 2 Node Name"] = value

    @property
    def setpoint_2_node_name(self):
        """Get setpoint_2_node_name

        Returns:
            str: the value of `setpoint_2_node_name` or None if not set
        """
        return self._data["Setpoint 2 Node Name"]

    @setpoint_2_node_name.setter
    def setpoint_2_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_2_node_name`

        Args:
            value (str): value for IDD Field `setpoint_2_node_name`
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
                                 'for field `setpoint_2_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_2_node_name`')

        self._data["Setpoint 2 Node Name"] = value

    @property
    def component_2_flow_rate(self):
        """Get component_2_flow_rate

        Returns:
            float: the value of `component_2_flow_rate` or None if not set
        """
        return self._data["Component 2 Flow Rate"]

    @component_2_flow_rate.setter
    def component_2_flow_rate(self, value=None):
        """  Corresponds to IDD Field `component_2_flow_rate`

        Args:
            value (float): value for IDD Field `component_2_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_2_flow_rate`'.format(value))

        self._data["Component 2 Flow Rate"] = value

    @property
    def operation_2_type(self):
        """Get operation_2_type

        Returns:
            str: the value of `operation_2_type` or None if not set
        """
        return self._data["Operation 2 Type"]

    @operation_2_type.setter
    def operation_2_type(self, value=None):
        """  Corresponds to IDD Field `operation_2_type`

        Args:
            value (str): value for IDD Field `operation_2_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_2_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_2_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Dual")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `operation_2_type`'.format(value))

        self._data["Operation 2 Type"] = value

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
    def demand_calculation_3_node_name(self):
        """Get demand_calculation_3_node_name

        Returns:
            str: the value of `demand_calculation_3_node_name` or None if not set
        """
        return self._data["Demand Calculation 3 Node Name"]

    @demand_calculation_3_node_name.setter
    def demand_calculation_3_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_calculation_3_node_name`

        Args:
            value (str): value for IDD Field `demand_calculation_3_node_name`
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
                                 'for field `demand_calculation_3_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_3_node_name`')

        self._data["Demand Calculation 3 Node Name"] = value

    @property
    def setpoint_3_node_name(self):
        """Get setpoint_3_node_name

        Returns:
            str: the value of `setpoint_3_node_name` or None if not set
        """
        return self._data["Setpoint 3 Node Name"]

    @setpoint_3_node_name.setter
    def setpoint_3_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_3_node_name`

        Args:
            value (str): value for IDD Field `setpoint_3_node_name`
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
                                 'for field `setpoint_3_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_3_node_name`')

        self._data["Setpoint 3 Node Name"] = value

    @property
    def component_3_flow_rate(self):
        """Get component_3_flow_rate

        Returns:
            float: the value of `component_3_flow_rate` or None if not set
        """
        return self._data["Component 3 Flow Rate"]

    @component_3_flow_rate.setter
    def component_3_flow_rate(self, value=None):
        """  Corresponds to IDD Field `component_3_flow_rate`

        Args:
            value (float): value for IDD Field `component_3_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_3_flow_rate`'.format(value))

        self._data["Component 3 Flow Rate"] = value

    @property
    def operation_3_type(self):
        """Get operation_3_type

        Returns:
            str: the value of `operation_3_type` or None if not set
        """
        return self._data["Operation 3 Type"]

    @operation_3_type.setter
    def operation_3_type(self, value=None):
        """  Corresponds to IDD Field `operation_3_type`

        Args:
            value (str): value for IDD Field `operation_3_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_3_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_3_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Dual")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `operation_3_type`'.format(value))

        self._data["Operation 3 Type"] = value

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
    def demand_calculation_4_node_name(self):
        """Get demand_calculation_4_node_name

        Returns:
            str: the value of `demand_calculation_4_node_name` or None if not set
        """
        return self._data["Demand Calculation 4 Node Name"]

    @demand_calculation_4_node_name.setter
    def demand_calculation_4_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_calculation_4_node_name`

        Args:
            value (str): value for IDD Field `demand_calculation_4_node_name`
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
                                 'for field `demand_calculation_4_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_4_node_name`')

        self._data["Demand Calculation 4 Node Name"] = value

    @property
    def setpoint_4_node_name(self):
        """Get setpoint_4_node_name

        Returns:
            str: the value of `setpoint_4_node_name` or None if not set
        """
        return self._data["Setpoint 4 Node Name"]

    @setpoint_4_node_name.setter
    def setpoint_4_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_4_node_name`

        Args:
            value (str): value for IDD Field `setpoint_4_node_name`
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
                                 'for field `setpoint_4_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_4_node_name`')

        self._data["Setpoint 4 Node Name"] = value

    @property
    def component_4_flow_rate(self):
        """Get component_4_flow_rate

        Returns:
            float: the value of `component_4_flow_rate` or None if not set
        """
        return self._data["Component 4 Flow Rate"]

    @component_4_flow_rate.setter
    def component_4_flow_rate(self, value=None):
        """  Corresponds to IDD Field `component_4_flow_rate`

        Args:
            value (float): value for IDD Field `component_4_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_4_flow_rate`'.format(value))

        self._data["Component 4 Flow Rate"] = value

    @property
    def operation_4_type(self):
        """Get operation_4_type

        Returns:
            str: the value of `operation_4_type` or None if not set
        """
        return self._data["Operation 4 Type"]

    @operation_4_type.setter
    def operation_4_type(self, value=None):
        """  Corresponds to IDD Field `operation_4_type`

        Args:
            value (str): value for IDD Field `operation_4_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_4_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_4_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Dual")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `operation_4_type`'.format(value))

        self._data["Operation 4 Type"] = value

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
    def demand_calculation_5_node_name(self):
        """Get demand_calculation_5_node_name

        Returns:
            str: the value of `demand_calculation_5_node_name` or None if not set
        """
        return self._data["Demand Calculation 5 Node Name"]

    @demand_calculation_5_node_name.setter
    def demand_calculation_5_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_calculation_5_node_name`

        Args:
            value (str): value for IDD Field `demand_calculation_5_node_name`
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
                                 'for field `demand_calculation_5_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_5_node_name`')

        self._data["Demand Calculation 5 Node Name"] = value

    @property
    def setpoint_5_node_name(self):
        """Get setpoint_5_node_name

        Returns:
            str: the value of `setpoint_5_node_name` or None if not set
        """
        return self._data["Setpoint 5 Node Name"]

    @setpoint_5_node_name.setter
    def setpoint_5_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_5_node_name`

        Args:
            value (str): value for IDD Field `setpoint_5_node_name`
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
                                 'for field `setpoint_5_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_5_node_name`')

        self._data["Setpoint 5 Node Name"] = value

    @property
    def component_5_flow_rate(self):
        """Get component_5_flow_rate

        Returns:
            float: the value of `component_5_flow_rate` or None if not set
        """
        return self._data["Component 5 Flow Rate"]

    @component_5_flow_rate.setter
    def component_5_flow_rate(self, value=None):
        """  Corresponds to IDD Field `component_5_flow_rate`

        Args:
            value (float): value for IDD Field `component_5_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_5_flow_rate`'.format(value))

        self._data["Component 5 Flow Rate"] = value

    @property
    def operation_5_type(self):
        """Get operation_5_type

        Returns:
            str: the value of `operation_5_type` or None if not set
        """
        return self._data["Operation 5 Type"]

    @operation_5_type.setter
    def operation_5_type(self, value=None):
        """  Corresponds to IDD Field `operation_5_type`

        Args:
            value (str): value for IDD Field `operation_5_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_5_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_5_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Dual")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `operation_5_type`'.format(value))

        self._data["Operation 5 Type"] = value

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
    def demand_calculation_6_node_name(self):
        """Get demand_calculation_6_node_name

        Returns:
            str: the value of `demand_calculation_6_node_name` or None if not set
        """
        return self._data["Demand Calculation 6 Node Name"]

    @demand_calculation_6_node_name.setter
    def demand_calculation_6_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_calculation_6_node_name`

        Args:
            value (str): value for IDD Field `demand_calculation_6_node_name`
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
                                 'for field `demand_calculation_6_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_6_node_name`')

        self._data["Demand Calculation 6 Node Name"] = value

    @property
    def setpoint_6_node_name(self):
        """Get setpoint_6_node_name

        Returns:
            str: the value of `setpoint_6_node_name` or None if not set
        """
        return self._data["Setpoint 6 Node Name"]

    @setpoint_6_node_name.setter
    def setpoint_6_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_6_node_name`

        Args:
            value (str): value for IDD Field `setpoint_6_node_name`
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
                                 'for field `setpoint_6_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_6_node_name`')

        self._data["Setpoint 6 Node Name"] = value

    @property
    def component_6_flow_rate(self):
        """Get component_6_flow_rate

        Returns:
            float: the value of `component_6_flow_rate` or None if not set
        """
        return self._data["Component 6 Flow Rate"]

    @component_6_flow_rate.setter
    def component_6_flow_rate(self, value=None):
        """  Corresponds to IDD Field `component_6_flow_rate`

        Args:
            value (float): value for IDD Field `component_6_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_6_flow_rate`'.format(value))

        self._data["Component 6 Flow Rate"] = value

    @property
    def operation_6_type(self):
        """Get operation_6_type

        Returns:
            str: the value of `operation_6_type` or None if not set
        """
        return self._data["Operation 6 Type"]

    @operation_6_type.setter
    def operation_6_type(self, value=None):
        """  Corresponds to IDD Field `operation_6_type`

        Args:
            value (str): value for IDD Field `operation_6_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_6_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_6_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Dual")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `operation_6_type`'.format(value))

        self._data["Operation 6 Type"] = value

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
    def demand_calculation_7_node_name(self):
        """Get demand_calculation_7_node_name

        Returns:
            str: the value of `demand_calculation_7_node_name` or None if not set
        """
        return self._data["Demand Calculation 7 Node Name"]

    @demand_calculation_7_node_name.setter
    def demand_calculation_7_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_calculation_7_node_name`

        Args:
            value (str): value for IDD Field `demand_calculation_7_node_name`
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
                                 'for field `demand_calculation_7_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_7_node_name`')

        self._data["Demand Calculation 7 Node Name"] = value

    @property
    def setpoint_7_node_name(self):
        """Get setpoint_7_node_name

        Returns:
            str: the value of `setpoint_7_node_name` or None if not set
        """
        return self._data["Setpoint 7 Node Name"]

    @setpoint_7_node_name.setter
    def setpoint_7_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_7_node_name`

        Args:
            value (str): value for IDD Field `setpoint_7_node_name`
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
                                 'for field `setpoint_7_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_7_node_name`')

        self._data["Setpoint 7 Node Name"] = value

    @property
    def component_7_flow_rate(self):
        """Get component_7_flow_rate

        Returns:
            float: the value of `component_7_flow_rate` or None if not set
        """
        return self._data["Component 7 Flow Rate"]

    @component_7_flow_rate.setter
    def component_7_flow_rate(self, value=None):
        """  Corresponds to IDD Field `component_7_flow_rate`

        Args:
            value (float): value for IDD Field `component_7_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_7_flow_rate`'.format(value))

        self._data["Component 7 Flow Rate"] = value

    @property
    def operation_7_type(self):
        """Get operation_7_type

        Returns:
            str: the value of `operation_7_type` or None if not set
        """
        return self._data["Operation 7 Type"]

    @operation_7_type.setter
    def operation_7_type(self, value=None):
        """  Corresponds to IDD Field `operation_7_type`

        Args:
            value (str): value for IDD Field `operation_7_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_7_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_7_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Dual")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `operation_7_type`'.format(value))

        self._data["Operation 7 Type"] = value

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
    def demand_calculation_8_node_name(self):
        """Get demand_calculation_8_node_name

        Returns:
            str: the value of `demand_calculation_8_node_name` or None if not set
        """
        return self._data["Demand Calculation 8 Node Name"]

    @demand_calculation_8_node_name.setter
    def demand_calculation_8_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_calculation_8_node_name`

        Args:
            value (str): value for IDD Field `demand_calculation_8_node_name`
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
                                 'for field `demand_calculation_8_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_8_node_name`')

        self._data["Demand Calculation 8 Node Name"] = value

    @property
    def setpoint_8_node_name(self):
        """Get setpoint_8_node_name

        Returns:
            str: the value of `setpoint_8_node_name` or None if not set
        """
        return self._data["Setpoint 8 Node Name"]

    @setpoint_8_node_name.setter
    def setpoint_8_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_8_node_name`

        Args:
            value (str): value for IDD Field `setpoint_8_node_name`
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
                                 'for field `setpoint_8_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_8_node_name`')

        self._data["Setpoint 8 Node Name"] = value

    @property
    def component_8_flow_rate(self):
        """Get component_8_flow_rate

        Returns:
            float: the value of `component_8_flow_rate` or None if not set
        """
        return self._data["Component 8 Flow Rate"]

    @component_8_flow_rate.setter
    def component_8_flow_rate(self, value=None):
        """  Corresponds to IDD Field `component_8_flow_rate`

        Args:
            value (float): value for IDD Field `component_8_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_8_flow_rate`'.format(value))

        self._data["Component 8 Flow Rate"] = value

    @property
    def operation_8_type(self):
        """Get operation_8_type

        Returns:
            str: the value of `operation_8_type` or None if not set
        """
        return self._data["Operation 8 Type"]

    @operation_8_type.setter
    def operation_8_type(self, value=None):
        """  Corresponds to IDD Field `operation_8_type`

        Args:
            value (str): value for IDD Field `operation_8_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_8_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_8_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Dual")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `operation_8_type`'.format(value))

        self._data["Operation 8 Type"] = value

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
    def demand_calculation_9_node_name(self):
        """Get demand_calculation_9_node_name

        Returns:
            str: the value of `demand_calculation_9_node_name` or None if not set
        """
        return self._data["Demand Calculation 9 Node Name"]

    @demand_calculation_9_node_name.setter
    def demand_calculation_9_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_calculation_9_node_name`

        Args:
            value (str): value for IDD Field `demand_calculation_9_node_name`
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
                                 'for field `demand_calculation_9_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_9_node_name`')

        self._data["Demand Calculation 9 Node Name"] = value

    @property
    def setpoint_9_node_name(self):
        """Get setpoint_9_node_name

        Returns:
            str: the value of `setpoint_9_node_name` or None if not set
        """
        return self._data["Setpoint 9 Node Name"]

    @setpoint_9_node_name.setter
    def setpoint_9_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_9_node_name`

        Args:
            value (str): value for IDD Field `setpoint_9_node_name`
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
                                 'for field `setpoint_9_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_9_node_name`')

        self._data["Setpoint 9 Node Name"] = value

    @property
    def component_9_flow_rate(self):
        """Get component_9_flow_rate

        Returns:
            float: the value of `component_9_flow_rate` or None if not set
        """
        return self._data["Component 9 Flow Rate"]

    @component_9_flow_rate.setter
    def component_9_flow_rate(self, value=None):
        """  Corresponds to IDD Field `component_9_flow_rate`

        Args:
            value (float): value for IDD Field `component_9_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_9_flow_rate`'.format(value))

        self._data["Component 9 Flow Rate"] = value

    @property
    def operation_9_type(self):
        """Get operation_9_type

        Returns:
            str: the value of `operation_9_type` or None if not set
        """
        return self._data["Operation 9 Type"]

    @operation_9_type.setter
    def operation_9_type(self, value=None):
        """  Corresponds to IDD Field `operation_9_type`

        Args:
            value (str): value for IDD Field `operation_9_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_9_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_9_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Dual")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `operation_9_type`'.format(value))

        self._data["Operation 9 Type"] = value

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

    @property
    def demand_calculation_10_node_name(self):
        """Get demand_calculation_10_node_name

        Returns:
            str: the value of `demand_calculation_10_node_name` or None if not set
        """
        return self._data["Demand Calculation 10 Node Name"]

    @demand_calculation_10_node_name.setter
    def demand_calculation_10_node_name(self, value=None):
        """  Corresponds to IDD Field `demand_calculation_10_node_name`

        Args:
            value (str): value for IDD Field `demand_calculation_10_node_name`
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
                                 'for field `demand_calculation_10_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_calculation_10_node_name`')

        self._data["Demand Calculation 10 Node Name"] = value

    @property
    def setpoint_10_node_name(self):
        """Get setpoint_10_node_name

        Returns:
            str: the value of `setpoint_10_node_name` or None if not set
        """
        return self._data["Setpoint 10 Node Name"]

    @setpoint_10_node_name.setter
    def setpoint_10_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_10_node_name`

        Args:
            value (str): value for IDD Field `setpoint_10_node_name`
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
                                 'for field `setpoint_10_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_10_node_name`')

        self._data["Setpoint 10 Node Name"] = value

    @property
    def component_10_flow_rate(self):
        """Get component_10_flow_rate

        Returns:
            float: the value of `component_10_flow_rate` or None if not set
        """
        return self._data["Component 10 Flow Rate"]

    @component_10_flow_rate.setter
    def component_10_flow_rate(self, value=None):
        """  Corresponds to IDD Field `component_10_flow_rate`

        Args:
            value (float): value for IDD Field `component_10_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `component_10_flow_rate`'.format(value))

        self._data["Component 10 Flow Rate"] = value

    @property
    def operation_10_type(self):
        """Get operation_10_type

        Returns:
            str: the value of `operation_10_type` or None if not set
        """
        return self._data["Operation 10 Type"]

    @operation_10_type.setter
    def operation_10_type(self, value=None):
        """  Corresponds to IDD Field `operation_10_type`

        Args:
            value (str): value for IDD Field `operation_10_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Dual
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
                                 'for field `operation_10_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `operation_10_type`')
            vals = set()
            vals.add("Heating")
            vals.add("Cooling")
            vals.add("Dual")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `operation_10_type`'.format(value))

        self._data["Operation 10 Type"] = value

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
        out.append(self._to_str(self.demand_calculation_1_node_name))
        out.append(self._to_str(self.setpoint_1_node_name))
        out.append(self._to_str(self.component_1_flow_rate))
        out.append(self._to_str(self.operation_1_type))
        out.append(self._to_str(self.equipment_2_object_type))
        out.append(self._to_str(self.equipment_2_name))
        out.append(self._to_str(self.demand_calculation_2_node_name))
        out.append(self._to_str(self.setpoint_2_node_name))
        out.append(self._to_str(self.component_2_flow_rate))
        out.append(self._to_str(self.operation_2_type))
        out.append(self._to_str(self.equipment_3_object_type))
        out.append(self._to_str(self.equipment_3_name))
        out.append(self._to_str(self.demand_calculation_3_node_name))
        out.append(self._to_str(self.setpoint_3_node_name))
        out.append(self._to_str(self.component_3_flow_rate))
        out.append(self._to_str(self.operation_3_type))
        out.append(self._to_str(self.equipment_4_object_type))
        out.append(self._to_str(self.equipment_4_name))
        out.append(self._to_str(self.demand_calculation_4_node_name))
        out.append(self._to_str(self.setpoint_4_node_name))
        out.append(self._to_str(self.component_4_flow_rate))
        out.append(self._to_str(self.operation_4_type))
        out.append(self._to_str(self.equipment_5_object_type))
        out.append(self._to_str(self.equipment_5_name))
        out.append(self._to_str(self.demand_calculation_5_node_name))
        out.append(self._to_str(self.setpoint_5_node_name))
        out.append(self._to_str(self.component_5_flow_rate))
        out.append(self._to_str(self.operation_5_type))
        out.append(self._to_str(self.equipment_6_object_type))
        out.append(self._to_str(self.equipment_6_name))
        out.append(self._to_str(self.demand_calculation_6_node_name))
        out.append(self._to_str(self.setpoint_6_node_name))
        out.append(self._to_str(self.component_6_flow_rate))
        out.append(self._to_str(self.operation_6_type))
        out.append(self._to_str(self.equipment_7_object_type))
        out.append(self._to_str(self.equipment_7_name))
        out.append(self._to_str(self.demand_calculation_7_node_name))
        out.append(self._to_str(self.setpoint_7_node_name))
        out.append(self._to_str(self.component_7_flow_rate))
        out.append(self._to_str(self.operation_7_type))
        out.append(self._to_str(self.equipment_8_object_type))
        out.append(self._to_str(self.equipment_8_name))
        out.append(self._to_str(self.demand_calculation_8_node_name))
        out.append(self._to_str(self.setpoint_8_node_name))
        out.append(self._to_str(self.component_8_flow_rate))
        out.append(self._to_str(self.operation_8_type))
        out.append(self._to_str(self.equipment_9_object_type))
        out.append(self._to_str(self.equipment_9_name))
        out.append(self._to_str(self.demand_calculation_9_node_name))
        out.append(self._to_str(self.setpoint_9_node_name))
        out.append(self._to_str(self.component_9_flow_rate))
        out.append(self._to_str(self.operation_9_type))
        out.append(self._to_str(self.equipment_10_object_type))
        out.append(self._to_str(self.equipment_10_name))
        out.append(self._to_str(self.demand_calculation_10_node_name))
        out.append(self._to_str(self.setpoint_10_node_name))
        out.append(self._to_str(self.component_10_flow_rate))
        out.append(self._to_str(self.operation_10_type))
        return ",".join(out)

class PlantEquipmentOperationOutdoorDryBulbDifference(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDryBulbDifference`
        Plant equipment operation scheme for outdoor dry-bulb temperature difference
        operation. Specifies one or more groups of equipment which are available to operate
        for successive ranges based the difference between a reference node temperature and
        the outdoor dry-bulb temperature.
    """
    internal_name = "PlantEquipmentOperation:OutdoorDryBulbDifference"
    field_count = 32

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:OutdoorDryBulbDifference`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Temperature Node Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 1 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 2 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 3 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 4 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 5 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 6 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 7 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 8 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 9 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Dry-Bulb Temperature Difference Range 10 Lower Limit"] = None
        self._data["Dry-Bulb Temperature Difference Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None

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
            self.reference_temperature_node_name = None
        else:
            self.reference_temperature_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_1_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_1_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_1_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_1_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_2_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_2_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_2_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_2_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_3_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_3_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_3_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_3_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_4_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_4_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_4_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_4_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_5_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_5_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_5_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_5_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_6_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_6_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_6_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_6_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_7_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_7_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_7_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_7_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_8_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_8_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_8_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_8_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_9_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_9_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_9_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_9_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_10_lower_limit = None
        else:
            self.drybulb_temperature_difference_range_10_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drybulb_temperature_difference_range_10_upper_limit = None
        else:
            self.drybulb_temperature_difference_range_10_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def reference_temperature_node_name(self):
        """Get reference_temperature_node_name

        Returns:
            str: the value of `reference_temperature_node_name` or None if not set
        """
        return self._data["Reference Temperature Node Name"]

    @reference_temperature_node_name.setter
    def reference_temperature_node_name(self, value=None):
        """  Corresponds to IDD Field `reference_temperature_node_name`

        Args:
            value (str): value for IDD Field `reference_temperature_node_name`
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
                                 'for field `reference_temperature_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_temperature_node_name`')

        self._data["Reference Temperature Node Name"] = value

    @property
    def drybulb_temperature_difference_range_1_lower_limit(self):
        """Get drybulb_temperature_difference_range_1_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_1_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 1 Lower Limit"]

    @drybulb_temperature_difference_range_1_lower_limit.setter
    def drybulb_temperature_difference_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_1_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_1_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_1_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_1_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_1_lower_limit`')

        self._data["Dry-Bulb Temperature Difference Range 1 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_1_upper_limit(self):
        """Get drybulb_temperature_difference_range_1_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_1_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 1 Upper Limit"]

    @drybulb_temperature_difference_range_1_upper_limit.setter
    def drybulb_temperature_difference_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_1_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_1_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_1_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_1_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_1_upper_limit`')

        self._data["Dry-Bulb Temperature Difference Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_1_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_1_equipment_list_name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')

        self._data["Range 1 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_2_lower_limit(self):
        """Get drybulb_temperature_difference_range_2_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_2_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 2 Lower Limit"]

    @drybulb_temperature_difference_range_2_lower_limit.setter
    def drybulb_temperature_difference_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_2_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_2_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_2_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_2_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_2_lower_limit`')

        self._data["Dry-Bulb Temperature Difference Range 2 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_2_upper_limit(self):
        """Get drybulb_temperature_difference_range_2_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_2_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 2 Upper Limit"]

    @drybulb_temperature_difference_range_2_upper_limit.setter
    def drybulb_temperature_difference_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_2_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_2_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_2_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_2_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_2_upper_limit`')

        self._data["Dry-Bulb Temperature Difference Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_2_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_2_equipment_list_name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')

        self._data["Range 2 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_3_lower_limit(self):
        """Get drybulb_temperature_difference_range_3_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_3_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 3 Lower Limit"]

    @drybulb_temperature_difference_range_3_lower_limit.setter
    def drybulb_temperature_difference_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_3_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_3_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_3_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_3_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_3_lower_limit`')

        self._data["Dry-Bulb Temperature Difference Range 3 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_3_upper_limit(self):
        """Get drybulb_temperature_difference_range_3_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_3_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 3 Upper Limit"]

    @drybulb_temperature_difference_range_3_upper_limit.setter
    def drybulb_temperature_difference_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_3_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_3_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_3_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_3_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_3_upper_limit`')

        self._data["Dry-Bulb Temperature Difference Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_3_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_3_equipment_list_name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')

        self._data["Range 3 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_4_lower_limit(self):
        """Get drybulb_temperature_difference_range_4_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_4_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 4 Lower Limit"]

    @drybulb_temperature_difference_range_4_lower_limit.setter
    def drybulb_temperature_difference_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_4_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_4_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_4_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_4_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_4_lower_limit`')

        self._data["Dry-Bulb Temperature Difference Range 4 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_4_upper_limit(self):
        """Get drybulb_temperature_difference_range_4_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_4_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 4 Upper Limit"]

    @drybulb_temperature_difference_range_4_upper_limit.setter
    def drybulb_temperature_difference_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_4_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_4_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_4_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_4_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_4_upper_limit`')

        self._data["Dry-Bulb Temperature Difference Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_4_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_4_equipment_list_name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')

        self._data["Range 4 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_5_lower_limit(self):
        """Get drybulb_temperature_difference_range_5_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_5_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 5 Lower Limit"]

    @drybulb_temperature_difference_range_5_lower_limit.setter
    def drybulb_temperature_difference_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_5_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_5_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_5_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_5_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_5_lower_limit`')

        self._data["Dry-Bulb Temperature Difference Range 5 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_5_upper_limit(self):
        """Get drybulb_temperature_difference_range_5_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_5_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 5 Upper Limit"]

    @drybulb_temperature_difference_range_5_upper_limit.setter
    def drybulb_temperature_difference_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_5_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_5_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_5_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_5_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_5_upper_limit`')

        self._data["Dry-Bulb Temperature Difference Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_5_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_5_equipment_list_name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')

        self._data["Range 5 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_6_lower_limit(self):
        """Get drybulb_temperature_difference_range_6_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_6_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 6 Lower Limit"]

    @drybulb_temperature_difference_range_6_lower_limit.setter
    def drybulb_temperature_difference_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_6_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_6_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_6_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_6_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_6_lower_limit`')

        self._data["Dry-Bulb Temperature Difference Range 6 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_6_upper_limit(self):
        """Get drybulb_temperature_difference_range_6_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_6_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 6 Upper Limit"]

    @drybulb_temperature_difference_range_6_upper_limit.setter
    def drybulb_temperature_difference_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_6_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_6_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_6_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_6_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_6_upper_limit`')

        self._data["Dry-Bulb Temperature Difference Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_6_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_6_equipment_list_name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')

        self._data["Range 6 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_7_lower_limit(self):
        """Get drybulb_temperature_difference_range_7_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_7_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 7 Lower Limit"]

    @drybulb_temperature_difference_range_7_lower_limit.setter
    def drybulb_temperature_difference_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_7_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_7_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_7_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_7_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_7_lower_limit`')

        self._data["Dry-Bulb Temperature Difference Range 7 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_7_upper_limit(self):
        """Get drybulb_temperature_difference_range_7_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_7_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 7 Upper Limit"]

    @drybulb_temperature_difference_range_7_upper_limit.setter
    def drybulb_temperature_difference_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_7_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_7_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_7_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_7_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_7_upper_limit`')

        self._data["Dry-Bulb Temperature Difference Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_7_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_7_equipment_list_name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')

        self._data["Range 7 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_8_lower_limit(self):
        """Get drybulb_temperature_difference_range_8_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_8_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 8 Lower Limit"]

    @drybulb_temperature_difference_range_8_lower_limit.setter
    def drybulb_temperature_difference_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_8_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_8_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_8_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_8_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_8_lower_limit`')

        self._data["Dry-Bulb Temperature Difference Range 8 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_8_upper_limit(self):
        """Get drybulb_temperature_difference_range_8_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_8_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 8 Upper Limit"]

    @drybulb_temperature_difference_range_8_upper_limit.setter
    def drybulb_temperature_difference_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_8_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_8_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_8_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_8_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_8_upper_limit`')

        self._data["Dry-Bulb Temperature Difference Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_8_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_8_equipment_list_name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')

        self._data["Range 8 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_9_lower_limit(self):
        """Get drybulb_temperature_difference_range_9_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_9_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 9 Lower Limit"]

    @drybulb_temperature_difference_range_9_lower_limit.setter
    def drybulb_temperature_difference_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_9_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_9_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_9_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_9_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_9_lower_limit`')

        self._data["Dry-Bulb Temperature Difference Range 9 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_9_upper_limit(self):
        """Get drybulb_temperature_difference_range_9_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_9_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 9 Upper Limit"]

    @drybulb_temperature_difference_range_9_upper_limit.setter
    def drybulb_temperature_difference_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_9_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_9_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_9_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_9_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_9_upper_limit`')

        self._data["Dry-Bulb Temperature Difference Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_9_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_9_equipment_list_name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')

        self._data["Range 9 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_10_lower_limit(self):
        """Get drybulb_temperature_difference_range_10_lower_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_10_lower_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 10 Lower Limit"]

    @drybulb_temperature_difference_range_10_lower_limit.setter
    def drybulb_temperature_difference_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_10_lower_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_10_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_10_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_10_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_10_lower_limit`')

        self._data["Dry-Bulb Temperature Difference Range 10 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_10_upper_limit(self):
        """Get drybulb_temperature_difference_range_10_upper_limit

        Returns:
            float: the value of `drybulb_temperature_difference_range_10_upper_limit` or None if not set
        """
        return self._data["Dry-Bulb Temperature Difference Range 10 Upper Limit"]

    @drybulb_temperature_difference_range_10_upper_limit.setter
    def drybulb_temperature_difference_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `drybulb_temperature_difference_range_10_upper_limit`

        Args:
            value (float): value for IDD Field `drybulb_temperature_difference_range_10_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `drybulb_temperature_difference_range_10_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `drybulb_temperature_difference_range_10_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `drybulb_temperature_difference_range_10_upper_limit`')

        self._data["Dry-Bulb Temperature Difference Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_10_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_10_equipment_list_name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')

        self._data["Range 10 Equipment List Name"] = value

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
        out.append(self._to_str(self.reference_temperature_node_name))
        out.append(self._to_str(self.drybulb_temperature_difference_range_1_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_difference_range_1_upper_limit))
        out.append(self._to_str(self.range_1_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_difference_range_2_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_difference_range_2_upper_limit))
        out.append(self._to_str(self.range_2_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_difference_range_3_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_difference_range_3_upper_limit))
        out.append(self._to_str(self.range_3_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_difference_range_4_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_difference_range_4_upper_limit))
        out.append(self._to_str(self.range_4_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_difference_range_5_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_difference_range_5_upper_limit))
        out.append(self._to_str(self.range_5_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_difference_range_6_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_difference_range_6_upper_limit))
        out.append(self._to_str(self.range_6_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_difference_range_7_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_difference_range_7_upper_limit))
        out.append(self._to_str(self.range_7_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_difference_range_8_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_difference_range_8_upper_limit))
        out.append(self._to_str(self.range_8_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_difference_range_9_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_difference_range_9_upper_limit))
        out.append(self._to_str(self.range_9_equipment_list_name))
        out.append(self._to_str(self.drybulb_temperature_difference_range_10_lower_limit))
        out.append(self._to_str(self.drybulb_temperature_difference_range_10_upper_limit))
        out.append(self._to_str(self.range_10_equipment_list_name))
        return ",".join(out)

class PlantEquipmentOperationOutdoorWetBulbDifference(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorWetBulbDifference`
        Plant equipment operation scheme for outdoor wet-bulb temperature difference
        operation. Specifies one or more groups of equipment which are available to operate
        for successive ranges based the difference between a reference node temperature and
        the outdoor wet-bulb temperature.
    """
    internal_name = "PlantEquipmentOperation:OutdoorWetBulbDifference"
    field_count = 32

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:OutdoorWetBulbDifference`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Temperature Node Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 1 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 2 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 3 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 4 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 5 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 6 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 7 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 8 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 9 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Wet-Bulb Temperature Difference Range 10 Lower Limit"] = None
        self._data["Wet-Bulb Temperature Difference Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None

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
            self.reference_temperature_node_name = None
        else:
            self.reference_temperature_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_1_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_1_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_1_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_1_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_2_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_2_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_2_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_2_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_3_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_3_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_3_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_3_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_4_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_4_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_4_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_4_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_5_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_5_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_5_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_5_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_6_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_6_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_6_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_6_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_7_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_7_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_7_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_7_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_8_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_8_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_8_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_8_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_9_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_9_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_9_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_9_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_10_lower_limit = None
        else:
            self.wetbulb_temperature_difference_range_10_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wetbulb_temperature_difference_range_10_upper_limit = None
        else:
            self.wetbulb_temperature_difference_range_10_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def reference_temperature_node_name(self):
        """Get reference_temperature_node_name

        Returns:
            str: the value of `reference_temperature_node_name` or None if not set
        """
        return self._data["Reference Temperature Node Name"]

    @reference_temperature_node_name.setter
    def reference_temperature_node_name(self, value=None):
        """  Corresponds to IDD Field `reference_temperature_node_name`

        Args:
            value (str): value for IDD Field `reference_temperature_node_name`
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
                                 'for field `reference_temperature_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_temperature_node_name`')

        self._data["Reference Temperature Node Name"] = value

    @property
    def wetbulb_temperature_difference_range_1_lower_limit(self):
        """Get wetbulb_temperature_difference_range_1_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_1_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 1 Lower Limit"]

    @wetbulb_temperature_difference_range_1_lower_limit.setter
    def wetbulb_temperature_difference_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_1_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_1_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_1_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_1_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_1_lower_limit`')

        self._data["Wet-Bulb Temperature Difference Range 1 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_1_upper_limit(self):
        """Get wetbulb_temperature_difference_range_1_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_1_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 1 Upper Limit"]

    @wetbulb_temperature_difference_range_1_upper_limit.setter
    def wetbulb_temperature_difference_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_1_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_1_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_1_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_1_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_1_upper_limit`')

        self._data["Wet-Bulb Temperature Difference Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_1_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_1_equipment_list_name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')

        self._data["Range 1 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_2_lower_limit(self):
        """Get wetbulb_temperature_difference_range_2_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_2_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 2 Lower Limit"]

    @wetbulb_temperature_difference_range_2_lower_limit.setter
    def wetbulb_temperature_difference_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_2_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_2_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_2_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_2_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_2_lower_limit`')

        self._data["Wet-Bulb Temperature Difference Range 2 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_2_upper_limit(self):
        """Get wetbulb_temperature_difference_range_2_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_2_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 2 Upper Limit"]

    @wetbulb_temperature_difference_range_2_upper_limit.setter
    def wetbulb_temperature_difference_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_2_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_2_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_2_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_2_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_2_upper_limit`')

        self._data["Wet-Bulb Temperature Difference Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_2_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_2_equipment_list_name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')

        self._data["Range 2 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_3_lower_limit(self):
        """Get wetbulb_temperature_difference_range_3_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_3_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 3 Lower Limit"]

    @wetbulb_temperature_difference_range_3_lower_limit.setter
    def wetbulb_temperature_difference_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_3_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_3_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_3_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_3_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_3_lower_limit`')

        self._data["Wet-Bulb Temperature Difference Range 3 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_3_upper_limit(self):
        """Get wetbulb_temperature_difference_range_3_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_3_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 3 Upper Limit"]

    @wetbulb_temperature_difference_range_3_upper_limit.setter
    def wetbulb_temperature_difference_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_3_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_3_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_3_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_3_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_3_upper_limit`')

        self._data["Wet-Bulb Temperature Difference Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_3_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_3_equipment_list_name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')

        self._data["Range 3 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_4_lower_limit(self):
        """Get wetbulb_temperature_difference_range_4_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_4_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 4 Lower Limit"]

    @wetbulb_temperature_difference_range_4_lower_limit.setter
    def wetbulb_temperature_difference_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_4_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_4_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_4_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_4_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_4_lower_limit`')

        self._data["Wet-Bulb Temperature Difference Range 4 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_4_upper_limit(self):
        """Get wetbulb_temperature_difference_range_4_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_4_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 4 Upper Limit"]

    @wetbulb_temperature_difference_range_4_upper_limit.setter
    def wetbulb_temperature_difference_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_4_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_4_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_4_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_4_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_4_upper_limit`')

        self._data["Wet-Bulb Temperature Difference Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_4_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_4_equipment_list_name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')

        self._data["Range 4 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_5_lower_limit(self):
        """Get wetbulb_temperature_difference_range_5_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_5_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 5 Lower Limit"]

    @wetbulb_temperature_difference_range_5_lower_limit.setter
    def wetbulb_temperature_difference_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_5_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_5_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_5_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_5_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_5_lower_limit`')

        self._data["Wet-Bulb Temperature Difference Range 5 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_5_upper_limit(self):
        """Get wetbulb_temperature_difference_range_5_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_5_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 5 Upper Limit"]

    @wetbulb_temperature_difference_range_5_upper_limit.setter
    def wetbulb_temperature_difference_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_5_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_5_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_5_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_5_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_5_upper_limit`')

        self._data["Wet-Bulb Temperature Difference Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_5_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_5_equipment_list_name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')

        self._data["Range 5 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_6_lower_limit(self):
        """Get wetbulb_temperature_difference_range_6_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_6_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 6 Lower Limit"]

    @wetbulb_temperature_difference_range_6_lower_limit.setter
    def wetbulb_temperature_difference_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_6_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_6_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_6_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_6_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_6_lower_limit`')

        self._data["Wet-Bulb Temperature Difference Range 6 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_6_upper_limit(self):
        """Get wetbulb_temperature_difference_range_6_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_6_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 6 Upper Limit"]

    @wetbulb_temperature_difference_range_6_upper_limit.setter
    def wetbulb_temperature_difference_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_6_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_6_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_6_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_6_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_6_upper_limit`')

        self._data["Wet-Bulb Temperature Difference Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_6_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_6_equipment_list_name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')

        self._data["Range 6 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_7_lower_limit(self):
        """Get wetbulb_temperature_difference_range_7_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_7_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 7 Lower Limit"]

    @wetbulb_temperature_difference_range_7_lower_limit.setter
    def wetbulb_temperature_difference_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_7_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_7_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_7_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_7_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_7_lower_limit`')

        self._data["Wet-Bulb Temperature Difference Range 7 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_7_upper_limit(self):
        """Get wetbulb_temperature_difference_range_7_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_7_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 7 Upper Limit"]

    @wetbulb_temperature_difference_range_7_upper_limit.setter
    def wetbulb_temperature_difference_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_7_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_7_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_7_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_7_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_7_upper_limit`')

        self._data["Wet-Bulb Temperature Difference Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_7_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_7_equipment_list_name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')

        self._data["Range 7 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_8_lower_limit(self):
        """Get wetbulb_temperature_difference_range_8_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_8_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 8 Lower Limit"]

    @wetbulb_temperature_difference_range_8_lower_limit.setter
    def wetbulb_temperature_difference_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_8_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_8_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_8_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_8_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_8_lower_limit`')

        self._data["Wet-Bulb Temperature Difference Range 8 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_8_upper_limit(self):
        """Get wetbulb_temperature_difference_range_8_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_8_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 8 Upper Limit"]

    @wetbulb_temperature_difference_range_8_upper_limit.setter
    def wetbulb_temperature_difference_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_8_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_8_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_8_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_8_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_8_upper_limit`')

        self._data["Wet-Bulb Temperature Difference Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_8_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_8_equipment_list_name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')

        self._data["Range 8 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_9_lower_limit(self):
        """Get wetbulb_temperature_difference_range_9_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_9_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 9 Lower Limit"]

    @wetbulb_temperature_difference_range_9_lower_limit.setter
    def wetbulb_temperature_difference_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_9_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_9_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_9_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_9_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_9_lower_limit`')

        self._data["Wet-Bulb Temperature Difference Range 9 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_9_upper_limit(self):
        """Get wetbulb_temperature_difference_range_9_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_9_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 9 Upper Limit"]

    @wetbulb_temperature_difference_range_9_upper_limit.setter
    def wetbulb_temperature_difference_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_9_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_9_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_9_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_9_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_9_upper_limit`')

        self._data["Wet-Bulb Temperature Difference Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_9_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_9_equipment_list_name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')

        self._data["Range 9 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_10_lower_limit(self):
        """Get wetbulb_temperature_difference_range_10_lower_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_10_lower_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 10 Lower Limit"]

    @wetbulb_temperature_difference_range_10_lower_limit.setter
    def wetbulb_temperature_difference_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_10_lower_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_10_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_10_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_10_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_10_lower_limit`')

        self._data["Wet-Bulb Temperature Difference Range 10 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_10_upper_limit(self):
        """Get wetbulb_temperature_difference_range_10_upper_limit

        Returns:
            float: the value of `wetbulb_temperature_difference_range_10_upper_limit` or None if not set
        """
        return self._data["Wet-Bulb Temperature Difference Range 10 Upper Limit"]

    @wetbulb_temperature_difference_range_10_upper_limit.setter
    def wetbulb_temperature_difference_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `wetbulb_temperature_difference_range_10_upper_limit`

        Args:
            value (float): value for IDD Field `wetbulb_temperature_difference_range_10_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `wetbulb_temperature_difference_range_10_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `wetbulb_temperature_difference_range_10_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `wetbulb_temperature_difference_range_10_upper_limit`')

        self._data["Wet-Bulb Temperature Difference Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_10_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_10_equipment_list_name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')

        self._data["Range 10 Equipment List Name"] = value

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
        out.append(self._to_str(self.reference_temperature_node_name))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_1_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_1_upper_limit))
        out.append(self._to_str(self.range_1_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_2_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_2_upper_limit))
        out.append(self._to_str(self.range_2_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_3_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_3_upper_limit))
        out.append(self._to_str(self.range_3_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_4_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_4_upper_limit))
        out.append(self._to_str(self.range_4_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_5_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_5_upper_limit))
        out.append(self._to_str(self.range_5_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_6_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_6_upper_limit))
        out.append(self._to_str(self.range_6_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_7_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_7_upper_limit))
        out.append(self._to_str(self.range_7_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_8_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_8_upper_limit))
        out.append(self._to_str(self.range_8_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_9_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_9_upper_limit))
        out.append(self._to_str(self.range_9_equipment_list_name))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_10_lower_limit))
        out.append(self._to_str(self.wetbulb_temperature_difference_range_10_upper_limit))
        out.append(self._to_str(self.range_10_equipment_list_name))
        return ",".join(out)

class PlantEquipmentOperationOutdoorDewpointDifference(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDewpointDifference`
        Plant equipment operation scheme for outdoor dewpoint temperature difference
        operation. Specifies one or more groups of equipment which are available to operate
        for successive ranges based the difference between a reference node temperature and
        the outdoor dewpoint temperature.
    """
    internal_name = "PlantEquipmentOperation:OutdoorDewpointDifference"
    field_count = 32

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:OutdoorDewpointDifference`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Temperature Node Name"] = None
        self._data["Dewpoint Temperature Difference Range 1 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 1 Upper Limit"] = None
        self._data["Range 1 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 2 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 2 Upper Limit"] = None
        self._data["Range 2 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 3 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 3 Upper Limit"] = None
        self._data["Range 3 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 4 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 4 Upper Limit"] = None
        self._data["Range 4 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 5 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 5 Upper Limit"] = None
        self._data["Range 5 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 6 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 6 Upper Limit"] = None
        self._data["Range 6 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 7 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 7 Upper Limit"] = None
        self._data["Range 7 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 8 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 8 Upper Limit"] = None
        self._data["Range 8 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 9 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 9 Upper Limit"] = None
        self._data["Range 9 Equipment List Name"] = None
        self._data["Dewpoint Temperature Difference Range 10 Lower Limit"] = None
        self._data["Dewpoint Temperature Difference Range 10 Upper Limit"] = None
        self._data["Range 10 Equipment List Name"] = None

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
            self.reference_temperature_node_name = None
        else:
            self.reference_temperature_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_1_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_1_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_1_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_1_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_1_equipment_list_name = None
        else:
            self.range_1_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_2_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_2_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_2_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_2_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_2_equipment_list_name = None
        else:
            self.range_2_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_3_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_3_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_3_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_3_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_3_equipment_list_name = None
        else:
            self.range_3_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_4_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_4_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_4_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_4_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_4_equipment_list_name = None
        else:
            self.range_4_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_5_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_5_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_5_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_5_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_5_equipment_list_name = None
        else:
            self.range_5_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_6_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_6_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_6_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_6_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_6_equipment_list_name = None
        else:
            self.range_6_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_7_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_7_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_7_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_7_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_7_equipment_list_name = None
        else:
            self.range_7_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_8_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_8_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_8_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_8_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_8_equipment_list_name = None
        else:
            self.range_8_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_9_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_9_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_9_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_9_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_9_equipment_list_name = None
        else:
            self.range_9_equipment_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_10_lower_limit = None
        else:
            self.dewpoint_temperature_difference_range_10_lower_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dewpoint_temperature_difference_range_10_upper_limit = None
        else:
            self.dewpoint_temperature_difference_range_10_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.range_10_equipment_list_name = None
        else:
            self.range_10_equipment_list_name = vals[i]
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
    def reference_temperature_node_name(self):
        """Get reference_temperature_node_name

        Returns:
            str: the value of `reference_temperature_node_name` or None if not set
        """
        return self._data["Reference Temperature Node Name"]

    @reference_temperature_node_name.setter
    def reference_temperature_node_name(self, value=None):
        """  Corresponds to IDD Field `reference_temperature_node_name`

        Args:
            value (str): value for IDD Field `reference_temperature_node_name`
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
                                 'for field `reference_temperature_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_temperature_node_name`')

        self._data["Reference Temperature Node Name"] = value

    @property
    def dewpoint_temperature_difference_range_1_lower_limit(self):
        """Get dewpoint_temperature_difference_range_1_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_1_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 1 Lower Limit"]

    @dewpoint_temperature_difference_range_1_lower_limit.setter
    def dewpoint_temperature_difference_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_1_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_1_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_1_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_1_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_1_lower_limit`')

        self._data["Dewpoint Temperature Difference Range 1 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_1_upper_limit(self):
        """Get dewpoint_temperature_difference_range_1_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_1_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 1 Upper Limit"]

    @dewpoint_temperature_difference_range_1_upper_limit.setter
    def dewpoint_temperature_difference_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_1_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_1_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_1_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_1_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_1_upper_limit`')

        self._data["Dewpoint Temperature Difference Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """Get range_1_equipment_list_name

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set
        """
        return self._data["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_1_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_1_equipment_list_name`
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
                                 'for field `range_1_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_1_equipment_list_name`')

        self._data["Range 1 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_2_lower_limit(self):
        """Get dewpoint_temperature_difference_range_2_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_2_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 2 Lower Limit"]

    @dewpoint_temperature_difference_range_2_lower_limit.setter
    def dewpoint_temperature_difference_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_2_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_2_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_2_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_2_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_2_lower_limit`')

        self._data["Dewpoint Temperature Difference Range 2 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_2_upper_limit(self):
        """Get dewpoint_temperature_difference_range_2_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_2_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 2 Upper Limit"]

    @dewpoint_temperature_difference_range_2_upper_limit.setter
    def dewpoint_temperature_difference_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_2_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_2_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_2_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_2_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_2_upper_limit`')

        self._data["Dewpoint Temperature Difference Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """Get range_2_equipment_list_name

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set
        """
        return self._data["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_2_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_2_equipment_list_name`
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
                                 'for field `range_2_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_2_equipment_list_name`')

        self._data["Range 2 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_3_lower_limit(self):
        """Get dewpoint_temperature_difference_range_3_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_3_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 3 Lower Limit"]

    @dewpoint_temperature_difference_range_3_lower_limit.setter
    def dewpoint_temperature_difference_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_3_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_3_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_3_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_3_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_3_lower_limit`')

        self._data["Dewpoint Temperature Difference Range 3 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_3_upper_limit(self):
        """Get dewpoint_temperature_difference_range_3_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_3_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 3 Upper Limit"]

    @dewpoint_temperature_difference_range_3_upper_limit.setter
    def dewpoint_temperature_difference_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_3_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_3_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_3_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_3_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_3_upper_limit`')

        self._data["Dewpoint Temperature Difference Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """Get range_3_equipment_list_name

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set
        """
        return self._data["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_3_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_3_equipment_list_name`
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
                                 'for field `range_3_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_3_equipment_list_name`')

        self._data["Range 3 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_4_lower_limit(self):
        """Get dewpoint_temperature_difference_range_4_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_4_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 4 Lower Limit"]

    @dewpoint_temperature_difference_range_4_lower_limit.setter
    def dewpoint_temperature_difference_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_4_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_4_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_4_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_4_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_4_lower_limit`')

        self._data["Dewpoint Temperature Difference Range 4 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_4_upper_limit(self):
        """Get dewpoint_temperature_difference_range_4_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_4_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 4 Upper Limit"]

    @dewpoint_temperature_difference_range_4_upper_limit.setter
    def dewpoint_temperature_difference_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_4_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_4_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_4_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_4_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_4_upper_limit`')

        self._data["Dewpoint Temperature Difference Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """Get range_4_equipment_list_name

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set
        """
        return self._data["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_4_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_4_equipment_list_name`
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
                                 'for field `range_4_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_4_equipment_list_name`')

        self._data["Range 4 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_5_lower_limit(self):
        """Get dewpoint_temperature_difference_range_5_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_5_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 5 Lower Limit"]

    @dewpoint_temperature_difference_range_5_lower_limit.setter
    def dewpoint_temperature_difference_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_5_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_5_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_5_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_5_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_5_lower_limit`')

        self._data["Dewpoint Temperature Difference Range 5 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_5_upper_limit(self):
        """Get dewpoint_temperature_difference_range_5_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_5_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 5 Upper Limit"]

    @dewpoint_temperature_difference_range_5_upper_limit.setter
    def dewpoint_temperature_difference_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_5_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_5_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_5_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_5_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_5_upper_limit`')

        self._data["Dewpoint Temperature Difference Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """Get range_5_equipment_list_name

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set
        """
        return self._data["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_5_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_5_equipment_list_name`
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
                                 'for field `range_5_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_5_equipment_list_name`')

        self._data["Range 5 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_6_lower_limit(self):
        """Get dewpoint_temperature_difference_range_6_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_6_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 6 Lower Limit"]

    @dewpoint_temperature_difference_range_6_lower_limit.setter
    def dewpoint_temperature_difference_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_6_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_6_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_6_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_6_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_6_lower_limit`')

        self._data["Dewpoint Temperature Difference Range 6 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_6_upper_limit(self):
        """Get dewpoint_temperature_difference_range_6_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_6_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 6 Upper Limit"]

    @dewpoint_temperature_difference_range_6_upper_limit.setter
    def dewpoint_temperature_difference_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_6_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_6_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_6_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_6_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_6_upper_limit`')

        self._data["Dewpoint Temperature Difference Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """Get range_6_equipment_list_name

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set
        """
        return self._data["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_6_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_6_equipment_list_name`
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
                                 'for field `range_6_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_6_equipment_list_name`')

        self._data["Range 6 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_7_lower_limit(self):
        """Get dewpoint_temperature_difference_range_7_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_7_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 7 Lower Limit"]

    @dewpoint_temperature_difference_range_7_lower_limit.setter
    def dewpoint_temperature_difference_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_7_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_7_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_7_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_7_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_7_lower_limit`')

        self._data["Dewpoint Temperature Difference Range 7 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_7_upper_limit(self):
        """Get dewpoint_temperature_difference_range_7_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_7_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 7 Upper Limit"]

    @dewpoint_temperature_difference_range_7_upper_limit.setter
    def dewpoint_temperature_difference_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_7_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_7_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_7_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_7_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_7_upper_limit`')

        self._data["Dewpoint Temperature Difference Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """Get range_7_equipment_list_name

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set
        """
        return self._data["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_7_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_7_equipment_list_name`
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
                                 'for field `range_7_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_7_equipment_list_name`')

        self._data["Range 7 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_8_lower_limit(self):
        """Get dewpoint_temperature_difference_range_8_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_8_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 8 Lower Limit"]

    @dewpoint_temperature_difference_range_8_lower_limit.setter
    def dewpoint_temperature_difference_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_8_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_8_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_8_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_8_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_8_lower_limit`')

        self._data["Dewpoint Temperature Difference Range 8 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_8_upper_limit(self):
        """Get dewpoint_temperature_difference_range_8_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_8_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 8 Upper Limit"]

    @dewpoint_temperature_difference_range_8_upper_limit.setter
    def dewpoint_temperature_difference_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_8_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_8_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_8_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_8_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_8_upper_limit`')

        self._data["Dewpoint Temperature Difference Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """Get range_8_equipment_list_name

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set
        """
        return self._data["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_8_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_8_equipment_list_name`
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
                                 'for field `range_8_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_8_equipment_list_name`')

        self._data["Range 8 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_9_lower_limit(self):
        """Get dewpoint_temperature_difference_range_9_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_9_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 9 Lower Limit"]

    @dewpoint_temperature_difference_range_9_lower_limit.setter
    def dewpoint_temperature_difference_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_9_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_9_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_9_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_9_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_9_lower_limit`')

        self._data["Dewpoint Temperature Difference Range 9 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_9_upper_limit(self):
        """Get dewpoint_temperature_difference_range_9_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_9_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 9 Upper Limit"]

    @dewpoint_temperature_difference_range_9_upper_limit.setter
    def dewpoint_temperature_difference_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_9_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_9_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_9_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_9_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_9_upper_limit`')

        self._data["Dewpoint Temperature Difference Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """Get range_9_equipment_list_name

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set
        """
        return self._data["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_9_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_9_equipment_list_name`
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
                                 'for field `range_9_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_9_equipment_list_name`')

        self._data["Range 9 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_10_lower_limit(self):
        """Get dewpoint_temperature_difference_range_10_lower_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_10_lower_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 10 Lower Limit"]

    @dewpoint_temperature_difference_range_10_lower_limit.setter
    def dewpoint_temperature_difference_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_10_lower_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_10_lower_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_10_lower_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_10_lower_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_10_lower_limit`')

        self._data["Dewpoint Temperature Difference Range 10 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_10_upper_limit(self):
        """Get dewpoint_temperature_difference_range_10_upper_limit

        Returns:
            float: the value of `dewpoint_temperature_difference_range_10_upper_limit` or None if not set
        """
        return self._data["Dewpoint Temperature Difference Range 10 Upper Limit"]

    @dewpoint_temperature_difference_range_10_upper_limit.setter
    def dewpoint_temperature_difference_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD Field `dewpoint_temperature_difference_range_10_upper_limit`

        Args:
            value (float): value for IDD Field `dewpoint_temperature_difference_range_10_upper_limit`
                Unit: deltaC
                value >= -50.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dewpoint_temperature_difference_range_10_upper_limit`'.format(value))
            if value < -50.0:
                raise ValueError('value need to be greater or equal -50.0 '
                                 'for field `dewpoint_temperature_difference_range_10_upper_limit`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `dewpoint_temperature_difference_range_10_upper_limit`')

        self._data["Dewpoint Temperature Difference Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """Get range_10_equipment_list_name

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set
        """
        return self._data["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `range_10_equipment_list_name`

        Args:
            value (str): value for IDD Field `range_10_equipment_list_name`
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
                                 'for field `range_10_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `range_10_equipment_list_name`')

        self._data["Range 10 Equipment List Name"] = value

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
        out.append(self._to_str(self.reference_temperature_node_name))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_1_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_1_upper_limit))
        out.append(self._to_str(self.range_1_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_2_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_2_upper_limit))
        out.append(self._to_str(self.range_2_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_3_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_3_upper_limit))
        out.append(self._to_str(self.range_3_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_4_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_4_upper_limit))
        out.append(self._to_str(self.range_4_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_5_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_5_upper_limit))
        out.append(self._to_str(self.range_5_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_6_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_6_upper_limit))
        out.append(self._to_str(self.range_6_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_7_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_7_upper_limit))
        out.append(self._to_str(self.range_7_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_8_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_8_upper_limit))
        out.append(self._to_str(self.range_8_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_9_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_9_upper_limit))
        out.append(self._to_str(self.range_9_equipment_list_name))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_10_lower_limit))
        out.append(self._to_str(self.dewpoint_temperature_difference_range_10_upper_limit))
        out.append(self._to_str(self.range_10_equipment_list_name))
        return ",".join(out)

class PlantEquipmentOperationUserDefined(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:UserDefined`
        Defines a generic plant operation scheme for custom supervisory control
        using Energy Management System or External Interface to dispatch loads
    """
    internal_name = "PlantEquipmentOperation:UserDefined"
    field_count = 23

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperation:UserDefined`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Main Model Program Calling Manager Name"] = None
        self._data["Initialization Program Calling Manager Name"] = None
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
            self.main_model_program_calling_manager_name = None
        else:
            self.main_model_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initialization_program_calling_manager_name = None
        else:
            self.initialization_program_calling_manager_name = vals[i]
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
        This is the name of the plant operation scheme

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
    def main_model_program_calling_manager_name(self):
        """Get main_model_program_calling_manager_name

        Returns:
            str: the value of `main_model_program_calling_manager_name` or None if not set
        """
        return self._data["Main Model Program Calling Manager Name"]

    @main_model_program_calling_manager_name.setter
    def main_model_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `main_model_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `main_model_program_calling_manager_name`
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
                                 'for field `main_model_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `main_model_program_calling_manager_name`')

        self._data["Main Model Program Calling Manager Name"] = value

    @property
    def initialization_program_calling_manager_name(self):
        """Get initialization_program_calling_manager_name

        Returns:
            str: the value of `initialization_program_calling_manager_name` or None if not set
        """
        return self._data["Initialization Program Calling Manager Name"]

    @initialization_program_calling_manager_name.setter
    def initialization_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `initialization_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `initialization_program_calling_manager_name`
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
                                 'for field `initialization_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `initialization_program_calling_manager_name`')

        self._data["Initialization Program Calling Manager Name"] = value

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
        out.append(self._to_str(self.main_model_program_calling_manager_name))
        out.append(self._to_str(self.initialization_program_calling_manager_name))
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