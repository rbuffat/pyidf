from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class AirTerminalSingleDuctUncontrolled(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:Uncontrolled`
        Central air system terminal unit, single duct, constant volume, no controls other than
        on/off schedule.
    """
    internal_name = "AirTerminal:SingleDuct:Uncontrolled"
    field_count = 4
    required_fields = ["Name", "Zone Supply Air Node Name", "Maximum Air Flow Rate"]
    extensible_fields = 0
    format = None
    min_fields = 4
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:Uncontrolled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Supply Air Node Name"] = None
        self._data["Maximum Air Flow Rate"] = None
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
            self.zone_supply_air_node_name = None
        else:
            self.zone_supply_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
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
                                 ' for field `AirTerminalSingleDuctUncontrolled.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctUncontrolled.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctUncontrolled.name`')
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
                                 ' for field `AirTerminalSingleDuctUncontrolled.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctUncontrolled.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctUncontrolled.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def zone_supply_air_node_name(self):
        """Get zone_supply_air_node_name

        Returns:
            str: the value of `zone_supply_air_node_name` or None if not set
        """
        return self._data["Zone Supply Air Node Name"]

    @zone_supply_air_node_name.setter
    def zone_supply_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Supply Air Node Name`

        Args:
            value (str): value for IDD Field `Zone Supply Air Node Name`
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
                                 ' for field `AirTerminalSingleDuctUncontrolled.zone_supply_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctUncontrolled.zone_supply_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctUncontrolled.zone_supply_air_node_name`')
        self._data["Zone Supply Air Node Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctUncontrolled.maximum_air_flow_rate`'.format(value))
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctUncontrolled.maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctUncontrolled.maximum_air_flow_rate`')
        self._data["Maximum Air Flow Rate"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctUncontrolled:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctUncontrolled:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctUncontrolled: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctUncontrolled: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctConstantVolumeReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:ConstantVolume:Reheat`
        Central air system terminal unit, single duct, constant volume, with reheat coil (hot
        water, electric, gas, or steam).
    """
    internal_name = "AirTerminal:SingleDuct:ConstantVolume:Reheat"
    field_count = 12
    required_fields = ["Name", "Air Outlet Node Name", "Air Inlet Node Name", "Maximum Air Flow Rate", "Reheat Coil Object Type", "Reheat Coil Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:ConstantVolume:Reheat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Maximum Air Flow Rate"] = None
        self._data["Hot Water or Steam Inlet Node Name"] = None
        self._data["Reheat Coil Object Type"] = None
        self._data["Reheat Coil Name"] = None
        self._data["Maximum Hot Water or Steam Flow Rate"] = None
        self._data["Minimum Hot Water or Steam Flow Rate"] = None
        self._data["Convergence Tolerance"] = None
        self._data["Maximum Reheat Air Temperature"] = None
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
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_water_or_steam_inlet_node_name = None
        else:
            self.hot_water_or_steam_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_object_type = None
        else:
            self.reheat_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_name = None
        else:
            self.reheat_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hot_water_or_steam_flow_rate = None
        else:
            self.maximum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_hot_water_or_steam_flow_rate = None
        else:
            self.minimum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_tolerance = None
        else:
            self.convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_reheat_air_temperature = None
        else:
            self.maximum_reheat_air_temperature = vals[i]
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.name`')
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.maximum_air_flow_rate`'.format(value))
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.maximum_air_flow_rate`')
        self._data["Maximum Air Flow Rate"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """Get hot_water_or_steam_inlet_node_name

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set
        """
        return self._data["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Hot Water or Steam Inlet Node Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.hot_water_or_steam_inlet_node_name`')
        self._data["Hot Water or Steam Inlet Node Name"] = value

    @property
    def reheat_coil_object_type(self):
        """Get reheat_coil_object_type

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set
        """
        return self._data["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Object Type`

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.reheat_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.reheat_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `AirTerminalSingleDuctConstantVolumeReheat.reheat_coil_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctConstantVolumeReheat.reheat_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """Get reheat_coil_name

        Returns:
            str: the value of `reheat_coil_name` or None if not set
        """
        return self._data["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.reheat_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.reheat_coil_name`')
        self._data["Reheat Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """Get maximum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `maximum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Hot Water or Steam Flow Rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.maximum_hot_water_or_steam_flow_rate`'.format(value))
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.maximum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.maximum_hot_water_or_steam_flow_rate`')
        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Hot Water or Steam Flow Rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.minimum_hot_water_or_steam_flow_rate`')
        self._data["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Convergence Tolerance`
                Default value: 0.001
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.convergence_tolerance`')
        self._data["Convergence Tolerance"] = value

    @property
    def maximum_reheat_air_temperature(self):
        """Get maximum_reheat_air_temperature

        Returns:
            float: the value of `maximum_reheat_air_temperature` or None if not set
        """
        return self._data["Maximum Reheat Air Temperature"]

    @maximum_reheat_air_temperature.setter
    def maximum_reheat_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Reheat Air Temperature`
        Specifies the maximum allowable supply air temperature leaving the reheat coil.
        If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.

        Args:
            value (float): value for IDD Field `Maximum Reheat Air Temperature`
                Units: C
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeReheat.maximum_reheat_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeReheat.maximum_reheat_air_temperature`')
        self._data["Maximum Reheat Air Temperature"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctConstantVolumeReheat:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctConstantVolumeReheat:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctConstantVolumeReheat: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctConstantVolumeReheat: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctVavNoReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:NoReheat`
        Central air system terminal unit, single duct, variable volume, with no reheat coil.
    """
    internal_name = "AirTerminal:SingleDuct:VAV:NoReheat"
    field_count = 10
    required_fields = ["Name", "Air Outlet Node Name", "Air Inlet Node Name", "Maximum Air Flow Rate", "Zone Minimum Air Flow Input Method"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:VAV:NoReheat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Maximum Air Flow Rate"] = None
        self._data["Zone Minimum Air Flow Input Method"] = None
        self._data["Constant Minimum Air Flow Fraction"] = None
        self._data["Fixed Minimum Air Flow Rate"] = None
        self._data["Minimum Air Flow Fraction Schedule Name"] = None
        self._data["Design Specification Outdoor Air Object Name"] = None
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
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_minimum_air_flow_input_method = None
        else:
            self.zone_minimum_air_flow_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.constant_minimum_air_flow_fraction = None
        else:
            self.constant_minimum_air_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fixed_minimum_air_flow_rate = None
        else:
            self.fixed_minimum_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_air_flow_fraction_schedule_name = None
        else:
            self.minimum_air_flow_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name = None
        else:
            self.design_specification_outdoor_air_object_name = vals[i]
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
                                 ' for field `AirTerminalSingleDuctVavNoReheat.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavNoReheat.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavNoReheat.name`')
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
                                 ' for field `AirTerminalSingleDuctVavNoReheat.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavNoReheat.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavNoReheat.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavNoReheat.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavNoReheat.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavNoReheat.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavNoReheat.air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavNoReheat.air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavNoReheat.air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctVavNoReheat.maximum_air_flow_rate`'.format(value))
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctVavNoReheat.maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavNoReheat.maximum_air_flow_rate`')
        self._data["Maximum Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_input_method(self):
        """Get zone_minimum_air_flow_input_method

        Returns:
            str: the value of `zone_minimum_air_flow_input_method` or None if not set
        """
        return self._data["Zone Minimum Air Flow Input Method"]

    @zone_minimum_air_flow_input_method.setter
    def zone_minimum_air_flow_input_method(self, value=None):
        """  Corresponds to IDD Field `Zone Minimum Air Flow Input Method`
        Constant = Constant Minimum Air Flow Fraction (a fraction of Maximum Air Flow Rate)
        FixedFlowRate = Fixed Minimum Air Flow Rate (a fixed minimum air volume flow rate)
        Scheduled = Scheduled Minimum Air Flow Fraction (a fraction of Maximum Air Flow

        Args:
            value (str): value for IDD Field `Zone Minimum Air Flow Input Method`
                Accepted values are:
                      - Constant
                      - FixedFlowRate
                      - Scheduled
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
                                 ' for field `AirTerminalSingleDuctVavNoReheat.zone_minimum_air_flow_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavNoReheat.zone_minimum_air_flow_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavNoReheat.zone_minimum_air_flow_input_method`')
            vals = {}
            vals["constant"] = "Constant"
            vals["fixedflowrate"] = "FixedFlowRate"
            vals["scheduled"] = "Scheduled"
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
                                     'field `AirTerminalSingleDuctVavNoReheat.zone_minimum_air_flow_input_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctVavNoReheat.zone_minimum_air_flow_input_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Minimum Air Flow Input Method"] = value

    @property
    def constant_minimum_air_flow_fraction(self):
        """Get constant_minimum_air_flow_fraction

        Returns:
            float: the value of `constant_minimum_air_flow_fraction` or None if not set
        """
        return self._data["Constant Minimum Air Flow Fraction"]

    @constant_minimum_air_flow_fraction.setter
    def constant_minimum_air_flow_fraction(self, value=None):
        """  Corresponds to IDD Field `Constant Minimum Air Flow Fraction`
        This field is used if the field Zone Minimum Air Flow Input Method is Constant
        If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        If both this field and the following field are entered, the larger result is used.

        Args:
            value (float): value for IDD Field `Constant Minimum Air Flow Fraction`
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
                                 ' for field `AirTerminalSingleDuctVavNoReheat.constant_minimum_air_flow_fraction`'.format(value))
        self._data["Constant Minimum Air Flow Fraction"] = value

    @property
    def fixed_minimum_air_flow_rate(self):
        """Get fixed_minimum_air_flow_rate

        Returns:
            float: the value of `fixed_minimum_air_flow_rate` or None if not set
        """
        return self._data["Fixed Minimum Air Flow Rate"]

    @fixed_minimum_air_flow_rate.setter
    def fixed_minimum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Fixed Minimum Air Flow Rate`
        This field is used if the field Zone Minimum Air Flow Input Method is FixedFlowRate.
        If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        If both this field and the previous field are entered, the larger result is used.

        Args:
            value (float): value for IDD Field `Fixed Minimum Air Flow Rate`
                Units: m3/s
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
                                 ' for field `AirTerminalSingleDuctVavNoReheat.fixed_minimum_air_flow_rate`'.format(value))
        self._data["Fixed Minimum Air Flow Rate"] = value

    @property
    def minimum_air_flow_fraction_schedule_name(self):
        """Get minimum_air_flow_fraction_schedule_name

        Returns:
            str: the value of `minimum_air_flow_fraction_schedule_name` or None if not set
        """
        return self._data["Minimum Air Flow Fraction Schedule Name"]

    @minimum_air_flow_fraction_schedule_name.setter
    def minimum_air_flow_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Air Flow Fraction Schedule Name`
        This field is used if the field Zone Minimum Air Flow Input Method is Scheduled
        Schedule values are fractions, 0.0 to 1.0.
        If the field Constant Minimum Air Flow Fraction is blank, then the average of the
        minimum and maximum schedule values is used for sizing normal-action reheat coils.

        Args:
            value (str): value for IDD Field `Minimum Air Flow Fraction Schedule Name`
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
                                 ' for field `AirTerminalSingleDuctVavNoReheat.minimum_air_flow_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavNoReheat.minimum_air_flow_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavNoReheat.minimum_air_flow_fraction_schedule_name`')
        self._data["Minimum Air Flow Fraction Schedule Name"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """Get design_specification_outdoor_air_object_name

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification Outdoor Air Object Name`
        When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        unit will increase flow as needed to meet this outdoor air requirement.
        If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        be computed based on the current number of occupants in the zone.
        At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.
        If this field is blank, then the terminal unit will not be controlled for outdoor air flow.

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`
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
                                 ' for field `AirTerminalSingleDuctVavNoReheat.design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavNoReheat.design_specification_outdoor_air_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavNoReheat.design_specification_outdoor_air_object_name`')
        self._data["Design Specification Outdoor Air Object Name"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctVavNoReheat:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctVavNoReheat:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctVavNoReheat: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctVavNoReheat: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctVavReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:Reheat`
        Central air system terminal unit, single duct, variable volume, with reheat coil (hot
        water, electric, gas, or steam).
    """
    internal_name = "AirTerminal:SingleDuct:VAV:Reheat"
    field_count = 20
    required_fields = ["Name", "Damper Air Outlet Node Name", "Air Inlet Node Name", "Maximum Air Flow Rate", "Zone Minimum Air Flow Input Method", "Reheat Coil Object Type", "Reheat Coil Name", "Air Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:VAV:Reheat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Damper Air Outlet Node Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Maximum Air Flow Rate"] = None
        self._data["Zone Minimum Air Flow Input Method"] = None
        self._data["Constant Minimum Air Flow Fraction"] = None
        self._data["Fixed Minimum Air Flow Rate"] = None
        self._data["Minimum Air Flow Fraction Schedule Name"] = None
        self._data["Reheat Coil Object Type"] = None
        self._data["Reheat Coil Name"] = None
        self._data["Maximum Hot Water or Steam Flow Rate"] = None
        self._data["Minimum Hot Water or Steam Flow Rate"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Convergence Tolerance"] = None
        self._data["Damper Heating Action"] = None
        self._data["Maximum Flow per Zone Floor Area During Reheat"] = None
        self._data["Maximum Flow Fraction During Reheat"] = None
        self._data["Maximum Reheat Air Temperature"] = None
        self._data["Design Specification Outdoor Air Object Name"] = None
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
            self.damper_air_outlet_node_name = None
        else:
            self.damper_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_minimum_air_flow_input_method = None
        else:
            self.zone_minimum_air_flow_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.constant_minimum_air_flow_fraction = None
        else:
            self.constant_minimum_air_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fixed_minimum_air_flow_rate = None
        else:
            self.fixed_minimum_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_air_flow_fraction_schedule_name = None
        else:
            self.minimum_air_flow_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_object_type = None
        else:
            self.reheat_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_name = None
        else:
            self.reheat_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hot_water_or_steam_flow_rate = None
        else:
            self.maximum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_hot_water_or_steam_flow_rate = None
        else:
            self.minimum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_tolerance = None
        else:
            self.convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.damper_heating_action = None
        else:
            self.damper_heating_action = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_flow_per_zone_floor_area_during_reheat = None
        else:
            self.maximum_flow_per_zone_floor_area_during_reheat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_flow_fraction_during_reheat = None
        else:
            self.maximum_flow_fraction_during_reheat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_reheat_air_temperature = None
        else:
            self.maximum_reheat_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name = None
        else:
            self.design_specification_outdoor_air_object_name = vals[i]
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
                                 ' for field `AirTerminalSingleDuctVavReheat.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.name`')
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
                                 ' for field `AirTerminalSingleDuctVavReheat.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def damper_air_outlet_node_name(self):
        """Get damper_air_outlet_node_name

        Returns:
            str: the value of `damper_air_outlet_node_name` or None if not set
        """
        return self._data["Damper Air Outlet Node Name"]

    @damper_air_outlet_node_name.setter
    def damper_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Damper Air Outlet Node Name`
        the outlet node of the damper and the inlet node of the reheat coil
        this is an internal node to the terminal unit and connects the damper and reheat coil

        Args:
            value (str): value for IDD Field `Damper Air Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheat.damper_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.damper_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.damper_air_outlet_node_name`')
        self._data["Damper Air Outlet Node Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`
        the inlet node to the terminal unit and the damper

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheat.air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctVavReheat.maximum_air_flow_rate`'.format(value))
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctVavReheat.maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavReheat.maximum_air_flow_rate`')
        self._data["Maximum Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_input_method(self):
        """Get zone_minimum_air_flow_input_method

        Returns:
            str: the value of `zone_minimum_air_flow_input_method` or None if not set
        """
        return self._data["Zone Minimum Air Flow Input Method"]

    @zone_minimum_air_flow_input_method.setter
    def zone_minimum_air_flow_input_method(self, value=None):
        """  Corresponds to IDD Field `Zone Minimum Air Flow Input Method`
        Constant = Constant Minimum Air Flow Fraction (a fraction of Maximum Air Flow Rate)
        FixedFlowRate = Fixed Minimum Air Flow Rate (a fixed minimum air volume flow rate)
        Scheduled = Scheduled Minimum Air Flow Fraction (a fraction of Maximum Air Flow

        Args:
            value (str): value for IDD Field `Zone Minimum Air Flow Input Method`
                Accepted values are:
                      - Constant
                      - FixedFlowRate
                      - Scheduled
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
                                 ' for field `AirTerminalSingleDuctVavReheat.zone_minimum_air_flow_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.zone_minimum_air_flow_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.zone_minimum_air_flow_input_method`')
            vals = {}
            vals["constant"] = "Constant"
            vals["fixedflowrate"] = "FixedFlowRate"
            vals["scheduled"] = "Scheduled"
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
                                     'field `AirTerminalSingleDuctVavReheat.zone_minimum_air_flow_input_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctVavReheat.zone_minimum_air_flow_input_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Minimum Air Flow Input Method"] = value

    @property
    def constant_minimum_air_flow_fraction(self):
        """Get constant_minimum_air_flow_fraction

        Returns:
            float: the value of `constant_minimum_air_flow_fraction` or None if not set
        """
        return self._data["Constant Minimum Air Flow Fraction"]

    @constant_minimum_air_flow_fraction.setter
    def constant_minimum_air_flow_fraction(self, value=None):
        """  Corresponds to IDD Field `Constant Minimum Air Flow Fraction`
        This field is used if the field Zone Minimum Air Flow Input Method is Constant
        If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        If both this field and the following field are entered, the larger result is used.

        Args:
            value (float): value for IDD Field `Constant Minimum Air Flow Fraction`
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
                                 ' for field `AirTerminalSingleDuctVavReheat.constant_minimum_air_flow_fraction`'.format(value))
        self._data["Constant Minimum Air Flow Fraction"] = value

    @property
    def fixed_minimum_air_flow_rate(self):
        """Get fixed_minimum_air_flow_rate

        Returns:
            float: the value of `fixed_minimum_air_flow_rate` or None if not set
        """
        return self._data["Fixed Minimum Air Flow Rate"]

    @fixed_minimum_air_flow_rate.setter
    def fixed_minimum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Fixed Minimum Air Flow Rate`
        This field is used if the field Zone Minimum Air Flow Input Method is FixedFlowRate.
        If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        If both this field and the previous field are entered, the larger result is used.

        Args:
            value (float): value for IDD Field `Fixed Minimum Air Flow Rate`
                Units: m3/s
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
                                 ' for field `AirTerminalSingleDuctVavReheat.fixed_minimum_air_flow_rate`'.format(value))
        self._data["Fixed Minimum Air Flow Rate"] = value

    @property
    def minimum_air_flow_fraction_schedule_name(self):
        """Get minimum_air_flow_fraction_schedule_name

        Returns:
            str: the value of `minimum_air_flow_fraction_schedule_name` or None if not set
        """
        return self._data["Minimum Air Flow Fraction Schedule Name"]

    @minimum_air_flow_fraction_schedule_name.setter
    def minimum_air_flow_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Air Flow Fraction Schedule Name`
        This field is used if the field Zone Minimum Air Flow Input Method is Scheduled
        Schedule values are fractions, 0.0 to 1.0.
        If the field Constant Minimum Air Flow Fraction is blank, then the average of the
        minimum and maximum schedule values is used for sizing normal-action reheat coils.

        Args:
            value (str): value for IDD Field `Minimum Air Flow Fraction Schedule Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheat.minimum_air_flow_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.minimum_air_flow_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.minimum_air_flow_fraction_schedule_name`')
        self._data["Minimum Air Flow Fraction Schedule Name"] = value

    @property
    def reheat_coil_object_type(self):
        """Get reheat_coil_object_type

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set
        """
        return self._data["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Object Type`

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
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
                                 ' for field `AirTerminalSingleDuctVavReheat.reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.reheat_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.reheat_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `AirTerminalSingleDuctVavReheat.reheat_coil_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctVavReheat.reheat_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """Get reheat_coil_name

        Returns:
            str: the value of `reheat_coil_name` or None if not set
        """
        return self._data["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheat.reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.reheat_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.reheat_coil_name`')
        self._data["Reheat Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """Get maximum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `maximum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Hot Water or Steam Flow Rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctVavReheat.maximum_hot_water_or_steam_flow_rate`'.format(value))
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctVavReheat.maximum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavReheat.maximum_hot_water_or_steam_flow_rate`')
        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Hot Water or Steam Flow Rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
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
                                 ' for field `AirTerminalSingleDuctVavReheat.minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavReheat.minimum_hot_water_or_steam_flow_rate`')
        self._data["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`
        The outlet node of the terminal unit and the reheat coil.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheat.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Convergence Tolerance`
                Default value: 0.001
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctVavReheat.convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctVavReheat.convergence_tolerance`')
        self._data["Convergence Tolerance"] = value

    @property
    def damper_heating_action(self):
        """Get damper_heating_action

        Returns:
            str: the value of `damper_heating_action` or None if not set
        """
        return self._data["Damper Heating Action"]

    @damper_heating_action.setter
    def damper_heating_action(self, value="Normal"):
        """  Corresponds to IDD Field `Damper Heating Action`

        Args:
            value (str): value for IDD Field `Damper Heating Action`
                Accepted values are:
                      - Normal
                      - Reverse
                Default value: Normal
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
                                 ' for field `AirTerminalSingleDuctVavReheat.damper_heating_action`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.damper_heating_action`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.damper_heating_action`')
            vals = {}
            vals["normal"] = "Normal"
            vals["reverse"] = "Reverse"
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
                                     'field `AirTerminalSingleDuctVavReheat.damper_heating_action`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctVavReheat.damper_heating_action`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Damper Heating Action"] = value

    @property
    def maximum_flow_per_zone_floor_area_during_reheat(self):
        """Get maximum_flow_per_zone_floor_area_during_reheat

        Returns:
            float: the value of `maximum_flow_per_zone_floor_area_during_reheat` or None if not set
        """
        return self._data["Maximum Flow per Zone Floor Area During Reheat"]

    @maximum_flow_per_zone_floor_area_during_reheat.setter
    def maximum_flow_per_zone_floor_area_during_reheat(self, value=None):
        """  Corresponds to IDD Field `Maximum Flow per Zone Floor Area During Reheat`
        Used only when Reheat Coil Object Type = Coil:Heating:Water and Damper Heating Action = Reverse
        When autocalculating, the maximum flow per zone is set to 0.002032 m3/s-m2 (0.4 cfm/sqft)
        This optional field limits the maximum flow allowed in reheat mode.
        If this field and the following field are left blank, the maximum flow will not be limited.
        At no time will the maximum flow rate calculated here exceed the value of
        Maximum Air Flow Rate.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Maximum Flow per Zone Floor Area During Reheat`
                Units: m3/s-m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Maximum Flow per Zone Floor Area During Reheat"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `AirTerminalSingleDuctVavReheat.maximum_flow_per_zone_floor_area_during_reheat`'.format(value))
                    self._data["Maximum Flow per Zone Floor Area During Reheat"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `AirTerminalSingleDuctVavReheat.maximum_flow_per_zone_floor_area_during_reheat`'.format(value))
        self._data["Maximum Flow per Zone Floor Area During Reheat"] = value

    @property
    def maximum_flow_fraction_during_reheat(self):
        """Get maximum_flow_fraction_during_reheat

        Returns:
            float: the value of `maximum_flow_fraction_during_reheat` or None if not set
        """
        return self._data["Maximum Flow Fraction During Reheat"]

    @maximum_flow_fraction_during_reheat.setter
    def maximum_flow_fraction_during_reheat(self, value=None):
        """  Corresponds to IDD Field `Maximum Flow Fraction During Reheat`
        Used only when Reheat Coil Object Type = Coil:Heating:Water and Damper Heating Action = Reverse
        When autocalculating, the maximum flow fraction is set to the ratio of
        0.002032 m3/s-m2 (0.4 cfm/sqft) multiplied by the zone floor area and the
        Maximum Air Flow Rate.
        This optional field limits the maximum flow allowed in reheat mode.
        If this field and the previous field are left blank, the maximum flow will not be limited.
        At no time will the maximum flow rate calculated here exceed the value of
        Maximum Air Flow Rate.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Maximum Flow Fraction During Reheat`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Maximum Flow Fraction During Reheat"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `AirTerminalSingleDuctVavReheat.maximum_flow_fraction_during_reheat`'.format(value))
                    self._data["Maximum Flow Fraction During Reheat"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `AirTerminalSingleDuctVavReheat.maximum_flow_fraction_during_reheat`'.format(value))
        self._data["Maximum Flow Fraction During Reheat"] = value

    @property
    def maximum_reheat_air_temperature(self):
        """Get maximum_reheat_air_temperature

        Returns:
            float: the value of `maximum_reheat_air_temperature` or None if not set
        """
        return self._data["Maximum Reheat Air Temperature"]

    @maximum_reheat_air_temperature.setter
    def maximum_reheat_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Reheat Air Temperature`
        Specifies the maximum allowable supply air temperature leaving the reheat coil.
        If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.

        Args:
            value (float): value for IDD Field `Maximum Reheat Air Temperature`
                Units: C
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctVavReheat.maximum_reheat_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctVavReheat.maximum_reheat_air_temperature`')
        self._data["Maximum Reheat Air Temperature"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """Get design_specification_outdoor_air_object_name

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification Outdoor Air Object Name`
        When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        unit will increase flow as needed to meet this outdoor air requirement.
        If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        be computed based on the current number of occupants in the zone.
        At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.
        If this field is blank, then the terminal unit will not be controlled for outdoor air flow.

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheat.design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheat.design_specification_outdoor_air_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheat.design_specification_outdoor_air_object_name`')
        self._data["Design Specification Outdoor Air Object Name"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctVavReheat:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctVavReheat:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctVavReheat: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctVavReheat: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctVavReheatVariableSpeedFan(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan`
        Central air system terminal unit, single duct, variable volume, with reheat coil (hot
        water, electric, gas, or steam) and variable-speed fan. These units are usually
        employed in underfloor air distribution (UFAD) systems where the air is supplied at
        low static pressure through an underfloor plenum. The fan is used to control the flow
        of conditioned air that enters the space.
    """
    internal_name = "AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan"
    field_count = 16
    required_fields = ["Name", "Maximum Cooling Air Flow Rate", "Maximum Heating Air Flow Rate", "Zone Minimum Air Flow Fraction", "Fan Object Type", "Fan Name", "Heating Coil Object Type", "Heating Coil Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Maximum Cooling Air Flow Rate"] = None
        self._data["Maximum Heating Air Flow Rate"] = None
        self._data["Zone Minimum Air Flow Fraction"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Heating Coil Air Inlet Node Name"] = None
        self._data["Hot Water or Steam Inlet Node Name"] = None
        self._data["Fan Object Type"] = None
        self._data["Fan Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Maximum Hot Water or Steam Flow Rate"] = None
        self._data["Minimum Hot Water or Steam Flow Rate"] = None
        self._data["Heating Convergence Tolerance"] = None
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
            self.maximum_cooling_air_flow_rate = None
        else:
            self.maximum_cooling_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_heating_air_flow_rate = None
        else:
            self.maximum_heating_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_minimum_air_flow_fraction = None
        else:
            self.zone_minimum_air_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_air_inlet_node_name = None
        else:
            self.heating_coil_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_water_or_steam_inlet_node_name = None
        else:
            self.hot_water_or_steam_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_object_type = None
        else:
            self.fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_name = None
        else:
            self.fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hot_water_or_steam_flow_rate = None
        else:
            self.maximum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_hot_water_or_steam_flow_rate = None
        else:
            self.minimum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_convergence_tolerance = None
        else:
            self.heating_convergence_tolerance = vals[i]
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.name`')
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def maximum_cooling_air_flow_rate(self):
        """Get maximum_cooling_air_flow_rate

        Returns:
            float: the value of `maximum_cooling_air_flow_rate` or None if not set
        """
        return self._data["Maximum Cooling Air Flow Rate"]

    @maximum_cooling_air_flow_rate.setter
    def maximum_cooling_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Cooling Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Cooling Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Cooling Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.maximum_cooling_air_flow_rate`'.format(value))
                    self._data["Maximum Cooling Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.maximum_cooling_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.maximum_cooling_air_flow_rate`')
        self._data["Maximum Cooling Air Flow Rate"] = value

    @property
    def maximum_heating_air_flow_rate(self):
        """Get maximum_heating_air_flow_rate

        Returns:
            float: the value of `maximum_heating_air_flow_rate` or None if not set
        """
        return self._data["Maximum Heating Air Flow Rate"]

    @maximum_heating_air_flow_rate.setter
    def maximum_heating_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Heating Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Heating Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Heating Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.maximum_heating_air_flow_rate`'.format(value))
                    self._data["Maximum Heating Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.maximum_heating_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.maximum_heating_air_flow_rate`')
        self._data["Maximum Heating Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_fraction(self):
        """Get zone_minimum_air_flow_fraction

        Returns:
            float: the value of `zone_minimum_air_flow_fraction` or None if not set
        """
        return self._data["Zone Minimum Air Flow Fraction"]

    @zone_minimum_air_flow_fraction.setter
    def zone_minimum_air_flow_fraction(self, value=None):
        """  Corresponds to IDD Field `Zone Minimum Air Flow Fraction`
        fraction of cooling air flow rate

        Args:
            value (float): value for IDD Field `Zone Minimum Air Flow Fraction`
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.zone_minimum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.zone_minimum_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.zone_minimum_air_flow_fraction`')
        self._data["Zone Minimum Air Flow Fraction"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def heating_coil_air_inlet_node_name(self):
        """Get heating_coil_air_inlet_node_name

        Returns:
            str: the value of `heating_coil_air_inlet_node_name` or None if not set
        """
        return self._data["Heating Coil Air Inlet Node Name"]

    @heating_coil_air_inlet_node_name.setter
    def heating_coil_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Air Inlet Node Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Heating Coil Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_air_inlet_node_name`')
        self._data["Heating Coil Air Inlet Node Name"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """Get hot_water_or_steam_inlet_node_name

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set
        """
        return self._data["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Hot Water or Steam Inlet Node Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.hot_water_or_steam_inlet_node_name`')
        self._data["Hot Water or Steam Inlet Node Name"] = value

    @property
    def fan_object_type(self):
        """Get fan_object_type

        Returns:
            str: the value of `fan_object_type` or None if not set
        """
        return self._data["Fan Object Type"]

    @fan_object_type.setter
    def fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Fan Object Type`

        Args:
            value (str): value for IDD Field `Fan Object Type`
                Accepted values are:
                      - Fan:VariableVolume
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.fan_object_type`')
            vals = {}
            vals["fan:variablevolume"] = "Fan:VariableVolume"
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
                                     'field `AirTerminalSingleDuctVavReheatVariableSpeedFan.fan_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctVavReheatVariableSpeedFan.fan_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Fan Object Type"] = value

    @property
    def fan_name(self):
        """Get fan_name

        Returns:
            str: the value of `fan_name` or None if not set
        """
        return self._data["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """  Corresponds to IDD Field `Fan Name`

        Args:
            value (str): value for IDD Field `Fan Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.fan_name`')
        self._data["Fan Name"] = value

    @property
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """Get heating_coil_name

        Returns:
            str: the value of `heating_coil_name` or None if not set
        """
        return self._data["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_coil_name`')
        self._data["Heating Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """Get maximum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `maximum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Hot Water or Steam Flow Rate`
        Not used when heating coil type is gas or electric

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.maximum_hot_water_or_steam_flow_rate`'.format(value))
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.maximum_hot_water_or_steam_flow_rate`'.format(value))
        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Hot Water or Steam Flow Rate`
        Not used when heating coil type is gas or electric

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.minimum_hot_water_or_steam_flow_rate`')
        self._data["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def heating_convergence_tolerance(self):
        """Get heating_convergence_tolerance

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set
        """
        return self._data["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Heating Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`
                Default value: 0.001
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctVavReheatVariableSpeedFan.heating_convergence_tolerance`')
        self._data["Heating Convergence Tolerance"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctVavReheatVariableSpeedFan:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctVavReheatVariableSpeedFan:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctVavReheatVariableSpeedFan: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctVavReheatVariableSpeedFan: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctVavHeatAndCoolNoReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat`
        Central air system terminal unit, single duct, variable volume for both cooling and
        heating, with no reheat coil.
    """
    internal_name = "AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat"
    field_count = 6
    required_fields = ["Name", "Air Outlet Node Name", "Air Inlet Node Name", "Maximum Air Flow Rate", "Zone Minimum Air Flow Fraction"]
    extensible_fields = 0
    format = None
    min_fields = 6
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Maximum Air Flow Rate"] = None
        self._data["Zone Minimum Air Flow Fraction"] = None
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
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_minimum_air_flow_fraction = None
        else:
            self.zone_minimum_air_flow_fraction = vals[i]
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.name`')
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`
        The outlet node of the terminal unit.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.maximum_air_flow_rate`'.format(value))
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.maximum_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.maximum_air_flow_rate`')
        self._data["Maximum Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_fraction(self):
        """Get zone_minimum_air_flow_fraction

        Returns:
            float: the value of `zone_minimum_air_flow_fraction` or None if not set
        """
        return self._data["Zone Minimum Air Flow Fraction"]

    @zone_minimum_air_flow_fraction.setter
    def zone_minimum_air_flow_fraction(self, value=None):
        """  Corresponds to IDD Field `Zone Minimum Air Flow Fraction`
        fraction of maximum air flow

        Args:
            value (float): value for IDD Field `Zone Minimum Air Flow Fraction`
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.zone_minimum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.zone_minimum_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolNoReheat.zone_minimum_air_flow_fraction`')
        self._data["Zone Minimum Air Flow Fraction"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctVavHeatAndCoolNoReheat:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctVavHeatAndCoolNoReheat:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctVavHeatAndCoolNoReheat: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctVavHeatAndCoolNoReheat: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctVavHeatAndCoolReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat`
        Central air system terminal unit, single duct, variable volume for both cooling and
        heating, with reheat coil (hot water, electric, gas, or steam).
    """
    internal_name = "AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat"
    field_count = 14
    required_fields = ["Name", "Damper Air Outlet Node Name", "Air Inlet Node Name", "Maximum Air Flow Rate", "Zone Minimum Air Flow Fraction", "Reheat Coil Object Type", "Reheat Coil Name", "Air Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 12
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Damper Air Outlet Node Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Maximum Air Flow Rate"] = None
        self._data["Zone Minimum Air Flow Fraction"] = None
        self._data["Hot Water or Steam Inlet Node Name"] = None
        self._data["Reheat Coil Object Type"] = None
        self._data["Reheat Coil Name"] = None
        self._data["Maximum Hot Water or Steam Flow Rate"] = None
        self._data["Minimum Hot Water or Steam Flow Rate"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Convergence Tolerance"] = None
        self._data["Maximum Reheat Air Temperature"] = None
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
            self.damper_air_outlet_node_name = None
        else:
            self.damper_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_minimum_air_flow_fraction = None
        else:
            self.zone_minimum_air_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_water_or_steam_inlet_node_name = None
        else:
            self.hot_water_or_steam_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_object_type = None
        else:
            self.reheat_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_name = None
        else:
            self.reheat_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hot_water_or_steam_flow_rate = None
        else:
            self.maximum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_hot_water_or_steam_flow_rate = None
        else:
            self.minimum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_tolerance = None
        else:
            self.convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_reheat_air_temperature = None
        else:
            self.maximum_reheat_air_temperature = vals[i]
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.name`')
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def damper_air_outlet_node_name(self):
        """Get damper_air_outlet_node_name

        Returns:
            str: the value of `damper_air_outlet_node_name` or None if not set
        """
        return self._data["Damper Air Outlet Node Name"]

    @damper_air_outlet_node_name.setter
    def damper_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Damper Air Outlet Node Name`
        the outlet node of the damper and the inlet node of the reheat coil
        this is an internal node to the terminal unit and connects the damper and reheat coil

        Args:
            value (str): value for IDD Field `Damper Air Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.damper_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.damper_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.damper_air_outlet_node_name`')
        self._data["Damper Air Outlet Node Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`
        the inlet node to the terminal unit and the damper

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.maximum_air_flow_rate`'.format(value))
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.maximum_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.maximum_air_flow_rate`')
        self._data["Maximum Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_fraction(self):
        """Get zone_minimum_air_flow_fraction

        Returns:
            float: the value of `zone_minimum_air_flow_fraction` or None if not set
        """
        return self._data["Zone Minimum Air Flow Fraction"]

    @zone_minimum_air_flow_fraction.setter
    def zone_minimum_air_flow_fraction(self, value=None):
        """  Corresponds to IDD Field `Zone Minimum Air Flow Fraction`
        fraction of maximum air flow

        Args:
            value (float): value for IDD Field `Zone Minimum Air Flow Fraction`
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.zone_minimum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.zone_minimum_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.zone_minimum_air_flow_fraction`')
        self._data["Zone Minimum Air Flow Fraction"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """Get hot_water_or_steam_inlet_node_name

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set
        """
        return self._data["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Hot Water or Steam Inlet Node Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.hot_water_or_steam_inlet_node_name`')
        self._data["Hot Water or Steam Inlet Node Name"] = value

    @property
    def reheat_coil_object_type(self):
        """Get reheat_coil_object_type

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set
        """
        return self._data["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Object Type`

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.reheat_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.reheat_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `AirTerminalSingleDuctVavHeatAndCoolReheat.reheat_coil_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctVavHeatAndCoolReheat.reheat_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """Get reheat_coil_name

        Returns:
            str: the value of `reheat_coil_name` or None if not set
        """
        return self._data["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Name`
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.reheat_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.reheat_coil_name`')
        self._data["Reheat Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """Get maximum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `maximum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Hot Water or Steam Flow Rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.maximum_hot_water_or_steam_flow_rate`'.format(value))
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.maximum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.maximum_hot_water_or_steam_flow_rate`')
        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Hot Water or Steam Flow Rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.minimum_hot_water_or_steam_flow_rate`')
        self._data["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`
        The outlet node of the terminal unit and the reheat coil.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Convergence Tolerance`
                Default value: 0.001
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.convergence_tolerance`')
        self._data["Convergence Tolerance"] = value

    @property
    def maximum_reheat_air_temperature(self):
        """Get maximum_reheat_air_temperature

        Returns:
            float: the value of `maximum_reheat_air_temperature` or None if not set
        """
        return self._data["Maximum Reheat Air Temperature"]

    @maximum_reheat_air_temperature.setter
    def maximum_reheat_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Maximum Reheat Air Temperature`
        Specifies the maximum allowable supply air temperature leaving the reheat coil.
        If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.

        Args:
            value (float): value for IDD Field `Maximum Reheat Air Temperature`
                Units: C
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctVavHeatAndCoolReheat.maximum_reheat_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctVavHeatAndCoolReheat.maximum_reheat_air_temperature`')
        self._data["Maximum Reheat Air Temperature"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctVavHeatAndCoolReheat:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctVavHeatAndCoolReheat:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctVavHeatAndCoolReheat: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctVavHeatAndCoolReheat: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctSeriesPiuReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:SeriesPIU:Reheat`
        Central air system terminal unit, single duct, variable volume, series powered
        induction unit (PIU), with reheat coil (hot water, electric, gas, or steam).
    """
    internal_name = "AirTerminal:SingleDuct:SeriesPIU:Reheat"
    field_count = 17
    required_fields = ["Name", "Maximum Air Flow Rate", "Maximum Primary Air Flow Rate", "Minimum Primary Air Flow Fraction", "Reheat Coil Object Type", "Reheat Coil Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:SeriesPIU:Reheat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Maximum Air Flow Rate"] = None
        self._data["Maximum Primary Air Flow Rate"] = None
        self._data["Minimum Primary Air Flow Fraction"] = None
        self._data["Supply Air Inlet Node Name"] = None
        self._data["Secondary Air Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Reheat Coil Air Inlet Node Name"] = None
        self._data["Zone Mixer Name"] = None
        self._data["Fan Name"] = None
        self._data["Reheat Coil Object Type"] = None
        self._data["Reheat Coil Name"] = None
        self._data["Maximum Hot Water or Steam Flow Rate"] = None
        self._data["Minimum Hot Water or Steam Flow Rate"] = None
        self._data["Hot Water or Steam Inlet Node Name"] = None
        self._data["Convergence Tolerance"] = None
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
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_primary_air_flow_rate = None
        else:
            self.maximum_primary_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_primary_air_flow_fraction = None
        else:
            self.minimum_primary_air_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_inlet_node_name = None
        else:
            self.supply_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_air_inlet_node_name = None
        else:
            self.secondary_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_air_inlet_node_name = None
        else:
            self.reheat_coil_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_mixer_name = None
        else:
            self.zone_mixer_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_name = None
        else:
            self.fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_object_type = None
        else:
            self.reheat_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_name = None
        else:
            self.reheat_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hot_water_or_steam_flow_rate = None
        else:
            self.maximum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_hot_water_or_steam_flow_rate = None
        else:
            self.minimum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_water_or_steam_inlet_node_name = None
        else:
            self.hot_water_or_steam_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_tolerance = None
        else:
            self.convergence_tolerance = vals[i]
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.name`')
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.maximum_air_flow_rate`'.format(value))
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.maximum_air_flow_rate`')
        self._data["Maximum Air Flow Rate"] = value

    @property
    def maximum_primary_air_flow_rate(self):
        """Get maximum_primary_air_flow_rate

        Returns:
            float: the value of `maximum_primary_air_flow_rate` or None if not set
        """
        return self._data["Maximum Primary Air Flow Rate"]

    @maximum_primary_air_flow_rate.setter
    def maximum_primary_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Primary Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Primary Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Primary Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.maximum_primary_air_flow_rate`'.format(value))
                    self._data["Maximum Primary Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.maximum_primary_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.maximum_primary_air_flow_rate`')
        self._data["Maximum Primary Air Flow Rate"] = value

    @property
    def minimum_primary_air_flow_fraction(self):
        """Get minimum_primary_air_flow_fraction

        Returns:
            float: the value of `minimum_primary_air_flow_fraction` or None if not set
        """
        return self._data["Minimum Primary Air Flow Fraction"]

    @minimum_primary_air_flow_fraction.setter
    def minimum_primary_air_flow_fraction(self, value=None):
        """  Corresponds to IDD Field `Minimum Primary Air Flow Fraction`

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Primary Air Flow Fraction`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Minimum Primary Air Flow Fraction"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.minimum_primary_air_flow_fraction`'.format(value))
                    self._data["Minimum Primary Air Flow Fraction"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.minimum_primary_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.minimum_primary_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.minimum_primary_air_flow_fraction`')
        self._data["Minimum Primary Air Flow Fraction"] = value

    @property
    def supply_air_inlet_node_name(self):
        """Get supply_air_inlet_node_name

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.supply_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.supply_air_inlet_node_name`')
        self._data["Supply Air Inlet Node Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """Get secondary_air_inlet_node_name

        Returns:
            str: the value of `secondary_air_inlet_node_name` or None if not set
        """
        return self._data["Secondary Air Inlet Node Name"]

    @secondary_air_inlet_node_name.setter
    def secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Secondary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Secondary Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.secondary_air_inlet_node_name`')
        self._data["Secondary Air Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def reheat_coil_air_inlet_node_name(self):
        """Get reheat_coil_air_inlet_node_name

        Returns:
            str: the value of `reheat_coil_air_inlet_node_name` or None if not set
        """
        return self._data["Reheat Coil Air Inlet Node Name"]

    @reheat_coil_air_inlet_node_name.setter
    def reheat_coil_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_air_inlet_node_name`')
        self._data["Reheat Coil Air Inlet Node Name"] = value

    @property
    def zone_mixer_name(self):
        """Get zone_mixer_name

        Returns:
            str: the value of `zone_mixer_name` or None if not set
        """
        return self._data["Zone Mixer Name"]

    @zone_mixer_name.setter
    def zone_mixer_name(self, value=None):
        """  Corresponds to IDD Field `Zone Mixer Name`

        Args:
            value (str): value for IDD Field `Zone Mixer Name`
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.zone_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.zone_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.zone_mixer_name`')
        self._data["Zone Mixer Name"] = value

    @property
    def fan_name(self):
        """Get fan_name

        Returns:
            str: the value of `fan_name` or None if not set
        """
        return self._data["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """  Corresponds to IDD Field `Fan Name`
        Fan type must be Fan:ConstantVolume

        Args:
            value (str): value for IDD Field `Fan Name`
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.fan_name`')
        self._data["Fan Name"] = value

    @property
    def reheat_coil_object_type(self):
        """Get reheat_coil_object_type

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set
        """
        return self._data["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Object Type`

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """Get reheat_coil_name

        Returns:
            str: the value of `reheat_coil_name` or None if not set
        """
        return self._data["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Name`
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.reheat_coil_name`')
        self._data["Reheat Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """Get maximum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `maximum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Hot Water or Steam Flow Rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.maximum_hot_water_or_steam_flow_rate`'.format(value))
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.maximum_hot_water_or_steam_flow_rate`'.format(value))
        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Hot Water or Steam Flow Rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.minimum_hot_water_or_steam_flow_rate`')
        self._data["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """Get hot_water_or_steam_inlet_node_name

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set
        """
        return self._data["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Hot Water or Steam Inlet Node Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.hot_water_or_steam_inlet_node_name`')
        self._data["Hot Water or Steam Inlet Node Name"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Convergence Tolerance`
                Default value: 0.001
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctSeriesPiuReheat.convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctSeriesPiuReheat.convergence_tolerance`')
        self._data["Convergence Tolerance"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctSeriesPiuReheat:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctSeriesPiuReheat:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctSeriesPiuReheat: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctSeriesPiuReheat: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctParallelPiuReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:ParallelPIU:Reheat`
        Central air system terminal unit, single duct, variable volume, parallel powered
        induction unit (PIU), with reheat coil (hot water, electric, gas, or steam).
    """
    internal_name = "AirTerminal:SingleDuct:ParallelPIU:Reheat"
    field_count = 18
    required_fields = ["Name", "Maximum Primary Air Flow Rate", "Maximum Secondary Air Flow Rate", "Minimum Primary Air Flow Fraction", "Fan On Flow Fraction", "Reheat Coil Object Type", "Reheat Coil Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:ParallelPIU:Reheat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Maximum Primary Air Flow Rate"] = None
        self._data["Maximum Secondary Air Flow Rate"] = None
        self._data["Minimum Primary Air Flow Fraction"] = None
        self._data["Fan On Flow Fraction"] = None
        self._data["Supply Air Inlet Node Name"] = None
        self._data["Secondary Air Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Reheat Coil Air Inlet Node Name"] = None
        self._data["Zone Mixer Name"] = None
        self._data["Fan Name"] = None
        self._data["Reheat Coil Object Type"] = None
        self._data["Reheat Coil Name"] = None
        self._data["Maximum Hot Water or Steam Flow Rate"] = None
        self._data["Minimum Hot Water or Steam Flow Rate"] = None
        self._data["Hot Water or Steam Inlet Node Name"] = None
        self._data["Convergence Tolerance"] = None
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
            self.maximum_primary_air_flow_rate = None
        else:
            self.maximum_primary_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_secondary_air_flow_rate = None
        else:
            self.maximum_secondary_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_primary_air_flow_fraction = None
        else:
            self.minimum_primary_air_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_on_flow_fraction = None
        else:
            self.fan_on_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_inlet_node_name = None
        else:
            self.supply_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_air_inlet_node_name = None
        else:
            self.secondary_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_air_inlet_node_name = None
        else:
            self.reheat_coil_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_mixer_name = None
        else:
            self.zone_mixer_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_name = None
        else:
            self.fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_object_type = None
        else:
            self.reheat_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reheat_coil_name = None
        else:
            self.reheat_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hot_water_or_steam_flow_rate = None
        else:
            self.maximum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_hot_water_or_steam_flow_rate = None
        else:
            self.minimum_hot_water_or_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_water_or_steam_inlet_node_name = None
        else:
            self.hot_water_or_steam_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_tolerance = None
        else:
            self.convergence_tolerance = vals[i]
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.name`')
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def maximum_primary_air_flow_rate(self):
        """Get maximum_primary_air_flow_rate

        Returns:
            float: the value of `maximum_primary_air_flow_rate` or None if not set
        """
        return self._data["Maximum Primary Air Flow Rate"]

    @maximum_primary_air_flow_rate.setter
    def maximum_primary_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Primary Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Primary Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Primary Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.maximum_primary_air_flow_rate`'.format(value))
                    self._data["Maximum Primary Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.maximum_primary_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.maximum_primary_air_flow_rate`')
        self._data["Maximum Primary Air Flow Rate"] = value

    @property
    def maximum_secondary_air_flow_rate(self):
        """Get maximum_secondary_air_flow_rate

        Returns:
            float: the value of `maximum_secondary_air_flow_rate` or None if not set
        """
        return self._data["Maximum Secondary Air Flow Rate"]

    @maximum_secondary_air_flow_rate.setter
    def maximum_secondary_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Secondary Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Secondary Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Secondary Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.maximum_secondary_air_flow_rate`'.format(value))
                    self._data["Maximum Secondary Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.maximum_secondary_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.maximum_secondary_air_flow_rate`')
        self._data["Maximum Secondary Air Flow Rate"] = value

    @property
    def minimum_primary_air_flow_fraction(self):
        """Get minimum_primary_air_flow_fraction

        Returns:
            float: the value of `minimum_primary_air_flow_fraction` or None if not set
        """
        return self._data["Minimum Primary Air Flow Fraction"]

    @minimum_primary_air_flow_fraction.setter
    def minimum_primary_air_flow_fraction(self, value=None):
        """  Corresponds to IDD Field `Minimum Primary Air Flow Fraction`

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Primary Air Flow Fraction`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Minimum Primary Air Flow Fraction"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.minimum_primary_air_flow_fraction`'.format(value))
                    self._data["Minimum Primary Air Flow Fraction"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.minimum_primary_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.minimum_primary_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.minimum_primary_air_flow_fraction`')
        self._data["Minimum Primary Air Flow Fraction"] = value

    @property
    def fan_on_flow_fraction(self):
        """Get fan_on_flow_fraction

        Returns:
            float: the value of `fan_on_flow_fraction` or None if not set
        """
        return self._data["Fan On Flow Fraction"]

    @fan_on_flow_fraction.setter
    def fan_on_flow_fraction(self, value=None):
        """  Corresponds to IDD Field `Fan On Flow Fraction`
        the fraction of the primary air flow at which fan turns on

        Args:
            value (float or "Autosize"): value for IDD Field `Fan On Flow Fraction`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Fan On Flow Fraction"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.fan_on_flow_fraction`'.format(value))
                    self._data["Fan On Flow Fraction"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.fan_on_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.fan_on_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.fan_on_flow_fraction`')
        self._data["Fan On Flow Fraction"] = value

    @property
    def supply_air_inlet_node_name(self):
        """Get supply_air_inlet_node_name

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.supply_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.supply_air_inlet_node_name`')
        self._data["Supply Air Inlet Node Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """Get secondary_air_inlet_node_name

        Returns:
            str: the value of `secondary_air_inlet_node_name` or None if not set
        """
        return self._data["Secondary Air Inlet Node Name"]

    @secondary_air_inlet_node_name.setter
    def secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Secondary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Secondary Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.secondary_air_inlet_node_name`')
        self._data["Secondary Air Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def reheat_coil_air_inlet_node_name(self):
        """Get reheat_coil_air_inlet_node_name

        Returns:
            str: the value of `reheat_coil_air_inlet_node_name` or None if not set
        """
        return self._data["Reheat Coil Air Inlet Node Name"]

    @reheat_coil_air_inlet_node_name.setter
    def reheat_coil_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Air Inlet Node Name`
        mixer outlet node

        Args:
            value (str): value for IDD Field `Reheat Coil Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_air_inlet_node_name`')
        self._data["Reheat Coil Air Inlet Node Name"] = value

    @property
    def zone_mixer_name(self):
        """Get zone_mixer_name

        Returns:
            str: the value of `zone_mixer_name` or None if not set
        """
        return self._data["Zone Mixer Name"]

    @zone_mixer_name.setter
    def zone_mixer_name(self, value=None):
        """  Corresponds to IDD Field `Zone Mixer Name`

        Args:
            value (str): value for IDD Field `Zone Mixer Name`
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.zone_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.zone_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.zone_mixer_name`')
        self._data["Zone Mixer Name"] = value

    @property
    def fan_name(self):
        """Get fan_name

        Returns:
            str: the value of `fan_name` or None if not set
        """
        return self._data["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """  Corresponds to IDD Field `Fan Name`
        Fan type must be Fan:ConstantVolume

        Args:
            value (str): value for IDD Field `Fan Name`
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.fan_name`')
        self._data["Fan Name"] = value

    @property
    def reheat_coil_object_type(self):
        """Get reheat_coil_object_type

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set
        """
        return self._data["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Object Type`

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
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
                                     'field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """Get reheat_coil_name

        Returns:
            str: the value of `reheat_coil_name` or None if not set
        """
        return self._data["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """  Corresponds to IDD Field `Reheat Coil Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Name`
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.reheat_coil_name`')
        self._data["Reheat Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """Get maximum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `maximum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Hot Water or Steam Flow Rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.maximum_hot_water_or_steam_flow_rate`'.format(value))
                    self._data["Maximum Hot Water or Steam Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.maximum_hot_water_or_steam_flow_rate`'.format(value))
        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Hot Water or Steam Flow Rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.minimum_hot_water_or_steam_flow_rate`')
        self._data["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """Get hot_water_or_steam_inlet_node_name

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set
        """
        return self._data["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Hot Water or Steam Inlet Node Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.hot_water_or_steam_inlet_node_name`')
        self._data["Hot Water or Steam Inlet Node Name"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Convergence Tolerance`
                Default value: 0.001
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctParallelPiuReheat.convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctParallelPiuReheat.convergence_tolerance`')
        self._data["Convergence Tolerance"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctParallelPiuReheat:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctParallelPiuReheat:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctParallelPiuReheat: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctParallelPiuReheat: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctConstantVolumeFourPipeInduction(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction`
        Central air system terminal unit, single duct, variable volume, induction unit with
        hot water reheat coil and chilled water recool coil.
    """
    internal_name = "AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction"
    field_count = 20
    required_fields = ["Name", "Maximum Total Air Flow Rate", "Induction Ratio", "Supply Air Inlet Node Name", "Induced Air Inlet Node Name", "Air Outlet Node Name", "Heating Coil Object Type", "Heating Coil Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Maximum Total Air Flow Rate"] = None
        self._data["Induction Ratio"] = None
        self._data["Supply Air Inlet Node Name"] = None
        self._data["Induced Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Hot Water Inlet Node Name"] = None
        self._data["Cold Water Inlet Node Name"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Maximum Hot Water Flow Rate"] = None
        self._data["Minimum Hot Water Flow Rate"] = None
        self._data["Heating Convergence Tolerance"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Maximum Cold Water Flow Rate"] = None
        self._data["Minimum Cold Water Flow Rate"] = None
        self._data["Cooling Convergence Tolerance"] = None
        self._data["Zone Mixer Name"] = None
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
            self.maximum_total_air_flow_rate = None
        else:
            self.maximum_total_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.induction_ratio = None
        else:
            self.induction_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_inlet_node_name = None
        else:
            self.supply_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.induced_air_inlet_node_name = None
        else:
            self.induced_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_water_inlet_node_name = None
        else:
            self.hot_water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cold_water_inlet_node_name = None
        else:
            self.cold_water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hot_water_flow_rate = None
        else:
            self.maximum_hot_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_hot_water_flow_rate = None
        else:
            self.minimum_hot_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_convergence_tolerance = None
        else:
            self.heating_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_cold_water_flow_rate = None
        else:
            self.maximum_cold_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_cold_water_flow_rate = None
        else:
            self.minimum_cold_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_convergence_tolerance = None
        else:
            self.cooling_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_mixer_name = None
        else:
            self.zone_mixer_name = vals[i]
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.name`')
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def maximum_total_air_flow_rate(self):
        """Get maximum_total_air_flow_rate

        Returns:
            float: the value of `maximum_total_air_flow_rate` or None if not set
        """
        return self._data["Maximum Total Air Flow Rate"]

    @maximum_total_air_flow_rate.setter
    def maximum_total_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Total Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Total Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Total Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.maximum_total_air_flow_rate`'.format(value))
                    self._data["Maximum Total Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.maximum_total_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.maximum_total_air_flow_rate`')
        self._data["Maximum Total Air Flow Rate"] = value

    @property
    def induction_ratio(self):
        """Get induction_ratio

        Returns:
            float: the value of `induction_ratio` or None if not set
        """
        return self._data["Induction Ratio"]

    @induction_ratio.setter
    def induction_ratio(self, value=2.5):
        """  Corresponds to IDD Field `Induction Ratio`
        ratio of induced air flow rate to primary air flow rate

        Args:
            value (float): value for IDD Field `Induction Ratio`
                Default value: 2.5
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.induction_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.induction_ratio`')
        self._data["Induction Ratio"] = value

    @property
    def supply_air_inlet_node_name(self):
        """Get supply_air_inlet_node_name

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.supply_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.supply_air_inlet_node_name`')
        self._data["Supply Air Inlet Node Name"] = value

    @property
    def induced_air_inlet_node_name(self):
        """Get induced_air_inlet_node_name

        Returns:
            str: the value of `induced_air_inlet_node_name` or None if not set
        """
        return self._data["Induced Air Inlet Node Name"]

    @induced_air_inlet_node_name.setter
    def induced_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Induced Air Inlet Node Name`
        should be a zone exhaust node, also the heating coil inlet node

        Args:
            value (str): value for IDD Field `Induced Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.induced_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.induced_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.induced_air_inlet_node_name`')
        self._data["Induced Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`
        should be a zone inlet node

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def hot_water_inlet_node_name(self):
        """Get hot_water_inlet_node_name

        Returns:
            str: the value of `hot_water_inlet_node_name` or None if not set
        """
        return self._data["Hot Water Inlet Node Name"]

    @hot_water_inlet_node_name.setter
    def hot_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Hot Water Inlet Node Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.hot_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.hot_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.hot_water_inlet_node_name`')
        self._data["Hot Water Inlet Node Name"] = value

    @property
    def cold_water_inlet_node_name(self):
        """Get cold_water_inlet_node_name

        Returns:
            str: the value of `cold_water_inlet_node_name` or None if not set
        """
        return self._data["Cold Water Inlet Node Name"]

    @cold_water_inlet_node_name.setter
    def cold_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Cold Water Inlet Node Name`
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.

        Args:
            value (str): value for IDD Field `Cold Water Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cold_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cold_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cold_water_inlet_node_name`')
        self._data["Cold Water Inlet Node Name"] = value

    @property
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.heating_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
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
                                     'field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.heating_coil_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.heating_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """Get heating_coil_name

        Returns:
            str: the value of `heating_coil_name` or None if not set
        """
        return self._data["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.heating_coil_name`')
        self._data["Heating Coil Name"] = value

    @property
    def maximum_hot_water_flow_rate(self):
        """Get maximum_hot_water_flow_rate

        Returns:
            float: the value of `maximum_hot_water_flow_rate` or None if not set
        """
        return self._data["Maximum Hot Water Flow Rate"]

    @maximum_hot_water_flow_rate.setter
    def maximum_hot_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Hot Water Flow Rate`
        Not used when heating coil type is gas or electric

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Hot Water Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.maximum_hot_water_flow_rate`'.format(value))
                    self._data["Maximum Hot Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.maximum_hot_water_flow_rate`'.format(value))
        self._data["Maximum Hot Water Flow Rate"] = value

    @property
    def minimum_hot_water_flow_rate(self):
        """Get minimum_hot_water_flow_rate

        Returns:
            float: the value of `minimum_hot_water_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water Flow Rate"]

    @minimum_hot_water_flow_rate.setter
    def minimum_hot_water_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Hot Water Flow Rate`
        Not used when heating coil type is gas or electric

        Args:
            value (float): value for IDD Field `Minimum Hot Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.minimum_hot_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.minimum_hot_water_flow_rate`')
        self._data["Minimum Hot Water Flow Rate"] = value

    @property
    def heating_convergence_tolerance(self):
        """Get heating_convergence_tolerance

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set
        """
        return self._data["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Heating Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`
                Default value: 0.001
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.heating_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.heating_convergence_tolerance`')
        self._data["Heating Convergence Tolerance"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
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
                                     'field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cooling_coil_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cooling_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """Get cooling_coil_name

        Returns:
            str: the value of `cooling_coil_name` or None if not set
        """
        return self._data["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Name`

        Args:
            value (str): value for IDD Field `Cooling Coil Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cooling_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cooling_coil_name`')
        self._data["Cooling Coil Name"] = value

    @property
    def maximum_cold_water_flow_rate(self):
        """Get maximum_cold_water_flow_rate

        Returns:
            float: the value of `maximum_cold_water_flow_rate` or None if not set
        """
        return self._data["Maximum Cold Water Flow Rate"]

    @maximum_cold_water_flow_rate.setter
    def maximum_cold_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Cold Water Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Cold Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Cold Water Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.maximum_cold_water_flow_rate`'.format(value))
                    self._data["Maximum Cold Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.maximum_cold_water_flow_rate`'.format(value))
        self._data["Maximum Cold Water Flow Rate"] = value

    @property
    def minimum_cold_water_flow_rate(self):
        """Get minimum_cold_water_flow_rate

        Returns:
            float: the value of `minimum_cold_water_flow_rate` or None if not set
        """
        return self._data["Minimum Cold Water Flow Rate"]

    @minimum_cold_water_flow_rate.setter
    def minimum_cold_water_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Minimum Cold Water Flow Rate`

        Args:
            value (float): value for IDD Field `Minimum Cold Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                Default value: 0.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.minimum_cold_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.minimum_cold_water_flow_rate`')
        self._data["Minimum Cold Water Flow Rate"] = value

    @property
    def cooling_convergence_tolerance(self):
        """Get cooling_convergence_tolerance

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set
        """
        return self._data["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Cooling Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Cooling Convergence Tolerance`
                Default value: 0.001
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cooling_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.cooling_convergence_tolerance`')
        self._data["Cooling Convergence Tolerance"] = value

    @property
    def zone_mixer_name(self):
        """Get zone_mixer_name

        Returns:
            str: the value of `zone_mixer_name` or None if not set
        """
        return self._data["Zone Mixer Name"]

    @zone_mixer_name.setter
    def zone_mixer_name(self, value=None):
        """  Corresponds to IDD Field `Zone Mixer Name`

        Args:
            value (str): value for IDD Field `Zone Mixer Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.zone_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.zone_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeFourPipeInduction.zone_mixer_name`')
        self._data["Zone Mixer Name"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctConstantVolumeFourPipeInduction:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctConstantVolumeFourPipeInduction:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctConstantVolumeFourPipeInduction: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctConstantVolumeFourPipeInduction: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctConstantVolumeCooledBeam(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:ConstantVolume:CooledBeam`
        Central air system terminal unit, single duct, constant volume, with cooled beam
        (active or passive).
    """
    internal_name = "AirTerminal:SingleDuct:ConstantVolume:CooledBeam"
    field_count = 23
    required_fields = ["Name", "Cooled Beam Type", "Supply Air Inlet Node Name", "Supply Air Outlet Node Name", "Chilled Water Inlet Node Name", "Chilled Water Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 23
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:ConstantVolume:CooledBeam`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Cooled Beam Type"] = None
        self._data["Supply Air Inlet Node Name"] = None
        self._data["Supply Air Outlet Node Name"] = None
        self._data["Chilled Water Inlet Node Name"] = None
        self._data["Chilled Water Outlet Node Name"] = None
        self._data["Supply Air Volumetric Flow Rate"] = None
        self._data["Maximum Total Chilled Water Volumetric Flow Rate"] = None
        self._data["Number of Beams"] = None
        self._data["Beam Length"] = None
        self._data["Design Inlet Water Temperature"] = None
        self._data["Design Outlet Water Temperature"] = None
        self._data["Coil Surface Area per Coil Length"] = None
        self._data["Model Parameter a"] = None
        self._data["Model Parameter n1"] = None
        self._data["Model Parameter n2"] = None
        self._data["Model Parameter n3"] = None
        self._data["Model Parameter a0"] = None
        self._data["Model Parameter K1"] = None
        self._data["Model Parameter n"] = None
        self._data["Coefficient of Induction Kin"] = None
        self._data["Leaving Pipe Inside Diameter"] = None
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
            self.cooled_beam_type = None
        else:
            self.cooled_beam_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_inlet_node_name = None
        else:
            self.supply_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_outlet_node_name = None
        else:
            self.supply_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.chilled_water_inlet_node_name = None
        else:
            self.chilled_water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.chilled_water_outlet_node_name = None
        else:
            self.chilled_water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_volumetric_flow_rate = None
        else:
            self.supply_air_volumetric_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_total_chilled_water_volumetric_flow_rate = None
        else:
            self.maximum_total_chilled_water_volumetric_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_beams = None
        else:
            self.number_of_beams = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.beam_length = None
        else:
            self.beam_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_inlet_water_temperature = None
        else:
            self.design_inlet_water_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_outlet_water_temperature = None
        else:
            self.design_outlet_water_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coil_surface_area_per_coil_length = None
        else:
            self.coil_surface_area_per_coil_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.model_parameter_a = None
        else:
            self.model_parameter_a = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.model_parameter_n1 = None
        else:
            self.model_parameter_n1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.model_parameter_n2 = None
        else:
            self.model_parameter_n2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.model_parameter_n3 = None
        else:
            self.model_parameter_n3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.model_parameter_a0 = None
        else:
            self.model_parameter_a0 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.model_parameter_k1 = None
        else:
            self.model_parameter_k1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.model_parameter_n = None
        else:
            self.model_parameter_n = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_of_induction_kin = None
        else:
            self.coefficient_of_induction_kin = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.leaving_pipe_inside_diameter = None
        else:
            self.leaving_pipe_inside_diameter = vals[i]
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.name`')
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def cooled_beam_type(self):
        """Get cooled_beam_type

        Returns:
            str: the value of `cooled_beam_type` or None if not set
        """
        return self._data["Cooled Beam Type"]

    @cooled_beam_type.setter
    def cooled_beam_type(self, value=None):
        """  Corresponds to IDD Field `Cooled Beam Type`

        Args:
            value (str): value for IDD Field `Cooled Beam Type`
                Accepted values are:
                      - Active
                      - Passive
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.cooled_beam_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.cooled_beam_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.cooled_beam_type`')
            vals = {}
            vals["active"] = "Active"
            vals["passive"] = "Passive"
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
                                     'field `AirTerminalSingleDuctConstantVolumeCooledBeam.cooled_beam_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalSingleDuctConstantVolumeCooledBeam.cooled_beam_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Cooled Beam Type"] = value

    @property
    def supply_air_inlet_node_name(self):
        """Get supply_air_inlet_node_name

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.supply_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.supply_air_inlet_node_name`')
        self._data["Supply Air Inlet Node Name"] = value

    @property
    def supply_air_outlet_node_name(self):
        """Get supply_air_outlet_node_name

        Returns:
            str: the value of `supply_air_outlet_node_name` or None if not set
        """
        return self._data["Supply Air Outlet Node Name"]

    @supply_air_outlet_node_name.setter
    def supply_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.supply_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.supply_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.supply_air_outlet_node_name`')
        self._data["Supply Air Outlet Node Name"] = value

    @property
    def chilled_water_inlet_node_name(self):
        """Get chilled_water_inlet_node_name

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set
        """
        return self._data["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Chilled Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Chilled Water Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.chilled_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.chilled_water_inlet_node_name`')
        self._data["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """Get chilled_water_outlet_node_name

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set
        """
        return self._data["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Chilled Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Chilled Water Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.chilled_water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.chilled_water_outlet_node_name`')
        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def supply_air_volumetric_flow_rate(self):
        """Get supply_air_volumetric_flow_rate

        Returns:
            float: the value of `supply_air_volumetric_flow_rate` or None if not set
        """
        return self._data["Supply Air Volumetric Flow Rate"]

    @supply_air_volumetric_flow_rate.setter
    def supply_air_volumetric_flow_rate(self, value="autosize"):
        """  Corresponds to IDD Field `Supply Air Volumetric Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Volumetric Flow Rate`
                Units: m3/s
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Volumetric Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.supply_air_volumetric_flow_rate`'.format(value))
                    self._data["Supply Air Volumetric Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.supply_air_volumetric_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.supply_air_volumetric_flow_rate`')
        self._data["Supply Air Volumetric Flow Rate"] = value

    @property
    def maximum_total_chilled_water_volumetric_flow_rate(self):
        """Get maximum_total_chilled_water_volumetric_flow_rate

        Returns:
            float: the value of `maximum_total_chilled_water_volumetric_flow_rate` or None if not set
        """
        return self._data["Maximum Total Chilled Water Volumetric Flow Rate"]

    @maximum_total_chilled_water_volumetric_flow_rate.setter
    def maximum_total_chilled_water_volumetric_flow_rate(self, value="autosize"):
        """  Corresponds to IDD Field `Maximum Total Chilled Water Volumetric Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Total Chilled Water Volumetric Flow Rate`
                Units: m3/s
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Total Chilled Water Volumetric Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.maximum_total_chilled_water_volumetric_flow_rate`'.format(value))
                    self._data["Maximum Total Chilled Water Volumetric Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.maximum_total_chilled_water_volumetric_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.maximum_total_chilled_water_volumetric_flow_rate`')
        self._data["Maximum Total Chilled Water Volumetric Flow Rate"] = value

    @property
    def number_of_beams(self):
        """Get number_of_beams

        Returns:
            int: the value of `number_of_beams` or None if not set
        """
        return self._data["Number of Beams"]

    @number_of_beams.setter
    def number_of_beams(self, value="autosize"):
        """  Corresponds to IDD Field `Number of Beams`
        Number of individual beam units in the zone

        Args:
            value (int or "Autosize"): value for IDD Field `Number of Beams`
                Default value: "autosize"
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Number of Beams"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.number_of_beams`'.format(value))
                    self._data["Number of Beams"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.number_of_beams`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.number_of_beams`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.number_of_beams`')
        self._data["Number of Beams"] = value

    @property
    def beam_length(self):
        """Get beam_length

        Returns:
            float: the value of `beam_length` or None if not set
        """
        return self._data["Beam Length"]

    @beam_length.setter
    def beam_length(self, value="autosize"):
        """  Corresponds to IDD Field `Beam Length`
        Length of an individual beam unit

        Args:
            value (float or "Autosize"): value for IDD Field `Beam Length`
                Units: m
                Default value: "autosize"
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Beam Length"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.beam_length`'.format(value))
                    self._data["Beam Length"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.beam_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.beam_length`')
        self._data["Beam Length"] = value

    @property
    def design_inlet_water_temperature(self):
        """Get design_inlet_water_temperature

        Returns:
            float: the value of `design_inlet_water_temperature` or None if not set
        """
        return self._data["Design Inlet Water Temperature"]

    @design_inlet_water_temperature.setter
    def design_inlet_water_temperature(self, value=15.0):
        """  Corresponds to IDD Field `Design Inlet Water Temperature`

        Args:
            value (float): value for IDD Field `Design Inlet Water Temperature`
                Units: C
                Default value: 15.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.design_inlet_water_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.design_inlet_water_temperature`')
        self._data["Design Inlet Water Temperature"] = value

    @property
    def design_outlet_water_temperature(self):
        """Get design_outlet_water_temperature

        Returns:
            float: the value of `design_outlet_water_temperature` or None if not set
        """
        return self._data["Design Outlet Water Temperature"]

    @design_outlet_water_temperature.setter
    def design_outlet_water_temperature(self, value=17.0):
        """  Corresponds to IDD Field `Design Outlet Water Temperature`

        Args:
            value (float): value for IDD Field `Design Outlet Water Temperature`
                Units: C
                Default value: 17.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.design_outlet_water_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.design_outlet_water_temperature`')
        self._data["Design Outlet Water Temperature"] = value

    @property
    def coil_surface_area_per_coil_length(self):
        """Get coil_surface_area_per_coil_length

        Returns:
            float: the value of `coil_surface_area_per_coil_length` or None if not set
        """
        return self._data["Coil Surface Area per Coil Length"]

    @coil_surface_area_per_coil_length.setter
    def coil_surface_area_per_coil_length(self, value=5.422):
        """  Corresponds to IDD Field `Coil Surface Area per Coil Length`

        Args:
            value (float): value for IDD Field `Coil Surface Area per Coil Length`
                Units: m2/m
                Default value: 5.422
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.coil_surface_area_per_coil_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.coil_surface_area_per_coil_length`')
        self._data["Coil Surface Area per Coil Length"] = value

    @property
    def model_parameter_a(self):
        """Get model_parameter_a

        Returns:
            float: the value of `model_parameter_a` or None if not set
        """
        return self._data["Model Parameter a"]

    @model_parameter_a.setter
    def model_parameter_a(self, value=15.3):
        """  Corresponds to IDD Field `Model Parameter a`

        Args:
            value (float): value for IDD Field `Model Parameter a`
                Default value: 15.3
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_a`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_a`')
        self._data["Model Parameter a"] = value

    @property
    def model_parameter_n1(self):
        """Get model_parameter_n1

        Returns:
            float: the value of `model_parameter_n1` or None if not set
        """
        return self._data["Model Parameter n1"]

    @model_parameter_n1.setter
    def model_parameter_n1(self, value=0.0):
        """  Corresponds to IDD Field `Model Parameter n1`

        Args:
            value (float): value for IDD Field `Model Parameter n1`
                Default value: 0.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_n1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_n1`')
        self._data["Model Parameter n1"] = value

    @property
    def model_parameter_n2(self):
        """Get model_parameter_n2

        Returns:
            float: the value of `model_parameter_n2` or None if not set
        """
        return self._data["Model Parameter n2"]

    @model_parameter_n2.setter
    def model_parameter_n2(self, value=0.84):
        """  Corresponds to IDD Field `Model Parameter n2`

        Args:
            value (float): value for IDD Field `Model Parameter n2`
                Default value: 0.84
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_n2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_n2`')
        self._data["Model Parameter n2"] = value

    @property
    def model_parameter_n3(self):
        """Get model_parameter_n3

        Returns:
            float: the value of `model_parameter_n3` or None if not set
        """
        return self._data["Model Parameter n3"]

    @model_parameter_n3.setter
    def model_parameter_n3(self, value=0.12):
        """  Corresponds to IDD Field `Model Parameter n3`

        Args:
            value (float): value for IDD Field `Model Parameter n3`
                Default value: 0.12
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_n3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_n3`')
        self._data["Model Parameter n3"] = value

    @property
    def model_parameter_a0(self):
        """Get model_parameter_a0

        Returns:
            float: the value of `model_parameter_a0` or None if not set
        """
        return self._data["Model Parameter a0"]

    @model_parameter_a0.setter
    def model_parameter_a0(self, value=0.171):
        """  Corresponds to IDD Field `Model Parameter a0`
        Free area of the coil in plan view per unit beam length

        Args:
            value (float): value for IDD Field `Model Parameter a0`
                Units: m2/m
                Default value: 0.171
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_a0`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_a0`')
        self._data["Model Parameter a0"] = value

    @property
    def model_parameter_k1(self):
        """Get model_parameter_k1

        Returns:
            float: the value of `model_parameter_k1` or None if not set
        """
        return self._data["Model Parameter K1"]

    @model_parameter_k1.setter
    def model_parameter_k1(self, value=0.0057):
        """  Corresponds to IDD Field `Model Parameter K1`

        Args:
            value (float): value for IDD Field `Model Parameter K1`
                Default value: 0.0057
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_k1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_k1`')
        self._data["Model Parameter K1"] = value

    @property
    def model_parameter_n(self):
        """Get model_parameter_n

        Returns:
            float: the value of `model_parameter_n` or None if not set
        """
        return self._data["Model Parameter n"]

    @model_parameter_n.setter
    def model_parameter_n(self, value=0.4):
        """  Corresponds to IDD Field `Model Parameter n`

        Args:
            value (float): value for IDD Field `Model Parameter n`
                Default value: 0.4
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_n`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.model_parameter_n`')
        self._data["Model Parameter n"] = value

    @property
    def coefficient_of_induction_kin(self):
        """Get coefficient_of_induction_kin

        Returns:
            float: the value of `coefficient_of_induction_kin` or None if not set
        """
        return self._data["Coefficient of Induction Kin"]

    @coefficient_of_induction_kin.setter
    def coefficient_of_induction_kin(self, value="Autocalculate"):
        """  Corresponds to IDD Field `Coefficient of Induction Kin`

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient of Induction Kin`
                Default value: "Autocalculate"
                value >= 0.0
                value <= 4.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient of Induction Kin"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.coefficient_of_induction_kin`'.format(value))
                    self._data["Coefficient of Induction Kin"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.coefficient_of_induction_kin`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.coefficient_of_induction_kin`')
            if value > 4.0:
                raise ValueError('value need to be smaller 4.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.coefficient_of_induction_kin`')
        self._data["Coefficient of Induction Kin"] = value

    @property
    def leaving_pipe_inside_diameter(self):
        """Get leaving_pipe_inside_diameter

        Returns:
            float: the value of `leaving_pipe_inside_diameter` or None if not set
        """
        return self._data["Leaving Pipe Inside Diameter"]

    @leaving_pipe_inside_diameter.setter
    def leaving_pipe_inside_diameter(self, value=0.0145):
        """  Corresponds to IDD Field `Leaving Pipe Inside Diameter`

        Args:
            value (float): value for IDD Field `Leaving Pipe Inside Diameter`
                Units: m
                Default value: 0.0145
                value > 0.0
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
                                 ' for field `AirTerminalSingleDuctConstantVolumeCooledBeam.leaving_pipe_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `AirTerminalSingleDuctConstantVolumeCooledBeam.leaving_pipe_inside_diameter`')
        self._data["Leaving Pipe Inside Diameter"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctConstantVolumeCooledBeam:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctConstantVolumeCooledBeam:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctConstantVolumeCooledBeam: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctConstantVolumeCooledBeam: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctInletSideMixer(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:InletSideMixer`
        Mix 2 inlet air streams into one outlet stream.
    """
    internal_name = "AirTerminal:SingleDuct:InletSideMixer"
    field_count = 6
    required_fields = ["Name", "ZoneHVAC Terminal Unit Object Type", "ZoneHVAC Terminal Unit Name", "Terminal Unit Outlet Node Name", "Terminal Unit Primary Air Inlet Node Name", "Terminal Unit Secondary Air Inlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:InletSideMixer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["ZoneHVAC Terminal Unit Object Type"] = None
        self._data["ZoneHVAC Terminal Unit Name"] = None
        self._data["Terminal Unit Outlet Node Name"] = None
        self._data["Terminal Unit Primary Air Inlet Node Name"] = None
        self._data["Terminal Unit Secondary Air Inlet Node Name"] = None
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
            self.zonehvac_terminal_unit_object_type = None
        else:
            self.zonehvac_terminal_unit_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zonehvac_terminal_unit_name = None
        else:
            self.zonehvac_terminal_unit_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terminal_unit_outlet_node_name = None
        else:
            self.terminal_unit_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terminal_unit_primary_air_inlet_node_name = None
        else:
            self.terminal_unit_primary_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terminal_unit_secondary_air_inlet_node_name = None
        else:
            self.terminal_unit_secondary_air_inlet_node_name = vals[i]
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
                                 ' for field `AirTerminalSingleDuctInletSideMixer.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctInletSideMixer.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctInletSideMixer.name`')
        self._data["Name"] = value

    @property
    def zonehvac_terminal_unit_object_type(self):
        """Get zonehvac_terminal_unit_object_type

        Returns:
            str: the value of `zonehvac_terminal_unit_object_type` or None if not set
        """
        return self._data["ZoneHVAC Terminal Unit Object Type"]

    @zonehvac_terminal_unit_object_type.setter
    def zonehvac_terminal_unit_object_type(self, value=None):
        """  Corresponds to IDD Field `ZoneHVAC Terminal Unit Object Type`

        Args:
            value (str): value for IDD Field `ZoneHVAC Terminal Unit Object Type`
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
                                 ' for field `AirTerminalSingleDuctInletSideMixer.zonehvac_terminal_unit_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctInletSideMixer.zonehvac_terminal_unit_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctInletSideMixer.zonehvac_terminal_unit_object_type`')
        self._data["ZoneHVAC Terminal Unit Object Type"] = value

    @property
    def zonehvac_terminal_unit_name(self):
        """Get zonehvac_terminal_unit_name

        Returns:
            str: the value of `zonehvac_terminal_unit_name` or None if not set
        """
        return self._data["ZoneHVAC Terminal Unit Name"]

    @zonehvac_terminal_unit_name.setter
    def zonehvac_terminal_unit_name(self, value=None):
        """  Corresponds to IDD Field `ZoneHVAC Terminal Unit Name`

        Args:
            value (str): value for IDD Field `ZoneHVAC Terminal Unit Name`
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
                                 ' for field `AirTerminalSingleDuctInletSideMixer.zonehvac_terminal_unit_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctInletSideMixer.zonehvac_terminal_unit_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctInletSideMixer.zonehvac_terminal_unit_name`')
        self._data["ZoneHVAC Terminal Unit Name"] = value

    @property
    def terminal_unit_outlet_node_name(self):
        """Get terminal_unit_outlet_node_name

        Returns:
            str: the value of `terminal_unit_outlet_node_name` or None if not set
        """
        return self._data["Terminal Unit Outlet Node Name"]

    @terminal_unit_outlet_node_name.setter
    def terminal_unit_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Outlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctInletSideMixer.terminal_unit_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctInletSideMixer.terminal_unit_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctInletSideMixer.terminal_unit_outlet_node_name`')
        self._data["Terminal Unit Outlet Node Name"] = value

    @property
    def terminal_unit_primary_air_inlet_node_name(self):
        """Get terminal_unit_primary_air_inlet_node_name

        Returns:
            str: the value of `terminal_unit_primary_air_inlet_node_name` or None if not set
        """
        return self._data["Terminal Unit Primary Air Inlet Node Name"]

    @terminal_unit_primary_air_inlet_node_name.setter
    def terminal_unit_primary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Primary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Primary Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctInletSideMixer.terminal_unit_primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctInletSideMixer.terminal_unit_primary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctInletSideMixer.terminal_unit_primary_air_inlet_node_name`')
        self._data["Terminal Unit Primary Air Inlet Node Name"] = value

    @property
    def terminal_unit_secondary_air_inlet_node_name(self):
        """Get terminal_unit_secondary_air_inlet_node_name

        Returns:
            str: the value of `terminal_unit_secondary_air_inlet_node_name` or None if not set
        """
        return self._data["Terminal Unit Secondary Air Inlet Node Name"]

    @terminal_unit_secondary_air_inlet_node_name.setter
    def terminal_unit_secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Secondary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Secondary Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctInletSideMixer.terminal_unit_secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctInletSideMixer.terminal_unit_secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctInletSideMixer.terminal_unit_secondary_air_inlet_node_name`')
        self._data["Terminal Unit Secondary Air Inlet Node Name"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctInletSideMixer:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctInletSideMixer:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctInletSideMixer: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctInletSideMixer: {} / {}".format(out_fields,
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

class AirTerminalSingleDuctSupplySideMixer(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:SupplySideMixer`
        Mix 2 inlet air streams into one outlet stream.
    """
    internal_name = "AirTerminal:SingleDuct:SupplySideMixer"
    field_count = 6
    required_fields = ["Name", "ZoneHVAC Terminal Unit Object Type", "ZoneHVAC Terminal Unit Name", "Terminal Unit Outlet Node Name", "Terminal Unit Primary Air Inlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:SupplySideMixer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["ZoneHVAC Terminal Unit Object Type"] = None
        self._data["ZoneHVAC Terminal Unit Name"] = None
        self._data["Terminal Unit Outlet Node Name"] = None
        self._data["Terminal Unit Primary Air Inlet Node Name"] = None
        self._data["Terminal Unit Secondary Air Inlet Node Name"] = None
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
            self.zonehvac_terminal_unit_object_type = None
        else:
            self.zonehvac_terminal_unit_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zonehvac_terminal_unit_name = None
        else:
            self.zonehvac_terminal_unit_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terminal_unit_outlet_node_name = None
        else:
            self.terminal_unit_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terminal_unit_primary_air_inlet_node_name = None
        else:
            self.terminal_unit_primary_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terminal_unit_secondary_air_inlet_node_name = None
        else:
            self.terminal_unit_secondary_air_inlet_node_name = vals[i]
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
                                 ' for field `AirTerminalSingleDuctSupplySideMixer.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.name`')
        self._data["Name"] = value

    @property
    def zonehvac_terminal_unit_object_type(self):
        """Get zonehvac_terminal_unit_object_type

        Returns:
            str: the value of `zonehvac_terminal_unit_object_type` or None if not set
        """
        return self._data["ZoneHVAC Terminal Unit Object Type"]

    @zonehvac_terminal_unit_object_type.setter
    def zonehvac_terminal_unit_object_type(self, value=None):
        """  Corresponds to IDD Field `ZoneHVAC Terminal Unit Object Type`

        Args:
            value (str): value for IDD Field `ZoneHVAC Terminal Unit Object Type`
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
                                 ' for field `AirTerminalSingleDuctSupplySideMixer.zonehvac_terminal_unit_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.zonehvac_terminal_unit_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.zonehvac_terminal_unit_object_type`')
        self._data["ZoneHVAC Terminal Unit Object Type"] = value

    @property
    def zonehvac_terminal_unit_name(self):
        """Get zonehvac_terminal_unit_name

        Returns:
            str: the value of `zonehvac_terminal_unit_name` or None if not set
        """
        return self._data["ZoneHVAC Terminal Unit Name"]

    @zonehvac_terminal_unit_name.setter
    def zonehvac_terminal_unit_name(self, value=None):
        """  Corresponds to IDD Field `ZoneHVAC Terminal Unit Name`

        Args:
            value (str): value for IDD Field `ZoneHVAC Terminal Unit Name`
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
                                 ' for field `AirTerminalSingleDuctSupplySideMixer.zonehvac_terminal_unit_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.zonehvac_terminal_unit_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.zonehvac_terminal_unit_name`')
        self._data["ZoneHVAC Terminal Unit Name"] = value

    @property
    def terminal_unit_outlet_node_name(self):
        """Get terminal_unit_outlet_node_name

        Returns:
            str: the value of `terminal_unit_outlet_node_name` or None if not set
        """
        return self._data["Terminal Unit Outlet Node Name"]

    @terminal_unit_outlet_node_name.setter
    def terminal_unit_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Outlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Outlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctSupplySideMixer.terminal_unit_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.terminal_unit_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.terminal_unit_outlet_node_name`')
        self._data["Terminal Unit Outlet Node Name"] = value

    @property
    def terminal_unit_primary_air_inlet_node_name(self):
        """Get terminal_unit_primary_air_inlet_node_name

        Returns:
            str: the value of `terminal_unit_primary_air_inlet_node_name` or None if not set
        """
        return self._data["Terminal Unit Primary Air Inlet Node Name"]

    @terminal_unit_primary_air_inlet_node_name.setter
    def terminal_unit_primary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Primary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Primary Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctSupplySideMixer.terminal_unit_primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.terminal_unit_primary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.terminal_unit_primary_air_inlet_node_name`')
        self._data["Terminal Unit Primary Air Inlet Node Name"] = value

    @property
    def terminal_unit_secondary_air_inlet_node_name(self):
        """Get terminal_unit_secondary_air_inlet_node_name

        Returns:
            str: the value of `terminal_unit_secondary_air_inlet_node_name` or None if not set
        """
        return self._data["Terminal Unit Secondary Air Inlet Node Name"]

    @terminal_unit_secondary_air_inlet_node_name.setter
    def terminal_unit_secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Terminal Unit Secondary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Secondary Air Inlet Node Name`
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
                                 ' for field `AirTerminalSingleDuctSupplySideMixer.terminal_unit_secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.terminal_unit_secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalSingleDuctSupplySideMixer.terminal_unit_secondary_air_inlet_node_name`')
        self._data["Terminal Unit Secondary Air Inlet Node Name"] = value

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
                    raise ValueError("Required field AirTerminalSingleDuctSupplySideMixer:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalSingleDuctSupplySideMixer:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalSingleDuctSupplySideMixer: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalSingleDuctSupplySideMixer: {} / {}".format(out_fields,
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

class AirTerminalDualDuctConstantVolume(object):
    """ Corresponds to IDD object `AirTerminal:DualDuct:ConstantVolume`
        Central air system terminal unit, dual duct, constant volume.
    """
    internal_name = "AirTerminal:DualDuct:ConstantVolume"
    field_count = 6
    required_fields = ["Name", "Air Outlet Node Name", "Hot Air Inlet Node Name", "Cold Air Inlet Node Name", "Maximum Air Flow Rate"]
    extensible_fields = 0
    format = None
    min_fields = 6
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:DualDuct:ConstantVolume`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Hot Air Inlet Node Name"] = None
        self._data["Cold Air Inlet Node Name"] = None
        self._data["Maximum Air Flow Rate"] = None
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
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_air_inlet_node_name = None
        else:
            self.hot_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cold_air_inlet_node_name = None
        else:
            self.cold_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
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
                                 ' for field `AirTerminalDualDuctConstantVolume.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctConstantVolume.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctConstantVolume.name`')
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
                                 ' for field `AirTerminalDualDuctConstantVolume.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctConstantVolume.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctConstantVolume.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`
        The outlet node of the terminal unit.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `AirTerminalDualDuctConstantVolume.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctConstantVolume.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctConstantVolume.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def hot_air_inlet_node_name(self):
        """Get hot_air_inlet_node_name

        Returns:
            str: the value of `hot_air_inlet_node_name` or None if not set
        """
        return self._data["Hot Air Inlet Node Name"]

    @hot_air_inlet_node_name.setter
    def hot_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Hot Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Hot Air Inlet Node Name`
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
                                 ' for field `AirTerminalDualDuctConstantVolume.hot_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctConstantVolume.hot_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctConstantVolume.hot_air_inlet_node_name`')
        self._data["Hot Air Inlet Node Name"] = value

    @property
    def cold_air_inlet_node_name(self):
        """Get cold_air_inlet_node_name

        Returns:
            str: the value of `cold_air_inlet_node_name` or None if not set
        """
        return self._data["Cold Air Inlet Node Name"]

    @cold_air_inlet_node_name.setter
    def cold_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Cold Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Cold Air Inlet Node Name`
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
                                 ' for field `AirTerminalDualDuctConstantVolume.cold_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctConstantVolume.cold_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctConstantVolume.cold_air_inlet_node_name`')
        self._data["Cold Air Inlet Node Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalDualDuctConstantVolume.maximum_air_flow_rate`'.format(value))
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalDualDuctConstantVolume.maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalDualDuctConstantVolume.maximum_air_flow_rate`')
        self._data["Maximum Air Flow Rate"] = value

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
                    raise ValueError("Required field AirTerminalDualDuctConstantVolume:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalDualDuctConstantVolume:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalDualDuctConstantVolume: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalDualDuctConstantVolume: {} / {}".format(out_fields,
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

class AirTerminalDualDuctVav(object):
    """ Corresponds to IDD object `AirTerminal:DualDuct:VAV`
        Central air system terminal unit, dual duct, variable volume.
    """
    internal_name = "AirTerminal:DualDuct:VAV"
    field_count = 8
    required_fields = ["Name", "Air Outlet Node Name", "Hot Air Inlet Node Name", "Cold Air Inlet Node Name", "Maximum Damper Air Flow Rate", "Zone Minimum Air Flow Fraction"]
    extensible_fields = 0
    format = None
    min_fields = 7
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:DualDuct:VAV`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Hot Air Inlet Node Name"] = None
        self._data["Cold Air Inlet Node Name"] = None
        self._data["Maximum Damper Air Flow Rate"] = None
        self._data["Zone Minimum Air Flow Fraction"] = None
        self._data["Design Specification Outdoor Air Object Name"] = None
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
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_air_inlet_node_name = None
        else:
            self.hot_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cold_air_inlet_node_name = None
        else:
            self.cold_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_damper_air_flow_rate = None
        else:
            self.maximum_damper_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_minimum_air_flow_fraction = None
        else:
            self.zone_minimum_air_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name = None
        else:
            self.design_specification_outdoor_air_object_name = vals[i]
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
                                 ' for field `AirTerminalDualDuctVav.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVav.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVav.name`')
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
                                 ' for field `AirTerminalDualDuctVav.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVav.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVav.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`
        The outlet node of the terminal unit.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `AirTerminalDualDuctVav.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVav.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVav.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def hot_air_inlet_node_name(self):
        """Get hot_air_inlet_node_name

        Returns:
            str: the value of `hot_air_inlet_node_name` or None if not set
        """
        return self._data["Hot Air Inlet Node Name"]

    @hot_air_inlet_node_name.setter
    def hot_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Hot Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Hot Air Inlet Node Name`
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
                                 ' for field `AirTerminalDualDuctVav.hot_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVav.hot_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVav.hot_air_inlet_node_name`')
        self._data["Hot Air Inlet Node Name"] = value

    @property
    def cold_air_inlet_node_name(self):
        """Get cold_air_inlet_node_name

        Returns:
            str: the value of `cold_air_inlet_node_name` or None if not set
        """
        return self._data["Cold Air Inlet Node Name"]

    @cold_air_inlet_node_name.setter
    def cold_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Cold Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Cold Air Inlet Node Name`
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
                                 ' for field `AirTerminalDualDuctVav.cold_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVav.cold_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVav.cold_air_inlet_node_name`')
        self._data["Cold Air Inlet Node Name"] = value

    @property
    def maximum_damper_air_flow_rate(self):
        """Get maximum_damper_air_flow_rate

        Returns:
            float: the value of `maximum_damper_air_flow_rate` or None if not set
        """
        return self._data["Maximum Damper Air Flow Rate"]

    @maximum_damper_air_flow_rate.setter
    def maximum_damper_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Damper Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Damper Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Damper Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalDualDuctVav.maximum_damper_air_flow_rate`'.format(value))
                    self._data["Maximum Damper Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalDualDuctVav.maximum_damper_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalDualDuctVav.maximum_damper_air_flow_rate`')
        self._data["Maximum Damper Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_fraction(self):
        """Get zone_minimum_air_flow_fraction

        Returns:
            float: the value of `zone_minimum_air_flow_fraction` or None if not set
        """
        return self._data["Zone Minimum Air Flow Fraction"]

    @zone_minimum_air_flow_fraction.setter
    def zone_minimum_air_flow_fraction(self, value=0.2):
        """  Corresponds to IDD Field `Zone Minimum Air Flow Fraction`
        fraction of maximum air flow

        Args:
            value (float): value for IDD Field `Zone Minimum Air Flow Fraction`
                Default value: 0.2
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
                                 ' for field `AirTerminalDualDuctVav.zone_minimum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalDualDuctVav.zone_minimum_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `AirTerminalDualDuctVav.zone_minimum_air_flow_fraction`')
        self._data["Zone Minimum Air Flow Fraction"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """Get design_specification_outdoor_air_object_name

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification Outdoor Air Object Name`
        When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        unit will increase flow as needed to meet this outdoor air requirement.
        If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        be computed based on the current number of occupants in the zone.
        At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.
        If this field is blank, then the terminal unit will not be controlled for outdoor air flow.

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`
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
                                 ' for field `AirTerminalDualDuctVav.design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVav.design_specification_outdoor_air_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVav.design_specification_outdoor_air_object_name`')
        self._data["Design Specification Outdoor Air Object Name"] = value

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
                    raise ValueError("Required field AirTerminalDualDuctVav:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalDualDuctVav:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalDualDuctVav: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalDualDuctVav: {} / {}".format(out_fields,
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

class AirTerminalDualDuctVavOutdoorAir(object):
    """ Corresponds to IDD object `AirTerminal:DualDuct:VAV:OutdoorAir`
        Central air system terminal unit, dual duct, variable volume with special controls.
        One VAV duct is controlled to supply ventilation air and the other VAV duct is
        controlled to meet the zone cooling load.
    """
    internal_name = "AirTerminal:DualDuct:VAV:OutdoorAir"
    field_count = 8
    required_fields = ["Name", "Air Outlet Node Name", "Outdoor Air Inlet Node Name", "Maximum Terminal Air Flow Rate", "Design Specification Outdoor Air Object Name"]
    extensible_fields = 0
    format = None
    min_fields = 7
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:DualDuct:VAV:OutdoorAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Outdoor Air Inlet Node Name"] = None
        self._data["Recirculated Air Inlet Node Name"] = None
        self._data["Maximum Terminal Air Flow Rate"] = None
        self._data["Design Specification Outdoor Air Object Name"] = None
        self._data["Per Person Ventilation Rate Mode"] = None
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
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_inlet_node_name = None
        else:
            self.outdoor_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.recirculated_air_inlet_node_name = None
        else:
            self.recirculated_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_terminal_air_flow_rate = None
        else:
            self.maximum_terminal_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name = None
        else:
            self.design_specification_outdoor_air_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.per_person_ventilation_rate_mode = None
        else:
            self.per_person_ventilation_rate_mode = vals[i]
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
                                 ' for field `AirTerminalDualDuctVavOutdoorAir.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.name`')
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
                                 ' for field `AirTerminalDualDuctVavOutdoorAir.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`
        The outlet node of the terminal unit.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `AirTerminalDualDuctVavOutdoorAir.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """Get outdoor_air_inlet_node_name

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`
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
                                 ' for field `AirTerminalDualDuctVavOutdoorAir.outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.outdoor_air_inlet_node_name`')
        self._data["Outdoor Air Inlet Node Name"] = value

    @property
    def recirculated_air_inlet_node_name(self):
        """Get recirculated_air_inlet_node_name

        Returns:
            str: the value of `recirculated_air_inlet_node_name` or None if not set
        """
        return self._data["Recirculated Air Inlet Node Name"]

    @recirculated_air_inlet_node_name.setter
    def recirculated_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Recirculated Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Recirculated Air Inlet Node Name`
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
                                 ' for field `AirTerminalDualDuctVavOutdoorAir.recirculated_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.recirculated_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.recirculated_air_inlet_node_name`')
        self._data["Recirculated Air Inlet Node Name"] = value

    @property
    def maximum_terminal_air_flow_rate(self):
        """Get maximum_terminal_air_flow_rate

        Returns:
            float: the value of `maximum_terminal_air_flow_rate` or None if not set
        """
        return self._data["Maximum Terminal Air Flow Rate"]

    @maximum_terminal_air_flow_rate.setter
    def maximum_terminal_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Terminal Air Flow Rate`
        If autosized this is the sum of flow needed for cooling and maximum required outdoor air

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Terminal Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Terminal Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.maximum_terminal_air_flow_rate`'.format(value))
                    self._data["Maximum Terminal Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirTerminalDualDuctVavOutdoorAir.maximum_terminal_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.maximum_terminal_air_flow_rate`')
        self._data["Maximum Terminal Air Flow Rate"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """Get design_specification_outdoor_air_object_name

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification Outdoor Air Object Name`
        When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        unit will increase flow as needed to meet this outdoor air requirement.
        If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        be computed based mode selected in the next field.
        At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`
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
                                 ' for field `AirTerminalDualDuctVavOutdoorAir.design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.design_specification_outdoor_air_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.design_specification_outdoor_air_object_name`')
        self._data["Design Specification Outdoor Air Object Name"] = value

    @property
    def per_person_ventilation_rate_mode(self):
        """Get per_person_ventilation_rate_mode

        Returns:
            str: the value of `per_person_ventilation_rate_mode` or None if not set
        """
        return self._data["Per Person Ventilation Rate Mode"]

    @per_person_ventilation_rate_mode.setter
    def per_person_ventilation_rate_mode(self, value=None):
        """  Corresponds to IDD Field `Per Person Ventilation Rate Mode`
        CurrentOccupancy models demand controlled ventilation using the current number of people
        DesignOccupancy uses the total Number of People in the zone and is constant

        Args:
            value (str): value for IDD Field `Per Person Ventilation Rate Mode`
                Accepted values are:
                      - CurrentOccupancy
                      - DesignOccupancy
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
                                 ' for field `AirTerminalDualDuctVavOutdoorAir.per_person_ventilation_rate_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.per_person_ventilation_rate_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirTerminalDualDuctVavOutdoorAir.per_person_ventilation_rate_mode`')
            vals = {}
            vals["currentoccupancy"] = "CurrentOccupancy"
            vals["designoccupancy"] = "DesignOccupancy"
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
                                     'field `AirTerminalDualDuctVavOutdoorAir.per_person_ventilation_rate_mode`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirTerminalDualDuctVavOutdoorAir.per_person_ventilation_rate_mode`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Per Person Ventilation Rate Mode"] = value

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
                    raise ValueError("Required field AirTerminalDualDuctVavOutdoorAir:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirTerminalDualDuctVavOutdoorAir:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirTerminalDualDuctVavOutdoorAir: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirTerminalDualDuctVavOutdoorAir: {} / {}".format(out_fields,
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

class ZoneHvacAirDistributionUnit(object):
    """ Corresponds to IDD object `ZoneHVAC:AirDistributionUnit`
        Central air system air distribution unit, serves as a wrapper for a specific type of
        air terminal unit. This object is referenced in a ZoneHVAC:EquipmentList.
    """
    internal_name = "ZoneHVAC:AirDistributionUnit"
    field_count = 6
    required_fields = ["Name", "Air Distribution Unit Outlet Node Name", "Air Terminal Object Type", "Air Terminal Name"]
    extensible_fields = 0
    format = None
    min_fields = 4
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:AirDistributionUnit`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Air Distribution Unit Outlet Node Name"] = None
        self._data["Air Terminal Object Type"] = None
        self._data["Air Terminal Name"] = None
        self._data["Nominal Upstream Leakage Fraction"] = None
        self._data["Constant Downstream Leakage Fraction"] = None
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
            self.air_distribution_unit_outlet_node_name = None
        else:
            self.air_distribution_unit_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_terminal_object_type = None
        else:
            self.air_terminal_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_terminal_name = None
        else:
            self.air_terminal_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_upstream_leakage_fraction = None
        else:
            self.nominal_upstream_leakage_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.constant_downstream_leakage_fraction = None
        else:
            self.constant_downstream_leakage_fraction = vals[i]
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
                                 ' for field `ZoneHvacAirDistributionUnit.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacAirDistributionUnit.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacAirDistributionUnit.name`')
        self._data["Name"] = value

    @property
    def air_distribution_unit_outlet_node_name(self):
        """Get air_distribution_unit_outlet_node_name

        Returns:
            str: the value of `air_distribution_unit_outlet_node_name` or None if not set
        """
        return self._data["Air Distribution Unit Outlet Node Name"]

    @air_distribution_unit_outlet_node_name.setter
    def air_distribution_unit_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Distribution Unit Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Distribution Unit Outlet Node Name`
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
                                 ' for field `ZoneHvacAirDistributionUnit.air_distribution_unit_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacAirDistributionUnit.air_distribution_unit_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacAirDistributionUnit.air_distribution_unit_outlet_node_name`')
        self._data["Air Distribution Unit Outlet Node Name"] = value

    @property
    def air_terminal_object_type(self):
        """Get air_terminal_object_type

        Returns:
            str: the value of `air_terminal_object_type` or None if not set
        """
        return self._data["Air Terminal Object Type"]

    @air_terminal_object_type.setter
    def air_terminal_object_type(self, value=None):
        """  Corresponds to IDD Field `Air Terminal Object Type`

        Args:
            value (str): value for IDD Field `Air Terminal Object Type`
                Accepted values are:
                      - AirTerminal:DualDuct:ConstantVolume
                      - AirTerminal:DualDuct:VAV
                      - AirTerminal:SingleDuct:ConstantVolume:Reheat
                      - AirTerminal:SingleDuct:VAV:Reheat
                      - AirTerminal:SingleDuct:VAV:NoReheat
                      - AirTerminal:SingleDuct:SeriesPIU:Reheat
                      - AirTerminal:SingleDuct:ParallelPIU:Reheat
                      - AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction
                      - AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan
                      - AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat
                      - AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat
                      - AirTerminal:SingleDuct:ConstantVolume:CooledBeam
                      - AirTerminal:DualDuct:VAV:OutdoorAir
                      - AirTerminal:SingleDuct:UserDefined
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
                                 ' for field `ZoneHvacAirDistributionUnit.air_terminal_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacAirDistributionUnit.air_terminal_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacAirDistributionUnit.air_terminal_object_type`')
            vals = {}
            vals["airterminal:dualduct:constantvolume"] = "AirTerminal:DualDuct:ConstantVolume"
            vals["airterminal:dualduct:vav"] = "AirTerminal:DualDuct:VAV"
            vals["airterminal:singleduct:constantvolume:reheat"] = "AirTerminal:SingleDuct:ConstantVolume:Reheat"
            vals["airterminal:singleduct:vav:reheat"] = "AirTerminal:SingleDuct:VAV:Reheat"
            vals["airterminal:singleduct:vav:noreheat"] = "AirTerminal:SingleDuct:VAV:NoReheat"
            vals["airterminal:singleduct:seriespiu:reheat"] = "AirTerminal:SingleDuct:SeriesPIU:Reheat"
            vals["airterminal:singleduct:parallelpiu:reheat"] = "AirTerminal:SingleDuct:ParallelPIU:Reheat"
            vals["airterminal:singleduct:constantvolume:fourpipeinduction"] = "AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction"
            vals["airterminal:singleduct:vav:reheat:variablespeedfan"] = "AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan"
            vals["airterminal:singleduct:vav:heatandcool:reheat"] = "AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat"
            vals["airterminal:singleduct:vav:heatandcool:noreheat"] = "AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat"
            vals["airterminal:singleduct:constantvolume:cooledbeam"] = "AirTerminal:SingleDuct:ConstantVolume:CooledBeam"
            vals["airterminal:dualduct:vav:outdoorair"] = "AirTerminal:DualDuct:VAV:OutdoorAir"
            vals["airterminal:singleduct:userdefined"] = "AirTerminal:SingleDuct:UserDefined"
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
                                     'field `ZoneHvacAirDistributionUnit.air_terminal_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacAirDistributionUnit.air_terminal_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Air Terminal Object Type"] = value

    @property
    def air_terminal_name(self):
        """Get air_terminal_name

        Returns:
            str: the value of `air_terminal_name` or None if not set
        """
        return self._data["Air Terminal Name"]

    @air_terminal_name.setter
    def air_terminal_name(self, value=None):
        """  Corresponds to IDD Field `Air Terminal Name`

        Args:
            value (str): value for IDD Field `Air Terminal Name`
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
                                 ' for field `ZoneHvacAirDistributionUnit.air_terminal_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacAirDistributionUnit.air_terminal_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacAirDistributionUnit.air_terminal_name`')
        self._data["Air Terminal Name"] = value

    @property
    def nominal_upstream_leakage_fraction(self):
        """Get nominal_upstream_leakage_fraction

        Returns:
            float: the value of `nominal_upstream_leakage_fraction` or None if not set
        """
        return self._data["Nominal Upstream Leakage Fraction"]

    @nominal_upstream_leakage_fraction.setter
    def nominal_upstream_leakage_fraction(self, value=0.0):
        """  Corresponds to IDD Field `Nominal Upstream Leakage Fraction`
        fraction at system design Flow; leakage Flow constant, leakage fraction
        varies with variable system Flow Rate.

        Args:
            value (float): value for IDD Field `Nominal Upstream Leakage Fraction`
                Default value: 0.0
                value >= 0.0
                value <= 0.3
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
                                 ' for field `ZoneHvacAirDistributionUnit.nominal_upstream_leakage_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacAirDistributionUnit.nominal_upstream_leakage_fraction`')
            if value > 0.3:
                raise ValueError('value need to be smaller 0.3 '
                                 'for field `ZoneHvacAirDistributionUnit.nominal_upstream_leakage_fraction`')
        self._data["Nominal Upstream Leakage Fraction"] = value

    @property
    def constant_downstream_leakage_fraction(self):
        """Get constant_downstream_leakage_fraction

        Returns:
            float: the value of `constant_downstream_leakage_fraction` or None if not set
        """
        return self._data["Constant Downstream Leakage Fraction"]

    @constant_downstream_leakage_fraction.setter
    def constant_downstream_leakage_fraction(self, value=0.0):
        """  Corresponds to IDD Field `Constant Downstream Leakage Fraction`

        Args:
            value (float): value for IDD Field `Constant Downstream Leakage Fraction`
                Default value: 0.0
                value >= 0.0
                value <= 0.3
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
                                 ' for field `ZoneHvacAirDistributionUnit.constant_downstream_leakage_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacAirDistributionUnit.constant_downstream_leakage_fraction`')
            if value > 0.3:
                raise ValueError('value need to be smaller 0.3 '
                                 'for field `ZoneHvacAirDistributionUnit.constant_downstream_leakage_fraction`')
        self._data["Constant Downstream Leakage Fraction"] = value

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
                    raise ValueError("Required field ZoneHvacAirDistributionUnit:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacAirDistributionUnit:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacAirDistributionUnit: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacAirDistributionUnit: {} / {}".format(out_fields,
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