from collections import OrderedDict

class PlantEquipmentOperationSchemes(object):
    """ Corresponds to IDD object `PlantEquipmentOperationSchemes`
        Operation schemes are listed in "priority" order.  Note that each scheme
        must address the entire load and/or condition ranges for the simulation.
        The actual one selected for use will be the first that is "Scheduled"
        on.  That is, if control scheme 1 is not "on" and control scheme 2
        is -- then control scheme 2 is selected.
        Only plant equipment should be listed on a Control Scheme for this item.
    """
    internal_name = "PlantEquipmentOperationSchemes"
    field_count = 25

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantEquipmentOperationSchemes`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Scheme 1 Object Type"] = None
        self._data["Control Scheme 1 Name"] = None
        self._data["Control Scheme 1 Schedule Name"] = None
        self._data["Control Scheme 2 Object Type"] = None
        self._data["Control Scheme 2 Name"] = None
        self._data["Control Scheme 2 Schedule Name"] = None
        self._data["Control Scheme 3 Object Type"] = None
        self._data["Control Scheme 3 Name"] = None
        self._data["Control Scheme 3 Schedule Name"] = None
        self._data["Control Scheme 4 Object Type"] = None
        self._data["Control Scheme 4 Name"] = None
        self._data["Control Scheme 4 Schedule Name"] = None
        self._data["Control Scheme 5 Object Type"] = None
        self._data["Control Scheme 5 Name"] = None
        self._data["Control Scheme 5 Schedule Name"] = None
        self._data["Control Scheme 6 Object Type"] = None
        self._data["Control Scheme 6 Name"] = None
        self._data["Control Scheme 6 Schedule Name"] = None
        self._data["Control Scheme 7 Object Type"] = None
        self._data["Control Scheme 7 Name"] = None
        self._data["Control Scheme 7 Schedule Name"] = None
        self._data["Control Scheme 8 Object Type"] = None
        self._data["Control Scheme 8 Name"] = None
        self._data["Control Scheme 8 Schedule Name"] = None

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
            self.control_scheme_1_object_type = None
        else:
            self.control_scheme_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_1_name = None
        else:
            self.control_scheme_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_1_schedule_name = None
        else:
            self.control_scheme_1_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_2_object_type = None
        else:
            self.control_scheme_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_2_name = None
        else:
            self.control_scheme_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_2_schedule_name = None
        else:
            self.control_scheme_2_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_3_object_type = None
        else:
            self.control_scheme_3_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_3_name = None
        else:
            self.control_scheme_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_3_schedule_name = None
        else:
            self.control_scheme_3_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_4_object_type = None
        else:
            self.control_scheme_4_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_4_name = None
        else:
            self.control_scheme_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_4_schedule_name = None
        else:
            self.control_scheme_4_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_5_object_type = None
        else:
            self.control_scheme_5_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_5_name = None
        else:
            self.control_scheme_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_5_schedule_name = None
        else:
            self.control_scheme_5_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_6_object_type = None
        else:
            self.control_scheme_6_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_6_name = None
        else:
            self.control_scheme_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_6_schedule_name = None
        else:
            self.control_scheme_6_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_7_object_type = None
        else:
            self.control_scheme_7_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_7_name = None
        else:
            self.control_scheme_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_7_schedule_name = None
        else:
            self.control_scheme_7_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_8_object_type = None
        else:
            self.control_scheme_8_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_8_name = None
        else:
            self.control_scheme_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.control_scheme_8_schedule_name = None
        else:
            self.control_scheme_8_schedule_name = vals[i]
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
    def control_scheme_1_object_type(self):
        """Get control_scheme_1_object_type

        Returns:
            str: the value of `control_scheme_1_object_type` or None if not set
        """
        return self._data["Control Scheme 1 Object Type"]

    @control_scheme_1_object_type.setter
    def control_scheme_1_object_type(self, value=None):
        """  Corresponds to IDD Field `control_scheme_1_object_type`

        Args:
            value (str): value for IDD Field `control_scheme_1_object_type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_1_object_type`')
            vals = set()
            vals.add("PlantEquipmentOperation:CoolingLoad")
            vals.add("PlantEquipmentOperation:HeatingLoad")
            vals.add("PlantEquipmentOperation:Uncontrolled")
            vals.add("PlantEquipmentOperation:ComponentSetpoint")
            vals.add("PlantEquipmentOperation:UserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_scheme_1_object_type`'.format(value))

        self._data["Control Scheme 1 Object Type"] = value

    @property
    def control_scheme_1_name(self):
        """Get control_scheme_1_name

        Returns:
            str: the value of `control_scheme_1_name` or None if not set
        """
        return self._data["Control Scheme 1 Name"]

    @control_scheme_1_name.setter
    def control_scheme_1_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_1_name`

        Args:
            value (str): value for IDD Field `control_scheme_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_1_name`')

        self._data["Control Scheme 1 Name"] = value

    @property
    def control_scheme_1_schedule_name(self):
        """Get control_scheme_1_schedule_name

        Returns:
            str: the value of `control_scheme_1_schedule_name` or None if not set
        """
        return self._data["Control Scheme 1 Schedule Name"]

    @control_scheme_1_schedule_name.setter
    def control_scheme_1_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_1_schedule_name`

        Args:
            value (str): value for IDD Field `control_scheme_1_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_1_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_1_schedule_name`')

        self._data["Control Scheme 1 Schedule Name"] = value

    @property
    def control_scheme_2_object_type(self):
        """Get control_scheme_2_object_type

        Returns:
            str: the value of `control_scheme_2_object_type` or None if not set
        """
        return self._data["Control Scheme 2 Object Type"]

    @control_scheme_2_object_type.setter
    def control_scheme_2_object_type(self, value=None):
        """  Corresponds to IDD Field `control_scheme_2_object_type`

        Args:
            value (str): value for IDD Field `control_scheme_2_object_type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_2_object_type`')
            vals = set()
            vals.add("PlantEquipmentOperation:CoolingLoad")
            vals.add("PlantEquipmentOperation:HeatingLoad")
            vals.add("PlantEquipmentOperation:Uncontrolled")
            vals.add("PlantEquipmentOperation:ComponentSetpoint")
            vals.add("PlantEquipmentOperation:UserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_scheme_2_object_type`'.format(value))

        self._data["Control Scheme 2 Object Type"] = value

    @property
    def control_scheme_2_name(self):
        """Get control_scheme_2_name

        Returns:
            str: the value of `control_scheme_2_name` or None if not set
        """
        return self._data["Control Scheme 2 Name"]

    @control_scheme_2_name.setter
    def control_scheme_2_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_2_name`

        Args:
            value (str): value for IDD Field `control_scheme_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_2_name`')

        self._data["Control Scheme 2 Name"] = value

    @property
    def control_scheme_2_schedule_name(self):
        """Get control_scheme_2_schedule_name

        Returns:
            str: the value of `control_scheme_2_schedule_name` or None if not set
        """
        return self._data["Control Scheme 2 Schedule Name"]

    @control_scheme_2_schedule_name.setter
    def control_scheme_2_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_2_schedule_name`

        Args:
            value (str): value for IDD Field `control_scheme_2_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_2_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_2_schedule_name`')

        self._data["Control Scheme 2 Schedule Name"] = value

    @property
    def control_scheme_3_object_type(self):
        """Get control_scheme_3_object_type

        Returns:
            str: the value of `control_scheme_3_object_type` or None if not set
        """
        return self._data["Control Scheme 3 Object Type"]

    @control_scheme_3_object_type.setter
    def control_scheme_3_object_type(self, value=None):
        """  Corresponds to IDD Field `control_scheme_3_object_type`

        Args:
            value (str): value for IDD Field `control_scheme_3_object_type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_3_object_type`')
            vals = set()
            vals.add("PlantEquipmentOperation:CoolingLoad")
            vals.add("PlantEquipmentOperation:HeatingLoad")
            vals.add("PlantEquipmentOperation:Uncontrolled")
            vals.add("PlantEquipmentOperation:ComponentSetpoint")
            vals.add("PlantEquipmentOperation:UserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_scheme_3_object_type`'.format(value))

        self._data["Control Scheme 3 Object Type"] = value

    @property
    def control_scheme_3_name(self):
        """Get control_scheme_3_name

        Returns:
            str: the value of `control_scheme_3_name` or None if not set
        """
        return self._data["Control Scheme 3 Name"]

    @control_scheme_3_name.setter
    def control_scheme_3_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_3_name`

        Args:
            value (str): value for IDD Field `control_scheme_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_3_name`')

        self._data["Control Scheme 3 Name"] = value

    @property
    def control_scheme_3_schedule_name(self):
        """Get control_scheme_3_schedule_name

        Returns:
            str: the value of `control_scheme_3_schedule_name` or None if not set
        """
        return self._data["Control Scheme 3 Schedule Name"]

    @control_scheme_3_schedule_name.setter
    def control_scheme_3_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_3_schedule_name`

        Args:
            value (str): value for IDD Field `control_scheme_3_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_3_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_3_schedule_name`')

        self._data["Control Scheme 3 Schedule Name"] = value

    @property
    def control_scheme_4_object_type(self):
        """Get control_scheme_4_object_type

        Returns:
            str: the value of `control_scheme_4_object_type` or None if not set
        """
        return self._data["Control Scheme 4 Object Type"]

    @control_scheme_4_object_type.setter
    def control_scheme_4_object_type(self, value=None):
        """  Corresponds to IDD Field `control_scheme_4_object_type`

        Args:
            value (str): value for IDD Field `control_scheme_4_object_type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_4_object_type`')
            vals = set()
            vals.add("PlantEquipmentOperation:CoolingLoad")
            vals.add("PlantEquipmentOperation:HeatingLoad")
            vals.add("PlantEquipmentOperation:Uncontrolled")
            vals.add("PlantEquipmentOperation:ComponentSetpoint")
            vals.add("PlantEquipmentOperation:UserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_scheme_4_object_type`'.format(value))

        self._data["Control Scheme 4 Object Type"] = value

    @property
    def control_scheme_4_name(self):
        """Get control_scheme_4_name

        Returns:
            str: the value of `control_scheme_4_name` or None if not set
        """
        return self._data["Control Scheme 4 Name"]

    @control_scheme_4_name.setter
    def control_scheme_4_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_4_name`

        Args:
            value (str): value for IDD Field `control_scheme_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_4_name`')

        self._data["Control Scheme 4 Name"] = value

    @property
    def control_scheme_4_schedule_name(self):
        """Get control_scheme_4_schedule_name

        Returns:
            str: the value of `control_scheme_4_schedule_name` or None if not set
        """
        return self._data["Control Scheme 4 Schedule Name"]

    @control_scheme_4_schedule_name.setter
    def control_scheme_4_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_4_schedule_name`

        Args:
            value (str): value for IDD Field `control_scheme_4_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_4_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_4_schedule_name`')

        self._data["Control Scheme 4 Schedule Name"] = value

    @property
    def control_scheme_5_object_type(self):
        """Get control_scheme_5_object_type

        Returns:
            str: the value of `control_scheme_5_object_type` or None if not set
        """
        return self._data["Control Scheme 5 Object Type"]

    @control_scheme_5_object_type.setter
    def control_scheme_5_object_type(self, value=None):
        """  Corresponds to IDD Field `control_scheme_5_object_type`

        Args:
            value (str): value for IDD Field `control_scheme_5_object_type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_5_object_type`')
            vals = set()
            vals.add("PlantEquipmentOperation:CoolingLoad")
            vals.add("PlantEquipmentOperation:HeatingLoad")
            vals.add("PlantEquipmentOperation:Uncontrolled")
            vals.add("PlantEquipmentOperation:ComponentSetpoint")
            vals.add("PlantEquipmentOperation:UserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_scheme_5_object_type`'.format(value))

        self._data["Control Scheme 5 Object Type"] = value

    @property
    def control_scheme_5_name(self):
        """Get control_scheme_5_name

        Returns:
            str: the value of `control_scheme_5_name` or None if not set
        """
        return self._data["Control Scheme 5 Name"]

    @control_scheme_5_name.setter
    def control_scheme_5_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_5_name`

        Args:
            value (str): value for IDD Field `control_scheme_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_5_name`')

        self._data["Control Scheme 5 Name"] = value

    @property
    def control_scheme_5_schedule_name(self):
        """Get control_scheme_5_schedule_name

        Returns:
            str: the value of `control_scheme_5_schedule_name` or None if not set
        """
        return self._data["Control Scheme 5 Schedule Name"]

    @control_scheme_5_schedule_name.setter
    def control_scheme_5_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_5_schedule_name`

        Args:
            value (str): value for IDD Field `control_scheme_5_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_5_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_5_schedule_name`')

        self._data["Control Scheme 5 Schedule Name"] = value

    @property
    def control_scheme_6_object_type(self):
        """Get control_scheme_6_object_type

        Returns:
            str: the value of `control_scheme_6_object_type` or None if not set
        """
        return self._data["Control Scheme 6 Object Type"]

    @control_scheme_6_object_type.setter
    def control_scheme_6_object_type(self, value=None):
        """  Corresponds to IDD Field `control_scheme_6_object_type`

        Args:
            value (str): value for IDD Field `control_scheme_6_object_type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_6_object_type`')
            vals = set()
            vals.add("PlantEquipmentOperation:CoolingLoad")
            vals.add("PlantEquipmentOperation:HeatingLoad")
            vals.add("PlantEquipmentOperation:Uncontrolled")
            vals.add("PlantEquipmentOperation:ComponentSetpoint")
            vals.add("PlantEquipmentOperation:UserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_scheme_6_object_type`'.format(value))

        self._data["Control Scheme 6 Object Type"] = value

    @property
    def control_scheme_6_name(self):
        """Get control_scheme_6_name

        Returns:
            str: the value of `control_scheme_6_name` or None if not set
        """
        return self._data["Control Scheme 6 Name"]

    @control_scheme_6_name.setter
    def control_scheme_6_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_6_name`

        Args:
            value (str): value for IDD Field `control_scheme_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_6_name`')

        self._data["Control Scheme 6 Name"] = value

    @property
    def control_scheme_6_schedule_name(self):
        """Get control_scheme_6_schedule_name

        Returns:
            str: the value of `control_scheme_6_schedule_name` or None if not set
        """
        return self._data["Control Scheme 6 Schedule Name"]

    @control_scheme_6_schedule_name.setter
    def control_scheme_6_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_6_schedule_name`

        Args:
            value (str): value for IDD Field `control_scheme_6_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_6_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_6_schedule_name`')

        self._data["Control Scheme 6 Schedule Name"] = value

    @property
    def control_scheme_7_object_type(self):
        """Get control_scheme_7_object_type

        Returns:
            str: the value of `control_scheme_7_object_type` or None if not set
        """
        return self._data["Control Scheme 7 Object Type"]

    @control_scheme_7_object_type.setter
    def control_scheme_7_object_type(self, value=None):
        """  Corresponds to IDD Field `control_scheme_7_object_type`

        Args:
            value (str): value for IDD Field `control_scheme_7_object_type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_7_object_type`')
            vals = set()
            vals.add("PlantEquipmentOperation:CoolingLoad")
            vals.add("PlantEquipmentOperation:HeatingLoad")
            vals.add("PlantEquipmentOperation:Uncontrolled")
            vals.add("PlantEquipmentOperation:ComponentSetpoint")
            vals.add("PlantEquipmentOperation:UserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_scheme_7_object_type`'.format(value))

        self._data["Control Scheme 7 Object Type"] = value

    @property
    def control_scheme_7_name(self):
        """Get control_scheme_7_name

        Returns:
            str: the value of `control_scheme_7_name` or None if not set
        """
        return self._data["Control Scheme 7 Name"]

    @control_scheme_7_name.setter
    def control_scheme_7_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_7_name`

        Args:
            value (str): value for IDD Field `control_scheme_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_7_name`')

        self._data["Control Scheme 7 Name"] = value

    @property
    def control_scheme_7_schedule_name(self):
        """Get control_scheme_7_schedule_name

        Returns:
            str: the value of `control_scheme_7_schedule_name` or None if not set
        """
        return self._data["Control Scheme 7 Schedule Name"]

    @control_scheme_7_schedule_name.setter
    def control_scheme_7_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_7_schedule_name`

        Args:
            value (str): value for IDD Field `control_scheme_7_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_7_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_7_schedule_name`')

        self._data["Control Scheme 7 Schedule Name"] = value

    @property
    def control_scheme_8_object_type(self):
        """Get control_scheme_8_object_type

        Returns:
            str: the value of `control_scheme_8_object_type` or None if not set
        """
        return self._data["Control Scheme 8 Object Type"]

    @control_scheme_8_object_type.setter
    def control_scheme_8_object_type(self, value=None):
        """  Corresponds to IDD Field `control_scheme_8_object_type`

        Args:
            value (str): value for IDD Field `control_scheme_8_object_type`
                Accepted values are:
                      - PlantEquipmentOperation:CoolingLoad
                      - PlantEquipmentOperation:HeatingLoad
                      - PlantEquipmentOperation:Uncontrolled
                      - PlantEquipmentOperation:ComponentSetpoint
                      - PlantEquipmentOperation:UserDefined
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_8_object_type`')
            vals = set()
            vals.add("PlantEquipmentOperation:CoolingLoad")
            vals.add("PlantEquipmentOperation:HeatingLoad")
            vals.add("PlantEquipmentOperation:Uncontrolled")
            vals.add("PlantEquipmentOperation:ComponentSetpoint")
            vals.add("PlantEquipmentOperation:UserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_scheme_8_object_type`'.format(value))

        self._data["Control Scheme 8 Object Type"] = value

    @property
    def control_scheme_8_name(self):
        """Get control_scheme_8_name

        Returns:
            str: the value of `control_scheme_8_name` or None if not set
        """
        return self._data["Control Scheme 8 Name"]

    @control_scheme_8_name.setter
    def control_scheme_8_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_8_name`

        Args:
            value (str): value for IDD Field `control_scheme_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_8_name`')

        self._data["Control Scheme 8 Name"] = value

    @property
    def control_scheme_8_schedule_name(self):
        """Get control_scheme_8_schedule_name

        Returns:
            str: the value of `control_scheme_8_schedule_name` or None if not set
        """
        return self._data["Control Scheme 8 Schedule Name"]

    @control_scheme_8_schedule_name.setter
    def control_scheme_8_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_scheme_8_schedule_name`

        Args:
            value (str): value for IDD Field `control_scheme_8_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_scheme_8_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_scheme_8_schedule_name`')

        self._data["Control Scheme 8 Schedule Name"] = value

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
        out.append(self._to_str(self.control_scheme_1_object_type))
        out.append(self._to_str(self.control_scheme_1_name))
        out.append(self._to_str(self.control_scheme_1_schedule_name))
        out.append(self._to_str(self.control_scheme_2_object_type))
        out.append(self._to_str(self.control_scheme_2_name))
        out.append(self._to_str(self.control_scheme_2_schedule_name))
        out.append(self._to_str(self.control_scheme_3_object_type))
        out.append(self._to_str(self.control_scheme_3_name))
        out.append(self._to_str(self.control_scheme_3_schedule_name))
        out.append(self._to_str(self.control_scheme_4_object_type))
        out.append(self._to_str(self.control_scheme_4_name))
        out.append(self._to_str(self.control_scheme_4_schedule_name))
        out.append(self._to_str(self.control_scheme_5_object_type))
        out.append(self._to_str(self.control_scheme_5_name))
        out.append(self._to_str(self.control_scheme_5_schedule_name))
        out.append(self._to_str(self.control_scheme_6_object_type))
        out.append(self._to_str(self.control_scheme_6_name))
        out.append(self._to_str(self.control_scheme_6_schedule_name))
        out.append(self._to_str(self.control_scheme_7_object_type))
        out.append(self._to_str(self.control_scheme_7_name))
        out.append(self._to_str(self.control_scheme_7_schedule_name))
        out.append(self._to_str(self.control_scheme_8_object_type))
        out.append(self._to_str(self.control_scheme_8_name))
        out.append(self._to_str(self.control_scheme_8_schedule_name))
        return ",".join(out)