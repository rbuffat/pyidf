from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class DemandManagerAssignmentList(object):
    """ Corresponds to IDD object `DemandManagerAssignmentList`
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    internal_name = "DemandManagerAssignmentList"
    field_count = 8
    required_fields = ["Name", "Meter Name", "Demand Limit Safety Fraction", "Demand Window Length", "Demand Manager Priority"]
    extensible_fields = 2
    format = None
    min_fields = 0
    extensible_keys = ["DemandManager 1 Object Type", "DemandManager 1 Name"]

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
        self._data["extensibles"] = []
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
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `DemandManagerAssignmentList.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerAssignmentList.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerAssignmentList.name`')
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
                                 ' for field `DemandManagerAssignmentList.meter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerAssignmentList.meter_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerAssignmentList.meter_name`')
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
                                 ' for field `DemandManagerAssignmentList.demand_limit_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerAssignmentList.demand_limit_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerAssignmentList.demand_limit_schedule_name`')
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
                                 ' for field `DemandManagerAssignmentList.demand_limit_safety_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DemandManagerAssignmentList.demand_limit_safety_fraction`')
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
                                 ' for field `DemandManagerAssignmentList.billing_period_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerAssignmentList.billing_period_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerAssignmentList.billing_period_schedule_name`')
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
                                 ' for field `DemandManagerAssignmentList.peak_period_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerAssignmentList.peak_period_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerAssignmentList.peak_period_schedule_name`')
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DemandManagerAssignmentList.demand_window_length`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DemandManagerAssignmentList.demand_window_length`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `DemandManagerAssignmentList.demand_window_length`')
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
                                 ' for field `DemandManagerAssignmentList.demand_manager_priority`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerAssignmentList.demand_manager_priority`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerAssignmentList.demand_manager_priority`')
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
                                     'field `DemandManagerAssignmentList.demand_manager_priority`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `DemandManagerAssignmentList.demand_manager_priority`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Demand Manager Priority"] = value

    def add_extensible(self,
                       demandmanager_1_object_type=None,
                       demandmanager_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            demandmanager_1_object_type (str): value for IDD Field `DemandManager 1 Object Type`
                Accepted values are:
                      - DemandManager:ExteriorLights
                      - DemandManager:Lights
                      - DemandManager:ElectricEquipment
                      - DemandManager:Thermostats
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            demandmanager_1_name (str): value for IDD Field `DemandManager 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_demandmanager_1_object_type(demandmanager_1_object_type))
        vals.append(self._check_demandmanager_1_name(demandmanager_1_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_demandmanager_1_object_type(self, value):
        """ Validates falue of field `DemandManager 1 Object Type`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DemandManagerAssignmentList.demandmanager_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerAssignmentList.demandmanager_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerAssignmentList.demandmanager_1_object_type`')
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
                                     'field `DemandManagerAssignmentList.demandmanager_1_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `DemandManagerAssignmentList.demandmanager_1_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        return value

    def _check_demandmanager_1_name(self, value):
        """ Validates falue of field `DemandManager 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DemandManagerAssignmentList.demandmanager_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerAssignmentList.demandmanager_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerAssignmentList.demandmanager_1_name`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DemandManagerAssignmentList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DemandManagerAssignmentList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DemandManagerAssignmentList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DemandManagerAssignmentList: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
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
    field_count = 8
    required_fields = ["Name", "Limit Control", "Selection Control"]
    extensible_fields = 1
    format = None
    min_fields = 0
    extensible_keys = ["Exterior Lights 1 Name"]

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
        self._data["extensibles"] = []
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
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `DemandManagerExteriorLights.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerExteriorLights.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerExteriorLights.name`')
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
                                 ' for field `DemandManagerExteriorLights.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerExteriorLights.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerExteriorLights.availability_schedule_name`')
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
                                 ' for field `DemandManagerExteriorLights.limit_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerExteriorLights.limit_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerExteriorLights.limit_control`')
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
                                     'field `DemandManagerExteriorLights.limit_control`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `DemandManagerExteriorLights.limit_control`'.format(value, vals[value_lower]))
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DemandManagerExteriorLights.minimum_limit_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DemandManagerExteriorLights.minimum_limit_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `DemandManagerExteriorLights.minimum_limit_duration`')
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
                                 ' for field `DemandManagerExteriorLights.maximum_limit_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DemandManagerExteriorLights.maximum_limit_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `DemandManagerExteriorLights.maximum_limit_fraction`')
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
                                 ' for field `DemandManagerExteriorLights.limit_step_change`'.format(value))
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
                                 ' for field `DemandManagerExteriorLights.selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerExteriorLights.selection_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerExteriorLights.selection_control`')
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
                                     'field `DemandManagerExteriorLights.selection_control`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `DemandManagerExteriorLights.selection_control`'.format(value, vals[value_lower]))
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DemandManagerExteriorLights.rotation_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DemandManagerExteriorLights.rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `DemandManagerExteriorLights.rotation_duration`')
        self._data["Rotation Duration"] = value

    def add_extensible(self,
                       exterior_lights_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            exterior_lights_1_name (str): value for IDD Field `Exterior Lights 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_exterior_lights_1_name(exterior_lights_1_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_exterior_lights_1_name(self, value):
        """ Validates falue of field `Exterior Lights 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DemandManagerExteriorLights.exterior_lights_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerExteriorLights.exterior_lights_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerExteriorLights.exterior_lights_1_name`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DemandManagerExteriorLights:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DemandManagerExteriorLights:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DemandManagerExteriorLights: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DemandManagerExteriorLights: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
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
    field_count = 8
    required_fields = ["Name", "Limit Control", "Selection Control"]
    extensible_fields = 1
    format = None
    min_fields = 0
    extensible_keys = ["Lights 1 Name"]

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
        self._data["extensibles"] = []
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
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `DemandManagerLights.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerLights.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerLights.name`')
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
                                 ' for field `DemandManagerLights.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerLights.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerLights.availability_schedule_name`')
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
                                 ' for field `DemandManagerLights.limit_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerLights.limit_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerLights.limit_control`')
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
                                     'field `DemandManagerLights.limit_control`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `DemandManagerLights.limit_control`'.format(value, vals[value_lower]))
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DemandManagerLights.minimum_limit_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DemandManagerLights.minimum_limit_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `DemandManagerLights.minimum_limit_duration`')
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
                                 ' for field `DemandManagerLights.maximum_limit_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DemandManagerLights.maximum_limit_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `DemandManagerLights.maximum_limit_fraction`')
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
                                 ' for field `DemandManagerLights.limit_step_change`'.format(value))
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
                                 ' for field `DemandManagerLights.selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerLights.selection_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerLights.selection_control`')
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
                                     'field `DemandManagerLights.selection_control`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `DemandManagerLights.selection_control`'.format(value, vals[value_lower]))
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DemandManagerLights.rotation_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DemandManagerLights.rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `DemandManagerLights.rotation_duration`')
        self._data["Rotation Duration"] = value

    def add_extensible(self,
                       lights_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            lights_1_name (str): value for IDD Field `Lights 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_lights_1_name(lights_1_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_lights_1_name(self, value):
        """ Validates falue of field `Lights 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DemandManagerLights.lights_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerLights.lights_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerLights.lights_1_name`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DemandManagerLights:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DemandManagerLights:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DemandManagerLights: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DemandManagerLights: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
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
    field_count = 8
    required_fields = ["Name", "Limit Control", "Selection Control"]
    extensible_fields = 1
    format = None
    min_fields = 0
    extensible_keys = ["Electric Equipment 1 Name"]

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
        self._data["extensibles"] = []
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
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `DemandManagerElectricEquipment.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerElectricEquipment.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerElectricEquipment.name`')
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
                                 ' for field `DemandManagerElectricEquipment.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerElectricEquipment.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerElectricEquipment.availability_schedule_name`')
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
                                 ' for field `DemandManagerElectricEquipment.limit_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerElectricEquipment.limit_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerElectricEquipment.limit_control`')
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
                                     'field `DemandManagerElectricEquipment.limit_control`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `DemandManagerElectricEquipment.limit_control`'.format(value, vals[value_lower]))
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DemandManagerElectricEquipment.minimum_limit_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DemandManagerElectricEquipment.minimum_limit_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `DemandManagerElectricEquipment.minimum_limit_duration`')
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
                                 ' for field `DemandManagerElectricEquipment.maximum_limit_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DemandManagerElectricEquipment.maximum_limit_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `DemandManagerElectricEquipment.maximum_limit_fraction`')
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
                                 ' for field `DemandManagerElectricEquipment.limit_step_change`'.format(value))
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
                                 ' for field `DemandManagerElectricEquipment.selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerElectricEquipment.selection_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerElectricEquipment.selection_control`')
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
                                     'field `DemandManagerElectricEquipment.selection_control`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `DemandManagerElectricEquipment.selection_control`'.format(value, vals[value_lower]))
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DemandManagerElectricEquipment.rotation_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DemandManagerElectricEquipment.rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `DemandManagerElectricEquipment.rotation_duration`')
        self._data["Rotation Duration"] = value

    def add_extensible(self,
                       electric_equipment_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            electric_equipment_1_name (str): value for IDD Field `Electric Equipment 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_electric_equipment_1_name(electric_equipment_1_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_electric_equipment_1_name(self, value):
        """ Validates falue of field `Electric Equipment 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DemandManagerElectricEquipment.electric_equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerElectricEquipment.electric_equipment_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerElectricEquipment.electric_equipment_1_name`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DemandManagerElectricEquipment:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DemandManagerElectricEquipment:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DemandManagerElectricEquipment: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DemandManagerElectricEquipment: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
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
    field_count = 9
    required_fields = ["Name", "Reset Control", "Maximum Heating Setpoint Reset", "Maximum Cooling Setpoint Reset", "Selection Control"]
    extensible_fields = 1
    format = None
    min_fields = 0
    extensible_keys = ["Thermostat 1 Name"]

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
        self._data["extensibles"] = []
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
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
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
                                 ' for field `DemandManagerThermostats.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerThermostats.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerThermostats.name`')
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
                                 ' for field `DemandManagerThermostats.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerThermostats.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerThermostats.availability_schedule_name`')
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
                                 ' for field `DemandManagerThermostats.reset_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerThermostats.reset_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerThermostats.reset_control`')
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
                                     'field `DemandManagerThermostats.reset_control`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `DemandManagerThermostats.reset_control`'.format(value, vals[value_lower]))
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DemandManagerThermostats.minimum_reset_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DemandManagerThermostats.minimum_reset_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `DemandManagerThermostats.minimum_reset_duration`')
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
                                 ' for field `DemandManagerThermostats.maximum_heating_setpoint_reset`'.format(value))
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
                                 ' for field `DemandManagerThermostats.maximum_cooling_setpoint_reset`'.format(value))
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
                                 ' for field `DemandManagerThermostats.reset_step_change`'.format(value))
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
                                 ' for field `DemandManagerThermostats.selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerThermostats.selection_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerThermostats.selection_control`')
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
                                     'field `DemandManagerThermostats.selection_control`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `DemandManagerThermostats.selection_control`'.format(value, vals[value_lower]))
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DemandManagerThermostats.rotation_duration`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DemandManagerThermostats.rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `DemandManagerThermostats.rotation_duration`')
        self._data["Rotation Duration"] = value

    def add_extensible(self,
                       thermostat_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            thermostat_1_name (str): value for IDD Field `Thermostat 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_thermostat_1_name(thermostat_1_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_thermostat_1_name(self, value):
        """ Validates falue of field `Thermostat 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DemandManagerThermostats.thermostat_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DemandManagerThermostats.thermostat_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DemandManagerThermostats.thermostat_1_name`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DemandManagerThermostats:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DemandManagerThermostats:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DemandManagerThermostats: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DemandManagerThermostats: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])