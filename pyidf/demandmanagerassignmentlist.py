from collections import OrderedDict

class DemandManagerAssignmentList(object):
    """ Corresponds to IDD object `DemandManagerAssignmentList`
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    internal_name = "DemandManagerAssignmentList"
    field_count = 28

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DemandManagerAssignmentList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Meter Name"] = None
        self._data["Demand Limit Schedule Name"] = None
        self._data["Demand Limit Safety Fraction"] = None
        self._data["Billing Period Schedule Name"] = None
        self._data["Peak Period Schedule Name"] = None
        self._data["Demand Window Length"] = None
        self._data["Demand Manager Priority"] = None
        self._data["DemandManager 1 Object Type"] = None
        self._data["DemandManager 1 Name"] = None
        self._data["DemandManager 2 Object Type"] = None
        self._data["DemandManager 2 Name"] = None
        self._data["DemandManager 3 Object Type"] = None
        self._data["DemandManager 3 Name"] = None
        self._data["DemandManager 4 Object Type"] = None
        self._data["DemandManager 4 Name"] = None
        self._data["DemandManager 5 Object Type"] = None
        self._data["DemandManager 5 Name"] = None
        self._data["DemandManager 6 Object Type"] = None
        self._data["DemandManager 6 Name"] = None
        self._data["DemandManager 7 Object Type"] = None
        self._data["DemandManager 7 Name"] = None
        self._data["DemandManager 8 Object Type"] = None
        self._data["DemandManager 8 Name"] = None
        self._data["DemandManager 9 Object Type"] = None
        self._data["DemandManager 9 Name"] = None
        self._data["DemandManager 10 Object Type"] = None
        self._data["DemandManager 10 Name"] = None

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
            self.meter_name = None
        else:
            self.meter_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_limit_schedule_name = None
        else:
            self.demand_limit_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_limit_safety_fraction = None
        else:
            self.demand_limit_safety_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.billing_period_schedule_name = None
        else:
            self.billing_period_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.peak_period_schedule_name = None
        else:
            self.peak_period_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_window_length = None
        else:
            self.demand_window_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_manager_priority = None
        else:
            self.demand_manager_priority = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_1_object_type = None
        else:
            self.demandmanager_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_1_name = None
        else:
            self.demandmanager_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_2_object_type = None
        else:
            self.demandmanager_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_2_name = None
        else:
            self.demandmanager_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_3_object_type = None
        else:
            self.demandmanager_3_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_3_name = None
        else:
            self.demandmanager_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_4_object_type = None
        else:
            self.demandmanager_4_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_4_name = None
        else:
            self.demandmanager_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_5_object_type = None
        else:
            self.demandmanager_5_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_5_name = None
        else:
            self.demandmanager_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_6_object_type = None
        else:
            self.demandmanager_6_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_6_name = None
        else:
            self.demandmanager_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_7_object_type = None
        else:
            self.demandmanager_7_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_7_name = None
        else:
            self.demandmanager_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_8_object_type = None
        else:
            self.demandmanager_8_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_8_name = None
        else:
            self.demandmanager_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_9_object_type = None
        else:
            self.demandmanager_9_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_9_name = None
        else:
            self.demandmanager_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_10_object_type = None
        else:
            self.demandmanager_10_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demandmanager_10_name = None
        else:
            self.demandmanager_10_name = vals[i]
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
    def meter_name(self):
        """Get meter_name

        Returns:
            str: the value of `meter_name` or None if not set
        """
        return self._data["Meter Name"]

    @meter_name.setter
    def meter_name(self, value=None):
        """  Corresponds to IDD Field `meter_name`

        Args:
            value (str): value for IDD Field `meter_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_name`')

        self._data["Meter Name"] = value

    @property
    def demand_limit_schedule_name(self):
        """Get demand_limit_schedule_name

        Returns:
            str: the value of `demand_limit_schedule_name` or None if not set
        """
        return self._data["Demand Limit Schedule Name"]

    @demand_limit_schedule_name.setter
    def demand_limit_schedule_name(self, value=None):
        """  Corresponds to IDD Field `demand_limit_schedule_name`

        Args:
            value (str): value for IDD Field `demand_limit_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_limit_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_limit_schedule_name`')

        self._data["Demand Limit Schedule Name"] = value

    @property
    def demand_limit_safety_fraction(self):
        """Get demand_limit_safety_fraction

        Returns:
            float: the value of `demand_limit_safety_fraction` or None if not set
        """
        return self._data["Demand Limit Safety Fraction"]

    @demand_limit_safety_fraction.setter
    def demand_limit_safety_fraction(self, value=None):
        """  Corresponds to IDD Field `demand_limit_safety_fraction`

        Args:
            value (float): value for IDD Field `demand_limit_safety_fraction`
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
                                 'for field `demand_limit_safety_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `demand_limit_safety_fraction`')

        self._data["Demand Limit Safety Fraction"] = value

    @property
    def billing_period_schedule_name(self):
        """Get billing_period_schedule_name

        Returns:
            str: the value of `billing_period_schedule_name` or None if not set
        """
        return self._data["Billing Period Schedule Name"]

    @billing_period_schedule_name.setter
    def billing_period_schedule_name(self, value=None):
        """  Corresponds to IDD Field `billing_period_schedule_name`
        This field should reference the same schedule as the month schedule name field of the
        UtilityCost:Tariff object, if used.
        If blank, defaults to regular divisions between months.

        Args:
            value (str): value for IDD Field `billing_period_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `billing_period_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `billing_period_schedule_name`')

        self._data["Billing Period Schedule Name"] = value

    @property
    def peak_period_schedule_name(self):
        """Get peak_period_schedule_name

        Returns:
            str: the value of `peak_period_schedule_name` or None if not set
        """
        return self._data["Peak Period Schedule Name"]

    @peak_period_schedule_name.setter
    def peak_period_schedule_name(self, value=None):
        """  Corresponds to IDD Field `peak_period_schedule_name`
        This field should reference the same schedule as the period schedule name field of the
        UtilityCost:Tariff object, if used.
        If blank, defaults to always on peak.

        Args:
            value (str): value for IDD Field `peak_period_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `peak_period_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `peak_period_schedule_name`')

        self._data["Peak Period Schedule Name"] = value

    @property
    def demand_window_length(self):
        """Get demand_window_length

        Returns:
            int: the value of `demand_window_length` or None if not set
        """
        return self._data["Demand Window Length"]

    @demand_window_length.setter
    def demand_window_length(self, value=None):
        """  Corresponds to IDD Field `demand_window_length`

        Args:
            value (int): value for IDD Field `demand_window_length`
                Unit: minutes
                value > 0
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
                                 'for field `demand_window_length`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `demand_window_length`')

        self._data["Demand Window Length"] = value

    @property
    def demand_manager_priority(self):
        """Get demand_manager_priority

        Returns:
            str: the value of `demand_manager_priority` or None if not set
        """
        return self._data["Demand Manager Priority"]

    @demand_manager_priority.setter
    def demand_manager_priority(self, value=None):
        """  Corresponds to IDD Field `demand_manager_priority`

        Args:
            value (str): value for IDD Field `demand_manager_priority`
                Accepted values are:
                      - Sequential
                      - All
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_manager_priority`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_manager_priority`')
            vals = set()
            vals.add("Sequential")
            vals.add("All")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demand_manager_priority`'.format(value))

        self._data["Demand Manager Priority"] = value

    @property
    def demandmanager_1_object_type(self):
        """Get demandmanager_1_object_type

        Returns:
            str: the value of `demandmanager_1_object_type` or None if not set
        """
        return self._data["DemandManager 1 Object Type"]

    @demandmanager_1_object_type.setter
    def demandmanager_1_object_type(self, value=None):
        """  Corresponds to IDD Field `demandmanager_1_object_type`

        Args:
            value (str): value for IDD Field `demandmanager_1_object_type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_1_object_type`')
            vals = set()
            vals.add("DemandManager:ExteriorLights")
            vals.add("DemandManager:Lights")
            vals.add("DemandManager:ElectricEquipment")
            vals.add("DemandManager:Thermostats")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demandmanager_1_object_type`'.format(value))

        self._data["DemandManager 1 Object Type"] = value

    @property
    def demandmanager_1_name(self):
        """Get demandmanager_1_name

        Returns:
            str: the value of `demandmanager_1_name` or None if not set
        """
        return self._data["DemandManager 1 Name"]

    @demandmanager_1_name.setter
    def demandmanager_1_name(self, value=None):
        """  Corresponds to IDD Field `demandmanager_1_name`

        Args:
            value (str): value for IDD Field `demandmanager_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_1_name`')

        self._data["DemandManager 1 Name"] = value

    @property
    def demandmanager_2_object_type(self):
        """Get demandmanager_2_object_type

        Returns:
            str: the value of `demandmanager_2_object_type` or None if not set
        """
        return self._data["DemandManager 2 Object Type"]

    @demandmanager_2_object_type.setter
    def demandmanager_2_object_type(self, value=None):
        """  Corresponds to IDD Field `demandmanager_2_object_type`

        Args:
            value (str): value for IDD Field `demandmanager_2_object_type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_2_object_type`')
            vals = set()
            vals.add("DemandManager:ExteriorLights")
            vals.add("DemandManager:Lights")
            vals.add("DemandManager:ElectricEquipment")
            vals.add("DemandManager:Thermostats")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demandmanager_2_object_type`'.format(value))

        self._data["DemandManager 2 Object Type"] = value

    @property
    def demandmanager_2_name(self):
        """Get demandmanager_2_name

        Returns:
            str: the value of `demandmanager_2_name` or None if not set
        """
        return self._data["DemandManager 2 Name"]

    @demandmanager_2_name.setter
    def demandmanager_2_name(self, value=None):
        """  Corresponds to IDD Field `demandmanager_2_name`

        Args:
            value (str): value for IDD Field `demandmanager_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_2_name`')

        self._data["DemandManager 2 Name"] = value

    @property
    def demandmanager_3_object_type(self):
        """Get demandmanager_3_object_type

        Returns:
            str: the value of `demandmanager_3_object_type` or None if not set
        """
        return self._data["DemandManager 3 Object Type"]

    @demandmanager_3_object_type.setter
    def demandmanager_3_object_type(self, value=None):
        """  Corresponds to IDD Field `demandmanager_3_object_type`

        Args:
            value (str): value for IDD Field `demandmanager_3_object_type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_3_object_type`')
            vals = set()
            vals.add("DemandManager:ExteriorLights")
            vals.add("DemandManager:Lights")
            vals.add("DemandManager:ElectricEquipment")
            vals.add("DemandManager:Thermostats")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demandmanager_3_object_type`'.format(value))

        self._data["DemandManager 3 Object Type"] = value

    @property
    def demandmanager_3_name(self):
        """Get demandmanager_3_name

        Returns:
            str: the value of `demandmanager_3_name` or None if not set
        """
        return self._data["DemandManager 3 Name"]

    @demandmanager_3_name.setter
    def demandmanager_3_name(self, value=None):
        """  Corresponds to IDD Field `demandmanager_3_name`

        Args:
            value (str): value for IDD Field `demandmanager_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_3_name`')

        self._data["DemandManager 3 Name"] = value

    @property
    def demandmanager_4_object_type(self):
        """Get demandmanager_4_object_type

        Returns:
            str: the value of `demandmanager_4_object_type` or None if not set
        """
        return self._data["DemandManager 4 Object Type"]

    @demandmanager_4_object_type.setter
    def demandmanager_4_object_type(self, value=None):
        """  Corresponds to IDD Field `demandmanager_4_object_type`

        Args:
            value (str): value for IDD Field `demandmanager_4_object_type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_4_object_type`')
            vals = set()
            vals.add("DemandManager:ExteriorLights")
            vals.add("DemandManager:Lights")
            vals.add("DemandManager:ElectricEquipment")
            vals.add("DemandManager:Thermostats")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demandmanager_4_object_type`'.format(value))

        self._data["DemandManager 4 Object Type"] = value

    @property
    def demandmanager_4_name(self):
        """Get demandmanager_4_name

        Returns:
            str: the value of `demandmanager_4_name` or None if not set
        """
        return self._data["DemandManager 4 Name"]

    @demandmanager_4_name.setter
    def demandmanager_4_name(self, value=None):
        """  Corresponds to IDD Field `demandmanager_4_name`

        Args:
            value (str): value for IDD Field `demandmanager_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_4_name`')

        self._data["DemandManager 4 Name"] = value

    @property
    def demandmanager_5_object_type(self):
        """Get demandmanager_5_object_type

        Returns:
            str: the value of `demandmanager_5_object_type` or None if not set
        """
        return self._data["DemandManager 5 Object Type"]

    @demandmanager_5_object_type.setter
    def demandmanager_5_object_type(self, value=None):
        """  Corresponds to IDD Field `demandmanager_5_object_type`

        Args:
            value (str): value for IDD Field `demandmanager_5_object_type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_5_object_type`')
            vals = set()
            vals.add("DemandManager:ExteriorLights")
            vals.add("DemandManager:Lights")
            vals.add("DemandManager:ElectricEquipment")
            vals.add("DemandManager:Thermostats")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demandmanager_5_object_type`'.format(value))

        self._data["DemandManager 5 Object Type"] = value

    @property
    def demandmanager_5_name(self):
        """Get demandmanager_5_name

        Returns:
            str: the value of `demandmanager_5_name` or None if not set
        """
        return self._data["DemandManager 5 Name"]

    @demandmanager_5_name.setter
    def demandmanager_5_name(self, value=None):
        """  Corresponds to IDD Field `demandmanager_5_name`

        Args:
            value (str): value for IDD Field `demandmanager_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_5_name`')

        self._data["DemandManager 5 Name"] = value

    @property
    def demandmanager_6_object_type(self):
        """Get demandmanager_6_object_type

        Returns:
            str: the value of `demandmanager_6_object_type` or None if not set
        """
        return self._data["DemandManager 6 Object Type"]

    @demandmanager_6_object_type.setter
    def demandmanager_6_object_type(self, value=None):
        """  Corresponds to IDD Field `demandmanager_6_object_type`

        Args:
            value (str): value for IDD Field `demandmanager_6_object_type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_6_object_type`')
            vals = set()
            vals.add("DemandManager:ExteriorLights")
            vals.add("DemandManager:Lights")
            vals.add("DemandManager:ElectricEquipment")
            vals.add("DemandManager:Thermostats")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demandmanager_6_object_type`'.format(value))

        self._data["DemandManager 6 Object Type"] = value

    @property
    def demandmanager_6_name(self):
        """Get demandmanager_6_name

        Returns:
            str: the value of `demandmanager_6_name` or None if not set
        """
        return self._data["DemandManager 6 Name"]

    @demandmanager_6_name.setter
    def demandmanager_6_name(self, value=None):
        """  Corresponds to IDD Field `demandmanager_6_name`

        Args:
            value (str): value for IDD Field `demandmanager_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_6_name`')

        self._data["DemandManager 6 Name"] = value

    @property
    def demandmanager_7_object_type(self):
        """Get demandmanager_7_object_type

        Returns:
            str: the value of `demandmanager_7_object_type` or None if not set
        """
        return self._data["DemandManager 7 Object Type"]

    @demandmanager_7_object_type.setter
    def demandmanager_7_object_type(self, value=None):
        """  Corresponds to IDD Field `demandmanager_7_object_type`

        Args:
            value (str): value for IDD Field `demandmanager_7_object_type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_7_object_type`')
            vals = set()
            vals.add("DemandManager:ExteriorLights")
            vals.add("DemandManager:Lights")
            vals.add("DemandManager:ElectricEquipment")
            vals.add("DemandManager:Thermostats")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demandmanager_7_object_type`'.format(value))

        self._data["DemandManager 7 Object Type"] = value

    @property
    def demandmanager_7_name(self):
        """Get demandmanager_7_name

        Returns:
            str: the value of `demandmanager_7_name` or None if not set
        """
        return self._data["DemandManager 7 Name"]

    @demandmanager_7_name.setter
    def demandmanager_7_name(self, value=None):
        """  Corresponds to IDD Field `demandmanager_7_name`

        Args:
            value (str): value for IDD Field `demandmanager_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_7_name`')

        self._data["DemandManager 7 Name"] = value

    @property
    def demandmanager_8_object_type(self):
        """Get demandmanager_8_object_type

        Returns:
            str: the value of `demandmanager_8_object_type` or None if not set
        """
        return self._data["DemandManager 8 Object Type"]

    @demandmanager_8_object_type.setter
    def demandmanager_8_object_type(self, value=None):
        """  Corresponds to IDD Field `demandmanager_8_object_type`

        Args:
            value (str): value for IDD Field `demandmanager_8_object_type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_8_object_type`')
            vals = set()
            vals.add("DemandManager:ExteriorLights")
            vals.add("DemandManager:Lights")
            vals.add("DemandManager:ElectricEquipment")
            vals.add("DemandManager:Thermostats")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demandmanager_8_object_type`'.format(value))

        self._data["DemandManager 8 Object Type"] = value

    @property
    def demandmanager_8_name(self):
        """Get demandmanager_8_name

        Returns:
            str: the value of `demandmanager_8_name` or None if not set
        """
        return self._data["DemandManager 8 Name"]

    @demandmanager_8_name.setter
    def demandmanager_8_name(self, value=None):
        """  Corresponds to IDD Field `demandmanager_8_name`

        Args:
            value (str): value for IDD Field `demandmanager_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_8_name`')

        self._data["DemandManager 8 Name"] = value

    @property
    def demandmanager_9_object_type(self):
        """Get demandmanager_9_object_type

        Returns:
            str: the value of `demandmanager_9_object_type` or None if not set
        """
        return self._data["DemandManager 9 Object Type"]

    @demandmanager_9_object_type.setter
    def demandmanager_9_object_type(self, value=None):
        """  Corresponds to IDD Field `demandmanager_9_object_type`

        Args:
            value (str): value for IDD Field `demandmanager_9_object_type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_9_object_type`')
            vals = set()
            vals.add("DemandManager:ExteriorLights")
            vals.add("DemandManager:Lights")
            vals.add("DemandManager:ElectricEquipment")
            vals.add("DemandManager:Thermostats")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demandmanager_9_object_type`'.format(value))

        self._data["DemandManager 9 Object Type"] = value

    @property
    def demandmanager_9_name(self):
        """Get demandmanager_9_name

        Returns:
            str: the value of `demandmanager_9_name` or None if not set
        """
        return self._data["DemandManager 9 Name"]

    @demandmanager_9_name.setter
    def demandmanager_9_name(self, value=None):
        """  Corresponds to IDD Field `demandmanager_9_name`

        Args:
            value (str): value for IDD Field `demandmanager_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_9_name`')

        self._data["DemandManager 9 Name"] = value

    @property
    def demandmanager_10_object_type(self):
        """Get demandmanager_10_object_type

        Returns:
            str: the value of `demandmanager_10_object_type` or None if not set
        """
        return self._data["DemandManager 10 Object Type"]

    @demandmanager_10_object_type.setter
    def demandmanager_10_object_type(self, value=None):
        """  Corresponds to IDD Field `demandmanager_10_object_type`

        Args:
            value (str): value for IDD Field `demandmanager_10_object_type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_10_object_type`')
            vals = set()
            vals.add("DemandManager:ExteriorLights")
            vals.add("DemandManager:Lights")
            vals.add("DemandManager:ElectricEquipment")
            vals.add("DemandManager:Thermostats")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demandmanager_10_object_type`'.format(value))

        self._data["DemandManager 10 Object Type"] = value

    @property
    def demandmanager_10_name(self):
        """Get demandmanager_10_name

        Returns:
            str: the value of `demandmanager_10_name` or None if not set
        """
        return self._data["DemandManager 10 Name"]

    @demandmanager_10_name.setter
    def demandmanager_10_name(self, value=None):
        """  Corresponds to IDD Field `demandmanager_10_name`

        Args:
            value (str): value for IDD Field `demandmanager_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `demandmanager_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_10_name`')

        self._data["DemandManager 10 Name"] = value

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
        out.append(self._to_str(self.meter_name))
        out.append(self._to_str(self.demand_limit_schedule_name))
        out.append(self._to_str(self.demand_limit_safety_fraction))
        out.append(self._to_str(self.billing_period_schedule_name))
        out.append(self._to_str(self.peak_period_schedule_name))
        out.append(self._to_str(self.demand_window_length))
        out.append(self._to_str(self.demand_manager_priority))
        out.append(self._to_str(self.demandmanager_1_object_type))
        out.append(self._to_str(self.demandmanager_1_name))
        out.append(self._to_str(self.demandmanager_2_object_type))
        out.append(self._to_str(self.demandmanager_2_name))
        out.append(self._to_str(self.demandmanager_3_object_type))
        out.append(self._to_str(self.demandmanager_3_name))
        out.append(self._to_str(self.demandmanager_4_object_type))
        out.append(self._to_str(self.demandmanager_4_name))
        out.append(self._to_str(self.demandmanager_5_object_type))
        out.append(self._to_str(self.demandmanager_5_name))
        out.append(self._to_str(self.demandmanager_6_object_type))
        out.append(self._to_str(self.demandmanager_6_name))
        out.append(self._to_str(self.demandmanager_7_object_type))
        out.append(self._to_str(self.demandmanager_7_name))
        out.append(self._to_str(self.demandmanager_8_object_type))
        out.append(self._to_str(self.demandmanager_8_name))
        out.append(self._to_str(self.demandmanager_9_object_type))
        out.append(self._to_str(self.demandmanager_9_name))
        out.append(self._to_str(self.demandmanager_10_object_type))
        out.append(self._to_str(self.demandmanager_10_name))
        return ",".join(out)