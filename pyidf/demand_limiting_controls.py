from collections import OrderedDict
import logging
import re

class DemandManagerAssignmentList(object):
    """ Corresponds to IDD object `DemandManagerAssignmentList`
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    internal_name = "DemandManagerAssignmentList"
    field_count = 28
    required_fields = ["Name", "Meter Name", "Demand Limit Safety Fraction", "Demand Window Length", "Demand Manager Priority"]

    def __init__(self):
        """ Init data dictionary object for IDD  `DemandManagerAssignmentList`
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
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.meter_name = None
        else:
            self.meter_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_limit_schedule_name = None
        else:
            self.demand_limit_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_limit_safety_fraction = None
        else:
            self.demand_limit_safety_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.billing_period_schedule_name = None
        else:
            self.billing_period_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.peak_period_schedule_name = None
        else:
            self.peak_period_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_window_length = None
        else:
            self.demand_window_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_manager_priority = None
        else:
            self.demand_manager_priority = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_1_object_type = None
        else:
            self.demandmanager_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_1_name = None
        else:
            self.demandmanager_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_2_object_type = None
        else:
            self.demandmanager_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_2_name = None
        else:
            self.demandmanager_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_3_object_type = None
        else:
            self.demandmanager_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_3_name = None
        else:
            self.demandmanager_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_4_object_type = None
        else:
            self.demandmanager_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_4_name = None
        else:
            self.demandmanager_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_5_object_type = None
        else:
            self.demandmanager_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_5_name = None
        else:
            self.demandmanager_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_6_object_type = None
        else:
            self.demandmanager_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_6_name = None
        else:
            self.demandmanager_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_7_object_type = None
        else:
            self.demandmanager_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_7_name = None
        else:
            self.demandmanager_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_8_object_type = None
        else:
            self.demandmanager_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_8_name = None
        else:
            self.demandmanager_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_9_object_type = None
        else:
            self.demandmanager_9_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_9_name = None
        else:
            self.demandmanager_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_10_object_type = None
        else:
            self.demandmanager_10_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demandmanager_10_name = None
        else:
            self.demandmanager_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Meter Name`

        Args:
            value (str): value for IDD Field `Meter Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `meter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Demand Limit Schedule Name`

        Args:
            value (str): value for IDD Field `Demand Limit Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demand_limit_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_limit_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Demand Limit Safety Fraction`

        Args:
            value (float): value for IDD Field `Demand Limit Safety Fraction`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
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
        """  Corresponds to IDD Field `Billing Period Schedule Name`
        This field should reference the same schedule as the month schedule name field of the
        UtilityCost:Tariff object, if used.
        If blank, defaults to regular divisions between months.

        Args:
            value (str): value for IDD Field `Billing Period Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `billing_period_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `billing_period_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Peak Period Schedule Name`
        This field should reference the same schedule as the period schedule name field of the
        UtilityCost:Tariff object, if used.
        If blank, defaults to always on peak.

        Args:
            value (str): value for IDD Field `Peak Period Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `peak_period_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `peak_period_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Demand Window Length`

        Args:
            value (int): value for IDD Field `Demand Window Length`
                Units: minutes
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `demand_window_length`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
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
        """  Corresponds to IDD Field `Demand Manager Priority`

        Args:
            value (str): value for IDD Field `Demand Manager Priority`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demand_manager_priority`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_manager_priority`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_manager_priority`')
            vals = {}
            vals["sequential"] = "Sequential"
            vals["all"] = "All"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demand_manager_priority`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demand_manager_priority`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 1 Object Type`

        Args:
            value (str): value for IDD Field `DemandManager 1 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_1_object_type`')
            vals = {}
            vals["demandmanager:exteriorlights"] = "DemandManager:ExteriorLights"
            vals["demandmanager:lights"] = "DemandManager:Lights"
            vals["demandmanager:electricequipment"] = "DemandManager:ElectricEquipment"
            vals["demandmanager:thermostats"] = "DemandManager:Thermostats"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demandmanager_1_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demandmanager_1_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 1 Name`

        Args:
            value (str): value for IDD Field `DemandManager 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `DemandManager 2 Object Type`

        Args:
            value (str): value for IDD Field `DemandManager 2 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_2_object_type`')
            vals = {}
            vals["demandmanager:exteriorlights"] = "DemandManager:ExteriorLights"
            vals["demandmanager:lights"] = "DemandManager:Lights"
            vals["demandmanager:electricequipment"] = "DemandManager:ElectricEquipment"
            vals["demandmanager:thermostats"] = "DemandManager:Thermostats"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demandmanager_2_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demandmanager_2_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 2 Name`

        Args:
            value (str): value for IDD Field `DemandManager 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `DemandManager 3 Object Type`

        Args:
            value (str): value for IDD Field `DemandManager 3 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_3_object_type`')
            vals = {}
            vals["demandmanager:exteriorlights"] = "DemandManager:ExteriorLights"
            vals["demandmanager:lights"] = "DemandManager:Lights"
            vals["demandmanager:electricequipment"] = "DemandManager:ElectricEquipment"
            vals["demandmanager:thermostats"] = "DemandManager:Thermostats"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demandmanager_3_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demandmanager_3_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 3 Name`

        Args:
            value (str): value for IDD Field `DemandManager 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `DemandManager 4 Object Type`

        Args:
            value (str): value for IDD Field `DemandManager 4 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_4_object_type`')
            vals = {}
            vals["demandmanager:exteriorlights"] = "DemandManager:ExteriorLights"
            vals["demandmanager:lights"] = "DemandManager:Lights"
            vals["demandmanager:electricequipment"] = "DemandManager:ElectricEquipment"
            vals["demandmanager:thermostats"] = "DemandManager:Thermostats"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demandmanager_4_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demandmanager_4_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 4 Name`

        Args:
            value (str): value for IDD Field `DemandManager 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `DemandManager 5 Object Type`

        Args:
            value (str): value for IDD Field `DemandManager 5 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_5_object_type`')
            vals = {}
            vals["demandmanager:exteriorlights"] = "DemandManager:ExteriorLights"
            vals["demandmanager:lights"] = "DemandManager:Lights"
            vals["demandmanager:electricequipment"] = "DemandManager:ElectricEquipment"
            vals["demandmanager:thermostats"] = "DemandManager:Thermostats"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demandmanager_5_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demandmanager_5_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 5 Name`

        Args:
            value (str): value for IDD Field `DemandManager 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `DemandManager 6 Object Type`

        Args:
            value (str): value for IDD Field `DemandManager 6 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_6_object_type`')
            vals = {}
            vals["demandmanager:exteriorlights"] = "DemandManager:ExteriorLights"
            vals["demandmanager:lights"] = "DemandManager:Lights"
            vals["demandmanager:electricequipment"] = "DemandManager:ElectricEquipment"
            vals["demandmanager:thermostats"] = "DemandManager:Thermostats"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demandmanager_6_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demandmanager_6_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 6 Name`

        Args:
            value (str): value for IDD Field `DemandManager 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `DemandManager 7 Object Type`

        Args:
            value (str): value for IDD Field `DemandManager 7 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_7_object_type`')
            vals = {}
            vals["demandmanager:exteriorlights"] = "DemandManager:ExteriorLights"
            vals["demandmanager:lights"] = "DemandManager:Lights"
            vals["demandmanager:electricequipment"] = "DemandManager:ElectricEquipment"
            vals["demandmanager:thermostats"] = "DemandManager:Thermostats"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demandmanager_7_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demandmanager_7_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 7 Name`

        Args:
            value (str): value for IDD Field `DemandManager 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `DemandManager 8 Object Type`

        Args:
            value (str): value for IDD Field `DemandManager 8 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_8_object_type`')
            vals = {}
            vals["demandmanager:exteriorlights"] = "DemandManager:ExteriorLights"
            vals["demandmanager:lights"] = "DemandManager:Lights"
            vals["demandmanager:electricequipment"] = "DemandManager:ElectricEquipment"
            vals["demandmanager:thermostats"] = "DemandManager:Thermostats"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demandmanager_8_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demandmanager_8_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 8 Name`

        Args:
            value (str): value for IDD Field `DemandManager 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `DemandManager 9 Object Type`

        Args:
            value (str): value for IDD Field `DemandManager 9 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_9_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_9_object_type`')
            vals = {}
            vals["demandmanager:exteriorlights"] = "DemandManager:ExteriorLights"
            vals["demandmanager:lights"] = "DemandManager:Lights"
            vals["demandmanager:electricequipment"] = "DemandManager:ElectricEquipment"
            vals["demandmanager:thermostats"] = "DemandManager:Thermostats"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demandmanager_9_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demandmanager_9_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 9 Name`

        Args:
            value (str): value for IDD Field `DemandManager 9 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `DemandManager 10 Object Type`

        Args:
            value (str): value for IDD Field `DemandManager 10 Object Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_10_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_10_object_type`')
            vals = {}
            vals["demandmanager:exteriorlights"] = "DemandManager:ExteriorLights"
            vals["demandmanager:lights"] = "DemandManager:Lights"
            vals["demandmanager:electricequipment"] = "DemandManager:ElectricEquipment"
            vals["demandmanager:thermostats"] = "DemandManager:Thermostats"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demandmanager_10_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `demandmanager_10_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `DemandManager 10 Name`

        Args:
            value (str): value for IDD Field `DemandManager 10 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `demandmanager_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demandmanager_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demandmanager_10_name`')
        self._data["DemandManager 10 Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DemandManagerExteriorLights(object):
    """ Corresponds to IDD object `DemandManager:ExteriorLights`
        used for demand limiting Exterior:Lights objects.
    """
    internal_name = "DemandManager:ExteriorLights"
    field_count = 18
    required_fields = ["Name", "Limit Control", "Selection Control", "Exterior Lights 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `DemandManager:ExteriorLights`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Limit Control"] = None
        self._data["Minimum Limit Duration"] = None
        self._data["Maximum Limit Fraction"] = None
        self._data["Limit Step Change"] = None
        self._data["Selection Control"] = None
        self._data["Rotation Duration"] = None
        self._data["Exterior Lights 1 Name"] = None
        self._data["Exterior Lights 2 Name"] = None
        self._data["Exterior Lights 3 Name"] = None
        self._data["Exterior Lights 4 Name"] = None
        self._data["Exterior Lights 5 Name"] = None
        self._data["Exterior Lights 6 Name"] = None
        self._data["Exterior Lights 7 Name"] = None
        self._data["Exterior Lights 8 Name"] = None
        self._data["Exterior Lights 9 Name"] = None
        self._data["Exterior Lights 10 Name"] = None
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.limit_control = None
        else:
            self.limit_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_limit_duration = None
        else:
            self.minimum_limit_duration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_limit_fraction = None
        else:
            self.maximum_limit_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.limit_step_change = None
        else:
            self.limit_step_change = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.selection_control = None
        else:
            self.selection_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rotation_duration = None
        else:
            self.rotation_duration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exterior_lights_1_name = None
        else:
            self.exterior_lights_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exterior_lights_2_name = None
        else:
            self.exterior_lights_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exterior_lights_3_name = None
        else:
            self.exterior_lights_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exterior_lights_4_name = None
        else:
            self.exterior_lights_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exterior_lights_5_name = None
        else:
            self.exterior_lights_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exterior_lights_6_name = None
        else:
            self.exterior_lights_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exterior_lights_7_name = None
        else:
            self.exterior_lights_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exterior_lights_8_name = None
        else:
            self.exterior_lights_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exterior_lights_9_name = None
        else:
            self.exterior_lights_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exterior_lights_10_name = None
        else:
            self.exterior_lights_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def limit_control(self):
        """Get limit_control

        Returns:
            str: the value of `limit_control` or None if not set
        """
        return self._data["Limit Control"]

    @limit_control.setter
    def limit_control(self, value=None):
        """  Corresponds to IDD Field `Limit Control`

        Args:
            value (str): value for IDD Field `Limit Control`
                Accepted values are:
                      - Off
                      - Fixed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `limit_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `limit_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `limit_control`')
            vals = {}
            vals["off"] = "Off"
            vals["fixed"] = "Fixed"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `limit_control`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `limit_control`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Limit Control"] = value

    @property
    def minimum_limit_duration(self):
        """Get minimum_limit_duration

        Returns:
            int: the value of `minimum_limit_duration` or None if not set
        """
        return self._data["Minimum Limit Duration"]

    @minimum_limit_duration.setter
    def minimum_limit_duration(self, value=None):
        """  Corresponds to IDD Field `Minimum Limit Duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `Minimum Limit Duration`
                Units: minutes
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `minimum_limit_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `minimum_limit_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `minimum_limit_duration`')
        self._data["Minimum Limit Duration"] = value

    @property
    def maximum_limit_fraction(self):
        """Get maximum_limit_fraction

        Returns:
            float: the value of `maximum_limit_fraction` or None if not set
        """
        return self._data["Maximum Limit Fraction"]

    @maximum_limit_fraction.setter
    def maximum_limit_fraction(self, value=None):
        """  Corresponds to IDD Field `Maximum Limit Fraction`

        Args:
            value (float): value for IDD Field `Maximum Limit Fraction`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `maximum_limit_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_limit_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_limit_fraction`')
        self._data["Maximum Limit Fraction"] = value

    @property
    def limit_step_change(self):
        """Get limit_step_change

        Returns:
            float: the value of `limit_step_change` or None if not set
        """
        return self._data["Limit Step Change"]

    @limit_step_change.setter
    def limit_step_change(self, value=None):
        """  Corresponds to IDD Field `Limit Step Change`
        Not yet implemented

        Args:
            value (float): value for IDD Field `Limit Step Change`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `limit_step_change`'.format(value))
        self._data["Limit Step Change"] = value

    @property
    def selection_control(self):
        """Get selection_control

        Returns:
            str: the value of `selection_control` or None if not set
        """
        return self._data["Selection Control"]

    @selection_control.setter
    def selection_control(self, value=None):
        """  Corresponds to IDD Field `Selection Control`

        Args:
            value (str): value for IDD Field `Selection Control`
                Accepted values are:
                      - All
                      - RotateMany
                      - RotateOne
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `selection_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `selection_control`')
            vals = {}
            vals["all"] = "All"
            vals["rotatemany"] = "RotateMany"
            vals["rotateone"] = "RotateOne"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `selection_control`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `selection_control`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Selection Control"] = value

    @property
    def rotation_duration(self):
        """Get rotation_duration

        Returns:
            int: the value of `rotation_duration` or None if not set
        """
        return self._data["Rotation Duration"]

    @rotation_duration.setter
    def rotation_duration(self, value=None):
        """  Corresponds to IDD Field `Rotation Duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `Rotation Duration`
                Units: minutes
                value >= 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `rotation_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `rotation_duration`')
        self._data["Rotation Duration"] = value

    @property
    def exterior_lights_1_name(self):
        """Get exterior_lights_1_name

        Returns:
            str: the value of `exterior_lights_1_name` or None if not set
        """
        return self._data["Exterior Lights 1 Name"]

    @exterior_lights_1_name.setter
    def exterior_lights_1_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Lights 1 Name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `Exterior Lights 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `exterior_lights_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_lights_1_name`')
        self._data["Exterior Lights 1 Name"] = value

    @property
    def exterior_lights_2_name(self):
        """Get exterior_lights_2_name

        Returns:
            str: the value of `exterior_lights_2_name` or None if not set
        """
        return self._data["Exterior Lights 2 Name"]

    @exterior_lights_2_name.setter
    def exterior_lights_2_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Lights 2 Name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `Exterior Lights 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `exterior_lights_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_lights_2_name`')
        self._data["Exterior Lights 2 Name"] = value

    @property
    def exterior_lights_3_name(self):
        """Get exterior_lights_3_name

        Returns:
            str: the value of `exterior_lights_3_name` or None if not set
        """
        return self._data["Exterior Lights 3 Name"]

    @exterior_lights_3_name.setter
    def exterior_lights_3_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Lights 3 Name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `Exterior Lights 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `exterior_lights_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_lights_3_name`')
        self._data["Exterior Lights 3 Name"] = value

    @property
    def exterior_lights_4_name(self):
        """Get exterior_lights_4_name

        Returns:
            str: the value of `exterior_lights_4_name` or None if not set
        """
        return self._data["Exterior Lights 4 Name"]

    @exterior_lights_4_name.setter
    def exterior_lights_4_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Lights 4 Name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `Exterior Lights 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `exterior_lights_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_lights_4_name`')
        self._data["Exterior Lights 4 Name"] = value

    @property
    def exterior_lights_5_name(self):
        """Get exterior_lights_5_name

        Returns:
            str: the value of `exterior_lights_5_name` or None if not set
        """
        return self._data["Exterior Lights 5 Name"]

    @exterior_lights_5_name.setter
    def exterior_lights_5_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Lights 5 Name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `Exterior Lights 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `exterior_lights_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_lights_5_name`')
        self._data["Exterior Lights 5 Name"] = value

    @property
    def exterior_lights_6_name(self):
        """Get exterior_lights_6_name

        Returns:
            str: the value of `exterior_lights_6_name` or None if not set
        """
        return self._data["Exterior Lights 6 Name"]

    @exterior_lights_6_name.setter
    def exterior_lights_6_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Lights 6 Name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `Exterior Lights 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `exterior_lights_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_lights_6_name`')
        self._data["Exterior Lights 6 Name"] = value

    @property
    def exterior_lights_7_name(self):
        """Get exterior_lights_7_name

        Returns:
            str: the value of `exterior_lights_7_name` or None if not set
        """
        return self._data["Exterior Lights 7 Name"]

    @exterior_lights_7_name.setter
    def exterior_lights_7_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Lights 7 Name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `Exterior Lights 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `exterior_lights_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_lights_7_name`')
        self._data["Exterior Lights 7 Name"] = value

    @property
    def exterior_lights_8_name(self):
        """Get exterior_lights_8_name

        Returns:
            str: the value of `exterior_lights_8_name` or None if not set
        """
        return self._data["Exterior Lights 8 Name"]

    @exterior_lights_8_name.setter
    def exterior_lights_8_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Lights 8 Name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `Exterior Lights 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `exterior_lights_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_lights_8_name`')
        self._data["Exterior Lights 8 Name"] = value

    @property
    def exterior_lights_9_name(self):
        """Get exterior_lights_9_name

        Returns:
            str: the value of `exterior_lights_9_name` or None if not set
        """
        return self._data["Exterior Lights 9 Name"]

    @exterior_lights_9_name.setter
    def exterior_lights_9_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Lights 9 Name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `Exterior Lights 9 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `exterior_lights_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_lights_9_name`')
        self._data["Exterior Lights 9 Name"] = value

    @property
    def exterior_lights_10_name(self):
        """Get exterior_lights_10_name

        Returns:
            str: the value of `exterior_lights_10_name` or None if not set
        """
        return self._data["Exterior Lights 10 Name"]

    @exterior_lights_10_name.setter
    def exterior_lights_10_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Lights 10 Name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `Exterior Lights 10 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `exterior_lights_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_lights_10_name`')
        self._data["Exterior Lights 10 Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DemandManagerLights(object):
    """ Corresponds to IDD object `DemandManager:Lights`
        used for demand limiting Lights objects.
    """
    internal_name = "DemandManager:Lights"
    field_count = 18
    required_fields = ["Name", "Limit Control", "Selection Control", "Lights 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `DemandManager:Lights`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Limit Control"] = None
        self._data["Minimum Limit Duration"] = None
        self._data["Maximum Limit Fraction"] = None
        self._data["Limit Step Change"] = None
        self._data["Selection Control"] = None
        self._data["Rotation Duration"] = None
        self._data["Lights 1 Name"] = None
        self._data["Lights 2 Name"] = None
        self._data["Lights 3 Name"] = None
        self._data["Lights 4 Name"] = None
        self._data["Lights 5 Name"] = None
        self._data["Lights 6 Name"] = None
        self._data["Lights 7 Name"] = None
        self._data["Lights 8 Name"] = None
        self._data["Lights 9 Name"] = None
        self._data["Lights 10 Name"] = None
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.limit_control = None
        else:
            self.limit_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_limit_duration = None
        else:
            self.minimum_limit_duration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_limit_fraction = None
        else:
            self.maximum_limit_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.limit_step_change = None
        else:
            self.limit_step_change = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.selection_control = None
        else:
            self.selection_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rotation_duration = None
        else:
            self.rotation_duration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lights_1_name = None
        else:
            self.lights_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lights_2_name = None
        else:
            self.lights_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lights_3_name = None
        else:
            self.lights_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lights_4_name = None
        else:
            self.lights_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lights_5_name = None
        else:
            self.lights_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lights_6_name = None
        else:
            self.lights_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lights_7_name = None
        else:
            self.lights_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lights_8_name = None
        else:
            self.lights_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lights_9_name = None
        else:
            self.lights_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lights_10_name = None
        else:
            self.lights_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def limit_control(self):
        """Get limit_control

        Returns:
            str: the value of `limit_control` or None if not set
        """
        return self._data["Limit Control"]

    @limit_control.setter
    def limit_control(self, value=None):
        """  Corresponds to IDD Field `Limit Control`

        Args:
            value (str): value for IDD Field `Limit Control`
                Accepted values are:
                      - Off
                      - Fixed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `limit_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `limit_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `limit_control`')
            vals = {}
            vals["off"] = "Off"
            vals["fixed"] = "Fixed"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `limit_control`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `limit_control`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Limit Control"] = value

    @property
    def minimum_limit_duration(self):
        """Get minimum_limit_duration

        Returns:
            int: the value of `minimum_limit_duration` or None if not set
        """
        return self._data["Minimum Limit Duration"]

    @minimum_limit_duration.setter
    def minimum_limit_duration(self, value=None):
        """  Corresponds to IDD Field `Minimum Limit Duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `Minimum Limit Duration`
                Units: minutes
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `minimum_limit_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `minimum_limit_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `minimum_limit_duration`')
        self._data["Minimum Limit Duration"] = value

    @property
    def maximum_limit_fraction(self):
        """Get maximum_limit_fraction

        Returns:
            float: the value of `maximum_limit_fraction` or None if not set
        """
        return self._data["Maximum Limit Fraction"]

    @maximum_limit_fraction.setter
    def maximum_limit_fraction(self, value=None):
        """  Corresponds to IDD Field `Maximum Limit Fraction`

        Args:
            value (float): value for IDD Field `Maximum Limit Fraction`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `maximum_limit_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_limit_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_limit_fraction`')
        self._data["Maximum Limit Fraction"] = value

    @property
    def limit_step_change(self):
        """Get limit_step_change

        Returns:
            float: the value of `limit_step_change` or None if not set
        """
        return self._data["Limit Step Change"]

    @limit_step_change.setter
    def limit_step_change(self, value=None):
        """  Corresponds to IDD Field `Limit Step Change`
        Not yet implemented

        Args:
            value (float): value for IDD Field `Limit Step Change`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `limit_step_change`'.format(value))
        self._data["Limit Step Change"] = value

    @property
    def selection_control(self):
        """Get selection_control

        Returns:
            str: the value of `selection_control` or None if not set
        """
        return self._data["Selection Control"]

    @selection_control.setter
    def selection_control(self, value=None):
        """  Corresponds to IDD Field `Selection Control`

        Args:
            value (str): value for IDD Field `Selection Control`
                Accepted values are:
                      - All
                      - RotateMany
                      - RotateOne
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `selection_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `selection_control`')
            vals = {}
            vals["all"] = "All"
            vals["rotatemany"] = "RotateMany"
            vals["rotateone"] = "RotateOne"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `selection_control`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `selection_control`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Selection Control"] = value

    @property
    def rotation_duration(self):
        """Get rotation_duration

        Returns:
            int: the value of `rotation_duration` or None if not set
        """
        return self._data["Rotation Duration"]

    @rotation_duration.setter
    def rotation_duration(self, value=None):
        """  Corresponds to IDD Field `Rotation Duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `Rotation Duration`
                Units: minutes
                value >= 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `rotation_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `rotation_duration`')
        self._data["Rotation Duration"] = value

    @property
    def lights_1_name(self):
        """Get lights_1_name

        Returns:
            str: the value of `lights_1_name` or None if not set
        """
        return self._data["Lights 1 Name"]

    @lights_1_name.setter
    def lights_1_name(self, value=None):
        """  Corresponds to IDD Field `Lights 1 Name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `Lights 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `lights_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lights_1_name`')
        self._data["Lights 1 Name"] = value

    @property
    def lights_2_name(self):
        """Get lights_2_name

        Returns:
            str: the value of `lights_2_name` or None if not set
        """
        return self._data["Lights 2 Name"]

    @lights_2_name.setter
    def lights_2_name(self, value=None):
        """  Corresponds to IDD Field `Lights 2 Name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `Lights 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `lights_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lights_2_name`')
        self._data["Lights 2 Name"] = value

    @property
    def lights_3_name(self):
        """Get lights_3_name

        Returns:
            str: the value of `lights_3_name` or None if not set
        """
        return self._data["Lights 3 Name"]

    @lights_3_name.setter
    def lights_3_name(self, value=None):
        """  Corresponds to IDD Field `Lights 3 Name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `Lights 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `lights_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lights_3_name`')
        self._data["Lights 3 Name"] = value

    @property
    def lights_4_name(self):
        """Get lights_4_name

        Returns:
            str: the value of `lights_4_name` or None if not set
        """
        return self._data["Lights 4 Name"]

    @lights_4_name.setter
    def lights_4_name(self, value=None):
        """  Corresponds to IDD Field `Lights 4 Name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `Lights 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `lights_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lights_4_name`')
        self._data["Lights 4 Name"] = value

    @property
    def lights_5_name(self):
        """Get lights_5_name

        Returns:
            str: the value of `lights_5_name` or None if not set
        """
        return self._data["Lights 5 Name"]

    @lights_5_name.setter
    def lights_5_name(self, value=None):
        """  Corresponds to IDD Field `Lights 5 Name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `Lights 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `lights_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lights_5_name`')
        self._data["Lights 5 Name"] = value

    @property
    def lights_6_name(self):
        """Get lights_6_name

        Returns:
            str: the value of `lights_6_name` or None if not set
        """
        return self._data["Lights 6 Name"]

    @lights_6_name.setter
    def lights_6_name(self, value=None):
        """  Corresponds to IDD Field `Lights 6 Name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `Lights 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `lights_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lights_6_name`')
        self._data["Lights 6 Name"] = value

    @property
    def lights_7_name(self):
        """Get lights_7_name

        Returns:
            str: the value of `lights_7_name` or None if not set
        """
        return self._data["Lights 7 Name"]

    @lights_7_name.setter
    def lights_7_name(self, value=None):
        """  Corresponds to IDD Field `Lights 7 Name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `Lights 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `lights_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lights_7_name`')
        self._data["Lights 7 Name"] = value

    @property
    def lights_8_name(self):
        """Get lights_8_name

        Returns:
            str: the value of `lights_8_name` or None if not set
        """
        return self._data["Lights 8 Name"]

    @lights_8_name.setter
    def lights_8_name(self, value=None):
        """  Corresponds to IDD Field `Lights 8 Name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `Lights 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `lights_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lights_8_name`')
        self._data["Lights 8 Name"] = value

    @property
    def lights_9_name(self):
        """Get lights_9_name

        Returns:
            str: the value of `lights_9_name` or None if not set
        """
        return self._data["Lights 9 Name"]

    @lights_9_name.setter
    def lights_9_name(self, value=None):
        """  Corresponds to IDD Field `Lights 9 Name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `Lights 9 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `lights_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lights_9_name`')
        self._data["Lights 9 Name"] = value

    @property
    def lights_10_name(self):
        """Get lights_10_name

        Returns:
            str: the value of `lights_10_name` or None if not set
        """
        return self._data["Lights 10 Name"]

    @lights_10_name.setter
    def lights_10_name(self, value=None):
        """  Corresponds to IDD Field `Lights 10 Name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `Lights 10 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `lights_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `lights_10_name`')
        self._data["Lights 10 Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DemandManagerElectricEquipment(object):
    """ Corresponds to IDD object `DemandManager:ElectricEquipment`
        used for demand limiting ElectricEquipment objects.
    """
    internal_name = "DemandManager:ElectricEquipment"
    field_count = 18
    required_fields = ["Name", "Limit Control", "Selection Control", "Electric Equipment 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `DemandManager:ElectricEquipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Limit Control"] = None
        self._data["Minimum Limit Duration"] = None
        self._data["Maximum Limit Fraction"] = None
        self._data["Limit Step Change"] = None
        self._data["Selection Control"] = None
        self._data["Rotation Duration"] = None
        self._data["Electric Equipment 1 Name"] = None
        self._data["Electric Equipment 2 Name"] = None
        self._data["Electric Equipment 3 Name"] = None
        self._data["Electric Equipment 4 Name"] = None
        self._data["Electric Equipment 5 Name"] = None
        self._data["Electric Equipment 6 Name"] = None
        self._data["Electric Equipment 7 Name"] = None
        self._data["Electric Equipment 8 Name"] = None
        self._data["Electric Equipment 9 Name"] = None
        self._data["Electric Equipment 10 Name"] = None
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.limit_control = None
        else:
            self.limit_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_limit_duration = None
        else:
            self.minimum_limit_duration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_limit_fraction = None
        else:
            self.maximum_limit_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.limit_step_change = None
        else:
            self.limit_step_change = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.selection_control = None
        else:
            self.selection_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rotation_duration = None
        else:
            self.rotation_duration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electric_equipment_1_name = None
        else:
            self.electric_equipment_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electric_equipment_2_name = None
        else:
            self.electric_equipment_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electric_equipment_3_name = None
        else:
            self.electric_equipment_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electric_equipment_4_name = None
        else:
            self.electric_equipment_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electric_equipment_5_name = None
        else:
            self.electric_equipment_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electric_equipment_6_name = None
        else:
            self.electric_equipment_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electric_equipment_7_name = None
        else:
            self.electric_equipment_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electric_equipment_8_name = None
        else:
            self.electric_equipment_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electric_equipment_9_name = None
        else:
            self.electric_equipment_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.electric_equipment_10_name = None
        else:
            self.electric_equipment_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def limit_control(self):
        """Get limit_control

        Returns:
            str: the value of `limit_control` or None if not set
        """
        return self._data["Limit Control"]

    @limit_control.setter
    def limit_control(self, value=None):
        """  Corresponds to IDD Field `Limit Control`

        Args:
            value (str): value for IDD Field `Limit Control`
                Accepted values are:
                      - Off
                      - Fixed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `limit_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `limit_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `limit_control`')
            vals = {}
            vals["off"] = "Off"
            vals["fixed"] = "Fixed"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `limit_control`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `limit_control`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Limit Control"] = value

    @property
    def minimum_limit_duration(self):
        """Get minimum_limit_duration

        Returns:
            int: the value of `minimum_limit_duration` or None if not set
        """
        return self._data["Minimum Limit Duration"]

    @minimum_limit_duration.setter
    def minimum_limit_duration(self, value=None):
        """  Corresponds to IDD Field `Minimum Limit Duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `Minimum Limit Duration`
                Units: minutes
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `minimum_limit_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `minimum_limit_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `minimum_limit_duration`')
        self._data["Minimum Limit Duration"] = value

    @property
    def maximum_limit_fraction(self):
        """Get maximum_limit_fraction

        Returns:
            float: the value of `maximum_limit_fraction` or None if not set
        """
        return self._data["Maximum Limit Fraction"]

    @maximum_limit_fraction.setter
    def maximum_limit_fraction(self, value=None):
        """  Corresponds to IDD Field `Maximum Limit Fraction`

        Args:
            value (float): value for IDD Field `Maximum Limit Fraction`
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `maximum_limit_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_limit_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_limit_fraction`')
        self._data["Maximum Limit Fraction"] = value

    @property
    def limit_step_change(self):
        """Get limit_step_change

        Returns:
            float: the value of `limit_step_change` or None if not set
        """
        return self._data["Limit Step Change"]

    @limit_step_change.setter
    def limit_step_change(self, value=None):
        """  Corresponds to IDD Field `Limit Step Change`
        Not yet implemented

        Args:
            value (float): value for IDD Field `Limit Step Change`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `limit_step_change`'.format(value))
        self._data["Limit Step Change"] = value

    @property
    def selection_control(self):
        """Get selection_control

        Returns:
            str: the value of `selection_control` or None if not set
        """
        return self._data["Selection Control"]

    @selection_control.setter
    def selection_control(self, value=None):
        """  Corresponds to IDD Field `Selection Control`

        Args:
            value (str): value for IDD Field `Selection Control`
                Accepted values are:
                      - All
                      - RotateMany
                      - RotateOne
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `selection_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `selection_control`')
            vals = {}
            vals["all"] = "All"
            vals["rotatemany"] = "RotateMany"
            vals["rotateone"] = "RotateOne"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `selection_control`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `selection_control`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Selection Control"] = value

    @property
    def rotation_duration(self):
        """Get rotation_duration

        Returns:
            int: the value of `rotation_duration` or None if not set
        """
        return self._data["Rotation Duration"]

    @rotation_duration.setter
    def rotation_duration(self, value=None):
        """  Corresponds to IDD Field `Rotation Duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `Rotation Duration`
                Units: minutes
                value >= 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `rotation_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `rotation_duration`')
        self._data["Rotation Duration"] = value

    @property
    def electric_equipment_1_name(self):
        """Get electric_equipment_1_name

        Returns:
            str: the value of `electric_equipment_1_name` or None if not set
        """
        return self._data["Electric Equipment 1 Name"]

    @electric_equipment_1_name.setter
    def electric_equipment_1_name(self, value=None):
        """  Corresponds to IDD Field `Electric Equipment 1 Name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `Electric Equipment 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `electric_equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electric_equipment_1_name`')
        self._data["Electric Equipment 1 Name"] = value

    @property
    def electric_equipment_2_name(self):
        """Get electric_equipment_2_name

        Returns:
            str: the value of `electric_equipment_2_name` or None if not set
        """
        return self._data["Electric Equipment 2 Name"]

    @electric_equipment_2_name.setter
    def electric_equipment_2_name(self, value=None):
        """  Corresponds to IDD Field `Electric Equipment 2 Name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `Electric Equipment 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `electric_equipment_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electric_equipment_2_name`')
        self._data["Electric Equipment 2 Name"] = value

    @property
    def electric_equipment_3_name(self):
        """Get electric_equipment_3_name

        Returns:
            str: the value of `electric_equipment_3_name` or None if not set
        """
        return self._data["Electric Equipment 3 Name"]

    @electric_equipment_3_name.setter
    def electric_equipment_3_name(self, value=None):
        """  Corresponds to IDD Field `Electric Equipment 3 Name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `Electric Equipment 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `electric_equipment_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electric_equipment_3_name`')
        self._data["Electric Equipment 3 Name"] = value

    @property
    def electric_equipment_4_name(self):
        """Get electric_equipment_4_name

        Returns:
            str: the value of `electric_equipment_4_name` or None if not set
        """
        return self._data["Electric Equipment 4 Name"]

    @electric_equipment_4_name.setter
    def electric_equipment_4_name(self, value=None):
        """  Corresponds to IDD Field `Electric Equipment 4 Name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `Electric Equipment 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `electric_equipment_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electric_equipment_4_name`')
        self._data["Electric Equipment 4 Name"] = value

    @property
    def electric_equipment_5_name(self):
        """Get electric_equipment_5_name

        Returns:
            str: the value of `electric_equipment_5_name` or None if not set
        """
        return self._data["Electric Equipment 5 Name"]

    @electric_equipment_5_name.setter
    def electric_equipment_5_name(self, value=None):
        """  Corresponds to IDD Field `Electric Equipment 5 Name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `Electric Equipment 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `electric_equipment_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electric_equipment_5_name`')
        self._data["Electric Equipment 5 Name"] = value

    @property
    def electric_equipment_6_name(self):
        """Get electric_equipment_6_name

        Returns:
            str: the value of `electric_equipment_6_name` or None if not set
        """
        return self._data["Electric Equipment 6 Name"]

    @electric_equipment_6_name.setter
    def electric_equipment_6_name(self, value=None):
        """  Corresponds to IDD Field `Electric Equipment 6 Name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `Electric Equipment 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `electric_equipment_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electric_equipment_6_name`')
        self._data["Electric Equipment 6 Name"] = value

    @property
    def electric_equipment_7_name(self):
        """Get electric_equipment_7_name

        Returns:
            str: the value of `electric_equipment_7_name` or None if not set
        """
        return self._data["Electric Equipment 7 Name"]

    @electric_equipment_7_name.setter
    def electric_equipment_7_name(self, value=None):
        """  Corresponds to IDD Field `Electric Equipment 7 Name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `Electric Equipment 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `electric_equipment_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electric_equipment_7_name`')
        self._data["Electric Equipment 7 Name"] = value

    @property
    def electric_equipment_8_name(self):
        """Get electric_equipment_8_name

        Returns:
            str: the value of `electric_equipment_8_name` or None if not set
        """
        return self._data["Electric Equipment 8 Name"]

    @electric_equipment_8_name.setter
    def electric_equipment_8_name(self, value=None):
        """  Corresponds to IDD Field `Electric Equipment 8 Name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `Electric Equipment 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `electric_equipment_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electric_equipment_8_name`')
        self._data["Electric Equipment 8 Name"] = value

    @property
    def electric_equipment_9_name(self):
        """Get electric_equipment_9_name

        Returns:
            str: the value of `electric_equipment_9_name` or None if not set
        """
        return self._data["Electric Equipment 9 Name"]

    @electric_equipment_9_name.setter
    def electric_equipment_9_name(self, value=None):
        """  Corresponds to IDD Field `Electric Equipment 9 Name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `Electric Equipment 9 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `electric_equipment_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electric_equipment_9_name`')
        self._data["Electric Equipment 9 Name"] = value

    @property
    def electric_equipment_10_name(self):
        """Get electric_equipment_10_name

        Returns:
            str: the value of `electric_equipment_10_name` or None if not set
        """
        return self._data["Electric Equipment 10 Name"]

    @electric_equipment_10_name.setter
    def electric_equipment_10_name(self, value=None):
        """  Corresponds to IDD Field `Electric Equipment 10 Name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `Electric Equipment 10 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `electric_equipment_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `electric_equipment_10_name`')
        self._data["Electric Equipment 10 Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DemandManagerThermostats(object):
    """ Corresponds to IDD object `DemandManager:Thermostats`
        used for demand limiting ZoneControl:Thermostat objects.
    """
    internal_name = "DemandManager:Thermostats"
    field_count = 19
    required_fields = ["Name", "Reset Control", "Maximum Heating Setpoint Reset", "Maximum Cooling Setpoint Reset", "Selection Control", "Thermostat 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `DemandManager:Thermostats`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Reset Control"] = None
        self._data["Minimum Reset Duration"] = None
        self._data["Maximum Heating Setpoint Reset"] = None
        self._data["Maximum Cooling Setpoint Reset"] = None
        self._data["Reset Step Change"] = None
        self._data["Selection Control"] = None
        self._data["Rotation Duration"] = None
        self._data["Thermostat 1 Name"] = None
        self._data["Thermostat 2 Name"] = None
        self._data["Thermostat 3 Name"] = None
        self._data["Thermostat 4 Name"] = None
        self._data["Thermostat 5 Name"] = None
        self._data["Thermostat 6 Name"] = None
        self._data["Thermostat 7 Name"] = None
        self._data["Thermostat 8 Name"] = None
        self._data["Thermostat 9 Name"] = None
        self._data["Thermostat 10 Name"] = None
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reset_control = None
        else:
            self.reset_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_reset_duration = None
        else:
            self.minimum_reset_duration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_heating_setpoint_reset = None
        else:
            self.maximum_heating_setpoint_reset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_cooling_setpoint_reset = None
        else:
            self.maximum_cooling_setpoint_reset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reset_step_change = None
        else:
            self.reset_step_change = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.selection_control = None
        else:
            self.selection_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rotation_duration = None
        else:
            self.rotation_duration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_1_name = None
        else:
            self.thermostat_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_2_name = None
        else:
            self.thermostat_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_3_name = None
        else:
            self.thermostat_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_4_name = None
        else:
            self.thermostat_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_5_name = None
        else:
            self.thermostat_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_6_name = None
        else:
            self.thermostat_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_7_name = None
        else:
            self.thermostat_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_8_name = None
        else:
            self.thermostat_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_9_name = None
        else:
            self.thermostat_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_10_name = None
        else:
            self.thermostat_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def reset_control(self):
        """Get reset_control

        Returns:
            str: the value of `reset_control` or None if not set
        """
        return self._data["Reset Control"]

    @reset_control.setter
    def reset_control(self, value=None):
        """  Corresponds to IDD Field `Reset Control`

        Args:
            value (str): value for IDD Field `Reset Control`
                Accepted values are:
                      - Off
                      - Fixed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `reset_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reset_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reset_control`')
            vals = {}
            vals["off"] = "Off"
            vals["fixed"] = "Fixed"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `reset_control`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `reset_control`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reset Control"] = value

    @property
    def minimum_reset_duration(self):
        """Get minimum_reset_duration

        Returns:
            int: the value of `minimum_reset_duration` or None if not set
        """
        return self._data["Minimum Reset Duration"]

    @minimum_reset_duration.setter
    def minimum_reset_duration(self, value=None):
        """  Corresponds to IDD Field `Minimum Reset Duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `Minimum Reset Duration`
                Units: minutes
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `minimum_reset_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `minimum_reset_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `minimum_reset_duration`')
        self._data["Minimum Reset Duration"] = value

    @property
    def maximum_heating_setpoint_reset(self):
        """Get maximum_heating_setpoint_reset

        Returns:
            float: the value of `maximum_heating_setpoint_reset` or None if not set
        """
        return self._data["Maximum Heating Setpoint Reset"]

    @maximum_heating_setpoint_reset.setter
    def maximum_heating_setpoint_reset(self, value=None):
        """  Corresponds to IDD Field `Maximum Heating Setpoint Reset`

        Args:
            value (float): value for IDD Field `Maximum Heating Setpoint Reset`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `maximum_heating_setpoint_reset`'.format(value))
        self._data["Maximum Heating Setpoint Reset"] = value

    @property
    def maximum_cooling_setpoint_reset(self):
        """Get maximum_cooling_setpoint_reset

        Returns:
            float: the value of `maximum_cooling_setpoint_reset` or None if not set
        """
        return self._data["Maximum Cooling Setpoint Reset"]

    @maximum_cooling_setpoint_reset.setter
    def maximum_cooling_setpoint_reset(self, value=None):
        """  Corresponds to IDD Field `Maximum Cooling Setpoint Reset`

        Args:
            value (float): value for IDD Field `Maximum Cooling Setpoint Reset`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `maximum_cooling_setpoint_reset`'.format(value))
        self._data["Maximum Cooling Setpoint Reset"] = value

    @property
    def reset_step_change(self):
        """Get reset_step_change

        Returns:
            float: the value of `reset_step_change` or None if not set
        """
        return self._data["Reset Step Change"]

    @reset_step_change.setter
    def reset_step_change(self, value=None):
        """  Corresponds to IDD Field `Reset Step Change`
        Not yet implemented

        Args:
            value (float): value for IDD Field `Reset Step Change`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 'for field `reset_step_change`'.format(value))
        self._data["Reset Step Change"] = value

    @property
    def selection_control(self):
        """Get selection_control

        Returns:
            str: the value of `selection_control` or None if not set
        """
        return self._data["Selection Control"]

    @selection_control.setter
    def selection_control(self, value=None):
        """  Corresponds to IDD Field `Selection Control`

        Args:
            value (str): value for IDD Field `Selection Control`
                Accepted values are:
                      - All
                      - RotateMany
                      - RotateOne
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `selection_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `selection_control`')
            vals = {}
            vals["all"] = "All"
            vals["rotatemany"] = "RotateMany"
            vals["rotateone"] = "RotateOne"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `selection_control`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `selection_control`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Selection Control"] = value

    @property
    def rotation_duration(self):
        """Get rotation_duration

        Returns:
            int: the value of `rotation_duration` or None if not set
        """
        return self._data["Rotation Duration"]

    @rotation_duration.setter
    def rotation_duration(self, value=None):
        """  Corresponds to IDD Field `Rotation Duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `Rotation Duration`
                Units: minutes
                value >= 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `rotation_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `rotation_duration`')
        self._data["Rotation Duration"] = value

    @property
    def thermostat_1_name(self):
        """Get thermostat_1_name

        Returns:
            str: the value of `thermostat_1_name` or None if not set
        """
        return self._data["Thermostat 1 Name"]

    @thermostat_1_name.setter
    def thermostat_1_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat 1 Name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `Thermostat 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `thermostat_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_1_name`')
        self._data["Thermostat 1 Name"] = value

    @property
    def thermostat_2_name(self):
        """Get thermostat_2_name

        Returns:
            str: the value of `thermostat_2_name` or None if not set
        """
        return self._data["Thermostat 2 Name"]

    @thermostat_2_name.setter
    def thermostat_2_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat 2 Name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `Thermostat 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `thermostat_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_2_name`')
        self._data["Thermostat 2 Name"] = value

    @property
    def thermostat_3_name(self):
        """Get thermostat_3_name

        Returns:
            str: the value of `thermostat_3_name` or None if not set
        """
        return self._data["Thermostat 3 Name"]

    @thermostat_3_name.setter
    def thermostat_3_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat 3 Name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `Thermostat 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `thermostat_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_3_name`')
        self._data["Thermostat 3 Name"] = value

    @property
    def thermostat_4_name(self):
        """Get thermostat_4_name

        Returns:
            str: the value of `thermostat_4_name` or None if not set
        """
        return self._data["Thermostat 4 Name"]

    @thermostat_4_name.setter
    def thermostat_4_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat 4 Name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `Thermostat 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `thermostat_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_4_name`')
        self._data["Thermostat 4 Name"] = value

    @property
    def thermostat_5_name(self):
        """Get thermostat_5_name

        Returns:
            str: the value of `thermostat_5_name` or None if not set
        """
        return self._data["Thermostat 5 Name"]

    @thermostat_5_name.setter
    def thermostat_5_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat 5 Name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `Thermostat 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `thermostat_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_5_name`')
        self._data["Thermostat 5 Name"] = value

    @property
    def thermostat_6_name(self):
        """Get thermostat_6_name

        Returns:
            str: the value of `thermostat_6_name` or None if not set
        """
        return self._data["Thermostat 6 Name"]

    @thermostat_6_name.setter
    def thermostat_6_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat 6 Name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `Thermostat 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `thermostat_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_6_name`')
        self._data["Thermostat 6 Name"] = value

    @property
    def thermostat_7_name(self):
        """Get thermostat_7_name

        Returns:
            str: the value of `thermostat_7_name` or None if not set
        """
        return self._data["Thermostat 7 Name"]

    @thermostat_7_name.setter
    def thermostat_7_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat 7 Name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `Thermostat 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `thermostat_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_7_name`')
        self._data["Thermostat 7 Name"] = value

    @property
    def thermostat_8_name(self):
        """Get thermostat_8_name

        Returns:
            str: the value of `thermostat_8_name` or None if not set
        """
        return self._data["Thermostat 8 Name"]

    @thermostat_8_name.setter
    def thermostat_8_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat 8 Name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `Thermostat 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `thermostat_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_8_name`')
        self._data["Thermostat 8 Name"] = value

    @property
    def thermostat_9_name(self):
        """Get thermostat_9_name

        Returns:
            str: the value of `thermostat_9_name` or None if not set
        """
        return self._data["Thermostat 9 Name"]

    @thermostat_9_name.setter
    def thermostat_9_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat 9 Name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `Thermostat 9 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `thermostat_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_9_name`')
        self._data["Thermostat 9 Name"] = value

    @property
    def thermostat_10_name(self):
        """Get thermostat_10_name

        Returns:
            str: the value of `thermostat_10_name` or None if not set
        """
        return self._data["Thermostat 10 Name"]

    @thermostat_10_name.setter
    def thermostat_10_name(self, value=None):
        """  Corresponds to IDD Field `Thermostat 10 Name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `Thermostat 10 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `thermostat_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_10_name`')
        self._data["Thermostat 10 Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])